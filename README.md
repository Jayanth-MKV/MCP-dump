# MCP-dump

A collection of Model Context Protocol (MCP) servers, clients, and experiments for learning, prototyping, and comparing implementation styles across runtimes (Cloudflare Workers, Python, etc.).

## Table of Contents

1. Overview
2. Repository Structure
3. What is MCP?
4. Project Summaries
5. Quick Start
6. Development Environment
7. Contributing
8. Disclaimer

---

## 1. Overview

This monorepo hosts multiple MCP server and client implementations exploring different tooling stacks (Python + `uv`, TypeScript + Cloudflare Workers) and agent patterns (LLM-backed analysis, reactive agents, tool invocation). It is intended as a playground and reference.

## 2. Repository Structure

```
MCP-dump/
├── ai-agent-postgres-mcp/        # AI agent using MCP to analyze a Postgres database
│   ├── ai_agent_postgres_mcp.ipynb
│   ├── main.py
│   └── README.md
├── mcp-hello/                    # Minimal MCP server (Cloudflare Workers / JS)
│   ├── src/
│   ├── test/
│   ├── package.json
│   └── README.md
├── mcp-files/                    # New Python MCP workspace (managed via uv)
│   ├── pyproject.toml            # Root Python project (workspace style)
│   ├── uv.lock
│   ├── examples/                 # Example Python clients & agents
│   │   └── clients/
│   │       ├── base.py
│   │       ├── gemini.py
│   │       └── react_agent.py
│   ├── mcp-server/               # Python MCP server implementation
│   │   ├── pyproject.toml
│   │   └── src/mcp_server/
│   │       ├── cli.py
│   │       ├── config.py
│   │       ├── helpers.py
│   │       ├── mcp.py
│   │       ├── tools.py
│   │       └── __init__.py
│   └── mcp-hello/                # (Experimental) parallel minimal example in Python
│       └── README.md
└── README.md
```

> Note: `mcp-files/mcp-hello` is a Python-flavored minimal example separate from the root `mcp-hello` Cloudflare Workers implementation. They intentionally explore analogous concepts in different runtimes.

## 3. What is MCP?

Model Context Protocol (MCP) standardizes how tools, agents, and large language models exchange contextual information, resources, and tool invocation results. It aims to:

- Provide predictable, typed exchanges
- Reduce ad-hoc prompt engineering glue
- Support richer, stateful multi-step agent behaviors

## 4. Project Summaries

- `ai-agent-postgres-mcp`: Demonstrates connecting an AI agent to Postgres via MCP for conversational querying & analysis.
- `mcp-hello` (Cloudflare / Workers): Minimal TypeScript MCP server showcasing deployment in edge environments.
- `mcp-files/mcp-server`: A Python MCP server with tooling abstractions, CLI entrypoint, and strongly-typed helpers.
- `mcp-files/examples/clients`: Example Python clients (including a basic reactive agent pattern and Gemini integration placeholder).
- `mcp-files/mcp-hello`: Lightweight Python analogue of the Cloudflare example (experimental).

## 5. Quick Start

### A. Cloudflare Workers MCP server (`mcp-hello` root)
1. Enter the directory:
    ```bash
    cd mcp-hello
    ```
2. Install deps (pnpm / npm / yarn):
    ```bash
    npm install
    ```
3. Run tests:
    ```bash
    npm test
    ```
4. (Optional) Publish / dev with Wrangler:
    ```bash
    npx wrangler dev
    ```

### B. Python MCP workspace (`mcp-files`)
This workspace uses [`uv`](https://github.com/astral-sh/uv) for fast resolution & execution.

1. Navigate:
    ```bash
    cd mcp-files
    ```
2. Run the Python MCP server (CLI):
    ```bash
    uv run mcp-server
    ```
3. Try a client example (reactive agent):
    ```bash
    uv run examples/clients/react_agent.py
    ```
4. Explore available tools by invoking help:
    ```bash
    uv run mcp-server --help
    ```

### C. Postgres AI Agent (`ai-agent-postgres-mcp`)
Follow its local `README.md` for database connection setup. Typically you'll:
```bash
cd ai-agent-postgres-mcp
uv run main.py  # or python main.py depending on your environment
```

## 6. Development Environment

| Layer | Tech | Notes |
|-------|------|-------|
| Edge server | Cloudflare Workers | Uses `workers-mcp` + Wrangler dev server |
| Python server | uv + pyproject | Fast lockfile (`uv.lock`), typed package layout |
| Tooling | LLM clients (Gemini placeholder) | Extend via `tools.py` in Python server |

Recommended:
- Install `uv` for Python: https://docs.astral.sh/uv/
- Keep commits atomic (feature / chore / docs) using Conventional Commits.
- Use `uv lock --upgrade` when updating deps in Python workspace.

## 7. Contributing

Contributions are welcome. Suggested contribution types:
- New MCP tool modules (`mcp-files/mcp-server/src/mcp_server/tools.py`)
- Additional runtime adapters (Rust, Go, etc.)
- Agent strategy examples (planning, retrieval-augmented, streaming)
- Documentation improvements & diagrams

Workflow:
1. Fork & branch from `main`.
2. Implement + add minimal docs/tests.
3. Run lint/tests (where applicable).
4. Open PR with clear description and rationale.

## 8. Disclaimer

These implementations are experimental and not guaranteed production-grade. Security, robustness, and performance concerns may be intentionally simplified for clarity.

---

If you find this useful, feel free to open issues with questions or ideas for additional MCP experiment directions.
