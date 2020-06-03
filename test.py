from pprint import pprint
import numpy as np
import matplotlib.pyplot as plt
from operator import itemgetter
import math
import collections
from data import Data
from nlp import NLP


txt1 = Data("text1.txt")
txt2 = Data("text2.txt")
txt3 = Data("text3.txt")

txt = [txt1, txt2, txt3] # samples of Data class

data1 = txt1.mod_txt()
data2 = txt2.mod_txt()
data3 = txt3.mod_txt()

corpus = [data1, data2, data3]

nlp = NLP(corpus)
occMatrix = nlp.occurenceMatrix()
# pprint(occMatrix)


words = sorted(list(occMatrix.keys()))
O = np.zeros((len(words), len(corpus)))
for i, w in enumerate(words):
    O[i, :] = occMatrix[w]

# method 1: consider only most frequent words in each text 
keys_mfw = [] # list of most frequent words
mfw_size = int(0.1*len(O))
# keys_lfw = [] # list of least frequent words

# colormap = ['r','g','b']
# for i in range(len(corpus)):
# wd_sorted = sorted(O, key=itemgetter(0), reverse=True)
# for k in range(100):
#     for fr in ocurrence.items():
#         if collections.Counter(fr[1]) == collections.Counter(wd_sorted[k]):
#             if fr[0] not in keys_mfw:
#                 keys_mfw.append(fr[0])

    # X = []
    # Y = []
    # for j, wd in enumerate(wd_sorted):
    #     X.append(j)
    #     Y.append(wd[i])
    #     # X.append(math.log(j+1))
    #     # Y.append(math.log(wd[i]+1))

    # plt.scatter(X,Y,c=colormap[i])

# plt.xlabel('rank')
# plt.ylabel('frequency')
# plt.show()


# #method 2: adding up frequencies

# add_O = []
# sum_all = 0
# for i,word in enumerate(O):
#     sum=0
#     for fr in word:
#         sum+=fr
#         sum_all+=fr
#     add_O.append([i,sum])

# sorted_addO = sorted(add_O,key=itemgetter(1),reverse=True)
# # pprint(sorted_addO)


sorted_addO = nlp.addUp_method(O)

X = []
Y = []
for k in range(50):
    for fr in occMatrix.items():
        if collections.Counter(fr[1]) == collections.Counter(O[sorted_addO[k][0]]):
            if fr[0] not in keys_mfw:
                keys_mfw.append(fr[0])
                # Y.append(math.log(add_O[sorted_addO[k][0]][1]))
                # X.append(k)
# print(len(X))
# print(len(Y))

# plt.scatter(X,Y)
# plt.xlabel('rank')
# plt.ylabel('frequency')
# plt.show()

print(keys_mfw)


# pprint(O)