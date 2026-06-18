A Matrix Finsler's Lemma with Applications to Data-Driven Control

Topics include Data-driven control, Matrix Finsler's lemma, Matrix S-lemma, Noisy data, Linear matrix inequalities, Lure systems, Robust control, Quadratic constraints.

Provides a matrix Finsler lemma that unifies exact-data and noisy-data direct control conditions under one quadratic-constraint view. It clarifies how several data-driven LMI synthesis results fit together and extends the machinery to Lur'e systems.

In a recent paper it was shown how a matrix S-lemma can be applied to construct controllers from noisy data. The current paper complements these results by proving a matrix version of the classical Finsler's lemma. This matrix Finsler's lemma provides a tractable condition under which all matrix solutions to a quadratic equality also satisfy a quadratic inequality. We will apply this result to bridge known data-driven control design techniques for both exact and noisy data, thereby revealing a more general theory. The result is also applied to data-driven control of Lur'e systems.

## Introduction

Data-driven control refers to all approaches that use measured data as starting point in the control design. This design can be done either indirectly via model identification, or by directly mapping data to control policies. Both paradigms have a long history, but data-driven control has recently witnessed a renewed surge of interest, partly because of the widespread availability of data and the successes of machine learning algorithms. We mention contributions to data-driven optimal control, predictive control and robust tracking control, nonlinear control and system level synthesis.

Several recent papers aim at deriving tractable data-based linear matrix inequalities (LMI's) that enable direct data-driven control design. The paper proposes a semidefinite programming relaxation for the stabilization of switched systems. The authors of provide a data-based parameterization of controllers, which is applied to stabilization and optimal control problems. In, notions of informative data are defined, which leads to necessary and sufficient data-based conditions for different analysis and control problems.

An important question in this line of work regards the conservatism of the proposed LMI conditions. In this direction, a state-of-the-art result is the matrix generalization of the classical S-lemma. This result provides an LMI condition under which all matrix solutions to one quadratic matrix inequality (QMI) also satisfy another QMI. The first inequality is motivated by the data: a quadratic bound on the noise, used , has the consequence that all systems explaining the data satisfy a QMI. The second inequality captures design specifications such as stability or $\mathcal{H}_{2}$/$\mathcal{H}_{\infty}$ performance.

In this paper we resolve this issue by introducing a matrix version of Finsler's lemma. The classical Finsler's lemma provides an LMI condition under which a quadratic inequality is the consequence of a quadratic *equality*. We will explain the difficulties in generalizing this result to matrix variables. Then, as our main contribution we will provide a Finsler's lemma for matrix variables in case the involved matrices obey some special structure. This matrix Finsler's lemma is then applied to data-driven stabilization.
