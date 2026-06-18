Robust Distributed Planar Formation Control for Higher-Order Holonomic and Nonholonomic Agents

Topics include Multi-agent systems, Robotics, Aerial robotics, Robustness, Online algorithms, Distributed systems, Control, BCB.

We present a distributed formation control strategy for agents with a variety of dynamics to achieve a desired planar formation. Our approach is based on the barycentric-coordinate-based (BCB) control, which is fully distributed, does not require inter-agent communication or a common sense of orientation, and can be implemented using relative position measurements acquired by agents in their local coordinate frames. This removes the need for global positioning or alignment of local coordinate frames, which are required across several existing strategies. We show how the BCB control for agents with the simplest dynamical model, i.e., the single-integrator dynamics, can be extended to agents with higher-order dynamics such as quadrotors, and nonholonomic agents such as unicycles and cars. Specifically, our extension preserves the desired convergence and robustness guarantees of the BCB approach and is provably robust to saturations in the input and unmodeled linear actuator dynamics for unicycle and car agents....

## Introduction

Technological advances in recent years has made it increasingly possible to deploy a large fleet of agents to cooperatively map and monitor an environment, deliver goods, or manipulate objects. In these applications, the ability to bring the agents to a desired geometric shape is a fundamental building block upon which more sophisticated maneuvering and navigation policies are constructed. By assigning local control laws to individual agents, distributed formation control strategies ensure that a desired geometric shape emerge from the collective behavior of agents....

Figure 1: The proposed formation control strategy implemented on our distributed robotic platform to form the letters UTD.

We presented a distributed formation control strategy for a team of agents with a variety of dynamics to autonomously achieve a desired planar formation. Under the assumption that the sensing graph is undirected and universally rigid, we showed that formation control gains can be designed by solving a SDP problem. This design enjoys several robustness properties, such as robustness to positive scaling and rotation (up to $\pm 90^{\circ}$) of the control vector, saturations in the input, and switches in the sensing topology....

Future work includes investigating additional requirements, such as inter-agent communication, to guarantee that the collision avoidance algorithm can overcome gridlock scenarios. Moreover, inter-agent communication can be exploited in a distributed optimization scheme to solve the SDP problem in a decentralized way. Other possible research avenues include formation control of heterogeneous vehicles and time-varying formations.

### Remark 8

### Theorem 4

The main difference between the rear and front-wheel drive car is that when $\varphi_{i} = {\pm \frac{\pi}{2}}$, from $v_{i}^{r}$, and hence $v_{i}$, become zero. On the contrary, $v_{i}$ in a front-wheel drive car can take any desired value in this case (one can interpret this as the car pivoting about its rear wheels).

In this work, we present a unified, distributed control strategy for planar formations of agents with a variety of dynamics. In particular, we consider agents with linear or input-to-state linearizable dynamics, and further extend the results to agents with nonholonomic unicycle and car dynamics....
