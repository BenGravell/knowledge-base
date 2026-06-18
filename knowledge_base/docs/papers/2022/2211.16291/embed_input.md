On Controller Reduction in Linear Quadratic Gaussian Control with Performance Bounds

The problem of controller reduction has a rich history in control theory. Yet, many questions remain open. In particular, there exist very few results on the order reduction of general non-observer based controllers and the subsequent quantification of the closed-loop performance. Recent developments in model-free policy optimization for Linear Quadratic Gaussian (LQG) control have highlighted the importance of this question. In this paper, we first propose a new set of sufficient conditions ensuring that a perturbed controller remains internally stabilizing. Based on this result, we illustrate how to perform order reduction of general non-observer based controllers using balanced truncation and modal truncation. We also provide explicit bounds on the LQG performance of the reduced-order controller. Furthermore, for single-input-single-output (SISO) systems, we introduce a new controller reduction technique by truncating unstable modes. We illustrate our theoretical results with numerical simulations. Our results will serve as valuable tools to design direct policy search algorithms for control problems with partial observations.

## Introduction

In many control applications, low-order controllers are often preferred over high-order controllers, because they are simpler to maintain, more interpretable, and computationally less demanding. Thus, given a high-order controller, one often would like to approximate it using a lower-order controller that still stabilizes the plant whilst performing similarly on relevant closed-loop performance metrics, such as the Linear Quadratic Gaussian (LQG) cost. This problem is known as *controller reduction*....

However, the problem of order-reduction for general non-observer based controllers has been less studied, especially in the context of LQG control. Recent progress in model-free policy optimization for linear control has highlighted the importance of order-reduction for general controllers. In particular, a natural problem in model-free policy optimization is to learn an optimal policy iteratively using policy gradient methods. It has recently been shown that the optimization landscape of LQG control may contain saddle points in state-space dynamic controllers....

## Conclusion

We have presented on controller reduction for general non observer-based controllers using balanced truncation and modal truncation. For SISO systems, we demonstrate how LQG control may be performed even when there are no stable components in the controller. We hope that our work will be useful not only for policy optimization in LQG control but also for the controller reduction community. Two interesting future directions are 1) extending truncation of unstable modes to MIMO systems and 2) applying the results to escape saddle points in the LQG policy optimization.

### Lemma 4 (\[17, Theorem 3.2\], \[16, Theorem 7.9\])

First, noting that $\mathbf{Y} ≔ {({I - {\mathbf{G}\mathbf{K}}})}^{- 1}$ and using 12; zhengy@eng.ucsd.edu (Yang Zheng); mfazel@uw.edu (Maryam Fazel); and nali@seas.harvard.edu (Na Li)."), we have

Consider a minimal $n$-th order controller $\mathbf{K}$ which stabilizes the plant $\mathbf{G}$. Consider the decomposition $\mathbf{K} = {\mathbf{K}_{<} + \mathbf{K}_{\geq}}$ in 24; zhengy@eng.ucsd.edu (Yang Zheng); mfazel@uw.edu (Maryam Fazel); and nali@seas.harvard.edu (Na Li)."), and suppose we obtain a lower-order approximation $\mathbf{K}_{r, <}$ of $\mathbf{K}_{<}$ using the modal truncation algorithm in Algorithm 3 ‣ 5 Controller reduction...
