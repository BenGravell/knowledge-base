Dynamic Risk-Aware MPPI for Mobile Robots in Crowds via Efficient Monte Carlo Approximations

Topics include Model predictive control, Predictive control, Robotics, Safety, Uncertainty, Real-time systems, Control, Monte Carlo methods, Distributionally robust model predictive path integral control, Scenario-based, S-MPC, Mobile robots.

Deploying mobile robots safely among humans requires the motion planner to account for the uncertainty in the other agents' predicted trajectories. This remains challenging in traditional approaches, especially with arbitrarily shaped predictions and real-time constraints. To address these challenges, we propose a Dynamic Risk-Aware Model Predictive Path Integral control (DRA-MPPI), a motion planner that incorporates uncertain future motions modelled with potentially non-Gaussian stochastic predictions. By leveraging MPPI's gradient-free nature, we propose a method that efficiently approximates the joint Collision Probability (CP) among multiple dynamic obstacles for several hundred sampled trajectories in real-time via a Monte Carlo (MC) approach. This enables the rejection of samples exceeding a predefined CP threshold or the integration of CP as a weighted objective within the navigation cost function. Consequently, DRA-MPPI mitigates the freezing robot problem while enhancing safety.

## Introduction

Mobile robots have the potential to enhance various aspects of daily life, from optimizing logistics in warehouses to enabling safer and more efficient transportation through autonomous vehicles. However, for robots to be successfully integrated into real-world settings like urban areas, they must be capable of safely and efficiently manoeuvring through human-populated spaces. Achieving this requires an ability to interpret and anticipate human movement---a task complicated by the inherent unpredictability of human behaviour. Prediction models, such as, provide probabilistic distributions over potential human trajectories.

A key challenge in planning under uncertainty is finding a safe trajectory despite the stochastic nature of surrounding obstacles. One approach to handle uncertainty in dynamic environments is robust optimization, which enforces safety guarantees by considering worst-case scenarios within bounded uncertainty sets. This method assumes that the probability density of uncertainty is nonzero within a defined region of the ego agent's workspace, ensuring strict safety constraints.

## II-A Contributions

Our

DRA-MPPI: An MPPI-based planner that approximates the CPs of trajectories using MC methods. It handles joint CPs over several dynamic obstacles and manages non-Gaussian predictions with minimal approximations.
