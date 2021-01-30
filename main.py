import PreProcess, Kmaens , Evaluation


if __name__ == '__main__':

    # arr = {1:2,3:4,5:1}
    # print(max(arr.values()))
    preProcess = PreProcess.PreProcess()
    eval = Evaluation.Evaluation()

    for n in range(40,60,2):
        kmeans = Kmaens.Kmeans(n,preProcess.vectorize_tf_idf())
        print(eval.purity(n,kmeans.y,preProcess.labels))

    # preProcess.word2wec()

