<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Risk-aware Product Decisions in A/B Tests with Multiple Metrics

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

In the past decade, AB tests have become the standard method for making product decisions in tech companies. They offer a scientific approach to product development, using statistical hypothesis testing to control the risks of incorrect decisions. Typically, multiple metrics are used in AB tests to serve different purposes, such as establishing evidence of success, guarding against regressions, or verifying test validity. To mitigate risks in AB tests with multiple outcomes, it's crucial to adapt the design and analysis to the varied roles of these outcomes. This paper introduces the theoretical framework for decision rules guiding the evaluation of experiments at Spotify. First, we show that if guardrail metrics with non-inferiority tests are used, the significance level does not need to be multiplicity-adjusted for those tests. Second, if the decision rule includes non-inferiority tests, deterioration tests, or tests for quality, the type II error rate must be corrected to guarantee the desired power level for the decision. We propose a decision rule encompassing success, guardrail, deterioration, and quality metrics, employing diverse tests. This is accompanied by a design and analysis plan that mitigates risks across any data-generating process. The theoretical results are demonstrated using Monte Carlo simulations.
