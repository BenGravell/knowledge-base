<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

BC-MPPI: A Probabilistic Constraint Layer for Safe Model-Predictive Path-Integral Control

Topics include Model predictive path integral control, Trajectory optimization, Safety, Bayesian constraints, Probabilistic constraints.

<!-- chunk {"id": "summary-0002", "role": "summary", "section": "Summary", "weight": 2.0} -->

Adds a Bayesian probabilistic layer to MPPI that models constraint satisfaction as a probability distribution, enabling principled soft constraint handling within the MPPI sampling framework.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Model Predictive Path Integral (MPPI) control has recently emerged as a fast, gradient-free alternative to model-predictive control in highly non-linear robotic tasks, yet it offers no hard guarantees on constraint satisfaction. We introduce Bayesian-Constraints MPPI (BC-MPPI), a lightweight safety layer that attaches a probabilistic surrogate to every state and input constraint. At each re-planning step the surrogate returns the probability that a candidate trajectory is feasible; this joint probability scales the weight given to a candidate, automatically down-weighting rollouts likely to collide or exceed limits and pushing the sampling distribution toward the safe subset; no hand-tuned penalty costs or explicit sample rejection required. We train the surrogate from 1,000 offline simulations and deploy the controller on a quadrotor in MuJoCo with both static and moving obstacles. Across K in rollouts BC-MPPI preserves safety margins while satisfying the prescribed probability of violation. Because the surrogate is a stand-alone, version-controlled artefact and the runtime safety score is a single scalar, the approach integrates naturally with verification-and-validation pipelines for certifiable autonomous systems.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

Model Predictive Control (MPC) was first developed in the process-control community and has since become a workhorse in robotics, underpinning behaviors as diverse as mobile-robot navigation, manipulation, legged locomotion, and aerial acrobatics. Its appeal lies in the explicit use of a predictive model to optimize a finite-horizon cost while respecting user-defined constraints at every step. Yet this very strength is also a weakness: effective deployment still depends on hand-crafting analytic cost terms and constraint sets that are differentiable, well-conditioned, and sufficiently rich to capture task objectives and safety limits. For highly nonlinear, contact-rich, or perception-driven tasks---where objectives may be implicit in sensor data or learned from experience---defining such functions becomes a substantial engineering burden and can limit MPC's practicality in advanced robotic applications.\

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

Stochastic sampling--based Model Predictive Path Integral (MPPI) control offers a compelling alternative. MPPI sidesteps gradient evaluations by estimating the path integral of cost along thousands of Monte-Carlo rollouts, allowing it to tackle highly nonlinear, non-convex dynamics and non-differentiable objectives. It has delivered state-of-the-art performance in aggressive autonomous driving, agile quadrotor flight, and contact-rich quadruped locomotion. The adoption of GPU-accelerated sampling and differentiable programming frameworks now enables sub-millisecond evaluation of tens of thousands of trajectories, bringing MPPI firmly into the real-time regime. At the same time, techniques such as low pass filtering and learned importance sample priors mitigate the characteristic action noise of MPPI, reducing oscillations and improving closed-loop stability.\

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

However, where MPC excels in hard constraint satisfaction MPPI struggles. Its Monte-Carlo nature makes it difficult to guarantee that every sampled trajectory respects state and input limits, and naive penalty costs often lead to brittle tuning and constraint-violation outliers. Embedding a principled constraint-handling layer within MPPI, therefore, remains an open challenge, especially for safety-critical robotic applications that must certify collision-avoidance, torque limits, or contact-stability conditions in real time.\

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

In this work we close that gap with Bayesian Constraints MPPI (BC-MPPI), a safety layer that learns a probabilistic description of task constraints and folds it directly into the MPPI sampling process. We represent each hard constraint with a Bayesian surrogate - a Bayesian neural network (BNN) - which returns both a mean estimate of constraint satisfaction and an epistemic uncertainty measure. At every control step, these surrogates reshape the MPPI proposal distribution: trajectories that venture into regions with high violation probability or high model uncertainty are exponentially down-weighted. At the same time, those that remain in the safe set are sampled more densely. We validate BC-MPPI in a high-fidelity quadrotor simulator, where the drone must fly point-to-point while respecting static obstacles (fixed walls, ceiling, and floor) and dynamic constraints (moving no-fly zones and time-varying thrust limits). The experiments show that the learned Bayesian constraint layer steers the sampling toward safe rollouts, keeping the violation probability below 1 without sacrificing trajectory optimality.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Related Works", "weight": 1.0} -->

Early efforts to inject constraints into stochastic optimal control pre-date MPPI itself. Cross-Entropy Motion Planning (CEM) biases a Gaussian distribution over control sequences via the cross-entropy method so that almost all sampled rollouts satisfy kinodynamic and obstacle constraints, enabling agile ground-vehicle and quadrotor manoeuvres without requiring gradients. In model-based reinforcement learning, Robust CEM Planning couples an ensemble dynamics model with a violation-budgeted CEM optimiser; uncertainty and sparse hazard rewards are folded into the cost, dramatically reducing failure counts on Safety-Gym tasks while maintaining sample efficiency.\

<!-- chunk {"id": "body-0009", "role": "body", "section": "Related Works", "weight": 1.0} -->

Within MPPI, the simplest strategy is to encode safety softly into the objective. Risk-Aware MPPI (RA-MPPI) replaces the expected cost with Conditional Value-at-Risk, steering optimisation toward the worst-case tail of the rollout distribution; on autonomous-racing benchmarks, it achieves baseline lap times with an order-of-magnitude fewer crashes. Because constraints appear only as penalties, however, violations remain possible whenever no high-quality feasible sample is drawn.\

<!-- chunk {"id": "body-0010", "role": "body", "section": "Related Works", "weight": 1.0} -->

A contrasting line of work enforces hard constraints through projection or real-time filtering. Constrained Stochastic Optimal Control projects every Monte-Carlo rollout onto equality manifolds and surrounds inequalities with differentiable barrier functions, guaranteeing feasibility on manipulators and legged robots while preserving MPPI's gradient-free character. Shield-MPPI passes each MPPI command through a discrete-time control-barrier-function (CBF) quadratic programme, giving zero off-track events in aggressive racing on CPU-only hardware. Extending this idea to hybrid dynamics, Risk-Aware MPPI for Stochastic Hybrid Systems encodes timed reach-avoid objectives in the cost while a companion CBF filter ensures collision-free motion around moving obstacles with formal guarantees. Projection and filtering, however, can over-constrain the optimiser and sacrifice solution optimality.\

<!-- chunk {"id": "body-0011", "role": "body", "section": "Related Works", "weight": 1.0} -->

The closest work to ours shapes the sampling distribution itself so that feasible, low-risk rollouts are drawn more often. Robust MPPI perturbs a nominal tube of trajectories and minimises a free-energy bound to keep an AutoRally car strictly within track limits despite disturbances. Dynamic Risk-Aware MPPI computes joint collision probabilities for hundreds of rollouts against moving humans and rejects samples above a risk threshold, enabling smooth crowd navigation without freezing. Constrained Covariance-Steering MPPI augments the sampler with a low-level covariance-steering controller that shapes the state-distribution tube so the robot respects obstacle chance constraints with high probability. Our Bayesian-Constraints MPPI follows this distribution-shaping philosophy but, unlike, needs no sample-rejection step---the probabilistic constraint model directly modulates the sampling law, allowing us to bound violation probability analytically.\

<!-- chunk {"id": "body-0012", "role": "body", "section": "The Bayesian Constraints MPPI", "weight": 1.0} -->

We now detail how a probabilistic safety layer can be fused with Model-Predictive Path-Integral control. The presentation proceeds top-down: Secs. 3.1--3.2 recap the standard MPPI sampler, describe the Bayesian surrogate constraints, and show how the joint feasibility probability reshapes the sampling weights. A high-level block diagram of the full pipeline is given in Fig. 1

<!-- chunk {"id": "body-0013", "role": "body", "section": "Sampling and weighting", "weight": 1.0} -->

We draw $K$ perturbations ${\Delta\theta^{k}} \sim {\mathcal{N}{(0,\mathbf{\Sigma})}}$ about the previous mean $\overline{\theta}$, roll out the dynamics, and evaluate

<!-- chunk {"id": "body-0014", "role": "body", "section": "Sampling and weighting", "weight": 1.0} -->

Each perturbation is weighted by an exponentiated cost

<!-- chunk {"id": "body-0015", "role": "body", "section": "Sampling and weighting", "weight": 1.0} -->

with temperature $\lambda$ trading off exploration and exploitation.

<!-- chunk {"id": "body-0016", "role": "body", "section": "Execution", "weight": 1.0} -->

The first control in the optimised sequence is issued as

<!-- chunk {"id": "body-0017", "role": "body", "section": "Execution", "weight": 1.0} -->

and held constant until the next replanning instant. Because rollouts are embarrassingly parallel, modern MPPI implementations evaluate thousands of trajectories on a GPU in sub-millisecond time, enabling real-time control of agile UAVs and legged robots.

<!-- chunk {"id": "body-0018", "role": "body", "section": "Probabilistic Constraint Satisfaction in BC-MPPI", "weight": 1.0} -->

In this subsection, we introduce the core mechanism that enforces constraint satisfaction in *Bayesian Constraints MPPI* (BC-MPPI). The idea is directly inspired by the feasibility--weighted acquisition rules of *Constrained Bayesian Optimisation* (CBO): we reshape the sampling distribution so that samples likely to violate any constraint receive exponentially smaller weight.\

<!-- chunk {"id": "body-0019", "role": "body", "section": "Probabilistic Constraint Satisfaction in BC-MPPI", "weight": 1.0} -->

Equation mirrors CBO's strategy of multiplying an acquisition function by a joint feasibility probability.\

<!-- chunk {"id": "body-0020", "role": "body", "section": "Probabilistic Constraint Satisfaction in BC-MPPI", "weight": 1.0} -->

Classic MPPI can be viewed as an importance--sampling estimator of the optimal control distribution. At each iteration we draw i.i.d. perturbations ${\Delta{\mathbf{θ}}^{k}} \sim {\mathcal{N}{(\mathbf{0},\mathbf{\Sigma})}}$ around the current mean $\overline{\theta}$ and assign the importance weight

<!-- chunk {"id": "body-0021", "role": "body", "section": "Probabilistic Constraint Satisfaction in BC-MPPI", "weight": 1.0} -->

BC-MPPI retains the same Gaussian sampling distribution but augments the target density with the joint feasibility probability,

<!-- chunk {"id": "body-0022", "role": "body", "section": "Probabilistic Constraint Satisfaction in BC-MPPI", "weight": 1.0} -->

Because the sampling distribution is unchanged, the importance ratio acquires a single extra factor, yielding the new weight

<!-- chunk {"id": "body-0023", "role": "body", "section": "Probabilistic Constraint Satisfaction in BC-MPPI", "weight": 1.0} -->

If the surrogate models predict that a sample ${\mathbf{θ}}^{k}$ will satisfy *all* constraints with high probability, every factor $\Pr{\lbrack{{c_{j}{({\mathbf{θ}}^{k})}} \leq 0}\rbrack}$ is close to $1$; the weight ${\overset{\sim}{\mu}}^{k}$ therefore coincides with the classic MPPI weight $\mu^{k}$ and the sample contributes normally to the control update. Conversely, if any constraint is likely to be violated, at least one factor becomes vanishingly small, driving ${\overset{\sim}{\mu}}^{k}$ towards zero. The sample is not discarded outright---it remains in the Monte-Carlo pool---but its influence on the weighted average, and hence on the control law, is effectively null.

<!-- chunk {"id": "body-0024", "role": "body", "section": "Probabilistic Constraint Satisfaction in BC-MPPI", "weight": 1.0} -->

In this way BC-MPPI enforces constraints *without* an explicit rejection step such as the one used in Dynamic Risk-Aware MPPI, while preserving the unbiased, gradient-free character of the original algorithm.

<!-- chunk {"id": "body-0025", "role": "body", "section": "Simulation Experiments", "weight": 1.0} -->

Classic MPPI, as described previously, applies an importance weighting to samples of the form in equation, where samples with a higher cost are effectively rejected. Similarly, BC-MPPI -- as described in equation -- applies an additional weighting layer to the samples based on their probability of constraint violation as predicted by the model, in our case a Bayesian Neural Network (BNN). To establish a baseline between these weighting methods, we also introduced a simplified version of MPPI -- 'MPPI-penalty', where constraint violations are handled only by applying a penalty term in the objective function, and there is no explicit rejection rule. Constraint violations are therefore accounted for by evaluating the following expression,

<!-- chunk {"id": "body-0026", "role": "body", "section": "Simulation Experiments", "weight": 1.0} -->

where a constraint violation term D is added to the cost based on the average L1 distance between the current position of the quadrotor and the obstacles, as described below.

<!-- chunk {"id": "body-0027", "role": "body", "section": "Simulation Experiments", "weight": 1.0} -->

We evaluated BC-MPPI in the MuJoCo physics engine on a quadrotor tasked with point-to-point flight in the presence of obstacles. Our method was evaluated against the two baselines: MPPI-penalty and Classic MPPI.\

<!-- chunk {"id": "body-0028", "role": "body", "section": "Simulation Experiments", "weight": 1.0} -->

A wide range of scenarios was considered, including both stationary and moving obstacles. To systematically increase task complexity, the number of obstacles was increased, ranging from 3 to 15, and in the most demanding settings, both the obstacle trajectories and the target position were randomized at each iteration. These variations were designed to probe not only average-case performance but also the breakdown points of the respective methods.\

<!-- chunk {"id": "body-0029", "role": "body", "section": "Simulation Experiments", "weight": 1.0} -->

For each scenario, we collected metrics characterizing both computational performance and trajectory quality. The performance metrics were simulation runtime - the duration of the simulation with each method -- and the control frequency during the simulation. The metrics for trajectory quality were as follows: average distance of the quadrotor from the obstacles, total distance of the quadrotor from the target, and the number of collisions with obstacles that occurred. Additionally, for the rejection-based methods, we recorded the rejection rate, defined as the percentage of sampled rollouts that were discarded before evaluation.\

<!-- chunk {"id": "body-0030", "role": "body", "section": "Simulation Experiments", "weight": 1.0} -->

Our final implementation of BC-MPPI employed a BNN surrogate. The BNN was trained on a dataset of 1000 simulated rollouts, where each sample included the initial system state (13 dimensions), the sequence of control inputs over a 25-step horizon (100 dimensions), and the corresponding constraint-violation term. The latter was computed as the average of the penalty terms across the horizon, giving a total input dimensionality of 113 and a single scalar output. To ensure data richness, rollouts were generated under three obstacle trajectory functions---circular, diagonal, and sinusoidal---combined in a 2:2:1 ratio. The dataset was shuffled, stored offline, and subsequently split into training and test sets in a 7:3 ratio. All features were standardized to mitigate scale bias and improve surrogate training.\

<!-- chunk {"id": "body-0031", "role": "body", "section": "Simulation Experiments", "weight": 1.0} -->

On a held-out test set, the model achieved a mean squared error of 1.07 and an $R^{2}$ score of 0.08. Although the predictive accuracy could've been improved, the model proved sufficient for probabilistic weighting of rollouts in the closed-loop controller.\

<!-- chunk {"id": "body-0032", "role": "body", "section": "BC-MPPI vs MPPI-penalty", "weight": 1.0} -->

Across all tested scenarios, MPPI-penalty failed to reach the target. This was consistent irrespective of the number or motion of obstacles. Consequently, the resulting trajectories exhibited both large average distances from the target and reduced distances from obstacles, as shown in Figure 3. The high obstacle proximity was particularly pronounced as the number of obstacles increased, leading to a significant rise in collisions. These observations reinforce that penalty-based shaping of the cost function is insufficient for enforcing safety in practice, as the optimizer continues to sample unsafe rollouts that are not filtered or strongly down-weighted.\

<!-- chunk {"id": "body-0033", "role": "body", "section": "BC-MPPI vs MPPI-penalty", "weight": 1.0} -->

From a computational perspective, MPPI-penalty achieved shorter simulation runtimes and higher control frequencies than BC-MPPI, especially in stationary-obstacle settings. However, the resulting large distances from obstacles and the target show that this computational efficiency came at the cost of safety: while control frequency was higher, the number of collisions grew rapidly as task complexity increased. This underscores the need for explicit rejection or probabilistic safety evaluation, since raw penalty terms proved unable to prevent unsafe rollouts from dominating the sampling distribution.

<!-- chunk {"id": "body-0034", "role": "body", "section": "BC-MPPI vs Classic MPPI", "weight": 1.0} -->

When compared against Classic MPPI, BC-MPPI achieved clearer safety margins in the stationary-obstacle settings. As shown in Figure 3, the average distance from obstacles was consistently larger under BC-MPPI for low-to-moderate numbers of obstacles, confirming the surrogate's ability to bias the sampling distribution toward safer rollouts. In more complex scenarios (moving obstacles with circular, diagonal and sinusoidal trajectories), this margin narrowed, with both methods yielding similar average obstacle clearances.\

<!-- chunk {"id": "body-0035", "role": "body", "section": "BC-MPPI vs Classic MPPI", "weight": 1.0} -->

Interestingly, despite comparable distance from obstacles in complex cases, BC-MPPI consistently tracked the target more closely (Fig. 4). While the absolute difference in average distance to the target was small (on the order of centimeters), the effect was consistent across trials. In safety-critical applications, where repeated small deviations can accumulate into large errors over time, such improvements remain practically significant.\

<!-- chunk {"id": "body-0036", "role": "body", "section": "BC-MPPI vs Classic MPPI", "weight": 1.0} -->

Most importantly, in the most complex scenarios, BC-MPPI produced fewer collisions than Classic MPPI while also maintaining a lower rejection rate overall (Fig. 6). This indicates that BC-MPPI uses samples more efficiently: unsafe rollouts are not discarded outright, but are probabilistically down-weighted, preserving useful gradient-free exploration while still improving safety.\

<!-- chunk {"id": "body-0037", "role": "body", "section": "BC-MPPI vs Classic MPPI", "weight": 1.0} -->

Finally, Classic MPPI demonstrated higher control frequencies across nearly all scenarios, making it more responsive to dynamic changes in obstacle trajectories. This responsiveness, however, comes at the expense of a higher rejection rate and greater variability in trajectory quality, whereas BC-MPPI traded computational efficiency for more consistent safety and goal-tracking.\

<!-- chunk {"id": "body-0038", "role": "body", "section": "Discussion", "weight": 1.5} -->

The Bayesian--Constraints layer converts MPPI---an inherently stochastic, gradient--free controller---into a closed--loop scheme with an explicit, probabilistic notion of safety. Two properties make the approach amenable to Verification and Validation (V&V). *First*, the BNN surrogate is learned offline from a finite, version--controlled dataset; its predictive mean and variance form a static artefact that can be unit--tested, regression--tested as new data arrive, or subjected to formal probabilistic checks (e.g., proving that the posterior variance never exceeds a threshold over the reachable state space). *Second*, at runtime every trajectory receives a single scalar weight

<!-- chunk {"id": "body-0039", "role": "body", "section": "Discussion", "weight": 1.5} -->

which monotonically reflects constraint satisfaction. This scalar is easily monitored by a lightweight runtime guard: if $w{(\theta)}$ falls below a certified bound, control can be handed over to a simpler, formally verified safe mode.\

<!-- chunk {"id": "body-0040", "role": "body", "section": "Discussion", "weight": 1.5} -->

The experimental results further highlight how this architecture balances computational cost with safety guarantees. Compared to MPPI--penalty, BC--MPPI was the only method that successfully reached the target across all scenarios, whereas penalty--based control failed even in simple cases, confirming that penalty shaping alone is inadequate for enforcing hard safety requirements. Against classic MPPI, BC--MPPI achieved comparable or better obstacle clearance and consistently maintained closer target tracking, while also reducing collisions in the most complex environments. Importantly, these improvements were obtained with a lower rejection rate, showing that probabilistic weighting can use samples more efficiently than hard rejection.\

<!-- chunk {"id": "body-0041", "role": "body", "section": "Discussion", "weight": 1.5} -->

A key trade--off is computational: BC--MPPI incurred longer simulation runtimes and lower control frequencies due to surrogate evaluation and weighting. Although the baselines were more responsive, their higher collision rates and reduced reliability illustrate that raw frequency is not synonymous with safety. For safety--critical applications, the modest loss in control rate is offset by a measurable reduction in constraint violations and the ability to certify probabilistic guarantees.\

<!-- chunk {"id": "body-0042", "role": "body", "section": "Discussion", "weight": 1.5} -->

The architecture therefore yields a clean separation of concerns: low--level dynamics remain in fast, handwritten code; the surrogate and weighting rule reside in a self--contained module that can be verified with traditional software--engineering practices (code review, static analysis, continuous integration); and high--level mission logic can rely on the weight as a measurable contract, simplifying compositional reasoning about the overall system.\

<!-- chunk {"id": "body-0043", "role": "body", "section": "Limitations and Future Work", "weight": 1.5} -->

While the present results demonstrate the feasibility of BC-MPPI, several limitations remain. First, the surrogate accuracy was modest $R^{2} \approx 0.08$, yet still sufficient for weighting; more expressive models or larger datasets may improve predictive fidelity without compromising runtime. Second, the experiments focused on a quadrotor in obstacle-avoidance tasks; scaling to higher-dimensional robots or more diverse environments may reveal new challenges in training efficiency and model generalization. Finally, although the additional runtime cost was acceptable in our setting, deploying BC-MPPI on embedded hardware will require further optimization of surrogate inference and sampling. Addressing these limitations---through model compression, online updating of the surrogate, or integration with other safety-filtering methods---offers a promising direction for future work.

<!-- chunk {"id": "body-0044", "role": "body", "section": "Conclusion", "weight": 1.5} -->

We have shown that embedding a probabilistic constraint layer into MPPI yields a controller that is both agile and safety-aware, outperforming a classic penalty-based baseline in static and dynamic obstacle fields. Future work will develop automatic coverage metrics for the offline data set, perform formal co-analysis of the surrogate model with temporal-logic mission specifications, and design incremental re-training pipelines that preserve previously proven safety margins while adapting to changing environments.
