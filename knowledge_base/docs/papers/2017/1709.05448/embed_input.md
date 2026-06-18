Learning Sampling Distributions for Robot Motion Planning

Topics include Motion planning, Robotics, Variational autoencoders, Autoencoders, Probabilistic models, Sampling-based methods, Planning, Learning, Sampling, State space.

A defining feature of sampling-based motion planning is the reliance on an implicit representation of the state space, which is enabled by a set of probing samples. Traditionally, these samples are drawn either probabilistically or deterministically to uniformly cover the state space. Yet, the motion of many robotic systems is often restricted to "small" regions of the state space, due to, for example, differential constraints or collision-avoidance constraints. To accelerate the planning process, it is thus desirable to devise non-uniform sampling strategies that favor sampling in those regions where an optimal solution might lie. This paper proposes a methodology for non-uniform sampling, whereby a sampling distribution is learned from demonstrations, and then used to bias sampling. The sampling distribution is computed through a conditional variational autoencoder, allowing sample generation from the latent space conditioned on the specific planning problem.

## Introduction

Sampling-based motion planning (SBMP) has emerged as a successful algorithmic paradigm for solving high-dimensional, complex, and dynamically-constrained motion planning problems. A defining feature of SBMP is the reliance on an implicit representation of the state space, achieved through sampling the feasible space and probing local connections through a black-box collision checking module. Traditionally, these samples are drawn either probabilistically or deterministically to uniformly cover the state space.

In this work we approach this challenge through biasing the sampling of the state space towards these promising regions via learned sample distributions (see Fig. 1). At the core of this methodology is a conditional variational autoencoder (CVAE), which is capable of learning complex manifolds and the regions around them, and is trained from demonstrations of successful motion plans and previous robot experience.

## Future Work

There are many possible avenues open for future research. One promising extension is the incorporation of semantic workspace information through the conditioning variable. These semantic maps show promise towards allowing mobile robots to better understand task specifications and interact with humans. Another promising extension builds upon recent work demonstrating the favorable theoretical properties and improved performance of non-independent samples. An approach to reducing the independence of the samples was presented in Section 5.3, but extensions beyond this exist, including generating large sample sets (e.g., $> 1000$).

In this work we have explored conditioning on workspace maps. However, this was performed only for relatively small, planar problems. Scaling this to large problems is challenging, as the number of conditioning variables grows exponentially with the occupancy grid resolution and with the problem dimensionality. However, our experiments provided promising evidence that this conditioning could be used to substantially improve performance. As such, a promising future line of work is investigating more efficient methods for environment conditioning.
