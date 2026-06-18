A Matrix Finsler's Lemma with Applications to Data-Driven Control

Topics include Data-driven control, Matrix Finsler's lemma, Matrix S-lemma, Noisy data, Linear matrix inequalities, Lure systems, Robust control, Quadratic constraints.

Provides a matrix Finsler lemma that unifies exact-data and noisy-data direct control conditions under one quadratic-constraint view. It clarifies how several data-driven LMI synthesis results fit together and extends the machinery to Lur'e systems.

In a recent paper it was shown how a matrix S-lemma can be applied to construct controllers from noisy data. The current paper complements these results by proving a matrix version of the classical Finsler's lemma. This matrix Finsler's lemma provides a tractable condition under which all matrix solutions to a quadratic equality also satisfy a quadratic inequality. We will apply this result to bridge known data-driven control design techniques for both exact and noisy data, thereby revealing a more general theory. The result is also applied to data-driven control of Lur'e systems.

## Introduction

Data-driven control refers to all approaches that use measured data as starting point in the control design. This design can be done either indirectly via model identification, or by directly mapping data to control policies. Both paradigms have a long history, but data-driven control has recently witnessed a renewed surge of interest, partly because of the widespread availability of data and the successes of machine learning algorithms. We mention contributions to data-driven optimal control, predictive control and robust tracking control, nonlinear control and system level synthesis.

Several recent papers aim at deriving tractable data-based linear matrix inequalities (LMI's) that enable direct data-driven control design. The paper proposes a semidefinite programming relaxation for the stabilization of switched systems. The authors of provide a data-based parameterization of controllers, which is applied to stabilization and optimal control problems. In, notions of informative data are defined, which leads to necessary and sufficient data-based conditions for different analysis and control problems....

To prove the "only if" part, suppose that there exist $P = P^{\top} > 0$ and $K$ such that holds for all ${(A,B,E)} \in \Sigma$. Using a Schur complement argument twice this implies holds. Analogous to \[17, Lem. 15\] it can be shown that $A + {BK}$ and $E$ are the same for all ${(A,B,E)} \in \Sigma$. This implies that still holds for all ${(A,B,E)} \in \Sigma$ if we replace the strict inequality by a non-strict inequality and $P^{- 1}$ by $P^{- 1} - {\betaI}$ for some sufficienctly small $\beta > 0$. Define

By Theorem 1 ‣ III The matrix Finsler’s lemma ‣ A Matrix Finsler’s Lemma with Applications to Data-Driven Control"), we conclude that there exists an $\alpha \in {\mathbb{R}}$ such that ${M - {\alphaN}} \geq 0$. Finally, by defining the variables $Q:=P^{- 1}$ and $L:={KQ}$ and using a Schur complement argument, we see that ${CQC^{\top}} < 4$ and is feasible. ∎

### Proposition 5 (Strict Finsler's lemma)

### Proposition 3 (Strict matrix S-lemma)

In this section, we will apply the matrix Finsler's lemma to find a new characterization of informativity for stabilization in the exact data case, thereby bridging the exact and noisy formulations. The result can be formulated as follows.
