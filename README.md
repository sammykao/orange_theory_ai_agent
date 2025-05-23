# LLM Project: AI Agent, MCP Server & Next.js Interface

This repository contains a full-stack project for interacting with a local AI agent via a modern web interface. It consists of three main parts:

- **agent/**: Python backend AI agent (JSON-RPC server)
- **mcp_server/**: Python MCP (Multi-Component Platform) server for additional backend services
- **ai-agent-nextjs/**: Next.js frontend demo for user interaction

---

## Key Concepts & Technologies

### MCP (Model Context Protocol)
MCP stands for **Model Context Protocol**. In this project, MCP is a protocol and server (see `mcp_server/`) that manages context, state, and communication between different components (such as the AI agent and external tools). It enables modular, extensible, and context-aware orchestration of LLMs and tools, making it easier to build complex, multi-step workflows.

### A2A (Agent-to-Agent, Google A2A System)
A2A refers to **Agent-to-Agent** communication, inspired by Google's A2A system. In this project, A2A is a conceptual and architectural pattern that allows multiple agents (or services) to communicate, delegate tasks, and collaborate. This enables distributed intelligence, where specialized agents can handle different parts of a workflow or problem.

### Langraph
**Langraph** is a framework or library for building, visualizing, and managing LLM-powered workflows as graphs. It allows you to define nodes (steps, tools, agents) and edges (data flow, control flow) to create complex, interpretable pipelines for language model applications.

---

## Project Structure

```
llm_project/
├── agent/                # Python AI agent backend
│   └── test.py           # Example server script
├── mcp_server/           # MCP server for additional backend services
│   └── mcp_server.py     # MCP server script
├── ai-agent-nextjs/      # Next.js frontend interface
│   ├── pages/
│   ├── ...
│   └── README.md
├── README.md             # (this file)
└── ...
```

---

## How It Works
- The **Python agent** runs a server on `http://localhost:10000/` and processes JSON-RPC requests.
- The **MCP server** provides additional backend APIs/services that may be used by the agent or frontend.
- The **Next.js frontend** provides a modern UI and proxies user messages to the Python agent via an API route.
- The architecture is designed to support A2A (agent-to-agent) communication and can be extended with Langraph for workflow orchestration.

---

## Setup & Running

### 1. Start the MCP Server
```bash
cd mcp_server
python mcp_server.py
```

### 2. Start the Python AI Agent
```bash
cd agent
python test.py
```

### 3. Start the Next.js Frontend
```bash
cd ai-agent-nextjs
npm install
npm run dev
```

- Visit [http://localhost:3000](http://localhost:3000) to use the interface.
- All servers must be running for full functionality if your use case requires the MCP server.

---

## Customization
- Edit `agent/test.py` for backend logic.
- Edit `mcp_server/mcp_server.py` for MCP server logic.
- Edit `ai-agent-nextjs/pages/index.tsx` for UI changes.

---

**Enjoy building with your AI agent platform!** 