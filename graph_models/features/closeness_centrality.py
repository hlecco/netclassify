import numpy as np
import networkx as nx

from graph_models.features.base_feature import BaseFeature

class ClosenessCentrality(BaseFeature):
    name = "Mean closeness centrality"

    @staticmethod
    def run(G):
        return np.mean([c for node, c in nx.closeness_centrality(G).items()])
