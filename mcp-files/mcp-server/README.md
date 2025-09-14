## mcp-server (Python FastMCP File Workspace Server)

Feature-rich Model Context Protocol server exposing safe file + directory management inside a confined workspace.

### Highlights

- Secure path resolution (prevents escaping the configured workspace).
- Comprehensive CRUD + metadata tools (see table below).
- SSE (Server-Sent Events) transport by default; HTTP & stdio hooks scaffolded.
- Easily embeddable (`from mcp_server import run`).

---

### Install / Dev

From repository (or package) root:

```bash
uv sync
```

Run (defaults: host 127.0.0.1, port 8000, SSE transport):

```bash
uv run mcp-server
```

Help:

```bash
uv run mcp-server --help
```

Custom workspace & port:

```bash
uv run mcp-server --workspace ./my-workspace --port 9001
```

Environment variable equivalents (precedence: env < CLI args):

```
MCP_SERVER_HOST=0.0.0.0
MCP_SERVER_PORT=9001
MCP_WORKSPACE_DIR=./data
```

---

### Programmatic Usage

```python
from mcp_server import run

run(host="0.0.0.0", port=8050)  # blocks until interrupted
```

### Tool Reference

| Tool              | Description                           | Parameters     |
| ----------------- | ------------------------------------- | -------------- |
| `create_file`     | Create file (parents auto-created).   | path, content? |
| `read_file`       | Read text file.                       | path           |
| `write_file`      | Overwrite/create file.                | path, content  |
| `append_file`     | Append to file.                       | path, content  |
| `delete_path`     | Delete file or directory recursively. | path           |
| `rename_path`     | Rename/move entity.                   | src, dst       |
| `copy_path`       | Copy file or directory.               | src, dst       |
| `move_path`       | Move file or directory.               | src, dst       |
| `list_files`      | List all files (relative).            | —              |
| `list_dirs`       | List all directories (relative).      | —              |
| `search_file`     | Return lines containing term.         | path, term     |
| `file_info`       | JSON metadata (size, mtime, etc.).    | path           |
| `workspace_stats` | Aggregate workspace statistics.       | —              |
| `path_exists`     | file / dir / none.                    | path           |

---

### Example Client (FastMCP)

```python
import asyncio
from fastmcp import Client
from fastmcp.client.transports import SSETransport

async def main():
	async with Client(SSETransport(url="http://127.0.0.1:8000/sse")) as c:
		await c.ping()
		tools = await c.list_tools()
		print([t.name for t in tools])
		await c.call_tool("create_file", {"path": "demo.txt", "content": "Hello"})

asyncio.run(main())
```

---

### Project Layout

| File                     | Purpose                           |
| ------------------------ | --------------------------------- |
| `mcp_server/cli.py`      | CLI entry point (`mcp-server`).   |
| `mcp_server/config.py`   | Environment + default resolution. |
| `mcp_server/tools.py`    | All exposed MCP tools.            |
| `mcp_server/helpers.py`  | Internal path & response helpers. |
| `mcp_server/__init__.py` | Re-exports & `run` convenience.   |

---

### Extending

Add a new tool:

```python
from .mcp import mcp

@mcp.tool
def my_tool(arg: str) -> str:
	return f"processed {arg}"
```

Restart the server; tool auto-registers.

---

### Testing Ideas (Not Yet Implemented)

- Param edge cases (empty path, binary files).
- Large directory stats performance.
- Race conditions on rename/move.

---

### License

This project is licensed under the MIT License - see the LICENSE file for complete details.