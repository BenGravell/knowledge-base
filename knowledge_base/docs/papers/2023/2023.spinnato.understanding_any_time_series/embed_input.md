<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Understanding Any Time Series Classifier with a Subsequence-based Explainer

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

The growing availability of time series data has increased the usage of classifiers for this data type. Unfortunately, state-of-the-art time series classifiers are black-box models and, therefore, not usable in critical domains such as healthcare or finance, where explainability can be a crucial requirement. This paper presents a framework to explain the predictions of any black-box classifier for univariate and multivariate time series. The provided explanation is composed of three parts. First, a saliency map highlighting the most important parts of the time series for the classification. Second, an instance-based explanation exemplifies the black-box’s decision by providing a set of prototypical and counterfactual time series. Third, a factual and counterfactual rule-based explanation, revealing the reasons for the classification through logical conditions based on subsequences that must, or must not, be contained in the time series. Experiments and benchmarks show that the proposed method provides faithful, meaningful, stable, and interpretable explanations.
