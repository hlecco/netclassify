import networkx as nx

from graph_models.features.base_feature import BaseFeature

class Efficiency(BaseFeature):
    name = "Mean local efficiency"

    @staticmethod
    def run(G):
        return nx.local_efficiency(G)
