import numpy as np
import networkx as nx

from graph_models.features.base_feature import BaseFeature

class Transitivity(BaseFeature):
    name = "Transitivity"

    @staticmethod
    def run(G):
        return nx.transitivity(G)
