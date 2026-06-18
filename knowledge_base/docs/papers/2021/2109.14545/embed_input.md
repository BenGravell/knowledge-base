Activation Functions in Deep Learning: A Comprehensive Survey and Benchmark

Topics include Activation functions, Deep learning, Neural networks, Benchmarking, ReLU activations, Exponential linear units, Swish, Mish, Function taxonomy, Survey.

This survey combines a taxonomy of deep-learning activation functions with empirical comparisons across several architectures and data types. Its benchmark framing makes it a practical complement to purely historical catalogs, especially for comparing families such as sigmoid, tanh, ReLU, ELU, learned, Swish, and Mish variants.

Neural networks have shown tremendous growth in recent years to solve numerous problems. Various types of neural networks have been introduced to deal with different types of problems. However, the main goal of any neural network is to transform the non-linearly separable input data into more linearly separable abstract features using a hierarchy of layers. These layers are combinations of linear and nonlinear functions. The most popular and common non-linearity layers are activation functions (AFs), such as Logistic Sigmoid, Tanh, ReLU, ELU, Swish and Mish. In this paper, a comprehensive overview and survey is presented for AFs in neural networks for deep learning. Different classes of AFs such as Logistic Sigmoid and Tanh based, ReLU based, ELU based, and Learning based are covered. Several characteristics of AFs such as output range, monotonicity, and smoothness are also pointed out. A performance comparison is also performed among 18 state-of-the-art AFs with different networks on different types of data. The insights of AFs are presented to benefit the researchers for doing further research and practitioners to select among different choices.

## Introduction

In recent years, deep learning has shown a tremondous growth to solve the challenging problems such as object detection, semantic segmentation, person re-identification, image retrieval, anomaly detection, skin disease diagnosis, and many more. Various types of neural networks have been defined in deep learning to learn abstract features from data, such as Multilayer Perceptron (MLP), Convolutional Neural Networks (CNN), Recurrent Neural Networks (RNN), and Generative Adversarial Networks (GAN). The important aspects of neural networks include weight initialization, loss functions, different layers, overfitting, and optimization.

The activation functions (AFs) play a very crucial role in neural networks by learning the abstract features through non-linear transformations. Some common properties of the AFs are as follows: a) it should add the non-linear curvature in the optimization landscape to improve the training convergence of the network; b) it should not increase the computational complexity of the model extensively; c) it should not hamper the gradient flow during training; d) it should retain the distribution of data to facilitate the better training of the network.

This survey provides a detailed classification for a wide range of AFs. It also includes the AFs very comprehensively, including Logistic Sigmoid/Tanh, Rectified Unit, Exponential Unit, and Adaptive AFs.

This survey enriches the reader with the state-of-the-art AFs with analysis from various perspectives. It specifically covers the progress in AFs for deep learning.

This paper also presents the performance comparisons on 4 benchmark datasets of different modalities using 18 state-of-the-art AFs with different types of networks (Refer to Tables 8, 9 and 11).

## Conclusion and Recommendations

An extensive and up to date survey of activation functions is conducted in this paper. Different types of AFs are considered, including Logistic Sigmoid and Tanh based, ReLU based, ELU based, and Learning based. However, the main focus is given to the recent developments in AFs in view of the deep learning applications of neural networks. The overview of AFs presented in this paper focuses on the aspects including the detailed coverage of AFs, classification and performance comparison over image, text and speech data.

Following
