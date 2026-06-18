Very Deep Convolutional Networks for Large-Scale Image Recognition

Topics include Convolutional networks, Computer vision, Classification, Datasets, Accuracy.

In this work we investigate the effect of the convolutional network depth on its accuracy in the large-scale image recognition setting. Our main contribution is a thorough evaluation of networks of increasing depth using an architecture with very small (3x3) convolution filters, which shows that a significant improvement on the prior-art configurations can be achieved by pushing the depth to 16-19 weight layers. These findings were the basis of our ImageNet Challenge 2014 submission, where our team secured the first and the second places in the localisation and classification tracks respectively. We also show that our representations generalise well to other datasets, where they achieve state-of-the-art results. We have made our two best-performing ConvNet models publicly available to facilitate further research on the use of deep visual representations in computer vision.

## Introduction

Convolutional networks (ConvNets) have recently enjoyed a great success in large-scale image and video recognition which has become possible due to the large public image repositories, such as ImageNet, and high-performance computing systems, such as GPUs or large-scale distributed clusters. In particular, an important role in the advance of deep visual recognition architectures has been played by the ImageNet Large-Scale Visual Recognition Challenge (ILSVRC), which has served as a testbed for a few generations of large-scale image classification systems, from high-dimensional shallow feature encodings to deep ConvNets.

With ConvNets becoming more of a commodity in the computer vision field, a number of attempts have been made to improve the original architecture of Krizhevsky et al. in a bid to achieve better accuracy. For instance, the best-performing submissions to the ILSVRC-2013 utilised smaller receptive window size and smaller stride of the first convolutional layer. Another line of improvements dealt with training and testing the networks densely over the whole image and over multiple scales. In this paper, we address another important aspect of ConvNet architecture design -- its depth....

## Conclusion

In this work we evaluated very deep convolutional networks (up to 19 weight layers) for large-scale image classification. It was demonstrated that the representation depth is beneficial for the classification accuracy, and that state-of-the-art performance on the ImageNet challenge dataset can be achieved using a conventional ConvNet architecture with substantially increased depth. In the appendix, we also show that our models generalise well to a wide range of tasks and datasets, matching or outperforming more complex recognition pipelines built around less deep image representations....

While more sophisticated methods of speeding up ConvNet training have been recently proposed, which employ model and data parallelism for different layers of the net, we have found that our conceptually much simpler scheme already provides a speedup of $3.75$ times on an off-the-shelf 4-GPU system, as compared to using a single GPU. On a system equipped with four NVIDIA Titan Black GPUs, training a single net took 2--3 weeks depending on the architecture.
