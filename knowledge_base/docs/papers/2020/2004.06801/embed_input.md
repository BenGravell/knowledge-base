Scalable Autonomous Vehicle Safety Validation through Dynamic Programming and Scene Decomposition

Topics include Autonomous driving, Vehicles, Safety, Scalability, Dynamic programming.

An open question in autonomous driving is how best to use simulation to validate the safety of autonomous vehicles. Existing techniques rely on simulated rollouts, which can be inefficient for finding rare failure events, while other techniques are designed to only discover a single failure. In this work, we present a new safety validation approach that attempts to estimate the distribution over failures of an autonomous policy using approximate dynamic programming. Knowledge of this distribution allows for the efficient discovery of many failure examples. To address the problem of scalability, we decompose complex driving scenarios into subproblems consisting of only the ego vehicle and one other vehicle. These subproblems can be solved with approximate dynamic programming and their solutions are recombined to approximate the solution to the full scenario. We apply our approach to a simple two-vehicle scenario to demonstrate the technique as well as a more complex five-vehicle scenario to demonstrate scalability. In both experiments, we observed an increase in the number of failures discovered compared to baseline approaches.

## INTRODUCTION

One common practice for automated vehicle (AV) safety validation is to maintain a suite of challenging driving scenarios that the vehicle must successfully navigate after each update to the driving policy. Although useful, this approach will miss any failures that are not already included in the test suite. Automated testing procedures that treat the vehicle as a black box must be developed to catch unknown and unexpected failure modes of the AV which could dramatically decrease testing time and improve the safety of autonomous vehicles.

Much of the literature on black box testing focuses on falsification where inputs are generated that cause a system to violate a safety specification. Those inputs serve as a counter example to the hypothesis that the system is safe. For autonomous driving, it is not feasible to create an agent that can avoid all possible accidents, so rather than find any failure of an AV, it is preferable to find the most likely failures. Traditional falsification techniques do not consider the probability of the failures they find and are therefore ill-suited to this goal....

## CONCLUSIONS

In this work, we have made progress toward the goal of automated testing of autonomous vehicles. We introduced a safety validation formulation that uses approximate dynamic programming to estimate the distribution over failures and create sequences of disturbances that cause an autonomous system to fail. The problem of scalability was addressed by decomposing the driving scenario into pairwise interactions between the ego vehicles and other agents on the road. These subproblems were solved and recombined to estimate the probability of failure of the full system....

Considering the definition of $f^{\ast}{(\tau)}$, we have

The space of all trajectories is exponential in the legnth of the trajectory, so it will be challenging to represent the distribution $f{(\tau)}$ directly. To reduce the dimensionality of the distribution we assume that the SUT and environment are Markov. The current disturbance $x$ and next state $s^{\prime}$ will only depend on the current state $s$ such that

This section describes two experimental driving scenarios, a simple scenario with two vehicles, and a more complex scenario with five vehicles. The simulations were designed with AutomotiveSimulator.jl, an open-source julia package....
