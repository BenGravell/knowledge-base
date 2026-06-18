Implications of Regret on Stability of Linear Dynamical Systems

The setting of an agent making decisions under uncertainty and under dynamic constraints is common for the fields of optimal control, reinforcement learning, and recently also for online learning. In the online learning setting, the quality of an agent's decision is often quantified by the concept of regret, comparing the performance of the chosen decisions to the best possible ones in hindsight. While regret is a useful performance measure, when dynamical systems are concerned, it is important to also assess the stability of the closed-loop system for a chosen policy. In this work, we show that for linear state feedback policies and linear systems subject to adversarial disturbances, linear regret implies asymptotic stability in both time-varying and time-invariant settings. Conversely, we also show that bounded input bounded state stability and summability of the state transition matrices imply linear regret.

## Introduction

A number of real-world problems can be cast into the framework of agents making optimal decisions under uncertainty and/or adversarial disturbances. In this setting, the agent has an associated dynamical system and at each timestep suffers an *a priori* unknown cost that depends on its state and input. In the case of perfect knowledge of the dynamics and the future costs, this can be turned into an optimal control problem and solved with one of the plethora of available methods. As is often the case, however, the dynamics, disturbances, and/or future costs are either entirely unknown or only partially known....

As agents make decisions "on-the-go", there is a need to quantify and compare the performance of various algorithms. Considering a closed-loop system with a given, possibly time-varying policy, one can study its asymptotic stability as an asymptotic metric. Another approach is to look into the problem through the lens of online optimization. An important metric in the literature of the latter is the notion of regret. Given a policy $\mu$, its regret $\mathcal{R}_{T}$, is defined as the difference between its accumulated cost over some time horizon $T$ and that of some benchmark policy $\pi$....

## Conclusions

In this work, we studied the interconnection of the notion of regret coming from online optimization and the control theoretic concept of stability. Given a linear state feedback policy that attains linear regret, and certain upper and lower bounds on the objective stage costs, we show that the closed-loop system is necessarily asymptotically stable, both for the time-varying and time-invariant cases. The converse result also holds given that the closed-loop system is BIBS stable and has absolute summable norms of its state transition matrices....

### Example 3.1

### Assumption 2.5

We note that given Assumption 2.5.iii. holds, the condition in is stronger than asymptotic stability. In fact, if is satisfied, then Assumption 2.5.iii. implies asymptotic stability of the closed-loop system.

A special case of the optimal control problem, the linear quadratic regulator (LQR) has been extensively studied in this context. The results in show that the certainty equivalence approach can synthesize stable linear state feedback controllers as long as the model estimate errors are small enough....
