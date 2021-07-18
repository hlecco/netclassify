import networkx as nx

from graph_models.graph.base_graph import BaseGraph

class RandomGraph(BaseGraph):
    label = "ER"
    name = "Erdos-Rényi"

    def generate(self, N, p1, p2):
        """Generates a random (Erdos-Renyi) graph

         - p1: p in G_n,p
         - p2: unused

        """
        p1 = min(1, max(p1, 0))
        G = nx.fast_gnp_random_graph(N, p1)
        return G

