Conditional Validity of Inductive Conformal Predictors

Topics include Conformal prediction, Inductive conformal prediction, Conditional validity, Marginal coverage, Prediction sets, Distribution-free inference, Machine learning theory.

Studies what kinds of conditional coverage guarantees can and cannot be obtained by inductive, split-sample conformal predictors. The paper is a key bridge between the practical efficiency of inductive conformal prediction and the stronger validity notions that are often desired in deployment.

Conformal predictors are set predictors that are automatically valid in the sense of having coverage probability equal to or exceeding a given confidence level. Inductive conformal predictors are a computationally efficient version of conformal predictors satisfying the same property of validity. However, inductive conformal predictors have been only known to control unconditional coverage probability. This paper explores various versions of conditional validity and various ways to achieve them using inductive conformal predictors and their modifications.

## Introduction

This paper continues study of the method of conformal prediction, introduced in Vovk et al. and Saunders et al. and further developed in Vovk et al.. An advantage of the method is that its predictions (which are set rather than point predictions) automatically satisfy a finite-sample property of validity. Its disadvantage is its relative computational inefficiency in many situations. A modification of conformal predictors, called inductive conformal predictors, was proposed in Papadopoulos et al. with the purpose of improving on the computational efficiency of conformal predictors.

Most of the literature on conformal prediction studies the behavior of set predictors in the online mode of prediction, perhaps because the property of validity can be stated in an especially strong form in the on-line mode. The online mode, however, is much less popular in applications of machine learning than the batch mode of prediction. This paper follows the recent papers by Lei et al., Lei and Wasserman, and Lei et al. studying properties of conformal prediction in the batch mode; we, however, concentrate on inductive conformal prediction....

The known property of validity of inductive conformal predictors (Proposition 1. ‣ 2 Inductive conformal predictors ‣ Conditional validity of inductive conformal predictors")) can be stated in the traditional statistical language by saying that they are $1 - \epsilon$ expectation tolerance regions, where $\epsilon$ is the significance level. In classical statistics, however, there are two kinds of tolerance regions: $1 - \epsilon$ expectation tolerance regions and PAC-type $1 - \delta$ tolerance regions for a proportion $1 - \epsilon$, in the terminology of Fraser....

A disadvantage of inductive conformal predictors is their potential predictive inefficiency: indeed, the calibration set is wasted as far as the development of the prediction rule $f$ in is concerned, and the proper training set is wasted as far as the calibration of conformity scores into p-values is concerned. Conformal predictors use the full training set for both purposes, and so can be expected to be significantly more efficient....

Suppose $\mathbf{X}$ is a separable metric space equipped with the Borel $\sigma$-algebra. Let $\epsilon \in {}$. Suppose that a set predictor $\Gamma$ has $1 - \epsilon$ object conditional validity....
