<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Algebraic Characterization of Equivalence between Oracle-based Iterative Algorithms

Topics include Convex optimization, Linear transformations, Optimization, Control.

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

When are two algorithms the same? How can we be sure a recently proposed algorithm is novel, and not a minor variation on an existing method? In this paper, we present a framework for reasoning about equivalence between a broad class of iterative algorithms, with a focus on algorithms designed for convex optimization. We propose several notions of what it means for two algorithms to be equivalent, and provide computationally tractable means to detect equivalence. Our main definition, oracle equivalence, states that two algorithms are equivalent if they result in the same sequence of calls to the function oracles (for suitable initialization). Borrowing from control theory, we use state-space realizations to represent algorithms and characterize algorithm equivalence via transfer functions. Our framework can also identify and characterize equivalence between algorithms that use different oracles that are related via a linear fractional transformation. Prominent examples include linear transformations and function conjugation. To support the paper, we have developed a software package named Linnaeus that implements the framework to identify other iterative algorithms that are equivalent to an input algorithm.
