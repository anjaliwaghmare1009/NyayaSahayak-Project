"""Pydantic models for request/response validation."""
from pydantic import BaseModel, Field
from typing import List, Optional


class UploadResponse(BaseModel):
    file_name: str
    full_text: str   # ✅ changed
    total_characters: int
    total_pages: int


class AnalyzeRequest(BaseModel):
    text: str = Field(..., min_length=1, description="Legal document text to analyze")


class ClauseRisk(BaseModel):
    clause: str
    risk_level: str = Field(..., description="High | Medium | Safe")
    reason: str


class CaseLaw(BaseModel):
    title: str
    summary: str
    relevance: Optional[str] = None


class SimplifiedExplanation(BaseModel):
    marathi: str
    hindi: str


class AnalyzeResponse(BaseModel):
    risk_score: str = Field(..., description="Overall risk: High | Medium | Safe")
    risk_details: List[ClauseRisk]
    case_laws: List[CaseLaw]
    simplified_explanation: SimplifiedExplanation
