Distributionally Robust Optimization over Wasserstein Balls with I.i.d. Structure

We consider distributionally robust optimization problems where the uncertainty is modeled via a structured Wasserstein ambiguity set. Specifically, the ambiguity is restricted to product measures P^(otimes) N, where P lies within a Wasserstein ball centered at an empirical distribution widehatP. This structure reflects the assumption of independent and identically distributed (i.i.d.) uncertainty components and yields a non-convex ambiguity set that is strictly contained in its unstructured counterpart, thereby reducing conservatism. The resulting optimization problem is generally intractable due to the loss of convexity. We address this by introducing a sequence of tractable convex relaxations, each admitting strong duality, and prove that this sequence converges to the original problem value under suitable conditions. Numerical examples are provided to illustrate the effectiveness of the proposed approach. As a byproduct of our proofs, we establish a novel formula, of independent interest, relating the Wasserstein distance of a mixture of product distributions to the Wasserstein distance between its constituent measures.

## Introduction

In stochastic optimization a common goal is to minimize an objective $\Psi$ over a set of feasible decisions $\Theta$, where the objective $\Psi$ is defined as an average of a family of individual uncertainty-affected loss functions $\ell:{{\Theta \times X}\rightarrow{\mathbb{R}}}$, with $X$ being a random vector of uncertain parameters defined on a probability space $(X,\Sigma,P)$. In mathematical terms, a stochastic optimization method evaluates

To avoid trivialities, we assume throughout that the feasible set $\Theta \subseteq {\mathbb{R}}^{m}$ and the support set $X \subseteq {\mathbb{R}}^{d}$ are non-empty and closed.

## Conclusions and Outlook

In this paper, we focused on Wasserstein DRO formulations where the uncertain vector exhibits an i.i.d. structure. By exploiting this structure, we construct a structured ambiguity set that only contains product distributions. To solve the resulting non-convex program, we devise a sequence of convex relaxations that, under mild conditions on the loss function, converge to the optimal solution of the original non-convex problem. Our numerical results certify how structured ambiguity sets can capture uncertainty in a more effective manner than unstructured ambiguity sets, ultimately improving the overall decision-making....

### Relaxation gap

is a potentially tighter upper bound on $S{(\ell)}$ than $U{(\ell)}$. Similar arguments have been used in to obtain convex upper bounds on the structured singular value in the domain of control theory. To obtain such a class $\mathcal{F}$ for our problem, we make the following, crucial observation: If $\pi \in \mathcal{S}_{N}$ is a permutation, then the transformation $F_{\pi}:{\ell\mapsto\ell_{\pi}}$ with ${\ell_{\pi}{(x)}} = {\ell{({\pi{(x)}})}}$, where ${\pi{(x)}} = {(x_{\pi{}},\ldots,x_{\pi{(N)}})}$ for $x \in X^{N}$, satisfies

shows that concavity of the objective function $F$ is sufficient for the absence of a relaxation gap. The following theorem gives a sufficient condition for the function ${F_{\ell}{(P)}} = {\int{\ell\text{d}P^{\otimes N}}}$ to be convex in the sense of the usual linear structure on $\mathcal{P}{(X)}$....
