Deep Learning-based Vehicle Behaviour Prediction for Autonomous Driving Applications: A Review

Topics include Motion prediction, Vehicle behavior prediction, Trajectory prediction, Intention prediction, Deep learning, Autonomous driving, Review, Survey.

Reviews deep learning approaches for vehicle behavior prediction in autonomous driving, categorizing methods by architecture and prediction output type, with discussion of datasets and evaluation metrics.

Behaviour prediction function of an autonomous vehicle predicts the future states of the nearby vehicles based on the current and past observations of the surrounding environment. This helps enhance their awareness of the imminent hazards. However, conventional behaviour prediction solutions are applicable in simple driving scenarios that require short prediction horizons. Most recently, deep learning-based approaches have become popular due to their superior performance in more complex environments compared to the conventional approaches. Motivated by this increased popularity, we provide a comprehensive review of the state-of-the-art of deep learning-based approaches for vehicle behaviour prediction in this paper. We firstly give an overview of the generic problem of vehicle behaviour prediction and discuss its challenges, followed by classification and review of the most recent deep learning-based solutions based on three criteria: input representation, output type, and prediction method. The paper also discusses the performance of several well-known solutions, identifies the research gaps in the literature and outlines potential new research directions.

## Introduction

Adoption of autonomous vehicles in the near future is expected to reduce the number of road accidents and improve road safety. However, for safe and efficient operation on roads, an autonomous vehicle should not only understand the current state of the nearby road-users, but also proactively anticipate their future behaviour. One part of this general problem is to predict the behaviour of pedestrians (or generally speaking, the vulnerable road-users), which is well-studied in computer vision literature. There are also several review papers on pedestrian behaviour prediction such as....

There are several published survey papers on vehicle behaviour analysis. For example, Shirazi and Morris provide a review of vehicle monitoring, behaviour and safety analysis at intersections. A review of unsupervised approaches for vehicle behaviour analysis with a focus on trajectory clustering and topic modelling methods is provided in. Anomaly detection techniques using visual surveillance are reviewed in. In a joint review is provided on tracking, prediction and decision making for autonomous driving. None of these studies specifically focus on vehicle behaviour prediction. In the most related paper to our work, Lefevre et al....

## Conclusion

Although deep learning-based behaviour prediction solutions have shown promising performance, especially in complex driving scenarios, by utilizing sophisticated input representation and output type, there are several open challenges that need to be addressed to enable their adoption in autonomous driving applications. Particularly, while most of existing solutions considered the interaction among vehicles, factors such as environment conditions and set of traffic rules are not directly inputted to the prediction model....

### III-B4 Occupancy map

Table I provides a summary of classification of existing studies based on input representation. It also summarizes the advantages and disadvantages of each class.

A convolution network extracts spatial features from the input image. These features are fed to

The rest of this paper is organised to a number of sections: Section II is an introduction to the basics and the challenges of vehicle behaviour prediction for autonomous vehicles. The definition of used terminologies and the generic problem formulation are also given in section II....
