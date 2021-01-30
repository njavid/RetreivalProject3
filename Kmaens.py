from sklearn.cluster import KMeans
# import numpy as np

class Kmeans:

    def __init__(self,n,X):
        kmeans = KMeans(n_clusters=n, random_state=0).fit(X)
        # print(kmeans.labels_.tolist())
        self.y = kmeans.labels_.tolist()
