Transformers in Time Series: A Survey

Topics include Robustness, Transformers, Computer vision, Classification, Time series, Series.

Transformers have achieved superior performances in many tasks in natural language processing and computer vision, which also triggered great interest in the time series community. Among multiple advantages of Transformers, the ability to capture long-range dependencies and interactions is especially attractive for time series modeling, leading to exciting progress in various time series applications. In this paper, we systematically review Transformer schemes for time series modeling by highlighting their strengths as well as limitations. In particular, we examine the development of time series Transformers in two perspectives. From the perspective of network structure, we summarize the adaptations and modifications that have been made to Transformers in order to accommodate the challenges in time series analysis. From the perspective of applications, we categorize time series Transformers based on common tasks including forecasting, anomaly detection, and classification. Empirically, we perform robust analysis, model size analysis, and seasonal-trend decomposition analysis to study how Transformers perform in time series.

## Introduction

The innovation of Transformer in deep learning Vaswani et al. has brought great interests recently due to its excellent performances in natural language processing (NLP) Kenton and others, computer vision (CV) Dosovitskiy et al., and speech processing Dong et al.. Over the past few years, numerous Transformers have been proposed to advance the state-of-the-art performances of various tasks significantly. There are quite a few literature reviews from different aspects, such as in NLP applications Han et al., CV applications Han et al., and efficient Transformers Tay et al..

Transformers have shown great modeling ability for long-range dependencies and interactions in sequential data and thus are appealing to time series modeling. Many variants of Transformer have been proposed to address special challenges in time series modeling and have been successfully applied to various time series tasks, such as forecasting Li et al.; Zhou et al., anomaly detection Xu et al.; Tuli et al., and classification Zerveas et al.; Yang et al.. Specifically, seasonality or periodicity is an important feature of time series Wen et al..

In this paper, we aim to fill the gap by summarizing the main developments of time series Transformers. We first give a brief introduction about vanilla Transformer, and then propose a new taxonomy from perspectives of both network modifications and application domains for time series Transformers. For network modifications, we discuss the improvements made on both low-level (i.e. module) and high-level (i.e. architecture) of Transformers, with the aim to optimize the performance of time series modeling.

## Conclusion

We have provided a survey on time series Transformers. We organize the reviewed methods in a new taxonomy consisting of network design and application. We summarize representative methods in each category, discuss their strengths and limitations by experimental evaluation, and highlight future research directions.
