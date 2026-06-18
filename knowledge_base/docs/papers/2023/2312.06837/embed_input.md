Spectral State Space Models

Topics include Robustness, Convolutional networks, Learning.

This paper studies sequence modeling for prediction tasks with long range dependencies. We propose a new formulation for state space models (SSMs) based on learning linear dynamical systems with the spectral filtering algorithm (Hazan et al. ). This gives rise to a novel sequence prediction architecture we call a spectral state space model. Spectral state space models have two primary advantages. First, they have provable robustness properties as their performance depends on neither the spectrum of the underlying dynamics nor the dimensionality of the problem. Second, these models are constructed with fixed convolutional filters that do not require learning while still outperforming SSMs in both theory and practice. The resulting models are evaluated on synthetic dynamical systems and long-range prediction tasks of various modalities. These evaluations support the theoretical benefits of spectral filtering for tasks requiring very long range memory.

## Introduction

Handling long-range dependencies efficiently remains a core problem in sequence prediction/modelling. Recurrent Neural Networks (RNN) \[, RHW^+^85, \] are a natural choice, but are notoriously hard to train; they often suffer from vanishing and exploding gradients \[, \] and despite techniques to mitigate the issue \[, CVMG^+^14, \], they are also hard to scale given the inherently sequential nature of their computation.

In recent years, transformer models \[VSP^+^17\] have become the staple of sequence modelling, achieving remarkable success across multiple domains \[BMR^+^20, DBK^+^20, JEP^+^21\]. Transformer models are naturally parallelizable and hence scale significantly better than RNNs. However, attention layers have memory/computation requirements that scale quadratically with context length. Many approximations have been proposed (see for a recent survey).

RNNs have seen a recent resurgence in the form of state space models (SSM) which have shown promise in modelling long sequences across varied modalities \[, DFS^+^22 OSG^+^23, PMN^+^23, \]. SSMs use linear dynamical systems (LDS) to model the sequence-to sequence transform by evolving the internal state of a dynamical system according to the dynamics equations

## Conclusion

Insprired by the success of SSMs, we present a new theoretically-founded deep neural network architecture, Spectral SSM, for sequence modelling based on the Spectral Filtering algorithm for learning Linear Dynamical Systems. The SSM performs a reparameterization of the LDS and is guaranteed to learn even marginally stable symmetric LDS stably and efficiently. We demonstrate the core advantages of the Spectal SSM, viz. robustness to long memory through experiments on a synthetic LDS and the Long Range Arena benchmark.
