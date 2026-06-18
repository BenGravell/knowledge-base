Painless Stochastic Gradient: Interpolation, Line-Search, and Convergence Rates

Topics include Gradient descent, Stochastic gradients, Robustness, Classification, Datasets, Generalization, Optimization, Stochastic gradient descent, Line search.

Recent works have shown that stochastic gradient descent (SGD) achieves the fast convergence rates of full-batch gradient descent for over-parameterized models satisfying certain interpolation conditions. However, the step-size used in these works depends on unknown quantities and SGD's practical performance heavily relies on the choice of this step-size. We propose to use line-search techniques to automatically set the step-size when training models that can interpolate the data. In the interpolation setting, we prove that SGD with a stochastic variant of the classic Armijo line-search attains the deterministic convergence rates for both convex and strongly-convex functions. Under additional assumptions, SGD with Armijo line-search is shown to achieve fast convergence for non-convex functions. Furthermore, we show that stochastic extra-gradient with a Lipschitz line-search attains linear convergence for an important class of non-convex functions and saddle-point problems satisfying interpolation. To improve the proposed methods' practical performance, we give heuristics to use larger step-sizes and acceleration....

## Introduction

Stochastic gradient descent (SGD) and its variants are the preferred optimization methods in modern machine learning. They only require the gradient for one training example (or a small "mini-batch" of examples) in each iteration and thus can be used with large datasets. These first-order methods have been particularly successful for training highly-expressive, over-parameterized models such as non-parametric regression and deep neural networks....

Variance-reduction (VR) methods are relatively new variants of SGD that improve its slow convergence rate. These methods exploit the finite-sum structure of typical loss functions arising in machine learning, achieving both the low iteration cost of SGD and the fast convergence rate of deterministic methods that compute the full-gradient in each iteration. Moreover, VR makes setting the learning rate easier and there has been work exploring the use of line-search techniques for automatically setting the step-size for these methods. These methods have resulted in impressive performance on a variety of problems....

## Conclusion

We showed that under the interpolation condition satisfied by modern over-parametrized models, simple line-search techniques for classic SGD and SEG lead to fast convergence in both theory and practice. For future work, we hope to strengthen our results for non-convex minimization using SGD with line-search and study stochastic momentum techniques under interpolation. More generally, we hope to utilize the rich literature on line-search and trust-region methods to improve stochastic optimization for machine learning.

It computes the gradient at an extrapolated point $w_{k}^{\prime}$ and uses it in the update from the current iterate $w_{k}$. Note that using the same sample $i_{k}$ and step-size $\eta_{k}$ for both steps is important for the subsequent theoretical results. We now describe a "Lipschitz" line-search strategy in order to automatically set the step-size for SEG.

### Theorem 1 (Strongly-Convex)

In this section, we give heuristics to use larger step-sizes across iterations and discuss ways to use common acceleration schemes with our line-search techniques.

Indeed, recent works have shown that when training over-parameterized models, classic SGD with a constant step-size and *without VR* can achieve the convergence rates of full-batch gradient descent....
