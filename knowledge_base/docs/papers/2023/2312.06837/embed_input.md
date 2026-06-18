Spectral State Space Models

Topics include Robustness, Convolutional networks, Learning.

This paper studies sequence modeling for prediction tasks with long range dependencies. We propose a new formulation for state space models (SSMs) based on learning linear dynamical systems with the spectral filtering algorithm (Hazan et al. ). This gives rise to a novel sequence prediction architecture we call a spectral state space model. Spectral state space models have two primary advantages. First, they have provable robustness properties as their performance depends on neither the spectrum of the underlying dynamics nor the dimensionality of the problem. Second, these models are constructed with fixed convolutional filters that do not require learning while still outperforming SSMs in both theory and practice. The resulting models are evaluated on synthetic dynamical systems and long-range prediction tasks of various modalities. These evaluations support the theoretical benefits of spectral filtering for tasks requiring very long range memory.

## Introduction

Handling long-range dependencies efficiently remains a core problem in sequence prediction/modelling. Recurrent Neural Networks (RNN) \[, RHW^+^85, []\] are a natural choice, but are notoriously hard to train; they often suffer from vanishing and exploding gradients \[, []\] and despite techniques to mitigate the issue \[, CVMG^+^14, []\], they are also hard to scale given the inherently sequential nature of their computation.

In recent years, transformer models \[VSP^+^17\] have become the staple of sequence modelling, achieving remarkable success across multiple domains \[BMR^+^20, DBK^+^20, JEP^+^21\]. Transformer models are naturally parallelizable and hence scale significantly better than RNNs. However, attention layers have memory/computation requirements that scale quadratically with context length. Many approximations have been proposed (see \[\] for a recent survey).

## Conclusion

Insprired by the success of SSMs, we present a new theoretically-founded deep neural network architecture, Spectral SSM, for sequence modelling based on the Spectral Filtering algorithm for learning Linear Dynamical Systems. The SSM performs a reparameterization of the LDS and is guaranteed to learn even marginally stable symmetric LDS stably and efficiently. We demonstrate the core advantages of the Spectal SSM, viz. robustness to long memory through experiments on a synthetic LDS and the Long Range Arena benchmark....

It is shown in the appendix (see Lemma C.1) that $Z = {\int_{0}^{1}{\mu{(\alpha)}\mu{(\alpha)}^{\top}{d\alpha}}}$. Thus it can be seen that $Z$ is a real PSD Hankel matrix. It is known (see Lemma C.4. ‣ Appendix C Proof of Theorem 3.1 ‣ Spectral State Space Models") in the appendix) that real PSD Hankel matrices have an exponentially decaying spectrum....

The technique of spectral filtering \[\] was developed as a convex improper learning alternative to directly parameterizing an LDS (as in the case of SSMs) leading to an efficient, polynomial-time algorithm and near-optimal regret guarantees. Different from regression-based methods (eg. SSMs) that aim to identify the system dynamics, spectral filtering's guarantee does not depend on the stability of the underlying system, and is the first method to obtain condition number-free regret guarantees for the MIMO setting....
