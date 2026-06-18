<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Completely Derandomized Self-Adaptation in Evolution Strategies

Topics include Covariance matrix adaptation evolution strategy, Evolution strategies, Covariance matrix adaptation, Derandomization, Cumulation, Black-box optimization, Evolutionary computation.

<!-- chunk {"id": "summary-0002", "role": "summary", "section": "Summary", "weight": 2.0} -->

Introduces covariance matrix adaptation and cumulation for evolution strategies, producing the core CMA-ES self-adaptation mechanism for arbitrary normal mutation distributions. The paper explains how derandomized adaptation uses selected mutation steps and evolution paths to learn scaling and correlations, giving large speedups on ill-conditioned nonseparable problems.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

This paper puts forward two useful methods for self-adaptation of the mutation distribution - the concepts of derandomization and cumulation. Principle shortcomings of the concept of mutative strategy parameter control and two levels of derandomization are reviewed. Basic demands on the self-adaptation of arbitrary (normal) mutation distributions are developed. Applying arbitrary, normal mutation distributions is equiv-alent to applying a general, linear problem encoding. The underlying objective of mutative strategy parameter control is roughly to favor previously selected mutation steps in the future. If this objective is pursued rigor-ously, a completely derandomized self-adaptation scheme results, which adapts arbitrary normal mutation distributions. This scheme, called covariance matrix adaptation (CMA), meets the previously stated demands. It can still be considerably improved by cumulation - utilizing an evolution path rather than single search steps. Simulations on various test functions reveal local and global search properties of the evolution strategy with and without covariance matrix adaptation. Their performances are comparable only on perfectly scaled functions. On badly scaled, non-separable functions usually a speed up factor of several orders of magnitude is ob-served.

<!-- chunk {"id": "abstract-0004", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

On moderately mis-scaled functions a speed up factor of three to ten can be expected.
