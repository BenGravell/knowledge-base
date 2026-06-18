Scenario Diffusion: Controllable Driving Scenario Generation with Diffusion

Topics include Vehicles, Safety, Diffusion models, Object detection, Graphs, Regression, Control, Diffusion.

Automated creation of synthetic traffic scenarios is a key part of validating the safety of autonomous vehicles (AVs). In this paper, we propose Scenario Diffusion, a novel diffusion-based architecture for generating traffic scenarios that enables controllable scenario generation. We combine latent diffusion, object detection and trajectory regression to generate distributions of synthetic agent poses, orientations and trajectories simultaneously. To provide additional control over the generated scenario, this distribution is conditioned on a map and sets of tokens describing the desired scenario. We show that our approach has sufficient expressive capacity to model diverse traffic patterns and generalizes to different geographical regions.

## Introduction

Automated creation of synthetic traffic scenarios is a key part of validating the safety of autonomous vehicles (AVs). To efficiently target rare and safety critical scenarios we would like to direct scenario generation to produce specific types of events. Prior methods for heuristically created scenarios tend to be of limited complexity and miss a large number of possible real-world situations. Recent works using deep learning models are able to produce complex scenarios conditioned on a map region, but do not offer additional controls over the generation process....

Our problem setting is to generate a set of bounding boxes with associated trajectories that describe the location and behavior of agents in a driving scenario. We accomplish this scenario generation using a denoising diffusion generative model. We condition our model on both a map image and a set of tokens describing the scenario. We leverage these tokens to provide a variable rate of control over the generated scenario, so that the diffusion model can generalize to complex scenes conditioned only on a small set of tokens that control both a subset of the individual agents and global scene properties....

Limitations: More work is required to show broader generalization. The training data assumes a specific model of perception in the form of bounding boxes and trajectory models. Additionally, we restricted the agent models to on-road vehicle models. While we do not anticipate significant challenges in applying this model to other forms of agents such as pedestrians, we have not incorporated those agents in the research described here. In simulation this approach may need to be extended to iteratively generate agents over a larger region as the AV navigates through the environment.

Broader Impact: This paper focuses on developing models to improve self-driving car technologies. There are many positive and negative aspects to the development of self-driving cars that depend as much on the system-wide design and regulatory aspects as these aspects depend on the technical capabilities. However, the focus on simulation in this paper should partially reduce the risks of deploying self-driving cars by providing more effective and systematic coverage of testing scenarios.

### Datasets
