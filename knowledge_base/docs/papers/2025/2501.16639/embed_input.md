Finite Sample Analysis of Open-loop Subspace Identification Methods

Subspace identification methods (SIMs) are known for their simple parameterization for MIMO systems and robust numerical properties. However, a comprehensive statistical analysis of SIMs remains an open problem. Following a three-step procedure generally used in SIMs, this work presents a finite sample analysis for open-loop SIMs. In Step 1 we begin with a parsimonious SIM. Leveraging a recent analysis of an individual ARX model, we obtain a union error bound for a Hankel-like matrix constructed from a bank of ARX models. Step 2 involves model reduction via weighted singular value decomposition (SVD), where we use robustness results for SVD to obtain error bounds on extended controllability and observability matrices, respectively. The final Step 3 focuses on deriving error bounds for system matrices, where two different realization algorithms, the MOESP type and the CVA type, are studied. Our results not only agree with classical asymptotic results, but also show how much data is needed to guarantee a desired error bound with high probability. The proposed method generalizes related finite sample analyses and applies broadly to many variants of SIMs.

## Introduction

Originating from the celebrated Ho-Kalman algorithm, subspace identification methods (SIMs) have proven extremely useful for estimating linear state-space models and became one of the mainstream approaches in system identification. Over the past 50 years, numerous efforts have been made to develop improved algorithms and gain a deeper understanding of them. For a comprehensive overview of SIMs, we refer to. Overall speaking, SIMs can be categorized into two types, namely, the open-loop and closed-loop. Open-loop SIMs were developed first and formed the basis for the development of closed-loop ones.

## Contributions

The

\(1\) We develop a robust and scalable framework for finite sample analysis of a broad class of SIMs. To avoid non-causal models caused by the projection step in classical SIMs, we propose to use PARSIM to enforce a causal model. Such a choice brings convenience to statistical analysis, and the method can be applied to other ARX-based SIMs, such as SSARX and PBSID.

\(2\) We establish a more general PE condition. Compared with related studies that only include past inputs and past outputs as regressors, our work also includes future inputs as regressors, leading to a more general PE condition. This broader PE condition is instrumental in deriving error bounds and in analyzing the use of data-dependent weighting matrices. Therefore, it serves as a contribution of independent interest.

## Conclusion

This paper presents a finite sample analysis for a large class of open-loop SIMs. Compared with the-state-of-art that mainly analyzes the performance of the Ho-Kalman algorithm or similar variants, we investigate one of the most representative SIMs, PARSIM. Our analysis establishes a more general PE condition, and takes the different weighting matrices and two realization algorithms into account.
