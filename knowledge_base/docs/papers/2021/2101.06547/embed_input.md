LookOut: Diverse Multi-Future Prediction and Planning for Self-Driving

In this paper, we present LookOut, a novel autonomy system that perceives the environment, predicts a diverse set of futures of how the scene might unroll and estimates the trajectory of the SDV by optimizing a set of contingency plans over these future realizations. In particular, we learn a diverse joint distribution over multi-agent future trajectories in a traffic scene that covers a wide range of future modes with high sample efficiency while leveraging the expressive power of generative models. Unlike previous work in diverse motion forecasting, our diversity objective explicitly rewards sampling future scenarios that require distinct reactions from the self-driving vehicle for improved safety. Our contingency planner then finds comfortable and non-conservative trajectories that ensure safe reactions to a wide range of future scenarios. Through extensive evaluations, we show that our model demonstrates significantly more diverse and sample-efficient motion forecasting in a large-scale self-driving dataset as well as safer and less-conservative motion plans in long-term closed-loop simulations when compared to current state-of-the-art models.

## Introduction

Self-driving vehicles (SDVs) have the potential to enhance considerably the safety of our roads as, unlike humans, they can constantly scan the surrounding environment without getting distracted or being impaired while driving. Key to the success of a self-driving vehicle is its ability to perceive its surroundings and predict the future trajectory of the traffic participants, particularly those that might affect its decision making. These predictions are then exploited by the motion planning module to plan a safe and comfortable maneuver towards the goal.

Figure 1: We illustrate the fact that the future is highly uncertain and multi-modal by showing 2 distinct futures at the scene-level. In such scenario, LookOut plans a short-term executable action that leads to 2 different contingent plans to stay safe in both cases.

## Conclusion

We have proposed a prediction and planning model that generates more diverse motion forecasts and safer trajectories for the SDV. Our prediction model learns to generate multimodal trajectory samples from a joint distribution over actor trajectories. Unlike previous diverse forecasting approaches, we directly optimize for predicting rare behavior that could impact the SDV, and estimate the probability distribution over these samples for more accurate risk assessment. Our contingency planner improves the decision making over these diverse samples....

### Contingency Planner

where $\mathbf{Y} = {\{ Y_{1},\ldots,Y_{K}\}}$, $Y_{k} = {f_{\theta}{(X,Z_{k})}}$, $Z_{k} = {\mathcal{M}_{\eta_{k}}{(X,\varepsilon)}}$ and the minimization is with respect to learnable parameters of the pair of GNNs $\eta$. Note that the decoder is fixed, i.e., $\theta$ is not optimized. This is key to maintain a high realism of the decoded trajectories, since the diversity objective can be otherwise cheated (e.g., by making other actors "appear" right in front of the SDV).

ATG4D is composed of over one million frames of LiDAR, HD maps with very accurate object tracks. It was collected with careful expert drivers in several North American cities. All models are trained to predict 5-second trajectories, given 1 second of LiDAR history. We evaluate motion forecasting in the test set of this dataset.

Forecasting the behavior of traffic participants is very challenging as humans do not always follow the rules of the road and sometimes...
