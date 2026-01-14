import json
from fastapi import FastAPI
from pydantic import BaseModel
from app.scoring import compute_dimension_score, compute_global_score
from app.interpretation import interpret_dimension, detect_profiles

app = FastAPI(title="Innovation Diagnostic API")

with open("app/schema.json", "r", encoding="utf-8") as f:
    SCHEMA = json.load(f)


class DiagnosticInput(BaseModel):
    answers: dict


@app.get("/")
def healthcheck():
    return {"status": "ok"}


@app.post("/diagnostic")
def run_diagnostic(data: DiagnosticInput):
    dimension_scores = {}
    dimension_interpretations = {}

    for dim in SCHEMA["dimensions"]:
        dim_id = dim["id"]
        qids = [q["id"] for q in dim["questions"]]

        score = compute_dimension_score(data.answers, qids)
        dimension_scores[dim_id] = score
        dimension_interpretations[dim_id] = interpret_dimension(score)

    global_score = compute_global_score(dimension_scores)
    profiles = detect_profiles(dimension_scores)

    return {
        "global_score": global_score,
        "dimension_scores": dimension_scores,
        "dimension_interpretations": dimension_interpretations,
        "profiles": profiles
    }
