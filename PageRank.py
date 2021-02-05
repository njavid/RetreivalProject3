import json
import networkx as nx


class PageRank:
    def __init__(self, path):
        self.G = nx.Graph()
        with open(path) as json_file:
            data = json.load(json_file)
            for p in data['articles']:
                self.G.add_node(p['id'])
                self.G.add_edges_from([(p['id'], i) for i in p['references']])

    def rank(self, alpha):
        return nx.pagerank(self.G, alpha)
