# LLM Project: AI Agent, MCP Server & Next.js Interface

This repository provides a modular, extensible platform for building, orchestrating, and interacting with LLM-powered agents and tools. It is designed for research, prototyping, and production use cases involving multi-agent systems, tool integration, and advanced workflow management.

- **agent/**: Python backend AI agent (JSON-RPC server)
- **mcp_server/**: Python MCP (Multi-Component Platform) server for additional backend services
- **ai-agent-nextjs/**: Next.js frontend demo for user interaction

---

## Key Concepts & Technologies

### MCP (Model Context Protocol)
MCP is a protocol and server (see `mcp_server/`) that manages context, state, and communication between different components (such as the AI agent and external tools). It enables modular, extensible, and context-aware orchestration of LLMs and tools, making it easier to build complex, multi-step workflows. MCP can be extended to support new tools, agents, or data sources.

### A2A (Agent-to-Agent, Google A2A System)
A2A refers to Agent-to-Agent communication, inspired by Google's A2A system. In this project, A2A is a conceptual and architectural pattern that allows multiple agents (or services) to communicate, delegate tasks, and collaborate. This enables distributed intelligence, where specialized agents can handle different parts of a workflow or problem, and can be extended to support agent negotiation, coordination, and dynamic task assignment.

### Langraph
Langraph is a framework or library for building, visualizing, and managing LLM-powered workflows as graphs. It allows you to define nodes (steps, tools, agents) and edges (data flow, control flow) to create complex, interpretable pipelines for language model applications. Langraph can be used to design, debug, and optimize agent workflows, and is compatible with both MCP and A2A patterns.

---

## Project Structure

```
llm_project/
├── agent/                # Python AI agent backend
│   └── test.py           # Example server script
├── mcp_server/           # MCP server for additional backend services
│   └── mcp_server.py     # MCP server script
├── ai-agent-nextjs/      # Next.js frontend demo interface
│   ├── pages/
│   ├── ...
│   └── README.md
├── README.md             # (this file)
├── requirements.txt      # Python dependencies for agent and MCP
├── .env.example          # Example environment variables
└── ...
```

---

## Component Details

### agent/
- **Purpose:** Runs a JSON-RPC server that processes user messages, invokes LLMs or tools, and returns responses.
- **Extensibility:** Add new methods, integrate external APIs, or connect to the MCP server for advanced context management.
- **Entry Point:** `test.py`

### mcp_server/
- **Purpose:** Provides context management, state tracking, and additional APIs/services for agents and tools. Can be used for session management, logging, or orchestrating multi-agent workflows.
- **Extensibility:** Add new endpoints, context providers, or integrations with databases and external services.
- **Entry Point:** `mcp_server.py`

### ai-agent-nextjs/
- **Purpose:** Modern web UI for interacting with the agent. Proxies user messages to the backend and displays responses in a user-friendly format.
- **Extensibility:** Customize the UI, add authentication, or integrate with other frontend frameworks.
- **Entry Point:** `pages/index.tsx`

---

## How It Works
- The **Python agent** runs a server on `http://localhost:10000/` and processes JSON-RPC requests.
- The **MCP server** provides additional backend APIs/services that may be used by the agent or frontend.
- The **Next.js frontend** provides a modern UI and proxies user messages to the Python agent via an API route.
- The architecture is designed to support A2A (agent-to-agent) communication and can be extended with Langraph for workflow orchestration.

---

## Example Use Cases
- **Conversational AI:** Build chatbots or assistants that can use tools, access external data, and maintain context across sessions.
- **Multi-Agent Collaboration:** Implement workflows where multiple agents (e.g., planner, executor, retriever) communicate and solve tasks together.
- **Tool Augmentation:** Integrate APIs (search, database, code execution) as tools accessible to the agent via MCP.
- **Workflow Orchestration:** Use Langraph to design and visualize complex LLM-powered pipelines.

---

## Setup & Running

### 1. Environment Variables
- Copy `.env.example` to `.env` and fill in any required secrets or configuration.
- Each component may have its own environment variables (see their respective READMEs).

### 2. Install Python Dependencies
```bash
pip install -r requirements.txt
```

### 3. Start the MCP Server
```bash
cd mcp_server
python mcp_server.py
```

### 4. Start the Python AI Agent
```bash
cd agent
python test.py
```

### 5. Start the Next.js Frontend
```bash
cd ai-agent-nextjs
npm install
npm run dev
```

- Visit [http://localhost:3000](http://localhost:3000) to use the interface.
- All servers must be running for full functionality if your use case requires the MCP server.

---

## Advanced Customization
- **Add new tools or agents:** Extend the MCP server and agent to support new capabilities.
- **Integrate with Langraph:** Use Langraph to design, debug, and optimize agent workflows.
- **Production deployment:** Use Docker, cloud services, or orchestration tools to deploy at scale.
- **Security:** Add authentication, authorization, and rate limiting as needed.

---

## Troubleshooting
- **Port conflicts:** Make sure each server runs on a unique port.
- **CORS issues:** The Next.js API route proxies requests to avoid CORS problems.
- **Dependency errors:** Ensure all Python and Node.js dependencies are installed.
- **Environment variables:** Double-check your `.env` files for required settings.

---

## Contributing
1. Fork the repo and create a feature branch.
2. Make your changes with clear commit messages.
3. Add/modify tests if needed.
4. Open a pull request with a description of your changes.

---

**Enjoy building with your AI agent platform!** 