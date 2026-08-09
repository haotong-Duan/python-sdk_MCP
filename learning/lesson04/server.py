from logging import error

from mcp.server import MCPServer

mcp = MCPServer(
    "Prompt Demo"
)

@mcp.prompt()
def explain_code(code: str):
    """
    Explain a piece of code.
    """
    return f"You are an expert Python engineer. Explain the following code: python {code}"

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
    code:str
    language:str="python"
    level:str="expert"
):
    """
    Review a piece of code.
    """
    return f"You are an expert Python engineer. Review the following code: python {code}. Please follow these steps: 1. Analyze code 2. Provide feedback 3. Suggest improvements."