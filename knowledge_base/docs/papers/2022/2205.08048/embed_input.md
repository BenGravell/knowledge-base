A Short Introduction to the Koopman Representation of Dynamical Systems

Topics include Online algorithms, Dynamic mode decomposition, AKA, Dynamical systems, Transfer operator.

The Koopman representation is an infinite dimensional linear representation of linear or nonlinear dynamical systems. It represents the dynamics of output maps (aka observables), which are functions on the state space whose evaluation is interpreted as an output. Conceptually simple derivations and commentary on the Koopman representation are given. We emphasize an important duality between initial conditions and output maps of the original system, and those of the Koopman representation. This duality is an important consideration when this representation is used in data-driven applications such as the Dynamic Mode Decomposition (DMD) and its variants. The adjoint relation between the Koopman representation and the transfer operator of mass transport is also shown.

## Abstract

The Koopman representation is an infinite dimensional linear representation of linear or nonlinear dynamical systems. It represents the dynamics of output maps (aka observables), which are functions on the state space whose evaluation is interpreted as an output. Conceptually simple derivations and commentary on the Koopman representation are given. We emphasize an important duality between initial conditions and output maps of the original system, and those of the Koopman representation.

## The Basic Construction

The simplest approach to define the Koopman representation is in a general and abstract manner using the flow map of a dynamical system. This conceptually simple approach clarifies some of the properties of the representation without getting sidetracked by the details of the underlying differential or difference equations, or modal and spectral decompositions. Those should be introduced after the basic features and properties of the representation are established.

Consider a continuous (or discrete) time dynamical system written abstractly

where at each time, $x_{t} \in \mathbf{X}$, the state space, $y_{t} \in \mathbf{Y}$, the output space, the mapping $f:{\mathbf{X}\rightarrow\mathbf{X}}$ is a vector field that generates the dynamics (or the one-step iteration in the discrete-time case), and the mapping $\overline{G}:{\mathbf{X}\rightarrow\mathbf{Y}}$ is the output (i.e. "readout") mapping if the state is not directly observed, but only through the output variables $y_{t}$. If the state is directly observed, then the mapping $\overline{G}$ is simply the identity mapping.
