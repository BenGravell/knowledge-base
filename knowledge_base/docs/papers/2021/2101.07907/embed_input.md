IntentNet: Learning to Predict Intention from Raw Sensor Data

In order to plan a safe maneuver, self-driving vehicles need to understand the intent of other traffic participants. We define intent as a combination of discrete high-level behaviors as well as continuous trajectories describing future motion. In this paper, we develop a one-stage detector and forecaster that exploits both 3D point clouds produced by a LiDAR sensor as well as dynamic maps of the environment. Our multi-task model achieves better accuracy than the respective separate modules while saving computation, which is critical to reducing reaction time in self-driving applications.

## Introduction

Autonomous driving is one of the most exciting problems of modern artificial intelligence. Self-driving vehicles have the potential to revolutionize the way people and freight move. While a plethora of systems have been built in the past few decades, many challenges still remain. One of the fundamental difficulties is that self driving vehicles have to share the roads with human drivers, which can perform maneuvers that are difficult to predict.

Human drivers understand intention by exploiting the actors' past motion as well as prior knowledge about the scene (e.g. the location of lanes, direction of driving). Previous work attempted to solve this problem by first performing vehicle detection and then extracting intent from the position and motion of detected bounding boxes. This, however, restricts the information that the intent estimation module has access to, resulting in suboptimal estimates. Very recently, FaF directly exploited LiDAR sensor data to predict the future trajectories of vehicles....

## Conclusion

In this paper we introduce IntentNet, a learnable end-to-end model that is able to tackle the tasks of detection and intent prediction of vehicles in the context of self-driving cars. By exploiting 3D point clouds produced by a LiDAR sensor and prior knowledge of the scene coming from an HD map, we are able to achieve higher performance than previous work across all tasks, with a single neural network. In the future, we plan to investigate how more sophisticated algorithms can model the statistical dependencies between discrete and continuous intention. We also plan to extend our approach to handle pedestrians and bicyclists.

Our model is fully differentiable and thus can be trained end-to-end through back-propagation. In particular, we minimize a multi-task loss containing a regression term for the trajectory prediction over $T$ time steps, a binary classification term for the detection (background vs vehicle) and a multi-class classification for discrete intention. Thus

Our model predicts drivers' intentions in both discrete and continuous form.

### Inference

In this paper, we take this approach one step further and propose a novel deep neural network that reasons about both high level behavior and long term trajectories....
