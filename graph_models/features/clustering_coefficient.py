import numpy as np
import networkx as nx

from graph_models.features.base_feature import BaseFeature

class ClusteringCoefficient(BaseFeature):
    name = "Mean clustering coefficient"

    @staticmethod
    def run(G):
        return np.mean(list(nx.clustering(G).values()))
