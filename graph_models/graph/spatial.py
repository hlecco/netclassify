import networkx as nx
import random

from graph_models.graph.base_graph import BaseGraph

class Geometric(BaseGraph):
    label = "GE"
    name = "Geometric"

    def generate(self, N, p1, p2):
        """Generates a geometric random graph

         - p1: radius to attach nodes
         - p2: probability that a node will be attached
        """
        p1 = min(1, max(0, p1))
        p2 = min(1, max(0, p2))

        G = nx.Graph()
        G.add_nodes_from(range(N))
        positions = [
            (random.random(), random.random())
            for _ in range(N)
        ]
        dist_max = p1**2
        for node in range(N):
            for neighbor in range(N):
                if node == neighbor:
                    continue
                distance = (positions[node][0] - positions[neighbor][0])**2\
                           + (positions[node][1] - positions[neighbor][1])**2
                if distance < dist_max:
                    if random.random() < p2:
                        G.add_edge(node, neighbor)
        return G
