<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

HyperLogLog: The Analysis of a Near-Optimal Cardinality Estimation Algorithm

Topics include Cardinality estimation, Streaming algorithms, Probabilistic sketches, Hashing, Distinct counting, HyperLogLog.

<!-- chunk {"id": "summary-0002", "role": "summary", "section": "Summary", "weight": 2.0} -->

Derives and analyzes HyperLogLog, the now-standard streaming sketch for approximate distinct counting. Its key contribution is a memory-efficient estimator with predictable relative error that composes naturally across distributed streams.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

This extended paper describes and analyses a near-optimal probabilistic algorithm, HyperLogLog, dedicated to estimating the number of distinct elements (the cardinality) of very large data ensembles. Using an auxiliary memory of m units (typically, short bytes), HyperLogLog performs a single pass over the data and produces an estimate of the cardinality such that the relative accuracy (the standard error) is typically about 1.04/sqrt(m). This improves on the best previously known cardinality estimator, LogLog, whose accuracy can be matched by consuming only 64% of the original memory. For instance, the new algorithm makes it possible to estimate cardinalities well beyond 10^9 with a typical accuracy of 2% while using a memory of only 1.5 kilobytes. The algorithm parallelizes optimally and adapts to the sliding window model.
