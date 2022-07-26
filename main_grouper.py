import numpy as np
import scipy.spatial as spatial
from scipy.cluster.vq import kmeans
import editdistance
from collections import Counter

# finding k most frequent labels
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

#cleaning the data
def data_cleaning(strings):
    strings = [x.lower() for x in strings]
    strings = [''.join(c for c in x if c.isalnum() or c.isspace()) for x in strings]
    strings = [x.replace('ltd', '').replace('enterprises', '').replace(' est', '') for x in strings]
    return strings

# strings list
input_strings = ['BRAZEMAX ESTATYS, LTD',
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

#to check runtime on 1000 names
# with open('1000_names.txt') as file:
#      words = file.readlines()
#      words = [line.rstrip() for line in words]

#dealing with invalid input
if len(input_strings)< 5:
    raise Exception("This clustering program requires at least five words as input")

strings_processed = data_cleaning(input_strings)

# distance matrix
distance_matrix = np.array([
    [
        editdistance.eval(str1, str2)
        for str1 in strings_processed
    ]
    for str2 in strings_processed
], dtype=float)

results_list = []

#to repeat the k means and caching results process 10 times
for i in range(10):
    centroids, _ = kmeans(distance_matrix, k_or_guess=5)
    string_clusters = np.argmin([
        [spatial.distance.euclidean(wv, cv) for cv in centroids]
        for wv in distance_matrix
    ], 1)

    top_3_labels = k_most_freq_num(string_clusters, 3) #find the k most common clustring labels]
    for label in top_3_labels:
        results_list.append([string for i, string in enumerate(input_strings) if string_clusters[i] == label]) #append the 3 biggest lists

most = Counter(tuple(i) for i in results_list).most_common(3) #take the most common 3 biggest lists
for i in range(3):
   print(list(most[i][0]))