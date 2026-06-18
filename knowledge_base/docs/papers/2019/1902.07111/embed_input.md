Global Convergence of Adaptive Gradient Methods for an Over-parameterized Neural Network

Adaptive gradient methods like AdaGrad are widely used in optimizing neural networks. Yet, existing convergence guarantees for adaptive gradient methods require either convexity or smoothness, and, in the smooth setting, only guarantee convergence to a stationary point. We propose an adaptive gradient method and show that for two-layer over-parameterized neural networks - if the width is sufficiently large (polynomially) - then the proposed method converges to the global minimum in polynomial time, and convergence is robust, without the need to fine-tune hyper-parameters such as the step-size schedule and with the level of over-parametrization independent of the training error. Our analysis indicates in particular that over-parametrization is crucial for the harnessing the full potential of adaptive gradient methods in the setting of neural networks.

## Introduction

Gradient-based methods are widely used in optimizing neural networks. One crucial component in gradient methods is the learning rate (a.k.a. step size) hyper-parameter, which determines the convergence speed of the optimization procedure. A large learning rate can speed up the convergence but if it is larger than a threshold, the optimization algorithm cannot converge. This is by now well-understood for convex problems; excellent works on this topic include Nash and Nocedal, Bertsekas, Nesterov, Haykin et al., Bubeck et al., and the recent review for large-scale stochastic optimization to Bottou et al..

Recently, a series of breakthrough papers showed that (stochastic) gradient descent can provably converge to the global minima for over-parameterized neural networks. However, these papers all require the step size to be sufficiently small to guarantee the global convergence. In practice, these optimization algorithms can use a much larger learning rate while still converging to the global minimum.

*What is the optimal learning rate in optimizing neural networks?*

On the other hand, the theoretical investigation in adaptive methods in optimizing neural networks is limited. Existing analyses only deal with general (non)-convex and smooth functions, and thus, only concern convergence to first-order stationary points. However, a neural network is *neither smooth nor convex*. And yet, adaptive gradient methods are widely used in this setting as they converge without requiring a fine-tuned learning rate schedule.

In this paper, we make progress on these two problems for the two-layer over-parameterized ReLU-activated neural networks setting.

## Discussion on Variants of AdaGrad

In this section we compare our proposed algorithm AdaLoss with existing adaptive methods. Algorithm 1 can be viewed as a variant of the standard AdaGrad algorithm proposed by Duchi et al., where the norm version of the update is

Our algorithm AdaLoss is similar to AdaGrad, but is distinctly different from AdaGrad: we update $b_{k + 1}^{2}$ using the *norm* of the *loss* instead of the *squared norm* of the *gradient*. We considered the AdaLoss update instead of AdaGrad because, in the setting considered here, the modifications allowed for dramatically better theoretical convergence rate.
