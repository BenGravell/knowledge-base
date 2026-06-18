Planning with Learned Dynamics: Probabilistic Guarantees on Safety and Reachability via Lipschitz Constants

Topics include Learned dynamics, Feedback motion planning, Safety guarantees, Reachability, Lipschitz constants, Sampling-based planning.

Plans with learned control-affine dynamics while bounding model error through estimated Lipschitz constants and feedback-law existence constraints. The result is a sampling-based planner that returns nominal plans with probabilistic safety, reachability, and local goal-stability guarantees under the learned-model trust region.

We present a method for feedback motion planning of systems with unknown dynamics which provides probabilistic guarantees on safety, reachability, and goal stability. To find a domain in which a learned control-affine approximation of the true dynamics can be trusted, we estimate the Lipschitz constant of the difference between the true and learned dynamics, and ensure the estimate is valid with a given probability. Provided the system has at least as many controls as states, we also derive existence conditions for a one-step feedback law which can keep the real system within a small bound of a nominal trajectory planned with the learned dynamics. Our method imposes the feedback law existence as a constraint in a sampling-based planner, which returns a feedback policy around a nominal plan ensuring that, if the Lipschitz constant estimate is valid, the true system is safe during plan execution, reaches the goal, and is ultimately invariant in a small set about the goal. We demonstrate our approach by planning using learned models of a 6D quadrotor and a 7DOF Kuka arm.

## INTRODUCTION

Planning and control with guarantees on safety and reachability for systems with unknown dynamics has long been sought-after in the robotics and control community. Model-based optimal control can achieve this if the dynamics are precisely modeled, but modeling assumptions inevitably break down when applied to real physical systems due to unmodeled effects from friction, slip, flexing, etc. To account for this gap, data-driven machine learning methods and robust control seek to sidestep the need to precisely model the dynamics a priori.

To address this gap, we propose a method for planning with learned dynamics which yields probabilistic guarantees on safety, reachability, and goal invariance in execution on the true system. Our core insight is that we can determine where a learned model can be trusted for planning using the Lipschitz constant of the error (the difference between the true and learned dynamics), which also informs how well the training data covers the task-relevant domain. Under the assumption of deterministic true dynamics, we can plan trajectories in this trusted domain with strong safety guarantees for an important class of learned dynamical systems.

Specifically, with a Lipschitz constant, we can bound the difference in dynamics between a novel point (that our model was not trained on) and a training point. Since the bound grows with the distance to training points, we can naturally define a domain where the model can be trusted as the set of points within a certain distance to training points. Conversely, to obtain a small bound over a desired domain, it is necessary to have good training data coverage in the task-relevant domain.

## DISCUSSION AND CONCLUSION

We present a method to bound the difference between learned and true dynamics in a given domain and derive conditions that guarantee a one-step feedback law exists. We combine these two properties to design a planner that can guarantee safety, goal reachability, and that the closed-loop system remains in a small region about the goal.
