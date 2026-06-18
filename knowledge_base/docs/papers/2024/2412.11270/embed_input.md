Monte Carlo Tree Search with Spectral Expansion for Planning with Dynamical Systems

Topics include Trajectory planning, Motion planning, Monte Carlo tree search, Spectral methods, Dynamical systems, Real-time planning, Nonlinear systems, Underactuated systems, Markov decision process.

Bridges Monte Carlo Tree Search and continuous physical dynamics by using the spectrum of locally linearized systems to build a low-complexity discrete model.

The ability of a robot to plan complex behaviors with real-time computation, rather than adhering to predesigned or offline-learned routines, alleviates the need for specialized algorithms or training for each problem instance. Monte Carlo tree search is a powerful planning algorithm that strategically explores simulated future possibilities, but it requires a discrete problem representation that is irreconcilable with the continuous dynamics of the physical world. We present Spectral Expansion Tree Search (SETS), a real-time, tree-based planner that uses the spectrum of the locally linearized system to construct a low-complexity and approximately equivalent discrete representation of the continuous world. We prove that SETS converges to a bound of the globally optimal solution for continuous, deterministic, and differentiable Markov decision processes, a broad class of problems that includes underactuated nonlinear dynamics, nonconvex reward functions, and unstructured environments. We experimentally validated SETS on drone, spacecraft, and ground vehicle robots and one numerical experiment, each of which is not directly solvable with existing methods.

## Introduction

Endowing robots with high-performing and reliable autonomous decision-making is the ultimate goal of robotics research and will enable applications such as sea, air, and space autonomous exploration, self-driving cars, and urban air mobility. These autonomous robots need to make decisions encompassing low-level physical movements (i.e., motion planning) and high-level strategy such as selecting goals, sequencing actions, and optimizing other decision variables.

This vision of robotic autonomy remains elusive because solving the decision-making problem exactly in high-dimensional continuous-space systems has "the curse of dimensionality". In light of this complexity, many autonomous robots in deployment avoid a general problem formulation and instead exploit particular problem structure for computational benefits. For example, motion planning can be solved with sampling-based methods, trajectory optimization can be solved with convex optimization, and high-level discrete decision-making can be solved with value iteration.

In this work, we present Spectral Expansion Tree Search (SETS), a real-time and continuous-space planning algorithm that converges to globally optimal solutions. The new capability of SETS is enabled by efficiently representing continuous space with the system's natural motions, a concept formalized through the spectrum of the locally linearized controllability Gramian. Without further assumptions on the dynamics or reward, the transformed low-complexity form is solved with Monte Carlo Tree Search (MCTS). The SETS tree is visualized in Fig A.

We use this last experiment as a case study to empirically validate the theoretical result, compare our method to state-of-the-art baselines, and tune parameters in a systematic and informed procedure.

## Discussion

We present a qualitative comparison with existing approaches and discuss how our work can impact the field of robotics.
