from graph_models.features.base_feature import BaseFeature

class Size(BaseFeature):
    name = "Graph size"

    @staticmethod
    def run(G):
        return len(G)
