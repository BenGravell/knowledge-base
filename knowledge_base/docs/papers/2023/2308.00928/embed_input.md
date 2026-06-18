QUANT: A Minimalist Interval Method for Time Series Classification

Topics include Classification, Time series classification, Time series, UCR archive, Classifiers, Datasets, Benchmarks, Accuracy, QUANT.

We show that it is possible to achieve the same accuracy, on average, as the most accurate existing interval methods for time series classification on a standard set of benchmark datasets using a single type of feature (quantiles), fixed intervals, and an 'off the shelf' classifier. This distillation of interval-based approaches represents a fast and accurate method for time series classification, achieving state-of-the-art accuracy on the expanded set of 142 datasets in the UCR archive with a total compute time (training and inference) of less than 15 minutes using a single CPU core.

## Introduction

Figure 1: Multiple Comparison Matrix for Quant vs TSF, STSF, rSTSF, CIF, and DrCIF, for a subset of 112 datasets from the UCR archive.

Interval methods represent a long-standing and prominent approach to time series classification. Most interval methods are strikingly similar, closely following a paradigm established by Rodríguez et al and Geurts, and involve computing various descriptive statistics and other miscellaneous features over multiple subseries of an input time series, and/or some transformation of an input time series (e.g., the first difference or discrete Fourier transform), and using those features to train a classifier, typically an ensemble of decision trees. This represents an appealingly simple approach to time series classification.

## Conclusion

We demonstrate that a simplified interval method, Quant, using a single type of feature (quantiles), fixed intervals, and a standard classifier, without any separate interval or feature selection process, can achieve the same accuracy as the most accurate current interval methods. Compared to most current state-of-the-art methods for time series classification---many of which require considerable computational resources---Quant is both simpler, and represents a significant improvement in terms of accuracy relative to computational cost....

### Classifier

## Method

Over these 142 datasets, Quant is reasonably similar to both WEASEL-D and InceptionTime in terms of mean accuracy and win/draw/loss. However, Quant is clearly somewhat less accurate than the most accurate methods (RDST, MultiRocket+Hydra, and HC2). Quant is more accurate than rSTSF on 81 datasets, and less accurate on 56. In contrast, Quant is more accurate than HC2 on only 41 datasets, and less accurate on 97.

We observe that it is possible to achieve the same accuracy, on average, as the most accurate existing interval methods simply by sorting the values in each interval and using the sorted values as features or, in order to reduce the size of the feature space (and, accordingly, computational cost), to subsample these sorted values, i.e., to use the quantiles of the values in the intervals as features. We name this approach Quant.

The difference in mean accuracy and the pairwise win/draw/loss between Quant and several other prominent interval methods, namely, TSF, STSF, rSTSF, CIF, and DrCIF, for a...
