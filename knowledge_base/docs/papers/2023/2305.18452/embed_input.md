Generating Driving Scenes with Diffusion

Topics include Diffusion models, Object detection.

In this paper we describe a learned method of traffic scene generation designed to simulate the output of the perception system of a self-driving car. In our "Scene Diffusion" system, inspired by latent diffusion, we use a novel combination of diffusion and object detection to directly create realistic and physically plausible arrangements of discrete bounding boxes for agents. We show that our scene generation model is able to adapt to different regions in the US, producing scenarios that capture the intricacies of each region.

## INTRODUCTION

Simulation has long been a useful component for integration testing as part of the development of autonomous vehicles. The advent of high quality photorealism and realistic physics in recent simulators has enabled the development and evaluation of new models and algorithms for autonomy with much more reliability than has historically been possible.

However, one of the limitations of all simulations is the difficulty in creating a range of simulated scenarios that vary in ways that accurately match the distribution of scenarios in the real world. Given a set of simulation assets, those assets must still be arranged in a scenario that is physically plausible, e.g., for a traffic simulator, simulated vehicles must be oriented correctly with respect to the road surface and their motion must be a reasonable facsimile of human driving. Scenario construction can be performed by hand or with hand-crafted heuristics, but the number of scenarios that can be constructed manually is limited.

For the purposes of developing prediction and planning algorithms for an autonomous vehicle, we are less interested in photorealistic scenario generation than we are in simulating an abstraction of the scenario that would be produced by a perception system such as dynamic, oriented bounding boxes that represent cars and pedestrians in the environment. Several recent results in procedural scene generation have shown promise in learning different models of the distributions of real-world scenes.

In this paper we describe a traffic scene generation architecture we refer to as "Scene Diffusion". Following, there are two parts to our model architecture: an autoencoder which is trained first, and a diffusion model which is trained second on the latent embeddings from the autoencoder. We use a novel combination of diffusion and object detection to directly output discrete bounding boxes for agents.

We propose a novel end-to-end differentiable architecture based on latent diffusion and object detection for generating driving scenes.

We evaluate the generalization capabilities of our scene generation model across different geographical regions qualitatively and quantitatively.
