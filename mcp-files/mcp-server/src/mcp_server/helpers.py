from pathlib import Path
from .config import BASE
from typing import Iterable


# ----------------------------- helpers ---------------------------------- #

def _resolve(rel: str) -> Path:
    """Resolve a relative path safely within the workspace sandbox."""
    p = (BASE / rel).resolve()
    if BASE not in p.parents and p != BASE:
        raise ValueError("Path escapes workspace")
    return p


def _iter_files() -> Iterable[Path]:
    for p in BASE.rglob("*"):
        if p.is_file():
            yield p


def _ok(msg: str) -> str:  # tiny convention wrapper
    return msg


def _err(e: Exception) -> str:  # pragma: no cover (simple path)
    return f"Error: {e}"

__all__ = ["_resolve", "_iter_files", "_ok", "_err"]