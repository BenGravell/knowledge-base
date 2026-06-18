MultiRocket: Multiple Pooling Operators and Transformations for Fast and Effective Time Series Classification

Topics include Classification, Time series classification, Time series, Datasets, Benchmarks, Accuracy, MultiRocket, fast time series classification, TSC.

We propose MultiRocket, a fast time series classification (TSC) algorithm that achieves state-of-the-art performance with a tiny fraction of the time and without the complex ensembling structure of many state-of-the-art methods. MultiRocket improves on MiniRocket, one of the fastest TSC algorithms to date, by adding multiple pooling operators and transformations to improve the diversity of the features generated. In addition to processing the raw input series, MultiRocket also applies first order differences to transform the original series. Convolutions are applied to both representations, and four pooling operators are applied to the convolution outputs. When benchmarked using the University of California Riverside TSC benchmark datasets, MultiRocket is significantly more accurate than MiniRocket, and competitive with the best ranked current method in terms of accuracy, HIVE-COTE 2.0, while being orders of magnitude faster.

## Introduction

Many of the most accurate methods for time series classification (TSC), such as HIVE-COTE 2.0, achieve high classification accuracy at the expense of high computational complexity and limited scalability. Hence scalable TSC has become an important research topic in recent years. Rocket and MiniRocket are the fastest and most scalable among all the proposed scalable TSC methods that achieve state-of-the-art (SOTA) accuracy. They achieve SOTA accuracy with a fraction of the computational expense of any other method of similar accuracy.

MiniRocket is built on Rocket and is recommended over Rocket due to its scalability. We show that it is possible to significantly improve the accuracy of MiniRocket, with some additional computational expense, by transforming the time series prior to the convolution operations, and by expanding the set of pooling operations used to generate features. We call this method MultiRocket -- for MiniRocket with multiple pooling operators and transformations.

The rest of the paper is organised as follows. In Section 2, we review the relevant existing work. In Section 3, we describe MultiRocket in detail. In Section 4, we present our experimental results and conclude our paper.

## Conclusion

We introduce MultiRocket, by adding multiple pooling operators and transformations to MiniRocket to improve the diversity of the features generated. MultiRocket is significantly more accurate than MiniRocket but not significantly less accurate than the most accurate univariate TSC algorithm, HIVE-COTE 2.0 on the UCR archive. While being approximately 10 times slower than MiniRocket, MultiRocket is still significantly faster than all other state-of-the-art time series classification algorithms.

MultiRocket applies first order differencing to transform the time series. Then four pooling operators PPV, MPV, MIPV and LSPV are used to extract summary statistics from the convolution outputs of the base and first difference series. As the application of convolutions to time series is designed to highlight useful properties of the series, it seems likely that further development of methods to isolate the relevant signals in these convolutions will be highly productive. Besides, different transformation methods can also be explored to further improve the diversity of MultiRocket.
