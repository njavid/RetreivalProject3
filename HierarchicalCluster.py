from sklearn.cluster import AgglomerativeClustering


class HierarchicalCluster:
    def __init__(self, data_vectors, n):
        self.hc = AgglomerativeClustering(n_clusters=n)
        self.data = data_vectors

    def cluster(self):
        return self.hc.fit_predict(self.data)
