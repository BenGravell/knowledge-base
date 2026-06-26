<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Do What I Want, Not What I Did: Imitation of Skills by Planning Sequences of Actions

Topics include Motion planning, Robotics, Sampling-based methods, Planning, Learning, Sampling.

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

We propose a learning-from-demonstration approach for grounding actions from expert data and an algorithm for using these actions to perform a task in new environments. Our approach is based on an application of sampling-based motion planning to search through the tree of discrete, high-level actions constructed from a symbolic representation of a task. Recursive sampling-based planning is used to explore the space of possible continuous-space instantiations of these actions. We demonstrate the utility of our approach with a magnetic structure assembly task, showing that the robot can intelligently select a sequence of actions in different parts of the workspace and in the presence of obstacles. This approach can better adapt to new environments by selecting the correct high-level actions for the particular environment while taking human preferences into account.

<!-- chunk {"id": "body-0003", "role": "body", "section": "Introduction", "weight": 1.5} -->

Learning from demonstration has emerged as a useful paradigm to teach robots the skills they need to interact with the real world. The challenge in learning from demonstration is to generalize what is learned to new contexts and new tasks. Consider a moderately complex task such as assembling part of a structure, shown in Fig. 1 and defined by the PDDL in Fig. 3. The precise movements and the particular movement goals and parameters will vary from one situation to the next. When attempting to execute this task in a new environment, the robot must be able to select the particular actions, motions, and manipulation goals that will allow completion of the task in this new environment. By exploiting learned models for actions, we are able to demonstrate a planner that is able to produce solutions for performing tasks in an effective manner, is able to improve with additional demonstration data, and can adapt to new circumstances.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

Adapting to new environments in the context of task and motion planning poses several challenges when attempting to generalize learned actions. Recently there has been significant progress in integrating symbolic task planning and continuous motion planning, which have in the past evolved as two separate fields. At the same time, learning from demonstration has been established as a powerful tool for learning models of individual actions. Learning from demonstration has previously been connected to symbolic task planning, but these approaches are yet to be incorporated in the context of a motion-constrained task planning in a principled manner. This paper aims to address this gap.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

In our approach, probabilistic models over features associated with each action are learned from human demonstrations and later refined in a supervised manner using additional robot-generated examples scored by a human teacher. At the core of this approach lies a mapping from symbolic actions (e.g. approach, grasp) to physical motions encoded probabilistically as a distribution over observed features along each motion trajectory. Fig. 2 shows this relationship: multiple demonstrations connect predicate states, which allow us to learn a model of each action. Features $x$ are defined as a set of functional relations between the robot and its environment (e.g. relative position and orientation between robot end-effector and desired object to grasp).

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

Planning in a new environment is accomplished by updating each action distribution to remain as close as possible to the prior while satisfying new environment constraints such as different obstacles and object shapes. This is accomplished through importance sampling and optimal distribution re-estimation using the cross-entropy method. Transitions from symbolic states to actions are similarly encoded as a discrete probability distribution representing the "preference" of executing different actions. A product model is induced over a complete task from the sequence of probabilistic action models, together with discrete transition models. Planning a complete task then corresponds to optimally updating this model to reproduce the prior and satisfy the new scenario.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

(define (domain structure-assembly) (:requirements:typing:adl) (:types link node grasp-pt) (near ?x - link) (near-grasp ?g - grasp-pt) (in-hand ?x - link) (standing ?x - link) (aligned ?x - link ?y - node) (grasp-for ?x - link ?g - grasp-pt) (grasp-for ?y - node ?g - grasp-pt) (attached ?x - link ?y - node) (define (problem build-simple-structure) link1 - link link2 - link node1 - node node2 - node (:goal (exists (?x - link ?y - node) (attached ?x ?y)))) Figure 3: Partial PDDL domain and problem definition for the structure assembly task. The domain can be thought of as a version of the basic blocks world task, where the goal is to latch two pieces together.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Introduction", "weight": 1.5} -->

The contributions of this paper are: a new method for reproducing demonstrated actions in novel environments, derived from sampling-based motion planning; an algorithm for combining these learned actions for executing multi-step tasks with multiple valid plans; and experimental validation of this algorithm on a simple assembly task as shown in Fig. 1. Experiments in a 2D Android game domain were omitted for reasons of space.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Task Description", "weight": 1.0} -->

We assume existence of a symbolic description of a task, and labeled training data associating features with each low-level action that can appear in this domain. The symbolic description naturally decomposes the task into a sequence of predicate world states $w_{0},w_{1},\ldots,w_{g}$ For the structure assembly task, part of the symbolic description is shown in Fig. 3. A world state $w$ is then defined as a combination of predicates. In turn, actions $a$ are the connections between these predicate states as shown in Fig. 2. Each $a$ in a given task is represented as a probability distribution over a set of features associated with a successful instantiation of a skill in a new environment given $w$.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Task Description", "weight": 1.0} -->

The features are denoted by $x \in {\mathbb{R}}^{n}$ and defined using the function $\phi$ through relationship ${x = {\phi{(t,s,u)}}},$ where $t \in {\lbrack t_{0},t_{f}\rbrack}$ denotes time in the action starting at $t_{0}$ and ending at $t_{f}$, $s \in S$ is the robot state, and $u \in U$ are the applied controls. With these definitions, a probabilistic model associated to each action $a$ is denoted by $p_{d}{(\left. x \middle| a \right.)}$ and is computed using unsupervised learning from expert demonstrations, typically assuming a parametric density $p_{d}$. A joint model of a task $T$ consisting of multiple actions can be constructed using a density ${p_{d}{(\left. x \middle| T \right.)}} \propto {p_{d}{(\left.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Task Description", "weight": 1.0} -->

x \middle| a_{0} \right.)}\cdotsp_{d}{(\left. x \middle| a_{n_{T}} \right.)}}$ assuming conditional independence between actions.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Task Description", "weight": 1.0} -->

Specific features are derived from the PDDL description of the task. For example, in Fig. 3, the approach action describes the arm moving to pick up a link object without knocking it over. In this case $x = {\phi{(t,s,u)}}$ would return the relative position, orientation, and velocity between the robot end effector and the link object. To use the proposed method, one would provide the identifier for an action and a list of associated symbols from perception.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Task Description", "weight": 1.0} -->

An optimal task $T^{\ast}$ is a sequence of actions $T^{\ast} = {\{ a_{i}\}}_{i = 1}^{N}$ that takes the robot from the initial state $w_{0}$ to goal $w_{g}$ that have the highest probability given our expert model, while also avoiding hard constraints such as collisions and joint limits: Our goal is to learn a stochastic "symbolic" policy $\pi{(\left. a \middle| w \right.)}$ over the sequence of predicate states, as well as continuous-space "physical" policy $p{(\left. u \middle| {s,\xi_{a}} \right.)}$ generating trajectories for each action $a$. We represent trajectories using parameters $\xi \in \mathcal{Z}$, where $\mathcal{Z}$ represents the space of all possible parameters resulting in valid trajectories in the new environment. Since robot perception and motion are uncertain, each parameter induces a density $p{(\left.

<!-- chunk {"id": "body-0014", "role": "body", "section": "Task Description", "weight": 1.0} -->

\tau \middle| \xi \right.)}$ where denotes the system trajectory. For instance, $\xi$ would typically define a reference trajectory and an associated tracking control law resulting in the density In practice, given $\xi$ the trajectory $\tau$ will either be sampled using a high-fidelity simulator or generated by the real robot.

<!-- chunk {"id": "body-0015", "role": "body", "section": "IV-A Local Planning Algorithm", "weight": 1.0} -->

First, we consider adaptation of only a single action $a$ to a new environment. When presented with a new environment, we pose the planning task as the problem of learning a new parameterized policy $\xi^{\ast}$. To do so we employ a stochastic optimization technique using a surrogate distribution $\xi \sim \pi{( \cdot |v)}$ which is iteratively updated so that generated trajectories $\tau$ produce feature observations $x$ with high likelihoods under the expert distribution $p_{d}{(\left. x \middle| a \right.)}$ for action $a \in {A{(w)}}$, where $A{(w)}$ is the set of actions available from predicate state $w$.

<!-- chunk {"id": "body-0016", "role": "body", "section": "IV-A Local Planning Algorithm", "weight": 1.0} -->

We follow the Cross Entropy Method described by Rubinstein et al., particularly following its application to motion planning by Kobilarov. This is accomplished by introducing an artificial *surrogate* distribution over $\mathcal{V}$ that will induce a distribution over trajectories $\tau$ and over the corresponding features $x$ along these trajectories. The surrogate will then be iteratively optimized until it becomes optimally close (in a distribution sense) to the expert density $p_{d}{(\left. x \middle| a \right.)}$ without violating the constraints of the environment such as obstacles and joint limits. The surrogate model is built using a parametric density $\pi{(\left. \xi \middle| v \right.)}$ such as a multivariate Gaussian or a GMM with parameters $v$.

<!-- chunk {"id": "body-0017", "role": "body", "section": "IV-A Local Planning Algorithm", "weight": 1.0} -->

Assuming that a nominal (prior) parameter $v_{0}$ is known the problem can be formalized as the optimal estimation of the expectation The optimal importance sampling density for estimating this integral is where the numerator in can be thought of as the correlation between the expert feature distribution $p_{d}{(\cdot |a)}$ and the parameterized distribution $p{(\cdot |v_{0})}$. Unfortunately we cannot compute the solution to as it involves computing the estimator $l$. Instead, we approximate this optimal $q^{\ast}$ by finding the appropriate parameters $v$ of $p{(\left. x \middle| v \right.)}$. A logical way of doing this is to minimize the Kullback-Leibler (KL) divergence: To find the value of $v$ that minimizes this expression, we approximate this solution by drawing $M$ i.i.d. samples $\xi_{1},\ldots,\xi_{M}$ from $v_{0}$.

<!-- chunk {"id": "body-0018", "role": "body", "section": "IV-A Local Planning Algorithm", "weight": 1.0} -->

This can be more formally expressed as If we assume that there is a bijection between a tuple $\left\langle t,s,u \right\rangle$ along a trajectory $\tau$ and a feature $x \in {\phi{(\tau)}}$ then we have the following approximation since $\xi_{j}$ were sampled under $v_{0}$, and substituting into results: The necessary conditions for a minimum correspond to setting the gradient of to zero, i.e. by solving the equality: where the weights $z_{i,j}$ are given by $z_{i,j} \triangleq {p_{d}{(x_{i,j})}}$.

<!-- chunk {"id": "body-0019", "role": "body", "section": "IV-A Local Planning Algorithm", "weight": 1.0} -->

When $\pi{(\cdot |v)} = \mathcal{N}{(\cdot |\mu,\Sigma)}|_{\mathcal{V}}$ (i.e. a single multivariate Gaussian with domain restricted to feasible parameter set $\mathcal{Z}$), the relationship can be solved in closed form as where $z_{j} = {\sum_{i = 0}^{N}z_{i,j}}$ and ${\overline{z}}_{j} = {z_{j}/{\sum_{j = 1}^{M}z_{j}}}$. When $\pi{(\cdot |v)}$ is a GMM the minimization from Eq. is performed using a weighted expectation maximization (EM) algorithm.

<!-- chunk {"id": "body-0020", "role": "body", "section": "IV-A Local Planning Algorithm", "weight": 1.0} -->

In practice, the optimal parameter $v$ is computed iteratively starting with some nominal choice $v_{0}$ which approximately covers the trajectory space of interest. At each iteration we draw $M$ samples $\xi_{j} \sim \pi{( \cdot |v_{0})},j \in 1,\ldots,M$ and compute the next $v$ by minimizing. At the next iteration $v_{0}$ is set to $v$ and the process continues until the cost converges.

<!-- chunk {"id": "body-0021", "role": "body", "section": "IV-A Local Planning Algorithm", "weight": 1.0} -->

We add a fixed normalization term to the diagonal entries in $\Sigma$ of $p_{d}$ and of $\pi{( \cdot |v)}$ to make sure covariances stay well-defined. In addition, to prevent premature convergence, we introduce an extra parameter $0 < \alpha < 1$, which controls the size of steps taken at each iteration.

<!-- chunk {"id": "body-0022", "role": "body", "section": "Avoiding Obstacles and Joint Limits", "weight": 1.0} -->

We constrain $\mathcal{Z}$ to consist only of the space of valid trajectories, removing any samples that would collide with objects or pass joint limits. This means that when drawing our $M$ samples, we remove samples currently in collision or past joint limits in our new environment and continue to draw sample trajectories until we have all $M$ valid examples. This works effectively in practice as long as the task does not require generalization in environments with very narrow passages that the system has never been trained. Such cases are extremely difficult since the probability of obtaining samples in the narrow passage is close to zero, unless an informative nominal density parameter $v_{0}$ is used with enough probability mass over such regions.

<!-- chunk {"id": "body-0023", "role": "body", "section": "IV-B Task Planning Algorithm", "weight": 1.0} -->

We wish to optimize parameters for all possible actions in a successful execution of the task, where our cost is the joint probability over any sequence of actions that represent a valid execution of the task as per Eq.. Our task planning approach takes the algorithm described in Section IV-A and expands it into a recursive algorithm similar to Monte Carlo Tree Search.

<!-- chunk {"id": "body-0024", "role": "body", "section": "IV-B Task Planning Algorithm", "weight": 1.0} -->

First, consider the problem of choosing one of $N_{A{(w)}}$ possible actions. We think of this as the choice of which action would be most similar to our expert's demonstrations in other scenes, starting in symbolic state $w$. We expand our notion of $p_{d}{(x)}$ to include the switch between each possible action as ${p_{d}{(x)}} = {p_{d}{(\left. a_{i} \middle| w \right.)}p_{d}{(\left. x_{i,j} \middle| a_{i} \right.)}}$. Substituting this into Eq. gives us: where $v_{a_{i}}$ is the trajectory distribution associated with $a_{i}$.

<!-- chunk {"id": "body-0025", "role": "body", "section": "IV-B Task Planning Algorithm", "weight": 1.0} -->

Action selection is modeled as a stochastic policy over possible worlds. We introduce a surrogate distribution into our trajectory search that captures the probability of choosing each future action from the current $w$. When sampling trajectories, we draw the next action $a \sim \pi{( \cdot |w)}$ according to this probability.

<!-- chunk {"id": "body-0026", "role": "body", "section": "IV-B Task Planning Algorithm", "weight": 1.0} -->

Furthermore, we can extend this reasoning to consider which of a whole tree of possible actions is the most similar to an expert tree, allowing us to capture expert preferences for particular actions in addition to continuous-space trajectories. Assuming that all actions in a branch of the tree are independent given time, we can define the expert probability of a particular action starting at continuous robot state $s_{0}$: Where $s_{N,j}$ is the final state in sampled trajectory $\tau_{j}$ and $w$ represents the world after symbolic action $a$. Eq. describes the probability of all possible actions from a continuous world state $s$ occurring after execution of an action $a$.

<!-- chunk {"id": "body-0027", "role": "body", "section": "IV-B Task Planning Algorithm", "weight": 1.0} -->

When recording a set of $N_{w}$ demonstrations starting in the same predicate state $w$, we compute the conditional probability for action $a \in {A{(w)}}$: We specify a surrogate distribution over possible choices of actions for a world $w$ given as $p{(\left. a \middle| w \right.)}$. This probability is initialized as ${\pi{(\left. a \middle| w \right.)}} = \frac{1}{N_{A{(w)}}}$. In the case where $H = 0$ this is updated as ${\pi{(\left. a \middle| w \right.)}} \propto {\frac{1}{M}{\sum_{j}^{M}z_{j}}}$ where $M$ trajectory samples $\tau$ have been drawn from $a$. Otherwise we compute this as: for starting state $s_{0} \in S_{0}$ and action $a \in {A{(w)}}$.

<!-- chunk {"id": "body-0028", "role": "body", "section": "IV-B Task Planning Algorithm", "weight": 1.0} -->

In practice we use the step size $\alpha$ to prevent this term from converging too quickly.

<!-- chunk {"id": "body-0029", "role": "body", "section": "IV-B Task Planning Algorithm", "weight": 1.0} -->

Each predicate state $w$ corresponds to a range of valid continuous-space states. The algorithm recursively samples from the trajectories associated with each successive action to map to continuous states. As shown in Alg. 1, we repeatedly call the Sample function from Alg. 2, providing it with the set of possible start states $S_{0}$. We select a start state from these $s_{0}$ according to the cumulative probability of these actions. The process continues until we reach a user-provided horizon $H$. This approach allows us to maintain a constant number of samples: over successive iterations, more samples will be devoted to promising regions of the search space.

<!-- chunk {"id": "body-0030", "role": "body", "section": "IV-B Task Planning Algorithm", "weight": 1.0} -->

This results in a recursive search strategy outlined in Alg. 1. The return of the Sample function is the average probability of all future actions and trajectories associated with each current start state. This value is used to compute a version of the weights in Eq., where $p_{d}$ is replaced by the probability of all future actions from each trajectory. Fig. 4 illustrates how the algorithm works in practice.

<!-- chunk {"id": "body-0031", "role": "body", "section": "IV-B Task Planning Algorithm", "weight": 1.0} -->

(a) At the first iteration of the algorithm, we sample trajectories (dashed lines) corresponding to a1, a2, a3, etc. according to and compute pd (τ|a, w). Trajectory distributions for π(⋅|v1),π(⋅|v2), etc. are updated, as are π (a|w) (b) On subsequent iterations, trajectory sampling is biased towards a1 due to the comparatively high probability of valid trajectories for each action in this space.

<!-- chunk {"id": "body-0032", "role": "body", "section": "IV-B Task Planning Algorithm", "weight": 1.0} -->

Given: initial world w0, initial state s0, horizon H, step size α, max iterations Ni t e r if V (w0, s0) has converged then Algorithm 1 Pseudocode algorithm for optimal reproduction of demonstrated tasks in new environments. w = W (a) ⊳ Predicate world after performing action s0 ∼ S0 ∝ p (S) ⊳ Sample start points S0′ = [sN]j = 1N ⊳ Set start points ⊳ Compute probabilities of each start point ${\pi{(\left. a' \middle| w \right.)}} = {\frac{p_{d}{(\left.

<!-- chunk {"id": "body-0033", "role": "body", "section": "Experiments", "weight": 1.0} -->

We performed experiments in a simulated Barrett WAM arm and on a Universal Robot UR5, applied to an object manipulation task. The goal of this task was to build a structure of increasing complexity out of magnetic blocks, as per the task described. In our case, we only perform a part of the whole structure assembly task: we combine one link and one node object to create a sub-structure. The connections between different skills are described by the PDDL specification in Figure 3. We used FastDownward to translate the PDDL into a graph of possible actions that can be performed assuming all *feasibility* predicates are true.

<!-- chunk {"id": "body-0034", "role": "body", "section": "Experiments", "weight": 1.0} -->

We use three types of features: the time in a particular state, the gripper command variables, the transforms between the end frame and the objects. Relevant features are determined by the parameters specified in the task description in Fig. 3. In cases where two objects are parameters, we used the transform between the in-hand object and the other object. For these examples, ${\phi{(t,s,u)}} = {\lbrack t,p_{x},p_{y},p_{z},r_{x},r_{y},r_{z},r_{w},{\| p\|},{\overset{˙}{p}}_{x},{\overset{˙}{p}}_{y},{\overset{˙}{p}}_{z},{\|\overset{˙}{p}\|}\rbrack}$, where values are computed from the offset between the current manipulation frame and and the relevant object.

<!-- chunk {"id": "body-0035", "role": "body", "section": "Experiments", "weight": 1.0} -->

The values $(r_{x},r_{y},r_{z},r_{w})$ define a unit quaternion. The manipulation frame is either an end effector position or the coordinate frame associated with the object in the gripper, for actions defined where the hand-occupied predicate is true.

<!-- chunk {"id": "body-0036", "role": "body", "section": "Experiments", "weight": 1.0} -->

We parameterize trajectories $\xi$ with Dynamic Movement Primitives with $5$ basis functions in the robot's joint space, plus a goal pose $g \in {SO{}}$. This allows us to find paths in the space of the robot arm, but to adapt to different possible continuous-space goals. We implemented the system using ROS with Orocos KDL for inverse kinematics.

<!-- chunk {"id": "body-0037", "role": "body", "section": "Experiments", "weight": 1.0} -->

In practice, the "link" object can shift in unpredictable ways after a grasp action, so we adjust the plan after completion of the grasp action. We add noise to the parameters of the trajectory distribution associated with the subsequent align and place actions and replan. In the real robot experiment we omit this step due to the lack of accurate position information once the object is in the gripper.

<!-- chunk {"id": "body-0038", "role": "body", "section": "Experiments", "weight": 1.0} -->

The current implementation of the planner is single-threaded. The single largest inefficiency was detecting collisions, followed by computation of inverse kinematics. Particularly in scenes with more obstacles, both of these are very important: inverse kinematics are required to adapt trajectories to different possible grasp points, and accurate collision detection guarantees safe execution. As inverse kinematics and collision detection are outside the purview of this paper, we did not focus on efficiency.

<!-- chunk {"id": "body-0039", "role": "body", "section": "V-A Simulation Experiments", "weight": 1.0} -->

We collected three demonstrations of each of the different skills with a dynamic simulation of the Barrett WAM arm. We then place these pieces in different positions in the environment, and validated our method by performing the task in different locations. The results of one performance in a novel environment are shown in Fig. 5.

<!-- chunk {"id": "body-0040", "role": "body", "section": "V-A Simulation Experiments", "weight": 1.0} -->

To create a model of each of these skills, we collect three demonstrations of the object manipulation action using the same grasp, with two of the Barrett Hand's fingers on the left side of the link and one on the right. The simulated WAM arm was teleoperated with a Razer Hydra to collect training data. The user provided examples of three different grasps: a direct approach and approaching from the left or the right. The user specified $p_{d}{(\left. {\mathtt{a}\mathtt{p}\mathtt{p}\mathtt{r}\mathtt{o}\mathtt{a}\mathtt{c}\mathtt{h}} \middle| \mathtt{w}_{\mathtt{0}} \right.)}$ to indicate a preference for a direct approach.

<!-- chunk {"id": "body-0041", "role": "body", "section": "V-A Simulation Experiments", "weight": 1.0} -->

We perform our task on scenes with one link and two nodes at different positions, and demonstrate task effectiveness for $10$ trials with different configurations of the world. The key measure of performance is how easily we can add extra training data to our model and how close these results will be to the target mate. We set $\alpha = 0.5$ and used $M = 200$ trajectories, with a maximum of $15$ iterations. Our full algorithm used a depth of $H = 5$: a long enough horizon to plan the whole assembly task. Average likelihood of sampled trajectories converged exponentially as we proceeded through various iterations. Fig 6 shows distance to an ideal final mate after outliers were removed.

<!-- chunk {"id": "body-0042", "role": "body", "section": "V-A Simulation Experiments", "weight": 1.0} -->

By way of comparison, we remove one or both of two parts of our algorithm. We use a single randomly selected task plan ("no options" in Fig. 6). We also compare against the case where our planner only examines the currently available actions, setting $H = 1$ ("no lookahead" in Fig. 6). The "no options/no lookahead" case functions as our baseline: it uses the algorithm in Sec. IV-A to reproduce an action based on a GMM. While our approach is technically unconstrained, due to the sampling method we implicitly constrain the trajectory search to a feasible set of valid trajectories. To demonstrate how we can improve performance by improving action models, a human user selected three successful trials from the automatic performance of this task and added them to the model ("auto" in Fig. 6).

<!-- chunk {"id": "body-0043", "role": "body", "section": "V-A Simulation Experiments", "weight": 1.0} -->

Table I shows the number of planning failures associated with different environments. These are cases where the algorithm failed to find a trajectory with nonzero probability under the expert distributions defining each of our actions. Without the full algorithm, either the robot often cannot find a solution that will accomplish the task or performance is significantly degraded. The case where there are options and no lookahead is a good example. While the robot is almost always able to find a plan in this situation, the quality of plans is far worse, as shown by Fig. 6. In the higher-performing "Auto" case, the robot was always able to find a plan but few of these plans were successful: only 4/10 achieved high-quality mates, and several outliers fell off the node and the table completely. This is because without knowledge of the place and release actions, the align action will often not terminate in a good state to complete the task.

<!-- chunk {"id": "body-0044", "role": "body", "section": "V-A Simulation Experiments", "weight": 1.0} -->

Fig. 6 shows a comparison on successful trials in different environments without obstacles. The full algorithm was highly reliable and accurate, achieving less than 1 cm of placement error. Other versions of the algorithm made mistakes that planning alone could not recover. In addition, performance of all versions of the algorithm showed improvement when extra data was added, though the full version of the algorithm was still better and more flexible.

<!-- chunk {"id": "body-0045", "role": "body", "section": "V-A Simulation Experiments", "weight": 1.0} -->

Expert Data Only With Auto Data Table I: Number of failures when generalizing to novel environments. (*) indicates the full algorithm. Columns represent whether model was taught using only expert demonstrations or whether extra data was added from successful executions.

<!-- chunk {"id": "body-0046", "role": "body", "section": "V-A Simulation Experiments", "weight": 1.0} -->

We also introduced different obstacles into the environment. In these cases, the algorithm is able to avoid these objects and still complete its required task. Figure 7 shows examples of these results. Since the planner removes paths that are in collision, this restricts the set of feasible trajectories. As in the upper left of Figure 7, the most likely action in a particular scenario might be an approach from a particular direction. Once this grasp is blocked, the planner can either attempt a less likely trajectory that results in that grasp, or it can approach from a different direction. This tradeoff illustrates why our approach is more powerful than adding a potential field term to action primitives as in or similar work.

<!-- chunk {"id": "body-0047", "role": "body", "section": "V-B Real Robot Experiments", "weight": 1.0} -->

The UR5 was given the option of grabbing either of two links or a node object and combining them to create the same structure as in the simulation experiments. Demonstrations were provided in which the robot grasped either the node or the link first. The object localization technique described by Li et al. was used to determine the poses of all objects in the scene.

<!-- chunk {"id": "body-0048", "role": "body", "section": "V-B Real Robot Experiments", "weight": 1.0} -->

Our system intelligently selected whether to grasp the link or the node, and selected which face of the link to grasp based on feasibility and presence of other obstacles. The UR5 had a fairly limited workspace and has a limited ability to interact with objects when compared to the Barrett WAM arm used in the simulation experiments, making this a more challenging problem. However, the robot was able to grasp both node and link objects and complete the task. Our video supplement provides examples of the UR5 performing this task in different configurations, as well as an overview of the algorithm and videos of the simulation experiments.

<!-- chunk {"id": "body-0049", "role": "body", "section": "V-B Real Robot Experiments", "weight": 1.0} -->

In particular, when presented with both link and node objects in different orientations, the robot was able to correctly select available faces not blocked by other obstacles. If the node was better aligned with the robot's gripper, then the algorithm chose to grasp the node; if one of the links was better aligned, it would grasp this link.

<!-- chunk {"id": "body-0050", "role": "body", "section": "Conclusions", "weight": 1.0} -->

We described a practical approach for task and motion planning based on models of skills grounded from expert demonstrations of skills. By representing actions as probability distributions learned from expert demonstrations, we create a framework that can combine a broad range of actions to accomplish a task. We validated this approach with experiments in a structure assembly domain both in simulation and in a real robot. While we did not address efficiency in the implementation used in this paper, we will examine strategies for decreasing the number of costly trajectory evaluations and collision checks and apply our planner to larger and more complex tasks.
