Identification and Adaptive Control of Markov Jump Systems: Sample Complexity and Regret Bounds

Topics include Markov jump systems, System identification, Adaptive control, Regret bounds, Sample complexity, Certainty equivalence.

Combines identification of Markov jump linear dynamics with episodic certainty-equivalent control and regret analysis. The paper is valuable because it handles both mode-dependent dynamics and transition learning from a single trajectory, then translates estimation rates into adaptive-control guarantees.

Learning how to effectively control unknown dynamical systems is crucial for intelligent autonomous systems. This task becomes a significant challenge when the underlying dynamics are changing with time. Motivated by this challenge, this paper considers the problem of controlling an unknown Markov jump linear system (MJS) to optimize a quadratic objective. By taking a model-based perspective, we consider identification-based adaptive control of MJSs. We first provide a system identification algorithm for MJS to learn the dynamics in each mode as well as the Markov transition matrix, underlying the evolution of the mode switches, from a single trajectory of the system states, inputs, and modes. Through martingale-based arguments, sample complexity of this algorithm is shown to be O(1/sqrt(T)). We then propose an adaptive control scheme that performs system identification together with certainty equivalent control to adapt the controllers in an episodic fashion.

## Introduction

A canonical problem at the intersection of machine learning and control is that of adaptive control of an unknown dynamical system. An intelligent autonomous system is likely to encounter such a task; from an observation of the inputs and outputs, it needs to both learn and effectively control the dynamics. A commonly used control paradigm is the Linear Quadratic Regulator (LQR), which is theoretically well understood when system dynamics are linear and known. LQR also provides an interesting benchmark, when system dynamics are unknown, for reinforcement learning (RL) with continuous state and action spaces and for adaptive control.

A generalization of linear dynamical systems called Markov jump linear systems (MJSs) models dynamics that switch between multiple linear systems, called modes, according to an underlying finite Markov chain. MJS allows for modeling a richer set of problems where the underlying dynamics can abruptly change over time. One can, similarly, generalize the LQR paradigm to MJS by using mode-dependent cost matrices, which allow different control goals under different modes.

In this paper, we provide the first comprehensive system identification and regret guarantees for learning and controlling Markov jump linear systems using a single trajectory while assuming only mean-square stability (see Def. 3.1 ‣ 3.1 Markov Jump Linear Systems ‣ 3 Preliminaries and Problem Setup ‣ Identification and Adaptive Control of Markov Jump Systems: Sample Complexity and Regret Bounds")). Importantly, our guarantees are optimal in the trajectory length $T$.

$\mathcal{O}{(\sqrt{T})}$-regret bound: We employ our system identification guarantees for the MJS-LQR. When the system dynamics are unknown, we show that the certainty-equivalent adaptive MJS-LQR Algorithm (Alg. 2) achieves a regret bound of $\mathcal{O}{(\sqrt{T})}$. Remarkably, this coincides with the optimal regret bound for the standard LQR problem obtained via certainty equivalence.

## Discussion

In this section, we discuss how one may obtain the initial stabilizing controller for MJS as required in the input to Algorithms 1 and 2 and the application of our results to offline data-driven control.
