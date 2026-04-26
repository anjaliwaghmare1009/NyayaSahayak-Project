"""API routes for document upload and analysis."""
import os
import uuid
import logging
from fastapi import APIRouter, UploadFile, File, HTTPException
from app.services.pdf_service import extract_text_from_pdf
from app.controllers.analyze_controller import perform_analysis
from app.models.schemas import UploadResponse, AnalyzeRequest, AnalyzeResponse

logger = logging.getLogger(__name__)
router = APIRouter()

UPLOAD_DIR = "app/uploads"
MAX_FILE_SIZE = 5 * 1024 * 1024  # 5 MB


@router.post("/upload", response_model=UploadResponse, tags=["Document"])
async def upload_pdf(file: UploadFile = File(...)):
    """
    Upload a PDF document (max 5MB).
    Extracts text and returns a preview.
    """
    # Validate file type
    if not file.filename or not file.filename.lower().endswith(".pdf"):
        raise HTTPException(status_code=400, detail="Only PDF files are accepted.")

    # Validate file size
    contents = await file.read()
    if len(contents) > MAX_FILE_SIZE:
        raise HTTPException(status_code=400, detail="File size exceeds 5MB limit.")

    # Save file
    unique_name = f"{uuid.uuid4().hex}_{file.filename}"
    file_path = os.path.join(UPLOAD_DIR, unique_name)

    try:
        with open(file_path, "wb") as f:
            f.write(contents)

        # Extract text
        result = extract_text_from_pdf(file_path)

        return UploadResponse(
            file_name=file.filename,
            full_text=result["full_text"],   # ✅ change here
            total_characters=result["total_characters"],
            total_pages=result["total_pages"],
           )
    except ValueError as e:
        raise HTTPException(status_code=422, detail=str(e))
    except Exception as e:
        logger.error(f"Upload processing failed: {e}")
        raise HTTPException(status_code=500, detail="Failed to process the uploaded PDF.")


@router.post("/analyze", response_model=AnalyzeResponse, tags=["Analysis"])
async def analyze_document(request: AnalyzeRequest):
    """
    Analyze legal document text.
    Returns risk assessment, relevant case laws, and simplified explanations.
    """
    try:
        result = perform_analysis(request.text)
        return result
    except Exception as e:
        logger.error(f"Analysis failed: {e}")
        raise HTTPException(status_code=500, detail="Document analysis failed.")
