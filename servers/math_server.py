
from mcp.server.fastmcp import FastMCP

mcp = FastMCP("math-server")

@mcp.tool()
def add(a: int, b: int) -> int:
    """
    This function adds two numbers.
    """
    return a + b


@mcp.tool()
def multiply(a: int, b: int) -> int:
    """
    This function multiplies two numbers.
    """
    return a * b


if __name__ == "__main__":
    mcp.run(transport="stdio")
    