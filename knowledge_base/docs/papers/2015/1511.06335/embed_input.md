<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Unsupervised Deep Embedding for Clustering Analysis

Topics include Neural networks, Clustering, Learning, DEC, Propose deep embedded clustering, Deep neural networks.

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Clustering is central to many data-driven application domains and has been studied extensively in terms of distance functions and grouping algorithms. Relatively little work has focused on learning representations for clustering. In this paper, we propose Deep Embedded Clustering (DEC), a method that simultaneously learns feature representations and cluster assignments using deep neural networks. DEC learns a mapping from the data space to a lower-dimensional feature space in which it iteratively optimizes a clustering objective. Our experimental evaluations on image and text corpora show significant improvement over state-of-the-art methods.

<!-- chunk {"id": "body-0003", "role": "body", "section": "Introduction", "weight": 1.5} -->

Clustering, an essential data analysis and visualization tool, has been studied extensively in unsupervised machine learning from different perspectives: What defines a cluster? What is the right distance metric? How to efficiently group instances into clusters? How to validate clusters? And so. Numerous different distance functions and embedding methods have been explored in the literature. Relatively little work has focused on the unsupervised learning of the feature space in which to perform clustering.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

A notion of *distance* or *dissimilarity* is central to data clustering algorithms. Distance, in turn, relies on representing the data in a feature space. The $k$-means clustering algorithm, for example, uses the Euclidean distance between points in a given feature space, which for images might be raw pixels or gradient-orientation histograms. The choice of feature space is customarily left as an application-specific detail for the end-user to determine. Yet it is clear that the choice of feature space is crucial; for all but the simplest image datasets, clustering with Euclidean distance on raw pixels is completely ineffective. In this paper, we revisit cluster analysis and ask: *Can we use a data driven approach to solve for the feature space and cluster memberships jointly?* We take inspiration from recent work on deep learning for computer vision, where clear gains on benchmark tasks have resulted from learning better features. These improvements, however, were obtained with *supervised* learning, whereas our goal is *unsupervised* data clustering.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

To this end, we define a parameterized non-linear mapping from the data space $X$ to a lower-dimensional feature space $Z$, where we optimize a clustering objective. Unlike previous work, which operates on the data space or a shallow linear embedded space, we use stochastic gradient descent (SGD) via backpropagation on a clustering objective to learn the mapping, which is parameterized by a deep neural network. We refer to this clustering algorithm as *Deep Embedded Clustering*, or DEC.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

Optimizing DEC is challenging. We want to simultaneously solve for cluster assignment and the underlying feature representation. However, unlike in supervised learning, we cannot train our deep network with labeled data. Instead we propose to iteratively refine clusters with an auxiliary target distribution derived from the current soft cluster assignment. This process gradually improves the clustering as well as the feature representation.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

Our experiments show significant improvements over state-of-the-art clustering methods in terms of both accuracy and running time on image and textual datasets. We evaluate DEC on MNIST, STL, and REUTERS, comparing it with standard and state-of-the-art clustering methods. In addition, our experiments show that DEC is significantly less sensitive to the choice of hyperparameters compared to state-of-the-art methods. This robustness is an important property of our clustering algorithm since, when applied to real data, supervision is not available for hyperparameter cross-validation.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Introduction", "weight": 1.5} -->

Our contributions are: (a) joint optimization of deep embedding and clustering; (b) a novel iterative refinement via soft assignment; and (c) state-of-the-art clustering results in terms of clustering accuracy and speed. Our Caffe-based implementation of DEC is available at

<!-- chunk {"id": "body-0009", "role": "body", "section": "Deep embedded clustering", "weight": 1.0} -->

Consider the problem of clustering a set of $n$ points ${\{{x_{i} \in X}\}}_{i = 1}^{n}$ into $k$ clusters, each represented by a centroid ${{\mu_{j},j} = 1},{\ldots,k}$. Instead of clustering directly in the *data space* $X$, we propose to first transform the data with a non-linear mapping $f_{\theta}:{X\rightarrow Z}$, where $\theta$ are learnable parameters and $Z$ is the latent *feature space*. The dimensionality of $Z$ is typically much smaller than $X$ in order to avoid the "curse of dimensionality". To parametrize $f_{\theta}$, deep neural networks (DNNs) are a natural choice due to their theoretical function approximation properties and their demonstrated feature learning capabilities.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Deep embedded clustering", "weight": 1.0} -->

The proposed algorithm (DEC) clusters data by *simultaneously* learning a set of $k$ cluster centers ${\{{\mu_{j} \in Z}\}}_{j = 1}^{k}$ in the feature space $Z$ and the parameters $\theta$ of the DNN that maps data points into $Z$. DEC has two phases: parameter initialization with a deep autoencoder and parameter optimization (i.e., clustering), where we iterate between computing an auxiliary target distribution and minimizing the Kullback--Leibler (KL) divergence to it. We start by describing phase parameter optimization/clustering, given an initial estimate of $\theta$ and ${\{\mu_{j}\}}_{j = 1}^{k}$.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Clustering with KL divergence", "weight": 1.0} -->

Given an initial estimate of the non-linear mapping $f_{\theta}$ and the initial cluster centroids ${\{\mu_{j}\}}_{j = 1}^{k}$, we propose to improve the clustering using an unsupervised algorithm that alternates between two steps. In the first step, we compute a soft assignment between the embedded points and the cluster centroids. In the second step, we update the deep mapping $f_{\theta}$ and refine the cluster centroids by learning from current high confidence assignments using an auxiliary target distribution. This process is repeated until a convergence criterion is met.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Soft Assignment", "weight": 1.0} -->

Following van der Maaten & Hinton we use the Student's $t$-distribution as a kernel to measure the similarity between embedded point $z_{i}$ and centroid $\mu_{j}$: where $z_{i} = {f_{\theta}{(x_{i})}} \in Z$ corresponds to $x_{i} \in X$ after embedding, $\alpha$ are the degrees of freedom of the Student's $t$-distribution and $q_{ij}$ can be interpreted as the probability of assigning sample $i$ to cluster $j$ (i.e., a soft assignment). Since we cannot cross-validate $\alpha$ on a validation set in the unsupervised setting, and learning it is superfluous, we let $\alpha = 1$ for all experiments.

<!-- chunk {"id": "body-0013", "role": "body", "section": "KL divergence minimization", "weight": 1.0} -->

We propose to iteratively refine the clusters by learning from their high confidence assignments with the help of an auxiliary target distribution. Specifically, our model is trained by matching the soft assignment to the target distribution. To this end, we define our objective as a KL divergence loss between the soft assignments $q_{i}$ and the auxiliary distribution $p_{i}$ as follows: The choice of target distributions $P$ is crucial for DEC's performance. A naive approach would be setting each $p_{i}$ to a delta distribution (to the nearest centroid) for data points above a confidence threshold and ignore the rest. However, because $q_{i}$ are soft assignments, it is more natural and flexible to use softer probabilistic targets. Specifically, we would like our target distribution to have the following properties: strengthen predictions (i.e., improve cluster purity), put more emphasis on data points assigned with high confidence, and normalize loss contribution of each centroid to prevent large clusters from distorting the hidden feature space.

<!-- chunk {"id": "body-0014", "role": "body", "section": "KL divergence minimization", "weight": 1.0} -->

In our experiments, we compute $p_{i}$ by first raising $q_{i}$ to the second power and then normalizing by frequency per cluster: where $f_{j} = {\sum_{i}q_{ij}}$ are soft cluster frequencies. Please refer to section 4 for discussions on empirical properties of $L$ and $P$.

<!-- chunk {"id": "body-0015", "role": "body", "section": "KL divergence minimization", "weight": 1.0} -->

Our training strategy can be seen as a form of self-training. As in self-training, we take an initial classifier and an unlabeled dataset, then label the dataset with the classifier in order to train on its own high confidence predictions. Indeed, in experiments we observe that DEC improves upon the initial estimate in each iteration by learning from high confidence predictions, which in turn helps to improve low confidence ones.

<!-- chunk {"id": "body-0016", "role": "body", "section": "Optimization", "weight": 1.0} -->

We jointly optimize the cluster centers $\{\mu_{j}\}$ and DNN parameters $\theta$ using Stochastic Gradient Descent (SGD) with momentum. The gradients of $L$ with respect to feature-space embedding of each data point $z_{i}$ and each cluster centroid $\mu_{j}$ are computed as: The gradients $\partial{L/{\partial z_{i}}}$ are then passed down to the DNN and used in standard backpropagation to compute the DNN's parameter gradient $\partial{L/{\partial\theta}}$. For the purpose of discovering cluster assignments, we stop our procedure when less than ${tol}\%$ of points change cluster assignment between two consecutive iterations.

<!-- chunk {"id": "body-0017", "role": "body", "section": "Parameter initialization", "weight": 1.0} -->

We initialize DEC with a stacked autoencoder (SAE) because recent research has shown that they consistently produce semantically meaningful and well-separated representations on real-world datasets. Thus the unsupervised representation learned by SAE naturally facilitates the learning of clustering representations with DEC.

<!-- chunk {"id": "body-0018", "role": "body", "section": "Parameter initialization", "weight": 1.0} -->

We initialize the SAE network layer by layer with each layer being a denoising autoencoder trained to reconstruct the previous layer's output after random corruption. A denoising autoencoder is a two layer neural network defined as: where ${Dropout}{(\cdot)}$ is a stochastic mapping that randomly sets a portion of its input dimensions to 0, $g_{1}$ and $g_{2}$ are activation functions for encoding and decoding layer respectively, and $\theta = {\{ W_{1},b_{1},W_{2},b_{2}\}}$ are model parameters. Training is performed by minimizing the least-squares loss ${\|{x - y}\|}_{2}^{2}$. After training of one layer, we use its output $h$ as the input to train the next layer.

<!-- chunk {"id": "body-0019", "role": "body", "section": "Parameter initialization", "weight": 1.0} -->

We use rectified linear units (ReLUs) in all encoder/decoder pairs, except for $g_{2}$ of the *first* pair (it needs to reconstruct input data that may have positive and negative values, such as zero-mean images) and $g_{1}$ of the *last* pair (so the final data embedding retains full information).

<!-- chunk {"id": "body-0020", "role": "body", "section": "Parameter initialization", "weight": 1.0} -->

After greedy layer-wise training, we concatenate all encoder layers followed by all decoder layers, in reverse layer-wise training order, to form a deep autoencoder and then finetune it to minimize reconstruction loss. The final result is a multilayer deep autoencoder with a bottleneck coding layer in the middle. We then discard the decoder layers and use the encoder layers as our initial mapping between the data space and the feature space, as shown in Fig. 1.

<!-- chunk {"id": "body-0021", "role": "body", "section": "Parameter initialization", "weight": 1.0} -->

To initialize the cluster centers, we pass the data through the initialized DNN to get embedded data points and then perform standard $k$-means clustering in the feature space $Z$ to obtain $k$ initial centroids ${\{\mu_{j}\}}_{j = 1}^{k}$.

<!-- chunk {"id": "body-0022", "role": "body", "section": "Datasets", "weight": 1.0} -->

We evaluate the proposed method (DEC) on one text dataset and two image datasets and compare it against other algorithms including $k$-means, LDGMI, and SEC. LDGMI and SEC are spectral clustering based algorithms that use a Laplacian matrix and various transformations to improve clustering performance. Empirical evidence reported in Yang et al.; Nie et al. shows that LDMGI and SEC outperform traditional spectral clustering methods on a wide range of datasets. We show qualitative and quantitative results that demonstrate the benefit of DEC compared to LDGMI and SEC.

<!-- chunk {"id": "body-0023", "role": "body", "section": "Datasets", "weight": 1.0} -->

In order to study the performance and generality of different algorithms, we perform experiment on two image datasets and one text data set: MNIST: The MNIST dataset consists of 70000 handwritten digits of 28-by-28 pixel size. The digits are centered and size-normalized.

<!-- chunk {"id": "body-0024", "role": "body", "section": "Datasets", "weight": 1.0} -->

STL-10: A dataset of 96-by-96 color images. There are 10 classes with 1300 examples each. It also contains 100000 unlabeled images of the same resolution. We also used the unlabeled set when training our autoencoders. Similar to Doersch et al., we concatenated HOG feature and a 8-by-8 color map to use as input to all algorithms.

<!-- chunk {"id": "body-0025", "role": "body", "section": "Datasets", "weight": 1.0} -->

REUTERS: Reuters contains about 810000 English news stories labeled with a category tree. We used the four root categories: corporate/industrial, government/social, markets, and economics as labels and further pruned all documents that are labeled by multiple root categories to get 685071 articles. We then computed tf-idf features on the 2000 most frequently occurring word stems. Since some algorithms do not scale to the full Reuters dataset, we also sampled a random subset of 10000 examples, which we call REUTERS-10k, for comparison purposes.

<!-- chunk {"id": "body-0026", "role": "body", "section": "Datasets", "weight": 1.0} -->

A summary of dataset statistics is shown in Table 1. For all algorithms, we normalize all datasets so that $\frac{1}{d}{\| x_{i}\|}_{2}^{2}$ is approximately 1, where $d$ is the dimensionality of the data space point $x_{i} \in X$.

<!-- chunk {"id": "body-0027", "role": "body", "section": "Evaluation Metric", "weight": 1.0} -->

We use the standard unsupervised evaluation metric and protocols for evaluations and comparisons to other algorithms. For all algorithms we set the number of clusters to the number of ground-truth categories and evaluate performance with *unsupervised clustering accuracy ($ACC$)*: where $l_{i}$ is the ground-truth label, $c_{i}$ is the cluster assignment produced by the algorithm, and $m$ ranges over all possible one-to-one mappings between clusters and labels.

<!-- chunk {"id": "body-0028", "role": "body", "section": "Evaluation Metric", "weight": 1.0} -->

Intuitively this metric takes a cluster assignment from an *unsupervised* algorithm and a ground truth assignment and then finds the best matching between them. The best mapping can be efficiently computed by the Hungarian algorithm.

<!-- chunk {"id": "body-0029", "role": "body", "section": "Implementation", "weight": 1.0} -->

Determining hyperparameters by cross-validation on a validation set is not an option in unsupervised clustering. Thus we use commonly used parameters for DNNs and avoid dataset specific tuning as much as possible. Specifically, inspired by van der Maaten, we set network dimensions to $d$--500--500--2000--10 for all datasets, where $d$ is the data-space dimension, which varies between datasets. All layers are densely (fully) connected.

<!-- chunk {"id": "body-0030", "role": "body", "section": "Implementation", "weight": 1.0} -->

During greedy layer-wise pretraining we initialize the weights to random numbers drawn from a zero-mean Gaussian distribution with a standard deviation of 0.01. Each layer is pretrained for 50000 iterations with a dropout rate of $20\%$. The entire deep autoencoder is further finetuned for 100000 iterations without dropout. For both layer-wise pretraining and end-to-end finetuning of the autoencoder the minibatch size is set to 256, starting learning rate is set to 0.1, which is divided by 10 every 20000 iterations, and weight decay is set to 0. All of the above parameters are set to achieve a reasonably good reconstruction loss and are held constant across all datasets. Dataset-specific settings of these parameters might improve performance on each dataset, but we refrain from this type of unrealistic parameter tuning. To initialize centroids, we run $k$-means with 20 restarts and select the best solution.

<!-- chunk {"id": "body-0031", "role": "body", "section": "Implementation", "weight": 1.0} -->

In the KL divergence minimization phase, we train with a constant learning rate of 0.01. The convergence threshold is set to ${tol} = {0.1\%}$. Our implementation is based on Python and Caffe and is available at For all baseline algorithms, we perform 20 random restarts when initializing centroids and pick the result with the best objective value. For a fair comparison with previous work, we vary one hyperparameter for each algorithm over 9 possible choices and report the best accuracy in Table 2 and the range of accuracies in Fig. 2. For LDGMI and SEC, we use the same parameter and range as in their corresponding papers. For our proposed algorithm, we vary $\lambda$, the parameter that controls annealing speed, over ${{{2^{i} \times 10},i} = 0},{1,\ldots,8}$. Since $k$-means does not have tunable hyperparameters (aside from $k$), we simply run them 9 times. GMMs perform similarly to $k$-means so we only report $k$-means results.

<!-- chunk {"id": "body-0032", "role": "body", "section": "Implementation", "weight": 1.0} -->

Traditional spectral clustering performs worse than LDGMI and SEC so we only report the latter.

<!-- chunk {"id": "body-0033", "role": "body", "section": "Experiment results", "weight": 1.0} -->

We evaluate the performance of our algorithm both quantitatively and qualitatively. In Table 2, we report the best performance, over 9 hyperparameter settings, of each algorithm. Note that DEC outperforms all other methods, sometimes with a significant margin. To demonstrate the effectiveness of end-to-end training, we also show the results from freezing the non-linear mapping $f_{\theta}$ during clustering. We find that this ablation ("DEC w/o backprop") generally performs worse than DEC.

<!-- chunk {"id": "body-0034", "role": "body", "section": "Experiment results", "weight": 1.0} -->

In order to investigate the effect of hyperparameters, we plot the accuracy of each method under all 9 settings (Fig. 2). We observe that DEC is more consistent across hyperparameter ranges compared to LDGMI and SEC. For DEC, hyperparameter $\lambda = 40$ gives near optimal performance on all dataset, whereas for other algorithms the optimal hyperparameter varies widely. Moreover, DEC can process the entire REUTERS dataset in half an hour with GPU acceleration while the second best algorithms, LDGMI and SEC, would need months of computation time and terabytes of memory. We, indeed, could not run these methods on the full REUTERS dataset and report N/A in Table 2 (GPU adaptation of these methods is non-trivial).

<!-- chunk {"id": "body-0035", "role": "body", "section": "Experiment results", "weight": 1.0} -->

In Fig. 3 we show 10 top scoring images from each cluster in MNIST and STL. Each row corresponds to a cluster and images are sorted from left to right based on their distance to the cluster center. We observe that for MNIST, DEC's cluster assignment corresponds to natural clusters very well, with the exception of confusing 4 and 9, while for STL, DEC is mostly correct with airplanes, trucks and cars, but spends part of its attention on poses instead of categories when it comes to animal classes.

<!-- chunk {"id": "body-0036", "role": "body", "section": "Assumptions and Objective", "weight": 1.0} -->

The underlying assumption of DEC is that the initial classifier's high confidence predictions are mostly correct. To verify that this assumption holds for our task and that our choice of $P$ has the desired properties, we plot the magnitude of the gradient of $L$ with respect to each embedded point, $|{\partial{L/{\partial z_{i}}}}|$, against its soft assignment, $q_{ij}$, to a randomly chosen MNIST cluster $j$ (Fig. 4).

<!-- chunk {"id": "body-0037", "role": "body", "section": "Assumptions and Objective", "weight": 1.0} -->

We observe points that are closer to the cluster center (large $q_{ij}$) contribute more to the gradient. We also show the raw images of 10 data points at each 10 percentile sorted by $q_{ij}$. Instances with higher similarity are more canonical examples of "5". As confidence decreases, instances become more ambiguous and eventually turn into a mislabeled "8" suggesting the soundness of our assumptions.

<!-- chunk {"id": "body-0038", "role": "body", "section": "Contribution of Iterative Optimization", "weight": 1.0} -->

In Fig. 5 we visualize the progression of the embedded representation of a random subset of MNIST during training. For visualization we use t-SNE applied to the embedded points $z_{i}$. It is clear that the clusters are becoming increasingly well separated. Fig. 5 (f) shows how accuracy correspondingly improves over SGD epochs.

<!-- chunk {"id": "body-0039", "role": "body", "section": "Contribution of Autoencoder Initialization", "weight": 1.0} -->

To better understand the contribution of each component, we show the performance of all algorithms with autoencoder features in Table 3. We observe that SEC and LDMGI's performance do not change significantly with autoencoder feature, while $k$-means improved but is still below DEC. This demonstrates the power of deep embedding and the benefit of fine-tuning with the proposed KL divergence objective.

<!-- chunk {"id": "body-0040", "role": "body", "section": "Performance on Imbalanced Data", "weight": 1.0} -->

In order to study the effect of imbalanced data, we sample subsets of MNIST with various retention rates. For minimum retention rate $r_{min}$, data points of class 0 will be kept with probability $r_{min}$ and class 9 with probability 1, with the other classes linearly in between. As a result the largest cluster will be $1/r_{min}$ times as large as the smallest one. From Table 4 we can see that DEC is fairly robust against cluster size variation. We also observe that KL divergence minimization (DEC) consistently improves clustering accuracy after autoencoder and $k$-means initialization (shown as AE+$k$-means).

<!-- chunk {"id": "body-0041", "role": "body", "section": "Number of Clusters", "weight": 1.0} -->

So far we have assumed that the number of natural clusters is given to simplify comparison between algorithms. However, in practice this quantity is often unknown. Therefore a method for determining the optimal number of clusters is needed. To this end, we define two metrics: the standard metric, Normalized Mutual Information (NMI), for evaluating clustering results with different cluster number: where $I$ is the mutual information metric and $H$ is entropy, and generalizability ($G$) which is defined as the ratio between training and validation loss: $G$ is small when training loss is lower than validation loss, which indicate a high degree of overfitting.

<!-- chunk {"id": "body-0042", "role": "body", "section": "Number of Clusters", "weight": 1.0} -->

Fig. 6 shows a sharp drop in generalizability when cluster number increases from 9 to 10, which suggests that 9 is the optimal number of clusters. We indeed observe the highest NMI score at 9, which demonstrates that generalizability is a good metric for selecting cluster number. NMI is highest at 9 instead 10 because 9 and 4 are similar in writing and DEC thinks that they should form a single cluster. This corresponds well with our qualitative results in Fig. 3.

<!-- chunk {"id": "body-0043", "role": "body", "section": "Conclusion", "weight": 1.5} -->

This paper presents Deep Embedded Clustering, or DEC---an algorithm that clusters a set of data points in a jointly optimized feature space. DEC works by iteratively optimizing a KL divergence based clustering objective with a self-training target distribution. Our method can be viewed as an unsupervised extension of semisupervised self-training. Our framework provide a way to learn a representation specialized for clustering without groundtruth cluster membership labels.

<!-- chunk {"id": "body-0044", "role": "body", "section": "Conclusion", "weight": 1.5} -->

Empirical studies demonstrate the strength of our proposed algorithm. DEC offers improved performance as well as robustness with respect to hyperparameter settings, which is particularly important in unsupervised tasks since cross-validation is not possible. DEC also has the virtue of linear complexity in the number of data points which allows it to scale to large datasets.
