import pytest

from modelroute.core import Provider, route


def p(name="a", healthy=True, cost=0.1, latency=100, structured=True):
    return Provider(name, healthy, cost, latency, structured)


def test_selects_eligible():
    assert route([p()], budget=0.2, deadline_ms=200).provider == "a"


def test_rejects_unhealthy():
    assert route([p(healthy=False)], budget=0.2, deadline_ms=200).fallback


def test_rejects_cost():
    assert route([p(cost=0.3)], budget=0.2, deadline_ms=200).fallback


def test_rejects_latency():
    assert route([p(latency=300)], budget=0.2, deadline_ms=200).fallback


def test_rejects_schema():
    assert route([p(structured=False)], budget=0.2, deadline_ms=200).fallback


def test_can_allow_unstructured():
    assert not route(
        [p(structured=False)], budget=0.2, deadline_ms=200, require_structured=False
    ).fallback


@pytest.mark.parametrize("cost,latency", [(0.01, 500), (0.5, 50), (0.5, 500)])
def test_policy_combinations(cost, latency):
    assert route([p(cost=cost, latency=latency)], budget=0.2, deadline_ms=200).fallback


def test_prefers_cost():
    assert (
        route(
            [p("fast", cost=0.2, latency=10), p("cheap", cost=0.1, latency=100)],
            budget=0.3,
            deadline_ms=200,
        ).provider
        == "cheap"
    )


def test_tie_is_deterministic():
    assert route([p("b"), p("a")], budget=0.2, deadline_ms=200).provider == "a"
