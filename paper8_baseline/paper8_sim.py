"""
Paper 8 – 3Sync baseline simulator (simplified).

Provides a baseline for comparison with Paper 9.
No stabilization function, no invariant pull, no epistemic validation.
"""

from dataclasses import dataclass
from typing import Dict, Any, List, Tuple


@dataclass
class Paper8Result:
    num_agents: int
    steps: int
    history: List[List[Tuple[float, float, float]]]
    metadata: Dict[str, Any]


def _init_agents() -> List[Tuple[float, float, float]]:
    return [
        (10.0, 20.0, 30.0),
        (20.0, 30.0, 40.0),
        (30.0, 40.0, 50.0),
    ]


def run_paper8_baseline(steps: int = 10) -> Paper8Result:
    agents = _init_agents()
    history: List[List[Tuple[float, float, float]]] = [[] for _ in agents]

    for t in range(steps):
        new_agents = []
        for idx, (s1, s2, s3) in enumerate(agents):
            # Simple averaging (3Sync-style convergence, no invariant)
            avg = (s1 + s2 + s3) / 3.0
            s1n = (s1 + avg) / 2
            s2n = (s2 + avg) / 2
            s3n = (s3 + avg) / 2
            new_agents.append((s1n, s2n, s3n))
            history[idx].append((s1n, s2n, s3n))
        agents = new_agents

    return Paper8Result(
        num_agents=len(agents),
        steps=steps,
        history=history,
        metadata={},
    )
