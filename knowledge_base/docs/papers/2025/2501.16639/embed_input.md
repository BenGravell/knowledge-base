Finite Sample Analysis of Open-loop Subspace Identification Methods

Subspace identification methods (SIMs) are known for their simple parameterization for MIMO systems and robust numerical properties. However, a comprehensive statistical analysis of SIMs remains an open problem. Following a three-step procedure generally used in SIMs, this work presents a finite sample analysis for open-loop SIMs. In Step 1 we begin with a parsimonious SIM. Leveraging a recent analysis of an individual ARX model, we obtain a union error bound for a Hankel-like matrix constructed from a bank of ARX models. Step 2 involves model reduction via weighted singular value decomposition (SVD), where we use robustness results for SVD to obtain error bounds on extended controllability and observability matrices, respectively. The final Step 3 focuses on deriving error bounds for system matrices, where two different realization algorithms, the MOESP type and the CVA type, are studied. Our results not only agree with classical asymptotic results, but also show how much data is needed to guarantee a desired error bound with high probability. The proposed method generalizes related finite sample analyses and applies broadly to many variants of SIMs.

## Introduction

Originating from the celebrated Ho-Kalman algorithm \[\], subspace identification methods (SIMs) have proven extremely useful for estimating linear state-space models and became one of the mainstream approaches in system identification. Over the past 50 years, numerous efforts have been made to develop improved algorithms and gain a deeper understanding of them. For a comprehensive overview of SIMs, we refer to. Overall speaking, SIMs can be categorized into two types, namely, the open-loop and closed-loop. Open-loop SIMs were developed first and formed the basis for the development of closed-loop ones....

### Related Work

## Conclusion

This paper presents a finite sample analysis for a large class of open-loop SIMs. Compared with the-state-of-art that mainly analyzes the performance of the Ho-Kalman algorithm or similar variants, we investigate one of the most representative SIMs, PARSIM. Our analysis establishes a more general PE condition, and takes the different weighting matrices and two realization algorithms into account....

### Definition 4.1

where $\Pi_{U_{f}}^{\perp} = {I - {U_{f}^{\top}{({U_{f}U_{f}^{\top}})}^{- 1}U_{f}}}$. Although the estimate ${\hat{\mathcal{H}}}_{fp}$ is consistent \[\], the one-step regression method cannot preserve the lower-triangular Toeplitz structure of the transmission matrix $G_{f}$, which is responsible for recording the impact of future input $U_{f}$ on future output $Y_{f}$. Due to the loss of this structure in ${\hat{G}}_{f}$, the model format is not causal anymore, which poses a challenge in statistical analysis.

After obtaining an error bound on ${\overset{\sim}{\Theta}}_{i}$ in each ARX model, we proceed to bound the total error of $\mathcal{H}_{fp}$, which is crucial for our subsequent analysis. Based on the norm relation between a block matrix and its blocks in Lemma 13.9. ‣ 13 Technical Lemmas ‣ Finite Sample Analysis of Open-loop Subspace Identification Methods"), it is straightforward to obtain a total bound on ${\hat{\mathcal{H}}}_{fp} - \mathcal{H}_{fp}$ from each bound $\left\| {\overset{\sim}{\Theta}}_{i} \right\|$.

There are some significant contributions to statistical properties of SIMs in the asymptotic regime. The consistency and asymptotic variance of SIMs are analyzed in and, respectively....
