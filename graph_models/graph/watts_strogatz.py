import networkx as nx

from graph_models.graph.base_graph import BaseGraph

class WattsStrogatz(BaseGraph):
    label = "WS"
    name = "Watts-Strogatz"

    def generate(self, N, p1, p2):
        """Generates a small-world (Watts-Strogatz) graph

         - p1: mean degree divided by N
         - p2: probability to rewire each edge divided by N

        """
        p1 = p1*N
        p1 = int(min(N, max(1, p1)))
        p2 = p2*N
        p2 = int(min(N, max(1, p2)))
        G = nx.watts_strogatz_graph(N, p1, p2)
        return G
