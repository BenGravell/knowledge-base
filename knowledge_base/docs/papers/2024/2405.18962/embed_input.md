Beyond the Fundamental Lemma: From Finite Time Series to Linear System

Topics include Behavioral systems, System identification, Fundamental lemma, Linear systems, Finite time series, Minimal realization, Lag bounds, Input-output data.

Revisits what can be identified from finite input-output time series beyond the trajectory-spanning statement of the fundamental lemma. The paper gives exact identifiability conditions and dimension/lag bounds, making it a more system-identification-oriented complement to direct control results.

We state necessary and sufficient conditions to uniquely identify (modulo state isomorphism) a linear time-invariant minimal input-state-output system from finite input-output data and upper- and lower bounds on lag and state space dimension.

## Introduction

Background. J.C. Willems' trilogy is one of broader, deeper, and more influential studies about mathematical modelling of dynamical systems from time series. The second part concerns the problem of obtaining a mathematical model for a linear system from a given (infinite) trajectory. It significantly influenced subspace identification methods, that compute a state sequence from finite-length data by adapting Willems' state construction from infinite- to finite-length data. Two assumptions are crucial: the state space dimension of the system is known; and a rank condition holds for a Hankel matrix constructed from the data.

The fundamental lemma parameterizes all trajectories of a system from a single sufficiently informative one. This parameterization was applied in linear quadratic control, simulation, model reduction of dissipative systems, and predictive control. More recently, this approach has gained significant momentum, initiated by papers such as and followed by many contributions addressing a variety of data-driven analysis and control problems.

The recent surge in popularity of this parameterization has also revived the interest in the fundamental lemma itself. Its original proof was presented in the language of behavioral systems; an alternative proof for state space systems was provided. The original proof and that are by contradiction; a direct proof was presented for single-input systems. Generalizations to uncontrollable systems are in and extensions to continuous-time systems . Quantitative/robust variations are explored , frequency domain formulations , and online experiment design.

Contributions. The fundamental lemma gives a *sufficient* condition for identifiability (in the sense of ); in this paper we investigate necessary and sufficient conditions on finite input-output data for identifiability of an unknown minimal input-state-output (ISO) system whose lag and state space dimension lie between given lower and upper bounds.

Using the concept of *data informativity* (see ), we develop a framework for ISO system identification from finite input-output data, incorporating a priori knowledge or assumptions. While currently limited to exact (deterministic) identification problems, such framework is of broader potential interest, for example in approximate modelling and for noisy data.
