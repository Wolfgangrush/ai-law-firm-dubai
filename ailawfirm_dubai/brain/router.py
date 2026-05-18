"""
Brain router — dispatches an intent to the matching agent.

v0.1: import-and-call pattern. v0.2+: dynamic agent registry.

PROVENANCE: structural (no domain claims here).
"""

import importlib
from ailawfirm_dubai.brain.intents import Intent, AGENT_FOR_INTENT


def route(intent: Intent, payload: str) -> dict:
    """Dispatch an intent to the matching agent's handle() function."""
    agent_module_name = AGENT_FOR_INTENT.get(intent, "matter_agent")
    full_module = f"ailawfirm_dubai.agents.{agent_module_name}"
    try:
        mod = importlib.import_module(full_module)
        handler = getattr(mod, "handle", None)
        if handler is None:
            return {
                "ok": False,
                "intent": intent.value,
                "agent": agent_module_name,
                "error": f"agent module {full_module} has no handle() function",
            }
        result = handler(payload)
        return {
            "ok": True,
            "intent": intent.value,
            "agent": agent_module_name,
            "result": result,
        }
    except ImportError as e:
        return {
            "ok": False,
            "intent": intent.value,
            "agent": agent_module_name,
            "error": f"agent module import failed: {e}",
        }


def think(text: str) -> dict:
    """Convenience: classify + route in one call."""
    from ailawfirm_dubai.brain.classifier import classify

    intent = classify(text)
    return route(intent, text)
