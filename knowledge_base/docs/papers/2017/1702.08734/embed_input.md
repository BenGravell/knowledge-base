<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Billion-scale Similarity Search with GPUs

Topics include Graphs, Nearest neighbors, Datasets, Accuracy.

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Similarity search finds application in specialized database systems handling complex data such as images or videos, which are typically represented by high-dimensional features and require specific indexing structures. This paper tackles the problem of better utilizing GPUs for this task. While GPUs excel at data-parallel tasks, prior approaches are bottlenecked by algorithms that expose less parallelism, such as k-min selection, or make poor use of the memory hierarchy. We propose a design for k-selection that operates at up to 55% of theoretical peak performance, enabling a nearest neighbor implementation that is 8.5x faster than prior GPU state of the art. We apply it in different similarity search scenarios, by proposing optimized design for brute-force, approximate and compressed-domain search based on product quantization. In all these setups, we outperform the state of the art by large margins. Our implementation enables the construction of a high accuracy k-NN graph on 95 million images from the Yfcc100M dataset in 35 minutes, and of a graph connecting 1 billion vectors in less than 12 hours on 4 Maxwell Titan X GPUs. We have open-sourced our approach for the sake of comparison and reproducibility.

<!-- chunk {"id": "body-0003", "role": "body", "section": "Introduction", "weight": 1.5} -->

Images and videos constitute a new massive source of data for indexing and search. Extensive metadata for this content is often not available. Search and interpretation of this and other human-generated content, like text, is difficult and important. A variety of machine learning and deep learning algorithms are being used to interpret and classify these complex, real-world entities. Popular examples include the text representation known as word2vec, representations of images by convolutional neural networks, and image descriptors for instance search. Such representations or embeddings are usually real-valued, high-dimensional vectors of 50 to 1000+ dimensions. Many of these vector representations can only effectively be produced on GPU systems, as the underlying processes either have high arithmetic complexity and/or high data bandwidth demands, or cannot be effectively partitioned without failing due to communication overhead or representation quality. Once produced, their manipulation is itself arithmetically intensive. However, how to utilize GPU assets is not straightforward. More generally, how to exploit new heterogeneous architectures is a key subject for the database community.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

In this context, searching by numerical similarity rather than via structured relations is more suitable. This could be to find the most similar content to a picture, or to find the vectors that have the highest response to a linear classifier on all vectors of a collection.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

One of the most expensive operations to be performed on large collections is to compute a $k$-NN graph. It is a directed graph where each vector of the database is a node and each edge connects a node to its $k$ nearest neighbors. This is our flagship application. Note, state of the art methods like NN-Descent have a large memory overhead on top of the dataset itself and cannot readily scale to the billion-sized databases we consider.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

Such applications must deal with the curse of dimensionality, rendering both exhaustive search or exact indexing for non-exhaustive search impractical on billion-scale databases. This is why there is a large body of work on approximate search and/or graph construction. To handle huge datasets that do not fit in RAM, several approaches employ an internal compressed representation of the vectors using an encoding. This is especially convenient for memory-limited devices like GPUs. It turns out that accepting a minimal accuracy loss results in orders of magnitude of compression. The most popular vector compression methods can be classified into either binary codes, or quantization methods. Both have the desirable property that searching neighbors does not require reconstructing the vectors.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

Our paper focuses on methods based on product quantization (PQ) codes, as these were shown to be more effective than binary codes. In addition, binary codes incur important overheads for non-exhaustive search methods. Several improvements were proposed after the original product quantization proposal known as IVFADC; most are difficult to implement efficiently on GPU. For instance, the inverted multi-index, useful for high-speed/low-quality operating points, depends on a complicated "multi-sequence" algorithm. The optimized product quantization or OPQ is a linear transformation on the input vectors that improves the accuracy of the product quantization; it can be applied as a pre-processing. The SIMD-optimized IVFADC implementation from operates only with sub-optimal parameters (few coarse quantization centroids). Many other methods, like LOPQ and the Polysemous codes are too complex to be implemented efficiently on GPUs.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Introduction", "weight": 1.5} -->

There are many implementations of similarity search on GPUs, but mostly with binary codes, small datasets, or exhaustive search. To the best of our knowledge, only the work by Wieschollek et al. appears suitable for billion-scale datasets with quantization codes. This is the prior state of the art on GPUs, which we compare against in Section 6.4.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Introduction", "weight": 1.5} -->

a GPU $k$-selection algorithm, operating in fast register memory and flexible enough to be fusable with other kernels, for which we provide a complexity analysis;

<!-- chunk {"id": "body-0010", "role": "body", "section": "Introduction", "weight": 1.5} -->

a near-optimal algorithmic layout for exact and approximate $k$-nearest neighbor search on GPU;

<!-- chunk {"id": "body-0011", "role": "body", "section": "Introduction", "weight": 1.5} -->

a range of experiments that show that these improvements outperform previous art by a large margin on mid- to large-scale nearest-neighbor search tasks, in single or multi-GPU configurations.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Introduction", "weight": 1.5} -->

The paper is organized as follows. Section 2 introduces the context and notation. Section 3 reviews GPU architecture and discusses problems appearing when using it for similarity search. Section 4 introduces one of our main contributions, *i.e.*, our k-selection method for GPUs, while Section 5 provides details regarding the algorithm computation layout. Finally, Section 6 provides extensive experiments for our approach, compares it to the state of the art, and shows concrete use cases for image collections.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Problem statement", "weight": 1.0} -->

We are concerned with similarity search in vector collections. Given the query vector $x \in {\mathbb{R}}^{d}$ and the collection^22^2To avoid clutter in 0-based indexing, we use the array notation $0:\ell$ to denote the range $\{ 0,\ldots,{\ell - 1}\}$ inclusive.

<!-- chunk {"id": "body-0014", "role": "body", "section": "Problem statement", "weight": 1.0} -->

i.e., we search the $k$ nearest neighbors of $x$ in terms of L2 distance. The L2 distance is used most often, as it is optimized by design when learning several embeddings (*e.g.*, ), due to its attractive linear algebra properties.

<!-- chunk {"id": "body-0015", "role": "body", "section": "Problem statement", "weight": 1.0} -->

The lowest distances are collected by $k$-selection. For an array ${\lbrack a_{i}\rbrack}_{{i = 0}:\ell}$, $k$-selection finds the $k$ lowest valued elements ${\lbrack a_{s_{i}}\rbrack}_{{i = 0}:k}$, $a_{s_{i}} \leq a_{s_{i + 1}}$, along with the indices ${\lbrack s_{i}\rbrack}_{{i = 0}:k}$, $0 \leq s_{i} < \ell$, of those elements from the input array. The $a_{i}$ will be 32-bit floating point values; the $s_{i}$ are 32- or 64-bit integers. Other comparators are sometimes desired; *e.g.*, for cosine similarity we search for *highest* values.

<!-- chunk {"id": "body-0016", "role": "body", "section": "Problem statement", "weight": 1.0} -->

The order between equivalent keys $a_{s_{i}} = a_{s_{j}}$ is not specified.

<!-- chunk {"id": "body-0017", "role": "body", "section": "Batching", "weight": 1.0} -->

Typically, searches are performed in batches of $n_{q}$ query vectors ${\lbrack x_{j}\rbrack}_{{j = 0}:n_{q}}{({x_{j} \in {\mathbb{R}}^{d}})}$ in parallel, which allows for more flexibility when executing on multiple CPU threads or on GPU. Batching for $k$-selection entails selecting $n_{q} \times k$ elements and indices from $n_{q}$ separate arrays, where each array is of a potentially different length $\ell_{i} \geq k$.

<!-- chunk {"id": "body-0018", "role": "body", "section": "Exact search", "weight": 1.0} -->

The two first terms can be precomputed in one pass over the matrices $X$ and $Y$ whose rows are the $\lbrack x_{j}\rbrack$ and $\lbrack y_{i}\rbrack$. The bottleneck is to evaluate $\langle x_{j},y_{i}\rangle$, equivalent to the matrix multiplication $XY^{\top}$. The $k$-nearest neighbors for each of the $n_{q}$ queries are $k$-selected along each row of $D$.

<!-- chunk {"id": "body-0019", "role": "body", "section": "Compressed-domain search", "weight": 1.0} -->

From now, we focus on approximate nearest-neighbor search. We consider, in particular, the IVFADC indexing structure. The IVFADC index relies on two levels of quantization, and the database vectors are encoded.

<!-- chunk {"id": "body-0020", "role": "body", "section": "Compressed-domain search", "weight": 1.0} -->

where $q_{1}:{{\mathbb{R}}^{d}\rightarrow\mathcal{C}_{1} \subset {\mathbb{R}}^{d}}$ and $q_{2}:{{\mathbb{R}}^{d}\rightarrow\mathcal{C}_{2} \subset {\mathbb{R}}^{d}}$ are quantizers; *i.e.*, functions that output an element from a finite set. Since the sets are finite, $q{(y)}$ is encoded as the index of $q_{1}{(y)}$ and that of $q_{2}{({y - {q_{1}{(y)}}})}$. The first-level quantizer is a coarse quantizer and the second level fine quantizer encodes the residual vector after the first level.

<!-- chunk {"id": "body-0021", "role": "body", "section": "Compressed-domain search", "weight": 1.0} -->

For IVFADC the search is not exhaustive.

<!-- chunk {"id": "body-0022", "role": "body", "section": "Compressed-domain search", "weight": 1.0} -->

The multi-probe parameter $\tau$ is the number of coarse-level centroids we consider. The quantizer operates a nearest-neighbor search with exact distances, in the set of reproduction values. Then, the IVFADC search computes

<!-- chunk {"id": "body-0023", "role": "body", "section": "Compressed-domain search", "weight": 1.0} -->

Hence, IVFADC relies on the same distance estimations as the two-step quantization of ADC, but computes them only on a subset of vectors.

<!-- chunk {"id": "body-0024", "role": "body", "section": "Compressed-domain search", "weight": 1.0} -->

The corresponding data structure, the *inverted file*, groups the vectors $y_{i}$ into $|\mathcal{C}_{1}|$ *inverted lists* $\mathcal{I}_{1},\ldots,\mathcal{I}_{|\mathcal{C}_{1}|}$ with homogeneous $q_{1}{(y_{i})}$. Therefore, the most memory-intensive operation is computing $L_{IVFADC}$, and boils down to linearly scanning $\tau$ inverted lists.

<!-- chunk {"id": "body-0025", "role": "body", "section": "The quantizers", "weight": 1.0} -->

The quantizers $q_{1}$ and $q_{2}$ have different properties. $q_{1}$ needs to have a relatively low number of reproduction values so that the number of inverted lists does not explode. We typically use ${|C_{1}|} \approx \sqrt{\ell}$, trained via $k$-means. For $q_{2}$, we can afford to spend more memory for a more extensive representation. The ID of the vector (a 4- or 8-byte integer) is also stored in the inverted lists, so it makes no sense to have shorter codes than that; i.e., ${\log_{2}{|\mathcal{C}_{2}|}} > {4 \times 8}$.

<!-- chunk {"id": "body-0026", "role": "body", "section": "Product quantizer", "weight": 1.0} -->

We use a product quantizer for $q_{2}$, which provides a large number of reproduction values without increasing the processing cost. It interprets the vector $y$ as $b$ sub-vectors $y = {\lbrack{y^{0}\ldotsy^{b - 1}}\rbrack}$, where $b$ is an even divisor of the dimension $d$. Each sub-vector is quantized with its own quantizer, yielding the tuple $(q^{0}{(y^{0})},$..., $q^{b - 1}{(y^{b - 1})})$. The sub-quantizers typically have 256 reproduction values, to fit in one byte.

<!-- chunk {"id": "body-0027", "role": "body", "section": "Product quantizer", "weight": 1.0} -->

The quantization value of the product quantizer is then ${q_{2}{(y)}} = {{q^{0}{(y^{0})}} + {{256 \times q^{1}}{(y^{1})}} + \ldots + {256^{b - 1} \times q^{b - 1}}}$, which from a storage point of view is just the concatenation of the bytes produced by each sub-quantizer. Thus, the product quantizer generates $b$-byte codes with ${|\mathcal{C}_{2}|} = 256^{b}$ reproduction values. The $k$-means dictionaries of the quantizers are small and quantization is computationally cheap.

<!-- chunk {"id": "body-0028", "role": "body", "section": "GPU: overview and k-selection", "weight": 1.0} -->

This section reviews salient details of Nvidia's general-purpose GPU architecture and programming model. We then focus on one of the less GPU-compliant parts involved in similarity search, namely the $k$-selection, and discuss the literature and challenges.

<!-- chunk {"id": "body-0029", "role": "body", "section": "GPU lanes and warps", "weight": 1.0} -->

The Nvidia GPU is a general-purpose computer that executes instruction streams using a 32-wide vector of CUDA threads (the warp); individual threads in the warp are referred to as lanes, with a *lane ID* from 0 -- 31. Despite the "thread" terminology, the best analogy to modern vectorized multicore CPUs is that each warp is a separate CPU hardware thread, as the warp shares an instruction counter. Warp lanes taking different execution paths results in warp divergence, reducing performance. Each lane has up to 255 32-bit registers in a shared register file. The CPU analogy is that there are up to 255 vector registers of width 32, with warp lanes as SIMD vector lanes.

<!-- chunk {"id": "body-0030", "role": "body", "section": "Collections of warps", "weight": 1.0} -->

A user-configurable collection of 1 to 32 warps comprises a block or a co-operative thread array (CTA). Each block has a high speed shared memory, up to 48 KiB in size. Individual CUDA threads have a block-relative ID, called a thread id, which can be used to partition and assign work. Each block is run on a single core of the GPU called a streaming multiprocessor (SM). Each SM has functional units, including ALUs, memory load/store units, and various special instruction units. A GPU hides execution latencies by having many operations in flight on warps across all SMs. Each individual warp lane instruction throughput is low and latency is high, but the aggregate arithmetic throughput of all SMs together is 5 -- 10$\times$ higher than typical CPUs.

<!-- chunk {"id": "body-0031", "role": "body", "section": "Grids and kernels", "weight": 1.0} -->

Blocks are organized in a grid of blocks in a kernel. Each block is assigned a grid relative ID. The kernel is the unit of work (instruction stream with arguments) scheduled by the host CPU for the GPU to execute. After a block runs through to completion, new blocks can be scheduled. Blocks from different kernels can run concurrently. Ordering between kernels is controllable via ordering primitives such as streams and events.

<!-- chunk {"id": "body-0032", "role": "body", "section": "Resources and occupancy", "weight": 1.0} -->

The number of blocks executing concurrently depends upon shared memory and register resources used by each block. Per-CUDA thread register usage is determined at compilation time, while shared memory usage can be chosen at runtime. This usage affects occupancy on the GPU. If a block demands all 48 KiB of shared memory for its private usage, or 128 registers per thread as opposed to 32, then only 1 -- 2 other blocks can run concurrently on the same SM, resulting in low occupancy. Under high occupancy more blocks will be present across all SMs, allowing more work to be in flight at once.

<!-- chunk {"id": "body-0033", "role": "body", "section": "Memory types", "weight": 1.0} -->

Different blocks and kernels communicate through global memory, typically 4 -- 32 GB in size, with 5 -- 10$\times$ higher bandwidth than CPU main memory. Shared memory is analogous to CPU L1 cache in terms of speed. GPU register file memory is the highest bandwidth memory. In order to maintain the high number of instructions in flight on a GPU, a vast register file is also required: 14 MB in the latest Pascal P100, in contrast with a few tens of KB on CPU. A ratio of 250: 6.25: 1 for register to shared to global memory aggregate cross-sectional bandwidth is typical on GPU, yielding 10 -- 100s of TB/s for the register file.

<!-- chunk {"id": "body-0034", "role": "body", "section": "Structured register data", "weight": 1.0} -->

Shared and register memory usage involves efficiency tradeoffs; they lower occupancy but can increase overall performance by retaining a larger working set in a faster memory. Making heavy use of register-resident data at the expense of occupancy or instead of shared memory is often profitable.

<!-- chunk {"id": "body-0035", "role": "body", "section": "Structured register data", "weight": 1.0} -->

As the GPU register file is very large, storing structured data (not just temporary operands) is useful. A single lane can use its (scalar) registers to solve a local task, but with limited parallelism and storage. Instead, lanes in a GPU warp can instead exchange register data using the warp shuffle instruction, enabling warp-wide parallelism and storage.

<!-- chunk {"id": "body-0036", "role": "body", "section": "Lane-stride register array", "weight": 1.0} -->

A common pattern to achieve this is a lane-stride register array. That is, given elements ${\lbrack a_{i}\rbrack}_{{i = 0}:\ell}$, each successive value is held in a register by neighboring lanes. The array is stored in $\ell/32$ registers per lane, with $\ell$ a multiple of 32. Lane $j$ stores $\{ a_{j},a_{32 + j},\ldots,a_{{\ell - 32} + j}\}$, while register $r$ holds $\{ a_{32r},a_{{32r} + 1},\ldots,a_{{32r} + 31}\}$.

<!-- chunk {"id": "body-0037", "role": "body", "section": "Lane-stride register array", "weight": 1.0} -->

For manipulating the $\lbrack a_{i}\rbrack$, the register in which $a_{i}$ is stored (i.e., $\left\lfloor {i/32} \right\rfloor$) and $\ell$ must be known at assembly time, while the lane (i.e., $i\operatorname{mod}32$) can be runtime knowledge. A wide variety of access patterns (shift, any-to-any) are provided; we use the butterfly permutation extensively.

<!-- chunk {"id": "body-0038", "role": "body", "section": "k-selection on CPU versus GPU", "weight": 1.0} -->

$k$-selection algorithms, often for arbitrarily large $\ell$ and $k$, can be translated to a GPU, including radix selection and bucket selection, probabilistic selection, quickselect, and truncated sorts. Their performance is dominated by multiple passes over the input in global memory. Sometimes for similarity search, the input distances are computed on-the-fly or stored only in small blocks, not in their entirety. The full, explicit array might be too large to fit into any memory, and its size could be unknown at the start of the processing, rendering algorithms that require multiple passes impractical. They suffer from other issues as well. Quickselect requires partitioning on a storage of size $\mathcal{O}{(\ell)}$, a data-dependent memory movement. This can result in excessive memory transactions, or requiring parallel prefix sums to determine write offsets, with synchronization overhead. Radix selection has no partitioning but multiple passes are still required.

<!-- chunk {"id": "body-0039", "role": "body", "section": "Heap parallelism", "weight": 1.0} -->

In similarity search applications, one is usually interested only in a small number of results, $k < 1000$ or so. In this regime, selection via max-heap is a typical choice on the CPU, but heaps do not expose much data parallelism (due to serial tree update) and cannot saturate SIMD execution units. The ad-heap takes better advantage of parallelism available in heterogeneous systems, but still attempts to partition serial and parallel work between appropriate execution units. Despite the serial nature of heap update, for small $k$ the CPU can maintain all of its state in the L1 cache with little effort, and L1 cache latency and bandwidth remains a limiting factor. Other similarity search components, like PQ code manipulation, tend to have greater impact on CPU performance.

<!-- chunk {"id": "body-0040", "role": "body", "section": "GPU heaps", "weight": 1.0} -->

Heaps can be similarly implemented on a GPU. However, a straightforward GPU heap implementation suffers from high warp divergence and irregular, data-dependent memory movement, since the path taken for each inserted element depends upon other values in the heap.

<!-- chunk {"id": "body-0041", "role": "body", "section": "GPU heaps", "weight": 1.0} -->

GPU parallel priority queues improve over the serial heap update by allowing multiple concurrent updates, but they require a potential number of small sorts for each insert and data-dependent memory movement. Moreover, it uses multiple synchronization barriers through kernel launches in different streams, plus the additional latency of successive kernel launches and coordination with the CPU host.

<!-- chunk {"id": "body-0042", "role": "body", "section": "GPU heaps", "weight": 1.0} -->

Other more novel GPU algorithms are available for small $k$, namely the selection algorithm in the fgknn library. This is a complex algorithm that may suffer from too many synchronization points, greater kernel launch overhead, usage of slower memories, excessive use of hierarchy, partitioning and buffering. However, we take inspiration from this particular algorithm through the use of parallel merges as seen in their *merge queue* structure.

<!-- chunk {"id": "body-0043", "role": "body", "section": "Fast k-selection on the GPU", "weight": 1.0} -->

For any CPU or GPU algorithm, either memory or arithmetic throughput should be the limiting factor as per the roofline performance model. For input from global memory, $k$-selection cannot run faster than the time required to scan the input once at peak memory bandwidth. We aim to get as close to this limit as possible. Thus, we wish to perform a single pass over the input data (from global memory or produced on-the-fly, perhaps fused with a kernel that is generating the data).

<!-- chunk {"id": "body-0044", "role": "body", "section": "Fast k-selection on the GPU", "weight": 1.0} -->

We want to keep intermediate state in the fastest memory: the register file. The major disadvantage of register memory is that the indexing into the register file must be known at assembly time, which is a strong constraint on the algorithm.

<!-- chunk {"id": "body-0045", "role": "body", "section": "In-register sorting", "weight": 1.0} -->

We use an in-register sorting primitive as a building block. Sorting networks are commonly used on SIMD architectures, as they exploit vector parallelism. They are easily implemented on the GPU, and we build sorting networks with lane-stride register arrays.

<!-- chunk {"id": "body-0046", "role": "body", "section": "In-register sorting", "weight": 1.0} -->

We use a variant of Batcher's bitonic sorting network, which is a set of parallel merges on an array of size $2^{k}$. Each merge takes $s$ arrays of length $t$ ($s$ and $t$ a power of 2) to $s/2$ arrays of length $2t$, using $\log_{2}{(t)}$ parallel steps. A bitonic sort applies this merge recursively: to sort an array of length $\ell$, merge $\ell$ arrays of length $1$ to $\ell/2$ arrays of length $2$, to $\ell/4$ arrays of length $4$, successively to $1$ sorted array of length $\ell$, leading to $\frac{1}{2}{(\log_{2}{(\ell)}^{2} + \log_{2}{(\ell)})}$ parallel merge steps.

<!-- chunk {"id": "body-0047", "role": "body", "section": "In-register sorting", "weight": 1.0} -->

parallel for i ← 0: min (ℓL,ℓR) do
⊳ inverted 1st stage; inputs are already sorted
⊳ If ℓL = ℓR and a power-of-2, these are equivalent
h ← 2⌈log2ℓ⌉ − 1 ⊳ largest power-of-2 &lt; ℓ
⊳ Implemented with warp shuffle butterfly
if p = left then ⊳ left side recursion
else⊳ right side recursion
Algorithm 1 Odd-size merging network

<!-- chunk {"id": "body-0048", "role": "body", "section": "Odd-size merging and sorting networks", "weight": 1.0} -->

If some input data is already sorted, we can modify the network to avoid merging steps. We may also not have a full power-of-2 set of data, in which case we can efficiently shortcut to deal with the smaller size.

<!-- chunk {"id": "body-0049", "role": "body", "section": "Odd-size merging and sorting networks", "weight": 1.0} -->

Algorithm 1 is an odd-sized merging network that merges already sorted left and right arrays, each of arbitrary length. While the bitonic network merges bitonic sequences, we start with monotonic sequences: sequences sorted monotonically. A bitonic merge is made monotonic by reversing the first comparator stage.

<!-- chunk {"id": "body-0050", "role": "body", "section": "Odd-size merging and sorting networks", "weight": 1.0} -->

The odd size algorithm is derived by considering arrays to be padded to the next highest power-of-2 size with dummy elements that are never swapped (the merge is monotonic) and are already properly positioned; any comparisons with dummy elements are elided. A left array is considered to be padded with dummy elements at the start; a right array has them at the end. A merge of two sorted arrays of length $\ell_{L}$ and $\ell_{R}$ to a sorted array of $\ell_{L} + \ell_{R}$ requires $\left\lceil {\log_{2}{({\max{(\ell_{L},\ell_{R})}})}} \right\rceil + 1$ parallel steps. Figure 1 shows Algorithm 1's merging network for arrays of size 5 and 3, with 4 parallel steps.

<!-- chunk {"id": "body-0051", "role": "body", "section": "Odd-size merging and sorting networks", "weight": 1.0} -->

The compare-swap is implemented using warp shuffles on a lane-stride register array. Swaps with a stride a multiple of 32 occur directly within a lane as the lane holds both elements locally. Swaps of stride $\leq 16$ or a non-multiple of 32 occur with warp shuffles. In practice, used array lengths are multiples of 32 as they are held in lane-stride arrays.

<!-- chunk {"id": "body-0052", "role": "body", "section": "Odd-size merging and sorting networks", "weight": 1.0} -->

Algorithm 2 extends the merge to a full sort. Assuming no structure present in the input data, $\frac{1}{2}{({\left\lceil {\log_{2}{(\ell)}} \right\rceil^{2} + \left\lceil {\log_{2}{(\ell)}} \right\rceil})}$ parallel steps are required for sorting data of length $\ell$.

<!-- chunk {"id": "body-0053", "role": "body", "section": "WarpSelect", "weight": 1.0} -->

Our $k$-selection implementation, WarpSelect, maintains state entirely in registers, requires only a single pass over data and avoids cross-warp synchronization. It uses merge-odd and sort-odd as primitives. Since the register file provides much more storage than shared memory, it supports $k \leq 1024$. Each warp is dedicated to $k$-selection to a single one of the $n$ arrays $\lbrack a_{i}\rbrack$. If $n$ is large enough, a single warp per each $\lbrack a_{i}\rbrack$ will result in full GPU occupancy. Large $\ell$ per warp is handled by recursive decomposition, if $\ell$ is known in advance.

<!-- chunk {"id": "body-0054", "role": "body", "section": "Overview", "weight": 1.0} -->

Our approach (Algorithm 3 and Figure 2) operates on values, with associated indices carried along (omitted from the description for simplicity). It selects the $k$ least values that come from global memory, or from intermediate value registers if fused into another kernel providing the values. Let ${\lbrack a_{i}\rbrack}_{{i = 0}:\ell}$ be the sequence provided for selection.

<!-- chunk {"id": "body-0055", "role": "body", "section": "Overview", "weight": 1.0} -->

The elements (on the left of Figure 2) are processed in groups of 32, the warp size. Lane $j$ is responsible for processing $\{ a_{j},a_{32 + j},\ldots\}$; thus, if the elements come from global memory, the reads are contiguous and coalesced into a minimal number of memory transactions.

<!-- chunk {"id": "body-0056", "role": "body", "section": "Overview", "weight": 1.0} -->

insert a into our [Tij]i = 0: t
⊳ Reinterpret thread queues as lane-stride array
⊳ concatenate and sort thread queues
⊳ Reinterpret lane-stride array as thread queues
⊳ Back in thread queue order, invariant restored
Algorithm 3 WarpSelect pseudocode for lane j

<!-- chunk {"id": "body-0057", "role": "body", "section": "Data structures", "weight": 1.0} -->

Each lane $j$ maintains a small queue of $t$ elements in registers, called the thread queues ${\lbrack T_{i}^{j}\rbrack}_{{i = 0}:t}$, ordered from largest to smallest ($T_{i}^{j} \geq T_{i + 1}^{j}$). The choice of $t$ is made relative to $k$, see Section 4.3. The thread queue is a first-level filter for new values coming. If a new $a_{{32i} + j}$ is greater than the largest key currently in the queue, $T_{0}^{j}$, it is guaranteed that it won't be in the $k$ smallest final results.

<!-- chunk {"id": "body-0058", "role": "body", "section": "Data structures", "weight": 1.0} -->

The warp shares a lane-stride register array of $k$ smallest seen elements, ${\lbrack W_{i}\rbrack}_{{i = 0}:k}$, called the warp queue. It is ordered from smallest to largest ($W_{i} \leq W_{i + 1}$); if the requested $k$ is not a multiple of 32, we round it up. This is a second level data structure that will be used to maintain all of the $k$ smallest warp-wide seen values. The thread and warp queues are initialized to maximum sentinel values, e.g., $+ \infty$.

<!-- chunk {"id": "body-0059", "role": "body", "section": "Update", "weight": 1.0} -->

all per-lane $T_{0}^{j}$ are greater than all warp queue keys $W_{i}$

<!-- chunk {"id": "body-0060", "role": "body", "section": "Update", "weight": 1.0} -->

all $a_{i}$ seen so far in the min-$k$ are contained in either some lane's thread queue (${\lbrack T_{i}^{j}\rbrack}_{{i = 0}:{{t,j} = 0}:32}$), or in the warp queue.

<!-- chunk {"id": "body-0061", "role": "body", "section": "Update", "weight": 1.0} -->

Lane $j$ receives a new $a_{{32i} + j}$ and attempts to insert it into its thread queue. If $a_{{32i} + j} > T_{0}^{j}$, then the new pair is by definition not in the $k$ minimum, and can be rejected.

<!-- chunk {"id": "body-0062", "role": "body", "section": "Update", "weight": 1.0} -->

Otherwise, it is inserted into its proper sorted position in the thread queue, thus ejecting the old $T_{0}^{j}$. All lanes complete doing this with their new received pair and their thread queue, but it is now possible that the second invariant have been violated. Using the warp ballot instruction, we determine if any lane has violated the second invariant. If not, we are free to continue processing new elements.

<!-- chunk {"id": "body-0063", "role": "body", "section": "Restoring the invariants", "weight": 1.0} -->

If any lane has its invariant violated, then the warp uses odd-merge to merge and sort the thread and warp queues together. The new warp queue will be the min-$k$ elements across the merged, sorted queues, and the new thread queues will be the remainder, from min-$({k + 1})$ to min-$({k + {32t} + 1})$. This restores the invariants and we are free to continue processing subsequent elements.

<!-- chunk {"id": "body-0064", "role": "body", "section": "Restoring the invariants", "weight": 1.0} -->

Since the thread and warp queues are already sorted, we merge the sorted warp queue of length $k$ with 32 sorted arrays of length $t$. Supporting odd-sized merges is important because Batcher's formulation would require that ${32t} = k$ and is a power-of-2; thus if $k = 1024$, $t$ must be 32. We found that the optimal $t$ is way smaller (see below).

<!-- chunk {"id": "body-0065", "role": "body", "section": "Restoring the invariants", "weight": 1.0} -->

Using odd-merge to merge the 32 already sorted thread queues would require a struct-of-arrays to array-of-structs transposition in registers across the warp, since the $t$ successive sorted values are held in different registers in the same lane rather than a lane-stride array. This is possible, but would use a comparable number of warp shuffles, so we just reinterpret the thread queue registers as an (unsorted) lane-stride array and sort from scratch. Significant speedup is realizable by using odd-merge for the merge of the aggregate sorted thread queues with the warp queue.

<!-- chunk {"id": "body-0066", "role": "body", "section": "Handling the remainder", "weight": 1.0} -->

If there are remainder elements because $\ell$ is not a multiple of 32, those are inserted into the thread queues for the lanes that have them, after which we proceed to the output stage.

<!-- chunk {"id": "body-0067", "role": "body", "section": "Output", "weight": 1.0} -->

A final sort and merge is made of the thread and warp queues, after which the warp queue holds all min-$k$ values.

<!-- chunk {"id": "body-0068", "role": "body", "section": "Complexity and parameter selection", "weight": 1.0} -->

read 32 elements, compare to all thread queue heads $T_{0}^{j}$, cost $C_{1}$, happens $N_{1}$ times;

<!-- chunk {"id": "body-0069", "role": "body", "section": "Computation layout", "weight": 1.0} -->

This section explains how IVFADC, one of the indexing methods originally built upon product quantization, is implemented efficiently. Details on distance computations and articulation with $k$-selection are the key to understanding why this method can outperform more recent GPU-compliant approximate nearest neighbor strategies.

<!-- chunk {"id": "body-0070", "role": "body", "section": "Exact search", "weight": 1.0} -->

We briefly come back to the exhaustive search method, often referred to as exact brute-force. It is interesting on its own for exact nearest neighbor search in small datasets. It is also a component of many indexes in the literature. In our case, we use it for the IVFADC coarse quantizer $q_{1}$.

<!-- chunk {"id": "body-0071", "role": "body", "section": "Exact search", "weight": 1.0} -->

As stated in Section 2, the distance computation boils down to a matrix multiplication. We use optimized GEMM routines in the cuBLAS library to calculate the $- {2{\langle x_{j},y_{i}\rangle}}$ term for L2 distance, resulting in a partial distance matrix $D^{\prime}$. To complete the distance calculation, we use a fused $k$-selection kernel that adds the ${\| y_{i}\|}^{2}$ term to each entry of the distance matrix and immediately submits the value to $k$-selection in registers. The ${\| x_{j}\|}^{2}$ term need not be taken into account before $k$-selection. Kernel fusion thus allows for only 2 passes (GEMM write, $k$-select read) over $D^{\prime}$, compared to other implementations that may require 3 or more. Row-wise $k$-selection is likely not fusable with a well-tuned GEMM kernel, or would result in lower overall efficiency.

<!-- chunk {"id": "body-0072", "role": "body", "section": "Exact search", "weight": 1.0} -->

As $D^{\prime}$ does not fit in GPU memory for realistic problem sizes, the problem is tiled over the batch of queries, with $t_{q} \leq n_{q}$ queries being run in a single tile. Each of the $\left\lceil {n_{q}/t_{q}} \right\rceil$ tiles are independent problems, but we run two in parallel on different streams to better occupy the GPU, so the effective memory requirement of $D$ is $\mathcal{O}{({2\ellt_{q}})}$. The computation can similarly be tiled over $\ell$. For very large input coming from the CPU, we support buffering with pinned memory to overlap CPU to GPU copy with GPU compute.

<!-- chunk {"id": "body-0073", "role": "body", "section": "PQ lookup tables", "weight": 1.0} -->

At its core, the IVFADC requires computing the distance from a vector to a set of product quantization reproduction values.

<!-- chunk {"id": "body-0074", "role": "body", "section": "PQ lookup tables", "weight": 1.0} -->

Each quantizer $q^{1},\ldots,q^{b}$ has 256 reproduction values, so when $x$ and $q_{1}{(y)}$ are known all distances can be precomputed and stored in tables $T_{1},\ldots,T_{b}$ each of size 256. Computing the sum consists of $b$ look-ups and additions.

<!-- chunk {"id": "body-0075", "role": "body", "section": "PQ lookup tables", "weight": 1.0} -->

With lookup tables: $256 \times d$ multiply-adds and $n \times b$ lookup-adds.

<!-- chunk {"id": "body-0076", "role": "body", "section": "PQ lookup tables", "weight": 1.0} -->

This is the key to the efficiency of the product quantizer. In our GPU implementation, $b$ is any multiple of 4 up to 64. The codes are stored as sequential groups of $b$ bytes per vector within lists.

<!-- chunk {"id": "body-0077", "role": "body", "section": "IVFADC lookup tables", "weight": 1.0} -->

When scanning over the elements of the inverted list $\mathcal{I}_{L}$ (where by definition $q_{1}{(y)}$ is constant), the look-up table method can be applied, as the query $x$ and $q_{1}{(y)}$ are known.

<!-- chunk {"id": "body-0078", "role": "body", "section": "IVFADC lookup tables", "weight": 1.0} -->

Moreover, the computation of the tables $T_{1}\ldotsT_{b}$ is further optimized.

<!-- chunk {"id": "body-0079", "role": "body", "section": "IVFADC lookup tables", "weight": 1.0} -->

The objective is to minimize inner loop computations.

<!-- chunk {"id": "body-0080", "role": "body", "section": "IVFADC lookup tables", "weight": 1.0} -->

Term 1 is independent of the query. It can be precomputed from the quantizers, and stored in a table $\mathcal{T}$ of size ${|\mathcal{C}_{1}|} \times 256 \times b$;

<!-- chunk {"id": "body-0081", "role": "body", "section": "IVFADC lookup tables", "weight": 1.0} -->

Term 2 is the distance to $q_{1}$'s reproduction value. It is thus a by-product of the first-level quantizer $q_{1}$;

<!-- chunk {"id": "body-0082", "role": "body", "section": "IVFADC lookup tables", "weight": 1.0} -->

Term 3 can be computed independently of the inverted list. Its computation costs $d \times 256$ multiply-adds.

<!-- chunk {"id": "body-0083", "role": "body", "section": "IVFADC lookup tables", "weight": 1.0} -->

This decomposition is used to produce the lookup tables $T_{1}\ldotsT_{b}$ used during the scan of the inverted list. For a single query, computing the $\tau \times b$ tables from scratch costs $\tau \times d \times 256$ multiply-adds, while this decomposition costs $256 \times d$ multiply-adds and $\tau \times b \times 256$ additions. On the GPU, the memory usage of $\mathcal{T}$ can be prohibitive, so we enable the decomposition only when memory is a not a concern.

<!-- chunk {"id": "body-0084", "role": "body", "section": "GPU implementation", "weight": 1.0} -->

Algorithm 4 summarizes the process as one would implement it on a CPU. The inverted lists are stored as two separate arrays, for PQ codes and associated IDs. IDs are resolved only if $k$-selection determines $k$-nearest membership. This lookup yields a few sparse memory reads in a large array, thus the IDs can optionally be stored on CPU for tiny performance cost.

<!-- chunk {"id": "body-0085", "role": "body", "section": "List scanning", "weight": 1.0} -->

A kernel is responsible for scanning the $\tau$ closest inverted lists for each query, and calculating the per-vector pair distances using the lookup tables $T_{i}$. The $T_{i}$ are stored in shared memory: up to $n_{q} \times \tau \times {\max_{i}{{|\mathcal{I}_{i}|} \times b}}$ lookups are required for a query set (trillions of accesses in practice), and are random access. This limits $b$ to at most 48 (32-bit floating point) or 96 (16-bit floating point) with current architectures. In case we do not use the decomposition of Equation, the $T_{i}$ are calculated by a separate kernel before scanning.

<!-- chunk {"id": "body-0086", "role": "body", "section": "Multi-pass kernels", "weight": 1.0} -->

Each $n_{q} \times \tau$ pairs of query against inverted list can be processed independently. At one extreme, a block is dedicated to each of these, resulting in up to $n_{q} \times \tau \times {\max_{i}{|\mathcal{I}_{i}|}}$ partial results being written back to global memory, which is then $k$-selected to $n_{q} \times k$ final results. This yields high parallelism but can exceed available GPU global memory; as with exact search, we choose a tile size $t_{q} \leq n_{q}$ to reduce memory consumption, bounding its complexity by $\mathcal{O}{({2t_{q}\tau{\max_{i}{|\mathcal{I}_{i}|}}})}$ with multi-streaming.

<!-- chunk {"id": "body-0087", "role": "body", "section": "Multi-pass kernels", "weight": 1.0} -->

A single warp could be dedicated to $k$-selection of each $t_{q}$ set of lists, which could result in low parallelism. We introduce a two-pass $k$-selection, reducing $t_{q} \times \tau \times {\max_{i}{|\mathcal{I}_{i}|}}$ to $t_{q} \times f \times k$ partial results for some subdivision factor $f$. This is reduced again via $k$-selection to the final $t_{q} \times k$ results.

<!-- chunk {"id": "body-0088", "role": "body", "section": "Fused kernel", "weight": 1.0} -->

As with exact search, we experimented with a kernel that dedicates a single block to scanning all $\tau$ lists for a single query, with $k$-selection fused with distance computation. This is possible as WarpSelect does not fight for the shared memory resource which is severely limited. This reduces global memory write-back, since almost all intermediate results can be eliminated. However, unlike $k$-selection overhead for exact computation, a significant portion of the runtime is the gather from the $T_{i}$ in shared memory and linear scanning of the $\mathcal{I}_{i}$ from global memory; the write-back is not a dominant contributor. Timing for the fused kernel is improved by at most 15%, and for some problem sizes would be subject to lower parallelism and worse performance without subsequent decomposition. Therefore, and for reasons of implementation simplicity, we do not use this layout.

<!-- chunk {"id": "body-0089", "role": "body", "section": "Fused kernel", "weight": 1.0} -->

function ivfpq-search([x1, …, xnq], ℐ1, …, ℐ|𝒞1|)
for i ← 0: nq do ⊳ batch quantization of Section 5.1
Compute term 3 (see Section 5.2)
for L in LIVFi do ⊳ τ loops
Compute distance tables T1, …, Tb
⊳ distance estimation, Equation
Ri← k-select smallest distances d from L
Algorithm 4 IVFPQ batch search routine

<!-- chunk {"id": "body-0090", "role": "body", "section": "Multi-GPU parallelism", "weight": 1.0} -->

Modern servers can support several GPUs. We employ this capability for both compute power and memory.

<!-- chunk {"id": "body-0091", "role": "body", "section": "Replication", "weight": 1.0} -->

If an index instance fits in the memory of a single GPU, it can be replicated across $\mathcal{R}$ different GPUs. To query $n_{q}$ vectors, each replica handles a fraction $n_{q}/\mathcal{R}$ of the queries, joining the results back together on a single GPU or in CPU memory. Replication has near linear speedup, except for a potential loss in efficiency for small $n_{q}$.

<!-- chunk {"id": "body-0092", "role": "body", "section": "Sharding", "weight": 1.0} -->

If an index instance does not fit in the memory of a single GPU, an index can be sharded across $\mathcal{S}$ different GPUs. For adding $\ell$ vectors, each shard receives $\ell/\mathcal{S}$ of the vectors, and for query, each shard handles the full query set $n_{q}$, joining the partial results (an additional round of $k$-selection is still required) on a single GPU or in CPU memory. For a given index size $\ell$, sharding will yield a speedup (sharding has a query of $n_{q}$ against $\ell/\mathcal{S}$ versus replication with a query of $n_{q}/\mathcal{R}$ against $\ell$), but is usually less than pure replication due to fixed overhead and cost of subsequent $k$-selection.

<!-- chunk {"id": "body-0093", "role": "body", "section": "Sharding", "weight": 1.0} -->

Replication and sharding can be used together ($\mathcal{S}$ shards, each with $\mathcal{R}$ replicas for $\mathcal{S} \times \mathcal{R}$ GPUs in total). Sharding or replication are both fairly trivial, and the same principle can be used to distribute an index across multiple machines.

<!-- chunk {"id": "body-0094", "role": "body", "section": "Experiments & Applications", "weight": 1.0} -->

This section compares our GPU $k$-selection and nearest-neighbor approach to existing libraries. Unless stated otherwise, experiments are carried out on a 2$\times$`<!-- -->`{=html}2.8GHz Intel Xeon E5-2680v2 with 4 Maxwell Titan X GPUs on CUDA 8.0.

<!-- chunk {"id": "body-0095", "role": "body", "section": "k-selection performance", "weight": 1.0} -->

We compare against two other GPU small $k$-selection implementations: the row-based Merge Queue with Buffered Search and Hierarchical Partition extracted from the fgknn library of Tang et al. and Truncated Bitonic Sort (TBiS) from Sismanis et al.. Both were extracted from their respective exact search libraries.

<!-- chunk {"id": "body-0096", "role": "body", "section": "k-selection performance", "weight": 1.0} -->

We evaluate $k$-selection for $k = 100$ and 1000 of each row from a row-major matrix $n_{q} \times \ell$ of random 32-bit floating point values on a single Titan X. The batch size $n_{q}$ is fixed at 10000, and the array lengths $\ell$ vary from 1000 to 128000. Inputs and outputs to the problem remain resident in GPU memory, with the output being of size $n_{q} \times k$, with corresponding indices. Thus, the input problem sizes range from 40 MB ($\ell$ = $1000$) to 5.12 GB ($\ell$ = $128$k). TBiS requires large auxiliary storage, and is limited to $\ell \leq 48000$ in our tests.

<!-- chunk {"id": "body-0097", "role": "body", "section": "Differences from fgknn", "weight": 1.0} -->

WarpSelect is influenced by fgknn, but has several improvements: all state is maintained in registers (no shared memory), no inter-warp synchronization or buffering is used, no "hierarchical partition", the $k$-selection can be fused into other kernels, and it uses odd-size networks for efficient merging and sorting.

<!-- chunk {"id": "body-0098", "role": "body", "section": "k-means clustering", "weight": 1.0} -->

The exact search method with $k = 1$ can be used by a $k$-means clustering method in the assignment stage, to assign $n_{q}$ training vectors to $|\mathcal{C}_{1}|$ centroids. Despite the fact that it does not use the IVFADC and $k = 1$ selection is trivial (a parallel reduction is used for the $k = 1$ case, not WarpSelect), $k$-means is a good benchmark for the clustering used to train the quantizer $q_{1}$.

<!-- chunk {"id": "body-0099", "role": "body", "section": "k-means clustering", "weight": 1.0} -->

We apply the algorithm on MNIST8m images. The 8.1M images are graylevel digits in 28x28 pixels, linearized to vectors of 784-d. We compare this $k$-means implementation to the GPU $k$-means of BIDMach, which was shown to be more efficient than several distributed $k$-means implementations that require dozens of machines^33^3BIDMach numbers from Both algorithms were run for 20 iterations. Table 1 shows that our implementation is more than 2$\times$ faster, although both are built upon cuBLAS. Our implementation receives some benefit from the $k$-selection fusion into L2 distance computation. For multi-GPU execution via replicas, the speedup is close to linear for large enough problems (3.16$\times$ for 4 GPUs with 4096 centroids). Note that this benchmark is somewhat unrealistic, as one would typically sub-sample the dataset randomly when so few centroids are requested.

<!-- chunk {"id": "body-0100", "role": "body", "section": "Large scale", "weight": 1.0} -->

We can also compare to, an approximate CPU method that clusters $10^{8}$ 128-d vectors to 85k centroids. Their clustering method runs in 46 minutes, but requires 56 minutes (at least) of pre-processing to encode the vectors. Our method performs *exact* k-means on 4 GPUs in 52 minutes without any pre-processing.

<!-- chunk {"id": "body-0101", "role": "body", "section": "Exact nearest neighbor search", "weight": 1.0} -->

We consider a classical dataset used to evaluate nearest neighbor search: Sift1M. Its characteristic sizes are $\ell = 10^{6}$, $d = 128$, $n_{q} = 10^{4}$. Computing the partial distance matrix $D^{\prime}$ costs ${n_{q} \times \ell \times d} = 1.28$ Tflop, which runs in less than one second on current GPUs. Figure 4 shows the cost of the distance computations against the cost of our tiling of the GEMM for the $- {2\left\langle x_{j},y_{i} \right\rangle}$ term of Equation 2 and the peak possible $k$-selection performance on the distance matrix of size $n_{q} \times \ell$, which additionally accounts for reading the tiled result matrix $D^{\prime}$ at peak memory bandwidth.

<!-- chunk {"id": "body-0102", "role": "body", "section": "Exact nearest neighbor search", "weight": 1.0} -->

In addition to our method from Section 5, we include times from the two GPU libraries evaluated for $k$-selection performance in Section 6.1.

<!-- chunk {"id": "body-0103", "role": "body", "section": "Exact nearest neighbor search", "weight": 1.0} -->

for $k$-selection, the naive algorithm that sorts the full result array for each query using `thrust::sort_by_key` is more than $10 \times$ slower than the comparison methods;

<!-- chunk {"id": "body-0104", "role": "body", "section": "Exact nearest neighbor search", "weight": 1.0} -->

L2 distance and $k$-selection cost is dominant for all but our method, which has 85 % of the peak possible performance, assuming GEMM usage and our tiling of the partial distance matrix $D^{\prime}$ on top of GEMM is close to optimal. The cuBLAS GEMM itself has low efficiency for small reduction sizes ($d = 128$);

<!-- chunk {"id": "body-0105", "role": "body", "section": "Exact nearest neighbor search", "weight": 1.0} -->

Our fused L2/$k$-selection kernel is important. Our same exact algorithm without fusion (requiring an additional pass through $D^{\prime}$) is at least 25% slower.

<!-- chunk {"id": "body-0106", "role": "body", "section": "Exact nearest neighbor search", "weight": 1.0} -->

Efficient $k$-selection is even more important in situations where approximate methods are used to compute distances, because the relative cost of $k$-selection with respect to distance computation increases.

<!-- chunk {"id": "body-0107", "role": "body", "section": "Billion-scale approximate search", "weight": 1.0} -->

There are few studies on GPU-based approximate nearest-neighbor search on large datasets ($\ell \gg 10^{6}$). We report a few comparison points here on index search, using standard datasets and evaluation protocol in this field.

<!-- chunk {"id": "body-0108", "role": "body", "section": "SIFT1M", "weight": 1.0} -->

For the sake of completeness, we first compare our GPU search speed on Sift1M with the implementation of Wieschollek et al.. They obtain a nearest neighbor recall at 1 (fraction of queries where the true nearest neighbor is in the top 1 result) of R@1 = 0.51, and R@100 = 0.86 in 0.02 ms per query on a Titan X. For the same time budget, our implementation obtains R@1 = 0.80 and R@100 = 0.95.

<!-- chunk {"id": "body-0109", "role": "body", "section": "SIFT1B", "weight": 1.0} -->

We compare again with Wieschollek et al., on the Sift1B dataset of 1 billion SIFT image features at $n_{q} = 10^{4}$. We compare the search performance in terms of same memory usage for similar accuracy (more accurate methods may involve greater search time or memory usage). On a single GPU, with $m = 8$ bytes per vector, R@10 = 0.376 in 17.7 $\mu$s per query vector, versus their reported R@10 = 0.35 in 150 $\mu$s per query vector. Thus, our implementation is more accurate at a speed 8.5$\times$ faster.

<!-- chunk {"id": "body-0110", "role": "body", "section": "DEEP1B", "weight": 1.0} -->

We also experimented on the Deep1B dataset of $\ell$=1 billion CNN representations for images at $n_{q} = 10^{4}$. The paper that introduces the dataset reports CPU results (1 thread): R@1 = 0.45 in 20 ms search time per vector. We use a PQ encoding of $m = 20$, with $d = 80$ via OPQ, and ${|\mathcal{C}_{1}|} = 2^{18}$, which uses a comparable dataset storage as the original paper (20 GB). This requires multiple GPUs as it is too large for a single GPU's global memory, so we consider 4 GPUs with $\mathcal{S} = 2$, $\mathcal{R} = 2$. We obtain a R@1 = 0.4517 in 0.0133 ms per vector. While the hardware platforms are different, it shows that making searches on GPUs is a game-changer in terms of speed achievable on a single machine.

<!-- chunk {"id": "body-0111", "role": "body", "section": "The k-NN graph", "weight": 1.0} -->

An example usage of our similarity search method is to construct a $k$-nearest neighbor graph of a dataset via brute force (all vectors queried against the entire index).

<!-- chunk {"id": "body-0112", "role": "body", "section": "Experimental setup", "weight": 1.0} -->

We evaluate the trade-off between speed, precision and memory on two datasets: 95 million images from the Yfcc100M dataset and Deep1B. For Yfcc100M, we compute CNN descriptors as the one-before-last layer of a ResNet, reduced to $d$ = 128 with PCA.

<!-- chunk {"id": "body-0113", "role": "body", "section": "Experimental setup", "weight": 1.0} -->

Speed: How much time it takes to build the IVFADC index from scratch and construct the whole $k$-NN graph ($k = 10$) by searching nearest neighbors for all vectors in the dataset. Thus, this is an end-to-end test that includes indexing as well as search time;

<!-- chunk {"id": "body-0114", "role": "body", "section": "Experimental setup", "weight": 1.0} -->

Quality: We sample 10,000 images for which we compute the exact nearest neighbors. Our accuracy measure is the fraction of 10 found nearest neighbors that are within the ground-truth 10 nearest neighbors.

<!-- chunk {"id": "body-0115", "role": "body", "section": "Experimental setup", "weight": 1.0} -->

For Yfcc100M, we use a coarse quantizer ($2^{16}$ centroids), and consider $m =$ 16, 32 and 64 byte PQ encodings for each vector. For Deep1B, we pre-process the vectors to $d = 120$ via OPQ, use ${|\mathcal{C}_{1}|} = 2^{18}$ and consider $m =$ 20, 40. For a given encoding, we vary $\tau$ from 1 to 256, to obtain trade-offs between efficiency and quality, as seen in Figure 5.

<!-- chunk {"id": "body-0116", "role": "body", "section": "Discussion", "weight": 1.5} -->

For Yfcc100M we used $\mathcal{S} = 1$, $\mathcal{R} = 4$. An accuracy of more than 0.8 is obtained in 35 minutes. For Deep1B, a lower-quality graph can be built in 6 hours, with higher quality in about half a day. We also experimented with more GPUs by doubling the replica set, using 8 Maxwell M40s (the M40 is roughly equivalent in performance to the Titan X). Performance is improved sub-linearly ($\sim 1.6 \times$ for $m = 20$, $\sim 1.7 \times$ for $m = 40$).

<!-- chunk {"id": "body-0117", "role": "body", "section": "Discussion", "weight": 1.5} -->

For comparison, the largest $k$-NN graph construction we are aware of used a dataset comprising 36.5 million 384-d vectors, which took a cluster of 128 CPU servers 108.7 hours of compute, using NN-Descent. Note that NN-Descent could also build or refine the $k$-NN graph for the datasets we consider, but it has a large memory overhead over the graph storage, which is already 80 GB for Deep1B. Moreover it requires random access across all vectors (384 GB for Deep1B).

<!-- chunk {"id": "body-0118", "role": "body", "section": "Discussion", "weight": 1.5} -->

The largest GPU $k$-NN graph construction we found is a brute-force construction using exact search with GEMM, of a dataset of 20 million 15,000-d vectors, which took a cluster of 32 Tesla C2050 GPUs 10 days. Assuming computation scales with GEMM cost for the distance matrix, this approach for Deep1B would take an impractical 200 days of computation time on their cluster.

<!-- chunk {"id": "body-0119", "role": "body", "section": "Using the k-NN graph", "weight": 1.0} -->

When a $k$-NN graph has been constructed for an image dataset, we can find paths in the graph between any two images, provided there is a single connected component (this is the case). For example, we can search the shortest path between two images of flowers, by propagating neighbors from a starting image to a destination image. Denoting by $S$ and $D$ the source and destination images, and $d_{ij}$ the distance between nodes, we search the path $P = {\{ p_{1},\ldots,p_{n}\}}$ with $p_{1} = S$ and $p_{n} = D$ such that

<!-- chunk {"id": "body-0120", "role": "body", "section": "Using the k-NN graph", "weight": 1.0} -->

i.e., we want to favor smooth transitions. An example result is shown in Figure 6 from Yfcc100M^44^4The mapping from vectors to images is not available for Deep1B. It was obtained after 20 seconds of propagation in a $k$-NN graph with $k = 15$ neighbors. Since there are many flower images in the dataset, the transitions are smooth.

<!-- chunk {"id": "body-0121", "role": "body", "section": "Conclusion", "weight": 1.5} -->

The arithmetic throughput and memory bandwidth of GPUs are well into the teraflops and hundreds of gigabytes per second. However, implementing algorithms that approach these performance levels is complex and counter-intuitive. In this paper, we presented the algorithmic structure of similarity search methods that achieves near-optimal performance on GPUs.

<!-- chunk {"id": "body-0122", "role": "body", "section": "Conclusion", "weight": 1.5} -->

This work enables applications that needed complex approximate algorithms before. For example, the approaches presented here make it possible to do exact $k$-means clustering or to compute the $k$-NN graph with simple brute-force approaches in less time than a CPU (or a cluster of them) would take to do this approximately.

<!-- chunk {"id": "body-0123", "role": "body", "section": "Conclusion", "weight": 1.5} -->

GPU hardware is now very common on scientific workstations, due to their popularity for machine learning algorithms. We believe that our work further demonstrates their interest for database applications. Along with this work, we are publishing a carefully engineered implementation of this paper's algorithms, so that these GPUs can now also be used for efficient similarity search.
