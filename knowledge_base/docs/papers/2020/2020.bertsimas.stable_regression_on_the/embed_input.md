<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Stable Regression: On the Power of Optimization over Randomization

Topics include Robust optimization, Regression, Stability, Training-validation split, Feature selection, Distributionally robust optimization.

<!-- chunk {"id": "summary-0002", "role": "summary", "section": "Summary", "weight": 2.0} -->

Replaces random train-validation splitting for regression with an optimization problem that selects harder, more stable splits. The paper connects stable predictive performance and support recovery to robustness over subpopulations, giving an optimization-based alternative to repeated random resampling and cross-validation.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

We investigate and ultimately suggest remediation to the widely held belief that the best way to train regression models is via random assignment of our data to training and validation sets. In particular, we show that taking a robust optimization approach, and optimally selecting such training and validation sets, leads to models that not only perform significantly better than their randomly constructed counterparts in terms of prediction error, but more importantly, are considerably more stable in the sense that the standard deviation of the resulting predictions, as well as of the model coefficients, is greatly reduced. Moreover, we show that this optimization approach to training is far more effective at recovering the true support of a given data set, i.e., correctly identifying important features while simultaneously excluding spurious ones. We further compare the robust optimization approach to cross validation and find that optimization continues to have a performance edge albeit smaller. Finally, we show that this optimization approach to training is equivalent to building models that are robust to all subpopulations in the data, and thus in particular are robust to the hardest subpopulation, which leads to interesting domain specific interpretations through the use of optimal classification trees. The proposed robust optimization algorithm is efficient and scales training to essentially any desired size.
