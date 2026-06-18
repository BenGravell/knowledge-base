The Probability Density Function of a Transformation-based Hyperellipsoid Sampling Technique

Sun and Farooq showed that random samples can be efficiently drawn from an arbitrary n-dimensional hyperellipsoid by transforming samples drawn randomly from the unit n-ball. They stated that it was a straightforward to show that, given a uniform distribution over the n-ball, the transformation results in a uniform distribution over the hyperellipsoid, but did not present a full proof. This technical note presents such a proof.

## Abstract

Sun and Farooq showed that random samples can be efficiently drawn from an arbitrary $n$-dimensional hyperellipsoid by transforming samples drawn randomly from the unit $n$-ball. They stated that it was a straightforward to show that, given a uniform distribution over the $n$-ball, the transformation results in a uniform distribution over the hyperellipsoid, but did not present a full proof. This technical note presents such a proof.

## Transformation-based Sampling of Hyperellipsoids

where we have made use of the orthogonality of rotation matrices, ${{\forall\mathbf{C}} \in {SO(n)}},{\mathbf{C}^{T} \equiv \mathbf{C}^{- 1}}$. Substituting into finally gives,

Where we have made use of the fact that all rotation matrices have a unity determinant, ${{{\forall\mathbf{C}} \in {SO(n)}},{{\det\left\{ \mathbf{C} \right\}} = 1}},$ and that the determinant of a diagonal matrix is the product of the diagonal terms. As expected, is exactly the inverse of the volume of an $n$-dimensional hyperellipsoid with radii $\left\{ r_{i} \right\}$.

For clarity, the full proof is presented below.

### Lemma 1

From, we can calculate the inverse transformation as,

Let $X_{ellipse}$ be the set of points within an $n$-dimensional hyperellipsoid such that

where $\mathbf{S} \in {\mathbb{R}}^{n \times n}$ is the hyperellipsoid matrix, and $\mathbf{x}_{centre} = {\left( {\mathbf{x}_{f1} + \mathbf{x}_{f2}} \right)/2}$ is the centre of the hyperellipsoid in terms of its two focal points, $\mathbf{x}_{f1}$ and $\mathbf{x}_{f2}$. We can then transform points from the unit $n$-ball, $\mathbf{x}_{ball} \in X_{ball}$, to points in the hyperellipsoid, $\mathbf{x}_{ellipse} \in X_{ellipse}$, by a linear invertible transformation as,

The transformation $\mathbf{L}$ is given by the Cholesky decomposition of the hyperellipsoid matrix,

and the unit $n$-ball is defined in terms of the Euclidean norm, $\left| \middle| \cdot \middle| \right|_{2}$, by

## Resulting Probability Density Function

In response to concerns expressed by Li that sampling the hyperellipsoid by transforming uniformly-drawn samples from the unit $n$-ball, $\mathbf{x}_{ball} \sim {\mathcal{U}\left( X_{ball} \right)}$, by would not result in a uniform distribution, Sun and Farooq stated the following Lemma and Proof.
