Small Nonlinearities in Activation Functions Create Bad Local Minima in Neural Networks

We investigate the loss surface of neural networks. We prove that even for one-hidden-layer networks with "slightest" nonlinearity, the empirical risks have spurious local minima in most cases. Our results thus indicate that in general "no spurious local minima" is a property limited to deep linear networks, and insights obtained from linear networks may not be robust. Specifically, for ReLU(-like) networks we constructively prove that for almost all practical datasets there exist infinitely many local minima. We also present a counterexample for more general activations (sigmoid, tanh, arctan, ReLU, etc.), for which there exists a bad local minimum. Our results make the least restrictive assumptions relative to existing results on spurious local optima in neural networks. We complete our discussion by presenting a comprehensive characterization of global optimality for deep linear networks, which unifies other results on this topic.

## Introduction

Neural network training reduces to solving nonconvex empirical risk minimization problems, a task that is in general intractable. But success stories of deep learning suggest that local minima of the empirical risk could be close to global minima. Choromanska et al. use spherical spin-glass models from statistical physics to justify how the size of neural networks may result in local minima that are close to global. However, due to the complexities introduced by nonlinearity, a rigorous understanding of optimality in deep neural networks remains elusive.

Initial steps towards understanding optimality have focused on *deep linear* networks. This area has seen substantial recent progress. In deep linear networks there is no nonlinear activation; the output is simply a multilinear function of the input. Baldi & Hornik prove that some shallow networks have no spurious local minima, and Kawaguchi extends this result to squared error deep linear networks, showing that they only have global minima and saddle points. Several other works on linear nets have also appeared.

## Discussion and future work

We investigated the loss surface of deep linear and nonlinear neural networks. We proved two theorems showing existence of spurious local minima on nonlinear networks, which apply to almost all datasets (Theorem 1) and a wide class of activations (Theorem 2). We concluded by Theorem 4, showing a general result studying the behavior of critical points in multilinearly parametrized functions, which unifies other existing results on linear neural networks....

It is worth comparing our result with Laurent & Brecht, who use hinge loss based classification and assume linear separability to prove "no spurious local minima" for Leaky-ReLU networks. Their result does not contradict our theorem because the losses are different and we do not assume linear separability.

where ${s_{+} > 0},{s_{-} \geq 0}$ and $s_{+} \neq s_{-}$. Note that ReLU and Leaky-ReLU are members of this class.

### Theorem 2

The theory of nonlinear neural networks (which is the actual setting of interest), however, is still in its infancy. There have been attempts to extend the "local minima are global" property from linear to nonlinear networks, but recent results suggest that this property does not usually hold....
