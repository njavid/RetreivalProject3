
class Evaluation:

    def purity(self,n,y,label):

        sum = 0
        for i in range(n):
            dict = {}
            for j in range(len(y)):
                if y[j] == i:
                    if label[j] in dict:
                        dict[label[j]]+=1
                    else:
                        dict[label[j]]=1

            sum += y.count(i)/len(y)*max(dict.values())/y.count(i)
            
        return sum

