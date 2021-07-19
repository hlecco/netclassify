from graph_models import CustomGraph
from classifier.model_classifier import ModelClassifier

if __name__ == '__main__':
    graphs_to_test = [
        'bio_celegansneural',
        'bio_ecolitranscription',
        'bio_malariagenes',
        'social_contact',
        'social_facebookfriends',
        'social_copenhagen',
        'tech_jdk',
        'tech_linux',
        'tech_power'
    ]

    cls = ModelClassifier()
    cls.train(200, N_min=50, N_max=1000)

    for graph in graphs_to_test:
        G = CustomGraph(graph)
        predict = cls.predict(G)
        print(f'Model for graph {graph} is {predict}')

