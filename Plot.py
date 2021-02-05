from sklearn.decomposition import PCA
import numpy as np
import matplotlib.pyplot as plt


class Plot:
    def plot(self, clusters, X, cluster_type):
        pca = PCA(n_components=2)
        two_dim = pca.fit_transform(X)

        scatter_x = two_dim[:, 0]  # first principle component
        scatter_y = two_dim[:, 1]  # second principle component

        plt.style.use('ggplot')

        plt.scatter(scatter_x, scatter_y, c=clusters, cmap=plt.cm.Paired)
        plt.title(cluster_type)
        plt.xlabel("PCA 0")
        plt.ylabel("PCA 1")
        plt.show()
