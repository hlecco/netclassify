import networkx as nx

from graph_models.graph.base_graph import BaseGraph

class CustomGraph(BaseGraph):
    """Loads a graph from a file"""
    label = "--"
    name = "Custom"
    def __init__(self, path):
        """Reads an edgelist

        Parameters
        ----------
        path: str
            Graph name (without .txt extension and directory)

        """
        G = nx.read_edgelist(f'networks/{path}.txt')
        G.remove_edges_from(nx.selfloop_edges(G))
        component = max(sorted(nx.connected_components(G), key=len))
        self.graph = G.subgraph(component)
        

    def generate(self, N, p1, p2):
        pass
