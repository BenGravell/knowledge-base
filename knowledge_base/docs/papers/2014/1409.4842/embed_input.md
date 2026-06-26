<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Going Deeper with Convolutions

Topics include Neural networks, Convolutional networks, Classification, Inception, Convolutional neural network, Network architecture.

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

We propose a deep convolutional neural network architecture codenamed "Inception", which was responsible for setting the new state of the art for classification and detection in the ImageNet Large-Scale Visual Recognition Challenge 2014. The main hallmark of this architecture is the improved utilization of the computing resources inside the network. This was achieved by a carefully crafted design that allows for increasing the depth and width of the network while keeping the computational budget constant. To optimize quality, the architectural decisions were based on the Hebbian principle and the intuition of multi-scale processing. One particular incarnation used in our submission for ILSVRC 2014 is called GoogLeNet, a 22 layers deep network, the quality of which is assessed in the context of classification and detection.

<!-- chunk {"id": "body-0003", "role": "body", "section": "Introduction", "weight": 1.5} -->

In the last three years, mainly due to the advances of deep learning, more concretely convolutional networks, the quality of image recognition and object detection has been progressing at a dramatic pace. One encouraging news is that most of this progress is not just the result of more powerful hardware, larger datasets and bigger models, but mainly a consequence of new ideas, algorithms and improved network architectures. No new data sources were used, for example, by the top entries in the ILSVRC 2014 competition besides the classification dataset of the same competition for detection purposes. Our GoogLeNet submission to ILSVRC 2014 actually uses $12 \times$ fewer parameters than the winning architecture of Krizhevsky et al from two years ago, while being significantly more accurate. The biggest gains in object-detection have not come from the utilization of deep networks alone or bigger models, but from the synergy of deep architectures and classical computer vision, like the R-CNN algorithm by Girshick et al.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

Another notable factor is that with the ongoing traction of mobile and embedded computing, the efficiency of our algorithms -- especially their power and memory use -- gains importance. It is noteworthy that the considerations leading to the design of the deep architecture presented in this paper included this factor rather than having a sheer fixation on accuracy numbers. For most of the experiments, the models were designed to keep a computational budget of $1.5$ billion multiply-adds at inference time, so that the they do not end up to be a purely academic curiosity, but could be put to real world use, even on large datasets, at a reasonable cost.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

In this paper, we will focus on an efficient deep neural network architecture for computer vision, codenamed "Inception", which derives its name from the "Network in network" paper by Lin et al in conjunction with the famous "we need to go deeper" internet meme. In our case, the word "deep" is used in two different meanings: first of all, in the sense that we introduce a new level of organization in the form of the "Inception module" and also in the more direct sense of increased network depth. In general, one can view the Inception model as a logical culmination of while taking inspiration and guidance from the theoretical work by Arora et al. The benefits of the architecture are experimentally verified on the ILSVRC 2014 classification and detection challenges, on which it significantly outperforms the current state of the art.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Motivation and High Level Considerations", "weight": 1.0} -->

The most straightforward way of improving the performance of deep neural networks is by increasing their size. This includes both increasing the depth -- the number of levels -- of the network and its width: the number of units at each level. This is as an easy and safe way of training higher quality models, especially given the availability of a large amount of labeled training data. However this simple solution comes with two major drawbacks.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Motivation and High Level Considerations", "weight": 1.0} -->

Bigger size typically means a larger number of parameters, which makes the enlarged network more prone to overfitting, especially if the number of labeled examples in the training set is limited. This can become a major bottleneck, since the creation of high quality training sets can be tricky and expensive, especially if expert human raters are necessary to distinguish between fine-grained visual categories like those in ImageNet (even in the 1000-class ILSVRC subset) as demonstrated by Figure 1.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Motivation and High Level Considerations", "weight": 1.0} -->

Another drawback of uniformly increased network size is the dramatically increased use of computational resources. For example, in a deep vision network, if two convolutional layers are chained, any uniform increase in the number of their filters results in a quadratic increase of computation. If the added capacity is used inefficiently (for example, if most weights end up to be close to zero), then a lot of computation is wasted. Since in practice the computational budget is always finite, an efficient distribution of computing resources is preferred to an indiscriminate increase of size, even when the main objective is to increase the quality of results.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Motivation and High Level Considerations", "weight": 1.0} -->

The fundamental way of solving both issues would be by ultimately moving from fully connected to sparsely connected architectures, even inside the convolutions. Besides mimicking biological systems, this would also have the advantage of firmer theoretical underpinnings due to the groundbreaking work of Arora et al.. Their main result states that if the probability distribution of the data-set is representable by a large, very sparse deep neural network, then the optimal network topology can be constructed layer by layer by analyzing the correlation statistics of the activations of the last layer and clustering neurons with highly correlated outputs. Although the strict mathematical proof requires very strong conditions, the fact that this statement resonates with the well known Hebbian principle -- neurons that fire together, wire together -- suggests that the underlying idea is applicable even under less strict conditions, in practice.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Motivation and High Level Considerations", "weight": 1.0} -->

On the downside, today's computing infrastructures are very inefficient when it comes to numerical calculation on non-uniform sparse data structures. Even if the number of arithmetic operations is reduced by $100 \times$, the overhead of lookups and cache misses is so dominant that switching to sparse matrices would not pay off. The gap is widened even further by the use of steadily improving, highly tuned, numerical libraries that allow for extremely fast dense matrix multiplication, exploiting the minute details of the underlying CPU or GPU hardware. Also, non-uniform sparse models require more sophisticated engineering and computing infrastructure. Most current vision oriented machine learning systems utilize sparsity in the spatial domain just by the virtue of employing convolutions. However, convolutions are implemented as collections of dense connections to the patches in the earlier layer. ConvNets have traditionally used random and sparse connection tables in the feature dimensions since in order to break the symmetry and improve learning, the trend changed back to full connections with in order to better optimize parallel computing. The uniformity of the structure and a large number of filters and greater batch size allow for utilizing efficient dense computation.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Motivation and High Level Considerations", "weight": 1.0} -->

This raises the question whether there is any hope for a next, intermediate step: an architecture that makes use of the extra sparsity, even at filter level, as suggested by the theory, but exploits our current hardware by utilizing computations on dense matrices. The vast literature on sparse matrix computations (e.g. ) suggests that clustering sparse matrices into relatively dense submatrices tends to give state of the art practical performance for sparse matrix multiplication. It does not seem far-fetched to think that similar methods would be utilized for the automated construction of non-uniform deep-learning architectures in the near future.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Motivation and High Level Considerations", "weight": 1.0} -->

The Inception architecture started out as a case study of the first author for assessing the hypothetical output of a sophisticated network topology construction algorithm that tries to approximate a sparse structure implied by for vision networks and covering the hypothesized outcome by dense, readily available components. Despite being a highly speculative undertaking, only after two iterations on the exact choice of topology, we could already see modest gains against the reference architecture based. After further tuning of learning rate, hyperparameters and improved training methodology, we established that the resulting Inception architecture was especially useful in the context of localization and object detection as the base network for and. Interestingly, while most of the original architectural choices have been questioned and tested thoroughly, they turned out to be at least locally optimal.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Motivation and High Level Considerations", "weight": 1.0} -->

One must be cautious though: although the proposed architecture has become a success for computer vision, it is still questionable whether its quality can be attributed to the guiding principles that have lead to its construction. Making sure would require much more thorough analysis and verification: for example, if automated tools based on the principles described below would find similar, but better topology for the vision networks. The most convincing proof would be if an automated system would create network topologies resulting in similar gains in other domains using the same algorithm but with very differently looking global architecture. At very least, the initial success of the Inception architecture yields firm motivation for exciting future work in this direction.

<!-- chunk {"id": "body-0014", "role": "body", "section": "Architectural Details", "weight": 1.0} -->

The main idea of the Inception architecture is based on finding out how an optimal local sparse structure in a convolutional vision network can be approximated and covered by readily available dense components. Note that assuming translation invariance means that our network will be built from convolutional building blocks. All we need is to find the optimal local construction and to repeat it spatially. Arora et al. suggests a layer-by layer construction in which one should analyze the correlation statistics of the last layer and cluster them into groups of units with high correlation. These clusters form the units of the next layer and are connected to the units in the previous layer. We assume that each unit from the earlier layer corresponds to some region of the input image and these units are grouped into filter banks. In the lower layers (the ones close to the input) correlated units would concentrate in local regions. This means, we would end up with a lot of clusters concentrated in a single region and they can be covered by a layer of $1 \times 1$ convolutions in the next layer, as suggested.

<!-- chunk {"id": "body-0015", "role": "body", "section": "Architectural Details", "weight": 1.0} -->

However, one can also expect that there will be a smaller number of more spatially spread out clusters that can be covered by convolutions over larger patches, and there will be a decreasing number of patches over larger and larger regions. In order to avoid patch-alignment issues, current incarnations of the Inception architecture are restricted to filter sizes $1 \times 1$, $3 \times 3$ and $5 \times 5$, however this decision was based more on convenience rather than necessity. It also means that the suggested architecture is a combination of all those layers with their output filter banks concatenated into a single output vector forming the input of the next stage. Additionally, since pooling operations have been essential for the success in current state of the art convolutional networks, it suggests that adding an alternative parallel pooling path in each such stage should have additional beneficial effect, too (see Figure 2(a)).

<!-- chunk {"id": "body-0016", "role": "body", "section": "Architectural Details", "weight": 1.0} -->

(a) Inception module, naïve version (b) Inception module with dimension reductions Figure 2: Inception module As these "Inception modules" are stacked on top of each other, their output correlation statistics are bound to vary: as features of higher abstraction are captured by higher layers, their spatial concentration is expected to decrease suggesting that the ratio of $3 \times 3$ and $5 \times 5$ convolutions should increase as we move to higher layers.

<!-- chunk {"id": "body-0017", "role": "body", "section": "Architectural Details", "weight": 1.0} -->

One big problem with the above modules, at least in this naïve form, is that even a modest number of $5 \times 5$ convolutions can be prohibitively expensive on top of a convolutional layer with a large number of filters. This problem becomes even more pronounced once pooling units are added to the mix: their number of output filters equals to the number of filters in the previous stage. The merging of the output of the pooling layer with the outputs of convolutional layers would lead to an inevitable increase in the number of outputs from stage to stage. Even while this architecture might cover the optimal sparse structure, it would do it very inefficiently, leading to a computational blow up within a few stages.

<!-- chunk {"id": "body-0018", "role": "body", "section": "Architectural Details", "weight": 1.0} -->

This leads to the second idea of the proposed architecture: judiciously applying dimension reductions and projections wherever the computational requirements would increase too much otherwise. This is based on the success of embeddings: even low dimensional embeddings might contain a lot of information about a relatively large image patch. However, embeddings represent information in a dense, compressed form and compressed information is harder to model. We would like to keep our representation sparse at most places (as required by the conditions of ) and compress the signals only whenever they have to be aggregated en masse. That is, $1 \times 1$ convolutions are used to compute reductions before the expensive $3 \times 3$ and $5 \times 5$ convolutions. Besides being used as reductions, they also include the use of rectified linear activation which makes them dual-purpose. The final result is depicted in Figure 2(b).

<!-- chunk {"id": "body-0019", "role": "body", "section": "Architectural Details", "weight": 1.0} -->

In general, an Inception network is a network consisting of modules of the above type stacked upon each other, with occasional max-pooling layers with stride 2 to halve the resolution of the grid. For technical reasons (memory efficiency during training), it seemed beneficial to start using Inception modules only at higher layers while keeping the lower layers in traditional convolutional fashion. This is not strictly necessary, simply reflecting some infrastructural inefficiencies in our current implementation.

<!-- chunk {"id": "body-0020", "role": "body", "section": "Architectural Details", "weight": 1.0} -->

One of the main beneficial aspects of this architecture is that it allows for increasing the number of units at each stage significantly without an uncontrolled blow-up in computational complexity. The ubiquitous use of dimension reduction allows for shielding the large number of input filters of the last stage to the next layer, first reducing their dimension before convolving over them with a large patch size. Another practically useful aspect of this design is that it aligns with the intuition that visual information should be processed at various scales and then aggregated so that the next stage can abstract features from different scales simultaneously.

<!-- chunk {"id": "body-0021", "role": "body", "section": "Architectural Details", "weight": 1.0} -->

The improved use of computational resources allows for increasing both the width of each stage as well as the number of stages without getting into computational difficulties. Another way to utilize the inception architecture is to create slightly inferior, but computationally cheaper versions of it. We have found that all the included the knobs and levers allow for a controlled balancing of computational resources that can result in networks that are $2 - 3 \times$ faster than similarly performing networks with non-Inception architecture, however this requires careful manual design at this point.

<!-- chunk {"id": "body-0022", "role": "body", "section": "GoogLeNet", "weight": 1.0} -->

We chose GoogLeNet as our team-name in the competition. This name is an homage to Yann LeCun's pioneering LeNet 5 network. We also use GoogLeNet to refer to the particular incarnation of the Inception architecture used in our submission for the competition. We have also used a deeper and wider Inception network, the quality of which was slightly inferior, but adding it to the ensemble seemed to improve the results marginally. We omit the details of that network, since our experiments have shown that the influence of the exact architectural parameters is relatively minor. Here, the most successful particular instance (named GoogLeNet) is described in Table 1 for demonstrational purposes. The exact same topology (trained with different sampling methods) was used for 6 out of the 7 models in our ensemble. patch size/ stride

<!-- chunk {"id": "body-0023", "role": "body", "section": "× 5", "weight": 1.0} -->

Given the relatively large depth of the network, the ability to propagate gradients back through all the layers in an effective manner was a concern. One interesting insight is that the strong performance of relatively shallower networks on this task suggests that the features produced by the layers in the middle of the network should be very discriminative. By adding auxiliary classifiers connected to these intermediate layers, we would expect to encourage discrimination in the lower stages in the classifier, increase the gradient signal that gets propagated back, and provide additional regularization. These classifiers take the form of smaller convolutional networks put on top of the output of the Inception (4a) and (4d) modules. During training, their loss gets added to the total loss of the network with a discount weight (the losses of the auxiliary classifiers were weighted by 0.3). At inference time, these auxiliary networks are discarded.

<!-- chunk {"id": "body-0024", "role": "body", "section": "× 5", "weight": 1.0} -->

The exact structure of the extra network on the side, including the auxiliary classifier, is as follows: An average pooling layer with $5 \times 5$ filter size and stride $3$, resulting in an $4 \times 4 \times 512$ output for the (4a), and $4 \times 4 \times 528$ for the (4d) stage.

<!-- chunk {"id": "body-0025", "role": "body", "section": "× 5", "weight": 1.0} -->

A $1 \times 1$ convolution with 128 filters for dimension reduction and rectified linear activation.

<!-- chunk {"id": "body-0026", "role": "body", "section": "× 5", "weight": 1.0} -->

A fully connected layer with 1024 units and rectified linear activation.

<!-- chunk {"id": "body-0027", "role": "body", "section": "× 5", "weight": 1.0} -->

A dropout layer with 70% ratio of dropped outputs.

<!-- chunk {"id": "body-0028", "role": "body", "section": "× 5", "weight": 1.0} -->

A linear layer with softmax loss as the classifier (predicting the same 1000 classes as the main classifier, but removed at inference time).

<!-- chunk {"id": "body-0029", "role": "body", "section": "× 5", "weight": 1.0} -->

A schematic view of the resulting network is depicted in Figure 3.

<!-- chunk {"id": "body-0030", "role": "body", "section": "Training Methodology", "weight": 1.0} -->

Our networks were trained using the DistBelief distributed machine learning system using modest amount of model and data-parallelism. Although we used CPU based implementation only, a rough estimate suggests that the GoogLeNet network could be trained to convergence using few high-end GPUs within a week, the main limitation being the memory usage. Our training used asynchronous stochastic gradient descent with 0.9 momentum, fixed learning rate schedule (decreasing the learning rate by 4% every 8 epochs). Polyak averaging was used to create the final model used at inference time.

<!-- chunk {"id": "body-0031", "role": "body", "section": "Training Methodology", "weight": 1.0} -->

Our image sampling methods have changed substantially over the months leading to the competition, and already converged models were trained on with other options, sometimes in conjunction with changed hyperparameters, like dropout and learning rate, so it is hard to give a definitive guidance to the most effective single way to train these networks. To complicate matters further, some of the models were mainly trained on smaller relative crops, others on larger ones, inspired. Still, one prescription that was verified to work very well after the competition includes sampling of various sized patches of the image whose size is distributed evenly between 8% and 100% of the image area and whose aspect ratio is chosen randomly between $3/4$ and $4/3$. Also, we found that the photometric distortions by Andrew Howard were useful to combat overfitting to some extent. In addition, we started to use random interpolation methods (bilinear, area, nearest neighbor and cubic, with equal probability) for resizing relatively late and in conjunction with other hyperparameter changes, so we could not tell definitely whether the final results were affected positively by their use.

<!-- chunk {"id": "body-0032", "role": "body", "section": "ILSVRC 2014 Classification Challenge Setup and Results", "weight": 1.0} -->

The ILSVRC 2014 classification challenge involves the task of classifying the image into one of 1000 leaf-node categories in the Imagenet hierarchy. There are about 1.2 million images for training, 50,000 for validation and 100,000 images for testing. Each image is associated with one ground truth category, and performance is measured based on the highest scoring classifier predictions. Two numbers are usually reported: the top-1 accuracy rate, which compares the ground truth against the first predicted class, and the top-5 error rate, which compares the ground truth against the first 5 predicted classes: an image is deemed correctly classified if the ground truth is among the top-5, regardless of its rank in them. The challenge uses the top-5 error rate for ranking purposes.

<!-- chunk {"id": "body-0033", "role": "body", "section": "ILSVRC 2014 Classification Challenge Setup and Results", "weight": 1.0} -->

We participated in the challenge with no external data used for training. In addition to the training techniques aforementioned in this paper, we adopted a set of techniques during testing to obtain a higher performance, which we elaborate below.

<!-- chunk {"id": "body-0034", "role": "body", "section": "ILSVRC 2014 Classification Challenge Setup and Results", "weight": 1.0} -->

We independently trained 7 versions of the same GoogLeNet model (including one wider version), and performed ensemble prediction with them. These models were trained with the same initialization (even with the same initial weights, mainly because of an oversight) and learning rate policies, and they only differ in sampling methodologies and the random order in which they see input images.

<!-- chunk {"id": "body-0035", "role": "body", "section": "ILSVRC 2014 Classification Challenge Setup and Results", "weight": 1.0} -->

During testing, we adopted a more aggressive cropping approach than that of Krizhevsky et al.. Specifically, we resize the image to 4 scales where the shorter dimension (height or width) is 256, 288, 320 and 352 respectively, take the left, center and right square of these resized images (in the case of portrait images, we take the top, center and bottom squares). For each square, we then take the 4 corners and the center $224 \times 224$ crop as well as the square resized to $224 \times 224$, and their mirrored versions. This results in ${4 \times 3 \times 6 \times 2} = 144$ crops per image. A similar approach was used by Andrew Howard in the previous year's entry, which we empirically verified to perform slightly worse than the proposed scheme. We note that such aggressive cropping may not be necessary in real applications, as the benefit of more crops becomes marginal after a reasonable number of crops are present (as we will show later on).

<!-- chunk {"id": "body-0036", "role": "body", "section": "ILSVRC 2014 Classification Challenge Setup and Results", "weight": 1.0} -->

The softmax probabilities are averaged over multiple crops and over all the individual classifiers to obtain the final prediction. In our experiments we analyzed alternative approaches on the validation data, such as max pooling over crops and averaging over classifiers, but they lead to inferior performance than the simple averaging.

<!-- chunk {"id": "body-0037", "role": "body", "section": "ILSVRC 2014 Classification Challenge Setup and Results", "weight": 1.0} -->

In the remainder of this paper, we analyze the multiple factors that contribute to the overall performance of the final submission.

<!-- chunk {"id": "body-0038", "role": "body", "section": "ILSVRC 2014 Classification Challenge Setup and Results", "weight": 1.0} -->

Uses external data Table 2: Classification performance Our final submission in the challenge obtains a top-5 error of 6.67% on both the validation and testing data, ranking the first among other participants. This is a 56.5% relative reduction compared to the SuperVision approach in 2012, and about 40% relative reduction compared to the previous year's best approach (Clarifai), both of which used external data for training the classifiers. The following table shows the statistics of some of the top-performing approaches.

<!-- chunk {"id": "body-0039", "role": "body", "section": "ILSVRC 2014 Detection Challenge Setup and Results", "weight": 1.0} -->

The ILSVRC detection task is to produce bounding boxes around objects in images among 200 possible classes. Detected objects count as correct if they match the class of the groundtruth and their bounding boxes overlap by at least 50% (using the Jaccard index). Extraneous detections count as false positives and are penalized. Contrary to the classification task, each image may contain many objects or none, and their scale may vary from large to tiny. Results are reported using the mean average precision (mAP).

<!-- chunk {"id": "body-0040", "role": "body", "section": "ILSVRC 2014 Detection Challenge Setup and Results", "weight": 1.0} -->

The approach taken by GoogLeNet for detection is similar to the R-CNN, but is augmented with the Inception model as the region classifier. Additionally, the region proposal step is improved by combining the Selective Search approach with multi-box predictions for higher object bounding box recall. In order to cut down the number of false positives, the superpixel size was increased by $2 \times$. This halves the proposals coming from the selective search algorithm. We added back 200 region proposals coming from multi-box resulting, in total, in about 60% of the proposals used, while increasing the coverage from 92% to 93%. The overall effect of cutting the number of proposals with increased coverage is a 1% improvement of the mean average precision for the single model case. Finally, we use an ensemble of 6 ConvNets when classifying each region which improves results from 40% to 43.9% accuracy. Note that contrary to R-CNN, we did not use bounding box regression due to lack of time.

<!-- chunk {"id": "body-0041", "role": "body", "section": "ILSVRC 2014 Detection Challenge Setup and Results", "weight": 1.0} -->

Bounding box regression Table 5: Single model performance for detection In Table 5, we compare results using a single model only. The top performing model is by Deep Insight and surprisingly only improves by 0.3 points with an ensemble of 3 models while the GoogLeNet obtains significantly stronger results with the ensemble.

<!-- chunk {"id": "body-0042", "role": "body", "section": "Conclusions", "weight": 1.0} -->

Our results seem to yield a solid evidence that approximating the expected optimal sparse structure by readily available dense building blocks is a viable method for improving neural networks for computer vision. The main advantage of this method is a significant quality gain at a modest increase of computational requirements compared to shallower and less wide networks. Also note that our detection work was competitive despite of neither utilizing context nor performing bounding box regression and this fact provides further evidence of the strength of the Inception architecture. Although it is expected that similar quality of result can be achieved by much more expensive networks of similar depth and width, our approach yields solid evidence that moving to sparser architectures is feasible and useful idea in general. This suggest promising future work towards creating sparser and more refined structures in automated ways on the basis of.
