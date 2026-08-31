from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class Provider:
    name: str
    healthy: bool
    cost_per_call: float
    latency_ms: int
    structured: bool = True


@dataclass(frozen=True)
class Route:
    provider: str
    reason: str
    fallback: bool


def route(
    providers: list[Provider], *, budget: float, deadline_ms: int, require_structured: bool = True
) -> Route:
    eligible = [
        p
        for p in providers
        if p.healthy
        and p.cost_per_call <= budget
        and p.latency_ms <= deadline_ms
        and (p.structured or not require_structured)
    ]
    if eligible:
        winner = min(eligible, key=lambda p: (p.cost_per_call, p.latency_ms, p.name))
        return Route(winner.name, "lowest cost provider satisfying policy", False)
    return Route("deterministic-local", "no remote provider satisfied policy", True)
