<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Approximate Nearest Neighbors

Topics include Approximate nearest neighbors, Locality-sensitive hashing, High-dimensional search, Random projections, Similarity search, Data structures, Sublinear algorithms.

<!-- chunk {"id": "summary-0002", "role": "summary", "section": "Summary", "weight": 2.0} -->

Introduces locality-sensitive hashing as an algorithmic route to approximate nearest-neighbor search in high-dimensional Euclidean spaces. The paper gives theoretical sublinear-query data structures and shows that randomized hashing can beat tree-based search where dimensionality makes exact nearest-neighbor indexing ineffective.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

The nearest neighbor problem is the follolving: Given a set of n points P = (PI,...,p,} in some metric space X, preprocess P so as to efficiently answer queries which require finding bhe point in P closest to a query point q E X. We focus on the particularly interesting case of the d-dimensional Euclidean space where X = Wd under some Zp norm. Despite decades of effort, t,he current solutions are far from saabisfactory; in fact, for large d, in theory or in practice, they provide litt,le improvement over the brute-force algorithm which compares the query point to each data point. Of late, t,here has been some interest in the approximate newest neighbors problem, which is: Find a point p E P that is an c-approximate nearest neighbor of the query q in t,hat for all p' E P, d(p, q) < (1 + e)d(p', q).

<!-- chunk {"id": "abstract-0004", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

We present two algorithmic results for the approximate version t,hat significantly improve the known bounds: (a) preprocessing cost polynomial in n and d, and a truly sublinear query t.ime (for 6 > 1); and, (b) query time polynomial in log-n and d, and only a mildly exponential preprocessing cost* O(n) x 0(1/~)~. Furt.her, applying a classical geometric lemma on random projections (for which we give a simpler proof), we obtain t.he first known algorithm with polynomial preprocessing and query t.ime polynomial in d and log n. Unfortunately, for small E, the latter is a purely theoretical result since bhe e?rponent depends on l/e. Experimental resuits indicate that our tit algori&m offers orders of magnitude improvement on running times over real data sets. Its key ingredient is the notion of locality-sensitive hashing which may be of independent interest; here, we give applications to information ret,rieval, pattern recognition, dynamic closest-pairs, and fast clustering algorithms.
