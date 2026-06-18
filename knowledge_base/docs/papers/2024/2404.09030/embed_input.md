<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Active Learning for Control-Oriented Identification of Nonlinear Systems

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Model-based reinforcement learning is an effective approach for controlling an unknown system. It is based on a longstanding pipeline familiar to the control community in which one performs experiments on the environment to collect a dataset, uses the resulting dataset to identify a model of the system, and finally performs control synthesis using the identified model. As interacting with the system may be costly and time consuming, targeted exploration is crucial for developing an effective control-oriented model with minimal experimentation. Motivated by this challenge, recent work has begun to study finite sample data requirements and sample efficient algorithms for the problem of optimal exploration in model-based reinforcement learning. However, existing theory and algorithms are limited to model classes which are linear in the parameters. Our work instead focuses on models with nonlinear parameter dependencies, and presents the first finite sample analysis of an active learning algorithm suitable for a general class of nonlinear dynamics. In certain settings, the excess control cost of our algorithm achieves the optimal rate, up to logarithmic factors. We validate our approach in simulation, showcasing the advantage of active, control-oriented exploration for controlling nonlinear systems.

<!-- chunk {"id": "body-0003", "role": "body", "section": "Introduction", "weight": 1.5} -->

In recent years, model-based reinforcement learning has been successfully applied to various application domains including robotics, healthcare, and autonomous driving (Levine et al. Moerland et al., ). These approaches often proceed by performing experiments on a system to collect data, and then using the data to fit models for the dynamics. In the specified application domains, performing experiments requires interaction with the physical world, which can be both costly and time-consuming. It is therefore important to design the experimentation and identification procedures to efficiently extract the most information relevant to control. In particular, experiments must be designed with the downstream control objective in mind. This fact is well-established in classical controls and identification literature (Ljung Gevers Hjalmarsson et al. Pukelsheim, ). While these works provide some guidance for experiment design, they mostly focus on linear systems, and supply only asymptotic guarantees.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

Driven by the empirical success of machine and deep learning in solving classes of complex control problems, the learning and control communities have recently begun revisiting the classical pipeline of identification to control, proposing new algorithms, and analyzing them from a non-asymptotic viewpoint. Early efforts focused on end-to-end control guarantees for unknown linear system under naive exploration (injecting white noise inputs) (Dean et al. Mania et al., ). These methods have also been refined by using active learning to collect better data for control synthesis. This approach has been extended to nonlinear systems with a linear dependence on the unknown parameters. Other works studying model-based control of nonlinear systems also assume linear dependence on the unknown parameters, or consider related simplifying assumptions in settings including tabular or low-rank Markov Decision Processes (Uehara and Sun Song and Sun, ). Model-based reinforcement learning for a general class of nonlinear systems has also been considered. However, their guarantees focus on the worst case uncertainty of any control policy rather than end-to-end control costs for a particular objective.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

There is a significant gap in that there are no algorithms with strong guarantees (achieving the optimal rates) for model-based reinforcement learning of general nonlinear dynamical systems. We leverage recently developed machinery for non-asymptotic analysis of nonlinear system identification to tackle this problem.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Contribution", "weight": 1.0} -->

We introduce and analyze the Active Learning for Control-Oriented Identification (ALCOI) algorithm. This algorithm extends an approach for model-based reinforcement learning proposed by Wagenmaker et al. for dynamical systems with a linear dependence on the unknown parameter to general nonlinear dynamics that satisfy some smoothness assumptions. The algorithm is inspired by a reduction of the excess control cost to the system identification error, which may then be controlled using novel finite sample system identification error bounds for smooth nonlinear systems.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Contribution", "weight": 1.0} -->

Leveraging the aforementioned reduction of the excess control cost and system identification error bounds, we derive finite sample bounds for the excess cost of our algorithm.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Additional Work Analyzing Identification & Control", "weight": 1.0} -->

Finite sample guarantees for active exploration of pure system identification have been studied in linear, and nonlinear (with linear dependence on the unknown parameters) settings. Lower bounds complementing the upper bounds for the end-to-end control are also present (Wagenmaker et al. ), and have been specialized to the linear-quadratic regulator setting to characterize systems which are hard to learn to control. Recent literature considers gradient-based approaches for experiment design in linear-quadratic control. For more details on finite sample analysis of learning to control, see the survey by Tsiamis et al.. The aforementioned results do not focus on general nonlinear systems. Such analysis exists for identification; however, in the absence of end-to-end control error bounds (Sattar and Oymak Ziemann and Tu, ). In contrast, we achieve end-to-end control error bounds for active learning applied for learning to control general nonlinear systems.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Dual Control", "weight": 1.0} -->

A related paradigm to the "identify then control" scheme studied in this work is that of *dual control*, in which the learner must interact with an unknown system while simultaneously optimizing a control objective. Åström and Wittenmark study a version of this problem known as the self-tuning regulator, providing asymptotic guarantees of convergence. Non-asymptotic guarantees for the self tuning regulator have been studied more recently from the online learning perspective of regret. Subsequent work provides matching upper and lower bounds for the regret of the self-tuning regulator problem. Lower bounds refining the dependence on system-theoretic constants have also been established Ziemann and Sandberg. The regret of learning to control nonlinear dynamical systems (with linear dependence on the unknown parameter) has also been studied (Kakade et al. Boffi et al., ). As in the "identify then control" setting, prior work in dual control has not provided finite sample analysis of the end-to-end control error for systems with nonlinear dependence on the unknown parameters.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Dual Control", "weight": 1.0} -->

\
Notation: Expectation (respectively probability) with respect to all the randomness of the underlying probability space is denoted by $\mathbb{E}$ (respectively $\mathbb{P}$). The Euclidean norm of a vector $x$ is denoted $\left\| x \right\|$. For a matrix $A$, the spectral norm is denoted $\left\| A \right\|$, and the Frobenius norm is denoted $\left\| A \right\|_{F}$. A symmetric, positive semi-definite matrix $A = A^{\top}$ is denoted $A \succeq 0$. $A \succeq B$ denotes that $A - B$ is positive semi-definite. Similarly, a symmetric, positive definite matrix $A$ is denoted $A \succ 0$. The minimum eigenvalue of a symmetric, positive semi-definite matrix $A$ is denoted $\lambda_{\min}{(A)}$.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Dual Control", "weight": 1.0} -->

For a positive definite matrix $A$, we define the $A$-norm as $\left\| x \right\|_{A}^{2} = {x^{\top}Ax}$. The gradient of a scalar valued function $f:{{\mathbb{R}}^{n}\rightarrow{\mathbb{R}}}$ is denoted $\nabla f$, and the Hessian is denoted $\nabla^{2}f$. The Jacobian of a vector-valued function $g:{{\mathbb{R}}^{n}\rightarrow{\mathbb{R}}^{m}}$ is denoted $Dg$, and follows the convention for any $x \in {\mathbb{R}}^{n}$, the rows of $Dg{(x)}$ are the transposed gradients of $g_{i}{(x)}$. The $p^{th}$ order derivative of $g$ is denoted by $D^{p}g$.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Problem Formulation", "weight": 1.0} -->

We consider a nonlinear dynamical system evolving according to

<!-- chunk {"id": "body-0013", "role": "body", "section": "Problem Formulation", "weight": 1.0} -->

The functions $c_{t}$ are known stage costs. The superscript on the expectation denotes that the dynamics are rolled out under parameter $\phi$, while the subscript denotes that the system is played in closed-loop under the feedback control policy $U_{t} = {\pi_{t}{(X_{1},U_{1},\ldots,X_{t - 1},U_{t - 1},X_{t})}}$ for $t = {1,\ldots,T}$. The learner follows a two step interaction protocol with an exploration phase, and an evaluation phase. In the exploration phase, the learner interacts with the system for a total of $N$ episodes, each consisting of $T$ timesteps, by playing exploration policies $\pi \in \Pi_{\exp}$. The policy class $\Pi_{\exp}$ is an exploration policy class, described in more detail below. The learner does not incur any cost during the exploration episodes, and seeks only to gain information about the system.

<!-- chunk {"id": "body-0014", "role": "body", "section": "Problem Formulation", "weight": 1.0} -->

After the $N$ interaction episodes, it uses the collected data to propose a policy $\hat{\pi} \in \Pi^{\star}$. The learner is then evaluated on the expected cost of the proposed policy on a new evaluation episode. In particular, it incurs cost $\mathcal{J}{(\hat{\pi},\phi^{\star})}$.

<!-- chunk {"id": "body-0015", "role": "body", "section": "Problem Formulation", "weight": 1.0} -->

No such parametric assumption is made on the exploration class $\Pi_{\exp}$. It instead consists of whatever experimental procedures are available. For instance, it may be the class of policies with power or energy bounded inputs. Policies belonging to $\Pi_{\exp}$ must be history dependent (causal). We assume that the learner is allowed to randomly select choices of policies in $\Pi_{\exp}$.^11^1i.e. for any ${\pi^{1},\pi^{2}} \in \Pi_{\exp}$ and any $b \in {\lbrack 0,1\rbrack}$, the policy $\pi_{\mathsf{m}\mathsf{i}\mathsf{x}}$ which at the start of a new episode plays $\pi^{1}$ for the duration of the episode with probability $b$ and $\pi^{2}$ for the duration of the episode with probability $1 - b$ also belongs to $\Pi_{\exp}$.

<!-- chunk {"id": "body-0016", "role": "body", "section": "Problem Formulation", "weight": 1.0} -->

Given these policy classes, the learning procedure should seek to identify the best exploitation policy belonging to $\Pi^{\star}$ by playing the most informative exploration policy in the class $\Pi_{\exp}$.

<!-- chunk {"id": "body-0017", "role": "body", "section": "Certainty Equivalent Control", "weight": 1.0} -->

We focus on learners which follow a model-based approach to synthesize a control policy from interaction with the system, outlined in Figure 1. In this section, we discuss the learner's procedure for the last two steps: system identification and control synthesis. In Section 3, we return to the question of which experiments the learner should perform.

<!-- chunk {"id": "body-0018", "role": "body", "section": "Certainty Equivalent Control", "weight": 1.0} -->

Given the data collected during the experimentation phase, the learner finds an estimate for the dynamics by solving a nonlinear least squares problem. In particular, suppose that during the $N$ experimentation episodes of length $T$, the learner collects data $\left\{ {(U_{t}^{n},X_{t}^{n},X_{t + 1}^{n})} \right\}_{{n,t} = 1}^{N,{T + 1}}$. The subscript denotes the time index within each episode, while the superscript denotes the episode index. Using this dataset, the learner may identify the dynamics of the system by solving

<!-- chunk {"id": "body-0019", "role": "body", "section": "Certainty Equivalent Control", "weight": 1.0} -->

Solving this problem provides a parameter estimate which is an effective predictor under the distribution of states and inputs seen during the experimentation. This notion can be captured via the prediction error.

<!-- chunk {"id": "body-0020", "role": "body", "section": "Assumptions", "weight": 1.0} -->

By, the optimal policy for the objective under the true parameter $\phi^{\star}$ defining the dynamics is thus given by $\pi^{\star}{(\phi^{\star})}$, and the corresponding objective value is $\mathcal{J}{({\pi^{\star}{(\phi^{\star})}},\phi^{\star})}$. Meanwhile, the objective value attained under an estimate $\hat{\phi}$ is $\mathcal{J}{({\pi^{\star}{(\hat{\phi})}},\phi^{\star})}$. We abuse notation and define the shorthand

<!-- chunk {"id": "body-0021", "role": "body", "section": "Assumptions", "weight": 1.0} -->

to describe the control cost of applying a certainty equivalence policy synthesized using parameter $\phi$ on a system with dynamics described by $\overset{\sim}{\phi}$. It has been shown by Wagenmaker et al. that for models which are linear in the parameters, the gap ${\mathcal{J}_{\phi^{\star}}{(\phi)}} - {\mathcal{J}_{\phi^{\star}}{(\phi^{\star})}}$ is characterized by the squared parameter error weighted by the *model-task Hessian*, defined below.

<!-- chunk {"id": "body-0022", "role": "body", "section": "Assumption 2.1", "weight": 1.0} -->

The above assumption is satisfied, e.g., control-affine dynamics which depend smoothly on $\phi$: ${f{(x_{t},u_{t};\phi)}} = {{g_{1}{(x_{t};\phi)}} + {g_{2}{(u_{t};\phi)}u}}$, with $g_{1}$ and $g_{2}$ each three time differentiable with respect to $\phi$. In this example, differentiability with respect to $u$ is immediate from the affine dependence.

<!-- chunk {"id": "body-0023", "role": "body", "section": "Assumption 2.1", "weight": 1.0} -->

We also require that the policy class $\Pi^{\star}$ is smooth.

<!-- chunk {"id": "body-0024", "role": "body", "section": "Assumption 2.2", "weight": 1.0} -->

Note that such smoothness conditions are not imposed for the exploration policy class $\Pi_{\exp}$. The exploration policy class could, for instance, consist of model predictive controllers with constraints on the injected input energy, which do not satisfy such smoothness assumptions.

<!-- chunk {"id": "body-0025", "role": "body", "section": "Assumption 2.2", "weight": 1.0} -->

We additionally require that the costs are bounded for policies in the class $\Pi_{\star}$ and all dynamics parameters in a neighborhood of the true parameter.

<!-- chunk {"id": "body-0026", "role": "body", "section": "Assumption 2.3", "weight": 1.0} -->

We additionally assume that the certainty equivalent policy is a smooth function of the dynamics parameter in a neighborhood around the optimal parameter.

<!-- chunk {"id": "body-0027", "role": "body", "section": "Assumption 2.4", "weight": 1.0} -->

It is shown in Proposition 6 of Wagenmaker et al. that the above condition holds if ${{\nabla_{\theta}^{2}J}{(\pi^{\theta},\phi^{\star})}} \succ 0$.^22^2Wagenmaker et al. show this result for the linear in the parameters setting; however, it extends easily to the smooth nonlinear setting. See Appendix B. The above assumption also holds in the setting of linear-quadratic regulation, as may be verified using the LQR derivative expressions in Simchowitz and Foster.

<!-- chunk {"id": "body-0028", "role": "body", "section": "Assumption 2.4", "weight": 1.0} -->

In order to bound the parameter recovery error in terms of the prediction error, additional identifiability conditions are needed. The following definition of a Lojasiewicz exploration policy is determined from a Lojasiewicz condition that arises in the optimization literature that measures the sharpness of an objective near its optimizer. In our setting, it quantifies the degree of identifiability from using a particular exploration policy. It does so by bounding the growth of identification error as a polynomial of prediction error.

<!-- chunk {"id": "body-0029", "role": "body", "section": "Assumption 2.5", "weight": 1.0} -->

While the Lojasiewicz assumption ensures that the data collected via the exploration policy $\pi^{0}$ is sufficient to identify the parameters, the rate of recovery may be slow. To bypass this limitation, we assume that some policy in the exploration class satisfies a persistence of excitation condition. This condition can be expressed by first defining the Fisher information matrix for a parameter $\phi$ and a policy $\pi$ as

<!-- chunk {"id": "body-0030", "role": "body", "section": "Assumption 2.5", "weight": 1.0} -->

where $Df{(X_{t},U_{t},\phi)}$ is the Jacobian of $f$ with respect to $\phi$. The Fisher information measures the signal-to-noise ratio of the data collected from an episode of interaction with the system under exploration policy $\pi$. With this definition, persistance of excitation is equivalent to the positive definiteness of the matrix ${\mathbf{F}\mathbf{I}}^{\pi}{(\phi^{\star})}$.

<!-- chunk {"id": "body-0031", "role": "body", "section": "Assumption 2.6", "weight": 1.0} -->

There exists a policy $\pi \in \Pi_{\exp}$ for which

<!-- chunk {"id": "body-0032", "role": "body", "section": "Proposed Algorithm and Main Result", "weight": 1.0} -->

The above smoothness assumptions allow us to characterize the excess control cost of a policy synthesized via certainty equivalence applied to a parameter estimate $\hat{\phi}$,. In particular, we extend a result from Wagenmaker et al. from the linear in parameters setting to the smooth nonlinear setting.

<!-- chunk {"id": "body-0033", "role": "body", "section": "Numerical Validation", "weight": 1.0} -->

We deploy ALCOI on an illustrative example to illustrate the benefits of active control-oriented exploration. For more experiments, and further details, see Appendix D. Consider the two dimensional system

<!-- chunk {"id": "body-0034", "role": "body", "section": "Numerical Validation", "weight": 1.0} -->

We consider model-based reinforcement learning with a horizon $T = 10$ and quadratic cost functions: for all $t \in {\lbrack T\rbrack}$,

<!-- chunk {"id": "body-0035", "role": "body", "section": "Numerical Validation", "weight": 1.0} -->

We compare ALCOI with random exploration and approximate $A$-optimal experiment design. For random exploration, the learner injects isotropic Gaussian noise which is normalized such that ${\sum_{t = 1}^{T}\left\| U_{t} \right\|^{2}} = T$. For approximate $A$-optimal experiment design, the learner runs the ALCOI, but with the model-task Hessian estimate, $\mathcal{H}{({\hat{\phi}}^{-})}$, replaced by $I$.

<!-- chunk {"id": "body-0036", "role": "body", "section": "Conclusions", "weight": 1.0} -->

We have introduced and analyzed the Active Learning for Control-Oriented Identification (ALCOI) algorithm, marking a significant step towards understanding active exploration in model-based reinforcement learning for a general class of nonlinear dynamical systems. We provide finite sample bounds on the excess control cost achieved by the algorithm which offer insight into the interaction between the hardness of control and identification. Our bounds are known to be sharp up to logarithmic factors in the setting of nonlinear dynamical systems with linear dependence on the parameters, and we conjecture that they are sharp in general. Future work will attempt to verify that this is the case. It would also be interesting for future work to consider learning partially observed dynamics using general prediction error methods, rather than assuming a noiseless state observation.
