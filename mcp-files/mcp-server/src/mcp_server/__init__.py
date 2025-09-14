"""Lean MCP File Server tools.

Simplified + organized. Redundant / niche tools removed.
Core focus: create, read, write, list, search, move, copy, delete, stats.
Paths are validated & sandboxed inside the configured workspace.
"""

from __future__ import annotations

import os

from .mcp import mcp
from .config import BASE, DEFAULT_HOST, DEFAULT_PORT
from .tools import (
    create_file,
    read_file,
    write_file,
    append_file,
    delete_path,
    rename_path,
    copy_path,
    move_path,
    list_files,
    list_dirs,
    search_file,
    file_info,
    workspace_stats,
    path_exists,
)



__all__ = [
    "mcp",
    "run",
    # file ops
    "create_file",
    "read_file",
    "write_file",
    "append_file",
    "delete_path",
    "rename_path",
    "copy_path",
    "move_path",
    "list_files",
    "list_dirs",
    "search_file",
    "file_info",
    "workspace_stats",
    "path_exists",
]


# ----------------------------- server run ------------------------------- #


def run(
    host: str | None = None, port: int | None = None, transport: str = "sse"
) -> None:
    """Run the MCP server."""
    _host = host or os.getenv("MCP_SERVER_HOST", DEFAULT_HOST)
    _port = int(port or os.getenv("MCP_SERVER_PORT", DEFAULT_PORT))
    print(f"Workspace: {BASE}")
    print(f"Listening on {_host}:{_port} (transport={transport})")
    if transport in {"sse", "http"}:
        mcp.run(transport=transport, host=_host, port=_port)
    else:
        mcp.run()
