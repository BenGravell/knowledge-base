Parting with Misconceptions about Learning-based Vehicle Motion Planning

Topics include Motion planning, Vehicles, Graphs, Datasets, Planning, Learning.

The release of nuPlan marks a new era in vehicle motion planning research, offering the first large-scale real-world dataset and evaluation schemes requiring both precise short-term planning and long-horizon ego-forecasting. Existing systems struggle to simultaneously meet both requirements. Indeed, we find that these tasks are fundamentally misaligned and should be addressed independently. We further assess the current state of closed-loop planning in the field, revealing the limitations of learning-based methods in complex real-world scenarios and the value of simple rule-based priors such as centerline selection through lane graph search algorithms. More surprisingly, for the open-loop sub-task, we observe that the best results are achieved when using only this centerline as scene context (i.e., ignoring all information regarding the map and other agents). Combining these insights, we propose an extremely simple and efficient planner which outperforms an extensive set of competitors, winning the nuPlan planning challenge 2023.

## Introduction

Despite learning-based systems' success in vehicle motion planning research, a lack of standardized large-scale datasets for benchmarking holds back their transfer from research to applications. The recent release of the nuPlan dataset and simulator, a collection of 1300 hours of real-world vehicle motion data, has changed this, enabling the development of a new generation of learned motion planners, which promise reduced manual design effort and improved scalability.

Our contributions are as follows: We demonstrate and analyze the misalignment between open- and closed-loop evaluation schemes in planning. We propose a lightweight extension of IDM with real-time capability that achieves state-of-the-art closed-loop performance. We conduct experiments with an open-loop planner, which is only conditioned on the current dynamic state and a centerline, showing that it outperforms sophisticated models with complex input representations.

## Discussion

Although rule-based planning is often criticized for its limited generalization, our results demonstrate strong performance in the closed-loop nuPlan task which best resembles real-world evaluation. Notably, open-loop success in part requires a trade-off in closed-loop performance. Consequently, imitation-trained ego-forecasting methods fare poorly in closed-loop. This suggests that rule-based planners remain promising and warrant further exploration. At the same time, given their poor performance out-of-the-box, there is room for improvement in imitation-based methods on nuPlan.

Integrating the strengths of closed-loop planning and open-loop ego-forecasting, we present a hybrid model. However, this does not enhance closed-loop driving performance; instead, it boosts open-loop performance while executing identical driving maneuvers. We conclude that considering precise open-loop ego-forecasting as a prerequisite for achieving long-term planning goals is misleading.
