The Shortest Experiment for Linear System Identification

Topics include System identification, Experiment design, Behavioral systems, Linear systems, Persistency of excitation, Online experiment design, Sample complexity, Input-output data.

Designs adaptive inputs that recover an unknown LTI system with the shortest possible experiment length under dimension and lag bounds. It is closely related to the informativity perspective because it asks how little data can be made informative for identification.

This paper is concerned with the following problem: given an upper bound of the state-space dimension and lag of a linear time-invariant system, design a sequence of inputs so that the system dynamics can be recovered from the resulting input-output data. As our main result we propose a new online experiment design method, meaning that the selection of the inputs is iterative and guided by data samples collected in the past. We show that this approach leads to the shortest possible experiments for linear system identification. In terms of sample complexity, the proposed method outperforms offline methods based on persistency of excitation as well as existing online experiment design methods.

## Introduction

*Background*: In the context of system identification, *experiment design* is concerned with the selection of inputs of a dynamical system in such a way that the resulting input-output data contain sufficient information about the system dynamics. Experiment design is a classical topic that has been investigated from different angles throughout the years.

An experiment design result that has recently been popularized is the so-called *fundamental lemma* by Willems and his coauthors. Roughly speaking, the result says that the dynamics of a linear time-invariant system can be uniquely identified from input-output data if the input data are chosen to be sufficiently persistently exciting. The fundamental lemma also provides a parameterization of all finite trajectories of the system, in terms of a data Hankel matrix.

The recent interest in data-driven control has also led to extensions of the fundamental lemma itself. Its original proof was presented in the language of behavioral theory; an alternative proof for state space systems was provided. Generalizations to uncontrollable systems are presented in and extensions to continuous-time systems . Robust/quantitative versions are explored in while frequency domain formulations have been considered . Furthermore, the fundamental lemma has been generalized to various other model classes such as descriptor systems, flat nonlinear systems, linear parameter-varying systems, and stochastic ones.

In this paper, we will build on the framework of. However, unlike that focused on analyzing informativity of given data sets, the purpose of this paper is to *design* experiments that are informative for system identification.

We propose the experiment design method OnlineExperiment$(L,N)$. This procedure designs the inputs *online*, i.e., on the basis of past input-output samples. In Theorem we prove that this method leads to informative experiments of length $T$.

A remarkable outcome of this paper is the fact that experiments can be designed of length *precisely equal to the lower bound $T$*. Interestingly, this number of samples $T$ depends on the unknown system and is thus not given a priori. It is revealed after the experiment design algorithm terminates.
