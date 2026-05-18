# SECURITY — AI Law Firm · Dubai-DIFC

## Reporting a vulnerability

If you discover a security vulnerability, please report via **GitHub Security Advisories** at:

https://github.com/Wolfgangrush/ai-law-firm-dubai/security/advisories/new

Or via private email: advrushikeshravindramahajan@gmail.com (please do NOT post vulnerabilities to public GitHub Issues).

Please include:
- A description of the vulnerability
- Steps to reproduce
- Potential impact
- Any suggested mitigation

We aim to acknowledge reports within 72 hours and provide an initial assessment within 7 days.

## Scope

Vulnerabilities in scope:
- Code-execution vulnerabilities
- Sensitive-data exposure
- Local privilege escalation via tool usage
- Cryptographic weaknesses

Out of scope:
- Upstream dependencies
- Cloud AI vendors
- Social-engineering attacks
- Physical access attacks

## Disclosure policy

Coordinated disclosure. No public disclosure until fix released or 90 days pass. Reporter credited (unless anonymity requested). No bug bounty at this time.

## Security hygiene

- Dependencies pinned in `requirements.txt`
- Quarterly `pip-audit` review
- No `eval` · no `exec`
- All user input filtered before crossing tool/OS boundary
- File paths normalized
- Subprocess calls audited

## Past advisories

(None as of v0.1)

---

*References LEGAL_EXPOSURE_PLAYBOOK §3.V11. Playbook v0.1.*
