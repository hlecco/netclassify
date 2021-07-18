import random

import numpy as np
import pandas as pd
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import RobustScaler
from sklearn.impute import KNNImputer
from tqdm import tqdm

import graph_models

class ModelClassifier:
    available_models = [
        graph_models.RandomGraph,
        graph_models.BarabasiAlbert,
        graph_models.WattsStrogatz,
        graph_models.ZipfConfiguration,
        graph_models.Geometric
    ]

    def __init__(self, k=5):
        """Initializes the classifier

        Parameters
        ----------
        k: int, default 5
            Number of neighbors
        """
        self.k = k
        self.classifier = KNeighborsClassifier(n_neighbors=self.k)
        self.scaler = RobustScaler()
        self.labels = {
            model.label: i
            for i, model in enumerate(self.available_models)
        }
        self.inverted_labels = {
            value: key
            for key, value in self.labels.items()
            for i, model in enumerate(self.available_models)
        }
        self.names = {
            model.label: model.name
            for model in self.available_models
        }


    def generate_train_set(self, N, N_min=50, N_max=1000):
        """Generates a training of graphs from every available model

        Parameters
        ----------
        N: int
            Train set size
        N_min: int, default 50
            Minimum size of network
        N_max: int default 1000
            Maximum size of network

        Returns
        -------
        iterator
            Iterator of graphs

        """
        n_models = len(self.available_models)
        N_each = max(1, N // n_models)

        for _ in range(N_each):
            for model in self.available_models:
                yield model(random.randint(N_min, N_max))

    def train(self, N, N_min=50, N_max=100):
        """Trains the model

        Parameters
        ----------
        N: int
            Train set size
        N_min: int, default 50
            Minimum size of network
        N_max: int default 1000
            Maximum size of network

        Returns
        -------
        self

        """
        train_set = self.generate_train_set(N, N_min=N_min, N_max=N_max)

        values, labels = self._features_labels_from_graphs(train_set, size=N)

        values = self.scaler.fit_transform(values)
        self.classifier.fit(values, labels)

        return self

    def validate(self, N, N_min=50, N_max=1000, fold=10):
        """Validates the model

        Parameters
        ----------
        N: int
            Validation set size
        N_min: int, default 200
            Minimum size of network
        N_max: int default 5000
            Maximum size of network
        fold: int, default 10:
            How many subset to break into to validate

        Returns
        -------
        self
            This object

        """
        N = (N // fold) * fold
        subset = N // fold
        test_set = self.generate_train_set(N, N_min=N_min, N_max=N_max)

        values, labels = self._features_labels_from_graphs(test_set, size=N)

        values = self.scaler.transform(values)

        scores = [
            sum(labels[start:end] == np.array(self.classifier.predict(values[start:end])))
            for start, end in zip(range(0, N, subset),
                                  range(subset, N+subset, subset))
        ]

        return np.mean(scores)/subset

    def predict(self, graph):
        """Predicts an appropriate model for graph

        Parameters
        ----------
        graph: graph_models.BaseGraph subclass
            Graph to test

        Returns
        -------
        str
            Name of predicted class
        """
        values, labels = self._features_labels_from_graphs([graph])
        values = self.scaler.transform(values)
        predict = self.classifier.predict(values)[0]

        predict_label = self.inverted_labels[predict]
        predict_name = self.names[predict_label]

        return predict_name

    def _features_labels_from_graphs(self, graphs, size=None):
        """Returns feature values and labels for each graph in an iterator

        Nans and infs will be replaced by nearest neighbor values

        Parameters
        ----------
        graphs: iterator
            Iterator of graphs to generate features
        size: int, default None
            If size is provided, it will print a progress bar

        Returns
        -------
        numpy.array, numpy.array 
            Array (matrix) of features and array of labels

        """
        values = []
        labels = []

        if not size:
            for i, x in enumerate(graphs):
                values.append(x.features)
                labels.append(self.labels.get(x.label, '--'))
        else:
            with tqdm(total=size) as pbar:
                for i, x in enumerate(graphs):
                    values.append(x.features)
                    labels.append(self.labels.get(x.label, '--'))
                    pbar.update(1)


        values = pd.DataFrame(
            values
        )
        values = values.replace([-np.inf, np.inf],
                                [np.nan, np.nan]).values
        imputer = KNNImputer(n_neighbors=self.k)
        values = imputer.fit_transform(values)

        return values, np.array(labels)
