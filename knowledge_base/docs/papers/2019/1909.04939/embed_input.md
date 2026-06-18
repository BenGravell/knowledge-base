InceptionTime: Finding AlexNet for Time Series Classification

Topics include Neural networks, Deep learning, Convolutional networks, Attention mechanisms, Classification, Time series classification, Time series, Classifiers, Datasets, Accuracy, Scalability, Learning, InceptionTime, TSC, Convolutional neural network.

This paper brings deep learning at the forefront of research into Time Series Classification (TSC). TSC is the area of machine learning tasked with the categorization (or labelling) of time series. The last few decades of work in this area have led to significant progress in the accuracy of classifiers, with the state of the art now represented by the HIVE-COTE algorithm. While extremely accurate, HIVE-COTE cannot be applied to many real-world datasets because of its high training time complexity in O(N2 * T4) for a dataset with N time series of length T. For example, it takes HIVE-COTE more than 8 days to learn from a small dataset with N = 1500 time series of short length T = 46. Meanwhile deep learning has received enormous attention because of its high accuracy and scalability. Recent approaches to deep learning for TSC have been scalable, but less accurate than HIVE-COTE. We introduce InceptionTime - an ensemble of deep Convolutional Neural Network (CNN) models, inspired by the Inception-v4 architecture....

## Introduction

Recent times have seen an explosion in the magnitude and prevalence of time series data. Industries varying from health care and social security to human activity recognition and remote sensing, all now produce time series datasets of previously unseen scale --- both in terms of time series length and quantity. This growth also means an increased dependence on automatic classification of time series data, and ideally, algorithms with the ability to do this at scale.

These problems, known as Time Series Classification (TSC), differ significantly to traditional supervised learning for structured data, in that the algorithms should be able to handle and harness the temporal information present in the signal. It is easy to draw parallels from this scenario to computer vision problems such as image classification and object localization, where successful algorithms learn from the spatial information contained in an image. Put simply, the time series problem is essentially the same class of problem, just with one less dimension....

## Conclusion

Deep learning for time series classification still lags behind neural networks for image recognition in terms of experimental studies and architectural designs. In this paper, we fill this gap by introducing InceptionTime, inspired by the recent success of Inception-based networks for various computer vision tasks. We ensemble these networks to produce new state-of-the-art results for TSC on the 85 datasets of the UCR archive. Our approach is highly scalable, two orders of magnitude faster than current state-of-the-art models such as HIVE-COTE....

To further visualize the difference between the InceptionTime and HIVE-COTE, Figure 6 depicts the accuracy plot of InceptionTime against HIVE-COTE for each of the 85 UCR datasets. The results show a Win/Tie/Loss of 40/6/39 in favor of InceptionTime, however the difference is not statistically significant as previously discussed. From Figure 6, we can also easily spot the two datasets for which InceptionTime noticeably under-performs (in terms of accuracy) with respect to HIVE-COTE: Wine and Beef....

Our proposed state-of-the-art InceptionTime model is an ensemble of 5 Inception networks, with each prediction given an even weight....
