Learning and Transfer of Modulated Locomotor Controllers

We study a novel architecture and training procedure for locomotion tasks. A high-frequency, low-level "spinal" network with access to proprioceptive sensors learns sensorimotor primitives by training on simple tasks. This pre-trained module is fixed and connected to a low-frequency, high-level "cortical" network, with access to all sensors, which drives behavior by modulating the inputs to the spinal network. Where a monolithic end-to-end architecture fails completely, learning with a pre-trained spinal module succeeds at multiple high-level tasks, and enables the effective exploration required to learn from sparse rewards. We test our proposed architecture on three simulated bodies: a 16-dimensional swimming snake, a 20-dimensional quadruped, and a 54-dimensional humanoid. Our results are illustrated in the accompanying video at

## Introduction

A newborn antelope attempts its first steps only minutes after birth and is capable of walking within half an hour. A human baby, when lifted so that its feet just graze the ground, will step in a cyclical walking motion. Nature provides clear examples of evolutionarily determined, innate behaviors of surprising complexity, and basic locomotor circuits are well-developed prior to any significant goal-directed experience. The innate structure simplifies the production of goal-directed behavior by confining exploration to stable and coherent, yet flexible dynamics.

On the other hand, machine learning's recent success stories have emphasized rich models with weakly-defined prior structure, sculpted by large amounts of data. And indeed, several recent studies have shown that end-to-end reinforcement learning approaches are capable of generating high-quality motor control policies using generic neural networks. A key question is how to get the best of both worlds: to build modular, hierarchical components that support coherent exploration while retaining the richness and flexibility of data-driven learning.

We believe that the general idea of reusing learned behavioral primitives is important, and the design principles we have followed represent possible steps towards this goal. Our hierarchical design with information hiding has enabled the construction of low-level motor behaviors that are sheltered from task-specific information, enabling their reuse....

Our approach currently depends on the assumption that we can propose a set of low-level tasks that are simple to solve yet whose mastery in turn facilitates the solution of other high-level tasks. For motor behavior, we believe this assumption holds rather generally, as walking, for example, underpins a multitude of more complex tasks. By instilling a relatively small number of reusable skills into the low-level controllers, we expect that a large number of more complicated tasks involving composition of multiple behaviors should become solvable....

### 6-link snake

### Policy gradient with hierarchical noise

Figure 5: Transfer tasks for the quadruped: illustration of the target-seeking (left) and soccer task (right).

Here, we aim to create flexible motor primitives using a reinforcement learning method....
