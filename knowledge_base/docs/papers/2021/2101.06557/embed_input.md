TrafficSim: Learning to Simulate Realistic Multi-Agent Behaviors

Simulation has the potential to massively scale evaluation of self-driving systems enabling rapid development as well as safe deployment. To close the gap between simulation and the real world, we need to simulate realistic multi-agent behaviors. Existing simulation environments rely on heuristic-based models that directly encode traffic rules, which cannot capture irregular maneuvers (e.g., nudging, U-turns) and complex interactions (e.g., yielding, merging). In contrast, we leverage real-world data to learn directly from human demonstration and thus capture a more diverse set of actor behaviors. To this end, we propose TrafficSim, a multi-agent behavior model for realistic traffic simulation. In particular, we leverage an implicit latent variable model to parameterize a joint actor policy that generates socially-consistent plans for all actors in the scene jointly. To learn a robust policy amenable for long horizon simulation, we unroll the policy in training and optimize through the fully differentiable simulation across time. Our learning objective incorporates both human demonstrations as well as common sense....

## Introduction

Self-driving has the potential to make drastic impact on our society. One of the key remaining challenges is how to measure progress. There are three main approaches for measuring the performance of a self-driving vehicle (SDV): 1) structured testing in the real world, 2) virtual replay of pre-recorded scenarios, and 3) simulation. These approaches are complementary, and each has its key advantages and shortcomings. The use of a test track enables structured and repeatable evaluation in the physical world....

Figure 1: Generating realistic multi-agent behaviors is a key component for simulation

## Conclusion

In this work, we have proposed a novel method for generating diverse and realistic traffic simulation. TrafficSim is a multi-agent behavior model that generates socially-consistent plans for all actors in the scene jointly. It is learned using back-propagation through the fully differentiable simulation, by imitating trajectory observations from a real-world self driving dataset and incorporating common sense. TrafficSim enables exciting new possibilities in data augmentation, interactive scenario design, and safety evaluation....

We use Huber loss $L_{\delta}$ for reconstruction and reweight the KL term with $\beta$ as proposed by.

Figure 5: We optimize our policy with back-propagation through the differentiable simulation (left), and apply imitation and common sense loss at each simulated state (right).

Table 2: [ATG4D] Ablation study (S = 15 samples, T = 12 seconds, Tlabel = 8 seconds)

Simulation systems typically consists of three steps: 1) specifying the scene layout which includes the road topology and actor placement, 2) simulating the motion of dynamic agents forward, and 3) rendering the generated scenario with realistic geometry and appearance, as shown in Figure 1. In this paper, we focus on the second step: generating realistic multi-agent behaviors automatically....

Figure 2: Complex human driving behavior observed in the real world: red is actor of interest, green are interacting actors

However, bridging the behavior gap between the simulated world and the real world remains an open challenge. Manually specifying each actor's trajectory is not scalable and results in unrealistic simulations since the actors will not react to the SDV actions....
