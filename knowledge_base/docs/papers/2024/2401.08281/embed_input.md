The Faiss Library

Topics include Benchmarks, Optimization, Faiss library.

Vector databases typically manage large collections of embedding vectors. Currently, AI applications are growing rapidly, and so is the number of embeddings that need to be stored and indexed. The Faiss library is dedicated to vector similarity search, a core functionality of vector databases. Faiss is a toolkit of indexing methods and related primitives used to search, cluster, compress and transform vectors. This paper describes the trade-off space of vector search and the design principles of Faiss in terms of structure, approach to optimization and interfacing. We benchmark key features of the library and discuss a few selected applications to highlight its broad applicability.

## Introduction

The emergence of deep learning has induced a shift in how complex data is stored and searched, noticeably by the development of *embeddings*. Embeddings are vector representations, typically produced by a neural network, that map (embed) the input media item into a vector space, where the locality encodes the semantics of the input. Embeddings are extracted from various forms of media: words, text, images, users and items for recommendation \[\]. They can even encode object relations, for instance multi-modal text-image or text-audio relations.

Embeddings are employed as an intermediate representation for further processing, e.g. self-supervised image embeddings are input to shallow supervised image classifiers. They are also leveraged as a pretext task for self-supervision \[\]. In fact, embeddings are a compact intermediate representation that can be re-used for several purposes.

## Conclusion

Throughout the years, Faiss continuously expanded its focus to include the most relevant vector indexing techniques from research. We continue doing this to include novel quantization techniques \[\], better hardware support for some indexes \[\] and new indexing forms, such as associative vector memories for transformer architectures.

### The local search quantizer (LSQ)

Faiss supports various vector codecs: these are methods to compress vectors so that they take up less memory. A compression method $C:{{\mathbb{R}}^{d}\rightarrow{\{ 1,\ldots,K\}}}$, a.k.a. a quantizer, converts a continuous multi-dimensional vector to an integer. This integer is equivalent to a bit string of code size $\lceil{\log_{2}K}\rceil$. The decoder $D:{{\{ 1,\ldots,K\}}\rightarrow{\mathbb{R}}^{d}}$ reconstructs an approximation of the vector from the integer. The decoder can only reconstruct a finite number, $K$, of distinct vectors.

Figure shows that encoding residuals is beneficial for shorter codes. For larger codes, the contribution of the residual is less important. Indeed, as the original data is 96-dimensional, it can be compressed to 64 bytes relatively accurately. Note that using higher $K_{IVF}$ also improves the accuracy of the quantizer with residual encoding....
