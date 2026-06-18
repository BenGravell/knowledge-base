ROCKET: Exceptionally Fast and Accurate Time Series Classification Using Random Convolutional Kernels

Topics include Neural networks, Convolutional networks, Classification, Time series classification, Time series, Computational complexity, Convolutional kernels, Linear classifiers, Classifiers, Datasets, Accuracy, ROCKET, Convolutional neural network.

Most methods for time series classification that attain state-of-the-art accuracy have high computational complexity, requiring significant training time even for smaller datasets, and are intractable for larger datasets. Additionally, many existing methods focus on a single type of feature such as shape or frequency. Building on the recent success of convolutional neural networks for time series classification, we show that simple linear classifiers using random convolutional kernels achieve state-of-the-art accuracy with a fraction of the computational expense of existing methods.

## Introduction

Figure 1: Mean rank of Rocket versus state-of-the-art classifiers on the 85 ‘bake off’ datasets.

Most methods for time series classification that attain state-of-the-art accuracy have high computational complexity, requiring significant training time even for smaller datasets, and simply do not scale to large datasets. This has motivated the development of more scalable methods such as Proximity Forest, TS-CHIEF, and InceptionTime.

Rocket makes key use of the proportion of positive values (or ppv) to summarise the output of feature maps, allowing a classifier to weight the prevalence of a pattern in a given time series. To our knowledge, ppv has not been used in this way before. We find that this is substantially more effective than a simple maximum as applied in a conventional max pooling operation. It is credible that ppv would also be effective for other data types such as images.

In future work, we propose to explore feature selection for Rocket, the application of Rocket to multivariate timeseries, the application of Rocket beyond time series data, and the use of aspects of Rocket with learned kernels.

Accordingly, for $k$ kernels and $n$ time series, each of length $l_{\text{input}}$, the complexity of the transform is $O{({k \cdot n \cdot l_{\text{input}}})}$. For datasets with time series of different lengths, this could be taken to represent average complexity for an average length of $l_{\text{input}}$, or worst-case complexity for a maximum length of $l_{\text{input}}$.

Bias. Bias is sampled from a uniform distribution, $b \sim {\mathcal{U}{({- 1},1)}}$. Only positive values in the feature maps are used (see section 3.2). Bias therefore has the effect that two otherwise similar kernels, but with different biases, can 'highlight' different aspects of the resulting feature maps by shifting the values in a feature map above or below zero by a fixed amount.

For this purpose, we integrate Rocket with logistic regression. The transform is performed in tranches, which are further divided into minibatches for training. Each time series is normalised to have a zero mean and unit standard deviation.

We show that state-of-the-art classification accuracy can be achieved using a fraction of the time required by even these recent, more scalable methods, by transforming time series using random convolutional kernels, and using the...
