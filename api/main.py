from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional
from analyzer.ast_parser import analyze_python_code
from analyzer.ml_model import analyze_with_ml
from analyzer.nlp_analysis import analyze_with_nlp

app = FastAPI(title="Code Quality Analyzer")

class CodeRequest(BaseModel):
    language: str
    code: str

class AnalysisResponse(BaseModel):
    functions: Optional[list]
    variables: Optional[list]
    ml_analysis: str
    nlp_analysis: str

@app.post("/analyze", response_model=AnalysisResponse)
async def analyze_code(request: CodeRequest):
    if request.language.lower() == "python":
        ast_result = analyze_python_code(request.code)
    else:
        raise HTTPException(status_code=400, detail="Language not supported yet")

    ml_result = analyze_with_ml(request.code)
    nlp_result = analyze_with_nlp(request.code)

    return AnalysisResponse(
        functions=ast_result.get("functions"),
        variables=ast_result.get("variables"),
        ml_analysis=ml_result,
        nlp_analysis=nlp_result
    )
