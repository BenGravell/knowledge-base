<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

An Unsupervised C-Uniform Trajectory Sampler with Applications to Model Predictive Path Integral Control

Topics include Model predictive path integral control, Trajectory optimization, Sampling-based control, Action sampling distribution, Neural networks, Reachable sets.

<!-- chunk {"id": "summary-0002", "role": "summary", "section": "Summary", "weight": 2.0} -->

Extension of C-Uniform trajectory sampling that trains a neural network to approximate the reachable-set-based sampling distribution in an unsupervised manner, achieving similar reachable state coverage as the original method with dramatically faster training time.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Sampling-based model predictive controllers generate trajectories by sampling control inputs from a fixed, simple distribution such as the normal or uniform distributions. This sampling method yields trajectory samples that are tightly clustered around a mean trajectory. This clustering behavior in turn, limits the exploration capability of the controller and reduces the likelihood of finding feasible solutions in complex environments. Recent work has attempted to address this problem by either reshaping the resulting trajectory distribution or increasing the sample entropy to enhance diversity and promote exploration. In our recent work, we introduced the concept of C-Uniform trajectory generation which allows the computation of control input probabilities to generate trajectories that sample the configuration space uniformly. In this work, we first address the main limitation of this method: lack of scalability due to computational complexity. We introduce Neural C-Uniform, an unsupervised C-Uniform trajectory sampler that mitigates scalability issues by computing control input probabilities without relying on a discretized configuration space. Experiments show that Neural C-Uniform achieves a similar uniformity ratio to the original C-Uniform approach and generates trajectories over a longer time horizon while preserving uniformity.

<!-- chunk {"id": "abstract-0004", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Next, we present CU-MPPI, which integrates Neural C-Uniform sampling into existing MPPI variants. We analyze the performance of CU-MPPI in simulation and real-world experiments. Our results indicate that in settings where the optimal solution has high curvature, CU-MPPI leads to drastic improvements in performance.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

Sampling-based model predictive controllers generate "minimum cost" trajectories using a set of trajectory samples to achieve objectives such as arriving at a goal location while avoiding obstacles and adhering to motion constraints. They have been used in various robotics applications including autonomous driving, manipulation, and drone navigation. In order to generate random trajectories which are also kinematically valid, existing methods sample control inputs using a simple distribution such as the normal distribution. The system model is then used to propagate the state using these random inputs. However, as shown in Fig. 1, these sampling strategy generally yield samples that are clustered around a mean trajectory which limits the exploration capacity of the controller and reduces the likelihood of finding feasible solutions.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

Recent works have addressed this issue of insufficient exploration by modifying control input sampling distribution to promote higher trajectory sample diversity and enhanced exploration. For example, log-MPPI introduced a new sampling distribution, normal-log-normal, to flatten the resulting trajectory distribution. Even though this approach enhances exploration during trajectory sampling, the exploration is still local which can be problematic in high-curvature or multimodal settings.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

Rather than modifying the final trajectory distribution, an alternative is to focus on finding a better nominal trajectory to initialize the sampling mechanism to avoid the mode collapse. This is achieved by generating a set of proposals and optimizing them to locate trajectories around lower-cost areas so that subsequent sampling can be performed around those regions. Recently introduced Stein Variational Guided Model Predictive Path Integral Control (SVG-MPPI) integrates Stein Variational Gradient Descent (SVGD) to find a good nominal trajectory. It iteratively refines a set of trajectory samples by pushing them toward lower-cost regions. This mode-seeking behavior helps to concentrate the trajectory sampling around low-cost regions in the cost landscape. However, the efficiency of this process heavily depends on the quality of the initial sample set. For example, if the starting trajectories do not adequately cover the C-space, the refinement process may require many iterations with the added computational cost, or the gradient may provide limited information that causes the solution to get trapped in a local minimum.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Introduction", "weight": 1.5} -->

In our previous work, we presented the C-Uniform trajectory sampling method that computes control input probabilities to generate trajectories that uniformly sample the configuration space (C-space). In other words, C-Uniform provides a systematic and unified approach to exploration. However, it relies on discretization of the configuration space to build a flow network to compute the optimal flow which is costly both in computation time and space.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Introduction", "weight": 1.5} -->

In this paper, we address these limitations using an unsupervised learning approach and present the *Neural C-Uniform trajectory sampling method*, in which a neural network is trained to map the state to control input probabilities that lead to C-Uniform trajectories. This approach eliminates the need for discretization and enables the generation of trajectories for longer horizons while maintaining uniformity (Fig. 1). Our second contribution is a new variant of MPPI, CU-MPPI, that leverages trajectories from Neural C-Uniform to increase the chances of finding a better nominal trajectory by covering the C-space uniformly and avoiding the dependence on the gradient.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Introduction", "weight": 1.5} -->

In summary, the contributions of our work are: We present Neural C-Uniform trajectory sampler, which uses entropy maximization formulation to generate trajectories that are uniform in the configuration space (Sec. IV).

<!-- chunk {"id": "body-0011", "role": "body", "section": "Introduction", "weight": 1.5} -->

We present CU-MPPI, a new sampling-based model predictive controller that utilizes Neural C-Uniform trajectories to enhance exploration. By ensuring broad coverage of the C-space, our method increases the likelihood of finding the global minimum regions while reducing dependence on gradient-based refinements (Sec. V).

<!-- chunk {"id": "body-0012", "role": "body", "section": "Introduction", "weight": 1.5} -->

We perform experimental validation through real-world and simulation experiments to assess the advantages of having a diverse trajectory sampling strategy and its effectiveness in sampling-based model predictive controller settings (Sec. VI).

<!-- chunk {"id": "body-0013", "role": "body", "section": "Introduction", "weight": 1.5} -->

The results indicate that the notion of C-Uniformity provides a systematic trade-off between exploration and gradient-seeking (exploitation) for MPPI-based methods. We start with an overview of related work.

<!-- chunk {"id": "body-0014", "role": "body", "section": "II-A Trajectory Sampling", "weight": 1.0} -->

Trajectory sampling arises in a wide range of research domains, such as stochastic processes, control theory, motion planning, and reinforcement learning. It is often employed to study system behavior under uncertainty to get insights into the probabilistic dynamics of stochastic processes. In control theory, it is used to design and analyze control inputs that navigate systems along desired objectives while satisfying the constraints; on the motion planning side, it is used to determine a path or a trajectory to guide systems, while similarly adhering to constraints. Even though there is extensive research on trajectory sampling, it turns out that determining controls for the trajectory distribution remains a relatively less explored area. The two works closest to this context are C-Uniform trajectory sampling and sample-based MPC. Thomas et al proposed sampling-based MPC to generate control inputs for collision-free paths using a normalizing flow as a sampling distribution. In our previous work, we proposed C-Uniform trajectory sampling, which concerns uniformly sampling the set of valid configuration space using robot inputs to maintain the desired trajectory distribution over time.

<!-- chunk {"id": "body-0015", "role": "body", "section": "II-B Sampling-based Model Predictive Control", "weight": 1.0} -->

In recent years, with the enhancement of parallel computing power, sampling-based model predictive control methods (SBMPC) have increased in popularity. Pioneer work called Model Predictive Path Integral (MPPI) control combines the path integral theory and MPC formulation. In that work, control inputs are sampled using a Gaussian to generate a tractable and controllable trajectory distribution around a nominal trajectory. However, the Gaussian assumption leads to vital problems in changing environment settings. Researchers have addressed this issue in several ways. In, covariance steering theory is used to shift the final shape of trajectory distribution. Similarly, log-MPPI, uses normal-log-normal distribution to flatten the resulting sampling distribution or adding bias to the cost distribution allows to have arbitrary sampling distributions. Moreover, some methods use adaptive importance sampling to shift the solution to the lower-cost regions. Alternatively, other methods tend to move the nominal cost to areas with low-cost by solving reverse Kullback-Leibler divergence to find a mode of the cost distribution.

<!-- chunk {"id": "body-0016", "role": "body", "section": "II-B Sampling-based Model Predictive Control", "weight": 1.0} -->

Comparably, Stein Variational Gradient Descent is also used for understanding cost distribution or guiding the MPPI trajectories to low-cost regions by modifying both the nominal trajectory and the covariances.

<!-- chunk {"id": "body-0017", "role": "body", "section": "III-A C-Uniform Trajectory Sampling", "weight": 1.0} -->

We provide key concepts of the C-Uniform trajectory sampling. For more details, we direct the reader to prior research. We first define a Level Set $L_{t}$ as the following equation: where the set of all states $\mathbf{x}_{t} \in \mathcal{X}$ such that there is a control sequence $\mathbf{U}$ of length $t$ with $\mathbf{x} = {F{(\mathbf{x}_{0},\mathbf{U})}}$. We also need to note that these level sets are disjoint, meaning if a state $\mathbf{x}_{i}$ is already covered by some $L_{i}$, we discard that state that is also reachable in any later level set $L_{j}$, where $j > i$.

<!-- chunk {"id": "body-0018", "role": "body", "section": "III-A C-Uniform Trajectory Sampling", "weight": 1.0} -->

Lastly, we define $L_{D,t}$ as the discretized version of $L_{t}$ where each representative state $\mathbf{x}_{D,t} \in L_{D,t}$ is found by $L_{t}/\delta$ where $\delta$ defines a small measurable uniform region of C-Uniform. We use the Lebesgue measure ($\mu$) to quantify the size of these regions. Then, the uniform probability of representatives for each level set is defined as ${P{({\mathbf{x}_{t} \in \delta})}} = {{{\mu{(\delta)}}/\mu}{(L_{t})}}$, where $\mathbf{x}_{t}$ is a state in the uniformity cell.

<!-- chunk {"id": "body-0019", "role": "body", "section": "III-A C-Uniform Trajectory Sampling", "weight": 1.0} -->

The probabilities associated with level sets are computed recursively for each level set as follows. where $\mathbf{x}_{t + 1}$ is the state in the next level set, and the control inputs $\mathbf{u}_{i}$ are the ones that reach the state $\mathbf{x}_{t + 1}$ by propagating the current state $\mathbf{x}_{t}$. Additionally, we also discretize the action space $\mathcal{U}$ into a set of distinct actions $\mathcal{U} = {\{ u_{0},u_{1},\ldots,u_{N}\}}$ and we define a probability mass function (pmf) over it. The pmf is denoted as $p{(\left. \mathcal{U} \middle| \mathbf{x} \right.)}$, where ${\sum_{i = 0}^{N}{p{(\left.

<!-- chunk {"id": "body-0020", "role": "body", "section": "III-A C-Uniform Trajectory Sampling", "weight": 1.0} -->

By introducing the Eq. 3, we can state a similar problem formulation for the Neural C-Uniform trajectory sampling, as defined: Given an initial state $\mathbf{x}_{0}$ and a system's dynamic model $F$ determine control action probabilities $p{(\left. \mathcal{U} \middle| \mathbf{x} \right.)}$ for each state such that the probability distribution associated with each level set is uniform.

<!-- chunk {"id": "body-0021", "role": "body", "section": "Unsupervised C-Uniform Trajectory Sampler", "weight": 1.0} -->

In this section, we introduce our Neural C-Uniform trajectory sampling approach. We first present an entropy maximization formulation of Neural C-Uniform to generate the probability distribution of control inputs $p{(\left. \mathcal{U} \middle| \mathbf{x} \right.)}$ that satisfies the Eq. 3. In particular, given a state $\mathbf{x}$, we generate a probability distribution of control inputs $p{(\left. \mathcal{U} \middle| \mathbf{x} \right.)}$ which uniformly samples all level sets.

<!-- chunk {"id": "body-0022", "role": "body", "section": "IV-A Entropy Maximization Formulation", "weight": 1.0} -->

Uniform distribution leads to maximum entropy which is unique among all probability distributions defined over a domain. Hence, we formulate Neural C-Uniform as an iterative level set entropy maximization problem to learn generating $p_{\theta}{(\left. \mathcal{U} \middle| \mathbf{x} \right.)}$ parameterized by $\theta$ for each state $\mathbf{x}_{t}$ in $L_{t}$ and resulting in $\mathbf{x}_{t + 1} = {F{(\mathbf{x}_{t},\mathbf{u}_{\mathbf{t}})}}$ in $L_{t + 1}$ to maximize for entropy $\mathcal{H}{(\mathbf{x}_{t + 1})}$ defined by Eq. 4.

<!-- chunk {"id": "body-0023", "role": "body", "section": "IV-A Entropy Maximization Formulation", "weight": 1.0} -->

where $p{(\mathbf{x}_{t + 1})}$ shows the probability of state $\mathbf{x}_{t + 1} \in L_{t + 1}$ when an action $\mathbf{u}$ is taken from the $\mathbf{x}_{t} \in L_{t}$. We now describe the training procedure and network architecture of Neural C-Uniform using Eq. 4.

<!-- chunk {"id": "body-0024", "role": "body", "section": "IV-B Network Architecture", "weight": 1.0} -->

Neural C-Uniform architecture is capable of learning to determine $p{(\left. \mathcal{U} \middle| \mathbf{x} \right.)}$ for any state $\mathbf{x}$ from any level set $L_{t}$ to uniformly sample the next level set $L_{t + 1}$ provided the level sets are disjoint. Neural C-Uniform architecture consists of two linear layers of 256 nodes and an output layer of 45 actions representing the action distribution. The intermediate layers are applied with the ReLU activation function to capture the non-linearity of the level-set propagation over time while the output is applied with softmax to convert logits to a probability distribution. Additionally, Batchnorm layers were added after each ReLU activation function of intermediate layers. The input to the architecture is $\mathbf{x} \in {\mathbb{R}}^{n}$ where $n$ is the dimension of the state vector of the given dynamics system.

<!-- chunk {"id": "body-0025", "role": "body", "section": "IV-B Network Architecture", "weight": 1.0} -->

In our case, the input is $\mathbf{x} = {\lbrack x,y,\psi\rbrack} \in {\mathbb{R}}^{3}$ as shown in Eqn. 1 where $x$, $y$ represents the positions and $\psi$ represents the heading of the vehicle which is converted to $\cos\psi$ and $\sin\psi$ to account for the periodicity.

<!-- chunk {"id": "body-0026", "role": "body", "section": "IV-B Network Architecture", "weight": 1.0} -->

Input: LD: Discretized C-Uniform Level Sets; Nt: The number of time steps in a trajectory; 𝒰: the set of actions; LD = {LD, t}t = 0N where LD, t is the discretized C-Uniform Level set at time step t; for each time step t = 0 to N − 1 do for each state xD, t ∈ LD, t do for each action u ∈ 𝒰 do Neural C-Uniform architecture is trained for entropy maximization which is defined by Eq. 4. In particular, $- {\sum_{\mathbf{x}_{t}}{\sum_{\mathbf{u}}{p{(\left. \mathbf{x}_{t + 1} \middle| {\mathbf{u},\mathbf{x}_{t}} \right.)}{\log p}{(\left.

<!-- chunk {"id": "body-0027", "role": "body", "section": "IV-B Network Architecture", "weight": 1.0} -->

\mathbf{x}_{t + 1} \middle| {\mathbf{u},\mathbf{x}_{t}} \right.)}}}}$ is used as the loss function where the negative sign is omitted to account for the gradient descent step. In order to maximize with respect to $p{(\mathbf{x}_{t + 1})}$, we first generate next states $\mathbf{x}_{t + 1}$ using action space $\mathcal{U}$ for each discretized states $\mathbf{x}_{D,t}$ of C-Uniform $L_{D,t}$ and perform assignment to $\mathbf{x}_{D,{t + 1}}$ in $L_{D,{t + 1}}$ for calculating $p{(\mathbf{x}_{t + 1})}$. To ensure differentiable loss, we use a soft assignment which is defined by Eq. 5.

<!-- chunk {"id": "body-0028", "role": "body", "section": "IV-B Network Architecture", "weight": 1.0} -->

The soft assignment is then used to maximize $\mathcal{H}{(\mathbf{x}_{D,{t + 1}})}$ resulting in determining $p_{\theta}{(\left. \mathbf{u} \middle| \mathbf{x}_{D,t} \right.)}$ which uniformly samples all level sets.

<!-- chunk {"id": "body-0029", "role": "body", "section": "IV-B Network Architecture", "weight": 1.0} -->

We use Adam optimizer with a learning rate of 0.0001 and train it for 20 epochs on a dataset of $L_{D}$ consisting of a time horizon of 3 seconds with 0.2 time discretization resulting in 16 level sets. Algorithm 1 shows the full end-to-end training pipeline of Neural C-Uniform architecture where $\mathbf{x}_{D,t}$ is in $L_{D,t}$ and $\mathbf{x}_{D,{t + 1}}$ is in $L_{D,{t + 1}}$.

<!-- chunk {"id": "body-0030", "role": "body", "section": "C-Uniform Based Model Predictive Path Integral", "weight": 1.0} -->

In this section, we introduce a new MPPI variant, CU-MPPI. We illustrate the general overview of our approach in Fig. 2. The method first generates a set of Neural C-Uniform trajectories for the current state $\mathbf{x}_{t}$. Then, our approach selects the trajectory with the lowest cost from the samples set. Once the lowest-cost trajectory identified, we use it as the nominal trajectory for MPPI trajectory sampling. The MPPI algorithm solves the optimization problem in Eq. 7 to get the final input sequence for the current time step $t$.

<!-- chunk {"id": "body-0031", "role": "body", "section": "C-Uniform Based Model Predictive Path Integral", "weight": 1.0} -->

A key advantage of our Neural C-Uniform sampling strategy is its ability to improve the likelihood of selecting a near-optimal trajectory as the number of samples increases by ensuring uniform coverage of the trajectory space. Let $\mathcal{T} = {\{\tau_{1},\tau_{2},\ldots,\tau_{N}\}}$ represent the set of $N$ sampled Neural C-Uniform trajectories, each associated with a cost $J^{\tau_{i}} = {J{(\mathbf{x}_{t},U)}}$.

<!-- chunk {"id": "body-0032", "role": "body", "section": "C-Uniform Based Model Predictive Path Integral", "weight": 1.0} -->

Instead of expectation minimization of the cost, as, we use direct cost minimization of the cost for the nominal trajectory selection as: where $\tau^{\ast}$ is the minimum cost trajectory in the set $\mathcal{T}$.

<!-- chunk {"id": "body-0033", "role": "body", "section": "C-Uniform Based Model Predictive Path Integral", "weight": 1.0} -->

As the number of samples increases, the uniform coverage of the trajectory space improves, leading to a higher probability change to get a trajectory around low-cost regions. In cases where the cost function has a multimodal distribution, where multiple trajectories have the same minimum cost, we break ties by selecting one trajectory uniformly at random to ensure unbiased selection among optimal candidates.

<!-- chunk {"id": "body-0034", "role": "body", "section": "V-A MPPI Trajectory Sampling", "weight": 1.0} -->

In Fig.2, the green trajectory represents $\tau^{\ast}$, which has the minimum cost among the sampled trajectories shown in blue. Furthermore, the action sequence $\mathbf{U}$ that generates the trajectory $\tau^{\ast} = {F{(\mathbf{x}_{t},\mathbf{U})}}$ is used as the nominal control input sequence $\overset{\sim}{\mathbf{U}}$ in MPPI algorithm with a fixed covariance matrix $\Sigma$.

<!-- chunk {"id": "body-0035", "role": "body", "section": "V-A MPPI Trajectory Sampling", "weight": 1.0} -->

After the nominal input sequence is selected and fed into the MPPI algorithm. The red trajectories in Fig. 2 show the sampled trajectories with the factorized Gaussian probability density function $q{(\left. \mathbf{V} \middle| {\overset{\sim}{\mathbf{U}},\Sigma} \right.)}$. Then, the optimal action sequence by those samples is calculated: where, $\mathbf{V} = {\mathbf{U} + \epsilon}$ and $\epsilon \sim {\mathcal{N}{(0,\Sigma)}}$. In practice, Monte Carlo sampling methods are used to approximate the expectation. Further details on the derivation can be found. The optimal sequence $\mathbf{U}^{\ast}$ is shown in cyan in Fig.2.

<!-- chunk {"id": "body-0036", "role": "body", "section": "V-B Nominal Trajectory Selection", "weight": 1.0} -->

In each control iteration, the method adds the MPPI optimal solution into the Neural C-Uniform trajectories so that the optimal trajectory from the previous time step can also be considered for the next nominal sequence selection. This integration enhances exploitation by increasing the likelihood of staying within a low-cost region. At the same time, the inherent stochasticity of C-Uniform sampling preserves exploration. Even if MPPI provides a non-optimal solution, this exploration ability prevents premature convergence to suboptimal solutions.

<!-- chunk {"id": "body-0037", "role": "body", "section": "Experiments", "weight": 1.0} -->

We evaluate the Neural C-Uniform sampling method and CU-MPPI controller by studying the following questions through experiments.

<!-- chunk {"id": "body-0038", "role": "body", "section": "Experiments", "weight": 1.0} -->

Can the Neural C-Uniform trajectory sampling method maintain uniformity over a given planning horizon, and how does the uniformity of sampled trajectories change when extrapolated to longer horizons than it was trained on? (Sec. VI-B) Can the proposed controller algorithm effectively find optimal paths even when the curvature of the optimal solution is high? (Sec. VI-C) Can the proposed controller algorithm adapt and perform reliably in dynamic and complex environments in both simulation and real-world scenarios? (Secs. VI-D and VI-E.)

<!-- chunk {"id": "body-0039", "role": "body", "section": "VI-A Experimental Setup", "weight": 1.0} -->

Baselines: In our simulation and real-world experiments, we compare our method against three baselines controllers: MPPI, log-MPPI, and SVG-MPPI.

<!-- chunk {"id": "body-0040", "role": "body", "section": "VI-A Experimental Setup", "weight": 1.0} -->

MPPI and log-MPPI are selected to highlight how different trajectory distributions affect the performance of various navigation tasks. MPPI only uses Gaussian samples around a nominal trajectory, and log-MPPI uses Normal-Log-Normal distribution to generate samples. We implemented both methods with a temperature parameter of $\lambda = 0.5$. We also initialized with two covariance values $\Sigma = {\lbrack 0.05,0.1\rbrack}$.

<!-- chunk {"id": "body-0041", "role": "body", "section": "VI-A Experimental Setup", "weight": 1.0} -->

Additionally, we include SVG-MPPI as a baseline, which represents the state-of-the-art MPPI-variant with mode-seeking behavior. We use the standard implementation and hyperparameters of SVG-MPPI.

<!-- chunk {"id": "body-0042", "role": "body", "section": "VI-A Experimental Setup", "weight": 1.0} -->

System Specs: All simulation experiments are conducted on a Ubuntu 24.04 platform. The computer is equipped with an Intel i9-13900HX and a Nvidia GeForce RTX 4090. Real-world experiments were conducted on the F1Tenth racer platform, which runs ROS2 Foxy on Ubuntu 20.04 and is equipped with a Nvidia Jetson Xavier. The parameters for the vehicle are taken.

<!-- chunk {"id": "body-0043", "role": "body", "section": "VI-A Experimental Setup", "weight": 1.0} -->

Cost Function: The cost function $J$ has two components: the state obstacle cost $\mathcal{C}_{\text{obs}}{(x_{t})}$, which penalizes states based on the local costmap values to avoid obstacles and the distance-to-goal cost $\mathcal{C}_{\text{goal}}{(x_{t},x_{\text{goal}})}$, which encourages the trajectory to minimize the distance to the goal $x_{\text{goal}}$. The total cost $J$ is computed over a time horizon $T$, and the relative importance of obstacle avoidance and goal-reaching is controlled by a weighting factor $\lambda$.

<!-- chunk {"id": "body-0044", "role": "body", "section": "VI-A Experimental Setup", "weight": 1.0} -->

\right)$ To compute $\mathcal{C}_{\text{obs}}{(x_{t}^{\tau})}$, we define it based on the collision conditions: where $\mathcal{C}_{\text{collision}}$ is the max collision cost, and $\mathcal{C}_{\text{local}}{(x_{t}^{\tau})}$ calculates the cost of robot footprint of the state based on the local costmap.

<!-- chunk {"id": "body-0045", "role": "body", "section": "VI-A Experimental Setup", "weight": 1.0} -->

We define the goal cost function $\mathcal{C}_{\text{goal}}{(x_{t}^{\tau},x_{\text{goal}})}$ as follows: where $\mathcal{C}_{\text{distance}}$ is the goal cost of the state where the collision happened along a trajectory $\tau$. It is important to note that if any state in a trajectory $\tau$ reaches the goal, we stop the cost calculation. This means the trajectory cost is measured up to the goal-reaching state.

<!-- chunk {"id": "body-0046", "role": "body", "section": "VI-B Uniformity Analysis", "weight": 1.0} -->

We investigate whether Neural C-Uniform can sample each level set uniformly beyond the training distribution (extrapolation in time). To do so, we estimate the number of occurrences of each $\mathbf{x}_{D,{t + 1}}$ in $L_{D,{t + 1}}$ when sampled from $\mathbf{x}_{D,t}$ of $L_{D,t}$ using $p_{\theta}{(\left. \mathcal{U} \middle| \mathbf{x}_{D,t} \right.)}$. We then calculate the entropy with uniform samples of each $\mathbf{x}_{D,{t + 1}}$ in $L_{D,{t + 1}}$. The uniformity percentage metric is defined as the entropy ratio between occurrence distribution using Neural C-Uniform and uniform distribution. We mainly perform the uniformity analysis for extrapolation in which the architecture is trained on level sets of 3 seconds with 0.2 discretization and is tested on 4 seconds 0.2 discretization.

<!-- chunk {"id": "body-0047", "role": "body", "section": "VI-B Uniformity Analysis", "weight": 1.0} -->

Fig. 3 shows the uniformity percentage of Neural C-Uniform on untrained level sets. It can be observed that Neural C-Uniform is able to maintain high uniformity.

<!-- chunk {"id": "body-0048", "role": "body", "section": "VI-C High Curvature Shortest Paths", "weight": 1.0} -->

The experiments evaluate the performance of both baseline methods and our approach in configuration-to-configuration (C2C) navigation tasks within an open-space environment. We consider the same robot system as in Eq. 1 over 4.5-second long trajectories. The initial state is fixed at $\mathbf{x}_{0} = {\lbrack 0,0,0\rbrack}$. The cost function $J$ is the same as Eq. 8, without the obstacle component. The cost weights are selected for each state element and the terminal cost as $\lambda_{\mathbf{x}} = {\lbrack 1.5,1.5,1.0\rbrack}$ and $\lambda_{\phi} = 20.0$. We use $\cos\psi$, and $\sin\psi$ for the heading representation for the cost calculations. We design two sets of experiments. In the first experiment, the goal is to come back to the initial state which requires a circular motion -- the highest curvature maneuver. Second, we showcase the navigation performance for three challenging C2C tasks, each requiring a full turn.

<!-- chunk {"id": "body-0049", "role": "body", "section": "VI-C High Curvature Shortest Paths", "weight": 1.0} -->

We run 10 trials for each method.

<!-- chunk {"id": "body-0050", "role": "body", "section": "VI-C High Curvature Shortest Paths", "weight": 1.0} -->

As shown in Fig. 4, Neural C-Uniform generates high-curvature turns that help identify the low-cost regions, and navigates the vehicle towards the goal configuration. Among the baselines, log-MPPI achieves the highest success rates, while others have issues as a result of non-diversity in trajectories and ineffective gradient approximation that lead them to a failure.

<!-- chunk {"id": "body-0051", "role": "body", "section": "VI-C High Curvature Shortest Paths", "weight": 1.0} -->

Fig. 5 highlights the differences in three more tasks: Fig. 5(a) shows the adaptability of the approaches that shifts the nominal trajectory for sampling. It can be seen that SVG-MPPI and our methods can directly identify the optimal regions while the other two MPPIs need some iterations to find the low-cost areas. However, when the gradient information gets lost due to the complexity of the cost landscape, SVG-MPPI method starts to struggle. Similarly, when the need for high-curvature increases, the performance of the MPPI and log-MPPI decreases.

<!-- chunk {"id": "body-0052", "role": "body", "section": "VI-D Dynamic Environment Simulation Experiments", "weight": 1.0} -->

We investigate the navigation performance in complex and dynamic settings on a set of simulation environments by sudden obstacles appearing at varying distances from the vehicle. We design a set of cluttered environments with predetermined positions of 10, 15, 20, 25, and 30 circular obstacles of radius 1m in an environment size of ${{35m} \times 10}m$, resulting in a total of 50 environments. The difficulty is defined by increasing the number of obstacles and simulating the obstacles as sudden appearances at reducing distances from the vehicle. In particular, the vehicle has a constant egocentric detection range of ${{3m} \times 3}m$ but the obstacle is only revealed to the vehicle if it is within the experiment distance threshold: 1.5m, 1.25m, 1m, and 0.5m. The shorter distances require more agility to react dynamically to obstacle appearing at different distances. Additionally, we also add small state noise to simulate localization error.

<!-- chunk {"id": "body-0053", "role": "body", "section": "VI-D Dynamic Environment Simulation Experiments", "weight": 1.0} -->

We evaluate the baselines on the dataset for success rate where success is defined when the vehicle reaches from initial location to goal location without any collisions. We choose one combination of initial and goal location for all the baselines and also compare the performance for different variance and number of trajectories. Table I shows the comparison of the average success rate across all environments and distance thresholds of our methods CU-MPPI and CU-LogMPPI to the baselines. We also report the success rate when the obstacle distance threshold is the lowest which is 0.5m to show the ability of the approaches to rapidly evade the obstacle.

<!-- chunk {"id": "body-0054", "role": "body", "section": "VI-E Cluttered Environments", "weight": 1.0} -->

We perform real-world and simulation experiments in cluttered environments. The BARN dataset is used to assess the performance of methods in both experiments. The simulation experiments were performed on the full BARN dataset, and the environments of real-world experiments are selected by separating the dataset into three difficulty groups and picking an environment from each group uniformly at random. These three environments are: Map 21 (easy) has relatively open areas, Map 110 (medium) has moderate clutter, and Map 289 (hard) has dense obstacles and narrow corridors. These maps provide a structured benchmark for assessing real-world navigation performance under varying difficulty levels. For these experiments, start and goal positions are fixed for all environments. Robot localization is performed using the Nav2 stack that employs the adaptive Monte Carlo localization method against a pre-built map, without pre-specified obstacle positions. The sensing range is clipped to a radius of 3 meters around the LiDAR sensor. Each controller setting was evaluated over 10 trials and controlled at a frequency of 10 Hz. SVG-MPPI is excluded from the real-world experiments because it cannot run at 10 Hz on Nvidia Jetson Xavier due to hardware limitations.

<!-- chunk {"id": "body-0055", "role": "body", "section": "VI-E Cluttered Environments", "weight": 1.0} -->

In simulation, SVG-MPPI achieved 0.85 and 0.87 success rates for variance setting 0.05 and 0.1 respectively.

<!-- chunk {"id": "body-0056", "role": "body", "section": "VI-E Cluttered Environments", "weight": 1.0} -->

Real Avg. Length(↓) TABLE II: Performance Comparison of Real-World and Simulation Experiments on Easy (E), Medium (M), and Hard (H) Cluttered Environments. The average trajectory length is computed using only the successful trials.

<!-- chunk {"id": "body-0057", "role": "body", "section": "VI-E Cluttered Environments", "weight": 1.0} -->

Table II shows the success rate reported and the average trajectory length among successful runs using 1500 trajectories for both simulation and real-world. Log-MPPI with a variance of 0.05 has a looping trajectory in the medium-difficulty environment, which increases the average trajectory length dramatically. CU-MPPI and CU-LogMPPI show higher success rates in medium and high-difficulty environments compared to baselines while maintaining a similar average trajectory length to Log-MPPI. In simulation, CU-MPPI and CU-LogMPPI outperform all the approaches by achieving 100% collision-free paths for all environments. The improved performance of all the approaches in simulation is directly related to the localization and hardware noise in real-world experiments. As an additional validation of the real-world applicability of our results, Figure 7 shows a side-by-side comparison of trajectories generated in real and simulation for the same environment.

<!-- chunk {"id": "body-0058", "role": "body", "section": "Conclusion", "weight": 1.5} -->

In this work, we presented a new approach to choose control input probabilities to sample trajectories which are C-Uniform: At each time step $t$, and for each subset $S$ of the level set $L_{t}$, the probability that the robot is in $S$ is proportional to the measure of $S$. In contrast to our previous work in which the probabilities are obtained by building a flow network based on a discretization of the configuration space, our new approach is based on learning the weights of a neural network which maps robot states to action probability distributions using entropy as unsupervised loss. It mitigates scalability issues of our previous approach in terms of both spatial resolution and time-horizon. Next, we showed how the C-Uniform trajectory sampler can be coupled with a local sampling-based gradient-follower to obtain a novel MPPI variant, CU-MPPI. Our method outperforms existing MPPI variants in high curvature settings.

<!-- chunk {"id": "body-0059", "role": "body", "section": "Conclusion", "weight": 1.5} -->

Our current implementation of CU-MPPI uses a pre-built map of the environment for localization (the obstacles are not necessarily pre-mapped). In our future work, we are planning to incorporate localization into navigation to remove this dependency.
