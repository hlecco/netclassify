from abc import ABC, abstractmethod

import numpy as np

class BaseFeature(ABC):
    """Base class for features"""
    @property
    @abstractmethod
    def name(self):
        pass

    @abstractmethod
    def run(graph):
        """Calculates a feature for a given graph, must be overridden

        Parameters
        ----------
        graph: networkx.Graph
            Graph to calculate feature from

        Returns
        -------
        int or float
            Feaure value

        """
        pass

    def calculate(self, graph):
        """Calculates a feature for a given graph

        Parameters
        ----------
        graph: networkx.Graph
            Graph to calculate feature from

        Returns
        -------
        int or float
            Feaure value

        """
        try:
            feature = self.run(graph)
            if np.isnan(feature):
                raise ValueError
        except Exception as e:
            print(f'Failed to calculate {self.name}, results may be innacurate')
            print(e)
            feature = 0
        return feature
