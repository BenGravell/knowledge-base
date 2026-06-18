Multimodal Trajectory Predictions for Autonomous Driving Using Deep Convolutional Networks

Autonomous driving presents one of the largest problems that the robotics and artificial intelligence communities are facing at the moment, both in terms of difficulty and potential societal impact. Self-driving vehicles (SDVs) are expected to prevent road accidents and save millions of lives while improving the livelihood and life quality of many more. However, despite large interest and a number of industry players working in the autonomous domain, there still remains more to be done in order to develop a system capable of operating at a level comparable to best human drivers. One reason for this is high uncertainty of traffic behavior and large number of situations that an SDV may encounter on the roads, making it very difficult to create a fully generalizable system. To ensure safe and efficient operations, an autonomous vehicle is required to account for this uncertainty and to anticipate a multitude of possible behaviors of traffic actors in its surrounding. We address this critical problem and present a method to predict multiple possible trajectories of actors while also estimating their probabilities....

## Introduction

Recent years have witnessed unprecedented progress in Artificial Intelligence (AI) applications, with smart algorithms rapidly becoming an integral part of our daily lives. The AI methods are used by hospitals to help diagnose diseases, matchmaking services are using learned models to connect potential couples, and social media feeds are built by algorithmic approaches, to name just a few affecting millions of people. Nevertheless, despite huge strides the AI revolution is far from over, and is likely to further accelerate in the coming years....

Driving a vehicle in traffic is a surprisingly dangerous task considering it is such a common activity of many, even for human drivers with several years of experience. While the car manufacturers are working hard on improving vehicle safety through better design and ADAS systems, grim year-to-year statistics indicate that there is still a lot more to be done in order to revert the negative trends observed on public roads. In particular, car accidents amounted to more than $5\%$ of deaths in the US in 2015, with the human factor to blame in the vast majority of the crashes....

## Conclusion

Due to the inherent uncertainty of traffic behavior, autonomous vehicles need to consider multiple possible future trajectories of the surrounding actors in order to ensure a safe and efficient ride. In this work, we addressed this critical aspect of the self-driving problem and proposed a method to model the multimodality of vehicle movement prediction. The approach first generates a raster image encoding surrounding context of each vehicle actor and uses a CNN model to output several possible trajectories along with their probabilities....

After selecting the best matching mode $m^{\ast}$, the final loss function can be defined as follows,

### III-A Problem setting

In Figure 4 we show rasters for the same scene but using two different following lanes marked in light pink, one going straight and one turning left. The method outputs trajectories that follow the intended paths well, and can be used to generate multitude of trajectories for lane-following vehicles.

Self-driving technology has been under development for a long time, with the earliest attempts going as far back as the 1980s and the work on ALVINN....
