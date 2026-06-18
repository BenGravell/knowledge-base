Perceive, Predict, and Plan: Safe Motion Planning through Interpretable Semantic Representations

In this paper we propose a novel end-to-end learnable network that performs joint perception, prediction and motion planning for self-driving vehicles and produces interpretable intermediate representations. Unlike existing neural motion planners, our motion planning costs are consistent with our perception and prediction estimates. This is achieved by a novel differentiable semantic occupancy representation that is explicitly used as cost by the motion planning process. Our network is learned end-to-end from human demonstrations. The experiments in a large-scale manual-driving dataset and closed-loop simulation show that the proposed model significantly outperforms state-of-the-art planners in imitating the human behaviors while producing much safer trajectories.

## Introduction

The goal of an autonomy system is to take the output of the sensors, a map, and a high-level route, and produce a safe and comfortable ride. Meanwhile, producing interpretable intermediate representations that can explain why the vehicle performed a certain maneuver is very important in safety critical applications such as self-driving, particularly if a bad event was to happen. Traditional autonomy stacks produce interpretable representations through the perception and prediction modules in the form of bounding boxes as well as distributions over their future motion....

First attempts to perform end-to-end neural motion planning did not produce interpretable representations, and instead focused on producing accurate control outputs that mimic how humans drive. Recent approaches, have tried to incorporate interpretability. The neural motion planner of shared feature representations between perception, prediction and motion planning. However it can produce inconsistent estimates between the modules, as it is framed as a multi-task learning problem with separate headers between the tasks. As a consequence, the motion planner might ignore detections or motion forecasts, resulting in unsafe behaviors.

## Conclusion

In this paper, we have proposed an end-to-end perception, prediction and motion planning model that generates safe trajectories for the SDV from raw sensor data. Importantly, our model not only produces interpretable intermediate representations, but also the generated ego-vehicle trajectories are consistent with the perception and prediction outputs. Furthermore, unlike most previous approaches that employ thresholded activations in detection and trajectory prediction of objects, we use semantic occupancy layers that are able to carry information about low probability objects to the motion planning module....

Given the occupancy predictions $\mathbf{o}$ and the input data $\mathbf{x}$ in the form of the HD-map, the high level route, traffic-lights states, and the kinematic state of the SDV, we perform motion planning by sampling a diverse set of trajectories for the ego-car and pick the one that minimizes a learned cost function as follows:

Figure 2: Semantic classes in our occupancy forecasting. Colors match between drawing and hierarchy. Shadowed area corresponds to the SDV route....
