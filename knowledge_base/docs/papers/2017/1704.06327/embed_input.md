<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Deep Clustering via Joint Convolutional Autoencoder Embedding and Relative Entropy Minimization

Topics include Convolutional networks, Autoencoders, Computer vision, Clustering, Regression, Scalability, Optimization, Learning, Deep embedded clustering, DEPICT.

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Image clustering is one of the most important computer vision applications, which has been extensively studied in literature. However, current clustering methods mostly suffer from lack of efficiency and scalability when dealing with large-scale and high-dimensional data. In this paper, we propose a new clustering model, called DEeP Embedded RegularIzed ClusTering (DEPICT), which efficiently maps data into a discriminative embedding subspace and precisely predicts cluster assignments. DEPICT generally consists of a multinomial logistic regression function stacked on top of a multi-layer convolutional autoencoder. We define a clustering objective function using relative entropy (KL divergence) minimization, regularized by a prior for the frequency of cluster assignments. An alternating strategy is then derived to optimize the objective by updating parameters and estimating cluster assignments. Furthermore, we employ the reconstruction loss functions in our autoencoder, as a data-dependent regularization term, to prevent the deep embedding function from overfitting.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

In order to benefit from end-to-end optimization and eliminate the necessity for layer-wise pretraining, we introduce a joint learning framework to minimize the unified clustering and reconstruction loss functions together and train all network layers simultaneously. Experimental results indicate the superiority and faster running time of DEPICT in real-world clustering tasks, where no labeled data is available for hyper-parameter tuning.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

Clustering is one of the fundamental research topics in machine learning and computer vision research, and it has gained significant attention for discriminative representation of data points without any need for supervisory signals. The clustering problem has been extensively studied in various applications; however, the performance of standard clustering algorithms is adversely affected when dealing with high-dimensional data, and their time complexity dramatically increases when working with large-scale datasets. Tackling the curse of dimensionality, previous studies often initially project data into a low-dimensional manifold, and then cluster the embedded data in this new subspace. Handling large-scale datasets, there are also several studies which select only a subset of data points to accelerate the clustering process.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

However, dealing with real-world image data, existing clustering algorithms suffer from different issues: 1) Using inflexible hand-crafted features, which do not depend on the input data distribution; 2) Using shallow and linear embedding functions, which are not able to capture the non-linear nature of data; 3) Non-joint embedding and clustering processes, which do not result in an optimal embedding subspace for clustering; 4) Complicated clustering algorithms that require tuning the hyper-parameters using labeled data, which is not feasible in real-world clustering tasks.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

To address the mentioned challenging issues, we propose a new clustering algorithm, called deep embedded regularized clustering (DEPICT), which exploits the advantages of both discriminative clustering methods and deep embedding models. DEPICT generally consists of two main parts, a multinomial logistic regression (soft-max) layer stacked on top of a multi-layer convolutional autoencoder. The soft-max layer along with the encoder pathway can be considered as a discriminative clustering model, which is trained using the relative entropy (KL divergence) minimization. We further add a regularization term based on a prior distribution for the frequency of cluster assignments. The regularization term penalizes unbalanced cluster assignments and prevents allocating clusters to outlier samples.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

Although this deep clustering model is flexible enough to discriminate the complex real-world input data, it can easily get stuck in non-optimal local minima during training and result in undesirable cluster assignments. In order to avoid overfitting the deep clustering model to spurious data correlations, we utilize the reconstruction loss function of autoencoder models as a data-dependent regularization term for training parameters.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Introduction", "weight": 1.5} -->

In order to benefit from a joint learning framework for embedding and clustering, we introduce a unified objective function including our clustering and auxiliary reconstruction loss functions. We then employ an alternating approach to efficiently update the parameters and estimate the cluster assignments. It is worth mentioning that in the standard learning approach for training a multi-layer autoencoder, the encoder and decoder parameters are first pretrained layer-wise using the reconstruction loss, and the encoder parameters are then fine-tuned using the objective function of the main task. However, it has been argued that the non-joint fine-tuning step may overwrite the encoder parameters entirely and consequently cancel out the benefit of the layer-wise pretraining step. To avoid this problem and achieve optimal joint learning results, we simultaneously train all of the encoder and decoder layers together along with the soft-max layer. To do so, we sum up the squared error reconstruction loss functions between the decoder and their corresponding (clean) encoder layers and add them to the clustering loss function.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Introduction", "weight": 1.5} -->

Moreover, experimental results show that DEPICT achieves superior or competitive results compared to the state-of-the-art algorithms on the image benchmark datasets while having faster running times. In addition, we compared different learning strategies for DEPICT, and confirm that our joint learning approach has the best results. It should also be noted that DEPICT does not require any hyper-parameter tuning using supervisory signals, and consequently is a better candidate for the real-world clustering tasks.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Introduction", "weight": 1.5} -->

Providing a discriminative non-linear embedding subspace via the deep convolutional autoencoder;

<!-- chunk {"id": "body-0011", "role": "body", "section": "Introduction", "weight": 1.5} -->

Introducing an end-to-end joint learning approach, which unifies the clustering and embedding tasks, and avoids layer-wise pretraining;

<!-- chunk {"id": "body-0012", "role": "body", "section": "Introduction", "weight": 1.5} -->

Achieving superior or competitive clustering results on high-dimensional and large-scale datasets with no need for hyper-parameter tuning using labeled data.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Related Works", "weight": 1.0} -->

There is a large number of clustering algorithms in literature, which can be grouped into different perspectives, such as hierarchical, centroid-based, graph-based, sequential (temporal), regression model based, and subspace clustering models. In another sense, they are generally divided into two subcategories, generative and discriminative clustering algorithms. The generative algorithms like $K$-means and Gaussian mixture model explicitly represent the clusters using geometric properties of the feature space, and model the categories via the statistical distributions of input data. Unlike the generative clustering algorithms, the discriminative methods directly identify the categories using their separating hyperplanes regardless of data distribution. Information theoretic, max-margin, and spectral graph algorithms are examples of discriminative clustering models. Generally it has been argued that the discriminative models often have better results compared to their generative counterparts, since they have fewer assumptions about the data distribution and directly separate the clusters, but their training can suffer from overfitting or getting stuck in undesirable local minima.

<!-- chunk {"id": "body-0014", "role": "body", "section": "Related Works", "weight": 1.0} -->

Our DEPICT algorithm is also a discriminative clustering model, but it benefits from the auxiliary reconstruction task of autoencoder to alleviate this issues in training of our discriminative clustering algorithm.

<!-- chunk {"id": "body-0015", "role": "body", "section": "Related Works", "weight": 1.0} -->

There are also several studies regarding the combination of clustering with feature embedding learning. Ye *et al.* introduced a kernelized $K$-means algorithm, denoted by DisKmeans, where embedding to a lower dimensional subspace via linear discriminant analysis (LDA) is jointly learned with $K$-means cluster assignments. proposed to a new method to simultaneously conduct both clustering and feature embedding/selection tasks to achieve better performance. But these models suffer from having shallow and linear embedding functions, which cannot represent the non-linearity of real-world data.

<!-- chunk {"id": "body-0016", "role": "body", "section": "Related Works", "weight": 1.0} -->

A joint learning framework for updating code books and estimating image clusters was proposed in while SIFT features are used as input data. A deep structure, named TAGnet was introduced, where two layers of sparse coding followed by a clustering algorithm are trained with an alternating learning approach. Similar work is presented in that formulates a joint optimization framework for discriminative clustering and feature extraction using sparse coding. However, the inference complexity of sparse coding forces the model in to reduce the dimension of input data with PCA and the model in to use an approximate solution. Hand-crafted features and dimension reduction techniques degrade the clustering performance by neglecting the distribution of input data.

<!-- chunk {"id": "body-0017", "role": "body", "section": "Related Works", "weight": 1.0} -->

Tian *et al.* learned a non-linear embedding of the affinity graph using a stacked autoencoder, and then obtained the clusters in the embedding subspace via $K$-means. Trigeorgis *et al.* extended semi non-negative matrix factorization (semi-NMF) to stacked multi-layer (deep) semi-NMF to capture the abstract information in the top layer. Afterwards, they run $K$-means over the embedding subspace for cluster assignments. More recently, Xie *et al.* employed denoising stacked autoencoder learning approach, and first pretrained the model layer-wise and then fine-tuned the encoder pathway stacked by a clustering algorithm using Kullback-Leibler divergence minimization. Unlike these models that require layer-wise pretraining as well as non-joint embedding and clustering learning, DEPICT utilizes an end-to-end optimization for training all network layers simultaneously using the unified clustering and reconstruction loss functions.

<!-- chunk {"id": "body-0018", "role": "body", "section": "Related Works", "weight": 1.0} -->

Yang *et al.* introduced a new clustering model, named JULE, based on a recurrent framework, where data is represented via a convolutional neural network and embedded data is iteratively clustered using an agglomerative clustering algorithm. They derived a unified loss function consisting of the merging process for agglomerative clustering and updating the parameters of the deep representation. While JULE achieved good results using the joint learning approach, it requires tuning of a large number of hyper-parameters, which is not practical in real-world clustering tasks. In contrast, our model does not need any supervisory signals for hyper-parameter tuning.

<!-- chunk {"id": "body-0019", "role": "body", "section": "Deep Embedded Regularized Clustering", "weight": 1.0} -->

In this section, we first introduce the clustering objective function and the corresponding optimization algorithm, which alternates between estimating the cluster assignments and updating model parameters. Afterwards, we show the architecture of DEPICT and provide the joint learning framework to simultaneously train all network layers using the unified clustering and reconstruction loss functions.

<!-- chunk {"id": "body-0020", "role": "body", "section": "DEPICT Algorithm", "weight": 1.0} -->

Given the embedded features, we use a multinomial logistic regression (soft-max) function $f_{\theta}:{Z\rightarrow Y}$ to predict the probabilistic cluster assignments as follows.

<!-- chunk {"id": "body-0021", "role": "body", "section": "DEPICT Algorithm", "weight": 1.0} -->

In order to define our clustering objective function, we employ an auxiliary target variable $\mathbf{Q}$ to refine the model predictions iteratively. To do so, we first use Kullback-Leibler (KL) divergence to decrease the distance between the model prediction $\mathbf{P}$ and the target variable $\mathbf{Q}$.

<!-- chunk {"id": "body-0022", "role": "body", "section": "DEPICT Algorithm", "weight": 1.0} -->

In order to avoid degenerate solutions, which allocate most of the samples to a few clusters or assign a cluster to outlier samples, we aim to impose a regularization term to the target variable.

<!-- chunk {"id": "body-0023", "role": "body", "section": "DEPICT Algorithm", "weight": 1.0} -->

where $f_{k}$ can be considered as the soft frequency of cluster assignments in the target distribution. Using this empirical distribution, we are able to enforce our preference for having balanced assignments by adding the following KL divergence to the loss function.

<!-- chunk {"id": "body-0024", "role": "body", "section": "DEPICT Algorithm", "weight": 1.0} -->

where $\mathbf{u}$ is the uniform prior for the empirical label distribution. While the first term in the objective minimizes the distance between the target and model prediction distributions, the second term balances the frequency of clusters in the target variables. Utilizing the balanced target variables, we can force the model to have more balanced predictions (cluster assignments) $\mathbf{P}$ indirectly. It is also simple to change the prior from the uniform distribution to any arbitrary distribution in the objective function if there is any extra knowledge about the frequency of clusters.

<!-- chunk {"id": "body-0025", "role": "body", "section": "DEPICT Algorithm", "weight": 1.0} -->

An alternating learning approach is utilized to optimize the objective function. Using this approach, we estimate the target variables $\mathbf{Q}$ via fixed parameters (expectation step), and update the parameters while the target variables $\mathbf{Q}$ are assumed to be known (maximization step).

<!-- chunk {"id": "body-0026", "role": "body", "section": "DEPICT Algorithm", "weight": 1.0} -->

where the target variables are constrained to ${\sum_{k}q_{ik}} = 1$. This problem can be solved using first order methods, such as gradient descent, projected gradient descent, and Nesterov optimal method, which only require the objective function value and its (sub)gradient at each iteration. In the following equation, we show the partial derivative of the objective function with respect to the target variables.

<!-- chunk {"id": "body-0027", "role": "body", "section": "DEPICT Algorithm", "weight": 1.0} -->

Investigating this problem more carefully, we approximate the gradient in Eq. by removing the second term, since the number of samples N is often big enough to ignore the second term. Setting the gradient equal to zero, we are now able to compute the closed form solution for $\mathbf{Q}$ accordingly.

<!-- chunk {"id": "body-0028", "role": "body", "section": "DEPICT Algorithm", "weight": 1.0} -->

For the maximization step, we update the network parameters ${\mathbf{ψ}} = {\{\mathbf{\Theta},\mathbf{W}\}}$ using the estimated target variables with the following objective function.

<!-- chunk {"id": "body-0029", "role": "body", "section": "DEPICT Algorithm", "weight": 1.0} -->

Interestingly, this problem can be considered as a standard cross entropy loss function for classification tasks, and the parameters of soft-max layer $\mathbf{\Theta}$ and embedding function $\mathbf{W}$ can be efficiently updated by backpropagating the error.

<!-- chunk {"id": "body-0030", "role": "body", "section": "DEPICT Architecture", "weight": 1.0} -->

In this section, we extend our general clustering loss function using a denoising autoencoder. The deep embedding function is useful for capturing the non-linear nature of input data; However, it may overfit to spurious data correlations and get stuck in undesirable local minima during training. To avoid this overfitting, we employ autoencoder structures and use the reconstruction loss function as a data-dependent regularization for training the parameters. Therefore, we design DEPICT to consist of a soft-max layer stacked on top of a multi-layer convolutional autoencoder. Due to the promising performance of strided convolutional layers, we employ convolutional layers in our encoder and strided convolutional layers in the decoder pathways, and avoid deterministic spatial pooling layers (like max-pooling). Strided convolutional layers allow the network to learn its own spatial upsampling, providing a better generation capability.

<!-- chunk {"id": "body-0031", "role": "body", "section": "DEPICT Architecture", "weight": 1.0} -->

Unlike the standard learning approach for denoising autoencoders, which contains layer-wise pretraining and then fine-tuning, we simultaneously learn all of the autoencoder and soft-max layers.

<!-- chunk {"id": "body-0032", "role": "body", "section": "DEPICT Architecture", "weight": 1.0} -->

1\) Corrupted feedforward (encoder) pathway maps the noisy input data into the embedding subspace using a few convolutional layers followed by a fully connected layer. The following equation indicates the output of each layer in the noisy encoder pathway.

<!-- chunk {"id": "body-0033", "role": "body", "section": "DEPICT Architecture", "weight": 1.0} -->

where ${\overset{\sim}{\mathbf{z}}}^{l}$ are the noisy features of the $l$-th layer, $Dropout$ is a stochastic mask function that randomly sets a subset of its inputs to zero, $g$ is the activation function of convolutional or fully connected layers, and $\mathbf{W}_{e}^{l}$ indicates the weights of the $l$-th layer in the encoder. Note that the first layer features, ${\overset{\sim}{\mathbf{z}}}^{0}$, are equal to the noisy input data, $\overset{\sim}{\mathbf{x}}$.

<!-- chunk {"id": "body-0034", "role": "body", "section": "DEPICT Architecture", "weight": 1.0} -->

2\) Followed by the corrupted encoder, the decoder pathway reconstructs the input data through a fully connected and multiple strided convolutional layers as follows,

<!-- chunk {"id": "body-0035", "role": "body", "section": "DEPICT Architecture", "weight": 1.0} -->

3\) Clean feedforward (encoder) pathway shares its weights with the corrupted encoder, and infers the clean embedded features. The following equation shows the outputs of the clean encoder, which are used in the reconstruction loss functions and obtaining the final cluster assignments.

<!-- chunk {"id": "body-0036", "role": "body", "section": "DEPICT Architecture", "weight": 1.0} -->

where $\mathbf{z}^{l}$ is the clean output of the $l$-th layer in the encoder. Consider the first layer features $\mathbf{z}^{0}$ equal to input data $\mathbf{x}$.

<!-- chunk {"id": "body-0037", "role": "body", "section": "DEPICT Architecture", "weight": 1.0} -->

4\) Given the top layer of the corrupted and clean encoder pathways as the embedding subspace, the soft-max layer obtains the cluster assignments using Eq..

<!-- chunk {"id": "body-0038", "role": "body", "section": "DEPICT Architecture", "weight": 1.0} -->

Note that we compute target variables $\mathbf{Q}$ using the clean pathway, and model prediction $\overset{\sim}{\mathbf{P}}$ via the corrupted pathway. Hence, the clustering loss function $KL{({\mathbf{Q} \parallel \overset{\sim}{\mathbf{P}}})}$ forces the model to have invariant features with respect to noise. In other words, the model is assumed to have a dual role: a clean model, which is used to compute the more accurate target variables; and a noisy model, which is trained to achieve noise-invariant predictions.

<!-- chunk {"id": "body-0039", "role": "body", "section": "DEPICT Architecture", "weight": 1.0} -->

As a crucial point, DEPICT algorithm provides a joint learning framework that optimizes the soft-max and autoencoder parameters together.

<!-- chunk {"id": "body-0040", "role": "body", "section": "DEPICT Architecture", "weight": 1.0} -->

where $|\mathbf{z}_{i}^{l}|$ is the output size of the $l$-th hidden layer (input for $l = 0$), and $L$ is the depth of the autoencoder model.

<!-- chunk {"id": "body-0041", "role": "body", "section": "DEPICT Architecture", "weight": 1.0} -->

The benefit of joint learning frameworks for training multi-layer autoencoders is also reported in semi-supervised classification tasks. However, DEPICT is different from previous studies, since it is designed for the unsupervised clustering task, it also does not require max-pooling switches used in stacked what-where autoencoder (SWWAE), and lateral (skip) connections between encoder and decoder layers used in ladder network. Algorithm 1 shows a brief description of DEPICT algorithm.

<!-- chunk {"id": "body-0042", "role": "body", "section": "Experiments", "weight": 1.0} -->

In this section, we first evaluate DEPICT^11^1Our code is available in in comparison with state-of-the-art clustering methods on several benchmark image datasets. Then, the running speed of the best clustering models are compared. Moreover, we examine different learning approaches for training DEPICT. Finally, we analyze the performance of DEPICT model on semi-supervised classification tasks.

<!-- chunk {"id": "body-0043", "role": "body", "section": "Experiments", "weight": 1.0} -->

Datasets: In order to show that DEPICT works well with various kinds of datasets, we have chosen the following handwritten digit and face image datasets. Considering that clustering tasks are fully unsupervised, we concatenate the training and testing samples when applicable. MNIST-full: A dataset containing a total of 70,000 handwritten digits with 60,000 training and 10,000 testing samples, each being a 32 by 32 monochrome image. MNIST-test: A dataset which only consists of the testing part of MNIST-full data. USPS: It is a handwritten digits dataset from the USPS postal service, containing 11,000 samples of 16 by 16 images. CMU-PIE: A dataset including 32 by 32 face images of 68 people with 4 different expressions. Youtube-Face (YTF): Following, we choose the first 41 subjects of YTF dataset. Faces inside images are first cropped and then resized to 55 by 55 sizes. FRGC: Using the 20 random selected subjects in from the original dataset, we collect 2,462 face images.

<!-- chunk {"id": "body-0044", "role": "body", "section": "Experiments", "weight": 1.0} -->

Similarly, we first crop the face regions and resize them into 32 by 32 images. Table 1 provides a brief description of each dataset.

<!-- chunk {"id": "body-0045", "role": "body", "section": "Experiments", "weight": 1.0} -->

## Samples
## Classes
## Dimensions

<!-- chunk {"id": "body-0046", "role": "body", "section": "Experiments", "weight": 1.0} -->

Clustering Metrics: We have used 2 of the most popular evaluation criteria widely used for clustering algorithms, accuracy (ACC) and normalized mutual information (NMI). The best mapping between cluster assignments and true labels is computed using the Hungarian algorithm to measure accuracy. NMI calculates the normalized measure of similarity between two labels of the same data. Results of NMI do not change by permutations of clusters (classes), and they are normalized to have $\lbrack 0,1\rbrack$ range, with $0$ meaning no correlation and $1$ exhibiting perfect correlation.

<!-- chunk {"id": "body-0047", "role": "body", "section": "Evaluation of Clustering Algorithm", "weight": 1.0} -->

Alternative Models: We compare our clustering model, DEPICT, with several baseline and state-of-the-art clustering algorithms, including $K$-means, normalized cuts (N-Cuts), self-tuning spectral clustering (SC-ST), large-scale spectral clustering (SC-LS), graph degree linkage-based agglomerative clustering (AC-GDL), agglomerative clustering via path integral (AC-PIC), spectral embedded clustering (SEC), local discriminant models and global integration (LDMGI), NMF with deep model (NMF-D), task-specific clustering with deep model (TSC-D), deep embedded clustering (DEC), and joint unsupervised learning (JULE).

<!-- chunk {"id": "body-0048", "role": "body", "section": "Evaluation of Clustering Algorithm", "weight": 1.0} -->

Implementation Details: We use a common architecture for DEPICT and avoid tuning any hyper-parameters using the labeled data in order to provide a practical algorithm for real-world clustering tasks. For all datasets, we consider two convolutional layers followed by a fully connected layer in encoder and decoder pathways. While for all convolutional layers, the feature map size is 50 and the kernel size is about $5 \times 5$, the dimension of the embedding subspace is set equal to the number of clusters in each dataset. We also pick the proper stride, padding and crop to have an output size of about $10 \times 10$ in the second convolutional layer. Inspired, we consider leaky rectified (leaky RELU) non-linearity as the activation function of convolutional and fully connected layers, except in the last layer of encoder and first layer of decoder, which have Tanh non-linearity functions. Consequently, we normalize the image intensities to be in the range of $\lbrack{- 1},1\rbrack$.

<!-- chunk {"id": "body-0049", "role": "body", "section": "Evaluation of Clustering Algorithm", "weight": 1.0} -->

Moreover, we set the learning rate and dropout to $10^{- 4}$ and $0.1$ respectively, adopt adam as our optimization method with the default hyper-parameters $\beta_{1} = 0.9$, $\beta_{2} = 0.999$, $\epsilon = {{1e} - 08}$. The weights of convolutional and fully connected layers are all initialized by Xavier approach. Since the clustering assignments in the first iterations are random and not reliable for clustering loss, we first train DEPICT without clustering loss function for a while, then initialize the clustering assignment $q_{ik}$ by clustering the embedding subspace features via simple algorithms like $K$-means or AC-PIC.

<!-- chunk {"id": "body-0050", "role": "body", "section": "Evaluation of Clustering Algorithm", "weight": 1.0} -->

Quantitative Comparison: We run DEPICT and other clustering methods on each dataset. We followed the implementation details for DEPICT and report the average results from 5 runs. For the rest, we present the best reported results either from their original papers or. For unreported results on specific datasets, we run the released code with hyper-parameters mentioned in the original papers, these results are marked by ($\ast$) on top. But, when the code is not publicly available, or running the released code is not practical, we put dash marks (-) instead of the corresponding results. Moreover, we mention the number of hyper-parameters that are tuned using supervisory signals (labeled data) for each algorithm. Note that this number only shows the quantity of hyper-parameters, which are set differently for various datasets for better performance.

<!-- chunk {"id": "body-0051", "role": "body", "section": "Evaluation of Clustering Algorithm", "weight": 1.0} -->

Table 2 reports the clustering metrics, normalized mutual information (NMI) and accuracy (ACC), of the algorithms on the aforementioned datasets. As shown, DEPICT outperforms other algorithms on four datasets and achieves competitive results on the remaining two. It should be noted that we think hyper-parameter tuning using supervisory signals is not feasible in real-world clustering tasks, and hence DEPICT is a significantly better clustering algorithm compared to the alternative models in practice. For example, DEC, SEC, and LDMGI report their best results by tuning one hyper-parameter over nine different options, and JULE-SF and JULE-RC achieve their good performance by tweaking several hyper-parameters over various datasets. However, we do not tune any hyper-parameters for DEPICT using the labeled data and only report the result with the same (default) hyper-parameters for all datasets.

<!-- chunk {"id": "body-0052", "role": "body", "section": "Running Time Comparison", "weight": 1.0} -->

In order to evaluate the efficiency of our clustering algorithm in dealing with large-scale and high dimensional data, we compare the running speed of DEPICT with its competing algorithms, JULE-SF and JULE-RC. Moreover, the fast versions of JULE-SF and JULE-RC are also evaluated. Note that JULE-SF(fast) and JULE-RC(fast) both require tuning one extra hyper-parameter for each dataset to achieve results similar to the original JULE algorithms in Table 2. We run DEPICT and the released code for JULE algorithms^22^2 on a machine with one Titan X pascal GPU and a Xeon E5-2699 CPU.

<!-- chunk {"id": "body-0053", "role": "body", "section": "Evaluation of Learning Approach", "weight": 1.0} -->

In order to evaluate our joint learning approach, we compare several strategies for training DEPICT. For training a multi-layer convolutional autoencoder, we analyze the following three approaches: 1) Standard stacked denoising autoencoder (SdA), in which the model is first pretrained using the reconstruction loss function in a layer-wise manner, and the encoder pathway is then fine-tuned using the clustering objective function. 2) Another approach (RdA) is suggested in to improve the SdA learning approach, in which all of the autoencoder layers are retrained after the pretraining step, only using the reconstruction of input layer while data is not corrupted by noise. The fine-tuning step is also done after the retraining step. 3) Our learning approach (MdA), in which the whole model is trained simultaneously using the joint reconstruction loss functions from all layers along with the clustering objective function.

<!-- chunk {"id": "body-0054", "role": "body", "section": "Evaluation of Learning Approach", "weight": 1.0} -->

Furthermore, we also examine the effect of clustering loss (through error back-prop) in constructing the embedding subspace. To do so, we train a similar multi-layer convolutional autoencoder (Deep-ConvAE) only using the reconstruction loss function to generate the embedding subspace. Then, we run the best shallow clustering algorithm (AC-PIC) on the embedded data. Hence, this model (Deep-ConvAE+AC-PIC) differs from DEPICT in the sense that its embedding subspace is only constructed using the reconstruction loss and does not involve the clustering loss.

<!-- chunk {"id": "body-0055", "role": "body", "section": "Evaluation of Learning Approach", "weight": 1.0} -->

Table 3 indicates the results of DEPICT and Deep-ConvAE+AC-PIC when using the different learning approaches. As expected, DEPICT trained by our joint learning approach (MdA) consistently outperforms the other alternatives on all datasets. Interestingly, MdA learning approach shows promising results for Deep-ConvAE+AC-PIC model, where only reconstruction losses are used to train the embedding subspace. Thus, our learning approach is an efficient strategy for training autoencoder models due to its superior results and fast end-to-end training.

<!-- chunk {"id": "body-0056", "role": "body", "section": "Semi-Supervised Classification Performance", "weight": 1.0} -->

Representation learning in an unsupervised manner or using a small number of labeled data has recently attracted great attention. Due to the potential of our model in learning a discriminative embedding subspace, we evaluate DEPICT in a semi-supervised classification task. Following the semi-supervised experiment settings, we train our model using a small random subset of MNIST-training dataset as labeled data and the remaining as unlabeled data. The classification error of DEPICT is then computed using the MNIST-test dataset, which is not seen during training. Compared to our unsupervised learning approach, we only utilize the clusters corresponding to each labeled data in training process. In particular, only for labeled data, the cluster labels (assignments) are set using the best map technique from the original classification labels once, and then they will be fixed during the training step.

<!-- chunk {"id": "body-0057", "role": "body", "section": "Semi-Supervised Classification Performance", "weight": 1.0} -->

Table 4 shows the error results for several semi-supervised classification models using different numbers of labeled data. Surprisingly, DEPICT achieves comparable results with the state-of-the-art, despite the fact that the semi-supervised classification models use 10,000 validation data to tune their hyper-parameters, DEPICT only employs the labeled training data (e.g. 100) and does not tune any hyper-parameters. Although DEPICT is not mainly designed for classification tasks, it outperforms several models including SWWAE, M1+M2, and AtlasRBF, and has comparable results with the complicated Ladder network. These results further confirm the discriminative quality of the embedding features of DEPICT.

<!-- chunk {"id": "body-0058", "role": "body", "section": "Conclusion", "weight": 1.5} -->

In this paper, we proposed a new deep clustering model, DEPICT, consisting of a soft-max layer stacked on top of a multi-layer convolutional autoencoder. We employed a regularized relative entropy loss function for clustering, which leads to balanced cluster assignments. Adopting our autoencoder reconstruction loss function enhanced the embedding learning. Furthermore, a joint learning framework was introduced to train all network layers simultaneously and avoid layer-wise pretraining. Experimental results showed that DEPICT is a good candidate for real-world clustering tasks, since it achieved superior or competitive results compared to alternative methods while having faster running speed and not needing hyper-parameter tuning. Efficiency of our joint learning approach was also confirmed in clustering and semi-supervised classification tasks.
