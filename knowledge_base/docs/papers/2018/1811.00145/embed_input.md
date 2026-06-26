<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Scalable End-to-End Autonomous Vehicle Testing via Rare-event Simulation

Topics include Autonomous driving, Vehicles, Control, Learning, Sampling, Monte Carlo methods, AV, De facto.

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

While recent developments in autonomous vehicle (AV) technology highlight substantial progress, we lack tools for rigorous and scalable testing. Real-world testing, the de facto evaluation environment, places the public in danger, and, due to the rare nature of accidents, will require billions of miles in order to statistically validate performance claims. We implement a simulation framework that can test an entire modern autonomous driving system, including, in particular, systems that employ deep-learning perception and control algorithms. Using adaptive importance-sampling methods to accelerate rare-event probability evaluation, we estimate the probability of an accident under a base distribution governing standard traffic behavior. We demonstrate our framework on a highway scenario, accelerating system evaluation by 2-20 times over naive Monte Carlo sampling methods and 10-300 mathsfP times (where mathsfP is the number of processors) over real-world testing.

<!-- chunk {"id": "body-0003", "role": "body", "section": "Introduction", "weight": 1.5} -->

Recent breakthroughs in deep learning have accelerated the development of autonomous vehicles (AVs); many research prototypes now operate on real roads alongside human drivers. While advances in computer-vision techniques have made human-level performance possible on narrow perception tasks such as object recognition, several fatal accidents involving AVs underscore the importance of testing whether the perception and control pipeline---when considered as a *whole system*---can safely interact with humans. Unfortunately, testing AVs in real environments, the most straightforward validation framework for system-level input-output behavior, requires prohibitive amounts of time due to the rare nature of serious accidents. Concretely, a recent study argues that AVs need to drive "hundreds of millions of miles and, under some scenarios, hundreds of billions of miles to create enough data to clearly demonstrate their safety." Alteratively, formally verifying an AV algorithm's "correctness" is difficult since all driving policies are subject to crashes caused by other drivers. It is unreasonable to ask that the policy be safe under *all* scenarios.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

Unfortunately, ruling out scenarios where the AV should not be blamed is a task subject to logical inconsistency, combinatorial growth in specification complexity, and subjective assignment of fault.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

Motivated by the challenges underlying real-world testing and formal verification, we consider a probabilistic paradigm---which we call a *risk-based framework*---where the goal is to evaluate the *probability of an accident* under a base distribution representing standard traffic behavior. By assigning learned probability values to environmental states and agent behaviors, our risk-based framework considers performance of the AV's policy under a data-driven model of the world. To efficiently evaluate the probability of an accident, we implement a photo-realistic and physics-based simulator that provides the AV with perceptual inputs (e.g. video and range data) and traffic conditions (e.g. other cars and pedestrians). The simulator allows parallelized, faster-than-real-time evaluations in varying environments (e.g. weather, geographic locations, and aggressiveness of other cars).

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

Formally, we let $P_{0}$ denote the base distribution that models standard traffic behavior and $X \sim P_{0}$ be a realization of the simulation (e.g. weather conditions and driving policies of other agents). For an objective function $f:{\mathcal{X}\rightarrow{\mathbb{R}}}$ that measures "safety"---so that low values of $f{(x)}$ correspond to dangerous scenarios---our goal is to evaluate the probability of a dangerous event for some threshold $\gamma$. Our risk-based framework is agnostic to the complexity of the ego-policy and views it as a black-box module. Such an approach allows, in particular, deep-learning based perception systems that make formal verification methods intractable.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

An essential component of this approach is to estimate the base distribution $P_{0}$ from data; we use public traffic data collected by the US Department of Transportation. While such datasets do not offer insights into how AVs interact with human agents---this is precisely why we design our simulator---they illustrate the range of standard human driving behavior that the base distribution $P_{0}$ must model. We use imitation learning to learn a generative model for the behavior (policy) of environment vehicles; unlike traditional imitation learning, we train an ensemble of models to characterize a distribution of human-like driving policies.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Introduction", "weight": 1.5} -->

As serious accidents are rare ($p_{\gamma}$ is small), we view this as a *rare-event simulation* problem; naive Monte Carlo sampling methods require prohibitively many simulation rollouts to generate dangerous scenarios and estimate $p_{\gamma}$. To accelerate safety evaluation, we use adaptive importance-sampling methods to learn alternative distributions $P_{\theta}$ that generate accidents more frequently. Specifically, we use the cross-entropy algorithm to iteratively approximate the optimal importance sampling distribution. In contrast to simple classical settings which allow analytic updates to $P_{\theta}$, our high-dimensional search space requires solving convex optimization problems in each iteration (Section 2). To address numerical instabilities of importance sampling estimators in high dimensions, we carefully design search spaces and perform computations in logarithmic scale. Our implementation produces $2$-$20$ times as many rare events as naive Monte Carlo methods, independent of the complexity of the ego-policy.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Introduction", "weight": 1.5} -->

In addition to accelerating evaluation of $p_{\gamma}$, learning a distribution $P_{\theta}$ that *frequently* generates realistic dangerous scenarios $X_{i} \sim P_{\theta}$ is useful for engineering purposes. The importance-sampling distribution $P_{\theta}$ not only efficiently samples dangerous scenarios, but also ranks them according to their likelihoods under the base distribution $P_{0}$. This capability enables a deeper understanding of failure modes and prioritizes their importance to improving the ego-policy.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Introduction", "weight": 1.5} -->

In what follows, we describe components of our open-source toolchain, a photo-realistic simulator equipped with our data-driven risk-based framework and cross-entropy search techniques. The toolchain can test an AV as a *whole system*, simulating the driving policy of the ego-vehicle by viewing it as a black-box model. The use of adaptive-importance sampling methods motivates a unique simulator architecture (Section 3) which allows real-time updates of the policies of environment vehicles. In Section 4, we test our toolchain by considering an end-to-end deep-learning-based ego-policy in a multi-agent highway scenario. Figure 1 shows one configuration of this scenario in the real world along with rendered images from the simulator, which uses Unreal Engine 4. Our experiments show that we accelerate the assessment of rare-event probabilities with respect to naive Monte Carlo methods as well as real-world testing. We believe our open-source framework is a step towards a rigorous yet scalable platform for evaluating AV systems, with the broader goal of understanding how to reliably deploy deep-learning systems in safety-critical applications.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Rare-event simulation", "weight": 1.0} -->

To motivate our risk-based framework, we first argue that formally verifying correctness of a AV system is infeasible due to the challenge of defining "correctness." Consider a scenario where an AV commits a traffic violation to avoid collision with an out-of-control truck approaching from behind. If the ego-vehicle decides to avoid collision by running through a red light with no further ramifications, is it "correct" to do so? The "correctness" of the policy depends on the extent to which the traffic violation endangers nearby humans and whether any element of the "correctness" specification explicitly forbids such actions. That is, "correctness" as a binary output is a concept defined by its exceptions, many elements of which are subject to individual valuations.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Rare-event simulation", "weight": 1.0} -->

Instead of trying to verify correctness, we begin with a continuous measure of safety $f:{\mathcal{X}\rightarrow{\mathbb{R}}}$, where $\mathcal{X}$ is space of traffic conditions and behaviors of other vehicles. The prototypical example in this paper is the minimum time-to-collision (TTC) (see Appendix A for its definition) to other environmental agents over a simulation rollout. Rather than requiring safety for all $x \in \mathcal{X}$, we relax the deterministic verification problem into a probabilistic one where we are concerned with the probability under standard traffic conditions that $f{(X)}$ goes below a safety threshold.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Rare-event simulation", "weight": 1.0} -->

Given a distribution $P_{0}$ on $\mathcal{X}$, our goal is to estimate the rare event probability $p_{\gamma}:={P_{0}{({{f{(X)}} \leq \gamma})}}$ based on simulated rollouts ${f{(X_{1})}},\ldots,{f{(X_{n})}}$. As accidents are rare and $p_{\gamma}$ is near $0$, we treat this as a rare-event simulation problem; see \[11, 4, Chapter VI\] for an overview of this topic.

<!-- chunk {"id": "body-0014", "role": "body", "section": "Rare-event simulation", "weight": 1.0} -->

As $p_{\gamma}$ is small, we use relative accuracy to measure our performance, and the central limit theorem implies the relative accuracy is approximately For small $p_{\gamma}$, we require a sample of size $N \gtrsim {1/{({p_{\gamma}\epsilon^{2}})}}$ to achieve $\epsilon$-relative accuracy, and if $f{(X)}$ is light-tailed, the sample size must grow exponentially in $\gamma$.

<!-- chunk {"id": "body-0015", "role": "body", "section": "Cross-entropy method", "weight": 1.0} -->

The cross-entropy method iteratively tries to find $\theta^{\star} \in \operatorname{argmin}_{\theta \in \Theta}D_{kl}\left( P^{\star}||P_{\theta} \right)$, the Kullback-Leibler projection of $P^{\star}$ onto the class of parameterized distributions $\mathcal{P} = {\{ P_{\theta}\}}_{\theta \in \Theta}$.

<!-- chunk {"id": "body-0016", "role": "body", "section": "Cross-entropy method", "weight": 1.0} -->

Over iterations $k$, we maintain a surrogate distribution ${q_{k}{(x)}} \propto {\mathbf{1}\left\{ {{f{(x)}} \leq \gamma_{k}} \right\}p_{0}{(x)}}$ where $\gamma_{k} \geq \gamma$ is a (potentially random) proxy for the rare-event threshold $\gamma$, and we use samples from $P_{\theta}$ to update $\theta$ as an approximate projection of $Q$ onto $\mathcal{P}$. The motivation underlying this approach is to update $\theta$ so that $P_{\theta}$ upweights regions of $\mathcal{X}$ with low objective value (i.e. unsafe) $f{(x)}$.

<!-- chunk {"id": "body-0017", "role": "body", "section": "Cross-entropy method", "weight": 1.0} -->

We fix a quantile level $\rho \in {}$---usually we choose $\rho \in {\lbrack 0.01,0.2\rbrack}$---and use the $\rho$-quantile of $f{(X)}$ where $X \sim P_{\theta_{k}}$ as $\gamma_{k}$, our proxy for the rare event threshold $\gamma$ (see for alternatives). We have the additional challenge that the $\rho$-quantile of $f{(X)}$ is unknown, so we approximate it using i.i.d. samples $X_{i} \sim P_{\theta_{k}}$. Compared to applications of the cross-entropy method that focus on low-dimensional problems permitting analytic updates to $\theta$, our high-dimensional search space requires solving convex optimization problems in each iteration. To address numerical challenges in computing likelihood ratios in high-dimensions, our implementation carefully constrains the search space and we compute likelihoods in logarithmic scale.

<!-- chunk {"id": "body-0018", "role": "body", "section": "Cross-entropy method", "weight": 1.0} -->

We now rigorously describe the algorithmic details. First, we use natural exponential families as our class of importance samplers $\mathcal{P}$.

<!-- chunk {"id": "body-0019", "role": "body", "section": "Cross-entropy method", "weight": 1.0} -->

1:Input: Quantile ρ ∈, Stepsizes {αk}k ∈ ℕ, Sample sizes {Nk}k ∈ ℕ, Number of iterations K 4: Sample ${X_{k,1},\ldots,X_{k,N_{k}}}\overset{iid}{\sim}P_{\theta_{k}}$ 5: Set γk as the minimum of γ and the ρ-quantile of f (Xk, 1), …, f (Xk, Nk) Algorithm 1 Cross-Entropy Method

<!-- chunk {"id": "body-0020", "role": "body", "section": "Simulation framework", "weight": 1.0} -->

Two key considerations in our risk-based framework influence design choices for our simulation toolchain: learning the base distribution $P_{0}$ of nominal traffic behavior via data-driven modeling, and testing the AV as a *whole system*. We now describe how our toolchain achieves these goals.

<!-- chunk {"id": "body-0021", "role": "body", "section": "Data-driven generative modeling", "weight": 1.0} -->

While our risk-based framework (cf. Section 2) is a concise, unambiguous measure of system safety, the rare-event probability $p_{\gamma}$ is only meaningful insofar as the base distribution $P_{0}$ of road conditions and the behaviors of other (human) drivers is estimable. Thus, to implement our risk-based framework, we first learn a base distribution $P_{0}$ of nominal traffic behavior. Using the highway traffic dataset NGSim, we train policies of human drivers via imitation learning. Our data consists of videos of highway traffic, and our goal is to create models that imitate human driving behavior even in scenarios distinct from those in the data. We employ an ensemble of generative adversarial imitation learning (GAIL) models to learn $P_{0}$. Our approach is motivated by the observation that reducing an imitation-learning problem to supervised learning---where we simply use expert data to predict actions given vehicle states---suffers from poor performance in regions of the state space not encountered in data.

<!-- chunk {"id": "body-0022", "role": "body", "section": "Data-driven generative modeling", "weight": 1.0} -->

Reinforcement-learning techniques have been observed to improve generalization performance, as the imitation agent is able to explore regions of the state space in simulation during training that do not necessarily occur in the expert data traces.

<!-- chunk {"id": "body-0023", "role": "body", "section": "Data-driven generative modeling", "weight": 1.0} -->

Generically, GAIL is a minimax game between two functions: a discriminator $D_{\phi}$ and a generator $G_{\xi}$ (with parameters $\phi$ and $\xi$ respectively). The discriminator takes in a state-action pair $(s,u)$ and outputs the probability that the pair came from real data, ${\mathbb{P}}{(\text{real data})}$. The generator takes in a state $s$ and outputs a conditional distribution ${G_{\xi}{(s)}}:={{\mathbb{P}}{({u \mid s})}}$ of the action $u$ to take given state $s$. In our context, $G_{\xi}{( \cdot )}$ is then the (learned) policy of a human driver given environmental inputs $s$.

<!-- chunk {"id": "body-0024", "role": "body", "section": "Data-driven generative modeling", "weight": 1.0} -->

Training the generator weights $\xi$ occurs in a reinforcement-learning paradigm with reward $- {\log{({1 - {D_{\phi}{(s,{G_{\xi}{(s)}})}}})}}$. We use the model-based variant of GAIL (MGAIL) which renders this reward fully differentiable with respect to $\xi$ over a simulation rollout, allowing efficient model training. GAIL has been validated by Kuefler et al. to realistically mimic human-like driving behavior from the NGSim dataset across multiple metrics. These include the similarity of low-level actions (speeds, accelerations, turn-rates, jerks, and time-to-collision), as well as higher-level behaviors (lane change rate, collision rate, hard-brake rate, etc). See Appendix C for a reference to an example video of the learned model driving in a scenario alongside data traces from human drivers.

<!-- chunk {"id": "body-0025", "role": "body", "section": "Data-driven generative modeling", "weight": 1.0} -->

Our importance sampling and cross-entropy methods use not just a single instance of model parameters $\xi$, but rather a distribution over them to form a generative model of human driving behavior. To model this distribution, we use a (multivariate normal) parametric bootstrap over a trained ensemble of generators ${{\xi^{i},i} = 1},{\ldots,m}$. Our models $\xi^{i}$ are high-dimensional (${\xi \in {\mathbb{R}}^{d}},{d > m}$) as they characterize the weights of large neural networks, so we employ the graphical lasso to fit the inverse covariance matrix for our ensemble. This approach to modeling uncertainty in neural-network weights is similar to the bootstrap approach of Osband et al.. Other approaches include using dropout for inference and variational methods.

<!-- chunk {"id": "body-0026", "role": "body", "section": "Data-driven generative modeling", "weight": 1.0} -->

While several open source driving simulators have been proposed, our problem formulation requires unique features to allow sampling from a continuous distribution of driving policies for environmental agents. Conditional on each sample of model parameters $\xi$, the simulator constructs a (random) rollout of vehicle behaviors according to $G_{\xi}$. Unlike other existing simulators, ours is designed to efficiently execute and update these policies as new samples $\xi$ are drawn for each rollout.

<!-- chunk {"id": "body-0027", "role": "body", "section": "System architecture", "weight": 1.0} -->

The second key characteristic of our framework is that it enables black-box testing the AV as a whole system. Flaws in complex systems routinely occur at poorly specified interfaces between components, as interactions between processes can induce unexpected behavior. Consequently, solely testing subcomponents of an AV control pipeline separately is insufficient. Moreover, it is increasingly common for manufacturers to utilize software and hardware artifacts for which they do not have any whitebox model. We provide a concise but extensible language-agnostic interface to our benchmark world model so that common AV sensors such as cameras and lidar can provide the necessary inputs to induce vehicle actuation commands.

<!-- chunk {"id": "body-0028", "role": "body", "section": "System architecture", "weight": 1.0} -->

Our simulator is a distributed, modular framework, which is necessary to support the inclusion of new AV systems and updates to the environment-vehicle policies. A benefit of this design is that simulation rollouts are simple to parallelize. In particular, we allow instantiation of multiple simulations simultaneously, without requiring that each include the entire set of components. For example, a desktop may support only one instance of Unreal Engine but could be capable of simulating 10 physics simulations in parallel; it would be impossible to fully utilize the compute resource with a monolithic executable wrapping all engines together. Our architecture enables instances of the components to be distributed on heterogeneous GPU compute clusters while maintaining the ability to perform meaningful analysis locally on commodity desktops. In Appendix A, we detail our scenario specification, which describes how Algorithm 1 maps onto our distributed architecture.

<!-- chunk {"id": "body-0029", "role": "body", "section": "Experiments", "weight": 1.0} -->

In this section, we demonstrate our risk-based framework on a multi-agent highway scenario. As the rare-event probability of interest $p_{\gamma}$ gets smaller, the cross-entropy method learns to sample more rare events compared to naive Monte Carlo sampling; we empirically observe that the cross-entropy method produces $2$-$20$ times as many rare events as its naive counterpart. Our findings hold across different ego-vehicle policies, base distributions $P_{0}$, and scenarios.

<!-- chunk {"id": "body-0030", "role": "body", "section": "Experiments", "weight": 1.0} -->

To highlight the modularity of our simulator, we evaluate the rare-event probability $p_{\gamma}$ on two different ego-vehicle policies. The first is an instantiation of an imitation learning (non-vision) policy which uses lidar as its primary perceptual input. Secondly, we investigate a vision-based controller (vision policy), where the ego-vehicle drives with an end-to-end highway autopilot network, taking as input a rendered image from the simulator (and lidar observations) and outputting actuation commands. See Appendix B for a summary of network architectures used.

<!-- chunk {"id": "body-0031", "role": "body", "section": "Experiments", "weight": 1.0} -->

We consider a scenario consisting of six agents, five of which are considered part of the environment. The environment vehicles' policies follow the distribution learned in Section 3.1. All vehicles are constrained to start within a set of possible initial configurations consisting of pose and velocity, and each vehicle has a goal of reaching the end of the approximately 2 km stretch of road. Fig. 1 shows one such configuration of the scenario, along with rendered images from the simulator. We create scene geometry based on surveyors' records and photogrammetric reconstructions of satellite imagery of the portion of I-80 in Emeryville, California where the traffic data was collected.

<!-- chunk {"id": "body-0032", "role": "body", "section": "Simulation parameters", "weight": 1.0} -->

We detail our postulated base distribution $P_{0}$. Letting $m$ denote the number of vehicles, we consider the random tuple $X = {(S,T,W,V,\xi)}$ as our simulation parameter where the pair ${(S,T)} \in {\mathbb{R}}_{+}^{m \times 2}$ indicates the two-dimensional positioning of each vehicle in their respective lanes (in meters), $W$ the orientation of each vehicle (in degrees), and $V$ the initial velocity of each vehicle (in meters per second). We use $\xi \in {\mathbb{R}}^{404}$ to denote the weights of the last layer of the neural network trained to imitate human-like driving behavior.

<!-- chunk {"id": "body-0033", "role": "body", "section": "Simulation parameters", "weight": 1.0} -->

Specifically, we set $S \sim {{40\text{Beta}{}} + 80}$ with respect to the starting point of the road, $T \sim {{0.5\text{Beta}{}} - 0.25}$ with respect to the lane's center, $W \sim {{7.2\text{Beta}{}} - 3.6}$ with respect to facing forward, and $V \sim {{10\text{Beta}{}} + 10}$. We assume $\xi \sim {\mathcal{N}{(\mu_{0},\Sigma_{0})}}$, with the mean and covariance matrices learned via the ensemble approach outlined in Section 3.1. The neural network whose last layer is parameterized by $\xi$ describes the policy of environment vehicles; it takes as input the state of the vehicle and lidar observations of the surrounding environment (see Appendix B for more details).

<!-- chunk {"id": "body-0034", "role": "body", "section": "Simulation parameters", "weight": 1.0} -->

Throughout this section, we define our measure of safety $f:{\mathcal{X}\rightarrow{\mathbb{R}}}$ as the minimum time-to-collision (TTC) over the simulation rollout. We calculate TTC from the center of mass of the ego vehicle; if the ego-vehicle's body crashes into obstacles, we end the simulation before the TTC can further decrease (see Appendix A for details).

<!-- chunk {"id": "body-0035", "role": "body", "section": "Simulation parameters", "weight": 1.0} -->

(a) Ratio of number of rare events vs. threshold (b) Ratio of variance vs. threshold Figure 2: The ratio of (a) number of rare events and (b) variance of estimator for pγ between cross-entropy method and naive MC sampling for the non-vision ego policy. Rarity is inversely proportional to γ, and, as expected, we see the best performance for our method over naive MC at small γ.

<!-- chunk {"id": "body-0036", "role": "body", "section": "Cross-entropy method", "weight": 1.0} -->

Throughout our experiments, we impose constraints on the space of importance samplers (adversarial distributions) for feasibility. Numerical stability considerations predominantly drive our hyperparameter choices. For model parameters $\xi$, we also constrain the search space to ensure that generative models $G_{\xi}$ maintain reasonably realistic human-like policies (recall Sec. 3.1). For $S,T,W$, and $V$, we let $\{{\text{Beta}{(\alpha,\beta)}}:{{\alpha,\beta} \in {\lbrack 1.5,7\rbrack}}\}$ be the model space over which the cross-entropy method searches, scaled and centered appropriately to match the scale of the respective base distributions.

<!-- chunk {"id": "body-0037", "role": "body", "section": "Cross-entropy method", "weight": 1.0} -->

We restrict the search space of distributions over $\xi \in {\mathbb{R}}^{404}$ by searching over $\{{\mathcal{N}{(\mu,\Sigma_{0})}}:{\left\| {\mu - \mu_{0}} \right\|_{\infty} \leq.01}\}$, where $(\mu_{0},\Sigma_{0})$ are the parameters of the base (bootstrap) distribution. For our importance sampling distribution $P_{\theta}$, we use products of the above marginal distributions. These restrictions on the search space mitigate numerical instabilities in computing likelihood ratios within our optimization routines, which is important for our high-dimensional problems.

<!-- chunk {"id": "body-0038", "role": "body", "section": "Cross-entropy method", "weight": 1.0} -->

We first illustrate the dependence of the cross-entropy method on its hyperparameters. We choose to use a non-vision ego-vehicle policy as a test bed for hyperparameter tuning, since this allows us to take advantage of the fastest simulation speeds for our experiments. We focus on the effects (in Algorithm 1) of varying the most influential hyperparameter, $\rho \in {(0,1\rbrack}$, which is the quantile level determining the rarity of the observations used to compute the importance sampler $\theta_{k}$. Intuitively, as $\rho$ approaches 0, the cross-entropy method learns importance samplers $P_{\theta}$ that up-weight unsafe regions of $\mathcal{X}$ with lower $f{(x)}$, increasing the frequency of sampling rare events (events with ${f{(X)}} \leq \gamma$). In order to avoid overfitting $\theta_{k}$ as $\rho\rightarrow 0$, we need to increase $N_{k}$ as $\rho$ decreases.

<!-- chunk {"id": "body-0039", "role": "body", "section": "Cross-entropy method", "weight": 1.0} -->

Our choice of $N_{k}$ is borne out of computational constraints as it is the biggest factor that determines the run-time of the cross-entropy method. Consistent with prior works, we observe empirically that $\rho \in {\lbrack 0.01,0.2\rbrack}$ is a good range for the values of $N_{k}$ deemed feasible for our computational budget ($N_{k} = 1000 \sim 5000$). We fix the number of iterations at $K = 100$, number of samples taken per iteration at $N_{k} = 5000$, step size for updates at $\alpha_{k} = 0.8$, and $\gamma = 0.14$. As we see below, we consistently observe that the cross-entropy method learns to sample significantly more rare events, despite the high-dimensional nature $({d \approx 500})$ of the problem.

<!-- chunk {"id": "body-0040", "role": "body", "section": "Cross-entropy method", "weight": 1.0} -->

To evaluate the learned parameters, we draw $n = 10^{5}$ samples from the importance sampling distribution to form an estimate of $p_{\gamma}$. In Figure 2, we vary $\rho$ and report the relative performance of the cross-entropy method compared to naive Monte Carlo sampling. Even though we set $\gamma = 0.14$ in Algorithm 1, we evaluate the performance of all models with respect to multiple threshold levels $\gamma_{test}$. We note that as $\rho$ approaches $0$, the cross-entropy method learns to frequently sample increasingly rare events; the cross-entropy method yields $3$-$10$ times as many dangerous scenarios, and achieves $2$-$16$ times variance reduction depending on the threshold level $\gamma_{test}$. In Table 1, we contrast the estimates provided by naive Monte Carlo and the importance sampling estimator provided by the cross-entropy method with $\rho = 0.01$; to form a baseline estimate, we run naive Monte Carlo with $1.3 \cdot 10^{6}$ samples.

<!-- chunk {"id": "body-0041", "role": "body", "section": "Cross-entropy method", "weight": 1.0} -->

For a given number of samples, the cross-entropy method with $\rho = 0.01$ provides more precise estimates for the rare-event probability $p_{\gamma} \approx 10^{- 5}$ over naive Monte Carlo.

<!-- chunk {"id": "body-0042", "role": "body", "section": "Cross-entropy method", "weight": 1.0} -->

We now leverage the tuned hyperparameter ($\rho = 0.01$) for our main experiment: evaluating the probability of a dangerous event for the vision-based ego policy. We find that the hyperparameters for the cross-entropy method generalize, allowing us to produce good importance samplers for a very different policy without further tuning. Based on our computational budget (with our current implementation, vision-based simulations run about 15 times slower than simulations with only non-vision policies), we choose $K = 20$ and $N_{k} = 1000$ for the cross-entropy method to learn a good importance sampling distribution for the vision-based policy (although we also observe similar behavior for $N_{k}$ as small as $100$). In Figure 3, we illustrate again that the cross-entropy method learns to sample dangerous scenarios more frequently (Figure 3a)---up to $18$ times that of naive Monte Carlo---and produces importance sampling estimators with lower variance (Figure 3b). As a result, our estimator in Table 2 is better calibrated compared to that computed from naive Monte Carlo.

<!-- chunk {"id": "body-0043", "role": "body", "section": "Qualitative analysis", "weight": 1.0} -->

We provide a qualitative interpretation for the learned parameters of the importance sampler. For initial velocities, angles, and positioning of vehicles, the importance sampler shifts environmental vehicles to box in the ego-vehicle and increases the speeds of trailing vehicles by $20\%$, making accidents more frequent. We also observe that the learned distribution for initial conditions have variance $50\%$ smaller than that of the base distribution, implying concentration around adversarial conditions. Perturbing the policy weights $\xi$ for GAIL increases the frequency of risky high-level behaviors (lane-change rate, hard-brake rate, etc.). An interesting consequence of using our definition of TTC from the center of the ego vehicle (cf. Appendix A) as a measure of safety is that dangerous events ${f{(X)}} \leq \gamma_{test}$ (for small $\gamma_{test}$) include frequent sideswiping behavior, as such accidents result in smaller TTC values than front- or rear-end collisions. See Appendix C for a reference to supplementary videos that exhibit the range of behavior across many levels $\gamma_{test}$.

<!-- chunk {"id": "body-0044", "role": "body", "section": "Qualitative analysis", "weight": 1.0} -->

The modularity of our simulation framework easily allows us to modify the safety objective to an alternative definition of TTC or even include more sophisticated notions of safety, e.g. temporal-logic specifications or implementations of responsibility-sensitive safety (RSS).

<!-- chunk {"id": "body-0045", "role": "body", "section": "Qualitative analysis", "weight": 1.0} -->

(a) Ratio of number of rare events vs. threshold (b) Ratio of variance vs. threshold Figure 3: The ratio of (a) number of rare events and (b) variance of estimator for pγ between cross-entropy method and naive MC sampling for the vision-based ego policy.
