## Introduction

Figure 1: Mean rank of Rocket versus state-of-the-art classifiers on the 85 ‘bake off’ datasets.

Most methods for time series classification that attain state-of-the-art accuracy have high computational complexity, requiring significant training time even for smaller datasets, and simply do not scale to large datasets. This has motivated the development of more scalable methods such as Proximity Forest, TS-CHIEF, and InceptionTime.

We show that state-of-the-art classification accuracy can be achieved using a fraction of the time required by even these recent, more scalable methods, by transforming time series using random convolutional kernels, and using the transformed features to train a linear classifier. We call this method Rocket (for RandOm Convolutional KErnel Transform).

Existing methods for time series classification typically focus on a single representation such as shape, frequency, or variance. Convolutional kernels constitute a single mechanism which can capture many of the features which have each previously required their own specialized techniques, and have been shown to be effective in convolutional neural networks for time series classification such as ResNet, and InceptionTime.

In contrast to learned convolutional kernels as used in typical convolutional neural networks, we show that it is effective to generate a large number of random convolutional kernels which, in combination, capture features relevant for time series classification (even though, in isolation, a single random convolutional kernel may only very approximately capture a relevant feature in a given time series).

Rocket achieves state-of-the-art classification accuracy on the datasets in the UCR archive, but requires only a fraction of the training time of existing methods. Figure 1 shows the mean rank of Rocket versus several state-of-the-art methods for time series classification on the 85 'bake off' datasets from the UCR archive. Restricted to a single CPU core, the total training time for Rocket is:

6 minutes for the 'bake off' dataset with the largest training set (ElectricDevices, with 8,926 training examples), compared to 1 hour 35 minutes for Proximity Forest, 2 hours 24 minutes for TS-CHIEF, and 7 hours 46 minutes for InceptionTime (trained on GPUs); and

4 minutes and 52 seconds for the 'bake off' dataset with the longest time series (HandOutlines, with time series of length 2,709), compared to 8 hours 10 minutes for InceptionTime (trained on GPUs), almost 3 days for Proximity Forest, and more than 4 days for TS-CHIEF.

The total compute time (training and test) for Rocket on all 85 'bake off' datasets is 1 hour 50 minutes, compared to more than 6 days for InceptionTime (trained and tested using GPUs), and more than 11 days for each of Proximity Forest and TS-CHIEF. (Timings for Rocket are averages over 10 runs, performed on a cluster using a mixture of Intel Xeon E5-2680 v3 and Intel Xeon Gold 6150 processors, restricted to a single CPU core per dataset per run.)

Rocket is also more scalable for large datasets, with training complexity linear in both time series length and the number of training examples. Rocket can learn from 1 million time series in 1 hour 15 minutes, to a similar accuracy as Proximity Forest, which requires more than 16 hours to train on the same quantity of data. A restricted variant of Rocket can learn from the same 1 million time series in less than 1 minute, or approximately 100 times faster again, albeit to a slightly lower accuracy. Rocket is naturally parallel, and can be made even faster by using multiple CPU cores (our implementation automatically parallelises the transform across multiple CPU cores where available) or GPUs.

The rest of this paper is structured as follows. In section 2, we review relevant related work. In section 3, we explain Rocket in detail. In section 4, we present our experimental results, including a comparison of the accuracy of Rocket against existing state-of-the-art classifiers on the datasets in the UCR archive, a scalability study, and a sensitivity analysis.

## Related Work

### State-of-the-Art Methods

The task of time series classification can be thought of as involving learning or detecting signals or patterns within time series associated with relevant classes. '\[D\]ifferent problems require different representations', and classes may be distinguished by multiple types of patterns: 'discriminatory features in multiple domains'.

Different methods for time series classification represent different approaches for extracting useful features from time series. Existing approaches typically focus on a single type of feature, such as frequency or variance of the signal, or the presence of discriminative subseries (shapelets). Bagnall et al. identified COTE (since superseded by HIVE-COTE), Shapelet Transform, and BOSS as the three most accurate classifiers on the UCR archive.

BOSS is one of several dictionary-based methods which use a representation based on the frequency of occurrence of patterns in time series. BOSS has a training complexity quadratic in both the number of training examples and time series length, $O{({n^{2} \cdot l^{2}})}$. BOSS-VS is a more scalable variant of BOSS, but is less accurate. Another related method, WEASEL, is more accurate than BOSS, but with a similar training complexity and high memory complexity.

Shapelet Transform is one of several methods based on finding discriminative subseries, so-called 'shapelets'. Shapelet Transform has a training complexity quadratic in the number of training examples, and quartic in time series length, $O{({n^{2} \cdot l^{4}})}$. There are other, more scalable, shapelet methods, but these are less accurate.

HIVE-COTE is a large ensemble of other classifiers, including BOSS and Shapelet Transform, as well as classifiers based on elastic distance measures and frequency representations. Since Lines et al., HIVE-COTE has been considered the most accurate method for time series classification. The training complexity of HIVE-COTE is bound by the complexity of Shapelet Transform, $O{({n^{2} \cdot l^{4}})}$, but its other components also have high computational complexity, such as the Elastic Ensemble with $O{({n^{2} \cdot l^{2}})}$.

### More Scalable Methods

The high computational complexity of existing state-of-the-art methods for time series classification makes these methods slow, even for smaller datasets, and intractable for large datasets. This has motivated the development of more scalable methods, including Proximity Forest, TS-CHIEF, and InceptionTime.

Proximity Forest is an ensemble of decision trees, using elastic distance measures as splitting criteria, with a training complexity quasilinear in the number of training examples, but quadratic in time series length.

TS-CHIEF builds on Proximity Forest, incorporating dictionary-based and interval-based splitting criteria. Like Proximity Forest, TS-CHIEF has a training complexity quasilinear in the number of training examples, but quadratic in time series length.

Several methods for time series classification using convolutional neural networks have been proposed. More recently, InceptionTime, an ensemble of five deep convolutional neural networks based on the Inception architecture, has been demonstrated to be competitive with HIVE-COTE on the UCR archive.

Convolutional neural networks are typically trained using stochastic gradient descent or closely related algorithms such as, for example, Adam. The training complexity of stochastic gradient descent is essentially linear with respect to the number of training examples, and training can be parallelised using GPUs.

### Convolutional Neural Networks and Convolutional Kernels

Ismail Fawaz et al. observe that the success of convolutional neural networks for image classification suggests that they should also be effective for time series classification, given that time series have essentially the same topology as images, with one less dimension.

Convolutional neural networks represent a different approach to time series classification than many other methods. Rather than approaching the problem with a preconceived representation, convolutional neural networks use convolutional kernels to detect patterns in the input. In learning the weights of the kernels, a convolutional neural network learns the features in time series associated with different classes.

A kernel is convolved with an input time series through a sliding dot product operation, to produce a feature map which is, in turn, used as the basis for classification. The basic parameters of a kernel are its size (length), weights and bias, dilation, and padding. A kernel has the same structure as the input, but is typically much smaller. For time series, a kernel is a vector of weights, with a bias term which is added to the result of the convolution operation between an input time series and the weights of the given kernel. Dilation 'spreads' a kernel over the input such that with a dilation of two, for example, the weights in a kernel are convolved with every second element of an input time series. Padding involves appending values (typically zero) to the start and end of input time series, typically such that the 'middle' weight of a given kernel aligns with the first element of an input time series at the start of the convolution operation.

Convolutional kernels can capture many of the types of features used in other methods. Kernels can capture basic patterns or shapes in time series, similar to shapelets: the convolution operation will produce large output values where the kernel matches the input. Further, dilation allows kernels to capture the same pattern at different scales. Multiple kernels in combination can capture complex patterns.

The feature maps produced in applying a kernel to a time series reflect the extent to which the pattern represented by the kernel is present in the time series. In a sense, this is not unlike dictionary methods, which are based on the frequency of occurrence of patterns in time series.

The kernels learned in convolutional neural networks often include filters for frequency. Saxe et al. demonstrate that even random kernels are frequency selective. Frequency information is also captured through dilation: larger dilations correspond to lower frequencies, smaller dilations to higher frequencies.

Kernels can detect patterns in time series despite warping. Pooling mechanisms make kernels invariant to the position of patterns in time series. Dilation allows kernels with similar weights to capture patterns at different scales, i.e., despite rescaling. Multiple kernels with different dilations can, in combination, capture discriminative patterns despite complex warping.

The success of convolutional neural networks for time series classification, such as ResNet and InceptionTime, demonstrates the effectiveness of convolutional kernels as the basis for time series classification.

### Random Convolutional Kernels

The weights of convolutional kernels are typically learned. However, it is well established that random convolutional kernels can be effective.

Ismail Fawaz et al. observe that individual convolutional neural networks exhibit high variance in classification accuracy on the UCR archive, motivating the use of ensembles of such architectures with a large number and variety of kernels. It may be that learning 'good' kernels is difficult on small datasets. Random convolutional kernels may have an advantage in this context.

The idea of using convolutional kernels as a transform, and using the transformed features as the input to another classifier is well established. Franceschi et al. present a method for unsupervised learning of convolutional kernels for a feature transform for time series input, based on a multilayer convolutional architecture with dilation increasing exponentially in each successive layer. The method is demonstrated using the output features as the input for a support vector machine.

Random convolutional kernels have been used as the basis of feature transformations. In Saxe et al., random convolutional layers are used as the basis of a feature transform (for images), used as the input for a support vector machine.

Here, there is a link between using random convolutional kernels as a transform for time series and work in relation to random transforms for kernel methods (as in support vector machines, not to be confused with convolutional kernels). Rahimi and Recht proposed a random transform for approximating kernels for kernel methods. Morrow et al. propose a method for approximating a string kernel for DNA sequences, based on Rahimi and Recht, which involves transforming input sequences using random convolutional kernels, and using the resulting features to train a linear classifier. Morrow et al. describe their method as 'a 1 layer random convolutional neural network'. Also following Rahimi and Recht, Jimenez and Raj propose a similar method for approximating a cross-correlation kernel for measuring similarity between time series, involving convolving input time series with random time series of the same length to produce what they call 'random convolutional features', which can be used to train a linear classifier. Jimenez and Raj evaluate their method on a selection of binary classification datasets from the UCR archive. (In both cases, there are some differences with the convolution operation as used in typical convolutional neural networks.) Farahmand et al. propose a feature transformation based on convolving input time series with random autoregressive filters.

A number of things distinguish Rocket from convolutional layers as used in typical convolutional neural networks, and from other methods using convolutional kernels (including random convolutional kernels) in relation to time series, set out in detail in section 3. We show that leveraging all aspects of kernel architecture---crucially, with a variety of random length, dilation, and padding (as well as weights and bias), and drawing an effective set of features from the output of the convolutions---provides for state-of-the-art accuracy with a fraction of the computational expense of existing state-of-the-art methods.

## Method

Rocket transforms time series using a large number of random convolutional kernels, i.e., kernels with random length, weights, bias, dilation, and padding. The transformed features are used to train a linear classifier. The combination of Rocket and logistic regression forms, in effect, a single-layer convolutional neural network with random kernel weights, where the transformed features form the input for a trained softmax layer. However, in practice, for all but the largest datasets, we use a ridge regression classifier, which has the advantage of fast cross-validation for the regularization hyperparameter (and no other hyperparameters). Nonetheless, as logistic regression trained using stochastic gradient descent is more scalable for very large datasets, we use logistic regression when the number of training examples is substantially greater than the number of features.

Four things distinguish Rocket from convolutional layers as used in typical convolutional neural networks, and from previous work using convolutional kernels (including random kernels) with time series:

Rocket uses a very large number of kernels. As there is only a single 'layer' of kernels, and as the kernel weights are not learned, the computational cost of computing the convolutions is low, and it is possible to use a very large number of kernels with relatively little computational expense.

Rocket uses a massive variety of kernels. In contrast to typical convolutional networks, where it is common for groups of kernels to share the same size, dilation, and padding, for Rocket each kernel has random length, dilation, and padding, as well as random weights and bias.

In particular, Rocket makes key use of kernel dilation. In contrast to the typical use of dilation in convolutional neural networks, where dilation increases exponentially with depth, we sample dilation randomly for each kernel, producing a huge variety of kernel dilation, capturing patterns at different frequencies and scales, which is critical to the performance of the method (see section 4.3.4, below).

As well as using the maximum value of the resulting feature maps (broadly speaking, similar to global max pooling), Rocket uses an additional and, to our knowledge, novel feature: the proportion of positive values (or ppv). This enables a classifier to weight the prevalence of a given pattern within a time series. This is the single element of the Rocket architecture that is most critical to its outstanding accuracy (see section 4.3.6).

In effect, the only hyperparameter for Rocket is the number of kernels, $k$. In setting $k$, there is a tradeoff between classification accuracy and computation time. Generally speaking, a larger value of $k$ results in higher classification accuracy (see section 4.3.1), but at the expense of proportionally longer computation. (The complexity of the transform is linear with respect to $k$.) However, even with a very large number of kernels (we use 10,000 by default), Rocket is extremely fast.

We implement Rocket in Python, using just-in-time compilation via Numba. For the experiments on the datasets in the UCR archive, we use a ridge regression classifier from scikit-learn. For the experiments studying scalability, we integrate Rocket with logistic regression and Adam, implemented using PyTorch. Our code will be made available at [https://github.com/angus924/rocket](https://github.com/angus924/rocket).

In developing Rocket, we have endeavoured to not overfit the entire UCR archive. At the same time, in order to develop the method, we required representative time series datasets. Accordingly, we chose to develop the method on a subset of 40 randomly-selected datasets from the 85 'bake off' datasets. We refer to these as the 'development' datasets. We provide a separate evaluation of the performance of Rocket on the 'development' datasets and the remaining 'holdout' datasets in Appendix B.

### Kernels

Rocket transforms time series using convolutional kernels, as found in typical convolutional neural networks. Essentially all aspects of the kernels are random: length, weights, bias, dilation, and padding. For each kernel, these values are set as follows (as determined by experimentation to produce the highest classification accuracy on the 'development' datasets):

Length. Length is selected randomly from $\{ 7,9,11\}$ with equal probability, making kernels considerably shorter than input time series in most cases.

Weights. The weights are sampled from a normal distribution, ${\forall w} \in {\mathbf{W}}$, $w \sim {\mathcal{N}{}}$, and are mean centered after being set, $\omega = {{\mathbf{W}} - \overline{\mathbf{W}}}$. As such, most weights are relatively small, but can take on larger magnitudes.

Bias. Bias is sampled from a uniform distribution, $b \sim {\mathcal{U}{({- 1},1)}}$. Only positive values in the feature maps are used (see section 3.2). Bias therefore has the effect that two otherwise similar kernels, but with different biases, can 'highlight' different aspects of the resulting feature maps by shifting the values in a feature map above or below zero by a fixed amount.

Dilation. Dilation is sampled on an exponential scale ${d = {\lfloor 2^{x}\rfloor}},{x \sim {\mathcal{U}{(0,A)}}}$, where $A = {log_{2}\frac{l_{\text{input}} - 1}{l_{\text{kernel}} - 1}}$, which ensures that the effective length of the kernel, including dilation, is up to the length of the input time series, $l_{\text{input}}$. Dilation allows otherwise similar kernels but with different dilations to match the same or similar patterns at different frequencies and scales.

Padding. When each kernel is generated, a decision is made (at random, with equal probability) whether or not padding will be used when applying the kernel. If padding is used, an amount of zero padding is appended to the start and end of each time series when applying the kernel, such that the 'middle' element of the kernel is centered on every point in the time series, i.e., ${({{({l_{\text{kernel}} - 1})} \times d})}/2$. Without padding, kernels are not centered at the first and last $\lfloor{l_{\text{kernel}}/2}\rfloor$ points of the time series, and 'focus' on patterns in the central regions of time series whereas with padding, kernels also match patterns at the start or end of time series (see also section 3.4.1).

Stride is always one. We do not apply a nonlinearity such as ReLU to the resulting feature maps (indeed both ppv and max are agnostic to ReLU). Note that the parameters for the weights and bias have been set based on the assumption that, as is standard practice, input time series have been normalized to have a mean of zero and a standard deviation of one.

As noted above, these parameters were determined to produce the highest classification accuracy on the 'development' datasets. However, as demonstrated in section 4.3, below, there are several alternative configurations which produce similar classification accuracy. Overall, this suggests that our method is likely to generalise well to new problems, and that the kernel parameters are relatively 'uninformative' in the Bayesian sense of the word.

### Transform

Each kernel is applied to each input time series, producing a feature map. The convolution operation involves a sliding dot product between a kernel and an input time series. The result of applying a kernel, $\omega$, with dilation, $d$, to a given time series, $X$, from position $i$ in $X$, is given by:

Rocket computes two aggregate features from each feature map, producing two real-valued numbers as features per kernel, and composing our transform:

the maximum value (broadly speaking, equivalent to global max pooling); and

the proportion of positive values (or ppv).

Pooling, including global average pooling, and global max pooling, is used in convolutional neural networks for dimensionality reduction and spatial (or temporal) invariance.

The other feature computed by Rocket on each feature map is ppv. The ppv directly captures the proportion of the input which matches a given pattern. We found that ppv produces meaningfully higher classification accuracy than other features, including the mean (broadly equivalent to global average pooling).

For $k$ kernels, Rocket produces $2k$ features per time series (i.e., ppv and max). For 10,000 kernels (the default), Rocket produces 20,000 features. For smaller datasets (in fact, for all the datasets in the UCR archive), the number of features is therefore possibly much larger than either the number of examples in the dataset or the number of elements in each time series.

Nevertheless, we find that the features produced by Rocket provide for high classification accuracy when used as the input for a linear classifier, even for datasets where the number of features dwarfs both the number of examples and the length of the time series.

### Classifier

The transformed features are used to train a linear classifier. Rocket can, in principle, be used with any classifier. We have found that Rocket is very effective when used in conjunction with linear classifiers (which have the capacity to make use of a small amount of information from each of a large number of features).

### Logistic regression

Rocket can be used with logistic regression and stochastic gradient descent. This is particularly suitable for very large datasets because it provides for fast training with a fixed memory cost (fixed by the size of each minibatch). The transform can be performed on each minibatch, or on larger tranches of the dataset which are then divided further into minibatches for training.

### Ridge regression

However, for all of the datasets in the UCR archive we use a ridge regression classifier. (A ridge regression model is trained for each class in a 'one versus rest' fashion, with $L_{2}$ regularization.)

Regularization is critically important where the number of features is significantly greater than the number of training examples, allowing for the optimization of linear models, and preventing pathological behaviour in iterative optimisation, e.g., for logistic regression. The ridge regression classifier can exploit generalised cross-validation to determine an appropriate regularization parameter quickly. We find that for smaller datasets, a ridge regression classifier is significantly faster in practice than logistic regression, while still achieving high classification accuracy.

### Complexity Analysis

The computational complexity of Rocket has two aspects: the complexity of the transform itself; and the complexity of the linear classifier trained using the transformed features.

### Transform

The transform itself is linear in relation to both: (a) the number of examples; and (b) the length of the time series in a given dataset. Formally, the computational complexity of the transform is $O{({k \cdot n \cdot l_{\text{input}}})}$, where $k$ is the number of kernels, $n$ is the number of examples, and $l_{input}$ is the length of the time series. The transform must be applied to both training and test sets.

The convolution operation can be implemented in more than one way, including as a matrix multiplication typical of implementations for convolutional neural networks, and using the fast Fourier transform. We implement Rocket simply, 'sliding' each kernel along each time series and computing the dot product at each location. This involves repeated elementwise multiplication and summation, the complexity of which is dictated by the length of the time series, and the length of the kernels (that is, the number of weights in the kernels). The length of the kernels for Rocket is limited to, at most, 11. Accordingly, kernel length is a constant factor for the purpose of this analysis.

Dilation increases the effective size of a kernel. Accordingly, where no padding is used, dilation reduces computational complexity. Without padding, the convolution is computed with the first element of the kernel starting at the first element of the time series, and ends once the last element of the kernel reaches the last element of the time series. In an extreme case, for the largest values of dilation, the kernel will 'fill' the entire time series, and the number of computations will be the number of weights in the kernel. However, padding is applied randomly with equal probability, so the reduction in complexity is a constant factor.

Where padding is used, dilation has no effect on complexity: the same number of computations are required regardless of dilation or the effective size of the kernel. Regardless of dilation, the kernel is centered on the first element of the time series, and 'slides' the same number of elements along the time series.

Accordingly, for $k$ kernels and $n$ time series, each of length $l_{\text{input}}$, the complexity of the transform is $O{({k \cdot n \cdot l_{\text{input}}})}$. For datasets with time series of different lengths, this could be taken to represent average complexity for an average length of $l_{\text{input}}$, or worst-case complexity for a maximum length of $l_{\text{input}}$.

### Classifier

### Logistic regression and stochastic gradient descent

The complexity of stochastic gradient descent is proportional to the number of parameters (dictated by the number of features and the number of classes), but is linear in relation to the number of training examples. Further, the rate of convergence is not determined by the number of training examples. For large datasets, convergence may occur in a single pass of the data, or even without using all of the training data.

### Ridge regression

In practice, the ridge regression classifier is significantly faster than logistic regression on smaller datasets because it can make use of so-called generalized cross-validation to determine appropriate regularization. The implementation used here employs eigen decomposition where there are more features than training examples, or singular value decomposition otherwise, with effective complexity of $O{({n^{2} \cdot f})}$ and $O{({n \cdot f^{2}})}$ respectively, where $n$ is the number of training examples and $f$ is the number of features.

This makes the ridge regression classifier less scalable for large datasets. This also requires the complete transform, and does not work incrementally. In practice, these limitations do not affect any of the datasets in the UCR archive. For larger datasets, where the importance of regularization decreases, and it is appropriate to perform the transform incrementally, the benefit of using the ridge regression classifier wanes, and training with stochastic gradient descent makes more sense.

## Experiments

We evaluate Rocket on the UCR archive (section 4.1), demonstrating that Rocket is competitive with current state-of-the-art methods, obtaining the best mean rank over the 85 'bake off' datasets.

We evaluate scalability in terms of both training set size and time series length (section 4.2), demonstrating that Rocket is orders of magnitude faster than current methods. We also evaluate the effect of different kernel parameters (section 4.3), showing that several alternative configurations of Rocket perform similarly well, which is a good indication of the power of the idea, rather than of its fine-tuning. Unless otherwise stated, all experiments use 10,000 kernels.

The experiments on the datasets in the UCR archive are performed using Rocket in conjunction with a ridge regression classifier, and the experiment in relation to training set size is performed using Rocket integrated with logistic regression. The experiments on the UCR archive were conducted on a cluster (but using a single CPU core per experiment, not parallelised for speed). The experiments in relation to scalability (both time series length and training set size) were performed locally using an Intel Core i5-5200U dual-core processor.

### UCR

### 'Bake Off' Datasets

We evaluate Rocket on the 85 'bake off' datasets from the UCR archive (on the original training/test split for each dataset). The results presented for Rocket are mean results over 10 runs (using a different set of random kernels for each run).

We compare Rocket to existing state-of-the-art methods for time series classification, namely, BOSS, Shapelet Transform, Proximity Forest, ResNet, and HIVE-COTE. We also compare Rocket with two more recent methods (with papers on arXiv), InceptionTime and TS-CHIEF, that have been demonstrated to be competitive with HIVE-COTE, while being more scalable. The results for BOSS, Shapelet Transform, and HIVE-COTE are taken from Bagnall et al..

For comparability with other published results, we compare Rocket to the other methods on all 85 'bake off' datasets. However, as noted above, Rocket was developed using a subset of 40 randomly-selected datasets, to make sure we didn't overfit the UCR archive. Separate rankings for the 40 'development' datasets, as well as the remaining 45 'holdout' datasets, are provided in Appendix B.

Figure 1 on page 1 gives the mean rank for each method included in the comparison. Classifiers for which the difference in pairwise classification accuracy is not statistically significant, as determined by a Wilcoxon signed-rank test with Holm correction (as a post hoc test to the Friedman test), are connected with a black line. The relative accuracy of Rocket and each of the other methods included in the comparison is shown in Figure 13, Appendix A.

Figure 1 on page 1 shows that Rocket is competitive with (in fact, ranks slightly ahead of) HIVE-COTE, TS-CHIEF, and InceptionTime, although the difference in accuracy between Rocket, HIVE-COTE, InceptionTime, and TS-CHIEF is not statistically significant. TS-CHIEF ranks ahead of Rocket on the 45 'holdout' datasets (Figure 14, Appendix B), but the difference is not significant.

### Additional 2018 Datasets

Figure 2: Relative accuracy of Rocket versus 1NN-DTW on the 43 additional 2018 datasets.

We have also evaluated Rocket on the 43 additional datasets in the UCR archive as of 2018, in order to: show that our method is able to handle datasets with varying lengths; and provide reference results for future research papers.

There are no published results for state-of-the-art methods on these datasets. Adapting these methods to work on variable-length time series is nontrivial, as the most appropriate method for handling variable lengths depends on whether the variable lengths represent subsampling or variable sampling frequencies, and is classifier dependent. Accordingly, we restrict our comparison to the available results for 1NN-DTW, where variable length time series have been padded with 'low amplitude random \[noise\]' to the same length as the longest time series. Figure 2 shows the relative accuracy of Rocket and 1NN-DTW on the 43 additional datasets. Rocket is more accurate on all but four datasets, and substantially more so on most.

Following Dau et al., we have normalized each time series and interpolated missing values. Variable-length time series have been rescaled or used 'as is' (with their original lengths) as determined by 10-fold cross-validation.

### Scalability

### Training Set Size

Figure 3: Accuracy (left) and training time (right) versus training set size.

Following Lucas et al., Shifaz et al., and Ismail Fawaz et al., we evaluate scalability in terms of training set size on increasingly larger subsets (up to approximately 1 million time series) of the Satellite Image Time Series dataset. The time series in this dataset represent a vegetation index, calculated from spectral data acquired by the Formosat-2 satellite, and the classes represent different land cover types. The aim in classifying these time series is to map different vegetation profiles to different types of crops and forested areas. Each time series has a length of 46.

For this purpose, we integrate Rocket with logistic regression. The transform is performed in tranches, which are further divided into minibatches for training. Each time series is normalised to have a zero mean and unit standard deviation.

We train the model for at least one epoch for each subset size. To prevent overfitting, we stop training (after the first epoch) if validation loss has failed to improve after 20 updates. In practice, while training may continue for 40 or 50 epochs for smaller subset sizes, training converges within a single pass for anything more than approximately 16,000 training examples. Validation loss is computed on a separate validation set (the same set of 2,048 examples for all subset sizes).

Optimization is performed using Adam. We perform a minimal search on the initial learning rate to ensure that training loss does not diverge. The learning rate is halved if training loss fails to improve after 100 updates (only relevant for larger subset sizes).

We have run Rocket in three guises: with 100, 1,000, and 10,000 kernels (the default). We compare Rocket against Proximity Forest and TS-CHIEF, which have already been demonstrated to be fundamentally more scalable than HIVE-COTE. (Results for larger quantities of data are not yet available for InceptionTime.)

Figure 3 shows classification accuracy and training time versus training set size for Rocket, Proximity Forest, and TS-CHIEF. As expected, Rocket scales linearly with respect to both the number of training examples, and the number of kernels (see section 3.4). With 1,000 or 10,000 kernels, Rocket achieves similar classification accuracy to Proximity Forest and TS-CHIEF. With 100 kernels, Rocket achieves lower classification accuracy, but takes less than a minute to learn from more than 1 million time series. Even with 10,000 kernels, Rocket is an order of magnitude faster than Proximity Forest. (Training time for smaller subset sizes for Rocket is dominated by the cost of the transform for the validation set, which is why training time is 'flat' for smaller subset sizes.)

### Time Series Length

Figure 4: Training time versus time series length.

Following Shifaz et al. and Ismail Fawaz et al., we evaluate scalability in terms of time series length using the InlineSkate dataset from the UCR archive. We use Rocket in the same configuration as for the other datasets in the UCR archive (that is, using the ridge regression classifier and 10,000 kernels). Results for HIVE-COTE and TS-CHIEF are taken from Shifaz et al..

Figure 4 shows training time versus time series length for Rocket, TS-CHIEF, HIVE-COTE, and InceptionTime. The difference in training time between Rocket and TS-CHIEF is substantial. Rocket takes approximately as long to train on time series of length 2,048 as TS-CHIEF takes for time series of length 32, and is approximately three orders of magnitude faster for the longest time series length.

Rocket is considerably faster than InceptionTime as well. However, fundamental scalability is likely to be similar, given that both InceptionTime and Rocket are based on convolutional architectures.

### Sensitivity Analysis

We explore the effect of different kernel parameters on classification accuracy. We compare the accuracy of the default configuration (i.e., using the parameters specified in section 3) against different choices for the number of kernels, length, weights and bias, dilation, padding, and output features. In each case, only the given parameter (e.g., length) is varied, keeping all other parameters fixed at their default values. The comparison is made on the 'development' datasets. The results are mean results over 10 runs (using a different set of random kernels per run).

In most cases, alternative configurations represent a relatively subtle change from the default configuration. Unsurprisingly, therefore, in many cases one or more alternative choices for the relevant parameter produces similar accuracy to the baseline configuration. In other words, Rocket is relatively robust to different choices for many parameters. However, it is clear that dilation and ppv, in particular, are two key aspects of the performance of the method.

### Number of Kernels

Figure 5: Mean ranks (left), and variance in accuracy (right), versus k.

We evaluate increasing numbers of kernels between 10 and 100,000. Figure 5 shows the effect of the number of kernels, $k$, on accuracy. Clearly, increasing the number of kernels improves accuracy. However, the actual difference in accuracy between, for example, $k = {5,000}$ and $k = {10,000}$, is relatively small, even if statistically significant. Indeed, $k = {5,000}$ produces higher accuracy on some datasets (Figure 16, Appendix C). Nevertheless, $k = {10,000}$ is noticeably ahead in terms of win/draw/loss (29/3/8). The differences between $k = {10,000}$, $k = {50,000}$, and $k = {100,000}$ are not statistically significant.

Even though Rocket is nondeterministic, the variability in accuracy is reasonably low for large numbers of kernels. Unsurprisingly, standard deviation diminishes as $k$ increases. The median standard deviation across the 40 'development' datasets is 0.0038 for $k = {10,000}$, and 0.0021 for $k = {100,000}$.

### Kernel Length

Figure 6: Mean ranks for different choices in terms of kernel length.

We vary kernel length, comparing the baseline (selecting length randomly from $\{ 7,9,11\}$) to:

fixed lengths of 3, 5, 7, 9, 11, 13, and 15; and

Figure 6 shows the effect of these choices on accuracy. Fixed lengths of 7, 9, and 11, as well as selecting length randomly from $\{ 5,7,9\}$ and $\{ 9,11,13\}$ result in similar accuracy to the default configuration, and the differences are not statistically significant (see also Figure 17, Appendix C). Shorter kernels are undesirable, being more strongly correlated with each other for a large number of kernels.

### Weights (Including Centering) and Bias

### Weights

Figure 7: Mean ranks for different choices in terms of the sampling distribution for the weights.

We vary the distribution from which the weights are sampled, comparing the baseline (sampling from a normal distribution) to:

sampling from a uniform distribution, ${\forall w} \in {\mathbf{W}}$, $w \sim {\mathcal{U}{({- 1},1)}}$; and

sampling integer weights uniformly from $\{{- 1},0,1\}$.

Figure 7 and Bias ‣ 4.3 Sensitivity Analysis ‣ 4 Experiments ‣ ROCKET: Exceptionally fast and accurate time series classification using random convolutional kernels") shows the effect of these choices on accuracy. While sampling from a normal distribution produces higher accuracy, the actual difference in accuracy is small and not statistically significant (see also Figure 18, Appendix C). While it may seem surprising that weights sampled from only three integer values are so effective, note that kernels are still mean centered by default and have random bias, and there is still substantial variety in terms of length and dilation.

### Centering

Figure 8: Mean ranks for different choices in terms of centering.

We vary centering, comparing the baseline (always centering) against:

never centering the kernel weights; and

centering or not centering at random with equal probability.

Figure 8 and Bias ‣ 4.3 Sensitivity Analysis ‣ 4 Experiments ‣ ROCKET: Exceptionally fast and accurate time series classification using random convolutional kernels") shows the effect of these choices on accuracy. It is clear that centering produces higher accuracy, but the difference between always centering and centering at random is very small and not statistically significant. Always centering, however, is noticeably more accurate on some datasets (Figure 19, Appendix C).

### Bias

Figure 9: Mean ranks for different choices in terms of bias.

We vary bias, comparing the baseline (using a uniform distribution) against:

using zero bias; and

sampling bias from a normal distribution, $b \sim {\mathcal{N}{}}$.

Figure 9 and Bias ‣ 4.3 Sensitivity Analysis ‣ 4 Experiments ‣ ROCKET: Exceptionally fast and accurate time series classification using random convolutional kernels") shows the effect of these choices on accuracy. Using a bias term produces higher accuracy, but the difference between sampling bias from a uniform distribution or a normal distribution is relatively small and not statistically significant (see also Figure 20, Appendix C.)

### Dilation

Figure 10: Mean ranks for different choices in terms of dilation.

We vary dilation, comparing the baseline (sampling dilation on an exponential scale) against:

no dilation (i.e., a fixed dilation of one); and

sampling dilation uniformly, $d = {\lfloor x\rfloor}$, $x \sim {\mathcal{U}{(1,\frac{l_{\text{input}} - 1}{l_{\text{kernel}} - 1})}}$.

Figure 10 shows the effect of these choices in terms of accuracy. It is clear that dilation is key to performance. Dilation produces obviously higher accuracy than no dilation. Exponential dilation produces higher accuracy than uniform dilation on most datasets (significantly higher on some datasets), and the difference is statistically significant (see also Figure 21, Appendix C).

### Padding

Figure 11: Mean ranks for different choices in terms of padding.

We vary padding, comparing the baseline (applying padding at random) against:

always padding, such that the 'middle' element of a given kernel is centered on the first element of the time series, $p = {{({{({l_{\text{kernel}} - 1})} \times d})}/2}$;

sampling padding uniformly, $p \sim {\mathcal{U}{(0,{{({{({l_{\text{kernel}} - 1})} \times d})}/2})}}$; and

Figure 11 shows the effect of these choices on accuracy. Padding is superior to not padding, but none of the differences are statistically significant. Different choices produce very similar results (Figure 22, Appendix C).

### Features

Figure 12: Mean ranks (left), and relative accuracy (right), ppv and max.

We vary the output features, comparing the baseline, ppv and max, against using each in isolation. Figure 12 shows the effect of these choices on accuracy. It is clear that ppv is superior to max: ppv produces substantially higher classification accuracy for the majority of the 'development' datasets. In fact, ppv has the single biggest effect on accuracy of all the parameters. The combination of ppv and max is better again, although the difference between ppv and ppv plus max is small and not statistically significant (see also Figure 23, Appendix C).

## Conclusion

Convolutional kernels are a single, powerful instrument which can capture many of the features used by existing methods for time series classification. We show that, rather than learning kernel weights, a large number of random kernels---while in isolation only approximating relevant patterns---in combination are extremely effective for capturing discriminative patterns in time series.

Further, random kernels have very low computational requirements, making learning and classification extremely fast. Our proposed method utilising random convolutional kernels for the purposes of transforming and classifying time series, Rocket, achieves state-of-the-art accuracy with a fraction of the computational expense of existing methods. Rocket also scales to millions of time series.

Rocket makes key use of the proportion of positive values (or ppv) to summarise the output of feature maps, allowing a classifier to weight the prevalence of a pattern in a given time series. To our knowledge, ppv has not been used in this way before. We find that this is substantially more effective than a simple maximum as applied in a conventional max pooling operation. It is credible that ppv would also be effective for other data types such as images.

In future work, we propose to explore feature selection for Rocket, the application of Rocket to multivariate timeseries, the application of Rocket beyond time series data, and the use of aspects of Rocket with learned kernels.
