<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

cvxRiskOpt: A Risk-Based Optimization Tool Based on CVXPY

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

We introduce cvxRiskOpt (convex Risk-based Optimization): a Python package built on top of CVXPY for the rapid prototyping of convex risk-based optimization problems and generating embeddable C code using CVXPYgen. Our package provides high-level functions to handle several risk-based optimization problems and constraints. These functions reformulate problems and constraints involving random variables and uncertainty into deterministic convex counterparts. The output is either a CVXPY Problem instance or CVXPY constraints that users can directly add to their CVXPY Problem instance. Accordingly, our package can use CVXPYgen to generate C code resulting in custom embeddable risk-based optimization problems. cvxRiskOpt is available at
