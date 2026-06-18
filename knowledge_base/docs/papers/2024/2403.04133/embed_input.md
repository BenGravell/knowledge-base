Towards Learning-based Planning: The nuPlan Benchmark for Real-world Autonomous Driving

Topics include Autonomous driving, Vehicles, Safety, Datasets, Benchmarks, Planning, Learning, nuPlan, Machine learning.

Machine Learning (ML) has replaced traditional handcrafted methods for perception and prediction in autonomous vehicles. Yet for the equally important planning task, the adoption of ML-based techniques is slow. We present nuPlan, the world's first real-world autonomous driving dataset, and benchmark. The benchmark is designed to test the ability of ML-based planners to handle diverse driving situations and to make safe and efficient decisions. To that end, we introduce a new large-scale dataset that consists of 1282 hours of diverse driving scenarios from 4 cities (Las Vegas, Boston, Pittsburgh, and Singapore) and includes high-quality auto-labeled object tracks and traffic light data. We exhaustively mine and taxonomize common and rare driving scenarios which are used during evaluation to get fine-grained insights into the performance and characteristics of a planner. Beyond the dataset, we provide a simulation and evaluation framework that enables a planner's actions to be simulated in closed-loop to account for interactions with other traffic participants. We present a detailed analysis of numerous baselines and investigate gaps between ML-based and traditional methods.

## Introduction

In the last decade, autonomous vehicle perception and prediction have been revolutionized by deep learning-based methods trained on large-scale datasets. While similar attempts have been made in the field of learning-based or neural planning, these are not yet able to surpass their rule-based counterparts. One possible reason is the difficulty of generalizing driving scenarios when learned from a limited number of examples. Furthermore, driving scenarios typically follow a long-tail distribution, which further exacerbates the generalization issue.

We introduce the nuPlan dataset and simulation framework for autonomous vehicle planning. Our goal is to create a testbed for open-loop and closed-loop planning starting in real-world scenarios. This test bed is then used to compare traditional, learning-based, and hybrid planners. nuPlan enables numerous novel types of research, such as learning-based planning, the interplay between prediction and planning, and end-to-end planning using a large amount of published sensor data.

We release the largest dataset for autonomous driving to date, with a total of 1282h from 4 cities. We also publish an unprecedented 128h of sensor data.

We develop techniques to auto-label the dataset with accurate object tracks, traffic lights, and scenario labels.

## Conclusion

We presented nuPlan, the first real-world driving benchmark and the largest existing labeled autonomous driving dataset. The dataset consists of 1282 hours of diverse driving scenarios across 4 cities as well as an unprecedented 128 hours of raw sensor data and is accompanied by an evaluation framework powered by a closed-loop simulator; the dataset and the evaluation framework are publicly available. We investigated the state of current rule-based and learned-based planners by evaluating multiple approaches on the nuPlan dataset across challenging driving scenarios.
