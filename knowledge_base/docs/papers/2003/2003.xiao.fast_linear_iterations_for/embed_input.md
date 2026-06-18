<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Fast Linear Iterations for Distributed Averaging

Topics include Distributed averaging, Consensus, Semidefinite programming, Network optimization, Linear iterations, Graph algorithms, Distributed algorithms.

<!-- chunk {"id": "summary-0002", "role": "summary", "section": "Summary", "weight": 2.0} -->

Formulates the design of the fastest symmetric linear consensus iteration for distributed averaging as a semidefinite program. The paper shows that globally optimized edge weights can substantially accelerate average consensus compared with Laplacian-based heuristics.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

We consider the problem of finding a linear iteration that yields distributed averaging consensus over a network, i.e., that asymptotically computes the average of some initial values given at the nodes. When the iteration is assumed symmetric, the problem of finding the fastest converging linear iteration can be cast as a semidefinite program, and therefore efficiently and globally solved. These optimal linear iterations are often substantially faster than several simple heuristics that are based on the Laplacian matrix of the associated graph.
