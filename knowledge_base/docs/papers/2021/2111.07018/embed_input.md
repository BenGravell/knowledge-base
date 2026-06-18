Identification and Adaptive Control of Markov Jump Systems: Sample Complexity and Regret Bounds

Topics include Markov jump systems, System identification, Adaptive control, Regret bounds, Sample complexity, Certainty equivalence.

Combines identification of Markov jump linear dynamics with episodic certainty-equivalent control and regret analysis. The paper is valuable because it handles both mode-dependent dynamics and transition learning from a single trajectory, then translates estimation rates into adaptive-control guarantees.

Learning how to effectively control unknown dynamical systems is crucial for intelligent autonomous systems. This task becomes a significant challenge when the underlying dynamics are changing with time. Motivated by this challenge, this paper considers the problem of controlling an unknown Markov jump linear system (MJS) to optimize a quadratic objective. By taking a model-based perspective, we consider identification-based adaptive control of MJSs. We first provide a system identification algorithm for MJS to learn the dynamics in each mode as well as the Markov transition matrix, underlying the evolution of the mode switches, from a single trajectory of the system states, inputs, and modes. Through martingale-based arguments, sample complexity of this algorithm is shown to be O(1/sqrt(T)). We then propose an adaptive control scheme that performs system identification together with certainty equivalent control to adapt the controllers in an episodic fashion....

## Introduction

A canonical problem at the intersection of machine learning and control is that of adaptive control of an unknown dynamical system. An intelligent autonomous system is likely to encounter such a task; from an observation of the inputs and outputs, it needs to both learn and effectively control the dynamics. A commonly used control paradigm is the Linear Quadratic Regulator (LQR), which is theoretically well understood when system dynamics are linear and known. LQR also provides an interesting benchmark, when system dynamics are unknown, for reinforcement learning (RL) with continuous state and action spaces and for adaptive control.

Figure 1: State trajectories for a two-modes MJS $\left\{ \begin{matrix}
\end{matrix} \right.$ with Markov matrix $\begin{bmatrix}
\end{bmatrix}$ and x0 = 1. Red and blue curves: mode switching sequences Ω1 = {1, 1, …} and Ω2 = {2, 2, …}. Yellow curve: average over all realizations. Gray area: region for all possible trajectories.

Markov jump systems are fundamental to a rich class of control problems where the underlying dynamics are changing with time. Despite its importance, statistical understanding (system identification and regret bounds) of MJS have been lacking due to the technicalities such as Markovian transitions and weaker notion of mean-square stability. At a high-level, this work overcomes (much of) these challenges to provide finite sample system identification and model-based adaptive control guarantees for MJS....

We want to mention possible negative societal impacts. While our work is theoretical and has many potential positive impacts in reinforcement learning, robotics, and autonomous systems, there are also potential negative applications in the military (e.g. with drone control) and for malicious actors (e.g. computer network hackers), among others. Additionally, all our work was built on stochastic noise assumptions, whereas in reality intelligent autonomous systems may instead encounter adversarial behavior....

Note that, our system identification result achieves near-optimal ($\mathcal{O}{({1/\sqrt{T}})}$) dependence on the trajectory length $T$. However, the effective sample complexity of our system identification algorithm is $\mathcal{O}{({{s{({n + p})}^{2}{\log^{2}{(T)}}}/\pi_{\min}^{2}})}$, that is, the sample complexity grows quadratically in the state dimension $n$, which...
