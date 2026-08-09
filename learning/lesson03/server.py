from pathlib import Path
from mcp.server import MCPServer

mcp = MCPServer(
    "Developer Resource Server"
)

BASE = Path("/Users/haotongduan/Documents/VS_code/python-sdk_MCP/learning/lesson03/project")
BASE_knowledge = Path("/Users/haotongduan/Documents/VS_code/python-sdk_MCP/learning/lesson03/knowledge")

@mcp.resource(
    "project://readme"
)
def read_readme():

    return (
        BASE
        .joinpath("README.md")
        .read_text()
    )

@mcp.resource(
    "knowledge://{topic}}"
)
def read_knowledge_readme(topic: str):

    return (
        BASE_knowledge
        .joinpath(f"{topic}.md")
        .read_text()
    )


@mcp.resource(
    "project://config"
)
def read_config():

    return (
        BASE
        .joinpath("config.json")
        .read_text()
    )

@mcp.resource("user://{id}-{name}-{role}")
def read_user(id: int, name: str, role: str):

    return {
        "id": id,
        "name": name,
        "role": role
    }

@mcp.resource("project://tree")
def get_project_tree() -> str:
    """
    Tree structure of the project directory, excluding certain directories/files.
    """
    root = Path(".")
    lines = [f"{root.resolve().name}/"]

    ignore_set = {".git", ".venv", "venv", "__pycache__", ".pytest_cache", ".idea", ".vscode"}
    paths = sorted(root.rglob("*"))

    for path in paths:
        if any(part in ignore_set for part in path.parts):
            continue
        rel_path = path.relative_to(root)
        depth = len(rel_path.parts) - 1
        indent = "│   " * depth
        prefix = "├── "
        display_name = f"{path.name}/" if path.is_dir() else path.name
        lines.append(f"{indent}{prefix}{display_name}")

    return "\n".join(lines)