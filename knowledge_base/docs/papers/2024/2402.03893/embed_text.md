## Introduction

Automated vehicles (AVs) are becoming increasingly prevalent, and trajectory prediction of surrounding road users (RUs) is a critical component of these systems, since the AV's decisions will be largely based on the predicted motion of other RUs. When designing a system that accounts for the future motion of surrounding RUs, one must decide how much into the future to predict, i.e. the prediction horizon, which is used to plan an AV trajectory for the same horizon. The choice of prediction horizon can have a significant impact on AV behavior, however, in the development of prediction models the chosen horizon is often an ad hoc decision that depends on practical aspects, such as the length of traces available in the data used to develop these models. Additionally, the typical assessment of prediction models is performed at the subsystem-level, i.e. the prediction module, focusing on predictive accuracy \[(https://arxiv.org/html/2402.03893v2#bib.bibx1)\]. However, with this approach, the impact of predictions on the overall system, namely the AV, remains unclear (Fig (https://arxiv.org/html/2402.03893v2#S1.F1 "Figure 1 ‣ I Introduction ‣ Prediction Horizon Requirements for Automated Driving: Optimizing Safety, Comfort, and Efficiency This work was supported by SAFE-UP under EU’s Horizon 2020 research and innovation programme, grant agreement 861570.")). Consequently, prediction horizon requirements remain undefined.

Figure 1: Typical assessment of trajectory prediction work (left) and our approach (right).

Despite the existence of several works showing that it is beneficial to integrate predictions in motion planning \[(https://arxiv.org/html/2402.03893v2#bib.bibx2)\], there is no clear quantification of the relationship between the prediction horizon and the resulting impact on AV behavior. To establish requirements that a prediction model should adhere to, the impact that predictions have on AV behavior must first be understood. Once we understand this impact, we can determine the ideal prediction horizons that ensure safety and other key aspects like ride comfort and efficiency.

The requirements that predictions must satisfy will be dependent on several other factors, like the type of object being predicted (e.g. vehicle vs. pedestrian), the specific scenario (e.g. lane change in a highway vs a crossing pedestrian), or even user preferences (e.g. a smoother ride is preferred over lower travel time). Hence, these requirements are application-dependent and should adapt to each situation.

To specify prediction requirements, this work first investigates the impact that different prediction horizons have on the safety, comfort and efficiency of an AV. We do this by simulating and integrating predictions into a state of the art optimization-based planner that considers the predicted actions of other RUs \[(https://arxiv.org/html/2402.03893v2#bib.bibx3)\]. Additionally, we introduce a framework to establish both the minimum required and optimal prediction horizons for achieving targeted vehicle performance in specific applications. To show the applicability of our method, we focus on urban driving scenarios involving crossing pedestrians, which are among the most vulnerable participants in traffic \[(https://arxiv.org/html/2402.03893v2#bib.bibx4)\].

Our main contributions are summarized as follows:

Impact analysis of trajectory prediction horizons: We explore the relationship between different prediction horizons and the safety, comfort, and efficiency of AVs in scenarios involving crossing pedestrians.

A methodology to derive application-specific requirements: We introduce a versatile framework to determine prediction horizon requirements tailored to specific AV applications and performance goals. While we demonstrate its application in a limited set of scenarios and performance criteria, the framework is adaptable to other scenarios and criteria.

Guidelines for required and optimal prediction horizons: Using our framework, we provide recommendations for the ideal horizon of trajectory prediction models in AV applications involving crossing pedestrians.

The remainder of this article is structured as follows. Section [II](https://arxiv.org/html/2402.03893v2#S2 "II Related Work ‣ Prediction Horizon Requirements for Automated Driving: Optimizing Safety, Comfort, and Efficiency This work was supported by SAFE-UP under EU’s Horizon 2020 research and innovation programme, grant agreement 861570.") highlights prevalent choices of prediction horizons, related work combining predictions and motion planning, and vehicle-level metrics commonly used to evaluate AV performance. Section [III](https://arxiv.org/html/2402.03893v2#S3 "III Methodology ‣ Prediction Horizon Requirements for Automated Driving: Optimizing Safety, Comfort, and Efficiency This work was supported by SAFE-UP under EU’s Horizon 2020 research and innovation programme, grant agreement 861570.") introduces our proposed methodology to derive horizon requirements. Section [IV](https://arxiv.org/html/2402.03893v2#S4 "IV Results ‣ Prediction Horizon Requirements for Automated Driving: Optimizing Safety, Comfort, and Efficiency This work was supported by SAFE-UP under EU’s Horizon 2020 research and innovation programme, grant agreement 861570.") summarizes the results and highlights limitations of this study. Finally, Section [V](https://arxiv.org/html/2402.03893v2#S5 "V Conclusion ‣ Prediction Horizon Requirements for Automated Driving: Optimizing Safety, Comfort, and Efficiency This work was supported by SAFE-UP under EU’s Horizon 2020 research and innovation programme, grant agreement 861570.") concludes the work and outlines future improvements.

## Related Work

This section offers a review of prevalent choices of prediction horizon. Subsequently, we analyze works considering predictions and motion planning jointly. Finally, we delve into the metrics that can be used to evaluate AV performance.

### II-A Choosing a Prediction Horizon

The field of trajectory prediction is dominated by machine learning methods nowadays \[(https://arxiv.org/html/2402.03893v2#bib.bibx1)\]. The development of these methods relies on datasets with pre-recorded RU trajectories, segmented in two parts with an observation and a prediction horizon, i.e. the portion of the trajectory available before prediction, and the portion to be predicted, respectively.

Table [I](https://arxiv.org/html/2402.03893v2#S2.T1 "TABLE I ‣ II-A Choosing a Prediction Horizon ‣ II Related Work ‣ Prediction Horizon Requirements for Automated Driving: Optimizing Safety, Comfort, and Efficiency This work was supported by SAFE-UP under EU’s Horizon 2020 research and innovation programme, grant agreement 861570.") presents an overview of popular datasets commonly used for trajectory prediction research. Methods using these datasets seem to be conditioned on either (i) the length of the traces contained in the dataset, or (ii) popular choice of horizons for a specific dataset used in previous work, which facilitates comparison of a new method without the need to re-implement previous ones.

TABLE I: Popular trajectory prediction datasets and associated (maximum) prediction horizons reported

Since the choice of prediction horizon is arbitrary and independent from AV performance metrics, predictive accuracy is often analyzed at various horizons to obtain a better coverage of a model's capabilities. For instance, methods working with UCY, ETH and SSD typically report performance at a horizon of 4.8 seconds \[(https://arxiv.org/html/2402.03893v2#bib.bibx7), (https://arxiv.org/html/2402.03893v2#bib.bibx8), (https://arxiv.org/html/2402.03893v2#bib.bibx9)\], but some works also report their performance at 3.2 seconds \[(https://arxiv.org/html/2402.03893v2#bib.bibx10)\]. Methods evaluated on NGSIM, highD, and exiD report from 1 up to 5 seconds \[(https://arxiv.org/html/2402.03893v2#bib.bibx11), (https://arxiv.org/html/2402.03893v2#bib.bibx12), (https://arxiv.org/html/2402.03893v2#bib.bibx13)\]. Reporting the performance at different horizons presents a more complete assessment of a model's predictive capabilities, but it remains unclear how its predictions ultimately affect AV behavior and what the required and optimal horizons are.

### II-B Evaluating Predictions & their Impact on Vehicle Behavior

Predictions are mainly evaluated in terms of geometric accuracy with metrics such as minimum average displacement error, and minimum final displacement error \[(https://arxiv.org/html/2402.03893v2#bib.bibx14)\], often disregarding their associated uncertainty and the impact they have on the behavior of the vehicle.

The authors of \[(https://arxiv.org/html/2402.03893v2#bib.bibx15)\] take a critical look at current evaluation practices and conclude that trajectory prediction metrics do not reflect well the impact they have on AV behavior. To address this limitation, the authors of \[(https://arxiv.org/html/2402.03893v2#bib.bibx16)\] advocate for a novel planning-aware metric which better reflects performance in AVs, weighting the error of each prediction according to the impact it would have on the planned AV trajectory.

Other than lacking evaluation practices, the authors of \[(https://arxiv.org/html/2402.03893v2#bib.bibx17)\] raise concern regarding the currently accepted output representation of predictions for downstream integration, since a majority of planning and control algorithms reason about system dynamics instead of the current prediction representation, i.e. a sequence of positions. Accordingly, they propose a dynamical system representation that allows the planning optimizer to simultaneously explore different AV controls and their effect on the predictions of surrounding RU's. Although not as efficiently as proposed in \[(https://arxiv.org/html/2402.03893v2#bib.bibx17)\], the current representation allows incorporating predictions in motion planning \[(https://arxiv.org/html/2402.03893v2#bib.bibx18)\], and conversely use the AV's planned trajectory to influence predictions of surrounding RUs \[(https://arxiv.org/html/2402.03893v2#bib.bibx19)\].

Despite the existence of numerous studies coupling predictions with planning for improved AV performance, there is a noticeable gap in research quantifying these improvements \[(https://arxiv.org/html/2402.03893v2#bib.bibx2)\]. A significant aspect of uncertainty involves determining the necessary and ideal prediction horizons. That is, the shortest horizon that ensures acceptable AV performance, and the horizon that optimizes AV performance. Short horizons might not allow enough time to react accordingly, and the full benefits of predictions might not be realized. Conversely, excessively long horizons could lead to overly cautious behavior or increased computational demands, potentially diminishing AV performance.

### II-C Vehicle-level Metrics

To assess the impact of predictions on AV behavior, vehicle-level performance metrics are needed. AV performance is often measured in terms of safety, comfort, and efficiency \[(https://arxiv.org/html/2402.03893v2#bib.bibx20), (https://arxiv.org/html/2402.03893v2#bib.bibx21), (https://arxiv.org/html/2402.03893v2#bib.bibx22)\].

### II-C1 Safety

The potential to increase safety is one of the main reasons AVs are a desirable technology. According to the National Highway Traffic Safety Administration \[(https://arxiv.org/html/2402.03893v2#bib.bibx23)\], human error is a contributing factor in 94% of crashes, and it is expected that AVs will be able to prevent such crashes \[(https://arxiv.org/html/2402.03893v2#bib.bibx20)\]. Consequently, one of the most popular metrics to assess safety is collision rate, often compared to human-driven vehicles \[(https://arxiv.org/html/2402.03893v2#bib.bibx24)\]. Nonetheless, there are other relevant metrics used to assess the safety of an AV, such as disengagements (i.e. the number of times a human driver needed to take control of the vehicle) \[(https://arxiv.org/html/2402.03893v2#bib.bibx25)\], and safety violations \[(https://arxiv.org/html/2402.03893v2#bib.bibx26)\].

### II-C2 Comfort

The comfort of AVs is commonly measured using ISO standard 2631 \[(https://arxiv.org/html/2402.03893v2#bib.bibx27)\], which provides approaches for categorizing comfort levels of vibration and shock motion at frequencies similar to those encountered in a vehicle. However, a recent study investigated empirically the relationship between a vehicle's acceleration and jerk, and the discomfort experienced by passengers, concluding that the standard models in ISO 2631 may not effectively describe the comfort of motions experienced in a vehicle \[(https://arxiv.org/html/2402.03893v2#bib.bibx21)\]. At the same time, they concluded that acceleration is the main descriptor of (dis)comfort, and derived acceleration thresholds for seven different ranges of comfort, from excellent to terrible.

### II-C3 Efficiency

Efficiency of an AV can be considered with respect to several aspects. A commonly used metric for measuring the efficiency of an AV is fuel efficiency \[(https://arxiv.org/html/2402.03893v2#bib.bibx28)\], which in turn can help reduce emissions \[(https://arxiv.org/html/2402.03893v2#bib.bibx29)\]. Efficiency is also often measured in terms of travel time \[(https://arxiv.org/html/2402.03893v2#bib.bibx30)\], which can be considered a deciding factor for choosing a mode of transport \[(https://arxiv.org/html/2402.03893v2#bib.bibx31)\].

## Methodology

This section describes our methodology to derive prediction horizon requirements. Fig. (https://arxiv.org/html/2402.03893v2#S3.F2 "Figure 2 ‣ III Methodology ‣ Prediction Horizon Requirements for Automated Driving: Optimizing Safety, Comfort, and Efficiency This work was supported by SAFE-UP under EU’s Horizon 2020 research and innovation programme, grant agreement 861570.") presents an overview of this process. First, relevant scenarios are selected based on accidentology and pedestrian walking studies. Next, typical modules of an AV are integrated in a simulation environment considering varying prediction horizons of surrounding RUs. Finally, combining vehicle-level performance when using different horizons and the intended application operational design domain (ODD), horizon requirements are derived.

Figure 2: Methodology to derive prediction horizon requirements.

### III-A Scenario Selection

Accidentology studies highlight that vulnerable RUs such as pedestrians are among the most at-risk traffic participants in urban environments \[(https://arxiv.org/html/2402.03893v2#bib.bibx4)\]. Specifically, the most frequently occurring accident is a pedestrian crossing from the right without any sight obstruction. This group of accidents makes up 22.8% of car-to-pedestrian collisions, and it is the most lethal collision, amounting to 23.2% of all killed or severely injured pedestrians \[(https://arxiv.org/html/2402.03893v2#bib.bibx4)\]. In these accidents, vehicle speed ranged from 26 to 48 km/h, and pedestrian speeds are unknown. This group of accidents is selected as the basis of our study.

We investigate the impact of predictions on three similar scenario categories (SCs): SC1, SC2, and SC3, where the AV speeds are set to 30, 40 and 50km/h respectively. For the three SCs, one hundred different pedestrian speeds are sampled randomly from a normal distribution describing pedestrian walking speeds, with mean 1.34m/s and standard deviation 0.37m/s \[(https://arxiv.org/html/2402.03893v2#bib.bibx32)\]. Thus, with 3 SCs, 22 different horizons, and 100 pedestrian speeds, a total of 6600 runs are executed.

The scenarios are set up such that if the AV does not react to the pedestrian, a front collision occurs in the middle of the AV when the pedestrian is walking at the mean speed of 1.34m/s. Consequently, for pedestrian speeds that significantly deviate from this value, there would be no collision even when the AV does not react to the pedestrian, due to the pedestrian walking too slow or too fast (Fig. (https://arxiv.org/html/2402.03893v2#S3.F3 "Figure 3 ‣ III-A Scenario Selection ‣ III Methodology ‣ Prediction Horizon Requirements for Automated Driving: Optimizing Safety, Comfort, and Efficiency This work was supported by SAFE-UP under EU’s Horizon 2020 research and innovation programme, grant agreement 861570.")). We refer to these three groups of pedestrian speeds as follows:

Slow pedestrian speeds, such that the AV passes the pedestrian collision-free before it crosses the road.

Pedestrian speeds that result in a collision when the AV does not react to the pedestrian.

Fast pedestrian speeds, such that the AV passes the pedestrian collision-free after it has crossed the road.

Figure 3: Histogram of pedestrian speeds used during this study and corresponding scenario when the vehicle does not react to the pedestrian.

### III-B Automated Driving Functions

### III-B1 Perception and world modeling

Analyzing the impact of perception and world modeling performance on vehicle performance falls out of the scope of this study. Consequently, factors such as sensor noise and perception-related challenges are not considered. In our simulations, we gather data on nearby objects, such as road lanes and other RUs, directly from the simulator.

### III-B2 Predictions

A wide range of methods exists for predicting the trajectories of RUs \[(https://arxiv.org/html/2402.03893v2#bib.bibx1), (https://arxiv.org/html/2402.03893v2#bib.bibx33)\], each with distinct advantages and drawbacks. Opting for a single prediction method could skew our results in favor of that method. Additionally, trajectory prediction methods are rapidly evolving and becoming more accurate. Thus, if using currently existing prediction methods to derive their requirements, these requirements could become obsolete as the field evolves. To circumvent this, our approach involves simulating an ideal scenario, where predictions are flawless, to find the horizons that would provide the most benefits if predictions were perfect. Different time horizons of these ideal predictions are then provided to the planner to find the necessary and most beneficial horizons. A thorough investigation into the effects of prediction inaccuracies and the subsequent derivation of accuracy requirements is reserved for future work. To limit simulation times and have a good coverage of the search space, we consider horizons

and the achieved performance with horizons that are not in $\mathcal{H}$ is calculated by linear interpolation.

### III-B3 Planning & Control

To evaluate the effect of trajectory prediction on AV behavior, a state of the art planner is integrated in our simulations \[(https://arxiv.org/html/2402.03893v2#bib.bibx3)\]. This planner considers both the road infrastructure and the predicted positions of surrounding objects. It uses artificial potential-based risk fields within the cost function of a model-predictive control problem to find a trajectory that minimizes risk while progressing towards the AV's intended destination. For a more comprehensive description of this planner, we defer the reader to \[(https://arxiv.org/html/2402.03893v2#bib.bibx3)\].

### III-C Performance Assessment

In this section, we outline our methodology for AV performance assessment and derivation of prediction horizon requirements. First, we present the vehicle-level performance metrics employed in our assessment. Subsequently, the proposed framework designed to determine both required and optimal prediction horizons is introduced. Lastly, we illustrate the versatility of this framework by introducing four distinct use cases to demonstrate its application across various AV settings tailored to specific operational purposes.

### III-C1 Vehicle-level Performance

To assess the impact of prediction horizons on AV behavior, we measure safety, comfort and efficiency as described in this section. Additionally, we analyze the real-time capabilities of our system.

Let $f^{m}{(h,s)}$ denote the value achieved for vehicle-level metric $m$ and SC $s$ when using a prediction horizon $h$. Each of these metrics is defined as:

### Safety

The percentage of runs that are collision-free. Since we are mainly interested in achieving collision-free runs, we do not weigh in the AV's speed at impact, but we visualize it for illustrative purposes.

### Comfort

We adapt the categorization of (dis)comfort based on acceleration presented in \[(https://arxiv.org/html/2402.03893v2#bib.bibx21)\] in combination with \[(https://arxiv.org/html/2402.03893v2#bib.bibx34)\] and consider deceleration values as comfortable, uncomfortable, and highly uncomfortable, as shown in Table [II](https://arxiv.org/html/2402.03893v2#S3.T2 "TABLE II ‣ Comfort ‣ III-C1 Vehicle-level Performance ‣ III-C Performance Assessment ‣ III Methodology ‣ Prediction Horizon Requirements for Automated Driving: Optimizing Safety, Comfort, and Efficiency This work was supported by SAFE-UP under EU’s Horizon 2020 research and innovation programme, grant agreement 861570."). Considering the time that the vehicle is decelerating, we report the percentage of time spent on each comfort category. The resulting comfort in SC $s$ when using a prediction horizon $h$, $f^{\text{𝑐𝑜𝑚𝑓𝑜𝑟𝑡}}{(h,s)}$, is the percentage of time spent on the comfortable category.

TABLE II: Deceleration thresholds for (dis)comfort level

### Efficiency

We investigate efficiency in terms of travel time, and calculate the relative increase of travel time, $\Delta t$, for each prediction horizon. That is, if $t_{b}{(s)}$ is the time it takes the vehicle to complete the route in scenario $s$ without a pedestrian crossing the road, and $t{(h,s)}$ is the time with the crossing pedestrian and using prediction horizon $h$, then

To keep the interpretation of efficiency consistent with other metrics (i.e. within a positive range, and where a higher value of the metric denotes better performance), the final efficiency is calculated as

### Real-time execution

The ability to operate at a high frequency is not one of the goals of this study. However, with higher prediction and planning horizons, the load on the trajectory planner impeded its operation at the desired frequency^11^1All simulations are executed on a desktop computer with an AMD Ryzen 9 5900X processor, GeForce RTX 3070 Ti GPU, and 64GB DDR4 RAM., which had an impact on comfort and efficiency. Thus, we evaluate the frequency at which the planner updates its trajectories^22^2Measured by the rate of new trajectory arrivals on the corresponding ROS topic, averaged over a 21-sample sliding window.. For each simulation, we record the minimum frequency, and then report the mean and standard deviation of these values across the 100 runs for each horizon.

### III-C2 Deriving Required and Optimal Prediction Horizons

Different scenarios and metrics can lead to significantly different horizon requirements. Thus, concluding on a preferred horizon is not trivial. This section describes a methodology to derive the preferred horizon by combining multiple system-level (i.e. vehicle) metrics in a variety of scenarios.

In our simulations, all possible vehicle-level metrics are $\mathcal{M} = {\{\text{𝑠𝑎𝑓𝑒𝑡𝑦},\text{𝑐𝑜𝑚𝑓𝑜𝑟𝑡},\text{𝑒𝑓𝑓𝑖𝑐𝑖𝑒𝑛𝑐𝑦}\}}$, all possible SCs are $\mathcal{S} = {\{\textit{SC1},\textit{SC2},\textit{SC3}\}}$, and all possible horizons are $\mathcal{H}$ as in ((https://arxiv.org/html/2402.03893v2#S3.E1 "1 ‣ III-B2 Predictions ‣ III-B Automated Driving Functions ‣ III Methodology ‣ Prediction Horizon Requirements for Automated Driving: Optimizing Safety, Comfort, and Efficiency This work was supported by SAFE-UP under EU’s Horizon 2020 research and innovation programme, grant agreement 861570.")). When considering a collection of metrics $M \subseteq \mathcal{M}$ and SCs $S \subseteq \mathcal{S}$, we aim to find a required and an optimal horizon, $r_{M}^{S}$, and $o_{M}^{S}$, such that horizon $r_{M}^{S}$ yields satisfactory AV performance for all metrics and scenarios considered, and horizon $o_{M}^{S}$ yields the best value of each metric in every scenario. If that is not possible, we should find the horizon that yields the best trade-off, as explained later in this section.

When considering individual metrics, our definitions of satisfactory and optimal vary depending on the metric:

When considering only safety, i.e. $M = {\{\text{𝑠𝑎𝑓𝑒𝑡𝑦}\}}$, $r_{M}^{S} = o_{M}^{S}$ is the shortest horizon that maximizes safety. We aim at zero collisions, and anything else is not considered satisfactory.

If $M = {\{\text{𝑐𝑜𝑚𝑓𝑜𝑟𝑡}\}}$, $o_{M}^{S}$ is the shortest horizon that maximizes the share of comfortable braking, and $r_{M}^{S}$ is the horizon that minimizes the share of highly uncomfortable braking.

If $M = {\{\text{𝑒𝑓𝑓𝑖𝑐𝑖𝑒𝑛𝑐𝑦}\}}$, $o_{M}^{S}$ is the shortest horizon that maximizes efficiency, and $r_{M}^{S}$ is the shortest satisficing \[(https://arxiv.org/html/2402.03893v2#bib.bibx35)\] horizon, that is, the horizon achieving an efficiency that is within 15% of the optimal efficiency^33^3The threshold for the satisficing, i.e. near optimal "good enough" \[(https://arxiv.org/html/2402.03893v2#bib.bibx35)\], horizon is determined by visual inspection, selecting the horizon at which efficiency begins to converge. All the selected horizons yield an efficiency that is within 15% of the optimal value..

Different metrics may lead to conflicting required and optimal horizons; thus, a procedure is needed to find the overall optimal and required horizons when considering multiple potentially conflicting objectives and scenarios.

### Overall optimal horizon

When considering multiple objectives and scenarios to conclude on the overall optimal horizon, different situations are possible. Consider as an example the two situations shown in Fig. (https://arxiv.org/html/2402.03893v2#S3.F4 "Figure 4 ‣ Overall optimal horizon ‣ III-C2 Deriving Required and Optimal Prediction Horizons ‣ III-C Performance Assessment ‣ III Methodology ‣ Prediction Horizon Requirements for Automated Driving: Optimizing Safety, Comfort, and Efficiency This work was supported by SAFE-UP under EU’s Horizon 2020 research and innovation programme, grant agreement 861570."), where the value of two metrics $m_{1}$ and $m_{2}$ are shown as a function of the prediction horizon. For simplicity, different SCs are left out of the example. In the first situation (left), both metrics $m_{1}$ and $m_{2}$ converge to their optimal values at horizons $o_{m_{1}}$ and $o_{m_{2}}$. In this case, we would choose the optimal horizon, $o_{M}$, to be the same as $o_{m_{2}}$, as this is the minimum horizon with which all considered metrics achieve their optimal value.

Figure 4: Example of two situations yielding a different overall optimal horizon. Left: it is possible to choose one of the optimal horizons without negatively affecting any metric. Right: it is not possible to choose an optimal horizon without negatively affecting some metric.

In the second example (Fig. (https://arxiv.org/html/2402.03893v2#S3.F4 "Figure 4 ‣ Overall optimal horizon ‣ III-C2 Deriving Required and Optimal Prediction Horizons ‣ III-C Performance Assessment ‣ III Methodology ‣ Prediction Horizon Requirements for Automated Driving: Optimizing Safety, Comfort, and Efficiency This work was supported by SAFE-UP under EU’s Horizon 2020 research and innovation programme, grant agreement 861570."), right), however, $m_{1}$ is negatively affected by longer horizons, therefore choosing $o_{m_{2}}$ as the optimal horizon is no longer possible. Since it is not possible to choose a horizon that leads to the optimal value across all metrics and scenarios, we should find the best trade-off. The best trade-off is subjective and depends on the relative importance given to different metrics and scenarios. To find the horizon that best balances all considered metrics across all considered SCs, the cost function $f^{C}$ is introduced as

where $w_{s}$ and $w_{m}$ are weighting factors to balance the importance of each SC and metric. Recall that $f^{m}{(h,s)}$ denotes the value of metric $m$ achieved in scenario $s$ when using a prediction horizon $h$, thus, $f^{m}{(o_{m}^{s},s)}$ denotes the best value of metric $m$ in scenario $s$, achieved with horizon $o_{m}^{s}$. Additionally, note that ${\overset{\sim}{f}}^{m}$ is used instead of $f^{m}$, which denotes a normalized version of $f^{m}$ to ensure all metric values are in a common range^44^4In our case, between 0 and 100, where 0 maps to the worst value of the metric achieved in all simulations, and 100 maps to the best. in order to provide a more intuitive weighting scheme.

The optimal horizon over all scenario categories $S$ and metrics $M$, $o_{M}^{S}$, is then calculated by obtaining the horizon that minimizes deviation from all optimal metric values for each scenario $s \in S$ and metric $m \in M$. In case the resulting horizon is not sufficient to guarantee safety, then the horizon that maximizes safety is used instead. That is,

### Overall required horizon

A different approach is taken to find the overall required prediction horizon. The reason for this deviation is illustrated with an example. Consider the two situations shown in Fig. (https://arxiv.org/html/2402.03893v2#S3.F5 "Figure 5 ‣ Overall required horizon ‣ III-C2 Deriving Required and Optimal Prediction Horizons ‣ III-C Performance Assessment ‣ III Methodology ‣ Prediction Horizon Requirements for Automated Driving: Optimizing Safety, Comfort, and Efficiency This work was supported by SAFE-UP under EU’s Horizon 2020 research and innovation programme, grant agreement 861570.").

Figure 5: Example of two situations yielding a different overall required horizon. Left: it is possible to choose a horizon that satisfies the required value of all metrics. Right: it is not possible to choose a horizon that satisfies the required value of all metrics.

In the first example (left), horizons beyond the required $r_{m_{1}}$ and $r_{m_{2}}$ all yield a satisfactory value for metrics $m_{1}$ and $m_{2}$, respectively, denoted in the figure by the highlighted rectangular area. Similarly to the example from Fig. (https://arxiv.org/html/2402.03893v2#S3.F4 "Figure 4 ‣ Overall optimal horizon ‣ III-C2 Deriving Required and Optimal Prediction Horizons ‣ III-C Performance Assessment ‣ III Methodology ‣ Prediction Horizon Requirements for Automated Driving: Optimizing Safety, Comfort, and Efficiency This work was supported by SAFE-UP under EU’s Horizon 2020 research and innovation programme, grant agreement 861570.") (left), in this case the overall minimum required horizon, $r_{M}$, can simply be chosen the same as $r_{m_{2}}$. However, in Fig. (https://arxiv.org/html/2402.03893v2#S3.F5 "Figure 5 ‣ Overall required horizon ‣ III-C2 Deriving Required and Optimal Prediction Horizons ‣ III-C Performance Assessment ‣ III Methodology ‣ Prediction Horizon Requirements for Automated Driving: Optimizing Safety, Comfort, and Efficiency This work was supported by SAFE-UP under EU’s Horizon 2020 research and innovation programme, grant agreement 861570.") (right), there is no horizon that yields a satisfactory value for all metrics simultaneously. If this value does not exist, the best alternative is to use the horizon achieving the best trade-off across all metrics and scenarios, the optimal horizon $o_{M}^{S}$ in ((https://arxiv.org/html/2402.03893v2#S3.E5 "5 ‣ Overall optimal horizon ‣ III-C2 Deriving Required and Optimal Prediction Horizons ‣ III-C Performance Assessment ‣ III Methodology ‣ Prediction Horizon Requirements for Automated Driving: Optimizing Safety, Comfort, and Efficiency This work was supported by SAFE-UP under EU’s Horizon 2020 research and innovation programme, grant agreement 861570.")), or the system designer should review the previously specified requirements for each vehicle-level metric.

Thus, the overall required horizon is calculated as the shortest horizon that yields a satisfactory value for all considered metrics and scenarios, if it exists. Otherwise, no required horizon can be provided. To formalize the derivation of the required horizon, let us first introduce an auxiliary binary function $f^{I}$ to determine whether or not a metric $m$ in scenario $s$ is considered, based on their weights $w_{s}$ and $w_{m}$. We shall consider it if both weights are nonzero:

The set of horizons that yield a satisfactory value for all metrics and scenarios is given by

Then the overall required horizon, if $\mathcal{H}^{r} \neq \varnothing$, is given by

Figure 6: Collisions and the AV’s speed at impact for different prediction horizons and pedestrian speeds. An “x” denotes a collision, and its color indicates the AV speed at the moment of collision. A blue “.” denotes a run without a collision.

Figure 7: Percentage of time spent on different levels of comfort during braking for different horizons.

### III-C3 Application-specific requirements

To exemplify the relevance of the intended application, and the versatility of our framework, let us consider four fictional applications:

General-purpose urban driving. The AV operates between 30km/h and 50km/h, and having the best trade-off between comfort and efficiency is desired.

Driverless food delivery. There is no human in the AV, thus emphasis is placed on minimizing delivery time over passenger comfort. Depending on the items being delivered, the AV is estimated to operate at 30, 40, and 50km/h 20, 10, and 70% of the time, respectively.

Driverless taxi. Passenger is not in a hurry. The person in the AV does not care about saving time to their destination. The AV operates between 30 and 50km/h.

Driverless taxi. Passenger is in a hurry. The person in the AV is in a hurry to get to the airport as soon as possible, even if that means sacrificing comfort. The AV operates at 50km/h whenever possible.

With the proposed framework, it is possible to determine the necessary and ideal horizons for each specific application by customizing the weights assigned to each scenario and metric. Note that safety is not factored into this weighting, as it should not be compromised for other secondary objectives like comfort or efficiency. In the considered applications, the suggested weights might look like those outlined in Table [III](https://arxiv.org/html/2402.03893v2#S3.T3 "TABLE III ‣ III-C3 Application-specific requirements ‣ III-C Performance Assessment ‣ III Methodology ‣ Prediction Horizon Requirements for Automated Driving: Optimizing Safety, Comfort, and Efficiency This work was supported by SAFE-UP under EU’s Horizon 2020 research and innovation programme, grant agreement 861570."). These weights are flexible and can be modified based on user preferences or the specific application requirements. For instance, if an AV is not expected to operate at speeds of 50km/h, this can be factored in by assigning a zero weight to scenario SC3. Similarly, if a customer receiving a meal delivery (as in application b)) values a smoother ride, potentially at the cost of longer delivery times, this preference can be reflected by adjusting the weights for comfort and efficiency accordingly. It is important to note that the values in Table [III](https://arxiv.org/html/2402.03893v2#S3.T3 "TABLE III ‣ III-C3 Application-specific requirements ‣ III-C Performance Assessment ‣ III Methodology ‣ Prediction Horizon Requirements for Automated Driving: Optimizing Safety, Comfort, and Efficiency This work was supported by SAFE-UP under EU’s Horizon 2020 research and innovation programme, grant agreement 861570.") are provided merely as examples for the hypothetical applications described and are not necessarily the recommended values.

TABLE III: Possible metric and scenario weights for each application

## Results

This section first presents vehicle-level metrics with different prediction horizons. Then we analyze the real-time capabilities of our AV architecture, highlighting how extended prediction and planning horizons can influence overall AV performance negatively due to increased computational demands. Next, the proposed framework is applied to derive prediction requirements for different AV applications. Finally, the main limitations of our methodology and results are highlighted.

### IV-A Vehicle-level Performance Metrics

### IV-A1 Safety

An overview of the pedestrian speeds and trajectory prediction horizons that resulted in a collision is depicted in Fig. (https://arxiv.org/html/2402.03893v2#S3.F6 "Figure 6 ‣ Overall required horizon ‣ III-C2 Deriving Required and Optimal Prediction Horizons ‣ III-C Performance Assessment ‣ III Methodology ‣ Prediction Horizon Requirements for Automated Driving: Optimizing Safety, Comfort, and Efficiency This work was supported by SAFE-UP under EU’s Horizon 2020 research and innovation programme, grant agreement 861570."). In the figure, a cross indicates a simulation where the AV collided with the pedestrian, and the color the cross denotes the speed of the AV at the moment of collision. As the prediction horizon increases, the number of collisions and the AV collision speed rapidly decrease. SC1 requires a minimum horizon of 0.8 seconds to avoid all collisions^55^5Note that with a horizon of 0.6 seconds, some of the collisions were caused by the pedestrian not reacting to the vehicle, i.e. the vehicle stopped in time but the pedestrian collided on the side. This is a limitation of the simulations, where the pedestrian does not react to the vehicle in these cases.. For SC2 and SC3, all collisions are avoided with at least 1.2 and 1.6 seconds, respectively.

### IV-A2 Comfort

An overview of the braking comfort for each scenario is shown in Fig. (https://arxiv.org/html/2402.03893v2#S3.F7 "Figure 7 ‣ Overall required horizon ‣ III-C2 Deriving Required and Optimal Prediction Horizons ‣ III-C Performance Assessment ‣ III Methodology ‣ Prediction Horizon Requirements for Automated Driving: Optimizing Safety, Comfort, and Efficiency This work was supported by SAFE-UP under EU’s Horizon 2020 research and innovation programme, grant agreement 861570."). The figure shows the percentage of the total braking time that was comfortable, uncomfortable, or highly uncomfortable, as a function of the prediction horizon.

### SC1

Highly uncomfortable braking is minimized with a prediction horizon of 7 seconds, occurring less than 0.13% of the time. Already with horizons between 5-9 seconds, this high discomfort stays below 0.8%, increasing slightly for higher horizons due to the decreased update rate of the planner, but it remains under 3.4% up to 15 seconds. With a horizon of 10 seconds, the share of uncomfortable braking is minimized (5%), and the share of comfortable braking is maximized (93.6%). Thus, for SC1 the recommended minimum horizon is 7 seconds. Horizons beyond 10 seconds do not present any additional comfort benefit.

### SC2

Highly uncomfortable braking is minimized with a horizon of 7 seconds, occurring less than 1.7% of the time. With 6 seconds, highly uncomfortable braking is already under 1.93%. Beyond 7 seconds it begins to increase again, but it remains under 5% up to 12 seconds. With a horizon of 15 seconds, uncomfortable braking is minimized (10.5%) and comfortable braking is maximized (84.2%). Thus, for SC2 the recommended horizons are between 7 and 15 seconds.

### SC3

Highly uncomfortable braking is minimized with a prediction horizon of 10 seconds, occurring about 3.6% of the time. Even with 9 seconds, highly uncomfortable braking is already is under 3.8%. Beyond 10 seconds it begins to increase again, but it remains under 5.9% up to 15 seconds. The share of uncomfortable braking that does not involve highly uncomfortable braking is minimized (13%) with a horizon of 15 seconds, and at the same horizon the comfortable braking is maximized (81%). For optimal comfort in SC3, the optimal horizons are 10-15 seconds.

### IV-A3 Efficiency

Fig. (https://arxiv.org/html/2402.03893v2#S4.F8 "Figure 8 ‣ IV-A3 Efficiency ‣ IV-A Vehicle-level Performance Metrics ‣ IV Results ‣ Prediction Horizon Requirements for Automated Driving: Optimizing Safety, Comfort, and Efficiency This work was supported by SAFE-UP under EU’s Horizon 2020 research and innovation programme, grant agreement 861570.") presents the average increase in travel time, for all SCs and pedestrian speeds: P1, P2, P3, and an overall average. Generally, the trends are consistent across these scenarios. With slow pedestrian speeds (P1), there is a notable increase in travel delay. The maximum delay ranges from 27.3% to 39.6%, while the minimum delay varies between 19.1% and 22%, depending on the specific scenario. For P2 speeds, the maximum delay is between 18% and 20.5%, and the minimum delay lies between 7.4% and 7.7%. P3 speeds result in the least delay, with maximum values ranging from 4.5% to 7.6% and minimum values from 2.8% to 3.1%.

Overall, the maximum and minimum travel delays are observed with horizons ranging between 1.8 and 2 seconds and between 7 and 8 seconds, respectively, as detailed in Table [IV](https://arxiv.org/html/2402.03893v2#S4.T4 "TABLE IV ‣ IV-A3 Efficiency ‣ IV-A Vehicle-level Performance Metrics ‣ IV Results ‣ Prediction Horizon Requirements for Automated Driving: Optimizing Safety, Comfort, and Efficiency This work was supported by SAFE-UP under EU’s Horizon 2020 research and innovation programme, grant agreement 861570.").

TABLE IV: Maximum and minimum mean travel time delay and respective prediction horizons

Figure 8: Mean travel time increase with different horizons for the three pedestrian speed groups, and overall.

### IV-B Real-time Execution

The mean and standard deviation of the minimum frequencies achieved by the trajectory planner for the different horizons are shown in Fig. (https://arxiv.org/html/2402.03893v2#S4.F9 "Figure 9 ‣ IV-B Real-time Execution ‣ IV Results ‣ Prediction Horizon Requirements for Automated Driving: Optimizing Safety, Comfort, and Efficiency This work was supported by SAFE-UP under EU’s Horizon 2020 research and innovation programme, grant agreement 861570."). The mean of the minimum frequencies across runs is consistently kept above 10Hz up to and including 10 seconds of horizon for all three SCs. Due to computational overhead caused by planning for longer horizons, the minimum frequencies drop significantly beyond horizons 7, 6 and 5 seconds for SC1, SC2 and SC3 respectively. This drop in the throughput of trajectory generation has a negative impact on the stability of the AV, and consequently vehicle-level metrics, as shown next analysing the AV's acceleration during one of the simulations with various horizons.

Figure 9: Update rate of the trajectory planner for each prediction horizon.

Comfort with increased computational load. Fig. (https://arxiv.org/html/2402.03893v2#S4.F10 "Figure 10 ‣ IV-B Real-time Execution ‣ IV Results ‣ Prediction Horizon Requirements for Automated Driving: Optimizing Safety, Comfort, and Efficiency This work was supported by SAFE-UP under EU’s Horizon 2020 research and innovation programme, grant agreement 861570.") shows an example of the impact that the computational load caused by longer horizons can have on comfort. With 10 seconds of horizon, the planner cannot maintain the configured 20Hz output, dropping somewhere between 12-20Hz when re-planning due to the pedestrian. This drop can cause some minor acceleration peaks, which are still maintained within the comfortable range. However, with a horizon of 20 seconds, the planning frequency drops below 10Hz, which causes significant oscillations in the AV's acceleration and result in uncomfortable braking.

Figure 10: Example of the impact of increased computational load on the resulting acceleration due longer planning horizons. The green, yellow and red background on the top plot indicate the thresholds for comfortable, uncomfortable, and highly uncomfortable

### IV-C Application-dependent Prediction Horizons

The required and optimal prediction horizons for each SC and metric combination are summarized in Table [V](https://arxiv.org/html/2402.03893v2#S4.T5 "TABLE V ‣ IV-C Application-dependent Prediction Horizons ‣ IV Results ‣ Prediction Horizon Requirements for Automated Driving: Optimizing Safety, Comfort, and Efficiency This work was supported by SAFE-UP under EU’s Horizon 2020 research and innovation programme, grant agreement 861570."), including the overall horizons considering every SC and metric equally important. Note that some entries are empty, meaning that a required horizon satisfying all metrics in all scenarios could not be found. Recall the four AV applications introduced earlier: a) general-purpose urban driving, b) driverless food delivery, c) driverless taxi where the passenger is not in a hurry, and d) driverless taxi where the passenger is in a hurry. Depending on the specific application, the required and optimal horizons vary significantly. According to the applications considered and the possible weighting scheme introduced in Table [III](https://arxiv.org/html/2402.03893v2#S3.T3 "TABLE III ‣ III-C3 Application-specific requirements ‣ III-C Performance Assessment ‣ III Methodology ‣ Prediction Horizon Requirements for Automated Driving: Optimizing Safety, Comfort, and Efficiency This work was supported by SAFE-UP under EU’s Horizon 2020 research and innovation programme, grant agreement 861570."), the required and optimal horizons achieved are shown in Table [VI](https://arxiv.org/html/2402.03893v2#S4.T6 "TABLE VI ‣ IV-C Application-dependent Prediction Horizons ‣ IV Results ‣ Prediction Horizon Requirements for Automated Driving: Optimizing Safety, Comfort, and Efficiency This work was supported by SAFE-UP under EU’s Horizon 2020 research and innovation programme, grant agreement 861570.").

TABLE V: Required and optimal horizons for each SC and metric. Calculated with -

a) General-purpose urban driving

b) Driverless food delivery

c) Driverless taxi (not hurried)

d) Driverless taxi (hurried)

TABLE VI: Required and optimal horizons for each application. Calculated with -

Among the considered applications, driverless food delivery presents the shortest horizon requirements, with a required horizon of 4.4 seconds and an optimal horizon of 7.9 seconds. Driverless taxi applications would benefit from a minimum horizon of 10 seconds, and optimally 14.8 seconds if the passenger is not in a hurry. If the passenger is in a hurry, no horizon exists satisfying all requirements simultaneously, but optimally a horizon of 8.9 seconds would be selected. Finally, for a general-purpose AV operating in environments with crossing pedestrians, the optimal prediction horizon is 11.8 seconds.

### IV-D Limitations

The methodology presented in this work, and consequently our results regarding the recommended horizons for prediction models, has three main limitations.

Firstly, our work operates under the assumption of perfect predictions, which is highly unlikely in real-world driving. If prediction accuracy degrades rapidly with increased horizon, the resulting required and optimal horizons will be affected. It is challenging to discern the effect of these inaccuracies without further experiments, as they will depend on the considered vehicle-level metrics. For instance, inaccurate predictions might lead to more aggressive AV behavior, which would negatively affect comfort, while more aggressive acceleration could be beneficial for travel time efficiency.

Secondly, the current study is constrained to scenarios involving crossing pedestrians and the use of a single planner. Given that different scenarios lead to distinct conclusions, it is vital to explore different scenarios and interactions with other RUs. Furthermore, our conclusions are tied to the specific trajectory planner used during this work. Integrating different planners into our study will enhance the generalizability of our conclusions.

Lastly, the potential benefits of very long prediction horizons remain ambiguous due to computational constraints. It remains unclear whether the optimal value of each metric was achieved, and whether this optimal value would remain constant or degrade with longer horizons.

## Conclusion

Predicting the future movements of surrounding road users is essential for enhancing the performance of an automated vehicle (AV). However, the degree to which these predictions influence the AV's behavior is unknown.

In this study, we explore how various prediction horizons impact the behavior of an AV in terms of safety, comfort, and efficiency. We simulate trajectory predictions in crossing pedestrian scenarios and test different horizons of to 20 seconds, which are integrated into a state-of-the-art trajectory planner that considers the future motion of other road users.

Our results indicate that a prediction horizon of 1.6 seconds is sufficient for avoiding collisions with crossing pedestrians in urban settings. Optimal travel time efficiency is achieved with longer horizons of 7-8 seconds, while predicting up to 15 seconds improves comfort. Longer horizons incur a higher computational load which negatively affects AV performance.

In this work we show that selecting a single optimal prediction horizon is not possible, as the best choice depends on the desired balance between different metrics and scenarios. To this end, we offer a framework to determine the required and optimal prediction horizons based on the specific AV application. Our study suggests a prediction horizon of 11.8 seconds as a general recommendation for AVs operating in environments with crossing pedestrians.

Future work will focus on extending our methodology to derive accuracy requirements for trajectory prediction models.
