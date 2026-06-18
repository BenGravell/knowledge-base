Beyond the Fundamental Lemma: From Finite Time Series to Linear System

Topics include Behavioral systems, System identification, Fundamental lemma, Linear systems, Finite time series, Minimal realization, Lag bounds, Input-output data.

Revisits what can be identified from finite input-output time series beyond the trajectory-spanning statement of the fundamental lemma. The paper gives exact identifiability conditions and dimension/lag bounds, making it a more system-identification-oriented complement to direct control results.

We state necessary and sufficient conditions to uniquely identify (modulo state isomorphism) a linear time-invariant minimal input-state-output system from finite input-output data and upper- and lower bounds on lag and state space dimension.

## Introduction

Background. J.C. Willems' trilogy is one of broader, deeper, and more influential studies about mathematical modelling of dynamical systems from time series. The second part \[\] concerns the problem of obtaining a mathematical model for a linear system from a given (infinite) trajectory. It significantly influenced subspace identification methods \[\], that compute a state sequence from finite-length data by adapting Willems' state construction from infinite- to finite-length data....

The fundamental lemma parameterizes all trajectories of a system from a single sufficiently informative one. This parameterization was applied in linear quadratic control \[\], simulation \[\], model reduction of dissipative systems \[\], and predictive control \[\]. More recently, this approach has gained significant momentum, initiated by papers such as and followed by many contributions addressing a variety of data-driven analysis and control problems.

We stated necessary and sufficient conditions for informativity for system identification in the class of minimal ISO systems whose lag and state dimension lie between given lower/upper bounds. To establish such result we obtained some intermediate ones of independent interest, most prominently the iterative construction of a state sequence and a corresponding ISO model in the proof of Theorem.

We aim to apply the concept of informativity for system identification in a model class to other classes than minimal systems, e.g. to dissipative systems. We also plan to work on the application of the informativity concept to identification in the behavioral framework, where interesting results have recently appeared.

If $L_{+} = \ell_{true}$ and $N_{+} = n_{true}$, a necessary condition for informativity is that $T \geqslant {{{({\ell_{true} + 1})}m} + \ell_{true} + n_{true}}$ (see (19c)). It follows that if $T < 11$ then $(u_{\lbrack 0,{T - 1}\rbrack},y_{\lbrack 0,{T - 1}\rbrack})$ is not informative for every $L_{+}$ and $N_{+}$. The symbol '✓' in Table denotes data informativity for different values of $L_{+}$, $N_{+}$, and $T$, as inferred from the fundamental lemma and Theorem....

The proof of Theorem in Section 7.2 relies on a new iterative state-computation scheme from input-output data.
