"""Risk classification service for legal clauses."""
import logging
import re
from typing import List, Dict

logger = logging.getLogger(__name__)

HIGH_RISK_KEYWORDS = ["penalty", "termination", "liability", "fine", "breach",
                       "indemnify", "forfeit", "damages", "waiver of rights"]
MEDIUM_RISK_KEYWORDS = ["notice", "condition", "restriction", "obligation",
                         "amendment", "arbitration", "jurisdiction"]


def split_into_clauses(text: str) -> List[str]:
    """Split legal text into individual clauses."""
    # Split by numbered patterns, newlines, or sentence endings
    clauses = re.split(r'(?:\d+[\.\)]\s)|(?:\n\s*\n)|(?<=[.;])\s+', text)
    # Clean and filter
    clauses = [c.strip() for c in clauses if c and len(c.strip()) > 20]
    return clauses


def classify_clause(clause: str) -> Dict[str, str]:
    """
    Classify a single clause by risk level.
    
    # TODO: Replace keyword logic with BERT-based ML model API call:
    # response = httpx.post("http://ml-model-api/classify", json={"text": clause})
    # return response.json()
    """
    clause_lower = clause.lower()

    for keyword in HIGH_RISK_KEYWORDS:
        if keyword in clause_lower:
            return {
                "clause": clause[:200],
                "risk_level": "High",
                "reason": f"Contains high-risk term: '{keyword}'"
            }

    for keyword in MEDIUM_RISK_KEYWORDS:
        if keyword in clause_lower:
            return {
                "clause": clause[:200],
                "risk_level": "Medium",
                "reason": f"Contains conditional term: '{keyword}'"
            }

    return {
        "clause": clause[:200],
        "risk_level": "Safe",
        "reason": "No significant risk indicators detected"
    }


def analyze_risk(text: str) -> Dict:
    """Analyze full document text and return risk assessment."""
    clauses = split_into_clauses(text)
    if not clauses:
        clauses = [text[:500]]

    risk_details = [classify_clause(c) for c in clauses]

    # Determine overall score
    levels = [r["risk_level"] for r in risk_details]
    if "High" in levels:
        overall = "High"
    elif "Medium" in levels:
        overall = "Medium"
    else:
        overall = "Safe"

    logger.info(f"Analyzed {len(clauses)} clauses. Overall risk: {overall}")
    return {"risk_score": overall, "risk_details": risk_details}
