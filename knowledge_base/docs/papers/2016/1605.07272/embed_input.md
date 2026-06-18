Matrix Completion Has No Spurious Local Minimum

Matrix completion is a basic machine learning problem that has wide applications, especially in collaborative filtering and recommender systems. Simple non-convex optimization algorithms are popular and effective in practice. Despite recent progress in proving various non-convex algorithms converge from a good initial point, it remains unclear why random or arbitrary initialization suffices in practice. We prove that the commonly used non-convex objective function for \textit{positive semidefinite} matrix completion has no spurious local minima - all local minima must also be global. Therefore, many popular optimization algorithms such as (stochastic) gradient descent can provably solve positive semidefinite matrix completion with \textit{arbitrary} initialization in polynomial time. The result can be generalized to the setting when the observed entries contain noise. We believe that our main proof strategy can be useful for understanding geometric properties of other statistical problems involving partial or noisy observations.

## Introduction

Matrix completion is the problem of recovering a low rank matrix from partially observed entries. It has been widely used in collaborative filtering and recommender systems, dimension reduction and multi-class learning. There has been extensive work on designing efficient algorithms for matrix completion with guarantees. One earlier line of results (see and the references therein) rely on convex relaxations. These algorithms achieve strong statistical guarantees, but are quite computationally expensive in practice.

More recently, there has been growing interest in analyzing non-convex algorithms for matrix completion. Let $M \in {\mathbb{R}}^{d \times d}$ be the target matrix with rank $r \ll d$ that we aim to recover, and let $\Omega = {\{{(i,j)}:{M_{i,j}\text{~is observed}}\}}$ be the set of observed entries. These methods are instantiations of optimization algorithms applied to the objective^11^1In this paper, we focus on the symmetric case when the true $M$ has a symmetric decomposition $M = {ZZ^{T}}$. Some of previous papers work on the asymmetric case when $M = {ZW^{T}}$, which is harder than the symmetric case.,

## Conclusions

Although the matrix completion objective is non-convex, we showed the objective function has very nice properties that ensures the local minima are also global. This property gives guarantees for many basic optimization algorithms. An important open problem is the robustness of this property under different model assumptions: Can we extend the result to handle asymmetric matrix completion? Is it possible to add weights to different entries (similar to the settings studied in )? Can we replace the objective function with a different distance measure rather than Frobenius norm (which is related to works on 1-bit matrix sensing )?...

### Lemma 4.3

Intuitively, this proof says that the norm of a critical point $x$ is controlled by its correlation with $z$. Here at the lasa sampling version of the f aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa ∎

Here we recall that $\alpha$ was chosen to be ${10\mu}/\sqrt{d}$ and $\lambda$ is chosen to be large so that the $\alpha$ dominates the second term $\mu\sqrt{p/\lambda}$ in the setting of Theorem 4.2.

These algorithms are much faster than the convex relaxation algorithms, which is crucial for their empirical success in large-scale collaborative...
