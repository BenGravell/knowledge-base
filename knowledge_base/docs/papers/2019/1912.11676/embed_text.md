## Introduction

Adoption of autonomous vehicles in the near future is expected to reduce the number of road accidents and improve road safety. However, for safe and efficient operation on roads, an autonomous vehicle should not only understand the current state of the nearby road-users, but also proactively anticipate their future behaviour. One part of this general problem is to predict the behaviour of pedestrians (or generally speaking, the vulnerable road-users), which is well-studied in computer vision literature. There are also several review papers on pedestrian behaviour prediction such as. Another equally important part of the problem is prediction of the intended behaviour of other vehicles on the road. In contrast to pedestrians, vehicles' behaviour is constrained by their higher inertia, driving rules and road geometry, which could help reduce the complexity of the problem, compared to aforementioned problem. Nonetheless, new challenges arise from interdependency among vehicles behaviour, influence of traffic rules and driving environment, and multimodality of vehicles behaviour. Practical limitations in observing the surrounding environment and the required computational resources to execute prediction algorithms also add to the difficulty of the problem, as explained in the later sections of this paper.

There are several published survey papers on vehicle behaviour analysis. For example, Shirazi and Morris provide a review of vehicle monitoring, behaviour and safety analysis at intersections. A review of unsupervised approaches for vehicle behaviour analysis with a focus on trajectory clustering and topic modelling methods is provided . Anomaly detection techniques using visual surveillance are reviewed . In a joint review is provided on tracking, prediction and decision making for autonomous driving. None of these studies specifically focus on vehicle behaviour prediction. In the most related paper to our work, Lefevre et al. provide a survey on vehicle behaviour prediction and risk assessment in the context of autonomous vehicles. The authors review various conventional approaches that applied physics-based models and/or traditional machine learning algorithms such as Hidden Markov Models, Support Vector Machines, and Dynamic Bayesian Networks. Recent advances in machine learning techniques (e.g., deep learning) have provided new and powerful tools for solving the problem of vehicle behaviour prediction. Such approaches have become increasingly important due to their promising performance in complex and realistic scenarios. However, to the best of our knowledge, there is no systematic and comparative review of the latter deep learning-based approaches. We thus present a review of such studies using a new classification method which is based on three criteria: input representation, output type, and prediction method. In addition, we report the practical limitations of implementing recent solutions in autonomous vehicles. To make the paper self-contained, we also provide a generic problem definition for vehicle behaviour prediction.

The rest of this paper is organised to a number of sections: Section II is an introduction to the basics and the challenges of vehicle behaviour prediction for autonomous vehicles. The definition of used terminologies and the generic problem formulation are also given in section II. Section III reviews the related deep learning-based solutions and classifies them based on three criteria: input representation, output type, and prediction method. Section IV discusses the commonly used evaluation metrics, compares the performance of several well-known trajectory prediction models in public highway driving datasets, and highlights the current research gaps in the literature and potential new research directions. The key concluding remarks are given in section V.

## Basics and Challenges of Vehicle Behaviour Prediction

Object detection and behaviour prediction can be considered as two main functions of the perception system of an autonomous vehicle. While both of them rely on on- and off-board sensory data, the former aims to localize and classify the objects in the surrounding environment of the autonomous vehicle and the latter provides an understanding of the dynamics of surrounding objects and predicts their future behaviour. Behaviour prediction plays a pivotal role in autonomous driving applications as it supports efficient decision making and enables risk assessment. In this section, we firstly discuss the challenges of vehicle behaviour prediction, then we provide a terminology for vehicle behaviour prediction, and finally we present a generic probabilistic formulation of the problem.

### II-A Challenges

Vehicles (e.g., cars and trucks) have well-structured motions which are governed by driving rules and environment conditions. In addition, vehicles, as non-holonomic systems, cannot change their trajectories instantly to desired ones. However, vehicle behaviour prediction is not a trivial task due to several challenges. First, there is an interdependency among vehicles behaviour where the behaviour of a vehicle affects the behaviour of other vehicles and vice versa. Therefore, predicting the behaviour of a vehicle requires observing the behaviour of surrounding vehicles. Second, road geometry and traffic rules can reshape the behaviour of vehicles. For example, placing a give-way sign in an intersection can completely change the behaviour of vehicles approaching it. Therefore, without considering traffic rules and road geometry, a model trained in a specific driving environment would have limited performance in other driving environments. Third, the future behaviour of vehicles is multimodal, meaning that given history of motion of a vehicle, there may exist more than one possible future behaviour for it. For example, when a vehicle is slowing down at an intersection without changing its heading direction, both turning right and turning left motions could be expected. A comprehensive behaviour prediction module in an autonomous vehicle should identify all possible future motions to allow the vehicle to act reliably.

In addition to the intrinsic challenges of the vehicle behaviour prediction problem, implementing a behaviour prediction module in autonomous vehicles comes with several practical limitations. For example, there are restricted computational resources for on-board implementation in autonomous vehicles. In addition, autonomous vehicles can partially observe the surrounding environment using their on-board sensors due to their limitations (e.g., object occlusion, limited sensor range, and sensor noise). Most of existing studies assume having access to a wide unobstructed top-down view of the driving environment which can be obtained by infrastructure sensors (e.g. an infrastructure surveillance camera). Nonetheless, such data can be available if there exists a communication channel with sufficient capacity between the infrastructure and the autonomous vehicle. In addition, it is not cost-effective to cover all road sections with such sensors. Therefore, a behaviour prediction module cannot always rely on unobstructed vision from an infrastructure sensor.

### II-B Terminology

To define the problem of vehicle behaviour prediction, we adopt the following terms: Target Vehicles (TVs) are the vehicles whose behaviour we are interested in predicting.

Ego Vehicle (EV) is the autonomous vehicle which observes the surrounding environment to predict the behaviour of TVs.

Surrounding Vehicles (SVs) are the vehicles whose behaviour is explored by the prediction model as it can potentially impact TV's future behaviour. Different studies may adopt different criteria for selecting SVs based on their modelling assumptions.

Non Effective Vehicles (NVs) are the remaining vehicles in driving environment that are assumed to have no impact on the TV's behaviour.

Figure 1 illustrates an example of a driving scenario using the proposed terminology. In this Figure a distance-based criterion, as an example, is used to divide the vehicles into SVs and NVs.

Figure 1: An illustration of the adopted terminology and limited observability of the EV’s onboard sensors. As an example of a criterion for dividing vehicles into SVs and NVs, the vehicles within a threshold distance, d, to the TV are considered to have impact on the TV’s behaviour. Unobservable vehicles by the EV, including two of the SVs are represented with blur effect. The limited observability can cause inaccurate prediction. For example, the preceding vehicle of the TV, which is not observable by the EV, is changing its lane allowing the TV to accelerate.

### II-C Generic Problem Formulation

We use a probabilistic formulation for vehicle behaviour prediction to cope with the uncertain nature of the problem. The word "behaviour" and "manoeuvre" are sometimes used in the literature interchangeably; however, we consider "vehicle behaviour" as a general term that can imply vehicle manoeuvre or trajectory depending on how it is represented in the problem formulation. In the generic problem formulation, we represent the future behaviour of TVs as the states $X_{TVs}$ they will traverse in the future, defined as: Where $x_{t}^{i}$ represents the states (e.g., position) of vehicle $i$ at time step $t$, $N$ is the number of TVs, and $m$ is the length of the prediction window.

The generic problem is formulated as computing the conditional distribution $P{(\left. X_{TVs} \middle| O_{EV} \right.)}$, where $O_{EV}$ are the available observations to the EV. This distribution is a mutual distribution over series of states of several interdependent vehicles, which can be intractable. To reduce the computational requirement of estimating $P{(\left. X_{TVs} \middle| O_{EV} \right.)}$, many of existing works dropped the interdependency among vehicles future behaviour. As such, the behaviour of each TV can be predicted separately with an affordable computational requirement. At each step, one vehicle is selected as the TV and its $P{(\left. X_{TV} \middle| O_{EV} \right.)}$ is calculated, where: Where $T$ is the selected TV.

## Classifications of Existing Works

Lefevre et al. classifies vehicle behaviour prediction models to physics-based, manoeuvre-based, and interaction-aware models. The simplest approaches that assume the behaviour of vehicles only depends on laws of physics are classified in physics-based models. The models that predict vehicles' behaviour based on their intended manoeuvre are called maneuvre-based approaches. Finally, the more advanced models that consider interaction among vehicles are called interaction-aware models. At the time of writing their paper, in 2014, there has been only a few examples of such interaction-aware model. However, several advanced approaches, mostly deep learning-based has been proposed in the literature since 2014 that requires more detailed classification. Thus, we present three classifications based on three different criteria: input representation, output type, and prediction method. First, we classify existing studies based on how they represent the input data. In this classification, the interaction-aware models are divided into three classes. In second classification, different approaches are classified based on their prediction output. We do not include physics-based approaches as they are no longer state-of-the-art, but different deep learning methods used in behaviour prediction are discussed and classified in the last classification. Figure 2 provides the classes and sub-classes for each aforementioned classification criterion. The following subsections address the classification based on each criterion individually.

Figure 2: Proposed classifications of state-of-the-art deep learning approaches for vehicle behaviour prediction

### III-A Input Representation

In this subsection, we provide a classification of existing studies based on the type of input data and how it is represented. We divide them into four classes: track history of the TV, track history of the TV and SVs, simplified bird's eye view, and raw sensor data. The last three classes can be considered as sub-classes of interaction-aware approaches which was introduced . We also discuss the availability of these input data in autonomous driving applications.

### III-A1 Track history of the TV

The conventional approach for predicting behaviour of the TV is to only use its current state (e.g. position, velocity, acceleration, heading) or track history of its states over time. This feature can be estimated if the TV is observable by the EV's sensors.

In, the track history of x-y position, speed, and heading of the TV are used to predict its behaviour at different road junctions. All these works study the behaviour of the TV in an environment without any SVs. Few deep learning-based methods use this input set to predict the vehicle behaviour in a driving environment with presence of other vehicles. Xin et al. argue that the information of SVs is not available due to EV's sensor limitations and object occlusion; however, some of the SVs can usually be observed by EV's sensor (see Figure 1). Excluding the observable SV's state from the input set may result in inaccurate prediction of the TV's behaviour due to interdependencies of vehicles' behaviour.

Although the track history of the TV has highly informative features about its short-term future motion, relying only on the TV's track history can lead to erroneous results particularly in long-term prediction in crowded driving environments.

### III-A2 Track history of the TV and SVs

One approach to consider the interaction among vehicles is to explicitly feed the track history of the TV and SVs to the prediction model. The SVs' states, similar to the TV's states, can be estimated in the object detection module of the EV; however, some of the SVs can be outside of the EV's sensor range or they might be occluded by other vehicles on the road.

The existing studies vary in how to divide the vehicles in the scene into surrounding vehicles (SVs) and non-effective vehicles (NVs). In, history of states of the TV and six of its closest neighbours are exploited to predict the TV's behaviour. In, the three closest vehicles in the TV's current lane and two adjacent lanes are chosen as reference vehicles. The reference vehicles and the vehicles in front and behind of the two reference vehicles in adjacent lanes are selected as the SVs. The authors in consider nine vehicles in three lanes surrounding the target vehicle including two vehicles in front of the TV. They indicate that considering more vehicles in the input data can improve the performance of behaviour prediction. For example, in a traffic jam, knowing that the second vehicle ahead of the TV is accelerating can enable early prediction of speed increase for the TV. Instead of considering a fixed number of vehicles as the SVs, a distance threshold is defined to divide vehicle into the SVs and NVs . It means that only the interactions of vehicles within this threshold are considered in the prediction model. In, the states of all the observable agents (e.g. vehicles, pedestrian, and cyclist) are used with different weights, obtained by soft attention mechanism, corresponding to their impacts on TV's behaviour.

One drawback of most of these studies is that they assume that the states of all SVs are always observable, which is not a practical assumption in autonomous driving applications. A more realistic approach should always consider sensor impairments like occlusion and noise. In addition, relying only on the track history of the TV and SVs is not sufficient for behaviour prediction, because other factors like environment conditions and traffic rules can also modify the behaviour of vehicles.

### III-A3 Simplified Bird's Eye View

An alternative way to consider the interaction among vehicles is by exploiting a simplified Bird's Eye View (BEV) of the environment. In this approach, static and dynamic objects, road lane, and other elements of the environment are usually depicted with a collection of polygons and lines in a BEV image. The result is a map-like image which preserves the size and location of objects (e.g. vehicles) and the road geometry while ignoring their texture.

Lee et al. fuse front-facing radar and camera data to form a binary two-channel BEV image covering the frontal area of the EV. One of the image channels specifies whether the pixel is occupied by a vehicle or not, and the other depicts the existence of lane marks. For $n$ past frames, the images are produced and stacked together to form a 2n-channel image as the input to the prediction model. Instead of using a sequence of binary images, indicating the existence of objects over time, a single BEV image is used . In this image, each element of the scene (e.g., road, cross-walks) loses its actual texture and instead is colour coded according to its semantics. The vehicles are depicted by colour-coded bounding boxes and the location history of vehicles are plotted using bounding boxes with same colour and reduced level of brightness.

To enrich the temporal information within the BEV image, Deo and Trivedi use a social tensor which was first introduced in (known as social pooling layer). A social tensor is a spatial grid around the target vehicle that the occupied cells are filled with the processed temporal data (e.g., LSTM hidden state value) of the corresponding vehicle. Therefore, a social tensor contains both the temporal dynamic of vehicles and spatial inter-dependencies among them. The authors in add scene context encoding channels to the input representation used . These channels are produced by encoding the static context of the scene (i.e., top-down view image of the scene) using a convolutional neural network. Lee et al. use social pooling layer as an additional input to another BEV representation created by performing semantic segmentation on front-facing camera of the EV and transforming it to the BEV.

The aforementioned works do not consider sensor impairment in the input representation. To overcome this drawback, a dynamic occupancy grid map (DOGMa ) is exploited . DOGMa is created from the data fusion of a variety of sensors and provides a BEV image of the environment. The channels of this image contain the probability of occupancy and velocity estimate for each pixel. The velocity information helps distinguish between static and dynamic objects in the environment; however, it does not provide complete knowledge about the history of dynamic objects.

The advantages of simplified BEV is that first it is flexible in terms of complexity of representation. Thus, it can match applications with different computational resource constraints. Second, it enables data fusion from different type of sensors into a single BEV representation.

One drawback of this input representation, that applies to the previously discussed input representations as well, is that it inherits the limitations of the perception module(e.g., object detection and tracking) used for estimating the states of static and dynamic objects (e.g., vehicles) in the driving environment. Therefore, an error in estimating the states, or under-representing the environment in the perception module will be cascaded to the prediction module. For example, if the object detection module use same label for an ambulance and a normal car, the influence of the ambulance on future behaviour of surrounding vehicles cannot be modelled.

- Complies with limited

- Does not consider the impact of environment and interaction among vehicles

- Inherits the limitation of the perception module of the EV.

Track history of the TV’s states (e.g., position, velocity, heading, and etc.).

Track History of the TV and SVs - Considers the impact of interaction among vehicles on the TV’s behaviour. - Does not consider the impact of environment on the TV’s behaviour. - The States of SVs are not always observable to the EV. - Inherits the limitation of the perception module of the EV History of states for the TV and six SVs.

History of states for the TV and three reference vehicles and four adjacent vehicles to them.

History of states for the TV and nine SVs.

A distance threshold is defined to divide vehicles into the SVs and NVs.

A soft attention mechanism is used to weight the impact of each observed vehicle.

Simplified Bird’s Eye View - Considers the impact of environment and interaction among vehicles on the TV’s behaviour. - Facilitates fusing the data gathered from different sensors on the EV. - Flexible in terms of complexity of representation. - It can comply with limited observability of the EV. - Inherits the limitation of the perception module of the EV.

A sequence of 2 channel top-down image covering the environment in front of the TV.

It indicates the existence of vehicles and lane lines over time.

A BEV image of environment, in which the road elements and vehicles are represented with color-coded polygons and lines.

A top-down grid representation. Each occupied cell is filled with the corresponding vehicle’s LSTM hidden state (similar to). is augmented with CNN encoded image of the static context of the driving scene.

Semantic segmentation of environment in BEV.

A top-down grid representation. Each cell contains the probability of the cell occupation, and its velocity.

Raw Sensor Data - Complies with limited observability of the EV. - No information loss. - High computational cost.

3D point clouds data over several time steps.

Lidar data and rasterized map (i.e., the TABLE I: Summary of classification of existing studies based on input representation and the advantages/disadvantages of each class

### III-A4 Raw sensor data

In this approach, raw sensor data is fed to the prediction model. Thus, the input data contains all available knowledge about the surrounding environment. This allows the model to learn extracting useful features from all available sensory data.

Raw sensor data, compared to previous input representations, has larger dimension. Therefore, more computational resources are required to process the input data, which can make it impractical for on-board implementation in autonomous vehicles. One solution to this problem is to share the computational resources among different functions of autonomous vehicle. In deep learning literature, it is common to train a model for multiple tasks. In an autonomous vehicle, the object detection module exploits raw sensor data, and it usually relies on a model with millions of parameters. Thus, it can be a good candidate for parameter sharing with the behaviour prediction module.

Leo et al. use a deep neural network to jointly solve the problems of 3D detection, tracking, and motion forecasting for autonomous vehicles. They exploit 3D point clouds data over several time frames. The data is represented in BEV images, and the height is considered as the channel dimension. To exploit the lidar data, the same approach is used ; however, they feed the 3D point cloud data in addition to a simplified BEV to their deep model.

Table I provides a summary of classification of existing studies based on input representation. It also summarizes the advantages and disadvantages of each class.

### III-B Output Type

In this subsection, we classify existing studies based on how they represent a vehicle future behaviour as the output of their prediction model. We consider four classes: manoeuvre intention, unimodal trajectory, multimodal trajectory, and occupancy map.

### III-B1 Manoeuvre Intention

Manoeuvre intention prediction (we shortly refer it as intention prediction) is the task of estimating what manoeuvre the vehicle intends to do in upcoming time-steps. For example, in highway driving, the set of manoeuvres could be left lane change, right lane change, and keeping the lane; while in an intersection, it could be: go straight, turn left, and turn right.

To predict the intention of a vehicle approaching a T-junction, Zyner et al. define three classes based on the destination of the vehicle, namely "east", "west", or "south". In, the same set of classes are used to predict the intention of a vehicle at an un-signalized roundabout. Phillips et al. design a generalizable intention prediction model that can predict the direction of travel of a vehicle up to 150m before reaching three- and four-way intersections. Ding et al. and Lee et al. apply intention prediction to highway driving scenario. The former proposes an intention prediction model to predict lane change and lane keeping behaviour for the TV; while, the latter designs a model to predict the cut-in intention of right/left preceding TVs w.r.t. the EV.

Existing studies predict the intention of vehicles using a set of few classes. One drawback of these works is that they can only provide a high-level understanding of the vehicle behaviour. This problem can be solved by subdividing high-level manoeuvres into sub-classes that describe the behaviour more precisely. For example, in a highway driving scenario, we can subdivide lane change classes into sharp lane change and normal lane change. Another drawback is the specificity of manoeuvre set to single driving environment, which can be resolved by defining a set that contains the manoeuvres in all desired driving scenarios. However, to predict a vehicle behaviour using large and in depth set of classes, a larger and more diverse training dataset that includes sufficient samples in each class is required. In addition, larger model capacity is needed to learn the mapping of the input data to the intention set.

### III-B2 Unimodal trajectory

Trajectory prediction models describe the future behaviour of a vehicle by predicting series of future locations of the TV over a time window. Dealing with continuous output of trajectory prediction models can add more complexity to the problem compared to discrete output of intention prediction models. However, predicting trajectory instead of intention, provides more precise information about future behaviour of vehicles. Given a specific driving situation and history of motion for a vehicle, it might be possible for it to traverse multiple different trajectories. Therefore, the corresponding distribution has multiple modes. Unimodal trajectory predictors are the models that only predict one of these possible trajectories (usually the one with highest likelihood). We divide such approaches into two sub-classes: Independent of intended manoeuvre: These approaches predict a unimodal trajectory without explicitly considering the effect of possible manoeuvres on it. The straightforward approach to predict the trajectory of the TV is to estimate the position of it over time. The predictor model can also estimate the displacement of the TV relative to its last position at each step. The other approach used in is to predict lateral position and longitudinal velocity separately. This approach can be specially useful when the region of interest is longitudinally large, therefore longitudinal position can be a quite large figure. In addition to the position and velocity, the heading angle of the vehicle is predicted. To cope with uncertainty of the trajectory prediction problem, Djuric et al. propose a trajectory prediction model that estimates standard deviation for the predicted x- and y-positions. In, the mean, standard deviation, and correlation coefficient of a bivariate Gaussian distribution corresponding to x- and y- positions are predicted for each time step. The main disadvantage of unimodal trajectory prediction models which are independent of intended manoeuvre is that they may converge to the average of all the possible modes because the average can minimize the displacement error of unimodal trajectory prediction; however, the average of modes is not necessarily a valid future behaviour. Figure 3 illustrates this problem.

Conditioned on intended manoeuvre: The other unimodal trajectory prediction approaches estimate the likelihood of each member of a predefined manoeuvre intention set and predict the trajectory that corresponds to the most probable intention. Xin et al. propose an intention-aware model to predict trajectory based on estimated lane change intention for the TV in highway driving. In, the intention set is extended from only lane change intentions to turning right, turning left, stopping, and so . This allows using the prediction model in urban driving. Unimodal trajectory prediction approaches conditioned on intended manoeuvre are unlikely to converge to the mean of modes, as in these approaches the predicted trajectory corresponds to one of predefined behaviour modes. However, there are two main drawbacks in these approaches. First, they cannot accurately predict a vehicle trajectory if the vehicle's intention does not exist in the predefined intention set. This problem can commonly occur in complex driving scenarios, as it is hard to predetermine all possible driving intentions in such environments. Second, unlike previous sub-class, we need to manually label the intention of vehicles in the training dataset, which is time-consuming, expensive and error-prone.

Figure 3: An illustration of invalidity of the average of manoeuvres. The red car is approaching the green car on the road. It is probable for the red car to either reduce its speed (green dots) or change its lane (blue dots). A unimodal non manoeuvre-based trajectory predictor may predict an average of these two manoeuvres (red dots) to reduce the prediction error. However, the average of these two manoeuvres is not a valid manoeuvre since it results in a collision with the preceding vehicle.

Summary of Output Type

- Usually has low computational cost. - Only provides a high-level understanding of the vehicle behaviour. - Usually covers manoeuvres that are specifically defined for a single driving scenario.

The destination of travel at a roundabout and The probabilities of turning right, left, and going straight at an intersection.

Lane change behaviour of the TV in highway driving scenarios.

Right/left cut-in of left/right preceding TVs.

General: - Less computational cost compared to multimodal models. Conditioned on intended manoeuvre: - Fixes the problem of convergence to the mean of behaviour modes. General: - Does not fully represent the vehicle behaviour prediction space which is multimodal. Independent from intended manoeuvre: - Is prone to convergence to the mean of behaviour modes. Conditioned on intended manoeuvre: - Is prone to trajectory prediction error if the vehicle’s intention is not among pre-defined intentions. - Manual labelling is required.

The positions of the TV over The displacement of the TV relative to its last position for each step.

Longitudinal velocities and lateral positions over time.

The x-y position and the standard deviation.

The mean and variance of a bivariate Gaussian distribution corresponding to The bounding box (e.g. location and heading angle) of the TV.

The TV’s trajectory (based on lane change estimation for highway driving).

The TV’s trajectory (based on intention estimation for urban driving).

General: Potentially can fully represent the vehicle behaviour prediction multimodal space. Dynamic modes: - No manual labelling for behaviour modes is required. - Potentially can adopt to different driving situations. General: - High computational cost. Dynamic modes: - Is prone to convergence to one behaviour mode or not to explore all the modes. Static modes: Same drawbacks of unimodal models conditioned on intention.

The trajectory distribution per each of six predefined manoeuvres and A number of samples from the estimated A number of deterministic trajectories sequences and their probabilities.

- Can potentially predict multiple

- prediction accuracy is limited by size of cells of the map.

The probability of occupancy for each pixel of BEV grid map of the driving TABLE II: Summary of classification of existing studies based on output type and the advantages/disadvantages of each class

### III-B3 Multimodal trajectory

Multimodal trajectory prediction models predict one trajectory per behaviour modes (a.k.a. policy/manoeuvre/intention) alongside the mode probability. We divide multimodal prediction approaches into two sub-categories: Static modes: In this sub-class, a set of behaviour modes is explicitly defined and the trajectories are predicted for each member of this set. In, a set of six manoeuvre classes for highway driving is defined and the trajectory distribution for each manoeuvre class is predicted. Predicting the distribution allows them to model the uncertainty of trajectory prediction for each manoeuvre separately. Their models also predict the likelihood of each manoeuvre.

Dynamic modes: In these approaches, the modes can be dynamically learnt based on the driving scenario. Cui et al. develop a model that predicts a fixed number of deterministic trajectory sequences and their probabilities. Each of these sequences can correspond to a possible manoeuvre in the driving environment. In, the distribution of vehicles' trajectory is modelled. Then, a fixed number of trajectory sequences are sampled from the modelled distribution and ranked based on their likelihoods.

The first sub-category of multimodal approaches can be considered as a multimodal extension to unimodal trajectory prediction approaches conditioned on intended manoeuvre as they predict the trajectories for all the behaviour modes rather than the mode with highest likelihood. Therefore, the drawbacks we mentioned for unimodal models conditioned on intended manoeuvre, namely difficulties in defining a comprehensive intention set and manual labelling of intentions in the training dataset, are not solved here. In contrast, the approaches in the second sub-category are exempted from these two problems as they do not require a pre-defined intention set. However, due to dynamic definition of modes, they are prone to converge to a single mode or not being able to explore all the existing modes.

### III-B4 Occupancy map

In these approaches, instead of predicting vehicles trajectories, the occupancy of each cell in a BEV map of the driving environment is estimated for future time-steps. In, the trajectory is predicted by estimating the vehicles occupancy likelihood for each cell in the dynamic occupancy grid map (DOGMa ) and each time-step in prediction horizon. They create DOGMa by assigning a grid map to a bird's eye view of the environment around the EV. Their model can dynamically predict multiple trajectory modes by assigning high probability to separate groups of cells in front of a TV. The drawback of such approaches is that their prediction accuracy is limited by the size of the cells in the map. Increasing the number of cells in the grid will reduce the cells' size; however, it results in higher computational costs.

Table II provides a summary of classification of existing studies based on output type. It also summarizes the advantages and disadvantages of each class.

### III-C Prediction Method

In this subsection, we classify existing studies based on the prediction model used into three classes, namely recurrent neural networks, convolutional neural networks, and other methods.

Summary of Prediction Method Recurrent Neural Networks - Good at processing temporal dependencies. Single RNN: - Requires additional mechanism to model interaction and contextual features.

Single RNN: Multi-layer LSTM network is used as a sequence classifier.

Single RNN: Two-layer LSTM is used to predict the parameters of acceleration distribution.

Single RNN: Single-layer LSTM is used to predict future x-y position of the TV.

Single RNN: An encoder-decoder LSTM is used to predict the probability of the occupancy Multiple RNNs: A group of GRUs is used to model the pairwise interaction between the TV and each of the SVs.

Multiple RNNs: One group of LSTMs is used to model individual vehicles’ trajectory, another group is used to model pairwise interaction.

Multiple RNNs: One LSTM is used to estimate the target lane, another LSTM is used to predict the trajectory based on estimated target lane.

Multiple RNNs: Multi-layer LSTM are used to predict mixtures of Gaussian distribution.

Multiple RNNs: One LSTM encoder is applied to the input sequence. The hidden state is fed to six LSTM decoders (one per manoeuvre). Another LSTM encoder is used to predict the probability of each manoeuvre.

Multiple RNNs: multiple LSTMs are grouped as two layers: instance layer and category layer.

The former learns instance movement and their interactions, while the latter reason about the similarities of the instance in the same category.

Convolutional Neural Networks - Good at processing spatial dependencies. - 2D CNNs lack a mechanism to model data series.

Six layer CNN with convolution and fully connected layers are used to predict the intention MobileNetV2 is used as feature extractor.

A convolution-deconvolution architecture, introduced, is used to predict First, 3D convolutions are applied to the temporal dimension of input data. Then, a series of 2D convolution is used to capture spatial features. Finally, two branches of convolution layers are used to find the probability of being a vehicle and predict the bounding box over current and future frames.

First, two backbone CNNs are used to extract the features of lidar data and rasterized map separately. Then three different networks are applied to the concatenation of extracted features to detect vehicles and predict their future intention and trajectory.

- Usually rely on current state Parameters of vehicle behaviour distribution are estimated using multi-layer fully-connected Combination of RNNs and CNNs: - Can take advantage of capabilities of both RNNs and CNNs.

An LSTM is applied to each vehicle trajectory. The result is represented in a BEV grid structure and then is fed to a CNN. The output is fed to six LSTM decoders (one per manoeuvre).

A convolution network extracts spatial features from the input image. These features are fed to encoder-decoder LSTM. The result is fed to deconvolution network to map to output image with the same size as input.

CVAE-based encoder-decoder GRU generates trajectory distribution. A number of samples from this distribution are ranked and refined based on contextual features.

A concatenated vector of agents’ movement and static scene encoded by LSTMs and CNNs, respectively are fed to a U-net like network. The encoded movement in the input and output of the mentioned network is fed to LSTM decoders to predict future trajectory for the agents.

Graph Neural Networks: - Comply with graph structure of traffic. - Static scene context is usually neglected.

Graph Convolutional Network (GCN) and Graph Attention Network (GAT) are used with some adaptations.

Graph Convolutional Model is used which consists of several convolutional and graph operation TABLE III: Summary of classification of existing studies based on the prediction method and the advantages/disadvantages of each class

### III-C1 Recurrent neural networks

The simplest recurrent neural network (a.k.a. Vanilla RNN) can be considered as an extension to two-layer fully-connected neural network where the hidden layer has a feedback. This small change allows to model sequential data more efficiently. At each sequence step, the Vanilla RNN processes the input data from current step alongside the memory of past steps, which is carried in the previous hidden neurons. A Vanilla RNN with sufficient number of hidden units can, in principle, learn to approximate any sequence to sequence mapping. However, it is difficult to train this network to learn long sequences in practice due to gradient vanishing or exploding, which is why gated RNNs are introduced. In each cell of these networks, instead of a simple fully connected hidden layer, a gated architecture is deployed. Long short-term memory (LSTM) and Gated recurrent unit (GRU) are the most commonly used gated RNNs. In vehicle behaviour prediction, LSTMs are the most used deep models. Here, we sub-categorize recent studies based on the complexity of network architecture: Single RNN: In these models, either a single recurrent neural network is used in the simplest form of behaviour prediction (e.g., intention prediction or unimodal trajectory prediction) or a secondary model is used alongside a single RNN to support more sophisticated features like interaction-awareness and/or multimodal prediction. To predict the intention of vehicles, an LSTM is used by as a sequence classifier. In this task a sequence of features is fed to successive cells of an LSTM. Then, the hidden state of the last cell in the sequence is mapped to output dimension (i.e., the number of defined classes). In, the input is embedded using a fully-connected layer and is fed to a three-layer LSTM; while, a two-layer LSTM without embedding is used. Altché and de La Fortelle use a single layer LSTM to predict the future x-y position of the TV as a regression task. Despite having less parameters and complexity, single layer LSTMs are reported to achieve competitive results compared to the multilayer counterpart in some tasks. To predict an intention-based trajectory, Ding and Shen use an LSTM encoder to predict the intention of the TV using its states. Then, the predicted intention and map information are used to generate an initial future trajectory for the TV. Finally, a nonlinear optimization method is used to refine the initial future trajectory based on the vehicles interaction, traffic rules (e.g. red lights), and road geometry. To predict multimodal behaviour, Zyner et al. first use an encoder-decoder three-layer LSTM to predict the parameters of a weighted Gaussian Mixture Model (GMM) for each step of the future trajectory. Then, a clustering approach is used to extract the trajectories that correspond to the modes with highest probabilities. Park et al. use an encoder decoder LSTM to predict the probability of occupancy on a grid map and apply a beam search algorithm to select $k$ most probable future trajectory candidates.

Multiple RNNs: To deal with multimodality and/or interaction awareness within recurrent neural networks, usually an architecture of several RNNs are used in existing studies. Ding et al. use a group of GRU encoders to model the pairwise interaction between the TV and each of SVs, based on which the intention of the TV is predicted for a longer horizon. Dai et al. use two groups of LSTM networks for the TV's trajectory prediction, one group for modelling the TV and each of SVs individual trajectory and the other for modelling the interaction between the TV and each of the SVs. Xin et al. exploit one LSTM to predict the target lane of the TV and another LSTM to predict the trajectory based on the TV's states and the predicted target lane. To predict multimodal trajectories, the authors in use six different decoder LSTMs which correlate with six specific manoeuvres of highway driving. An encoder LSTM is applied to the past trajectory of vehicles. The hidden state of each decoder LSTM is initialized with the concatenation of the last hidden state of the encoder LSTM and a one-hot vector representing the manoeuvre specific to each decoder. The decoder LSTMs predict the parameters of manoeuvre-conditioned bivariate Gaussian distribution of future locations of the TV. Another encoder LSTM is also used to predict the probability of each of six manoeuvres. Multiple LSTMs are structured in as two main layers, named as instance layer and category layer. The former learns the instance (i.e. agents) movement and their interactions and the latter reason about the similarities among the instances of same category. This network is applied to a graph representation of input data containing 4 dimensions for the instances, their interactions, time, and high-level categorization of instances.

Although RNNs are one of the main neural networks associated with data series analysis and prediction such as trajectory prediction, they have deficiency in modelling spatial relationship such as vehicles spatial interaction and image-like data such as driving scene context. This explains why sophisticated solutions using RNNs usually exploit additional methods to compensate the weakness of single RNN.

### III-C2 Convolutional neural networks

Convolutional neural networks (CNNs) include convolution layers, where a filter with learnable weights is convolved over the input, pooling layers, which reduce the spatial size of input by sub-sampling, and fully-connected layers, which map their input to desired output dimension. CNNs are commonly used to extract features from image data. They have achieved successful results in the computer vision domain. This success motivates researchers in other domains to represent their data as an image to be able to apply CNNs on them. However, recently one-dimensional CNNs are also widely used to extract features from one-dimensional signals.

Lee et al. use a six-layer CNN to predict the intention of surrounding vehicles using a binary BEV representation. MobileNetV2, which is a memory-efficient CNN designed for mobile applications, is used in to extract relevant features from a relatively complex BEV representation. Hoermann et al. use a convolution-deconvolution architecture, which was previously introduced in for image segmentation task, to output the probability of occupancy for future time steps in a BEV image. This model first generates a feature vector using a convolutional network. Then, a deconvolutional network is used to upscale this vector to the output image. A more complex architecture is used in to deal with the tasks of object detection and behaviour prediction simultaneously. In, 3D convolution is performed on the temporal dimension of 4D representation of voxelized lidar data to capture temporal features, then a series of 2D convolutions are applied to extract spatial features. Finally, two branches of convolution layers are added to predict the bounding boxes over the detected objects for current and future frames and estimate the probability of being a vehicle for the detected objects, respectively. In, two backbone CNNs are used to separately process the BEV lidar input data and the rasterized map. The extracted features are concatenated and fed to three different networks to detect the vehicles, estimate their intention, and predict their trajectories.

Convolutional neural network are valued in vehicle behaviour prediction for their capabilities in taking image-like data, generating image-like output, and keeping spatial relationship of the input data while processing it. These capabilities enables modelling vehicles' interaction and driving scene context and producing occupancy map output. However, 2D CNNs lack a mechanism to model data series which is required in vehicle behaviour prediction for modelling temporal dependencies among vehicles' states over time.

### III-C3 Other Methods

Fully-connected Neural Networks: A simplistic approach for vehicle behaviour modelling is to rely only on the current state of the vehicles, which might be inevitable due to unavailability of states history of vehicles or first-order Markov assumption. In this case, the input data is not a sequence and any feed-forward neural networks (e.g. fully-connected neural network) can be used instead of RNNs. In, it is shown that in some driving scenarios, feed-forward neural networks can have competitive results with faster processing time compared to recurrent neural networks. Hu et al. use a multi-layer fully connected network to predict the parameters of a Gaussian Mixture Model (GMM). The GMM models the multimodal distribution of arriving time and final location for the TV.

Combination of RNNs and CNNs: In existing works, recurrent neural networks are used because of their temporal feature extracting power, and convolutional neural networks are used for their spatial feature extracting ability. This inspires some researchers to use both in their models to process both the temporal and spatial dimensions of the data. Nachiket et al. use one encoder-LSTM per vehicle to extract the temporal dynamics of the vehicle. The internal states of these LSTMs form a social tensor which is fed to a convolutional neural network to learn the spatial interdependencies. Finally, six decoder LSTMs are used to produce the manoeuvre-conditioned distribution of the future trajectory of the TV. In, a CNN is applied on simplified BEV images each representing the environment around the TV at different time frame. Then, the sequence of extracted features is fed to an Encoder-Decoder LSTM to learn the temporal dynamics of the input data. The decoder LSTM outputs are fed to a deconvolutional neural network to produce output images which represent how the environment around the TV will evolve in the following time steps. In, an encoder-decoder GRU is used to generate the distribution of trajectories, then multiple samples of this distribution are fed to decoder GRU to refine and rank them. The latter module also receives the contextual features which are extracted by a CNN model applied on the scene representation. Multi-Agent Tensor Fusion (MATF) encoding and decoding is introduced . In the encoding part, a social tensor, augmented with convolutional encoded scene context channels, is fed to a U-net like fully convolutional network to fuse interaction among agents and between agents and scene context while keeping spatial locality. Finally, the fused vectors for each vehicle are extracted from the output layer of the U-net like network and are added to the LSTM encoded vectors of the vehicles dynamics and then are fed to LSTM decoders to predict future trajectory per vehicle.

Graph Neural Networks: The vehicles in a driving scenario and their interaction can be considered as a graph in which the nodes are the vehicles and the edges represent the interaction among them. Using this representation, Graph Neural Networks (GNNs) can be used to predict TV's behaviour. Diehl et al. compare the trajectory prediction performance of two state-of-the-art graph neural networks, namely, Graph Convolutional Network(GCN) and Graph Attention Network (GAT). They also propose some adaptations to improve the performance of these networks for the vehicle behaviour prediction problem. Li et al. propose a graph-based interaction-aware trajectory prediction (GRIP) model. They use a graph convolutional model, which consists of several convolutional layers as well as graph operations, to model the interaction among the vehicles. The output of the graph convolutional model is fed to an LSTM encoder-decoder to predict the trajectory for multiple TVs. One drawback of current graph-based approach is that static scene context is usually neglected in the modelling procedure.

Table III provides a summary of classification of existing studies based on the prediction method.

## Evaluation

In this section, first we present evaluation metrics that are commonly used for vehicle behaviour prediction in existing studies. Then, the performance of some of existing works is discussed. Finally, we identify and discuss the main research gaps and opportunities.

### IV-A Evaluation Metrics

We discuss the evaluation metrics for intention prediction models and trajectory prediction models separately, as the former is a classification problem and the latter is a regression problem and each problem has a separate set of metrics.

Track history of the TV and SVs RNN (Single RNN) Track history of the TV RNN (Multiple RNNs) Simplified Bird’s Eye View Combination of RNNs and CNNs Track history of the TV and SVs RNN (Multiple RNNs) Simplified Bird’s Eye View Combination of RNNs and CNNs Track history of the TV and SVs RNN (Multiple RNNs) Track history of the TV and SVs Graph Neural Networks TABLE IV: Comparison of Trajectory Prediction Error of Some of the Existing Works for Different Prediction Horizons

### IV-A1 Intention Prediction Metrics

Accuracy: One of the most common classification metrics is accuracy which is defined as total number of correctly classified data samples divided by total number of data samples. However, relying only on the accuracy can be misleading for an imbalanced dataset. For example, the number of lane changes in a highway driving dataset is usually much less than lane keeping. Thus, an intention predictor that regardless of input data always output lane keeping gains high accuracy score. Therefore, other metrics like precision, recall, and F1 score are also used in existing studies.

Precision: For a given class, precision is defined as the ratio of total number of data samples which are correctly classified in that class to the total number of samples classified as the given class. A low precision indicates a large number of incorrectly classified data as the given class.

Recall: For a given class, recall is defined as the ratio of total number of data samples which are correctly classified in that class to the total number of samples in the given class. A low Recall indicates a large number of data in the given class that are incorrectly classified in other classes.

F1 Score: The F1 score (a.k.a. F-score or F-measure) is a balance between precision and recall and is defined as: Negative Log Likelihood (NLL): For each data sample in a multi-class classification task, NLL is calculated as: Where $y_{c}$ is a binary indicator of correctness of predicting the data sample in class $c$, ${\hat{y}}_{c}$ is the predicted probability of the data sample belonging to class $c$, and $M$ is the number of classes. Although NLL values are not as interpretable as previously discussed metrics, it can be used to compare the uncertainty of different intention prediction models.

Average Prediction Time: This metric is used in intention prediction approaches, such as lane change prediction, where the approach is applied on a sliding window of the input data series to predict the occurrence of a positive class(e.g., lane change). The metric is obtained by taking the average of the time of the first correct positive class prediction for all samples, considering the time of lane change occurrence as the origin. In, they considered the time when a consistent correct lane change prediction starts to increase robustness of the metric.

### IV-A2 Trajectory Prediction Metrics

The following metrics are the commonly used metrics in the literature. A detailed discussion on other trajectory prediction metrics can be found .

Final Displacement Error (FDE): This error measures the distance between predicted final location ${\hat{y}}_{t_{final}}$ and true final location of the TV $y_{t_{final}}$ at the end of prediction horizon $t_{final}$, while it does not consider the prediction error occurred in other time steps in the prediction horizon.

Mean Absolute Error (MAE) or Root Mean Squared Error (RMSE): MAE measures the average magnitude of prediction error $e_{t}$, while RMSE measures the square root of the average of the squared prediction error: Where $n$ is number of data samples and $e_{t}$ can be defined as the displacement error between the predicted trajectory and the ground truth. MAE and RMSE are two of the most common metrics for regression problems and act roughly similar. However, RMSE is more sensitive to large errors due to usage of squared error in its definition.

Minimum of K Metric: In some of existing multimodal trajectory prediction studies, where $K$ trajectories are predicted for different modes, the metric (e.g., MSE, FDE) is calculated using one of the $K$ trajectories that minimize the metric (i.e., best predicted trajectory). The main shortcoming of this evaluation method, also discussed , is that the quality of ignored $K - 1$ trajectories is not examined. Therefore, a model, reported to have high performance using this metric, can have mostly poor predictions.

Cross Entropy: For a modelled trajectory distribution $q$, and ground truth data distribution $p$, the cross entropy can be calculated as: Cross entropy (a.k.a. Negative Log Likelihood) can be reported as a metric in both intention prediction and trajectory prediction; however, in multimodal trajectory prediction this metric can be more important as both MAE and RMSE are biased in favour of models that predict the average of modes which is not necessarily a good prediction, as discussed before. Although cross entropy penalises a multimodal prediction model for not covering all the modes of ground truth data distribution, it will assign relatively low penalty for a model that predict other modes in addition to ground truth modes. Therefore, Rhinehart et al. propose using a symmetrized cross entropy metric which is defined as: where $\overline{p}$ is an approximate to $p$, as it is not possible to evaluate the ground truth data distribution $p'$s PDF.

Computation Time: The trajectory prediction models are usually more complex compared to intention prediction models. Therefore, they can take more computation time which might make them impractical for on-board implementation in autonomous vehicles. Thus, it is crucial to report and compare computation time in trajectory prediction models.

### IV-B Performance of Existing Methods

In this part we compare the performance of some of reviewed trajectory prediction methods. The selected studies for comparison are the ones that used common publicly available datasets and common metrics. These studies report RMSE errors for prediction horizons of 1.0 to 5.0s on NGSIM I-80 and US-101 highway driving datasets. Table IV provides the reported error for each model which is obtained from the original paper (except the RMSE calculation of which has been modified by to match the position error in SI units). Note that the RMSE error is reported for longitudinal and lateral position separately ; however, we calculated the total RMSE error to be consistent with other studies. Furthermore, in the error is calculated for US-101 and I-80 separately; while, we report the average of them. We also report the prediction result of a constant velocity Kalman Filter(CV) model as a simple baseline which is obtained .

To compare the performance of selected works, Table IV states the category each work belongs to. According to the table IV, most of deep learning-based methods surpass the simple baseline constant velocity model (CV) with a high margin. Among reviewed deep learning-based models, complex models (e.g., Multiple RNNs or Combination of RNNs and CNNs) achieve better performance compared to simple models like single RNN. Nonetheless, increasing the complexity of output, by predicting multimodal trajectory instead of unimodal trajectory, does not always result in lower RMSE. For example, the models named GRIP and ST-LSTM achieve better performance compared to M-LSTM and CS-LSTM, while the former studies predict unimodal trajectories and the latter ones predict multimodal trajectories. This can be due to limited model capacity or limited data used in training the discussed multimodal trajectory prediction models.

### IV-C Research Gaps and New Opportunities

We discuss some of the main research gaps in vehicle behaviour prediction problem, which can be considered as opportunities for future works: Unlike object detection which has unified way of evaluation, there is no benchmark for evaluating existing studies on vehicle behaviour prediction. This prevents a fair comparison among different deep learning-based approaches and between deep learning-based and other methods. For example, among the reviewed deep learning-based papers, there are only seven works that use unified evaluation method (the works that we compare their performance in this paper). In addition, only a few works report the computation time of their algorithms, while this metric is highly important in autonomous driving applications. As a future work, a benchmark can be defined and used in vehicle behaviour prediction to be able to thoroughly compare the performance of different studies.

Most of the existing works consider full observability of the surrounding environment and vehicles' states which is not feasible in practice. Infrastructure sensors can provide non-occluded top-down view of the environment; however, it is impractical to cover all road sections with such sensors. Therefore, a realistic solution for behaviour prediction should always consider sensor impairments (e.g. occlusion, noise) which can limit the number of observable vehicles around the TV and in turn may reduce the accuracy of behaviour predictors in autonomous vehicles. One possible solution is the utilization of connected autonomous vehicles. In this case, the connected vehicle can exploit the information gained by sensors implemented in other vehicles or infrastructure through V2V and V2I communication (see Figure 4).

In recent studies, traffic rules are rarely considered as an explicit input to the model; while, they can reshape the behaviour of a vehicle in a driving scenario. Some of the existing studies include road direction or traffic light as an input to the prediction model which are only a small part of traffic signs and rules.

In addition to the vehicle's states and scene information which both are usually considered in recent works, other visual and auditory data of vehicles, like vehicle's signalling lights and vehicle horn can also be used to infer about its future behaviour.

Most of the existing works are limited to a specific driving scenario such as roundabout, intersection, and T-junction. However, a vehicle behaviour prediction module in fully autonomous vehicle should be able to predict the behaviour in any driving scenario. Developing a model which can be applied to a variety of driving environment can be a direction for future research.

Figure 4: An illustration of the vehicle behaviour prediction problem for connected autonomous vehicles. The sensors implemented in other autonomous vehicles and infrastructure can provide more information about the SVs and reduce the object occlusion problem in ego vehicle.

## Conclusion

Although deep learning-based behaviour prediction solutions have shown promising performance, especially in complex driving scenarios, by utilizing sophisticated input representation and output type, there are several open challenges that need to be addressed to enable their adoption in autonomous driving applications. Particularly, while most of existing solutions considered the interaction among vehicles, factors such as environment conditions and set of traffic rules are not directly inputted to the prediction model. In addition, practical limitations such as sensor impairments and limited computational resources have not been fully taken into account.
