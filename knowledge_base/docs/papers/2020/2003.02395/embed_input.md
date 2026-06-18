A Simple Convergence Proof of Adam and Adagrad

Topics include Optimization, Rate of convergence.

We provide a simple proof of convergence covering both the Adam and Adagrad adaptive optimization algorithms when applied to smooth (possibly non-convex) objective functions with bounded gradients. We show that in expectation, the squared norm of the objective gradient averaged over the trajectory has an upper-bound which is explicit in the constants of the problem, parameters of the optimizer, the dimension d, and the total number of iterations N. This bound can be made arbitrarily small, and with the right hyper-parameters, Adam can be shown to converge with the same rate of convergence O(dln(N)/sqrt(N)). When used with the default parameters, Adam doesn't converge, however, and just like constant step-size SGD, it moves away from the initialization point faster than Adagrad, which might explain its practical success. Finally, we obtain the tightest dependency on the heavy ball momentum decay rate beta_1 among all previous convergence bounds for non-convex Adam and Adagrad, improving from O((1-beta_1)^(-3)) to O((1-beta_1)^(-1)).

## Introduction

First-order methods with adaptive step sizes have proved useful in many fields of machine learning, be it for sparse optimization, tensor factorization or deep learning. Duchi et al. introduced Adagrad, which rescales each coordinate by a sum of squared past gradient values. While Adagrad proved effective for sparse optimization, experiments showed that it under-performed when applied to deep learning. RMSProp proposed an exponential moving average instead of a cumulative sum to solve this....

In the online convex optimization setting, Duchi et al. showed that Adagrad achieves optimal regret for online convex optimization. Kingma & Ba provided a similar proof for Adam when using a decreasing overall step size, although this proof was later shown to be incorrect by Reddi et al., who introduced AMSGrad as a convergent alternative. Ward et al. proved that Adagrad also converges to a critical point for non convex objectives with a rate $O{({{\ln{(N)}}/\sqrt{N}})}$ when using a scalar adaptive step-size, instead of diagonal. Zou et al. extended this proof to the vector case, while Zou et al....

### Broader Impact Statement

The present theoretical results on the optimization of non convex losses in a stochastic settings impact our understanding of the training of deep neural network. It might allow a deeper understanding of neural network training dynamics and thus reinforce any existing deep learning applications. There would be however no direct possible negative impact to society.

which differ from (10. ‣ No heavy-ball momentum ‣ 4.1 Convergence bounds ‣ 4 Main results ‣ A Simple Convergence Proof of Adam and Adagrad")) only by a $+ {N/{({N - 1})}}$ next to the log term.

### Theorem 2 (Convergence of Adam without momentum)

Injecting (28 ‣ A Simple Convergence Proof of Adam and Adagrad")) and (21 ‣ A Simple Convergence Proof of Adam and Adagrad")) into (20 ‣ A Simple Convergence Proof of Adam and Adagrad")) finishes the proof. ∎

In this paper, we present a simplified and unified proof of convergence to a critical point for Adagrad and Adam for stochastic non-convex smooth optimization. We assume that the objective function is lower bounded, smooth and the stochastic gradients are almost surely bounded....
