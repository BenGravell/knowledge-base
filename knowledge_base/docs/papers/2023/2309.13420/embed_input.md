DenMune: Density Peak Based Clustering Using Mutual Nearest Neighbors

Topics include Robustness, Nearest neighbors, Clustering, Datasets, DenMune.

Many clustering algorithms fail when clusters are of arbitrary shapes, of varying densities, or the data classes are unbalanced and close to each other, even in two dimensions. A novel clustering algorithm, DenMune is presented to meet this challenge. It is based on identifying dense regions using mutual nearest neighborhoods of size K, where K is the only parameter required from the user, besides obeying the mutual nearest neighbor consistency principle. The algorithm is stable for a wide range of values of K. Moreover, it is able to automatically detect and remove noise from the clustering process as well as detecting the target clusters. It produces robust results on various low and high-dimensional datasets relative to several known state-of-the-art clustering algorithms.

## Introduction

Data clustering, which is the process of gathering similar data samples into groups/clusters, has been found useful in different fields such as medical imaging (to differentiate between different types of tissues medical_applications_2018 ), market research (to partition consumers into perceptual market segments customers_segmentation_2018 ), document retrieval (to find documents that are relevant to a user query in a collection of documents document_retrieval_2018 ), and fraud detection (to detect suspicious fraudulent patterns) fraud_detection_2019 ), as well as many others clustering_survey_2013.

## Partitioning-based Clustering Algorithms

In this category, data objects are divided into non-overlapping subsets (clusters) such that each object lies in exactly one subset. The most well-known and commonly used algorithm in this class is K-means. K-means is heavily dependent on the initial cluster centers, which are badly affected by noise and outliers. A well known variant is K-medoid. K-medoid selects the most centrally located point in a cluster, namely its medoid, as its representative point. Another well-known variant of K-means is KMeans++. It chooses centers at random, but weighs them according to the square distance from the closest already chosen center.

## Conclusion and Future Work

In this paper, a novel shared nearest neighbors clustering algorithm DenMune, is presented. It utilizes the MNN size to calculate the density of each point and chooses the high-density points as the seeds from which clusters may grow up. In contrast to recent similar algorithms, such as DPC and CMune, no cut-off parameter is needed from the user of DenMune. Guided by the principle of Mutual Nearest-Neighbors (MNN) consistency, DenMune prioritizes points according to a voting system and partitions them into seeds and non-seeds.

Although the motivations behind the algorithm are logical (the scheme adopted by the algorithm to partition points in a given data set into three types (seed, noise and potential noise points) and the MNN consistency principle that governs clusters growth), the conducted experiments on a variety of data sets, have shown its efficiency and robustness in detecting clusters of different sizes, shapes and densities in the presence of noise. In summary, DenMune is conceptually simple, logically sound, relies on a single parameter.
