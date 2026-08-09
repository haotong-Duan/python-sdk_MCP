from mcp.server import MCPServer
mcp = MCPServer("Lesson05 Server")

@mcp.tool()
def add(a: int, b: int) -> int:
    """Add two integers."""
    return a + b


@mcp.resource("greeting://{name}")
def greeting(name: str) -> str:
    """Generate a greeting."""
    return f"Hello, {name}!"


@mcp.prompt()
def explain(topic: str) -> str:
    """Create an explanation prompt."""
    return f"""
You are an expert teacher.

Explain the following topic clearly:

{topic}
"""