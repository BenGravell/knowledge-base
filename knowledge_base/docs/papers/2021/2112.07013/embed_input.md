PantheonRL: A MARL Library for Dynamic Training Interactions

We present PantheonRL, a multiagent reinforcement learning software package for dynamic training interactions such as round-robin, adaptive, and ad-hoc training. Our package is designed around flexible agent objects that can be easily configured to support different training interactions, and handles fully general multiagent environments with mixed rewards and n agents. Built on top of StableBaselines3, our package works directly with existing powerful deep RL algorithms. Finally, PantheonRL comes with an intuitive yet functional web user interface for configuring experiments and launching multiple asynchronous jobs. Our package can be found at

## Introduction

Multiagent reinforcement learning (MARL) is becoming increasingly important as more AI systems are being deployed. Many potential applications of MARL involve dynamic interactions between agents, such as agents adapting to each other, ad-hoc coordination, and more (Fig 1). However, experimenting with these dynamic interactions using modern deep RL frameworks can be a difficult process. Existing MARL libraries are largely designed around training a fix set of agents, making them unsuitable for experimenting with more dynamic and adaptive agent interactions.

We propose $\mathsf{P}\mathsf{a}\mathsf{n}\mathsf{t}\mathsf{h}\mathsf{e}\mathsf{o}\mathsf{n}\mathsf{R}\mathsf{L}$, an easy-to-use and extensible MARL software package that focuses on dynamic interactions between agents.

to support adaptive MARL, with dynamic training interactions ranging from self-play, round-robin, adaptive (few-shot), and ad-hoc (zero-shot) training,

to provide a web user interface for launching and monitoring experiments, with support for the different dynamic training interactions described above.

## Discussion

With focus on adaptive MARL and dynamic training interactions, $\mathsf{P}\mathsf{a}\mathsf{n}\mathsf{t}\mathsf{h}\mathsf{e}\mathsf{o}\mathsf{n}\mathsf{R}\mathsf{L}$ is a valuable addition to the MARL software ecosystem. The modularity of the agent policies combined with the inheritance of $\mathsf{S}\mathsf{t}\mathsf{a}\mathsf{b}\mathsf{l}\mathsf{e}\mathsf{B}\mathsf{a}\mathsf{s}\mathsf{e}\mathsf{l}\mathsf{i}\mathsf{n}\mathsf{e}\mathsf{s}\mathsf{3}$ capabilities together give users a flexible and powerful library for experimenting with complex multiagent interactions.
