Do Better ImageNet Classifiers Assess Perceptual Similarity Better?

Perceptual distances between images, as measured in the space of pre-trained deep features, have outperformed prior low-level, pixel-based metrics on assessing perceptual similarity. While the capabilities of older and less accurate models such as AlexNet and VGG to capture perceptual similarity are well known, modern and more accurate models are less studied. In this paper, we present a large-scale empirical study to assess how well ImageNet classifiers perform on perceptual similarity. First, we observe a inverse correlation between ImageNet accuracy and Perceptual Scores of modern networks such as ResNets, EfficientNets, and Vision Transformers: that is better classifiers achieve worse Perceptual Scores. Then, we examine the ImageNet accuracy/Perceptual Score relationship on varying the depth, width, number of training steps, weight decay, label smoothing, and dropout. Higher accuracy improves Perceptual Score up to a certain point, but we uncover a Pareto frontier between accuracies and Perceptual Score in the mid-to-high accuracy regime.

## Introduction

ImageNet is the cornerstone of modern supervised learning and has enabled significant progress in computer vision. Features learnt via training on ImageNet transfer well to a number of downstream tasks, making ImageNet pretraining a standard recipe.

In this paper, we are motivated by the following questions: Considering ImageNet classification has progressed significantly since then, can we obtain a better perceptual similarity metric by using a better classifier directly? Since modern neural network training involves a large number of hyperparameters, are there design choices that can improve a classifier's perceptual similarity? Are there latent factors that govern the relationship between ImageNet accuracy and perceptual similarity?

While modern classifiers outperform prior pixel-based metrics in PS, they under-perform moderate classifiers like AlexNet.

## Conclusion

In Fig. 1, we plot the accuracy and PS from all our above experiments. While their exact relationship is architecture and hyperparameter dependent, we uncover a global Pareto frontier between PS and accuracies, see Fig. 1. Up to a certain peak, better classifiers achieve PS and beyond this peak, better accuracy hurts PS.

In this paper, we explore the question if better classifiers can serve as better feature extractors for perceptual metrics. To answer this question, we conduct experiments across ResNets and ViTs across many different hyperparameters. Except for label smoothing and dropout, we see that PS exhibits an inverse-U relationship with accuracy across the hyperparameters we considered. We then probe a number of explanations for the inverse-U relationship involving skip connections, Global Similarity Functions, Distortion Sensitivity, Layer-wise Perceptual Scores, Spatial Frequency, Sensitivity, and ImageNet Class Granularity.
