Prediction Horizon Requirements for Automated Driving: Optimizing Safety, Comfort, and Efficiency

Topics include Motion prediction, Prediction horizon, Automated driving, Safety, Comfort, Efficiency.

Analyzes how the required prediction horizon for autonomous driving depends on the competing objectives of safety, comfort, and efficiency, providing a framework for selecting appropriate prediction horizons for different driving scenarios and speed profiles.

Predicting the movement of other road users is beneficial for improving automated vehicle (AV) performance. However, the relationship between the time horizon associated with these predictions and AV performance remains unclear. Despite the existence of numerous trajectory prediction algorithms, no studies have been conducted on how varying prediction lengths affect AV safety and other vehicle performance metrics, resulting in undefined horizon requirements for prediction methods. Our study addresses this gap by examining the effects of different prediction horizons on AV performance, focusing on safety, comfort, and efficiency. Through multiple experiments using a state-of-the-art, risk-based predictive trajectory planner, we simulated predictions with horizons up to 20 seconds. Based on our simulations, we propose a framework for specifying the minimum required and optimal prediction horizons based on specific AV performance criteria and application needs. Our results indicate that a horizon of 1.6 seconds is required to prevent collisions with crossing pedestrians, horizons of 7-8 seconds yield the best efficiency, and horizons up to 15 seconds improve passenger comfort....

## Introduction

Automated vehicles (AVs) are becoming increasingly prevalent, and trajectory prediction of surrounding road users (RUs) is a critical component of these systems, since the AV's decisions will be largely based on the predicted motion of other RUs. When designing a system that accounts for the future motion of surrounding RUs, one must decide how much into the future to predict, i.e. the prediction horizon, which is used to plan an AV trajectory for the same horizon....

Figure 1: Typical assessment of trajectory prediction work (left) and our approach (right).

In this work we show that selecting a single optimal prediction horizon is not possible, as the best choice depends on the desired balance between different metrics and scenarios. To this end, we offer a framework to determine the required and optimal prediction horizons based on the specific AV application. Our study suggests a prediction horizon of 11.8 seconds as a general recommendation for AVs operating in environments with crossing pedestrians.

Future work will focus on extending our methodology to derive accuracy requirements for trajectory prediction models.

In our simulations, all possible vehicle-level metrics are $\mathcal{M} = {\{\text{𝑠𝑎𝑓𝑒𝑡𝑦},\text{𝑐𝑜𝑚𝑓𝑜𝑟𝑡},\text{𝑒𝑓𝑓𝑖𝑐𝑖𝑒𝑛𝑐𝑦}\}}$, all possible SCs are $\mathcal{S} = {\{\textit{SC1},\textit{SC2},\textit{SC3}\}}$, and all possible horizons are $\mathcal{H}$ as in. When considering a collection of metrics $M \subseteq \mathcal{M}$ and SCs $S \subseteq \mathcal{S}$, we aim to find a required and an optimal horizon, $r_{M}^{S}$, and $o_{M}^{S}$, such that horizon $r_{M}^{S}$ yields satisfactory AV performance for all metrics and scenarios considered, and horizon $o_{M}^{S}$ yields the best value of each metric in every scenario....

### III-B2 Predictions

General-purpose urban driving. The AV operates between 30km/h and 50km/h, and having the best trade-off between comfort and efficiency is desired.

Despite the existence of several works showing that it is beneficial to integrate predictions in motion planning \[\], there is no clear quantification of the relationship between the prediction horizon and the resulting impact on AV behavior. To establish requirements that a prediction model should adhere to, the impact that predictions have on AV behavior must first be understood....
