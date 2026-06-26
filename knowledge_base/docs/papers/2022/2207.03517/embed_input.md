<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

HierarchicalForecast: A Reference Framework for Hierarchical Forecasting in Python

Topics include Graphs, Time series, Datasets, Learning, HierarchicalForecast, Machine learning.

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Large collections of time series data are commonly organized into structures with different levels of aggregation; examples include product and geographical groupings. It is often important to ensure that the forecasts are coherent so that the predicted values at disaggregate levels add up to the aggregate forecast. The growing interest of the Machine Learning community in hierarchical forecasting systems indicates that we are in a propitious moment to ensure that scientific endeavors are grounded on sound baselines. For this reason, we put forward the HierarchicalForecast library, which contains preprocessed publicly available datasets, evaluation metrics, and a compiled set of statistical baseline models. Our Python-based reference framework aims to bridge the gap between statistical and econometric modeling, and Machine Learning forecasting research. Code and documentation are available in

<!-- chunk {"id": "body-0003", "role": "body", "section": "Introduction", "weight": 1.5} -->

Multivariate time series data can often be organized into hierarchical structures with different levels of aggregation. Independently forecasting all the series is unlikely to produce *coherent* forecasts, that is, forecasts which satisfy the aggregation constraints as the original data. In a nutshell, hierarchical time series forecasting is a multitask forecasting problem with a set of linear aggregation constraints to be satisfied.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

While summing forecasts for the most disaggregated level (called *bottom-up*) will provide coherent forecasts, it can perform poorly on highly dissagregated series. Novel hierarchical forecasting methods first generate independent forecasts for each series (called *base* forecasts), then reconcile them to produce coherent forecasts.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

There is substantial interest on Hierarchical Forecasting from both industry and academia, as shown by the international forecasting competitions GEFCOM2012 and M5, and the Machine Learning (ML) community's growing interest in the topic.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

An enabling condition for the systematic development of useful forecasting methods is the ability to empirically evaluate and compare newly proposed methods with state-of-the-art and well-established baselines. However, ML research on hierarchical forecasting faces two challenges. First, while Python continues to grow in popularity among the ML community, it lacks many relevant statistical and econometric modeling packages (often originally developed in the R language). As a result, researchers must build Python bridges to access the R baselines' implementations. Rapid, substantial development in statistical methods for hierarchical forecasting exacerbates this problem. Secondly, the Python global interpreter lock limits its programs to use a single thread, which prevents us from taking advantage of the available multi-core resources to speed up the software. When implemented naively, statistical baselines in Python take excessively long execution times, surpassing those of more complex methods, and discouraging their use.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

We introduce the open-source benchmark library HierarchicalForecastto tackle these challenges^11^1License: CC-by 4.0, see Code and documentation are available in Our work builds upon Python's fastest open-source ETS/ARIMA^22^2Autoregressive Integrated Moving Average (ARIMA) and Exponential Smoothing (ETS) are two of the most important univariate forecasting baseline methods. implementations and well-performing neural forecasting methods to improve the availability, utility, and adoption of hierarchical forecast reference baselines.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Library description (/features)", "weight": 1.0} -->

Compared to existing hierarchical forecasting software libraries, HierarchicalForecast has the following distinctive features: Minimal dependencies. Our library is built with minimal dependencies using NumPy for linear algebra and array operations, Pandas for data manipulation and sklearn for predictive modeling. We compute base forecasts using the statsforecast package, which provides the fastest implementations of AutoARIMA and AutoETS based on NumBa. This just-in-time compiler optimizes Python's NumPy code to reach execution speed attainable with native C language code.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Library description (/features)", "weight": 1.0} -->

Comprehensive set of hierarchical forecasting methods. Some hierarchical forecasting Python implementations are available in the following packages: gluonts, darts, scikit-hts, sktime, and pyhts. However, as seen in Table 1 ‣ HierarchicalForecast: A Reference Framework for Hierarchical Forecasting"), each of these libraries only hosts a subset of the State-Of-The-Art (SOTA) methods. Our library provides unified access to a comprehensive set of these methods and enables robust performance validation of the implementations to ensure the Python community's access to efficient and reliable baselines. HierarchicalForecast's curated collection of reference algorithms includes BottomUp, TopDown, MiddleOut, MinTrace, and ERM for point forecasting, and it is the only Python library so far that includes SOTA probabilistic forecasting methods, including PERMBU, NORMALITY, and BOOTSTRAP.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Library description (/features)", "weight": 1.0} -->

Forecast evaluation and visualization. Our library facilitates a complete forecast evaluation across the levels of the hierarchical structure. It includes multiple standard accuracy measures for point forecasts. Furthermore, it also includes multiple scoring rules to evaluate probabilistic forecasts, such as the multivariate logarithmic and energy scores and the univariate scaled continuous ranked probability score (sCRPS). In addition to the forecast accuracy evaluation tools, the package provides specialized visualization tools.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Library description (/features)", "weight": 1.0} -->

Hierarchical time series datasets. The library provides access to five Pandas datasets and the aggregation utils to create them. Australian Labour monthly reports, SF Bay Area daily Traffic measurements, Quarterly Australian Tourism-S visits, Monthly Australian Tourism-L visits, and daily Wiki2 article views. Each dataset is accompanied by metadata capturing its seasonality/frequency, the forecast horizon used in previous publications, its corresponding hierarchical aggregation constraints matrix, and the names of its levels.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Related Software", "weight": 1.0} -->

We refer to Januschowski et al., and Siebert et al. for complete open-source forecasting software surveys. We describe packages relevant to HierarchicalForecast. Classic statistical and econometric time series models, such as ARIMA, ETS, and GARCH have low-level NumPy implementations in multiple libraries, including statsmodels, tf_sts, kats, and pyflux. Currently, the statsforecast package provides the fastest NumBa implementations of these methods, and it has been adopted in multiple popular open-source Python frameworks, such as darts and sktime. Other libraries, including gluonts have Python API R-connections that enable comparisons with well-established methods at the cost of R dependency frictions. Finally, higher-level libraries, including darts, sktime, tslearn, pmdarima, and seglearn, provide API access to various time series forecasting models.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Usage Example and Benchmarks", "weight": 1.0} -->

The code example below highlights the usability and wide rate of available reconciliation methods in HierarchicalForecast. It predicts eight months of the 57 series of the Labour dataset using AutoARIMA base model and later reconciles the base predictions using the BottomUp, TopDown, and MinTrace methods. We generate prediction intervals with 80% and 90% coverage using the BOOTSTRAP technique.

<!-- chunk {"id": "body-0014", "role": "body", "section": "Usage Example and Benchmarks", "weight": 1.0} -->

1 TopDown/PERMBU results are unavailable because, they cannot be applied to group hierarchical structures. 2 The combinations NORMALITY-TopDown and BOOTSTRAP-TopDown are yet to be implemented, this has never been done before.

<!-- chunk {"id": "body-0015", "role": "body", "section": "Conclusion and Plans", "weight": 1.5} -->

We present HierarchicalForecast, a Python open-source library dedicated to hierarchical time series forecasting. The library integrates publicly available processed datasets, evaluation metrics, and a curated set of highly efficient statistical baselines. We provide examples and references to extensive experiments to show how to use the baselines and evaluate their empirical performance. This work will help the Machine Learning forecasting community by bridging the gap between statistical and econometric modeling and providing benchmark tools for developing novel hierarchical forecasting algorithms compared to the well-established methods. We intend to continue maintaining and improving the repository and promoting collaboration across the forecasting research community.

<!-- chunk {"id": "body-0016", "role": "body", "section": "Acknowledments", "weight": 1.0} -->

This work was partially supported by the Defense Advanced Research Projects Agency (award FA8750-17-2-0130), the National Science Foundation (grant 2038612), the Space Technology Research Institutes grant from NASA's Space Technology Research Grants Program, the U.S. Department of Homeland Security (award 18DN-ARI-00031), and by the U.S. Army Contracting Command (contracts W911NF20D0002 and W911NF22F0014 delivery order #4). The Fonds de la Recherche Scientifique supported this work -- FNRS under Grant No J.0011.20. Thanks to Pedro Mercado, Syama Rangapuram, and Chirag Nagpal for the in-depth discussion and comments on the literature and library. The authors also thank Shibo Zhou and José Morales for their software contributions.
