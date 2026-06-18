<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

monviso: A Python Package for Solving Monotone Variational Inequalities

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

In this paper, we present monviso (monotone variational inequalities solver), a novel open-source Python package for solving monotone variational inequalities. We detail the package’s structure and baseline functionality, discussing a simple example that illustrates the essential methods and parameters. Moreover, we characterize how the proximal operator, which is the foundation of many iterative schemes, is handled through cvxpy, an open-source Python library for convex optimization. We list the available algorithms and describe the basic implementation of any general iterative method to enable users to build additional and (possibly new) algorithms. Finally, we illustrate several examples of possible use cases for monviso, showcasing the different applications the package can support across various fields, including control, optimization, dynamic game theory, and machine learning.
