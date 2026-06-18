<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

A Bayesian Nonparametric Approach to Modeling Motion Patterns

Topics include Bayesian nonparametrics, Gaussian processes, Dirichlet processes, Motion prediction, Target tracking, Trajectory modeling, Autonomous robots.

<!-- chunk {"id": "summary-0002", "role": "summary", "section": "Summary", "weight": 2.0} -->

Models target motion as a Dirichlet-process mixture of Gaussian-process trajectory patterns, letting the number and complexity of motion modes grow with the data. The paper is important for tracking because it replaces hand-designed motion classes with a flexible learned predictor that supports interception planning from relatively sparse demonstrations.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

The most difficult - and often most essential - aspect of many interception and tracking tasks is constructing motion models of the targets. Experts rarely can provide complete information about a target's expected motion pattern, and fitting parameters for complex motion patterns can require large amounts of training data. Specifying how to parameterize complex motion patterns is in itself a difficult task. In contrast, Bayesian nonparametric models of target motion are very flexible and generalize well with relatively little training data. We propose modeling target motion patterns as a mixture of Gaussian processes (GP) with a Dirichlet process (DP) prior over mixture weights. The GP provides an adaptive representation for each individual motion pattern, while the DP prior allows us to represent an unknown number of motion patterns. Both automatically adjust the complexity of the motion model based on the available data. Our approach outperforms several parametric models on a helicopter-based car-tracking task on data collected from the greater Boston area.
