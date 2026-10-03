from dataclasses import dataclass

@dataclass(frozen=True)
class ProjectConfig:
    target: str = "Class"
    random_state: int = 42
    test_size: float = 0.20
    valid_size: float = 0.20
    threshold: float = 0.50

CONFIG = ProjectConfig()
