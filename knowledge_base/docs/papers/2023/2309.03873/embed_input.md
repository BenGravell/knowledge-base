A Tutorial on the Non-Asymptotic Theory of System Identification

This tutorial serves as an introduction to recently developed non-asymptotic methods in the theory of - mainly linear - system identification. We emphasize tools we deem particularly useful for a range of problems in this domain, such as the covering technique, the Hanson-Wright Inequality and the method of self-normalized martingales. We then employ these tools to give streamlined proofs of the performance of various least-squares based estimators for identifying the parameters in autoregressive models. We conclude by sketching out how the ideas presented herein can be extended to certain nonlinear identification problems.

## Introduction

Machine learning methods are at an ever increasing pace being integrated into domains that have classically been within the purview of controls. There is a wide range of examples, including perception-based control, agile robotics, and autonomous driving and racing. As exciting as these developments may be, they have been most pronounced on the experimental and empirical sides. To deploy these systems safely, stably, and robustly into the real world, we argue that a principled and integrated theoretical understanding of a) fundamental limitations and b) statistical optimality is needed.

This tutorial seeks to provide a streamlined exposition of some of these recent advances that are most relevant to the non-asymptotic theory of linear system identification. Our aim is not to be encyclopedic but rather to give simple proofs of the main developments and to highlight and collect the key technical tools to arrive at these results. For a broader---and less technical---overview of the literature we point the reader to our recent survey.

## Problem Formulation

Let us now fix ideas.

where $Y_{1:T}$ is a sequence of outputs (or targets) assuming values in ${\mathbb{R}}^{d_{\mathsf{Y}}}$ and $X_{1:T}$ is a sequence of inputs (or covariates) assuming values in ${\mathbb{R}}^{d_{\mathsf{X}}}$. The goal of the user (or learner) is to recover the a priori unknown linear map $\theta^{\star} \in {\mathbb{R}}^{d_{\mathsf{Y}} \times d_{\mathsf{X}}}$ using only the observations $X_{1:T}$ and $Y_{1:T}$. The linear relationship in the regression model (1.1) is perturbed by a stochastic noise sequence $V_{1:T}$ assuming values in ${\mathbb{R}}^{d_{\mathsf{Y}}}$.
