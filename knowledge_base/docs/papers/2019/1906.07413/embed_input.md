Learning Imbalanced Datasets with Label-Distribution-Aware Margin Loss

Deep learning algorithms can fare poorly when the training dataset suffers from heavy class-imbalance but the testing criterion requires good generalization on less frequent classes. We design two novel methods to improve performance in such scenarios. First, we propose a theoretically-principled label-distribution-aware margin (LDAM) loss motivated by minimizing a margin-based generalization bound. This loss replaces the standard cross-entropy objective during training and can be applied with prior strategies for training with class-imbalance such as re-weighting or re-sampling. Second, we propose a simple, yet effective, training schedule that defers re-weighting until after the initial stage, allowing the model to learn an initial representation while avoiding some of the complications associated with re-weighting or re-sampling. We test our methods on several benchmark vision tasks including the real-world imbalanced dataset iNaturalist 2018. Our experiments show that either of these methods alone can already improve over existing techniques and their combination achieves even better performance gains.

## Introduction

Modern real-world large-scale datasets often have long-tailed label distributions. On these datasets, deep neural networks have been found to perform poorly on less represented classes. This is particularly detrimental if the testing criterion places more emphasis on minority classes. For example, accuracy on a uniform label distribution or the minimum accuracy among all classes are examples of such criteria. These are common scenarios in many applications due to various practical concerns such as transferability to new domains, fairness, etc.

The two common approaches for learning long-tailed data are re-weighting the losses of the examples and re-sampling the examples in the SGD mini-batch (see and the references therein). They both devise a training loss that is in expectation closer to the test distribution, and therefore can achieve better trade-offs between the accuracies of the frequent classes and the minority classes. However, because we have fundamentally less information about the minority classes and the models deployed are often huge, over-fitting to the minority classes appears to be one of the challenges in improving these methods.

## Conclusion

We propose two methods for training on imbalanced datasets, label-distribution-aware margin loss (LDAM), and a deferred re-weighting (DRW) training schedule. Our methods achieve significantly improved performance on a variety of benchmark vision tasks. Furthermore, we provide a theoretically-principled justification of LDAM by showing that it optimizes a uniform-label generalization error bound. For DRW, we believe that deferring re-weighting lets the model avoid the drawbacks associated with re-weighting or re-sampling until after it learns a good initial representation (see some analysis in Figure 3 and Figure 6)....

### Label-Distribution-Aware Margin Loss

### Fine-grained generalization error bounds

We evaluate our proposed algorithm on artificially created versions of IMDB review, CIFAR-10, CIFAR-100 and Tiny ImageNet with controllable degrees of data imbalance, as well as a real-world large-scale imbalanced dataset, iNaturalist 2018. Our core algorithm is developed using PyTorch.

We propose to regularize the minority classes more strongly than the frequent classes so that we can improve the generalization error of minority classes without sacrificing the model's...
