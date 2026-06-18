QuAD: Query-based Interpretable Neural Motion Planning for Autonomous Driving

A self-driving vehicle must understand its environment to determine the appropriate action. Traditional autonomy systems rely on object detection to find the agents in the scene. However, object detection assumes a discrete set of objects and loses information about uncertainty, so any errors compound when predicting the future behavior of those agents. Alternatively, dense occupancy grid maps have been utilized to understand free-space. However, predicting a grid for the entire scene is wasteful since only certain spatio-temporal regions are reachable and relevant to the self-driving vehicle. We present a unified, interpretable, and efficient autonomy framework that moves away from cascading modules that first perceive, then predict, and finally plan. Instead, we shift the paradigm to have the planner query occupancy at relevant spatio-temporal points, restricting the computation to those regions of interest. Exploiting this representation, we evaluate candidate trajectories around key factors such as collision avoidance, comfort, and progress for safety and interpretability.

## Introduction

Self-driving vehicles (SDVs) strive to reach their destinations safely and comfortably by analyzing their surroundings, envisioning potential future scenarios, and using this information to determine a plan of action to carry out. This is repeated with every new observation.

The majority of autonomy frameworks are object-based, which implies detecting a discrete set of objects, typically obtained by thresholding output confidence scores from an object detector, predicting a small set of hypothetical future trajectories, and finally planning a safe trajectory. However, this approach loses information about the scene from thresholding and has limited representation of future object uncertainty. Furthermore, the expressivity of the future trajectory forecasts is limited, as keeping the number of hypotheses low is crucial for real-time inference.

We propose QuAD, an interpretable, effective and efficient neural motion planner. QuAD diverges from prior works that first perceive, then predict, and finally plan. Instead, our unified autonomy first generates candidate trajectories respecting kinematic constraints and traffic rules, and then queries an implicit occupancy model only at spatio-temporal points needed for planning, which is used to rank the safety of the candidates. Fig. shows an example of the candidate trajectories, which we can see only occupy a small portion of the spatio-temporal volume prior works predict.

Through extensive evaluation we show that QuAD is able to achieve better closed loop performance in a state-of-the-art highway driving simulator while attaining better runtime than competitive baselines.

## Conclusion

In this paper, we have proposed an interpretable motion planner leveraging spatio-temporal occupancy queries to effectively understand the current and future free-space from sensor data. We showcased our proposed autonomy can drive more safely and progress further than contemporary object-based, sensor-to-plan and occupancy-based autonomy models. Our framework also achieves faster runtime than its closest competitors.
