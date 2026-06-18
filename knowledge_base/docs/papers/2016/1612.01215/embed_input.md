Do What I Want, Not What I Did: Imitation of Skills by Planning Sequences of Actions

Topics include Motion planning, Robotics, Sampling-based methods, Planning, Learning, Sampling.

We propose a learning-from-demonstration approach for grounding actions from expert data and an algorithm for using these actions to perform a task in new environments. Our approach is based on an application of sampling-based motion planning to search through the tree of discrete, high-level actions constructed from a symbolic representation of a task. Recursive sampling-based planning is used to explore the space of possible continuous-space instantiations of these actions. We demonstrate the utility of our approach with a magnetic structure assembly task, showing that the robot can intelligently select a sequence of actions in different parts of the workspace and in the presence of obstacles. This approach can better adapt to new environments by selecting the correct high-level actions for the particular environment while taking human preferences into account.

## Introduction

Learning from demonstration has emerged as a useful paradigm to teach robots the skills they need to interact with the real world. The challenge in learning from demonstration is to generalize what is learned to new contexts and new tasks. Consider a moderately complex task such as assembling part of a structure, shown in Fig. 1 and defined by the PDDL in Fig. 3. The precise movements and the particular movement goals and parameters will vary from one situation to the next....

Adapting to new environments in the context of task and motion planning poses several challenges when attempting to generalize learned actions. Recently there has been significant progress in integrating symbolic task planning and continuous motion planning, which have in the past evolved as two separate fields. At the same time, learning from demonstration has been established as a powerful tool for learning models of individual actions....

## Conclusions

We described a practical approach for task and motion planning based on models of skills grounded from expert demonstrations of skills. By representing actions as probability distributions learned from expert demonstrations, we create a framework that can combine a broad range of actions to accomplish a task. We validated this approach with experiments in a structure assembly domain both in simulation and in a real robot....

### IV-B Task Planning Algorithm

### IV-A Local Planning Algorithm

Figure 4: Illustration of the proposed algorithm. Boxes w1, w2, etc. indicate regions corresponding to the predicate state after each action, while dashed lines represent continuous state trajectories.

Figure 1: UR5 performing part of a structure assembly task by grabbing a link object in order to connect it to a node. Actions and goals were defined by human demonstrations.

Figure 2: Approach for grounding actions in symbolic planning. Training data represents actions connecting symbolic states in the graph of possible actions that constitute valid solutions to the task plan.

In our approach, probabilistic models over features associated with each action are learned from human demonstrations and later refined in a supervised manner using additional robot-generated examples scored by a human teacher. At the core of this approach lies a mapping from symbolic actions (e.g....
