DeepMind Control Suite

The DeepMind Control Suite is a set of continuous control tasks with a standardised structure and interpretable rewards, intended to serve as performance benchmarks for reinforcement learning agents. The tasks are written in Python and powered by the MuJoCo physics engine, making them easy to use and modify. We include benchmarks for several learning algorithms. The Control Suite is publicly available at. A video summary of all tasks is available at.

## Introduction

Controlling the physical world is an integral part and arguably a prerequisite of general intelligence. Indeed, the only known example of general-purpose intelligence emerged in primates which had been manipulating the world for millions of years.

Physical control tasks share many common properties and it is sensible to consider them as a distinct class of behavioural problems. Unlike board games, language and other symbolic domains, physical tasks are fundamentally continuous in state, time and action. Their dynamics are subject to second-order equations of motion, implying that the underlying state is composed of position-like and velocity-like variables, while state derivatives are acceleration-like. Sensory signals (i.e. observations) usually carry meaningful physical units and vary over corresponding timescales.

Table 1: Mean and Standard Error of 100 episodes after 108 training steps for each seed.

Table 2: Mean and standard error of 100 episodes after 24 hours of training for each seed.

The bindings provide easy access to all MuJoCo library functions, automatically converting NumPy arrays to data pointers where appropriate.

Starting an episode and running it to completion might look like

physics.data.ctrl = \... \# and control.

This decade has seen rapid progress in the application of Reinforcement Learning (RL) techniques to difficult problem domains such as video games. The Arcade Learning Environment was a vital facilitator of these developments, providing a set of standard benchmarks for evaluating and comparing learning algorithms. The DeepMind Control Suite provides a similar set of standard benchmarks for continuous control problems.

The OpenAI Gym currently includes a set of continuous control domains that has become the de-facto benchmark in continuous RL. The Control Suite is also a set of tasks for benchmarking continuous RL algorithms, with a few notable differences. We focus exclusively on continuous control, e.g. separating observations with similar units (position, velocity, force etc.) rather than concatenating into one vector. Our unified reward structure (see below) offers interpretable learning curves and aggregated suite-wide performance measures....

In Section 2 we explain the general structure of the Control Suite and in Section 3 we describe each domain in detail....
