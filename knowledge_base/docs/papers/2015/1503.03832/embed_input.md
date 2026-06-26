<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

FaceNet: A Unified Embedding for Face Recognition and Clustering

Topics include Deep learning, Convolutional networks, Clustering, Datasets, Accuracy, Online algorithms, Learning, FaceNet, LFW.

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Despite significant recent advances in the field of face recognition, implementing face verification and recognition efficiently at scale presents serious challenges to current approaches. In this paper we present a system, called FaceNet, that directly learns a mapping from face images to a compact Euclidean space where distances directly correspond to a measure of face similarity. Once this space has been produced, tasks such as face recognition, verification and clustering can be easily implemented using standard techniques with FaceNet embeddings as feature vectors. Our method uses a deep convolutional network trained to directly optimize the embedding itself, rather than an intermediate bottleneck layer as in previous deep learning approaches. To train, we use triplets of roughly aligned matching / non-matching face patches generated using a novel online triplet mining method. The benefit of our approach is much greater representational efficiency: we achieve state-of-the-art face recognition performance using only 128-bytes per face. On the widely used Labeled Faces in the Wild (LFW) dataset, our system achieves a new record accuracy of 99.63%. On YouTube Faces DB it achieves 95.12%.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Our system cuts the error rate in comparison to the best published result by 30% on both datasets. We also introduce the concept of harmonic embeddings, and a harmonic triplet loss, which describe different versions of face embeddings (produced by different networks) that are compatible to each other and allow for direct comparison between each other.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

In this paper we present a unified system for face verification (is this the same person), recognition (who is this person) and clustering (find common people among these faces). Our method is based on learning a Euclidean embedding per image using a deep convolutional network. The network is trained such that the squared L2 distances in the embedding space directly correspond to face similarity: faces of the same person have small distances and faces of distinct people have large distances.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

Once this embedding has been produced, then the aforementioned tasks become straight-forward: face verification simply involves thresholding the distance between the two embeddings; recognition becomes a k-NN classification problem; and clustering can be achieved using off-the-shelf techniques such as k-means or agglomerative clustering.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

Previous face recognition approaches based on deep networks use a classification layer trained over a set of known face identities and then take an intermediate bottleneck layer as a representation used to generalize recognition beyond the set of identities used in training. The downsides of this approach are its indirectness and its inefficiency: one has to hope that the bottleneck representation generalizes well to new faces; and by using a bottleneck layer the representation size per face is usually very large (1000s of dimensions). Some recent work has reduced this dimensionality using PCA, but this is a linear transformation that can be easily learnt in one layer of the network.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

In contrast to these approaches, FaceNet directly trains its output to be a compact 128-D embedding using a triplet-based loss function based on LMNN. Our triplets consist of two matching face thumbnails and a non-matching face thumbnail and the loss aims to separate the positive pair from the negative by a distance margin. The thumbnails are tight crops of the face area, no 2D or 3D alignment, other than scale and translation is performed.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Introduction", "weight": 1.5} -->

Choosing which triplets to use turns out to be very important for achieving good performance and, inspired by curriculum learning, we present a novel online negative exemplar mining strategy which ensures consistently increasing difficulty of triplets as the network trains. To improve clustering accuracy, we also explore hard-positive mining techniques which encourage spherical clusters for the embeddings of a single person.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Introduction", "weight": 1.5} -->

As an illustration of the incredible variability that our method can handle see Figure 1. Shown are image pairs from PIE that previously were considered to be very difficult for face verification systems.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Introduction", "weight": 1.5} -->

An overview of the rest of the paper is as follows: in section 2 we review the literature in this area; section 3.1 defines the triplet loss and section 3.2 describes our novel triplet selection and training procedure; in section 3.3 we describe the model architecture used. Finally in section 4 and 5 we present some quantitative results of our embeddings and also qualitatively explore some clustering results.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Method", "weight": 1.0} -->

FaceNet uses a deep convolutional network. We discuss two different core architectures: The Zeiler&Fergus style networks and the recent Inception type networks. The details of these networks are described in section 3.3.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Method", "weight": 1.0} -->

Given the model details, and treating it as a black box (see Figure 2), the most important part of our approach lies in the end-to-end learning of the whole system. To this end we employ the triplet loss that directly reflects what we want to achieve in face verification, recognition and clustering. Namely, we strive for an embedding $f{(x)}$, from an image $x$ into a feature space ${\mathbb{R}}^{d}$, such that the squared distance between *all* faces, independent of imaging conditions, of the same identity is small, whereas the squared distance between a pair of face images from different identities is large.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Method", "weight": 1.0} -->

Although we did not directly compare to other losses, *e.g*. the one using pairs of positives and negatives, as used in Eq., we believe that the triplet loss is more suitable for face verification. The motivation is that the loss from encourages all faces of one identity to be projected onto a single point in the embedding space. The triplet loss, however, tries to enforce a margin between each pair of faces from one person to all other faces. This allows the faces for one identity to live on a manifold, while still enforcing the distance and thus discriminability to other identities.

<!-- chunk {"id": "body-0014", "role": "body", "section": "Method", "weight": 1.0} -->

The following section describes this triplet loss and how it can be learned efficiently at scale.

<!-- chunk {"id": "body-0015", "role": "body", "section": "Triplet Loss", "weight": 1.0} -->

The embedding is represented by ${f{(x)}} \in {\mathbb{R}}^{d}$. It embeds an image $x$ into a $d$-dimensional Euclidean space. Additionally, we constrain this embedding to live on the $d$-dimensional hypersphere, *i.e*. ${\|{f{(x)}}\|}_{2} = 1$. This loss is motivated in in the context of nearest-neighbor classification. Here we want to ensure that an image $x_{i}^{a}$ (*anchor*) of a specific person is closer to all other images $x_{i}^{p}$ (*positive*) of the same person than it is to any image $x_{i}^{n}$ (*negative*) of any other person. This is visualized in Figure 3. where $\alpha$ is a margin that is enforced between positive and negative pairs. $\mathcal{T}$ is the set of all possible triplets in the training set and has cardinality $N$.

<!-- chunk {"id": "body-0016", "role": "body", "section": "Triplet Loss", "weight": 1.0} -->

The loss that is being minimized is then $L =$ Generating all possible triplets would result in many triplets that are easily satisfied (*i.e*. fulfill the constraint in Eq.). These triplets would not contribute to the training and result in slower convergence, as they would still be passed through the network. It is crucial to select hard triplets, that are active and can therefore contribute to improving the model. The following section talks about the different approaches we use for the triplet selection.

<!-- chunk {"id": "body-0017", "role": "body", "section": "Triplet Selection", "weight": 1.0} -->

It is infeasible to compute the $argmin$ and $argmax$ across the whole training set. Additionally, it might lead to poor training, as mislabelled and poorly imaged faces would dominate the hard positives and negatives. There are two obvious choices that avoid this issue: Generate triplets offline every n steps, using the most recent network checkpoint and computing the $argmin$ and $argmax$ on a subset of the data.

<!-- chunk {"id": "body-0018", "role": "body", "section": "Triplet Selection", "weight": 1.0} -->

Generate triplets online. This can be done by selecting the hard positive/negative exemplars from within a mini-batch.

<!-- chunk {"id": "body-0019", "role": "body", "section": "Triplet Selection", "weight": 1.0} -->

Here, we focus on the online generation and use large mini-batches in the order of a few thousand exemplars and only compute the $argmin$ and $argmax$ within a mini-batch.

<!-- chunk {"id": "body-0020", "role": "body", "section": "Triplet Selection", "weight": 1.0} -->

To have a meaningful representation of the anchor-positive distances, it needs to be ensured that a minimal number of exemplars of any one identity is present in each mini-batch. In our experiments we sample the training data such that around 40 faces are selected per identity per mini-batch. Additionally, randomly sampled negative faces are added to each mini-batch.

<!-- chunk {"id": "body-0021", "role": "body", "section": "Triplet Selection", "weight": 1.0} -->

Instead of picking the hardest positive, we use all anchor-positive pairs in a mini-batch while still selecting the hard negatives. We don't have a side-by-side comparison of hard anchor-positive pairs versus all anchor-positive pairs within a mini-batch, but we found in practice that the all anchor-positive method was more stable and converged slightly faster at the beginning of training.

<!-- chunk {"id": "body-0022", "role": "body", "section": "Triplet Selection", "weight": 1.0} -->

We also explored the offline generation of triplets in conjunction with the online generation and it may allow the use of smaller batch sizes, but the experiments were inconclusive.

<!-- chunk {"id": "body-0023", "role": "body", "section": "Triplet Selection", "weight": 1.0} -->

Selecting the hardest negatives can in practice lead to bad local minima early on in training, specifically it can result in a collapsed model (*i.e*. ${f{(x)}} = 0$). In order to mitigate this, it helps to select $x_{i}^{n}$ such that We call these negative exemplars *semi-hard*, as they are further away from the anchor than the positive exemplar, but still hard because the squared distance is close to the anchor-positive distance. Those negatives lie inside the margin $\alpha$.

<!-- chunk {"id": "body-0024", "role": "body", "section": "Triplet Selection", "weight": 1.0} -->

As mentioned before, correct triplet selection is crucial for fast convergence. On the one hand we would like to use small mini-batches as these tend to improve convergence during Stochastic Gradient Descent (SGD). On the other hand, implementation details make batches of tens to hundreds of exemplars more efficient. The main constraint with regards to the batch size, however, is the way we select hard relevant triplets from within the mini-batches. In most experiments we use a batch size of around 1,800 exemplars.

<!-- chunk {"id": "body-0025", "role": "body", "section": "Deep Convolutional Networks", "weight": 1.0} -->

In all our experiments we train the CNN using Stochastic Gradient Descent (SGD) with standard backprop and AdaGrad. In most experiments we start with a learning rate of $0.05$ which we lower to finalize the model. The models are initialized from random, similar to, and trained on a CPU cluster for 1,000 to 2,000 hours. The decrease in the loss (and increase in accuracy) slows down drastically after 500h of training, but additional training can still significantly improve performance. The margin $\alpha$ is set to $0.2$.

<!-- chunk {"id": "body-0026", "role": "body", "section": "Deep Convolutional Networks", "weight": 1.0} -->

We used two types of architectures and explore their trade-offs in more detail in the experimental section. Their practical differences lie in the difference of parameters and FLOPS. The best model may be different depending on the application. *E.g*. a model running in a datacenter can have many parameters and require a large number of FLOPS, whereas a model running on a mobile phone needs to have few parameters, so that it can fit into memory. All our models use rectified linear units as the non-linear activation function.

<!-- chunk {"id": "body-0027", "role": "body", "section": "Deep Convolutional Networks", "weight": 1.0} -->

The first category, shown in Table 1, adds $1 \times 1 \times d$ convolutional layers, as suggested, between the standard convolutional layers of the Zeiler&Fergus architecture and results in a model 22 layers deep. It has a total of 140 million parameters and requires around 1.6 billion FLOPS per image.

<!-- chunk {"id": "body-0028", "role": "body", "section": "Deep Convolutional Networks", "weight": 1.0} -->

The second category we use is based on GoogLeNet style Inception models. These models have $20 \times$ fewer parameters (around 6.6M-7.5M) and up to $5 \times$ fewer FLOPS (between 500M-1.6B). Some of these models are dramatically reduced in size (both depth and number of filters), so that they can be run on a mobile phone. One, NNS1, has 26M parameters and only requires 220M FLOPS per image. The other, NNS2, has 4.3M parameters and 20M FLOPS. Table 2 describes NN2 our largest network in detail. NN3 is identical in architecture but has a reduced input size of 160x160. NN4 has an input size of only 96x96, thereby drastically reducing the CPU requirements (285M FLOPS vs 1.6B for NN2). In addition to the reduced input size it does not use 5x5 convolutions in the higher layers as the receptive field is already too small by then. Generally we found that the 5x5 convolutions can be removed throughout with only a minor drop in accuracy.

<!-- chunk {"id": "body-0029", "role": "body", "section": "Deep Convolutional Networks", "weight": 1.0} -->

Figure 4 compares all our models.

<!-- chunk {"id": "body-0030", "role": "body", "section": "× 5", "weight": 1.0} -->

max pool + norm norm + max pool Table 2: NN2. Details of the NN2 Inception incarnation. This model is almost identical to the one described. The two major differences are the use of L2 pooling instead of max pooling (m), where specified. I.e. instead of taking the spatial max the L2 norm is computed. The pooling is always 3 × 3 (aside from the final average pooling) and in parallel to the convolutional modules inside each Inception module. If there is a dimensionality reduction after the pooling it is denoted with p. 1 × 1, 3 × 3, and 5 × 5 pooling are then concatenated to get the final output.

<!-- chunk {"id": "body-0031", "role": "body", "section": "Datasets and Evaluation", "weight": 1.0} -->

We evaluate our method on four datasets and with the exception of Labelled Faces in the Wild and YouTube Faces we evaluate our method on the face verification task. *I.e*. given a pair of two face images a squared $L_{2}$ distance threshold $D{(x_{i},x_{j})}$ is used to determine the classification of *same* and *different*. All faces pairs $(i,j)$ of the same identity are denoted with $\mathcal{P}_{\text{same}}$, whereas all pairs of different identities are denoted with $\mathcal{P}_{\text{diff}}$.

<!-- chunk {"id": "body-0032", "role": "body", "section": "Datasets and Evaluation", "weight": 1.0} -->

We define the set of all *true accepts* as These are the face pairs $(i,j)$ that were correctly classified as *same* at threshold $d$. Similarly is the set of all pairs that was incorrectly classified as *same* (*false accept*).

<!-- chunk {"id": "body-0033", "role": "body", "section": "Datasets and Evaluation", "weight": 1.0} -->

The validation rate ${VAL}{(d)}$ and the false accept rate ${FAR}{(d)}$ for a given face distance $d$ are then defined as

<!-- chunk {"id": "body-0034", "role": "body", "section": "Hold-out Test Set", "weight": 1.0} -->

We keep a hold out set of around one million images, that has the same distribution as our training set, but disjoint identities. For evaluation we split it into five disjoint sets of $200\text{k}$ images each. The $FAR$ and $VAL$ rate are then computed on ${{100\text{k}} \times 100}\text{k}$ image pairs. Standard error is reported across the five splits.

<!-- chunk {"id": "body-0035", "role": "body", "section": "Personal Photos", "weight": 1.0} -->

This is a test set with similar distribution to our training set, but has been manually verified to have very clean labels. It consists of three personal photo collections with a total of around $12\text{k}$ images. We compute the $FAR$ and $VAL$ rate across all 12k squared pairs of images.

<!-- chunk {"id": "body-0036", "role": "body", "section": "Academic Datasets", "weight": 1.0} -->

Labeled Faces in the Wild (LFW) is the de-facto academic test set for face verification. We follow the standard protocol for *unrestricted, labeled outside data* and report the mean classification accuracy as well as the standard error of the mean.

<!-- chunk {"id": "body-0037", "role": "body", "section": "Academic Datasets", "weight": 1.0} -->

Youtube Faces DB is a new dataset that has gained popularity in the face recognition community. The setup is similar to LFW, but instead of verifying pairs of images, pairs of videos are used.

<!-- chunk {"id": "body-0038", "role": "body", "section": "Experiments", "weight": 1.0} -->

If not mentioned otherwise we use between 100M-200M training face thumbnails consisting of about 8M different identities. A face detector is run on each image and a tight bounding box around each face is generated. These face thumbnails are resized to the input size of the respective network. Input sizes range from 96x96 pixels to 224x224 pixels in our experiments.

<!-- chunk {"id": "body-0039", "role": "body", "section": "Computation Accuracy Trade-off", "weight": 1.0} -->

Before diving into the details of more specific experiments we will discuss the trade-off of accuracy versus number of FLOPS that a particular model requires. Figure 4 shows the FLOPS on the x-axis and the accuracy at 0.001 false accept rate ($FAR$) on our user labelled test-data set from section 4.2. It is interesting to see the strong correlation between the computation a model requires and the accuracy it achieves. The figure highlights the five models (NN1, NN2, NN3, NNS1, NNS2) that we discuss in more detail in our experiments.

<!-- chunk {"id": "body-0040", "role": "body", "section": "Computation Accuracy Trade-off", "weight": 1.0} -->

We also looked into the accuracy trade-off with regards to the number of model parameters. However, the picture is not as clear in that case. For example, the Inception based model NN2 achieves a comparable performance to NN1, but only has a 20th of the parameters. The number of FLOPS is comparable, though. Obviously at some point the performance is expected to decrease, if the number of parameters is reduced further. Other model architectures may allow further reductions without loss of accuracy, just like Inception did in this case.

<!-- chunk {"id": "body-0041", "role": "body", "section": "Effect of CNN Model", "weight": 1.0} -->

NNS1 (mini Inception 165 × 165) NNS2 (tiny Inception 140 × 116) Table 3: Network Architectures. This table compares the performance of our model architectures on the hold out test set (see section 4.1). Reported is the mean validation rate VAL at 10 e-3 false accept rate. Also shown is the standard error of the mean across the five test splits.

<!-- chunk {"id": "body-0042", "role": "body", "section": "Effect of CNN Model", "weight": 1.0} -->

We now discuss the performance of our four selected models in more detail. On the one hand we have our traditional Zeiler&Fergus based architecture with $1 \times 1$ convolutions (see Table 1). On the other hand we have Inception based models that dramatically reduce the model size. Overall, in the final performance the top models of both architectures perform comparably. However, some of our Inception based models, such as NN3, still achieve good performance while significantly reducing both the FLOPS and the model size.

<!-- chunk {"id": "body-0043", "role": "body", "section": "Effect of CNN Model", "weight": 1.0} -->

The detailed evaluation on our personal photos test set is shown in Figure 5. While the largest model achieves a dramatic improvement in accuracy compared to the tiny NNS2, the latter can be run 30ms / image on a mobile phone and is still accurate enough to be used in face clustering. The sharp drop in the ROC for ${FAR} < 10^{- 4}$ indicates noisy labels in the test data groundtruth. At extremely low false accept rates a single mislabeled image can have a significant impact on the curve.

<!-- chunk {"id": "body-0044", "role": "body", "section": "Sensitivity to Image Quality", "weight": 1.0} -->

#pixels

<!-- chunk {"id": "body-0045", "role": "body", "section": "Sensitivity to Image Quality", "weight": 1.0} -->

Table 4 shows the robustness of our model across a wide range of image sizes. The network is surprisingly robust with respect to JPEG compression and performs very well down to a JPEG quality of 20. The performance drop is very small for face thumbnails down to a size of 120x120 pixels and even at 80x80 pixels it shows acceptable performance. This is notable, because the network was trained on 220x220 input images. Training with lower resolution faces could improve this range further.

<!-- chunk {"id": "body-0046", "role": "body", "section": "Embedding Dimensionality", "weight": 1.0} -->

#dims

<!-- chunk {"id": "body-0047", "role": "body", "section": "Embedding Dimensionality", "weight": 1.0} -->

We explored various embedding dimensionalities and selected 128 for all experiments other than the comparison reported in Table 5. One would expect the larger embeddings to perform at least as good as the smaller ones, however, it is possible that they require more training to achieve the same accuracy. That said, the differences in the performance reported in Table 5 are statistically insignificant.

<!-- chunk {"id": "body-0048", "role": "body", "section": "Embedding Dimensionality", "weight": 1.0} -->

It should be noted, that during training a 128 dimensional float vector is used, but it can be quantized to 128-bytes without loss of accuracy. Thus each face is compactly represented by a 128 dimensional byte vector, which is ideal for large scale clustering and recognition. Smaller embeddings are possible at a minor loss of accuracy and could be employed on mobile devices.

<!-- chunk {"id": "body-0049", "role": "body", "section": "Amount of Training Data", "weight": 1.0} -->

#training images

<!-- chunk {"id": "body-0050", "role": "body", "section": "Amount of Training Data", "weight": 1.0} -->

Table 6 shows the impact of large amounts of training data. Due to time constraints this evaluation was run on a smaller model; the effect may be even larger on larger models. It is clear that using tens of millions of exemplars results in a clear boost of accuracy on our personal photo test set from section 4.2. Compared to only millions of images the relative reduction in error is 60%. Using another order of magnitude more images (hundreds of millions) still gives a small boost, but the improvement tapers off.

<!-- chunk {"id": "body-0051", "role": "body", "section": "Performance on LFW", "weight": 1.0} -->

False accept False reject Figure 6: LFW errors. This shows all pairs of images that were incorrectly classified on LFW. Only eight of the 13 false rejects shown here are actual errors the other five are mislabeled in LFW.

<!-- chunk {"id": "body-0052", "role": "body", "section": "Performance on LFW", "weight": 1.0} -->

We evaluate our model on LFW using the standard protocol for *unrestricted, labeled outside data*. Nine training splits are used to select the $L_{2}$-distance threshold. Classification (*same* or *different*) is then performed on the tenth test split. The selected optimal threshold is $1.242$ for all test splits except split eighth ($1.256$).

<!-- chunk {"id": "body-0053", "role": "body", "section": "Performance on LFW", "weight": 1.0} -->

Our model is evaluated in two modes: Fixed center crop of the LFW provided thumbnail.

<!-- chunk {"id": "body-0054", "role": "body", "section": "Performance on LFW", "weight": 1.0} -->

A proprietary face detector (similar to Picasa ) is run on the provided LFW thumbnails. If it fails to align the face (this happens for two images), the LFW alignment is used.

<!-- chunk {"id": "body-0055", "role": "body", "section": "Performance on Youtube Faces DB", "weight": 1.0} -->

We use the average similarity of all pairs of the first one hundred frames that our face detector detects in each video. This gives us a classification accuracy of 95.12%$\pm 0.39$. Using the first one thousand frames results in 95.18%. Compared to 91.4% who also evaluate one hundred frames per video we reduce the error rate by almost half. DeepId2+ achieved 93.2% and our method reduces this error by 30%, comparable to our improvement on LFW.

<!-- chunk {"id": "body-0056", "role": "body", "section": "Face Clustering", "weight": 1.0} -->

Our compact embedding lends itself to be used in order to cluster a users personal photos into groups of people with the same identity. The constraints in assignment imposed by clustering faces, compared to the pure verification task, lead to truly amazing results. Figure 7 shows one cluster in a users personal photo collection, generated using agglomerative clustering. It is a clear showcase of the incredible invariance to occlusion, lighting, pose and even age.

<!-- chunk {"id": "body-0057", "role": "body", "section": "Summary", "weight": 1.0} -->

We provide a method to directly learn an embedding into an Euclidean space for face verification. This sets it apart from other methods who use the CNN bottleneck layer, or require additional post-processing such as concatenation of multiple models and PCA, as well as SVM classification. Our end-to-end training both simplifies the setup and shows that directly optimizing a loss relevant to the task at hand improves performance.

<!-- chunk {"id": "body-0058", "role": "body", "section": "Summary", "weight": 1.0} -->

Another strength of our model is that it only requires minimal alignment (tight crop around the face area)., for example, performs a complex 3D alignment. We also experimented with a similarity transform alignment and notice that this can actually improve performance slightly. It is not clear if it is worth the extra complexity.

<!-- chunk {"id": "body-0059", "role": "body", "section": "Summary", "weight": 1.0} -->

Future work will focus on better understanding of the error cases, further improving the model, and also reducing model size and reducing CPU requirements. We will also look into ways of improving the currently extremely long training times, *e.g*. variations of our curriculum learning with smaller batch sizes and offline as well as online positive and negative mining.
