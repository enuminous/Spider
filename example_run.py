import json
import pandas as pd
from spider import SPIDERExperiment

nodes = pd.read_csv("example_nodes.csv")
edges = pd.read_csv("example_edges.csv")

exp = SPIDERExperiment(
    time_column="time",
    target_column="cascade",
    node_columns=["n1","n2","n3","n4","n5"],
    horizons=(3,7,23),
    random_state=23,
)

result = exp.run(nodes, edges)
print(json.dumps(result, indent=2))
