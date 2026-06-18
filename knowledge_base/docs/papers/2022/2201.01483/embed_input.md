Risk Bounded Nonlinear Robot Motion Planning with Integrated Perception & Control

Topics include Model predictive control, Predictive control, Motion planning, Robotics, Robustness, Kalman filtering, Online algorithms, Planning, Control, Kalman filter.

Robust autonomy stacks require tight integration of perception, motion planning, and control layers, but these layers often inadequately incorporate inherent perception and prediction uncertainties, either ignoring them altogether or making questionable assumptions of Gaussianity. Robots with nonlinear dynamics and complex sensing modalities operating in an uncertain environment demand more careful consideration of how uncertainties propagate across stack layers. We propose a framework to integrate perception, motion planning, and control by explicitly incorporating perception and prediction uncertainties into planning so that risks of constraint violation can be mitigated. Specifically, we use a nonlinear model predictive control based steering law coupled with a decorrelation scheme based Unscented Kalman Filter for state and environment estimation to propagate the robot state and environment uncertainties. Subsequently, we use distributionally robust risk constraints to limit the risk in the presence of these uncertainties.

## Introduction

Safety is a critical issue for robotic and autonomous systems that must traverse through uncertain environments. More sophisticated motion planning and control algorithms are needed as environments become increasingly dynamic and uncertain to ensure safe and effective autonomous behavior. Safely deploying robots in such dynamic environments requires a systematic accounting of various risks both within and across layers in an autonomy stack from perception to motion planning and control. Many widely used motion planning algorithms have been developed in deterministic settings.

Traditionally, the perception and planning components in a robot autonomy stack are loosely coupled in the sense that nominal estimates from the perception system may be used for planning, while inherent perception uncertainties are usually ignored. This paradigm is inherited, in part, from the classical separation of estimation and control in linear systems theory.

This manuscript is a significant extension of our previous works. In this paper, we relax the assumptions from our previous works by considering both motion model and sensor models to be nonlinear with additive uncertainties and propose an unified framework aimed toward a tighter integration of perception and planning in autonomous robotic systems.

We propose a distributionally robust incremental sampling-based motion planning framework that explicitly and coherently incorporates perception and prediction uncertainties. Our solution approach called Nonlinear Risk Bounded $\text{RRT}^{\star}$ $(\text{NRB-RRT}^{\star})$ (Algorithm 1), approximates asymptotically optimal risk-bounded trajectories.

## Discussion of Results

The motion plan using $\text{NRB-RRT}^{\star}$ algorithm was generated on a machine with an Intel Core i7 CPU and 8GB of RAM. The trajectory tracking Monte Carlo simulations were performed on a machine with a Ryzen 7 2700X and 64GB of RAM. The nonlinear MPC problem in (43 Law ‣ 4 Output Feedback Based Steering Law: Unscented Kalman Filter with Nonlinear Model Predictive Controller ‣ Risk Bounded Nonlinear Robot Motion Planning With Integrated Perception & Control")) is modeled with CasADi Opti and solved with IPOPT solver. We demonstrate $\text{NRB-RRT}^{\star}$ in a obstacle cluttered environment as shown in Figure 5.

## of
## of
