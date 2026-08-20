import pandas as pd
from features import build_spider_features
from spider import SPIDERExperiment

NODES = ["n1","n2","n3","n4","n5"]

def test_features():
    nodes = pd.read_csv("example_nodes.csv")
    edges = pd.read_csv("example_edges.csv")
    sf = build_spider_features(nodes, edges, NODES)
    assert len(sf) == len(nodes)
    assert "spider_cascade_score" in sf.columns
    assert sf["spider_cascade_score"].between(0,1).all()

def test_experiment_runs():
    nodes = pd.read_csv("example_nodes.csv")
    edges = pd.read_csv("example_edges.csv")
    exp = SPIDERExperiment(
        time_column="time",
        target_column="cascade",
        node_columns=NODES,
    )
    out = exp.run(nodes, edges)
    assert "results" in out
    assert "spider" in out["results"]
    assert "node_only" in out["results"]
