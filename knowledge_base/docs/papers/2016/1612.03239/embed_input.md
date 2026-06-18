When Multiplicative Noise Stymies Control

Topics include Control, Multiplicative noise, Linear systems.

We consider the stabilization of an unstable discrete-time linear system that is observed over a channel corrupted by continuous multiplicative noise. Our main result shows that if the system growth is large enough, then the system cannot be stabilized in a second-moment sense. This is done by showing that the probability that the state magnitude remains bounded must go to zero with time. Our proof technique recursively bounds the conditional density of the system state (instead of focusing on the second moment) to bound the progress the controller can make. This sidesteps the difficulty encountered in using the standard data-rate theorem style approach; that approach does not work because the mutual information per round between the system state and the observation is potentially unbounded. It was known that a system with multiplicative observation noise can be stabilized using a simple memoryless linear strategy if the system growth is suitably bounded. In this paper, we show that while memory cannot improve the performance of a linear scheme, a simple non-linear scheme that uses one-step memory can do better than the best linear scheme.

## Introduction

We consider the control and stabilization of a system observed over a multiplicative noise channel. Specifically, we analyze the following system, $\mathcal{S}_{a}$, with initial state $X_{0} \sim {\mathcal{N}{}}$:

In the preceding formulation, the system state is represented by $X_{n}$ at time $n$, and the control $U_{n}$ can be any function of the current and previous observations $Y_{0}$ to $Y_{n}$. The $Z_{n}$'s are i.i.d. random variables with a known continuous distribution. The realization of the noise $Z_{n}$ is unknown to the controller, much like the fading coefficient (gain) of a channel might be unknown to the transmitter or receiver in non-coherent communication. The constant $a$ captures the growth of the system. The controller's objective is to stabilize the system in the second-moment sense, i.e....

This paper provides a first proof-of-concept converse for a control system observed over continuous multiplicative noise. However, there is an exponential gap between the scaling behavior of the achievable strategy and the converse.

We note that if the system $\mathcal{S}_{a}$ in (1.1) is restricted to using linear control strategies, then its performance limit is the same as that of a system with the same multiplicative actuation noise (i.e. the control $U_{n}$ is multiplied by a random scaling factor) but perfect observations (as in ). Previous work has shown how to compute the control capacity for systems with multiplicative noise on the actuation channel. However, computing the control capacity of the system $\mathcal{S}_{a}$, i.e. computing tight upper and lower bounds on the system growth factor $a$, remains open.

Let $\epsilon > 0$ be another small number to be specified later, and take $a = {1 + \epsilon^{2}}$. For our controls, we take

## Non-linear schemes

### Lemma 5.3

Figure 1: The state Xn is observed over a multiplicative noise channel Yn = Xn Zn.

Our main theorem provides an impossibility result for stabilizing the system $\mathcal{S}_{a}$.

### Theorem 1.1

Let the $Z_{n}$ be i.i.d. random variables with finite mean and variance and with bounded density ${f_{Z}{(z)}} = e^{- {\phi{(z)}}}$, where $\phi{( \cdot )}$ is a polynomial of even degree with positive leading coefficient....
