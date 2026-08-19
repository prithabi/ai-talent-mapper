from fastapi import FastAPI
from pydantic import BaseModel
from typing import Dict

from scoring.scoring_engine import generate_talent_profile


app = FastAPI(
    title="AI Talent Mapper API",
    description="AI-powered natural talent and intelligence mapping system",
    version="0.1.0"
)


class AssessmentRequest(BaseModel):
    answers: Dict[str, str]


@app.get("/")
def home():
    return {
        "project": "AI Talent Mapper",
        "status": "running",
        "message": "Find Right Talent. For Right Role. For Right Impact."
    }


@app.get("/health")
def health_check():
    return {
        "status": "healthy"
    }


@app.post("/assess")
def assess_candidate(request: AssessmentRequest):

    profile = generate_talent_profile(
        request.answers
    )

    return {
        "success": True,
        "result": profile
    }
