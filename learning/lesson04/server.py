from mcp.server import MCPServer

mcp = MCPServer(
    "Prompt Demo"
)

@mcp.tool()
def add_numbers(a: int, b: int):
    """
    Add two numbers together.
    """
    return a + b


@mcp.resource("device://{device_id}")
def get_device_info(device_id: str):
    """
    Get information about a device.
    """
    return f"Device info for {device_id}"

@mcp.prompt()
def debug_python(
    error:str,
    code:str
):
    """
    Debug a piece of Python code.
    """
    return f"You are an Python debugging expert. Debug the following code: python {code} and fix the following error: {error}. Please follow these steps: 1. Analyze error 2. Locate cause 3. Provide fix."

@mcp.prompt()
def review_code(
    code:str,
    language:str="python",
    level:str="expert"
):
    """
    Review a piece of code.
    """
    return f"You are an expert {language} engineer. Review the following code: python {code} with level {level}. Please follow these steps: 1. Analyze code 2. Provide feedback 3. Suggest improvements."
