<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Scenario Diffusion: Controllable Driving Scenario Generation with Diffusion

Topics include Vehicles, Safety, Diffusion models, Object detection, Graphs, Regression, Control, Diffusion.

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Automated creation of synthetic traffic scenarios is a key part of validating the safety of autonomous vehicles (AVs). In this paper, we propose Scenario Diffusion, a novel diffusion-based architecture for generating traffic scenarios that enables controllable scenario generation. We combine latent diffusion, object detection and trajectory regression to generate distributions of synthetic agent poses, orientations and trajectories simultaneously. To provide additional control over the generated scenario, this distribution is conditioned on a map and sets of tokens describing the desired scenario. We show that our approach has sufficient expressive capacity to model diverse traffic patterns and generalizes to different geographical regions.

<!-- chunk {"id": "body-0003", "role": "body", "section": "Introduction", "weight": 1.5} -->

Automated creation of synthetic traffic scenarios is a key part of validating the safety of autonomous vehicles (AVs). To efficiently target rare and safety critical scenarios we would like to direct scenario generation to produce specific types of events. Prior methods for heuristically created scenarios tend to be of limited complexity and miss a large number of possible real-world situations. Recent works using deep learning models are able to produce complex scenarios conditioned on a map region, but do not offer additional controls over the generation process. In this paper we propose Scenario Diffusion: a novel architecture for generating realistic traffic scenarios that enables *controllable* scenario generation.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

Our problem setting is to generate a set of bounding boxes with associated trajectories that describe the location and behavior of agents in a driving scenario. We accomplish this scenario generation using a denoising diffusion generative model. We condition our model on both a map image and a set of tokens describing the scenario. We leverage these tokens to provide a variable rate of control over the generated scenario, so that the diffusion model can generalize to complex scenes conditioned only on a small set of tokens that control both a subset of the individual agents and global scene properties. Further, this variable rate of control allows us to learn the model from partially tokenized training instances, substantially reducing the labelling requirements.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

Motivated by the insight that the instantaneous position of each agent is inextricably linked to their behaviors, we combine latent diffusion, object detection, and trajectory regression to simultaneously generate both oriented bounding boxes and trajectories, providing a generative model of both the static placement of agents and their behaviors. We evaluate Scenario Diffusion at generating driving scenarios conditioned on only the map, and with additional conditioning tokens as well. Finally, we provide an analysis of the generalization capabilities of our model across geographical regions, showing that our diffusion-based approach has sufficient expressive capacity to model diverse traffic patterns.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Problem Setting", "weight": 1.0} -->

We aim to generate traffic scenarios conditioned on a map and an optional description of the scenario. Similar to prior works we represent traffic scenarios abstractly with oriented bounding boxes and trajectories^11^1Our simulations are abstract representations that are produced by perception systems. While photorealistic simulation would also allow the perception system to be tested in the loop, in this work we focus on scenario generation that tests planning and decision making for computational tractability.. AV software is typically divided into *perception* and *motion planning*. The interface between these components describes agents with bounding boxes, historical trajectories, and additional attributes. In simulation this abstract representation is synthesized to evaluate the motion planning component in isolation, alleviating the need for expensive photorealistic simulation.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Problem Setting", "weight": 1.0} -->

Fig. 1 demonstrates the type of controllability we aim to achieve. We condition the generative model by describing the state of two vehicles: the AV (circled in red) and one key interacting agent (circled in orange). The model is able to generate a diverse set of scenarios that include these two agents and additional ones. Notably, describing the two key agents does not require having observed such agents in the real world (e.g. by copying these two agents from an existing log). Instead, the model is able to generalize to generating novel agents based on the given description.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Scenario Representation", "weight": 1.0} -->

In this work we use topdown birds' eye view (BEV) representations similar to for the inputs to convolutional networks and sparse representations of oriented boxes and trajectories as the final output of the decoder.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Topdown Representations", "weight": 1.0} -->

The map context is represented as a multi-channel BEV image $m$ of shape $C_{m} \times H \times W$ that contains information about road geometry, regions of interest (e.g. driveways, crosswalks), and traffic control devices (e.g. stop signs, traffic lights). Agents are also represented in a multi-channel BEV image $x$ of shape $C_{x} \times H \times W$ that encodes each agent's bounding box, heading, and trajectory. Sec. 4.1 describes two different datasets with different rendering styles for $m$ and $x$ that both yield good results with our model.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Sparse Representations", "weight": 1.0} -->

We also represent the agents in the scene as a set of oriented bounding boxes, with associated trajectories included as an additional feature vector per box. The oriented bounding box is defined by a center position, heading, length, and width and the agent trajectory as a sequence of future and past poses spaced at uniform intervals in time, as is common in motion forecasting, with the bounding box pose representing the "current timestep". This sparse representation is used as the labels for the autoencoder's detection task and to compute tokens describing agents in the scenario.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Method", "weight": 1.0} -->

As, our diffusion model consists of two parts: an autoencoder to transform between the data space and a latent space and a diffusion model that operates in this latent space.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Scenario Autoencoder", "weight": 1.0} -->

The scene autoencoder is a variational autoencoder (VAE) that learns to encode and decode sets of agents as shown in Fig. 2(a). The VAE is trained with a combination of a reconstruction loss $\mathcal{L}_{\text{rec}}$ on the decoder output and a KL divergence loss $\mathcal{L}_{\text{KL}}$ on the latent embedding. The architecture is based on the autoencoder of, but we train the model to perform anchor-free one-to-one detection instead of pixelwise image reconstruction.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Scenario Autoencoder", "weight": 1.0} -->

An encoder $\mathcal{E}$ takes the BEV image of the agents in the scene $x$ and outputs a latent embedding $z = {\mathcal{E}{(x)}}$ of shape $C_{z} \times H^{\prime} \times W^{\prime}$, where $H^{\prime} = {H/2^{f}}$ and $W^{\prime} = {W/2^{f}}$ for a downsampling factor $f \in {\mathbb{N}}$. Since the encoder is designed to capture the placement of agents, there was empirically no benefit to providing the map image as input to the encoder.

<!-- chunk {"id": "body-0014", "role": "body", "section": "Scenario Autoencoder", "weight": 1.0} -->

This latent embedding is given to the decoder $\mathcal{D}$ along with the BEV map image $m$ to obtain the detection output $y = {\mathcal{D}{(z,m)}}$ of shape $C_{y} \times H^{\operatorname{\prime\prime}} \times W^{\operatorname{\prime\prime}}$. Because we output detections, $H^{\operatorname{\prime\prime}}$ and $W^{\operatorname{\prime\prime}}$ do not need to equal $H$ and $W$, the original input shapes. In practice, having a lower output resolution provides significant memory savings during training.

<!-- chunk {"id": "body-0015", "role": "body", "section": "Scenario Autoencoder", "weight": 1.0} -->

The decoder downsamples the map image $m$, concatenates the latent embedding $z$, and then upsamples to produce the final output: ${\mathcal{D}{(z,m)}} = {\mathcal{D}_{\text{up}}\left( z,{\mathcal{D}_{\text{down}}{(m)}} \right)}$.

<!-- chunk {"id": "body-0016", "role": "body", "section": "Detection Outputs", "weight": 1.0} -->

The decoder output $y$ represents oriented bounding box detections and trajectories. Each pixel of $y$ represents one box proposal, with different channels representing the probability, position, heading, length, width, and trajectory of the box. Concretely, the first channel is a sigmoid logit for the box probability. The second and third channels represent the cosine and sine of the box orientation. The next four channels represent the distances from the pixel center to the front, left, back, and right edges of the box in log scale. These seven channels define the oriented bounding box for the agent.

<!-- chunk {"id": "body-0017", "role": "body", "section": "Detection Outputs", "weight": 1.0} -->

The trajectory describes the agent's pose from $T$ seconds in the past to $T$ seconds in the future at one second intervals. For each timestep $t \in {\{ 1,\ldots,T\}}$ of the future trajectory three channels of $y$ represent the delta between the pose at $t$ and the pose at $t - 1$ (with channels for x, y, and heading). These deltas are accumulated to produce the final trajectory starting from the center pose of the oriented bounding box. The past trajectory is handled symmetrically (i.e. deltas between $t$ and $t + 1$ for $t \in {\{{- T},\ldots,{- 1}\}}$). In total 1 channel encodes the box probability, 6 channels encode the oriented bounding box, and $6T$ channels encode the trajectory.

<!-- chunk {"id": "body-0018", "role": "body", "section": "Reconstruction Loss", "weight": 1.0} -->

The reconstruction loss used to train the autoencoder adapts the one-to-one detection loss of to accommodate oriented boxes. Given the simplicity of our detection problem (perfectly rendered rectangles with disambiguated orientations) we find that replacing the IoU loss (which is non-differentiable with oriented boxes) with an L2 loss on the box vertices yields detection performance sufficient for training the diffusion model. Following, each ground truth box is matched with one predicted box by selecting the predicted box that minimizes a matching score between it and the ground truth box. This matching score is a weighted combination of a classification score, L1 loss on the box parameters, and an L2 loss on the box vertices. A classification loss encourages matched predicted boxes to have high probability and unmatched predicted boxes to have low probability, and regression losses encourage matched predicted boxes and trajectories to equal their corresponding ground truth box. We use a weighted combination of an L1 loss on box parameters, L2 loss on box vertices, L2 loss on trajectory positions, and cosine loss on the trajectory headings. Further details on the reconstruction loss can be found in Sec. B.2.

<!-- chunk {"id": "body-0019", "role": "body", "section": "Diffusion Fundamentals", "weight": 1.0} -->

Once the autoencoder is trained, a diffusion model is trained in the latent space of the autoencoder. This means that the diffusion model does not operate on bounding boxes and trajectories directly. We use the EDM diffusion algorithm to train our model and generate novel scenarios.

<!-- chunk {"id": "body-0020", "role": "body", "section": "Training", "weight": 1.0} -->

Let $\hat{z} = {\mathcal{E}{(x)}}$ be the latent embedding obtained from a trained and frozen encoder. Each example can also include associated conditional information $c$ (e.g., map information, tokens). We discuss options for this conditional data in following sections.

<!-- chunk {"id": "body-0021", "role": "body", "section": "Training", "weight": 1.0} -->

For each training example we sample $\sigma$ according to a log-normal distribution (i.e. ${\log\sigma} \sim {\mathcal{N}\left( P_{\mu},P_{\sigma}^{2} \right)}$ with hyperparameters $P_{\mu}$ and $P_{\sigma}$). We then create a noisy sample $z = {\hat{z} + {\sigma\epsilon}}$, where $\epsilon$ has the same shape as $\hat{z}$ and is sampled from the standard normal distribution.

<!-- chunk {"id": "body-0022", "role": "body", "section": "Training", "weight": 1.0} -->

We train the denoising model $\mathcal{M}{(z;c,\sigma)}$ by minimizing the reconstruction loss

<!-- chunk {"id": "body-0023", "role": "body", "section": "Training", "weight": 1.0} -->

where $c_{\text{in}}{(\sigma)}$, $c_{\text{out}}{(\sigma)}$, $c_{\text{skip}}{(\sigma)}$, and $\lambda{(\sigma)}$ are all scalar functions of $\sigma$ as defined. In practice this model $\mathcal{M}$ is a conditional Unet as. This process is depicted in Fig. 2(b). Given a noisy sample $z$, the denoised version $\hat{z}$ can be estimated as

<!-- chunk {"id": "body-0024", "role": "body", "section": "Inference", "weight": 1.0} -->

To generate novel samples during inference, we start with an initial noisy sample $z \sim {\mathcal{N}\left( 0,{\sigma_{\text{max}}^{2}\mathbf{I}} \right)}$. This sample is iteratively refined according to the reverse process ODE as described. The gradient of the log probability distribution can be approximated as ${{{\nabla_{z}\log}p}{(z;c,\sigma)}} \approx {\left( {{M{(z;c,\sigma)}} - z} \right)/\sigma^{2}}$. This simplifies the reverse process ODE to

<!-- chunk {"id": "body-0025", "role": "body", "section": "Inference", "weight": 1.0} -->

After integrating the sample $z$ from $\sigma = \sigma_{\text{max}}$ to $\sigma = 0$ using Euler integration, it is passed through the decoder to obtain the generated boxes and trajectories $\mathcal{D}{(z,m)}$. This procedure is depicted in Fig. 2(c). During inference we keep the generated boxes with probability above a fixed threshold chosen by optimizing a metric that compares generated and ground truth boxes (described in Sec. 4.1). We then filter any overlapping boxes, keeping the highest probability box of those that overlap.

<!-- chunk {"id": "body-0026", "role": "body", "section": "Diffusion Conditioning", "weight": 1.0} -->

Conditional Unet models have two primary ways to provide the conditional information $c$: concatenating to the noisy sample that is input to the denoising model and applying cross attention over a set of tokens inside the denoising model. We explore both options in this work.

<!-- chunk {"id": "body-0027", "role": "body", "section": "Map Conditioning", "weight": 1.0} -->

One method to include conditional data in the denoising model is via a conditional image that gets concatenated with the noisy sample input to the denoising model. In this work we use the BEV map image $m$ as described in Sec. 2.1 as the conditional image. The map image $m$ is first processed by a separate encoder $\mathcal{E}_{m}$ to downsample it to the same pixel dimension as $z$. The encoded map $\mathcal{E}_{m}{(m)}$ is concatenated with $z$ in the channel dimension before being input to the denoising Unet $\mathcal{M}$.

<!-- chunk {"id": "body-0028", "role": "body", "section": "Token Conditioning", "weight": 1.0} -->

We can also condition diffusion models on a set of tokens via a cross-attention mechanism within the denoising model. In image generation these tokens often come from text embeddings of a caption for the image. While we do not have datasets of driving scenarios fully annotated with text captions, we can still use the concept of conditional tokens that describe aspects of the scenario. It is exactly these tokens that provide *controllability* over scenario generation. In this work we explore two types of tokens: *agent tokens* and *global scene tokens*.

<!-- chunk {"id": "body-0029", "role": "body", "section": "Agent Tokens", "weight": 1.0} -->

Agent tokens are tokens that describe a single agent. In this work we use procedurally generated tokens (i.e. tokens that can be computed from available data in the dataset), so are able to provide a token for every agent. However that is not a requirement for this approach; if using human-labeled tokens it would be possible to train a diffusion model while only having partially labeled scenarios. The token feature vector for each agent expresses various quantities that we might want associated with that agent, such as the agent's position, speed, length, or motion profile. In this work the meaning of the token feature vector is fixed for a given experiment. One potential direction for future work is to have a single model support multiple types of agent token feature embeddings (e.g. to allow the user to specify the length for one agent and the speed for another).

<!-- chunk {"id": "body-0030", "role": "body", "section": "Agent Tokens", "weight": 1.0} -->

To enable the model to generate agents not described by tokens we use a partial tokenization strategy. During training we achieve this by sampling a token mask probability $p_{\text{mask}}$ and masking out agent tokens with this probability. More information on this can be found in Sec. 4.3.1.

<!-- chunk {"id": "body-0031", "role": "body", "section": "Global Scene Tokens", "weight": 1.0} -->

Global scene tokens encode scalar quantities that allow us to control global properties of the entire scenario. In this work we consider a single global scene token to represent $p_{\text{mask}}$, which encodes information about the number of agents to be generated relative to the number of tokens provided. During inference the value represented by this global scene token can be modulated to control the number of agents in the generated scenarios. By providing no agent tokens and setting $p_{\text{mask}} = 1$ in the global scene token we are able to generate scenarios conditioned on only the map from the same model.

<!-- chunk {"id": "body-0032", "role": "body", "section": "Processing", "weight": 1.0} -->

Each type of token is processed by a separate MLP to get final embeddings in a common latent space, to be used as keys and values during cross-attention inside the denoising model. At different levels of the Unet each pixel from the intermediate image representation is used as a query, and the agent and global scene tokens are used as the keys and values. This architecture can support any number of tokens. We refer the reader to for more details on the cross-attention mechanism.

<!-- chunk {"id": "body-0033", "role": "body", "section": "Datasets", "weight": 1.0} -->

We use two datasets in this work. The Argoverse 2 motion forecasting dataset contains 250,000 driving scenarios over 6 geographical regions representing 763 hours of total driving. We use the provided training and validation splits. More information about this dataset can be found in Sec. A.1.

<!-- chunk {"id": "body-0034", "role": "body", "section": "Datasets", "weight": 1.0} -->

The second dataset is an internal dataset containing 6 million real world driving scenarios from Las Vegas (LV), Seattle (SEA), San Francisco (SF), and the campus of the Stanford Linear Accelerator Center (SLAC). Training and validation data are not separated by location, so a given validation example may have training examples from the same location at other times. More information about this dataset can be found in Sec. A.2.

<!-- chunk {"id": "body-0035", "role": "body", "section": "Datasets", "weight": 1.0} -->

For both datasets, the scenes are centered on the autonomous vehicle. As the autonomous vehicle is treated as just another vehicle during training, the model almost always places a vehicle in the center of the scene during inference. We use a 2 second time horizon for both the future and the past trajectory (i.e. the bounding box represents $t = 0$ and the trajectory goes from $t = {- 2}$ to $t = 2$). This time window is sufficient to populate the agent history for many motion forecasting methods.

<!-- chunk {"id": "body-0036", "role": "body", "section": "Training", "weight": 1.0} -->

See Appendix B and for details of training the autoencoder and Appendix C for details of training the diffusion model.

<!-- chunk {"id": "body-0037", "role": "body", "section": "Inference", "weight": 1.0} -->

We use 80% as the threshold for the generated box probabilities. See Sec. D.2 for the ablation experiment used to select this threshold. We note that the performance of Scenario Diffusion is relatively robust to choices of probability threshold between 50% and 90%.

<!-- chunk {"id": "body-0038", "role": "body", "section": "Metrics", "weight": 1.0} -->

We consider metrics to compare the generated and data distributions and measure the quality of generated scenarios. One popular metric for comparing two distributions using samples is the maximum mean discrepancy (MMD). While this metric is typically defined in terms of two distributions, in practice we compute this metric using samples drawn from the two distributions. Given two sets $A$ and $B$ generated by sampling from two distributions and some kernel $k$, the maximum mean discrepancy is defined as

<!-- chunk {"id": "body-0039", "role": "body", "section": "Metrics", "weight": 1.0} -->

Similar to, we use a Gaussian kernel $k$ and apply this metric to the sets of agent center positions, heading unit vectors, and velocities, all in ${\mathbb{R}}^{2}$.

<!-- chunk {"id": "body-0040", "role": "body", "section": "Metrics", "weight": 1.0} -->

To measure the quality of generated trajectories we compute the fraction of waypoints that fall within the drivable area, averaged over all generated agents and all 5 trajectory waypoints. For each predicted pose along the trajectory we also compute the minimum angle difference (in radians) between the pose heading and the heading of all lanes at that location. These metrics do not have a clear optimal value (trajectories in the Argoverse dataset sometimes leave the drivable area and aren't perfectly aligned with the lane tangent); we compare the metric between the dataset and generated scenarios.

<!-- chunk {"id": "body-0041", "role": "body", "section": "Baselines", "weight": 1.0} -->

As a simple heuristic baseline we implement Random Log Selection, which takes the agents from a random sample in the training dataset (ignoring map information). We also report the trajectory metrics on the ground truth validation samples themselves.

<!-- chunk {"id": "body-0042", "role": "body", "section": "Baselines", "weight": 1.0} -->

To compare our method to previous autoregressive approaches we adapt TrafficGen to the Argoverse 2 dataset. See Appendix E for more details on the modifications needed.

<!-- chunk {"id": "body-0043", "role": "body", "section": "Map-Conditioned Scenario Generation", "weight": 1.0} -->

We first evaluate Scenario Diffusion in generating scenarios conditioned on only map data, the problem setting explored in prior works. In Tab. 1 we report MMD metrics that compare generated and ground truth scenes and trajectory metrics that measure how well the trajectories conform to the map. We evaluate Scenario Diffusion models with and without the map context $m$, and compare against the baselines described above.

<!-- chunk {"id": "body-0044", "role": "body", "section": "Map-Conditioned Scenario Generation", "weight": 1.0} -->

Scenario Diffusion outperforms all other methods in the MMD metric for position and heading, and performs equally with TrafficGen in velocity. In the trajectory metrics, Scenario Diffusion produces similar values as those of the ground truth logs. As expected, Scenario Diffusion without map context performs similarly to random log selection, as both methods ignore the map context.

<!-- chunk {"id": "body-0045", "role": "body", "section": "Token Conditioning", "weight": 1.0} -->

We next explore applications of token conditioning in Scenario Diffusion. Fig. 1 demonstrates how tokens can be used to generate scenarios with a specific type of interaction between the AV and another agent. Our approach is able to generate these interactions without having to fully specify the box and trajectory for the agent (e.g. by hand or by copying an agent from an existing log). By using more abstract features in the agent tokens we allow the model to generate different scenarios that meet the given description (e.g. we do not prescribe the specific trajectory of the u-turning agent).

<!-- chunk {"id": "body-0046", "role": "body", "section": "Token Conditioning", "weight": 1.0} -->

The flexibility of tokens provides variable degrees of control over the generated scenarios. In this work we demonstrate models that use a variety of features in the agent tokens, such as position, heading, length, and speed. More details on the exact token features can be found in Sec. C.3.

<!-- chunk {"id": "body-0047", "role": "body", "section": "Partial Tokenization", "weight": 1.0} -->

It is crucial that the learned model be robust to the presence or absence of user-provided tokens. To ensure this, during training we omit or "mask" supervision tokens so that the model learns to fill in additional agents in the scenario. During training we select $p_{\text{mask}}$ such that 40% of the time we keep all tokens (i.e. $p_{\text{mask}} = 0$) and the other 60% of the time we sample $p_{\text{mask}} \sim {\text{Beta}{}}$.^22^2Simpler choices such as sampling $p_{\text{mask}}$ from a uniform distribution over yields similar results when fully trained. Empirically we find the chosen mixture distribution yields faster convergence. For each sample, the chosen masking probability is bucketed into one of ten bins (\0, 0.1), \[0.1, 0.2), etc.) and embedded as a one-hot vector to define the global scene token.

<!-- chunk {"id": "body-0048", "role": "body", "section": "Partial Tokenization", "weight": 1.0} -->

This global scene token and the agent tokens that remain after masking are used to condition the diffusion model as described in [Sec. 3.3.2.

<!-- chunk {"id": "body-0049", "role": "body", "section": "Partial Tokenization", "weight": 1.0} -->

During inference we can modulate the value represented by the global scene token to control how many additional agents the model generates beyond those described by agent tokens. Fig. 3 shows scenarios generated by the model using a fixed map, three agent tokens, and the global scene token. All scenarios contain the three agents described by the tokens. As the value set in the global scene token increases, the model infers that there are additional agents not described by tokens. This approach allows a user to specify certain agents while having the model fill in the remainder of the scenario. Using this formulation we are able to emulate a model conditioned on only the map image by setting the global scene token to 100% and providing no additional agent tokens.

<!-- chunk {"id": "body-0050", "role": "body", "section": "Partial Tokenization", "weight": 1.0} -->

We first evaluate the model's ability to use the token information by matching generated agents to tokens. We take samples from the Argoverse validation dataset, compute agent tokens from the ground truth scene, and apply a fixed amount of agent token masking. We generate scenes conditioned on these tokens and compute a one-to-one matching between generated agents and agent tokens using the Hungarian algorithm. We only consider pairs that are within 2.2 meters (we discretize position into bins of width 1.56m, and ${1.56 \ast \sqrt{2}} \approx 2.2$) and 0.2 radians. In Tab. 2 we report the agent token match rate (what percentage of agent tokens were matched to a corresponding generated agent) and the number of additional generated agents per scene (those unmatched to an agent token). As the value of $p_{\text{mask}}$ increases the agent token match rate stays at 96-97% while the average number of additional agents increases roughly linearly, showing that the model is able to follow both agent and global scene tokens.

<!-- chunk {"id": "body-0051", "role": "body", "section": "Token Controllability", "weight": 1.0} -->

To evaluate how well the model uses other information in the agent tokens we compare models that use different agent token features. We run inference conditioned on agent tokens computed from the ground truth sample as in Sec. 4.3.1. For these experiments we use no token dropout (i.e. $p_{\text{mask}} = 0$). We perform the same matching between generated and ground truth agents and report the agent token match rate as in the previous section. For each matched pair, we compute the error of the current speed and final (i.e. $t = 2$) speed. In Tab. 3 we report the mean absolute error (MAE) over all matched pairs, again showing the mean and standard deviation of this metric across multiple models trained with different initial random seeds. As described in Sec. C.3, the speed features are discretized into bins of width 2 m/s, so these models are not expected to achieve perfect reconstruction.

<!-- chunk {"id": "body-0052", "role": "body", "section": "Token Controllability", "weight": 1.0} -->

Adding current speed to the agent tokens significantly decreases the MAE for current speed and somewhat decreases it for final speed (as the current and final speed are correlated). Adding a final speed feature to the agent tokens further reduces the MAE for final speed. Adding these additional agent features does not significantly impact the agent token match rate.

<!-- chunk {"id": "body-0053", "role": "body", "section": "Token Controllability", "weight": 1.0} -->

Agent token match rate (↑)
Current speed MAE (↓)
Final speed MAE (↓)

<!-- chunk {"id": "body-0054", "role": "body", "section": "Relationship Between Agents", "weight": 1.0} -->

One of the key contributions of our work is to generate bounding boxes and trajectories simultaneously for all agents. Doing so allows the generated outputs to capture not just a static snapshot of the scene but also the behavior of various agents. This joint inference of the placement and behavior of agents is particularly important for controlled scenario generation using agent tokens. The behavior described by agent tokens influences where other agents can be placed. Approaches that separate initial placement and behavior into two models are not able to perform this joint reasoning.

<!-- chunk {"id": "body-0055", "role": "body", "section": "Relationship Between Agents", "weight": 1.0} -->

Fig. 4 shows scenarios generated using one agent token, with features for the position, heading, extents, current speed, and final speed (i.e. at +2s). Both cases use the same position, heading, extents, and current speed (set to 0 m/s); the only difference is the final speed. For this vehicle stopped at an intersection, its future behavior implies which lanes have right-of-way through the intersection. When the future speed is 0 m/s (resp., 8 m/s) the model generates additional agents traveling vertically (resp., horizontally).

<!-- chunk {"id": "body-0056", "role": "body", "section": "Generalization Across Geographic Region", "weight": 1.0} -->

To evaluate the ability to generalize across regions, we train models on data from each region of the internal dataset separately. We then evaluate these models and models trained on the full dataset on validation splits for each region. Results are shown in Tab. 4. Each entry is an average across 5 experiments with different random seeds, with the standard deviation reported in parentheses.

<!-- chunk {"id": "body-0057", "role": "body", "section": "Generalization Across Geographic Region", "weight": 1.0} -->

In each region, models trained on that region tend to outperform models trained on other regions. The models trained on the full dataset come close to the region-specialized models. This suggests that there are unique aspects of each region, and that the full model has sufficient capacity to capture this diversity. SLAC is the most distinct from the other regions and shows the largest generalization gap. Additional metrics can be found in Sec. D.3; they follow the same pattern as in Tab. 4.

<!-- chunk {"id": "body-0058", "role": "body", "section": "Generalization Across Geographic Region", "weight": 1.0} -->

Fig. 5 shows examples of models generalizing across the three metropolitan regions (LV, SEA, and SF). The model trained on San Francisco data is able to produce reasonable scenes in Seattle, and vice versa. This suggests the potential to produce validation data for new regions before large volumes of driving logs in the new regions have been collected.

<!-- chunk {"id": "body-0059", "role": "body", "section": "Generalization Across Geographic Region", "weight": 1.0} -->

Generalizing to dissimilar regions is significantly harder. Fig. 6 shows examples of generalization between LV (a major metropolitan area) and SLAC (a suburban academic campus). Not surprisingly, models trained on each of these two regions performs worse when applied to the other. For example, the LV model does not generate realistic parked vehicles in the parking lots from SLAC and the SLAC model generates vehicles facing against the lane direction at locations in LV. Fortunately, the model trained on the full dataset is able to produce high quality scenarios in both regions.

<!-- chunk {"id": "body-0060", "role": "body", "section": "Related Works", "weight": 1.0} -->

A number of prior works have used heuristics or fixed grammars to generate driving scenes. Such approaches are limited in their ability to generate complex and diverse driving scenes. SceneGen and TrafficGen use an autoregressive approach, adding agents one at a time. TrafficGen adds a second stage where a motion forecasting model is used to generate trajectories for the boxes. SimNet uses a conditional generative adversarial network to generate a BEV occupancy image. Heuristic post-processing is applied to identify connected components and fit bounding boxes to them. A second agent-centric model is then used to generate trajectories for these agents over time. In contrast, our method directly produces bounding boxes and trajectories simultaneously for all agents in an end-to-end differentiable architecture. Our approach also does not constrain vehicles to be in lane, as in TrafficGen and several heuristic approaches.

<!-- chunk {"id": "body-0061", "role": "body", "section": "Related Works", "weight": 1.0} -->

A number of works generate future trajectories for already-existing agents in simulation. Some focus on specifically producing adversarial future trajectories given agents' initial states. These approaches are complementary to our work, and can be used to extend trajectories beyond what is output by Scenario Diffusion.

<!-- chunk {"id": "body-0062", "role": "body", "section": "Conclusion", "weight": 1.5} -->

In this paper, we demonstrate a novel technique for using diffusion to learn to generate scenarios of dynamic agents moving through an environment for the purposes of testing an autonomous vehicle's ability to navigate through that environment and plan according to those agents. We have shown that our technique leads to models that not only appropriately capture the desired distributions of scenarios and agent trajectories, but allow scenario generation to be controlled to target specific types of scenarios. The fact that diffusion allows declarative information such as tokens to be combined with models learned from data creates the potential for new models that combine other forms of symbolic knowledge such as traffic rules, physical constraints, and common sense reasoning.

<!-- chunk {"id": "body-0063", "role": "body", "section": "Conclusion", "weight": 1.5} -->

More work is required to show broader generalization. The training data assumes a specific model of perception in the form of bounding boxes and trajectory models. Additionally, we restricted the agent models to on-road vehicle models. While we do not anticipate significant challenges in applying this model to other forms of agents such as pedestrians, we have not incorporated those agents in the research described here. In simulation this approach may need to be extended to iteratively generate agents over a larger region as the AV navigates through the environment.

<!-- chunk {"id": "body-0064", "role": "body", "section": "Conclusion", "weight": 1.5} -->

Broader Impact: This paper focuses on developing models to improve self-driving car technologies. There are many positive and negative aspects to the development of self-driving cars that depend as much on the system-wide design and regulatory aspects as these aspects depend on the technical capabilities. However, the focus on simulation in this paper should partially reduce the risks of deploying self-driving cars by providing more effective and systematic coverage of testing scenarios.
