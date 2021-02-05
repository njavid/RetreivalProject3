import PreProcess, Kmaens, Evaluation, GMMCluster, HierarchicalCluster, WebCrawler

if __name__ == '__main__':
    # arr = {1:2,3:4,5:1}
    # print(max(arr.values()))
    preProcess = PreProcess.PreProcess()
    eval = Evaluation.Evaluation()

    for n in range(40, 60, 2):
       kmeans = Kmaens.Kmeans(n, preProcess.vectorize_tf_idf())
       print(eval.purity(n, kmeans.y, preProcess.labels))

    #data_vectors = preProcess.vectorize_tf_idf()
    # Gaussian Mixture Model
    # gmm = GMMCluster.GMMCluster(data_vectors, 10)
    # print(gmm.cluster())

    # Hierarchical Clustering
    # hc = HierarchicalCluster.HierarchicalCluster(data_vectors, 5)
    # print(hc.cluster())


    # wc = WebCrawler.WebCrawler()
    # wc.crowl(["https://academic.microsoft.com/paper/2981549002",
    #           "https://academic.microsoft.com/paper/3105081694",
    #           "https://academic.microsoft.com/paper/2950893734"], 100)
