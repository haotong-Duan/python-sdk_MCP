import asyncio

from mcp import (
    ClientSession,
    StdioServerParameters
)

from mcp.client.stdio import (
    stdio_client
)

server_params = StdioServerParameters(
    command="uv",
    args=[
        "run",
        "python",
        "learning/lesson06/stdio_server.py"
    ]
)

async def main():
    async with stdio_client(
        server_params
    ) as (read,write):
        async with ClientSession(
            read,
            write
        ) as session:
            await session.initialize()
            tools = await session.list_tools()
            print("==== Available Tools ===")
            print([tool.name for tool in tools.tools])
            result = await session.call_tool(
                "multiply",
                {
                    "a":5,
                    "b":6
                }
            )
            print("==== Result of multiply(5,6) ===")
            print(result.content[0].text) # type: ignore
            system_info = await session.read_resource("system://info") # type: ignore
            print("==== System Information ===")
            print(system_info.contents[0].text) # type: ignore

if __name__=="__main__":
    asyncio.run(main())
