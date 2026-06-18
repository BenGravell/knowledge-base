<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Accelerating Large-Scale Inference with Anisotropic Vector Quantization

Topics include Benchmarks, Vector quantization.

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Quantization based techniques are the current state-of-the-art for scaling maximum inner product search to massive databases. Traditional approaches to quantization aim to minimize the reconstruction error of the database points. Based on the observation that for a given query, the database points that have the largest inner products are more relevant, we develop a family of anisotropic quantization loss functions. Under natural statistical assumptions, we show that quantization with these loss functions leads to a new variant of vector quantization that more greatly penalizes the parallel component of a datapoint's residual relative to its orthogonal component. The proposed approach achieves state-of-the-art results on the public benchmarks available .

<!-- chunk {"id": "body-0003", "role": "body", "section": "Introduction", "weight": 1.5} -->

Maximum inner product search (MIPS) has become a popular paradigm for solving large scale classification and retrieval tasks. For example, in recommendation systems, user queries and documents are embedded into a dense vector space of the same dimensionality and MIPS is used to find the most relevant documents given a user query. Similarly, in extreme classification tasks, MIPS is used to predict the class label when a large number of classes, often on the order of millions or even billions are involved. Lately, MIPS has also been applied to training tasks such as scalable gradient computation in large output spaces, efficient sampling for speeding up softmax computation and sparse updates in end-to-end trainable memory systems.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

To formally define the Maximum Inner Product Search (MIPS) problem, consider a database $X = {\{ x_{i}\}}_{i = {1,2,\ldots,n}}$ with $n$ datapoints, where each datapoint $x_{i} \in {\mathbb{R}}^{d}$ in a $d$-dimensional vector space. In the MIPS setup, given a query $q \in {\mathbb{R}}^{d}$, we would like to find the datapoint $x \in X$ that has the highest inner product with $q$, i.e., we would like to identify

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

Exhaustively computing the exact inner product between $q$ and $n$ datapoints is often expensive and sometimes infeasible. Several techniques have been proposed in the literature based on hashing, graph search, or quantization to solve the approximate maximum inner product search problem efficiently, and the quantization based techniques have shown strong performance.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

In most traditional quantization works, the objective in the quantization procedures is to minimize the reconstruction error for the database points. We show this is a suboptimal loss function for MIPS. This is because for a given query, quantization error for database points that score higher, or have larger inner products, is more important. Using this intuition, we propose a new family of score-aware quantization loss functions and apply it to multiple quantization techniques.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

We propose the score-aware quantization loss function. The proposed loss can work under any weighting function of the inner product and regardless of whether the datapoints vary in norm.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Introduction", "weight": 1.5} -->

Under natural statistical assumptions, we show that the score-aware quantization loss can be efficiently calculated. The loss function leads to an anisotropic weighting that more greatly penalizes error parallel with the datapoint than error orthogonal to the datapoint.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Introduction", "weight": 1.5} -->

The proposed loss is generally applicable to many quantization methods. We demonstrate the codebook learning and quantization procedures for product quantization and vector quantization can be efficiently adapted to the proposed loss function.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Introduction", "weight": 1.5} -->

We show that anisotropic quantization leads to large MIPS performance gains over reconstruction loss-based techniques. Our method achieves state-of-the-art performance on standard large-scale benchmarks such as Glove-1.2M. In addition to recall gains, anisotropic quantization gives significantly more accurate inner product value approximations.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Inference as Maximum Inner Product Search", "weight": 1.0} -->

Efficient maximum inner product search (MIPS) is necessary for many large-scale machine learning systems. One popular approach to information retrieval systems and recommender systems uses representation learning in the embedding space. In this framework, we learn embedding functions to map items to be retrieved in a common vector space, where the items can be words, images, users, audio, products, web pages, graph nodes, or anything of interest.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Inference as Maximum Inner Product Search", "weight": 1.0} -->

In recommender systems, two networks are jointly trained to generate query (user) vectors and item vectors, such that embedding vectors of queries and relevant items have high inner product when computed in the embedding space. To perform inference, we first pre-compute a database of embedding vectors for items to be recommended. When a query arrives, we compute the query embedding then return the items with the highest inner product. In extreme classification, a neural network classifier is trained, where each row of the weight matrix of the classification layer corresponds to the embedding of a class label. In both settings, the computationally expensive operation is finding the item embedding that has the largest inner product with the query embedding, which can be efficiently solved by Maximum Inner Product Search (MIPS).

<!-- chunk {"id": "body-0013", "role": "body", "section": "Methods for accelerating MIPS", "weight": 1.0} -->

There is a large body of similarity search literature on max inner product and nearest neighbor search. We refer readers to for a comprehensive survey. We include a brief summary here.

<!-- chunk {"id": "body-0014", "role": "body", "section": "Methods for accelerating MIPS", "weight": 1.0} -->

There are two main tasks required to develop an efficient MIPS system. One task is to reduce the number of items that are scored to identify the top result. This is typically done with a space partitioning method. The other task is improving the rate at which items are scored. This is typically done with quantization, and is where the main contribution of our work lies. Successful implementation of MIPS systems requires good performance in both tasks.

<!-- chunk {"id": "body-0015", "role": "body", "section": "Methods for accelerating MIPS", "weight": 1.0} -->

Many researchers have developed high quality implementations of libraries for nearest neighbor search, such as SPTAG Chen et al., FAISS Johnson et al., and hnswlib Malkov & Yashunin. We compare with the ones available on ANN-Benchmarks in Section 5.

<!-- chunk {"id": "body-0016", "role": "body", "section": "Reducing the Number of Evaluations", "weight": 1.0} -->

One class of approaches to reducing the number of items scored is space partitioning. These approaches partition the space into different buckets. To perform MIPS in this setting, we find the relevant buckets for a given query and score only the items in these buckets.

<!-- chunk {"id": "body-0017", "role": "body", "section": "Reducing the Number of Evaluations", "weight": 1.0} -->

Examples of this approach include tree search methods and locality sensitive hashing. Tree search methods such as partition the space recursively, forming a tree. Locality sensitive hashing partitions the space using a similarity-preserving hash function. There is also a class of approaches based on graph search. These methods work by navigating a graph by greedily selecting the neighbor with the highest dot product.

<!-- chunk {"id": "body-0018", "role": "body", "section": "Quantization", "weight": 1.0} -->

Quantization is an important technique for building state-of-the-art MIPS systems in large scale settings. Below we describe the several ways that quantization improves performance.

<!-- chunk {"id": "body-0019", "role": "body", "section": "Quantization", "weight": 1.0} -->

Efficient dot product computations: We can calculate the dot product of a $d$ dimensional query vector with $n$ quantized points in time $O{({{dk} + {mn}})}$ using look up tables, where $k$ is the size of each quantization codebook and $m$ is the number of codebooks. For typical choices of $k$ and $m$ this is faster than the $O{({nd})}$ complexity required for exact computation.

<!-- chunk {"id": "body-0020", "role": "body", "section": "Quantization", "weight": 1.0} -->

Memory bandwidth: modern processors need workloads with a high amount of computation per memory read in order to fully utilize their resources. Quantization compresses datapoints, resulting in less memory bandwidth usage and higher processor utilization.

<!-- chunk {"id": "body-0021", "role": "body", "section": "Quantization", "weight": 1.0} -->

Storage: quantized datapoints take up less space in memory or on disk. For large-scale datasets, this allows more datapoints to be stored on a single machine.

<!-- chunk {"id": "body-0022", "role": "body", "section": "Quantization", "weight": 1.0} -->

One approach to quantization is with random projections. One issue with random projections is that quantization is oblivious to the data, and it may be more efficient to use a quantization method that is able to exploit structure in the data. Quantization methods of this form are available for binary quantization, product quantization, additive quantization, and ternary quantization. We discuss product quantization in more detail in Section 4. There are also lines of work that focus on learning transformations before quantization. Learning quantization from the observed data distribution also has been studied in Marcheret et al.; Morozov & Babenko; Babenko et al..

<!-- chunk {"id": "body-0023", "role": "body", "section": "Quantization", "weight": 1.0} -->

Our work differs from the above methods as they essentially focus on minimizing reconstruction error as a loss function, while we develop an approach in the following section where we minimize a novel loss function that is designed to improve the downstream MIPS objective.

<!-- chunk {"id": "body-0024", "role": "body", "section": "Quantization", "weight": 1.0} -->

We also highlight the work May et al., where they consider quantization objectives for word embeddings that improve the downstream performance of training models for natural language processing tasks.

<!-- chunk {"id": "body-0025", "role": "body", "section": "Problem Formulation", "weight": 1.0} -->

Common quantization techniques focus on minimizing the reconstruction error (sum of squared error) when $x$ is quantized to $\overset{\sim}{x}$. It can be shown that minimizing the reconstruction errors is equivalent to minimizing the expected inner product quantization error under a mild condition on the query distribution without assumption on the database point distribution.

<!-- chunk {"id": "body-0026", "role": "body", "section": "Problem Formulation", "weight": 1.0} -->

Under the assumption that $q$ is isotropic, i.e., ${{\mathbb{E}}{\lbrack{qq^{T}}\rbrack}} = {cI}$, where $I$ is the identity matrix and $c \in {\mathbb{R}}^{+}$, the objective function becomes

<!-- chunk {"id": "body-0027", "role": "body", "section": "Problem Formulation", "weight": 1.0} -->

Therefore, the objective becomes minimizing the reconstruction errors of the database points $\sum_{i = 1}^{n}{\|{x_{i} - \overset{\sim}{x_{i}}}\|}^{2}$, and this has been considered extensively in the literature.

<!-- chunk {"id": "body-0028", "role": "body", "section": "Problem Formulation", "weight": 1.0} -->

One key observation about the above objective function is that it takes expectation over all possible combinations of datapoints $x$ and queries $q$. However, it is easy to see that not all pairs of $(x,q)$ are equally important. The approximation error on the pairs which have a high inner product is far more important since they are likely to be among the top ranked pairs and can greatly affect the search result, while for the pairs whose inner product is low the approximation error matters much less. In other words, for a given datapoint $x$, we should quantize it with a bigger focus on its error with those queries which have high inner product with $x$. See Figure 1 for the illustration.

<!-- chunk {"id": "body-0029", "role": "body", "section": "Problem Formulation", "weight": 1.0} -->

Following this key observation, we propose the score-aware quantization loss. This is a new loss function for quantization that weighs the inner product approximation error by $w$, an arbitrary function of our choice that returns a weight based on the value of the true inner product.

<!-- chunk {"id": "body-0030", "role": "body", "section": "Analyzing Score-Aware Quantization Loss", "weight": 1.0} -->

We show that regardless of the choice of $w$, a score-aware quantization loss $\ell{(x_{i},\overset{\sim}{x_{i}},w)}$ always decomposes into an anisotropic weighted sum of the magnitudes of the parallel and orthogonal residual errors. These two errors are defined as follows: first, define the residual error of a quantization $\overset{\sim}{x_{i}}$ as $x_{i} - \overset{\sim}{x_{i}}$. The parallel residual error is the component of the residual error parallel to the datapoint $x_{i}$; it can be computed as

<!-- chunk {"id": "body-0031", "role": "body", "section": "Analyzing Score-Aware Quantization Loss", "weight": 1.0} -->

Orthogonal residual error is defined analogously, and can be computed as

<!-- chunk {"id": "body-0032", "role": "body", "section": "Analyzing Score-Aware Quantization Loss", "weight": 1.0} -->

These two components are illustrated in Figure 1(b). The relative weights of these two error components in contributing to the score-aware loss are determined by the choice of $w$.

<!-- chunk {"id": "body-0033", "role": "body", "section": "Special case of ${w{(t)}} = {\\mathbf{I}{({t \\geq T})}}$", "weight": 1.0} -->

One particular $w$ of interest is the function ${w{(t)}} = {\mathbf{I}{({t \geq T})}}$. This weight function only considers quantization loss when the dot product is above a threshold $T$. Since $\mathbf{I}{({t \geq T})}$ satisfies the conditions for Theorem 3.3, it effectively penalizes parallel quantization error more greatly than orthogonal error.

<!-- chunk {"id": "body-0034", "role": "body", "section": "Special case of ${w{(t)}} = {\\mathbf{I}{({t \\geq T})}}$", "weight": 1.0} -->

We can recursively compute $\eta{({w = {{\mathbf{I}{({t \geq T})}},{\| x_{i}\|}}})}$ as a function of $d$ analytically. Furthermore we can prove that $\frac{\eta}{d - 1}$ has an limit as $d\rightarrow\infty$, as demonstrated empirically in Figure 2=I⁢(𝑡≥𝑇) ‣ Problem Formulation ‣ Accelerating Large-Scale Inference with Anisotropic Vector Quantization"). We can use this limit, which is easy to evaluate, as a proxy of $\eta$ in computing the proposed loss.

<!-- chunk {"id": "body-0035", "role": "body", "section": "Application to Quantization Techniques", "weight": 1.0} -->

In this section we consider the codebook learning and quantization procedure for our proposed anisotropic loss function. In the previous sections, we established that the loss function, $\ell{(x_{i},{\overset{\sim}{x}}_{i},w)}$ leads to a weighted combination of parallel quantization error and orthogonal quantization error. In practice, we can choose a fixed $\eta$ according to the choice of $w$ such as the one suggested in Section 3.2=I⁢(𝑡≥𝑇) ‣ Problem Formulation ‣ Accelerating Large-Scale Inference with Anisotropic Vector Quantization").

<!-- chunk {"id": "body-0036", "role": "body", "section": "Application to Quantization Techniques", "weight": 1.0} -->

After we quantize a database of $n$ points, we can calculate the dot product of a query vector $q$ with all quantized points in $O{({{kd} + n})}$ time. This is much better than the $O{({nd})}$ time required for the original unquantized database. We achieve the $O{({{kd} + n})}$ runtime by computing a lookup table containing the inner product of the $q$ with each of the $k$ codewords in $O{({kd})}$ time. We then do a table lookup for each of the $n$ datapoints to get their corresponding inner products.

<!-- chunk {"id": "body-0037", "role": "body", "section": "Application to Quantization Techniques", "weight": 1.0} -->

In order to construct the dictionary $C$, we need to optimize the choice of codewords over the loss function. For $\ell_{2}$-reconstruction loss, the optimization problem becomes

<!-- chunk {"id": "body-0038", "role": "body", "section": "Application to Quantization Techniques", "weight": 1.0} -->

This is exactly the well-studied $k$-means clustering objective, which is often solved using Lloyd's algorithm.

<!-- chunk {"id": "body-0039", "role": "body", "section": "Product Quantization", "weight": 1.0} -->

In vector quantization with a dictionary of size $k$, we quantize each datapoint into one of $k$ possible codewords. We can think of this as encoding each datapoint with one dimension with $k$ possible states.

<!-- chunk {"id": "body-0040", "role": "body", "section": "Product Quantization", "weight": 1.0} -->

With product quantization we encode each datapoint into an $M$ dimensional codeword, each with $k$ possible states. This allows us to represent $k^{M}$ possible codewords, which would not be scalable with vector quantization. To do this, we split each datapoint $x$ into $M$ subspaces each of dimension $d/M$: $x = {(x^{},x^{},\ldots,x^{(m)})}$. We then create $M$ dictionaries $C^{},C^{},\ldots,C^{(m)}$, each with $k$ codewords of dimension $d/M$. Each datapoint would then be encoded with $M$ dimensions, with every dimension taking one of $k$ states.

<!-- chunk {"id": "body-0041", "role": "body", "section": "Product Quantization", "weight": 1.0} -->

To calculate distances with product quantization, for every dictionary $C^{(m)}$ we calculate the partial dot product of the relevant subspace of the query with every codeword in the dictionary. The final dot product is obtain by sum up all $M$ partial dot product. We can then calculate the dot product with $m$ quantized datapoints in time $O{({{kd} + {mn}})}$.

<!-- chunk {"id": "body-0042", "role": "body", "section": "Experiments", "weight": 1.0} -->

In this section, we show our proposed quantization objective leads to improved performance on maximum inner product search. First, we fix the quantization mechanism and compare traditional reconstruction loss with our proposed loss to show that score-aware loss leads to better retrieval performance and more accurate estimation of maximum inner product values. Next, we compare in fixed-bit-rate settings against QUIPS and LSQ, which are the current state-of-the-art for many MIPS tasks. Finally, we analyze the end-to-end MIPS retrieval performance of our algorithm in terms of its speed-recall trade-off in a standardized hardware environment. We used the benchmark setup from [ann-benchmarks.com](ann-benchmarks.com), which provides 11 competitive baselines with pre-tuned parameters. We plot each algorithm's speed-recall curve and show ours achieves the state-of-the-art.

<!-- chunk {"id": "body-0043", "role": "body", "section": "Direct comparison with reconstruction loss", "weight": 1.0} -->

We compare our proposed score-aware quantization loss with the traditional reconstruction loss by fixing all parameters other than the loss function in the following experiments.

<!-- chunk {"id": "body-0044", "role": "body", "section": "Direct comparison with reconstruction loss", "weight": 1.0} -->

We use Glove1.2M which is a collection of 1.2 million 100-dimensional word embeddings trained as described in Pennington et al.. See Section 7.8 of the Appendix for our rationale for choosing this dataset. For all experiments we choose ${w{(t)}} = {\mathbf{I}{({t \geq T})}}$. The Glove dataset is meant to be used with a cosine distance similarity metric, while our algorithm is designed for the more general MIPS task. MIPS is equivalent to cosine similarity search when all datapoints are equal-norm, so we adopt our technique to cosine similarity search by unit-normalizing all datapoints at training time.

<!-- chunk {"id": "body-0045", "role": "body", "section": "Direct comparison with reconstruction loss", "weight": 1.0} -->

We first compare the two losses by their Recall1@10 when used for product quantization on Glove1.2M, as shown in Figure. 3(a). We learn a dictionary by optimizing product quantization with reconstruction loss. We then quantize datapoints two ways, first by minimizing reconstruction loss and then by minimizing score-aware loss. We see that score-aware quantization loss achieves significant recall gains as long as $T$ is chosen reasonably. For all subsequent experiments, we set $T = 0.2$, which by the limit in Equation (3=I⁢(𝑡≥𝑇) ‣ Problem Formulation ‣ Accelerating Large-Scale Inference with Anisotropic Vector Quantization")) corresponds to a value of $\eta = 4.125$.

<!-- chunk {"id": "body-0046", "role": "body", "section": "Direct comparison with reconstruction loss", "weight": 1.0} -->

Next we look at the accuracy of the estimated top-1 inner product as measured by relative error: $|\frac{{\langle q,x\rangle} - {\langle q,\overset{\sim}{x}\rangle}}{\langle q,x\rangle}|$. This is important in application scenarios where an accurate estimate of $\langle q,x\rangle$ is needed, such as softmax approximation, where the inner product values are often logits later used to compute probabilities. One direct consequence of score-aware loss functions is that the objective weighs pairs by their importance and thus leads to lower estimation error on top-ranking pairs. We see in Figure. 3(b) that our score-aware loss leads to smaller relative error over all bitrate settings.

<!-- chunk {"id": "body-0047", "role": "body", "section": "Direct comparison with reconstruction loss", "weight": 1.0} -->

Datasets other than Glove demonstrate similar performance gains from score-aware quantization loss. See Section 7.6 of the Appendix for results on the Amazon-670k extreme classification dataset.

<!-- chunk {"id": "body-0048", "role": "body", "section": "Maximum inner product search retrieval", "weight": 1.0} -->

Next, we compare our MIPS retrieval performance against other quantization techniques at equal bitrate. We compare to LSQ Martinez et al. and all three variants of QUIPS Guo et al.. In Figure 4 we measure the performance at fixed bitrates of 100 and 200 bits per datapoint. Our metric is Recall 1@N, which corresponds to the proportion of queries where the top $N$ retrieved results contain the true top-1 datapoint. Our algorithm using score-aware loss outperforms other algorithms at both bitrates and all ranges of $N$.

<!-- chunk {"id": "body-0049", "role": "body", "section": "Maximum inner product search retrieval", "weight": 1.0} -->

Other quantization methods may also benefit from using score-aware quantization loss. For example, binary quantization techniques such as Dai et al. use reconstruction loss in their original paper, but can be easily adapted to the proposed loss by a one line change to the loss objective. We show results which illustrate the improvement of such a change in Section 7.7 of Appendix.

<!-- chunk {"id": "body-0050", "role": "body", "section": "Recall-Speed benchmark", "weight": 1.0} -->

Fixed-bit-rate experiments mostly compare asymptotic behavior and often overlook preprocessing overhead such as learned rotation or lookup table computation, which can be substantial. To evaluate effectiveness of MIPS algorithms in a realistic setting, it is important to perform end-to-end benchmarks and compare speed-recall curves. We adopted the methodology of public benchmark ANN-Benchmarks Aumüller et al., which plots a comprehensive set of 11 algorithms for comparison, including faiss Johnson et al. and hnswlib Malkov & Yashunin.

<!-- chunk {"id": "body-0051", "role": "body", "section": "Recall-Speed benchmark", "weight": 1.0} -->

Our benchmarks are all conducted on an Intel Xeon W-2135 with a single CPU thread, and followed the benchmark's protocol. Our implementation builds on product quantization with the proposed quantization and SIMD based ADC Guo et al. for distance computation. This is further combined with a vector quantization based tree Wu et al.. Our implementation is open-source and available at and furthermore the exact configurations used to produce our benchmark numbers are part of the ANN-Benchmarks GitHub repository. Figure 4 shows our performance on Glove1.2M significantly outperforms competing methods in the high-recall region.

<!-- chunk {"id": "body-0052", "role": "body", "section": "Conclusion", "weight": 1.5} -->

In this paper, we propose a new quantization loss function for inner product search, which replaces traditional reconstruction error. The new loss function is weighted based on the inner product values, giving more weight to the pairs of query and database points with higher inner product values. The proposed loss function is theoretically proven and can be applied to a wide range of quantization methods, for example product and binary quantization. Our experiments show superior performance on retrieval recall and inner product value estimation compared to methods that use reconstruction error. The speed-recall benchmark on public datasets further indicates that the proposed method outperforms state-of-the-art baselines which are known to be hard to beat.
