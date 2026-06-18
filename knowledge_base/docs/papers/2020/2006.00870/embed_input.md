From Noisy Data to Feedback Controllers: Nonconservative Design via a Matrix S-Lemma

Topics include Data-driven control, Matrix S-lemma, Noisy data, Linear matrix inequalities, Quadratic stabilization, H2 control, H-infinity control, Robust control.

Uses a matrix S-lemma to derive exact, nonconservative LMI conditions for controller synthesis from noisy input-state data. The result is a central technical tool for the informativity framework because it converts sets of data-consistent systems into tractable robust-control inequalities.

We propose a new method to obtain feedback controllers of an unknown dynamical system directly from noisy input/state data. The key ingredient of our design is a new matrix S-lemma that will be proven in this paper. We provide both strict and non-strict versions of this S-lemma, that are of interest in their own right. Thereafter, we will apply these results to data-driven control. In particular, we will derive non-conservative design methods for quadratic stabilization, H_2 and H_inf control, all in terms of data-based linear matrix inequalities. In contrast to previous work, the dimensions of our decision variables are independent of the time horizon of the experiment. Our approach thus enables control design from large data sets.

## Introduction

In this paper we study the problem of designing control laws for an unknown dynamical system using noisy data. This general problem exists for a long time, but has seen a renewed surge of interest over the last few years. The problem can be approached via different angles, for example using combined system identification and model-based control, or by computing control laws from data without the intermediate modeling step. We will contribute to the second category of methods, aiming at control design directly from noisy data.

One of the main challenges in this area is to come up with robust control laws that guarantee stability and performance of the unknown system despite the inherent uncertainty caused by noisy data. Even though there are several recent contributions addressing this issue, there are multiple open questions. In fact, one of the unsolved problems is to come up with *non-conservative* control design strategies using only a finite number of data samples.

with $M$ given by (LABEL:Mstab). We will consider norm bounded noise samples in more detail in future work.

Yet another idea for future work is to extend the current results for state-feedback design to data-driven dynamic output feedback design. Specifically, it would be interesting to see whether the matrix S-lemmas can be applied to obtain dynamic output feedback controllers from a finite set of noisy *input/output* samples.

Let ${M,N} \in {\mathbb{R}}^{{({k + n})} \times {({k + n})}}$ be symmetric matrices, partitioned as in. Assume that $N$ is nonsingular, $N_{11} \geqslant 0$ and $N_{22} < 0$. Then we have that

### Remark 8

it is possible to prove a variant Theorem 14 in which the non-strict inequality is replaced by a strict inequality, and the term $- {\betaI}$ is removed. This can be done by invoking Theorem 11. ‣ III-B S-lemma with matrix variables ‣ III The matrix-valued S-lemma ‣ From noisy data to feedback controllers: non-conservative design via a matrix S-lemma"), which is possible since implies that the set $\Sigma$ is bounded. The reason is that the coefficient matrix $N_{22}$ defining the quadratic term in is negative definite if holds.

We will tackle this problem by providing necessary and sufficient conditions on noisy data under which controllers can be obtained....
