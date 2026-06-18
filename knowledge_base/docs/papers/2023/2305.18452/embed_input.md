Generating Driving Scenes with Diffusion

Topics include Diffusion models, Object detection.

In this paper we describe a learned method of traffic scene generation designed to simulate the output of the perception system of a self-driving car. In our "Scene Diffusion" system, inspired by latent diffusion, we use a novel combination of diffusion and object detection to directly create realistic and physically plausible arrangements of discrete bounding boxes for agents. We show that our scene generation model is able to adapt to different regions in the US, producing scenarios that capture the intricacies of each region.

## INTRODUCTION

Figure 1: Architectures for training and inference. In (a) an autoencoder is trained to encode a birds’ eye view image of vehicles in a scene (x) and output oriented bounding box detections (y) for the entities. In (b) the pre-trained autoencoder is used to train a diffusion model on the latent embeddings (z) of the autoencoder conditioned on a map image (m). In (c) the diffusion model and decoder are used to generate novel traffic scenes by first running diffusion inference in the latent space and then decoding to recover oriented bounding boxes.

Simulation has long been a useful component for integration testing as part of the development of autonomous vehicles. The advent of high quality photorealism and realistic physics in recent simulators has enabled the development and evaluation of new models and algorithms for autonomy with much more reliability than has historically been possible.

In this work we presented a novel approach to generating complex driving scenes using diffusion in an end-to-end differentiable architecture that directly generates discrete agents. We also analyze the generalization capabilities of our model across multiple regions.

Generating diverse, realistic, and complex driving scenarios is a key part of scaling the validation of autonomous driving systems. We believe this work provides a new approach to address this challenge that is more stable, controllable, and higher quality than prior approaches. In future work, we plan to extend these ideas beyond synthesis of the initial scenario to the time series generation of agents moving in a dynamic scenario. We hope this will contribute to the safe deployment of autonomous driving systems in the coming years.

The final loss for the denoising model is a weighted combination of these two losses:

The classification cost can be immediately applied to our setting. Our bounding boxes only have one class (vehicles), and so the classification cost is simply the binary cross-entropy between the probability $p{(b_{i})}$ and the probability of $g_{j}$ (defined to be 1 for all ground truth boxes).

### V-A3 Training

However, one of the limitations of all simulations is the difficulty in creating a range of simulated scenarios that vary in ways that accurately match the distribution of scenarios in the real world....
