Bake off Redux: A Review and Experimental Evaluation of Recent Time Series Classification Algorithms

Topics include Deep learning, Classification, Time series classification, Time series, UCR archive, Datasets, Benchmarks, Learning, Bake off redux, TSC, UCR, DTW, Dynamic time warping.

In 2017, a research paper compared 18 Time Series Classification (TSC) algorithms on 85 datasets from the University of California, Riverside (UCR) archive. This study, commonly referred to as a `bake off', identified that only nine algorithms performed significantly better than the Dynamic Time Warping (DTW) and Rotation Forest benchmarks that were used. The study categorised each algorithm by the type of feature they extract from time series data, forming a taxonomy of five main algorithm types. This categorisation of algorithms alongside the provision of code and accessible results for reproducibility has helped fuel an increase in popularity of the TSC field. Over six years have passed since this bake off, the UCR archive has expanded to 112 datasets and there have been a large number of new algorithms proposed. We revisit the bake off, seeing how each of the proposed categories have advanced since the original publication, and evaluate the performance of newer algorithms against the previous best-of-category using an expanded UCR archive. We extend the taxonomy to include three new categories to reflect recent developments.

## Introduction

Time series classification (TSC) involves fitting a model from a continuous, ordered sequence of real valued observations (a time series) to a discrete response variable. Time series can be univariate (a single variable observed at each time point) or multivariate (multiple variables observed at each time point). For example, we could treat raw audio signals as a univariate time series in a problem such as classifying whale species from their calls and motion tracking co-ordinate data could be a three-dimensional multivariate time series in a human activity recognition (HAR) task.

TSC problems arise in a wide variety of domains. Popular TSC archives^11^1 contain classification problems using: electroencephalograms; electrocardiograms; HAR and other motion data; image outlines; spectrograms; light curves; audio; traffic and pedestrian levels; electricity usage; electrical penetration graph; lightning tracking; hemodynamics; and simulated data. The huge variation in problem domains characterises TSC research.

We describe a range of new algorithms for TSC and place them in the context of those described in the bake off.

We compare performance of the new algorithms on the current UCR archive datasets in a univariate classification bake off redux.
