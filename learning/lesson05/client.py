import asyncio

from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client


server_params = StdioServerParameters(
    command="uv",
    args=[
        "run",
        "python",
        "learning/lesson05/server.py",
    ],
)


async def main():
    async with stdio_client(server_params) as (read, write):

        async with ClientSession(read, write) as session:

            await session.initialize()

            # Tools
            tools = await session.list_tools()

            print("=== Tools ===")
            for tool in tools.tools:
                print(tool.name)

            # Call tool
            result = await session.call_tool(
                "add",
                arguments={
                    "a": 10,
                    "b": 20,
                },
            )

            print("=== Tool Result ===")
            print(result)
            # meta=None content=[TextContent(type='text', text='30', annotations=None, meta=None)] structured_content={'result': 30} is_error=False result_type='complete'

            # Resources
            resources = await session.list_resources()

            print("=== Resources ===")
            for resource in resources.resources:
                print(resource.uri)

            # Resource templates
            templates = await session.list_resource_templates()

            print("=== Resource Templates ===")
            print(templates)
            # meta=None ttl_ms=0 cache_scope='private' next_cursor=None resource_templates=[ResourceTemplate(name='greeting', title=None, uri_template='greeting://{name}', description='Generate a greeting.', mime_type='text/plain', icons=None, annotations=None, meta=None)] result_type='complete'

            # Read resource
            resource_result = await session.read_resource(
                "greeting://Geoffrey"
            )

            print("=== Resource Result ===")
            print(resource_result)
            # meta=None ttl_ms=0 cache_scope='private' contents=[TextResourceContents(uri='greeting://Geoffrey', mime_type='text/plain', meta=None, text='Hello, Geoffrey!')] result_type='complete'

            # Prompts
            prompts = await session.list_prompts()

            print("=== Prompts ===")
            for prompt in prompts.prompts:
                print(prompt.name)

            # Get prompt
            prompt_result = await session.get_prompt(
                "explain",
                arguments={
                    "topic": "Model Context Protocol",
                },
            )

            print("=== Prompt Result ===")
            print(prompt_result)
            # meta=None description='Create an explanation prompt.' messages=[PromptMessage(role='user', content=TextContent(type='text', text='\nYou are an expert teacher.\n\nExplain the following topic clearly:\n\nModel Context Protocol\n', annotations=None, meta=None))] result_type='complete'

async def list_server_info():
    async with stdio_client(server_params) as (read, write):
        async with ClientSession(read, write) as session:
            await session.initialize()

            print("=== Tools ===")
            tools = await session.list_tools()
            for tool in tools.tools:
                print(tool.name)
            resources = await session.list_resources()

            print("=== Resources ===")
            for resource in resources.resources:
                print(resource.uri)

            # Resource templates
            templates = await session.list_resource_templates()

            print("=== Resource Templates ===")
            for template in templates.resource_templates:
                print(template.uri_template)
            prompts = await session.list_prompts()

            print("=== Prompts ===")
            for prompt in prompts.prompts:
                print(prompt.name)

async def test_tool():
    async with stdio_client(server_params) as (read, write):
        async with ClientSession(read, write) as session:
            await session.initialize()
            # Call tool
            result = await session.call_tool(
                "add",
                arguments={
                    "a": 10,
                    "b": 20,
                },
            )
            print(result.content[0].text)  # type: ignore # Should print '30'

async def test_resource():
    async with stdio_client(server_params) as (read, write):
        async with ClientSession(read, write) as session:
            await session.initialize()
            # Read resource
            resource_result = await session.read_resource(
                "greeting://Geoffrey"
            )
            print(resource_result.contents[0].text)  # type: ignore # Should print 'Hello, Geoffrey!'

async def execute_command(
    command: str):
    async with stdio_client(server_params) as (read, write):
            async with ClientSession(read, write) as session:
                await session.initialize()
                if command == "list_tools":
                    tools = await session.list_tools()
                    print("=== Tools ===")
                    for tool in tools.tools:
                        print(tool.name)
                elif command == "list_resources":
                    resources = await session.list_resources()
                    print("=== Resources ===")
                    for resource in resources.resources:
                        print(resource.uri)
                elif command == "list_resource_templates":
                    templates = await session.list_resource_templates()
                    print("=== Resource Templates ===")
                    for template in templates.resource_templates:
                        print(template.uri_template)
                elif command == "list_prompts":
                    prompts = await session.list_prompts()
                    print("=== Prompts ===")
                    for prompt in prompts.prompts:
                        print(prompt.name)
                else:
                    print(f"Unknown command: {command}")

if __name__ == "__main__":
    asyncio.run(test_resource())
    asyncio.run(test_tool())
    asyncio.run(execute_command("list_tools"))
    # main() / list_server_info() / test_tool() / test_resource() / execute_command() can be called to test the client functionality