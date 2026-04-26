"""Controller orchestrating the document analysis pipeline."""
import logging
from app.services.risk_service import analyze_risk
from app.services.rag_service import retrieve_case_laws
from app.services.llm_service import generate_explanation
from app.models.schemas import AnalyzeResponse, ClauseRisk, CaseLaw, SimplifiedExplanation

logger = logging.getLogger(__name__)


def perform_analysis(text: str) -> AnalyzeResponse:
    """
    Full analysis pipeline:
    1. Risk classification of clauses
    2. Relevant case law retrieval (RAG)
    3. Simplified explanation in Marathi & Hindi (LLM)
    """
    logger.info("Starting document analysis pipeline")

    # Step 1: Risk analysis
    risk_result = analyze_risk(text)

    # Step 2: Case law retrieval
    case_laws_raw = retrieve_case_laws(text)

    # Step 3: Simplified explanation
    explanation = generate_explanation(text, risk_result["risk_score"])

    # Build response
    response = AnalyzeResponse(
        risk_score=risk_result["risk_score"],
        risk_details=[ClauseRisk(**r) for r in risk_result["risk_details"]],
        case_laws=[CaseLaw(**c) for c in case_laws_raw],
        simplified_explanation=SimplifiedExplanation(**explanation),
    )

    logger.info("Analysis pipeline completed successfully")
    return response
