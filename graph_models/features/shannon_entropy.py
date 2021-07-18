import numpy as np

from graph_models.features.base_feature import BaseFeature

class ShannonEntropy(BaseFeature):
    name = "Shannon Entropy"

    @staticmethod
    def run(G):
        degrees = [deg for (node, deg) in G.degree]
        distr = np.array([degrees.count(x) for x in set(degrees)])
        nonzero = distr[distr.nonzero()]/len(G)
        entropy = -sum(nonzero * np.log2(nonzero))
        return entropy
