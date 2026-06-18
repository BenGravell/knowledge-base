Sketchy: Memory-Efficient Adaptive Regularization with Frequent Directions

Topics include Regularization, Sketching, Second-order optimization, Adaptive step size, Neural networks, Optimization, Machine learning efficiency.

Uses frequent-directions sketches to build a memory-efficient adaptive regularization method for training large models. Sketchy is positioned as a practical compromise between richer curvature information and the memory limits of standard adaptive optimizers.

Adaptive regularization methods that exploit more than the diagonal entries exhibit state of the art performance for many tasks, but can be prohibitive in terms of memory and running time. We find the spectra of the Kronecker-factored gradient covariance matrix in deep learning (DL) training tasks are concentrated on a small leading eigenspace that changes throughout training, motivating a low-rank sketching approach. We describe a generic method for reducing memory and compute requirements of maintaining a matrix preconditioner using the Frequent Directions (FD) sketch. While previous approaches have explored applying FD for second-order optimization, we present a novel analysis which allows efficient interpolation between resource requirements and the degradation in regret guarantees with rank k: in the online convex optimization (OCO) setting over dimension d, we match full-matrix d^ memory regret using only dk memory up to additive error in the bottom d-k eigenvalues of the gradient covariance. Further, we show extensions of our work to Shampoo, resulting in a method competitive in quality with Shampoo and Adam, yet requiring only sub-linear memory for tracking second moments.

## Introduction

DL optimization commonly relies on adaptive gradient methods, namely the Adam optimizer. It differs from stochastic gradient descent in that the learning rate is a structured diagonal matrix built from previous gradients rather than a scalar. In full matrix AdaGrad, the inverse matrix square root of the sum of outer products of previous gradients is the learning rate.

In the setting of online convex optimization, by applying a dynamic diagonal regularization to the FD sketch, we can recover full-matrix AdaGrad regret up to additive spectral terms under a memory constraint, providing a novel guarantee without curvature assumptions (Sec. 4.1). Rigorously composing our approach with Shampoo (Sec. 4.2) unlocks a second-order algorithm which requires sub-linear memory for its accumulators.

By modifying FD for exponential moving averages (Sec. 4.3), we demonstrate a practical algorithm competitive with at-least-linear memory Shampoo and Adam in three modern DL settings (Sec. 5.1). While previous work shows rank-1 preconditioners are effective for trading off quality for memory, these results demonstrate a Pareto improvement by using higher-rank approximations.

## Discussion

Up to spectral error, Alg. 2 achieves full-matrix AdaGrad regret despite approximating the *smallest* part of the spectrum of $G_{t}^{- {1/2}}$ at each step. Remarkably, these eigenvectors correspond to the *most* easily discernible signals of the covariance for the stream $g_{t}$. This apparent (and fortuitous) coincidence is resolved by considering the covariance of ${\overset{\sim}{G}}_{t}^{- {1/2}}g_{t}$: whitening the gradient to facilitate optimization best reflects on regret; as a result, approximating top eigenvectors of $G_{T}$ helps more than the bottom ones.

Our initial implementation focused on correctness rather than physical speed or memory reduction. Engineering optimizers competitive with existing industrial-strength implementations of Adam and Shampoo was out of scope. In implementing FD, we performed updates via the factored SVD of $\lbrack{\beta_{2}^{1/2}B_{t}};G_{t}\rbrack$ rather than the eigendecomposition depicted in Alg. 1; this avoids squaring, which is unavoidable in Shampoo. For speed, Shampoo subsamples gradients for its covariance estimation and updates its inverse matrix roots intermittently, every fixed number of steps.
