"""PDF text extraction service using pdfplumber."""
import logging
import pdfplumber

logger = logging.getLogger(__name__)


def extract_text_from_pdf(file_path: str) -> dict:
    """
    Extract text from a PDF file.
    Returns dict with full_text, preview, char count, and page count.
    """
    try:
        full_text = ""
        page_count = 0
        with pdfplumber.open(file_path) as pdf:
            page_count = len(pdf.pages)
            for page in pdf.pages:
                page_text = page.extract_text()
                if page_text:
                    full_text += page_text + "\n"

        full_text = full_text.strip()
        if not full_text:
            raise ValueError("No text could be extracted from the PDF.")

        return {
            "full_text": full_text,
            "preview": full_text[:500],
            "total_characters": len(full_text),
            "total_pages": page_count,
        }
    except Exception as e:
        logger.error(f"PDF extraction failed: {e}")
        raise
