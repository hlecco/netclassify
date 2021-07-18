import random

import networkx as nx
import numpy as np

from graph_models.graph.base_graph import BaseGraph

class ZipfConfiguration(BaseGraph):
    label = "ZI"
    name = "Power-law Configuration"

    def generate(self, N, p1, p2):
        """Generates a graph (configuration model) according to Zipf's law distribution

         - p1: power law coefficient
         - p2: unused

        """
        p1 = min(1, max(p1, 0.01))
        p1 = 2 + 3*p1
        seq = np.random.zipf(p1, N) #Zipf distribution

        if(sum(seq)%2 != 0): # the sum of stubs have to be even
            pos = random.randint(0, len(seq)-1)
            seq[pos] = seq[pos]+ 1

        G=nx.configuration_model(seq)

        Gcc = sorted(nx.connected_components(G), key=len, reverse=True)
        G = G.subgraph(Gcc[0])
        G = nx.Graph(G)
        G.remove_edges_from(nx.selfloop_edges(G))

        return G
