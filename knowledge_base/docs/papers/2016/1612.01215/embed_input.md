Do What I Want, Not What I Did: Imitation of Skills by Planning Sequences of Actions

Topics include Motion planning, Robotics, Sampling-based methods, Planning, Learning, Sampling.

We propose a learning-from-demonstration approach for grounding actions from expert data and an algorithm for using these actions to perform a task in new environments. Our approach is based on an application of sampling-based motion planning to search through the tree of discrete, high-level actions constructed from a symbolic representation of a task. Recursive sampling-based planning is used to explore the space of possible continuous-space instantiations of these actions. We demonstrate the utility of our approach with a magnetic structure assembly task, showing that the robot can intelligently select a sequence of actions in different parts of the workspace and in the presence of obstacles. This approach can better adapt to new environments by selecting the correct high-level actions for the particular environment while taking human preferences into account.

## Introduction

Learning from demonstration has emerged as a useful paradigm to teach robots the skills they need to interact with the real world. The challenge in learning from demonstration is to generalize what is learned to new contexts and new tasks. Consider a moderately complex task such as assembling part of a structure, shown in Fig. 1 and defined by the PDDL in Fig. 3. The precise movements and the particular movement goals and parameters will vary from one situation to the next.

Adapting to new environments in the context of task and motion planning poses several challenges when attempting to generalize learned actions. Recently there has been significant progress in integrating symbolic task planning and continuous motion planning, which have in the past evolved as two separate fields. At the same time, learning from demonstration has been established as a powerful tool for learning models of individual actions.

In our approach, probabilistic models over features associated with each action are learned from human demonstrations and later refined in a supervised manner using additional robot-generated examples scored by a human teacher. At the core of this approach lies a mapping from symbolic actions (e.g. approach, grasp) to physical motions encoded probabilistically as a distribution over observed features along each motion trajectory. Fig. 2 shows this relationship: multiple demonstrations connect predicate states, which allow us to learn a model of each action.

The contributions of this paper are: a new method for reproducing demonstrated actions in novel environments, derived from sampling-based motion planning; an algorithm for combining these learned actions for executing multi-step tasks with multiple valid plans; and experimental validation of this algorithm on a simple assembly task as shown in Fig. 1. Experiments in a 2D Android game domain were omitted for reasons of space.
