<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Signal Recovery from Random Measurements via Orthogonal Matching Pursuit

Topics include Compressed sensing, Orthogonal matching pursuit, Sparse recovery, Random measurements, Greedy algorithms, Signal reconstruction.

<!-- chunk {"id": "summary-0002", "role": "summary", "section": "Summary", "weight": 2.0} -->

Analyzes when orthogonal matching pursuit can recover sparse signals from random measurements. The paper gives theoretical support for a simple greedy alternative to convex L1 recovery in compressed sensing.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

This paper demonstrates theoretically and empirically that a greedy algorithm called Orthogonal Matching Pursuit (OMP) can reliably recover a signal with m nonzero entries in dimension d given O(m log d) random linear measurements of that signal. This is a massive improvement over previous results, which require O(m^2) measurements. The new results for OMP are comparable with recent results for another approach called Basis Pursuit (BP). In some settings, the OMP algorithm is faster and easier to implement, so it is an attractive alternative to BP for signal recovery problems.
