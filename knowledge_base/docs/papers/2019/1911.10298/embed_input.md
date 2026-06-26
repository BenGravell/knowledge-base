<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

CoverNet: Multimodal Behavior Prediction Using Trajectory Sets

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

We present CoverNet, a new method for multimodal, probabilistic trajectory prediction for urban driving. Previous work has employed a variety of methods, including multimodal regression, occupancy maps, and 1-step stochastic policies. We instead frame the trajectory prediction problem as classification over a diverse set of trajectories. The size of this set remains manageable due to the limited number of distinct actions that can be taken over a reasonable prediction horizon. We structure the trajectory set to a) ensure a desired level of coverage of the state space, and b) eliminate physically impossible trajectories. By dynamically generating trajectory sets based on the agent's current state, we can further improve our method's efficiency. We demonstrate our approach on public, real-world self-driving datasets, and show that it outperforms state-of-the-art methods.

<!-- chunk {"id": "body-0003", "role": "body", "section": "Introduction", "weight": 1.5} -->

We are motivated by autonomous systems operating in dynamic, interactive, and uncertain environments. Specifically, we focus on the problem of a self-driving car navigating in an urban environment, where it must share the road with a diverse set of other agents, including vehicles, bicyclists, and pedestrians. In this context, reasoning about the possible future states of agents is critical for safe and confident operation. Effective prediction of future agent states depends on both road context (e.g., lane geometry, crosswalks, traffic lights) and the recent behavior of other agents.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

Trajectory prediction is inherently challenging due to a wide distribution of agent preferences (e.g., a cautious vs. aggressive) and intents (e.g., turn right vs. go straight). Useful predictions must represent multiple possibilities and their associated likelihoods. Furthermore, we expect that predicted trajectories are physically realizable.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

Multimodal regression models appear naturally suited for this task, but may degenerate during training into a single mode. Avoiding this "mode collapse" requires careful considerations. Additionaly, most state-of-the-art methods predict unconstrained positions, resulting in trajectories that may not be physically possible for execution ( is a recent exception). Our main insights leverage domain-specific knowledge to effectively structure the output representation and address these concerns.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

Our first insight is that there are relatively few *distinct* actions that can be taken over a *reasonable* time horizon. Dynamic constraints considerably limit the set of reachable states over a standard six second prediction horizon, and the inherent uncertainty in agent behavior outweighs small approximation errors. We exploit this insight to formulate multimodal, probabilistic trajectory prediction as classification over a trajectory set. This avoids mode collapse and lets the user design the trajectory set to meet specific requirements (e.g., dynamically feasible, coverage guarantees).

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

Our second insight is that predicted trajectories should be consistent with the current dynamic state. Thus, we formulate our output as motions relative to our initial state (e.g., turn slightly right, accelerate). When integrated with a dynamics model, the output is converted to an appropriate sequence of positions. Beyond helping ensure physically valid trajectories, this *dynamic* output representation ensures that the outputs are diverse in the control space across a wide range of speeds. While exploit a similar insight for regression, we extend the use of a dynamic representation to classification and anchor-box regression.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Introduction", "weight": 1.5} -->

We now summarize our main contributions on multimodal, probabilistic trajectory prediction with CoverNet: introduce the notion of trajectory sets for multimodal trajectory prediction, and show how to generate them in both a fixed and dynamic manner; compare state-of-the-art methods on nuScenes, a public, real-world urban driving benchmark; empirically show the benefits of classification on trajectory sets over multimodal regression.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Method", "weight": 1.0} -->

In this section we outline the main contribution of the paper: a novel method for trajectory set generation, and show how it can be used for behavior prediction.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Output representation", "weight": 1.0} -->

Due to the relatively short trajectory prediction horizons (up to 6 seconds), and inherent uncertainty in agent behavior, we approximate all possible motions with a set of trajectories that gives sufficient coverage of the space.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Output representation", "weight": 1.0} -->

Let $\mathcal{R}{(s_{t})}$ be the set of all states that can be reached by an agent with current state $s_{t}$ in $N$ timesteps (purely based on physical capabilities). We approximate this set by a finite number of trajectories, defining a trajectory set $\mathcal{K} = {\{ s_{t:{t + N}}\}}$. We define a *dynamic* trajectory set generator as a function $f_{N}:{s_{0}\rightarrow\mathcal{K}}$, which allows the trajectory set to be consistent with the current dynamics. In contrast, a *fixed* generator does not use information about the current state, and thus returns the same trajectories for each instance. We discuss trajectory set construction in Section 3.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Output representation", "weight": 1.0} -->

We encode multimodal, probabilistic trajectory predictions by classifying over the appropriate trajectory set given an agent of interest and the scene context $\mathcal{C}$. As is common in the classification literature, we use the softmax distribution. Concretely, the probability of the $k$-th trajectory is given as ${p{(\left. s_{t:{t + N}}^{k} \middle| x \right.)}} = \frac{{\exp f_{k}}{(x)}}{\sum_{i}{{\exp f_{i}}{(x)}}}$, where ${f_{i}{(x)}} \in {\mathbb{R}}$ is the output of the network's penultimate layer.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Output representation", "weight": 1.0} -->

In contrast to previous work, we choose not to learn an uncertainty distribution over the space. While it is straightforward to add Gaussian uncertainty along each trajectory in a similar manner to, the density of our trajectory sets reduces its benefit compared to the case when there are only a handful of modes.

<!-- chunk {"id": "body-0014", "role": "body", "section": "Output representation", "weight": 1.0} -->

An ideal trajectory set always contains a trajectory that is close to the ground truth. We propose two broad categories of trajectory set generation functions: fixed and dynamic (see Figure 2). In both cases, we normalize the current state to be at the origin, with the heading oriented upwards.

<!-- chunk {"id": "body-0015", "role": "body", "section": "Fixed trajectory sets", "weight": 1.0} -->

We consider a trajectory set to be *fixed* if the trajectories that it contains do not change as a function of the agent's current dynamic state or environment. Intuitively, this makes it easy to classify over since it allows for a fixed enumeration over the set, but may result in many trajectories that are poor matches for the current situation.

<!-- chunk {"id": "body-0016", "role": "body", "section": "Fixed trajectory sets", "weight": 1.0} -->

Given a set of representative trajectory data, the problem of finding the smallest fixed approximating trajectory set $\mathcal{K}$ can be cast as an instance of the NP-hard set cover problem.. Approximating a dense trajectory set by a sparse trajectory set that still maintains good coverage and diversity has been studied in the context of robot motion planning. In this work, we use a coverage metric $\delta$ defined as the maximum point-wise Euclidean distance between trajectories. Our trajectory set construction procedure starts with subsampling a reasonably large set $\mathcal{K}'$ of trajectories (ours have size 20,000) from the training set.

<!-- chunk {"id": "body-0017", "role": "body", "section": "Fixed trajectory sets", "weight": 1.0} -->

We refer to this metric as the maximum point-wise $\ell^{2}$ distance.

<!-- chunk {"id": "body-0018", "role": "body", "section": "Fixed trajectory sets", "weight": 1.0} -->

We employ a simple greedy approximation algorithm to solve $$, which we refer to as the *bagging* algorithm. We cherry-pick the best among candidate trajectories to place in a bag of trajectories that will be used as the covering set. We repeatedly consider as candidates those trajectories that have not yet been covered and choose the one that covers the most uncovered trajectories (ties are broken arbitrarily).

<!-- chunk {"id": "body-0019", "role": "body", "section": "Fixed trajectory sets", "weight": 1.0} -->

Standard results (without using the specialized structure of the data) show that our deterministic greedy algorithm is suboptimal by a factor of at most $\log{({|\mathcal{K}'|})}$ (see Chapter 35.3 ). In our experiments, we were able to obtain decent coverage (specifically, under 2 meters in maximum point-wise $\ell^{2}$ distance for 6 second trajectories) with fewer than 2,000 elements in the covering set.

<!-- chunk {"id": "body-0020", "role": "body", "section": "Dynamic trajectory sets", "weight": 1.0} -->

We consider a trajectory set to be *dynamic* if the trajectories that it contains change as a function of the agent's current dynamic state. This construction guarantees that all trajectories in the set are dynamically feasible.

<!-- chunk {"id": "body-0021", "role": "body", "section": "Dynamic trajectory sets", "weight": 1.0} -->

We now describe a simple approach to constructing such a dynamic trajectory set, focused on predicting vehicle motion. We use a standard vehicle dynamical model as similar models are effective for planning at urban (non-highway) driving speeds. Our approach, however, is not limited to vehicles or any specific model. The dynamical model we use is: with states: $x$, $y$ (position), $v$ (speed), $\theta$ (yaw); controls: $u_{steer}$ (steering angle), $u_{accel}$ (longitudinal acceleration); and parameter: $b$ (wheelbase).

<!-- chunk {"id": "body-0022", "role": "body", "section": "Dynamic trajectory sets", "weight": 1.0} -->

We parameterize the controls (output space) by a diverse set of constant lateral and longitudinal accelerations over the prediction horizon. Using lateral acceleration instead of steering angle is a way of normalizing the output over a range of speeds (a desired lateral acceleration will correspond to different steering angles as a function of speed). We convert the lateral acceleration into a steering angle assuming instantaneous circular motion $a_{lat} = {v^{2}\kappa}$ with curvature $\kappa = {{\tan{(u_{steer})}}/b}$. This conversion is ill-defined when the speed is near zero, so we use $\max{(v,1)}$ in place of $v$. Note that it is straightforward to expand the controls (output space) to include multiple lateral and longitudinal accelerations over a non-uniform prediction horizon.

<!-- chunk {"id": "body-0023", "role": "body", "section": "Dynamic trajectory sets", "weight": 1.0} -->

We can further prune the dynamic trajectory set construction in a similar manner to how we handled the fixed trajectory sets in 3.3. The main difference is that the covering set here is constructed from the set of control input profiles as opposed to elements of $\mathcal{K}'$ itself. Namely, we use an analogous greedy procedure to cover the set of sample trajectories with a subset of control profiles (e.g., lateral and longitudinal accelerations as a function of time). Note that unlike the case of fixed trajectories, the synthetic nature of the dynamic profile may not guarantee 100% coverage of $\mathcal{K}'$. To counter this problem we can also create a *hybrid* trajectory set by combining a fixed and dynamic set. Particularly, we find a covering subset for the elements of $\mathcal{K}'$ that cannot be covered by the dynamic choices, and combine this subset with the dynamic choices. When the dynamic set is well-constructed, this can result in a smaller covering set as may be seen from Figure 3.

<!-- chunk {"id": "body-0024", "role": "body", "section": "Experiments", "weight": 1.0} -->

We present empirical results on trajectory prediction of vehicles in urban environments. The following sections describe the baselines, metrics, and urban driving datasets that we considered. We used the same input representation and model architecture across our models and baselines.

<!-- chunk {"id": "body-0025", "role": "body", "section": "Baselines", "weight": 1.0} -->

Physics oracle. We introduce a simple and interpretable model that extends classic physics-based models. We use the track's current velocity, acceleration, and yaw rate to compute the following predictions: i) constant velocity and yaw, ii) constant velocity and yaw rate, iii) constant acceleration and yaw, and iv) constant acceleration and yaw rate. The *oracle* is the minimum average point-wise Euclidean distance over the four models.

<!-- chunk {"id": "body-0026", "role": "body", "section": "Baselines", "weight": 1.0} -->

Regression baselines and extensions. We compare our contribution to state-of-the-art methods by implementing two main types of regression models: multimodal regression to coordinates and multimodal regression to residuals from a set of anchors (ordinal regression). We overview these methods for completeness and to provide context for novel variations that we introduce.

<!-- chunk {"id": "body-0027", "role": "body", "section": "Baselines", "weight": 1.0} -->

Multimodal regression to coordinates. Our implementation follows the details of Multiple-Trajectory Prediction (MTP), adapted for our datasets. This model predicts a fixed number of trajectories (modes) and their associated probabilities. The per-agent loss (agent $i$ at time $t$) is defined as: where $\mathbb{1}{(\cdot)}$ is the indicator function that equals $1$ only for the "best matching" mode, $k$ represents a mode, $L$ is the regression loss, and $\alpha$ is a hyper-parameter used to trade off between classification and regression. With some abuse of notation we use $\mathcal{K}$ to represent the set of trajectories predicted by a model. The original implementation uses a heuristic based on the relative angle between each mode and the ground truth. We select a mode uniformly at random when there are no modes with an angle below the threshold.

<!-- chunk {"id": "body-0028", "role": "body", "section": "Baselines", "weight": 1.0} -->

Multimodal regression to anchor residuals. Our implementation follows the details of MultiPath (MP). This model implements ordinal regression by first choosing among a fixed set of anchors (computed a priori) and then regressing to residuals from the chosen anchor. The proposed per-agent loss is where $\alpha = 1$ and the $k$-th trajectory is the sum of the corresponding anchor and predicted residual. To remain true to the implementation, we choose our best matching anchor by minimizing the average displacement to the ground truth.

<!-- chunk {"id": "body-0029", "role": "body", "section": "Baselines", "weight": 1.0} -->

We compute the set of fixed anchors by employing the same mechanism described in Section 3.3. Note that this set of trajectories is the same for all agents in our dataset. We then regress to the residuals from the chosen anchor.

<!-- chunk {"id": "body-0030", "role": "body", "section": "Our models", "weight": 1.0} -->

CoverNet (fixed). Our classification approach where the $\mathcal{K}$ set includes only fixed trajectories.

<!-- chunk {"id": "body-0031", "role": "body", "section": "Our models", "weight": 1.0} -->

CoverNet (dynamic). Our classification approach where the $\mathcal{K}$ set is a function of the current agent state.

<!-- chunk {"id": "body-0032", "role": "body", "section": "Our models", "weight": 1.0} -->

CoverNet (hybrid). Our classification approach where the $\mathcal{K}$ set is a combination of fixed and dynamic trajectories.

<!-- chunk {"id": "body-0033", "role": "body", "section": "Our models", "weight": 1.0} -->

MultiPath with dynamic anchors. The MultiPath approach, extended to use dynamic anchors, described in Section 3.4. The set of anchors is a function of the agent's speed, helping ensure that anchors are dynamically feasible. We then regress to the residuals from the chosen anchor.

<!-- chunk {"id": "body-0034", "role": "body", "section": "Implementation details", "weight": 1.0} -->

Our implementation setup follows and, with key differences highlighted below. See Figure 1 for an overview.

<!-- chunk {"id": "body-0035", "role": "body", "section": "Implementation details", "weight": 1.0} -->

We implemented our models using ResNet-50 as our backbone, with pre-trained ImageNet weights downloaded. We read the ResNet *conv5* feature map and apply a global pooling layer. We then concatenate the result with an agent state vector (including speed, acceleration, yaw rate), as detailed. We then add a fully connected layer, with dimension $4096$.

<!-- chunk {"id": "body-0036", "role": "body", "section": "Implementation details", "weight": 1.0} -->

The output dimension of CoverNet is equal to the number of modes, namely $|\mathcal{K}|$. For the hybrid models, the fixed:dynamic trajectory split for the nuScenes dataset is 92:682 and that of the internal dataset is 524:500. We chose these values to maximize coverage at $\epsilon \approx 2$ $meters$ and minimize the sum of the total number of categories.

<!-- chunk {"id": "body-0037", "role": "body", "section": "Implementation details", "weight": 1.0} -->

For the regression models, our outputs are of dimension ${|\mathcal{K}|} \times {({{{|\overset{\rightarrow}{x}|} \times N} + 1})}$, where $|\mathcal{K}|$ represents the total number of predicted modes, $|\overset{\rightarrow}{x}|$ represents the number of features we are predicting per point, $N$ represents the number of points in our predictions, and the extra output per mode is the probability associated with each mode. For our implementations, $N = {H \times F}$, where $H$ represents the length of the prediction horizon in seconds, and $F$ represents the sampling frequency. For each point, we predict $(x,y)$ coordinates, so ${|\overset{\rightarrow}{x}|} = 2$.

<!-- chunk {"id": "body-0038", "role": "body", "section": "Implementation details", "weight": 1.0} -->

Our internal datasets have $F = {10\ Hz}$, while the publicly available nuScenes is sampled at $F = {2\ Hz}$. We include results on two different prediction horizon lengths, namely $H = 3$ seconds and $H = 6$ seconds.

<!-- chunk {"id": "body-0039", "role": "body", "section": "Implementation details", "weight": 1.0} -->

The loss functions we use are the same across all of our implementations: for any classification losses, we utilize cross-entropy with positive samples determined by the element in the trajectory set closest to the actual ground truth in minimum average of point-wise Euclidean distances, and for any regression losses, we utilize smooth $\ell^{1}$. For our MTP implementation, we place equal weighting between the classification and regression components of the loss, setting $\alpha = 1$, similar to.

<!-- chunk {"id": "body-0040", "role": "body", "section": "Implementation details", "weight": 1.0} -->

For our classification models, we utilize a fixed learning rate of ${1e} - 4$. For our regression models, we use a learning rate of ${1e} - 4$, with a drop by $0.1$ as follows: for our internal dataset, we always perform the drop at epoch $6$; for nuScenes, we perform the drop at epoch $31$ for MTP with $1$ and $3$ modes and MP dynamic with $16$ modes, epoch $12$ for MTP with $16$ and $64$ modes, MP with $16$ modes and MP dynamic with $64$ modes, and epoch $7$ for MP with $64$ modes.

<!-- chunk {"id": "body-0041", "role": "body", "section": "Metrics", "weight": 1.0} -->

There are multiple ways of evaluating multimodal trajectory prediction. Common measures include log-likelihood, average displacement error, and hit rate. We focus on the a) displacement error, and b) hit rate, both computed over a subset of the most likely modes.

<!-- chunk {"id": "body-0042", "role": "body", "section": "Metrics", "weight": 1.0} -->

For insight into trajectory prediction performance in scenarios where there are multiple plausible actions, we use the minimum average displacement error (ADE). The minADE~k~ is ${\min_{\hat{s} \in \mathcal{P}}\frac{1}{N}}{\sum_{\tau = t}^{t + N}{\|{s_{\tau} - {\hat{s}}_{\tau}}\|}}$, where $\mathcal{P}$ is the set of $k$ most likely trajectories. We also analyze the final displacement error (FDE), which is $\|{s_{t + N} - {\hat{s}}_{t + N}^{\ast}}\|$, where $s^{\ast}$ is the most likely mode.

<!-- chunk {"id": "body-0043", "role": "body", "section": "Metrics", "weight": 1.0} -->

In the context of planning for a self-driving vehicle, the above metrics may be hard to interpret. We use the notion of a *hit rate* (see ) to simplify interpretation of whether or not a prediction was "close enough." We define a $\text{Hit}_{k,d}$ for a single instance (agent at a given time) as 1 if ${{\min_{\hat{s} \in \mathcal{P}}\max_{\tau = t}^{t + N}}{\|{s_{\tau} - {\hat{s}}_{\tau}}\|}} \leq d$, and 0 otherwise. When averaged over all instances, we refer to it as the $\text{HitRate}_{k,d}$.

<!-- chunk {"id": "body-0044", "role": "body", "section": "Input representation", "weight": 1.0} -->

Similar to, we rely on results from an object detection module, and we rasterize the scene for each agent as an RGB image. We start with a blank image of size ($H$, $W$, $3$) and draw the drivable area, crosswalks, and walk ways using a distinct color for each semantic category.

<!-- chunk {"id": "body-0045", "role": "body", "section": "Input representation", "weight": 1.0} -->

We rotate the image so that the agent's heading faces up, and place the agent on pixel ($l$, $w$), measured from the top-left of the image. We assign a different color to vehicles and pedestrians and choose a different color for the agent so that it is distinguishable. In our experiments, we use a resolution of 0.1 meters per pixel and choose $l = 400$ and $w = 250$. Thus, the model can "see" $40$ meters ahead, $10$ meters behind, and $25$ meters on each side of the agent.

<!-- chunk {"id": "body-0046", "role": "body", "section": "Input representation", "weight": 1.0} -->

We represent the sequence of past observations for each agent as faded bounding boxes of the same color as the agent's current bounding box. We fade colors by linearly decreasing saturation (in HSV space) as a function of time.

<!-- chunk {"id": "body-0047", "role": "body", "section": "Input representation", "weight": 1.0} -->

Although, we have only used one input representation in these experiments, our novel output representation can work with the input representations of.

<!-- chunk {"id": "body-0048", "role": "body", "section": "Datasets", "weight": 1.0} -->

Internal self-driving dataset. We collected 60 hours of real-world, urban driving data in Singapore. Raw sensor data is collected by a car outfitted with cameras, lidars, and radars. A highly-optimized object detection and tracking system filters the raw sensor data to produce tracks at a 10 Hz rate. Each track includes information regarding its type (e.g., car, pedestrian, bicycle, unknown), pose, physical extent, and speed, with quality sufficient for fully-autonomous driving. We also have access to high-definition maps with semantic labels of the road such as the drivable area, lane geometry, and crosswalks.

<!-- chunk {"id": "body-0049", "role": "body", "section": "Datasets", "weight": 1.0} -->

Each ego vehicle location at a given timestamp is considered a data point. We do not predict on any tracks that are stationary over the entire prediction horizon. Our internal dataset contains around 11 million usable data points but for this analysis we created train, validation, and test sets with 1 million, 300,000, and 300,000 data points, respectively. nuScenes. We also report results on nuScenes, a public self-driving car dataset. nuScenes consists of 1000 scenes, each 20 seconds in length. Scenes are taken from urban driving in Boston, USA and Singapore. Each scene includes hand-annotated tracks and high-definition maps. Tracks have 3D ground truth annotations, and are published at 2 Hz. Since annotations are not public on the test set, we created a set for validation from the train set (called the train-val set) and treated the validation set as the test set. As with our internal dataset, we removed vehicles that are stationary and also removed vehicles that go off the annotated map. This leaves us with 32,186 observations in the train set, 8,560 observations in the train-val set, and 9,041 observations in the validation set.

<!-- chunk {"id": "body-0050", "role": "body", "section": "Datasets", "weight": 1.0} -->

This split publicly available in the nuScenes software development kit.

<!-- chunk {"id": "body-0051", "role": "body", "section": "Results", "weight": 1.0} -->

The main results are summarized in Table 2. Qualitative results are shown in Figure 4.

<!-- chunk {"id": "body-0052", "role": "body", "section": "Results", "weight": 1.0} -->

Const. vel. & yaw Table 2: nuScenes and internal datasets (6 sec horizon). Results listed as nuScenes (internal). Smaller minADEk and FDE is better. Larger HitRate5, 2m is better. Dyn. = dynamic, vel. = velocity, const. = constant, ε is given in meters.

<!-- chunk {"id": "body-0053", "role": "body", "section": "Results", "weight": 1.0} -->

Quantitative results. Across the six metrics and the two datasets we used, CoverNet outperforms previous methods and baselines in 8 out of 12 cases. However, there are big differences in method ranking depending on the metric.

<!-- chunk {"id": "body-0054", "role": "body", "section": "Results", "weight": 1.0} -->

CoverNet represents a significant improvement on the HitRate~5,\ 2m~ metric, achieving $33\%$ on nuScenes with the hybrid trajectory set. The next best model is MultiPath, where our dynamic grid extension is a slight improvement over the fixed grid used by the authors ($13\%$ vs. $10\%$). MTP with three modes performs worse, achieving $10\%$, barely outperforming the constant velocity baseline.

<!-- chunk {"id": "body-0055", "role": "body", "section": "Results", "weight": 1.0} -->

We notice a similar pattern on the internal dataset, where CoverNet outperforms previous methods and baselines. Here, the fixed set with 1,937 modes performs best ($57\%$), closely followed by the hybrid set ($55\%$). Among previous methods, again MultiPath with dynamic set works the best at $30\%$ HitRate~5,\ 2m~. Figure 5 shows that CoverNet significantly outperforms previous methods as the hit rate is expanded over more modes.

<!-- chunk {"id": "body-0056", "role": "body", "section": "Results", "weight": 1.0} -->

CoverNet also performs well according the Average Displace Error minADE~k~ metrics, in particular for $k \in {\{ 5,10,15\}}$, where we see CoverNet outperforming state-of-the-art methods in every category. Most notably, under the minADE~15~ metric for our internal dataset, the hybrid CoverNet with fixed set and 2,206 modes performs best with minADE~15~ of $0.84$, 4x better than the constant velocity baseline and 2x better than the MTP and MultiPath. For the minADE~1~ metric the regression methods performed the best. This is not surprising since for low $k$ it is more important to have one trajectory very close to the ground truth, a metric paradigm that favors regression over classification.

<!-- chunk {"id": "body-0057", "role": "body", "section": "Results", "weight": 1.0} -->

A notable difference between nuScenes and internal is that the HitRate~5,\ 2m~ and minADE~k~ continues to improve for larger sets, while it plateaus, or even decreases at around 500-1,000 modes on nuScenes. We hypothesize that this is due to relatively limited size of nuScenes.

<!-- chunk {"id": "body-0058", "role": "body", "section": "Results", "weight": 1.0} -->

Qualititive results. In Figure 4, we show the visualization of a scene overlaid with predictions from our top models compared against our baselines. We note that our prediction horizon for this scene is six seconds. As such, the predictions do not reflect collisions as the pedestrians in the scene will have crossed the road before our vehicle reaches the pedestrian pose reflected in the images.

<!-- chunk {"id": "body-0059", "role": "body", "section": "Results", "weight": 1.0} -->

We emphasize that the CoverNet predictions do not include straight trajectories because the vehicle slows down before the curve. When visualized as a video, we first predict straight trajectories, followed by predicting left turn trajectories when the vehicle starts slowing down. We highlight the smoothness of the trajectories predicted by our model contrasted against the regression baselines. Figure 4 also suggests that the different alternatives for left turns are better captured by CoverNet than by the baseline models.

<!-- chunk {"id": "body-0060", "role": "body", "section": "Distance function", "weight": 1.0} -->

We analyzed different methods for matching the ground truth to the most suitable trajectory in the trajectory set. Table 1 compares performance using the max, average, and root-mean-square of the point-wise error vector of Euclidean distances for matching ground truth to the "best" trajectory in a fixed trajectory set of size 150. Performance is relatively consistent across all three choices, so we picked the average point-wise $\ell^{2}$ norm to better align with related regression approaches.

<!-- chunk {"id": "body-0061", "role": "body", "section": "Dynamic vs fixed trajectory set coverage", "weight": 1.0} -->

In Figure 3, we compare the number of trajectories needed to achieve 100% coverage of the trajectory set for different levels of $\varepsilon$ for the fixed and hybrid trajectory set generation functions, where the latter use a mix of fixed and dynamic trajectories. This figure highlights the advantage of adding dynamic trajectories: they are able to achieve the same level of coverage as the fixed trajectories, but need a smaller number of trajectories to do so.

<!-- chunk {"id": "body-0062", "role": "body", "section": "Conclusion", "weight": 1.5} -->

We introduced CoverNet, a novel method for multimodal, probabilistic trajectory prediction in real-world, urban driving scenarios. By framing this problem as classification over a diverse set of trajectories, we were able to a) ensure a desired level of coverage of the state space, b) eliminate dynamically infeasible trajectories, and c) avoid the issue of mode collapse. We showed that the size of our trajectory sets remain manageable over realistic prediction horizons. Dynamically generating trajectory sets based on the agent's current state further improved performance. We compared our results to multiple state-of-the-art methods on real-world self-driving datasets (public and internal), and showed that it outperforms similar methods.

<!-- chunk {"id": "body-0063", "role": "body", "section": "Conclusion", "weight": 1.5} -->

Acknowledgments. We would like to thank Emilio Frazzoli and Sourabh Vora for insightful discussions, and Robert Beaudoin for help on the implementation.
