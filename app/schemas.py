from pydantic import BaseModel, Field

class Transaction(BaseModel):
    features: dict[str, float]

class Prediction(BaseModel):
    fraud_probability: float = Field(ge=0.0, le=1.0)
    risk_score: int = Field(ge=0, le=1000)
    risk_band: str
