TimeGPT-1

Topics include Uncertainty, Deep learning, Foundation models, Time series, Datasets, Learning, Machine learning.

In this paper, we introduce TimeGPT, the first foundation model for time series, capable of generating accurate predictions for diverse datasets not seen during training. We evaluate our pre-trained model against established statistical, machine learning, and deep learning methods, demonstrating that TimeGPT zero-shot inference excels in performance, efficiency, and simplicity. Our study provides compelling evidence that insights from other domains of artificial intelligence can be effectively applied to time series analysis. We conclude that large-scale time series models offer an exciting opportunity to democratize access to precise predictions and reduce uncertainty by leveraging the capabilities of contemporary advancements in deep learning.

## Introduction

Uncertainty is an intrinsic aspect of life, a constant element that humans have tirelessly sought to navigate and comprehend. From the traditions established by ancient civilizations to the sophisticated research endeavors in our contemporary world, brilliant minds have ceaselessly strived to anticipate the distribution of possible future events, crafting systematic approaches to unveil the prospective future.

The aspiration to predict potential outcomes, foundational across a multitude of disciplines, reflects a deep-seated human tendency to anticipate, strategize, and mitigate risks. The goal to reduce uncertainty about what will come next maps to numerous real-world applications: from understanding economic cycles and trends to discerning consumer consumption patterns; from optimizing electricity demand for energy production and grid management to aligning capacity and infrastructure for servers, workers, and machines.

Time Series Embedding: While traditionally practitioners have hypothesized that series from the same categories like retail or finance would have greater similarity than those across domains, a robust metric to measure similarity between series could significantly benefit the field. This work suggests that certain assumptions around the taxonomy of time series warrant further examination.

Furthermore, adjacent questions about foundation models for time series classification and the integration of truly multimodal (text, video) and multi-temporal foundation models promise to be engaging areas for future study. These areas will not only extend our understanding of time series data but also improve our ability to develop more powerful and generalized models for forecasting.

It should be noted that TimeGPT is not based on an existing large language model (LLM). While TimeGPT follows the same principle of training a large transformer model on a vast dataset, its architecture is specialized in handling time series data and trained to minimize the forecasting error.

The potential of foundation models, namely large-scale models pre-trained on a large dataset and later fine-tuned for specific tasks, remains relatively under-explored for time series forecasting tasks. There are, however, early indicators of the possibility of forecasting foundational models....
