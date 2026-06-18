Prediction Horizon Requirements for Automated Driving: Optimizing Safety, Comfort, and Efficiency

Topics include Motion prediction, Prediction horizon, Automated driving, Safety, Comfort, Efficiency.

Analyzes how the required prediction horizon for autonomous driving depends on the competing objectives of safety, comfort, and efficiency, providing a framework for selecting appropriate prediction horizons for different driving scenarios and speed profiles.

Predicting the movement of other road users is beneficial for improving automated vehicle (AV) performance. However, the relationship between the time horizon associated with these predictions and AV performance remains unclear. Despite the existence of numerous trajectory prediction algorithms, no studies have been conducted on how varying prediction lengths affect AV safety and other vehicle performance metrics, resulting in undefined horizon requirements for prediction methods. Our study addresses this gap by examining the effects of different prediction horizons on AV performance, focusing on safety, comfort, and efficiency. Through multiple experiments using a state-of-the-art, risk-based predictive trajectory planner, we simulated predictions with horizons up to 20 seconds. Based on our simulations, we propose a framework for specifying the minimum required and optimal prediction horizons based on specific AV performance criteria and application needs. Our results indicate that a horizon of 1.6 seconds is required to prevent collisions with crossing pedestrians, horizons of 7-8 seconds yield the best efficiency, and horizons up to 15 seconds improve passenger comfort.

## Introduction

Automated vehicles (AVs) are becoming increasingly prevalent, and trajectory prediction of surrounding road users (RUs) is a critical component of these systems, since the AV's decisions will be largely based on the predicted motion of other RUs. When designing a system that accounts for the future motion of surrounding RUs, one must decide how much into the future to predict, i.e. the prediction horizon, which is used to plan an AV trajectory for the same horizon.

The requirements that predictions must satisfy will be dependent on several other factors, like the type of object being predicted (e.g. vehicle vs. pedestrian), the specific scenario (e.g. lane change in a highway vs a crossing pedestrian), or even user preferences (e.g. a smoother ride is preferred over lower travel time). Hence, these requirements are application-dependent and should adapt to each situation.

To specify prediction requirements, this work first investigates the impact that different prediction horizons have on the safety, comfort and efficiency of an AV. We do this by simulating and integrating predictions into a state of the art optimization-based planner that considers the predicted actions of other RUs. Additionally, we introduce a framework to establish both the minimum required and optimal prediction horizons for achieving targeted vehicle performance in specific applications.

A methodology to derive application-specific requirements: We introduce a versatile framework to determine prediction horizon requirements tailored to specific AV applications and performance goals. While we demonstrate its application in a limited set of scenarios and performance criteria, the framework is adaptable to other scenarios and criteria.

## Conclusion

Predicting the future movements of surrounding road users is essential for enhancing the performance of an automated vehicle (AV). However, the degree to which these predictions influence the AV's behavior is unknown.

In this study, we explore how various prediction horizons impact the behavior of an AV in terms of safety, comfort, and efficiency. We simulate trajectory predictions in crossing pedestrian scenarios and test different horizons of to 20 seconds, which are integrated into a state-of-the-art trajectory planner that considers the future motion of other road users.
