import numpy as np
import networkx as nx

from graph_models.features.base_feature import BaseFeature

class BetweennessCentrality(BaseFeature):
    name = "Mean betweenness centrality"

    @staticmethod
    def run(G):
        return np.mean([c for node, c in nx.betweenness_centrality(G).items()])
