<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Generating Driving Scenes with Diffusion

Topics include Diffusion models, Object detection.

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

In this paper we describe a learned method of traffic scene generation designed to simulate the output of the perception system of a self-driving car. In our "Scene Diffusion" system, inspired by latent diffusion, we use a novel combination of diffusion and object detection to directly create realistic and physically plausible arrangements of discrete bounding boxes for agents. We show that our scene generation model is able to adapt to different regions in the US, producing scenarios that capture the intricacies of each region.

<!-- chunk {"id": "body-0003", "role": "body", "section": "INTRODUCTION", "weight": 1.5} -->

Simulation has long been a useful component for integration testing as part of the development of autonomous vehicles. The advent of high quality photorealism and realistic physics in recent simulators has enabled the development and evaluation of new models and algorithms for autonomy with much more reliability than has historically been possible.

<!-- chunk {"id": "body-0004", "role": "body", "section": "INTRODUCTION", "weight": 1.5} -->

However, one of the limitations of all simulations is the difficulty in creating a range of simulated scenarios that vary in ways that accurately match the distribution of scenarios in the real world. Given a set of simulation assets, those assets must still be arranged in a scenario that is physically plausible, e.g., for a traffic simulator, simulated vehicles must be oriented correctly with respect to the road surface and their motion must be a reasonable facsimile of human driving. Scenario construction can be performed by hand or with hand-crafted heuristics, but the number of scenarios that can be constructed manually is limited. Unusual (but plausible) maneuvers such as cars moving into oncoming traffic around a double-parked vehicle may not be easily captured with heuristics.

<!-- chunk {"id": "body-0005", "role": "body", "section": "INTRODUCTION", "weight": 1.5} -->

For the purposes of developing prediction and planning algorithms for an autonomous vehicle, we are less interested in photorealistic scenario generation than we are in simulating an abstraction of the scenario that would be produced by a perception system such as dynamic, oriented bounding boxes that represent cars and pedestrians in the environment. Several recent results in procedural scene generation have shown promise in learning different models of the distributions of real-world scenes. However, the computational and data complexity of learning explicit statistical models such as scene grammars tend to be restricted to small scale, static scenes. More recent deep learning models have been shown to produce complex simulation scenes with larger numbers of agents. These works are based on established techniques for image generation.

<!-- chunk {"id": "body-0006", "role": "body", "section": "INTRODUCTION", "weight": 1.5} -->

The development of diffusion models has shown to be remarkably successful in image generation, surpassing prior methods. This work is motivated by the hypothesis that diffusion is also a better approach for generating traffic scenes. Latent diffusion is especially well suited for generating traffic scenes due to the decoupling of latent and output spaces. However, the image-based loss term that is conventionally used in generative models such as autoencoders needs to be adapted to this kind of abstract scene output.

<!-- chunk {"id": "body-0007", "role": "body", "section": "INTRODUCTION", "weight": 1.5} -->

In this paper we describe a traffic scene generation architecture we refer to as "Scene Diffusion". Following, there are two parts to our model architecture: an autoencoder which is trained first, and a diffusion model which is trained second on the latent embeddings from the autoencoder. We use a novel combination of diffusion and object detection to directly output discrete bounding boxes for agents.

<!-- chunk {"id": "body-0008", "role": "body", "section": "INTRODUCTION", "weight": 1.5} -->

We propose a novel end-to-end differentiable architecture based on latent diffusion and object detection for generating driving scenes.

<!-- chunk {"id": "body-0009", "role": "body", "section": "INTRODUCTION", "weight": 1.5} -->

We evaluate the generalization capabilities of our scene generation model across different geographical regions qualitatively and quantitatively.

<!-- chunk {"id": "body-0010", "role": "body", "section": "PROBLEM SETTING", "weight": 1.0} -->

Our goal is to develop a generative model to produce driving scenes conditioned on map data. In this work a driving scene consists of a map and a set of agents, where each agent is described by an oriented bounding box.

<!-- chunk {"id": "body-0011", "role": "body", "section": "PROBLEM SETTING", "weight": 1.0} -->

The map is represented as a multi-channel birds' eye view image $m \in {\mathbb{R}}^{C_{m} \times H \times W}$ similar to that described. This map image contains information about the road geometry, regions of interest (e.g. driveways, crosswalks, parking spots), and traffic light states.

<!-- chunk {"id": "body-0012", "role": "body", "section": "PROBLEM SETTING", "weight": 1.0} -->

The agents are also represented as a multi-channel birds' eye view image $x \in {\mathbb{R}}^{C_{x} \times H \times W}$, also similar to. In addition to a binary channel representing whether a pixel is occupied we also use channels that fill each agent's bounding box with the sine and cosine of the agent's heading to disambiguate the orientation of each box. This image $x$ is used to represent scenes during training and is not used for inference. An example of $x$ and $m$ is shown in Fig. 1.

<!-- chunk {"id": "body-0013", "role": "body", "section": "PROBLEM SETTING", "weight": 1.0} -->

At inference we wish to generate a set of bounding boxes conditioned on the map data $m$. While these boxes are eventually converted to a center pose, length, and width, the model itself can use a different parameterization as described in Sec. III-B.

<!-- chunk {"id": "body-0014", "role": "body", "section": "SCENE AUTOENCODER", "weight": 1.0} -->

The architecture of the scene autoencoder is adapted from that of. The main modification is in the decoder output representation and the associated reconstruction loss. The architecture for training the autoencoder is shown in Fig. 1(a).

<!-- chunk {"id": "body-0015", "role": "body", "section": "III-A Conditional Variational Autoencoder", "weight": 1.0} -->

From these parameters, a latent embedding is obtained using the reparametrization trick: $z = {z_{\mu} + {z_{\sigma}\epsilon}}$ where $\epsilon \sim {\mathcal{N}(0,\mathbf{I})}$. This latent embedding is then given to a decoder $\mathcal{D}$ along with $m$. The decoder output is $y = {\mathcal{D}{(z;m)}}$.

<!-- chunk {"id": "body-0016", "role": "body", "section": "III-A Conditional Variational Autoencoder", "weight": 1.0} -->

To train the VAE, a reconstruction loss $\mathcal{L}_{\text{rec}}{(y,x)}$ is applied between the decoder output and the original encoder inputs $x$. A KL regularization loss is applied to the latent embedding distributions,

<!-- chunk {"id": "body-0017", "role": "body", "section": "III-A Conditional Variational Autoencoder", "weight": 1.0} -->

One of the key adaptations to go from images to driving scenes is to change the output representation of the decoder and the reconstruction loss to train it. The exact structure of $y$ and $\mathcal{L}_{\text{rec}}$ is described in the sections below.

<!-- chunk {"id": "body-0018", "role": "body", "section": "III-B Oriented Bounding Boxes", "weight": 1.0} -->

We aim to produce an anchor-free one-to-one object detector that will produce a single oriented bounding box per agent without needing heuristic post-processing to construct boxes as. However, the approach of is not immediately applicable to *oriented* bounding box detection because differentiable IoU loss is not tractable for rotated bounding boxes.

<!-- chunk {"id": "body-0019", "role": "body", "section": "III-B Oriented Bounding Boxes", "weight": 1.0} -->

Our simplified detection problem setting (we provide perfectly rendered boxes with channels clearly indicating the correct orientation of the box) allows us to use a more straight-forward approach compared to prior works performing oriented object detection in more challenging settings.

<!-- chunk {"id": "body-0020", "role": "body", "section": "III-B1 Representation", "weight": 1.0} -->

In the decoder output $y$, each pixel represents one bounding box. Note that the pixel dimensions of $y$ can be different from those of $x$; in practice we use a lower resolution for $y$ to reduce computational and memory requirements.

<!-- chunk {"id": "body-0021", "role": "body", "section": "III-B1 Representation", "weight": 1.0} -->

Let $b$ be the feature vector for one pixel in $y$. The pixel location defines the 2D reference point ${r{(b)}} \in {\mathbb{R}}^{2}$ used to locate the box in space. There are seven channels of $b$ to define the probability, shape, and orientation of the box: $(l,\theta_{c},\theta_{s},d_{\text{front}},d_{\text{left}},d_{\text{back}},d_{\text{right}})$

<!-- chunk {"id": "body-0022", "role": "body", "section": "III-B1 Representation", "weight": 1.0} -->

The first channel $l$ is a sigmoid logit that defines the probability for the box. The next two channels represent the cosine ($\theta_{c}$) and sine ($\theta_{s}$) of the box orientation. By predicting sine and cosine values we avoid having an arbitrary discontinuity in the expected model output (e.g. between $- \pi$ and $\pi$).

<!-- chunk {"id": "body-0023", "role": "body", "section": "III-B1 Representation", "weight": 1.0} -->

Four more channels represent the log of the distances from the pixel center to the front ($d_{\text{front}}$), left ($d_{\text{left}}$), back ($d_{\text{back}}$), and right ($d_{\text{right}}$) sides of the box. These parameters are demonstrated in Fig. 2.

<!-- chunk {"id": "body-0024", "role": "body", "section": "III-B1 Representation", "weight": 1.0} -->

This parametrization for oriented bounding boxes means that the pixel does not need to be at the center of the box, but does have to be inside the box. This constraint limits how coarse the bounding box proposals can be to accurately capture entities in the scene. While having an output resolution of $\sim {1.5\text{m / px}}$ is sufficient for vehicles, it would be too coarse to ensure coverage of pedestrians. We leave a more complex oriented bounding box representation that can accommodate smaller entities without increasing the box resolution to a future work.

<!-- chunk {"id": "body-0025", "role": "body", "section": "III-B2 Training", "weight": 1.0} -->

Given a set of ground truth boxes $G = {\{ g_{j}\}}$ and a set of predicted boxes $B = {\{ b_{i}\}}$, we use a matching cost $C{(b_{i},g_{j})}$ to define a mapping from each ground truth box $j$ to the best matched predicted box $i{(j)}$ such that $g_{j}$ is matched with $b_{i{(j)}}$. uses a combination of classification, L1, and IoU costs. We modify this approach to account for the intractability of IoU for oriented bounding boxes.

<!-- chunk {"id": "body-0026", "role": "body", "section": "III-B2 Training", "weight": 1.0} -->

The classification cost can be immediately applied to our setting. Our bounding boxes only have one class (vehicles), and so the classification cost is simply the binary cross-entropy between the probability $p{(b_{i})}$ and the probability of $g_{j}$ (defined to be 1 for all ground truth boxes).

<!-- chunk {"id": "body-0027", "role": "body", "section": "III-B2 Training", "weight": 1.0} -->

The L1 cost is also easy to apply. For each pair of predicted box and ground truth box we compute the correct box parameters to match the ground truth box from the predicted box's pixel center. For the log distance terms we clip the distance in cases where the distance is negative (i.e. the pixel is outside the box). We then apply an L1 loss on the cosine, sine, and four log distance terms of the box representation.

<!-- chunk {"id": "body-0028", "role": "body", "section": "III-B2 Training", "weight": 1.0} -->

Several works have attempted to approximate IoU for oriented bounding boxes in a differentiable way. Given the simplified detection setting in this work (our input consists of clean, perfect rectangles with unambiguous orientations), we propose a simpler alternative that is tractable for oriented bounding boxes and describes the spatial alignment of the two boxes. We apply a vertex cost term as the average L2 norm between each pair of vertices.

<!-- chunk {"id": "body-0029", "role": "body", "section": "III-B2 Training", "weight": 1.0} -->

where $\text{vert}_{v}{(b)}$ computes the $v^{\text{th}}$ vertex of the box (front left, front right, back left, and back right). We find that this vertex cost is important in matching, as the L1 loss may prefer a good box for an adjacent vehicle (which gets good L1 loss for all but the left and right distance parameters) over a not-so-good box that aligns spatially with the ground truth box in question.

<!-- chunk {"id": "body-0030", "role": "body", "section": "III-B2 Training", "weight": 1.0} -->

The final matching cost is a weighted combination of these three costs

<!-- chunk {"id": "body-0031", "role": "body", "section": "III-B2 Training", "weight": 1.0} -->

Given these matching costs, we assign one predicted box $b_{i{(j)}}$ to each ground truth box $g_{j}$.

<!-- chunk {"id": "body-0032", "role": "body", "section": "III-B2 Training", "weight": 1.0} -->

A binary cross-entropy loss $\mathcal{L}_{\text{cls}}$ is used for the predicted box probabilities $p{(b_{i})}$ and an indicator $\mathbb{1}\left\lbrack \exists j:i{(j)} = i \right\rbrack$ for whether $b_{i}$ was assigned to some ground truth box. L1 and vertex losses are simply the corresponding matching costs applied between each pair $g_{j}$ and $b_{i{(j)}}$. Note that the parameters defining box shape are only regressed for predicted boxes that are matched to a ground truth box, while the box logit is trained for all predicted boxes. The overall detection loss is a weighted combination of the classification, L1, and vertex loss terms. The weighting coefficients do not need to be the same as that used for the matching cost.

<!-- chunk {"id": "body-0033", "role": "body", "section": "SCENE DIFFUSION", "weight": 1.0} -->

After the scene autoencoder is trained, we use the frozen encoder and decoder to train a diffusion model on the latent embeddings as. However, for the actual diffusion algorithm we use EDM with the addition of image conditional data. Fig. 1(b) shows the architecture for diffusion training and Fig. 1(c) shows the architecture for inference.

<!-- chunk {"id": "body-0034", "role": "body", "section": "IV-A Training", "weight": 1.0} -->

Let $\hat{z} = {\mathcal{E}{(x)}}$ be a latent embedding obtained from the frozen encoder and $m$ the corresponding map data as described in Sec. II.

<!-- chunk {"id": "body-0035", "role": "body", "section": "IV-A Training", "weight": 1.0} -->

We create a noisy version of the embeddings $z = {\hat{z} + {\sigma\epsilon}}$ where $\epsilon \in {\mathbb{R}}^{C^{\prime} \times H^{\prime} \times W^{\prime}}$ is sampled from the standard normal distribution.

<!-- chunk {"id": "body-0036", "role": "body", "section": "IV-A Training", "weight": 1.0} -->

Given a noisy sample $z$, we can estimate the denoised version $\hat{z}$ by

<!-- chunk {"id": "body-0037", "role": "body", "section": "IV-A Training", "weight": 1.0} -->

The L2 norm on the latent space treats all directions equally, but some will be more or less important for the decoder. To capture this, we apply an additional reconstruction loss

<!-- chunk {"id": "body-0038", "role": "body", "section": "IV-A Training", "weight": 1.0} -->

where $\mathcal{D}$ is the frozen decoder and $\mathcal{L}_{\text{rec}}$ is the same reconstruction loss used for the autoencoder in Sec. III-A.

<!-- chunk {"id": "body-0039", "role": "body", "section": "IV-B Inference", "weight": 1.0} -->

To generate new samples given a map image $m$, an initial noisy sample $z \sim {\mathcal{N}{(0,{\sigma_{\text{max}}^{2}\mathbf{I}})}}$ is drawn for some large noise level $\sigma_{\text{max}}$. This sample is then iteratively refined according to the reverse process ODE as described. Due to the manner in which the denoising model $\mathcal{M}$ is trained, the gradient of the log probability ${{{\nabla_{z}\log}p}{(z;m,\sigma)}} = {\left( {{M{(z;m,\sigma)}} - z} \right)/\sigma^{2}}$. Thus, the ODE simplifies to

<!-- chunk {"id": "body-0040", "role": "body", "section": "IV-B Inference", "weight": 1.0} -->

After the sample has been integrated from $\sigma_{\text{max}}$ to 0, it is passed through the decoder to get the final output $y = {\mathcal{D}{(z,m)}}$.

<!-- chunk {"id": "body-0041", "role": "body", "section": "V-A1 Dataset", "weight": 1.0} -->

We use a private dataset containing 6 million driving scenes from San Francisco, Las Vegas, Seattle, and the campus of the Stanford Linear Accelerator Center (SLAC). Scenes are sampled every 0.5 seconds from real-world driving logs.

<!-- chunk {"id": "body-0042", "role": "body", "section": "V-A1 Dataset", "weight": 1.0} -->

Each scene contains vehicle tracks as detected by an on-vehicle perception system. We filter these tracks to only include bounding boxes that overlap with drivable areas in the map (e.g. roads, public parking lots, driveways).

<!-- chunk {"id": "body-0043", "role": "body", "section": "V-A1 Dataset", "weight": 1.0} -->

Scenes are centered on the autonomous vehicle. The autonomous vehicle is treated as just another vehicle in the scene during training, so the model always sees scenes with a vehicle in the scene center.

<!-- chunk {"id": "body-0044", "role": "body", "section": "V-A1 Dataset", "weight": 1.0} -->

The birds' eye view images are $H = W = 256$ pixels in height and width and cover an area 100m x 100m. The entity image $x$ has $C_{x} = 3$ channels where the box for each agent is filled with ones, the sine of the agent's heading, and the cosine of the agent's heading, respectively.

<!-- chunk {"id": "body-0045", "role": "body", "section": "V-A2 Model Architecture", "weight": 1.0} -->

In the autoencoder, we use the same encoder architecture as with $f = 3$ downsampling layers so that the output latent embedding is $H^{\prime} = W^{\prime} = 32$ pixels in height and width. The encoder and decoder use 32, 64, 128, and 128 channels at the 0x, 1x, 2x, and 3x downsampled feature levels, respectively. We use a latent channel dimension of $C^{\prime} = 4$.

<!-- chunk {"id": "body-0046", "role": "body", "section": "V-A2 Model Architecture", "weight": 1.0} -->

For the decoder, we first use the same architecture as the encoder to downsample the map image to the same pixel dimension as the latent embedding. However, we also save feature maps at each level of downsampling. We then concatenate the compressed map data with the latent embedding from the encoder and use a modified version of the decoder from where we add skip connections in each upsampling block to the corresponding feature map from the map downsampling network. The decoder does not upsample all the way to the original encoder input size, and instead outputs bounding box detections at 64 x 64 pixels. This is a high enough resolution to consistently have a pixel within each vehicle, while low enough to avoid memory issues during training.

<!-- chunk {"id": "body-0047", "role": "body", "section": "V-A2 Model Architecture", "weight": 1.0} -->

In the denoising model we first use the same architecture as the autoencoder's encoder to process the conditional map image down to the same pixel size as the latent embedding. The processed map data is concatenated with the latent embedding and processed by a time-conditioned Unet as. The Unet uses 64, 128, and 256 layers in three levels of features. At the lowest resolution layer it uses self-attention with 8 heads. Each resolution layer uses 2 residual blocks.

<!-- chunk {"id": "body-0048", "role": "body", "section": "V-A2 Model Architecture", "weight": 1.0} -->

We threshold the boxes generated by the decoder based on the generated box probabilities. We use a probability threshold of $90\%$, although we observe that almost all generated boxes have probability either above 97% or below 40%.

<!-- chunk {"id": "body-0049", "role": "body", "section": "V-A3 Training", "weight": 1.0} -->

For training the autoencoder, we use the Adam optimizer with a learning rate of 1e-4 and a weight decay of 1e-5. For the detection matching we use $\alpha_{\text{cls}} = 4$, $\alpha_{\text{L1}} = 1$, and $\alpha_{\text{vert}} = 1$. For the detection loss we use $\beta_{\text{cls}} = 20$, $\beta_{\text{L1}} = 1$, and $\beta_{\text{vert}} = 1$.

<!-- chunk {"id": "body-0050", "role": "body", "section": "V-A3 Training", "weight": 1.0} -->

For training the diffusion model, we use $P_{\mu} = {- 0.5}$ and $P_{\sigma} = 1$. The loss weight $\beta_{y} = 0.2$. We use an AdamW optimizer with a learning rate of 3e-4 and weight decay of 1e-5.

<!-- chunk {"id": "body-0051", "role": "body", "section": "V-A3 Training", "weight": 1.0} -->

For inference we use 100 timesteps and select a noise schedule with $\rho = 7$.

<!-- chunk {"id": "body-0052", "role": "body", "section": "V-B Metrics", "weight": 1.0} -->

To determine whether the data produced under our learned models matches the training data used to train the model, we can examine whether the training distribution matches the synthesized data distribution. Since we do not have access to the actual distribution implicit in the diffusion model, we compare the distributions of the samples using the mean maximum discrepancy (MMD) under a Gaussian kernel. Given two distributions $p,q$ over ${\mathbb{R}}^{d}$,

<!-- chunk {"id": "body-0053", "role": "body", "section": "V-B Metrics", "weight": 1.0} -->

We apply this metric to the agent center positions and their heading vectors (i.e. a unit vector in the direction the agent is facing). We compute this metric between individual pairs of scenes using the same map location and average across the dataset as. This metric quantifies how well the distribution of generated scenes matches the given data sample at the same map location.

<!-- chunk {"id": "body-0054", "role": "body", "section": "V-C Generating Driving Scenes", "weight": 1.0} -->

Fig. 3 shows a number of generated driving scenes for various map locations. The model is able to generate diverse driving scenarios for various map locations. The generated bounding boxes conform to the map and are arranged in a realistic manner.

<!-- chunk {"id": "body-0055", "role": "body", "section": "V-D Performance Across Regions", "weight": 1.0} -->

The four regions included in our dataset each have unique driving features, road geometries, and distributions of vehicles. To quantify how well our model is able to generalize and learn multiple regions simultaneously, we train the same architecture on data from one region at a time, as well as the full dataset with all four regions. We then generate scenes using map locations from each region and compute MMD metrics as described in Sec. V-B.

<!-- chunk {"id": "body-0056", "role": "body", "section": "V-D Performance Across Regions", "weight": 1.0} -->

Tab. I shows the results for agent positions and Tab. II shows the results for agent headings. We observe that for both metrics and across all regions the model trained exclusively on that region performs best (i.e. has the lowest MMD). In all cases the model trained on the full dataset comes close to matching this performance. This demonstrates that our model has the capacity to incorporate the unique aspects of all four regions in a single model.

<!-- chunk {"id": "body-0057", "role": "body", "section": "V-D Performance Across Regions", "weight": 1.0} -->

The model trained on SLAC data consistency performs the worst in the other three regions, and SLAC scenes show the largest gap between models trained with and without that data. This intuitively makes sense, as SLAC is an academic campus while the other three regions consist of dense urban scenes.

<!-- chunk {"id": "body-0058", "role": "body", "section": "V-D Performance Across Regions", "weight": 1.0} -->

Qualitatively, we observe that models trained on only one region are unable to capture features of the driving scene unique to another region. Fig. 4 compares scenes generated by models trained on different regions.

<!-- chunk {"id": "body-0059", "role": "body", "section": "RELATED WORKS", "weight": 1.0} -->

Several works have generated agents conditioned on map information using different approaches. We also provide an overview of some relevant works from diffusion for natural images and oriented object detection.

<!-- chunk {"id": "body-0060", "role": "body", "section": "VI-A Driving Scene Generation", "weight": 1.0} -->

A number of prior works have used heuristics or fixed grammars to generate driving scenes. Such approaches are limited in their ability to generate large and diverse driving scenes using large-scale datasets.

<!-- chunk {"id": "body-0061", "role": "body", "section": "VI-A Driving Scene Generation", "weight": 1.0} -->

One learned approach to scene generation is to autoregressively generate one agent at a time. SceneGen uses a birds' eye view image of the map and a convolutional LSTM to iteratively predict a probability distribution over the next agent, moving from left to right in the scene. This probability distribution is factorized with chained terms for the object's class, position, heading, extent, and velocity.

<!-- chunk {"id": "body-0062", "role": "body", "section": "VI-A Driving Scene Generation", "weight": 1.0} -->

TrafficGen also uses an autoregressive generation process. They replace the rasterized map image with a vector representation. They also generate trajectories given the initial agent states with a disjoint second model that adapts to only consider a single timestep of history.

<!-- chunk {"id": "body-0063", "role": "body", "section": "VI-A Driving Scene Generation", "weight": 1.0} -->

In image synthesis, an alternative approach to autoregressive generation such as is to generate the entire image simultaneously. SimNet uses a conditional GAN to generate an occupancy map and apply heuristic post-processing to identify connected components and fit bounding boxes to them. A second agent-centric model is then used to generate trajectories for these agents over time.

<!-- chunk {"id": "body-0064", "role": "body", "section": "VI-A Driving Scene Generation", "weight": 1.0} -->

Our work adapts a different technique from image synthesis, latent diffusion, to generate the entire driving scene simultaneously. In contrast to, our model directly outputs oriented bounding boxes for agents and does not require post-processing to fit bounding boxes to occupancy maps.

<!-- chunk {"id": "body-0065", "role": "body", "section": "VI-B Diffusion for Image Synthesis", "weight": 1.0} -->

Diffusion models have become quite popular for generating images. Many works have explored conditioning the diffusion model on other image or text data (e.g. ).

<!-- chunk {"id": "body-0066", "role": "body", "section": "VI-B Diffusion for Image Synthesis", "weight": 1.0} -->

uses an autoencoder to compress images to a latent embedding and then applies diffusion to model the data distribution in that latent space. This decouples the output representation with the diffusion representation, allowing the diffusion model to focus on the semantic structure of the image while the decoder handles perceptual details.

<!-- chunk {"id": "body-0067", "role": "body", "section": "VI-B Diffusion for Image Synthesis", "weight": 1.0} -->

proposes a simplified algorithm for both training and inference using diffusion models. Their approach improves performance in image synthesis and simplifies the hyperparameters required.

<!-- chunk {"id": "body-0068", "role": "body", "section": "VI-C Object Detection", "weight": 1.0} -->

Oriented object detection has been studied in many contexts. In contrast to other works, our problem setting simplifies the detection task in several ways. While aerial imagery and text recognition can deal with very large aspect ratios, the sizes and aspect ratios of our bounding boxes are more constrained by the dimensions of vehicles. Furthermore, each vehicle's bounding box has a canonical orientation (i.e. the direction the vehicle is facing), removing the ambiguity over how to define box orientation and the "angle boundary discontinuity" present in other works. While 2-stage and non-differentiable approaches have been explored for other oriented object detection tasks, in this work we desire an end-to-end differentiable approach that does not require extensive post-processing.

<!-- chunk {"id": "body-0069", "role": "body", "section": "CONCLUSIONS", "weight": 1.0} -->

In this work we presented a novel approach to generating complex driving scenes using diffusion in an end-to-end differentiable architecture that directly generates discrete agents. We also analyze the generalization capabilities of our model across multiple regions.

<!-- chunk {"id": "body-0070", "role": "body", "section": "CONCLUSIONS", "weight": 1.0} -->

Generating diverse, realistic, and complex driving scenarios is a key part of scaling the validation of autonomous driving systems. We believe this work provides a new approach to address this challenge that is more stable, controllable, and higher quality than prior approaches. In future work, we plan to extend these ideas beyond synthesis of the initial scenario to the time series generation of agents moving in a dynamic scenario. We hope this will contribute to the safe deployment of autonomous driving systems in the coming years.
