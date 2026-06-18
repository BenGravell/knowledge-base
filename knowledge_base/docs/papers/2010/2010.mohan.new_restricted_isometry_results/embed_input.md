<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

New Restricted Isometry Results for Noisy Low-rank Recovery

Topics include Low-rank recovery, Restricted isometry property, Reweighted nuclear norm, Trace minimization, Noisy measurements, Compressed sensing, Convex relaxation.

<!-- chunk {"id": "summary-0002", "role": "summary", "section": "Summary", "weight": 2.0} -->

Analyzes noisy low-rank matrix recovery through RIP-style error bounds, with special attention to reweighted trace minimization. The main value is a sharper comparison between reweighted trace heuristics and plain nuclear-norm recovery, plus improved RIP constants for the nuclear-norm baseline itself.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

The problem of recovering a low-rank matrix consistent with noisy linear measurements is a fundamental problem with applications in machine learning, statistics, and control. Reweighted trace minimization, which extends and improves upon the popular nuclear norm heuristic, has been used as an iterative heuristic for this problem. In this paper, we present theoretical guarantees for the reweighted trace heuristic. We quantify its improvement over nuclear norm minimization by proving tighter bounds on the recovery error for low-rank matrices with noisy measurements. Our analysis is based on the Restricted Isometry Property (RIP) and extends some recent results from Compressed Sensing. As a second contribution, we improve the existing RIP recovery results for the nuclear norm heuristic, and show that recovery happens under a weaker assumption on the RIP constants.
