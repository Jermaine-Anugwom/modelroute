# ModelRoute

**Provider-neutral routing with budgets, deadlines, and deterministic fallback.**

> All people, organizations, records, measurements, and outcomes in this
> repository are synthetic.

## The operational problem

Production workflows need predictable behavior when a model is slow, unavailable, expensive, or malformed.

## The proof

Task policies, structured output validation, retry budgets, circuit state, and local fallbacks.

## Why this is forward deployed

The project begins with the operator's decision, uncertainty, failure cost,
integration boundary, and handoff—not with a model demo. It makes policy and
evidence inspectable, preserves human authority for consequential cases, and
remains useful when the optional model layer is unavailable.

## Architecture

```mermaid
flowchart LR
  A[Structured task policy] --> B[Provider health]
  B --> C[Budget gate]
  C --> D[Deadline gate]
  D --> E[Capability gate]
  E --> F[Lowest-cost eligible route]
  E -->|none| G[Deterministic local fallback]
```

## Quickstart

```bash
python3.12 -m venv .venv
source .venv/bin/activate
python -m pip install -e '.[dev]'
pytest -q
modelroute
```

No API key or network connection is required.

## Evaluation and limitations

Run `pytest -q` for the reproducible evaluation. The fixture set is deliberately
synthetic and cannot establish production performance. A real deployment would
require operator observation, representative data, policy review, privacy review,
security testing, and a monitored rollout.

## Project documents

- [Field discovery and handoff](FIELD_NOTES.md)
- [Security boundaries](SECURITY.md)
- [Operating runbook](RUNBOOK.md)
- [Development provenance](DEVELOPMENT.md)
- [Release history](CHANGELOG.md)

## Topics

`llm-routing`, `structured-outputs`, `reliability`, `python`, `llmops`
