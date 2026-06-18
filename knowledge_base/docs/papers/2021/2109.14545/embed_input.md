Activation Functions in Deep Learning: A Comprehensive Survey and Benchmark

Topics include Activation functions, Deep learning, Neural networks, Benchmarking, ReLU activations, Exponential linear units, Swish, Mish, Function taxonomy, Survey.

This survey combines a taxonomy of deep-learning activation functions with empirical comparisons across several architectures and data types. Its benchmark framing makes it a practical complement to purely historical catalogs, especially for comparing families such as sigmoid, tanh, ReLU, ELU, learned, Swish, and Mish variants.

Neural networks have shown tremendous growth in recent years to solve numerous problems. Various types of neural networks have been introduced to deal with different types of problems. However, the main goal of any neural network is to transform the non-linearly separable input data into more linearly separable abstract features using a hierarchy of layers. These layers are combinations of linear and nonlinear functions. The most popular and common non-linearity layers are activation functions (AFs), such as Logistic Sigmoid, Tanh, ReLU, ELU, Swish and Mish. In this paper, a comprehensive overview and survey is presented for AFs in neural networks for deep learning. Different classes of AFs such as Logistic Sigmoid and Tanh based, ReLU based, ELU based, and Learning based are covered. Several characteristics of AFs such as output range, monotonicity, and smoothness are also pointed out. A performance comparison is also performed among 18 state-of-the-art AFs with different networks on different types of data. The insights of AFs are presented to benefit the researchers for doing further research and practitioners to select among different choices....

## Introduction

In recent years, deep learning has shown a tremondous growth to solve the challenging problems such as object detection, semantic segmentation, person re-identification, image retrieval, anomaly detection, skin disease diagnosis, and many more. Various types of neural networks have been defined in deep learning to learn abstract features from data, such as Multilayer Perceptron (MLP), Convolutional Neural Networks (CNN), Recurrent Neural Networks (RNN), and Generative Adversarial Networks (GAN). The important aspects of neural networks include weight initialization, loss functions, different layers, overfitting, and optimization.

The activation functions (AFs) play a very crucial role in neural networks by learning the abstract features through non-linear transformations. Some common properties of the AFs are as follows: a) it should add the non-linear curvature in the optimization landscape to improve the training convergence of the network; b) it should not increase the computational complexity of the model extensively; c) it should not hamper the gradient flow during training; d) it should retain the distribution of data to facilitate the better training of the network....

The Tanh and SELU AFs are found better for language translation along with PReLU, LiSHT, SRS and PAU.

It is suggested to use the PReLU, GELU, Swish, Mish and PAU AFs for speech recognition.

Most of the aforementioned AFs are not adaptive and might not be able to adjust based on the dataset complexity. This problem is tackled using learning/adaptive AFs as summarized in Table 5. Some of the earlier mentioned AFs are also adaptive, such as PReLU, SReLU, PTELU, MTLU, PELU, MPELU, PREU, EELU, PDELU, SRS, etc.

in the output range of $\lbrack 0,\infty)$ where $a$ is a random number. At test time, the offset is set to zero. A data dependent Average Biased ReLU (AB-ReLU) is also investigated to tackle the negative values by a horizontal shifting based on the average of features. The ABReLU can be written as,

Parametric Deformable ELU (PDELU) - 2020
NIN and ResNet
and CIFAR100 classification
The PDELU performs better than the ReLU, ELU and FReLU.

This survey provides a detailed classification for a wide range of AFs. It also includes the AFs very comprehensively, including Logistic Sigmoid/Tanh, Rectified Unit, Exponential Unit, and Adaptive AFs.
