import networkx as nx

from graph_models.graph.base_graph import BaseGraph

class BarabasiAlbert(BaseGraph):
    label = "BA"
    name = "Barabasi-Albert"

    def generate(self, N, p1, p2):
        """Generates a scale-free (Barabasi-Albert) graph

         - p1: number of nodes to attach new nodes to at each step
        """
        p1 = p1*N
        p1 = int(min(N-1, max(1, p1)))
        G = nx.barabasi_albert_graph(N, p1)
        return G
