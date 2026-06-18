Scenario Diffusion: Controllable Driving Scenario Generation with Diffusion

Topics include Vehicles, Safety, Diffusion models, Object detection, Graphs, Regression, Control, Diffusion.

Automated creation of synthetic traffic scenarios is a key part of validating the safety of autonomous vehicles (AVs). In this paper, we propose Scenario Diffusion, a novel diffusion-based architecture for generating traffic scenarios that enables controllable scenario generation. We combine latent diffusion, object detection and trajectory regression to generate distributions of synthetic agent poses, orientations and trajectories simultaneously. To provide additional control over the generated scenario, this distribution is conditioned on a map and sets of tokens describing the desired scenario. We show that our approach has sufficient expressive capacity to model diverse traffic patterns and generalizes to different geographical regions.

## Introduction

Automated creation of synthetic traffic scenarios is a key part of validating the safety of autonomous vehicles (AVs). To efficiently target rare and safety critical scenarios we would like to direct scenario generation to produce specific types of events. Prior methods for heuristically created scenarios tend to be of limited complexity and miss a large number of possible real-world situations. Recent works using deep learning models are able to produce complex scenarios conditioned on a map region, but do not offer additional controls over the generation process.

Our problem setting is to generate a set of bounding boxes with associated trajectories that describe the location and behavior of agents in a driving scenario. We accomplish this scenario generation using a denoising diffusion generative model. We condition our model on both a map image and a set of tokens describing the scenario. We leverage these tokens to provide a variable rate of control over the generated scenario, so that the diffusion model can generalize to complex scenes conditioned only on a small set of tokens that control both a subset of the individual agents and global scene properties.

Motivated by the insight that the instantaneous position of each agent is inextricably linked to their behaviors, we combine latent diffusion, object detection, and trajectory regression to simultaneously generate both oriented bounding boxes and trajectories, providing a generative model of both the static placement of agents and their behaviors. We evaluate Scenario Diffusion at generating driving scenarios conditioned on only the map, and with additional conditioning tokens as well.

## Conclusion

In this paper, we demonstrate a novel technique for using diffusion to learn to generate scenarios of dynamic agents moving through an environment for the purposes of testing an autonomous vehicle's ability to navigate through that environment and plan according to those agents. We have shown that our technique leads to models that not only appropriately capture the desired distributions of scenarios and agent trajectories, but allow scenario generation to be controlled to target specific types of scenarios.
