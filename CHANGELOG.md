# Changelog

## [0.1.1] — 2026-06-05 · Dual-mode disclosure refinement (with UAE PDPL Article 22 + DIFC-DPL Article 26 cloud-mode clarification)

### Changed
- **README.md** — refined headline tagline, "Why this exists" closing line, tier table rows (Local Ollama · DeepSeek · Claude/Gemini), and "Privacy & Data Handling — what stays where" section to honestly disclose the dual-mode architecture (local-default · cloud-optional) and the role of the internalised Pseudonymisation Gateway as the structural privacy primitive when cloud mode is invoked.

  **UAE PDPL Article 22 + DIFC-DPL Article 26 are now explicitly framed dual-mode**:
  - Local Ollama tier — neither regime triggered (no cross-border transfer)
  - Cloud tier — both regimes apply; Gateway sanitisation supports the safeguard posture (technical measure) but does NOT discharge the underlying obligation (adequacy / standard contractual provisions / consent / other lawful basis)

  **Special-category data** (DIFC-DPL Article 9 + Mainland PDPL Article 9): pointed to Local Ollama tier as the safe default; cloud-mode requires explicit lawful basis + safeguards atop Gateway sanitisation.

  **goAML Tranche 2 AML** + **DIFC Code of Conduct** + **UAE Legal Profession Code** named as sectoral overlays that apply atop the dual-mode architecture.

  **DIFC-Mainland system separation** (independent of dual-mode privacy architecture) — clarified that `system_switch_agent` enforcement is orthogonal to the local-default / cloud-optional decision.

  Prior wording overstated by treating local-only as architectural fact across all tiers; the architecture is in fact **local-default with cloud-optional + Gateway-sanitised cloud transmission**.

### Why this matters
A Dubai solo practitioner relying on the prior *"Your data stays on your machine"* line who configured a cloud-LLM provider for Article 22-restricted client work would have been misled about the residual Article 22 / Article 26 safeguard obligations the Gateway supports but does NOT discharge. The refinement is honest disclosure; the Gateway as a privacy primitive is materially stronger than what most cloud-AI legal tools offer; the wedge for choosing this tool over commodity cloud AI is preserved.

### Unchanged
- All agents (including `system_switch_agent`), drafting templates (81 dual-track templates + 24 statute digests), tests, getting-started guides, and the Pseudonymisation Gateway itself are unchanged. This is a documentation + privacy-disclosure-honesty refinement, not a behavioural change.
