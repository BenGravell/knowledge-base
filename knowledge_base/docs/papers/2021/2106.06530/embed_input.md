Label Noise SGD Provably Prefers Flat Global Minimizers

In overparametrized models, the noise in stochastic gradient descent (SGD) implicitly regularizes the optimization trajectory and determines which local minimum SGD converges to. Motivated by empirical studies that demonstrate that training with noisy labels improves generalization, we study the implicit regularization effect of SGD with label noise. We show that SGD with label noise converges to a stationary point of a regularized loss L(theta) +lambdaR(theta), where L(theta) is the training loss, lambda is an effective regularization parameter depending on the step size, strength of the label noise, and the batch size, and R(theta) is an explicit regularizer that penalizes sharp minimizers. Our analysis uncovers an additional regularization effect of large learning rates beyond the linear scaling rule that penalizes large eigenvalues of the Hessian more than small ones. We also prove extensions to classification with general loss functions, SGD with momentum, and SGD with general noise covariance, significantly strengthening the prior work of Blanc et al. to global convergence and large learning rates and of HaoChen et al. to general models.

## Introduction

One of the central questions in modern machine learning theory is the generalization capability of overparametrized models trained by stochastic gradient descent (SGD). Recent work identifies the implicit regularization effect due to the optimization algorithm as one key factor in explaining the generalization of overparameterized models. This implicit regularization is controlled by many properties of the optimization algorithm including search direction, learning rate, batch size, momentum and dropout.

The parameter-dependent noise distribution in SGD is a crucial source of regularization. Blanc et al. initiated the study of the regularization effect of label noise SGD with square loss^11^1Label noise SGD computes the stochastic gradient by first drawing a sample $(x_{i},y_{i})$, perturbing $y_{i}^{\prime} = {y_{i} + \epsilon}$ with $\epsilon \sim {\{{- \sigma},\sigma\}}$, and computing the gradient with respect to $(x_{i},y_{i}^{\prime})$. by characterizing the local stability of global minimizers of the training loss. By identifying a data-dependent regularizer $R{(\theta)}$, Blanc et al....

The implicit regularizer $R{(\theta)}$ is intimately connected to data-dependent generalization bounds, which measure the Lipschitzness of the network via the network Jacobian. Specifically, Wei and Ma propose the all-layer margin, which bounds the $\text{generalization error} \lesssim {\frac{\sum_{l = 1}^{L}\mathcal{C}_{l}}{\sqrt{n}}\sqrt{\frac{1}{n}{\sum_{i = 1}^{n}\frac{1}{m_{F}{(x_{i},y_{i})}^{2}}}}}$, where $\mathcal{C}_{l}$ depends only on the norm of the parameters and $m_{F}$ is the all-layer margin....

as $R{(\theta)}$ is an upper bound on the squared norm of the Jacobian at any global minimizer $\theta$. We emphasize this bound is informal as we discarded the higher-order terms in controlling the all-layer margin, but it accurately reflects that the regularizer $R{(\theta)}$ lower bounds the all-layer margin $m_{F}$ up to higher-order terms. Therefore SGD with label noise implicitly regularizes the all-layer margin.

Therefore, when averaged over long timescales,

### Local Coupling

## Experiments

The analysis is only able to demonstrate that with sufficiently small step size $\eta$, label noise SGD initialized at $\theta^{\ast}$ locally diverges by a distance of $\eta^{0.4}$ and correspondingly decreases the regularizer by...
