DeepMind Control Suite

The DeepMind Control Suite is a set of continuous control tasks with a standardised structure and interpretable rewards, intended to serve as performance benchmarks for reinforcement learning agents. The tasks are written in Python and powered by the MuJoCo physics engine, making them easy to use and modify. We include benchmarks for several learning algorithms. The Control Suite is publicly available . A video summary of all tasks is available .

## Introduction

Controlling the physical world is an integral part and arguably a prerequisite of general intelligence. Indeed, the only known example of general-purpose intelligence emerged in primates which had been manipulating the world for millions of years.

Physical control tasks share many common properties and it is sensible to consider them as a distinct class of behavioural problems. Unlike board games, language and other symbolic domains, physical tasks are fundamentally continuous in state, time and action. Their dynamics are subject to second-order equations of motion, implying that the underlying state is composed of position-like and velocity-like variables, while state derivatives are acceleration-like. Sensory signals (i.e. observations) usually carry meaningful physical units and vary over corresponding timescales.

This decade has seen rapid progress in the application of Reinforcement Learning (RL) techniques to difficult problem domains such as video games. The Arcade Learning Environment was a vital facilitator of these developments, providing a set of standard benchmarks for evaluating and comparing learning algorithms. The DeepMind Control Suite provides a similar set of standard benchmarks for continuous control problems.

## Conclusion and future work

The DeepMind Control Suite is a starting place for the design and performance comparison of reinforcement learning algorithms for physics-based control. It offers a wide range of tasks, from near-trivial to quite difficult. The uniform reward structure allows for robust suite-wide performance measures.

The results presented here for A3C, DDPG, and D4PG constitute baselines using, to the best of our knowledge, well performing implementations of these algorithms. At the same time, we emphasise that the learning curves are not based on exhaustive hyperparameter optimisation, and that for a given algorithm the same hyperparameters were used across all tasks in the Control Suite. Thus, we expect that it may be possible to obtain better performance or data efficiency, especially on a per-task basis.
