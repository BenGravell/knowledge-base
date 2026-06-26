## Abstract

Sun and Farooq showed that random samples can be efficiently drawn from an arbitrary $n$-dimensional hyperellipsoid by transforming samples drawn randomly from the unit $n$-ball. They stated that it was a straightforward to show that, given a uniform distribution over the $n$-ball, the transformation results in a uniform distribution over the hyperellipsoid, but did not present a full proof. This technical note presents such a proof.

## Transformation-based Sampling of Hyperellipsoids

Let $X_{ellipse}$ be the set of points within an $n$-dimensional hyperellipsoid such that where $\mathbf{S} \in {\mathbb{R}}^{n \times n}$ is the hyperellipsoid matrix, and $\mathbf{x}_{centre} = {\left({\mathbf{x}_{f1} + \mathbf{x}_{f2}} \right)/2}$ is the centre of the hyperellipsoid in terms of its two focal points, $\mathbf{x}_{f1}$ and $\mathbf{x}_{f2}$. We can then transform points from the unit $n$-ball, $\mathbf{x}_{ball} \in X_{ball}$, to points in the hyperellipsoid, $\mathbf{x}_{ellipse} \in X_{ellipse}$, by a linear invertible transformation as, The transformation $\mathbf{L}$ is given by the Cholesky decomposition of the hyperellipsoid matrix, and the unit $n$-ball is defined in terms of the Euclidean norm, $\left| \middle| \cdot \middle| \right|_{2}$, by

## Resulting Probability Density Function

In response to concerns expressed by Li that sampling the hyperellipsoid by transforming uniformly-drawn samples from the unit $n$-ball, $\mathbf{x}_{ball} \sim {\mathcal{U}\left( X_{ball} \right)}$, by would not result in a uniform distribution, Sun and Farooq stated the following Lemma and Proof.

### Lemma 1

If the random points distributed in a hyper-ellipsoid are generated from the random points uniformly distributed in a hyper-sphere through a linear invertible non-orthogonal transformation, then the random points distributed in the hyper-ellipsoid are also uniformly distributed.

### Proof

The proof of the above lemma is very straightforward and is omitted here for brevity. The result of the lemma is further substantiated through the simulation shown in \[Figures\]. ∎ For clarity, the full proof is presented below.

### Proof

Let $p_{ball}(\cdot)$ be the probability density function of samples drawn uniformly from the unit $n$-ball of volume $\zeta_{n}$, such that, and $g(\cdot)$ be an invertible transformation from the unit $n$-ball to a hyperellipsoid, such that, Then the probability density function of samples drawn from the hyperellipsoid, $p_{ellipse}(\cdot)$, is given, From, we can calculate the inverse transformation as, whose Jacobian is then Substituting and into gives, where we have used the fact that ${g^{- 1}(\mathbf{x})} \in X_{ball}\Longrightarrow\mathbf{x} \in X_{ellipse}$. As $p_{ellipse}(\cdot)$ is constant for all $\mathbf{x}_{ellipse} \in X_{ellipse}$, this proves that transforms samples drawn uniformly from the unit $n$-ball such that they are uniformly distributed over the hyperellipsoid given by $\mathbf{S}$. ∎

### Orthogonal Hyperellipsoids

If the axes of hyperellipsoid are orthogonal, there is a coordinate frame aligned to the axes of the hyperellipsoid such that $\mathbf{S}$ will be diagonal, where $r_{i}$ is the radius of $i$-th axis of the hyperellipsoid. The transformation from the unit $n$-ball to the hyperellipsoid expressed in this aligned frame, $\mathbf{L}'$, will then be The hyperellipsoid in any arbitrary Cartesian frame can then be expressed as a rotation applied after this diagonal transformation, where $\mathbf{C} \in {SO(n)}$ is an $n$-dimensional rotation matrix. Rearranging and substituting into gives where we have made use of the orthogonality of rotation matrices, ${{\forall\mathbf{C}} \in {SO(n)}},{\mathbf{C}^{T} \equiv \mathbf{C}^{- 1}}$. Substituting into finally gives, Where we have made use of the fact that all rotation matrices have a unity determinant, ${{{\forall\mathbf{C}} \in {SO(n)}},{{\det\left\{ \mathbf{C} \right\}} = 1}},$ and that the determinant of a diagonal matrix is the product of the diagonal terms. As expected, is exactly the inverse of the volume of an $n$-dimensional hyperellipsoid with radii $\left\{ r_{i} \right\}$.
