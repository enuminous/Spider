import numpy as np
import pandas as pd

EPS = 1e-8

def robust_z(s, window=23):
    s = s.astype(float)
    med = s.rolling(window, min_periods=3).median()
    mad = (s-med).abs().rolling(window, min_periods=3).median()
    return ((s-med)/(1.4826*mad+EPS)).replace([np.inf,-np.inf], np.nan).fillna(0.0)

def build_spider_features(nodes, edges, node_columns, horizons=(3,7,23)):
    x = nodes[node_columns].astype(float).copy()
    out = pd.DataFrame(index=nodes.index)

    for c in node_columns:
        out[f"{c}__z"] = robust_z(x[c], max(horizons))
        out[f"{c}__dx"] = x[c].diff().fillna(0.0)

    edge_stress_cols = []
    edge_velocity_cols = []

    for _, row in edges.iterrows():
        a = row["source"]
        b = row["target"]
        lag = int(row.get("lag", 1))
        weight = float(row.get("weight", 1.0))

        if a not in x.columns or b not in x.columns:
            continue

        upstream = x[a]
        downstream = x[b].shift(lag)

        relation = upstream - downstream
        expected = relation.rolling(max(horizons), min_periods=3).median()
        residual = relation - expected
        mad = residual.abs().rolling(max(horizons), min_periods=3).median()

        stress_name = f"edge__{a}__{b}__stress"
        vel_name = f"edge__{a}__{b}__velocity"
        asym_name = f"edge__{a}__{b}__asymmetry"

        stress = (residual.abs()/(1.4826*mad+EPS)).replace([np.inf,-np.inf], np.nan).fillna(0.0)
        out[stress_name] = weight * stress
        out[vel_name] = out[stress_name].diff().fillna(0.0)
        out[asym_name] = (upstream.diff() - downstream.diff()).abs().fillna(0.0)

        edge_stress_cols.append(stress_name)
        edge_velocity_cols.append(vel_name)

    if edge_stress_cols:
        stress_df = out[edge_stress_cols]
        out["edge_stress_mean"] = stress_df.mean(axis=1)
        out["edge_stress_max"] = stress_df.max(axis=1)
        out["edge_stress_dispersion"] = stress_df.std(axis=1).fillna(0.0)

        total = stress_df.sum(axis=1).replace(0, np.nan)
        shares = stress_df.div(total, axis=0).fillna(0.0)
        out["edge_stress_concentration"] = (shares**2).sum(axis=1)
    else:
        out["edge_stress_mean"] = 0.0
        out["edge_stress_max"] = 0.0
        out["edge_stress_dispersion"] = 0.0
        out["edge_stress_concentration"] = 0.0

    if edge_velocity_cols:
        out["edge_velocity_mean"] = out[edge_velocity_cols].mean(axis=1)
        out["edge_velocity_positive"] = out[edge_velocity_cols].clip(lower=0).mean(axis=1)
    else:
        out["edge_velocity_mean"] = 0.0
        out["edge_velocity_positive"] = 0.0

    node_anomaly_cols = [f"{c}__z" for c in node_columns]
    out["node_anomaly_mean"] = out[node_anomaly_cols].abs().mean(axis=1)
    out["local_global_divergence"] = (
        out["edge_stress_mean"].rank(pct=True)
        - out["node_anomaly_mean"].rank(pct=True)
    ).abs()

    for h in horizons:
        out[f"stress_mean_{h}"] = out["edge_stress_mean"].rolling(h, min_periods=1).mean()
        out[f"stress_max_{h}"] = out["edge_stress_max"].rolling(h, min_periods=1).mean()
        out[f"velocity_mean_{h}"] = out["edge_velocity_positive"].rolling(h, min_periods=1).mean()
        out[f"divergence_mean_{h}"] = out["local_global_divergence"].rolling(h, min_periods=1).mean()

    components = [
        out["edge_stress_mean"],
        out["edge_stress_max"],
        out["edge_stress_dispersion"],
        out["edge_stress_concentration"],
        out["edge_velocity_positive"],
        out["local_global_divergence"],
    ]

    for h in horizons:
        components.extend([
            out[f"stress_mean_{h}"],
            out[f"stress_max_{h}"],
            out[f"velocity_mean_{h}"],
            out[f"divergence_mean_{h}"],
        ])

    ranked = pd.concat(components, axis=1).rank(pct=True)
    out["spider_cascade_score"] = ranked.mean(axis=1).fillna(0.0)

    return out.replace([np.inf,-np.inf], np.nan).fillna(0.0)
