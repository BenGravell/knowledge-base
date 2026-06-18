Learning Sampling Distributions for Robot Motion Planning

Topics include Motion planning, Robotics, Variational autoencoders, Autoencoders, Probabilistic models, Sampling-based methods, Planning, Learning, Sampling, State space.

A defining feature of sampling-based motion planning is the reliance on an implicit representation of the state space, which is enabled by a set of probing samples. Traditionally, these samples are drawn either probabilistically or deterministically to uniformly cover the state space. Yet, the motion of many robotic systems is often restricted to "small" regions of the state space, due to, for example, differential constraints or collision-avoidance constraints. To accelerate the planning process, it is thus desirable to devise non-uniform sampling strategies that favor sampling in those regions where an optimal solution might lie. This paper proposes a methodology for non-uniform sampling, whereby a sampling distribution is learned from demonstrations, and then used to bias sampling. The sampling distribution is computed through a conditional variational autoencoder, allowing sample generation from the latent space conditioned on the specific planning problem....

## Introduction

Sampling-based motion planning (SBMP) has emerged as a successful algorithmic paradigm for solving high-dimensional, complex, and dynamically-constrained motion planning problems. A defining feature of SBMP is the reliance on an implicit representation of the state space, achieved through sampling the feasible space and probing local connections through a black-box collision checking module. Traditionally, these samples are drawn either probabilistically or deterministically to uniformly cover the state space....

Figure 1: A fast marching tree (FMT∗) generated with learned samples for a double integrator, conditioned on the initial state (red circle), goal region (blue circle), and workspace obstacles (black). Note the significantly higher density of samples in the region around the solution.

### Application in Practice

Note again, the goal of this work is to compute a distribution representing promising regions (i.e., regions where optimal motion plans are likely to be found) through a learned latent representation of the system conditioned on the planning problem. During the offline CVAE training phase, we recommend training from optimal motion plans to best demonstrate promising regions. We generally train on the order of one hundred thousand motion plans, the generation of which can be accelerated with approximately optimal, GPU-based planning algorithms....

Figure 4: An example spacecraft debris recovery problem, whereby the spacecraft must maneuver from an initial state to recover debris (shown in the figure inset in green) between its end effectors, while avoiding obstacles (blue). The spacecraft (red) is modeled as a double integrator with a pair of 3 DoF kinematic arms (shown in the figure inset in black).

We now examine the methodology in detail, following along with the outline below. It begins with an offline phase which trains the CVAE, to be later sampled from. Line 1 initializes this phase with the required demonstration data. This data (states and any additional planning problem information) may be from successful motion plans, previous trajectories in the state space, human demonstration, or other sources that provide insight into how the system operates....

### Fraction of Learned Samples ($\lambda$)
