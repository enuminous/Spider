# SPIDER

<!-- ENUMINOUS-NETWORK:START -->
**eNuminous network:** [All repositories](https://enuminous.github.io/EFMW/repositories.html) · [EFMW](https://enuminous.github.io/EFMW/) · [102 equations](https://github.com/enuminous/Monolithic_102_EFMW) · [165 triplets](https://enuminous.github.io/FieldSpace/) · [Zoo](https://enuminous.github.io/Tortoise/) · [Lean](https://enuminous.github.io/Aristotle-102-Monolithic-Lean/) · [Engine](https://enuminous.github.io/Archimedes-Engine/) · [Papers](https://enuminous.github.io/medium/papers-essays-index.html) · [Audit](https://github.com/enuminous/EFMW_Post156_Zoo_Audit/blob/main/portfolio/INTERLOCK_AUDIT.md)

[Repository](https://github.com/enuminous/Spider) · This repository is linked through its source; GitHub Pages is not enabled.
<!-- ENUMINOUS-NETWORK:END -->

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
