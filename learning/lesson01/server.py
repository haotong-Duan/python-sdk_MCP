# uv run mcp dev learning/lesson01/server.py
from typing_extensions import Any
from mcp.server import MCPServer
import sys
import platform
import os

mcp = MCPServer("My First MCP Server")

@mcp.tool()
def add(a: int, b: int) -> int:       # schema(to json): {"a": "int", "b": "int"} -> int
    """Add two numbers."""
    return a + b

@mcp.tool()
def get_length(s: str) -> int:
    """Get the length of a string."""
    return len(s)

@mcp.resource("greeting://{name}")
def greeting(name: str) -> str:
    """Generate a greeting message."""
    return f"Hello, {name}!"

@mcp.tool()
def get_system_info() -> dict[str, Any]:
    """Get system information."""
    return {
        "platform": platform.platform(),
        "python_version": sys.version,
        "current_working_directory": os.getcwd(),
    }

