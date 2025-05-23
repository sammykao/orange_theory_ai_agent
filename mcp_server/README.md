# MCP Server

This folder contains the MCP (Multi-Component Platform) server for the project.

## Purpose
- Provides additional backend services or APIs that may be required by the AI agent or frontend.
- Typically runs as a separate Python server.

## How to Run

1. Make sure you have Python 3 installed.
2. Install any required dependencies (see `requirements.txt` in the project root).
3. Start the MCP server:

```bash
python mcp_server.py
```

- The server will listen on the port specified in `mcp_server.py` (check the file for details).
- You can modify `mcp_server.py` to change logic or port.

## How it Connects
- The MCP server may be called by the AI agent or frontend for specific tasks, data, or integrations.
- Check the codebase for where and how it is used.

---

**Edit `mcp_server.py` to customize the MCP server's behavior.** 