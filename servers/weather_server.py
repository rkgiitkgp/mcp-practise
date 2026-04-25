from typing import List

from mcp.server.fastmcp import FastMCP

mcp = FastMCP("weather-server")

@mcp.tool()
async def get_weather(location: str) -> str:
    """
    This function gets the current weather for a location.
    """
    return f"The current weather in {location} is sunny."

if __name__ == "__main__":
    mcp.run(transport="sse",port=8000)