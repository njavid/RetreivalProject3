import nltk, math, json
from hazm import *
from gensim.models import Word2Vec


def prepare(content):
    # normalize
    normalizer = Normalizer()
    content = normalizer.normalize(content)

    # tokenizing and removing punctuation marks
    tokenizer = nltk.RegexpTokenizer(r"\w+")
    tokens = tokenizer.tokenize(content)

    # stemming
    stemmer = Stemmer()
    res = [stemmer.stem(x) for x in tokens]

    return res


class PreProcess:

    def __init__(self):

        file = open("hamshahri" + ".json", "r", encoding='utf-8')
        data = file.read()
        data = json.loads(data)
        self.data = data
        file.close()
        self.N = len(data)
        self.all_terms = {}
        self.set_all_terms()
        self.labels = [self.data[i]['tags'][0] for i in range(len(data))]

    def vectorize_tf_idf(self):
        vectors = []
        x = []

        for i in range(0, len(self.data)):
            x.append(prepare(self.data[i]['title'] + ' ' + self.data[i]['summary']))

        for doc in x:
            tf = {}
            for term in doc:
                if term in tf:
                    tf[term] += 1
                else:
                    tf[term] = 1
            vector = []
            for term in self.all_terms.keys():
                if term not in tf:
                    vector.append(0)
                else:
                    vector.append(tf[term] * math.log(self.N / self.all_terms[term], 10))
            vectors.append(vector)
        # self.vectors = vectors
        return vectors

    def set_all_terms(self):
        x = []

        for i in range(0, len(self.data)):
            x.append(prepare(self.data[i]['title'] + ' ' + self.data[i]['summary']))

        for doc in x:
            tf = {}
            for term in doc:
                if term not in tf:
                    if term not in self.all_terms:
                        self.all_terms[term] = 1
                    else:
                        self.all_terms[term] += 1
                    tf[term] = 1

    def word2wec(self):
        x = []

        for i in range(0, len(self.data)):
            x.append(prepare(self.data[i]['title'] + ' ' + self.data[i]['summary']))

        word2vec = Word2Vec(x, min_count=2)
        # print(word2vec)
