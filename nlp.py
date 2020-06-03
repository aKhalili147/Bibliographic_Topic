from data import Data
import numpy as np 

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


    def addUp_method(self):
        occMatrix = self.occurenceMatrix()
        occSorted = dict()
        for i, fr in occMatrix:
            