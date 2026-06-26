<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

The Probability Density Function of a Transformation-based Hyperellipsoid Sampling Technique

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Sun and Farooq showed that random samples can be efficiently drawn from an arbitrary n-dimensional hyperellipsoid by transforming samples drawn randomly from the unit n-ball. They stated that it was a straightforward to show that, given a uniform distribution over the n-ball, the transformation results in a uniform distribution over the hyperellipsoid, but did not present a full proof. This technical note presents such a proof.

<!-- chunk {"id": "body-0003", "role": "body", "section": "Abstract", "weight": 1.5} -->

Sun and Farooq showed that random samples can be efficiently drawn from an arbitrary $n$-dimensional hyperellipsoid by transforming samples drawn randomly from the unit $n$-ball. They stated that it was a straightforward to show that, given a uniform distribution over the $n$-ball, the transformation results in a uniform distribution over the hyperellipsoid, but did not present a full proof. This technical note presents such a proof.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Transformation-based Sampling of Hyperellipsoids", "weight": 1.0} -->

Let $X_{ellipse}$ be the set of points within an $n$-dimensional hyperellipsoid such that where $\mathbf{S} \in {\mathbb{R}}^{n \times n}$ is the hyperellipsoid matrix, and $\mathbf{x}_{centre} = {\left({\mathbf{x}_{f1} + \mathbf{x}_{f2}} \right)/2}$ is the centre of the hyperellipsoid in terms of its two focal points, $\mathbf{x}_{f1}$ and $\mathbf{x}_{f2}$.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Transformation-based Sampling of Hyperellipsoids", "weight": 1.0} -->

We can then transform points from the unit $n$-ball, $\mathbf{x}_{ball} \in X_{ball}$, to points in the hyperellipsoid, $\mathbf{x}_{ellipse} \in X_{ellipse}$, by a linear invertible transformation as, The transformation $\mathbf{L}$ is given by the Cholesky decomposition of the hyperellipsoid matrix, and the unit $n$-ball is defined in terms of the Euclidean norm, $\left| \middle| \cdot \middle| \right|_{2}$, by

<!-- chunk {"id": "body-0006", "role": "body", "section": "Resulting Probability Density Function", "weight": 1.0} -->

In response to concerns expressed by Li that sampling the hyperellipsoid by transforming uniformly-drawn samples from the unit $n$-ball, $\mathbf{x}_{ball} \sim {\mathcal{U}\left( X_{ball} \right)}$, by would not result in a uniform distribution, Sun and Farooq stated the following Lemma and Proof.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Orthogonal Hyperellipsoids", "weight": 1.0} -->

If the axes of hyperellipsoid are orthogonal, there is a coordinate frame aligned to the axes of the hyperellipsoid such that $\mathbf{S}$ will be diagonal, where $r_{i}$ is the radius of $i$-th axis of the hyperellipsoid. The transformation from the unit $n$-ball to the hyperellipsoid expressed in this aligned frame, $\mathbf{L}'$, will then be The hyperellipsoid in any arbitrary Cartesian frame can then be expressed as a rotation applied after this diagonal transformation, where $\mathbf{C} \in {SO(n)}$ is an $n$-dimensional rotation matrix. Rearranging and substituting into gives where we have made use of the orthogonality of rotation matrices, ${{\forall\mathbf{C}} \in {SO(n)}},{\mathbf{C}^{T} \equiv \mathbf{C}^{- 1}}$.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Orthogonal Hyperellipsoids", "weight": 1.0} -->

Substituting into finally gives, Where we have made use of the fact that all rotation matrices have a unity determinant, ${{{\forall\mathbf{C}} \in {SO(n)}},{{\det\left\{ \mathbf{C} \right\}} = 1}},$ and that the determinant of a diagonal matrix is the product of the diagonal terms. As expected, is exactly the inverse of the volume of an $n$-dimensional hyperellipsoid with radii $\left\{ r_{i} \right\}$.
