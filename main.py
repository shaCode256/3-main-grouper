import numpy as np
import scipy.spatial as spatial
from scipy.cluster.vq import kmeans
import editdistance

# sample vocabulary list
words = ['BRAZEMAX ESTATYS, LTD',
         'Gramkai Books',
         'Bras5emax Estates, L.T.D.',
         'BOZEMAN Enterprises',
         'BOZERMAN ENTERPRISES',
         'Nadelman, Jr',
         'John Smith',
         'PC Adelman',
         'Gramkai, Inc.',
         'Bozeman Enterprises',
         'Michele LTD',
         'Gramkat, Inc.',
         'BBAZEMAX ESTATES, LTD',
         'BOZEMAN Ent.',
         'Gramkat Estates, Inc.'
         ]

# most occurrences
def k_most_freq_num(list, k):
    freq = {}
    top_k = []
    for item in list:
        if (item in freq):
            freq[item] += 1
        else:
            freq[item] = 1
    for i in range(k):
        max_key = max(freq, key=freq.get)
        top_k.append(max_key)
        freq.pop(max_key)
    return top_k


##to check runtime on 1000 names
# with open('1000_names.txt') as file:
#      words = file.readlines()
#      words = [line.rstrip() for line in words]
original_words = words
words = [x.lower() for x in words]
words = [''.join(c for c in x if c.isalnum() or c.isspace()) for x in words]
words = [x.replace('ltd', '').replace('enterprises', '').replace(' est', '') for x in words]
words = [x.replace('enterprises', '').replace(' est', '') for x in words]

# distance matrix
word_vectors = np.array([
    [
        editdistance.eval(w, _w)
        for _w in words
    ]
    for w in words
], dtype=float)

resOfLists = []
for i in range(10):
    centroids, _ = kmeans(word_vectors, k_or_guess=5)
    word_clusters = np.argmin([
        [spatial.distance.euclidean(wv, cv) for cv in centroids]
        for wv in word_vectors
    ], 1)

    top_3 = k_most_freq_num(word_clusters, 3) #find the most common clustring labels
    # print(top_3)
    for k in top_3:
        resOfLists.append([word for i, word in enumerate(original_words) if word_clusters[i] == k])

from collections import Counter

most = Counter(tuple(i) for i in resOfLists).most_common(3)
for i in range(3):
   print(list(most[i][0]))