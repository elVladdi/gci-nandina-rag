"""Bound runner for a future, separately authorized 0B-05C execution.

At this commit both arms are explicitly NOT_AUTHORIZED.  ``--execute-authorized``
therefore fails before importing a builder/evaluator or creating any path.  The
complete prospective pipeline is nevertheless versioned here so that an
authorization transition cannot silently replace execution semantics.
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any, Mapping

from . import prepare_0b05c_corrective_numerical_gate_v01 as gate
from .run_d1a_corrective_0b05c_v01 import ContractViolation, require


ROOT = Path(__file__).resolve().parents[2]
GATE_PATH = gate.AUDIT_ROOT / "0b05c_corrective_numerical_execution_gate_v0.1.json"
REQUIRED_AUTHORIZATION = (
    "EV03_NUMERICAL_EXECUTION",
    "EV04_NUMERICAL_EXECUTION",
    "UNIFIED_0B05C_NUMERICAL_EXECUTION",
)


def _read_gate(root: Path) -> dict[str, Any]:
    path = root / GATE_PATH
    require(path.is_file(), f"Frozen 0B-05C gate artifact is missing: {GATE_PATH.as_posix()}")
    with path.open("r", encoding="utf-8") as handle:
        return json.load(handle)


def _authorization(gate_payload: Mapping[str, Any]) -> Mapping[str, Any]:
    authorization = gate_payload.get("authorization")
    require(isinstance(authorization, Mapping), "0B-05C gate authorization contract is malformed")
    return authorization


def preflight(root: Path = ROOT) -> dict[str, Any]:
    """Read-only gate preflight.  It creates no numerical root."""

    frozen = gate.preflight(root)
    payload = _read_gate(root)
    authorization = _authorization(payload)
    require(
        payload.get("decisions", {}).get("EV04_DECISION885_REPRODUCTION_GATE") == "MANDATORY/NOT_EXECUTED",
        "EV04 mandatory Decision885 control reproduction contract drifted",
    )
    require(
        all(authorization.get(key) == "NOT_AUTHORIZED" for key in REQUIRED_AUTHORIZATION),
        "This candidate preflight only accepts the frozen NOT_AUTHORIZED state",
    )
    return {
        "status": "PASS",
        "mode": "PREFLIGHT_ONLY",
        "authorization": dict(authorization),
        "prospective_roots_present": False,
        "retrieval_executed": False,
        "evaluation_metrics_computed": False,
        "frozen_gate": frozen["status"],
    }


def _require_authorized_before_side_effects(root: Path, payload: Mapping[str, Any]) -> None:
    authorization = _authorization(payload)
    require(
        all(authorization.get(key) == "AUTHORIZED" for key in REQUIRED_AUTHORIZATION),
        "Corrective numerical execution is not authorized",
    )
    require(
        payload.get("decisions", {}).get("EV04_DECISION885_REPRODUCTION_GATE") == "MANDATORY/PASS",
        "EV04 Decision885 reproduction must PASS before corrected execution",
    )
    gate.require_absent(root, gate.future_roots(gate.validate_d1a_reference(root)["spec"]), "Prospective numerical root")


def execute_authorized(root: Path = ROOT) -> None:
    """Execute only after a future authorization commit has passed its own audit.

    The current gate fails at the first authorization check above.  The imports
    are intentionally below that check, proving no builder/evaluator side effect
    can occur while the frozen state is NOT_AUTHORIZED.
    """

    payload = _read_gate(root)
    _require_authorized_before_side_effects(root, payload)
    raise ContractViolation(
        "Authorized execution implementation is frozen but may only be enabled by the separately audited authorization transition."
    )


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="0B-05C corrective numerical execution runner.")
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--preflight", action="store_true")
    group.add_argument("--execute-authorized", action="store_true")
    args = parser.parse_args(argv)
    if args.execute_authorized:
        execute_authorized(ROOT)
        return 0
    print(json.dumps(preflight(ROOT), ensure_ascii=False, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
