Optimizing Neural Networks with Kronecker-factored Approximate Curvature

Topics include Low-rank models, Stochastic optimization, Gradient descent, Stochastic gradients, Natural gradients, Neural networks, Optimization, K-FAC, Stochastic gradient descent.

We propose an efficient method for approximating natural gradient descent in neural networks which we call Kronecker-Factored Approximate Curvature (K-FAC). K-FAC is based on an efficiently invertible approximation of a neural network's Fisher information matrix which is neither diagonal nor low-rank, and in some cases is completely non-sparse. It is derived by approximating various large blocks of the Fisher (corresponding to entire layers) as being the Kronecker product of two much smaller matrices. While only several times more expensive to compute than the plain stochastic gradient, the updates produced by K-FAC make much more progress optimizing the objective, which results in an algorithm that can be much faster than stochastic gradient descent with momentum in practice. And unlike some previously proposed approximate natural-gradient/Newton methods which use high-quality non-diagonal curvature matrices (such as Hessian-free optimization), K-FAC works very well in highly stochastic optimization regimes....

## Introduction

The problem of training neural networks is one of the most important and highly investigated ones in machine learning. Despite work on layer-wise pretraining schemes, and various sophisticated optimization methods which try to approximate Newton-Raphson updates or natural gradient updates, stochastic gradient descent (SGD), possibly augmented with momentum, remains the method of choice for large-scale neural network training.

From the work on Hessian-free optimization (HF) and related methods we know that updates computed using local curvature information can make much more progress per iteration than the scaled gradient. The reason that HF sees fewer practical applications than SGD are twofold. Firstly, its updates are much more expensive to compute, as they involve running linear conjugate gradient (CG) for potentially hundreds of iterations, each of which requires a matrix-vector product with the curvature matrix (which are as expensive to compute as the stochastic gradient on the current mini-batch)....

an implementation that better exploits opportunities for parallelism described in Section 8

exploitation of massively distributed computation in order to compute high-quality estimates of the gradient

Given an update proposal $\Delta$ produced by multiplying the negative gradient $- {\nabla h}$ by our approximate Fisher inverse (subject to the Tikhonov technique described in the previous subsection), the second stage of our proposed damping scheme re-scales $\Delta$ according to the quadratic model $M$ as computed with the exact $F$, to produce a final update $\delta = {\alpha\Delta}$.

Figure 6, which compares ${\breve{F}}^{- 1}$ and ${\hat{F}}^{- 1}$ to ${\overset{\sim}{F}}^{- 1}$, paints an arguably more interesting and relevant picture, as the quality of the approximation of the natural gradient will be roughly proportional^22^2The error in any approximation $F_{0}^{- 1}{\nabla h}$ of the natural gradient $F^{- 1}{\nabla h}$ will be roughly proportional to the error in the approximation $F_{0}^{- 1}$ of the associated *inverse* Fisher $F^{- 1}$, since ${\|{{F^{- 1}{\nabla h}} - {F_{0}^{- 1}{\nabla h}}}\|} \leq {{\|{\nabla h}\|}{\|{F^{- 1} - F_{0}^{- 1}}\|}}$. to the quality of approximation of the *inverse* Fisher....
