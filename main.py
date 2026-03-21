 #RuntimeError Level 2 — Pydantic field conflicts with protected namespace
# Classifier: RuntimeError | pydantic_namespace | affected_file: main.py
# Fix: rename fields or add model_config to allow model_ prefix (3-4 lines)

from pydantic import BaseModel


class PredictionResult(BaseModel):
    model_id: str        # conflicts with protected namespace "model_"
    model_name: str      # conflicts with protected namespace "model_"
    model_score: float   # conflicts with protected namespace "model_"
    prediction: str


result = PredictionResult(
    model_id="gpt-4",
    model_name="GPT-4 Turbo",
    model_score=0.97,
    prediction="positive",
)
print(result)
