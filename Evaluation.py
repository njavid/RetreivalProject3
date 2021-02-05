from sklearn.metrics.cluster import adjusted_rand_score
from sklearn.metrics.cluster import normalized_mutual_info_score


class Evaluation:

    def purity(self, n, y, label):

        sum = 0
        for i in range(n):
            dict = {}
            for j in range(len(y)):
                if y[j] == i:
                    if label[j] in dict:
                        dict[label[j]] += 1
                    else:
                        dict[label[j]] = 1

            sum += y.count(i) / len(y) * max(dict.values()) / y.count(i)

        return sum

    def adjusted_rand_index(self, labels_true, labels_pred):
        return adjusted_rand_score(labels_true, labels_pred)

    def normalized_mutual_information(self, labels_true, labels_pred):
        return normalized_mutual_info_score(labels_true, labels_pred)
