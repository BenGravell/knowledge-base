NuPlan: A Closed-loop ML-based Planning Benchmark for Autonomous Vehicles

Topics include Autonomous driving, Vehicles, Datasets, Benchmarks, Planning, nuPlan, Motion planning, Las vegas.

In this work, we propose the world's first closed-loop ML-based planning benchmark for autonomous driving. While there is a growing body of ML-based motion planners, the lack of established datasets and metrics has limited the progress in this area. Existing benchmarks for autonomous vehicle motion prediction have focused on short-term motion forecasting, rather than long-term planning. This has led previous works to use open-loop evaluation with L2-based metrics, which are not suitable for fairly evaluating long-term planning. Our benchmark overcomes these limitations by introducing a large-scale driving dataset, lightweight closed-loop simulator, and motion-planning-specific metrics. We provide a high-quality dataset with 1500h of human driving data from 4 cities across the US and Asia with widely varying traffic patterns (Boston, Pittsburgh, Las Vegas and Singapore). We will provide a closed-loop simulation framework with reactive agents and provide a large set of both general and scenario-specific planning metrics. We plan to release the dataset at NeurIPS 2021 and organize benchmark challenges starting in early 2022.

## Introduction

Large-scale human labeled datasets in combination with deep Convolutional Neural Networks have led to an impressive performance increase in autonomous vehicle (AV) perception over the last few years. In contrast, existing solutions for AV planning are still primarily based on carefully engineered expert systems, that require significant amounts of engineering to adapt to new geographies and do not scale with more training data. We believe that providing suitable data and metrics will enable ML-based planning and pave the way towards a full "Software 2.0" stack.

Existing real-world benchmarks are focused on short-term motion forecasting, also known as prediction, rather than planning. This is evident in the lack of high-level goals, the choice of metrics, and the open-loop evaluation. Prediction focuses on the behavior of other agents, while planning relates to the ego vehicle behavior. Prediction is typically multi-modal, which means that for each agent we predict the $N$ most likely trajectories. In contrast, planning is typically uni-modal (except for contingency planning) and we predict a single trajectory.

We instead provide a planning benchmark to address these shortcomings.

The largest existing public real-world dataset for autonomous driving with high quality autolabeled tracks from 4 cities.

## Conclusion

In this work we proposed the first ML-based planning benchmark for AVs. Contrary to existing forecasting benchmarks, we focus on goal-based planning, planning metrics and closed-loop evaluation. We hope that by providing a common benchmark, we will pave a path towards progress in ML-based planning, which is one of the final frontiers in autonomous driving.
