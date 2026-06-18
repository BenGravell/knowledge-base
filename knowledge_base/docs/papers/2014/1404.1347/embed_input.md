The Probability Density Function of a Transformation-based Hyperellipsoid Sampling Technique

Sun and Farooq showed that random samples can be efficiently drawn from an arbitrary n-dimensional hyperellipsoid by transforming samples drawn randomly from the unit n-ball. They stated that it was a straightforward to show that, given a uniform distribution over the n-ball, the transformation results in a uniform distribution over the hyperellipsoid, but did not present a full proof. This technical note presents such a proof.

## Abstract

Sun and Farooq showed that random samples can be efficiently drawn from an arbitrary $n$-dimensional hyperellipsoid by transforming samples drawn randomly from the unit $n$-ball. They stated that it was a straightforward to show that, given a uniform distribution over the $n$-ball, the transformation results in a uniform distribution over the hyperellipsoid, but did not present a full proof. This technical note presents such a proof.

## Transformation-based Sampling of Hyperellipsoids

Let $X_{ellipse}$ be the set of points within an $n$-dimensional hyperellipsoid such that

where $\mathbf{S} \in {\mathbb{R}}^{n \times n}$ is the hyperellipsoid matrix, and $\mathbf{x}_{centre} = {\left( {\mathbf{x}_{f1} + \mathbf{x}_{f2}} \right)/2}$ is the centre of the hyperellipsoid in terms of its two focal points, $\mathbf{x}_{f1}$ and $\mathbf{x}_{f2}$. We can then transform points from the unit $n$-ball, $\mathbf{x}_{ball} \in X_{ball}$, to points in the hyperellipsoid, $\mathbf{x}_{ellipse} \in X_{ellipse}$, by a linear invertible transformation as,

The transformation $\mathbf{L}$ is given by the Cholesky decomposition of the hyperellipsoid matrix,
