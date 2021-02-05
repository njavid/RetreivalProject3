import PreProcess, Kmaens, Evaluation, GMMCluster, HierarchicalCluster, WebCrawler, PageRank
import numpy as np

if __name__ == '__main__':
    # arr = {1:2,3:4,5:1}
    # print(max(arr.values()))
    preProcess = PreProcess.PreProcess()
    eval = Evaluation.Evaluation()
    #
    for n in range(40, 60, 2):
       kmeans = Kmaens.Kmeans(n, preProcess.vectorize_tf_idf())
       print(eval.purity(n, kmeans.y, preProcess.labels))



    # data_vectors_tf_idf = preProcess.vectorize_tf_idf()
    # data_vectors_wv = preProcess.word2wec()
    #optimal_n = len(set(preProcess.labels))

    # Gaussian Mixture Model
    # print("Gaussian Mixture Model(tf-idf):")
    # gmm = GMMCluster.GMMCluster(data_vectors_tf_idf[:100], 5)
    # cluster = gmm.cluster("tf-idf")
    # print("ARI= ", eval.adjusted_rand_index(preProcess.labels[:100], cluster))
    # print("NMI= ", eval.normalized_mutual_information(preProcess.labels[:100], cluster))
    #
    # print("Gaussian Mixture Model(vw):")
    # gmm = GMMCluster.GMMCluster(data_vectors_wv[:100], 5)
    # cluster = gmm.cluster("wv")
    # print("ARI= ", eval.adjusted_rand_index(preProcess.labels[:100], cluster))
    # print("NMI= ", eval.normalized_mutual_information(preProcess.labels[:100], cluster))


    # Hierarchical Clustering
    # print("Hierarchical Clustering(tf-idf):")
    # hc = HierarchicalCluster.HierarchicalCluster(data_vectors_tf_idf, optimal_n)
    # cluster = hc.cluster("tf-idf")
    # print("ARI= ", eval.adjusted_rand_index(preProcess.labels, cluster))
    # print("NMI= ", eval.normalized_mutual_information(preProcess.labels, cluster))
    #
    # print("Hierarchical Clustering(vw):")
    # hc = HierarchicalCluster.HierarchicalCluster(data_vectors_wv, optimal_n)
    # cluster = hc.cluster("wv")
    # print("ARI= ", eval.adjusted_rand_index(preProcess.labels, cluster))
    # print("NMI= ", eval.normalized_mutual_information(preProcess.labels, cluster))

    # Web Crawler Part
    # wc = WebCrawler.WebCrawler()
    # wc.crawl(["https://academic.microsoft.com/paper/2981549002",
    #           "https://academic.microsoft.com/paper/3105081694",
    #           "https://academic.microsoft.com/paper/2950893734"], 100)

    # pr = PageRank.PageRank('crawl_output.txt')
    # print(pr.rank(0.4))
