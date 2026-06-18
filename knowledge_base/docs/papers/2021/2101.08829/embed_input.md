Centralized Collision-free Polynomial Trajectories and Goal Assignment for Aerial Swarms

Topics include Robotics, Swarm robotics, Cooperative robotics, Multi-agent systems, Aerial swarms, Autonomous drones, Quadrotors, Uncrewed aerial vehicle coordination, Formation control, Centralized planning, Goal assignment, Task allocation, Assignment problem, Hungarian algorithm, Motion planning, Collision-free motion planning, Collision avoidance, Trajectory planning, Trajectory optimization, Polynomial trajectories.

Follow-up to earlier work "Concurrent Goal Assignment and Collision-Free Trajectory Generation for Multiple Aerial Robots" that makes fewer unrealistic assumptions (e.g. no instant altitude teleporting, kinodynamic constraints). Cool demo showing scaling up to swarms with 1000 agents for making arbitrary formation patterns like words and letters.

Computationally tractable methods are developed for centralized goal assignment and planning of collision-free polynomial-in-time trajectories for systems of multiple aerial robots. The method first assigns robots to goals to minimize total time-in-motion based on initial trajectories. By coupling the assignment and trajectory generation, the initial motion plans tend to require only limited collision resolution. The plans are then refined by checking for potential collisions and resolving them using either start time delays or altitude assignment. Numerical experiments using both methods show significant reductions in the total time required for agents to arrive at goals with only modest additional computational effort in comparison to state-of-the-art prior work, enabling planning for thousands of agents.

## Introduction

In the burgeoning field of autonomous robotics, aerial robots are quickly becoming a useful platform for firefighting, police, search-and-rescue, surveillance, and product delivery. In the deployment of large fleets of such robots, trajectory plans must satisfy the competing criteria of safety and performance. Specifically, the safety requirement of avoiding vehicle-to-vehicle collisions and the performance requirement of minimizing time-in-flight are considered. As the number of robots increases, so too does the complexity of satisfying these requirements, warranting the development of computationally tractable methods to this end.

A wide class of traditional single-agent motion planning methods rely on discretization of the state space and definition of a related state-transition graph. Optimal feasible paths are then found through a graph search or other combinatorial solvers. While these methods can solve the multi-agent planning problem e.g. as in, they become computationally intractable quickly as the number of agents increases, leading to an exponential growth of the search space dimensionality. Some methods have been explored which reduce the search space dimensionality, but are unable to sufficiently reduce the complexity for large numbers of agents....

Future work also includes extension to agents with more complex dynamics and/or motion constraints, dealing with uncontrolled obstacles, combining time delays with altitudes, reassigning goals dynamically to further reduce would-be collisions, and a parallel implementation to decrease solve times. Investigation of the setting when there are more goals than agents and the setting of multiple stages is also warranted, both requiring dynamic goal assignment and replanning.

Regarding the hardware implementation, refinements to the localization and state estimation furnished by the camera system as well as using more sophisticated controllers which account for downwash and ground effects could further reduce the magnitude of the actual position errors and allow shrinkage of the collision volumes.

### Collision resolution via time delay

represent a polynomial trajectory segment which encodes a polynomial, a heading, and a time interval.

Although altitude assignment resolves primary collisions, the possibility remains of secondary collisions during the vertical descent movements...
