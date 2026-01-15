from fastapi import FastAPI
from pydantic import BaseModel
from app.scoring import calculer_scores
from app.interpretation import interpreter_score_global, interpreter_dimensions
import json, os

app = FastAPI(title="API Diagnostic Innovation")

BASE_DIR = os.path.dirname(__file__)
SCHEMA_PATH = os.path.join(BASE_DIR, "schema.json")

with open(SCHEMA_PATH, encoding="utf-8") as f:
    SCHEMA = json.load(f)

class RequeteDiagnostic(BaseModel):
    reponses: dict

@app.post("/diagnostic")
def lancer_diagnostic(payload: RequeteDiagnostic):
    scores = calculer_scores(SCHEMA, payload.reponses)

    return {
        "scores": scores,
        "interpretation": {
            "globale": interpreter_score_global(scores["global"]),
            "par_dimension": interpreter_dimensions(scores["dimensions"])
        },
        "radar": [
            {"dimension": d, "score": s}
            for d, s in scores["dimensions"].items()
        ]
    }
