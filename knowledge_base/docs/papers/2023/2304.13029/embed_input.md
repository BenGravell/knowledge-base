<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Bake off Redux: A Review and Experimental Evaluation of Recent Time Series Classification Algorithms

Topics include Deep learning, Classification, Time series classification, Time series, UCR archive, Datasets, Benchmarks, Learning, Bake off redux, TSC, UCR, DTW, Dynamic time warping.

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

In 2017, a research paper compared 18 Time Series Classification (TSC) algorithms on 85 datasets from the University of California, Riverside (UCR) archive. This study, commonly referred to as a `bake off', identified that only nine algorithms performed significantly better than the Dynamic Time Warping (DTW) and Rotation Forest benchmarks that were used. The study categorised each algorithm by the type of feature they extract from time series data, forming a taxonomy of five main algorithm types. This categorisation of algorithms alongside the provision of code and accessible results for reproducibility has helped fuel an increase in popularity of the TSC field. Over six years have passed since this bake off, the UCR archive has expanded to 112 datasets and there have been a large number of new algorithms proposed. We revisit the bake off, seeing how each of the proposed categories have advanced since the original publication, and evaluate the performance of newer algorithms against the previous best-of-category using an expanded UCR archive. We extend the taxonomy to include three new categories to reflect recent developments.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Alongside the originally proposed distance, interval, shapelet, dictionary and hybrid based algorithms, we compare newer convolution and feature based algorithms as well as deep learning approaches. We introduce 30 classification datasets either recently donated to the archive or reformatted to the TSC format, and use these to further evaluate the best performing algorithm from each category. Overall, we find that two recently proposed algorithms, Hydra+MultiROCKET and HIVE-COTEv2, perform significantly better than other approaches on both the current and new TSC problems.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

Time series classification (TSC) involves fitting a model from a continuous, ordered sequence of real valued observations (a time series) to a discrete response variable. Time series can be univariate (a single variable observed at each time point) or multivariate (multiple variables observed at each time point). For example, we could treat raw audio signals as a univariate time series in a problem such as classifying whale species from their calls and motion tracking co-ordinate data could be a three-dimensional multivariate time series in a human activity recognition (HAR) task. Where relevant, we distinguish between univariate time series classification (UTSC) and multivariate time series classification (MTSC). The ordering of the series does not have to be in time: we could transform audio into the frequency domain using a discrete Fourier transform or map one dimensional image outlines onto a one dimensional series using radial or linear scanning. Hence, some researchers refer to TSC as data series classification. We retain the term TSC for continuity with past research.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

TSC problems arise in a wide variety of domains. Popular TSC archives^11^1 contain classification problems using: electroencephalograms; electrocardiograms; HAR and other motion data; image outlines; spectrograms; light curves; audio; traffic and pedestrian levels; electricity usage; electrical penetration graph; lightning tracking; hemodynamics; and simulated data. The huge variation in problem domains characterises TSC research. The initial question when comparing algorithms for TSC is whether we can draw any indicative conclusions on performance across a wide range of problems without any prior knowledge as to the underlying common structure of the data. An experimental evaluation of time series classification algorithms, which we henceforth refer to as the bake off, was conducted in 2016 and published in 2017. This bake off, coupled with a relaunch of time series classification archives, has helped increase the interest in TSC algorithms and applications. Our aim is to summarise the significant developments since 2017. A new MTSC archive has helped promote research in this field. A variety of new algorithms using different representations, including deep learners, convolution based algorithms and hierarchical meta ensembles, have been proposed for TSC.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

Furthermore, the growth in popularity of TSC open source toolkits such as aeon^22^2 and tslearn^33^3 have made comparison and reproduction easier. We extend and encompass recent experimental evaluations (e.g.) to provide insights into the current state of the art in the field and highlight future directions. Our target audience is both researchers interested in extending TSC research and practitioners who have TSC problems. Our contributions can be summarised as follows: We describe a range of new algorithms for TSC and place them in the context of those described in the bake off.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

We compare performance of the new algorithms on the current UCR archive datasets in a univariate classification bake off redux.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Introduction", "weight": 1.5} -->

We release $30$ new univariate datasets donated by various researchers through the TSC GitHub repository and compare the best in category on these new datasets.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Introduction", "weight": 1.5} -->

We analyse the factors that drive performance and discuss the merits of different approaches.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Introduction", "weight": 1.5} -->

To select algorithms, we use the same criteria as the bake off. Firstly, the algorithm must have been published post bake off in a high quality conference or journal (or be an extension of such an algorithm). Secondly, it must have been evaluated on one of the UCR/UEA dataset releases, or on a subset thereof, with reasoning provided for any datasets that are missing. Thirdly, source code must be available and easily adaptable to the time series machine learning tools we use (i.e. usable or easily wrappable in a Java or Python environment). Further explanation on our tools and reproducing our experiments is available in Appendix A. We describe many algorithms which inevitably leads to many acronyms and possible naming confusion. We direct the reader to Table 21 for a summary of the algorithms used and the associated reference. Section 2 describes the core terminology relating to TSC. Section 3 summarises how we conduct experimental evaluations of classifiers. We describe the latest TSC algorithms included in this bake off in Section 4. This section also describes the first set of experiments that link to the previous bake off: for each category of algorithms we compare the latest classifiers with the best in class.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Introduction", "weight": 1.5} -->

Section 5 extends the experimental evaluation to include the new datasets. Section 6 investigates variation in performance in more detail. Finally, we conclude and discuss future direction in Section 7.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Definitions and Terminology", "weight": 1.0} -->

We define the number of time series in a collection as $n$, the number of channels/dimensions of any observation as $d$ and length of a series as $m$.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Experimental Procedure", "weight": 1.0} -->

The bake off conducted experiments with the 85 UTSC datasets that were in the UCR archive relaunch of 2015. Each dataset was resampled 100 times for training and testing, and test accuracy was averaged over resamples. The evaluation began with 11 standard classifiers (such as Random Forest ), then classifiers in each category were compared, including an evaluation of reproducibility. Finally, the best in class were compared to hybrids (combinations of categories).

<!-- chunk {"id": "body-0014", "role": "body", "section": "Experimental Procedure", "weight": 1.0} -->

We adapt this approach for the bake off redux to reflect the progression of the field. First, we take the previously used benchmark of Dynamic Time Warping using a one nearest neighbour classifier (1-NN DTW) and, if appropriate, the best of each category from the bake off and compare them to new algorithms of that type. We do this stage of experimentation with the 112 equal length problems in the 2019 version of the UCR archive. Performance on these datasets, or some subset thereof, has been used to support every proposed approach, so this allows us to make a fair comparison of algorithms. We have regenerated all results for classifiers described both in the original bake off and this comparison.

<!-- chunk {"id": "body-0015", "role": "body", "section": "Experimental Procedure", "weight": 1.0} -->

Only a subset of the algorithms considered have been adapted for MTSC by their inventors. Furthermore, many algorithms have been proposed solely for MTSC, particularly in the deep learning field. Because of this and the considerable computational cost of including multivariate data, we restrict our attention to univariate classification only in this work.

<!-- chunk {"id": "body-0016", "role": "body", "section": "Experimental Procedure", "weight": 1.0} -->

We resample each pair of train/test data $30$ times for the redux, stratifying to retain the same class distribution. We do not adopt the bake off strategy of 100 resamples. We have found 30 resamples is sufficient to mitigate small changes in test accuracy over influencing ranks, and it is more computationally feasible. Resampling is seeded with the resample ID to aid with reproducibility. Resample 0 uses the original train and test split from the UCR archive.

<!-- chunk {"id": "body-0017", "role": "body", "section": "Experimental Procedure", "weight": 1.0} -->

Our primary performance measure is classification accuracy on the test set. We also compare predictive power with the balanced test set accuracy, to identify whether class imbalance is a problem for an algorithm. The quality of the probability estimates is measured with the negative log likelihood (NLL), also known as log loss. The ability to rank predictions is estimated by the area under the receiver operator characteristic curve (AUROC). For problems with two classes, we treat the minority class as a positive outcome. For multiclass problems, we calculate the AUROC for each class and weight it by the class frequency in the train data, as recommended. We present results with diagrams derived from the critical difference plots proposed. We average ranks over all datasets and plot them on a line and group classifiers into cliques, within which there is no significant difference in rank. We replace the post-hoc Nemenyi test used to form cliques described in with a mechanism built on pairwise tests. We perform pairwise one-sided Wilcoxon signed-rank tests and form cliques using the Holm correction for multiple testing as described.

<!-- chunk {"id": "body-0018", "role": "body", "section": "Experimental Procedure", "weight": 1.0} -->

Critical difference diagrams can be deceptive: they do not display the effective amount of differences, and the linear nature of clique finding can mask relationships between results. If, for example, three classifiers $A,B,C$ are ordered by rank $A > B > C$, and the test indicates $A$ is significantly better than $B$, and $B$ is significantly better than $C$, then we will form no cliques. However, it is entirely possible that $A$ is not significantly different to $C$, and the diagram cannot display this. Because of this, we expand our results to include pairwise plots, violin plots of accuracy distributions against a base line, tables of test accuracies and heatmap diagrams which include unadjusted p-values.

<!-- chunk {"id": "body-0019", "role": "body", "section": "New Datasets", "weight": 1.0} -->

The 112 equal length TSC problems in the archive constitute a relatively large corpus of problems for comparing classifiers. However, they have been extensively used in algorithm development, and there is always the risk of an implicit overfitting resulting in conclusions that do not generalise well to new problems. Hence, we have gathered new datasets which we use to perform our final comparison of algorithms. These data come from direct donation to the TSC GitHub repository^44^4 discretised regression datasets^55^5 a project on audio classification and reformatting current datasets with unequal length or missing values. Submissions of new datasets to the associated repository are welcomed.

<!-- chunk {"id": "body-0020", "role": "body", "section": "New Datasets", "weight": 1.0} -->

In total, we have gathered 30 new datasets, summarised in Table 1 and visualised in Figure 2. Datasets with the suffix \_eq are unequal length series made equal length through padding with the series mean perturbed by low level Gaussian noise. 11 of these problems (AllGestureWiimote versions, GestureMidAirD1, GesturePebbleZ, PickupGestureWiimoteZ, PLAID and ShakeGestureWiimoteZ) are already in the archive so need no further explanation.

<!-- chunk {"id": "body-0021", "role": "body", "section": "New Datasets", "weight": 1.0} -->

Covid3Month_disc Table 1: A summary of the 30 new univariate datasets used in our experiments with suffix: _eq, _nmv, _disc Figure 2: The 30 new univariate datasets showing one representative series for each class.

<!-- chunk {"id": "body-0022", "role": "body", "section": "New Datasets", "weight": 1.0} -->

Four problems with the suffix \_nmv (no missing values) are datasets where the original contains missing values. These are also from the current archive. We have used the simplest method for processing the data, and removed any cases which contain missing values for these problems (DodgerLoop variants and MelbournePedestrian). The number of cases removed per dataset amounts to 5-15% of the original size for all four datasets which we deemed acceptable. While there have been imputation methods proposed for time series, the amount of missing values present and their pattern varies. The DodgerLoop datasets have large strings of missing values, while MelbournePedestrian has singular values or small groupings of missing data.

<!-- chunk {"id": "body-0023", "role": "body", "section": "New Datasets", "weight": 1.0} -->

The four datasets ending with \_disc are taken from the TSER archive. The continuous response variable was discretised manually for each dataset, the original continuous labels and new class values for each dataset are shown in Figure 3. Both Covid3Month and FloodModeling2 had a minimum label value with many cases. For both of these, this minimum label value has been converted into its own class label. For problems where there are no obvious places where the label can be separated into classes by value (including Covid3Month where the value is greater than 0), a split point was manually selected taking into account the average label value and the number of cases in each class for a splitting point.

<!-- chunk {"id": "body-0024", "role": "body", "section": "New Datasets", "weight": 1.0} -->

This leaves 11 datasets that are completely new to the archive. The two AconityMINIPrinter data sets are described in and donated by the authors of that paper. The data comes from the AconityMINI 3D printer during the manufacturing of stainless steel blocks with a designed cavity. The problem is to predict whether there is a void in the output of the printer. The time series are temperature data that comes from pyrometers that monitor melt pool temperature. The pyrometers track the scan of the laser to provide a time-series sampled at 100 Hz. The data is sampled from the mid-section of these blocks and is organized into two datasets (large and small). The large dataset covers cubes with large pores (0.4 mm, 0.5 mm, and 0.6 mm) and the small dataset covers cubes with small pores (0.05 mm and 0.1 mm).

<!-- chunk {"id": "body-0025", "role": "body", "section": "New Datasets", "weight": 1.0} -->

The three Asphalt datasets were originally described in and donated by the author of that paper. Accelerometer data was collected on a smartphone installed inside a vehicle using a flexible suction holder near the dashboard. The acceleration forces are given by the accelerometer sensor of the device and are the data used for the classification task. The class values for AsphaltObstacles classes are four common obstacles in the region of data collection: raised cross walk (160 cases); raised markers (187 cases); speed bump (212 cases); and vertical patch (222 cases); flexible pavement (816 cases); cobblestone street (527 cases); and dirt road (768 cases). AsphaltRegularity is a two class problem: Regular (762 cases), where the asphalt is even and the driver's comfort changes little over time; and Deteriorated (740 cases), where irregularities and unevenness in a damaged road surface are responsible for transmitting vibrations to the interior of the vehicle and affecting the driver's comfort.

<!-- chunk {"id": "body-0026", "role": "body", "section": "New Datasets", "weight": 1.0} -->

The Colposcopy data is described in and was donated to the repository by the authors^66^6 The task is to classify the nature of a diagnosis from a colposcopy. The time series represent the change in intensity values of a pixel region through a sequence of digital colposcopic images obtained during the colposcopy test that was performed on each patient included in the study.

<!-- chunk {"id": "body-0027", "role": "body", "section": "New Datasets", "weight": 1.0} -->

The ElectricDeviceDetection data set contains formatted image data for the problem of detecting whether a segment of a 3-D X-Ray contains an electric device or not. The data originates from an unsupervised segmentation of 3-D X-Rays. The data are histograms of intensities, not time series.

<!-- chunk {"id": "body-0028", "role": "body", "section": "New Datasets", "weight": 1.0} -->

KeplerLightCurves was described in and donated by the authors. Each case is a light curve (brightness of an object sampled over time) from NASA's Kepler mission (3-month-long series, sampled every 30 min). There are seven classes relating to the nature of the observed star.

<!-- chunk {"id": "body-0029", "role": "body", "section": "New Datasets", "weight": 1.0} -->

The SharePriceIncrease data was formatted by Vladislavs Pazenuks as part of their 2018 undergraduate student project. The problem is to predict whether a share price will show an exceptional rise after quarterly announcement of the Earning Per Share based on the price movement of that share price on the preceding 60 days. Daily price data on NASDAQ 100 companies was extracted from a Kaggle data set^77^7 Each data represents the percentage change of the closing price from the day before. Each case is a series of 60 days data. The target class is defined as $0$ if the price did not increase after company report release by more than five percent or $1$ else-wise.

<!-- chunk {"id": "body-0030", "role": "body", "section": "New Datasets", "weight": 1.0} -->

PhoneHeartbeatSound and Tools are audio datasets. Tools contains the sound of a chainsaw, drill, hammer, horn and sword, with the task being to match which tool the audio belongs to. PhoneHeartbeatSound contains sounds of the heartbeats recorded on a phone using a digital stethoscope gathered for the 2011 PASCAL classifying heart sounds challenge^88^8 The time series represent the change in amplitude over time during an examination of patients suffering from common arrhythmias. The classes are Artifact (40 cases), ExtraStole (46 cases), Murmur (129 cases), Normal (351 cases) and ExtraHLS (40 cases).

<!-- chunk {"id": "body-0031", "role": "body", "section": "Reproducibility", "weight": 1.0} -->

The majority of the classifiers described are available in the aeon time series machine learning toolkit (see Footnote 2) and all datasets are available for download (see Footnote 1). Appendix A gives detailed code examples on how to reproduce these experiments, including parameters used, if they differ from the default. All results are available from the TSC website and can be directly loaded from there using aeon. Further guidance on reproducibility, parameterisation of the algorithms used in our experiments and our results files are available in an accompanying webpage^99^9 With the exception of three algorithms which only meet our usage criteria with a Java implementation, all the algorithms used in our experiments are runnable using the Python software and guides linked in the webpage.

<!-- chunk {"id": "body-0032", "role": "body", "section": "Time Series Classification Algorithms", "weight": 1.0} -->

The bake off introduced a taxonomy of algorithms based on the representation of the data at the heart of the algorithm. TSC algorithms were classified as either whole series, interval based, shapelet based, dictionary based, combinations or model based. We extend and refine this taxonomy to reflect recent developments.

<!-- chunk {"id": "body-0033", "role": "body", "section": "Time Series Classification Algorithms", "weight": 1.0} -->

Distance based: classification is based on some time series specific distance measure between whole series (Section 4.1).

<!-- chunk {"id": "body-0034", "role": "body", "section": "Time Series Classification Algorithms", "weight": 1.0} -->

Feature based: global features are extracted and passed to a standard classifier in a simple pipeline (Section 4.2).

<!-- chunk {"id": "body-0035", "role": "body", "section": "Time Series Classification Algorithms", "weight": 1.0} -->

Interval based: features are derived from selected phase dependent intervals in an ensemble of pipelines (Section 4.3).

<!-- chunk {"id": "body-0036", "role": "body", "section": "Time Series Classification Algorithms", "weight": 1.0} -->

Shapelet based: phase independent discriminatory subseries form the basis for classification (Section 4.4).

<!-- chunk {"id": "body-0037", "role": "body", "section": "Time Series Classification Algorithms", "weight": 1.0} -->

Dictionary based: histograms of counts of repeating patterns are the features for a classifier (Section 4.5).

<!-- chunk {"id": "body-0038", "role": "body", "section": "Time Series Classification Algorithms", "weight": 1.0} -->

Convolution based: convolutions and pooling operations create the feature space for classification (Section 4.6).

<!-- chunk {"id": "body-0039", "role": "body", "section": "Time Series Classification Algorithms", "weight": 1.0} -->

Deep learning based: neural network based classification (Section 4.7).

<!-- chunk {"id": "body-0040", "role": "body", "section": "Time Series Classification Algorithms", "weight": 1.0} -->

Hybrid approaches combine two or more of the above approaches (Section 4.8).

<!-- chunk {"id": "body-0041", "role": "body", "section": "Time Series Classification Algorithms", "weight": 1.0} -->

As well as the type of feature extracted, another defining characteristic is the design of the TSC algorithm. The simplest design pattern involves single pipelines where transformation of the series into discriminatory features is followed by the application of a standard machine learning classifier. These algorithms tend to involve an over-production and selection strategy: a large number of features are created, and the classifier determines which features are most useful. The transform can remove time dependency, e.g. by calculating summary features. We call this type series-to-vector transformations. Alternatively, they may be series-to-series, transforming into an alternative time series representation where we hope the task becomes more easily tractable, e.g. transforming to the frequency domain of the series.

<!-- chunk {"id": "body-0042", "role": "body", "section": "Time Series Classification Algorithms", "weight": 1.0} -->

The second transformation based design pattern involves ensembles of pipelines, where each base pipeline consists of making repeated, different, transforms and using a homogeneous base classifier. TSC ensembles can also be heterogeneous, collating the classifications from transformation pipelines and ensembles of differing representations of the time series.

<!-- chunk {"id": "body-0043", "role": "body", "section": "Time Series Classification Algorithms", "weight": 1.0} -->

The third common pattern involves transformations embedded inside a classifier structure. For example, a decision tree where the data is transformed at each node fits this pattern.

<!-- chunk {"id": "body-0044", "role": "body", "section": "Time Series Classification Algorithms", "weight": 1.0} -->

A common theme to all categories of algorithm is ensembling. Another popular method seen in multiple classifiers are transformation pipelines ending with a linear classifier. The most accurate classifiers we find all form homogeneous or heterogeneous ensembles, or extract features prior to a linear ridge classifier.

<!-- chunk {"id": "body-0045", "role": "body", "section": "Time Series Classification Algorithms", "weight": 1.0} -->

To try and capture the commonality and differences between algorithms we provide a Table in the Appendix B (Table 22) that groups algorithms by whether they employ the following design characteristics: dilation; discretisation; differences/derivatives; frequency domain; ensemble; and linear classification.

<!-- chunk {"id": "body-0046", "role": "body", "section": "Time Series Classification Algorithms", "weight": 1.0} -->

We review each category of algorithms by providing an overview of the approach, review selected classifiers and describe the pattern they use, starting with the best of class from the bake off. We perform a comparison of performance within category on the 112 equal length UTSC problems currently in the UCR archive using 1-NN DTW as a benchmark. More detailed evaluation is delayed until Section 5.

<!-- chunk {"id": "body-0047", "role": "body", "section": "Distance Based", "weight": 1.0} -->

Distance based classifiers use a distance function to measure the similarity between whole time series. Historically, distance functions have been mostly used with nearest neighbour (NN) classifiers. Alternative uses of time series distances are described. Prior to the bake off, 1-NN with DTW was considered state of the art for TSC. Figure 5 shows an example of how DTW attempts to align two series, depicted in red and green, to minimise their distance.

<!-- chunk {"id": "body-0048", "role": "body", "section": "Distance Based", "weight": 1.0} -->

In addition to DTW, a wide range of alternative elastic distance measures (distance measures that compensate for possible misalignment between series) have been proposed. These use combinations of warping and editing on series and the derivatives of series. See for an overview of elastic distances. Previous studies have shown there is little difference in performance between 1-NN classifiers with different elastic distances.

<!-- chunk {"id": "body-0049", "role": "body", "section": "Distance Based", "weight": 1.0} -->

The flowchart in Figure 6 visualises the distance based algorithms described in this section and the relation between them. Algorithms following another are not necessarily better than the predecessor, but are either direct extensions or heavily draw inspiration from it.

<!-- chunk {"id": "body-0050", "role": "body", "section": "Elastic Ensemble (EE)", "weight": 1.0} -->

The first algorithm to significantly outperform 1-NN DTW on the UCR data was the Elastic Ensemble (EE). EE is a weighted ensemble of 11 1-NN classifiers with a range of elastic distance measures. It was the best performing distance based classifier in the bake off. Elastic distances can be slow, and EE requires cross validation to find the weights of each classifier in the ensemble. A caching mechanism was proposed to help speed up fitting the classifier and alternative speed ups were described. The latter speed up is the version of EE we use in our experiments.

<!-- chunk {"id": "body-0051", "role": "body", "section": "Proximity Forest (PF)", "weight": 1.0} -->

Proximity Forest (PF) is an ensemble of Proximity Tree based classifiers. PF uses the same $11$ distance functions used by EE, but is more accurate and more scalable than the original EE algorithm. At every node of a tree, one of the 11 distances is selected to be applied with a fixed hyperparameter value. An exemplar single series is selected randomly for each class label. At every node, $r$ combinations of distance function, parameter value and class exemplars are randomly selected, and the combination with the highest Gini index split measure is selected. Series are passed down the branch with the exemplar that has the lowest distance to it, and the tree grows recursively until a node is pure.

<!-- chunk {"id": "body-0052", "role": "body", "section": "ShapeDTW", "weight": 1.0} -->

Shape based DTW (ShapeDTW) works by extracting a set of shape descriptors over sliding windows of each series. The descriptors include slope, wavelet transforms and piecewise approximations. Based on the results presented we use the raw and derivative subsequences. The output data of these series-to-series transformations is then used with a 1-NN classifier with DTW.

<!-- chunk {"id": "body-0053", "role": "body", "section": "Generic RepresentAtIon Learning (GRAIL)", "weight": 1.0} -->

The Generic RepresentAtIon Learning (GRAIL) paper focuses on efficient learning of time series representations that uphold bespoke distance function constraints. GRAIL harnesses kernel methods, particularly the Nyström method, to learn precise representations within these constraints. The construction of representations involves expressing each time series as a linear combination of expressive landmarks, identified through cluster centroids. This approach gives rise to the Shift-Invariant Kernel (SINK) kernel function, which employs the Fast Fourier Transform to compare time series under shift invariance. GRAIL can be used to multiple time series related tasks, but for classification GRAIL and the SINK kernel are evaluated using a linear SVM.

<!-- chunk {"id": "body-0054", "role": "body", "section": "Comparison of Distance Based Approaches", "weight": 1.0} -->

Table 2 shows PF is over 2.5% better in test accuracy and balanced test accuracy, has higher AUROC and lower NLL. Hence, we take PF as best of the distance based category.

<!-- chunk {"id": "body-0055", "role": "body", "section": "Feature Based", "weight": 1.0} -->

*Feature based* classifiers are a popular recent theme. These extract descriptive statistics as features from time series to be used in classifiers. Typically, these features summarise the whole series, so we characterise these as series-to-vector transforms. Most commonly, these features are used in a simple pipeline of transformation followed by a classifier (see Figure 8). Several toolkits exist for extracting features.

<!-- chunk {"id": "body-0056", "role": "body", "section": "Feature Based", "weight": 1.0} -->

The flowchart in Figure 9 displays the feature based algorithms described in this section and related algorithms.

<!-- chunk {"id": "body-0057", "role": "body", "section": "The Canonical Time Series Characteristics", "weight": 1.0} -->

The highly comparative time-series analysis (hctsa) toolbox can create over $7700$ features for exploratory time series analysis. The canonical time series characteristics are $22$ hctsa features determined to be the most discriminatory of the full set. The features were chosen by an evaluation on the UCR datasets. The hctsa features were initially pruned, removing those which are sensitive to the series mean and variance and those that could not be calculated on over $80\%$ of the UCR datasets. A feature evaluation was then performed based on predictive performance. Any features which performed below a threshold were removed. For the remaining features, a hierarchical clustering was performed on the correlation matrix to remove redundancy. From each of the 22 clusters formed, a single feature was selected, taking into account balanced accuracy, computational efficiency and interpretability. The features cover a wide range of concepts such as basic statistics of time series values, linear correlations, and entropy. Reported results for are based on training a decision tree classifier after applying the transform to each time series, the implementation we use builds a Random Forest classifier.

<!-- chunk {"id": "body-0058", "role": "body", "section": "Time Series Feature Extraction based on Scalable Hypothesis Tests (TSFresh)", "weight": 1.0} -->

TSFresh is a collection of just under 800 features extracted from time series. While the features can be used on their own, a feature selection method called FRESH is provided to remove irrelevant features. FRESH considered each feature using multiple hypotheses tests, including Fisher's exact test, the Kolmogorov-Smirnov test and the Kendal rank test. The Benjamini-Yekutieli procedure is then used to control the false discovery rate caused by comparing multiple hypotheses and features simultaneously.

<!-- chunk {"id": "body-0059", "role": "body", "section": "Time Series Feature Extraction based on Scalable Hypothesis Tests (TSFresh)", "weight": 1.0} -->

Results for the base features and after using the FRESH algorithm are reported using both a Random Forest and AdaBoost classifier. A comparison of alternative pipelines of feature extractor and classifier found that the most effective approach was the full set of TSFresh features with no feature selection applied, and combined with a Rotation Forest classifier. This pipeline was called the FreshPRINCE. We include both TSFresh with feature selection using a Random Forest and the FreshPRINCE classifier in our comparison.

<!-- chunk {"id": "body-0060", "role": "body", "section": "Generalised Signatures", "weight": 1.0} -->

Generalised signatures are a set of feature extraction techniques based on rough path theory. The generalised signature method and the accompanying canonical signature pipeline can be used as a transformation for classification. Signatures are collections of ordered cross-moments. The pipeline begins by applying two augmentations. The basepoint augmentation simply adds a zero at the beginning of the time series, making the signature sensitive to translations of the time series. The time augmentation adds the series timestamps as an extra coordinate to guarantee that each signature is unique and obtain information about the parameterisation of the time series. A hierarchical window is run over the two augmented series, with the signature transform being applied to each window. The output for each window is then concatenated into a feature vector. The features are used to build a Random Forest classifier. The transformation was primarily developed for MTSC, but can be applied to univariate series.

<!-- chunk {"id": "body-0061", "role": "body", "section": "Interval Based", "weight": 1.0} -->

Interval based classifiers extract phase dependent intervals of fixed offsets and compute (summary) statistics on these intervals. A majority of approaches include some form of random selection for choosing intervals, where the same random interval locations are used across every series. Many of the interval based classifiers combine features from multiple random intervals. The motivation for taking intervals is to mitigate for confounding noise. Figure 11 shows an example problem where taking intervals will be better than using features derived from the whole series.

<!-- chunk {"id": "body-0062", "role": "body", "section": "Interval Based", "weight": 1.0} -->

Most recent interval based classifiers adopt a random forest ensemble model, where each base classifier is a pipeline of transformation and a tree classifier (visualised in Figure 12). Diversity is injected through randomising the intervals for each tree. The relation flowchart for interval based algorithms is shown in Figure 13.

<!-- chunk {"id": "body-0063", "role": "body", "section": "Time Series Forest (TSF)", "weight": 1.0} -->

The Time Series Forest (TSF) is the simplest interval based tree based ensemble. For each tree, $\sqrt{m}$ (following the notation from Chapter 2, where $m$ is the length of the series and $d$ is the number of dimensions) intervals are selected with a random position and length. The same interval offsets are applied to all series. For each interval, three summary statistics (the mean, variance and slope) are extracted and concatenated into a feature vector. This feature vector is used to build the tree, and features extracted from the same intervals are used to make predictions. The ensemble makes the prediction using a majority vote of base classifiers. The TSF base classifier is a modified decision tree classifier referred to as a time series tree, which considers all attributes at each node and uses a metric called margin gain to break ties.

<!-- chunk {"id": "body-0064", "role": "body", "section": "Random Interval Spectral Ensemble (RISE)", "weight": 1.0} -->

First developed for the HIVE-COTE ensemble (described in Section 4.8), the Random Interval Spectral Ensemble (RISE) is an interval based tree ensemble that uses spectral features. Unlike TSF, RISE selects a single random interval for each base classifier. The periodogram and auto-regression function are calculated over each randomly selected interval, and these features are concatenated into a feature vector, from which a tree is built. RISE was primarily designed for use with audio problems, where spectral features are more likely to be discriminatory.

<!-- chunk {"id": "body-0065", "role": "body", "section": "STSF and R-STSF", "weight": 1.0} -->

Supervised Time Series Forest (STSF) is an interval based tree ensemble that includes a supervised method for extracting intervals. Intervals are found and extracted for a periodogram and the first order differences representation as well as the base series. STSF introduces bagging for each tree and extracts seven simple summary statistics from each interval. For each tree, an initial split point for the series is randomly selected. For both of these splits, the remaining subseries is cut in half, and the half with the higher Fisher score is retained as an interval. This process is then run recursively using higher scored intervals until the series is smaller than a threshold. This is repeated for each of the seven summary statistic features, with the extracted statistic being used to calculate the Fisher score.

<!-- chunk {"id": "body-0066", "role": "body", "section": "STSF and R-STSF", "weight": 1.0} -->

Randomised STSF (RSTSF) is an extension of STSF, altering its components with more randomised elements. The split points for interval selection are selected randomly instead of splitting each candidate in half after the first. Intervals extracted from an autoregressive representation are included alongside the previous additions. Features are extracted multiple times from each representation into a single pool. Rather than extract different features for each tree in an ensemble, the features are used in a pipeline to build an Extra Trees classifier.

<!-- chunk {"id": "body-0067", "role": "body", "section": "CIF and DrCIF", "weight": 1.0} -->

The Canonical Interval Forest (CIF) is another extension of TSF, that improves accuracy by integrating more informative features and by increasing diversity. Like other interval approaches, CIF is an ensemble of decision tree classifiers built on features extracted from phase dependent intervals. Alongside the mean, standard deviation and slope, CIF also extracts the features described in Section 4.2. Intervals remain randomly generated, with each tree selecting $k = {\sqrt{m}\sqrt{d}}$ intervals. To add additional diversity to the ensemble, $a$ attributes out of the pool of $25$ are randomly selected for each tree. The extracted features are concatenated into a $k \cdot a$ length vector for each time series and used to build the tree. For multivariate data, CIF randomly selects the dimension used for each interval.

<!-- chunk {"id": "body-0068", "role": "body", "section": "CIF and DrCIF", "weight": 1.0} -->

The Diverse Representation Canonical Interval Forest (DrCIF) incorporates two new series representations: the periodograms (also used by RISE and STSF) and first order differences (also used by STSF). For each of the three representations, ${({4 + {\sqrt{r}\sqrt{d}}})}/3$ phase dependent intervals are randomly selected and concatenated into a feature vector, where $r$ is the length of the series for a representation.

<!-- chunk {"id": "body-0069", "role": "body", "section": "QUANT", "weight": 1.0} -->

QUANT employs a singular feature type, quantiles, to encapsulate the distribution of a given time series. The method combines four distinct representations, namely raw time series, first-order differences, Fourier coefficients, and second-order differences. The extraction process involves fixed, dyadic intervals derived from the time series. These disjoint intervals are constructed through a pyramid structure, where each level successively halves the interval length. At depths greater than one, an identical set of intervals, shifted by half the interval length, is also included. The total count of intervals is calculated as ${2^{({d - 1})} \times 4} - 2 - d$ for a depth of $d = {\min{(6,{{\log_{2}n} + 1})}}$. Each representation can have up to $120$ intervals, resulting in a total of $480$ intervals across all four representations. The concatenated feature vector is used to build an Extra Trees classifier.

<!-- chunk {"id": "body-0070", "role": "body", "section": "Comparison of Interval Based Approaches", "weight": 1.0} -->

There is no significant difference between QUANT, DrCIF and RSTSF nor between their precursors CIF and STSF. All are significantly better than TSF, the best in class in the bake off. Figure 15(a) shows the scatter plot of QUANT vs DrCIF. QUANT wins on $63$, draws $5$ and loses $44$. Overall, the two algorithms produce very similar results (the test accuracies have a correlation of $98.1\%$).

<!-- chunk {"id": "body-0071", "role": "body", "section": "Comparison of Interval Based Approaches", "weight": 1.0} -->

We choose QUANT as the best in class because it is significantly faster than DrCIF and RSTSF. Figure 15(b) shows QUANT against TSF in order to confirm that QUANT, DrCIF and RSTSF represent genuine improvements to this type of algorithm over the previous best. Table 4 confirms that on average over 112 problems, the accuracy of the top clique is over $0.06$ higher than TSF.

<!-- chunk {"id": "body-0072", "role": "body", "section": "Shapelet Based", "weight": 1.0} -->

*Shapelets* are subseries from the training data that are independent of the phase and can be used to discriminate between classes of time series based on their presence or absence. To evaluate a shapelet, the subseries is slid across the time series, and the z-normalised Euclidean distance between the shapelet and the underlying window is calculated. The distance between a shapelet and any series, $sDist{}$, is the minimum distance over all such windows. Figure 16 shows a visualisation of the $sDist{}$ process. The shapelet $S$ is shifted along the time series $A$, and the most similar offset and distance in $A$ are recorded. The distance between a shapelet and the training series is then used as a feature to evaluate the quality of the shapelet.

<!-- chunk {"id": "body-0073", "role": "body", "section": "Shapelet Based", "weight": 1.0} -->

Shapelets were first proposed as a primitive, and were embedded in a decision tree classifier. There have been four important themes in shapelet research post bake off: The first has concentrated on finding the best way to use shapelets to maximise classification accuracy. The second has focused on overcoming the shortcomings of the original shapelet discovery which required full enumeration of the search space and has cubic complexity in the time series length; the third theme is the progress toward unifying research with convolutions and shapelets; and the fourth theme is the balance between optimisation, randomisation and interpretability when finding shapelets. The relation flowchart for shapelet based algorithms is shown in Figure 17.

<!-- chunk {"id": "body-0074", "role": "body", "section": "The Shapelet Transform Classifier (STC)", "weight": 1.0} -->

The Shapelet Transform Classifier (STC) is a pipeline classifier which searches the training data for shapelets, transforms series to vectors of $sDist{}$ distances to a filtered set of selected shapelets based on information gain, then builds a classifier on the latter. This is in contrast to the decision tree based approaches, which search for the best shapelet at each tree node. The first version of STC performed a full enumeration of all shapelets from all train cases before selecting the top $k$. The base classifier used was HESCA (later renamed CAWPE, ) ensemble of classifiers, a weighted heterogeneous ensemble of 8 classifiers including a diverse set of linear, tree based and Bayesian classifiers. Due to its full enumeration and large pool of base classifiers requiring weights, the algorithm does not scale well. We call the original full enumeration version ST-HESCA to differentiate it from the version described below which we simply call STC. It was the best performing shapelet based classifier in the bake off.

<!-- chunk {"id": "body-0075", "role": "body", "section": "The Shapelet Transform Classifier (STC)", "weight": 1.0} -->

The following incremental changes have been made to the STC pipeline, described: Search has been randomised, and the number of shapelets sampled is now a parameter, which defaults to 10,000. This does not lead to significantly worse performance on the UCR datasets.

<!-- chunk {"id": "body-0076", "role": "body", "section": "The Shapelet Transform Classifier (STC)", "weight": 1.0} -->

Shapelets are now binary, in that they represent the class of the origin series and are evaluated against all other classes as a single class using one hot encoding. This facilitates greater use of the early abandon of the order line creation (described in ), and makes evaluation of split points faster.

<!-- chunk {"id": "body-0077", "role": "body", "section": "The Shapelet Transform Classifier (STC)", "weight": 1.0} -->

The heterogeneous ensemble of base classifiers in HESCA has been replaced with a single Rotation Forest classifier, making STC a simple pipeline classifier.

<!-- chunk {"id": "body-0078", "role": "body", "section": "The Generalised Random Shapelet Forest (RSF)", "weight": 1.0} -->

The Random Shapelet Forest (RSF) is a bagging based tree ensemble that attempts to improve the computational efficiency and predictive accuracy of the Shapelet Tree through randomisation and ensembling. At each node of each tree $r$ univariate shapelets are selected from the training set at random. Each shapelet has a randomly selected length between predefined upper and lower limits. The quality of a shapelets is measured in the standard way with $sDist{}$ and information gain, and the best is selected. The data is split, and a tree is recursively built until a stopping condition is met. New samples are predicted by a majority vote on the tree's predictions and multiple trees are ensembled.

<!-- chunk {"id": "body-0079", "role": "body", "section": "MrSEQL and MrSQM", "weight": 1.0} -->

The Multiple Representation Sequence Learner (MrSEQL), is an ensemble classifier that extends previous adaptations of the SEQL classifier. MrSEQL looks for the presence or absence of a pattern (shapelet) in the data. Rather than using a distance based approach to measure the presence or not of a shapelet, MrSEQL discretises subseries into words. Words are generated through two symbolic representations, using SAX for time domain and SFA for frequency domain. A set of discriminative words is selected through Sequence Learner (SEQL) and the output of training is a logistic regression model, which in concept is a vector of relevant subseries and their weights. Diversification is achieved through the two different symbolic representations and varying the window size.

<!-- chunk {"id": "body-0080", "role": "body", "section": "MrSEQL and MrSQM", "weight": 1.0} -->

MrSQM extends MrSEQL. It also combines two symbolic transformations to create words from subseries and trains a logistic regression classifier. What sets it apart is its innovative strategy for selecting features (substrings).

<!-- chunk {"id": "body-0081", "role": "body", "section": "MrSEQL and MrSQM", "weight": 1.0} -->

To begin, MrSQM uses SFA and SAX to discretise time series subseries into words. It then utilizes a trie to store and rank frequent substrings, and applies either (a) a supervised chi-squared test to identify discriminative words or (b) an unsupervised random substring sampling method to prevent overestimating highly correlated substrings that are likely to be redundant. MrSQM establishes the number of learned representations (SFA or SAX) based on the length of the time series and utilizes an exponential scale for the window size parameter.

<!-- chunk {"id": "body-0082", "role": "body", "section": "Random Dilated Shapelet Transform (RDST)", "weight": 1.0} -->

The Random Dilated Shapelet Transform (RDST) is a shapelet-based algorithm that adopts many of the techniques of convolution approaches described in Section 4.6. While traditional shapelet algorithms search for the best shapelets from the train dataset, RDST takes a different approach by randomly selecting a large number of shapelets from the train data, typically ranging from thousands to tens of thousands, then training a linear Ridge classifier on features derived from these shapelets.

<!-- chunk {"id": "body-0083", "role": "body", "section": "Random Dilated Shapelet Transform (RDST)", "weight": 1.0} -->

RDST employs dilation with shapelets. Dilation is a form of down sampling, in that it defines spaces between time points. Hence, a shapelet with dilation $d$ is compared to time points $d$ steps apart when calculating the distance. RDST also uses two features in addition to $sDist{}$: it encodes the position of the minimum distance, and records a measure of the frequency of occurrences of the shapelet based on a threshold. Hence the transformed data has $3k$ features for $k$ shapelets.

<!-- chunk {"id": "body-0084", "role": "body", "section": "Comparison of Shapelet Based Approaches", "weight": 1.0} -->

Table 5 highlights the key differences between the shapelet-based approaches. yes (SAX/SFA) Random Tree Ensemble Table 5: Key differences in shapelet based TSC algorithms.

<!-- chunk {"id": "body-0085", "role": "body", "section": "Dictionary Based", "weight": 1.0} -->

Similar to shapelet based algorithms, *dictionary approaches* extract phase-independent subseries. However, instead of measuring the distance to a subseries, each window is converted into a short sequence of discrete symbols, commonly known as a word. Dictionary methods differentiate based on word frequency and are often referred to as bag-of-words approaches. Figure 20 illustrates the process that algorithms following the dictionary model take to create a classifier. This process can be summarized as: Extracting subseries, or windows, from a time series; Transforming each window of real values into a discrete-valued *word* (a sequence of symbols over a fixed alphabet); Building a sparse feature vector of histograms of word counts, and Finally, using a classification method from the machine learning repertoire on these feature vectors.

<!-- chunk {"id": "body-0086", "role": "body", "section": "Dictionary Based", "weight": 1.0} -->

Dictionary-based methods differ in the way they transform a window of real-valued measurements into discrete words. For example, the basis of the BOSS model is a representation called Symbolic Fourier Approximation (SFA). SFA works as follows: Values in each window of length $w$ are normalized to have standard deviation of $1$ to obtain amplitude invariance.

<!-- chunk {"id": "body-0087", "role": "body", "section": "Dictionary Based", "weight": 1.0} -->

Each normalized window of length $w$ is subjected to dimensionality reduction by the use of the truncated Fourier transform, keeping only the first $l < w$ coefficients for further analysis. This step acts as a low pass filter, as higher order Fourier coefficients typically represent rapid changes like dropouts or noise.

<!-- chunk {"id": "body-0088", "role": "body", "section": "Dictionary Based", "weight": 1.0} -->

Discretisation bins are derived through Multiple Coefficient Binning (MCB). It separately records the $l$ distributions of the real and imaginary values of the Fourier transform. These distributions are then subjected to either equi-depth or equi-width binning. The resulting output consists of $l$ sets of bins, corresponding to the target word length of $l$.

<!-- chunk {"id": "body-0089", "role": "body", "section": "Dictionary Based", "weight": 1.0} -->

Each coefficient is discretized to a symbol of an alphabet of fixed size $\alpha$ to achieve further robustness against noise.

<!-- chunk {"id": "body-0090", "role": "body", "section": "Bag-of-SFA-Symbols (BOSS)", "weight": 1.0} -->

Bag-of-SFA-Symbols (BOSS) was among the top-performing algorithms in the initial bake-off study and led to significant further investigation into dictionary-based classifiers. An individual BOSS classifier undergoes the same process described earlier, whereby each sliding window is transformed into a word using SFA. Subsequently, a feature vector is generated by counting the occurrences of each word over all windows. A non-symmetric distance function is then employed with a 1-NN classifier to categorize new instances. Experiments have shown that when presented with a query and a sample time series, disregarding words that exist solely in the sample time series using, the non-symmetric distance function leads to improved performance compared to using the Euclidean distance metric.

<!-- chunk {"id": "body-0091", "role": "body", "section": "Bag-of-SFA-Symbols (BOSS)", "weight": 1.0} -->

The complete BOSS classifier is an ensemble of individual BOSS classifiers. This ensemble is created by exploring a range of parameters, assessing each base classifier through cross-validation, and keeping all base classifiers with an estimated accuracy within $92\%$ of the best classifier. For new instances, the final prediction is obtained through a majority vote of the base classifiers.

<!-- chunk {"id": "body-0092", "role": "body", "section": "Word Extraction for Time Series Classification (WEASEL v1.0)", "weight": 1.0} -->

Word Extraction for Time Series Classification (WEASEL v1.0) is a pipeline classifier that revolves around identifying words whose frequency count distinguishes between classes and discarding words that lack discriminatory power. The classifier generates histograms of word counts over a broad spectrum of window sizes and word lengths parameters, including bigram words produced from non-overlapping windows. A Chi-squared test is then applied to determine the discriminatory power of each word, and those that fall below a particular threshold are discarded through feature selection. Finally, a linear Ridge classifier is trained on the remaining feature space. WEASEL utilizes a supervised variation of SFA to create discriminative words, and it leverages an information-gain based methodology for identifying breakpoints that separate the classes.

<!-- chunk {"id": "body-0093", "role": "body", "section": "WEASEL v2.0 (with dilation)", "weight": 1.0} -->

The dictionary-based WEASEL v2.0 is a complete overhaul of the WEASEL v1.0 classifier. It addresses the problem of the extensive memory footprint of WEASEL by controlling the search space using randomly parameterized SFA transformations. It also significantly improves accuracy. Notably, the most prominent modification is the inclusion of dilation to the sliding window approach. Table 7 presents a comprehensive summary of its alterations.

<!-- chunk {"id": "body-0094", "role": "body", "section": "WEASEL v2.0 (with dilation)", "weight": 1.0} -->

To extract subseries with non-consecutive values from a time series, a dilated sliding window approach is employed, where the dilation parameter maintains a fixed gap between each value. These dilated subseries undergo a Fourier transform, and a word is generated by discretising them using SFA. The unsupervised learning of bins is achieved using equi-depth and equi-width with an alphabet size of $2$. To improve performance, a feature selection strategy based on variance is introduced, which retains only the real and imaginary Fourier values with the highest variance.

<!-- chunk {"id": "body-0095", "role": "body", "section": "WEASEL v2.0 (with dilation)", "weight": 1.0} -->

Each of the $50$ to $150$ SFA transformations is randomly initialized subject to: Window length $w$: Randomly chosen from interval $\lbrack{w_ min},\ldots,{w_ max}\rbrack$.

<!-- chunk {"id": "body-0096", "role": "body", "section": "WEASEL v2.0 (with dilation)", "weight": 1.0} -->

Dilation $d$: Randomly chosen from interval $\lbrack 1,\ldots,2^{\log{(\frac{n - 1}{w - 1})}}\rbrack$. The formula is inherited from the convolution-based ROCKET group of classifiers.

<!-- chunk {"id": "body-0097", "role": "body", "section": "WEASEL v2.0 (with dilation)", "weight": 1.0} -->

Word length $l$: Randomly chosen from $\{ 7,8\}$.

<!-- chunk {"id": "body-0098", "role": "body", "section": "WEASEL v2.0 (with dilation)", "weight": 1.0} -->

Binning strategy: Randomly chosen from {"equi-depth", "equi-width"}.

<!-- chunk {"id": "body-0099", "role": "body", "section": "WEASEL v2.0 (with dilation)", "weight": 1.0} -->

First order differences: To extract words from both, the raw time series, and its first order difference, effectively doubling the feature space.

<!-- chunk {"id": "body-0100", "role": "body", "section": "WEASEL v2.0 (with dilation)", "weight": 1.0} -->

When using an alphabet size of $2$ and a length of $8$, each SFA transformation creates a dictionary containing only $256$ unique words of a fixed size. These dictionaries are then combined to produce a feature vector containing approximately $30k$ to $70k$ features. No feature selection is implemented by default. The resulting features serve as input for training a linear Ridge classifier.

<!-- chunk {"id": "body-0101", "role": "body", "section": "Contractable BOSS (cBOSS)", "weight": 1.0} -->

The size of the parameter grid searched by BOSS is data dependent, and BOSS uses a method of retaining ensemble members using a threshold of accuracy estimated from the train data. This makes its time and memory complexity unpredictable. BOSS was one of the slower algorithms tested in the bake off and could not be evaluated on the larger datasets in reasonable time. Contractable BOSS (cBOSS) revises the ensemble structure of BOSS to solve these scalability issues, using the same base transformations as the BOSS ensemble. cBOSS randomly selects $k$ parameter sets of hyper-parameters ($w$, $l$ and $\alpha$) for BOSS base classifiers. It retains the best $s$ classifiers (based on a cross validation estimate of accuracy) are retained for the final ensemble. cBOSS allows the $k$ parameter to be replaced by a train time limit $t$ through contraction, allowing the user to better control the training time of the classifier. A subsample of the train data is randomly selected without replacement for each ensemble member and an exponential weighting scheme used in the CAWPE ensemble is introduced. The cBOSS alterations to the BOSS ensemble structure showed an order of magnitude improvement in train times with no reduction in accuracy.

<!-- chunk {"id": "body-0102", "role": "body", "section": "SpatialBOSS", "weight": 1.0} -->

BOSS intentionally ignores the locations of words in series, classifying based on the frequency of patterns rather than their location. Spatial Boss introduced location information into the design of a BOSS classifier. Spatial pyramids are a technique used in computer vision to retain some temporal information back into the bag-of-words paradigm. The core idea, illustrated in Figure 23 is to split the series into different resolutions, segmenting the series based on depth and position, then building independent histograms on the splits. The histograms for each level are concatenated into a single feature vector which is used with a 1-NN classifier. While more accurate than BOSS, the increase in parameter search space and bag size makes it very difficult to run in practice.

<!-- chunk {"id": "body-0103", "role": "body", "section": "Temporal Dictionary Ensemble (TDE)", "weight": 1.0} -->

The Temporal Dictionary Ensemble (TDE) combines the best improvements introduced in WEASEL, SpatialBOSS and cBOSS and also includes several novel features. TDE is an ensemble of 1-NN classifiers which transforms each series into a histogram of word counts using SFA. From WEASEL, TDE takes the method for finding supervised breakpoints for discretisation, and captures frequencies of bigrams found from non-overlapping windows. The locality information derived from the spatial pyramids used in SpatialBOSS are incorporated. Word counts are found for each spatial subseries independently, with the resulting histograms being concatenated. Bigrams are only found for the full series. The cBOSS ensemble structure is applied with a modified parameter space sampling algorithm. It first randomly samples a small number of parameter sets, then constructs a Gaussian processes regressor on the historic accuracy for unseen parameter sets. The regressor is used to estimate the parameter set for the next candidate, and the model is then updated before the process is repeated. TDE has two additional parameters for its candidate models: the number of levels for the spatial pyramid and the method of generating breakpoints.

<!-- chunk {"id": "body-0104", "role": "body", "section": "Comparison of Dictionary Based Approaches", "weight": 1.0} -->

Table 7 shows the key design differences between the dictionary based approaches. optional (default: None) Feature Vector Size Table 7: Key differences in dictionary based TSC algorithms Figure 24 shows the ranked test accuracy of five dictionary classifiers we have described, with 1-NN DTW as a benchmark. SpatialBOSS is not included due to its significant runtime and memory requirements which would require the exclusion of multiple datasets. We believe that comparing more recent advances on the full archive is more valuable than its inclusion, and suggest those interested in SpatialBOSS view the results presented in which show it is comparable to WEASEL 1.0 in performance. WEASEL 1.0 and TDE are significantly more accurate than BOSS, but WEASEL 2.0 is the most accurate overall. Figure 25(a) illustrates the improvement of WEASEL 2.0 over BOSS, and Figure 25(b) shows the improvement dilation provides over WEASEL. Table 8 summarises the performance of the four new dictionary algorithms. WEASEL 2.0 is on average $4\%$ more accurate than BOSS and improves balanced accuracy by almost the same amount.

<!-- chunk {"id": "body-0105", "role": "body", "section": "Convolution Based", "weight": 1.0} -->

Kernel/Convolution classifiers use convolutions with kernels, which can be seen as subseries used to derive discriminatory features. Each kernel is convolved with a time series through a sliding dot product creating an activation map. Technically, each convolution creates a series to series transform from time series to the activation map (see Definition 6). ‣ 2 Definitions and Terminology ‣ Bake off redux: a review and experimental evaluation of recent time series classification algorithms")). Activation maps are used to create summary features. Convolutions and shapelets share a close methodological relationship. Shapelets can be realised through a convolution operation, followed by a min-pooling operation on the array of windowed Euclidean distances. This was first observed. However, despite this methodological connection, there is significant difference in the results obtained by convolution based and shapelet based approach, as illustrated in the Appendix C, Figure 50. For example, the ROCKET results are negatively correlated with shapelet based approaches such as STC or RDST.

<!-- chunk {"id": "body-0106", "role": "body", "section": "Convolution Based", "weight": 1.0} -->

The main difference between convolutions and shapelets is that shapelets are subseries from the training data whereas convolutions are found from the entire space of possible real-values.

<!-- chunk {"id": "body-0107", "role": "body", "section": "Convolution Based", "weight": 1.0} -->

Convolution based TSC algorithms follow a standard pipeline pattern depicted in Figure 26. The activation map is formed for each convolution, followed by pooling operations to extract one relevant feature for each operation. The resulting features are then concatenated to form a single feature vector. Finally, a Ridge classifier is trained on the output to classify the data. The relation flowchart for convolution based algorithms is shown in Figure 27.

<!-- chunk {"id": "body-0108", "role": "body", "section": "Random Convolutional Kernel Transform (ROCKET)", "weight": 1.0} -->

The most well known convolutional approach is the Random Convolutional Kernel Transform (ROCKET). ROCKET is a pipeline classifier. It generates a large number of randomly parameterised convolutional kernels (typically in the range of thousands to tens of thousands), then uses these to transform the data through two pooling operations: the max value and the proportion of positive values (PPV). These two features are concatenated into a feature vector for all kernels. For $k$ kernels, the transformed data has $2k$ features.

<!-- chunk {"id": "body-0109", "role": "body", "section": "Random Convolutional Kernel Transform (ROCKET)", "weight": 1.0} -->

In ROCKET, each kernel is randomly initialised with respect to the following parameters: the *kernel length $l$*, randomly selected from $\{ 7,9,11\}$; the *kernel weights $w$*, randomly initialised from a normal distribution; a *bias term $b$* added to the result of the convolution operation; the *dilation $d$* to define the spread of the kernel weights over the input instance, which allows for detecting patterns at different frequencies and scales. The dilation is randomly drawn from an exponential function; and padding *$p$* the input series at the start and the end (typically with zeros), such that the activation map has the same length as the input; The result of applying a kernel $\omega$ with dilation $d$ to a time series $T$ at offset $i$ is defined: The feature vectors are then used to train a Ridge classifier using cross-validation to train the $L_{2}$-regularisation parameter $\alpha$. A Logistic Regression classifier is suggested as a replacement for larger datasets.

<!-- chunk {"id": "body-0110", "role": "body", "section": "Random Convolutional Kernel Transform (ROCKET)", "weight": 1.0} -->

The combination of ROCKET with Logistic (RIDGE) Regression is conceptually the same as a single-layer Convolutional Neural Network with randomly initialised kernels and softmax loss.

<!-- chunk {"id": "body-0111", "role": "body", "section": "Mini-ROCKET and Multi-ROCKET", "weight": 1.0} -->

ROCKET has two extensions. The first extension is MiniROCKET, which speeds up ROCKET by over an order of magnitude with no significant difference in accuracy. MiniROCKET removes many of the random components of ROCKET, making the classifier almost deterministic. The kernel length is fixed to 9, only two weight values are used, and the bias value is drawn from the convolution output. Only the PPV is extracted, discarding the max. These changes alongside general optimisations taking advantage of the new fixed values provide a considerable speed-up to the algorithm. MiniROCKET generates a total of 10k features from 10k kernels and PPV pooling.

<!-- chunk {"id": "body-0112", "role": "body", "section": "Mini-ROCKET and Multi-ROCKET", "weight": 1.0} -->

MultiROCKET further extends the MiniROCKET improvements, extracting features from first order differences and adding three new pooling operations extracted from each kernel: mean of positive values (MPV), mean of indices of positive values (MIPV) and longest stretch of positive values (LSPV). MultiROCKET generates a total of 50k features from 10k kernels and 5 pooling operations.

<!-- chunk {"id": "body-0113", "role": "body", "section": "Hydra and MultiROCKET-Hydra", "weight": 1.0} -->

HYbrid Dictionary--ROCKET Architecture (Hydra) is a model that combines dictionary-based and convolution-based models. It begins by utilizing random convolutional kernels to calculate the activation of time series. These kernels, unlike ROCKET, are arranged into $g$ groups of $k$ kernels each. In each group of $k$ kernels, the activation of a kernel with the input time series is calculated, and we record how frequently this kernel is the best match (counts the highest activation). This results in a $k$-dimensional count vector for each of the $g$ groups, resulting in a total of $g \times k$ features.

<!-- chunk {"id": "body-0114", "role": "body", "section": "Hydra and MultiROCKET-Hydra", "weight": 1.0} -->

To implement Hydra, the time series is convolved with the kernels, and the resulting activation maps are organized into $g$ groups. Next, an (arg)max operation is performed to count the number of best matches, and the counts for each group's dictionary are increased. The main hyperparameters to consider are the number of groups and the number of kernels per group, with default values of $g = 64$ and $k = 8$. Hydra is applied to both the time series and its first-order differences. The best results in come from concatenating features from Hydra with features from MultiROCKET to form its pipeline. We call this classifier MultiROCKET-Hydra.

<!-- chunk {"id": "body-0115", "role": "body", "section": "Comparison of Convolution Based Approaches", "weight": 1.0} -->

Table 9 highlights the key differences between the convolution based approaches. fixed (relative to input) fixed (relative to input) PPV, MPV, MIPV, LSPV Response per Kernel/Group feature vector size Table 9: Key Differences in approaches from ROCKET to MiniROCKET to MultiROCKET.

<!-- chunk {"id": "body-0116", "role": "body", "section": "Deep Learning", "weight": 1.0} -->

Deep learning has been the most active area of TSC research since the bake off in terms of the number of publications. It was thought by many that the impact deep learning had on fields such as vision and speech would be replicated in TSC research. In a paper with *"Finding AlexNet for time series classification"* in the title, discuss the impact AlexNet had on computer vision and observe that this lesson indicates that *"given the similarities in the data, it is easy to suggest that there is much potential improvement for deep learning in TSC."*. A highly cited survey paper found that up to that point, ResNet was the most accurate TSC deep learner. Subsequently, the same group proposed InceptionTime, which was not significantly different to top perfming hybrid algorithms in terms of accuracy. Since InceptionTime there have been a huge number of deep learning papers proposing TSC algorithms: a recent survey references 246 papers, most of which have been published in the last three years. Table 11 summarises some recently proposed deep learning classification algorithms. Without giving specific examples, there are several concerning trends in the deep learning TSC research thread.

<!-- chunk {"id": "body-0117", "role": "body", "section": "Deep Learning", "weight": 1.0} -->

Most seriously, there is a tendency to perform model selection on test data, i.e. maximize the test accuracy over multiple epochs. This is obviously biased, yet seems to happen even with publications in highly selective venues. Secondly, many papers do not make their source code available. Given all these algorithms are based on standard tools like TensorFlow and PyTorch, this seem inexcusable. Thirdly, they often evaluate on subsets of the archive without any clear rationale as to why. Most are evaluated only on the multivariate archive. Whilst cherry-picking data is questionable, using just MTSC data is not, since deep learning classifiers are usually proposed specifically for MTSC. However, it puts them beyond the scope of this paper. Fourthly, they frequently only compare against other deep learning classifiers, often set up as weak straw men. Finally, they often do not seem to offer any advance on previous research. We have not seen any algorithm that can realistically claim to outperform InceptionTime, nor its successor H-InceptionTime. Because of this, we restrict our attention to five deep learning algorithms. We include a standard Convolutional Neural Network (CNN) implementation as a baseline.

<!-- chunk {"id": "body-0118", "role": "body", "section": "Deep Learning", "weight": 1.0} -->

We use the same CNN structure as used in the deep learning bake off. We evaluate ResNet since it was best performing. InceptionTime is included since it is, to the best our knowledge, best in category for deep learning. We also evaluate two recent extensions of InceptionTime: H-InceptionTime and LiteTime. The relation flowchart for deep learning algorithms is shown in Figure 30.

<!-- chunk {"id": "body-0119", "role": "body", "section": "Convolution Neural Networks (CNN)", "weight": 1.0} -->

Convolution Neural Networks (CNN), were first introduced, and have gained widespread use in image recognition. Their popularity has increased significantly since AlexNet won the ImageNet competition in 2012. CNNs comprise three types of layers: convolutional, pooling, and fully connected. The convolutional layer slides a filter over a time series, extracting features that are unique to the input. Convolving a one-dimensional filter with the input produces an activation or feature map.

<!-- chunk {"id": "body-0120", "role": "body", "section": "Convolution Neural Networks (CNN)", "weight": 1.0} -->

The result of applying one filter $\omega$ to a time series $T$ at offset $t$ is defined: Where the filter $\omega$ is of length $l$, the bias parameter is $b$, and $f$ is a non-linear activation function such as ReLu applied to the result of the convolution. One significant advantage of CNNs is that the filter weights are shared across each convolution, reducing the number of weights that must be learned when compared to fully connected neural networks. But instead of manually setting filter weights, these are learned by the CNN directly from the training data.

<!-- chunk {"id": "body-0121", "role": "body", "section": "Convolution Neural Networks (CNN)", "weight": 1.0} -->

As multiple learned filters are applied to the input, each resulting in one activation map of roughly the same size as the input, a pooling layer is used in-between every two convolution layers. A pooling layer, such as Max or Min-pooling, reduces the number of features in each map to i.e. the maximum value, thus providing phase-invariance. After several blocks of convolutional and pooling layers, one or more fully connected layers follow. Finally, a softmax layer with one output neuron per class is used in the final layer.

<!-- chunk {"id": "body-0122", "role": "body", "section": "Residual Network (ResNet)", "weight": 1.0} -->

The Residual Network (ResNet), is a deep learning architecture that has been successfully adapted for time series analysis. ResNet is composed of three residual blocks, each comprising two main components: (a) three convolutional layers that extract features from the input data followed by batch normalization and a ReLu non-linear activation function, and (b) a shortcut connection that allows the direct propagation of information from earlier layers to later ones. Figure 31 ‣ 4.7 Deep Learning ‣ 4 Time Series Classification Algorithms ‣ Bake off redux: a review and experimental evaluation of recent time series classification algorithms") illustrates the structure.

<!-- chunk {"id": "body-0123", "role": "body", "section": "Residual Network (ResNet)", "weight": 1.0} -->

The shortcut connection is designed to mitigate the vanishing gradients problem for deep neural networks, and the convolutional layers extract features from time series data. At the end of the model, the features are passed through one Global Average Pooling (GAP) and one fully-connected softmax layer is used with the number of neurons equal to the number of classes.

<!-- chunk {"id": "body-0124", "role": "body", "section": "InceptionTime", "weight": 1.0} -->

InceptionTime is a deep learning model proposed. It is an ensemble of five deep learning classifiers, each with the same architecture built on cascading Inception modules. Diversity is achieved through randomising initial weight values in each of the five models.

<!-- chunk {"id": "body-0125", "role": "body", "section": "InceptionTime", "weight": 1.0} -->

The network, illustrated in Figure 32, is composed of two consecutive residual blocks. Where each residual block is composed of three inception modules. The input of the residual block is connected via a shortcut connection to the block's output, to address the vanishing gradient problem. A Global Average Pooling (GAP) layer follows the two residual blocks. Finally, a fully-connected softmax output layer is used with the number of neurons equal to the number of classes. An inception module first applies a *bottleneck layer*, to transform an input multivariate TS to a lower dimensional TS. It then applies multiple convolutional filters of varying kernel sizes, termed multiplexing convolution, to capture temporal features at different scales.

<!-- chunk {"id": "body-0126", "role": "body", "section": "InceptionTime", "weight": 1.0} -->

Key design differences to ResNet are ensembling of models, the use of bottleneck layers, multiplexing convolution using varying kernel sizes, and the use of only two residual blocks, as opposed to three in ResNet.

<!-- chunk {"id": "body-0127", "role": "body", "section": "H-InceptionTime", "weight": 1.0} -->

proposed an extension of InceptionTime that included hand-craft one-dimensional convolution filters to detect very specific patterns in a time series: increasing trends, decreasing trends and peaks. Hybrid Inception (H-Inception) uses the hand-crafted filters in parallel with the first module of the Inception network. Like InceptionTime, H-InceptionTime is an ensemble of five base models. To avoid the need to find the best length of hand-crafted filters, H-InceptionTime chooses different lengths for each hand-crafted filter and used all of them. They found H-InceptionTime provided a small, but significant, improvement over InceptionTime on the 112 UCR datasets.

<!-- chunk {"id": "body-0128", "role": "body", "section": "LITETime", "weight": 1.0} -->

Both ResNet and Inception have approximately 500k trainable parameters and are computationally intensive. In 2023, proposed a smaller model for InceptionTime, called Light Inception with boosTing tEchniques (LITE). LITETime uses the DepthWise Separable Convolutions in order to significantly reduce the number of parameters while using boosting techniques to balance the trade off between complexity and performance. These boosting techniques are multiplexing convolution, dilated convolution and hand-crafted-filters. Multiplexing convolution is the approach of applying multiple convolution layers in parallel of different kernel size, motivated from Inception. The usage of dilated convolution is motivated from the fact of it boosting many TSC models in the literature, such as ROCKET. The LITETime ensemble of five base models is not significantly worse than full InceptionTime, but much faster.

<!-- chunk {"id": "body-0129", "role": "body", "section": "Hybrid", "weight": 1.0} -->

The nature of the data and the problem dictate which category of algorithm is most appropriate. The most accurate algorithms on average, with no apriori knowledge of the best approach, combine multiple transformation types in a hybrid algorithm. We define a hybrid algorithm as one which by design encompasses or ensembles multiple of the discriminatory representations we have previously described. Some algorithms will naturally include multiple transformation characteristics, but are not classified as hybrid approaches. For example, many interval approaches extract unsupervised summary statistics from the intervals they select, but as the focus of the algorithm is on generating features from intervals we would not consider it a hybrid.

<!-- chunk {"id": "body-0130", "role": "body", "section": "Hybrid", "weight": 1.0} -->

The overall best performing approach in the bake off by a significant margin was the Collective of Transformation Ensembles (COTE), which at the time was the only algorithm that explicitly ensembles over different representations. It has been subsequently renamed Flat-COTE due to its structure: it is an ensemble of $35$ time series classifiers built in the time, auto-correlation, power spectrum and shapelet domains. The components of the ST-HESCA and EE ensembles are pooled with classifiers built on autocorrelation (ACF) and power spectrum (PS) representation. All together, this includes the eight classifiers built on the shapelet transform from ST-HESCA, the 11 elastic distance $1$-NN classifiers from EE and the eight HESCA classifiers built on ACF and PS transformed series. A weighed vote is used to label new cases, with each classifier being weighted using its train set cross-validation accuracy.

<!-- chunk {"id": "body-0131", "role": "body", "section": "Hybrid", "weight": 1.0} -->

The COTE family of classifiers has evolved since Flat-COTE, and new hybrid algorithms have been produced following the success shown by ensembling multiple representations. The relation flowchart for hybrid based algorithms is shown in Figure 34 Figure 34: An overview of feature based classifiers and the relationship between them. Filled algorithms were released after the 2017 bake off and algorithms with a thin border are not included in our experiments.

<!-- chunk {"id": "body-0132", "role": "body", "section": "HIVE-COTE (HC$\\alpha$)", "weight": 1.0} -->

The Hierarchical Vote Collective of Transformation Ensembles (HIVE-COTE) was proposed to overcome some of the problems with Flat-COTE. This first version of HIVE-COTE, subsequently called HIVE-COTE~α~ (HC~α~), is a heterogeneous ensemble containing five modules each from a different representation: EE from the distance based representation; TSF from interval based methods; BOSS from dictionary based approaches and ST-HESCA from shapelet based techniques and the spectral based RISE. The five modules are ensembled using the Cross-validation Accuracy Weighted Probabilistic Ensemble (CAWPE, known at the time as HESCA, ). CAWPE employs a tilted probability distribution using exponential weighing of probabilities estimated for each module found through cross-validation on the train data. The weighted probabilities from each module are summed and standardised to produce the HIVE-COTE probability prediction.

<!-- chunk {"id": "body-0133", "role": "body", "section": "HIVE-COTE version 1 (HC1)", "weight": 1.0} -->

Whilst state-of-the-art in terms of accuracy, HC~α~ scales poorly. A range of improvements to make HIVE-COTE more usable were introduced in HIVE-COTE v1.0 (HC1). HC1 has four modules instead of the five used in HIVE-COTE~α~: it drops the computationally intensive EE algorithm without loss of accuracy. BOSS is replaced by the more configurable cBOSS. The improved randomised version of STC is included with a default limit on the search and the Rotation Forest classifier. TSF and RISE had usability improvements. HC1 is designed to be contractable, in that you can specify a maximum train time.

<!-- chunk {"id": "body-0134", "role": "body", "section": "HIVE-COTE version 2 (HC2)", "weight": 1.0} -->

In 2021, HIVE-COTE was again updated to further address scalability issues and reflect recent innovations to individual TSC representations and HIVE-COTE v2.0 (HC2) was proposed. In HC2, RISE, TSF and cBOSS are replaced, with only STC retained. TDE replaces cBOSS as the dictionary classifier. DrCIF replaces both TSF and RISE for the interval and frequency representations. An ensemble of ROCKET classifiers called the Arsenal is introduced as a new convolutional based approach. Estimation of test accuracy via cross-validation is replaced by an adapted form of out-of-bag error, although the final model is still built using all training data. Unlike previous versions, HC2 is capable of classifying multivariate time series. Figure 35 ‣ 4.8 Hybrid ‣ 4 Time Series Classification Algorithms ‣ Bake off redux: a review and experimental evaluation of recent time series classification algorithms") illustrates the structure of HC2, while Figure 36 ‣ 4.8 Hybrid ‣ 4 Time Series Classification Algorithms ‣ Bake off redux: a review and experimental evaluation of recent time series classification algorithms") visualises the ensemble members of HIVE-COTE over its evolution.

<!-- chunk {"id": "body-0135", "role": "body", "section": "TS-CHIEF", "weight": 1.0} -->

The Time Series Combination of Heterogeneous and Integrated Embedding Forest (TS-CHIEF) is a homogeneous ensemble where hybrid features are embedded in tree nodes rather than modularised through separate classifiers. The TS-CHIEF comprises an ensemble of trees that embed distance, dictionary, and spectral base features. At each node, a number of splitting criteria from each of these representations are considered. These splits use randomly initialised parameters to help maintain diversity in the ensemble. The dictionary based splits are based on BOSS, distance splits based on EE and interval splits based on RISE. The goal of TS-CHIEF was to obtain the benefits of multiple representations without the massive processing requirement of the original HIVE-COTE.

<!-- chunk {"id": "body-0136", "role": "body", "section": "Randomised Interval-Shapelet Transformation (RIST)", "weight": 1.0} -->

The Randomised Interval-Shapelet Transformation (RIST) pipeline is a simpler approach than the previously described hybrids. Rather than constructing an ensemble, RIST concatenates the output of multiple transformations to form a pipeline classifier. RIST uses the transformation portions from the interval based DrCIF and the shapelet based RDST algorithms. For both of these transformations, features are extracted from both the base series and multiple series representations. These representations are the first order differences, the periodogram of the series and the series autoregression coefficients. After concatenating the output, these features are then used to build an Extra Trees classifier. The aim of RIST is to provide a simple and relatively efficient hybrid algorithm which can be applied to both classification and extrinsic regression tasks.

<!-- chunk {"id": "body-0137", "role": "body", "section": "Results", "weight": 1.0} -->

To keep the analysis tractable, we restrict further analysis of performance to the best classifier in each of the eight categories. Further results tables and figures are available in Appendix C, with all results files available on the accompanying website and can be accessed directly accessible in code withg aeon. Figure 39 shows the ranking of these classifiers on the 112 UCR data for $30$ resamples of train/tests splits. HC2 and MR-Hydra are the top performing algorithms in terms of accuracy. There is no significant difference between QUANT, H-IT, RDST and WEASEL 2.0 in terms of test accuracy. HC2 is best performing with AUROC and NLL measures. H-IT performs better with balanced accuracy and NLL.

<!-- chunk {"id": "body-0138", "role": "body", "section": "Results", "weight": 1.0} -->

The AUROC and NLL need to be interpreted in context: Weasel 2.0, RDST and MR-Hydra use classifiers that only produce 0/1 predictions. This means they will inevitably perform poorly on AUROC and NLL.

<!-- chunk {"id": "body-0139", "role": "body", "section": "Results", "weight": 1.0} -->

(d) Negative Log Likelihood Figure 39: Averaged ranked performance statistics for eight best of category algorithms on 112 UCR UTSC problems. Statistics are averaged over 30 resamples of train and test splits. Names shortened for clarity: FP is FreshPrince, W 2.0 is Weasel 2.0, MR-H is MR-Hydra and H-IT is H-InceptionTime.

<!-- chunk {"id": "body-0140", "role": "body", "section": "Results", "weight": 1.0} -->

For context, Figure 40 shows the scatter plot of HC2 against the next best (MR-Hydra) and the worst performing (PF). It is worth reiterating that PF is significantly better than both EE and 1-NN DTW, both of which were considered state of the art until recently.

<!-- chunk {"id": "body-0141", "role": "body", "section": "Results", "weight": 1.0} -->

For convenience, Table 14 summarises the summary statistics presented in Section 4. HC2 is on average about 0.5% more accurate than MR-Hydra, over 6% more accurate than PF and over 12% more accurate than 1NN-DTW.

<!-- chunk {"id": "body-0142", "role": "body", "section": "Performance on New TSC Datasets", "weight": 1.0} -->

HC2 performs the best on the 112 datasets. However, HIVE-COTE has been in development for over five years, and all advances were judged by evaluation on these datasets. As acknowledged, there is always the risk of the introduction of subconscious bias in the design decisions that lead to the new algorithms. To counter this, we have assembled $30$ new datasets, as described in Section 3.1. Figure 41 shows the ranks for the eight best of category on these data sets. The top clique for accuracy contains MR-Hydra, HC2, RDST, QUANT and FreshPRINCE. The results for balanced accuracy are similar. Figure 42 shows the results for the combined 142 datasets. The performance of HC2 and MR-Hydra is very similar, and they are in a clique that is significantly better than the other six classifiers. noted that critical difference diagrams (CD) can be deceptive and lack stability, with the relative ordering being highly sensitive to the selection of comparates included in the comparisons. This sensitivity renders them susceptible to inadvertent manipulation.

<!-- chunk {"id": "body-0143", "role": "body", "section": "Performance on New TSC Datasets", "weight": 1.0} -->

To circumvent this problem, they propose a bespoke pairwise comparison tool, called multiple comparative matrix (MCM)^1111^11 It shows pairwise comparisons between all comparates, and includes difference in average scores, wins/draws/losses, and Wilcoxon p-values. Colors of the heat map represent mean differences in scores. Red indicates that the comparate in the row wins by more on average than the comparate in the column. Bold text indicates that the difference in significant. Figure 43 summarises the performance of the eight classifiers on 112 datasets using the MCM, with comparisons to the 30 new datasets and 142 datasets available in Appendix C. A notable observation arises when comparing the CD on accuracy in Figure 39 to this MCM on the 112 UCR UTSC. The rankings of WEASEL 2.0, QUANT, H-IT and RDST are deceptive. Despite WEASEL 2.0 demonstrating more pairwise wins compared to RDST or QUANT in the MCM, its ranking appears higher (worse) than both in the CD when all 8 comparates are taken into account.

<!-- chunk {"id": "body-0144", "role": "body", "section": "Performance on New TSC Datasets", "weight": 1.0} -->

In addition, H-IT has less pairwise wins than RDST in the MCM, yet shows the lower (better) rank in the CD.

<!-- chunk {"id": "body-0145", "role": "body", "section": "Analysis", "weight": 1.0} -->

Relative performance on test suites is important when evaluating classifiers, but it does not necessarily generalise to new problems. There will be problem domains and specific applications where different classifiers will be the most effective. Furthermore, characteristics such as the variability in performance and the run time complexity of algorithms are also of great interest to the practitioner.

<!-- chunk {"id": "body-0146", "role": "body", "section": "Analysis", "weight": 1.0} -->

We model the approach used in by comparing performance by data characteristics using all 142 datasets. Tables 15, 16 and 17 break performance down by series length, train set size and number of classes. HC2 and MR-Hydra are first or second on average in each category. HC2 seems to do better with longer series. MR-Hydra performs better with larger train set sizes. Table 18 breaks down performance by problem type. HC2 and MR-Hydra are the top two ranked in all categories except MOTION. MR-Hydra does particularly well on image outlines, whereas HC2 excels at electric devices and spectrograms.

<!-- chunk {"id": "body-0147", "role": "body", "section": "Analysis", "weight": 1.0} -->

Run time is clearly an important consideration. The speed of QUANT and the ROCKET family of classifiers is a significant feature. It was stated in the bake off that "\[a\]n algorithm that is faster than \[the current state of the art\] but not significantly less accurate would be a genuine advance in the field". ROCKET and the subsequent refinements fulfil this criteria and represent an important advance. Table 19 shows the total train time for classifiers on the $142$ problems and Figure 44 shows the plot of rank against train time (on a logarithmic scale). We do not include H-IT in these measurements because it was run on two different types of GPU, whereas the other algorithms were all trained on the same CPU (Intel Xeon Gold 5220R 2.2GHz). HC2 is clearly much slower than MR-Hydra. This is at least in parts the result of the configuration and implementation of HC2.

<!-- chunk {"id": "body-0148", "role": "body", "section": "Analysis", "weight": 1.0} -->

For example, TDE, a component of HC2, is not optimised using numba^1212^12 Nevertheless, there is no doubt that MR-Hydra offers a good accuracy/train time trade off: it is on average as accurate as HC2 but orders of magnitude faster. If results are required very quickly or train set sizes are large, MR-Hydra would seem to be the better option. However, for smaller train set sizes (see Table 16), or if probabilities or orderings are required (see Table 14), the results indicate that HC2 is the better option. A special mention must be given to QUANT. It achieves high accuracy remarkably fast: it is an order of magnitude faster. We would recommend QUANT for very large problems, assuming it scales accordingly.

<!-- chunk {"id": "body-0149", "role": "body", "section": "Analysis", "weight": 1.0} -->

We explored the effect on performance of the design decisions described in Table 22. If we group average accuracy ranks by each design factor of use of dilation, differences, ensemble, frequency domain and discretisation and perform a one factor ANOVA on each factor, we find a significant difference in rank distribution between those using dilation and those that do not, and those that use differences and those that do not. There was no significant difference in distribution when grouped by frequency, ensemble or discretisation. Care must be taken when interpreting these results since the assumptions behind the tests are not satisfied. However, there is at least some support for the utility of using dilation and differenced series. Finally, we have included a comprehensive correlation matrix on average accuracy ranks (Figure 49 in the appendix). These demonstrate the diversity in performance of these classifiers and show the difference in performance between shapelet based and convolution based algorithms (Figure 50).

<!-- chunk {"id": "body-0150", "role": "body", "section": "Conclusions", "weight": 1.0} -->

Research into algorithms for TSC has seen genuine progress in the last ten years, and the volume of research has dramatically increased. We have provided a particular view of this research landscape by grouping algorithms into eight categories defined by the core representation/transformation. We have compared the best in each category on 112 TSC problem and introduced 30 new datasets to counter any possible bias from over fitting. We evidence progress by benchmarking against algorithms previously considered the best performing, and show that two classifiers, MR-Hydra and HC2, generally perform the best. HC2 performs significantly better on the current UCR archive, but there is less observable difference when we compare them on 30 new problems we have introduced. This could be due to the smaller sample size, the nature of the data sets or reflect some embedded bias in algorithm design. We note that HC2 does worse than MR-Hydra on imbalanced data and with larger train set sizes, but is better with more class balance, smaller train set sizes and with long series.

<!-- chunk {"id": "body-0151", "role": "body", "section": "Conclusions", "weight": 1.0} -->

We are not claiming that these results should be taken to mean practitioners should always use MR-Hydra and/or HC2. There are strengths and weakness to all the algorithms we have described. Indeed, there is a case to be made for using QUANT by default, at least for exploratory analysis, because it is so fast. Understanding when it is appropriate to use which algorithm for a specific problem is an active research area. However, we suggest that, in the absence of any prior information these two algorithms make a sensible starting point for a new TSC problem. Despite significant research effort, there has not been an Alexnet for TSC, i.e. a deep learning approach that has dominated all others. It may be because the problems in the archives are relatively small compared to other archives used for deep learning evaluation: Table 16 shows that H-Inception time improves relative to other algorithms as the number of training cases increases.

<!-- chunk {"id": "body-0152", "role": "body", "section": "Conclusions", "weight": 1.0} -->

However, we think the core reason deep learning has not provided the gains many expected is that, unlike specific applications such as image classification or natural language processing, there is not one common underlying structure for the neural networks to exploit. Nevertheless, there is no doubt scope for improvements in deep learning algorithms for TSC. H-InceptionTime performs well overall, but Figure 45 demonstrates its limitations: it often performs terribly, and this makes its overall performance worse. If this tendency could be corrected, possibly by some automated structural optimisation, it seems likely that H-InceptionTime could match HC2 and MR-Hydra.

<!-- chunk {"id": "body-0153", "role": "body", "section": "Conclusions", "weight": 1.0} -->

Since the original bake off a number of trends have developed in research, and some prior observations remain true. On average, hybrid algorithms still perform better than single domain approaches on the UCR archive. The ROCKET and HIVE-COTE family of classifiers work well because they combine convolution/shapelet approaches with dictionary based ones, i.e. they look for the presence of or the frequency of subseries. A key component of ROCKET based classifiers is dilation. We have shown that using dilation has significantly improved the single representation classifiers RDST and WEASEL 2.0. Incorporation of dilation could well benefit other algorithms, such as interval based classifiers. Ensemble algorithms are still effective and popular, but pipeline algorithms combining a transformation with a linear classifier such as ridge regression have shown to be just as competitive. The algorithms using linear classifiers such as ROCKET, WEASEL 2.0 and RDST have shown to be more scalable than ensembles generally, but cannot produce good probability estimates. More algorithms now incorporate transformed series such as first-order differences and periodograms into their feature extraction. This has been shown to increase accuracy in the majority of the algorithm types we have presented.

<!-- chunk {"id": "body-0154", "role": "body", "section": "Conclusions", "weight": 1.0} -->

We believe there is great scope for improving time series specific classifiers: None except QUANT scale particularly well for large data, particularly in terms of memory: we are constructing a set of larger problems but none of the classifiers could be built in them in reasonable time and/or memory; there is a lack of principled work flows for using these classifiers to help understand the mechanisms for forming classifiers; multivariate TSC is less understood and many of the classifiers described have not been designed to be used in this way; and there has been little research into how best to handle unequal length series. We believe there are many unanswered questions in the field of TSC and predict it will remain as active and productive for the next 10 years.
