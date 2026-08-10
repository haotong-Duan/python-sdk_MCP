from mcp.server import MCPServer
import json
import platform
import sys
mcp = MCPServer(
    "stdio-demo"
)

@mcp.tool()
def multiply(
    a:int,
    b:int
)->int:

    """
    Multiply two numbers.
    """

    return a*b

@mcp.resource("system://info")
def system_info() -> str:
    """Return system information in JSON format."""
    info = {
        "os": "macOS" if platform.system() == "Darwin" else platform.system(),
        "python": f"{sys.version_info.major}.{sys.version_info.minor}",
    }
    return json.dumps(info, indent=2)

if __name__ == "__main__":
    mcp.run() # run MCP Server transport