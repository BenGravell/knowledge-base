The Faiss Library

Topics include Benchmarks, Optimization, Faiss library.

Vector databases typically manage large collections of embedding vectors. Currently, AI applications are growing rapidly, and so is the number of embeddings that need to be stored and indexed. The Faiss library is dedicated to vector similarity search, a core functionality of vector databases. Faiss is a toolkit of indexing methods and related primitives used to search, cluster, compress and transform vectors. This paper describes the trade-off space of vector search and the design principles of Faiss in terms of structure, approach to optimization and interfacing. We benchmark key features of the library and discuss a few selected applications to highlight its broad applicability.

## Introduction

The emergence of deep learning has induced a shift in how complex data is stored and searched, noticeably by the development of *embeddings*. Embeddings are vector representations, typically produced by a neural network, that map (embed) the input media item into a vector space, where the locality encodes the semantics of the input. Embeddings are extracted from various forms of media: words, text, images, users and items for recommendation. They can even encode object relations, for instance multi-modal text-image or text-audio relations.

Embeddings are employed as an intermediate representation for further processing, e.g. self-supervised image embeddings are input to shallow supervised image classifiers. They are also leveraged as a pretext task for self-supervision. In fact, embeddings are a compact intermediate representation that can be re-used for several purposes.

In this paper, we consider embeddings used directly to compare media items. The embedding extractor is designed so that the distance between embeddings reflects the similarity between their corresponding media. As a result, conducting neighborhood search in this vector space offers a direct implementation of similarity search between media items.

The basic structure of Faiss is an *index* that can have multiple implementations described in this paper. An index can store a number of *database vectors* that are progressively added to it. At search time, a *query vector* is submitted to the index. The index returns the database vector that is closest to the query vector w.r.t. the Euclidean distance.

## Conclusion

Throughout the years, Faiss continuously expanded its focus to include the most relevant vector indexing techniques from research. We continue doing this to include novel quantization techniques, better hardware support for some indexes and new indexing forms, such as associative vector memories for transformer architectures.
