Motion Forecasting for Autonomous Vehicles: A Survey

Topics include Motion forecasting, Autonomous vehicles, Survey, Trajectory prediction.

Comprehensive survey of motion forecasting methods for autonomous vehicles, covering classical physics-based approaches through modern deep learning methods, with discussion of datasets, metrics, and open problems.

In recent years, the field of autonomous driving has attracted increasingly significant public interest. Accurately forecasting the future behavior of various traffic participants is essential for the decision-making of Autonomous Vehicles (AVs). In this paper, we focus on both scenario-based and perception-based motion forecasting for AVs. We propose a formal problem formulation for motion forecasting and summarize the main challenges confronting this area of research. We also detail representative datasets and evaluation metrics pertinent to this field. Furthermore, this study classifies recent research into two main categories: supervised learning and self-supervised learning, reflecting the evolving paradigms in both scenario-based and perception-based motion forecasting. In the context of supervised learning, we thoroughly examine and analyze each key element of the methodology. For self-supervised learning, we summarize commonly adopted techniques. The paper concludes and discusses potential research directions, aiming to propel progress in this vital area of AV technology.

## Introduction

Motion Forecasting is vital in the functionality of autonomous driving systems. It assists these vehicles in planning their forthcoming actions and mitigates the risk of accidents. This survey addresses motion forecasting in autonomous vehicles, focusing on the two main approaches: Scenario-based Motion Forecasting and Perception-based Motion Forecasting.

Scenario-based Motion Forecasting predicts future states of traffic agents (TAs) by analyzing past states and relevant environmental context, such as high-definition maps (HDMaps) and the historical states of surrounding agents (SAs). This approach emphasizes structured, predefined inputs like agents' locations and HDMaps, intentionally excluding raw sensor data like RGB images, LiDAR point clouds, or semantic segmentation maps. By limiting input features to these structured elements, scenario-based forecasting models achieve a focused analysis of the traffic environment and agent interactions.

## Conclusion and Prospect

In this paper, we present a comprehensive review of the recent advancements in motion forecasting for autonomous vehicles. We begin by introducing the formulation of motion forecasting and then move on to an overview of diverse, widely-utilized datasets. This is followed by a detailed explanation of evaluation metrics specifically designed for motion forecasting. State-of-the-art prediction models have made significant strides, employing advanced techniques such as attention mechanisms, GNNs, transformers, and self-supervised architectures. Despite these technological advances, the field still faces substantial challenges.

Fusion of more prior information. Recent research has integrated HDMaps into motion forecasting models. This integration specifically involves incorporating lane information to ensure predicted trajectories are aligned with the road topology. In real-world scenarios, other factors also play a crucial role. These include traffic light status, various traffic signs, and additional elements that influence the movement and interactions of traffic participants. However, many current methodologies tend to overlook these aspects. This oversight results in limitations in the mechanistic understanding of motion forecasting models.
