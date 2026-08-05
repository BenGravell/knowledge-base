<!-- arxiv-full-text:v1 {"arxiv_id": "2308.00928", "source": "ar5iv"} -->

## Introduction

Figure 1: Multiple Comparison Matrix for Quant vs TSF, STSF, rSTSF, CIF, and DrCIF, for a subset of 112 datasets from the UCR archive.

Interval methods represent a long-standing and prominent approach to time series classification. Most interval methods are strikingly similar, closely following a paradigm established by Rodríguez et al and Geurts, and involve computing various descriptive statistics and other miscellaneous features over multiple subseries of an input time series, and/or some transformation of an input time series (e.g., the first difference or discrete Fourier transform), and using those features to train a classifier, typically an ensemble of decision trees. This represents an appealingly simple approach to time series classification.

We observe that it is possible to achieve the same accuracy, on average, as the most accurate existing interval methods simply by sorting the values in each interval and using the sorted values as features or, in order to reduce the size of the feature space (and, accordingly, computational cost), to subsample these sorted values, i.e., to use the quantiles of the values in the intervals as features. We name this approach Quant.

The difference in mean accuracy and the pairwise win/draw/loss between Quant and several other prominent interval methods, namely, TSF, STSF, rSTSF, CIF, and DrCIF, for a subset of 112 datasets from the UCR archive (for which published results are available for all methods), are shown in the Multiple Comparison Matrix (MCM) in Figure 1. Results for the other methods are taken from Middlehurst et al. As shown in Figure 1, Quant achieves higher accuracy on more datasets, and higher mean accuracy, than existing interval methods. Total compute time for Quant is significantly less than that of even the fastest of these methods (see further below).

When using quantiles (or sorted values) as features, as we increase or decrease interval length, we move between two extremes: (a) a single interval where the quantiles (or sorted values) represent the distribution of the values over the whole time series (distributional information without location information); and (b) intervals of length one, together consisting of all of the values in the time series in their original order (location information without distributional information): see Figure 2.

Figure 2: Sorted values for intervals of decreasing length. Larger intervals contain more distributional information but less location information.

Quantiles represent a superset of many of the features used in existing interval methods (min, max, median, etc.). Using quantiles allows us to trivially increase or decrease the number of features, by increasing or decreasing the number of quantiles per interval which, in turn, allows us to balance accuracy and computational cost. We find that quantiles can be used with fixed (nonrandom) intervals, without any explicit interval or feature selection process, and with an 'off the shelf' classifier, in particular, extremely randomised trees, following Cabello et al.

The key advantages of distilling interval methods down to these essential components are simplicity and computational efficiency. Quant represents one of the fastest methods for time series classification. The cost of computing the quantiles, in particular, is very low. Median transform time over 142 datasets in the UCR archive is less than one second. Total compute time (training and inference) is under 15 minutes for the same 142 datasets using a single CPU core. This is approximately $5 \times$ faster than the fastest existing interval method, rSTSF, already one of the fastest methods for time series classification.

The rest of this paper is structured as follows. In Section 2, we discuss relevant related work. In Section 3, we set out the key aspects of the method. In Section 4, we present experimental results including a sensitivity analysis.

## Background

### Interval Methods

Methods closely resembling current state-of-the-art interval methods have been applied to the domain of time series classification at least since Rodríguez et al and Geurts. Most interval methods are strikingly similar, closely following the basic concept set out, e.g., Rodríguez and Alonso, namely: for a set of intervals (subseries) taken from the input time series, and/or some transformation of the input time series such as the first difference or discrete Fourier transfom; compute descriptive statistics (e.g., mean and variance) and other features for the values in each interval; and use the computed features to train a classifier, typically an ensemble of decision trees.

Different interval methods are characterised by the set of transformations applied to the input time series, the characteristics of the intervals, the use of interval and/or feature selection, and the choice of classifier.

Many methods use one or more transformations of the input time series. RISE replaces the input time series with spectral, autocorrelation, and autoregressive representations. More recently, the use of the original input time series in combination with the first difference, and some form of frequency domain representation (e.g., the discrete Fourier transform), has lead to significant improvements in accuracy over earlier methods.

Some methods use fixed intervals, recursively splitting the input time series in half, while some use random intervals, recursively splitting the input time series at random points, or sampling intervals with random length and position. Others methods use heuristic approaches.

All or almost all proposed methods use a fixed set of descriptive statistics (e.g., mean and variance), often combined with other features such as slope. Several methods employ some form of explicit feature and/or interval selection process.

Other variations to the basic concept of interval methods include forming 'bag of words' representations of the features extracted from intervals, fitting Gaussian process models to intervals, and approaches incorporating clustering.

Most methods use an ensemble of decision trees, including specialised decision trees for interval features such as 'time series trees', or standard ensembles such as boosted decision trees, random forests, or extremely randomised trees. Some methods use other classifiers such as support vector machines. In this context, it is worth noting that some earlier methods were proposed prior to the introduction of what are now considered canonical classifiers such as random forests or extremely randomised trees, and prior to or only shortly after the introduction of the UCR archive.

The two most accurate current interval methods on the datasets in the UCR archive are DrCIF, and rSTSF. Both, in turn, build on TSF. TSF uses random intervals (intervals with random position and length), and computes the mean, variance, and slope of the values in each interval. TSF uses an ensemble of specialised decision trees ('time series trees'), using a splitting criteria that combines entropy and a tie-breaking procedure, and trains each tree separately using a different set of random of intervals. Bagnall et al found that TSF was faster and at least as accurate as other interval methods on the datasets in the UCR archive at the time.

DrCIF builds on CIF, sampling random intervals (random position and length) from the input time series, first difference, and a periodogram, and computes features including the mean, standard deviation, slope, median, interquartile range, min, max, as well as the catch22 features. DrCIF uses a version of 'time series trees' as per TSF, training each tree separately with a random set of intervals and a random subset of features. DrCIF is one of the four components of HIVE-COTE 2 (HC2), the most accurate method for time series classification on the datasets in the UCR archive. rSTSF builds on STSF. For each of the original time series, first difference, a periodogram, and an autoregressive representation (the coefficients of an autoregressive model), and for each of the mean, standard deviation, slope, min, max, median, interquartile range, and two additional features (the number of intersections with the mean and the number of values greater than the mean), rSTSF recursively splits the input at random points, selecting intervals using the Fisher score, performing a kind of interval or feature selection. Unlike DrCIF, rSTSF uses an 'off the shelf' classifier, namely, extremely randomised trees. While DrCIF and rSTSF produce similar accuracies on the datasets in the UCR archive, rSTSF is considerably faster.

### Other State-of-the-Art Methods

In the recent 'bake off redux', Middlehurst et al evaluate the most accurate current methods for time series classification over an expanded set of 142 datasets from the UCR archive. Middlehurst et al determine that the most accurate methods from each of a diverse set of different approaches to time series classification are: Proximity Forest, FreshPRINCE, rSTSF, WEASEL-D, InceptionTime, RDST, MultiRocket+Hydra, and HC2.

Proximity Forest (PF) is an ensemble of decision trees using distance measures as splitting criteria. Proximity Forest 2.0 (PF2) is a recent extension of PF that improves computational efficiency, and uses a different set of distance measures. (PF2 was published concurrently with Middlehurst et al, and is not included in the study.)

FreshPRINCE focuses on simplicity, and combines features drawn from the TSFresh feature set, computed over the whole input time series, with a rotation forest classifier.

WEASEL-D is a dictionary method, involving extracting and counting symbolic patterns in time series, building on WEASEL, and uses dilated sliding windows and the Symbolic Fourier Transform with random parameters to extract patterns, in conjunction with a ridge regression classifier.

InceptionTime is an ensemble of convolutional neural network models based on the Inception architecture, and represents the most accurate deep learning model on the datasets in the UCR archive.

RDST is a shapelet method, computing features based on the distance between input time series and a set of discriminative subseries drawn from the training set, which uses randomly-selected shapelets with various dilations, and a ridge regression classifier.

MultiRocket+Hydra combines features from both MultiRocket and Hydra. MultiRocket is an extension of Rocket and MiniRocket. Rocket transforms input time series using a large set of random convolutional kernels (random in terms of their length, weights, bias, dilation, and padding), and uses both PPV ('proportion of positive values') and max pooling. MiniRocket uses a small, fixed set of convolutional kernels and PPV pooling, allowing for highly-optimised computation, and is significantly faster than Rocket. MultiRocket combines the kernels from MiniRocket with an expanded set of pooling functions, and is close to the most accurate method for time series classification on the datasets in the UCR archive, while being only marginally slower than MiniRocket. Hydra combines aspects of both Rocket and dictionary methods, counting the occurrence of random patterns, represented by random convolutional kernels, in input time series. Hydra is both faster and, with the exception of WEASEL-D, more accurate than other dictionary methods. All four methods employ a ridge regression classifier by default.

HC2 is an ensemble combining TDE, a dictionary method predating WEASEL-D, DrCIF, STC, a shapelet method predating RDST, and Arsenal, an ensemble of Rocket models. HC2 is the most accurate method for time series classification on the datasets in the UCR archive.

While there has been significant progress in terms of both accuracy and computational cost since Bagnall et al, there is still great variability in the computational efficiency of the most accurate methods, with total compute time on the expanded set of 142 datasets ranging between hours, for the faster methods, and several weeks.

## Method

Quant involves computing quantiles over a fixed set of intervals on the input time series (and three transformations of the input time series), and using the computed quantiles to train a classifier. Compared to both DrCIF and rSTSF, we use: (a) a single type of feature (quantiles); and (b) fixed, dyadic intervals. In contrast to rSTSF, we use no explicit interval or feature selection process (in this sense, feature selection is delegated entirely to the classifier) and, in contrast to DrCIF, we use a standard classifier. The simplicity of our approach allows for exceptional computational efficiency, and helps to clarify the factors which are material to classification accuracy.

The key characteristics of Quant are: the set of input representations; the set of intervals; the features (quantiles); and We implement Quant in Python, using the implementation of extremely randomised trees from scikit-learn. Our code and results will be made available at

### Input Representations

Following Middlehurst et al, we use the original time series, the first difference, $X' = {\{{x_{1} - x_{0}},{x_{2} - x_{1}},\ldots,{x_{n - 1} - x_{n - 2}}\}}$, and the discrete Fourier transform, $\mathcal{F}{(X)}$. We find that it is also beneficial to use the second difference, $X^{\operatorname{\prime\prime}} = {\{{x_{1}' - x_{0}'},{x_{2}' - x_{1}'},\ldots,{x_{n - 1}' - x_{n - 2}'}\}}$, although the improvement in accuracy is marginal: see Section 4.2.2. We find that it is beneficial to smooth the first difference by applying a simple moving average. Again, the effect seems to be relatively small. We found no consistent improvement in accuracy by smoothing the other input representations.

### Intervals

Formally, a time series is a sequence of values ordered in time, $X = {\{ x_{0},x_{1},\ldots,x_{n - 1}\}}$, where $n$ is time series length. An interval is a contiguous subset of values $\{ x_{a},\ldots,x_{b}\}$, where ${a \geq 0},{{b > a},{b \leq {n - 1}}}$. We define interval length as $m = {b - a}$, and the number of quantiles per interval as a fraction of interval length, e.g., $m/\, 2$ corresponds to computing a number of quantiles equal to half the number of values in a given interval. For present purposes, we assume that all time series are univariate and of the same length. We leave the extension of the method to variable-length and multivariate time series to future work.

In contrast to Cabello et al, and Middlehurst et al, we use fixed, dyadic intervals. We define our set of intervals in terms of 'depth', $d$, such that we divide the input time series into $\{ 2^{0},2^{1},\ldots,2^{d - 1}\}$ intervals of length $\{{n/\, 2^{0}},{n/\, 2^{1}},\ldots,{n/2^{d - 1}}\}$, as shown in Figure 3. For each depth greater than one we also add the same set of intervals shifted by half the interval length.

Figure 3: An illustration of the set of intervals for a depth of d = 4, including ‘shifted’ intervals for d > 1.

Accordingly, the total number of intervals is ${2^{d - 1} \times 4} - 2 - d$ for each input representation. By default, we use a depth of $d = {\text{min}{(6,{{\lfloor{\log_{2}n}\rfloor} + 1})}}$, meaning that there are $120$ intervals per representation, and the smallest intervals are of length $\text{max}{(1,{n/\, 32})}$.

As we use nonoverlapping intervals (treating the 'shifted' intervals as a separate set of intervals at each depth), the total number of features per depth is always proportional to time series length, $n$, regardless of the number of intervals being constructed. For example, if we take $m/\, 2$ quantiles per interval, for a depth of $d = 1$ we take $n/\, 2$ quantiles (where $d = 1$, $m = n$), and for a depth of $d = 2$, we likewise take $n/\, 2$ quantiles ($m = {n/\, 2}$, so that ${{2 \times m}/\, 2} = m = {n/\, 2}$). Taking $m$ quantiles per interval is equivalent to using the sorted values.

### Features

The sorted values represent the empirical distribution of values in each interval. Quantiles, being a subsample of the sorted values, represent an approximation of the full set of values, that is, an approximation of the empirical distribution. Importantly, this approximation reduces the size of the feature space, in turn reducing computational complexity (in particular, in relation to classifier training).

As noted above, we define the number of quantiles per interval in proportion to interval length. By default, we compute $m/\, 4$ quantiles per interval, where $m$ is interval length. (For intervals of length one, we simply use the given value. For a single quantile, we use the median.)

Broadly speaking, we find that accuracy increases as the number of quantiles per interval increases, although the actual differences in accuracy are small, and computing more quantiles per interval results in proportionally higher computational cost: see Section 4.2.1.

We find that it is beneficial to compute both: (a) the quantiles of the values in each interval, representing the empirical distribution of the values in each interval; and (b) the quantiles of the values in each interval after subtracting the interval mean, representing the distribution of the values relative to the mean (i.e., such that the values are invariant to level shifts): see Figure 4. We find that an efficient means of doing this is to alternate between both representations by subtracting the interval mean from every second quantile. (We only subtract the mean where $m \geq 2$, and the number of quantiles is greater than one.) Note, however, that the effect of using both the original and mean-corrected quantiles, versus only the original quantiles, or only mean-corrected quantiles, is relatively small: see Section 4.2.3.

Figure 4: An illustration of quantiles drawn from intervals of length n/ 4. We compute quantiles for both the values in each interval, and the values after subtracting the interval mean, representing the distribution of the values and the distribution of the values relative to the mean respectively.

### Classifier

We use extremely randomised trees, as per rSTSF. The key distinctions with random forests are that extremely randomised trees do not use bagging, and extremely randomised trees consider a random split point for each candidate feature.

Interval methods can potentially produce a large number of features, depending on the number of input representations, the number of intervals, and the number of features per interval. For extremely randomised trees, the typical 'default' number of candidate features per split is the square root of the total number of features.

However, a large number of features in combination with a sublinear number of candidate features per split could potentially result in the classifier 'running out' of training examples before adequately exploring the feature space, especially in the context of smaller datasets. In other words, with a sublinear number of candidate features per split, as the size of the feature space grows, the probability of any given feature being considered decreases.

To this end, we find that it is beneficial to increase the number of candidate features per split to a linear proportion of the total number of features, in particular, $10\%$ of the total number features ($10\%$ of all features are considered at each split). In effect, we delegate interval and feature selection entirely to the classifier. The results show that this approach is both effective and computationally efficient.

### Complexity

We treat the computational cost of sorting the values as an upper bound on the cost of computing the quantiles: $O{({n{\log n}})}$, where $n$ is time series length. Naively, computing the quantiles for all intervals requires sorting the values in each interval, for each input representation. However, as we use a fixed number of input representations, and a fixed number of intervals, we treat these as constant factors.

In principle, we could sort each input representation once, keeping track of the indices of the sorted values, and then form any interval by selecting the already-sorted values using their indices. In practice, even the naive approach incurs negligible overall computational cost. Median transform time over 142 datasets in the expanded UCR archive is less than one second. The majority of compute time is spent in training the classifier. In other words, any attempt at optimising total compute time should concentrate on reducing the size of the feature space, and/or improving the efficiency of classifier training. We leave further optimisation for future work.

Assuming approximately balanced trees, the complexity of training the classifier is $O{({{p \cdot q}{\log q}})}$, where $p$ is the total number of features, and $q$ is the number of training examples. As we consider a linear proportion of the total number of features at each split, complexity is linear with $p$ (which is, in turn, linear with $n$). The number of trees is not proportional to the number of training examples, or the number of features, so we treat this as a constant factor.

## Experiments

We evaluate Quant on the datasets in the UCR archive, including 30 datasets recently incorporated into the archive, showing that Quant is at least as accurate, on average, as the most accurate existing interval methods, while being meaningfully faster. We also show the effect of key hyperparameter choices including the number of features, the set of input representations, the number of trees, and the number of candidate features per split.

### UCR Archive

We evaluate Quant on the datasets in the UCR archive. We compare Quant with the most accurate existing interval methods, and other state-of-the-art methods for time series classification. For direct compatibility with published results, we evaluate Quant on the same 30 resamples per Middlehurst et al. Results for other methods are taken from Middlehurst et al.

The difference in mean accuracy, the pairwise win/draw/loss, and the $p$ value for a Wilcoxon signed rank test---between Quant and other prominent interval methods, namely, TSF, STSF, rSTSF, CIF, and DrCIF, over a subset of 112 datasets from the UCR archive---are shown in the Multiple Comparison Matrix (MCM) in Figure 1 on page 1. In addition, Figure 5 shows the pairwise accuracy of Quant versus the two most accurate existing interval methods, namely, DrCIF (left), and rSTSF (right), on the same subset of 112 datasets.

Figure 5: Pairwise accuracy of Quant vs DrCIF (left), and rSTSF (right), for a subset of 112 datasets from the UCR archive.

Quant is more accurate on average than existing interval methods, including DrCIF and rSTSF, although the actual differences in accuracy are small. Quant is more accurate than DrCIF on 65 datasets, and less accurate on 43. Similarly, Quant is more accurate than rSTSF on 65 datasets, and less accurate on 42. However, as the results for all three methods are highly correlated, and the differences in accuracy are mostly small, even small changes in accuracy could change the appearance of the results, in particular, the ratio of wins and losses.

As noted above, thirty additional datasets were added to the UCR archive per the recent 'bakeoff redux'. Figure 7 shows the MCM for Quant versus current state-of-the-art methods, namely, HC2, MultiRocket+Hydra, RDST, WEASEL-D, InceptionTime, rSTSF, FreshPRINCE, and PF (see Section 2), over 30 resamples of the expanded set of 142 datasets. Figure 7 shows the pairwise accuracy of Quant versus rSTSF (left), and HC2 (right), for all 142 datasets.

Figure 6: MCM for Quant vs other state-of-the-art methods for 142 datasets from the UCR archive. Figure 7: Pairwise accuracy for Quant vs rSTSF (left), and HC2 (right), for 142 datasets from the UCR archive.

Over these 142 datasets, Quant is reasonably similar to both WEASEL-D and InceptionTime in terms of mean accuracy and win/draw/loss. However, Quant is clearly somewhat less accurate than the most accurate methods (RDST, MultiRocket+Hydra, and HC2). Quant is more accurate than rSTSF on 81 datasets, and less accurate on 56. In contrast, Quant is more accurate than HC2 on only 41 datasets, and less accurate on 97.

However, Quant is noticeably faster than any of these methods. Total compute time (training and inference) over all 142 datasets, averaged over 30 resamples, is less than 15 minutes using a single CPU core, compared to approximately 1 hour 15 minutes for MultiRocket+Hydra, 1 hour 35 minutes for rSTSF, almost 2 hours for WEASEL-D, more than 4 hours for RDST, more than one day for FreshPRINCE, several days for InceptionTime, and several weeks for HC2 and PF. (Timings for Quant are averages over 30 resamples, run on a cluster using Intel Xeon E5-2680 and Xeon Gold 6150 CPUs, restricted to a single CPU core per dataset per resample. Timings for other methods are taken from Middlehurst et al. Different timings are not necessarily directly comparable, due to hardware and software differences.) Using 8 CPU cores, compute time is reduced to 6 minutes.

The training time for the classifier is proportional to the total number of features. Accordingly, we can improve overall compute time by reducing the number of intervals and the number of quantiles per interval. To this end, Figure 17 (Appendix) shows the pairwise accuracy for a faster configuration of Quant (informally, Quant^FAST^), using approximately half the number of intervals ($d = 5$), and half the number of quantiles per interval ($m/\, 8$), versus rSTSF. Over 142 datasets, Quant^FAST^ is more accurate than rSTSF on 70 datasets, and less accurate on 66. Total compute time for Quant^FAST^ is approximately 7 minutes 40 seconds using a single CPU core. In other words, Quant^FAST^ achieves almost the same accuracy, on average, as rSTSF, but is approximately $10 \times$ faster.

### Sensitivity Analysis

We demonstrate the effect of key hyperparameters, namely: the number of features; the set of input representations (including smoothing); subtracting the mean; and the number of trees and the number of features per split.

Following Herrmann et al, in an effort to avoid the peculiarities of the smallest datasets and the original training/test splits, we conduct the sensitivity analysis using a random sample of 50 of the datasets from the subset of 112 datasets from the UCR archive used , e.g., Middlehurst et al, using stratified 5-fold cross-validation (such that, for each fold, $80\%$ of the data is used for training, and $20\%$ of the data is used for validation). In particular, from the subset of 112 datasets, we randomly sample 50 of the 100 datasets where there are at least 100 training examples on an 80/20 split, and at least 5 examples of each class.

### Number of Features

Figure 8 shows mean accuracy (left), and total compute time (right), in terms of both: (a) the number of intervals, expressed in terms of depth, $d$; and (b) the number of quantiles per interval, expressed as a proportion of interval length, $m$.

Figure 8: Mean accuracy (left), and total compute time (right), vs the number of intervals and the number of quantiles per interval.

Accuracy improves modestly as the number of quantiles per interval increases, although the accuracy for $m/\, 4$, $m/\, 2$, and $m$ quantiles per interval are very similar. The spread of accuracy values is very small. However, computing more quantiles per interval results in proportionally greater computational cost due to the expanded feature space: $m$ quantiles per interval requires twice the total compute time of $m/\, 2$ quantiles per interval.

It is apparent that, when computing a relatively small number of quantiles per interval, accuracy tends to increase as depth increases, up to a depth of approximately $d = 6$, and then decreases. The same effect is not evident for $m/\, 4$ or more quantiles per interval. We believe that this relates to the balance between distributional information and location information in larger versus smaller intervals: see Section 1. The results suggest that, broadly speaking, larger intervals are more informative than smaller intervals. With fewer quantiles per interval, more of the information in larger intervals is discarded, and smaller intervals dominate, which leads to lower accuracy. (It may be possible to counteract this effect by sampling features from larger intervals with higher probability when training the classifier. We leave this for future work.) Configurations using more quantiles per interval appear to be relatively immune to this effect.

While increasing depth significantly increases the number of intervals, the corresponding computational cost is linear with depth, as the total number of features computed at each depth is proportional to input length, rather than the number of intervals: see Section 3.2.

Figure 9 shows the pairwise accuracy for a depth of $d = 6$ with $m/\, 4$ quantiles per interval (the default) versus two extremes in terms of the total number of features, namely, a depth of $d = 4$ with $m/\, 16$ quantiles per interval (left), and a depth of $d = 8$ with $m$ quantiles per interval (right). While a smaller number of features clearly results in lower accuracy on several datasets, the differences in accuracy compared to a larger number of features are relatively small.

Figure 9: Pairwise accuracy for a depth of d = 6 with m/ 4 quantiles per interval (the default) vs a depth of d = 4 with m/ 16 quantiles per interval (left), and a depth of d = 8 with m quantiles per interval (right).

Figure 18 (Appendix) shows compute time versus the number of quantiles per interval for a depth of $d = 6$. This emphasises the extent to which compute time is dominated by the time required to train the classifier which, in turn, is determined by the size of the feature space.

We note that the results presented here relate to the characteristics of the datasets used in these experiments. In particular, we note that the lengths of most of the time series are relatively short: see Figure 19 (Appendix). In practice, it may be appropriate to adjust the parameters of the transform, e.g., depth, in order to suit the characteristics of a particular dataset.

### Input Representations

Figure 11 shows mean accuracy (left), and total compute time (right), for different combinations of input representation. Figure 11 shows pairwise accuracy for the default combination of the input time series, $X$, first difference, $X'$, second difference, $X^{\operatorname{\prime\prime}}$, and discrete Fourier transform, $\mathcal{F}{(X)}$, versus: $X,X',X^{\operatorname{\prime\prime}}$ (left); $X,X',{\mathcal{F}{(X)}}$ (centre); and $X,X^{\operatorname{\prime\prime}},{\mathcal{F}{(X)}}$ (right).

Figure 10: Mean accuracy (left), and total compute time (right), for different combinations of input representation. Figure 11: Pairwise accuracy for all representations (the default) vs removing ℱ (X) (left), removing X'' (centre), and removing X′ (right).

There is at least some advantage to using each of the three additional representations. Adding the discrete Fourier transform corresponds to the largest improvements in accuracy on individual datasets (Figure 11, left), while adding the second difference makes the least difference (Figure 11, centre). (For all configurations, we maintain the same number of features per representation.)

Figure 20 (Appendix) shows the pairwise accuracy for smoothing versus not smoothing the first difference, via a simple moving average with a window length of $5$. Smoothing the first difference clearly improves accuracy on several datasets. We found no consistent improvement in accuracy by smoothing any of the other representations.

### Subtracting the Mean

Figure 12 shows the pairwise accuracy for subtracting the mean from half of the quantiles (the default) versus not subtracting the mean from any quantiles (left), and subtracting the mean from all quantiles (right). Subtracting the mean from half of the quantiles results in higher accuracy than either not subtracting the mean, or subtracting the mean from all quantiles. There is no practical effect on compute time.

Figure 12: Pairwise accuracy for subtracting the mean from half of the quantiles (the default) vs not subtracting the mean from any quantiles (left), and subtracting the mean from all quantiles (right).

### Number of Trees

Figure 14 shows mean accuracy (left), and total compute time (right), versus the number of trees used in the classifier. Figure 14 shows the pairwise accuracy for 200 trees (the default) versus 50 trees (left), and 800 trees (right).

Figure 13: Mean accuracy (left), and total compute time (right), vs the number of trees. Figure 14: Pairwise accuracy for 200 trees (the default) vs 50 trees (left), and 800 trees (right).

Unsurprisingly, accuracy tends to increase as the number of trees increases, with a proportional increase in computational expense. However, while there are small but clear differences in accuracy between 50 trees and 200 trees, the differences in accuracy for more than approximately 200 trees are minimal.

### Number of Features per Split

Figure 16 shows mean accuracy (left), and total compute time (right), versus the number of candidate features per split as a proportion of the total number of features, $p$. Figure 16 shows the pairwise accuracy for $0.1 \times p$ (the default) versus $\sqrt{p}$ (left), and $0.2 \times p$ candidate features per split (right). Note that $\sqrt{p} > {0.01 \times p}$ for $p < {10,000}$.

Figure 15: Mean accuracy (left), and total compute time (right), vs the number of features per split as a proportion of the total number of features. Figure 16: Pairwise accuracy for 0.1 × p (the default) vs $\sqrt{p}$ (left), and 0.2 × p candidate features per split (right).

There is a clear advantage in terms of accuracy from increasing the number of candidate features per split to a linear proportion ($\geq {0.05 \times p}$) of the total number of features, with a proportional increase in computational expense. However, the differences in accuracy between sampling $5\%$, $10\%$, or $20\%$ of the features are minimal.

## Conclusion

We demonstrate that a simplified interval method, Quant, using a single type of feature (quantiles), fixed intervals, and a standard classifier, without any separate interval or feature selection process, can achieve the same accuracy as the most accurate current interval methods. Compared to most current state-of-the-art methods for time series classification---many of which require considerable computational resources---Quant is both simpler, and represents a significant improvement in terms of accuracy relative to computational cost. In future work, we intend to explore the extension of the method to variable-length and multivariate time series, as well as further improvements to computational efficiency.
