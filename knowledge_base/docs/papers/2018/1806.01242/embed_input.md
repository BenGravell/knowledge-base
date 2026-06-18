Graph Networks as Learnable Physics Engines for Inference and Control

Understanding and interacting with everyday physical scenes requires rich knowledge about the structure of the world, represented either implicitly in a value or policy function, or explicitly in a transition model. Here we introduce a new class of learnable models - based on graph networks - which implement an inductive bias for object- and relation-centric representations of complex, dynamical systems. Our results show that as a forward model, our approach supports accurate predictions from real and simulated data, and surprisingly strong and efficient generalization, across eight distinct physical systems which we varied parametrically and structurally. We also found that our inference model can perform system identification. Our models are also differentiable, and support online planning via gradient-based trajectory optimization, as well as offline policy optimization. Our framework offers new opportunities for harnessing and exploiting rich knowledge about the world, and takes a key step toward building machines with more human-like representations of the world.

## Introduction

Figure 1: (Top) Our experimental physical systems. (Bottom) Samples of parametrized versions of these systems (see videos: link).

Many domains, such as mathematics, language, and physical systems, are combinatorially complex. The possibilities scale rapidly with the number of elements. For example, a multi-link chain can assume shapes that are exponential in the number of angles each link can take, and a box full of bouncing balls yields trajectories which are exponential in the number of bounces that occur. How can an intelligent agent understand and control such complex systems?

Some key future directions include using our approach for control in real-world settings, supporting simulation-to-real transfer via pre-training models in simulation, extending our models to handle stochastic environments, and performing system identification over the structure of the system as well as the parameters. Our approach may also be useful within imagination-based planning frameworks, as well as integrated architectures with GN-like policies.

This work takes a key step towards realizing the promise of model-based methods by exploiting compositional representations within a powerful statistical learning framework, and opens new paths for robust, efficient, and general-purpose patterns of reasoning and decision-making.

### Prediction performance evaluation

For control, we exploit the fact that the GN is differentiable to use our learned forward and inference models for model-based planning within a classic, gradient-based trajectory optimization regime, also known as model-predictive control (MPC). We also develop an agent which simultaneously learns a GN-based model and policy function via Stochastic Value Gradients (SVG). ^66^6MPC and SVG are deeply connected: in MPC the control inputs are optimized given the initial conditions in a single episode, while in SVG a policy function that maps states to controls is optimized over states experienced during training.

Figure 7: Real and predicted test trajectories of a JACO robot arm. The recurrent model tracks the ground truth (a) orientations and (b) angular velocities closely. (c) The total 100-step rollout error was much better for the recurrent model, though the feed-forward model was still well below the constant prediction baseline....
