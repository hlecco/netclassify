# netclassify

This is a tool for classifying networks according to some popular models and finding out what is the best fit.

## Running

Make a python virtual environment with ```python3 -m venv .venv```, activate it with
```source .venv/bin/activate``` and install the requirements with ```pip install -r requirements```

The ```main.py``` script will train a KNN model and try to guess the classes for some networks in
the ```/networks``` directory.

All networks must be in "edgelist" format, that is, each line must have two space-separated nodes.
To register a custom network, put it in ```/networks``` folder and add them to the main script.

## Features

Features are defined inside ```graph_models.features``` package.
More features may be added and registered in ```graph_models.graph.base_graph.BaseGraph```
so they will be used. Some are commented out because they take too long to calculate.

## Models

Different models must inherit the BaseGraph class.
