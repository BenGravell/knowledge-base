Accelerating Large-Scale Inference with Anisotropic Vector Quantization

Topics include Benchmarks, Vector quantization.

Quantization based techniques are the current state-of-the-art for scaling maximum inner product search to massive databases. Traditional approaches to quantization aim to minimize the reconstruction error of the database points. Based on the observation that for a given query, the database points that have the largest inner products are more relevant, we develop a family of anisotropic quantization loss functions. Under natural statistical assumptions, we show that quantization with these loss functions leads to a new variant of vector quantization that more greatly penalizes the parallel component of a datapoint's residual relative to its orthogonal component. The proposed approach achieves state-of-the-art results on the public benchmarks available at.

## Introduction

Maximum inner product search (MIPS) has become a popular paradigm for solving large scale classification and retrieval tasks. For example, in recommendation systems, user queries and documents are embedded into a dense vector space of the same dimensionality and MIPS is used to find the most relevant documents given a user query. Similarly, in extreme classification tasks, MIPS is used to predict the class label when a large number of classes, often on the order of millions or even billions are involved....

To formally define the Maximum Inner Product Search (MIPS) problem, consider a database $X = {\{ x_{i}\}}_{i = {1,2,\ldots,n}}$ with $n$ datapoints, where each datapoint $x_{i} \in {\mathbb{R}}^{d}$ in a $d$-dimensional vector space. In the MIPS setup, given a query $q \in {\mathbb{R}}^{d}$, we would like to find the datapoint $x \in X$ that has the highest inner product with $q$, i.e., we would like to identify

## Conclusion

In this paper, we propose a new quantization loss function for inner product search, which replaces traditional reconstruction error. The new loss function is weighted based on the inner product values, giving more weight to the pairs of query and database points with higher inner product values. The proposed loss function is theoretically proven and can be applied to a wide range of quantization methods, for example product and binary quantization. Our experiments show superior performance on retrieval recall and inner product value estimation compared to methods that use reconstruction error....

Figure 2: The ratio η (I (t≥T=0.2), ∥x∥=1)/(d−1) in Theorem 3.4 computed analytically as a function of d quickly approaches the limit defined in Equation.

### Definition 3.1

By setting gradient respect to $c_{j}$ to zero, we obtain the following update rule:

Exhaustively computing the exact inner product between $q$ and $n$ datapoints is often expensive and sometimes infeasible. Several techniques have been proposed in the literature based on hashing, graph search, or quantization to solve the approximate maximum inner product search problem efficiently, and the quantization based techniques have shown strong performance.

In most traditional quantization works, the objective in the quantization procedures is to minimize the reconstruction error for the database points....
