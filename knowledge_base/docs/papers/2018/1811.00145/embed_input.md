Scalable End-to-End Autonomous Vehicle Testing via Rare-event Simulation

Topics include Autonomous driving, Vehicles, Control, Learning, Sampling, Monte Carlo methods, AV, De facto.

While recent developments in autonomous vehicle (AV) technology highlight substantial progress, we lack tools for rigorous and scalable testing. Real-world testing, the de facto evaluation environment, places the public in danger, and, due to the rare nature of accidents, will require billions of miles in order to statistically validate performance claims. We implement a simulation framework that can test an entire modern autonomous driving system, including, in particular, systems that employ deep-learning perception and control algorithms. Using adaptive importance-sampling methods to accelerate rare-event probability evaluation, we estimate the probability of an accident under a base distribution governing standard traffic behavior. We demonstrate our framework on a highway scenario, accelerating system evaluation by 2-20 times over naive Monte Carlo sampling methods and 10-300 mathsfP times (where mathsfP is the number of processors) over real-world testing.

## Introduction

Recent breakthroughs in deep learning have accelerated the development of autonomous vehicles (AVs); many research prototypes now operate on real roads alongside human drivers. While advances in computer-vision techniques have made human-level performance possible on narrow perception tasks such as object recognition, several fatal accidents involving AVs underscore the importance of testing whether the perception and control pipeline---when considered as a *whole system*---can safely interact with humans....

Motivated by the challenges underlying real-world testing and formal verification, we consider a probabilistic paradigm---which we call a *risk-based framework*---where the goal is to evaluate the *probability of an accident* under a base distribution representing standard traffic behavior. By assigning learned probability values to environmental states and agent behaviors, our risk-based framework considers performance of the AV's policy under a data-driven model of the world....

The cross-entropy method was introduced by Rubinstein and has attracted interest in many rare-event simulation scenarios. More broadly, it can be thought of as a model-based optimization method. With respect to assessing safety of AVs, the cross-entropy method has recently been applied in simple lane-changing and car-following scenarios in two dimensions. Our work significantly extends these works by implementing a photo-realistic simulator that can assess the deep-learning based perception pipeline along with the control framework. We leave the development of rare-event simulation methods that scale better with dimension as a future work.

To summarize, a fundamental tradeoff emerges when comparing the requirements of our risk-based framework to other testing paradigms, such as real-world testing or formal verification. Real-world testing endangers the public but is still in some sense a gold standard. Verified subsystems provide evidence that the AV should drive safely even if the estimated distribution shifts, but verification techniques are limited by computational intractability as well as the need for both white-box models and the completeness of specifications that assign blame (e.g. )....

### System architecture

### Definition 1

Figure 2: The ratio of (a) number of rare events and (b) variance of estimator for pγ between cross-entropy method...
