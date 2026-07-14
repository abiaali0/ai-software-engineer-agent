from fastapi import FastAPI

from app.agent import (
    create_implementation_plan,
    create_pull_request_summary,
    discover_context_files,
    extract_keywords,
)
from app.models import AnalysisResponse, IssueAnalysis, IssueRequest

app = FastAPI(
    title="AI Software Engineer Agent",
    version="0.1.0",
    description="Public portfolio reconstruction of an AI-assisted developer workflow.",
)


@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok"}


@app.post("/analyze", response_model=AnalysisResponse)
def analyze_issue(request: IssueRequest) -> AnalysisResponse:
    keywords = extract_keywords(request.title, request.body)
    context_files = discover_context_files(request.repository_path, keywords)
    plan = create_implementation_plan(request.title, keywords, context_files)
    summary = create_pull_request_summary(request.title, plan, context_files)

    return AnalysisResponse(
        issue=IssueAnalysis(
            title=request.title,
            keywords=keywords,
            summary=request.body.strip()[:300],
        ),
        context_files=context_files,
        implementation_plan=plan,
        pull_request_summary=summary,
    )
