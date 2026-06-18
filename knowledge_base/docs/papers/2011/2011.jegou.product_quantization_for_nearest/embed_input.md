<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Product Quantization for Nearest Neighbor Search

Topics include Approximate nearest neighbors, Product quantization, Vector quantization, Image retrieval, Inverted indexes, Compact codes, Large-scale search.

<!-- chunk {"id": "summary-0002", "role": "summary", "section": "Summary", "weight": 2.0} -->

Introduces product quantization for approximate nearest-neighbor search by splitting vectors into subspaces and quantizing each subspace separately. Its asymmetric distance computation and inverted-file integration made billion-scale descriptor search practical with compact codes and strong accuracy-memory tradeoffs.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

This paper introduces a product quantization-based approach for approximate nearest neighbor search. The idea is to decompose the space into a Cartesian product of low-dimensional subspaces and to quantize each subspace separately. A vector is represented by a short code composed of its subspace quantization indices. The euclidean distance between two vectors can be efficiently estimated from their codes. An asymmetric version increases precision, as it computes the approximate distance between a vector and a code. Experimental results show that our approach searches for nearest neighbors efficiently, in particular in combination with an inverted file system. Results for SIFT and GIST image descriptors show excellent search accuracy, outperforming three state-of-the-art approaches. The scalability of our approach is validated on a data set of two billion vectors.
