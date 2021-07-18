from abc import ABC, abstractmethod
from random import random

import networkx as nx
import pandas as pd

from graph_models import features

class BaseGraph(ABC):
    available_features = [
        features.ShannonEntropy,
        features.ClusteringCoefficient,
        features.SecondMoment,
        features.MeanDegree,
        features.DegreeCentralityCorrelation,
        features.ClosenessCentrality,
        features.BetweennessCentrality,
        features.Modularity
    ]

    """Abstraction layer for networkx graphs"""
    def __init__(self, N, p1=None, p2=None):
        """Generates a graph according to some models

        Parameters
        ----------
        N: int
            Number of nodes
        p1: float, default None
            Some parameter, between 0 and 1,
            indicated by subclass documentation
            If not specified, value will be random
        p2: float, default None
            Same as p1

        """
        p1 = p1 if p1 else random()
        p2 = p2 if p2 else random()
        self.graph = self.generate(N, p1, p2)

    @abstractmethod
    def generate(self, N, p1, p2):
        """Class specific function to generate a graph, must be overridden

        Parameters
        ----------
        N: int
            Number of nodes
        p1: float
            Some parameter, between 0 and 1,
            indicated by subclass documentation
        p2: float
            Same as p1

        Returns
        -------
        networkx graph

        """
        pass

    @property
    @abstractmethod
    def label(self):
        pass

    @property
    @abstractmethod
    def name(self):
        pass

    @property
    def features(self):
        """Features DataFrame"""
        return self._compute_features()

    def show(self):
        """Plots graph using spring layout"""
        nx.draw_spring(self.graph)

    def _compute_features(self):
        """Calculates every available feature for the graph

        Returns
        -------
        dict
            Feauture names and values

        """
        return {
            feature.name: feature().calculate(self.graph)
            for feature in self.available_features
        }

