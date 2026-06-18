Finite Sample Analysis for a Class of Subspace Identification Methods

While subspace identification methods (SIMs) are appealing due to their simple parameterization for MIMO systems and robust numerical realizations, a comprehensive statistical analysis of SIMs remains an open problem, especially in the non-asymptotic regime. In this work, we provide a finite sample analysis for a class of SIMs, which reveals that the convergence rates for estimating Markov parameters and system matrices are O(1/sqrt(N)), in line with classical asymptotic results. Based on the observation that the model format in classical SIMs becomes non-causal because of a projection step, we choose a parsimonious SIM that bypasses the projection step and strictly enforces a causal model to facilitate the analysis, where a bank of ARX models are estimated in parallel. Leveraging recent results from finite sample analysis of an individual ARX model, we obtain an overall error bound of an array of ARX models and proceed to derive error bounds for system matrices via robustness results for the singular value decomposition.

## Introduction

Originating from the celebrated Ho-Kalman algorithm, subspace identification methods (SIMs) have proven extremely useful for estimating linear state-space models. Over the past 50 years, numerous efforts have been made to develop improved algorithms and gain a deeper understanding of the family of SIMs, exemplified by the successful narrative of closed-loop identification. For a comprehensive overview of SIMs, we refer to. Despite their tremendous success both in theory and practice, several drawbacks have been recognized, including a lower accuracy compared to prediction error methods (PEMs) and an incomplete statistical analysis.

The

Our method can be extended to the class of SIMs that estimate an array of ARX models, for instance, the included PARSIM and SIMs based on predictor identification (PBSID). Therefore, it paves the way for comprehensively understanding the broader landscape of SIMs.

## Discussion and Future Work

This paper presents a finite sample analysis of a parsimonious SIM that estimates a bank of ARX models using OLS in parallel. It reveals that the convergence rates for estimating Markov parameters and system matrices are $\mathcal{O}{({1/\sqrt{N}})}$, consistent with classical asymptotic results. Besides, PE and the role of past horizon are also discussed. Although the algorithm studied in this paper streamlines the weighted SVD and realization steps, we believe that the findings herein pave the way for comprehensively grasping the broader landscape of the family of SIMs.

Our bound is not tight: Just like the existing bounds for partially observed systems, our bound is not tight, either. In this paper, PE in the $f$ ARX models are dealt with separately, which is convenient but somewhat conservative, given that the past output and input $Z_{p}$ is reused for every estimation. Our bound can be further optimized; however, akin to the challenge of finding an efficient SIM in the asymptotic regime, the pursuit of a lower bound in the non-saymptotic regime for partially observed systems is more challenging.
