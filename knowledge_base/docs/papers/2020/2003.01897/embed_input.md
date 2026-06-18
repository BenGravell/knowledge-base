Optimal Regularization Can Mitigate Double Descent

Recent empirical and theoretical studies have shown that many learning algorithms - from linear regression to neural networks - can have test performance that is non-monotonic in quantities such the sample size and model size. This striking phenomenon, often referred to as "double descent", has raised questions of if we need to re-think our current understanding of generalization. In this work, we study whether the double-descent phenomenon can be avoided by using optimal regularization. Theoretically, we prove that for certain linear regression models with isotropic data distribution, optimally-tuned l_2 regularization achieves monotonic test performance as we grow either the sample size or the model size. We also demonstrate empirically that optimally-tuned l_2 regularization can mitigate double descent for more general models, including neural networks. Our results suggest that it may also be informative to study the test risk scalings of various algorithms in the context of appropriately tuned regularization.

## Introduction

Recent works have demonstrated a ubiquitous "double descent" phenomenon present in a range of machine learning models, including decision trees, random features, linear regression, and deep neural networks Opper; Advani & Saxe; Spigler et al.; Belkin et al.; Geiger et al.; Nakkiran et al.; Belkin et al.; Hastie et al.; Bartlett et al.; Muthukumar et al.; Bibas et al.; Mitra; Mei & Montanari; Liang & Rakhlin; Liang et al.; Xu & Hsu; Dereziński et al.; Lampinen & Ganguli; Deng et al.; Nakkiran. The phenomenon is that models exhibit a peak of high test risk when they are just barely able to fit the train set, that is, to *interpolate*.

These striking observations highlight a potential gap in our understanding of generalization and an opportunity for improved methods. Ideally, we seek to use learning algorithms which robustly improve performance as the data or model size grow and do not exhibit such unexpected non-monotonic behaviors. In other words, we aim to improve the test performance in situations which would otherwise exhibit high test risk due to double descent. Here, a natural strategy would be to use a regularizer and tune its strength on a validation set.

This

When does optimally tuned regularization mitigate or remove the double-descent phenomenon?

## Discussion and Conclusion

In this work, we study the double descent phenomenon in the context of optimal regularization. We show that, while unregularized or under-regularized models often have non-monotonic behavior, appropriate regularization can eliminate this effect.

Theoretically, we prove that for certain linear regression models with isotropic covariates, optimally-tuned $\ell_{2}$ regularization achieves monotonic test performance as we grow either the sample size or the model size. These are the first non-asymptotic monotonicity results we are aware of in linear regression. We also demonstrate empirically that optimally-tuned $\ell_{2}$ regularization can mitigate double descent for more general models, including neural networks.
