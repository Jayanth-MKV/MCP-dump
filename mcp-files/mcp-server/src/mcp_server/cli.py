"""Command line interface for the mcp-server package.

Usage examples:
  uv run mcp-server --host 0.0.0.0 --port 9000
  python -m mcp_server.cli --transport sse
"""

from __future__ import annotations

import argparse
import os
from typing import Optional

from . import run as run_programmatic, mcp  # re-exported for potential dynamic use
from .config import DEFAULT_HOST, DEFAULT_PORT, WORKSPACE_DIR


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Run the MCP file server.")
    parser.add_argument(
        "--host",
        default=None,
        help=f"Host interface to bind (default: env MCP_SERVER_HOST or {DEFAULT_HOST})",
    )
    parser.add_argument(
        "--port",
        type=int,
        default=None,
        help=f"Port to listen on (default: env MCP_SERVER_PORT or {DEFAULT_PORT})",
    )
    parser.add_argument(
        "--transport",
        default="sse",
        choices=["sse", "http", "stdio"],
        help="Transport mechanism (currently only 'sse').",
    )
    parser.add_argument(
        "--workspace",
        default=None,
        help="Override workspace directory (default: env MCP_WORKSPACE_DIR or packaged workspace).",
    )
    return parser


def main(argv: Optional[list[str]] = None) -> None:
    parser = build_parser()
    args = parser.parse_args(argv)

    if args.workspace:
        # Override via environment for consistency with config module semantics
        os.environ["MCP_WORKSPACE_DIR"] = args.workspace

    run_programmatic(host=args.host, port=args.port, transport=args.transport)


if __name__ == "__main__":  # pragma: no cover
    main()
