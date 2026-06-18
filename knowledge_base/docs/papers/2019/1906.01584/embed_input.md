Robust Exploration in Linear Quadratic Reinforcement Learning

Topics include Convex optimization, Reinforcement learning, Robustness, Uncertainty, Optimization, Control, Learning.

This paper concerns the problem of learning control policies for an unknown linear dynamical system to minimize a quadratic cost function. We present a method, based on convex optimization, that accomplishes this task robustly: i.e., we minimize the worst-case cost, accounting for system uncertainty given the observed data. The method balances exploitation and exploration, exciting the system in such a way so as to reduce uncertainty in the model parameters to which the worst-case cost is most sensitive. Numerical simulations and application to a hardware-in-the-loop servo-mechanism demonstrate the approach, with appreciable performance and robustness gains over alternative methods observed in both.

## Introduction

Learning to make decisions in an uncertain and dynamic environment is a task of fundamental importance in a number of domains. Though it has been the subject of intense research activity since the formulation of the 'dual control problem' in the 1960s, the recent success of reinforcement learning (RL), particularly in games, has inspired a resurgence in interest in the topic. Problems of this nature require decisions to be made with respect to two objectives. First, there is a goal to be achieved, typically quantified as a reward function to be maximized....

It is important to recognize that the second objective (exploration) is important only in so far as it facilitates the first (maximizing reward); there is no intrinsic value in reducing uncertainty. As a consequence, exploration should be targeted or application specific; it should *not* excite the system arbitrarily, but rather in such a way that the information gathered is useful for achieving the goal. Furthermore, in many real-world applications, it is essential that exploration does not compromise the safe and reliable operation of the system.

### Hardware-in-the-loop experiment

In this section, we consider the RRL problem for a hardware-in-the-loop simulation comprised of the interconnection of a physical servo mechanism (Quanser QUBE 2) and a synthetic (simulated) LTI dynamical system; cf. Appendix A.2 for full details of the experimental setup. An experimental trial consisted of the following procedure. Initial data was obtained by simulating the system for 0.5 seconds, under closed-loop feedback control (cf. Appendix A.2) with data sampled at 500Hz, to give 250 initial data points. We then applied methods rrl (with horizon $h = 5$) and greedy as described in §5....

### Optimization of worst-case cost

The following lemma, cf. §A.1.2 for proof, suggests a specific means of constructing $D$, so as to ensure that $\Theta_{m}$ defines a high probability credibility region:

The data matrices $(\mathcal{A},\mathcal{B},\mathcal{C},\mathcal{P},\mathcal{F},\mathcal{G},\mathcal{H})$ satisfy, for all $X$ with ${I - {X^{\top}\mathcal{P}X}} \succeq 0$, the robust fractional quadratic matrix inequality

This paper is concerned with control of uncertain linear dynamical systems, with the goal of maximizing (minimizing) rewards (costs) that are a quadratic function of states and...
