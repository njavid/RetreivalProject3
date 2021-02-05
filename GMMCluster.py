from sklearn import mixture


class GMMCluster:
    def __init__(self, data_vectors, n):
        self.gmm = mixture.GaussianMixture(n_components=n)
        self.data = data_vectors

    def cluster(self):
        self.gmm.fit(self.data)
        return self.gmm.predict(self.data)
