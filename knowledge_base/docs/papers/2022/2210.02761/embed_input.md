<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Learning Autonomous Vehicle Safety Concepts from Demonstrations

Topics include Vehicles, Control barrier functions, Safety, Control, Learning, AV.

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Evaluating the safety of an autonomous vehicle (AV) depends on the behavior of surrounding agents which can be heavily influenced by factors such as environmental context and informally-defined driving etiquette. A key challenge is in determining a minimum set of assumptions on what constitutes reasonable foreseeable behaviors of other road users for the development of AV safety models and techniques. In this paper, we propose a data-driven AV safety design methodology that first learns ``reasonable'' behavioral assumptions from data, and then synthesizes an AV safety concept using these learned behavioral assumptions. We borrow techniques from control theory, namely high order control barrier functions and Hamilton-Jacobi reachability, to provide inductive bias to aid interpretability, verifiability, and tractability of our approach. In our experiments, we learn an AV safety concept using demonstrations collected from a highway traffic-weaving scenario, compare our learned concept to existing baselines, and showcase its efficacy in evaluating real-world driving logs.

<!-- chunk {"id": "body-0003", "role": "body", "section": "Introduction", "weight": 1.5} -->

As autonomous vehicle (AV) operations grow, developing appropriate methods for evaluating AV safety becomes ever more imperative. The question of "is a vehicle in an unsafe state?" is relevant for AV system developers, policymakers, and the general public alike (see Figure 1). While *guaranteeing* safety may not be practical in the face of the myriad uncertainties and complexities that come with real-world driving, there is still a broad desire to codify, to some extent, collectively agreed-upon notions of safety. Should safety be defined using data-driven methods that can account for the complexities of the AV's environment but lack interpretability and formal guarantees, or leverage control theoretic techniques derived from first principles which are interpretable and rigorous but not as scalable or expressive as their learned counterparts? In this work, we strike a middle-ground by a learning safety-critical driving behavior model and integrating it within a robust control framework to develop an interpretable and rigorous AV safety model that is informed by data.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

Towards this goal of building safe and trustworthy AVs, various stakeholders have advanced safety concepts consisting, in general, of two functions mapping world state (e.g., joint state of all agents and environmental context) to (i) a scalar measure of safety, and (ii) a set of allowable (safe) agent actions. Numerous uses of such safety concepts have been proposed throughout AV pipelines, e.g., a criterion to prune away unsafe plans, a safety monitor to determine when evasive action must be taken, a component in the planning objective, or for perception safety evaluation metrics. Critically, different behavioral assumptions lead to different safety concepts which in turn affects realized AV safety and performance. To mitigate overconservatism and enable maximum flexibility, we contend that the design of an effective safety concept hinges upon characterizing reasonable foreseeable behaviors of other agents, in a way conducive to efficiently evaluating the safety of driving scenes and producing associated safe controls.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

To address this challenge, we propose designing novel safety concepts by learning from data what are controls, specifically, control sets, that humans operate with when their safety is threatened, and then using these learned control sets to inform AVs of what are reasonable foreseeable behaviors of other agents in safety-critical scenarios. Equipped with such a learned "human behavior collision avoidance model," we perform safety concept synthesis by using robust control theory, specifically Hamilton-Jacobi reachability, as a powerful inductive bias for interpretability, verifiability, and tractability. Our control set learning approach differs from reward learning paradigms (i.e., inverse reinforcement learning / inverse optimal control ) which strive to learn high-level human intentions from demonstrations, often in the absence of constraints. Reward learning approaches aim to model a human's high-level planning objective which encapsulates more than just safety considerations. Whereas in this work, we are interested in learning control constraint boundaries associated with collision avoidance behaviors as opposed to nuanced behaviors (e.g., aggressive versus passive).

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

Structure and Contributions. We provide a literature review in Section II, give an overview on Hamilton-Jacobi (HJ) reachability in Section III, and formally state our safety concept learning problem in Section IV. Then we describe the details of our key contributions: (i) We propose a data-driven approach to learn humans' collision avoidance behaviors in the control space to capture "reasonable driving behaviors" (Section V). Specifically, we learn safe control sets from demonstrations via a high order control barrier function (HOCBF) framework. (ii) We develop a constrained game-theoretic optimization problem derived from a HJ reachability formulation to synthesize novel data-driven safety concepts that are robust to other agents' behaviors while respecting the learned collision avoidance behaviors (Section VI). (iii) We demonstrate our proposed learning framework using highway driving data and show that the resulting data-driven safety concept is less conservative than other common safety concepts (due to the way it captures constraints on reasonable agent behavior) and thus is useful as a "responsibility-aware" evaluation metric for the safety of AV interactions (Section VII).

<!-- chunk {"id": "body-0007", "role": "body", "section": "Safety Concept via Hamilton-Jacobi Reachability", "weight": 1.0} -->

We define a safety concept as a combination of two functions mapping world state to (i) a scalar measure of safety, and (ii) a set of allowable actions for each agent in which to preserve safety. A family of safety concepts can be described via a HJ reachability formulation.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Safety Concept via Hamilton-Jacobi Reachability", "weight": 1.0} -->

HJ reachability is a mathematical formalism used for characterizing the safety properties of dynamical systems. The outputs of a HJ reachability computation are (i) a HJ value function, a scalar-valued function that measures "distance" to collision, and (ii) a set of controls that prevents the safety measure from decreasing further---precisely the components needed for a safety concept.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Safety Concept via Hamilton-Jacobi Reachability", "weight": 1.0} -->

Consider a target set $\mathcal{T}$ which is the set of collision states between agents $A$ (ego agent) and $B$ (contender). The HJ reachability formulation describes a two-player differential game to determine whether it is possible for the ego agent to avoid entering $\mathcal{T}$ under any family of closed-loop policies of the contender, as well as the ego agent's appropriate control policy for ensuring safety. It is assumed that the contender follows an adversarial policy and has the advantage with respect to the information pattern.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Safety Concept via Hamilton-Jacobi Reachability", "weight": 1.0} -->

the available (bounded) controls^11^1The control sets $\mathcal{U}^{A}$ and $\mathcal{U}^{B}$ are typically chosen to reflect the physically feasible limits of the system.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Safety Concept via Hamilton-Jacobi Reachability", "weight": 1.0} -->

of agents $A$ and $B$, respectively, and $f{(\cdot, \cdot, \cdot)}$ is the joint dynamics assumed to be measurable in $u_{A}$ and $u_{B}$ for each $x$, and uniformly continuous, bounded, and Lipschitz continuous in $x$ for fixed $u_{A}$ and $u_{B}$.^22^2This assumption ensures that trajectories are generated by a unique control sequence. The boundary condition is defined by a function $\ell:{\mathcal{X}\rightarrow{\mathbb{R}}}$ whose zero sub-level set encodes the target set, i.e., $\mathcal{T} = {\{ x\mid{{\ell{(x)}} < 0}\}}$.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Safety Concept via Hamilton-Jacobi Reachability", "weight": 1.0} -->

Thus the HJ value function fulfills the first aspect of a safety concept. After obtaining the HJ value function, we can also consider the set of controls that prevent the HJ value function from decreasing over time. That is, we can compute the safety-preserving control set, ${\mathcal{U}_{safe}^{A}{(x)}} = {\{{u_{A} \in \mathcal{U}^{A}}\mid{{\min_{u_{B} \in \mathcal{U}^{B}}\frac{d\mathcal{V}{(x,t)}}{dt}} \geq 0}\}}$, thus fulfilling the second aspect of a safety concept. By varying the problem parameters, i.e., control sets, behavior type, and a choice of $\ell{(\cdot)}$, we can synthesize a family of safety concepts via HJ reachability.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Safety Concept via Hamilton-Jacobi Reachability", "weight": 1.0} -->

Although solving HJI PDE suffers from the curse of dimensionality, it is performed *offline*. For reasonably sized problems, such as the pairwise car-car system considered in the work, solving the HJI PDE is tractable on modern computers. Equipped with the HJ value function and a state $x$, computing $\mathcal{V}{(x,t)}$ and $\mathcal{U}_{safe}^{A}{(x)}$ is computationally lightweight, consisting of a table look-up, interpolation and/or matrix-vector multiplication.

<!-- chunk {"id": "body-0014", "role": "body", "section": "Towards Data-driven Safety Concept Synthesis", "weight": 1.0} -->

A key limitation to the standard HJ reachability setup is in the assumption the contender will choose optimal collision-seeking controls from $\mathcal{U}^{B}$, the set of admissible controls of the system (typically corresponding to the system's physical limits). While a worst-case assumption is key in providing robustness guarantees for the safety of the system, the assumption that a contender agent will execute any available, including worst-case, controls is unrealistic in practice.

<!-- chunk {"id": "body-0015", "role": "body", "section": "Towards Data-driven Safety Concept Synthesis", "weight": 1.0} -->

To reduce the conservatism in how we model a contender's behavior within the HJ formulation (and hence resulting safety concept), we aim to use data to learn state-dependent control sets to capture agent behaviors reflecting practical real-world operations. That is, the problem we seek to solve consists of two parts: (i) learning state-dependent control sets from data, and (ii) integration of the state-dependent control sets into the HJ reachability formulation for safety concept synthesis. Building upon the notation introduced in Section III, consider a nonlinear control-disturbance-affine^33^3Many vehicle dynamics models can be written as a control-affine system.

<!-- chunk {"id": "body-0016", "role": "body", "section": "Towards Data-driven Safety Concept Synthesis", "weight": 1.0} -->

Learning state-dependent control sets. Consider an offline dataset $\mathcal{S} = {\{{(x^{(i)},u_{A}^{(i)})}\}}_{i = 1}^{N}$ of joint states between agent $A$ and $B$, and agent $A$'s controls collected from safe interactions between agents $A$ and $B$. We assume agent $A$ does not observe the controls of agent $B$. We seek to find a mapping $\phi:{\mathcal{X}\rightarrow 2^{\mathcal{U}^{A}}}$ such that $u_{A}^{(i)} \in {\phi{(x^{(i)})}}$ for all ${(x^{(i)},u_{A}^{(i)})} \in \mathcal{S}$.

<!-- chunk {"id": "body-0017", "role": "body", "section": "Towards Data-driven Safety Concept Synthesis", "weight": 1.0} -->

Of course $\phi$ can be a trivial mapping, i.e., ${\phi{(x^{(i)})}} = \mathcal{U}^{A}$ for all $x \in \mathcal{X}$; thus we additionally require the learned state-dependent sets to be minimal in the sense that the set should contain the relevant points as tightly as possible.

<!-- chunk {"id": "body-0018", "role": "body", "section": "Towards Data-driven Safety Concept Synthesis", "weight": 1.0} -->

Safety concept synthesis. Equipped with $\phi$, we seek to integrate the learned control sets into the HJ reachability framework to restrict the feasible control set that an agent will operate.

<!-- chunk {"id": "body-0019", "role": "body", "section": "Learning State-Dependent Control Sets From Data", "weight": 1.0} -->

In this section, we describe our proposed approach to describing human collision avoidance behaviors by learning state-dependent control sets from data. First we give a self-contained overview to HOCBFs (Section V-A), then followed by our proposed learning procedure (Section V-B).

<!-- chunk {"id": "body-0020", "role": "body", "section": "V-A High-Order Control Barrier Functions", "weight": 1.0} -->

HOCBF provides a method to represent and reason about control invariant sets \[13, Theorem 4\]. Before introducing HOCBFs, we first introduce control barrier functions (CBFs), a special case of HOCBFs. Consider a control-affine system of the form, where $f:{\mathcal{X}\rightarrow{\mathbb{R}}^{n}}$ and $g:{\mathcal{X}\rightarrow{\mathbb{R}}^{m_{A}}}$ are locally Lipschitz continuous. Suppose there is a set which the system wants to stay inside of (e.g., set of safe states). A control invariant set is a set of states for which it is possible for a system to stay inside of indefinitely. In many settings, it is often desirable to find the largest control invariant set that is contained within the safe set.

<!-- chunk {"id": "body-0021", "role": "body", "section": "V-B State-dependent Control Set Learning Procedure", "weight": 1.0} -->

In this section, we detail our state-dependent control set learning procedure. Roughly, we use HOCBF as inductive bias in learning a mapping from state to control set.

<!-- chunk {"id": "body-0022", "role": "body", "section": "V-B1 Learning set-up and assumptions", "weight": 1.0} -->

We make the assumption that (safe and reasonable) drivers do not put themselves in situations where it is not possible for them to avoid a collision. That is, drivers execute controls that ensure they continually stay inside a "safe set" because leaving that set may lead to collision. For example, (typical) safe drivers avoid approaching obstacles at high speeds because they may not be able to steer and slow down to avoid the obstacle. This so-called "safe-set" is precisely a control invariant set (see Definition 1. ‣ V-A High-Order Control Barrier Functions ‣ V Learning State-Dependent Control Sets From Data ‣ Learning Autonomous Vehicle Safety Concepts from Demonstrations")). Thus, given a dataset of safe collision-free trajectories, the goal is to learn a control invariant set and corresponding control sets that contain the observed samples. We represent the control invariant set using HOCBFs \[13, Theorem 4\] which provides inductive bias that help make the learning process tractable and a direct and interpretable way to obtain state-dependent control sets (see (6.

<!-- chunk {"id": "body-0023", "role": "body", "section": "V-B1 Learning set-up and assumptions", "weight": 1.0} -->

‣ V-A High-Order Control Barrier Functions ‣ V Learning State-Dependent Control Sets From Data ‣ Learning Autonomous Vehicle Safety Concepts from Demonstrations"))) amenable for safety concept synthesis.

<!-- chunk {"id": "body-0024", "role": "body", "section": "V-B1 Learning set-up and assumptions", "weight": 1.0} -->

For collision avoidance, agents are aiming to avoid the same obstacle set but only differ in how they avoid it. Thus we use HOCBFs to avoid reasoning about obstacle sets in velocity states (or higher derivatives) which is difficult to construct, and instead reason about $\alpha_{i}$'s.

<!-- chunk {"id": "body-0025", "role": "body", "section": "V-B3 HOCBF learning algorithm", "weight": 1.0} -->

Next, we present our HOCBF learning algorithm whereby we aim to learn the parameters for $\alpha_{i}$ from data. Let $\mathcal{S} = {\{{(x^{(i)},u^{(i)})}\}}_{i = 1}^{N}$ be a dataset containing states and controls collected from humans operating in the target environment exhibiting safe collision avoidance behaviors. Since negative examples are rare and their explicit collection is impractical, one of the key strengths of our method is its ability to learn control invariant sets from just positive examples. A;though our method can also consider negative examples if available.

<!-- chunk {"id": "body-0026", "role": "body", "section": "V-B3 HOCBF learning algorithm", "weight": 1.0} -->

Suppose we have dynamics given. Let $\mathcal{C}$ describe the set of obstacle states in position space (we consider ${\mathbb{R}}^{2}$ but this analysis can extend to ${\mathbb{R}}^{3}$). Let $b:{\mathcal{X}\rightarrow{\mathbb{R}}}$ be a function where ${{b{(x)}} \leq 0}\Leftrightarrow{{{pos}{(x)}} \in \mathcal{C}}$, and ${pos}:{\mathcal{X}\rightarrow{\mathbb{R}}^{2}}$ is a function that extracts the position states. Let $m_{r} \geq 1$ be the relative degree of and $b$.

<!-- chunk {"id": "body-0027", "role": "body", "section": "V-B3 HOCBF learning algorithm", "weight": 1.0} -->

‣ V-A High-Order Control Barrier Functions ‣ V Learning State-Dependent Control Sets From Data ‣ Learning Autonomous Vehicle Safety Concepts from Demonstrations")) being true for all datapoints, (ii) we want the HOCBF control constraint (6.

<!-- chunk {"id": "body-0028", "role": "body", "section": "V-B3 HOCBF learning algorithm", "weight": 1.0} -->

‣ V-A High-Order Control Barrier Functions ‣ V Learning State-Dependent Control Sets From Data ‣ Learning Autonomous Vehicle Safety Concepts from Demonstrations")) to be satisfied, (iii) the states should be inside the (safe) control invariant set, and (iv) the dataset could contain outliers or noise, we seek to find $\mathbf{p}^{\star}$ such that, where $G_{x}^{j} = {\mathcal{L}_{g}\mathcal{L}_{f}^{m_{r} - 1}b{(x^{(j)})}}$, ${F_{x}^{j}{(\mathbf{p})}} = {{\mathcal{L}_{f}^{m_{r}}b{(x^{(j)})}} + {\mathcal{O}{({b{(x^{(j)})}};\mathbf{p})}} +

<!-- chunk {"id": "body-0029", "role": "body", "section": "V-B3 HOCBF learning algorithm", "weight": 1.0} -->

‣ V-A High-Order Control Barrier Functions ‣ V Learning State-Dependent Control Sets From Data ‣ Learning Autonomous Vehicle Safety Concepts from Demonstrations"))). We highlight some important considerations for this optimization problem.

<!-- chunk {"id": "body-0030", "role": "body", "section": "V-B3 HOCBF learning algorithm", "weight": 1.0} -->

Saturation: We apply $\tanh$ on the second and fourth terms in because while we desire all the data points to satisfy the HOCBF conditions, we are not too interested in how much each data point satisfies them. That is, we want to reduce the influence of extremely safe points (e.g., states very far and moving away from the obstacle).

<!-- chunk {"id": "body-0031", "role": "body", "section": "V-B3 HOCBF learning algorithm", "weight": 1.0} -->

Parameterization: The ${{\alpha_{i},i} = 1},{\ldots,m_{r}}$ functions must belong to extended class $\mathcal{K}_{\infty}$. As such, we can parameterize $\alpha_{i}$ as a linear combination of extended class $\mathcal{K}_{\infty}$ basis functions. In future work, we can consider using a monotonic neural network.

<!-- chunk {"id": "body-0032", "role": "body", "section": "V-B3 HOCBF learning algorithm", "weight": 1.0} -->

Pairwise joint dynamics: In the case with pairwise joint dynamics, as presented, there is an additional term corresponding to the contender's input (i.e., a disturbance term), and ultimately, it will show up. In particular, the HOCBF constraint becomes which is affine in $u_{A}$ and $u_{B}$. To select a value for $u_{B}$, depending on what information is available, we could either (i) use the ground truth value, (ii) assume the worst-case, or (iii) predict a distribution over agent $B$'s controls and take the worst-case with respect to the predictions.

<!-- chunk {"id": "body-0033", "role": "body", "section": "V-B3 HOCBF learning algorithm", "weight": 1.0} -->

Differentiability: If the dynamics and $b$ are differentiable, then can be optimized via standard gradient descent algorithms. In this work, we use JAX, a Python software library for automatic differentiation.

<!-- chunk {"id": "body-0034", "role": "body", "section": "V-B3 HOCBF learning algorithm", "weight": 1.0} -->

Negative examples: If negative examples are available (e.g., from real-world driving logs or synthetically generated ), we can include additional terms to that encourage the negative examples to violate the control constraint and have negative effective CBF values. The negative examples will help refine the delineation of the control invariant set.

<!-- chunk {"id": "body-0035", "role": "body", "section": "Safety Concept Synthesis via Constrained HJ Reachability", "weight": 1.0} -->

We incorporate the learned HOCBF into the HJ reachability formulation to synthesize a safety concept that assumes reasonable human behaviors in safety-critical situations. Directly adding the learned HOCBF control constraint to places the burden of constraint satisfaction on the agent that acts second (i.e., agent $B$), thus imposing a strong assumption that the other (uncontrolled) agents will always behave responsibly with respect to HOCBF constraint satisfaction. To address this, we swap the ordering in which the agents act, and the following proposition states that this swapping results in a more conservative HJ value function, i.e., it is more advantageous for a player to act first.

<!-- chunk {"id": "body-0036", "role": "body", "section": "Experiments and Discussion", "weight": 1.0} -->

We present two examples, a simple static obstacle collision avoidance example to aid understanding of our method, and a highway driving scenario studied in to illustrate the synthesis of a data-driven safety concept for AV applications. We note that our method can be applied to other settings, such as car-pedestrian interactions, and social navigation. We plan on releasing our code upon publication.

<!-- chunk {"id": "body-0037", "role": "body", "section": "VII-A Collision avoidance with circular obstacle", "weight": 1.0} -->

We continue with the example discussed in Section V-B. Consider a 4-state simple car model, with $(\delta,a)$ as steering and acceleration control inputs, and $\ell$ is the wheelbase length of the car. For the HOCBF learning, we use the following parametric form ${\alpha_{i}^{p_{i}}{(a)}} = {p_{i,1}a^{p_{i,2}}}$, ${p_{1} = {\lbrack 0.54,1.16\rbrack}},{p_{2} = {\lbrack 0.68,1.11\rbrack}}$ to generate a set of trajectories with various random initial conditions. The parameter values serves as the ground truth (GT).

<!-- chunk {"id": "body-0038", "role": "body", "section": "VII-A Collision avoidance with circular obstacle", "weight": 1.0} -->

When learning the parameters of $\alpha$ (i.e., performing gradient descent on ), we used $\beta_{1} = 1$, $\beta_{2} = \beta_{4} = 0.001$, $\beta_{3} = 1$, $\beta_{5} = 0.001$, step size / learning rate = $0.001$, and 150000 gradient steps (though it converged much earlier). Figure 3 visualizes the zero level set of the learned effective CBF (left) and resulting trajectory from running the same reach-avoid planner used to generate the dataset but with the different learned $\alpha_{i}$ parameterizations (right). We see that the learned HOCBFs except the cubic parameterization is able to closely recover the ground truth behavior (black line).

<!-- chunk {"id": "body-0039", "role": "body", "section": "VII-B Highway driving", "weight": 1.0} -->

In this example, we consider a highway driving scenario, synthesize a novel safety concept based on a highway driving dataset, and evaluate on real traffic data.

<!-- chunk {"id": "body-0040", "role": "body", "section": "VII-B1 Data collection", "weight": 1.0} -->

We use the traffic-weaving dataset, and assume the control inputs of the other cars are not observable (this is often true in real-world settings). Instead, we learn a generative model to construct distributions over likely contender controls (i.e., disturbances) and use them as ground truth for our HOCBF learning procedure. We trained a conditional variational autoencoder with a continuous latent space (latent dimension size of 8) with a history length of ten time steps, and prediction horizon of five. Although we predict five time steps into the future, we only consider the first (i.e., current) control of the other agent. We used LSTM cells for the encoder and decoder with hidden dimension 8. Given the prediction, we define $\mathcal{D}_{pred}$ as the interval three standard deviations away from the mean, and then compute $u_{B} \in \mathcal{D}_{pred}$ that minimizes the LHS of during the HOCBF learning process. Figure 4 shows an example which compares the learned distribution, three standard deviation bound, the ground truth, and control limits.

<!-- chunk {"id": "body-0041", "role": "body", "section": "VII-B1 Data collection", "weight": 1.0} -->

(a) Zero level-set of HJ value function evaluated at Δ x − Δ y slice. vA = 18ms-1, vB = 25ms-1, θA = θB = 0rad.

<!-- chunk {"id": "body-0042", "role": "body", "section": "VII-B1 Data collection", "weight": 1.0} -->

(b) HOCBF-HJ and WC-HJ optimal controls for agents A and B when agent B is approaching from behind.

<!-- chunk {"id": "body-0043", "role": "body", "section": "VII-B2 Safety concept analysis", "weight": 1.0} -->

We consider a HOCBF ${b{(x)}} = {{\frac{\Deltax^{2}}{a^{2}} + \frac{\Deltay^{2}}{b^{2}}} - 1}$, ${a = 5.4},{b = 2.4}$, and consider relative dynamics between two vehicles modeled by the simple car model, resulting in a relative degree of two. We applied the learning procedure outlined in Section V-B; we performed a hyperparameter sweep over the following parameters defined. The values are presented in Table I, and the bolded values are the hyperparameters that we found yielded the best results.

<!-- chunk {"id": "body-0044", "role": "body", "section": "VII-B2 Safety concept analysis", "weight": 1.0} -->

With our learned HOCBF, we then solved the corresponding HOCBF constrained HJ reachability problem described. As our problem is relatively low-dimensional, we can solve the constrained HJ reachability problem exactly by enumerating over the vertices of the feasible domain (but adds significant computational costs). We consider a two second horizon when solving the constrained HOCBF-HJ reachability problem and compare against various safety concepts (also synthesized via a HJ computation).

<!-- chunk {"id": "body-0045", "role": "body", "section": "VII-B3 Offline evaluation on real traffic data", "weight": 1.0} -->

We evaluate how various safety concepts perform ex post facto on the NGSIM dataset, a highway driving dataset containing vehicles traveling along the US 101 highway in Los Angeles, USA. There are no collisions observed, and therefore we expect all the datapoints to be considered "safe". Table III presents the mean and various percentile values of the HJ value of each safety concept. While it is difficult to definitively say that a particular safety concept is better than another based on these statistics since there are a lot of nuances in the interpreting the HJ value, we make the following observations: (i) The Brake safety concept presents the highest values in all the statistics, indicating that it is the most optimistic out of the safety concepts studied. Being overly-optimistic can lead to over-confident driving where the AV can over-estimate how safe a situation is. (ii) For situations when the HJ value is low (i.e., for low percentiles), both the HOCBF-HJ and WC-HJ safety concept present very similar statistics, but the HOCBF-HJ statistics gradually become more similar to the Constant statistics as we consider higher percentile values.

<!-- chunk {"id": "body-0046", "role": "body", "section": "VII-B3 Offline evaluation on real traffic data", "weight": 1.0} -->

This suggests that (perhaps not too surprisingly) HOCBF-HJ behaves like a hybrid between the WC-HJ and Constant safety concepts.

<!-- chunk {"id": "body-0047", "role": "body", "section": "Limitations, Future Work, and Conclusions", "weight": 1.5} -->

We conclude by highlighting some limitations of this work, laying out exciting future directions, and summarizing our key contributions.

<!-- chunk {"id": "body-0048", "role": "body", "section": "VIII-A Limitations", "weight": 1.0} -->

A major limitation of this work stems from (i) the curse of dimensionality in solving the HJI PDE explicitly (as opposed to implicit representations ), and (ii) multi-agent extensions to the HOCBF and HJ reachability theory. Although we are currently using pairwise decomposition when considering multi-agent scenarios, pairwise decomposition for multi-agent analysis is effective in practice, and in some settings, multi-agent analysis reduces to a pairwise decomposition. While the eventual goal is to investigate using implicit representation (e..g, neural networks) when solving the HJI PDE to account for high dimensional scenarios, the (HO)CBF and HJ reachability formulation nonetheless provides useful inductive biases in building responsibility-aware safety concepts.

<!-- chunk {"id": "body-0049", "role": "body", "section": "VIII-A Limitations", "weight": 1.0} -->

Our HOCBF-constrained safety concepts does run the risk of encountering behaviors not abiding by the HOCBF constraint and therefore invalidating assurances provided by the synthesized safety concept. While we can further improve the behavior learning step to help reduce model mismatch, there has been complementary work in out-of-distribution (OOD) detection to catch anomalous events. Such OOD detectors are designed to be used as a complementary safety filter and catch rare tail events that are not nominally considered by the system.

<!-- chunk {"id": "body-0050", "role": "body", "section": "VIII-B Future work", "weight": 1.0} -->

An area primed for future work is in investigating the division of responsibility for the constraint satisfaction of. A similar consideration is studied in which analyzes how much each agent should contribute to constraint satisfaction in a multi-agent setting. Fruitful future work entails learning appropriate responsibility allocation within a game theoretic context, and combining offline safety concept synthesis with online responsibility learning.

<!-- chunk {"id": "body-0051", "role": "body", "section": "VIII-C Conclusions", "weight": 1.0} -->

We have proposed a data-driven safety concept that is robust yet reflective of real-world driving interaction behaviors. We first learn control sets describing collision avoidance behaviors by leveraging high order control barrier functions, and then use them to constrain the HJ reachability computation used for safety concept synthesis. We show that our learned safety concept is less overly-conservative than other common AV safety concepts, and captures responsible behaviors, though there is more work to be done in testing safety concepts in closed-loop AV operations, and extensions to multi-agent interactive scenarios, especially where the division of responsibility for collision avoidance is ambiguous.
