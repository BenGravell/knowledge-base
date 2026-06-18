<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Multimodal Probabilistic Model-Based Planning for Human-Robot Interaction

Topics include Multimodal, Probabilistic, Motion planning, Interaction-aware, Human, Robot, Model-based.

<!-- chunk {"id": "summary-0002", "role": "summary", "section": "Summary", "weight": 2.0} -->

The paper puts together a few cool technologies, such as massively parallel trajectory sampling and evaluation on a GPU, as well as a CVAE neural network trained on actual human driving data for prediction of future driver response at robot inference time.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

This paper presents a method for constructing human-robot interaction policies in settings where multimodality, i.e., the possibility of multiple highly distinct futures, plays a critical role in decision making. We are motivated in this work by the example of traffic weaving, e.g., at highway on-ramps/off-ramps, where entering and exiting cars must swap lanes in a short distance - a challenging negotiation even for experienced drivers due to the inherent multimodal uncertainty of who will pass whom. Our approach is to learn multimodal probability distributions over future human actions from a dataset of human-human exemplars and perform real-time robot policy construction in the resulting environment model through massively parallel sampling of human responses to candidate robot action sequences. Direct learning of these distributions is made possible by recent advances in the theory of conditional variational autoencoders (CVAEs), whereby we learn action distributions simultaneously conditioned on the present interaction history, as well as candidate future robot actions in order to take into account response dynamics. We demonstrate the efficacy of this approach with a human-in-the-loop simulation of a traffic weaving scenario.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

Human behavior is inconsistent across populations, settings, and even different instants, with all other factors equal---addressing this inherent uncertainty is one of the fundamental challenges in human-robot interaction (HRI). Even when a human's broader intent is known, there are often multiple distinct courses of action they may pursue to accomplish their goals. For example, a driver signaling a lane change may throttle up aggressively to pass in front of a blocking car, or brake to allow the adjacent driver to pass first. To an observer, the choice of mode may seem to have a random component, yet also depend on the evolution of the human's surroundings, e.g., whether the adjacent driver begins to yield. Taking into account the full breadth of possibilities in how a human may respond to a robot's actions is a key component of enabling anticipatory and proactive robot interaction policies. With the goal of creating robots that interact intelligently with human counterparts, observing data from human-human interactions provides valuable insight into predicting interaction dynamics. In particular, a robot may reason about human actions, and corresponding likelihoods, based on how it has seen humans behave in similar settings.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

Accordingly, the objective of this paper is to devise a data-driven framework for HRI that leverages learned multimodal human action distributions in constructing robot action policies.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

Methods for autonomous decision making under uncertainty may be classified as model-free, whereby human action possibilities and associated likelihoods are implicitly encoded in a robot control policy learned from trial experience, or model-based, whereby a probabilistic understanding of the interaction dynamics is used as the basis for policy construction. In this paper we take a model-based approach to pairwise human-robot interaction, seeking to explicitly characterize a possibly multimodal distribution over human actions at each time step conditioned on interaction history as well as future robot action choices. By decoupling action/reaction prediction from policy construction, we aim to achieve a degree of transparency in a planner's decision making that is typically unavailable in model-free approaches. Conditioning on history allows a robot to reason about hidden factors like experience, mood, or engagement level that may influence the distribution, and conditioning on the future takes into account response dynamics. We develop our work around a traffic weaving case study (Fig. 1) for which we adapt methods from deep neural network-based language and path prediction to learn a Conditional Variational Autoencoder (CVAE) generative model of human driver behavior.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

We validate this model as the basis for a limited-lookahead autonomous driver action policy, applied in a receding horizon fashion, the behavior of which we explore with human-in-the-loop testing.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Introduction", "weight": 1.5} -->

We highlight five key considerations that motivate our modeling and policy construction framework. First, for interactive situations, the modeling framework must be capable of predicting human behavior in response to (i.e., conditioned on) candidate robot actions. Second, we target decision-making scenarios with characteristic action and response time scales on the order of $\sim$`<!-- -->`{=html}1 second. This is as opposed to higher-level reasoning over a set of multi-second action sequences or action-generating policies (e.g., whether a driver intends to turn or continue straight at an intersection, or intends to initiate a highway lane change ). Nor do we attempt to emulate lower-level reactive controllers (e.g., emergency collision avoidance systems ) that must operate on the order of milliseconds. Third, as previously stressed, the uncertainty in human actions on this time scale may be multimodal, corresponding to varied optimal robot action plans. Fourth, we desire a prediction model that is history-dependent, capable of inferring latent features of human behavior.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Introduction", "weight": 1.5} -->

Fifth, although our prediction model is trained "end-to-end" from state observations to human action distributions, this work decouples dynamics learning from policy construction to aid interpretability and enable flexibility with respect to robot goals.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Introduction", "weight": 1.5} -->

*Related Work*: A major challenge in learning generative probabilistic models for HRI is accounting for the rapid growth in problem size due to the time-series nature of interaction; state-of-the-art approaches rely on some form of dimensionality reduction to make the problem tractable. One option is to model humans as optimal planners and represent their motivations at each time step as a state/action-dependent cost (equivalently, negative reward) function. Minimizing this function, e.g., by following its gradients to select next actions, may be thought of as a computational proxy for human decision-making processes. This cost function has previously been expressed as a linear combination of potential functions in a driving context; Inverse Reinforcement Learning (IRL) is a generalization of this idea whereby a parameterized family of cost functions is fit to a dataset of human state-action trajectories.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Introduction", "weight": 1.5} -->

Typically, the cost function is represented as a linear combination of possibly nonlinear features, ${c{(x,u)}} = {\theta^{T}\phi{(x,u)}}$, and the weight parameters $\theta$ are fit to minimize a measure of error between the actions that optimize $c$ and the true human actions.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Introduction", "weight": 1.5} -->

Maximum entropy IRL interprets this cost function as a probability distribution over human actions, with ${p{(u)}} \propto {\exp{({- {c{(x,u)}}})}}$, and in this case the weights $\theta$ are fit according to maximum likelihood. This framework is employed in the context of interactive driving in to construct robot policies that avoid being overly defensive by leveraging expected human responses to robot actions. In that work, however, the probabilistic interpretation of $c$ is used only in fitting the human model, not in robot policy construction, where it is assumed that the human selects best responses to robot actions in a Stackelberg game formulation. This analysis yields a unified and tractable framework for prediction and policy construction, but fundamentally represents a unimodal assumption on interaction outcome; we note that this style of reasoning has proven dangerous in the case that critical outcomes go uncaptured.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Introduction", "weight": 1.5} -->

Regarding multimodal probabilistic dynamics, it is true that with sufficiently complex and numerous features the cost function $\theta^{T}\phi{(x,u)}$ may approximate any log-probability distribution over $u$, conditioned on state $x$, arbitrary well (although we note that IRL is typically applied to learn importance weights for a handful of human-interpretable features). Without some form of state augmentation, however, this formulation is Markovian and incapable of conditioning on interaction history when reasoning about the future.

<!-- chunk {"id": "body-0014", "role": "body", "section": "Introduction", "weight": 1.5} -->

An additional requirement of cost/motivation-based human modeling methods for use in interactive scenarios is a means to reason about a human's reasoning process. Game theory has been applied to combine human action/reaction inference and robot policy construction. Common choices are Stackelberg formulations whereby human and robot alternate "turns," hierarchical reasoning or "level-$k$" approaches whereby agents recursively reason about others reasoning about themselves down to a bounded base case, and equilibria assumption, taking $k\rightarrow\infty$. In this work we approach the human modeling problem phenomenologically, attempting to directly learn the action probability distribution that might arise from such a game formulation.

<!-- chunk {"id": "body-0015", "role": "body", "section": "Introduction", "weight": 1.5} -->

Computationally tractable human action modeling has also been achieved by grouping actions over multiple time steps and reasoning over a discrete set of template action sequences or action-generating policies. These methods often tailor means for modeling dependencies between observations, predictions, and latent variables specific to their application that may be used to incorporate information about interaction history. In the context of mutual adaptation for more efficient task execution, considers multimodal outcomes and maintains a latent state representing a human's inclination to adapt. The approach of for synthesizing autonomous driving policies is very similar in spirit to our work; their prediction model is capable of capturing multimodal human behavior at every time step, dependent on state history and robot future, which they use to score and select from a set of candidate policies for an autonomous vehicle. However, they restrict their treatment of time to changepoint-delineated segments within which the human action distribution takes the form of a Gaussian Mixture Model (GMM). The mean trajectories of these Gaussian components (modes) are predetermined by the choice of a finite set of high-level driving behavior policies, and mixture weight inference takes place over the current time segment.

<!-- chunk {"id": "body-0016", "role": "body", "section": "Introduction", "weight": 1.5} -->

Inspired by the recent groundbreaking success of deep neural networks in modeling distributions over language sequences and geometric paths, we seek instead to learn a generative model for human behavior that does not decouple time segmentation from probabilistic mode inference, and is capable of learning the equivalent of arbitrary mode policies from data. Instead of directly fitting a neural network function approximator to log probability, akin to extending maximum entropy IRL with deep-learned features, we use a CVAE setup to learn an efficiently sampleable mixture model with terms that represent different driving behaviors over a prediction time horizon. We use recurrent neural networks (RNNs) that maintain a hidden state to iteratively condition each time step's action prediction on the preceding time steps. This opens up the possibility for another level of multimodality within the prediction horizon (e.g., uncertainty in exactly when a human will initiate a predicted braking maneuver), that would otherwise require too many mixture components. An alternate interpretation of why this second level of multimodality is required is to address the case that a mode changepoint, in the language of, lies within the fixed prediction horizon.

<!-- chunk {"id": "body-0017", "role": "body", "section": "Introduction", "weight": 1.5} -->

We would also like to briefly mention as a recent nonparametric learning method that compares human driver trajectories to a form of nearest neighbors from an interaction dataset in order to predict future behavior, however, the authors of note that this comparison procedure is difficult to scale at run time for online policy construction.

<!-- chunk {"id": "body-0018", "role": "body", "section": "Introduction", "weight": 1.5} -->

*Statement of Contributions*: The primary contribution of this paper is the synthesis and demonstration of a data-driven framework for HRI that, to the best of our knowledge, uniquely meets all five aforementioned conditions for desirable model-based policy construction in rapidly evolving multimodal interaction scenarios. Our human modeling approach, while more data-intensive than some existing alternatives, does not make any assumptions on human preference or indifference between scenario outcome modes, nor does it assume any game-theoretic hierarchy of interaction participant beliefs. The decision framework maintains a degree of interpretability, even as a purely phenomenological data-driven approach, as we are able to visualize through model sampling how the robot anticipates a human might respond to its actions. We demonstrate a massively parallelized robot action sequence selection process that simulates nearly 100 000 human futures every 0.3 seconds on commodity GPU hardware; this allows us to claim coverage of all possible interaction modes within the planning horizon. This policy is demonstrated in a Model Predictive Control (MPC) fashion in real-time human-robot pairwise traffic weaving simulation.

<!-- chunk {"id": "body-0019", "role": "body", "section": "Introduction", "weight": 1.5} -->

Though the present work is validated in a virtual world for a scenario that, to be frank, may not require such powerful tools as deep neural network-empowered CVAEs or massively parallel GPU simulation for solution, our vision is that as more and more features, e.g., human gestures or verbalizations, beg algorithmic incorporation in more and more complex scenarios, our model-based approach may accommodate them without additional assumptions.

<!-- chunk {"id": "body-0020", "role": "body", "section": "Introduction", "weight": 1.5} -->

*Notation*: In this paper we use superscripts, e.g., $x^{(t)}$, to denote the values of quantities at discrete time steps, and the notation $x^{({t_{1}:t_{2}})} = {(x^{(t_{1})},x^{({t_{1} + 1})},\ldots,x^{(t_{2})})}$ to denote a sequence of values at time steps between $t_{1} \leq t_{2}$ inclusive.

<!-- chunk {"id": "body-0021", "role": "body", "section": "II-A Interaction Dynamics", "weight": 1.0} -->

Let the deterministic, time-invariant, discrete-time state space dynamics of a human and robot be given by

<!-- chunk {"id": "body-0022", "role": "body", "section": "II-A Interaction Dynamics", "weight": 1.0} -->

is a random variable (capitalized to distiguish from a drawn value $u_{h}^{({t + 1})}$). We suppose additionally that $U_{h}^{({t + 1})}$ is distributed according to a probability density function (pdf) which we write as $p{({u_{h}^{({t + 1})} \mid {x^{({0:t})},u^{({0:t})},u_{r}^{({t + 1})}}})}$.^11^1We note that if $U_{h}^{({t + 1})}$ has a discrete component, e.g., a zero acceleration action with positive probability mass, we may add a small amount of white noise to observed values $u$ when fitting distributions for $U_{h}^{({t + 1})}$ to preserve this assumption. In this work we assume full observability of all past states and actions by both agents.

<!-- chunk {"id": "body-0023", "role": "body", "section": "II-A Interaction Dynamics", "weight": 1.0} -->

Note that by iteratively propagating and sampling, a robot may reason about the random variable $U_{h}^{({{t + 1}:{t + N}})}$, denoting a human's response sequence to robot actions $u_{r}^{({{t + 1}:{t + N}})}$ over a horizon of length $N$.

<!-- chunk {"id": "body-0024", "role": "body", "section": "II-B Robot Goal", "weight": 1.0} -->

where $\gamma \in {\lbrack 0,1\rbrack}$ is a discount factor. Taking $N\rightarrow\infty$ recovers a classical infinite-horizon MDP formulation (although, we note that in this interpretation the state transition distribution is a function of the full state history due to ). In practice we take $N = 15$ (with time interval 0.1s) and iteratively solve, executing only the first action in an MPC fashion. Note that at time $t$ we are solving for the action to take at time step $t + 1$, as owing to nonzero computation times we regard the robot action $u_{r}^{(t)}$ to already be in progress, having been computed at the previous time step.

<!-- chunk {"id": "body-0025", "role": "body", "section": "II-C Traffic Weaving Scenario", "weight": 1.0} -->

Although we have developed our approach generally for pairwise human-robot interactions where the human may be regarded as acting stochastically, we focus in particular on a traffic weaving scenario as depicted in Fig. 1. We learn a human action model and compute a robot policy with the assumption that both agents are signaling an intent to swap lanes. Let $(s,\tau)$ be the coordinate system for the two-lane highway where $s$ denotes longitudinal distance along the length of the highway (with $0$ at the cutoff point and negative values before) and $\tau$ denotes lateral position between the lanes (with $0$ at the left-most extent of the left lane and negative values to the right).

<!-- chunk {"id": "body-0026", "role": "body", "section": "II-C Traffic Weaving Scenario", "weight": 1.0} -->

We consider the center of mass of the human-controlled car ("human") to obey double-integrator dynamics ($u_{h} = {\lbrack{\overset{¨}{s}}_{h},{\overset{¨}{\tau}}_{h}\rbrack}$, $x_{h} = {\lbrack s_{h},\tau_{h},{\overset{˙}{s}}_{h},{\overset{˙}{\tau}}_{h}\rbrack}$ in continuous form). These dynamics may be transformed to various simple car models and map closely to body-frame longitudinal acceleration and steering angle at highway velocities. It is for this latter consideration that we choose a second-order system model, as we believe it most straightforward to fit a generative pdf to inputs on the same order of the true human inputs (throttle and steering command), even if the reward is a function only of human position or velocity.

<!-- chunk {"id": "body-0027", "role": "body", "section": "II-C Traffic Weaving Scenario", "weight": 1.0} -->

The robot receives a large penalty for colliding with the human and is motivated to switch lanes before entering the terminal set $\mathcal{T} = {\{{x = {(x_{h},x_{r})}}\mid{s_{r} \geq 0}\}}$ by a running cost proportional to lateral distance to target lane $|{\tau_{r} - \tau_{r}^{\text{target}}}|$ multiplied by an increasing measure of urgency as $s_{r}$ approaches 0, as well as a reward term that encourages joint states $x$ where the two cars are moving apart longitudinally. Further details of the cost expression are discussed in Section V-C.

<!-- chunk {"id": "body-0028", "role": "body", "section": "II-C Traffic Weaving Scenario", "weight": 1.0} -->

A few comments are in order. First, we note that the distributional form admits the possibility that the human has knowledge of the robot's next action before selecting his/her own. This Stackelberg assumption has been employed previously in similar learning contexts, but we stress that in the present work this assumption has no bearing on policy construction, where we only sample from $P$. Conditioning on extraneous information should have a negligible effect on learning if $u_{h}^{({t + 1})}$ and $u_{r}^{({t + 1})}$ are truly independent. Second, this formulation is intended to capture factors that may be observed in the prior interaction history $x^{({0:t})}$, e.g., population differences in driving style, as well as the response dynamics of the interaction, e.g., game-theoretic behaviors that have previously been modeled explicitly. Admittedly, approaching this modeling problem phenomenologically, as opposed to devising a more first-principles approach, requires significantly more data to fit.

<!-- chunk {"id": "body-0029", "role": "body", "section": "II-C Traffic Weaving Scenario", "weight": 1.0} -->

However, with large-scale industrial data collection operations already in place, the ability to utilize large datasets in studying relatively common interaction scenarios, such as the traffic weaving example studied in this paper, is becoming increasingly common. Third, we note that the robot cost objective sketched above is admittedly rather ad hoc; this is a consequence of requiring the robot to make decisions over a fixed time horizon. We argue that it is difficult to trust interactive prediction models over long horizons $N \gg 0$ in any case, necessitating some sort of long-term cost heuristic to inform short-term actions. Furthermore, our model-based framework can accommodate other cost objectives should they better suit a system designer's preferences, though is not clear what a quantitative measure of quality should be for this traffic weaving scenario. Changing lanes smoothly and courteously, as a human would, does not imply, e.g., that the robot should plan for minimum time or safest possible behavior.

<!-- chunk {"id": "body-0030", "role": "body", "section": "Human Agent Modeling", "weight": 1.0} -->

Inspired by recent breakthroughs in sequence-to-sequence learning for language modeling and geometric path generation, as well as unsupervised end-to-end learning of complex conditional distributions, we design our learning framework as a neural network Conditional Variational Autoencoder (CVAE) with recurrent subcomponents to manage the time-series nature of the interaction. Considering a fixed prediction time step $t$, let $\mathbf{x} = {(x^{({0:t})},u^{({0:t})},u_{r}^{({{t + 1}:{t + N}})})}$ be the conditioning variable (joint interaction history + candidate robot future) and $\mathbf{y} = u_{h}^{({{t + 1}:{t + N}})}$ be the prediction output (human future). That is, we seek to learn a pdf $p{(\left. \mathbf{y} \middle| \mathbf{x} \right.)}$.

<!-- chunk {"id": "body-0031", "role": "body", "section": "Human Agent Modeling", "weight": 1.0} -->

The CVAE framework introduces a latent variable $\mathbf{z}$ so that ${p{(\left. \mathbf{y} \middle| \mathbf{x} \right.)}} = {\int_{\mathbf{z}}{p{(\left. \mathbf{y} \middle| {\mathbf{x},\mathbf{z}} \right.)}p{(\left. \mathbf{z} \middle| \mathbf{x} \right.)}{d\mathbf{z}}}}$; the intent of introducing such a $\mathbf{z}$ is to model inherent structure in the interaction which may both improve learning performance as well as provide a foothold for interpretation of the results. We model $p{(\left. \mathbf{y} \middle| {\mathbf{x},\mathbf{z}} \right.)}$ and $p{(\left.

<!-- chunk {"id": "body-0032", "role": "body", "section": "Human Agent Modeling", "weight": 1.0} -->

\mathbf{z} \middle| {\mathbf{x}_{i},\mathbf{y}_{i}} \right.)}$ of the true posterior $p{(\left. \mathbf{z} \middle| {\mathbf{x}_{i},\mathbf{y}_{i}} \right.)}$, and the evidence-based lower bound (ELBO) on log-likelihood is maximized instead. For a detailed discussion see. Our CVAE architecture, depicted in Fig. 2, is similar to existing sequence-to-sequence variational autoencoder architectures including the use of RNN encoders/decoders; we highlight here a few key design choices that we feel are essential to our model's success.

<!-- chunk {"id": "body-0033", "role": "body", "section": "III-A CVAE Architecture", "weight": 1.0} -->

\mathbf{y} \middle| {\mathbf{x},\mathbf{z}} \right.)}p{(\left. \mathbf{z} \middle| \mathbf{x} \right.)}}}$ may be thought of as a mixture model with components corresponding to each discrete instantiation of $\mathbf{z}$. The learned distributions in our work have $\mathbf{z}$ values that manifest as different human response modes, e.g., accelerating/decelerating or driving straight/turning over the next $N$ time steps, as illustrated in Section V-B. Modeling this multimodal human response behavior is a core focus of this work; the benefits of using a discrete latent space to learn multimodal distributions has been previously studied.

<!-- chunk {"id": "body-0034", "role": "body", "section": "III-A CVAE Architecture", "weight": 1.0} -->

In our model, the discrete latent variable $\mathbf{z}$ has the responsibility of representing high-level behavior modes, while a second level of multimodality within each such high-level behavior is facilitated by an autoregressive RNN sequence decoder (light purple cells, Fig. 2).

<!-- chunk {"id": "body-0035", "role": "body", "section": "III-A CVAE Architecture", "weight": 1.0} -->

where we use the notation $\mathbf{y}^{(i)} = u_{h}^{({t + i})}$, the $i$-th future human action after the current time step $t$. A GMM output layer of each RNN cell with $M_{\text{GMM}}$ components in human action space provides the basis for learning arbitrary distributions for each $p{(\left. \mathbf{y}^{(i)} \middle| {\mathbf{x},\mathbf{z},\mathbf{y}^{({1:{i - 1}})}} \right.)}$ (light blue, Fig. 2). This combined structure is designed to account for variances in human trajectories for the same latent behavior $\mathbf{z}$.

<!-- chunk {"id": "body-0036", "role": "body", "section": "III-A CVAE Architecture", "weight": 1.0} -->

For example, an action sequence of braking at the fourth time step instead of at the third time step would likely need to belong in a different component of, e.g., a non-recurrent Gaussian Mixture Model, causing an undue combinatorial explosion in the required number of distinct $\mathbf{z}$ values.

<!-- chunk {"id": "body-0037", "role": "body", "section": "III-A CVAE Architecture", "weight": 1.0} -->

We use long short-term memory (LSTM) RNN cells, and in addition to typical model training techniques (e.g., recurrent dropout regularization and hyperparameter annealing), we employ the method introduced in to prevent prediction errors from severely cascading into the future. During train time in the decoder (right side, Fig. 2), with a rate of $10\%$ we use the predicted value ${\hat{u}}_{h}^{(t)}$ as the input into the next cell, otherwise we use the true value from the training data. That is, instead of learning individual terms of, we occasionally learn them jointly. Similar to we augment the human action inputs for the autoregressive decoder RNN with an additional context vector $c^{(t)}$ composed of the robot action at that time step $u_{r}^{(t)}$, the latent variable $\mathbf{z}$ and the output from the encoder $h_{x}$. We do this to more explicitly mimic the form of the expression $p{(\left.

<!-- chunk {"id": "body-0038", "role": "body", "section": "Robot Policy Construction", "weight": 1.0} -->

We apply an exhaustive approach to optimizing problem over robot action sequences where at each time step the robot is allowed to take one of a finite set of actions (in particular, we group the $N = 15$ future time steps into five 3-step windows over which the robot takes 1 of 8 possible actions, see Section V-C for details). We stress that we are only discretizing the robot action space for policy computation efficiency; the human prediction model is still computed over a continuous action space. While Monte Carlo Tree Search (MCTS) methods have seen successful application in similar problems with continuous state/action spaces, due to the massively parallel GPU implementation of modern neural network frameworks we find it is more expedient to simply evaluate the expected cost of taking all action sequences (or a significant fraction of them) for sufficiently short horizons $N$. We take a two step approach, approximately evaluating all action sequences with a low number of samples (human response futures) each, and then reevaluating the most promising action sequences with a much larger number of samples to pick the best one (see Section V-C).

<!-- chunk {"id": "body-0039", "role": "body", "section": "Robot Policy Construction", "weight": 1.0} -->

We note that gradient-based methods could prove useful for further action sequence refinement, but for scenarios characterized by multimodal outcomes some form of broader search must be applied lest optimization end in a local minimum.

<!-- chunk {"id": "body-0040", "role": "body", "section": "Traffic Weaving Case Study", "weight": 1.0} -->

The human-human traffic weaving dataset and source code for all results in this section, including all network architecture details and hyperparameters, are available at All simulation and computation was done on a computer running Ubuntu 16.04 equipped with a 3.6GHz octocore AMD Ryzen 1800X CPU and an NVIDIA GeForce GTX 1080 Ti GPU.

<!-- chunk {"id": "body-0041", "role": "body", "section": "V-A Data Collection", "weight": 1.0} -->

State and action trajectories of two humans navigating a traffic weaving scenario were collected using a driving simulator shown in Fig. 1 (left). 1105 human-human driving interaction trials were recorded over 19 different pairs of people. The drivers had to swap lanes with each other (without verbal communication) within 135 meters of straight road. Each human trajectory in each trial exhibits interaction behavior to be learned, effectively doubling the data set. Furthermore, since we are conditioning on interaction history and partner future, cumulatively speaking we have roughly 35 histories per trial: each trial is approximately five seconds long, equating to $T \approx 50$ with 0.1s time steps, and taking the prediction horizon of $N = 15$ into account.

<!-- chunk {"id": "body-0042", "role": "body", "section": "V-A Data Collection", "weight": 1.0} -->

Hence in total, our dataset contains roughly 77 000 $\mathbf{x} = {(x^{({0:t})},u^{({0:t})},u_{r}^{({{t + 1}:{t + N}})})}$ to $\mathbf{y} = u_{h}^{({{t + 1}:{t + N}})}$ exemplars. We note that owing to the interactive nature of this scenario we elected to collect our own dataset using the simulator rather than use existing real-world data (e.g., ). Fitting the parameters of our model requires a high volume of traffic weaving interaction exemplars which these open datasets do not encompass, but which we believe a targeted industrial effort might easily procure.

<!-- chunk {"id": "body-0043", "role": "body", "section": "V-A Data Collection", "weight": 1.0} -->

Each scenario begins with initial conditions (IC) drawn randomly as follows: car 1 (left or right lane) starts with speed $v_{1} = 29$m/s (65mph) and car 2 at a speed difference of ${\Deltav} = {v_{1} - v_{2}} \in {\{ 0,{\pm 2}\}}$ m/s ($\pm 4.5$ mph). The faster car starts a distance ${|{\Deltav}|}t_{co}$ behind the other car where $t_{co} \in {\{ 1,2,3\}}$ represents a "crossover time" when the cars would be side-by-side if neither accelerates or decelerates, as shown in Fig. 3. The ICs were designed to make ambiguous which car should pass in front of the other, to encourage multimodality in action sequences and outcomes that may occur.

<!-- chunk {"id": "body-0044", "role": "body", "section": "V-A Data Collection", "weight": 1.0} -->

This ambiguity is indicated by Table I where as $t_{co}$ increases, the car moving faster but starting further behind, which usually passes in front of the other car, becomes less likely to cut in front. Reckless and irresponsible "video game" driving was discouraged by having a speedometer displayed on screen with engine hum sound feedback to reflect current speed and a high-pitched alert sound when speed exceeded 38m/s (85mph).

<!-- chunk {"id": "body-0045", "role": "body", "section": "V-B Generative Model for Human Driver Actions", "weight": 1.0} -->

We implemented the neural network architecture discussed in Section III in Tensorflow and fit human driver action distributions over a 1.5s time horizon conditioned on all available history up to prediction time, as well as the next 1.5s of the other driver's trajectory (i.e., a robot's candidate plan). Fig. 4 illustrates why we chose to design these action distributions as mixtures indexed by a discrete latent variable $\mathbf{z}$, where the component distributions are a combination of recurrent hidden state propagation and GMM sampling. All three models capture the same broad prediction: eventually, the human will cease accelerating. Comparing the left plot to the middle plot, the CVAE addition of a latent $\mathbf{z}$ manifests as modes predicting cessation on a few different time scales; this unsupervised clustering aids interpretability and slightly improves the performance metric of validation set negative log-likelihood.

<!-- chunk {"id": "body-0046", "role": "body", "section": "V-B Generative Model for Human Driver Actions", "weight": 1.0} -->

Comparing the right plot, of essentially a mixture of basic LSTM models, to the rest, we see that neglecting multimodality on the time step to time step scale prevents the prediction of sharp behavior (i.e., a human's foot quickly lifted off of the throttle).

<!-- chunk {"id": "body-0047", "role": "body", "section": "V-C Robot Policy Construction", "weight": 1.0} -->

We consider a discrete set of robot candidate futures over the 1.5s prediction horizon. We target a replanning rate of 0.3s and break the prediction horizon up into five 0.3s fixed action windows within which the robot may choose one of four longitudinal actions, ${\overset{¨}{s}}_{r} \in {{\{ 0,4,{- 3},{- 6}\}}\text{m/s}^{2}}$, and one of two lateral actions, moving towards either the left lane or the right lane.

<!-- chunk {"id": "body-0048", "role": "body", "section": "V-C Robot Policy Construction", "weight": 1.0} -->

Specifically, the robot control ${\overset{˙˙˙}{\tau}}_{r}$ is selected as the first 0.3s of the optimal control for the two point boundary value problem steering from $(\tau_{0},{\overset{˙}{\tau}}_{0},{\overset{¨}{\tau}}_{0})$, at the start of the window, to $(\tau_{\text{target}},0,0)$, at some free final time $t_{f}$ after the start of the window, with cost objective ${\int_{0}^{t_{f}}1} + {{{\overset{˙˙˙}{\tau}}_{r}^{2}/1000}dt}$. In total the robot has 8 possible actions per time window; given that actions in the first window are assumed fixed from the previous planning iteration this results in $8^{4} = 4096$ possible action sequences the robot may select.

<!-- chunk {"id": "body-0049", "role": "body", "section": "V-C Robot Policy Construction", "weight": 1.0} -->

These 4096 sequences are visualized in $(s,\tau)$ coordinates for a few initial robot states in Fig. 5.

<!-- chunk {"id": "body-0050", "role": "body", "section": "V-C Robot Policy Construction", "weight": 1.0} -->

Briefly, $J_{c}$ is a radial penalty past a near-collision threshold, $J_{a}$ is a quadratic control cost on longitudinal acceleration (lateral motion is free), $J_{l}$ is proportional to distance from target lane centerline ($\tau_{\text{goal}}$) with an urgency weight that increases as the robot nears the end of the road at $s = 0$, and $J_{d}$ incentivizes reaching states where $\Deltas$ is the same sign as $\Delta\overset{˙}{s}$, i.e., the two cars are moving apart from each other longitudinally. We use a discount factor $\gamma = 0.9$.

<!-- chunk {"id": "body-0051", "role": "body", "section": "V-C Robot Policy Construction", "weight": 1.0} -->

We draw 16 samples of human responses to each of the 4096 candidate robot action sequences and average their respective costs to approximate the expectation in problem. We select the top 32 sequences by this metric for further analysis, scoring 1024 sampled human trajectories each to gain a confident estimate (up to the model fidelity) of the true cost of pursuing that robot action sequence. This two-stage sampling and scoring process for our prediction model takes $\sim$`<!-- -->`{=html}0.25s parallelized on a single GTX 1080 Ti, simulating nearly 100 000 human responses in total. The robot action sequence with the lowest expected cost from the second stage is selected for enactment over the next action window. In particular, the second action window of the sequence is propagated next (as the first was already being propagated as the policy computation was running) and becomes the fixed first action window of the next search iteration.

<!-- chunk {"id": "body-0052", "role": "body", "section": "V-D Human-in-the-Loop Example Trials", "weight": 1.0} -->

This robot policy was integrated with the simulator, Fig. 1, enabling real-time human-in-the-loop validation of the robot action sequences it selects. As in the human-human input dataset, the intent of both parties is to switch lanes. Though, as noted in Section II-C, the desired behavior is qualitative and near-impossible to reliably quantify (especially human-in-the-loop), we highlight here some interesting emergent behaviors in robot reasoning. Fig. 6 illustrates an example of the robot's decision making at a single time step early in the interaction. The robot is aware of multiple possible actions the human might take, and even aware of how to elicit specific interaction modes, but chooses to wait in accordance with the sequence that minimizes its expected cost. Fig. 7 illustrates two examples where both the human and robot tried to be proactive in cutting in front of the other. When the human does not apply control actions early, the robot nudges towards the lane divider expecting the human to yield, showcased in the left figures.

<!-- chunk {"id": "body-0053", "role": "body", "section": "V-D Human-in-the-Loop Example Trials", "weight": 1.0} -->

The trial in the right figures starts out much the same, but the human's continued acceleration causes the robot to change its mind and brake to let the human pass. We note that the robot's cost function contains no explicit collaboration term, meaning it is essentially fending for itself while reasoning about relative likelihoods from its human action model. This is not unlike many drivers on the road today, but we note that our framework accommodates adjusting the robot cost but keeping the human model the same---friendlier behavior may be achieved through adding or changing cost terms.

<!-- chunk {"id": "body-0054", "role": "body", "section": "Conclusions", "weight": 1.0} -->

We have presented a robot policy construction framework for HRI that takes as input a dataset of human-human interaction trials, in order to learn an explicit, sampleable representation of human response behavior, and a cost function defined over a planning horizon, so that the desired robot behavior within the interaction model may be achieved through exhaustive action sequence evaluation applied in an MPC fashion. This framework makes no assumptions on human motivations nor does it rely on reasoning methods or features designed specifically for the traffic weaving scenario (other than the robot cost objective); it learns relative likelihoods of future human actions and responses at each time step from the raw state and action dataset. As such the robot is essentially blind to what it has not seen in the data---this framework is designed for probabilistic reasoning over relatively short time horizons in nominal operating conditions, but an important next step is to integrate it with lower-level emergency collision avoidance routines and higher-level inference algorithms, e.g., what if the human is not explicit in signaling its intent to change lanes? Another promising avenue of future research is to incorporate existing work in reasoning hierarchies into the human model learning architecture.

<!-- chunk {"id": "body-0055", "role": "body", "section": "Conclusions", "weight": 1.0} -->

Finally, our ultimate vision is to get this framework off the simulator and onto the road, where we may begin to benefit over alternative frameworks from our ability to incorporate additional learning features at will.
