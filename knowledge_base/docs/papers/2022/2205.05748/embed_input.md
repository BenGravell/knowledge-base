Tiny Robot Learning: Challenges and Directions for Machine Learning in Resource-Constrained Robots

Machine learning (ML) has become a pervasive tool across computing systems. An emerging application that stress-tests the challenges of ML system design is tiny robot learning, the deployment of ML on resource-constrained low-cost autonomous robots. Tiny robot learning lies at the intersection of embedded systems, robotics, and ML, compounding the challenges of these domains. Tiny robot learning is subject to challenges from size, weight, area, and power (SWAP) constraints; sensor, actuator, and compute hardware limitations; end-to-end system tradeoffs; and a large diversity of possible deployment scenarios. Tiny robot learning requires ML models to be designed with these challenges in mind, providing a crucible that reveals the necessity of holistic ML system design and automated end-to-end design tools for agile development. This paper gives a brief survey of the tiny robot learning space, elaborates on key challenges, and proposes promising opportunities for future work in ML system design.

## Introduction

Machine learning (ML) has become a pervasive technology, and as it spreads beyond traditional computing platforms (e.g., servers and desktops) towards devices on the edge (e.g., mobile, embedded, IoT, AR/VR, robotics, and other cyber-physical systems), new design pressures and constraints arise that fundamentally impact the ML system design process.

An emerging application that stress-tests the challenges of designing ML for edge devices is *tiny robot learning*, the deployment of ML on resource-constrained low-cost autonomous robots. These robots are lightweight (e.g., less than a pound, or under $\sim 500$g) and can operate in small spaces, making them a promising solution for applications ranging from emergency search and rescue, to routine monitoring and maintenance of infrastructure and equipment.

## Conclusion

In this work, we examined tiny robot learning: the deployment of ML on resource-constrained low-cost autonomous robots. Lying at the intersection of embedded systems, robotics, and ML, tiny robot learning is subject to challenges from size, weight, area, and power constraints; sensor, actuator, and compute hardware limitations; end-to-end system tradeoffs; and a large diversity of possible deployment scenarios. As such, it reveals promising opportunities for future work developing holistic ML system design techniques and automated end-to-end design tools for agile development.

### III-A SWAP-Constrained ML Compute for Robotics Applications

While the same general challenges arise from ML design for a variety of different types of robots (e.g., quadrotor drones, satellites, quadrupeds, cars, submersibles), some design considerations differ between these platforms. For example, when comparing quadrotors to quadrupeds, weight is a more extreme constraint for quadrotors, while quadrupeds require more computationally expensive motion planning and control algorithms due to their increased degrees of freedom.

### III-B Sensor and Actuator Limitations in Tiny Robot Platforms

Tiny robot learning dials up the challenges of edge device ML, maximizing opportunities to refine edge ML system design by putting it through the crucible of the combined challenges of tiny (i.e., embedded) systems, robotics, and machine learning, all in one system deployment (Fig. 1)....
