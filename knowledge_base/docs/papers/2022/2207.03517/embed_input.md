HierarchicalForecast: A Reference Framework for Hierarchical Forecasting in Python

Topics include Graphs, Time series, Datasets, Learning, HierarchicalForecast, Machine learning.

Large collections of time series data are commonly organized into structures with different levels of aggregation; examples include product and geographical groupings. It is often important to ensure that the forecasts are coherent so that the predicted values at disaggregate levels add up to the aggregate forecast. The growing interest of the Machine Learning community in hierarchical forecasting systems indicates that we are in a propitious moment to ensure that scientific endeavors are grounded on sound baselines. For this reason, we put forward the HierarchicalForecast library, which contains preprocessed publicly available datasets, evaluation metrics, and a compiled set of statistical baseline models. Our Python-based reference framework aims to bridge the gap between statistical and econometric modeling, and Machine Learning forecasting research. Code and documentation are available in

## Introduction

Multivariate time series data can often be organized into hierarchical structures with different levels of aggregation. Independently forecasting all the series is unlikely to produce *coherent* forecasts, that is, forecasts which satisfy the aggregation constraints as the original data. In a nutshell, hierarchical time series forecasting is a multitask forecasting problem with a set of linear aggregation constraints to be satisfied.

While summing forecasts for the most disaggregated level (called *bottom-up*) will provide coherent forecasts, it can perform poorly on highly dissagregated series. Novel hierarchical forecasting methods first generate independent forecasts for each series (called *base* forecasts), then reconcile them to produce coherent forecasts.

There is substantial interest on Hierarchical Forecasting from both industry and academia, as shown by the international forecasting competitions GEFCOM2012 and M5, and the Machine Learning (ML) community's growing interest in the topic (Rangapuram et al. Han et al. Paria et al. Olivares et al. Kamarthi et al. Panagiotelis et al., ).

We introduce the open-source benchmark library HierarchicalForecastto tackle these challenges^11^1License: CC-by 4.0, see
Code and documentation are available in Our work builds upon Python's fastest open-source ETS/ARIMA^22^2Autoregressive Integrated Moving Average (ARIMA) and Exponential Smoothing (ETS) are two of the most important univariate forecasting baseline methods. implementations and well-performing neural forecasting methods to improve the availability, utility, and adoption of hierarchical forecast reference baselines.

## Conclusion and Plans

We present HierarchicalForecast, a Python open-source library dedicated to hierarchical time series forecasting. The library integrates publicly available processed datasets, evaluation metrics, and a curated set of highly efficient statistical baselines. We provide examples and references to extensive experiments to show how to use the baselines and evaluate their empirical performance. This work will help the Machine Learning forecasting community by bridging the gap between statistical and econometric modeling and providing benchmark tools for developing novel hierarchical forecasting algorithms compared to the well-established methods.
