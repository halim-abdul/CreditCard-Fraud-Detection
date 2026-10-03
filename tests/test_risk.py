from src.risk import risk_band, risk_score


def test_risk_score_and_band():
    assert risk_score(0.75) == 750
    assert risk_band(0.75) == "high"
