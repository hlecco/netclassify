import numpy as np
import networkx as nx
from scipy import stats

from graph_models.features.base_feature import BaseFeature

class DegreeCentralityCorrelation(BaseFeature):
    name = "Correlation between degree and centrality"

    @staticmethod
    def run(G):
        centrality = np.array(list(nx.betweenness_centrality(G).values()))
        degrees = degrees = np.array([deg for (node, deg) in G.degree])

        corr = stats.pearsonr(degrees, centrality)[0]
        return corr
