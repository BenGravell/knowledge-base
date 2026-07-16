<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Cover Trees for Nearest Neighbor

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

We present a tree data structure for fast nearest neighbor operations in general n-point metric spaces (where the data set consists of n points). The data structure requires O(n) space regardless of the metric's structure yet maintains all performance properties of a navigating net. If the point set has a bounded expansion constant c, which is a measure of the intrinsic dimensionality, as defined , the cover tree data structure can be constructed in O (c6n log n) time. Furthermore, nearest neighbor queries require time only logarithmic in n, in particular O (c12 log n) time. Our experimental results show speedups over the brute force search varying between one and several orders of magnitude on natural machine learning datasets.
