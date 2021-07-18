import numpy as np
import networkx as nx
from networkx.algorithms.community import greedy_modularity_communities

from graph_models.features.base_feature import BaseFeature

class Modularity(BaseFeature):
    name = "Mean community size"

    @staticmethod
    def run(G):
        sizes = [len(community) for community in greedy_modularity_communities(G)]
        return np.mean(sizes)
