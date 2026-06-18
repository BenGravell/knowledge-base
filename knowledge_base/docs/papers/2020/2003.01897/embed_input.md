Optimal Regularization Can Mitigate Double Descent

Recent empirical and theoretical studies have shown that many learning algorithms - from linear regression to neural networks - can have test performance that is non-monotonic in quantities such the sample size and model size. This striking phenomenon, often referred to as "double descent", has raised questions of if we need to re-think our current understanding of generalization. In this work, we study whether the double-descent phenomenon can be avoided by using optimal regularization. Theoretically, we prove that for certain linear regression models with isotropic data distribution, optimally-tuned l_2 regularization achieves monotonic test performance as we grow either the sample size or the model size. We also demonstrate empirically that optimally-tuned l_2 regularization can mitigate double descent for more general models, including neural networks. Our results suggest that it may also be informative to study the test risk scalings of various algorithms in the context of appropriately tuned regularization.

## Introduction

Recent works have demonstrated a ubiquitous "double descent" phenomenon present in a range of machine learning models, including decision trees, random features, linear regression, and deep neural networks Opper; Advani & Saxe; Spigler et al.; Belkin et al.; Geiger et al.; Nakkiran et al.; Belkin et al.; Hastie et al.; Bartlett et al.; Muthukumar et al.; Bibas et al.; Mitra; Mei & Montanari; Liang & Rakhlin; Liang et al.; Xu & Hsu; Dereziński et al.; Lampinen & Ganguli; Deng et al.; Nakkiran. The phenomenon is that models exhibit a peak of high test risk when they are just barely able to fit the train set, that is, to *interpolate*....

Figure 1: Test Risk vs. Num. Samples for Isotropic Ridge Regression in d = 500 dimensions. Unregularized regression is non-monotonic in samples, but optimally-regularized regression (λ = λo p t) is monotonic. The sample distribution is (x,y) where x ∼ 𝒩 (0,Id) and y = ⟨β*, x⟩ + 𝒩 (0,σ2) for d = 500, σ = 0.5, and ∥β*∥2 = 1. For λ &gt; 0, the ridge estimator on n samples is ${\hat{\beta}}_{\lambda}:={{\operatorname{argmin}_{\beta}\left\| {{X\beta} - \overset{\rightarrow}{y}} \right\|_{2}^{2}} + {\lambda\left\| \beta \right\|_{2}^{2}}}$....

Second, more broadly, it is open to prove sample-wise or model-wise monotonicity for more general (non-linear) models with appropriate regularizers. Addressing the monotonicity of non-linear models may require us to design new regularizers which improve the generalization when the model size is close to the sample size. It is possible that data-dependent regularizers (which depend on certain statistics of the labeled or unlabeled data) can be used to induce sample monotonicity, analogous to the approach in Section 6.1 for linear models....

Finally, it is open to understand why large neural networks in practice are often sample-monotonic in realistic regimes of sample sizes, even without careful choice of regularization.

This proof follows exactly analogously as the proof of Lemma 2 from Lemma 1, in Section A.1. ∎

### Proof of Theorem 1

We consider the same ridge regression estimator,

These striking observations highlight a potential gap in our understanding of generalization and an opportunity for improved methods. Ideally, we seek to use learning algorithms which robustly improve performance as the data or model size grow and do not exhibit such unexpected...
