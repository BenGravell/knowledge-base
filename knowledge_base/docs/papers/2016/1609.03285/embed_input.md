<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Disciplined Multi-Convex Programming

Topics include Low-rank models, Matrix factorization, Convex optimization, Optimization, Control.

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

A multi-convex optimization problem is one in which the variables can be partitioned into sets over which the problem is convex when the other variables are fixed. Multi-convex problems are generally solved approximately using variations on alternating or cyclic minimization. Multi-convex problems arise in many applications, such as nonnegative matrix factorization, generalized low rank models, and structured control synthesis, to name just a few. In most applications to date the multi-convexity is simple to verify by hand. In this paper we study the automatic detection and verification of multi-convexity using the ideas of disciplined convex programming. We describe an implementation of our proposed method that detects and verifies multi-convexity, and then invokes one of the general solution methods.
