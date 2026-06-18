<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

EVORA: Deep Evidential Traversability Learning for Risk-Aware Off-Road Autonomy

Topics include Robotics, Uncertainty, Deep learning, Accuracy, Learning, EVORA, Uncertainty quantification.

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Traversing terrain with good traction is crucial for achieving fast off-road navigation. Instead of manually designing costs based on terrain features, existing methods learn terrain properties directly from data via self-supervision to automatically penalize trajectories moving through undesirable terrain, but challenges remain to properly quantify and mitigate the risk due to uncertainty in learned models. To this end, this work proposes a unified framework to learn uncertainty-aware traction model and plan risk-aware trajectories. For uncertainty quantification, we efficiently model both aleatoric and epistemic uncertainty by learning discrete traction distributions and probability densities of the traction predictor's latent features. Leveraging evidential deep learning, we parameterize Dirichlet distributions with the network outputs and propose a novel uncertainty-aware squared Earth Mover's distance loss with a closed-form expression that improves learning accuracy and navigation performance. For risk-aware navigation, the proposed planner simulates state trajectories with the worst-case expected traction to handle aleatoric uncertainty, and penalizes trajectories moving through terrain with high epistemic uncertainty.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Our approach is extensively validated in simulation and on wheeled and quadruped robots, showing improved navigation performance compared to methods that assume no slip, assume the expected traction, or optimize for the worst-case expected cost.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

Autonomous robots are increasingly being deployed in harsh off-road environments like mines, forests, and deserts, where both geometric and semantic understanding of the environments is required to identify non-geometric hazards (e.g., mud puddles, slippery surfaces) and geometric non-hazards (e.g., tall grass and foliage) \\editin order to achieve reliable navigation. To this end, recent approaches manually assign navigation costs based on semantic classification of the terrain, requiring significant human expertise to label and train a classifier sufficiently accurate and rich in order to achieve desired risk-aware behaviors. Alternatively, self-supervised learning can be used to learn a model of traversability directly from navigation data \\editto automatically assign higher costs for undesirable terrain during planning. \\editBecause self-supervised data collection in the real world can be slow and expensive, collecting more data is not beneficial unless we properly quantify and mitigate the risk due to uncertainty in the learned models. Uncertainty manifests in two forms as illustrated in Fig. in the context of off-road navigation. Aleatoric uncertainty is the inherent and irreducible uncertainty due to partial observability.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

For example, two patches of terrain may be indistinguishable to the onboard sensors but lead to different vehicle behaviors---such uncertainty cannot be reduced by collecting more data. Epistemic uncertainty is due to out-of-distribution (OOD) inputs encountered at test time that are not well-represented in the training data. \\editBecause it is often undesirable to collect OOD data in dangerous situations such as collisions and falling at the edge of a cliff, there can exist a large gap between training datasets and the various real-world scenarios encountered by the robot. Most existing work in off-road navigation has focused on either aleatoric uncertainty \\editby learning distributions of system parameters instead of point estimates, or epistemic uncertainty \\editby identifying OOD terrain, but limited effort has been made to \\editquantify both types of \\edituncertainty and mitigate the associated risk during planning.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

To achieve fast and reliable off-road navigation, this work considers both the upstream uncertainty-aware traversability learning problem and the downstream risk-aware navigation problem. Recognizing the inter-dependence of the two problems, our proposed pipeline, EVORA (EVidential Off-Road Autonomy), tightly integrates the proposed uncertainty-aware traversability model into the the proposed risk-aware planner. To plan fast trajectories, we model traversability with terrain traction that captures the "slip" or the ratio between \\editachieved and commanded velocities (for example, wet terrain that causes the robot's wheels to slip and reduce its intended velocity has low traction). Moreover, we efficiently quantify both aleatoric and epistemic \\edituncertainty by learning the empirical traction distributions and probability densities of the traction predictor's latent features. \\edit Because real world traction distributions may be multi-modal, as shown in Fig. (a) where vegetation with similar appearance may lead to different traction values, we learn categorical distributions over discretized traction values to capture multi-modality.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

By leveraging the evidential deep learning technique proposed, we parametrize Dirichlet distributions (the conjugate priors for the categorical distributions) with neural network (NN) outputs, and propose a novel uncertainty-aware loss based on the squared Earth Mover's distance. Our loss, which can be computed efficiently in closed-form, better captures the relationship among discretized traction values than the conventional cross entropy-based losses. To handle aleatoric uncertainty, we propose a risk-aware planner that simulates state trajectories using the worst-case expected traction, \\editwhich is shown to achieve improved or competitive performance compared to state-of-the-art methods that rely on the nominal traction, the expected traction or that optimize for the worst-case expected cost. To mitigate the risk due to epistemic uncertainty, the proposed method imposes a confidence threshold on the densities of the traction predictor's latent space features to identify OOD terrain and avoid moving through it using auxiliary planning costs. The overall approach is extensively analyzed in simulation and hardware with wheeled and quadruped robots, demonstrating feasibility and improved navigation performance in practice.

<!-- chunk {"id": "body-0008", "role": "body", "section": "I-A1 \\\\editTraversability Analysis", "weight": 1.0} -->

Suitability of terrain for navigation can be assessed in various ways, e.g., based on proprioceptive measurements, geometric features and combinations of geometric and semantic features. Due to the difficulty of hand-crafting planning costs based on terrain features, self-supervised learning is increasingly being adopted to learn task-relevant traversability representations. For example, \\editLi et al. proposed to learn the support surfaces underneath dense vegetation for legged robot locomotion, and \\editGasparino et al. modeled terrain traction that captures how well the robot can follow the desired velocities. However, these methods do not account for the aleatoric and epistemic \\edituncertainty due to the noisiness and scarcity of real-world data. To capture aleatoric uncertainty, \\editEwen et al. and Cai et al. learned multi-modal terrain properties via Gaussian mixture models or categorical distributions.

<!-- chunk {"id": "body-0009", "role": "body", "section": "I-A1 \\\\editTraversability Analysis", "weight": 1.0} -->

To capture epistemic uncertainty, \\editFrey et al. and Schmid et al. measured the trained NNs' ability to reconstruct terrain similar to the terrain types traversed in the past, and \\editSeo et al. trained a binary classifier for unfamiliar terrain. In comparison, \\editEndo et al. and Lee et al. leveraged Gaussian Process (GP) regression \\editto quantify epistemic uncertainty, but they \\editused a homoscedastic noise model that assumes the noise variance is globally constant. While \\editMurphy et al. adopted heteroscedastic GPs that can handle input-dependent noise, the predictive distributions are not analytically tractable and require approximations. \\edit In contrast, our work explicitly quantifies \\editboth the aleatoric and epistemic uncertainty in the learned traction model that predicts the ratio between achieved and commanded velocities. While we learn traction just like Gasparino et al., our model is uncertainty-aware and can be used to achieve risk-aware navigation.

<!-- chunk {"id": "body-0010", "role": "body", "section": "I-A1 \\\\editTraversability Analysis", "weight": 1.0} -->

In comparison, Frey et al. used the difference between achieved and commanded velocities in the planning objective, but they assumed no slip when simulating the state rollouts. In contrast, our traction model can be used to simulate state rollouts under the worst-case expected traction condition, which is shown by our results to achieve better performance than methods that assume nominal traction when obtaining state rollouts.

<!-- chunk {"id": "body-0011", "role": "body", "section": "I-A2 \\\\editUncertainty Quantification & OOD Detection", "weight": 1.0} -->

Uncertainty quantification is well studied in the machine learning literature with effective techniques such as Bayesian dropout, model ensembles, and evidential methods. In the off-road navigation literature, ensemble methods have been a popular choice, because they typically outperform methods based on Bayesian dropout. In comparison, evidential methods are better suited for real-world deployment, because they only require a single network evaluation without imposing high computation or memory requirements. Therefore, we leverage the evidential method proposed \\editby Charpentier et al. to directly parameterize the conjugate prior distribution of the target distribution with NN outputs \\editin order to quantify both aleatoric and epistemic uncertainty. \\editMoreover, we propose an uncertainty-aware loss based on the squared Earth Mover's Distance proposed by Hou et al. to better capture the relationship among the discrete traction values, resulting in more accurate traction predictions that in turn improve the downstream risk-aware planner's navigation performance.

<!-- chunk {"id": "body-0012", "role": "body", "section": "I-A2 \\\\editUncertainty Quantification & OOD Detection", "weight": 1.0} -->

When deploying the learned traction model, we explicitly identify OOD terrain based on the estimated epistemic uncertainty, which is an instance of the general OOD detection problem. For example, reconstruction-based method adopted by Seo et al. and density-based method adopted by Ancha et al. have shown promising results for off-road navigation to identify unsafe terrain. Similar to Ancha et al., our approach is a density-based approach that explicitly captures the normalized probability density under the training data distribution. Alternatively, energy-based approaches proposed by Liu et al. and Grathwohl et al. do not require explicit density normalization, and similar ideas have been adopted by Castaneda et al. to avoid OOD states. Instead of solely focusing on OOD detection and mitigation, this work quantifies and mitigates the risk due to both aleatoric and epistemic uncertainty. While OOD terrain with high epistemic uncertainty should be avoided at test time, in-distribution terrain may still lead to high aleatoric uncertainty in the predicted traction due to complex vehicle-terrain interactions.

<!-- chunk {"id": "body-0013", "role": "body", "section": "I-A2 \\\\editUncertainty Quantification & OOD Detection", "weight": 1.0} -->

Therefore, the risk due to aleatoric uncertainty should be mitigated separately to improve navigation performance by allowing the robot to trade off the likelihood of experiencing low traction with the potential time savings obtained from traversing terrain with uncertain traction.

<!-- chunk {"id": "body-0014", "role": "body", "section": "I-A3 \\\\editRisk-Aware Planning", "weight": 1.0} -->

The risk of traversing terrain with uncertain traversability values has been represented as costmaps by Fan et al. and Triest et al., where Conditional Value at Risk (CVaR) can be used to measure the cost of encountering worst-case expected failures, which satisfies a group of axioms important for rational risk assessment. \\editInstead of costmaps, navigation performance has also been assessed based on the expected future states by Gibson et al. or the expected terrain traction by Gasparino et al.. However, these methods rely on either the nominal or the expected system behavior, which may provide a poor indication of the actual performance when the vehicle-terrain interaction is noisy \\edit(i.e., high aleatoric uncertainty). \\editAlternatively, Wang et al. proposed to directly optimize the CVaR of the planning objective, which can be estimated by evaluating each control sequence over samples of \\edituncertain parameters, but this approach is computationally expensive.

<!-- chunk {"id": "body-0015", "role": "body", "section": "I-A3 \\\\editRisk-Aware Planning", "weight": 1.0} -->

\\editSimilar to our approach, the recent work of Lee et al. quantified both aleatoric and epistemic uncertainty using probabilistic ensembles and planned risk-aware trajectories by penalizing both types of \\edituncertainty, but it relied on the expected system behaviors. While we adopt a similar strategy used by Lee et al. for handling epistemic uncertainty via auxiliary penalties, we use the worst-case expected system parameters for forward simulation to assess the risk due to aleatoric uncertainty. Our approach is computationally more efficient than the method proposed by Wang et al. and produces behaviors more robust to multi-modal terrain properties observed in the real world compared to methods proposed by Lee et al. and Gasparino et al. that rely on the expected system behaviors.

<!-- chunk {"id": "body-0016", "role": "body", "section": "I-B Contributions", "weight": 1.0} -->

This work proposes an off-road navigation pipeline that tightly integrates the solutions to the uncertainty-aware traversability learning problem and the risk-aware motion planning problem. We explicitly quantify both the epistemic uncertainty to understand when the predicted traction values are unreliable due to novel terrain and the aleatoric uncertainty to enable the downstream planner to mitigate risk due to noisy traction estimates.

<!-- chunk {"id": "body-0017", "role": "body", "section": "I-B Contributions", "weight": 1.0} -->

A probabilistic traversability model based on traction distributions (aleatoric uncertainty), with the ability to identify unreliable predictions via the densities of the traction predictor's latent features (epistemic uncertainty).

<!-- chunk {"id": "body-0018", "role": "body", "section": "I-B Contributions", "weight": 1.0} -->

A novel uncertainty-aware loss based on the squared Earth Mover's Distance with a closed-form expression derived in this work that improves traction prediction accuracy, OOD detection performance, and downstream navigation performance when used together with the uncertainty-aware cross entropy loss.

<!-- chunk {"id": "body-0019", "role": "body", "section": "I-B Contributions", "weight": 1.0} -->

A risk-aware planner based on the CVaR of traction to handle aleatoric uncertainty. Our planner outperforms methods that assume the nominal traction or the expected traction, \\editand achieves improved or competitive performance compared to the method optimizing for the CVaR of cost in both simulation and hardware.

<!-- chunk {"id": "body-0020", "role": "body", "section": "I-B Contributions", "weight": 1.0} -->

A further extension of the risk-aware planner to handle epistemic uncertainty by avoiding OOD terrain, \\editwhich improves the navigation success rate in simulation and reduces human interventions in hardware experiments.

<!-- chunk {"id": "body-0021", "role": "body", "section": "I-B Contributions", "weight": 1.0} -->

The preliminary conference version of this work appeared, \\editwhich proposed to learn traction distributions and use CVaR of traction for planning. This work extends the prior work by \\editusing the evidential learning technique proposed for model training, and deriving a new uncertainty-aware $\text{EMD}^{2}$ loss based to improve learning performance. The new methods introduced in this work not only improve the accuracy of traction prediction and OOD detection but also leads to faster navigation. By adding extensive hardware experiments, this work provides stronger evidence of the performance improvements provided by the risk-aware planner proposed in the conference version compared to the state-of-the-art methods.

<!-- chunk {"id": "body-0022", "role": "body", "section": "Problem \\\\editOverview", "weight": 1.0} -->

We consider the problem of motion planning for a ground vehicle whose dynamics depend on the terrain traction. Because traction values can be uncertain \\editdue to rough terrain and imperfect sensing, we model traction values as random variables whose distributions can be estimated from sensor data using a learned model. \\editNext, we introduce the dynamical models and the planning objective under consideration.

<!-- chunk {"id": "body-0023", "role": "body", "section": "II-A \\\\editDynamical Models with Traction Parameters", "weight": 1.0} -->

where $\mathbf{x}_{t} \in \mathbf{X} \subseteq {\mathbb{R}}^{n}$ is the state vector such as the position and orientation of the robot, $\mathbf{u}_{t} \in {\mathbb{R}}^{m}$ is the control input provided to the robot, and ${\mathbf{ψ}}_{t} \in \mathbf{\Psi} \subseteq {\mathbb{R}}^{r}$ is the parameter vector that \\editcaptures terrain traction. We consider two models that are useful approximations of the dynamics of a wide range of robots as shown in Fig..

<!-- chunk {"id": "body-0024", "role": "body", "section": "II-A \\\\editDynamical Models with Traction Parameters", "weight": 1.0} -->

where $L$ is the wheelbase, $\mathbf{u}_{t} = {\lbrack v_{t},\delta_{t}\rbrack}^{\top}$ contains the commanded linear velocity and steering angle, and ${\mathbf{ψ}}_{t}$ plays the same role as in the unicycle model. The reference point for the bicycle model in is located at the center between the two rear wheels.

<!-- chunk {"id": "body-0025", "role": "body", "section": "II-B \\\\editPlanning Objective", "weight": 1.0} -->

As this work focuses on fast navigation to the goal, we adopt the minimum-time objective used, but other objectives \\editfor goal reaching could also be used. Intuitively, the objective only assigns stage costs by accumulating the elapsed time before any state falls in the goal region. If the state trajectory does not intersect the goal region, the terminal cost further penalizes the estimated time-to-goal.

<!-- chunk {"id": "body-0026", "role": "body", "section": "II-B \\\\editPlanning Objective", "weight": 1.0} -->

where $s^{\text{default}} > 0$ is the default speed for estimating time-to-go and $\Delta > 0$ is the constant time interval. To avoid accumulating costs after arrival at the goal, we use an indicator function $\mathbb{1}^{\text{done}}{(\mathbf{x}_{0:t})}$ that equals $1$ if any state in $\mathbf{x}_{0:t}$ has reached the goal, and equals $0$ otherwise. Although $\Delta$ is a constant, the number of time steps required to reach the goal changes according to the robot speed. Intuitively, this objective encourages the robot to reach the goal as quickly as possible.

<!-- chunk {"id": "body-0027", "role": "body", "section": "II-C Key Challenges", "weight": 1.0} -->

While the \\editobjective can be optimized \\editby finding an optimal control sequence via nonlinear optimization techniques such as Model Predictive Path Integral control, the terrain traction varies across terrain types and needs to be learned from real-world data. However, real-world terrain traction is uncertain since visually and geometrically similar terrain may have different traction properties (aleatoric uncertainty), and the traction models can only be trained on limited data (epistemic uncertainty). Even if uncertainty in terrain traction is quantified accurately, designing risk-aware planners that mitigate the risk of failures under this uncertainty is still challenging. To address these challenges, we introduce our proposed uncertainty-aware traversability model and the risk-aware planner in Sec. III and Sec. IV, respectively.

<!-- chunk {"id": "body-0028", "role": "body", "section": "Uncertainty-Aware Traversability Model", "weight": 1.0} -->

In this section, we first introduce the traction distribution predictor that captures aleatoric uncertainty, and the latent space density estimator that captures epistemic uncertainty. An overview of the traversability analysis pipeline is shown in Fig.. Then, we review \\editthe evidential method proposed in the context of traction learning, and propose a new uncertainty-aware loss to improve learning performance.

<!-- chunk {"id": "body-0029", "role": "body", "section": "III-A Aleatoric Uncertainty Captured in Traction Distribution", "weight": 1.0} -->

Let $\mathbf{\Psi} = {\{{\mathbf{ψ}}^{1},\ldots,{\mathbf{ψ}}^{B}\}}$ be a set of $B > 0$ discretized traction values (ratios between achieved and commanded velocities), and $\mathbf{O}$ be a set of terrain features containing elevation values and one-hot vectors of semantic labels.

<!-- chunk {"id": "body-0030", "role": "body", "section": "III-A Aleatoric Uncertainty Captured in Traction Distribution", "weight": 1.0} -->

We use categorical distributions as convenient alternatives to Gaussian Mixture Models and normalizing flows for learning multi-modal traction distributions observed in practice, because they do not require tuning the number of clusters, generate bounded distributions by construction, and converge faster than normalizing flows based on our empirical experience while achieving similar accuracy. Generally, discretizing a high-dimensional space can be challenging as the number of bins grows exponentially with the dimension. However, categorical distributions are well-suited in our case since we only need to discretize 1-D linear and angular traction values. Therefore a relatively small number of discrete bins suffice.

<!-- chunk {"id": "body-0031", "role": "body", "section": "III-A Aleatoric Uncertainty Captured in Traction Distribution", "weight": 1.0} -->

Examples of real world data collection and offline dataset generation can be found in Fig.. The semantic and geometric information about the environment can be built by using a semantic octomap that temporally fuses semantic point clouds. \\edit We used PointRend trained on the RUGD off-road navigation dataset with 24 semantic categories to segment RGB images and subsequently projected the semantics onto lidar point clouds. During offline dataset generation, we obtained the empirical linear and angular traction distributions by accumulating discretized traction measurements in histograms stored in every terrain cell traversed by the robot. The measurement counts were also stored so that, during training, we could weight the loss for each cell by the measurement counts to discount rarely visited terrain. In practice, we learned the linear and angular traction distributions separately. We used a shared encoder (convolutional layers followed by fully connected layers) to process the semantic and elevation patches of the terrain. The shared encoder is followed by two fully connected decoder heads with soft-max outputs for predicting the linear and angular traction distributions.

<!-- chunk {"id": "body-0032", "role": "body", "section": "III-B Epistemic Uncertainty Captured in Latent Space Density", "weight": 1.0} -->

Due to limited training data, the predicted traction distributions for novel parts of the terrain may be unreliable and lead to degraded navigation performance in those regions. To measure epistemic uncertainty, we want to estimate the density of the latent feature \\edit$\mathbf{z}^{\mathbf{o}} \in {\mathbb{R}}^{H}$ obtained from an intermediate layer of the traction predictor $p_{\mathbf{\phi}}$ based on the terrain feature $\mathbf{o}$.

<!-- chunk {"id": "body-0033", "role": "body", "section": "III-B Epistemic Uncertainty Captured in Latent Space Density", "weight": 1.0} -->

where we use a normalizing flow parameterized by $\mathbf{λ}$ to learn. At a high level, a normalizing flow works by transforming an arbitrary target distribution into a simple base distribution such as a standard normal via a sequence of invertible and differentiable mappings. Then, the density of a sample $\mathbf{z}^{\mathbf{o}}$ can be computed by change of variable formula --- it is the product of the density of the transformed sample under the base distribution, and the change in \\editvolume measured by the determinant of the Jacobian of the transformation. \\edit When selecting the latent space features, it is crucial to ensure that they contain task-relevant information. To this end, we use the latent features produced by the shared terrain feature encoder, because they contain information useful for predicting both linear and angular traction distributions.

<!-- chunk {"id": "body-0034", "role": "body", "section": "III-B Epistemic Uncertainty Captured in Latent Space Density", "weight": 1.0} -->

During deployment, terrain features with a confidence score below some threshold $g^{\text{thres}} \in {\mathbb{R}}$ are deemed OOD; these regions with OOD terrain features can be explicitly avoided during planning via auxiliary penalties. A principled way to set $g^{\text{thres}}$ is to use the $\kappa$-th percentile of the densities obtained from all the terrain features in the training dataset, where a higher value of $\kappa \in {\lbrack 0,100\rbrack}$ will cause more terrain features to be classified as OOD at test time. Because of the normalization, $g^{\text{thres}} = 0$ and $g^{\text{thres}} = 1$ conveniently correspond to the 0-th and 100-th percentiles. Note that the threshold can be selected offline, and $g^{\text{thres}} = 0$ can be used if the robot should only avoid terrain features with densities lower than densities observed during training.

<!-- chunk {"id": "body-0035", "role": "body", "section": "III-B Epistemic Uncertainty Captured in Latent Space Density", "weight": 1.0} -->

This strategy improves navigation success rate when the learned traction models are deployed in environments unseen during training, both in simulations (see Sec. VIII) and in hardware experiments (see Sec. IX-B).

<!-- chunk {"id": "body-0036", "role": "body", "section": "III-C Evidential Deep Learning", "weight": 1.0} -->

While the traction predictor and the density estimator can be trained sequentially, Charpentier et. al. have shown that joint training using evidential deep learning can improve OOD detection performance while retaining prediction accuracy. In this section, we review the method and training loss proposed, where NN outputs parameterize Dirichlet distributions (the conjugate priors of categorical distributions).

<!-- chunk {"id": "body-0037", "role": "body", "section": "III-C Evidential Deep Learning", "weight": 1.0} -->

The parameters $\mathbf{p}$ of the lower level categorical distribution ${Cat}{(\mathbf{p})}$ are sampled from the higher level Dirichlet distribution i.e. $\mathbf{p} \sim {\text{Dir}{({\mathbf{β}})}}$. The mean (also called the expected PMF) of the Dirichlet distribution is given by ${{\mathbb{E}}_{\mathbf{p} \sim q}\lbrack\mathbf{p}\rbrack} = {{\mathbf{β}}/{\sum_{b = 1}^{B}\beta_{b}}}$. The expected PMF captures aleatoric uncertainty. The sum of the parameters $\mathbf{β}$ i.e. $\sum_{b = 1}^{B}\beta_{b}$ represents how concentrated the Dirichlet distribution is around its mean.

<!-- chunk {"id": "body-0038", "role": "body", "section": "III-C Evidential Deep Learning", "weight": 1.0} -->

Therefore, $\sum_{b = 1}^{B}\beta_{b}$ is also known as the concentration parameter, and corresponds to the "total evidence" of a data point observed in the training set. Higher data evidence corresponds to lower epistemic uncertainty.

<!-- chunk {"id": "body-0039", "role": "body", "section": "III-C Evidential Deep Learning", "weight": 1.0} -->

Based on this formulation proposed, the posterior Dirichlet distribution $q_{\mathbf{\phi},{\mathbf{λ}}}^{\mathbf{o}}$ and expected traction distribution $\mathbf{p}_{\mathbf{\phi},{\mathbf{λ}}}^{\mathbf{o}}$ both depend on the traction predictor, density estimator and the input features. While the analysis of loss functions we perform below is for a generic Dirichlet distribution $q = {\text{Dir}{({\mathbf{β}})}}$ and PMF $\mathbf{p}$ for notational convenience, the posterior Dirichlet distribution and its expected PMF should be substituted by during training.

<!-- chunk {"id": "body-0040", "role": "body", "section": "III-C Evidential Deep Learning", "weight": 1.0} -->

The ablation study has shown that \\edittraining with improves OOD detection performance while retaining similar accuracy achieved using the conventional cross entropy (CE) loss. However, the key limitation of CE-based losses in our use case is that they treat the prediction errors across bins independently. The independence assumption is undesirable for learning traction where bins are obtained by discretizing continuous traction values. These bins are ordered --- bins closer to each other should be treated more similarly than bins far apart. We address this limitation by proposing a new loss function based on the squared Earth Mover's Distance that has been shown to achieve better accuracy than CE-based losses when bins are ordered.

<!-- chunk {"id": "body-0041", "role": "body", "section": "III-D Uncertainty-Aware Squared Earth Mover's Distance", "weight": 1.0} -->

Intuitively the Earth Mover's Distance (EMD) between two distributions measures the minimum cost of transporting the probability mass of one distribution to the other, which has a closed-form solution for two categorical distributions defined by PMFs with the same number of bins.

<!-- chunk {"id": "body-0042", "role": "body", "section": "III-D Uncertainty-Aware Squared Earth Mover's Distance", "weight": 1.0} -->

where $\text{cs}:{{\mathbb{R}}^{B}\rightarrow{\mathbb{R}}^{B}}$ is the cumulative sum operator. For convenience during training, we use $l = 2$ for Euclidean distance and optimize the squared EMD loss ($\text{EMD}^{2}$), dropping the constant factor. The toy example in Fig. clearly shows that $\text{EMD}^{2}$ better captures the physical meaning of the predicted PMFs than CE which ignores the relationship between bins.

<!-- chunk {"id": "body-0043", "role": "body", "section": "III-D Uncertainty-Aware Squared Earth Mover's Distance", "weight": 1.0} -->

Note that $\text{cs}{(\overline{\mathbf{p}})}$ can also be written as ${\text{cs}{({\mathbf{β}})}}/\beta_{0}$ due to the linearity of the cumulative sum operator. However, $L^{\text{EMD}^{2}}$ is invariant to the \\edittotal evidence $\beta_{0}$ of the Dirichlet distribution, as illustrated in the toy example in Fig., so the epistemic uncertainty cannot be learned accurately.

<!-- chunk {"id": "body-0044", "role": "body", "section": "III-D Uncertainty-Aware Squared Earth Mover's Distance", "weight": 1.0} -->

The following theorem states that our proposed $\text{UEMD}^{2}$ loss can be computed in a closed form.

<!-- chunk {"id": "body-0045", "role": "body", "section": "Planning with Learned Traction Distribution", "weight": 1.0} -->

While OOD terrain causing high epistemic uncertainty should be avoided, in-distribution terrain may still lead to high aleatoric uncertainty due to complex vehicle-terrain interactions. Therefore, we propose a risk-aware planner that trades off the risk of immobilization with potential time savings from traversing terrain that leads to high aleatoric uncertainty.

<!-- chunk {"id": "body-0046", "role": "body", "section": "IV-A Conditional Value at Risk (CVaR)", "weight": 1.0} -->

We adopt the Conditional Value at Risk (CVaR) as a risk metric because it satisfies a group of axioms important for rational risk assessment. The conventional definition of CVaR assumes the worst-case occurs at the right tail of the distribution.

<!-- chunk {"id": "body-0047", "role": "body", "section": "IV-A Conditional Value at Risk (CVaR)", "weight": 1.0} -->

Intuitively, $\text{CVaR}_{\alpha}^{\rightarrow}{(Z)}$ and $\text{CVaR}_{\alpha}^{\leftarrow}{(Z)}$ capture the expected outcomes that fall in the right tail and left tail of the distribution, respectively, where each tail occupies $\alpha$ portion of the total probability. Note that the right-tail definitions are suitable for costs to be minimized, and the left-tail definitions are suitable for low traction values. When $\alpha = 1$, either definition of CVaR is equivalent to the mean of the distribution ${\mathbb{E}}{\lbrack Z\rbrack}$.

<!-- chunk {"id": "body-0048", "role": "body", "section": "IV-B \\\\editRisk-Aware Planning", "weight": 1.0} -->

To account for the risk due to uncertain traction, we first present an existing approach that optimizes for the right-tail CVaR of the planning objective (CVaR-Cost), and then propose a more computationally efficient method that accounts for the left-tail CVaR of traction (CVaR-Dyn). \\editLastly, we discuss the advantages and limitations of these two methods.

<!-- chunk {"id": "body-0049", "role": "body", "section": "IV-B1 Worst-Case Expected Cost (CVaR-Cost )", "weight": 1.0} -->

Given the initial state $\mathbf{x}_{0}$, we want to find a control sequence $\mathbf{u}_{0:{T - 1}}$ that minimizes the worst-case expected value of the nominal objective $C$ given uncertain terrain traction: \\edit

<!-- chunk {"id": "body-0050", "role": "body", "section": "IV-B1 Worst-Case Expected Cost (CVaR-Cost )", "weight": 1.0} -->

where traction ${\overset{\sim}{\mathbf{ψ}}}_{t}$ is realized based on the predicted traction PMF $\mathbf{p}_{\mathbf{\phi},{\mathbf{λ}}}^{{\overset{\sim}{\mathbf{o}}}_{t}}$ after observing the terrain feature ${\overset{\sim}{\mathbf{o}}}_{t}$. Due to the uncertain traction, the original objective $C{({\overset{\sim}{\mathbf{x}}}_{0:T})}$ is now a random variable that depends on the realization of the state trajectory. Note that this approach is inspired, but we additionally handle terrain-dependent traction distributions.

<!-- chunk {"id": "body-0051", "role": "body", "section": "IV-B1 Worst-Case Expected Cost (CVaR-Cost )", "weight": 1.0} -->

In practice, optimizing ) using MPPI requires a subroutine that empirically estimates the right-tail CVaR of the objective by collecting $M > 0$ realizations of the nominal objective ${\{{C{({\overset{\sim}{\mathbf{x}}}_{0:T}^{m})}}\}}_{m = 1}^{M}$ for each candidate control sequence by using sampled traction values. To exploit GPU parallelization, we pre-generate $M > 0$ traction maps where each map cell contains sampled traction values. As a result, each candidate control sequence can be evaluated in parallel for all the pre-generated traction maps. While the sampled traction maps can be reused, the computation can still grow prohibitively as the map size grows. Therefore, we propose a cheaper cost design that accounts for the left-tail CVaR of terrain traction.

<!-- chunk {"id": "body-0052", "role": "body", "section": "IV-B2 Worst-Case Expected Terrain Traction (CVaR-Dyn)", "weight": 1.0} -->

where ${\overline{\mathbf{ψ}}}_{t}$ contains the left-tail CVaR of the linear and angular traction based on the predicted traction PMF $\mathbf{p}_{\mathbf{\phi},{\mathbf{λ}}}^{{\overline{\mathbf{o}}}_{t}}$ after observing the terrain feature ${\overline{\mathbf{o}}}_{t}$. When $\alpha = 1$, the expected values of the traction parameters are used, equivalent to the \\editplanning approach used.

<!-- chunk {"id": "body-0053", "role": "body", "section": "IV-B3 \\\\editAdvantages and Limitations", "weight": 1.0} -->

Both CVaR-Cost and CVaR-Dyn leverage intuitive notions of risk based on the worst-case expected cost and traction, respectively. Moreover, they are simple to tune with a single risk parameter $\alpha$ regardless of the number of terrain types. Note that CVaR-Cost is a general algorithm that handles uncertainty in the planning problem. In comparison, CVaR-Dyn is computationally cheaper, but it exploits the intuition that low traction usually worsens time-to-goal. However, such relationship between system parameters and task performance may not hold for more complicated systems and different tasks.

<!-- chunk {"id": "body-0054", "role": "body", "section": "Evaluation of Traversability Learning Pipeline", "weight": 1.0} -->

The proposed evidential traversability learning method is benchmarked using a synthetic terrain dataset (Sec. V-A) designed to simulate data scarcity during real-world data collection and provide ground truth traction distributions and OOD terrain masks. Several variants of the proposed loss are compared based on prediction accuracy and OOD detection performance (Sec. V-C). To highlight the benefits of joint training and our $\text{UEMD}^{2}$ loss, we provide an ablation study in Sec. V-D. After analyzing the proposed planner in Sec. VI, Sec. VII contains key results that show improved navigation performance due to our proposed loss.

<!-- chunk {"id": "body-0055", "role": "body", "section": "Evaluation of Traversability Learning Pipeline", "weight": 1.0} -->

As comparing uncertainty quantification methods is not the main focus of this work, we refer interested readers to that has demonstrated the computational advantages, learning accuracy and OOD detection performance of the NN architecture used in this work compared to the other state-of-the-art uncertainty quantification methods.

<!-- chunk {"id": "body-0056", "role": "body", "section": "V-A Synthetic 3D Terrain Datasets", "weight": 1.0} -->

The synthetic dataset contains randomly generated 3D terrain with ground truth traction distributions generated based on geometric properties (elevation and slope) and semantic types (dirt and vegetation); details are available in Table I. \\editNote that terrain slopes are only used for generating the ground truth traction distributions, but are not used as inputs to the NN. For simplicity, we use the same traction distribution for both linear and angular components, and dependencies only exist between dirt and terrain slope, and vegetation and terrain elevation. While more complex traction distributions can be designed, our dataset is sufficient for supporting our contributions.

<!-- chunk {"id": "body-0057", "role": "body", "section": "V-A Synthetic 3D Terrain Datasets", "weight": 1.0} -->

In total, there are 5 training, 20 test, and 40 OOD environments that are 30 meters in width and height, 0.5 meters in resolution, as well as different elevations, slopes and vegetation ratios, where the training dataset is intentionally small in order to examine the generalization of learned models. Every training environment is split into equal parts for training and cross validation respectively. The synthetic environments are selectively visualized in Fig.. To simulate real-world data collection, traction samples are only obtained along a circular path. Moreover, we consider the impact of increasing the number of samples by multiplying the base measurement counts by factors $10^{k}$ where $k \in {\{ 0,\ldots,4\}}$. \\editFor the training environments, the traction samples are accumulated in traversed terrain cells via histograms to obtain the empirical traction distributions, and the measurement counts are also stored in order to weight the training loss to discount the rarely visited terrain. In the test environments, we use the ground truth traction distributions to measure the prediction accuracy of trained models. In the OOD environments, terrain with slope and elevation values unseen in the training dataset are considered OOD.

<!-- chunk {"id": "body-0058", "role": "body", "section": "V-A Synthetic 3D Terrain Datasets", "weight": 1.0} -->

The associated OOD masks are the ground truth used to benchmark OOD detection performance. An example of the OOD mask is visualzied in Fig. (c).

<!-- chunk {"id": "body-0059", "role": "body", "section": "V-B Model Training", "weight": 1.0} -->

We use the same network architecture for all the loss functions, where the traction predictor \\editconsists of a shared encoder (convolutional layers followed by fully connected layers) to process the semantic and elevation patches of the terrain, and two fully connected decoder heads with soft-max outputs for predicting the linear and angular traction distributions. The latent space features \\editfrom the shared encoder are passed to a radial flow and we use a constant certainty budget that scales exponentially with the latent dimension for numerical purposes. \\editDuring training, we follow the two-step procedure outlined. First, we jointly train the traction distribution predictor and the flow network. After convergence, we freeze the traction predictor and only fine-tune the flow network. This strategy improves OOD detection accuracy. However, we observe no improvement by performing "warm-up training" for the flow network prescribed.

<!-- chunk {"id": "body-0060", "role": "body", "section": "V-B Model Training", "weight": 1.0} -->

Hyperparameter sweeps are conducted over learning rates in $\lbrack{{1e} - 4},{{3e} - 4},{{1e} - 3}\rbrack$ for the Adam optimizer, and entropy weights in $\lbrack 0,{{1e} - 6},{{1e} - 5}\rbrack$ when $\text{UEMD}^{2}$ and UCE are used separately. For the weighted sum of $\text{UEMD}^{2}$ and UCE, we fix the UCE term and consider additional weights for $\text{UEMD}^{2}$ in $\lbrack 0.1,1,10\rbrack$.

<!-- chunk {"id": "body-0061", "role": "body", "section": "V-B Model Training", "weight": 1.0} -->

For each combination of hyperparameters, we train the model with five random seeds and select the best model based on validation $\text{EMD}^{2}$ error averaged over the seeds because empirically, we have found that selecting models based on validation $\text{EMD}^{2}$ instead of Kullback-Leibler (KL) divergence leads to improved performance for all models. To guarantee fairness for the state-of-the-art and not clutter the figures, we only present the results for models selected based on validation KL divergence for the UCE loss.

<!-- chunk {"id": "body-0062", "role": "body", "section": "V-C Prediction Accuracy and OOD Detection Performance", "weight": 1.0} -->

Variations of the proposed loss function are compared in terms of prediction accuracy and OOD detection performance. The prediction accuracy is measured by $\text{EMD}^{2}$ and KL divergence by comparing the predicted and the ground truth traction distributions. The accuracy of OOD detection using the densities of latent features is measured by area under the receiver operating characteristic curve (AUC-ROC) and area under the precision-recall curve (AUC-PR) with respect to the ground truth OOD masks. Note that AUC-ROC and AUC-PR are standard metrics for binary classification that are invariant to scale and offset. Intuitively, a score of 0.5 means the classifier is as good as random guesses, and a score of 1 indicates a perfect classifier. To show the best performance achievable by the state-of-the-art with unlimited traction samples during training, we include models trained with UCE using the ground truth traction distributions in the training environments. \\edit The benchmark results are in Fig., where we report the average values and the standard deviations over all map cells, test environments and random seeds.

<!-- chunk {"id": "body-0063", "role": "body", "section": "V-C Prediction Accuracy and OOD Detection Performance", "weight": 1.0} -->

The main takeaway from the benchmark is that the models trained with the proposed weighted sum of $\text{UEMD}^{2}$ and UCE achieves the best prediction accuracy in both $\text{EMD}^{2}$ and KL divergence. Furthermore, the weighted-sum objective \\editleads to more stable improvements in test performance for both prediction accuracy and OOD detection as training samples become more abundant. \\edit Interestingly, too many training samples lead to degrading prediction accuracy achieved by the other loss designs at test time. Because we do not observe worsening accuracy on validation dataset, the degrading test performance can be attributed to the distribution shift between the training and test environments as shown in Table. I. Notably, compared to $\text{EMD}^{2}$-based losses, UCE does not capture the cross-bin relationship of the traction distribution, which leads to worse regularized latent space that causes unstable OOD detection performance (even for UCE trained with ground truth traction distributions in the training environments).

<!-- chunk {"id": "body-0064", "role": "body", "section": "V-D Ablation Study for $\\text{UEMD}^{2}$ and Joint Training", "weight": 1.0} -->

While the benefits of using uncertainty-aware loss and joint training have been established for UCE, we present a similar ablation study for $\text{UEMD}^{2}$ for completeness in Table. II. We set the sample multiplier to 10 for simplicity, but similar conclusions can be drawn with more samples. The takeaway is that both joint training and uncertainty awareness are required to achieve improved accuracy in $\text{EMD}^{2}$ and OOD detection. Despite these improvements, the results in Fig. show that both $\text{UEMD}^{2}$ and UCE are required to achieve more consistent and steadily improving performance in prediction accuracy and OOD detection performance.

<!-- chunk {"id": "body-0065", "role": "body", "section": "Evaluation of Risk-Aware Planners", "weight": 1.0} -->

Using simulated 2D semantic environments \\editwhose terrain traction has high aleatoric uncertainty, we show that the proposed CVaR-Dyn outperforms existing approaches that assume the nominal traction or the expected traction, while achieving \\editcompetitive performance compared to CVaR-Cost. Moreover, we discuss the advantages and limitations of \\editCVaR-Dyn and CVaR-Cost compared to the approach that assumes nominal traction while penalizing trajectories moving through terrain with high aleatoric uncertainty. For simplicity, we consider a grid world where dirt and vegetation cells have known traction distributions, as shown in Fig.. Vegetation cells are randomly spawned with increasing probabilities at the center of the arena, and a robot may \\editget stuck due to vegetation's bi-modal traction distribution. \\editThe mission is successful if the robot reaches the goal without encountering zero-traction regions, colliding with obstacles, or getting stuck in local minima (e.g., when the robot does not move or just repeat circular trajectories without progressing to the goal).

<!-- chunk {"id": "body-0066", "role": "body", "section": "VI-A Planner Implementation", "weight": 1.0} -->

We adopt MPPI \[, Algorithm 2\] because it is derivative-free and parallelizable on GPU. The planners run in a receding horizon fashion with 100 timesteps at 0.1 s intervals. The maximum linear and angular speeds are 3 m/s and $\pi$ rad/s, and the noise standard deviations for the control signals are 2 m/s and 2 rad/s. The number of control rollouts is 1024, and the number of sampled traction maps is 1024 (only for CVaR-Cost). We use PMFs with 20 uniform bins to approximate the traction distribution. A computer with Intel Core i9 CPU and Nvidia GeForce RTX 3070 GPU is used for the simulations, where the majority of the computation happens on the GPU. The CVaR-Cost planner is the most expensive to compute, but it is able to re-plan at 15 Hz while sampling new control actions and maps with dimensions of $200 \times 200$. Planners that do not sample traction maps can be executed at over 50 Hz.

<!-- chunk {"id": "body-0067", "role": "body", "section": "VI-B Navigation Performance", "weight": 1.0} -->

We compare the proposed CVaR-Dyn against CVaR-Cost, WayFAST that uses the expected traction, and the technique that assumes the nominal traction while adjusting the time cost with the CVaR of linear traction. Note that WayFAST is a vision-based navigation approach that predicts the expected terrain traction from images, but our analysis only focuses on the use of the expected traction values and its impact on the navigation performance. We vary the conservativeness of all the methods (other than WayFAST) by changing the quantile $\alpha \in {(0,1\rbrack}$ for computing the CVaR. Overall, we sample $40$ different semantic maps and $5$ random realizations of traction parameters for every semantic map. The traction parameters are drawn before starting each trial and remain fixed. \\edit The benchmark results can be found in Fig.. The takeaway is that the proposed CVaR-Dyn achieves better or similar success rate and time-to-goal when compared to CVaR-Cost if the risk tolerance $\alpha$ is sufficiently low. In addition, both CVaR-Dyn and CVaR-Cost outperform the other methods that use the nominal or the expected traction values.

<!-- chunk {"id": "body-0068", "role": "body", "section": "VI-B Navigation Performance", "weight": 1.0} -->

To compare CVaR-based methods against \\editanother baseline that plans with the nominal traction while imposing auxiliary penalties for vegetation terrain with high aleatoric uncertainty, we focus on the most challenging setting with 70% vegetation, where it is easy to get stuck in local minima. \\edit To adjust risk tolerance, we consider $\alpha \in {(0,1\rbrack}$ for CVaR-based methods and vegetation penalty $w \geq 0$ for the planner that assumes nominal traction. The benchmark result in Fig. shows the trade-offs between success rate and time-to-goal achieved by different methods (WayFAST included as a special case of CVaR-Dyn when $\alpha = 1$). Overall, all methods except WayFAST can be tuned to improve success rate and time-to-goal. Assigning high vegetation penalties leads to the best success rate, because we observe that the robot always avoids the vegetation terrain. On the other hand, CVaR-Dyn and CVaR-Cost can achieve better time-to-goal at a lower success rate, which may be desirable for more risk-tolerant and time-critical missions.

<!-- chunk {"id": "body-0069", "role": "body", "section": "VI-B Navigation Performance", "weight": 1.0} -->

As $\alpha$ decreases further, CVaR-Dyn's performance first plateaus and then worsens, because the state rollouts become too short when using the worst-case expected traction, making CVaR-Dyn susceptible to local minima. While CVaR-Cost also experiences worsening performance as $\alpha$ decreases, its conservativeness is caused by the greater difficulty of estimating CVaR of objective. Overall, none of methods completely dominate the others. Therefore, when domain knowledge is available, auxiliary penalties for undesirable terrain can be used together with CVaR-based methods to improve performance (see Sec. VIII). While the simulation shows comparable performance achieved by CVaR-Dyn, CVaR-Cost and the baseline, we show that CVaR-Dyn achieves the best performance in practice (see Sec. IX).

<!-- chunk {"id": "body-0070", "role": "body", "section": "Optimizing for $\\text{EMD}^{2}$ Improves Navigation", "weight": 1.0} -->

To support the key argument that $\text{EMD}^{2}$ is a better metric than KL divergence for measuring the quality of learned traction distributions for navigation, we evaluate the navigation performances when using models trained with different losses presented in Sec. V. The models are deployed in the same test environments visualized in Fig., where each map is 30 m in width and height and the start and goal positions are at the opposite diagonal corners. To not clutter the results, we only focus on the proposed CVaR-Dyn planner with $\alpha = 0.4$ and the same MPPI setup in Sec. VI-A, but similar trend can be observed with different choices of $\alpha$. Consistent with the loss benchmark in Sec. V, each loss is trained with 5 random seeds and 5 levels of data abundance. For each of the 20 test maps, we consider 5 randomly sampled traction maps and run the mission 3 times. The final results averaged over training seeds can be found in Fig., where all trials are successful, so the success rate is omitted.

<!-- chunk {"id": "body-0071", "role": "body", "section": "Optimizing for $\\text{EMD}^{2}$ Improves Navigation", "weight": 1.0} -->

Importantly, when the amount of \\edittraining data is low, $\text{UEMD}^{2}$ outperforms UCE in time-to-goal even though $\text{UEMD}^{2}$ leads to worse KL error than UCE loss as shown in Fig.. This validates our intuition that $\text{EMD}^{2}$ captures the cross-bin information of discretized traction values better, which facilitates the learning of traction distribution in low-data regime and leads to better navigation performance. \\edit As more training data becomes available, the proposed weighted sum of $\text{UEMD}^{2}$ and UCE outperforms the other loss designs. Due to the distribution shift between the training and test environments as discussed in Sec. V-C, the traction prediction accuracy may degrade when given too much training data, resulting in degrading navigation performance observed in Fig.. However, the proposed hybrid loss is less susceptible to the distribution shift, thus sustaining the navigation performance better than the other methods.

<!-- chunk {"id": "body-0072", "role": "body", "section": "Optimizing for $\\text{EMD}^{2}$ Improves Navigation", "weight": 1.0} -->

Furthermore, the navigation performance of the proposed hybrid loss approaches the best possible performance of the state-of-the-art UCE loss when trained on ground truth traction distributions in the training environments, indicating good generalization of our approach using only \\editthe limited data collected along circular paths in the training environments. For reference, the figure also provides the lower bound for the \\edittime-to-goal based on the ground truth traction models in the test environments.

<!-- chunk {"id": "body-0073", "role": "body", "section": "Benefits of Avoiding OOD Terrain", "weight": 1.0} -->

We demonstrate the benefit of the proposed density-based confidence score for detecting terrain with high epistemic uncertainty. To simulate training and test environments, we leverage the data collected in two distinct forests using Clearpath Husky, where the first one is used for training, and the second one is used as the test environment. \\editThe environment models were built using semantic octomaps that fused lidar points and segmented RGB images based on the 24 semantic categories in the RUGD dataset. The traction values will be drawn from the test environment's empirical traction distributions learned by a separate NN as the proxy ground truth. \\editWe use the proposed CVaR-Dyn with a low risk tolerance $\alpha = 0.2$ to handle the noisy terrain traction. Two specific start-goal pairs have been selected to highlight the most challenging parts of the test environment with novel features. Each start-goal pair is repeated 10 times for each selected confidence threshold $g^{\text{thres}}$. We investigate two ways to prevent the planner from entering terrain that is \\editclassified as OOD by either assigning zero traction, or adding large penalties. The mission is deemed successful if the goal is reached.

<!-- chunk {"id": "body-0074", "role": "body", "section": "Benefits of Avoiding OOD Terrain", "weight": 1.0} -->

As shown in Fig., the success rate improves by up to $30\%$ \\editas the confidence threshold $g^{\text{thres}}$ increases, because the robot avoids regions with unreliable traction predictions. Interestingly, using CVaR-Dyn with soft penalties for OOD terrain leads to better time-to-goal while retaining a similar success rate, because the auxiliary costs for OOD terrain make it easier for the planner to find trajectories that avoid the OOD terrain. Therefore, it is advantageous to use CVaR-Dyn with auxiliary costs when domain knowledge is available to achieve both a high success rate and fast navigation in practice.

<!-- chunk {"id": "body-0075", "role": "body", "section": "Hardware Experiments", "weight": 1.0} -->

To evaluate the effectiveness and feasibility of EVORA (the overall framework for uncertainty-aware traversability learning and risk-aware planning) in practice, we designed two experiment scenarios---an indoor race track scenario with fake vegetation using an RC car (Sec. IX-A) and a more challenging outdoor scenario using a legged robot (Sec. IX-B). \\edit For both scenarios, the robots used onboard sensors to map the environments online at test time, introducing more uncertainty due to motion blurs, lighting changes and incomplete maps. While both scenarios show that the proposed CVaR-Dyn planner leads to the best navigation performance, the outdoor scenario also shows the benefits of avoiding OOD terrain. In practice, the control signals generated by MPPI are very noisy, so we plan in the derivative space of the nominal control to generate smooth trajectories.

<!-- chunk {"id": "body-0076", "role": "body", "section": "IX-A Indoor Racing with an RC Car", "weight": 1.0} -->

The goal of the indoor experiments is to show the performance benefits of the proposed planner for mitigating the risk due to aleatoric uncertainty in a controlled environment.

<!-- chunk {"id": "body-0077", "role": "body", "section": "IX-A1 \\\\editExperiment Setup", "weight": 1.0} -->

An overview of the indoor setup is provided in Fig., which shows the 9.6 m by 8 m arena populated with turf and fake trees used to mimic outdoor vegetation. The 0.33 m by 0.25 m RC car was equipped with a RealSense D455 depth camera, an Intel Core i7 CPU, and a Nvidia RTX 2060 GPU. The robot ran onboard traction prediction, motion planning, and online elevation mapping with 0.1 m resolution, but Vicon was used for ground truth pose and velocity estimation. We identified vegetation by extracting the green image pixels instead of using a standalone NN semantic classifier in order to conserve GPU resources. The bicycle model was used for this experiment, and the traction values were obtained by analyzing the commanded linear velocities, steering angles, and the ground truth velocities from Vicon.

<!-- chunk {"id": "body-0078", "role": "body", "section": "IX-A1 \\\\editExperiment Setup", "weight": 1.0} -->

The traction model was trained based on 10 min of driving data with the proposed loss function, where $\text{UEMD}^{2}$ and UCE were both weighted by 1 and the entropy term was weighted by ${1e} - 5$ based on empirical tuning. The learned traction distributions are visualized in Fig. a to highlight multi-modality. At deployment time, the robot ran 2 laps around the race track along the ellipsoidal reference path, while deciding between a shorter path covered with vegetation or a less risky detour, as shown in Fig. b. We designed a moving goal region along the reference path, called the "carrot goal", that maintained a constant 75 degree offset from the robot's projected position on the ellipsoidal reference path. In addition to CVaR-Cost and the proposed CVaR-Dyn, we considered an intelligent baseline that assumes nominal traction but assigns auxiliary penalties for low-lying vegetation between 5 cm and 15 cm that could cause unfavorable driving conditions. All methods avoided the trees via auxiliary penalties. All planners considered 1024 rollouts while planning at 20 Hz with 5 s look-ahead.

<!-- chunk {"id": "body-0079", "role": "body", "section": "IX-A1 \\\\editExperiment Setup", "weight": 1.0} -->

Due to computational constraints, CVaR-Cost only considered 400 traction map samples. We set the maximum linear speed and steering angle to be 1.5 m/s and 30 degrees.

<!-- chunk {"id": "body-0080", "role": "body", "section": "IX-A2 \\\\editAleatoric Uncertainty Results", "weight": 1.0} -->

The qualitative and quantitative results comparing planners' abilities to mitigate the risk due to aleatoric uncertainty are summarized in Fig. and Fig.. We considered 3 risk tolerances $\alpha \in {\{ 0.6,0.8,1\}}$ for CVaR-Dyn, CVaR-Cost and vegetation penalties $w \in {\{ 10,20,100\}}$ for the baseline that assumes nominal traction while penalizing states entering vegetation terrain. We present results for WayFAST separately, but it is a special case of CVaR-Dyn when $\alpha = 1$. We repeated the race 5 times and each race consisted of 2 laps. Overall, CVaR-Dyn with $\alpha = 0.8$ achieved the best time-to-goal and success rate. Qualitative visualizations in Fig. show that the baseline and WayFAST both suffered from noisy real-world traction, causing wide turns. In comparison, CVaR-Cost and the proposed CVaR-Dyn handled the noisy terrain traction better by producing smoother trajectories.

<!-- chunk {"id": "body-0081", "role": "body", "section": "IX-A2 \\\\editAleatoric Uncertainty Results", "weight": 1.0} -->

Different from CVaR-Dyn, the CVaR-Cost planner more frequently took the detour and sometimes got stuck in local minima near obstacles.

<!-- chunk {"id": "body-0082", "role": "body", "section": "IX-B Outdoor Navigation with a Legged Robot", "weight": 1.0} -->

Compared to the indoor setting, the outdoor experiments introduce more diverse terrain types and uncertainty in perception due to lighting changes and rough motions. In addition to benchmarking the planners' ability to handle aleatoric uncertainty, the outdoor tests also demonstrate the benefits of mitigating epistemic uncertainty by avoiding OOD terrain, as well as the applicability of our approach on a legged robot.

<!-- chunk {"id": "body-0083", "role": "body", "section": "IX-B1 \\\\editExperiment Setup", "weight": 1.0} -->

An overview of the outdoor setup is shown in Fig.. A Boston Dynamics Spot robot was fitted with a RealSense D455, an Ouster OS0 lidar, and an Nvidia Jetson AGX Orin with good power efficiency but less powerful computation than the computers used in previous experiments. The unicycle model was used for this experiment, and traction values were obtained by comparing the commanded velocities and Spot's built-in odometry. \\editThe environment model was built using a semantic octomap that fused lidar points and segmented RGB images based on the 24 semantic categories in the RUGD dataset. The traction model was trained based on 5 minutes of walking data with the proposed loss function with the same weights used for the indoor experiment. The learned traction distributions are selectively visualized in Fig. a to highlight multi-modality. As shown in Fig. b, we chose 2 start-goal pairs for testing the planners and assessing the benefits of avoiding OOD terrain, respectively. All planners avoided the terrain with elevation greater than 1.4 m via auxiliary penalties, and the baseline assigned soft costs for the grass and bush semantic types with elevations less than 1.4 m.

<!-- chunk {"id": "body-0084", "role": "body", "section": "IX-B1 \\\\editExperiment Setup", "weight": 1.0} -->

While the 1.4 m height threshold is much higher than the robot's step height, the selected test environments did not have short and rigid obstacles in order to analyze the planners' ability to handle tall vegetation. The robot maintained a semantic octomap with 0.2 m resolution by fusing semantic pointclouds generated from projecting semantic images to lidar pointcloud for accurate depth. Due to limited GPU resources shared by semantic classification, traction prediction, and motion planning, the planners could only reliably plan at 5 Hz with 8 s look-ahead and 800 control rollouts, and CVaR-Cost was only allowed 200 traction map samples. The maximum linear and angular velocities were 1 m/s and 90 degree/s.

<!-- chunk {"id": "body-0085", "role": "body", "section": "IX-B2 \\\\editAleatoric Uncertainty Results", "weight": 1.0} -->

The qualitative and quantitative results comparing planners' abilities to mitigate the risk due to aleatoric uncertainty are shown in Fig. and Fig.. We considered 3 round trips to and from the goal (6 trials in total) for each method. Overall, CVaR-Dyn with $\alpha = 0.9$ achieved the best time-to-goal and success rate, consistent with the indoor experiments in Sec. IX-A. The CVaR-Cost planner was more conservative by staying far from the bushes. In comparison, the baseline and WayFAST both suffered from noisy real-world traction, causing wide turns. Notably, when the soft penalty for grass and bush semantic types was too high, the baseline planner was stuck in local minima, thus requiring human interventions and long mission time.

<!-- chunk {"id": "body-0086", "role": "body", "section": "IX-B3 \\\\editEpistemic Uncertainty Results", "weight": 1.0} -->

Different from previous experiments, the goal of the OOD terrain avoidance experiment is to show the benefit of mitigating the risk due to epistemic uncertainty. Therefore, we only used the proposed planner CVaR-Dyn with $\alpha = 0.9$, but similar conclusions still hold if we change the underlying local planner to CVaR-Cost or another baseline method to mitigate the risk due to aleatoric uncertainty. We executed 3 round trips in total.

<!-- chunk {"id": "body-0087", "role": "body", "section": "IX-B3 \\\\editEpistemic Uncertainty Results", "weight": 1.0} -->

The qualitative and quantitative results for the OOD avoidance experiments are shown in Fig. and Fig.. We considered the terrain as OOD if the normalized densities for the traction predictor's latent features fell below 0 \\edit(i.e., the 0-th percentile of the densities observed for all the training data), but a more conservative threshold may be used based on empirical tuning. \\edit Compared to the training environment shown in Fig., the test environment shown in Fig. contained much taller vegetation for which we did not collect training data. As a result, the traction predictions for the tall vegetation terrain produced high epistemic uncertainty and the associated terrain was marked as OOD. Without avoiding OOD terrain, the robot was more prone to getting stuck in local minima and required human interventions to drive to the robot to areas with feasible trajectories to goal. In contrast, the planner that avoided OOD terrain achieved better time-to-goal without requiring human interventions.

<!-- chunk {"id": "body-0088", "role": "body", "section": "IX-C \\\\editTakeaways From the Hardware Experiments", "weight": 1.0} -->

In summary, the hardware experiments have demonstrated that the proposed CVaR-Dyn is an attractive choice in practice, without incurring extra computation required by CVaR-Cost that samples additional traction maps or requiring human expertise in designing semantics-based costs for potentially a large variety of terrain types. In addition, the ability to estimate epistemic uncertainty allows us to identify and avoid OOD terrain with unreliable traction predictions, thus improving navigation success rate and reducing human interventions.

<!-- chunk {"id": "body-0089", "role": "body", "section": "\\\\editLimitations & Future Work", "weight": 1.0} -->

From the modeling standpoint, this work focused on 2D robot models, but models with six degrees of freedom are needed for more challenging terrain. In addition, we used a semantic octomap to model the environment, but computationally cheaper alternatives can be used instead. Moreover, our work relies on the accuracy of the semantic segmentation module, so the proposed pipeline may fail if the test environments look too different from the training environments (e.g., due to lighting and seasonal changes). Therefore, risk due to the uncertainty in the perception modules need to be addressed separately.

<!-- chunk {"id": "body-0090", "role": "body", "section": "\\\\editLimitations & Future Work", "weight": 1.0} -->

From the data collection standpoint, this work required empirical traction distributions for training, which may be difficult to attain for high-dimensional features such as RGB images. While the proposed loss can be used to train against instantaneous traction measurements directly, the performance benefits of using EMD^2^-based loss need to be reassessed. Moreover, uncertainty-guided data collection methods ) can be used to collect informative training samples.

<!-- chunk {"id": "body-0091", "role": "body", "section": "\\\\editLimitations & Future Work", "weight": 1.0} -->

From the planning standpoint, this work proposed to simulate state trajectories using the CVaR of traction, but more investigations are needed to generalize the idea to systems with more parameters and different performance metrics. Moreover, our planner avoids OOD terrain in new environments, but online adaptation can be performed if human supervision is available. Lastly, the proposed approach can be paired with a global planner that exploits far-field knowledge.

<!-- chunk {"id": "body-0092", "role": "body", "section": "Conclusion", "weight": 1.5} -->

This work proposed EVORA, a unified framework for uncertainty-aware traversability learning based on evidential deep learning and risk-aware planning based on CVaR. EVORA models uncertain terrain traction via empirical distributions (aleatoric uncertainty) and identifies OOD terrain based on densities of traction predictor's latent features (epistemic uncertainty). By leveraging the proposed uncertainty-aware squared Earth Mover's Distance loss, we improved the network's prediction accuracy, OOD detection performance, and the downstream navigation performance. To handle aleatoric uncertainty, \\editthe proposed risk-aware planner simulates state trajectories based on the left-tail CVaR of the traction distributions. To handle epistemic uncertainty, we proposed to assign auxiliary costs to terrain whose latent features have low densities, leading to higher navigation success rates. The overall pipeline was analyzed via extensive simulations and hardware experiments, demonstrating improved navigation performance across different ground robotic platforms.
