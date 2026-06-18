A Tutorial on Concentration Bounds for System Identification

Topics include System identification, Learning, State space.

We provide a brief tutorial on the use of concentration inequalities as they apply to system identification of state-space parameters of linear time invariant systems, with a focus on the fully observed setting. We draw upon tools from the theories of large-deviations and self-normalized martingales, and provide both data-dependent and independent bounds on the learning rate.

## Introduction

A key feature in modern reinforcement learning is the ability to provide high-probability guarantees on the finite-data/time behavior of an algorithm acting on a system. The enabling technical tools used in providing such guarantees are concentration of measure results, which should be interpreted as quantitative versions of the strong law of large numbers. This paper provides a brief introduction to such tools, as motivated by the identification of linear-time-invariant (LTI) systems.

In particular, we focus on the identifying the parameters $(A,B)$ of the LTI system

## conclusion

In this paper, we provided a brief introduction to tools useful for the finite-time analysis of system identification algorithms. We studied the full information setting, and showed how concentration of measure of sub-Gaussian and sub-exponential random variables are sufficient to analyze the independent trajectory estimator. We further showed that the analysis becomes much more challenging in the single-trajectory setting, but that tools from self-normalized martingale theory and small-ball probability are useful in this context. Finally, we provided computable data-dependent bounds that can be used in practical algorithms....

Choosing $\epsilon = {1/4}$, a standard volume comparison shows that $M_{\epsilon} \leq 9^{n}$ and $N_{\epsilon} \leq 9^{m}$ is sufficient, thus

We now return to our motivating example and analyze the error term. First, we observe that

Suppose that $\{\phi_{t}\}$ is a real-valued stochastic process adapted to the filtration $\{\mathcal{F}_{t}\}$. We say the process $\{\phi_{t}\}$ satisfies the $(k,\nu,p)$ block martingale small-ball (BMSB) condition if:

assuming *perfect* state measurements. This is in some sense the simplest possible system identification problem, making it the perfect case study for such a tutorial. Our companion paper shows how the results derived in this paper can then be integrated into self-tuning and adaptive control policies with finite-data guarantees. We also refer the reader to Section II of for an in-depth and comprehensive literature review of classical and contemporary results in system identification. Finally, we note that most of the results we present below are not the sharpest available in the literature, but are rather chosen for the pedagogical value.
