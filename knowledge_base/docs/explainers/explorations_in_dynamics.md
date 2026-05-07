# Explorations in Dynamics

*A few fascinating works that delve into the wild and wonderful world of systems that evolve over time.*

## Physics in *N* dimensions

[Marc ten Bosch](https://marctenbosch.com/) developed a formulation for rigid body dynamics that is **independent of the dimension of the space**, which is described using geometric algebra.

An interesting issue that was also solved was that of **collision resolution**, which is handled elegantly for convex polytopes.

### Links

- [SIGGRAPH 2020 paper](https://marctenbosch.com/ndphysics/NDrigidbody.pdf)
- [4D Toys app](https://4dtoys.com/)
- [Miegakure computer game](https://miegakure.com/)
- [Two Minute Papers](https://youtu.be/nkHL1GNU18M)

## Reaction-diffusion dynamics

Reaction-diffusion dynamics generalize the diffusion-only dynamics readers may be familiar with from the field of networked systems, which can actually be thought of as a discretization of the diffusion/heat partial differential equation. When the new reaction term is added, rather interesting behavior emerges due to the nonlinearities in the dynamics.

Check out [Robert Munafo’s exploration](https://mrob.com/pub/comp/xmorphia/) of different regimes of the parameter space of the reaction-diffusion dynamics.

One particularly interesting setting is called the [“U-skate world”](https://mrob.com/pub/comp/xmorphia/uskate-world.html) which exhibits emergent patterns similar to Conway’s Game of Life e.g. the appearance of [“still-lifes”](https://en.wikipedia.org/wiki/Still_life_(cellular_automaton)) (small patterns that retain their structure over time) and [“gliders”](https://en.wikipedia.org/wiki/Glider_(Conway%27s_Game_of_Life)) (small patterns that retain their structure over time and move across the state-space by delicate balancing of the forces over their bodies).

## SmoothLife

Conway’s Game of Life was a seminal development in computer science that spurred thought about information theory. It was a simple set of rules meant to mimic conditions of population pressures and incentives in living creatures, known as a cellular automata. The game is played on a grid and each cell has a binary state which is updated at discrete time steps. Stephan Rafler generalized the mathematical formulation of this game to continuous state and time, leading to qualitatively similar behavior as Conway’s Game, but with much more organic and arguably richer phenomena, including self-propelled gliders and chain-like structures.

### Links

- [Paper on arXiv](https://arxiv.org/pdf/1111.1567)
- [Code on SourceForge](https://sourceforge.net/projects/smoothlife/)
- [SmoothLifeL on YouTube](https://www.youtube.com/watch?v=KJe9H6qS82I)
- [Lex Fridman's interview with Stephen Wolfram on cellular automata](https://www.youtube.com/watch?v=VguG_y05Xe8)
