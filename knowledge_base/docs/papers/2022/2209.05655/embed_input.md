<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

A Gaussian Variational Inference Approach to Motion Planning

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

We propose a Gaussian variational inference framework for the motion planning problem. In this framework, motion planning is formulated as an optimization over the distribution of the trajectories to approximate the desired trajectory distribution by a tractable Gaussian distribution. Equivalently, the proposed framework can be viewed as a standard motion planning with an entropy regularization. Thus, the solution obtained is a transition from an optimal deterministic solution to a stochastic one, and the proposed framework can recover the deterministic solution by controlling the level of stochasticity. To solve this optimization, we adopt the natural gradient descent scheme. The sparsity structure of the proposed formulation induced by factorized objective functions is further leveraged to improve the scalability of the algorithm. We evaluate our method on several robot systems in simulated environments, and show that it achieves collision avoidance with smooth trajectories, and meanwhile brings robustness to the deterministic baseline results, especially in challenging environments and tasks.

<!-- chunk {"id": "body-0003", "role": "body", "section": "Introduction", "weight": 1.5} -->

Motion planning is a fundamental problem in robotics where the goal is to obtain a sequence of states in the space such that it connects a start and goal state while remaining feasible along the plan. When considering motion planning problems, ubiquitous uncertainties arise from imperfect system modeling and measurement noise. Robust motion planning under uncertainties has attracted attentions in the community. Guaranteed robustness was achieved by control and verification design where uncertainties are implicit in the formulation. Stochasticity can also be explicitly brought into the formulation. Planning in belief space models states and measurements as distributions named 'belief', and planning and control are conducted in these spaces over distributions. Explicitly encoding stochasticity in motion planning has been shown helpful in overcoming locally minimum deterministic solution for non-convex and multimodal optimization problem.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

In this work we propose a Gaussian variational inference (GVI) approach to solve motion planning as a probability inference. solved this inference problem using maximum a priori (MAP) estimation. Variational inference (VI) used in this paper, on the other hand, approaches inference problems by solving an optimization within a proposed distribution family. Operating on distributions, VI naturally accounts for stochasticity in an explicit way. A natural gradient descent scheme is used to solve the optimization. The linear Gaussian process (GP) representation of the trajectory used in this paper has gained its popularity in planning and estimation since it encodes smoothness and enjoys a sparsity pattern.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

Our framework takes into account uncertainties on top of Gaussian Process Motion Planning (GPMP2). We show that the proposed method is equivalently motion planning with entropy regularization. Entropy maximization in motion planning and reinforcement learning have been studied in and was shown to increase system's robustness to disturbances. Different from the existing works, our proposed method uses a Newton-style optimization scheme which does not need a sampling scheme or learning process, and is scalable by leveraging the sparsity. The proposed method is shown to be an interpolation from a deterministic solution to a stochastic one. It recovers the deterministic solution by controlling the uncertainty level. We show by experiment that the entropy term encodes the level of risk, which then serves as a metric measuring robustness in decision-making among multiple candidate plans. The optimization scheme for GVI in this paper was first proposed, and has been applied in the robot estimation problems, where the factorized property of the problem was leveraged. To the best knowledge of the authors this is the first work that GVI is used in robot motion planning.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

This paper is organized as follows. Section II discusses the related works. In Section III we formulate the motion planning problem as variational inference. The method to solve this inference problem is presented in Section IV. Our framework is illustrated in Section V through numerical experiments.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Problem formulation", "weight": 1.0} -->

In this section we formulate motion planning as a variational inference problem. Our formulation generalizes the Gaussian process motion planning that casts motion planning as a MAP task.

<!-- chunk {"id": "body-0008", "role": "body", "section": "III-A Gaussian process motion planning", "weight": 1.0} -->

Trajectory optimization formulates the motion planning problem as an optimization of the form where $\mathcal{F}$ is the cost function and $\mathcal{G}_{i}$'s, $\mathcal{H}_{i}$'s are constraints often related to system dynamics, collision avoidance, or actuation limits. The optimization is over the trajectory $\mathbf{x}{(\cdot)}$ and the control input $\mathbf{u}{(\cdot)}$ jointly.

<!-- chunk {"id": "body-0009", "role": "body", "section": "III-A Gaussian process motion planning", "weight": 1.0} -->

The GPMP framework, alternatively, formulates the motion planning as a MAP problem where the prior distribution $p{(\mathbf{x})}$ promotes smoothness of the solution, and the likelihood $p{(\left. \mathbf{z} \middle| \mathbf{x} \right.)}$ of some desired behavior encoded by event $\mathbf{z}$ enforces collision avoidance. In particular, the prior distribution is associated with a linear Gaussian process where $\mathbf{w}$ denotes standard white noise with covariance $\mathbf{Q}_{c}$.

<!-- chunk {"id": "body-0010", "role": "body", "section": "III-A Gaussian process motion planning", "weight": 1.0} -->

We note that the likelihood probability $p{(\left. \mathbf{z} \middle| \mathbf{x} \right.)}$ describes in general the probability of the feasibility of the current trajectory candidate. In this work we consider collision avoidance likelihood where ${\parallel{\mathbf{h}{(\mathbf{x})}}\parallel}_{\mathbf{\Sigma}_{obs}^{- 1}}^{2}$ is a penalty for the collision constraints. Clearly, the MAP problem is equivalent to minimizing the cost function where $\parallel \cdot \parallel_{\mathbf{K}^{- 1}}$ denotes weighted 2-norm.

<!-- chunk {"id": "body-0011", "role": "body", "section": "III-A Gaussian process motion planning", "weight": 1.0} -->

The prior in can be decomposed into factors and the collision cost can also be factorized into where each factor represents the collision cost evaluated at corresponding support state. The collision checking needs to be carried out at a very dense set of points along the trajectory. Gaussian process representation has the advantage that the intermediate collision-checking between the support states can be done through interpolation, which keeps the sparsity of the representation. The assumptions in and together with the GP interpolation bring a sparse parameterization to our problem formulation and is greatly beneficial to the scalability of the proposed algorithm.

<!-- chunk {"id": "body-0012", "role": "body", "section": "III-A Gaussian process motion planning", "weight": 1.0} -->

Finally, we remark that the MAP formulation can be viewed as a discretization of the following trajectory optimization To see this, note that, if we only evaluate $\mathbf{h}{(\mathbf{x})}$ at discretized time $\mathbf{t} = {\lbrack t_{0},\ldots,t_{N}\rbrack}$, then for a given $\mathbf{x} = {\lbrack x_{0},\ldots,x_{N}\rbrack}^{T}$, the optimization over $\mathbf{u}{(\cdot)}$ is a linear quadratic control problem for each time interval $(t_{i},t_{i + 1})$ and the corresponding closed-form minimum is exactly the exponent of $f_{gp}^{i}$.

<!-- chunk {"id": "body-0013", "role": "body", "section": "III-B Gaussian variational inference for motion planing", "weight": 1.0} -->

Though is a probabilistic inference problem, the solution obtained in GPMP is still deterministic in the sense that it searches for a trajectory which maximizes the posterior probability. To better capture the uncertainties and risk presented in motion planning, we instead propose to approximate the full posterior distribution $p{(\left. \mathbf{x} \middle| \mathbf{z} \right.)}$. In particular, we propose the Gaussian variational inference approach to motion planning that seeks to minimize the distance between a Gaussian distribution and the true posterior, measured by KL divergence. It reads where $\mathcal{Q}$ denotes the Gaussian distribution family. The expression ${\mathbb{E}}_{q}\log p{(\mathbf{z}|\mathbf{x})} - {KL}{\lbrack q{(\mathbf{x})}||p{(\mathbf{x})}\rbrack}$ is known as the evidence lower bound (ELBO).

<!-- chunk {"id": "body-0014", "role": "body", "section": "III-B Gaussian variational inference for motion planing", "weight": 1.0} -->

The optimal distribution $q^{\star}$ encourages putting mass on the likelihood $p{(\left. \mathbf{z} \middle| \mathbf{x} \right.)}$ while minimizing its distance from the prior $p{(\mathbf{x})}$. It shows the trade-off between the smoothness and the collision avoidance. where ${H{(q)}} = {- {{\mathbb{E}}_{q}{\lbrack{\log{(q)}}\rbrack}}}$ is the entropy of the distribution. The objective can thus be interpreted as Gaussian process motion planning with an entropy regularization term.

<!-- chunk {"id": "body-0015", "role": "body", "section": "III-B Gaussian variational inference for motion planing", "weight": 1.0} -->

To further balance the trade-off between the original prior-collision cost and the entropy cost, a temperature $T$ can be introduced, pointing to When the temperature is low (small $T$), the optimization puts more weight on maintaining smoothness while avoiding obstacles. When the temperature is high, more weights are put on the system entropy cost to find solutions which have larger covariances so that they can tolerate larger uncertainties.

<!-- chunk {"id": "body-0016", "role": "body", "section": "Remark", "weight": 1.0} -->

Formulation shows an interpolation from the deterministic smooth-collision-avoiding objective to an entropy regularized robust motion planning by changing the temperature $T$. To recover the deterministic solutions, as $T$ approaches to $0$, it can be shown that obtained optimal value will tend to the minimal value for the original objective. Indeed, when $T\rightarrow 0$, the objective in approaches ${\mathbb{E}}_{q}{\lbrack{{\log p}{(\left. \mathbf{x} \middle| \mathbf{z} \right.)}}\rbrack}$ with respect to $q \sim {\mathcal{N}{({\mathbf{μ}},\mathbf{\Sigma})}}$. In this case, when $\mathbf{\Sigma}$ shrinks to 0, the objective function ${\mathbb{E}}_{q}{\lbrack{{\log p}{(\left.

<!-- chunk {"id": "body-0017", "role": "body", "section": "Remark", "weight": 1.0} -->

Finally, we note that the variational inference formulation can be viewed as a time discretization of the following stochastic control problem The proof is based on an equivalence relation between the quadratic control energy and the KL divergence ${KL}{({q \parallel p})}$. The only difference between and is that the dynamics in is disturbed by white noise $T\mathbf{w}{(t)}$. Thus, as $T$ goes to zero, should converge to.

<!-- chunk {"id": "body-0018", "role": "body", "section": "optimization scheme", "weight": 1.0} -->

GVI formulates the motion planing problem as an optimization over Gaussian distributions ${q{(\mathbf{x})}} \sim {\mathcal{N}{({\mathbf{μ}},\mathbf{\Sigma})}}$. Denote the concatenation of the mean and covariance in vector form as ${\mathbf{α}} \triangleq {({\mathbf{μ}},{vec{(\mathbf{\Sigma}^{- 1})}})}$. The inference objective then reads To solve this optimization, we utilize the natural gradient descent scheme. The factorized objective assumption which leads to a sparsity pattern of the problem is also leveraged to improve the scalability of our algorithm.

<!-- chunk {"id": "body-0019", "role": "body", "section": "IV-A Natural gradient descent", "weight": 1.0} -->

For notation simplification, we denote ${\psi{(\mathbf{x})}} = {- {{\log p}{(\left. \mathbf{x} \middle| \mathbf{z} \right.)}}}$. The derivatives w.r.t. $\mathbf{μ}$ and $\mathbf{\Sigma}^{- 1}$ can be derived explicitly All expectations are taken w.r.t. $q$. Comparing (17b) and (17c) we obtain Having the relations in and, for Gaussian distribution $q \sim {\mathcal{N}{({\mathbf{μ}},\mathbf{\Sigma})}}$, a natural gradient descent update step w.r.t. objective function $V$ can be calculated straightforward as Using properties of the kronecker product and vectorizations of matrices, the update step in natural gradient is Notice that we write in terms of $\mathbf{\Sigma}^{- 1}$ to fully leverage its sparsity pattern.

<!-- chunk {"id": "body-0020", "role": "body", "section": "IV-A Natural gradient descent", "weight": 1.0} -->

Comparing and, we have Equation and tells that, to calculate the update ${\delta{\mathbf{μ}}},{\delta\mathbf{\Sigma}^{- 1}}$, we only need to compute (17a) and (17b). The new variables are calculated using the updates, a step size $\gamma < 1$, and a constant $R$ in a backtracking fashion as where $R > 1$ is increasing to shrink the step size for backtracking until the cost decreases. Line search algorithms can also be deployed to obtain locally minimum solutions for this non-convex optimization.

<!-- chunk {"id": "body-0021", "role": "body", "section": "IV-B Factorized objectives", "weight": 1.0} -->

We next show that with factorized cost functions, the update step in the algorithm will preserve the sparsity pattern of $\mathbf{\Sigma}^{- 1}$. Under the factorized assumptions and, and denote ${\psi_{k}{(\mathbf{x}_{k})}} = {- {{\log p}{(\left. \mathbf{x}_{k} \middle| \mathbf{z} \right.)}}}$, also factorizes where $V_{k}{(q_{k})}$'s are factored costs and $\mathbf{x}_{k}$ are the corresponding subsets of variables to the $k$th factor.

<!-- chunk {"id": "body-0022", "role": "body", "section": "IV-B Factorized objectives", "weight": 1.0} -->

The relation between the joint and the factorized variables reads In view of and, to compute the updates $\delta{\mathbf{μ}}$ and $\delta\mathbf{\Sigma}^{- 1}$, we need to calculate the derivatives of the joint objective which also factorizes as The factorized derivatives $\frac{\partial V_{k}}{\partial{\mathbf{μ}}_{k}}$ and $\frac{\partial^{2}V_{k}}{\partial{{\mathbf{μ}}_{k}{\mathbf{μ}}_{k}^{T}}}$ will have the same expressions as in w.r.t.

<!-- chunk {"id": "body-0023", "role": "body", "section": "IV-B Factorized objectives", "weight": 1.0} -->

marginal distributions $q_{k} \sim {\mathcal{N}{({\mathbf{μ}}_{k},\mathbf{\Sigma}_{k})}}$ and marginal factors $\psi{(\mathbf{x}_{k})}$ From, and we see that the sparsity pattern of the precision matrix $\mathbf{\Sigma}^{- 1}$ is preserved after the transitions between the joint and factorized updates.

<!-- chunk {"id": "body-0024", "role": "body", "section": "IV-B Factorized objectives", "weight": 1.0} -->

From we know that a joint covariance matrix $\mathbf{\Sigma}$ is computed in each update step. Throughout the iterations $\mathbf{\Sigma}^{- 1}$ remains sparse, but $\mathbf{\Sigma}$ need not to be. However, because of the consistent sparsity pattern, efficient methods exist in sparse linear algebra literature to compute only the parts of $\mathbf{\Sigma}$ corresponding to the non-zero elements in $\mathbf{\Sigma}^{- 1}$. Alternatively, Gaussian belief propagation can also solve the marginal covariance efficiently. The expectations in are approximately evaluated using Gauss-Hermite quadrature in this work. We note that when the posterior $p{(\left. \mathbf{x} \middle| \mathbf{z} \right.)}$ is linear, then expectations in have closed-form, which greatly accelerates the algorithm.

<!-- chunk {"id": "body-0025", "role": "body", "section": "experiments", "weight": 1.0} -->

In all our experiments, we consider a constant-velocity model. Let The transition matrix $\mathbf{\Phi}$, matrices $\mathbf{Q}_{i}$, $\mathbf{Q}_{i}^{- 1}$, $\mathbf{Q}$, and $\mathbf{B}$ in can be calculated explicitly. The likelihood function is defined the same as in by where $FK{(\cdot)}$ is the forward kinematics, $\mathbf{d}{(\cdot)}$ is the signed distance function given a signed distance field (SDF), and $\mathbf{c}_{\epsilon}{(\cdot)}$ is the hinge loss function When evaluating the signed distance function $\mathbf{d}{(\cdot)}$, robots are modeled as balls with fixed radius $r$ at designated locations. The minimum distance from robots to obstacles is efficiently computed using the distance between centers of the balls to the obstacles and the ball radius. In this paper, to highlight the convergence of the algorithm, GP interpolation is not involved in any experiments.

<!-- chunk {"id": "body-0026", "role": "body", "section": "V-A 2d point robot collision avoidance", "weight": 1.0} -->

The first experiment is conducted with a planar point robot, which better captures the idea of covariance by plotting ellipsoids. Fig.1 shows the convergence of the support states. Black dots represent $\mathbf{μ}$, and the red ellipsoids draw the $0.997$ confidence region contour. We initialize $\mathbf{μ}$ using a linear interpolation between the start and goal states, and initialize $\mathbf{\Sigma}^{- 1}$ using isotropic matrices.

<!-- chunk {"id": "body-0027", "role": "body", "section": "Trade-off between motion planning and system entropy", "weight": 1.0} -->

The cost function in contains two parts: a motion planning including prior and collision costs, and a regularized entropy cost. Fig. 2 shows the evolution of different costs and the total cost, where the prior and collision costs are factorized, and the cost on the entropy $\frac{1}{2}{\log{({|\mathbf{\Sigma}^{- 1}|})}}$ is computed on the joint level. As shown in Fig.2, during the first several iterations the prior and collision costs on each factor decreases, meaning that the system gets rid of the obstacle while maximizing trajectory smoothness and system dynamics assumptions imposed by the prior. Meanwhile, the entropy costs increase. After the system is safe and smooth, the algorithm moves to the region where the entropy cost decreases. During the two phases, the total loss decreases. This trade-off process is also reflected in the Fig. 1. The covariance pivots shrink while the system is avoiding the obstacles, and increase after the system is safe and smooth.

<!-- chunk {"id": "body-0028", "role": "body", "section": "Planning with high temperature", "weight": 1.0} -->

In, a temperature $T$ is introduced to alter the weights between planning objective and entropy cost. To achieve feasible trajectories, we use small $T$. However in low temperature regions, little changes on $\mathbf{\Sigma}$ will happen due to the low weight on the entropy cost. One motivation of the proposed formulation is that we would like to leverage the entropy in order to have wider-spread distributions in all areas, since the $3\sigma$ area measures the size of the safe regions in a probabilistic sense. Higher temperature promotes the system's entropy, but put less weights on the feasibility part. A compromise is to use a near-feasible initialization with high temperature. The initialization for the mean $\mathbf{μ}$ can either be the output of a lower temperature optimization as a re-planning, or from a higher level sampling based planner. Fig. 3 shows the converging process of the iterations for a high temperature re-planning. We note that the low temperature planning and the high temperature re-planning can be done in a consecutive manner in the optimization.

<!-- chunk {"id": "body-0029", "role": "body", "section": "V-B More challenging planning problems", "weight": 1.0} -->

In the next set of experiments we show that by introducing entropy regularization to the deterministic formulation, we gain flexibility in solution searching as well as a risk-measuring metric. We illustrate using several experiments. In paragraph (a), to test the performance in hard tasks, we conduct long range planning in cluttered environments. In (b) we use a narrow gap environment to show that stochasticity brings flexibility in choosing collision-checking radius, compared with deterministic baseline; In (c) we show that stochasticity help explore solution spaces and find multiple locally optimal candidate solutions. In (d) it is shown that entropy serves as a measure of risk which plays an important role in decision making in terms of choosing the final plan.

<!-- chunk {"id": "body-0030", "role": "body", "section": "Long distance planning in cluttered environments", "weight": 1.0} -->

We first conduct long-distance tasks in a cluttered environment for a planar point robot. Fig.4 shows the resulting trajectory distributions. In practice we found that the smoothness captured by Gaussian processes is the key for the trajectories to circumvent sharp corners and achieve long distance targets. We observe that the covariances shrink in the narrow areas and stretch in the safe zones. The volume of the confidence regions describes level of safety locally, since when sampling trajectories from the distributions, regions with wider confidence region provides more choices with the same level of confidence on feasibility. The adaptive confidence regions brings robustness to the trajectories in face of environment uncertainties.

<!-- chunk {"id": "body-0031", "role": "body", "section": "Planning through a narrow gap with more flexible collision-checking radius", "weight": 1.0} -->

Fig. 5 shows the planning task in a narrow-opening environment. We first show that the covariance can provide flexibility in collision checking. For the deterministic baseline GPMP2, the radius $r$ of collision-checking balls needs to be prefixed and in accordance with the environment. Fig. 5 shows that $r$ needs to be small enough to achieve a successful 'go-through' plan. In Fig. 6, our proposed method can obtain a successful motion plan using the same radius which has led to a failed plan in GPMP2 shown in the left subfigure in Fig. 5. We note that this is because that the proposed method optimizes directly over covariance so that the expected cost can always decrease even with large collision-checking radius. In complex planning tasks, variable covariance can give flexibility in choosing $r$ as one hyperparameter. In real-world planning tasks, different levels of safety are required in different regions in the environment, which is directly encoded in the variable covariance.

<!-- chunk {"id": "body-0032", "role": "body", "section": "Plan circumventing a narrow gap showing solution space exploration", "weight": 1.0} -->

We show by experiment that the entropy regularization can also promote solution space exploration. Trajectory optimization is often initialized using a sampling-based course plan such as RRT, which is partially because that the problem is non-convex and it is easier to find a local optimal value if started closer. In Fig. 2, a 'go-around' initialization is used for both the proposed method and GPMP2, other parameters being the same. Starting from the same initialized seed, the proposed framework finds a 'go-around' trajectory circumventing the gap while GPMP2 converged back to the 'go-through' plan. This shows that stochasticity encourage solution domain exploration in finding candidate motion plans. As explained in the next paragraphs, this is because the entropy cost regularizes the total cost.

<!-- chunk {"id": "body-0033", "role": "body", "section": "Comparing locally minimum solutions leveraging entropy", "weight": 1.0} -->

When comparing different solutions, the entropy cost serves as a risk-measuring metric in addition to motion planning costs. Intuitively, plans with lower entropy cost are considered to be less risky, because the covariance stretches wider in safer regions. As an example, Fig. 8 compares two motion plans visually, and Tab. I compares different costs for the two plans in Fig. 8. Results show that the 'go-around' plan has far lower collision and entropy costs which together beat the 'go-through' plan. In this scenario, it is reasonable to choose a longer but less risky 'go-around' plan which circumvents the narrow gap.

<!-- chunk {"id": "body-0034", "role": "body", "section": "V-C Arm robot", "weight": 1.0} -->

To validate our proposed framework, we conducted experiments on a 2 types of arm robots.

<!-- chunk {"id": "body-0035", "role": "body", "section": "2-link arm model", "weight": 1.0} -->

Fig. 9 shows the convergence process in a cluttered environment. Fig. 10 shows the sampled states from the obtained distributions. The last iteration in Fig. 9 shows a reasonable collision avoidance behavior while keeping the smoothness of the trajectory. In Fig. 10, we plot the means and samples for the support states of the last iteration in Fig. 9. The solid blue bars represent the mean values, and shadowed bars are samples. The depth of the shadowed states represents the sample frequency. As shown in Fig. 10, in less cluttered area, samples distribute wider, representing higher entropy, and in the more constrained areas, there are less freedom.

<!-- chunk {"id": "body-0036", "role": "body", "section": "7-DOF WAM arm model", "weight": 1.0} -->

Solving the optimization in the space of distributions brings additional computation complexities compared with the deterministic formulation. However, the factorized cost function and partial update schemes mitigate the problem. In addition, there exist more efficient methods in evaluating the integrals, which can further accelerate the algorithm. We evaluated the proposed algorithm on a 7-DOF WAM Arm robot in a more realistic dataset, the optimized mean and samples are shown in Fig. 11 and Fig. 12.

<!-- chunk {"id": "body-0037", "role": "body", "section": "conclusion", "weight": 1.5} -->

In this work we proposed a Gaussian variational inference framework to approach motion planning as a probability inference. On top of the Gaussian process representation of the trajectory, we calculate an optimal Gaussian distribution over the trajectories. Natural gradient descent scheme was deployed to solve the GVI. Factorized cost functions brings a sparsity pattern into the framework, and Gaussian assumption brings an explicit update scheme which converges quickly to locally minimum solutions. Alternatively, the proposed framework can be viewed as motion planning with entropy regularization. Experiments show that the proposed method achieves smooth collision-free trajectories, and also provides more robust solutions than deterministic baseline methods, especially in challenging environments. The limitation of the proposed algorithm is the computation complexity increased by introducing additional optimization variables, which is a trade-off for the additional distributional information gain. However, this issue can be mitigated by leveraging the problem's sparsity pattern and more advanced integration estimation techniques.
