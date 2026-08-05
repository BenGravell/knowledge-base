<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

A New Proof of Sub-Gaussian Norm Concentration Inequality

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

We present a new method for proving the norm concentration inequality of sub-Gaussian variables. Our proof is based on an averaged version of the moment generating function, termed the averaged moment generating function. Our method applies to both vector cases to bound the vector norm and matrix cases to bound the operator norm. Compared with the widely adopted epsilon-net technique-based proof of the sub-Gaussian norm concentration inequality, our method does not rely on the union bound and promises a tighter concentration bound.

<!-- chunk {"id": "body-0003", "role": "body", "section": "Abstract", "weight": 1.5} -->

We present a new method for proving the norm concentration inequality of sub-Gaussian variables. Our proof is based on an averaged version of the moment generating function, termed the averaged moment generating function. Our method applies to both vector cases to bound the vector norm and matrix cases to bound the operator norm. Compared with the widely adopted $\varepsilon$-net technique-based proof of the sub-Gaussian norm concentration inequality, our method does not rely on the union bound and promises a tighter concentration bound.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Sub-Gaussian Norm Concentration Inequality", "weight": 1.0} -->

Concentration inequalities are mathematical tools in probability theory that describe how a random variable deviates from some value, typically its expectation. Some commonly used instances include Markov's inequality, Chebyshev's inequality, and Chernoff bounds. These concentration inequalities play an essential role in various fields, including probability theory, statistics, machine learning, finance, etc, providing probabilistic guarantees when dealing with random quantities. Many probability distributions exhibit concentration properties, among which we consider an important class known as sub-Gaussian distribution. The sub-Gaussian random variable is formally defined as follows.

<!-- chunk {"id": "body-0005", "role": "body", "section": "New Proof based on Averaged Moment Generating Function", "weight": 1.0} -->

To analyze the concentration property of $\| X\|$, the $\varepsilon$-net strategy as described above first analyzes the concentration of the one-dimensional projection $\ell^{\top}X$ of $X$ using the Markov's inequality and then applies the union bound to establish the concentration bound for $\| X\|$. This gives rise to one question: is there a more direct approach to establish the concentration of $\| X\|$?

<!-- chunk {"id": "body-0006", "role": "body", "section": "New Proof based on Averaged Moment Generating Function", "weight": 1.0} -->

In this paper, we present a new proof of the sub-Gaussian norm concentration inequality that directly analyzes $\| X\|$. The key of our proof is a novel mathematical tool named the averaged moment generating function (AMGF) that bears similarity with ${\mathbb{E}}_{X}{(e^{\lambda{\| X\|}})}$.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Generalization to Sub-Gaussian Random Matrices", "weight": 1.0} -->

In this section, we extend our AMGF-based method to study the norm concentration property of sub-Gaussian matrices. In particular, we focus on the operator norm, which plays a pivotal role in applications related to random matrix theory. Recall that a random matrix $A \in {\mathbb{R}}^{m \times n}$ is said to be sub-Gaussian with variance proxy $\sigma^{2}$ if ${{\mathbb{E}}{(A)}} = 0$ and for any $\lambda \in {\mathbb{R}}$ \[1, Section 1.2\] Following Definition 2.1.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Generalization to Sub-Gaussian Random Matrices", "weight": 1.0} -->

‣ 2 New Proof based on Averaged Moment Generating Function ‣ A New Proof of Sub-Gaussian Norm Concentration Inequality"), we define the AMGF of a random matrix $A$ as ${\Phi_{A}{(\lambda)}} = {{\mathbb{E}}_{A}{({\Phi_{m,n}{({\lambda A})}})}}$, where the energy function Similar to the vector setting, the property of exponential growth holds for $\Phi_{m,n}{({\lambda A})}$.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Conclusion", "weight": 1.5} -->

This paper presents an alternative proof of the sub-Gaussian norm concentration inequality that applies to both random vectors and random matrices. The key to our proof is a modified MGF dubbed AMGF. The AMGF depends solely on the distribution of the norm of a random vector/matrix $X$, making it particularly suitable for analyzing the concentration properties of $\| X\|$. Unlike existing methods that rely on the union bound, our proof directly addresses ${\mathbb{P}}\left( {{\| X\|} > r} \right)$, leading to a more refined analysis. Our method can also be applied to study the norm concentration of some other classes of distributions such as sub-exponential distributions. Beyond its immediate application to the norm concentration, the AMGF and the associated energy function $\Phi_{n}$ hold the potential for broader and lasting contributions to probability theory and related fields.
