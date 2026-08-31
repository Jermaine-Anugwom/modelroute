from __future__ import annotations

import json
from dataclasses import asdict

from .core import Provider, route


def main() -> None:
    providers = [Provider("fast-model", True, 0.01, 180), Provider("cheap-model", True, 0.004, 320)]
    selected = route(providers, budget=0.02, deadline_ms=500)
    print(json.dumps({"synthetic": True, "route": asdict(selected)}, indent=2))
