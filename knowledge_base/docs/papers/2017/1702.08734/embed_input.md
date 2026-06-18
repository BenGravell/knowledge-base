Billion-scale Similarity Search with GPUs

Topics include Graphs, Nearest neighbors, Datasets, Accuracy.

Similarity search finds application in specialized database systems handling complex data such as images or videos, which are typically represented by high-dimensional features and require specific indexing structures. This paper tackles the problem of better utilizing GPUs for this task. While GPUs excel at data-parallel tasks, prior approaches are bottlenecked by algorithms that expose less parallelism, such as k-min selection, or make poor use of the memory hierarchy. We propose a design for k-selection that operates at up to 55% of theoretical peak performance, enabling a nearest neighbor implementation that is 8.5x faster than prior GPU state of the art. We apply it in different similarity search scenarios, by proposing optimized design for brute-force, approximate and compressed-domain search based on product quantization. In all these setups, we outperform the state of the art by large margins. Our implementation enables the construction of a high accuracy k-NN graph on 95 million images from the Yfcc100M dataset in 35 minutes, and of a graph connecting 1 billion vectors in less than 12 hours on 4 Maxwell Titan X GPUs....

## Introduction

Images and videos constitute a new massive source of data for indexing and search. Extensive metadata for this content is often not available. Search and interpretation of this and other human-generated content, like text, is difficult and important. A variety of machine learning and deep learning algorithms are being used to interpret and classify these complex, real-world entities. Popular examples include the text representation known as word2vec, representations of images by convolutional neural networks, and image descriptors for instance search....

In this context, searching by numerical similarity rather than via structured relations is more suitable. This could be to find the most similar content to a picture, or to find the vectors that have the highest response to a linear classifier on all vectors of a collection.

This work enables applications that needed complex approximate algorithms before. For example, the approaches presented here make it possible to do exact $k$-means clustering or to compute the $k$-NN graph with simple brute-force approaches in less time than a CPU (or a cluster of them) would take to do this approximately.

GPU hardware is now very common on scientific workstations, due to their popularity for machine learning algorithms. We believe that our work further demonstrates their interest for database applications. Along with this work, we are publishing a carefully engineered implementation of this paper's algorithms, so that these GPUs can now also be used for efficient similarity search.

### Output

We use an in-register sorting primitive as a building block. Sorting networks are commonly used on SIMD architectures, as they exploit vector parallelism. They are easily implemented on the GPU, and we build sorting networks with lane-stride register arrays.

A single warp could be dedicated to $k$-selection of each $t_{q}$ set of lists, which could result in low parallelism. We introduce a two-pass $k$-selection, reducing $t_{q} \times \tau \times {\max_{i}{|\mathcal{I}_{i}|}}$ to $t_{q} \times f \times k$ partial results for some subdivision factor $f$. This is reduced again via $k$-selection to the final $t_{q} \times k$ results.

One of the most expensive operations to be performed on large collections is to compute a $k$-NN graph....
