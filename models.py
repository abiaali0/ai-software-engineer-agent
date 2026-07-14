from pydantic import BaseModel, Field


class IssueRequest(BaseModel):
    title: str = Field(min_length=3, max_length=200)
    body: str = Field(min_length=1, max_length=10_000)
    repository_path: str = "."


class IssueAnalysis(BaseModel):
    title: str
    keywords: list[str]
    summary: str


class AnalysisResponse(BaseModel):
    issue: IssueAnalysis
    context_files: list[str]
    implementation_plan: list[str]
    pull_request_summary: str
