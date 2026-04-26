"""NyayaSahayak - AI-Powered Legal Document Analysis Platform"""
import os
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routes.analyze import router as analyze_router

app = FastAPI(
    title="NyayaSahayak",
    description="AI-powered legal document analysis platform for Indian law",
    version="1.0.0",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

os.makedirs("app/uploads", exist_ok=True)

app.include_router(analyze_router)

@app.get("/")
async def root():
    return {"message": "NyayaSahayak API is running", "docs": "/docs"}
