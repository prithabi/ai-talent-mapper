from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Dict

from scoring.scoring_engine import generate_talent_profile
from scoring.role_compatibility import calculate_role_compatibility
from scoring.team_synergy import calculate_team_synergy
app = FastAPI(
    title="AI Talent Mapper API",
    description="Talent and behavioral pattern assessment API for Vidhishastra Foundation",
    version="0.2.0"
)


class AssessmentRequest(BaseModel):
    answers: Dict[str, int]


class TeamSynergyRequest(BaseModel):
    code_a: str
    code_b: str




@app.get("/")
def home():
    return {
        "project": "AI Talent Mapper",
        "organization": "Vidhishastra Foundation",
        "status": "running",
        "version": "0.2.0",
        "message": (
            "Find Right Talent. "
            "For Right Role. "
            "For Right Impact."
        )
    }


@app.get("/health")
def health_check():
    return {
        "status": "healthy",
        "service": "AI Talent Mapper API"
    }


@app.post("/assess")
def assess_candidate(request: AssessmentRequest):
    try:
        profile = generate_talent_profile(
            request.answers
        )

        role_compatibility = calculate_role_compatibility(
            profile["score_percentages"]
        )

        profile["role_compatibility"] = role_compatibility

        return {
            "success": True,
            "result": profile
        }

    except ValueError as error:
        raise HTTPException(
            status_code=400,
            detail=str(error)
        )

  @app.post("/team-synergy")
def team_synergy(request: TeamSynergyRequest):
    try:
        result = calculate_team_synergy(
            request.code_a,
            request.code_b
        )

        return {
            "success": True,
            "result": result
        }

    except ValueError as error:
        raise HTTPException(
            status_code=400,
            detail=str(error)
        )

    except Exception:
        raise HTTPException(
            status_code=500,
            detail="Unable to calculate team synergy."
        )  
  
