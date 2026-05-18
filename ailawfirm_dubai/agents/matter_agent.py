"""
matter_agent — matter tracking + update (v0.1 stub).

v0.1: echoes the payload. v0.2+: full matter lifecycle (hearings, orders, billing).
PROVENANCE: STUB.
"""


def handle(payload: str) -> dict:
    return {
        "agent": "matter_agent",
        "status": "v0.1 — stub",
        "payload": payload[:500],
        "note": "full matter lifecycle lands in v0.2+",
    }
