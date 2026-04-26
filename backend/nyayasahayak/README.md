# NyayaSahayak - AI-Powered Legal Document Analysis

## Setup
```bash
pip install -r requirements.txt
```

## Run
```bash
uvicorn app.main:app --reload
```

## API Docs
Open http://127.0.0.1:8000/docs

## Endpoints
- `POST /upload` — Upload PDF (≤5MB), returns extracted text preview
- `POST /analyze` — Analyze legal text, returns risk score, case laws, explanations
