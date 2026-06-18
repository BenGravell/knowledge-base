QuAD: Query-based Interpretable Neural Motion Planning for Autonomous Driving

A self-driving vehicle must understand its environment to determine the appropriate action. Traditional autonomy systems rely on object detection to find the agents in the scene. However, object detection assumes a discrete set of objects and loses information about uncertainty, so any errors compound when predicting the future behavior of those agents. Alternatively, dense occupancy grid maps have been utilized to understand free-space. However, predicting a grid for the entire scene is wasteful since only certain spatio-temporal regions are reachable and relevant to the self-driving vehicle. We present a unified, interpretable, and efficient autonomy framework that moves away from cascading modules that first perceive, then predict, and finally plan. Instead, we shift the paradigm to have the planner query occupancy at relevant spatio-temporal points, restricting the computation to those regions of interest. Exploiting this representation, we evaluate candidate trajectories around key factors such as collision avoidance, comfort, and progress for safety and interpretability....

## Introduction

Self-driving vehicles (SDVs) strive to reach their destinations safely and comfortably by analyzing their surroundings, envisioning potential future scenarios, and using this information to determine a plan of action to carry out. This is repeated with every new observation.

The majority of autonomy frameworks are object-based, which implies detecting a discrete set of objects, typically obtained by thresholding output confidence scores from an object detector, predicting a small set of hypothetical future trajectories, and finally planning a safe trajectory. However, this approach loses information about the scene from thresholding and has limited representation of future object uncertainty. Furthermore, the expressivity of the future trajectory forecasts is limited, as keeping the number of hypotheses low is crucial for real-time inference.

## Conclusion

In this paper, we have proposed an interpretable motion planner leveraging spatio-temporal occupancy queries to effectively understand the current and future free-space from sensor data. We showcased our proposed autonomy can drive more safely and progress further than contemporary object-based, sensor-to-plan and occupancy-based autonomy models. Our framework also achieves faster runtime than its closest competitors.

### Occupancy

### Point Quantization

### Canonical driving set

Alternatively, sensor-to-plan imitation learning frameworks avoid reasoning about individual objects by learning to map sensor data directly to plans. These learned policies are typically brittle to distributional shift since supervision is only provided in states visited by the expert during training, so the policy never learns to recover from its own mistakes \[\]. Moreover, the decisions are not easy to interpret or explain, which is important for system validation and verification.

To tackle these limitations, occupancy-based approaches have proposed a more interpretable object-free paradigm. Occupancy describes the probability a point in space and time is occupied by any traffic participant. This enables planners to decide on consistent and effective actions with respect to this interpretable representation, serving as an explanation of their decision....
