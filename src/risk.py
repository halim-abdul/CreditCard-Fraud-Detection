def risk_band(probability: float) -> str:
    if probability >= 0.80:
        return "critical"
    if probability >= 0.50:
        return "high"
    if probability >= 0.20:
        return "medium"
    return "low"


def risk_score(probability: float) -> int:
    return int(round(max(0.0, min(1.0, probability)) * 1000))
