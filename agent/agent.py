import logging

from collections.abc import AsyncIterable
from typing import Any, Literal

import httpx

from langchain_core.messages import AIMessage, ToolMessage
from langchain_core.runnables.config import (
    RunnableConfig,
)
from langchain_core.tools import tool  # type: ignore
from langchain_openai import ChatOpenAI
from langgraph.checkpoint.memory import MemorySaver
from langgraph.prebuilt import create_react_agent  # type: ignore
from pydantic import BaseModel
from langchain_mcp_adapters.client import MultiServerMCPClient
import os
from mcp import ClientSession
from mcp.client.stdio import stdio_client
from langchain_mcp_adapters.tools import load_mcp_tools
from dotenv import load_dotenv

load_dotenv() 

ChatOpenAI.api_key = os.getenv("OPENAI_API_KEY")

logger = logging.getLogger(__name__)

memory = MemorySaver()




class ResponseFormat(BaseModel):
    """Respond to the user in this format."""

    status: Literal['input_required', 'completed', 'error'] = 'input_required'
    message: str


class OrangeTheoryAgent:
    """Orange Theory Agent."""

    SYSTEM_INSTRUCTION = (
        'You are an expert assistant for Orange Theory Fitness (OTF) members. '
        'Your purpose is to help users with their OTF account, bookings, class management, stats, studio search, and related tasks using the available tools. '
        'If you need a value (like a studio UUID, a booking Id, or a date) you do not have, use a tool to look it up first. Use the result in your next tool call. Do not guess or use placeholders.'
        'It is very important that you think carefully. Think step by step and reason through the problem before using a tool.'
        'If the user asks about anything outside of Orange Theory Fitness, politely state that you can only assist with OTF-related queries.'
    )

    RESPONSE_FORMAT_INSTRUCTION: str = (
        'Select status as completed if the request is complete. '
        'Select status as input_required if the input is a question to the user. '
        'Set response status to error if the input indicates an error.'
    )

    SUPPORTED_CONTENT_TYPES = ['text', 'text/plain']

    def __init__(self):
        self.model = ChatOpenAI(model="gpt-4.1-mini", temperature=0.8)
        self.graph = None

    async def invoke(self, query: str, sessionId: str) -> dict[str, Any]:
        client = MultiServerMCPClient(
            {
                "OrangeTheory": {
                    "url": "http://localhost:8000/sse",
                    "transport": "sse",
                }
            }
        )
        tools = await client.get_tools()
        for i, tool in enumerate(tools):
            print(f"Tool {i}: {tool.name}")
            print(f"Input schema: {getattr(tool, 'input_schema', None)}")
        self.graph = create_react_agent(
            self.model,
            tools=tools,
            checkpointer=memory,
            prompt=self.SYSTEM_INSTRUCTION,
            response_format=(self.RESPONSE_FORMAT_INSTRUCTION, ResponseFormat),
            debug=True
        )
        config: RunnableConfig = {'configurable': {'thread_id': sessionId}}
        await self.graph.ainvoke({'messages': [('user', query)]}, config)
        return self.get_agent_response(config)

    async def stream(
        self, query: str, sessionId: str
    ) -> AsyncIterable[dict[str, Any]]:
        pass

    def get_agent_response(self, config: RunnableConfig) -> dict[str, Any]:
        current_state = self.graph.get_state(config)

        structured_response = current_state.values.get('structured_response')
        if structured_response and isinstance(
            structured_response, ResponseFormat
        ):
            if structured_response.status in {'input_required', 'error'}:
                return {
                    'is_task_complete': False,
                    'require_user_input': True,
                    'content': structured_response.message,
                }
            if structured_response.status == 'completed':
                return {
                    'is_task_complete': True,
                    'require_user_input': False,
                    'content': structured_response.message,
                }

        return {
            'is_task_complete': False,
            'require_user_input': True,
            'content': 'We are unable to process your request at the moment. Please try again.',
        }