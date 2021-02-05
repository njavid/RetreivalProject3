from sklearn import mixture
import Plot


class GMMCluster:
    def __init__(self, data_vectors, n):
        self.gmm = mixture.GaussianMixture(n_components=n)
        self.data = data_vectors

    def cluster(self, type):
        self.gmm.fit(self.data)
        predict = self.gmm.predict(self.data)
        plot = Plot.Plot()
        plot.plot(predict, self.data, "GMM Clustering " + type)

        return predict
