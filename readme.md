# 3-main-grouper

main-grouper.py is a Python program for finding the 3 main groups of names (strings) in a list

## Prerequisites
you need to install these libraries:
```python
numpy, scipy, editdistance

# as the codes uses:
import numpy as np
import scipy.spatial as spatial
from scipy.cluster.vq import kmeans
import editdistance

```
## Running instructions

download the code from this repository, open the main_grouper.py file in PyCharm, install the required libs and then run it.

it's already populated with the required list of 15 words. 

It'll print to the screen, as asked, the 3 main groups that can be found in the list.

Another option is to run this Python program through bash/ cmd:

```bash
python main_grouper.py
```

## Usage

```python
# input: 
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

# outputs to screen:
# ['Gramkai Books', 'Gramkai, Inc.', 'Gramkat, Inc.', 'Gramkat Estates, Inc.']
# ['BOZEMAN Enterprises', 'BOZERMAN ENTERPRISES', 'Bozeman Enterprises', 'BOZEMAN Ent.']
# ['BRAZEMAX ESTATYS, LTD', 'Bras5emax Estates, L.T.D.', 'BBAZEMAX ESTATES, LTD']
```
## Explanation of implementation

The program performs cleaning on the data of names, e.g removing all chars which are not alphanumeric | space.

Computes an edit distance matrix for the word list, by calaulating pairwise Levenshtein Distance between names.

It uses scipy.K-means clustering on the distance matrix. 

It caches the 3-largest-groups by the clustering.

It repeats the clustering and caching process 20 times, and picks the most common results, which is our desired one, as seen in the example above.


## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.


## License
[MIT](https://choosealicense.com/licenses/mit/)
