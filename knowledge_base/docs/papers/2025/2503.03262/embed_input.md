Trajectory Prediction for Autonomous Driving: Progress, Limitations, and Future Directions

Topics include Trajectory prediction, Autonomous driving, Survey, Motion forecasting.

Reviews progress in trajectory prediction for autonomous driving, systematically discussing limitations of current approaches and outlining promising future research directions.

As the potential for autonomous vehicles to be integrated on a large scale into modern traffic systems continues to grow, ensuring safe navigation in dynamic environments is crucial for smooth integration. To guarantee safety and prevent collisions, autonomous vehicles must be capable of accurately predicting the trajectories of surrounding traffic agents. Over the past decade, significant efforts from both academia and industry have been dedicated to designing solutions for precise trajectory forecasting. These efforts have produced a diverse range of approaches, raising questions about the differences between these methods and whether trajectory prediction challenges have been fully addressed. This paper reviews a substantial portion of recent trajectory prediction methods proposing a taxonomy to classify existing solutions. A general overview of the prediction pipeline is also provided, covering input and output modalities, modeling features, and prediction paradigms existing in the literature. In addition, the paper discusses active research areas within trajectory prediction, addresses the posed research questions, and highlights the remaining research gaps and challenges.

## Introduction

The era of autonomous driving is on the verge of revolutionizing the modern transportation system. Automotive companies like Tesla, Waymo, and Cruise are pioneers in today's self-driving vehicle technology. The practical, innovative solutions developed by these companies, in conjunction with academic research, have led to rapid advancements in perception, prediction, planning, and control algorithms for autonomous driving. Predicting the future trajectories of surrounding traffic participants is essential for safe navigation and serves as a core task of the prediction module in the autonomous stack.

Autonomous vehicles (AVs) operate in heterogeneous traffic environments, and their prediction modules must account for the motion dynamics of all traffic participants, including vehicles, cyclists, pedestrians, and motorbikes. Among these, the motion of vehicles is influenced not only by their past motion, road topology, and physical constraints, but also by the behavior of nearby agents. As human drivers intuitively understand such interdependencies, e.g., anticipating that a neighboring car being cut off may respond with a sudden maneuver, AVs must be equipped with a similar interaction awareness mechanism.

## Discussion

In recent years, both academic and industrial research communities have made significant progress in advancing the field of trajectory prediction. To summarize these advancements, this section revisits the research questions posed at the beginning of the survey, elaborates on the remaining open challenges, and outlines potential future research directions.

## Conclusion

In this work, we have conducted an in-depth review of trajectory prediction approaches for autonomous driving, providing a comprehensive taxonomy to classify existing methodologies. This taxonomy distinguishes between learning-based and non-learning methods, with learning-based techniques further categorized into machine learning, deep learning, and reinforcement learning approaches. Additionally, we broadened the scope of the review to include a detailed overview of the prediction pipeline, covering input and output modalities, benchmark datasets used for evaluation, and the performance metrics critical for assessing prediction models.
