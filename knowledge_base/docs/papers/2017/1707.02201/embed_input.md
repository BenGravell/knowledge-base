Learning Human Behaviors from Motion Capture by Adversarial Imitation

Rapid progress in deep reinforcement learning has made it increasingly feasible to train controllers for high-dimensional humanoid bodies. However, methods that use pure reinforcement learning with simple reward functions tend to produce non-humanlike and overly stereotyped movement behaviors. In this work, we extend generative adversarial imitation learning to enable training of generic neural network policies to produce humanlike movement patterns from limited demonstrations consisting only of partially observed state features, without access to actions, even when the demonstrations come from a body with different and unknown physical parameters. We leverage this approach to build sub-skill policies from motion capture data and show that they can be reused to solve tasks when controlled by a higher level controller.

## Introduction

The problem of building a programmable humanoid dates back centuries. In 1495, five years after drawing the Vitruvian Man, Leonardo da Vinci constructed a humanoid automaton in the form of an armored knight. The knight was able to wave, sit up, and open and close its jaw via power delivered by a crank. Unlike most clockwork automata, which could only produce movements along individual limit cycles, the mechanical knight could be re-programmed to vary its movements, enabling refinement of the arm movements or alternative sequences of movements in time.

From a contemporary perspective, optimal control and reinforcement learning methods are enabling the design of movement controllers that can cope with the high-dimensionality of humanoid bodies, and neural networks are able to store multiple patterns of movement that can be reused, refined, and flexibly sequenced. Working towards a robust procedure for constructing controllers with a range of humanlike movements suited for reuse and refinement when employed in new tasks is the goal of this paper.

In this work, we present a pipeline for training low-level controllers to produce behaviors from motion capture using an extension of GAIL; and embedding the low-level controllers into larger control systems wherein a high-level controller learns by RL to modulate the low-level controller to solve new tasks (Figure 1). The acquisition of multiple behaviors from noisy motion capture data ("real-to-sim\") requires two extensions to the GAIL framework.

## Discussion

Looking beyond the scope of engineering skilled motor behaviors for humanoids, we think there is a broader issue to consider in the design of artificial agents. To communicate complex behaviors to agents, it is often most straightforward to demonstrate them. In contrast, it is extremely difficult to formalize different behaviors with simple reward functions.

Therefore, a core motivation to use imitation learning is that we lack good objective functions to describe complex behaviors. This necessarily presents an obstacle when developing and assessing algorithms as well as when monitoring convergence (not dissimilar from the difficulty of assessing generated samples from GANs). At present, we must rely on human judgment of the quality of the behaviors we have produced.
