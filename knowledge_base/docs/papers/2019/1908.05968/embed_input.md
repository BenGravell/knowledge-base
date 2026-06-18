<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

N2D: (Not Too) Deep Clustering via Clustering the Local Manifold of an Autoencoded Embedding

Topics include Neural networks, Autoencoders, Representation learning, Clustering, Datasets, Learning, N2D.

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Deep clustering has increasingly been demonstrating superiority over conventional shallow clustering algorithms. Deep clustering algorithms usually combine representation learning with deep neural networks to achieve this performance, typically optimizing a clustering and non-clustering loss. In such cases, an autoencoder is typically connected with a clustering network, and the final clustering is jointly learned by both the autoencoder and clustering network. Instead, we propose to learn an autoencoded embedding and then search this further for the underlying manifold. For simplicity, we then cluster this with a shallow clustering algorithm, rather than a deeper network. We study a number of local and global manifold learning methods on both the raw data and autoencoded embedding, concluding that UMAP in our framework is best able to find the most clusterable manifold in the embedding, suggesting local manifold learning on an autoencoded embedding is effective for discovering higher quality discovering clusters. We quantitatively show across a range of image and time-series datasets that our method has competitive performance against the latest deep clustering algorithms, including out-performing current state-of-the-art on several.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

We postulate that these results show a promising research direction for deep clustering. The code can be found at

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

Clustering is a fundamental pillar of unsupervised machine learning. It is widely used in a range of tasks across disciplines and well-known algorithms such as $k$-means have found success in many applications. For example, in science, data exploration and understanding is a fundamental task which clustering facilitates by uncovering the hidden structure of the data. However, $k$-means, along with many conventional clustering algorithms such as Gaussian Mixture Models (GMMs), DBSCAN, and hierarchical algorithms typically require hand engineered features to be created for each dataset and task. Further, these features may then be analysed using another process, feature selection, in order to eliminate redundant or poor quality features. This task is even more challenging in the unsupervised setting. Additionally, it is a time-consuming and brittle process, with the choice of features having a large influence over the subsequent performance of the clustering algorithm.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

However, recent advances in deep learning have paved the way for algorithms which can effectively learn from raw data, bypassing the need for manual feature extraction and selection. One such popular method which learns powerful representations of the data automatically is an autoencoder. Autoencoders effectively seek to learn the intrinsic structure of the data with a deep neural network, and do so by learning to reconstruct the original data, regularized for example, via a bottleneck inducing a compressed representation. This representation learned from the raw data is then typically used in a range of tasks, such as an input to a supervised classifier.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

This line of research has also impacted the unsupervised domain, where deep clustering has become a popular area of study. Deep clustering refers to the process of clustering with deep neural networks, typically with features automatically learned from the raw data by CNNs or autoencoders and clustered with a deep neural network.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

These algorithms have reported large performance gains on various benchmark tasks over conventional non-deep clustering algorithms. For example, Guo et al. pre-train an autoencoder, then initialize the weights of a deep clustering network with $k$-means. Following this, the autoencoder continues to learn a representation, but jointly with the clustering network which seeks a good clustering.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Introduction", "weight": 1.5} -->

In this work, we propose a simple approach, N2D, that effectively replaces the clustering network with a manifold learning technique on top of the autoencoded representation. Specifically, we intend for it to find a distance preserving manifold within this representation. Given this updated embedding, we can then cluster it with conventional non-deep clustering algorithms. By doing so, N2D replaces the complexity of the clustering network with a manifold learning method and straightforward non-deep clustering algorithm, reducing the deepness of the deep clustering, yet achieving superior performance via the extra manifold learning step.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Introduction", "weight": 1.5} -->

One important question is which manifold learning technique to apply to the autoencoded representation. There are many possible methods, such as the well-known Principal Component Analysis (PCA). PCA seeks to learn a linear transformation of data into a new space, typically via the use of eigendecomposition of the covariance matrix, or by computing the Singular Value Decomposition (SVD) of the data. However, PCA is a linear method and does not perform well in cases where relationships are non-linear. Thankfully, alternative non-linear manifold learning methods exist, and can be categorised by their focus on finding local or global structure. Well known globally focused methods include Isomap, while t-SNE is a well known locally focused method. More recently, UMAP has been proposed, which while also local, has been shown to better preserve global structure. All of these methods seek to utilize the distances between points in order to better learn the underlying structure, and we posit that they will improve the clusterability of an autoencoded embedding. To better understand this, we study the performance of each of these manifold learning methods on both the raw data and the autoencoded embedding.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Introduction", "weight": 1.5} -->

Thus, we propose a framework, N2D, where in contrast to recent deep clustering techniques, we replace the deep clustering network with a manifold learning method, and shallow cluster the resulting re-embedded space. We empirically observe that this method is competitive (top-3) with state-of-the-art deep clustering algorithms across a range of datasets. Further, we observe that it out-performs state-of-the-art algorithms on several others. Code and weights to reproduce the results are available at

<!-- chunk {"id": "body-0011", "role": "body", "section": "Method", "weight": 1.0} -->

Our method relies primarily on the combination of two different manifold learning methods. The first is an autoencoder, which while learning a representation, does not explicitly take local structure into account. We will show that by augmenting the autoencoder with a manifold learning technique which explicitly takes local structure into account, we can increase the quality of the representation learned in terms of clusterability.

<!-- chunk {"id": "body-0012", "role": "body", "section": "III-A Autoencoder", "weight": 1.0} -->

An autoencoder is a deep neural network consisting of two key components. The first is the encoder, which attempts to learn a function which maps the input $x$ to a new feature vector ($h = {f{(x)}}$). The second component is the decoder, which attempts to learn a function which maps the learned feature space back to the original input space ($r = {g{(h)}}$. In other words, it is a neural network which attempts to copy its input to its output. This is typically achieved via a form of regularization, for example by forcing the network to compress the input into a lower dimensional space.

<!-- chunk {"id": "body-0013", "role": "body", "section": "III-A Autoencoder", "weight": 1.0} -->

The learning process can be described as minimizing the loss function $L{(x,{g{({f{(x)}})}})}$, where $L$ is a function which penalizes $g{({f{(x)}})}$ for being dissimilar to $x$. One such loss may be the Mean Squared Error (MSE).

<!-- chunk {"id": "body-0014", "role": "body", "section": "III-A Autoencoder", "weight": 1.0} -->

While autoencoders have been shown to perform well at many feature representation tasks, they do not explicitly preserve the distances of the data in the representation that they learn. We believe that by taking this into account we can improve the quality of the clusters found.

<!-- chunk {"id": "body-0015", "role": "body", "section": "III-B Isomap", "weight": 1.0} -->

There are a multitude of manifold learning techniques that explicitly seek to preserve distances within the data. Isomap is a nonlinear method which extends multidimensional scaling (MDS) to incorporate geodesic distances imposed by a weighted graph. Geodesic distance is the distance between two points measured over the manifold, and thus by using the geodesic distance Isomap can learn the manifold structure. A k-nearest neighbourhood graph is constructed from the data, where the shortest distance between two nodes is considered the geodesic distance. Isomap constructs a global pairwise geodesic similarity matrix between all points in the data, on which classical scaling is applied. Thus, Isomap can be considered a global manifold learning technique as it seeks to retain the global structure of the data. While Isomap is a global approach and our hypothesis is that a learning a local manifold on the autoencoded embedding will lead to better results, we will investigate the use of Isomap within N2D, specifically to understand how a global method performs and test our hypothesis.

<!-- chunk {"id": "body-0016", "role": "body", "section": "III-B Isomap", "weight": 1.0} -->

We consider Isomap to have two key parameters in our setting, the first is the number of components, which is the top $n$ eigenvectors of the geodesic distance matrix which represent the co-ordinates in the new space. The next parameter of importance is the number of neighbours to consider, which is simply the number of $k$-nearest neighbours to consider as local to a point.

<!-- chunk {"id": "body-0017", "role": "body", "section": "III-C t-SNE", "weight": 1.0} -->

t-SNE (t-distributed Stochastic Neighbor Embedding) is a nonlinear method with a specific objective of optimizing local distances when creating the embedding. The first stage of the t-SNE algorithm is to construct a probability distribution over pairs within the data in such away that similar points will have a high probability of being chosen while dissimilar points have an extremely low probability of being chosen. In the second stage t-SNE defines a probability distribution over the mapped points, minimising the Kullback--Leibler (KL) divergence between the two distributions.

<!-- chunk {"id": "body-0018", "role": "body", "section": "III-C t-SNE", "weight": 1.0} -->

As with Isomap, t-SNE can choose the number of components in which to embed the data. It also requires a perplexity value which is related to the number of nearest neighbours used in Isomap. However, t-SNE is typically not very sensitive to this value.

<!-- chunk {"id": "body-0019", "role": "body", "section": "III-D UMAP", "weight": 1.0} -->

A recently proposed manifold learning method is UMAP (Uniform Manifold Approximation and Projection), which seeks to accurately represent local structure, but has been shown to also better incorporating global structure. Compared to t-SNE it has a number of benefits to motivate the comparison with t-SNE in our framework. While t-SNE typically struggles with large datasets, UMAP has been shown to scale well. Further, as UMAP better preserves global structure, while remaining focused on preserving distances within local neighbourhoods, it may inherit benefits from both local and global methods.

<!-- chunk {"id": "body-0020", "role": "body", "section": "III-D UMAP", "weight": 1.0} -->

UMAP relies on three assumptions, namely that the data is uniformly distributed on a Riemannian manifold, that the Riemannian metric is locally constant and that the manifold is locally connected. From these assumptions it is possible to model the manifold with a fuzzy topological structure. The embedding is found by searching for a low dimensional projection of the data that has the closest possible equivalent fuzzy topological structure.

<!-- chunk {"id": "body-0021", "role": "body", "section": "III-D UMAP", "weight": 1.0} -->

UMAP is similar to Isomap in that it uses a k-neighbour based graph algorithm to compute the nearest neighbours of points. At a high level, UMAP first constructs a weighted k-neighbour graph, and from this graph a low dimensional layout is computed. This low dimensional layout is optimized to have as close a fuzzy topological representation to the original as possible based on cross entropy.

<!-- chunk {"id": "body-0022", "role": "body", "section": "III-D UMAP", "weight": 1.0} -->

It has a number of important hyperparameters that influence performance. The first is the number of neighbours to consider as local. This represents the trade-off between the granularity of how much local structure is preserved and how much of the global structure is captured. As we are primarily concerned with the integration of local structure into our embedding, we will typically choose lower values for the number of neighbours. The second is the dimensionality of the target embedding. In our method we set the dimensionality to be the number of clusters we are seeking to find. UMAP also requires the minimum allowed separation between points in the embedding space. Lower values of this minimum distance will more accurately capture the true manifold structure, but may lead to dense clouds that make visualization difficult.

<!-- chunk {"id": "body-0023", "role": "body", "section": "III-E N2D", "weight": 1.0} -->

We posit that by learning the manifold of the autoencoded embedding, specifically learning a manifold with a specific emphasis on locality, we can achieve a more cluster friendly embedding. However, as there is generally no ability to cross-validate hyperparameters in the unsupervised setting, it is therefore important to choose sensible default parameters for each approach. For all manifold learning methods, we set the number of components or dimensions to be the number of clusters in the data. For Isomap and UMAP we consider the number of neighbours to be an important parameter, and we set it to a sensible default value of 5 for Isomap, and 20 for UMAP. UMAP also has another parameter we believe will be influential, which is the minimum distance between points. We believe that a default minimum distance of 0 is ideal for our method, as our prime motivation is not visualization and thus a more accurate representation of the true manifold is preferred.

<!-- chunk {"id": "body-0024", "role": "body", "section": "III-E N2D", "weight": 1.0} -->

Apply an autoencoder to the raw data to learn an initial representation.

<!-- chunk {"id": "body-0025", "role": "body", "section": "III-E N2D", "weight": 1.0} -->

We re-embed the autoencoded embedding by searching for a more clusterable manifold with a manifold learning method which preserves local distances.

<!-- chunk {"id": "body-0026", "role": "body", "section": "III-E N2D", "weight": 1.0} -->

Finally, given this new, more clusterable embedding, we apply a final shallow clustering algorithm to discover the clusters.

<!-- chunk {"id": "body-0027", "role": "body", "section": "III-E N2D", "weight": 1.0} -->

More concisely, we may also simply represent N2D as

<!-- chunk {"id": "body-0028", "role": "body", "section": "III-E N2D", "weight": 1.0} -->

where $C$ is the final clustering, $F_{C}$ is the clustering algorithm, $F_{M}$ is the manifold learner, $F_{A}$ is the autoencoder and $X$ is the original data.

<!-- chunk {"id": "body-0029", "role": "body", "section": "III-E N2D", "weight": 1.0} -->

We will study three manifold learning methods to understand the effect of the various approaches when applied to both the raw data and the autoencoded embedding, showing how one specific method, UMAP, achieves superior performance when applied to the embedding. On the question of why combine an autoencoder with a manifold learning method, we will demonstrate empirically in Section IV-D Deep Clustering via Clustering the Local Manifold of an Autoencoded Embedding") the contribution of each step to the overall performance, showing how this step can significantly increase performance. We will also demonstrate in Section IV-D Deep Clustering via Clustering the Local Manifold of an Autoencoded Embedding") how it is competitive with the state-of-the-art across a range of datasets, both image and time-series, and itself achieves state-of-the-art results on several.

<!-- chunk {"id": "body-0030", "role": "body", "section": "Experiments", "weight": 1.0} -->

In order to validate our idea, we conduct experiments on a range of diverse datasets, including standard datasets used to evaluate deep clustering algorithms.

<!-- chunk {"id": "body-0031", "role": "body", "section": "IV-A Datasets", "weight": 1.0} -->

MNIST: A traditional benchmark dataset consisting of 70,000 handwritten digits belong to 10 different classes.

<!-- chunk {"id": "body-0032", "role": "body", "section": "IV-A Datasets", "weight": 1.0} -->

MNIST-test: A subset of the MNIST dataset, containing only the test set of 10,000 images.

<!-- chunk {"id": "body-0033", "role": "body", "section": "IV-A Datasets", "weight": 1.0} -->

USPS: A dataset of 9298 images belonging to 10 different classes. Whereas MNIST images are 28x28, these images are 16x16.

<!-- chunk {"id": "body-0034", "role": "body", "section": "IV-A Datasets", "weight": 1.0} -->

Fashion: A more challenging alternative to the MNIST dataset, consisting of 70,000 images of clothing, for a total of 10 classes.

<!-- chunk {"id": "body-0035", "role": "body", "section": "IV-A Datasets", "weight": 1.0} -->

pendigits: A time series dataset consisting of sampled points from a pressure sensitive tablet as ten different digits are written. Each digit is represented by 8 coordinates of the stylus when writing a specific digit. There are 10992 data points.

<!-- chunk {"id": "body-0036", "role": "body", "section": "IV-A Datasets", "weight": 1.0} -->

HAR: A time series dataset consisting of sensor data from a smart phone. It was collected from 30 people performing various activities of daily living, and contains 6 different activities; walking, walking upstairs, walking downstairs, sitting, standing and laying.

<!-- chunk {"id": "body-0037", "role": "body", "section": "IV-B Evaluation Metrics", "weight": 1.0} -->

We will use two standard evaluation metrics for validating the performance of unsupervised clustering algorithms. In both cases, values range between 0 and 1, where higher values correspond to better clustering performance.

<!-- chunk {"id": "body-0038", "role": "body", "section": "IV-B1 Accuracy", "weight": 1.0} -->

In clustering, accuracy (ACC) is defined as the best match between the ground truth and the predicted clusters.

<!-- chunk {"id": "body-0039", "role": "body", "section": "IV-B1 Accuracy", "weight": 1.0} -->

where $y$ are the ground truth labels, $c$ are the cluster labels, and $m$ enumerates mappings between clusters and labels.

<!-- chunk {"id": "body-0040", "role": "body", "section": "IV-B2 Normalized Mutual Information", "weight": 1.0} -->

The Normalized Mutual Information (NMI) can be viewed as a normalization of the mutual information to scale the results between 0 and 1, where 0 has no mutual information and 1 is perfect correlation.

<!-- chunk {"id": "body-0041", "role": "body", "section": "IV-B2 Normalized Mutual Information", "weight": 1.0} -->

where $y$ are the ground truth labels, $c$ are the cluster labels, $H$ measures the entropy, and $I$ is the mutual information between the ground truth labels and the cluster labels.

<!-- chunk {"id": "body-0042", "role": "body", "section": "IV-C Experimental Settings", "weight": 1.0} -->

We base our autoencoder on the architecture described by Xie et al., which is a fully connected Multi-Layer Perceptron (MLP). The dimensions are inspired by those chosen by van der Maaten et al. in t-SNE, which are $d$-500-500-2000-$c$, where $d$ is the dimensionality of the data and $c$ is the number of clusters. As typical with autoencoders, the decoder network is a mirror of the encoder. All layers use ReLU activation. The optimizer is Adam. We train the autoencoder on for 1000 epochs for all datasets.

<!-- chunk {"id": "body-0043", "role": "body", "section": "IV-C Experimental Settings", "weight": 1.0} -->

We use UMAP with the following default parameter set across all datasets. The number of neighbours is 20, the number of dimensions is the number of clusters, and the minimum distance between each point in the manifold is 0.

<!-- chunk {"id": "body-0044", "role": "body", "section": "IV-C Experimental Settings", "weight": 1.0} -->

We use a GMM for the final clustering algorithm, where each component has its own general covariance matrix, and there are $c$ components, where $c$ is the number of clusters.

<!-- chunk {"id": "body-0045", "role": "body", "section": "IV-E Role of Each Component of N2D", "weight": 1.0} -->

Table I Deep Clustering via Clustering the Local Manifold of an Autoencoded Embedding") shows details of the accuracy and NMI of each individual component of N2D. This table shows that the performance of the non-deep clustering algorithm GMM is typically poorest across all datasets. When we introduce manifold learning methods, and cluster those embeddings, we see improvements in cluster accuracy and NMI.

<!-- chunk {"id": "body-0046", "role": "body", "section": "IV-E Role of Each Component of N2D", "weight": 1.0} -->

As well as the autoencoder, we use 3 different manifold learning methods with different properties. The first is Isomap, which is a globally focused manifold learner. It outperforms t-SNE, the local manifold learning technique, on 2 of the 4 datasets it was able to process. On 2 of the 6 datasets it was unable to complete the learning as it exhausted all memory on our 64GB system. Therefore, on two datasets t-SNE performed better than Isomap, and on two others, Isomap outperformed t-SNE.

<!-- chunk {"id": "body-0047", "role": "body", "section": "IV-E Role of Each Component of N2D", "weight": 1.0} -->

However, when Isomap and t-SNE are each applied to the autoencoded embedding, on only 1 of the 4 datasets does N2D with Isomap outperform N2D with t-SNE. This suggests that on some datasets the clusters are better discovered by a global method, and others by a local method. However, when applied the autoencoded embedding, the more local methods appear to be the better choice.

<!-- chunk {"id": "body-0048", "role": "body", "section": "IV-E Role of Each Component of N2D", "weight": 1.0} -->

This intuitively suggests that a technique which is primarily locally focused but captures global structure better than t-SNE may lead to further improvements. Therefore, when we experiment with UMAP, which meets this criteria, we see that UMAP is the superior approach on 3 of the 6 raw datasets. However, when applied to the autoencoded embedding, N2D with UMAP outperforms both Isomap and t-SNE on all datasets. This supports the hypothesis that a manifold learner, which, while locally focused, also captures a degree of the global structure, is best suited for discovering the clusterable manifold of an autoencoded embedding.

<!-- chunk {"id": "body-0049", "role": "body", "section": "IV-E Role of Each Component of N2D", "weight": 1.0} -->

The largest gains between our approach N2D and the sub-components is on HAR, where there is a 25 percentage point increase in performance compared to the AE and UMAP, while on MNIST and USPS, where there is an around a 15 percentage point increase in accuracy when using N2D.

<!-- chunk {"id": "body-0050", "role": "body", "section": "IV-E Role of Each Component of N2D", "weight": 1.0} -->

In Table III Deep Clustering via Clustering the Local Manifold of an Autoencoded Embedding") we show the amount of time it takes for each stage of the method in minutes, as well as the total time. From this, it is clear that our method is efficient, clustering MNIST and Fashion-MNIST in around 18 minutes, while clustering the remaining 4 datasets in between two and four minutes.

<!-- chunk {"id": "body-0051", "role": "body", "section": "IV-F Comparison with other methods", "weight": 1.0} -->

In Table II Deep Clustering via Clustering the Local Manifold of an Autoencoded Embedding") we show the accuracy and NMI results for a wide set of clustering algorithms on six different datasets. The clustering algorithms chosen include a number of conventional non-deep methods, such as $k$-means, spectral clustering (SC) and GMMs. They also include recent deep-clustering based methods, such as ClusterGAN, IDEC, JULE and ASPC-DA. These methods make significant use of deep networks, and typically outperform the non-deep clustering methods.

<!-- chunk {"id": "body-0052", "role": "body", "section": "IV-F Comparison with other methods", "weight": 1.0} -->

The most similar methods to N2D are IDEC and ASPC-DA. Both of these approaches pre-train an autoencoder before jointly training a second deep network with a clustering and non-clustering (reconstruction) loss. The clustering network weights are initialized with a non-deep clustering algorithm such as $k$-means.

<!-- chunk {"id": "body-0053", "role": "body", "section": "IV-F Comparison with other methods", "weight": 1.0} -->

In contrast, we replace the second deep network with a manifold learning method, UMAP, and then use a non-deep clustering algorithm, a GMM, to cluster the resulting embedding. Hence, our less deep method, N2D, benefits from less complexity, but as can be seen in Table II Deep Clustering via Clustering the Local Manifold of an Autoencoded Embedding"), has competitive or superior performance to all other methods.

<!-- chunk {"id": "body-0054", "role": "body", "section": "IV-F Comparison with other methods", "weight": 1.0} -->

On five of the six datasets tested, our approach is in the top 3 for at least one of the metrics. On MNIST-test we are around 1 percentage point lower in accuracy than JULE and DEPICT, and 2 percentage points lower than ASPC-DA which is top. However, on the Fashion dataset, we achieve the highest accuracy, around 5 absolute percentage points higher than ClusterGAN, and 8 absolute percentage points higher than ASPC-DA.

<!-- chunk {"id": "body-0055", "role": "body", "section": "IV-F Comparison with other methods", "weight": 1.0} -->

We also include two non-image datasets, pendigits and HAR, to validate performance on different types of data. Many of the best-performing deep-clustering methods are intended for image clustering (e.g., JULE, DBC, DAC ), and thus we were unable to find or easily obtain results on these datasets. However, for the algorithms for which we could obtain or produce results, our method also achieved the best performance. For both datasets we compare our method with some of the most similar deep clustering approaches, DEC and IDEC. On pendigits, we achieve 11 percentage points higher accuracy than the closest approach IDEC and on HAR a 15 percentage point increase in accuracy. In fact, consistently across all datasets, we achieve higher accuracy and NMI scores than these methods.

<!-- chunk {"id": "body-0056", "role": "body", "section": "IV-F Comparison with other methods", "weight": 1.0} -->

We also note that one of the closest competitors, ASPC-DA, which typically slightly outperforms our method on several datasets, achieves this performance due to data augmentation. When data augmentation is removed from ASPC-DA, they typically achieve less competitive performances, e.g. an accuracy of 0.924 (vs 0.988) on MNIST, 0.785 (vs 0.973) on MNIST-test and 0.688 (vs 0.982) on USPS. For future work we would like to evaluate our proposed method with data augmentation.

<!-- chunk {"id": "body-0057", "role": "body", "section": "Conclusion", "weight": 1.5} -->

In this paper we propose a simple deep clustering method, N2D, which reduces the deepness of typical deep clustering algorithms by replacing the clustering network with an alternative framework which seeks to find the manifold within the autoencoder embedding, and clusters this new embedding with a shallow clustering architecture. We studied both global and local manifold learning algorithms, with our results supporting the hypothesis that learning the local manifold of an autoencoded embedding, while also preserving global structure as UMAP does, is better able to discover the most clusterable manifold of an autoencoded embedding. N2D is the resulting combination which is shown to be effective on a range of datasets, including image and time-series datasets. We compare N2D with both conventional shallow clustering algorithms, and the latest state-of-the-art deep clustering algorithms. In the empirical comparison, we show how our proposed method is competitive with the current state-of-the-art clustering approaches, achieving top-3 performance in five of the six datasets datasets tested.

<!-- chunk {"id": "body-0058", "role": "body", "section": "Conclusion", "weight": 1.5} -->

Further, we outperform the state-of-the-art on several datasets, including surpassing the next best algorithm by around 5 absolute percentage points in accuracy on Fashion-MNIST and 15 percentage points on the activity recognition dataset HAR.
