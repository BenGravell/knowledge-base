<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

MultiPath: Multiple Probabilistic Anchor Trajectory Hypotheses for Behavior Prediction

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Predicting human behavior is a difficult and crucial task required for motion planning. It is challenging in large part due to the highly uncertain and multi-modal set of possible outcomes in real-world domains such as autonomous driving. Beyond single MAP trajectory prediction, obtaining an accurate probability distribution of the future is an area of active interest. We present MultiPath, which leverages a fixed set of future state-sequence anchors that correspond to modes of the trajectory distribution. At inference, our model predicts a discrete distribution over the anchors and, for each anchor, regresses offsets from anchor waypoints along with uncertainties, yielding a Gaussian mixture at each time step. Our model is efficient, requiring only one forward inference pass to obtain multi-modal future distributions, and the output is parametric, allowing compact communication and analytical probabilistic queries. We show on several datasets that our model achieves more accurate predictions, and compared to sampling baselines, does so with an order of magnitude fewer trajectories.

<!-- chunk {"id": "body-0003", "role": "body", "section": "Introduction", "weight": 1.5} -->

We focus on the problem of predicting future agent states, which is a crucial task for robot planning in real-world environments. We are particularly interested in addressing this problem for self-driving vehicles, an application with a potentially enormous societal impact. Importantly, predicting the future of other agents in this domain is vital for safe, comfortable and efficient operation. For example, it is important to know whether to yield to a vehicle if they are going to cut in front of our robot or when would be the best time to merge into traffic. Such future prediction requires an understanding of the static and dynamic world context: road semantics (*e.g*., lane connectivity, stop lines), traffic light information, and past observations of other agents, as depicted in Fig. 1.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

A fundamental aspect of future state prediction is that it is inherently stochastic, as agents cannot know each other's motivations. When driving, we can never really be sure what other drivers will do next, and it is important to consider multiple outcomes and their likelihoods.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

We seek a model of the future that can provide both a weighted, parsimonious set of discrete trajectories that covers the space of likely outcomes and a closed-form evaluation of the likelihood of any trajectory. These two attributes enable efficient reasoning in crucial planning use-cases, for example, human-like reactions to discrete trajectory hypotheses (*e.g*., yielding, following), and probabilistic queries such as the expected risk of collision in a space-time region.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

Both of these attributes present modeling challenges. Models which try to achieve diversity and coverage often suffer from mode collapse during training, while tractable probabilistic inference is difficult due to the space of possible trajectories growing exponentially over time.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

Our MultiPath model addresses these issues with a key insight: it employs a fixed set of trajectory anchors as the basis of our modeling. This lets us factor stochastic uncertainty hierarchically: First, intent uncertainty captures the uncertainty of what an agent intends to do and is encoded as a distribution over the set of anchor trajectories. Second, given an intent, control uncertainty represents our uncertainty over how they might achieve it. We assume control uncertainty is normally distributed at each future time step, parameterized such that the mean corresponds to a context-specific offset from the anchor state, with the associated covariance capturing the unimodal aleatoric uncertainty. Fig. 1 illustrates a typical scenario where there are 3 likely intents given the scene context, with control mean offset refinements respecting the road geometry, and control uncertainty intuitively growing over time.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Introduction", "weight": 1.5} -->

Our trajectory anchors are modes found in our training data in state-sequence space via unsupervised learning. These anchors provide templates for coarse-granularity futures for an agent and might correspond to semantic concepts like "change lanes", or "slow down" (although to be clear, we don't use any semantic concepts in our modeling).

<!-- chunk {"id": "body-0009", "role": "body", "section": "Introduction", "weight": 1.5} -->

Our complete model predicts a Gaussian mixture model (GMM) at each time step, with the mixture weights (intent distribution) fixed over time. Given such a parametric distribution model, we can directly evaluate the likelihood of any future trajectory and also have a simple way to obtain a compact, diverse weighted set of trajectory samples: the MAP sample from each anchor-intent.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Introduction", "weight": 1.5} -->

Our model contrasts with popular past approaches which either provide only a single MAP trajectory or an unweighted set of samples via a generative model. There are a number of downsides to sample-based methods when it comes to real-world applications such as self-driving vehicles: non-determinism in a safety critical system, a poor handle on approximation error (e.g,. "how many samples must I draw to know the chance the pedestrian will jaywalk?"), no easy way to perform probabilistic inference for relevant queries, such as computing expectations over a spacetime region.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Introduction", "weight": 1.5} -->

We demonstrate empirically that our model emits distributions which predict the observed outcomes better on synthetic and real-world prediction datasets: we achieve higher likelihood than a model which emits unimodal parametric distributions, showing the importance of multiple anchors in real-world data. We also compare to sampling-based methods by using our weighted set of MAP trajectories per anchor, which describe the future better with far fewer samples on sample-set metrics.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Method", "weight": 1.0} -->

Given observations $\mathbf{x}$ in the form of past trajectories of all agents in a scene and possibly additional contextual information (*e.g*., lane semantics, traffic light states), MultiPath seeks to provide a parametric distribution over future trajectories $\mathbf{s}$: $p{(\left. \mathbf{s} \middle| \mathbf{x} \right.)}$, and a compact weighted set of explicit trajectories which summarizes this distribution well.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Method", "weight": 1.0} -->

Let $t$ denote a discrete time step, and let $s_{t}$ denote the state of an agent at time $t$, the future trajectory $\mathbf{s} = {\lbrack s_{1},\ldots,s_{T}\rbrack}$ is a sequence of states from $t = 1$ to a fixed time horizon $T$. We also refer to a state in a trajectory as a waypoint.

<!-- chunk {"id": "body-0014", "role": "body", "section": "Method", "weight": 1.0} -->

We factorize the notion of uncertainty into independent quantities. Intent uncertainty models uncertainty about the agents' latent coarse-scale intent or desired goal. For example, in a driving context, uncertainty about which lane the agent is attempting to reach. Conditioned on intent, there is still control uncertainty, which describes the uncertainty over the sequence of states the agent will follow to satisfy its intent. Both intent and control uncertainty depend on the past observations of static and dynamic world context $\mathbf{x}$.

<!-- chunk {"id": "body-0015", "role": "body", "section": "Method", "weight": 1.0} -->

The Gaussian parameters $\mu_{t}^{k}$ and $\Sigma_{t}^{k}$ are directly predicted by our model as a function of $\mathbf{x}$ for each time-step of each anchor trajectory $\mathbf{a}_{t}^{k}$. Note in the Gaussian distribution mean, $a_{t}^{k} + \mu_{t}^{k}$, the $\mu_{t}^{k}$ represents a scene-specific offset from the anchor state $a_{t}^{k}$; it can be thought of as modeling a scene-specific residual or error term on top of the prior anchor distribution. This allows the model to refine the static anchor trajectories to the current context, with variations coming, *e.g*. specific road geometry, traffic light state, or interactions with other agents.

<!-- chunk {"id": "body-0016", "role": "body", "section": "Method", "weight": 1.0} -->

The time-step distributions are assumed to be conditionally independent given an anchor, *i.e*., we write $\phi{(\left. s_{t} \middle| \cdot \right.)}$ instead of $\phi{(\left. s_{t} \middle| {\cdot,s_{1:{t - 1}}} \right.)}$. This modeling assumption allows us to predict for all time steps jointly with a single inference pass, making our model simple to train and efficient to evaluate. If desired, it is straightforward to add a conditional next-time-step dependency to our model, using a recurrent structure (RNN).

<!-- chunk {"id": "body-0017", "role": "body", "section": "Method", "weight": 1.0} -->

Note that this yields a Gaussian Mixture Model distribution, with mixture weights fixed over all time steps. This is a natural choice to model both types of uncertainty: it has rich representational power, a closed-form partition function, and is also compact. It is easy to evaluate this distribution on a discretely sampled grid to obtain a probabilistic occupancy grid, more cheaply and with fewer parameters than a native occupancy grid formulation.

<!-- chunk {"id": "body-0018", "role": "body", "section": "Method", "weight": 1.0} -->

Obtaining anchor trajectories. Our distribution is parameterized by anchor trajectories $\mathcal{A}$. As noted, directly learning a mixture suffers from issues of mode collapse. As is common practice in other domains such as object detection and human pose estimation, we estimate our anchors a-priori before fixing them to learn the rest of our parameters. In practice, we used the k-means algorithm as a simple approximation to obtain $\mathcal{A}$ with the following squared distance between trajectories: ${d{(\mathbf{u},\mathbf{v})}} = {\sum_{t}^{T}{\|{{M_{u}\mathbf{u}_{t}} - {M_{v}\mathbf{v}_{t}}}\|}_{2}^{2}}$, where $M_{u},M_{v}$ are affine transformation matrices which put trajectories into a canonical rotation- and translation-invariant agent-centric coordinate frame.

<!-- chunk {"id": "body-0019", "role": "body", "section": "Method", "weight": 1.0} -->

In Sec. 4, on some datasets, k-means leads to highly redundant clusters due to prior distributions that are heavily skewed to a few common modes. To address this, we employ a simpler approach to obtain $\mathcal{A}$ by uniformly sampling trajectory space.

<!-- chunk {"id": "body-0020", "role": "body", "section": "Method", "weight": 1.0} -->

Learning. We train our model via imitation learning by fitting our parameters to maximize the log-likelihood of recorded driving trajectories. Let our data be of the form ${\{{(\mathbf{x}^{m},{\hat{\mathbf{s}}}^{m})}\}}_{m = 1}^{M}$. We learn to predict distribution parameters $\pi{(\left. \mathbf{a}^{k} \middle| \mathbf{x} \right.)}$,

<!-- chunk {"id": "body-0021", "role": "body", "section": "Method", "weight": 1.0} -->

This is a time-sequence extension of standard GMM likelihood fitting. The notation $\mathbb{1}{( \cdot )}$ is the indicator function, and ${\hat{k}}^{m}$ is the index of the anchor most closely matching the groundtruth trajectory ${\hat{\mathbf{s}}}^{m}$, measured as $\ell^{2}$-norm distance in state-sequence space. This hard-assignment of groundtruth anchors sidesteps the intractability of direct GMM likelihood fitting, avoids resorting to an expectation-maximization procedure, and gives practitioners control over the design of the anchors as they wish (see our choice below). One could also employ a soft-assignment to anchors (*e.g*., proportional to the distance of the anchor to the groundtruth trajectory), just as easily.

<!-- chunk {"id": "body-0022", "role": "body", "section": "Method", "weight": 1.0} -->

Inferring a diverse weighted set of test-time trajectories. Our model allows us to eschew standard sampling techniques at test time, and obtain a weighted set of $K$ trajectories without any additional computation: we take the MAP trajectory estimates from each of our $K$ anchor modes, and consider the distribution over anchors $\pi{(\left. \mathbf{a}_{k} \middle| \mathbf{x} \right.)}$ the sample weights (*i.e*., importance sampling). When metrics and applications call for a set of top $\kappa < K$ trajectories for evaluation, we return the top $\kappa$ according to these sample weights.

<!-- chunk {"id": "body-0023", "role": "body", "section": "Method", "weight": 1.0} -->

Input representation. We follow other recent approaches and represent a history of dynamic and static scene context as a 3-dimensional array of data rendered from a top-down orthographic perspective. The first two dimensions represent spatial locations in the top-down image. The channels in the depth dimension hold static and time-varying (dynamic) content of a fixed number of previous time steps. Agent observations are rendered as orientated bounding box binary images, one channel for each time step. Other dynamic context such as traffic light state and static context of the road (lane connectivity and type, stop lines, speed limit, *etc*.) form additional channels. See Sec. 4 for further details, as the input content differs from dataset to dataset. An important benefit of using such a top-down representation is the simplicity of representing contextual information like the agents' spatial relationships to each other and semantic road information. In Sec. B.4, we empirically highlight its benefit towards behavior prediction.

<!-- chunk {"id": "body-0024", "role": "body", "section": "Method", "weight": 1.0} -->

Neural network details. As shown in Fig. 1, we designed a jointly-trained, two-stage architecture that first extracts a feature representation for the whole scene and then attends to each agent in the scene to make agent-specific trajectory predictions.

<!-- chunk {"id": "body-0025", "role": "body", "section": "Method", "weight": 1.0} -->

The first stage is fully convolutional to preserve spatial structure; it takes the 3D input representation described above and outputs a 3D feature map of the entire top-down scene. We opt to use ResNet-based architectures for this scene-level feature extractor. We employ depth-wise thinned-out networks for all experiments, and a different number of residual layers depending on the dataset. See Sec. B.2 for a speed-accuracy analysis of different ResNet setups.

<!-- chunk {"id": "body-0026", "role": "body", "section": "Method", "weight": 1.0} -->

The second phase extracts patches of size $11 \times 11$ centered on agents locations in this feature map. To be orientation invariant, the extracted features are also rotated to an agent-centric coordinate system via a differentiable bilinear warping. The efficacy of this type of heading-normalization is shown in Sec. B.3. The second agent-centric network then operates on a per-agent basis. It contains 4 convolutional layers with kernel size 3 and 8 or 16 depth channels. It produces $K \times T \times 5$ parameters describing bivariate Gaussian's per time step per anchor (parameterized by $\mu_{x},\mu_{y},{\log\sigma_{x}},{\log{\sigma_{y}\text{~and~}\rho}}$; the last 3 parameters define the $2 \times 2$ covariance matrix $\Sigma_{xy}$ in the agent-centric $x,y$-coordinate space), as well as $K$ softmax logits to represent $\pi{(\left.

<!-- chunk {"id": "body-0027", "role": "body", "section": "Experiments", "weight": 1.0} -->

This section presents empirical results on a number of prediction tasks. We consider the following methods in order to contrast to different aspects of MultiPath.

<!-- chunk {"id": "body-0028", "role": "body", "section": "Experiments", "weight": 1.0} -->

MultiPath $\mu$ \[, $\Sigma$\]. Our proposed method with multiple anchors, modeling offsets $\mu$ and control uncertainty covariances $\Sigma$. For some experiments, we keep $\Sigma$ frozen, which reduces the maximum-likelihood loss to simple $\ell^{2}$-loss. However, we can no longer estimate likelihood $p{(\left. \mathbf{s} \middle| \mathbf{x} \right.)}$ without $\Sigma$ and only report distance-based metrics.

<!-- chunk {"id": "body-0029", "role": "body", "section": "Experiments", "weight": 1.0} -->

Regression $\mu$ \[, $\Sigma$\]. To verify our hypothesis that modeling multiple intents is important, we modified the MultiPath architecture to regress a single output trajectory. This is similar to 's output (but extended to include uncertainty).

<!-- chunk {"id": "body-0030", "role": "body", "section": "Experiments", "weight": 1.0} -->

Min-of-K. This method predicts $K$ trajectories directly, without pre-defined anchors. The authors define an $\ell^{2}$-loss on the single trajectory (out of $K$) with minimum distance to the groundtruth trajectory. This is similar to our method, but with implicit anchors and evolving hard-assignment of anchors to groundtruth as training progresses. This representation has inherent ambiguity problems and can suffer from mode collapse. In our experiments below, we extend this method to also predict $\mu,\Sigma$ values at each waypoint to evaluate likelihood.

<!-- chunk {"id": "body-0031", "role": "body", "section": "Experiments", "weight": 1.0} -->

CVAE. The Conditional Variational Auto-Encoder is a standard implicit generative sampling model and has been successfully adapted to predict trajectory for autonomous driving. We are interested in comparing its ability to generate a diverse set of samples compared to MultiPath's MAP trajectory per anchor---we hypothesize that MultiPath will have better coverage with the same number of trajectories due to its choice of anchors. For this baseline, we add a CVAE at the end of the second stage agent-centric feature extractor. The decoder and encoder have the same architecture: 4 fully-connected layers of 32 units each.

<!-- chunk {"id": "body-0032", "role": "body", "section": "Experiments", "weight": 1.0} -->

Linear. Following, we use a linear model on past states to establish how well a simple constant velocity model can perform. We fit past observed positions as a linear function of time: $\mathbf{x}^{t} = {\lbrack{{\alphat} + \beta},{{\gammat} + \delta}\rbrack}$ for $t \leq 0$, and use these models to evaluate future positions $\mathbf{x}^{1},\ldots,\mathbf{x}^{T}$. We investigated using higher-order polynomials with worse results.

<!-- chunk {"id": "body-0033", "role": "body", "section": "Experiments", "weight": 1.0} -->

We implemented the single-trajectory regression, Min-of-K, and CVAE using the same input representation and a comparable model architecture in order to achieve a fair comparison. For benchmark datasets, we also report numbers taken from recent publications.

<!-- chunk {"id": "body-0034", "role": "body", "section": "Metrics", "weight": 1.0} -->

Different approaches use a variety of output representations; primary examples are single trajectory prediction, an unweighted set of trajectory samples, a distribution over trajectories (ours), or probabilistic occupancy grids. Each representation comes with its own salient metrics, making it difficult to compare across all methods. Let $\hat{\mathbf{s}} = {\hat{s}}_{t = {1\ldotsT}}$ be a groundtruth trajectory.

<!-- chunk {"id": "body-0035", "role": "body", "section": "Metrics", "weight": 1.0} -->

Log-likelihood (LL). We report ${\log p}{(\left. \hat{\mathbf{s}} \middle| \mathbf{x} \right.)}$ if the model admits evaluation of likelihood, as does MultiPath when all parameters are learned (see Eq. ). The metric is scaled down by a factor of $2 \times T$, where $T$ is the number of time steps and $2$ for the two spatial dimensions.

<!-- chunk {"id": "body-0036", "role": "body", "section": "Metrics", "weight": 1.0} -->

For evaluating a set of trajectories, minADE~M~ ${\min_{s_{m}}\frac{1}{T}}{\sum_{t = 1}^{T}\left\| {{\hat{s}}_{t} - s_{m,t}} \right\|_{2}}$ measures the displacement error against the closest trajectory in the set of size $M$, so that reasonable predictions that simply do not happen to be the logged groundtruth are not penalized. Note that there is also the minMSD~M~, which is similar but the average is calculated on squared distances instead.

<!-- chunk {"id": "body-0037", "role": "body", "section": "Toy experiment: 3-way intersection", "weight": 1.0} -->

We first explore a simple proof-of-concept dataset generated based on our modeling assumptions. We generate synthetic 3-way intersections, with the probability of choosing the left, the middle or the right path set a priori to be the intent uncertainty distribution $\{ 0.3,0.5,0.2\}$. To emphasize the flexibility of our single-trajectory control uncertainty modeling, each path is generated by sampling parameterized sine waves: $y = {\sin{({{\omegat} + \phi})}}$, where the frequency $\omega \sim {\mathcal{U}{}}$ and phase shift $\phi \sim {\mathcal{U}{({- \pi},\pi)}}$. As shown in Figure 2, MultiPath is able to fit the underlying distribution correctly, recovering the intent uncertainty, and reaching approximately Bayes-optimal likelihood, while other methods fare worse.

<!-- chunk {"id": "body-0038", "role": "body", "section": "Behavior prediction for autonomous driving", "weight": 1.0} -->

To verify the performance of the proposed system, we collected a large dataset of real-world driving scenes from several cities in North America. Data is captured by a vehicle equipped with cameras, lidar and radar. As, we assume that an industry-grade perception system provides sufficiently accurate poses and tracks for all nearby agents, including vehicles, pedestrians, and cyclists. In our experiments, we treat the sensing vehicle as an additional agent, indistinguishable from any other agent in the scene. Most of the collected vehicle trajectories are either stationary or moving straight at a constant speed. Neither case is particularly interesting from a behavior prediction point of view. To address this and other dataset skew, we partitioned the space of future trajectories via a uniform, 2D grid over constant curvatures and distances, and performed stratified sampling such that the number of examples in each partition was capped to be at most 5% of the resulting dataset. The balanced dataset totals 3.85 million examples, contains 5.75 million agent trajectories and constitutes approximately 200 hours of driving.

<!-- chunk {"id": "body-0039", "role": "body", "section": "Behavior prediction for autonomous driving", "weight": 1.0} -->

The top-down rendered input tensor for this data has a resolution of 400 px $\times$ 400 px and corresponds to 80 m $\times$ 80 m in real-world coordinates. We sample time steps every 0.2 s (5 Hz). The following features are stacked in the depth dimension: 3 channels of color-coded road semantics, 1 channel of distance-to-road-edge map, 1 channel encoding the speed limit, 5 channels encoding the traffic light states over the past 5 time steps (=1 second), and 5 channels each showing vehicles' top-down orthographic projection for each of the past 5 time steps. This results in 15 input channels in total. We predict trajectories up to 30 frames / 6 seconds into the future. The number of anchors $K$ is set to 16 for MultiPath $\mu,\Sigma$ and 64 for MultiPath $\mu$. The scene-level network is a with a depth multiplier of 25%, followed by a depth-to-space operation that restores some of the lost spatial resolution in the ResNet back to $200 \times 200$.

<!-- chunk {"id": "body-0040", "role": "body", "section": "Behavior prediction for autonomous driving", "weight": 1.0} -->

Finally, we train the model end-to-end for 500k steps at a batch size of 32, with a learning rate warm-up phase and a cosine learning rate decay

<!-- chunk {"id": "body-0041", "role": "body", "section": "Behavior prediction for autonomous driving", "weight": 1.0} -->

Experimental results are shown in Tab. 1. MultiPath outperforms the baselines in all metrics. With respect to the log-likelihood, we have observed the most log-likelihood measurements for this task to fall between 3 to 4.2 nats, so the gain of roughly 0.2 nat by MultiPath compared to the regression baseline is quite significant. See Sec. A for in-depth analyses of these results. 16 anchors are used for MultiPath $\mu,\Sigma$, while 64 was the best $K$ for MultiPath $\mu$. An analysis of the effect of the number of anchors $K$ is in Sec. B.1, while the figures in Sec. C visualize the anchors.

<!-- chunk {"id": "body-0042", "role": "body", "section": "Stanford Drone", "weight": 1.0} -->

The Stanford Drone Dataset consists of top-down, near-orthographic videos of college campus scenes, collected by drones, containing interacting pedestrians, cyclists and vehicles. The RGB camera frames provide context similar to a rendered road semantics in the driving vehicle environment, and we treat it as such. We use the most common settings in the literature: sampling at 2.5 Hz, and predicting 4.8 seconds (12 frames) into the future, using 2 seconds of history (5 frames). Additional experimental details are in Sec. D.

<!-- chunk {"id": "body-0043", "role": "body", "section": "Stanford Drone", "weight": 1.0} -->

As shown in Tab. 2, we perform at or better than state-of-the-art in best single-trajectory distance metrics. Notably, CAR-Net outperforms our comparable single-trajectory model; their method focuses on a sophisticated attention and sequential architecture tuned to get the best single-trajectory distance metric performance. Interestingly, our single-trajectory model performs better when trained to predict uncertainty as well, a potential benefit of modeling uncertainty discussed.

<!-- chunk {"id": "body-0044", "role": "body", "section": "CARLA", "weight": 1.0} -->

We evaluate MultiPath on the publicly available multi-agent trajectory forecasting and planning dataset generated using the CARLA simulator. Experimental details are in Sec. E. Tab. 3 reproduces results reported by for the DESIRE, SocialGAN, R2P2-MA, and the PRECOG-ESP methods and compares the performance of MultiPath against them. We report the minMSD metric with the top $K = 12$ predictions as defined in to report our evaluation results.

<!-- chunk {"id": "body-0045", "role": "body", "section": "Conclusion", "weight": 1.5} -->

We have introduced MultiPath, a model which predicts parametric distributions of future trajectories for agents in real-world settings. Through synthetic and real-world datasets, we have shown the benefits of MultiPath over previous single-trajectory and stochastic models in achieving likelihood and trajectory-set metrics and needing only 1 feed-forward inference pass.
