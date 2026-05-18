"""
system_switch_agent — DIFC↔Mainland context switch (v0.1).

Handles Intent.SYSTEM_SWITCH: toggles between DIFC (offshore common-law English)
and Dubai Mainland (onshore civil-law Arabic) legal systems mid-session.

PROVENANCE: structural — no domain claims. ADR-005 mandates dual-system separation.
"""

from ailawfirm_dubai.core.ontology import System


# v0.1: in-memory session state. v0.2+: persistent per-project config.
_current_system: System = System.BOTH


def handle(payload: str) -> dict:
    global _current_system
    p = payload.lower()

    if any(k in p for k in ["difc", "offshore", "common law"]):
        _current_system = System.DIFC
        return {
            "agent": "system_switch_agent",
            "status": "switched",
            "system": "DIFC",
            "language": "English",
            "law": "Common-law",
            "courts": "DIFC CFI · CA · Cassation · SCT",
            "note": "DIFC context active — DIFC statutes, English proceedings",
        }
    elif any(k in p for k in ["mainland", "onshore", "civil law", "arabic"]):
        _current_system = System.MAINLAND
        return {
            "agent": "system_switch_agent",
            "status": "switched",
            "system": "Mainland",
            "language": "Arabic",
            "law": "Civil-law",
            "courts": "Dubai CFI · CA · Cassation · RDC",
            "note": "Mainland context active — UAE Federal statutes, Arabic proceedings",
        }
    elif "both" in p:
        _current_system = System.BOTH
        return {
            "agent": "system_switch_agent",
            "status": "switched",
            "system": "Both",
            "language": "English + Arabic",
            "law": "Common-law + Civil-law",
            "courts": "All DIFC + Mainland courts",
            "note": "Dual-system context active",
        }
    else:
        return {
            "agent": "system_switch_agent",
            "status": "no_switch",
            "current_system": _current_system.value,
            "hint": "Say 'switch to DIFC', 'switch to Mainland', or 'switch to both'",
        }


def get_current_system() -> str:
    """Return the current system context."""
    return _current_system.value
