Actor-Critic Model Predictive Control: Differentiable Optimization Meets Reinforcement Learning for Agile Flight

Topics include Reinforcement learning, Model predictive control, Predictive control, Aerial robotics, Robustness, Real-time systems, Online algorithms, Out-of-distribution generalization, Optimization, Planning, Control, Learning, Actor-critic model predictive control.

A key open challenge in agile quadrotor flight is how to combine the flexibility and task-level generality of model-free reinforcement learning (RL) with the structure and online replanning capabilities of model predictive control (MPC), aiming to leverage their complementary strengths in dynamic and uncertain environments. This paper provides an answer by introducing a new framework called Actor-Critic Model Predictive Control. The key idea is to embed a differentiable MPC within an actor-critic RL framework. This integration allows for short-term predictive optimization of control actions through MPC, while leveraging RL for end-to-end learning and exploration over longer horizons. Through various ablation studies, conducted in the context of agile quadrotor racing, we expose the benefits of the proposed approach: it achieves better out-of-distribution behaviour, better robustness to changes in the quadrotor's dynamics and improved sample efficiency.

## Introduction

The animal brain's exceptional ability to quickly learn and adjust to complex behaviors is one of its most remarkable traits, which remains unattained by robotic systems. This has often been attributed to the brain's ability to make both immediate and long-term predictions about the consequences of its actions and plan accordingly. In robotics and control theory, model-based control has demonstrated a wide array of tasks with commendable reliability. In particular, Model Predictive Control (MPC) has achieved notable success across various domains such as the operation of industrial chemical plants, control of legged robots.

Model Predictive Value Expansion (MPVE). We introduce an extension to our framework that incorporates Model Predictive Value Expansion, a critic-training scheme that re-uses the short-horizon state-action predictions produced by the differentiable MPC during every forward pass. Unlike general value expansion methods that may require a separate policy for generating rollouts, our approach efficiently improves the critic without incurring additional policy call overhead.

Exploration analysis We show that after optimizing hyperparameters, specifically exploration, AC-MPC can leverage the prior knowledge included in the quadrotor dynamics to achieve better training performance than AC-MLP on the drone racing task.

Extended real-world validation. We demonstrate in both simulation and real-world experiments that the proposed AC-MPC achieves superhuman performance in the extremely challenging task of drone racing, attaining speeds of up to 21 m/s on a real quadrotor platform. These results are on par with state-of-the-art model-free reinforcement learning and highlight that the strengths of AC-MPC do not come at the expense of performance.

## Discussion and Conclusion

This work presented a new learning-based control framework that combines the advantages of differentiable model predictive control with actor-critic training. Furthermore, we showed that for quadrotor racing tasks, AC-MPC can leverage the prior knowledge embedded in the system dynamics to achieve better training performance when compared to the main PPO baseline (AC-MLP), to better cope with out-of-distribution scenarios, and its ability to deal with variations in the nominal dynamics, without any further re-training.
