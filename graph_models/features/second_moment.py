import numpy as np

from graph_models.features.base_feature import BaseFeature

class SecondMoment(BaseFeature):
    name = "Second moment of degree distribution"

    @staticmethod
    def run(G):
        degrees = np.array([deg for (node, deg) in G.degree])
        return np.sum(degrees**2)/len(degrees)
