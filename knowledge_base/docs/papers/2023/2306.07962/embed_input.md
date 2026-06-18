Parting with Misconceptions about Learning-based Vehicle Motion Planning

Topics include Motion planning, Vehicles, Graphs, Datasets, Planning, Learning.

The release of nuPlan marks a new era in vehicle motion planning research, offering the first large-scale real-world dataset and evaluation schemes requiring both precise short-term planning and long-horizon ego-forecasting. Existing systems struggle to simultaneously meet both requirements. Indeed, we find that these tasks are fundamentally misaligned and should be addressed independently. We further assess the current state of closed-loop planning in the field, revealing the limitations of learning-based methods in complex real-world scenarios and the value of simple rule-based priors such as centerline selection through lane graph search algorithms. More surprisingly, for the open-loop sub-task, we observe that the best results are achieved when using only this centerline as scene context (i.e., ignoring all information regarding the map and other agents). Combining these insights, we propose an extremely simple and efficient planner which outperforms an extensive set of competitors, winning the nuPlan planning challenge 2023.

## Introduction

Despite learning-based systems' success in vehicle motion planning research, a lack of standardized large-scale datasets for benchmarking holds back their transfer from research to applications. The recent release of the nuPlan dataset and simulator, a collection of 1300 hours of real-world vehicle motion data, has changed this, enabling the development of a new generation of learned motion planners, which promise reduced manual design effort and improved scalability....

Open- and closed-loop evaluation are misaligned. Most learned planners are trained through the supervised learning task of forecasting the ego vehicle's future motion conditioned on a desired goal location. We refer to this setting as ego-forecasting. In nuPlan, planners can be evaluated in two ways: in open-loop evaluation, which measures ego-forecasting accuracy using distance-based metrics or in closed-loop evaluation, which assesses the actual driving performance in simulation with metrics such as progress or collision rates....

Limitations. While we significantly improve upon the established IDM model, PDM still does not execute lane-change maneuvers. Lane change attempts often lead to collisions when the ego-vehicle is between two lanes, resulting in a high penalty as per the nuPlan metrics. PDM relies on HD maps and precise offboard perception that may be unavailable in real-world driving situations. While real-world deployment was demonstrated for learning-based methods, it remains a significant challenge for rule-based approaches....

Conclusion. In this paper, we identify prevalent misconceptions in learning-based vehicle motion planning. Based on our insights, we introduce PDM-Hybrid, which builds upon IDM and combines it with a learned ego-forecasting component. It surpassed a comprehensive set of competitors and claimed victory in the 2023 nuPlan competition.

Forecasting. In nuPlan, the simulator provides an orientation vector and speed for each dynamic agent such as a vehicle or pedestrian. We leverage a simple yet effective constant velocity forecasting over the horizon $F$ of 8 seconds at 10Hz.

The acceleration limit $a$, target speed $v_{0}$, safety margin $s^{\ast}$, and exponent $\delta$ are manually selected. Intuitively, the policy uses an acceleration $a$ unless the velocity is already close to $v_{0}$ or the leading vehicle is at a distance of...
