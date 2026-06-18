Transformers in Time Series: A Survey

Topics include Robustness, Transformers, Computer vision, Classification, Time series, Series.

Transformers have achieved superior performances in many tasks in natural language processing and computer vision, which also triggered great interest in the time series community. Among multiple advantages of Transformers, the ability to capture long-range dependencies and interactions is especially attractive for time series modeling, leading to exciting progress in various time series applications. In this paper, we systematically review Transformer schemes for time series modeling by highlighting their strengths as well as limitations. In particular, we examine the development of time series Transformers in two perspectives. From the perspective of network structure, we summarize the adaptations and modifications that have been made to Transformers in order to accommodate the challenges in time series analysis. From the perspective of applications, we categorize time series Transformers based on common tasks including forecasting, anomaly detection, and classification. Empirically, we perform robust analysis, model size analysis, and seasonal-trend decomposition analysis to study how Transformers perform in time series....

## Introduction

The innovation of Transformer in deep learning Vaswani et al. has brought great interests recently due to its excellent performances in natural language processing (NLP) Kenton and others, computer vision (CV) Dosovitskiy et al., and speech processing Dong et al.. Over the past few years, numerous Transformers have been proposed to advance the state-of-the-art performances of various tasks significantly. There are quite a few literature reviews from different aspects, such as in NLP applications Han et al., CV applications Han et al., and efficient Transformers Tay et al..

Transformers have shown great modeling ability for long-range dependencies and interactions in sequential data and thus are appealing to time series modeling. Many variants of Transformer have been proposed to address special challenges in time series modeling and have been successfully applied to various time series tasks, such as forecasting Li et al.; Zhou et al., anomaly detection Xu et al.; Tuli et al., and classification Zerveas et al.; Yang et al.. Specifically, seasonality or periodicity is an important feature of time series Wen et al.....

## Conclusion

We have provided a survey on time series Transformers. We organize the reviewed methods in a new taxonomy consisting of network design and application. We summarize representative methods in each category, discuss their strengths and limitations by experimental evaluation, and highlight future research directions.

The second type of variant for module-level Transformers is the way to normalize time series data. To the best of our knowledge, Non-stationary Transformer Liu et al. is the only work that mainly focuses on modifying the normalization mechanism as shown in Figure 2. It explores the over-stationarization problem in time series forecasting tasks with a relatively simple plugin series stationary and De-stationary module to modify and boost the performance of various attention blocks.

Central to Transformer is the self-attention module. It can be viewed as a fully connected layer with weights that are dynamically generated based on the pairwise similarity of input patterns. As a result, it shares the same maximum path length as fully connected layers, but with a much less number of parameters, making it suitable for modeling long-term dependencies.
