Minimal Actuator Placement with Optimal Control Constraints

We introduce the problem of minimal actuator placement in a linear control system so that a bound on the minimum control effort for a given state transfer is satisfied while controllability is ensured. We first show that this is an NP-hard problem following the recent work of Olshevsky. Next, we prove that this problem has a supermodular structure. Afterwards, we provide an efficient algorithm that approximates up to a multiplicative factor of O(logn), where n is the size of the multi-agent network, any optimal actuator set that meets the specified energy criterion. Moreover, we show that this is the best approximation factor one can achieve in polynomial-time for the worst case. Finally, we test this algorithm over large Erdos-Renyi random networks to further demonstrate its efficiency.

## Introduction

During the past decade, control scientists have developed various tools for the regulation of large-scale systems, with the notable examples of for the control of biological systems, for the regulation of brain and neural networks, for network protection against spreading processes, and for load management in smart grid. On the other hand, the enormous size of these systems and the need for cost-effective control make the identification of a small fraction of their nodes to steer them around the state space a central problem within the control community.

This is a combinatorial task of formidable complexity; as it is shown in, identifying a small set of actuator nodes so that the resultant system is controllable alone is NP-hard. Nonetheless, a controllable system may be practically uncontrollable if the required input energy for the desired state transfers is forbidding, as when the controllability matrix is close to singularity. Therefore, by choosing input nodes to ensure controllability alone, one may not achieve a cost-effective control for the involved state transfers....

## Concluding Remarks

We introduced the problem of minimal actuator placement in a linear system so that a bound on the minimum control effort for a given state transfer is satisfied while controllability is ensured. This problem was shown to be NP-hard and to have a supermodular structure. Moreover, an efficient algorithm was provided for its solution. Finally, the efficiency of this algorithm was illustrated over large Erdős-Rényi random networks. Our future work is focused on investigating the case where no controllability constraint is placed on the end actuator set, as well as, on exploring the effects that the network topology has on this selection.

Note that $\omega$ is chosen independently of the parameters of system. Therefore, the absence of the controllability constraint at Problem (I^′^) for $0 < \epsilon \leq {1/E}$ is fictitious; nonetheless, it obviates the necessity of considering only those actuator sets that render the system controllable.

We consider the problem of actuating a small number of system's states so that the minimum control energy for a given transfer meets some specified criterion and controllability is ensured. The challenge is in doing so using as few actuators as possible....
