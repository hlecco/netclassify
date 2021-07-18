import numpy as np
import networkx as nx

from graph_models.features.base_feature import BaseFeature

class MeanDegree(BaseFeature):
    name = "Mean degree"

    @staticmethod
    def run(G):
        return np.mean([deg for node, deg in G.degree])
