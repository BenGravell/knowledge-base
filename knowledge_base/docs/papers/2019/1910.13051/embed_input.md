ROCKET: Exceptionally Fast and Accurate Time Series Classification Using Random Convolutional Kernels

Topics include Neural networks, Convolutional networks, Classification, Time series classification, Time series, Computational complexity, Convolutional kernels, Linear classifiers, Classifiers, Datasets, Accuracy, ROCKET, Convolutional neural network.

Most methods for time series classification that attain state-of-the-art accuracy have high computational complexity, requiring significant training time even for smaller datasets, and are intractable for larger datasets. Additionally, many existing methods focus on a single type of feature such as shape or frequency. Building on the recent success of convolutional neural networks for time series classification, we show that simple linear classifiers using random convolutional kernels achieve state-of-the-art accuracy with a fraction of the computational expense of existing methods.

## Introduction

Most methods for time series classification that attain state-of-the-art accuracy have high computational complexity, requiring significant training time even for smaller datasets, and simply do not scale to large datasets. This has motivated the development of more scalable methods such as Proximity Forest, TS-CHIEF, and InceptionTime.

We show that state-of-the-art classification accuracy can be achieved using a fraction of the time required by even these recent, more scalable methods, by transforming time series using random convolutional kernels, and using the transformed features to train a linear classifier. We call this method Rocket (for RandOm Convolutional KErnel Transform).

Existing methods for time series classification typically focus on a single representation such as shape, frequency, or variance. Convolutional kernels constitute a single mechanism which can capture many of the features which have each previously required their own specialized techniques, and have been shown to be effective in convolutional neural networks for time series classification such as ResNet, and InceptionTime.

In contrast to learned convolutional kernels as used in typical convolutional neural networks, we show that it is effective to generate a large number of random convolutional kernels which, in combination, capture features relevant for time series classification (even though, in isolation, a single random convolutional kernel may only very approximately capture a relevant feature in a given time series).

## Conclusion

Convolutional kernels are a single, powerful instrument which can capture many of the features used by existing methods for time series classification. We show that, rather than learning kernel weights, a large number of random kernels---while in isolation only approximating relevant patterns---in combination are extremely effective for capturing discriminative patterns in time series.

Further, random kernels have very low computational requirements, making learning and classification extremely fast. Our proposed method utilising random convolutional kernels for the purposes of transforming and classifying time series, Rocket, achieves state-of-the-art accuracy with a fraction of the computational expense of existing methods. Rocket also scales to millions of time series.
