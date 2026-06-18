An Unsupervised C-Uniform Trajectory Sampler with Applications to Model Predictive Path Integral Control

Topics include Model predictive path integral control, Trajectory optimization, Sampling-based control, Action sampling distribution, Neural networks, Reachable sets.

Extension of C-Uniform trajectory sampling that trains a neural network to approximate the reachable-set-based sampling distribution in an unsupervised manner, achieving similar reachable state coverage as the original method with dramatically faster training time.

Sampling-based model predictive controllers generate trajectories by sampling control inputs from a fixed, simple distribution such as the normal or uniform distributions. This sampling method yields trajectory samples that are tightly clustered around a mean trajectory. This clustering behavior in turn, limits the exploration capability of the controller and reduces the likelihood of finding feasible solutions in complex environments. Recent work has attempted to address this problem by either reshaping the resulting trajectory distribution or increasing the sample entropy to enhance diversity and promote exploration. In our recent work, we introduced the concept of C-Uniform trajectory generation which allows the computation of control input probabilities to generate trajectories that sample the configuration space uniformly. In this work, we first address the main limitation of this method: lack of scalability due to computational complexity. We introduce Neural C-Uniform, an unsupervised C-Uniform trajectory sampler that mitigates scalability issues by computing control input probabilities without relying on a discretized configuration space.

## Introduction

Sampling-based model predictive controllers generate "minimum cost" trajectories using a set of trajectory samples to achieve objectives such as arriving at a goal location while avoiding obstacles and adhering to motion constraints. They have been used in various robotics applications including autonomous driving, manipulation, and drone navigation. In order to generate random trajectories which are also kinematically valid, existing methods sample control inputs using a simple distribution such as the normal distribution. The system model is then used to propagate the state using these random inputs.

In this paper, we address these limitations using an unsupervised learning approach and present the *Neural C-Uniform trajectory sampling method*, in which a neural network is trained to map the state to control input probabilities that lead to C-Uniform trajectories. This approach eliminates the need for discretization and enables the generation of trajectories for longer horizons while maintaining uniformity.

We present Neural C-Uniform trajectory sampler, which uses entropy maximization formulation to generate trajectories that are uniform in the configuration space (Sec. IV).

We present CU-MPPI, a new sampling-based model predictive controller that utilizes Neural C-Uniform trajectories to enhance exploration. By ensuring broad coverage of the C-space, our method increases the likelihood of finding the global minimum regions while reducing dependence on gradient-based refinements (Sec. V).

## Conclusion

In this work, we presented a new approach to choose control input probabilities to sample trajectories which are C-Uniform: At each time step $t$, and for each subset $S$ of the level set $L_{t}$, the probability that the robot is in $S$ is proportional to the measure of $S$. In contrast to our previous work in which the probabilities are obtained by building a flow network based on a discretization of the configuration space, our new approach is based on learning the weights of a neural network which maps robot states to action probability distributions using entropy as unsupervised loss.

Our current implementation of CU-MPPI uses a pre-built map of the environment for localization (the obstacles are not necessarily pre-mapped). In our future work, we are planning to incorporate localization into navigation to remove this dependency.
