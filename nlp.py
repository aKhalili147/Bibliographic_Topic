from data import Data
import numpy as np 
from operator import itemgetter

class NLP:

    def __init__(self, corpus):
        self.corpus = corpus

    
    # create occurence matrix
    def occurenceMatrix(self):

        occurence = dict()
        for i, text in enumerate(self.corpus):
            for word in text:
                word_ = (''.join(list(c for c in word if c.isalpha()))).lower()
                if word_:
                    if word_ in occurence.keys():
                        occurence[word_][i] += 1
                    else:
                        occurence[word_] = np.zeros((len(self.corpus),))
                        occurence[word_][i] = 1

        return occurence


    def addUp_method(self,O_arr):
        occMatrix = self.occurenceMatrix()
        add_O = []
        sum_all = 0
        for i,word in enumerate(O_arr):
            sum=0
            for fr in word:
                sum+=fr
                sum_all+=fr
            add_O.append([i,sum])

        sorted_addO = sorted(add_O,key=itemgetter(1),reverse=True)
        # pprint(sorted_addO)
        return sorted_addO