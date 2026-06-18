Reciprocal n-Body Collision Avoidance

Topics include Collision avoidance, Multi-robot systems, Velocity obstacles, Reciprocal collision avoidance, Linear programming, Crowd simulation, Decentralized control.

Formalizes reciprocal n-body collision avoidance for many independent agents with no communication. By converting velocity-obstacle constraints into low-dimensional linear programs, the method provides local collision-free velocity choices for thousands of agents in milliseconds and became a basis for ORCA-style multi-agent navigation.

In this paper, we present a formal approach to reciprocal n-body collision avoidance, where multiple mobile robots need to avoid collisions with each other while moving in a common workspace. In our formulation, each robot acts fully independently, and does not communicate with other robots. Based on the definition of velocity obstacles, we derive sufficient conditions for collision-free motion by reducing the problem to solving a low-dimensional linear program. We test our approach on several dense and complex simulation scenarios involving thousands of robots and compute collision-free actions for all of them in only a few milliseconds. To the best of our knowledge, this method is the first that can guarantee local collision-free motion for a large number of robots in a cluttered workspace.
