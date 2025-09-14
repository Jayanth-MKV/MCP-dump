import os
from pathlib import Path

# Default network configuration (can be overridden via environment variables)
DEFAULT_HOST = os.getenv("MCP_SERVER_HOST", "127.0.0.1")
DEFAULT_PORT = int(os.getenv("MCP_SERVER_PORT", "8000"))

# Define the workspace directory relative to the package root unless overridden
WORKSPACE_DIR = os.getenv("MCP_WORKSPACE_DIR","workspace")

# Ensure the workspace directory exists
os.makedirs(WORKSPACE_DIR, exist_ok=True)


BASE = Path(WORKSPACE_DIR).resolve()
BASE.mkdir(parents=True, exist_ok=True)

__all__ = ["WORKSPACE_DIR", "DEFAULT_HOST", "DEFAULT_PORT"]
