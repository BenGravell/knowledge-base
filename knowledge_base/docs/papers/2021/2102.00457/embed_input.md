<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

MultiRocket: Multiple Pooling Operators and Transformations for Fast and Effective Time Series Classification

Topics include Classification, Time series classification, Time series, Datasets, Benchmarks, Accuracy, MultiRocket, fast time series classification, TSC.

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

We propose MultiRocket, a fast time series classification (TSC) algorithm that achieves state-of-the-art performance with a tiny fraction of the time and without the complex ensembling structure of many state-of-the-art methods. MultiRocket improves on MiniRocket, one of the fastest TSC algorithms to date, by adding multiple pooling operators and transformations to improve the diversity of the features generated. In addition to processing the raw input series, MultiRocket also applies first order differences to transform the original series. Convolutions are applied to both representations, and four pooling operators are applied to the convolution outputs. When benchmarked using the University of California Riverside TSC benchmark datasets, MultiRocket is significantly more accurate than MiniRocket, and competitive with the best ranked current method in terms of accuracy, HIVE-COTE 2.0, while being orders of magnitude faster.

<!-- chunk {"id": "body-0003", "role": "body", "section": "Introduction", "weight": 1.5} -->

Many of the most accurate methods for time series classification (TSC), such as HIVE-COTE 2.0, achieve high classification accuracy at the expense of high computational complexity and limited scalability. Hence scalable TSC has become an important research topic in recent years. Rocket and MiniRocket are the fastest and most scalable among all the proposed scalable TSC methods that achieve state-of-the-art (SOTA) accuracy. They achieve SOTA accuracy with a fraction of the computational expense of any other method of similar accuracy. Despite their scalability, Rocket and MiniRocket are somewhat less accurate than the variants of HIVE-COTE, including the most recent HIVE-COTE 2.0, which is the current best ranked method with respect to accuracy on 112 datasets in the widely used benchmark UCR archive of time series classification datasets.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

MiniRocket is built on Rocket and is recommended over Rocket due to its scalability. We show that it is possible to significantly improve the accuracy of MiniRocket, with some additional computational expense, by transforming the time series prior to the convolution operations, and by expanding the set of pooling operations used to generate features. We call this method MultiRocket -- for MiniRocket with multiple pooling operators and transformations.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

Rocket and MiniRocket apply convolutional kernels to the raw input series. The resulting outputs are each summarized by the *Proportion of Positive Values* (PPV) summary statistic. The resulting values are provided as input features to a simple linear model. MiniRocket uses a fixed set of 84 kernels and generates multiple dilations and biases for each kernel, by default producing a total of 10,000 features for the convolution operations.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

MultiRocket is based on MiniRocket, using the same set of kernels as MiniRocket. There are two main differences. First, MultiRocket transforms a time series into its first order difference. Then both the original and the first order difference time series are convolved with the 84 MiniRocket kernels. A different set of dilations and biases is used for each representation because both representations have different lengths (first order difference is shorter by 1) and range of values (bias values are sampled from the convolution output). Second, in addition to PPV, MultiRocket adds 3 additional pooling operators to increase the diversity and discriminatory power of the extracted features. By default, MultiRocket produces approximately 50,000 (49,728 to be exact) features per time series (i.e., $6,{216 \times 2 \times 4}$). For simplicity, when discussing the number of features, we round the number to the nearest 10,000 throughout the paper. Finally the transformed features are used to train a linear classifier.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

Using first order differencing, expanding the set of pooling operators, and increasing the total number of features to 50,000, increases the diversity of the extracted features. This enhancement makes MultiRocket one of the most accurate TSC methods, on average on the datasets in the UCR time series archive, as illustrated in a critical difference diagram shown in Figure 1. Figure 1 shows that MultiRocket is significantly more accurate than MiniRocket (and most top SOTA methods -- see Figure 5 in our experiments section). It is also not significantly less accurate than the most accurate TSC method to-date HIVE-COTE 2.0.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Introduction", "weight": 1.5} -->

The use of first order difference transform and additional pooling operators in MultiRocket substantially increases the computational expense of the transform over MiniRocket. Figures 2(a) and 2(b) compare the total compute time (first order difference transform, convolution transforms, training and testing) for MultiRocket and MiniRocket, both with 10,000 and 50,000 features, over 109 datasets from the UCR archive. Note that the timings are averages over 30 resamples of each dataset, and run on a cluster using AMD EPYC 7702 CPUs with 32 threads. Figure 2(a) shows that the default MultiRocket with 50,000 features is up to an order of magnitude slower than the default MiniRocket, which has 10,000 features. However, the default MultiRocket takes only 20% longer to process the entire repository than MiniRocket with the same number of features, as illustrated in Figure 2(b).

<!-- chunk {"id": "body-0009", "role": "body", "section": "Introduction", "weight": 1.5} -->

Although the default MultiRocket (using 50k features) is approximately 10 times slower than the default MiniRocket (using 10k features), the total compute time for 109 UCR datasets of 5 minutes, using 32 threads, is still orders of magnitude faster than most SOTA TSC algorithms. The smaller variant of MultiRocket with 10,000 features (the same number as the default MiniRocket) is on average half as fast as MiniRocket while being significantly more accurate. The relative computational disadvantage of MultiRocket relative to MiniRocket with the same number of features decreases as the number of features increases as the relative impact of once off operations such as taking the derivatives of the series decline as a proportion of total time.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Introduction", "weight": 1.5} -->

The rest of the paper is organised as follows. In Section 2, we review the relevant existing work. In Section 3, we describe MultiRocket in detail. In Section 4, we present our experimental results and conclude our paper.

<!-- chunk {"id": "body-0011", "role": "body", "section": "State of the art", "weight": 1.0} -->

The goal of TSC is to learn discriminating patterns that can be used to group time series into predefined categories (classes). The accuracy of a TSC algorithm is a measure of its discriminating power. The current SOTA TSC algorithms with respect to accuracy include HIVE-COTE and its variants, TS-CHIEF, MiniRocket, Rocket and InceptionTime. With some exceptions (namely, Rocket and MiniRocket), most SOTA TSC methods are burdened with high computational complexity.

<!-- chunk {"id": "body-0012", "role": "body", "section": "State of the art", "weight": 1.0} -->

InceptionTime is the most accurate deep learning architecture for TSC. It is an ensemble of 5 Inception-based convolutional neural networks. Ensembling reduces the variance of the model. The resulting method is significantly more accurate compared with other deep learning based TSC methods such as the Fully Convolutional Network (FCN) and Residual Network (ResNet).

<!-- chunk {"id": "body-0013", "role": "body", "section": "State of the art", "weight": 1.0} -->

TS-CHIEF was first introduced as a scalable TSC algorithm with accuracy competitive with HIVE-COTE. It builds on Proximity Forest, an ensemble of decision trees using distance measures at each node as the splitting criterion. TS-CHIEF improves on Proximity Forest by adding interval and spectral based splitting criteria, allowing the ensemble to capture a wider range of representations.

<!-- chunk {"id": "body-0014", "role": "body", "section": "State of the art", "weight": 1.0} -->

HIVE-COTE is a meta-ensemble that consists of the most accurate ensemble classifiers from different time series representation domains. The original HIVE-COTE consists of Ensemble of Elastic Distances (EE), Shapelet Transform Classifier (STC), Bag of SFA Symbols (BOSS) Ensemble, Time Series Forest (TSF) and Random Interval Forest (RIF), each of them being the most accurate classifier in their respective domains. The authors showed that HIVE-COTE is significantly more accurate than each of its constituent members, and it has stood as a high benchmark for classification accuracy ever since.

<!-- chunk {"id": "body-0015", "role": "body", "section": "State of the art", "weight": 1.0} -->

Recently HIVE-COTE 2.0 was proposed and has been shown to have the best average rank on accuracy against a spread of the SOTA both in the univariate UCR and the multivariate UEA time series archives. HIVE-COTE 2.0 is a meta-ensemble of four main components, STC, Arsenal, Temporal Dictionary Ensemble (TDE), and Diverse Representation Canonical Interval Forest (DrCIF). HIVE-COTE 2.0 drops EE from the ensemble as EE is not scalable and does not contribute greatly towards the accuracy of HIVE-COTE. The only module retained from the original HIVE-COTE is STC with some additional modifications to make it scalable. STC in HIVE-COTE 2.0 randomly searches for shapelets within a given contract time and transforms a time series using the distance to each shapelet. It then employs a rotation forest as the classifier. Arsenal is an ensemble of small Rocket classifiers with 4,000 features each. This approach allows the ensemble to return a probability distribution over the classes when making predictions, allowing Rocket to be used within the HIVE-COTE framework. The dictionary-based classifier, BOSS was replaced with the more accurate TDE.

<!-- chunk {"id": "body-0016", "role": "body", "section": "State of the art", "weight": 1.0} -->

TDE combines aspects of various earlier dictionary methods and is significantly more accurate than any existing dictionary method.

<!-- chunk {"id": "body-0017", "role": "body", "section": "State of the art", "weight": 1.0} -->

HIVE-COTE 2.0 updates HIVE-COTE by replacing RISE and TSF with DrCIF. DrCIF is significantly more accurate than RISE, TSF and its predecessor CIF. RISE is an ensemble of various classifiers that derives spectral features (periodogram and auto-regressive terms) from intervals of a time series. TSF identifies key intervals within the time series, uses simple summary statistics to extract features from these intervals and then applies Random Forests to those features. DrCIF builds on both RISE and TSF by transforming the time series using the first order difference and periodogram. It expands the original set of features used in TSF, using the catch22 features. Diversity is achieved by randomly sampling different intervals and subsets of features for each representation in each tree. The use of diverse representations and additional features from the catch22 feature set within DrCIF results in a considerable improvement in accuracy. We build on these observations and explore the possibility of extending MiniRocket with expanded feature sets and diverse representations.

<!-- chunk {"id": "body-0018", "role": "body", "section": "State of the art", "weight": 1.0} -->

While producing high classification accuracy, most of these methods do not scale well. The total compute time (training and testing) on the 109 datasets from the UCR time series archive, using a single CPU thread, is around two days for DrCIF, three days for TDE, more than a week for Proximity Forest, and more than two weeks for HIVE-COTE 2.0. On the other hand, MiniRocket was reported to be able to complete training and testing on 109 datasets within 8 minutes. To be comparable to MultiRocket, we ran MiniRocket on the same hardware, single threaded, and completed the whole 109 datasets just under 4 minutes, while MultiRocket with the default 50,000 features takes 40 minutes, an order of magnitude slower (see Figure 7(a) in Appendix D). However, as shown in Figure 2(a), MultiRocket was able to complete all 109 datasets in around 5 minutes using 32 threads, while the default MiniRocket with 10,000 features took around 2 minutes. Regardless, MultiRocket is still significantly faster than all SOTA methods other than MiniRocket and highly competitive on accuracy.

<!-- chunk {"id": "body-0019", "role": "body", "section": "MiniRocket and Rocket", "weight": 1.0} -->

Rocket is a significantly more scalable TSC algorithm, matching the accuracy of most SOTA TSC methods, and taking just 2 hours to train and classify the same 109 UCR datasets using a single CPU core. Rocket transforms the input time series using 10,000 random convolutional kernels (random in terms of their length, weights, bias, dilation, and padding). It then uses PPV and Max pooling operators to compute two features from each convolution output, producing 20,000 features per time series. The transformed features are used to train a linear classifier. The use of dilation and PPV are the key aspects of Rocket in achieving SOTA accuracy.

<!-- chunk {"id": "body-0020", "role": "body", "section": "MiniRocket and Rocket", "weight": 1.0} -->

MiniRocket is a much faster variant of Rocket. It takes less than 10 minutes to train and classify the same 109 UCR datasets using a single CPU core, while maintaining the same accuracy as Rocket. Unlike Rocket, MiniRocket uses a small, fixed set of kernels (with different bias and dilation combinations) and only computes PPV features. Since MiniRocket has the same accuracy as Rocket and is much faster, MiniRocket is recommended to be the default variant of Rocket. In this work, we extend MiniRocket with first order difference and additional pooling operators to achieve a new SOTA TSC algorithm that is also scalable. We describe MultiRocket in Section 3.

<!-- chunk {"id": "body-0021", "role": "body", "section": "Time series representations", "weight": 1.0} -->

Traditionally, time series analysis involves analysing time series data under different transformations, such as the Fourier transform. Different transformations and representations show different information about the time series. Transforming a time series to a useful representation allows us to better capture meaningful and indicative patterns to discriminate different or group similar time series, thus improving the performance of a model. A poor representation may lead to lost performance. For instance, it is easier to analyse time series of different frequencies if they were represented in the frequency domain. This is known as spectral analysis. The Fourier transform transforms a time series into the frequency domain, giving a spectrum of frequencies. Then the transformed time series is analysed using the magnitude of each frequency in the spectrum. A limitation of the Fourier transform is that it only gives information on which frequencies are present but has no information about location and time. In consequence, the wavelet transform was proposed to better capture the location of each frequency.

<!-- chunk {"id": "body-0022", "role": "body", "section": "Time series representations", "weight": 1.0} -->

A recent review groups different time series transforms that are often used in time series forecasting tasks into two categories, *mapping* and *splitting* transforms. Mapping-based transforms map a time series into another representation through a mathematical process such as logarithm, moving average and differencing. Splitting-based transforms split a time series into a number of component time series, such as Fourier and Wavelet transforms that split a time series into different frequencies. Each component is a simpler time series that can be analysed separately and later be reversed to obtain the original time series representation.

<!-- chunk {"id": "body-0023", "role": "body", "section": "Time series representations", "weight": 1.0} -->

The derivatives can also be used to capture different information about time series. The first order derivative captures the "velocity" (rate of change) of the data points in the time series. The second order derivative then measures the "acceleration" of each data point. Górecki and Łuczak combines the original raw series and its first order derivative by weighing the distance of the raw series and the first order derivative series. They showed that their approach achieved better classification accuracy than using the two representations separately. Calculating the exact derivatives of a time series is difficult without knowing the underlying function. There are many ways to estimate derivatives. Górecki and Łuczak explored 3 different methods and they found that they do not statistically differ from one another. Hence, we use the simple differencing approach to estimate the derivatives of a time series.

<!-- chunk {"id": "body-0024", "role": "body", "section": "Time series representations", "weight": 1.0} -->

In Section 4, we explore some time series transformation methods to improve the accuracy of MiniRocket and create MultiRocket.

<!-- chunk {"id": "body-0025", "role": "body", "section": "MultiRocket", "weight": 1.0} -->

This section describes MultiRocket in detail. MultiRocket shares the overarching architecture of MiniRocket -- it transforms time series using convolutional kernels, computes features from the convolution outputs and trains a linear classifier. There are two main differences between MultiRocket and MiniRocket. First is the usage of the first order difference transform and second is the additional 3 pooling operators used per kernel. The combination of these transformations significantly boosts the classification power of MiniRocket. The type of transforms and pooling operators used were tuned on the same 40 "development" datasets as used in to avoid overfitting the entire UCR archive.

<!-- chunk {"id": "body-0026", "role": "body", "section": "Time series representations", "weight": 1.0} -->

Diversity is the key to improve a classifier's accuracy. HIVE-COTE 2.0 is an accurate TSC classifier because it is a meta-ensemble of a diverse set of time series ensembles, each capturing different representations of a time series, e.g., DrCIF.

<!-- chunk {"id": "body-0027", "role": "body", "section": "Time series representations", "weight": 1.0} -->

Drawing inspiration from DrCIF, we first inject diversity into MiniRocket by transforming the original time series into its first order difference. From this point onward, we refer to the original time series that has not been transformed as the base time series. Then convolution is applied to both base and first order difference time series. We explored different transformation combinations in Section 4 and found that this combination works best overall on the 40 "development" datasets. Note that different transformations can be considered depending on the dataset and problem, and we consider this exploration as future work.

<!-- chunk {"id": "body-0028", "role": "body", "section": "Time series representations", "weight": 1.0} -->

The first order difference of a time series describes the rate of change of the time series between each unit time step. This gives additional information about the time series, such as identifying the slope of a time series or the presence of certain outliers (or patterns) in a time series that maybe easier to discriminate between two classes. A given time series $X = {\{ x_{1},x_{2},\ldots,x_{l}\}}$ is transformed into its first order difference, $X^{\prime}$ using Equation 1. We will use this notation to refer to a time series throughout the paper.

<!-- chunk {"id": "body-0029", "role": "body", "section": "Convolutional kernels", "weight": 1.0} -->

Now, we describe the convolutional kernels used in MultiRocket. MultiRocket uses the same fixed set of kernels as used in MiniRocket, producing high classification accuracy and allowing for a highly optimised transform. Note that the enhancement used in MultiRocket is also applicable to improve the classification accuracy of Rocket. However, MiniRocket is preferable over Rocket due to its scalability. We refer interested readers to for details of the kernels used in Rocket.

<!-- chunk {"id": "body-0030", "role": "body", "section": "Convolutional kernels", "weight": 1.0} -->

Length and weights: As per MiniRocket, MultiRocket uses kernels of length 9, with weights restricted to two values and, in particular, the subset of such kernels where six weights have the value $- 1$, and three weights have the value $2$, e.g., $W = {\lbrack{- 1},{- 1},{- 1},{- 1},{- 1},{- 1},2,2,2\rbrack}$. This gives a total of 84 fixed kernels.

<!-- chunk {"id": "body-0031", "role": "body", "section": "Convolutional kernels", "weight": 1.0} -->

Dilation: Each kernel uses the same (fixed) set of dilations. Dilations are set in the range $\{{\lfloor 2^{0}\rfloor},\ldots,{\lfloor 2^{\text{max}}\rfloor}\}$, with the exponents spread uniformly between 0 and $\text{max} = {{\log_{2}{({l_{\text{input}} - 1})}}/{({l_{\text{kernel}} - 1})}}$, where $l_{\text{input}}$ is the length of the input time series and $l_{\text{kernel}}$ is kernel length.

<!-- chunk {"id": "body-0032", "role": "body", "section": "Convolutional kernels", "weight": 1.0} -->

Bias: Bias values for each kernel/dilation combination are drawn from the convolution output. For each kernel/dilation combination, we compute the convolution output for a randomly-selected training example, and take the quantiles of this output as bias values. (The random selection of training examples is the only random aspect of these kernels.)

<!-- chunk {"id": "body-0033", "role": "body", "section": "Convolutional kernels", "weight": 1.0} -->

Padding: Padding is alternated between kernel/dilation combinations, such that half of the kernel/dilation combinations use padding (standard zero padding), and half do not.

<!-- chunk {"id": "body-0034", "role": "body", "section": "Convolution operation", "weight": 1.0} -->

The base and first order difference time series use different set of dilations and biases to produce the feature maps. The first order difference time series is shorter by one value than the base time series. Hence, the maximum dilation for the first order difference time series will be shorter than the base time series, resulting in a slightly different set of kernels than the base time series. Additionally, it has a different range of values from the base time series, resulting in a different set of bias values. Apart from these, the length, weights and padding are the same for both base and first order difference time series. The convolution operation then involves a sliding dot product between a kernel and a time series.

<!-- chunk {"id": "body-0035", "role": "body", "section": "Pooling operators", "weight": 1.0} -->

After the convolution operations, MultiRocket then computes four features per convolution output, $Z$, with length $n$. These features summarise the values in $Z$ and are also known as pooling operators. Table 1 shows a summary of the pooling operators used in MultiRocket, *Proportion of Positive Values* (PPV), *Mean of Positive Values* (MPV), *Mean of Indices of Positive Values* (MIPV) and *Longest Stretch of Positive Values* (LSPV). The features are illustrated in Figure 3. Algorithm 1 in Appendix A illustrates the procedure to calculate all four features for a given convolution output, $Z$.

<!-- chunk {"id": "body-0036", "role": "body", "section": "Proportion of positive values", "weight": 1.0} -->

PPV was introduced in Rocket and was found to be an exceptional feature for MiniRocket. It calculates the *proportion of positive values* from a convolution output $Z$. PPV is directly related to the bias term which can be seen as a 'threshold' for PPV, as described in Equation 2. A positive bias value means that PPV is able to capture the proportion of the time series reflecting even weak matches between the input and a given pattern, while a negative bias value means that PPV only captures the proportion of the input reflecting strong matches between the input and the given pattern. It is important to note that given PPV, computing the proportion of negative values would not add any extra information as they are complementary to each other. Given the exceptional performance and importance of PPV in MiniRocket, we retain PPV in MultiRocket.

<!-- chunk {"id": "body-0037", "role": "body", "section": "Proportion of positive values", "weight": 1.0} -->

We augment PPV with three further pooling operators that capture forms of information about the convolutional output to which PPV is blind.

<!-- chunk {"id": "body-0038", "role": "body", "section": "Mean of positive values", "weight": 1.0} -->

First, we propose the *Mean of Positive Values* (MPV) to capture the magnitude of the positive values in a convolution output, $Z$ of length $n$, for example, distinguishing A from E in Table 1. MPV is calculated using Equation 3 where $Z^{+}$ represents a vector of positive values of length $m$ and ${\text{PPV}{(Z)}} = {{|Z^{+}|}/n} = {m/n}$.

<!-- chunk {"id": "body-0039", "role": "body", "section": "Mean of positive values", "weight": 1.0} -->

Similar to PPV, MPV is related to the bias term. It captures the intensity of the matches between an input time series and a given pattern -- an information that is available when computing PPV but discarded. This means that MPV can be computed with negligible additional computational cost.

<!-- chunk {"id": "body-0040", "role": "body", "section": "Mean of indices of positive values", "weight": 1.0} -->

The *Mean of Indices of Positive Values* (MIPV) captures information about the relative location of positive values in the convolution outputs, for example, distinguishing A from B in Table 1. Consider the convolution output $Z$ as an array of values, MIPV is computed by first recording the relative location of all positive values in the array, i.e., its indices in the array. Then the mean of the indices is calculated using Equation 4, where $I^{+}$ indicates the indices of positive values. Note that ${\text{PPV}{(Z)}} = {{|I^{+}|}/n} = {m/n}$, where $m$ is the number of positive values in $Z$. In the case where there are no positive values, $m = 0$, MIPV returns -1 to differentiate from the first index, considering we start with index 0.

<!-- chunk {"id": "body-0041", "role": "body", "section": "Mean of indices of positive values", "weight": 1.0} -->

For example, the convolution output $A$ in the dummy example in Table 1 has positive values at locations $I^{+} = {\lbrack 6,7,8,9\rbrack}$ giving $\text{MIPV} = 7.5$.

<!-- chunk {"id": "body-0042", "role": "body", "section": "Mean of indices of positive values", "weight": 1.0} -->

Since ${\text{PPV}{(Z)}} = {{|I^{+}|}/n}$, the indices of positive values are also available when we are calculating PPV, but currently not used in MiniRocket. Thus, like MPV, MIPV can also be computed with negligible additional cost.

<!-- chunk {"id": "body-0043", "role": "body", "section": "Longest stretch of positive values", "weight": 1.0} -->

MIPV pools all positive values and hence fails to distinguish between many small sequences of successive positive values and a small number of long sequences. This can provide information of the underlying time series as shown in the example in Appendix B. The *Longest Stretch of Positive Values* (LSPV) returns the maximum length of any subsequence of positive values in a convolution output, calculated using Equation 5.

<!-- chunk {"id": "body-0044", "role": "body", "section": "Longest stretch of positive values", "weight": 1.0} -->

This provides a different form of information about the positive values in the convolutional output than is provided by any of the other features, for example, distinguishing C from the remaining series in Table 1. Note that calculating LSPV comes with a slight overhead over both MPV and MIPV.

<!-- chunk {"id": "body-0045", "role": "body", "section": "Classifier", "weight": 1.0} -->

By default, MultiRocket produces 50,000 features (49,728 to be exact, using 6,216 kernels, 2 representations and 4 pooling operators). Like MiniRocket, the transformed features are used to train a linear classifier. MultiRocket uses a ridge regression classifier by default. As suggested in Dempster et al., a logistic regression classifier is preferable for larger datasets as it is faster to train. All of our experiments in Section 4 were conducted with the ridge classifier. The software also supports the logistic regression classifier if required.

<!-- chunk {"id": "body-0046", "role": "body", "section": "Experiments", "weight": 1.0} -->

In this section, we evaluate MultiRocket on the datasets in the UCR univariate time series archive. We show that MultiRocket is significantly more accurate than its predecessor, MiniRocket and not significantly less accurate than the current most accurate TSC classifier, HIVE-COTE 2.0. By default, MultiRocket generates $50,000$ features. We show that even with $50,000$ features, MultiRocket is only about 10 times slower than MiniRocket, but orders of magnitude faster than other current state of the art methods. Our experiments also show that the smaller variant of MultiRocket with $10,000$ features (same number of features as MiniRocket) is as fast as MiniRocket while being significantly more accurate. Finally, we explore key design choices, including the choice of transformations, features and the number of features. These design choices are tuned on the 40 "development" datasets as used in to reduce overfitting of the whole UCR archive.

<!-- chunk {"id": "body-0047", "role": "body", "section": "Experiments", "weight": 1.0} -->

MultiRocket is implemented in Python, compiled via Numba and we use the ridge regression classifier from scikit-learn. Our code and results are all publicly available in the accompanying website, All of our experiments were conducted on a cluster with AMD EPYC 7702 CPU, 32 threads and 64 GB memory.

<!-- chunk {"id": "body-0048", "role": "body", "section": "Comparing with current state of the art", "weight": 1.0} -->

First, we evaluate MultiRocket and compare it with the current most accurate TSC algorithms, namely HIVE-COTE 2.0, TS-CHIEF, InceptionTime, MiniRocket, Arsenal, DrCIF, TDE, STC and ProximityForest. These algorithms^11^1We obtained the results from for MiniRocket and for the rest. are chosen because they are the most accurate in their respective domains. ProximityForest represents the distance-based algorithms; STC represents shapelet-based algorithms; While TDE and DrCIF represent dictionary-based and interval-based algorithms respectively.

<!-- chunk {"id": "body-0049", "role": "body", "section": "Comparing with current state of the art", "weight": 1.0} -->

For consistency and direct comparability with the SOTA TSC algorithms, we evaluate MultiRocket on the same 30 resamples of 109 datasets from the UCR archive as reported and used. Note that each resample creates a different distribution for the train and test sets. Resampling of each dataset is achieved by first mixing the train and test sets, then performing a stratified sampling for train and test sets and maintaining the same number of instances for each resample.

<!-- chunk {"id": "body-0050", "role": "body", "section": "Comparing with current state of the art", "weight": 1.0} -->

Although HIVE-COTE 2.0 is significantly more accurate than MultiRocket with 59 wins out of 109 datasets, the difference in accuracy between HIVE-COTE 2.0 and MultiRocket lies within $\pm {5\%}$, as shown in Figure 6(a), indicating that there is relatively little difference between the two methods. On the other hand, MultiRocket and InceptionTime are not significantly different from each other, despite MultiRocket having more larger wins, as depicted in Figure 6(b). For instance, MultiRocket is most accurate against InceptionTime on the SemgHandMovementCh2 dataset with accuracy of 0.792 and 0.551. While InceptionTime is the most accurate against MultiRocket on the PigAirwayPressure dataset with accuracy of 0.922 and 0.647. The large variance in the difference in accuracy between MultiRocket and InceptionTime implies that both methods are strong in their own ways and that MultiRocket can potentially be improved on datasets where InceptionTime performed much better.

<!-- chunk {"id": "body-0051", "role": "body", "section": "Comparing with current state of the art", "weight": 1.0} -->

HIVE-COTE 2.0, TS-CHIEF and InceptionTime are able to capture the different time series representations that have not been able to be captured by MultiRocket. This shows the importance of diversity in classifiers to achieve high classification accuracy. However, as shown in Figure 2(a), MultiRocket only takes 5 minutes (using 32 threads) to complete training and classification on all 109 datasets, a time that is at least an order of magnitude faster than HIVE-COTE 2.0, TS-CHIEF and InceptionTime.

<!-- chunk {"id": "body-0052", "role": "body", "section": "Comparing with current state of the art", "weight": 1.0} -->

As seen on both Figures 6(a) and 6(b), MultiRocket performed the worst on the PigAirwayPressure dataset, with the largest difference of 0.308 and 0.275 compared to HIVE-COTE 2.0 and InceptionTime respectively. Rocket achieved poor performance on this dataset as pointed out in due to the way the bias values are sampled. This issue has been mitigated in MiniRocket by sampling the bias values from the convolution output instead of a uniform distribution, $U{({- 1},1)}$ in Rocket. MultiRocket samples different sets of bias for the base and first order difference series. It is possible that the first order differences gives rise to the poor performance on this dataset.

<!-- chunk {"id": "body-0053", "role": "body", "section": "Runtime analysis", "weight": 1.0} -->

The addition of the first order difference transform and additional 3 features increases the total compute time of MiniRocket. Figures 7(a) and 7(b) show the total compute time (training and testing) of both MultiRocket and MiniRocket with 10,000 and 50,000 features using an AMD EPYC 7702 CPU with a single thread. The default MultiRocket with 50,000 features is about an order of magnitude slower than the default MiniRocket with 10,000 features. Comparing with the same number of 50,000 features, MultiRocket is only 4 times slower than MiniRocket. This makes sense since MultiRocket computes four features per kernel instead of one. Taking approximately 40 minutes to complete all 109 datasets, MultiRocket is still significantly faster than all other SOTA methods, as shown in Table 2. However, running MultiRocket with 32 threads significantly reduces this time to 5 minutes as shown in Figure 2(a). Hence it is recommended to use MultiRocket in a multi-threaded setting. Note that MultiRocket with 10,000 features is significantly more accurate than MiniRocket as shown in Appendix D.

<!-- chunk {"id": "body-0054", "role": "body", "section": "Runtime analysis", "weight": 1.0} -->

All the other SOTA methods have a long run time as reported. We took the total train time on 112 UCR datasets from and show them in Table 2 together with a few variants of MultiRocket and MiniRocket with 10,000 and 50,000 features as comparison. As expected, MiniRocket is the fastest, taking just under 3 minutes to train. This is followed by MultiRocket that took around 16 minutes. Rocket took approximately 3 hours to train, while Arsenal, an ensemble of Rocket took 28 hours. The fastest non-Rocket algorithm is DrCIF, taking about 2 days to train, followed by TDE with 3 days. Finally, the collective ensembles are the slowest taking at least 14 days to train. Note that the time for InceptionTime is not directly comparable as it was trained on a GPU.

<!-- chunk {"id": "body-0055", "role": "body", "section": "Ablation study", "weight": 1.0} -->

So far, we have shown that MultiRocket performed well overall. In this section, we explore the effect of key design choices for MultiRocket. The choices include (A) selecting the time series representations (B) selecting the set of pooling operators and (C) increasing the number of features.

<!-- chunk {"id": "body-0056", "role": "body", "section": "Time series representations", "weight": 1.0} -->

We explore the effect of the different representations using MiniRocket as the baseline. We consider the first and second order difference to estimate the derivatives of the time series and periodogram to capture information about the frequencies that are present in the time series. Figure 8 shows the comparison of the different combinations of the all 4 representations (including the base time series) for MiniRocket. The figure shows that using each of the representation alone does not improve the accuracy, as some information is inevitably lost during the transformation process. However, combining the base series with either representation improves MiniRocket, with the first order difference being the most accurate. The result indicates that adding diversity to MiniRocket by combining different time series representations with the base time series improves MiniRocket's performance.

<!-- chunk {"id": "body-0057", "role": "body", "section": "Time series representations", "weight": 1.0} -->

We then perform the same experiment on MultiRocket and observed similar results, as shown in Figure 9. We used the smaller variant of MultiRocket to be comparable to MiniRocket. In this case, comparing the base versions (MiniRocket and MultiRocket (10k) base) shows that adding the additional 3 pooling operators also improves the discriminating power of MiniRocket, as indicated in the discussion in Appendix D.

<!-- chunk {"id": "body-0058", "role": "body", "section": "Pooling operators", "weight": 1.0} -->

The previous section shows that applying convolutions to the base and first order difference series improves the discriminating power of MiniRocket and MultiRocket. Hence it is chosen as the default for MultiRocket. Now, we explore the effect of different combinations of pooling operators used by each kernel on classification accuracy. Figure 10 compares the different pooling operator combinations of MultiRocket with 10,000 features with the baseline MiniRocket and MiniRocket with base and first order difference series. The result shows that the variant using all pooling operators performed the best overall. This confirms our justification of using all four pooling operators in Section 3. Figure 10 also shows that PPV is a strong feature, where most of the combinations did not perform better than using PPV alone. The use of each pooling operator alone (without the combination) also performed significantly worse than PPV.

<!-- chunk {"id": "body-0059", "role": "body", "section": "Number of features", "weight": 1.0} -->

The default setting of MultiRocket uses the combination of the base and first order difference and extracts 4 features per convolution kernel. In this section, we explore the effect of increasing the number of features in MultiRocket. Figure 11 shows the comparison of MultiRocket with different numbers of features. We also compare with the default MiniRocket, MiniRocket with 50,000 features and MiniRocket with base and first order difference. Overall, using 50,000 features is the most accurate and there is little benefit in using 100,000 features as more and more features will be similar to one another. A similar phenomenon was shown in Dempster et al.. Figures 12(a) and 12(b) show that MultiRocket with 50,000 features is significantly more accurate than both MiniRocket with 50,000 features and with the first order difference. MultiRocket is more accurate on 76 and 68 datasets respectively. The results show that the increase in accuracy is not just due to the large number of features but also due to the diversity in the extracted features using the four pooling operators and first order difference. Therefore MultiRocket uses 50,000 features by default.

<!-- chunk {"id": "body-0060", "role": "body", "section": "Conclusion", "weight": 1.5} -->

We introduce MultiRocket, by adding multiple pooling operators and transformations to MiniRocket to improve the diversity of the features generated. MultiRocket is significantly more accurate than MiniRocket but not significantly less accurate than the most accurate univariate TSC algorithm, HIVE-COTE 2.0 on the UCR archive. While being approximately 10 times slower than MiniRocket, MultiRocket is still significantly faster than all other state-of-the-art time series classification algorithms.

<!-- chunk {"id": "body-0061", "role": "body", "section": "Conclusion", "weight": 1.5} -->

MultiRocket applies first order differencing to transform the time series. Then four pooling operators PPV, MPV, MIPV and LSPV are used to extract summary statistics from the convolution outputs of the base and first difference series. As the application of convolutions to time series is designed to highlight useful properties of the series, it seems likely that further development of methods to isolate the relevant signals in these convolutions will be highly productive. Besides, different transformation methods can also be explored to further improve the diversity of MultiRocket. Further promising future directions include exploring the utility of MultiRocket on multivariate time series, regression tasks and beyond time series data.
