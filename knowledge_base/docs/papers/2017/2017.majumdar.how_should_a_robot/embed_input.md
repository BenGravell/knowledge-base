<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

How Should a Robot Assess Risk? Towards an Axiomatic Theory of Risk in Robotics

Topics include Risk metrics, Robot safety, Decision making under uncertainty, Distortion risk metrics, Axiomatic risk, Planning.

<!-- chunk {"id": "summary-0002", "role": "summary", "section": "Summary", "weight": 2.0} -->

Argues that robotic risk measures should be chosen by axioms rather than convenience, highlighting distortion risk metrics as a principled class. It is a useful conceptual anchor for safety-aware planning under uncertainty.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Endowing robots with the capability of assessing risk and making risk-aware decisions is widely considered a key step toward ensuring safety for robots operating under uncertainty. But, how should a robot quantify risk? A natural and common approach is to consider the framework whereby costs are assigned to stochastic outcomes-an assignment captured by a cost random variable. Quantifying risk then corresponds to evaluating a risk metric, i.e., a mapping from the cost random variable to a real number. Yet, the question of what constitutes a good risk metric has received little attention within the robotics community. The goal of this paper is to explore and partially address this question by advocating axioms that risk metrics in robotics applications should satisfy in order to be employed as rational assessments of risk. We discuss general representation theorems that precisely characterize the class of metrics that satisfy these axioms (referred to as distortion risk metrics), and provide instantiations that can be used in applications. We further discuss pitfalls of commonly used risk metrics in robotics, and discuss additional properties that one must consider in sequential decision making tasks. Our hope is that the ideas presented here will lead to a foundational framework for quantifying risk (and hence safety) in robotics applications.
