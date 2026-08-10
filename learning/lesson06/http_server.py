from mcp.server import MCPServer
mcp = MCPServer(
    "http-demo"
)

@mcp.tool()
def add(
    a:int,
    b:int
):
    return a+b

if __name__=="__main__":
    mcp.run(
        transport="streamable-http"
    )