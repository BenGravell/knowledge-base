Accelerating Large-Scale Inference with Anisotropic Vector Quantization

Topics include Benchmarks, Vector quantization.

Quantization based techniques are the current state-of-the-art for scaling maximum inner product search to massive databases. Traditional approaches to quantization aim to minimize the reconstruction error of the database points. Based on the observation that for a given query, the database points that have the largest inner products are more relevant, we develop a family of anisotropic quantization loss functions. Under natural statistical assumptions, we show that quantization with these loss functions leads to a new variant of vector quantization that more greatly penalizes the parallel component of a datapoint's residual relative to its orthogonal component. The proposed approach achieves state-of-the-art results on the public benchmarks available .

## Introduction

Maximum inner product search (MIPS) has become a popular paradigm for solving large scale classification and retrieval tasks. For example, in recommendation systems, user queries and documents are embedded into a dense vector space of the same dimensionality and MIPS is used to find the most relevant documents given a user query. Similarly, in extreme classification tasks, MIPS is used to predict the class label when a large number of classes, often on the order of millions or even billions are involved.

To formally define the Maximum Inner Product Search (MIPS) problem, consider a database $X = {\{ x_{i}\}}_{i = {1,2,\ldots,n}}$ with $n$ datapoints, where each datapoint $x_{i} \in {\mathbb{R}}^{d}$ in a $d$-dimensional vector space. In the MIPS setup, given a query $q \in {\mathbb{R}}^{d}$, we would like to find the datapoint $x \in X$ that has the highest inner product with $q$, i.e., we would like to identify

In most traditional quantization works, the objective in the quantization procedures is to minimize the reconstruction error for the database points. We show this is a suboptimal loss function for MIPS. This is because for a given query, quantization error for database points that score higher, or have larger inner products, is more important. Using this intuition, we propose a new family of score-aware quantization loss functions and apply it to multiple quantization techniques.

We propose the score-aware quantization loss function. The proposed loss can work under any weighting function of the inner product and regardless of whether the datapoints vary in norm.

## Conclusion

In this paper, we propose a new quantization loss function for inner product search, which replaces traditional reconstruction error. The new loss function is weighted based on the inner product values, giving more weight to the pairs of query and database points with higher inner product values. The proposed loss function is theoretically proven and can be applied to a wide range of quantization methods, for example product and binary quantization. Our experiments show superior performance on retrieval recall and inner product value estimation compared to methods that use reconstruction error.
