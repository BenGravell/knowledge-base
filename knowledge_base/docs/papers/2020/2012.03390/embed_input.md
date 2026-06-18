On Infusing Reachability-Based Safety Assurance within Planning Frameworks for Human-Robot Vehicle Interactions

Topics include Model predictive control, Predictive control, Robotics, Autonomous driving, Vehicles, Safety, Uncertainty, Real-time systems, Planning, Control.

Action anticipation, intent prediction, and proactive behavior are all desirable characteristics for autonomous driving policies in interactive scenarios. Paramount, however, is ensuring safety on the road - a key challenge in doing so is accounting for uncertainty in human driver actions without unduly impacting planner performance. This paper introduces a minimally-interventional safety controller operating within an autonomous vehicle control stack with the role of ensuring collision-free interaction with an externally controlled (e.g., human-driven) counterpart while respecting static obstacles such as a road boundary wall. We leverage reachability analysis to construct a real-time (100Hz) controller that serves the dual role of (i) tracking an input trajectory from a higher-level planning algorithm using model predictive control, and (ii) assuring safety by maintaining the availability of a collision-free escape maneuver as a persistent constraint regardless of whatever future actions the other car takes.

## Introduction

Decision-making and control for mobile robots is typically stratified into levels. A high-level planner, informed by representative yet simplified dynamics of a robot and its environment, might be responsible for selecting an optimal, yet coarse trajectory plan, which is then implemented through a low-level controller that respects more accurate models of the robot's dynamics and control constraints. While additional components may be required to flesh out a robot's full control stack from model to motor commands, selecting the right "division of responsibilities" is fundamental to system design.

One consideration that defies clear classification, however, is how to ensure a mobile robot's safety when operating in close proximity with a rapidly evolving and stochastic environment. Safety is a function of uncertainty in both the robot's dynamics and those of its surroundings; high-level planners typically do not replan sufficiently rapidly to ensure split-second reactivity to threats, yet low-level controllers are typically too short-sighted to ensure safety beyond their local horizon.

Human-robot interactions are an unavoidable aspect of many modern robotic applications and ensuring safety for these interactions is critical, especially in applications such as autonomous driving where collisions may lead to life-threatening injury. However, ensuring safety within the planning and control framework can be very challenging due to the uncertainty in how humans may behave. To quantify this uncertainty, robots often rely on generative models of human behavior in order to inform their planning algorithms, thereby enabling more efficient and communicative interactions.

## Discussion

Beyond the qualitative and quantitative confirmation of our design goals, our experimental results reveal three main insights.

*Takeaway 1: The reachability cache is underly-conservative with respect to robot car dynamics and overly-conservative with respect to human car dynamics.*
