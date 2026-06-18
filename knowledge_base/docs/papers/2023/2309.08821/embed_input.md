Distributionally Robust CVaR-Based Safety Filtering for Motion Planning in Uncertain Environments

Topics include Model predictive control, Predictive control, Motion planning, Robotics, Safety, Robustness, Deep learning, Optimization, Planning, Control, Learning, DRO, Conditional value at risk.

Safety is a core challenge of autonomous robot motion planning, especially in the presence of dynamic and uncertain obstacles. Many recent results use learning and deep learning-based motion planners and prediction modules to predict multiple possible obstacle trajectories and generate obstacle-aware ego robot plans. However, planners that ignore the inherent uncertainties in such predictions incur collision risks and lack formal safety guarantees. In this paper, we present a computationally efficient safety filtering solution to reduce the collision risk of ego robot motion plans using multiple samples of obstacle trajectory predictions. The proposed approach reformulates the collision avoidance problem by computing safe halfspaces based on obstacle sample trajectories using distributionally robust optimization (DRO) techniques. The safe halfspaces are used in a model predictive control (MPC)-like safety filter to apply corrections to the reference ego trajectory thereby promoting safer planning. The efficacy and computational efficiency of our approach are demonstrated through numerical simulations.

## Introduction

Autonomous robots have many application areas including autonomous driving, warehouse management and logistics, drone delivery, and agriculture. A core challenge facing autonomous robots is navigation in dynamic and uncertain environments, i.e. in the presence of moving obstacles whose future motion cannot be predicted exactly. This scenario complicates the robot safety requirements: the ego robot must presume the dynamic obstacles' intentions and predict their future trajectories for use in computing its own motion plan. Thus, safety hinges on how accurately the dynamic obstacles' behavior can be predicted....

Various methods have been studied for predicting how obstacles will behave, but it is still an active area of research. In, a hidden Markov model is used for better understanding urban scenarios for autonomous vehicles (AVs). In another work, uses a support vector machine and Bayesian filtering to predict lane change intentions for AVs. Furthermore, deep learning approaches have also been used. End-to-end motion planners, such as, implicitly account for future predictions, but they fail to explicitly capture the environment uncertainties which may lead to collisions....

## Conclusion

In this work we presented a solution that improves a robot's safety when operating in a dynamic environment with prediction uncertainties. We posed a DRO problem that computes ${DR} - {CVaR}$ safe halfspaces that bound the $CVaR$ of a signed collision distance under any distribution close the empirical one based on data. These halfspaces are then used as linear constraints in an MPC safety filter that corrects the ego reference trajectory. We performed a numerical analysis on the ${DR} - {CVaR}$ safe halfspaces and demonstrated that 1) they can be computed in milliseconds, and 2) they can improve safety in edge cases....

The optimization problem (5. ‣ II-C Collision Avoidance using DR-CVaR Safe Halfspaces ‣ II DR-CVaR Safe Motion Planning with Uncertain Dynamic Obstacles ‣ Distributionally Robust CVaR-Based Safety Filtering for Motion Planning in Uncertain Environments")) with the support $\Xi:={\{ p\mid{{Vp} \leq v}\}}$ for the random variable $\mathbf{p}$ admits the finite-dimensional reformulation:

where $z$ is any chosen unit vector per.
