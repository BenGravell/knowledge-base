URLB: Unsupervised Reinforcement Learning Benchmark

Topics include Reinforcement learning, Unsupervised reinforcement learning, Benchmarks, Reward-free pretraining, DeepMind control suite, Intrinsic rewards, Continuous control, Open-source benchmark.

Introduces URLB, a two-phase benchmark for unsupervised RL in which agents first pretrain without rewards and then adapt to downstream control tasks. The benchmark standardizes environments and baselines, making it easier to compare intrinsic-motivation methods and exposing that existing approaches still struggle on broad continuous-control pretraining.

Deep Reinforcement Learning (RL) has emerged as a powerful paradigm to solve a range of complex yet specific control tasks. Yet training generalist agents that can quickly adapt to new tasks remains an outstanding challenge. Recent advances in unsupervised RL have shown that pre-training RL agents with self-supervised intrinsic rewards can result in efficient adaptation. However, these algorithms have been hard to compare and develop due to the lack of a unified benchmark. To this end, we introduce the Unsupervised Reinforcement Learning Benchmark (URLB). URLB consists of two phases: reward-free pre-training and downstream task adaptation with extrinsic rewards. Building on the DeepMind Control Suite, we provide twelve continuous control tasks from three domains for evaluation and open-source code for eight leading unsupervised RL methods. We find that the implemented baselines make progress but are not able to solve URLB and propose directions for future research.

## Introduction

Deep Reinforcement Learning (RL) has been at the source of a number of breakthroughs in autonomous control over the last five years. RL algorithms have been used to train agents to play Atari video games directly from pixels, learn robotic locomotion and manipulation policies from raw sensory input, master the game of Go, and play large-scale multiplayer video games. While these results were significant advances in autonomous decision making, a deeper look reveals a fundamental limitation. The above algorithms produced agents capable of only solving the single task they were trained to solve.

To make benchmarking and developing new unsupervised RL approaches easier, we introduce the Unsupervised Reinforcement Learning Benchmark (URLB). Built on top of the widely adopted DeepMind Control Suite, URLB provides a suite of domains of varying difficulty for unsupervised pre-training with diverse downstream evaluation tasks. URLB standardizes evaluation of unsupervised RL algorithms by defining fixed pre-training and fine-tuning procedures across all baselines.

We introduce URLB, a new benchmark for evaluating unsupervised RL algorithms, which consists of three domains and twelve continuous control tasks of varying difficulty to evaluate the adaptation efficiency of unsupervised RL algorithms.

## Conclusion

We presented URLB, a benchmark designed to measure the performance of unsupervised RL algorithms. URLB consists of a suite of twelve evaluation tasks of varying difficulty from three domains and standardized procedures for pre-training and evaluation. We've open-sourced implementations and evaluation scores for eight leading unsupervised RL algorithms from all major algorithm categories. To minimize confounding factors, we utilized the same optimization method across all baselines. While none of the implemented baselines solve URLB, many make substantial progress suggesting a number of fruitful directions for unsupervised RL research.
