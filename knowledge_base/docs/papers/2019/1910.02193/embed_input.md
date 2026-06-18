Mode Clustering for Markov Jump Systems

Topics include Markov jump systems, Mode clustering, System identification, Singular value decomposition, k-means, Model reduction.

Studies how to cluster latent modes in Markov jump models using mode-sequence estimation, singular-value structure, and k-means. The paper frames model reduction for switching systems as a statistically analyzable clustering problem over transition behavior rather than only over output trajectories.

In this work, we consider the problem of mode clustering in Markov jump models. This model class consists of multiple dynamical modes with a switching sequence that determines how the system switches between them over time. Under different active modes, the observations can have different characteristics. Given the observations only and without knowing the mode sequence, the goal is to cluster the modes based on their transition distributions in the Markov chain to find a reduced-rank Markov matrix that is embedded in the original Markov chain. Our approach involves mode sequence estimation, mode clustering and reduced-rank model estimation, where mode clustering is achieved by applying the singular value decomposition and k-means. We show that, under certain conditions, the clustering error can be bounded, and the reduced-rank Markov chain is a good approximation to the original Markov chain. Through simulations, we show the efficacy of our approach and the application of our approach to real world scenarios.

## Introduction

Modeling dynamic systems has been a problem of great interest in the signal processing and control communities for decades. Many real-world phenomena cannot be described with one dynamical model, and so switched models wherein the dynamics transition between different system models have been studied and applied widely. In human-made systems, for example, a robot may have different dynamics under different battery levels or when different modules within the robot fail....

A key challenge for such models is the model compactness -- how does one represent such a complicated dynamical system with as simple a model as possible? For example, modes like weather conditions and human emotions have extremely complex underlying dynamics with strong correlations over time. To satisfy the Markov property, one may concatenate underlying modes into a single Markov state, and Markov chains built in this way will have a state space that grows exponentially with the number of modes concatenated in the sequence....

In this paper, we consider the problem of model aggregation for Markov jump system from the perspective of clustering the modes based on their transition distributions. The proposed approach has guaranteed clustering error upper bound and exhibits decent performance in the experiments.

There are several interesting directions for future work: (i) we will see how lumpable Markov chain can help reformulate the model reduction problem; (ii) in the algorithm, after obtaining an estimate of the Markov transition matrix, one might use it to get a better estimate of the mode sequence, so several iterations between estimating switching sequence and Markov transition matrix may make both estimates more accurate; (iii) after the mode clustering, it is worth investigating if we could use a single mode to characterize the switching dynamics of all the modes within the cluster so that we could truly reduce the number of modes in...

Let $\mathbf{P} \in {n1{\mathbb{R}}^{n}{\mathbb{R}}^{n\mathsf{x}n}}$ be a row stochastic Markov transition matrix with stationary distribution $\mathbf{π}$. Then for all $\epsilon > 0$, the $\epsilon -$mixing time is defined as

We can see that as long as the approximation error ${\|{\mathbf{P} - \overset{\sim}{\mathbf{P}}}\|}_{\infty}$ is upper bounded, the stationary and transient behavior differences between the true...
