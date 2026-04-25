# MCP Practice

This repository contains practice examples for building and consuming Model Context Protocol (MCP) servers using Python, FastMCP, and LangChain.

## Project Structure

The project includes two MCP servers with different transport mechanisms, and a LangChain-based client that can interact with them.

### Servers (`servers/`)

*   **`math_server.py`**: A FastMCP server running over **STDIO** transport. It exposes basic mathematical tools:
    *   `add(a, b)`: Adds two numbers.
    *   `multiply(a, b)`: Multiplies two numbers.
*   **`weather_server.py`**: A FastMCP server running over **SSE** (Server-Sent Events) transport on port 8000. It exposes a tool to get the current weather:
    *   `get_weather(location)`: Returns a mock weather string for a given location.

### Clients

*   **`main.py`**: A LangChain-based client that demonstrates connecting to the `math_server` over STDIO. It creates a LangChain agent using the `gpt-4o-mini` model, loads the tools from the MCP server, and asks the agent to solve a math problem (`"What is 54 + 2 * 3 ?"`).
*   **`langchain-client.py`**: A stub script for a `MultiServerMCPClient` implementation.

## Setup & Dependencies

This project uses `uv` for dependency management. Dependencies include `langchain`, `langchain-mcp-adapters`, `langchain-openai`, `langgraph`, and `python-dotenv`.

1.  **Install dependencies** using `uv`:
    ```bash
    uv sync
    ```

2.  **Environment Variables**: Create a `.env` file in the root directory and add your OpenAI API key (required by the LangChain clients):
    ```env
    OPENAI_API_KEY=your_api_key_here
    ```

## Usage

### Running the Math Client

You can run the `main.py` client which automatically spawns the `math_server` via the `uv run` command over STDIO, initializes the session, and triggers an agent workflow.

```bash
uv run main.py
```
*(Or simply `python main.py` if your environment is activated)*

### Running the Weather Server

To run the SSE-based weather server independently:


```bash
uv run servers/weather_server.py
```
This will start the FastMCP weather server listening on `http://localhost:8000`.
