from __future__ import annotations

import json
import os
from pathlib import Path
from typing import Any, Mapping

PROJECT_ROOT_ENV = "NANDINA_PROJECT_ROOT"


def project_root() -> Path:
    """Resolve the repository root, optionally overridden by an environment variable."""
    override = os.environ.get(PROJECT_ROOT_ENV)
    if override:
        return Path(override).expanduser().resolve()
    return Path(__file__).resolve().parents[2]


def resolve_project_path(path_value: str | os.PathLike[str], base_dir: str | os.PathLike[str] | None = None) -> Path:
    """Resolve project-relative paths while still accepting absolute local paths."""
    path = Path(path_value).expanduser()
    if path.is_absolute():
        return path

    if base_dir:
        base = Path(base_dir).expanduser()
        if not base.is_absolute():
            base = project_root() / base
    else:
        base = project_root()
    return (base / path).resolve()


def load_json(path: str | os.PathLike[str]) -> dict[str, Any]:
    with open(path, "r", encoding="utf-8") as file:
        return json.load(file)


def config_paths(config: Mapping[str, Any]) -> dict[str, Path]:
    """Resolve the common path entries from experiment_config.json."""
    raw_paths = dict(config.get("paths", {}))
    base_dir = raw_paths.get("base_dir") or "."
    return {
        key: resolve_project_path(value, base_dir=base_dir)
        for key, value in raw_paths.items()
        if key != "base_dir" and value
    }


def ensure_parent(path: str | os.PathLike[str]) -> Path:
    resolved = Path(path)
    resolved.parent.mkdir(parents=True, exist_ok=True)
    return resolved
