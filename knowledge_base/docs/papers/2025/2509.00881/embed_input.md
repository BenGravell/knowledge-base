<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

An Elementary Proof of the Hanson-Wright Inequality

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

The Hanson-Wright inequality establishes exponential concentration for quadratic forms X^(T) M X, where X is a vector with independent sub-Gaussian entries and with parameters depending on the Frobenius and operator norms of M. The most elementary proof to date is due to Rudelson & Vershinyn, who still rely on a convex decoupling argument due to Bourgain, followed by Gaussian comparison to arrive at the result. In this note we sidestep this decoupling and provide an arguably simpler proof reliant only on elementary properties of sub-Gaussian variables and Gaussian rotational invariance. As a consequence we also obtain improved constants.

<!-- chunk {"id": "body-0003", "role": "body", "section": "Abstract", "weight": 1.5} -->

The Hanson-Wright inequality establishes exponential concentration for quadratic forms $X^{\mathsf{T}}MX$, where $X$ is a vector with independent sub-Gaussian entries and with parameters depending on the Frobenius and operator norms of $M$. The most elementary proof to date is due to Rudelson & Vershynin, who still rely on a convex decoupling argument due to Bourgain, followed by Gaussian comparison to arrive at the result. In this note we sidestep this decoupling and provide an arguably simpler proof reliant only on elementary properties of sub-Gaussian variables and Gaussian rotational invariance. As a consequence we also obtain improved constants.

<!-- chunk {"id": "body-0004", "role": "body", "section": "The Hanson-Wright Inequality", "weight": 1.0} -->

Let $X_{1:n}$ be a sequence of mean zero, iid-$\sigma^{2}$-sub-Gaussian random variables; $\mathbf{E}\exp\left(\lambda X_{i}\right)\leq\exp\left(\frac{\lambda^{2}\sigma^{2}}{2}\right),\forall\lambda\in\mathbb{R},i\in[n]$. In this note we prove the following exponential inequality.
