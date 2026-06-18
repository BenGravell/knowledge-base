From Noisy Data to Feedback Controllers: Nonconservative Design via a Matrix S-Lemma

Topics include Data-driven control, Matrix S-lemma, Noisy data, Linear matrix inequalities, Quadratic stabilization, H2 control, H-infinity control, Robust control.

Uses a matrix S-lemma to derive exact, nonconservative LMI conditions for controller synthesis from noisy input-state data. The result is a central technical tool for the informativity framework because it converts sets of data-consistent systems into tractable robust-control inequalities.

We propose a new method to obtain feedback controllers of an unknown dynamical system directly from noisy input/state data. The key ingredient of our design is a new matrix S-lemma that will be proven in this paper. We provide both strict and non-strict versions of this S-lemma, that are of interest in their own right. Thereafter, we will apply these results to data-driven control. In particular, we will derive non-conservative design methods for quadratic stabilization, H_2 and H_inf control, all in terms of data-based linear matrix inequalities. In contrast to previous work, the dimensions of our decision variables are independent of the time horizon of the experiment. Our approach thus enables control design from large data sets.

## Introduction

In this paper we study the problem of designing control laws for an unknown dynamical system using noisy data. This general problem exists for a long time, but has seen a renewed surge of interest over the last few years. The problem can be approached via different angles, for example using combined system identification and model-based control, or by computing control laws from data without the intermediate modeling step. We will contribute to the second category of methods, aiming at control design directly from noisy data.

One of the main challenges in this area is to come up with robust control laws that guarantee stability and performance of the unknown system despite the inherent uncertainty caused by noisy data. Even though there are several recent contributions addressing this issue, there are multiple open questions. In fact, one of the unsolved problems is to come up with *non-conservative* control design strategies using only a finite number of data samples.

## Discussion and conclusions

We have studied the problem of obtaining feedback controllers from noisy data. The essence of our approach has been to formulate data-driven control as the problem of determining when one quadratic matrix inequality implies another one. To get a grip on this fundamental question, we have generalized the classical S-lemma to matrix variables. The implication involving quadratic matrix inequalities is thereby *equivalent* to a linear matrix inequality in a scalar variable. We have established several versions of the matrix S-lemma, for both strict and non-strict inequalities.

We have followed up by applying our matrix S-lemma to data-driven control. In particular, we have given necessary and sufficient conditions under which stabilizing, $\mathcal{H}_{2}$, and $\mathcal{H}_{\infty}$ controllers can be obtained from noisy data. Our control design revolves around data-guided linear matrix inequalities, which can be solved efficiently using modern LMI solvers. In addition to being non-conservative, an attractive feature of our design procedure is that decision variables are *independent* of the time horizon of the experiment.
