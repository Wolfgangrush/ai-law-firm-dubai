"""
Ontology module — AI Law Firm · Dubai-DIFC · Solo · v0.1

Defines core enums for Dubai legal practice:
- System: DIFC vs Mainland (One City, Two Systems)
- MatterType: case file types for both systems
- DubaiCourt: court hierarchy (DIFC + Mainland)
- DubaiStatute: statute registry (DIFC + UAE Federal)
- DubaiBarRule: professional regulation references

v0.1 = shape only (enums + dataclasses). Real content lands v0.2+.

PROVENANCE: CITED:_research/ files for claims; STUB for metadata.
"""

from enum import Enum
from dataclasses import dataclass, field
from typing import Optional


class System(Enum):
    """Dubai operates as 'One City, Two Systems' per ADR-005.
    PROVENANCE: CITED:01-court-hierarchy.md
    """
    DIFC = "DIFC (offshore common-law · English)"
    MAINLAND = "Dubai Mainland (onshore civil-law · Arabic)"
    BOTH = "Dual-system practitioner"


class MatterType(Enum):
    """Dubai legal matter types — non-exhaustive v0.1 set.
    PROVENANCE: CITED:01-court-hierarchy.md, 02-difc-court-law.md, 04-dubai-judicial-authority-law.md
    """
    # DIFC
    DIFC_CIVIL = "DIFC Civil Claim (CFI)"
    DIFC_SMALL_CLAIMS = "DIFC Small Claims (under USD 500k)"
    DIFC_ARBITRATION = "DIFC Arbitration"
    DIFC_INSOLVENCY = "DIFC Insolvency Petition"
    DIFC_EMPLOYMENT = "DIFC Employment Claim"
    # Mainland
    MAINLAND_CIVIL = "Mainland Civil Suit"
    MAINLAND_COMMERCIAL = "Mainland Commercial Suit"
    MAINLAND_CRIMINAL = "Mainland Criminal Case"
    MAINLAND_PERSONAL_STATUS = "Mainland Personal Status (Family)"
    MAINLAND_LABOUR = "Mainland Labour Case"
    MAINLAND_RENTAL = "Rental Disputes Center matter"
    OTHER = "Other"


class DubaiCourt(Enum):
    """Dubai court hierarchy — v0.1 stubs.
    PROVENANCE: CITED:01-court-hierarchy.md, 02-difc-court-law.md, 04-dubai-judicial-authority-law.md, 21-rent-dispute-center-tribunal.md
    """
    # DIFC
    DIFC_CFI = "DIFC Court of First Instance"
    DIFC_CA = "DIFC Court of Appeal"
    DIFC_CASSATION = "DIFC Court of Cassation"
    DIFC_SCT = "DIFC Small Claims Tribunal"
    # Mainland
    DUBAI_CFI = "Dubai Court of First Instance"
    DUBAI_CA = "Dubai Court of Appeal"
    DUBAI_CASSATION = "Dubai Court of Cassation"
    DUBAI_RDC = "Rental Disputes Center"
    OTHER = "Other"


class DubaiStatute(Enum):
    """Dubai statute registry slots — v0.1 references only.
    PROVENANCE: CITED:_research/ files; STUB for text content (v0.2+).
    """
    # DIFC
    DIFC_CONTRACT_LAW = "DIFC Contract Law (Amendment No. 5 of 2024)"
    DIFC_EMPLOYMENT_LAW = "DIFC Employment Law (No. 2 of 2019)"
    DIFC_DPL = "DIFC Data Protection Law (No. 5 of 2020) — GDPR-aligned"
    DIFC_COMPANIES_LAW = "DIFC Companies Law"
    DIFC_INSOLVENCY_LAW = "DIFC Insolvency Law"
    DIFC_RDC = "Rules of the DIFC Courts (RDC)"
    # Mainland (Federal + Emirate)
    UAE_CIVIL_CODE = "UAE Federal Civil Transactions Law (Civil Code)"
    UAE_COMMERCIAL_CODE = "UAE Federal Commercial Transactions Law"
    UAE_PENAL_CODE = "UAE Federal Penal Code"
    UAE_PERSONAL_STATUS = "UAE Federal Personal Status Law"
    UAE_FEDERAL_DPP = "Federal Decree-Law No. 45 of 2021 — Federal Personal Data Protection"
    UAE_AML = "Federal Decree-Law No. 20 of 2018 — Anti-Money Laundering · goAML mandatory"


class DubaiBarRule(Enum):
    """Dubai bar rule references — professional regulation.
    PROVENANCE: CITED:06-uae-legal-profession-law.md, 10-bar-rule-publicity-solicitation.md, 26-mandatory-cpe-clpd-requirements.md
    """
    UAE_LEGAL_PROFESSION_LAW = "UAE Federal Law on the Legal Profession (Mainland)"
    DIFC_ACADEMY_STANDARDS = "DIFC Academy of Law Code of Conduct"
    CLPD_REQUIREMENT = "CLPD — 16 points/year mandatory for license renewal"
    PUBLICITY_RESTRICTION = "UAE Law on Legal Profession + DIFC Academy standards — publicity restrictions"
    CONFIDENTIALITY = "Confidentiality obligations per UAE Legal Profession Law"
    CONFLICT_OF_INTEREST = "Conflict of interest rules per bar regulation"


@dataclass
class Matter:
    """A single matter (case file) — v0.1 shape only.
    PROVENANCE: STUB — full lifecycle lands v0.2+.
    """
    matter_id: str
    matter_type: MatterType
    system: System
    court: DubaiCourt
    short_title: str
    parties_plaintiff: list[str] = field(default_factory=list)
    parties_defendant: list[str] = field(default_factory=list)
    statutes_invoked: list[DubaiStatute] = field(default_factory=list)
    language: str = "en"  # 'en' DIFC default · 'ar' Mainland default
    filed_date: Optional[str] = None
    next_hearing_date: Optional[str] = None
    next_hearing_location: Optional[str] = None
    status_note: Optional[str] = None


@dataclass
class Citation:
    """A parsed Dubai legal citation — produced by dubai_citation_validator MCP tool.
    PROVENANCE: CITED:09-citation-formats.md
    """
    raw: str
    format: str  # 'DIFC' | 'MAINLAND' | 'UNKNOWN'
    year: Optional[int] = None
    court_or_reporter: Optional[str] = None
    case_number: Optional[int] = None
    valid: bool = False
    parse_notes: Optional[str] = None
    system: Optional[str] = None  # 'DIFC' or 'MAINLAND'


@dataclass
class CalendarEvent:
    """A calendar event for Dubai matter — produced by dubai_calendar_sync MCP tool.
    PROVENANCE: STUB — ICS parsing is structural, not domain-specific.
    Timezone: Asia/Dubai (UTC+4, no DST).
    """
    uid: str
    summary: str
    start_time: str  # ISO 8601
    end_time: Optional[str] = None
    location: Optional[str] = None
    description: Optional[str] = None
    matter_id: Optional[str] = None
    timezone: str = "Asia/Dubai"
