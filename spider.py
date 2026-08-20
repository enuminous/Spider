from dataclasses import dataclass
import pandas as pd

from features import build_spider_features
from baselines import LogisticModel, BaseRateModel, degree_weighted_nodes, edge_variance_feature
from metrics import binary_metrics, stratify

@dataclass
class SPIDERExperiment:
    time_column: str
    target_column: str
    node_columns: list
    horizons: tuple = (3,7,23)
    train_fraction: float = 0.65
    random_state: int = 23

    def run(self, nodes, edges):
        nodes = nodes.sort_values(self.time_column).reset_index(drop=True).copy()
        cut = max(20, int(len(nodes)*self.train_fraction))
        y = nodes[self.target_column].astype(int).to_numpy()

        sf = build_spider_features(nodes, edges, self.node_columns, self.horizons)
        raw = nodes[self.node_columns].astype(float).ffill().fillna(0.0)
        full = pd.concat([raw, sf], axis=1).fillna(0.0)

        degree = degree_weighted_nodes(nodes, edges, self.node_columns)
        edgevar = edge_variance_feature(nodes, edges, self.node_columns)

        models = {
            "spider": (LogisticModel(self.random_state), full),
            "node_only": (LogisticModel(self.random_state), raw),
            "degree_weighted": (LogisticModel(self.random_state), degree),
            "edge_variance_only": (LogisticModel(self.random_state), edgevar),
            "base_rate": (BaseRateModel(), raw),
        }

        results = {}
        for name, (model, X) in models.items():
            model.fit(X.iloc[:cut], y[:cut])
            p = model.predict_proba(X.iloc[cut:])
            results[name] = {
                "overall": binary_metrics(y[cut:], p),
                "by_edge_stress": stratify(
                    y[cut:], p, sf["edge_stress_mean"].to_numpy()[cut:]
                )
            }

        return {
            "n_total": len(nodes),
            "train_n": cut,
            "test_n": len(nodes)-cut,
            "results": results,
            "primary_delta_brier_node_minus_spider": (
                results["node_only"]["overall"]["brier"]
                - results["spider"]["overall"]["brier"]
            ),
            "interpretation": (
                "Positive delta favors SPIDER over the matched node-only model. "
                "Check whether any gain is concentrated in high-edge-stress regimes."
            )
        }
