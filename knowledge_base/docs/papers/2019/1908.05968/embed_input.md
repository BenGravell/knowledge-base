N2D: (Not Too) Deep Clustering via Clustering the Local Manifold of an Autoencoded Embedding

Topics include Neural networks, Autoencoders, Representation learning, Clustering, Datasets, Learning, N2D.

Deep clustering has increasingly been demonstrating superiority over conventional shallow clustering algorithms. Deep clustering algorithms usually combine representation learning with deep neural networks to achieve this performance, typically optimizing a clustering and non-clustering loss. In such cases, an autoencoder is typically connected with a clustering network, and the final clustering is jointly learned by both the autoencoder and clustering network. Instead, we propose to learn an autoencoded embedding and then search this further for the underlying manifold. For simplicity, we then cluster this with a shallow clustering algorithm, rather than a deeper network. We study a number of local and global manifold learning methods on both the raw data and autoencoded embedding, concluding that UMAP in our framework is best able to find the most clusterable manifold in the embedding, suggesting local manifold learning on an autoencoded embedding is effective for discovering higher quality discovering clusters....

## Introduction

Clustering is a fundamental pillar of unsupervised machine learning. It is widely used in a range of tasks across disciplines and well-known algorithms such as $k$-means have found success in many applications. For example, in science, data exploration and understanding is a fundamental task which clustering facilitates by uncovering the hidden structure of the data. However, $k$-means, along with many conventional clustering algorithms such as Gaussian Mixture Models (GMMs), DBSCAN, and hierarchical algorithms typically require hand engineered features to be created for each dataset and task....

However, recent advances in deep learning have paved the way for algorithms which can effectively learn from raw data, bypassing the need for manual feature extraction and selection. One such popular method which learns powerful representations of the data automatically is an autoencoder. Autoencoders effectively seek to learn the intrinsic structure of the data with a deep neural network, and do so by learning to reconstruct the original data, regularized for example, via a bottleneck inducing a compressed representation....

## Conclusion

In this paper we propose a simple deep clustering method, N2D, which reduces the deepness of typical deep clustering algorithms by replacing the clustering network with an alternative framework which seeks to find the manifold within the autoencoder embedding, and clusters this new embedding with a shallow clustering architecture. We studied both global and local manifold learning algorithms, with our results supporting the hypothesis that learning the local manifold of an autoencoded embedding, while also preserving global structure as UMAP does, is better able to discover the most clusterable manifold of an autoencoded embedding....

Figure 1: Visualization of N2D applied to all six datasets. For visualization purposes we set the number of dimensions to 2 and points plotted to 5000. In contrast, when we use N2D for clustering and not visualization, we cluster in higher dimensions (where the number of dimensions is the number of clusters) and achieve higher clustering performance.

As with Isomap, t-SNE can choose the number of components in which to embed the data. It also requires a perplexity value which is related to the number of nearest neighbours used in Isomap....
