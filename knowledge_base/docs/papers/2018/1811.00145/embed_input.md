Scalable End-to-End Autonomous Vehicle Testing via Rare-event Simulation

Topics include Autonomous driving, Vehicles, Control, Learning, Sampling, Monte Carlo methods, AV, De facto.

While recent developments in autonomous vehicle (AV) technology highlight substantial progress, we lack tools for rigorous and scalable testing. Real-world testing, the de facto evaluation environment, places the public in danger, and, due to the rare nature of accidents, will require billions of miles in order to statistically validate performance claims. We implement a simulation framework that can test an entire modern autonomous driving system, including, in particular, systems that employ deep-learning perception and control algorithms. Using adaptive importance-sampling methods to accelerate rare-event probability evaluation, we estimate the probability of an accident under a base distribution governing standard traffic behavior. We demonstrate our framework on a highway scenario, accelerating system evaluation by 2-20 times over naive Monte Carlo sampling methods and 10-300 mathsfP times (where mathsfP is the number of processors) over real-world testing.

## Introduction

Recent breakthroughs in deep learning have accelerated the development of autonomous vehicles (AVs); many research prototypes now operate on real roads alongside human drivers. While advances in computer-vision techniques have made human-level performance possible on narrow perception tasks such as object recognition, several fatal accidents involving AVs underscore the importance of testing whether the perception and control pipeline---when considered as a *whole system*---can safely interact with humans.

Motivated by the challenges underlying real-world testing and formal verification, we consider a probabilistic paradigm---which we call a *risk-based framework*---where the goal is to evaluate the *probability of an accident* under a base distribution representing standard traffic behavior. By assigning learned probability values to environmental states and agent behaviors, our risk-based framework considers performance of the AV's policy under a data-driven model of the world.

Formally, we let $P_{0}$ denote the base distribution that models standard traffic behavior and $X \sim P_{0}$ be a realization of the simulation (e.g. weather conditions and driving policies of other agents). For an objective function $f:{\mathcal{X}\rightarrow{\mathbb{R}}}$ that measures "safety"---so that low values of $f{(x)}$ correspond to dangerous scenarios---our goal is to evaluate the probability of a dangerous event

for some threshold $\gamma$. Our risk-based framework is agnostic to the complexity of the ego-policy and views it as a black-box module. Such an approach allows, in particular, deep-learning based perception systems that make formal verification methods intractable.

As a system, our simulator allows fully distributed rollouts, making our approach orders of magnitude cheaper, faster, and safer than real-world testing. Using the asynchronous messaging library ZeroMQ, our implementation is fully-distributed among available CPUs and GPUs; our rollouts are up to $30\mathsf{P}$ times faster than real time, where $\mathsf{P}$ is the number of processors. Combined with the cross-entropy method's speedup, we achieve $10$-$300\mathsf{P}$ speedup over real-world testing.
