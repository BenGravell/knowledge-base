Multirobot Coordination with Counting Temporal Logics

Topics include Multi-agent systems, Multi-agent pathfinding, Temporal logic, Formal methods, Mixed-integer programming, Asynchronous coordination, Robotics.

Develops counting temporal logics for specifying collective multi-robot behavior without assigning every robot a unique role. The paper combines logic-based planning, optimization, and robustness to bounded asynchrony, making it a bridge between formal methods and scalable multi-agent coordination.

In many multirobot applications, planning trajectories in a way to guarantee that the collective behavior of the robots satisfies a certain high-level specification is crucial. Motivated by this problem, we introduce counting temporal logics-formal languages that enable concise expression of multirobot task specifications over possibly infinite horizons. We first introduce a general logic called counting linear temporal logic plus (cLTL+), and propose an optimization-based method that generates individual trajectories such that satisfaction of a given cLTL+ formula is guaranteed when these trajectories are synchronously executed. We then introduce a fragment of cLTL+, called counting linear temporal logic (cLTL), and show that a solution to planning problem with cLTL constraints can be obtained more efficiently if all robots have identical dynamics. In the second part of the paper, we relax the synchrony assumption and discuss how to generate trajectories that can be asynchronously executed, while preserving the satisfaction of the desired cLTL+ specification....

## Introduction

inline\]It would be a good idea to write about how solution times are sensitive to encoding methods in the introduction, to motivate why so many variants are introduced. Would also be good to add some intuitive explanations around the encodings, for a part there are just new encoding equations without too much explanation.

Multirobot systems can serve modern societies in a variety of ways, ranging from pure entertainment to critical search and rescue missions, from construction automation to micromanipulation. The number of robots required to achieve a common goal increases each day to improve the effectiveness and efficiency in such applications. Therefore, there is a need for scalable tools to coordinate the collective behavior of large numbers of robots....

## Conclusions

In this paper we presented counting temporal logics (cLTL and cLTL+) that are convenient for specifying desired behaviors for multirobot systems. We also proposed an optimization-based trajectory generation method to synthesize collective behaviors that satisfy specifications given in these formalisms. Furthermore, we showed how to generate trajectories that are robust to bounded asynchrony. We then discussed how to handle continuous-state systems and extended the cLTL+ syntax so that tasks can be assigned to a subset of robots....

### Problem 2

for all $n \in {\lbrack N\rbrack}$ and for all $t \in {\{ 0,\ldots,{h - 1}\}}$. These constraints guarantee that there exists a unique $t$ such that ${z_{loop}{(t)}} = 1$ and ${w_{n}{(h)}} = {w_{n}{(t)}}$. For all other time instances, the first two inequalities are trivially satisfied.

is used. Note that $r_{n}^{({\bigvee_{i}\phi_{i}})}{(t)}$ is only defined if all $\mu_{i}$ are $tcp$. In all other cases, we use the standard encoding:

Traditional algorithms for multirobot coordination tend to focus on relatively simple tasks such as reaching a goal state while avoiding unsafe regions and collisions, or reaching a consensus. Temporal logics, such as Linear Temporal Logic (LTL), provide a powerful framework for defining more complex specifications, for example: *Always avoid collision with obstacles, do not cross into region A before visiting region B, and eventually visit regions A and C repeatedly*....
