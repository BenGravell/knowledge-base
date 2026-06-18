<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Prediction Horizon Requirements for Automated Driving: Optimizing Safety, Comfort, and Efficiency

Topics include Motion prediction, Prediction horizon, Automated driving, Safety, Comfort, Efficiency.

<!-- chunk {"id": "summary-0002", "role": "summary", "section": "Summary", "weight": 2.0} -->

Analyzes how the required prediction horizon for autonomous driving depends on the competing objectives of safety, comfort, and efficiency, providing a framework for selecting appropriate prediction horizons for different driving scenarios and speed profiles.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Predicting the movement of other road users is beneficial for improving automated vehicle (AV) performance. However, the relationship between the time horizon associated with these predictions and AV performance remains unclear. Despite the existence of numerous trajectory prediction algorithms, no studies have been conducted on how varying prediction lengths affect AV safety and other vehicle performance metrics, resulting in undefined horizon requirements for prediction methods. Our study addresses this gap by examining the effects of different prediction horizons on AV performance, focusing on safety, comfort, and efficiency. Through multiple experiments using a state-of-the-art, risk-based predictive trajectory planner, we simulated predictions with horizons up to 20 seconds. Based on our simulations, we propose a framework for specifying the minimum required and optimal prediction horizons based on specific AV performance criteria and application needs. Our results indicate that a horizon of 1.6 seconds is required to prevent collisions with crossing pedestrians, horizons of 7-8 seconds yield the best efficiency, and horizons up to 15 seconds improve passenger comfort. We conclude that prediction horizon requirements are application-dependent, and recommend aiming for a prediction horizon of 11.8 seconds as a general guideline for applications involving crossing pedestrians.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

Automated vehicles (AVs) are becoming increasingly prevalent, and trajectory prediction of surrounding road users (RUs) is a critical component of these systems, since the AV's decisions will be largely based on the predicted motion of other RUs. When designing a system that accounts for the future motion of surrounding RUs, one must decide how much into the future to predict, i.e. the prediction horizon, which is used to plan an AV trajectory for the same horizon. The choice of prediction horizon can have a significant impact on AV behavior, however, in the development of prediction models the chosen horizon is often an ad hoc decision that depends on practical aspects, such as the length of traces available in the data used to develop these models. Additionally, the typical assessment of prediction models is performed at the subsystem-level, i.e. the prediction module, focusing on predictive accuracy. However, with this approach, the impact of predictions on the overall system, namely the AV, remains unclear. Consequently, prediction horizon requirements remain undefined.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

Despite the existence of several works showing that it is beneficial to integrate predictions in motion planning, there is no clear quantification of the relationship between the prediction horizon and the resulting impact on AV behavior. To establish requirements that a prediction model should adhere to, the impact that predictions have on AV behavior must first be understood. Once we understand this impact, we can determine the ideal prediction horizons that ensure safety and other key aspects like ride comfort and efficiency.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

The requirements that predictions must satisfy will be dependent on several other factors, like the type of object being predicted (e.g. vehicle vs. pedestrian), the specific scenario (e.g. lane change in a highway vs a crossing pedestrian), or even user preferences (e.g. a smoother ride is preferred over lower travel time). Hence, these requirements are application-dependent and should adapt to each situation.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

To specify prediction requirements, this work first investigates the impact that different prediction horizons have on the safety, comfort and efficiency of an AV. We do this by simulating and integrating predictions into a state of the art optimization-based planner that considers the predicted actions of other RUs. Additionally, we introduce a framework to establish both the minimum required and optimal prediction horizons for achieving targeted vehicle performance in specific applications. To show the applicability of our method, we focus on urban driving scenarios involving crossing pedestrians, which are among the most vulnerable participants in traffic.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Introduction", "weight": 1.5} -->

Impact analysis of trajectory prediction horizons: We explore the relationship between different prediction horizons and the safety, comfort, and efficiency of AVs in scenarios involving crossing pedestrians.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Introduction", "weight": 1.5} -->

A methodology to derive application-specific requirements: We introduce a versatile framework to determine prediction horizon requirements tailored to specific AV applications and performance goals. While we demonstrate its application in a limited set of scenarios and performance criteria, the framework is adaptable to other scenarios and criteria.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Introduction", "weight": 1.5} -->

Guidelines for required and optimal prediction horizons: Using our framework, we provide recommendations for the ideal horizon of trajectory prediction models in AV applications involving crossing pedestrians.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Introduction", "weight": 1.5} -->

The remainder of this article is structured as follows. Section II highlights prevalent choices of prediction horizons, related work combining predictions and motion planning, and vehicle-level metrics commonly used to evaluate AV performance. Section III introduces our proposed methodology to derive horizon requirements. Section IV summarizes the results and highlights limitations of this study. Finally, Section V concludes the work and outlines future improvements.

<!-- chunk {"id": "body-0012", "role": "body", "section": "II-A Choosing a Prediction Horizon", "weight": 1.0} -->

The field of trajectory prediction is dominated by machine learning methods nowadays. The development of these methods relies on datasets with pre-recorded RU trajectories, segmented in two parts with an observation and a prediction horizon, i.e. the portion of the trajectory available before prediction, and the portion to be predicted, respectively.

<!-- chunk {"id": "body-0013", "role": "body", "section": "II-A Choosing a Prediction Horizon", "weight": 1.0} -->

Table I presents an overview of popular datasets commonly used for trajectory prediction research. Methods using these datasets seem to be conditioned on either (i) the length of the traces contained in the dataset, or (ii) popular choice of horizons for a specific dataset used in previous work, which facilitates comparison of a new method without the need to re-implement previous ones.

<!-- chunk {"id": "body-0014", "role": "body", "section": "II-A Choosing a Prediction Horizon", "weight": 1.0} -->

Since the choice of prediction horizon is arbitrary and independent from AV performance metrics, predictive accuracy is often analyzed at various horizons to obtain a better coverage of a model's capabilities. For instance, methods working with UCY, ETH and SSD typically report performance at a horizon of 4.8 seconds, but some works also report their performance at 3.2 seconds. Methods evaluated on NGSIM, highD, and exiD report from 1 up to 5 seconds. Reporting the performance at different horizons presents a more complete assessment of a model's predictive capabilities, but it remains unclear how its predictions ultimately affect AV behavior and what the required and optimal horizons are.

<!-- chunk {"id": "body-0015", "role": "body", "section": "II-B Evaluating Predictions & their Impact on Vehicle Behavior", "weight": 1.0} -->

Predictions are mainly evaluated in terms of geometric accuracy with metrics such as minimum average displacement error, and minimum final displacement error, often disregarding their associated uncertainty and the impact they have on the behavior of the vehicle.

<!-- chunk {"id": "body-0016", "role": "body", "section": "II-B Evaluating Predictions & their Impact on Vehicle Behavior", "weight": 1.0} -->

The authors of take a critical look at current evaluation practices and conclude that trajectory prediction metrics do not reflect well the impact they have on AV behavior. To address this limitation, the authors of advocate for a novel planning-aware metric which better reflects performance in AVs, weighting the error of each prediction according to the impact it would have on the planned AV trajectory.

<!-- chunk {"id": "body-0017", "role": "body", "section": "II-B Evaluating Predictions & their Impact on Vehicle Behavior", "weight": 1.0} -->

Other than lacking evaluation practices, the authors of raise concern regarding the currently accepted output representation of predictions for downstream integration, since a majority of planning and control algorithms reason about system dynamics instead of the current prediction representation, i.e. a sequence of positions. Accordingly, they propose a dynamical system representation that allows the planning optimizer to simultaneously explore different AV controls and their effect on the predictions of surrounding RU's. Although not as efficiently as proposed, the current representation allows incorporating predictions in motion planning, and conversely use the AV's planned trajectory to influence predictions of surrounding RUs.

<!-- chunk {"id": "body-0018", "role": "body", "section": "II-B Evaluating Predictions & their Impact on Vehicle Behavior", "weight": 1.0} -->

Despite the existence of numerous studies coupling predictions with planning for improved AV performance, there is a noticeable gap in research quantifying these improvements. A significant aspect of uncertainty involves determining the necessary and ideal prediction horizons. That is, the shortest horizon that ensures acceptable AV performance, and the horizon that optimizes AV performance. Short horizons might not allow enough time to react accordingly, and the full benefits of predictions might not be realized. Conversely, excessively long horizons could lead to overly cautious behavior or increased computational demands, potentially diminishing AV performance.

<!-- chunk {"id": "body-0019", "role": "body", "section": "II-C Vehicle-level Metrics", "weight": 1.0} -->

To assess the impact of predictions on AV behavior, vehicle-level performance metrics are needed. AV performance is often measured in terms of safety, comfort, and efficiency.

<!-- chunk {"id": "body-0020", "role": "body", "section": "II-C1 Safety", "weight": 1.0} -->

The potential to increase safety is one of the main reasons AVs are a desirable technology. According to the National Highway Traffic Safety Administration, human error is a contributing factor in 94% of crashes, and it is expected that AVs will be able to prevent such crashes. Consequently, one of the most popular metrics to assess safety is collision rate, often compared to human-driven vehicles. Nonetheless, there are other relevant metrics used to assess the safety of an AV, such as disengagements (i.e. the number of times a human driver needed to take control of the vehicle), and safety violations.

<!-- chunk {"id": "body-0021", "role": "body", "section": "II-C2 Comfort", "weight": 1.0} -->

The comfort of AVs is commonly measured using ISO standard 2631, which provides approaches for categorizing comfort levels of vibration and shock motion at frequencies similar to those encountered in a vehicle. However, a recent study investigated empirically the relationship between a vehicle's acceleration and jerk, and the discomfort experienced by passengers, concluding that the standard models in ISO 2631 may not effectively describe the comfort of motions experienced in a vehicle. At the same time, they concluded that acceleration is the main descriptor of (dis)comfort, and derived acceleration thresholds for seven different ranges of comfort, from excellent to terrible.

<!-- chunk {"id": "body-0022", "role": "body", "section": "II-C3 Efficiency", "weight": 1.0} -->

Efficiency of an AV can be considered with respect to several aspects. A commonly used metric for measuring the efficiency of an AV is fuel efficiency, which in turn can help reduce emissions. Efficiency is also often measured in terms of travel time, which can be considered a deciding factor for choosing a mode of transport.

<!-- chunk {"id": "body-0023", "role": "body", "section": "Methodology", "weight": 1.0} -->

This section describes our methodology to derive prediction horizon requirements. Fig. presents an overview of this process. First, relevant scenarios are selected based on accidentology and pedestrian walking studies. Next, typical modules of an AV are integrated in a simulation environment considering varying prediction horizons of surrounding RUs. Finally, combining vehicle-level performance when using different horizons and the intended application operational design domain (ODD), horizon requirements are derived.

<!-- chunk {"id": "body-0024", "role": "body", "section": "III-A Scenario Selection", "weight": 1.0} -->

Accidentology studies highlight that vulnerable RUs such as pedestrians are among the most at-risk traffic participants in urban environments. Specifically, the most frequently occurring accident is a pedestrian crossing from the right without any sight obstruction. This group of accidents makes up 22.8% of car-to-pedestrian collisions, and it is the most lethal collision, amounting to 23.2% of all killed or severely injured pedestrians. In these accidents, vehicle speed ranged from 26 to 48 km/h, and pedestrian speeds are unknown. This group of accidents is selected as the basis of our study.

<!-- chunk {"id": "body-0025", "role": "body", "section": "III-A Scenario Selection", "weight": 1.0} -->

We investigate the impact of predictions on three similar scenario categories (SCs): SC1, SC2, and SC3, where the AV speeds are set to 30, 40 and 50km/h respectively. For the three SCs, one hundred different pedestrian speeds are sampled randomly from a normal distribution describing pedestrian walking speeds, with mean 1.34m/s and standard deviation 0.37m/s. Thus, with 3 SCs, 22 different horizons, and 100 pedestrian speeds, a total of 6600 runs are executed.

<!-- chunk {"id": "body-0026", "role": "body", "section": "III-A Scenario Selection", "weight": 1.0} -->

The scenarios are set up such that if the AV does not react to the pedestrian, a front collision occurs in the middle of the AV when the pedestrian is walking at the mean speed of 1.34m/s. Consequently, for pedestrian speeds that significantly deviate from this value, there would be no collision even when the AV does not react to the pedestrian, due to the pedestrian walking too slow or too fast.

<!-- chunk {"id": "body-0027", "role": "body", "section": "III-A Scenario Selection", "weight": 1.0} -->

Slow pedestrian speeds, such that the AV passes the pedestrian collision-free before it crosses the road.

<!-- chunk {"id": "body-0028", "role": "body", "section": "III-A Scenario Selection", "weight": 1.0} -->

Pedestrian speeds that result in a collision when the AV does not react to the pedestrian.

<!-- chunk {"id": "body-0029", "role": "body", "section": "III-A Scenario Selection", "weight": 1.0} -->

Fast pedestrian speeds, such that the AV passes the pedestrian collision-free after it has crossed the road.

<!-- chunk {"id": "body-0030", "role": "body", "section": "III-B1 Perception and world modeling", "weight": 1.0} -->

Analyzing the impact of perception and world modeling performance on vehicle performance falls out of the scope of this study. Consequently, factors such as sensor noise and perception-related challenges are not considered. In our simulations, we gather data on nearby objects, such as road lanes and other RUs, directly from the simulator.

<!-- chunk {"id": "body-0031", "role": "body", "section": "III-B2 Predictions", "weight": 1.0} -->

A wide range of methods exists for predicting the trajectories of RUs, each with distinct advantages and drawbacks. Opting for a single prediction method could skew our results in favor of that method. Additionally, trajectory prediction methods are rapidly evolving and becoming more accurate. Thus, if using currently existing prediction methods to derive their requirements, these requirements could become obsolete as the field evolves. To circumvent this, our approach involves simulating an ideal scenario, where predictions are flawless, to find the horizons that would provide the most benefits if predictions were perfect. Different time horizons of these ideal predictions are then provided to the planner to find the necessary and most beneficial horizons. A thorough investigation into the effects of prediction inaccuracies and the subsequent derivation of accuracy requirements is reserved for future work. To limit simulation times and have a good coverage of the search space, we consider horizons

<!-- chunk {"id": "body-0032", "role": "body", "section": "III-B2 Predictions", "weight": 1.0} -->

and the achieved performance with horizons that are not in $\mathcal{H}$ is calculated by linear interpolation.

<!-- chunk {"id": "body-0033", "role": "body", "section": "III-B3 Planning & Control", "weight": 1.0} -->

To evaluate the effect of trajectory prediction on AV behavior, a state of the art planner is integrated in our simulations. This planner considers both the road infrastructure and the predicted positions of surrounding objects. It uses artificial potential-based risk fields within the cost function of a model-predictive control problem to find a trajectory that minimizes risk while progressing towards the AV's intended destination. For a more comprehensive description of this planner, we defer the reader to.

<!-- chunk {"id": "body-0034", "role": "body", "section": "III-C Performance Assessment", "weight": 1.0} -->

In this section, we outline our methodology for AV performance assessment and derivation of prediction horizon requirements. First, we present the vehicle-level performance metrics employed in our assessment. Subsequently, the proposed framework designed to determine both required and optimal prediction horizons is introduced. Lastly, we illustrate the versatility of this framework by introducing four distinct use cases to demonstrate its application across various AV settings tailored to specific operational purposes.

<!-- chunk {"id": "body-0035", "role": "body", "section": "III-C1 Vehicle-level Performance", "weight": 1.0} -->

To assess the impact of prediction horizons on AV behavior, we measure safety, comfort and efficiency as described in this section. Additionally, we analyze the real-time capabilities of our system.

<!-- chunk {"id": "body-0036", "role": "body", "section": "III-C1 Vehicle-level Performance", "weight": 1.0} -->

Let $f^{m}{(h,s)}$ denote the value achieved for vehicle-level metric $m$ and SC $s$ when using a prediction horizon $h$.

<!-- chunk {"id": "body-0037", "role": "body", "section": "Safety", "weight": 1.0} -->

The percentage of runs that are collision-free. Since we are mainly interested in achieving collision-free runs, we do not weigh in the AV's speed at impact, but we visualize it for illustrative purposes.

<!-- chunk {"id": "body-0038", "role": "body", "section": "Comfort", "weight": 1.0} -->

We adapt the categorization of (dis)comfort based on acceleration presented in combination and consider deceleration values as comfortable, uncomfortable, and highly uncomfortable, as shown in Table II. Considering the time that the vehicle is decelerating, we report the percentage of time spent on each comfort category. The resulting comfort in SC $s$ when using a prediction horizon $h$, $f^{\text{𝑐𝑜𝑚𝑓𝑜𝑟𝑡}}{(h,s)}$, is the percentage of time spent on the comfortable category.

<!-- chunk {"id": "body-0039", "role": "body", "section": "Efficiency", "weight": 1.0} -->

We investigate efficiency in terms of travel time, and calculate the relative increase of travel time, $\Delta t$, for each prediction horizon. That is, if $t_{b}{(s)}$ is the time it takes the vehicle to complete the route in scenario $s$ without a pedestrian crossing the road, and $t{(h,s)}$ is the time with the crossing pedestrian and using prediction horizon $h$, then

<!-- chunk {"id": "body-0040", "role": "body", "section": "Efficiency", "weight": 1.0} -->

To keep the interpretation of efficiency consistent with other metrics (i.e. within a positive range, and where a higher value of the metric denotes better performance), the final efficiency is calculated as

<!-- chunk {"id": "body-0041", "role": "body", "section": "Real-time execution", "weight": 1.0} -->

The ability to operate at a high frequency is not one of the goals of this study. However, with higher prediction and planning horizons, the load on the trajectory planner impeded its operation at the desired frequency^11^1All simulations are executed on a desktop computer with an AMD Ryzen 9 5900X processor, GeForce RTX 3070 Ti GPU, and 64GB DDR4 RAM., which had an impact on comfort and efficiency. Thus, we evaluate the frequency at which the planner updates its trajectories^22^2Measured by the rate of new trajectory arrivals on the corresponding ROS topic, averaged over a 21-sample sliding window.. For each simulation, we record the minimum frequency, and then report the mean and standard deviation of these values across the 100 runs for each horizon.

<!-- chunk {"id": "body-0042", "role": "body", "section": "III-C2 Deriving Required and Optimal Prediction Horizons", "weight": 1.0} -->

Different scenarios and metrics can lead to significantly different horizon requirements. Thus, concluding on a preferred horizon is not trivial. This section describes a methodology to derive the preferred horizon by combining multiple system-level (i.e. vehicle) metrics in a variety of scenarios.

<!-- chunk {"id": "body-0043", "role": "body", "section": "III-C2 Deriving Required and Optimal Prediction Horizons", "weight": 1.0} -->

In our simulations, all possible vehicle-level metrics are $\mathcal{M} = {\{\text{𝑠𝑎𝑓𝑒𝑡𝑦},\text{𝑐𝑜𝑚𝑓𝑜𝑟𝑡},\text{𝑒𝑓𝑓𝑖𝑐𝑖𝑒𝑛𝑐𝑦}\}}$, all possible SCs are $\mathcal{S} = {\{\textit{SC1},\textit{SC2},\textit{SC3}\}}$, and all possible horizons are $\mathcal{H}$ as. When considering a collection of metrics $M \subseteq \mathcal{M}$ and SCs $S \subseteq \mathcal{S}$, we aim to find a required and an optimal horizon, $r_{M}^{S}$, and $o_{M}^{S}$, such that horizon $r_{M}^{S}$ yields satisfactory AV performance for all metrics and scenarios considered, and horizon $o_{M}^{S}$ yields the best value of each metric in every scenario. If that is not possible, we should find the horizon that yields the best trade-off, as explained later in this section.

<!-- chunk {"id": "body-0044", "role": "body", "section": "III-C2 Deriving Required and Optimal Prediction Horizons", "weight": 1.0} -->

When considering only safety, i.e. $M = {\{\text{𝑠𝑎𝑓𝑒𝑡𝑦}\}}$, $r_{M}^{S} = o_{M}^{S}$ is the shortest horizon that maximizes safety. We aim at zero collisions, and anything else is not considered satisfactory.

<!-- chunk {"id": "body-0045", "role": "body", "section": "III-C2 Deriving Required and Optimal Prediction Horizons", "weight": 1.0} -->

If $M = {\{\text{𝑐𝑜𝑚𝑓𝑜𝑟𝑡}\}}$, $o_{M}^{S}$ is the shortest horizon that maximizes the share of comfortable braking, and $r_{M}^{S}$ is the horizon that minimizes the share of highly uncomfortable braking.

<!-- chunk {"id": "body-0046", "role": "body", "section": "III-C2 Deriving Required and Optimal Prediction Horizons", "weight": 1.0} -->

If $M = {\{\text{𝑒𝑓𝑓𝑖𝑐𝑖𝑒𝑛𝑐𝑦}\}}$, $o_{M}^{S}$ is the shortest horizon that maximizes efficiency, and $r_{M}^{S}$ is the shortest satisficing horizon, that is, the horizon achieving an efficiency that is within 15% of the optimal efficiency^33^3The threshold for the satisficing, i.e. near optimal "good enough", horizon is determined by visual inspection, selecting the horizon at which efficiency begins to converge. All the selected horizons yield an efficiency that is within 15% of the optimal value..

<!-- chunk {"id": "body-0047", "role": "body", "section": "III-C2 Deriving Required and Optimal Prediction Horizons", "weight": 1.0} -->

Different metrics may lead to conflicting required and optimal horizons; thus, a procedure is needed to find the overall optimal and required horizons when considering multiple potentially conflicting objectives and scenarios.

<!-- chunk {"id": "body-0048", "role": "body", "section": "Overall optimal horizon", "weight": 1.0} -->

When considering multiple objectives and scenarios to conclude on the overall optimal horizon, different situations are possible. Consider as an example the two situations shown in Fig., where the value of two metrics $m_{1}$ and $m_{2}$ are shown as a function of the prediction horizon. For simplicity, different SCs are left out of the example. In the first situation (left), both metrics $m_{1}$ and $m_{2}$ converge to their optimal values at horizons $o_{m_{1}}$ and $o_{m_{2}}$. In this case, we would choose the optimal horizon, $o_{M}$, to be the same as $o_{m_{2}}$, as this is the minimum horizon with which all considered metrics achieve their optimal value.

<!-- chunk {"id": "body-0049", "role": "body", "section": "Overall optimal horizon", "weight": 1.0} -->

In the second example, however, $m_{1}$ is negatively affected by longer horizons, therefore choosing $o_{m_{2}}$ as the optimal horizon is no longer possible. Since it is not possible to choose a horizon that leads to the optimal value across all metrics and scenarios, we should find the best trade-off. The best trade-off is subjective and depends on the relative importance given to different metrics and scenarios. To find the horizon that best balances all considered metrics across all considered SCs, the cost function $f^{C}$ is introduced as

<!-- chunk {"id": "body-0050", "role": "body", "section": "Overall optimal horizon", "weight": 1.0} -->

where $w_{s}$ and $w_{m}$ are weighting factors to balance the importance of each SC and metric. Recall that $f^{m}{(h,s)}$ denotes the value of metric $m$ achieved in scenario $s$ when using a prediction horizon $h$, thus, $f^{m}{(o_{m}^{s},s)}$ denotes the best value of metric $m$ in scenario $s$, achieved with horizon $o_{m}^{s}$. Additionally, note that ${\overset{\sim}{f}}^{m}$ is used instead of $f^{m}$, which denotes a normalized version of $f^{m}$ to ensure all metric values are in a common range^44^4In our case, between 0 and 100, where 0 maps to the worst value of the metric achieved in all simulations, and 100 maps to the best. in order to provide a more intuitive weighting scheme.

<!-- chunk {"id": "body-0051", "role": "body", "section": "Overall optimal horizon", "weight": 1.0} -->

The optimal horizon over all scenario categories $S$ and metrics $M$, $o_{M}^{S}$, is then calculated by obtaining the horizon that minimizes deviation from all optimal metric values for each scenario $s \in S$ and metric $m \in M$. In case the resulting horizon is not sufficient to guarantee safety, then the horizon that maximizes safety is used instead. That is,

<!-- chunk {"id": "body-0052", "role": "body", "section": "Overall required horizon", "weight": 1.0} -->

A different approach is taken to find the overall required prediction horizon. The reason for this deviation is illustrated with an example. Consider the two situations shown in Fig..

<!-- chunk {"id": "body-0053", "role": "body", "section": "Overall required horizon", "weight": 1.0} -->

In the first example (left), horizons beyond the required $r_{m_{1}}$ and $r_{m_{2}}$ all yield a satisfactory value for metrics $m_{1}$ and $m_{2}$, respectively, denoted in the figure by the highlighted rectangular area. Similarly to the example from Fig. (left), in this case the overall minimum required horizon, $r_{M}$, can simply be chosen the same as $r_{m_{2}}$. However, in Fig. (right), there is no horizon that yields a satisfactory value for all metrics simultaneously. If this value does not exist, the best alternative is to use the horizon achieving the best trade-off across all metrics and scenarios, the optimal horizon $o_{M}^{S}$, or the system designer should review the previously specified requirements for each vehicle-level metric.

<!-- chunk {"id": "body-0054", "role": "body", "section": "Overall required horizon", "weight": 1.0} -->

Thus, the overall required horizon is calculated as the shortest horizon that yields a satisfactory value for all considered metrics and scenarios, if it exists. Otherwise, no required horizon can be provided. To formalize the derivation of the required horizon, let us first introduce an auxiliary binary function $f^{I}$ to determine whether or not a metric $m$ in scenario $s$ is considered, based on their weights $w_{s}$ and $w_{m}$.

<!-- chunk {"id": "body-0055", "role": "body", "section": "Overall required horizon", "weight": 1.0} -->

The set of horizons that yield a satisfactory value for all metrics and scenarios is given by

<!-- chunk {"id": "body-0056", "role": "body", "section": "Overall required horizon", "weight": 1.0} -->

Then the overall required horizon, if $\mathcal{H}^{r} \neq \varnothing$, is given by

<!-- chunk {"id": "body-0057", "role": "body", "section": "III-C3 Application-specific requirements", "weight": 1.0} -->

General-purpose urban driving. The AV operates between 30km/h and 50km/h, and having the best trade-off between comfort and efficiency is desired.

<!-- chunk {"id": "body-0058", "role": "body", "section": "III-C3 Application-specific requirements", "weight": 1.0} -->

Driverless food delivery. There is no human in the AV, thus emphasis is placed on minimizing delivery time over passenger comfort. Depending on the items being delivered, the AV is estimated to operate at 30, 40, and 50km/h 20, 10, and 70% of the time, respectively.

<!-- chunk {"id": "body-0059", "role": "body", "section": "III-C3 Application-specific requirements", "weight": 1.0} -->

Driverless taxi. Passenger is not in a hurry. The person in the AV does not care about saving time to their destination. The AV operates between 30 and 50km/h.

<!-- chunk {"id": "body-0060", "role": "body", "section": "III-C3 Application-specific requirements", "weight": 1.0} -->

Driverless taxi. Passenger is in a hurry. The person in the AV is in a hurry to get to the airport as soon as possible, even if that means sacrificing comfort. The AV operates at 50km/h whenever possible.

<!-- chunk {"id": "body-0061", "role": "body", "section": "III-C3 Application-specific requirements", "weight": 1.0} -->

With the proposed framework, it is possible to determine the necessary and ideal horizons for each specific application by customizing the weights assigned to each scenario and metric. Note that safety is not factored into this weighting, as it should not be compromised for other secondary objectives like comfort or efficiency. In the considered applications, the suggested weights might look like those outlined in Table III. These weights are flexible and can be modified based on user preferences or the specific application requirements. For instance, if an AV is not expected to operate at speeds of 50km/h, this can be factored in by assigning a zero weight to scenario SC3. Similarly, if a customer receiving a meal delivery (as in application b)) values a smoother ride, potentially at the cost of longer delivery times, this preference can be reflected by adjusting the weights for comfort and efficiency accordingly. It is important to note that the values in Table III are provided merely as examples for the hypothetical applications described and are not necessarily the recommended values.

<!-- chunk {"id": "body-0062", "role": "body", "section": "Results", "weight": 1.0} -->

This section first presents vehicle-level metrics with different prediction horizons. Then we analyze the real-time capabilities of our AV architecture, highlighting how extended prediction and planning horizons can influence overall AV performance negatively due to increased computational demands. Next, the proposed framework is applied to derive prediction requirements for different AV applications. Finally, the main limitations of our methodology and results are highlighted.

<!-- chunk {"id": "body-0063", "role": "body", "section": "IV-A1 Safety", "weight": 1.0} -->

An overview of the pedestrian speeds and trajectory prediction horizons that resulted in a collision is depicted in Fig.. In the figure, a cross indicates a simulation where the AV collided with the pedestrian, and the color the cross denotes the speed of the AV at the moment of collision. As the prediction horizon increases, the number of collisions and the AV collision speed rapidly decrease. SC1 requires a minimum horizon of 0.8 seconds to avoid all collisions^55^5Note that with a horizon of 0.6 seconds, some of the collisions were caused by the pedestrian not reacting to the vehicle, i.e. the vehicle stopped in time but the pedestrian collided on the side. This is a limitation of the simulations, where the pedestrian does not react to the vehicle in these cases.. For SC2 and SC3, all collisions are avoided with at least 1.2 and 1.6 seconds, respectively.

<!-- chunk {"id": "body-0064", "role": "body", "section": "IV-A2 Comfort", "weight": 1.0} -->

An overview of the braking comfort for each scenario is shown in Fig.. The figure shows the percentage of the total braking time that was comfortable, uncomfortable, or highly uncomfortable, as a function of the prediction horizon.

<!-- chunk {"id": "body-0065", "role": "body", "section": "SC1", "weight": 1.0} -->

Highly uncomfortable braking is minimized with a prediction horizon of 7 seconds, occurring less than 0.13% of the time. Already with horizons between 5-9 seconds, this high discomfort stays below 0.8%, increasing slightly for higher horizons due to the decreased update rate of the planner, but it remains under 3.4% up to 15 seconds. With a horizon of 10 seconds, the share of uncomfortable braking is minimized (5%), and the share of comfortable braking is maximized (93.6%). Thus, for SC1 the recommended minimum horizon is 7 seconds. Horizons beyond 10 seconds do not present any additional comfort benefit.

<!-- chunk {"id": "body-0066", "role": "body", "section": "SC2", "weight": 1.0} -->

Highly uncomfortable braking is minimized with a horizon of 7 seconds, occurring less than 1.7% of the time. With 6 seconds, highly uncomfortable braking is already under 1.93%. Beyond 7 seconds it begins to increase again, but it remains under 5% up to 12 seconds. With a horizon of 15 seconds, uncomfortable braking is minimized (10.5%) and comfortable braking is maximized (84.2%). Thus, for SC2 the recommended horizons are between 7 and 15 seconds.

<!-- chunk {"id": "body-0067", "role": "body", "section": "SC3", "weight": 1.0} -->

Highly uncomfortable braking is minimized with a prediction horizon of 10 seconds, occurring about 3.6% of the time. Even with 9 seconds, highly uncomfortable braking is already is under 3.8%. Beyond 10 seconds it begins to increase again, but it remains under 5.9% up to 15 seconds. The share of uncomfortable braking that does not involve highly uncomfortable braking is minimized (13%) with a horizon of 15 seconds, and at the same horizon the comfortable braking is maximized (81%). For optimal comfort in SC3, the optimal horizons are 10-15 seconds.

<!-- chunk {"id": "body-0068", "role": "body", "section": "IV-A3 Efficiency", "weight": 1.0} -->

Fig. presents the average increase in travel time, for all SCs and pedestrian speeds: P1, P2, P3, and an overall average. Generally, the trends are consistent across these scenarios. With slow pedestrian speeds (P1), there is a notable increase in travel delay. The maximum delay ranges from 27.3% to 39.6%, while the minimum delay varies between 19.1% and 22%, depending on the specific scenario. For P2 speeds, the maximum delay is between 18% and 20.5%, and the minimum delay lies between 7.4% and 7.7%. P3 speeds result in the least delay, with maximum values ranging from 4.5% to 7.6% and minimum values from 2.8% to 3.1%.

<!-- chunk {"id": "body-0069", "role": "body", "section": "IV-A3 Efficiency", "weight": 1.0} -->

Overall, the maximum and minimum travel delays are observed with horizons ranging between 1.8 and 2 seconds and between 7 and 8 seconds, respectively, as detailed in Table IV.

<!-- chunk {"id": "body-0070", "role": "body", "section": "IV-B Real-time Execution", "weight": 1.0} -->

The mean and standard deviation of the minimum frequencies achieved by the trajectory planner for the different horizons are shown in Fig.. The mean of the minimum frequencies across runs is consistently kept above 10Hz up to and including 10 seconds of horizon for all three SCs. Due to computational overhead caused by planning for longer horizons, the minimum frequencies drop significantly beyond horizons 7, 6 and 5 seconds for SC1, SC2 and SC3 respectively. This drop in the throughput of trajectory generation has a negative impact on the stability of the AV, and consequently vehicle-level metrics, as shown next analysing the AV's acceleration during one of the simulations with various horizons.

<!-- chunk {"id": "body-0071", "role": "body", "section": "IV-B Real-time Execution", "weight": 1.0} -->

Comfort with increased computational load. Fig. shows an example of the impact that the computational load caused by longer horizons can have on comfort. With 10 seconds of horizon, the planner cannot maintain the configured 20Hz output, dropping somewhere between 12-20Hz when re-planning due to the pedestrian. This drop can cause some minor acceleration peaks, which are still maintained within the comfortable range. However, with a horizon of 20 seconds, the planning frequency drops below 10Hz, which causes significant oscillations in the AV's acceleration and result in uncomfortable braking.

<!-- chunk {"id": "body-0072", "role": "body", "section": "IV-C Application-dependent Prediction Horizons", "weight": 1.0} -->

The required and optimal prediction horizons for each SC and metric combination are summarized in Table V, including the overall horizons considering every SC and metric equally important. Note that some entries are empty, meaning that a required horizon satisfying all metrics in all scenarios could not be found. Recall the four AV applications introduced earlier: a) general-purpose urban driving, b) driverless food delivery, c) driverless taxi where the passenger is not in a hurry, and d) driverless taxi where the passenger is in a hurry. Depending on the specific application, the required and optimal horizons vary significantly. According to the applications considered and the possible weighting scheme introduced in Table III, the required and optimal horizons achieved are shown in Table VI.

<!-- chunk {"id": "body-0073", "role": "body", "section": "IV-C Application-dependent Prediction Horizons", "weight": 1.0} -->

Among the considered applications, driverless food delivery presents the shortest horizon requirements, with a required horizon of 4.4 seconds and an optimal horizon of 7.9 seconds. Driverless taxi applications would benefit from a minimum horizon of 10 seconds, and optimally 14.8 seconds if the passenger is not in a hurry. If the passenger is in a hurry, no horizon exists satisfying all requirements simultaneously, but optimally a horizon of 8.9 seconds would be selected. Finally, for a general-purpose AV operating in environments with crossing pedestrians, the optimal prediction horizon is 11.8 seconds.

<!-- chunk {"id": "body-0074", "role": "body", "section": "IV-D Limitations", "weight": 1.0} -->

The methodology presented in this work, and consequently our results regarding the recommended horizons for prediction models, has three main limitations.

<!-- chunk {"id": "body-0075", "role": "body", "section": "IV-D Limitations", "weight": 1.0} -->

Firstly, our work operates under the assumption of perfect predictions, which is highly unlikely in real-world driving. If prediction accuracy degrades rapidly with increased horizon, the resulting required and optimal horizons will be affected. It is challenging to discern the effect of these inaccuracies without further experiments, as they will depend on the considered vehicle-level metrics. For instance, inaccurate predictions might lead to more aggressive AV behavior, which would negatively affect comfort, while more aggressive acceleration could be beneficial for travel time efficiency.

<!-- chunk {"id": "body-0076", "role": "body", "section": "IV-D Limitations", "weight": 1.0} -->

Secondly, the current study is constrained to scenarios involving crossing pedestrians and the use of a single planner. Given that different scenarios lead to distinct conclusions, it is vital to explore different scenarios and interactions with other RUs. Furthermore, our conclusions are tied to the specific trajectory planner used during this work. Integrating different planners into our study will enhance the generalizability of our conclusions.

<!-- chunk {"id": "body-0077", "role": "body", "section": "IV-D Limitations", "weight": 1.0} -->

Lastly, the potential benefits of very long prediction horizons remain ambiguous due to computational constraints. It remains unclear whether the optimal value of each metric was achieved, and whether this optimal value would remain constant or degrade with longer horizons.

<!-- chunk {"id": "body-0078", "role": "body", "section": "Conclusion", "weight": 1.5} -->

Predicting the future movements of surrounding road users is essential for enhancing the performance of an automated vehicle (AV). However, the degree to which these predictions influence the AV's behavior is unknown.

<!-- chunk {"id": "body-0079", "role": "body", "section": "Conclusion", "weight": 1.5} -->

In this study, we explore how various prediction horizons impact the behavior of an AV in terms of safety, comfort, and efficiency. We simulate trajectory predictions in crossing pedestrian scenarios and test different horizons of to 20 seconds, which are integrated into a state-of-the-art trajectory planner that considers the future motion of other road users.

<!-- chunk {"id": "body-0080", "role": "body", "section": "Conclusion", "weight": 1.5} -->

Our results indicate that a prediction horizon of 1.6 seconds is sufficient for avoiding collisions with crossing pedestrians in urban settings. Optimal travel time efficiency is achieved with longer horizons of 7-8 seconds, while predicting up to 15 seconds improves comfort. Longer horizons incur a higher computational load which negatively affects AV performance.

<!-- chunk {"id": "body-0081", "role": "body", "section": "Conclusion", "weight": 1.5} -->

In this work we show that selecting a single optimal prediction horizon is not possible, as the best choice depends on the desired balance between different metrics and scenarios. To this end, we offer a framework to determine the required and optimal prediction horizons based on the specific AV application. Our study suggests a prediction horizon of 11.8 seconds as a general recommendation for AVs operating in environments with crossing pedestrians.

<!-- chunk {"id": "body-0082", "role": "body", "section": "Conclusion", "weight": 1.5} -->

Future work will focus on extending our methodology to derive accuracy requirements for trajectory prediction models.
