from mcp.server import MCPServer
from typing import Any, Optional
from pydantic import BaseModel
mcp = MCPServer("Schema Demo")

@mcp.tool()
def user_profile(
    name: str,
    age: int,
    height: float,
    active: bool
) -> str:
    """
    Create a user profile.
    """

    return (
        f"name={name}, "
        f"age={age}, "
        f"height={height}, "
        f"active={active}"
    )

@mcp.tool()
def search(
    query: str,
    limit: Optional[int] = None
) -> str:

    """
    Search documents.
    """

    return f"query={query}, limit={limit}"

@mcp.tool()
def generate_report(
    topic: str,
    language: str = "English"
) -> str:

    """
    Generate report.
    """

    return f"{topic}-{language}"

class User(BaseModel):
    name: str
    age: int
    skills: list[str]

@mcp.tool()
def create_user(user: dict[str, Any]) -> str:
    """
    Create user.
    """
    user_obj = User.model_validate(user)
    return user_obj.model_dump_json()
'''
input example:
{
"name":"Alice",
"age":20,
"skills":[
"python",
"AI"
]
}
'''

