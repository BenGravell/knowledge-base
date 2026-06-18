OpenAI Gym

Topics include OpenAI Gym, Reinforcement learning, Benchmarking, Simulation environments, Research infrastructure, Standardized interface, Open-source software.

Introduces OpenAI Gym as a common interface and benchmark collection for reinforcement learning experiments. Its main contribution is infrastructural: standardizing environments, result sharing, and evaluation workflows so RL algorithms can be compared more consistently.

OpenAI Gym is a toolkit for reinforcement learning research. It includes a growing collection of benchmark problems that expose a common interface, and a website where people can share their results and compare the performance of algorithms. This whitepaper discusses the components of OpenAI Gym and the design decisions that went into the software.

## Introduction

Reinforcement learning (RL) is the branch of machine learning that is concerned with making sequences of decisions. RL has a rich mathematical theory and has found a variety of practical applications. Recent advances that combine deep learning with reinforcement learning have led to a great deal of excitement in the field, as it has become evident that general algorithms such as policy gradients and Q-learning can achieve good performance on difficult problems, without problem-specific engineering.

To build on recent progress in reinforcement learning, the research community needs good benchmarks on which to compare algorithms. A variety of benchmarks have been released, such as the Arcade Learning Environment (ALE), which exposed a collection of Atari 2600 games as reinforcement learning problems, and recently the RLLab benchmark for continuous control, to which we refer the reader for a survey on other RL benchmarks, including. OpenAI Gym aims to combine the best elements of these previous benchmark collections, in a software package that is maximally convenient and accessible.

Alongside the software library, OpenAI Gym has a website ([gym.openai.com](gym.openai.com)) where one can find scoreboards for all of the environments, showcasing results submitted by users. Users are encouraged to provide links to source code and detailed instructions on how to reproduce their results.

## Design Decisions

The design of OpenAI Gym is based on the authors' experience developing and comparing reinforcement learning algorithms, and our experience using previous benchmark collections. Below, we will summarize some of our design decisions.
