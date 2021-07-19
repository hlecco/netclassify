import networkx as nx

from graph_models.features.base_feature import BaseFeature

class Assortativity(BaseFeature):
    name = "Assortativity coefficient"

    @staticmethod
    def run(G):
        return nx.degree_assortativity_coefficient(G)
