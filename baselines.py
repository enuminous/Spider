import numpy as np
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import RobustScaler

class LogisticModel:
    def __init__(self, random_state=23):
        self.scaler = RobustScaler()
        self.model = LogisticRegression(max_iter=4000, random_state=random_state)
        self.constant_ = None

    def fit(self, X, y):
        y = np.asarray(y, dtype=int)
        if len(np.unique(y)) < 2:
            self.constant_ = float(y.mean()) if len(y) else 0.0
            return self
        self.scaler.fit(X)
        self.model.fit(self.scaler.transform(X), y)
        return self

    def predict_proba(self, X):
        if self.constant_ is not None:
            return np.full(len(X), self.constant_)
        return self.model.predict_proba(self.scaler.transform(X))[:,1]

class BaseRateModel:
    def fit(self, X, y):
        self.p_ = float(np.mean(y))
        return self

    def predict_proba(self, X):
        return np.full(len(X), self.p_, dtype=float)

def degree_weighted_nodes(nodes, edges, node_columns):
    degree = {c: 0.0 for c in node_columns}
    for _, row in edges.iterrows():
        if row["source"] in degree:
            degree[row["source"]] += float(row.get("weight",1.0))
        if row["target"] in degree:
            degree[row["target"]] += float(row.get("weight",1.0))
    total = sum(degree.values()) or 1.0
    weighted = sum(nodes[c].astype(float).fillna(0.0)*(degree[c]/total) for c in node_columns)
    return pd.DataFrame({"degree_weighted_state": weighted})

def edge_variance_feature(nodes, edges, node_columns):
    vals = []
    for _, row in edges.iterrows():
        a, b = row["source"], row["target"]
        lag = int(row.get("lag",1))
        if a in node_columns and b in node_columns:
            vals.append((nodes[a].astype(float)-nodes[b].astype(float).shift(lag)).abs())
    if not vals:
        return pd.DataFrame({"edge_variance": np.zeros(len(nodes))})
    mat = pd.concat(vals, axis=1)
    return pd.DataFrame({"edge_variance": mat.var(axis=1).fillna(0.0)})
