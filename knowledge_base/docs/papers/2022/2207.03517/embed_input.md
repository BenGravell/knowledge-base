HierarchicalForecast: A Reference Framework for Hierarchical Forecasting in Python

Topics include Graphs, Time series, Datasets, Learning, HierarchicalForecast, Machine learning.

Large collections of time series data are commonly organized into structures with different levels of aggregation; examples include product and geographical groupings. It is often important to ensure that the forecasts are coherent so that the predicted values at disaggregate levels add up to the aggregate forecast. The growing interest of the Machine Learning community in hierarchical forecasting systems indicates that we are in a propitious moment to ensure that scientific endeavors are grounded on sound baselines. For this reason, we put forward the HierarchicalForecast library, which contains preprocessed publicly available datasets, evaluation metrics, and a compiled set of statistical baseline models. Our Python-based reference framework aims to bridge the gap between statistical and econometric modeling, and Machine Learning forecasting research. Code and documentation are available in

## Introduction

Multivariate time series data can often be organized into hierarchical structures with different levels of aggregation. Independently forecasting all the series is unlikely to produce *coherent* forecasts, that is, forecasts which satisfy the aggregation constraints as the original data. In a nutshell, hierarchical time series forecasting is a multitask forecasting problem with a set of linear aggregation constraints to be satisfied.

While summing forecasts for the most disaggregated level (called *bottom-up*) will provide coherent forecasts, it can perform poorly on highly dissagregated series. Novel hierarchical forecasting methods first generate independent forecasts for each series (called *base* forecasts), then reconcile them to produce coherent forecasts.

## Acknowledments

This work was partially supported by the Defense Advanced Research Projects Agency (award FA8750-17-2-0130), the National Science Foundation (grant 2038612), the Space Technology Research Institutes grant from NASA's Space Technology Research Grants Program, the U.S. Department of Homeland Security (award 18DN-ARI-00031), and by the U.S. Army Contracting Command (contracts W911NF20D0002 and W911NF22F0014 delivery order #4). The Fonds de la Recherche Scientifique supported this work -- FNRS under Grant No J.0011.20....

## Related Software

Minimal dependencies. Our library is built with minimal dependencies using NumPy for linear algebra and array operations, Pandas for data manipulation and sklearn for predictive modeling. We compute base forecasts using the statsforecast package, which provides the fastest implementations of AutoARIMA and AutoETS based on NumBa. This just-in-time compiler optimizes Python's NumPy code to reach execution speed attainable with native C language code.

1 TopDown/PERMBU results are unavailable because, they cannot be applied to group hierarchical structures.
2 The combinations NORMALITY-TopDown and BOOTSTRAP-TopDown are yet to be implemented, this has never been done before.

There is substantial interest on Hierarchical Forecasting from both industry and academia, as shown by the international forecasting competitions GEFCOM2012 and M5, and the Machine Learning (ML) community's growing interest in the topic (Rangapuram et al. Han et al. Paria et al. Olivares et al. Kamarthi et al. Panagiotelis et al., ).
