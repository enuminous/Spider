# SPIDER

<!-- ENUMINOUS-UNIFIED-NAV:START -->
## Repository navigation

**eNuminous network:** [All public repositories](https://github.com/enuminous/EFMW/blob/main/REPOSITORY_NAVIGATION.md) · [EFMW](https://github.com/enuminous/EFMW) · [102 equations](https://github.com/enuminous/Monolithic_102_EFMW) · [Frozen Lean](https://github.com/enuminous/Monolithic-102-Zoo-Lean4) · [Zoo](https://github.com/enuminous/Tortoise) · [Papers](https://github.com/enuminous/papers) · [Quantum geometry](https://github.com/enuminous/Base888-Quantum-Geometry)

**This project:** [Repository home](https://github.com/enuminous/Spider) · [Subject index](https://github.com/enuminous/EFMW/blob/main/REPOSITORY_NAVIGATION.md#zoo-index-and-agents)

<details open>
<summary><strong>On this page</strong></summary>

- [Intended uses](#intended-uses)
- [Core signal path](#core-signal-path)
- [Flat-stack repository](#flat-stack-repository)
- [Scientific hypothesis](#scientific-hypothesis)
- [Example signals](#example-signals)
- [Baselines](#baselines)
- [Primary endpoint](#primary-endpoint)
- [Installation](#installation)
- [Run](#run)
- [Tests](#tests)
- [Minimal use](#minimal-use)
- [Freeze discipline](#freeze-discipline)
- [Negative results](#negative-results)
- [Status](#status)


</details>

**Related repositories:** [Tortoise](https://github.com/enuminous/Tortoise) · [Monolithic-Zoo-Lean4](https://github.com/enuminous/Monolithic-Zoo-Lean4) · [Monolithic-102-Zoo-Lean4](https://github.com/enuminous/Monolithic-102-Zoo-Lean4) · [Raven](https://github.com/enuminous/Raven) · [Fox](https://github.com/enuminous/Fox) · [Dolphin](https://github.com/enuminous/Dolphin) · [Cat](https://github.com/enuminous/Cat)

> **Evidence boundary:** A link between projects is navigation, not an assertion of proven equivalence, experimental validation, or shared authorship. See each repository’s own status and review notes.
<!-- ENUMINOUS-UNIFIED-NAV:END -->


**Systemic Precursor Inference through Distributed Edge Relations**

SPIDER is an EFMW-derived framework for networked systems where failure propagates across relationships.

Its narrow question is:

> Can changing edge relationships reveal a coming cascade before node-level thresholds make the failure obvious?

## Intended uses

- computer networks
- service dependency graphs
- power grids
- supply chains
- logistics networks
- fleet coordination
- sensor networks
- organizational dependencies
- distributed AI systems

## Core signal path

```text
node state
→ edge relation
→ edge stress
→ propagation asymmetry
→ concentration / dispersion
→ multiscale edge persistence
→ cascade precursor score
```

## Flat-stack repository

```text
README.md
LICENSE
CITATION.cff
pyproject.toml
requirements.txt
spider.py
features.py
baselines.py
metrics.py
freeze.py
cascade_schema.json
example_config.yaml
example_nodes.csv
example_edges.csv
example_run.py
test_spider.py
MANIFEST.sha256
```

## Scientific hypothesis

> In distributed networks, impending cascade failure may first appear as changing relations across edges rather than as extreme values at individual nodes.

SPIDER does not assume this is true.

## Example signals

- edge residual
- lagged edge disagreement
- edge stress velocity
- edge stress concentration
- graph-wide dispersion
- upstream/downstream asymmetry
- path persistence
- local-to-global divergence

## Baselines

Included:

- node-only logistic model
- graph-degree weighted node model
- edge-variance-only model
- base-rate predictor

## Primary endpoint

> Does SPIDER improve out-of-sample prediction of future cascade state over a matched node-only model?

Primary metric:

- Brier score

Secondary metrics:

- log loss
- ROC-AUC
- average precision
- performance by edge-stress regime

## Installation

```bash
python -m pip install -r requirements.txt
```

## Run

```bash
python example_run.py
```

## Tests

```bash
pytest -q
```

## Minimal use

```python
import pandas as pd
from spider import SPIDERExperiment

nodes = pd.read_csv("example_nodes.csv")
edges = pd.read_csv("example_edges.csv")

exp = SPIDERExperiment(
    time_column="time",
    target_column="cascade",
    node_columns=["n1","n2","n3","n4","n5"],
    horizons=(3,7,23),
)

print(exp.run(nodes, edges))
```

## Freeze discipline

Freeze before prospective use:

- node list
- edge list
- directionality
- lag rules
- edge relation equations
- horizons
- cascade definition
- cutoff
- baselines
- metrics
- exclusions
- seeds

Then run:

```bash
python freeze.py
```

## Negative results

If node-only models match or beat SPIDER, then edge-relational structure has not demonstrated incremental value.

## Status

Research software. Experimental. Not validated for safety-critical infrastructure operation.
