from sklearn.cluster import AgglomerativeClustering
import Plot


class HierarchicalCluster:
    def __init__(self, data_vectors, n):
        self.hc = AgglomerativeClustering(n_clusters=n)
        self.data = data_vectors

    def cluster(self, type):
        predict = self.hc.fit_predict(self.data)
        plot = Plot.Plot()
        plot.plot(predict, self.data, "Hierarchical Clustering "+type)
        return predict
