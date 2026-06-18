RLlib: Abstractions for Distributed Reinforcement Learning

Topics include Reinforcement learning, Scalability, Distributed systems, Control, Learning, RLlib, Distributed reinforcement learning, Abstraction.

Reinforcement learning (RL) algorithms involve the deep nesting of highly irregular computation patterns, each of which typically exhibits opportunities for distributed computation. We argue for distributing RL components in a composable way by adapting algorithms for top-down hierarchical control, thereby encapsulating parallelism and resource requirements within short-running compute tasks. We demonstrate the benefits of this principle through RLlib: a library that provides scalable software primitives for RL. These primitives enable a broad range of algorithms to be implemented with high performance, scalability, and substantial code reuse. RLlib is available at

## Introduction

Advances in parallel computing and composition through symbolic differentiation have been fundamental to the recent success of deep learning. Today, there are a wide range of deep learning frameworks that enable rapid innovation in neural network design and facilitate training at the scale necessary for progress in the field.

In contrast, while the reinforcement learning community enjoys the advances in systems and abstractions for deep learning, there has been comparatively less progress in the design of systems and abstractions that directly target reinforcement learning. Nonetheless, many of the challenges in reinforcement learning stem from the need to scale learning and simulation while also integrating a rapidly increasing range of algorithms and models. As a consequence, there is a fundamental need for composable parallel primitives to support research in reinforcement learning.

## Conclusion

RLlib is an open source library for reinforcement learning that leverages fine-grained nested parallelism to achieve state-of-the-art performance across a broad range of RL workloads. It offers both a collection of reference algorithms and scalable abstractions for easily composing new ones.

[⬇](data:text/plain;base64,ZXZhbHVhdG9ycyA9IFtybGxpYi5Qb2xpY3lFdmFsdWF0b3IucmVtb3RlKAogICAgZW52PVNvbWVFbnYsIGdyYXBoPVBvbGljeUdyYWRpZW50KQogIGZvciBfIGluIHJhbmdlKDEwKV0KcHJpbnQocmF5LmdldChbCiAgICBldi5zYW1wbGUucmVtb3RlKCkgZm9yIGV2IGluIGV2YWx1YXRvcnNdKSk=){download=""}

To leverage RLlib for distributed execution, algorithms must declare their policy $\pi$, experience postprocessor $\rho$, and loss $L$. These can be specified in any deep learning framework, including TensorFlow and PyTorch. RLlib provides policy evaluators and policy optimizers that implement strategies for distributed policy evaluation and training.

Model-based / Hybrid: Model-based RL algorithms extend $\pi_{\theta}{(o_{t},h_{t})}$ to make decisions based on model rollouts, which can be parallelized using Ray. To update their environment models, the model loss can either be bundled with $L$, or the model trained separately (i.e., in parallel using Ray primitives) and its weights periodically updated via $u^{1}$.

In the absence of a single dominant computational pattern (e.g., tensor algebra) or fundamental rules of composition (e.g., symbolic differentiation), the design and...
