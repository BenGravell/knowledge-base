Very Deep Convolutional Networks for Large-Scale Image Recognition

Topics include Convolutional networks, Computer vision, Classification, Datasets, Accuracy.

In this work we investigate the effect of the convolutional network depth on its accuracy in the large-scale image recognition setting. Our main contribution is a thorough evaluation of networks of increasing depth using an architecture with very small (3x3) convolution filters, which shows that a significant improvement on the prior-art configurations can be achieved by pushing the depth to 16-19 weight layers. These findings were the basis of our ImageNet Challenge 2014 submission, where our team secured the first and the second places in the localisation and classification tracks respectively. We also show that our representations generalise well to other datasets, where they achieve state-of-the-art results. We have made our two best-performing ConvNet models publicly available to facilitate further research on the use of deep visual representations in computer vision.

## Introduction

Convolutional networks (ConvNets) have recently enjoyed a great success in large-scale image and video recognition which has become possible due to the large public image repositories, such as ImageNet, and high-performance computing systems, such as GPUs or large-scale distributed clusters. In particular, an important role in the advance of deep visual recognition architectures has been played by the ImageNet Large-Scale Visual Recognition Challenge (ILSVRC), which has served as a testbed for a few generations of large-scale image classification systems, from high-dimensional shallow feature encodings to deep ConvNets.

With ConvNets becoming more of a commodity in the computer vision field, a number of attempts have been made to improve the original architecture of Krizhevsky et al. in a bid to achieve better accuracy. For instance, the best-performing submissions to the ILSVRC-2013 utilised smaller receptive window size and smaller stride of the first convolutional layer. Another line of improvements dealt with training and testing the networks densely over the whole image and over multiple scales. In this paper, we address another important aspect of ConvNet architecture design -- its depth.

## Discussion

Our ConvNet configurations are quite different from the ones used in the top-performing entries of the ILSVRC-2012 and ILSVRC-2013 competitions. Rather than using relatively large receptive fields in the first conv. layers (e.g. $11 \times 11$ with stride $4$ , or $7 \times 7$ with stride $2$ in ), we use very small $3 \times 3$ receptive fields throughout the whole net, which are convolved with the input at every pixel (with stride $1$). It is easy to see that a stack of two $3 \times 3$ conv.

The incorporation of $1 \times 1$ conv. layers (configuration C, Table 1) is a way to increase the non-linearity of the decision function without affecting the receptive fields of the conv. layers. Even though in our case the $1 \times 1$ convolution is essentially a linear projection onto the space of the same dimensionality (the number of input and output channels is the same), an additional non-linearity is introduced by the rectification function. It should be noted that $1 \times 1$ conv. layers have recently been utilised in the "Network in Network" architecture of Lin et al..
