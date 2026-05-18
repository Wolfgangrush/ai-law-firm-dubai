"""
drafting_agent — drafting needs detection (v0.1 stub).

v0.1: detects drafting intent, returns template category.
v0.2+: full drafting pipeline with Wolfgang Rush plugins.

PROVENANCE: STUB.
"""


def handle(payload: str) -> dict:
    p = payload.lower()
    suggestions = []
    if any(k in p for k in ["statement of claim", "claim form"]):
        suggestions.append("Statement of Claim / Claim Form template (DIFC)")
    if any(k in p for k in ["defence", "defense"]):
        suggestions.append("Defence template")
    if any(k in p for k in ["affidavit", "witness"]):
        suggestions.append("Witness Statement / Affidavit template")
    if any(k in p for k in ["skeleton", "submissions"]):
        suggestions.append("Skeleton Argument / Written Submissions template")
    return {
        "agent": "drafting_agent",
        "status": "v0.1 — keyword detection, no templates yet",
        "suggestions": suggestions or ["general drafting — specify document type"],
        "note": "drafting templates land via Wolfgang Rush plugin family · v0.2+",
    }
