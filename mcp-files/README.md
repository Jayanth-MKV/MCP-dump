# MCP Files Workspace

Multi-project workspace demonstrating the Model Context Protocol (MCP) across:

1. Python file management MCP server (`mcp-server` package) exposing safe workspace file + directory tools.
2. Example Python MCP clients (plain + LangGraph ReAct agent) in `examples/`.
3. Cloudflare Workers based MCP server (`mcp-hello`) using `workers-mcp` (TypeScript) to expose simple greeting/time tools.

---

## Contents

| Path                | Description                                                                        |
| ------------------- | ---------------------------------------------------------------------------------- |
| `pyproject.toml`    | Root Python workspace (managed by `uv`) pulling in the local `mcp-server` package. |
| `mcp-server/`       | Python FastMCP server exposing file operations.                                    |
| `examples/clients/` | Sample Python clients (FastMCP + LangGraph agent).                                 |
| `mcp-hello/`        | Cloudflare Workers MCP server in TypeScript.                                       |
| `workspace/`        | Default workspace directory the Python file server operates on.                    |

---

## Quick Start (Python File Server)

Prerequisites: Python 3.13+ and `uv` (https://github.com/astral-sh/uv).

```powershell
# From repository root
uv sync

# Run the file MCP server (defaults: 127.0.0.1:8000, SSE transport)
uv run mcp-server
```

Environment overrides (optional):

```powershell
$env:MCP_SERVER_HOST='0.0.0.0'
$env:MCP_SERVER_PORT='9001'
$env:MCP_WORKSPACE_DIR='workspace'
uv run mcp-server
```

### List Tools Programmatically

```python
from fastmcp import Client
from fastmcp.client.transports import SSETransport

async with Client(SSETransport(url="http://127.0.0.1:8000/sse")) as c:
	tools = await c.list_tools()
	print([t.name for t in tools])
```

---

## Example: LangGraph ReAct Agent

The example agent uses Gemini via `langchain-google-genai`.

Set env variable (PowerShell shown):

```powershell
$env:GOOGLE_API_KEY = '<your key>'
uv run examples/clients/react_agent.py
```

You can now chat and invoke file tools automatically.

---

## Tool Summary (Python File Server)

| Tool              | Purpose                                  | Key Params     |
| ----------------- | ---------------------------------------- | -------------- | ----- | ---- |
| `create_file`     | Create text file (parents auto-created). | path, content? |
| `read_file`       | Read file contents.                      | path           |
| `write_file`      | Overwrite / create file.                 | path, content  |
| `append_file`     | Append to file.                          | path, content  |
| `delete_path`     | Delete file or directory recursively.    | path           |
| `rename_path`     | Rename / move (non-recursive).           | src, dst       |
| `copy_path`       | Copy file or directory.                  | src, dst       |
| `move_path`       | Move file or directory.                  | src, dst       |
| `list_files`      | List all files (relative).               | —              |
| `list_dirs`       | List all directories.                    | —              |
| `search_file`     | Grep-like line match.                    | path, term     |
| `file_info`       | JSON metadata.                           | path           |
| `workspace_stats` | Aggregate JSON stats.                    | —              |
| `path_exists`     | Return file                              | dir            | none. | path |

---

## Cloudflare Workers MCP (`mcp-hello`)

Independent TypeScript MCP Worker exposing:

- `sayHello(name)` → friendly greeting.
- `getCurrentTime(message?)` → ISO timestamp with optional message.

Quick start:

```powershell
cd mcp-hello
pnpm install   # or npm install / yarn
pnpm dev       # starts wrangler dev
```

Run tests:

```powershell
pnpm test
```

Deploy (requires configured Cloudflare account + API token):

```powershell
pnpm deploy
```

The `workers-mcp docgen` step in the deploy script can emit MCP metadata for IDE / client integration.

---

## Development Notes

- Python dependency management: `uv sync` regenerates `.venv` (no `pip install` needed).
- Add new tools in `mcp-server/src/mcp_server/tools.py` using `@mcp.tool` decorator.
- The root project depends on local `mcp-server` via `[tool.uv.sources]`.
- Adjust workspace root for file operations using `--workspace` CLI arg or `MCP_WORKSPACE_DIR`.

---

## Roadmap / Ideas

- Add auth / capability filtering per tool.
- Streaming responses for large file reads (chunked).
- Syntax-aware search / indexing.
- Tests for tool edge cases.

---

## License

MIT (add full text in a LICENSE file if distributing publicly).

---

## Contributing

1. Fork & branch.
2. Make changes with clear commits.
3. Include or update examples if adding tools.
4. Open PR describing motivation + behavior.

---

## Troubleshooting

| Issue                | Tip                                                                |
| -------------------- | ------------------------------------------------------------------ |
| Server not reachable | Confirm port (default 8000) and transport `sse`.                   |
| Tools list empty     | Server may not have finished starting; retry after a moment.       |
| File ops denied      | Ensure path resolves inside configured workspace (security guard). |
| Gemini auth error    | Verify `GOOGLE_API_KEY` environment variable.                      |

---

Happy hacking with MCP! 🚀
