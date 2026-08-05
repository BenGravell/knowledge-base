<!-- arxiv-full-text:v1 {"arxiv_id": "1908.10396", "source": "ar5iv"} -->

## Introduction

Maximum inner product search (MIPS) has become a popular paradigm for solving large scale classification and retrieval tasks. For example, in recommendation systems, user queries and documents are embedded into a dense vector space of the same dimensionality and MIPS is used to find the most relevant documents given a user query. Similarly, in extreme classification tasks, MIPS is used to predict the class label when a large number of classes, often on the order of millions or even billions are involved. Lately, MIPS has also been applied to training tasks such as scalable gradient computation in large output spaces, efficient sampling for speeding up softmax computation and sparse updates in end-to-end trainable memory systems.

To formally define the Maximum Inner Product Search (MIPS) problem, consider a database $X = {\{ x_{i}\}}_{i = {1,2,\ldots,n}}$ with $n$ datapoints, where each datapoint $x_{i} \in {\mathbb{R}}^{d}$ in a $d$-dimensional vector space. In the MIPS setup, given a query $q \in {\mathbb{R}}^{d}$, we would like to find the datapoint $x \in X$ that has the highest inner product with $q$, i.e., we would like to identify Exhaustively computing the exact inner product between $q$ and $n$ datapoints is often expensive and sometimes infeasible. Several techniques have been proposed in the literature based on hashing, graph search, or quantization to solve the approximate maximum inner product search problem efficiently, and the quantization based techniques have shown strong performance.

In most traditional quantization works, the objective in the quantization procedures is to minimize the reconstruction error for the database points. We show this is a suboptimal loss function for MIPS. This is because for a given query, quantization error for database points that score higher, or have larger inner products, is more important. Using this intuition, we propose a new family of score-aware quantization loss functions and apply it to multiple quantization techniques. Our contributions are as follows: We propose the score-aware quantization loss function. The proposed loss can work under any weighting function of the inner product and regardless of whether the datapoints vary in norm.

Under natural statistical assumptions, we show that the score-aware quantization loss can be efficiently calculated. The loss function leads to an anisotropic weighting that more greatly penalizes error parallel with the datapoint than error orthogonal to the datapoint.

The proposed loss is generally applicable to many quantization methods. We demonstrate the codebook learning and quantization procedures for product quantization and vector quantization can be efficiently adapted to the proposed loss function.

We show that anisotropic quantization leads to large MIPS performance gains over reconstruction loss-based techniques. Our method achieves state-of-the-art performance on standard large-scale benchmarks such as Glove-1.2M. In addition to recall gains, anisotropic quantization gives significantly more accurate inner product value approximations.

## Background and Related Works

### Inference as Maximum Inner Product Search

Efficient maximum inner product search (MIPS) is necessary for many large-scale machine learning systems. One popular approach to information retrieval systems and recommender systems uses representation learning in the embedding space. In this framework, we learn embedding functions to map items to be retrieved in a common vector space, where the items can be words, images, users, audio, products, web pages, graph nodes, or anything of interest.

In recommender systems, two networks are jointly trained to generate query (user) vectors and item vectors, such that embedding vectors of queries and relevant items have high inner product when computed in the embedding space. To perform inference, we first pre-compute a database of embedding vectors for items to be recommended. When a query arrives, we compute the query embedding then return the items with the highest inner product. In extreme classification, a neural network classifier is trained, where each row of the weight matrix of the classification layer corresponds to the embedding of a class label. In both settings, the computationally expensive operation is finding the item embedding that has the largest inner product with the query embedding, which can be efficiently solved by Maximum Inner Product Search (MIPS).

### Methods for accelerating MIPS

There is a large body of similarity search literature on max inner product and nearest neighbor search. We refer readers to for a comprehensive survey. We include a brief summary here.

There are two main tasks required to develop an efficient MIPS system. One task is to reduce the number of items that are scored to identify the top result. This is typically done with a space partitioning method. The other task is improving the rate at which items are scored. This is typically done with quantization, and is where the main contribution of our work lies. Successful implementation of MIPS systems requires good performance in both tasks.

Many researchers have developed high quality implementations of libraries for nearest neighbor search, such as SPTAG Chen et al., FAISS Johnson et al., and hnswlib Malkov & Yashunin. We compare with the ones available on ANN-Benchmarks in Section 5.

### Reducing the Number of Evaluations

One class of approaches to reducing the number of items scored is space partitioning. These approaches partition the space into different buckets. To perform MIPS in this setting, we find the relevant buckets for a given query and score only the items in these buckets.

Examples of this approach include tree search methods and locality sensitive hashing. Tree search methods such as partition the space recursively, forming a tree. Locality sensitive hashing partitions the space using a similarity-preserving hash function. There is also a class of approaches based on graph search. These methods work by navigating a graph by greedily selecting the neighbor with the highest dot product.

### Quantization

Quantization is an important technique for building state-of-the-art MIPS systems in large scale settings. Below we describe the several ways that quantization improves performance.

Efficient dot product computations: We can calculate the dot product of a $d$ dimensional query vector with $n$ quantized points in time $O{({{dk} + {mn}})}$ using look up tables, where $k$ is the size of each quantization codebook and $m$ is the number of codebooks. For typical choices of $k$ and $m$ this is faster than the $O{({nd})}$ complexity required for exact computation.

Memory bandwidth: modern processors need workloads with a high amount of computation per memory read in order to fully utilize their resources. Quantization compresses datapoints, resulting in less memory bandwidth usage and higher processor utilization.

Storage: quantized datapoints take up less space in memory or on disk. For large-scale datasets, this allows more datapoints to be stored on a single machine.

One approach to quantization is with random projections. One issue with random projections is that quantization is oblivious to the data, and it may be more efficient to use a quantization method that is able to exploit structure in the data. Quantization methods of this form are available for binary quantization, product quantization, additive quantization, and ternary quantization. We discuss product quantization in more detail in Section 4. There are also lines of work that focus on learning transformations before quantization. Learning quantization from the observed data distribution also has been studied in Marcheret et al.; Morozov & Babenko; Babenko et al..

Our work differs from the above methods as they essentially focus on minimizing reconstruction error as a loss function, while we develop an approach in the following section where we minimize a novel loss function that is designed to improve the downstream MIPS objective.

We also highlight the work May et al., where they consider quantization objectives for word embeddings that improve the downstream performance of training models for natural language processing tasks.

## Problem Formulation

Common quantization techniques focus on minimizing the reconstruction error (sum of squared error) when $x$ is quantized to $\overset{\sim}{x}$. It can be shown that minimizing the reconstruction errors is equivalent to minimizing the expected inner product quantization error under a mild condition on the query distribution without assumption on the database point distribution. Indeed, consider the quantization objective of minimizing the expected total inner product quantization errors over the query distribution: Under the assumption that $q$ is isotropic, i.e., ${{\mathbb{E}}{\lbrack{qq^{T}}\rbrack}} = {cI}$, where $I$ is the identity matrix and $c \in {\mathbb{R}}^{+}$, the objective function becomes Therefore, the objective becomes minimizing the reconstruction errors of the database points $\sum_{i = 1}^{n}{\|{x_{i} - \overset{\sim}{x_{i}}}\|}^{2}$, and this has been considered extensively in the literature.

One key observation about the above objective function is that it takes expectation over all possible combinations of datapoints $x$ and queries $q$. However, it is easy to see that not all pairs of $(x,q)$ are equally important. The approximation error on the pairs which have a high inner product is far more important since they are likely to be among the top ranked pairs and can greatly affect the search result, while for the pairs whose inner product is low the approximation error matters much less. In other words, for a given datapoint $x$, we should quantize it with a bigger focus on its error with those queries which have high inner product with $x$. See Figure 1 for the illustration.

Following this key observation, we propose the score-aware quantization loss. This is a new loss function for quantization that weighs the inner product approximation error by $w$, an arbitrary function of our choice that returns a weight based on the value of the true inner product. Specifically, we define the loss function as the following:

### Definition 3.1

Given a datapoint $x_{i}$, its quantization $\overset{\sim}{x_{i}}$, and a weight function $w:{{\mathbb{R}}\mapsto{\mathbb{R}}^{+}}$ of the inner product score, the score-aware quantization loss with respect to a query distribution $\mathcal{Q}$ is defined as Figure 1: (a) Not all pairs of q and x are equally important: for x, it is more important to accurately quantize the inner product of ⟨q1, x⟩ than ⟨q2, x⟩ or ⟨q3, x⟩, because ⟨q1, x⟩ has a higher inner product and thus is more likely to be the maximum; (b) Quantization error of x given one of its quantizer c2 can be decomposed to a parallel component r∥ and an orthogonal component r⟂. (c) Graphical illustration of the intuition behind Equation. Even if c3 is closer to x in terms of Euclidean distance, c2 is a better quantizer than c3 in terms of inner product approximation error of ⟨q1, x − c⟩. Notice that c3 incur more parallel loss (r∥), while c2 incur more orthogonal loss (r⟂).

Since the norm of $q$ does not matter to the ranking result, we can assume ${\| q\|} = 1$ without loss of generality. Similarly, assuming we have no prior knowledge of the query distribution $\mathcal{Q}$, we trivially assume $q$ is uniformly spherically distributed. The expectation can be recomputed if $\mathcal{Q}$ is known or estimated empirically.

### Analyzing Score-Aware Quantization Loss

We show that regardless of the choice of $w$, a score-aware quantization loss $\ell{(x_{i},\overset{\sim}{x_{i}},w)}$ always decomposes into an anisotropic weighted sum of the magnitudes of the parallel and orthogonal residual errors. These two errors are defined as follows: first, define the residual error of a quantization $\overset{\sim}{x_{i}}$ as $x_{i} - \overset{\sim}{x_{i}}$. The parallel residual error is the component of the residual error parallel to the datapoint $x_{i}$; it can be computed as Orthogonal residual error is defined analogously, and can be computed as These two components are illustrated in Figure 1(b). The relative weights of these two error components in contributing to the score-aware loss are determined by the choice of $w$.

### Theorem 3.2

Suppose we are given a datapoint $x_{i}$, its quantization $\overset{\sim}{x_{i}}$, and a weight function $w$. Assuming that query $q$ is uniformly distributed in the $d$-dimensional unit sphere, the score-aware quantization loss equals with $h_{\parallel}$ and $h_{\perp}$ defined as follows:

### Proof

See Appendix Section 7.1. ∎ Any weight function would work for the above proposed loss. For the MIPS problem, it is intuitive to choose $w$ so that it puts greater weight on larger inner products. For such $w$, we show that parallel quantization error is weighted more heavily than orthogonal quantization error. This is formalized below and illustrated in Figure 1.

### Theorem 3.3

For any $w$ such that ${w{(t)}} = 0$ for $t < 0$ and $w{(t)}$ is monotonically non-decreasing for $t \geq 0$, with equality if and only if $w{(t)}$ is constant for ${t \in {\lbrack{- {\| x_{i}\|}},{\| x_{i}\|}\rbrack}}.$

### Proof

See Appendix Section 7.2. ∎

### Special case of ${w{(t)}} = {\mathbf{I}{({t \geq T})}}$

One particular $w$ of interest is the function ${w{(t)}} = {\mathbf{I}{({t \geq T})}}$. This weight function only considers quantization loss when the dot product is above a threshold $T$. Since $\mathbf{I}{({t \geq T})}$ satisfies the conditions for Theorem 3.3, it effectively penalizes parallel quantization error more greatly than orthogonal error. With this weight function, our expressions for $h_{\parallel}$ and $h_{\perp}$ simplify to: With ${w{(t)}} = {\mathbf{I}{({t \geq T})}}$, we have Figure 2: The ratio η (I (t ≥ T = 0.2), ∥x∥ = 1)/(d − 1) in Theorem 3.4 computed analytically as a function of d quickly approaches the limit defined in Equation.

We can recursively compute $\eta{({w = {{\mathbf{I}{({t \geq T})}},{\| x_{i}\|}}})}$ as a function of $d$ analytically. Furthermore we can prove that $\frac{\eta}{d - 1}$ has an limit as $d\rightarrow\infty$, as demonstrated empirically in Figure 2=I⁢(𝑡≥𝑇) ‣ Problem Formulation ‣ Accelerating Large-Scale Inference with Anisotropic Vector Quantization"). We can use this limit, which is easy to evaluate, as a proxy of $\eta$ in computing the proposed loss.

### Theorem 3.4

### Proof

See Appendix Section 7.3=I⁢(𝑡≥𝑇) ‣ Appendix ‣ Accelerating Large-Scale Inference with Anisotropic Vector Quantization"). ∎ As special cases, when $T = 0$, ${\eta{({\mathbf{I}{({t \geq 0})}},{\| x_{i}\|})}} = 1$ which implies parallel and orthogonal errors are weighted equally. When $T = {\|{|x_{i}|}|}$, we have ${\eta{({\mathbf{I}{({t \geq {\| x_{i}\|}})}},{\| x_{i}\|})}} = \infty$ which indicates we should only consider parallel error.

Theorem 3.2 shows that the weight of each datapoint's parallel and orthogonal quantization errors are dependent on $\| x_{i}\|$. However, when the database has constant norm, i.e. ${\| x_{i}\|} = c$, we can use the following simplified form:

## Application to Quantization Techniques

In this section we consider the codebook learning and quantization procedure for our proposed anisotropic loss function. In the previous sections, we established that the loss function, $\ell{(x_{i},{\overset{\sim}{x}}_{i},w)}$ leads to a weighted combination of parallel quantization error and orthogonal quantization error. In practice, we can choose a fixed $\eta$ according to the choice of $w$ such as the one suggested in Section 3.2=I⁢(𝑡≥𝑇) ‣ Problem Formulation ‣ Accelerating Large-Scale Inference with Anisotropic Vector Quantization").

In vector quantization, we first construct a dictionary $C = {\{ c_{1},c_{2},\ldots,c_{k}\}}$. To quantize a vector $x$ we replace $x$ with one of the codewords. Typically, the quantized vector $\overset{\sim}{x}$ minimizes some loss function: $\overset{\sim}{x} = {{{\arg\min}_{c_{1},c_{2},\ldots,c_{k}}L}{(x_{i},c_{i})}}$.

After we quantize a database of $n$ points, we can calculate the dot product of a query vector $q$ with all quantized points in $O{({{kd} + n})}$ time. This is much better than the $O{({nd})}$ time required for the original unquantized database. We achieve the $O{({{kd} + n})}$ runtime by computing a lookup table containing the inner product of the $q$ with each of the $k$ codewords in $O{({kd})}$ time. We then do a table lookup for each of the $n$ datapoints to get their corresponding inner products.

In order to construct the dictionary $C$, we need to optimize the choice of codewords over the loss function. For $\ell_{2}$-reconstruction loss, the optimization problem becomes This is exactly the well-studied $k$-means clustering objective, which is often solved using Lloyd's algorithm.

If, as in the previous section, we have our loss function ${\ell{(x,\overset{\sim}{x})}} = {{h_{i, \parallel}{\|{r_{\parallel}{(x_{i},\overset{\sim}{x_{i}})}}\|}^{2}} + {h_{i, \perp}{\|{r_{\perp}{(x_{i},\overset{\sim}{x_{i}})}}\|}^{2}}}$ for appropriate scaling parameters $h_{i, \parallel}$, $h_{i, \perp}$, we obtain a new objective function we call the anisotropic vector quantization problem.

### Definition 4.1

Given a dataset $x_{1},x_{2},\ldots,x_{n}$ of points in ${\mathbb{R}}^{d}$, scaling parameters $h_{i, \parallel}$, $h_{i, \perp}$ for every datapoint $x_{i}$, and $k$ codewords, the anisotropic vector quantization problem is finding the $k$ codewords that minimize the objective function Next we develop an iterative algorithm to optimize the anisotropic vector quantization problem. Similar to Lloyd's algorithm, our algorithm iterate between partition assignment step and codebook update step: (Initialization Step) Initialize codewords $c_{1},c_{2},\ldots,c_{k}$ to be random datapoints sampled from $x_{1}\ldotsx_{n}$.

(Partition Assignment Step) For each datapoint $x_{i}$ find its codeword $\overset{\sim}{x_{i}} = {{{\arg\min}_{{\overset{\sim}{x}}_{i} \in {\{ c_{1},\ldots,c_{k}\}}}\ell}{(x_{i},{\overset{\sim}{x}}_{i})}}$. This can be done by enumerating all $k$ possile choices of codewords.

(Codebook Update Step) For every codeword $c_{j}$, let $X_{j}$ be all datapoints $x_{i}$ such that ${\overset{\sim}{x}}_{i} = c_{j}$. Update $c_{j}$ by Repeat Step 2 and Step 3 until convergence to a fixed point or maximum number of iteration is reached.

In each iteration, we need perform update step for each of the codeword. Given a partition of the datapoints $X_{j}$, we can find the optimal value of the codeword $c_{j}$ that minimizes the following objective: By setting gradient respect to $c_{j}$ to zero, we obtain the following update rule:

### Theorem 4.2

Optimal codeword $c_{j}$ can be obtained in closed form by solving the optimization problem in Equation for a partition $X_{j}$. The update rule for the codebook is

### Proof

See Section 7.4 of the Appendix for the proof. ∎ As expected, we see that when all $h_{i, \parallel} = h_{i, \perp}$, our codeword update is equivalent to finding the weighted average of the partition. Furthermore, if ${w{(t)}} = 1$, the update rule becomes finding the average of datapoints in the partition, same as standard $k$-means update rule. Additionally, since there are only a finite number of partitions and at every iteration the loss function decreases or stays constant, our solution will eventually converge to a fixed point.

### Product Quantization

In vector quantization with a dictionary of size $k$, we quantize each datapoint into one of $k$ possible codewords. We can think of this as encoding each datapoint with one dimension with $k$ possible states.

With product quantization we encode each datapoint into an $M$ dimensional codeword, each with $k$ possible states. This allows us to represent $k^{M}$ possible codewords, which would not be scalable with vector quantization. To do this, we split each datapoint $x$ into $M$ subspaces each of dimension $d/M$: $x = {(x^{},x^{},\ldots,x^{(m)})}$. We then create $M$ dictionaries $C^{},C^{},\ldots,C^{(m)}$, each with $k$ codewords of dimension $d/M$. Each datapoint would then be encoded with $M$ dimensions, with every dimension taking one of $k$ states.

To calculate distances with product quantization, for every dictionary $C^{(m)}$ we calculate the partial dot product of the relevant subspace of the query with every codeword in the dictionary. The final dot product is obtain by sum up all $M$ partial dot product. We can then calculate the dot product with $m$ quantized datapoints in time $O{({{kd} + {mn}})}$.

Using our anisotropic loss function ${\ell{(x_{i},{\overset{\sim}{x}}_{i})}} = {{h_{i, \parallel}{\|{r_{\parallel}{(x_{i},{\overset{\sim}{x}}_{i})}}\|}^{2}} + {h_{i, \perp}{\|{r_{\perp}{(x_{i},{\overset{\sim}{x}}_{i})}}\|}^{2}}}$ we obtain a new objective function for product quantization we call the anisotropic product quantization problem.

### Definition 4.3

Given a dataset $x_{1},x_{2},\ldots,x_{n}$ of points in ${\mathbb{R}}^{d}$, a scaling parameter $\eta$, a number $M$ of dictionaries each with elements of size $d/M$ and $k$ codewords in each dictionary, the anisotropic product quantization problem is to find the $M$ dictionaries that minimizes We again consider an iterative algorithm for the problem. We first initialize all quantized datapoints with some element from every dictionary. We then consider the following iterative procedure: (Initialization Step) Select a dictionary $C^{(m)}$ by sampling from $\{ x_{1}^{(m)},{\ldotsx_{n}^{(m)}}\}$.

(Partition Assignment Step) For each datapoint $x_{i}$, update ${\overset{\sim}{x}}_{i}$ by using the value of $c \in C^{(m)}$ that minimizes the anisotropic loss of ${\overset{\sim}{x}}_{i}$.

(Codebook Update Step) Optimize the loss function over all codewords in all dictionaries while keeping every dictionaries partitions constant.

Repeat Step 2 and Step 3 until convergence to a fixed point or maximum number of iteration is reached.

We can perform the update step efficiently since once the partitions are fixed the update step minimizes a convex loss, similar to that of vector quantization. We include details in Section 7.5 of the Appendix. Additionally, since there are a finite number of partition assignment and at every step the loss function decreases or stays constant, our solution will eventually converge to a fixed point. We note that we can also optionally initialize the codebook by first training the codebook under regular $\ell_{2}$-reconstruction loss, which speed up training process.

## Experiments

In this section, we show our proposed quantization objective leads to improved performance on maximum inner product search. First, we fix the quantization mechanism and compare traditional reconstruction loss with our proposed loss to show that score-aware loss leads to better retrieval performance and more accurate estimation of maximum inner product values. Next, we compare in fixed-bit-rate settings against QUIPS and LSQ, which are the current state-of-the-art for many MIPS tasks. Finally, we analyze the end-to-end MIPS retrieval performance of our algorithm in terms of its speed-recall trade-off in a standardized hardware environment. We used the benchmark setup from [ann-benchmarks.com](ann-benchmarks.com), which provides 11 competitive baselines with pre-tuned parameters. We plot each algorithm's speed-recall curve and show ours achieves the state-of-the-art.

Figure 3: (a) The retrieval Recall1@10 for different values of the threshold T. We see that for T = 0.2 (corresponding to η = 4.125) our proposed score-aware quantization loss achieves significantly better Recall than traditional reconstruction loss. (b) The relative error of inner product estimation for true Top-1 on Glove1.2M dataset across multiple number of bits settings. We see that our proposed score-aware quantization loss reduces the relative error compared to reconstruction loss.

(c) MIPS recall on Glove1.2M.

(d) Speed-recall trade-off on Glove1.2M Recall 10@10.

Figure 4: (a) Recall 1@N curve on Glove1.2M comparing with variants of QUIPS Guo et al. and LSQ Martinez et al. on MIPS tasks. We see that our method improves over all of these methods. (b) Recall-Speed benchmark with 11 baselines from Aumüller et al. on Glove1.2M. The parameters of each baseline are pre-tuned and released : We see that our approach is the fastest in the high recall regime.

### Direct comparison with reconstruction loss

We compare our proposed score-aware quantization loss with the traditional reconstruction loss by fixing all parameters other than the loss function in the following experiments.

We use Glove1.2M which is a collection of 1.2 million 100-dimensional word embeddings trained as described in Pennington et al.. See Section 7.8 of the Appendix for our rationale for choosing this dataset. For all experiments we choose ${w{(t)}} = {\mathbf{I}{({t \geq T})}}$. The Glove dataset is meant to be used with a cosine distance similarity metric, while our algorithm is designed for the more general MIPS task. MIPS is equivalent to cosine similarity search when all datapoints are equal-norm, so we adopt our technique to cosine similarity search by unit-normalizing all datapoints at training time.

We first compare the two losses by their Recall1@10 when used for product quantization on Glove1.2M, as shown in Figure. 3(a). We learn a dictionary by optimizing product quantization with reconstruction loss. We then quantize datapoints two ways, first by minimizing reconstruction loss and then by minimizing score-aware loss. We see that score-aware quantization loss achieves significant recall gains as long as $T$ is chosen reasonably. For all subsequent experiments, we set $T = 0.2$, which by the limit in Equation (3=I⁢(𝑡≥𝑇) ‣ Problem Formulation ‣ Accelerating Large-Scale Inference with Anisotropic Vector Quantization")) corresponds to a value of $\eta = 4.125$.

Next we look at the accuracy of the estimated top-1 inner product as measured by relative error: $|\frac{{\langle q,x\rangle} - {\langle q,\overset{\sim}{x}\rangle}}{\langle q,x\rangle}|$. This is important in application scenarios where an accurate estimate of $\langle q,x\rangle$ is needed, such as softmax approximation, where the inner product values are often logits later used to compute probabilities. One direct consequence of score-aware loss functions is that the objective weighs pairs by their importance and thus leads to lower estimation error on top-ranking pairs. We see in Figure. 3(b) that our score-aware loss leads to smaller relative error over all bitrate settings.

Datasets other than Glove demonstrate similar performance gains from score-aware quantization loss. See Section 7.6 of the Appendix for results on the Amazon-670k extreme classification dataset.

### Maximum inner product search retrieval

Next, we compare our MIPS retrieval performance against other quantization techniques at equal bitrate. We compare to LSQ Martinez et al. and all three variants of QUIPS Guo et al.. In Figure 4 we measure the performance at fixed bitrates of 100 and 200 bits per datapoint. Our metric is Recall 1@N, which corresponds to the proportion of queries where the top $N$ retrieved results contain the true top-1 datapoint. Our algorithm using score-aware loss outperforms other algorithms at both bitrates and all ranges of $N$.

Other quantization methods may also benefit from using score-aware quantization loss. For example, binary quantization techniques such as Dai et al. use reconstruction loss in their original paper, but can be easily adapted to the proposed loss by a one line change to the loss objective. We show results which illustrate the improvement of such a change in Section 7.7 of Appendix.

### Recall-Speed benchmark

Fixed-bit-rate experiments mostly compare asymptotic behavior and often overlook preprocessing overhead such as learned rotation or lookup table computation, which can be substantial. To evaluate effectiveness of MIPS algorithms in a realistic setting, it is important to perform end-to-end benchmarks and compare speed-recall curves. We adopted the methodology of public benchmark ANN-Benchmarks Aumüller et al., which plots a comprehensive set of 11 algorithms for comparison, including faiss Johnson et al. and hnswlib Malkov & Yashunin.

Our benchmarks are all conducted on an Intel Xeon W-2135 with a single CPU thread, and followed the benchmark's protocol. Our implementation builds on product quantization with the proposed quantization and SIMD based ADC Guo et al. for distance computation. This is further combined with a vector quantization based tree Wu et al.. Our implementation is open-source and available at and furthermore the exact configurations used to produce our benchmark numbers are part of the ANN-Benchmarks GitHub repository. Figure 4 shows our performance on Glove1.2M significantly outperforms competing methods in the high-recall region.

## Conclusion

In this paper, we propose a new quantization loss function for inner product search, which replaces traditional reconstruction error. The new loss function is weighted based on the inner product values, giving more weight to the pairs of query and database points with higher inner product values. The proposed loss function is theoretically proven and can be applied to a wide range of quantization methods, for example product and binary quantization. Our experiments show superior performance on retrieval recall and inner product value estimation compared to methods that use reconstruction error. The speed-recall benchmark on public datasets further indicates that the proposed method outperforms state-of-the-art baselines which are known to be hard to beat.
