import json
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Dict
from fastapi.responses import StreamingResponse, FileResponse
from reporting.pdf_report import generate_candidate_report
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
class AssessAndReportRequest(BaseModel):
    candidate_name: str
    answers: Dict[str, int]

class TeamSynergyRequest(BaseModel):
    code_a: str
    code_b: str
class CandidateReportRequest(BaseModel):
    result: Dict



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
@app.get("/demo", include_in_schema=False)
def demo_page():
    return FileResponse(
        "demo/index.html",
        media_type="text/html",
    )
@app.get("/questions", include_in_schema=False)
def get_questions():
    with open("data/questions.json", encoding="utf-8") as file:
        assessment_data = json.load(file)

    public_questions = [
        {
            "id": question["id"],
            "text_hi": question["text_hi"],
            "text_en": question["text_en"],
        }
        for question in assessment_data["questions"]
    ]

    return {"questions": public_questions}
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
@app.post("/candidate-report")
def create_candidate_report(request: CandidateReportRequest):
    pdf_buffer = generate_candidate_report(request.result)

    return StreamingResponse(
        pdf_buffer,
        media_type="application/pdf",
        headers={
            "Content-Disposition": (
                "attachment; "
                "filename=ai_talent_mapper_candidate_report.pdf"
            )
        },
)
@app.post("/assess-and-report")
def assess_and_create_report(request: AssessAndReportRequest):
    try:
        profile = generate_talent_profile(request.answers)

        role_compatibility = calculate_role_compatibility(
            profile["score_percentages"]
        )

        profile["role_compatibility"] = role_compatibility
        profile["candidate_name"] = request.candidate_name

        pdf_buffer = generate_candidate_report(profile)

        return StreamingResponse(
            pdf_buffer,
            media_type="application/pdf",
            headers={
                "Content-Disposition": (
                    "attachment; "
                    "filename=ai_talent_mapper_complete_report.pdf"
                )
            },
        )

    except ValueError as error:
        raise HTTPException(
            status_code=400,
            detail=str(error),
        )

    except Exception:
        raise HTTPException(
            status_code=500,
            detail="Unable to assess candidate and generate report",
        )
