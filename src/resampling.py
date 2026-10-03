from imblearn.over_sampling import RandomOverSampler, SMOTE
from imblearn.under_sampling import RandomUnderSampler


def make_sampler(name: str, random_state: int = 42):
    name = name.lower()
    if name == "over":
        return RandomOverSampler(random_state=random_state)
    if name == "under":
        return RandomUnderSampler(random_state=random_state)
    if name == "smote":
        return SMOTE(random_state=random_state)
    raise ValueError(f"Unknown sampler: {name}")
