<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

FlowMP: Learning Motion Fields for Robot Planning with Conditional Flow Matching

Topics include Motion planning, Robotics, Diffusion models, Benchmarks, Planning, Learning, FlowMP.

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Prior flow matching methods in robotics have primarily learned velocity fields to morph one distribution of trajectories into another. In this work, we extend flow matching to capture second-order trajectory dynamics, incorporating acceleration effects either explicitly in the model or implicitly through the learning objective. Unlike diffusion models, which rely on a noisy forward process and iterative denoising steps, flow matching trains a continuous transformation (flow) that directly maps a simple prior distribution to the target trajectory distribution without any denoising procedure. By modeling trajectories with second-order dynamics, our approach ensures that generated robot motions are smooth and physically executable, avoiding the jerky or dynamically infeasible trajectories that first-order models might produce. We empirically demonstrate that this second-order conditional flow matching yields superior performance on motion planning benchmarks, achieving smoother trajectories and higher success rates than baseline planners. These findings highlight the advantage of learning acceleration-aware motion fields, as our method outperforms existing motion planning methods in terms of trajectory quality and planning success.

<!-- chunk {"id": "body-0003", "role": "body", "section": "Introduction", "weight": 1.5} -->

Motion planning is a fundamental problem in robotics, and its applications range from autonomous navigation to robotic manipulation. As robots are deployed in increasingly complex and dynamic environments, generating collision-free, smooth, and dynamically feasible trajectories is crucial for reliable operation. Traditional motion planning methods can be broadly classified into sampling-based and optimization-based approaches. Optimization-based motion planners, such as CHOMP and sequential convex optimization methods, aim to refine an initial trajectory by minimizing a cost functional that typically encodes factors such as smoothness, collision avoidance, and dynamic feasibility. Although these methods can produce locally optimal solutions, their performance is highly dependent on the quality of the initial guess. Poor initialization, often a simple straight-line interpolation in configuration space, can lead to the convergence of suboptimal solutions or even complete failure, particularly in environments with narrow passages or cluttered obstacles. Sampling-based methods like RRT-Connect guarantee probabilistic completeness by exploring the configuration space through random sampling. However, the trajectories produced by these methods are typically jerky and require additional smoothing or optimization steps to be suitable for execution in real robotic systems.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

These limitations have motivated the search for more informed trajectory priors to guide planners toward high-quality solutions. Rather than sampling a new path from scratch, early work draws on a library of solution trajectories to warm-start the planner. However, as the state dimension and database size grow, such memory-based methods suffer from the *curse of dimensionality*. Subsequent approaches address this limitation by learning mappings from task parameters to trajectories. For instance, Mansard et al. used a neural network to predict an initial trajectory for a given task. In contrast, Lembono et al., and Power et al. learned distributions of trajectories that allow sampling of diverse candidate paths.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

Another line of research incorporates demonstrations of bias motion planning. Koert et al. introduced Demonstration-Based Trajectory Optimization (DEBATO), which encodes demonstrated motions as a probabilistic movement primitive (ProMP) and then optimizes the trajectory using a combination of collision avoidance and adherence to the ProMP prior through relative entropy policy search. Rana et al. proposed a Gaussian Process-based prior (CLAMP) to learn from demonstrations. In contrast, Urain et al. used an energy-based model to capture multimodal trajectory distributions. However, these approaches are generally unimodal or computationally intensive when handling complex, multimodal tasks.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

Deep generative models have emerged as a promising way to represent complex trajectory distributions beyond the limitations of traditional parametric priors. Variational Autoencoders (VAE) and Generative Adversarial Networks (GAN) have been applied to learn data-driven priors but often struggle with training instabilities or mode collapse. Energy-based models offer another avenue, although they can be challenging to train and sample from effectively. More recently, diffusion models have gained traction in capturing complex multimodal trajectory distributions. In particular, Carvalho et al. introduced Motion Planning Diffusion (MPD), which uses diffusion models to generate robot trajectories conditioned on task constraints. However, these typically operate by simulating iterative denoising steps and usually model only first-order dynamics (e.g., joint positions and velocities), which can result in trajectories lacking smooth acceleration profiles.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

In this work, we propose to address these limitations by leveraging *flow matching* as an alternative generative modeling technique for motion planning. Flow matching directly learns a continuous transformation---a motion field---that transports a simple prior distribution (e.g., Gaussian noise) to the distribution of expert trajectories without iterative denoising. Moreover, we extend the standard flow-matching approach by incorporating second-order trajectory dynamics, explicitly modeling acceleration alongside velocity to generate smoother and more dynamically feasible trajectories. Our contributions are twofold.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Introduction", "weight": 1.5} -->

We introduce a conditional flow matching framework as a trajectory prior based on B-Spline representation to robot motion planning, offering a simulation-free, direct mapping from noise to feasible trajectories.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Introduction", "weight": 1.5} -->

We extend the flow matching approach to capture second-order dynamics, ensuring that the generated trajectories exhibit continuous velocity and acceleration profiles, critical for real-world robotic execution.

<!-- chunk {"id": "body-0010", "role": "body", "section": "III-A Expert Via-Points Construction", "weight": 1.0} -->

To find smooth and time-optimal trajectories going through optimal via-points $\mathbf{q}_{\text{via}}^{\ast}$, the cost function is minimized in the phase domain $\mathcal{S} \in {\lbrack 0,1\rbrack}$ (or $t = {0,1,\ldots,T}$): where $c{(\cdot)}$ is a task-specific cost function of collision avoidance, timing, and smoothness for kinodynamically valid and smooth trajectories, and $\overset{˙}{\mathbf{q}}{(s)}$, $\overset{¨}{\mathbf{q}}{(s)}$ are derivatives of Eq. 1.

<!-- chunk {"id": "body-0011", "role": "body", "section": "III-A Expert Via-Points Construction", "weight": 1.0} -->

The optimal via-points $\mathbf{q}_{\text{via}}$ for smooth and task-specific trajectories are optimized via the Covariance Matrix Adaptation Evolution Strategy (CMA-ES) algorithm by searching the via-point space and iteratively sampling candidate via-points from a Gaussian distribution $\mathcal{N}{(\mu_{\text{via}},\mathbf{\Sigma}_{\text{via}})}$, where $\mu_{\text{via}}$ is the mean and $\mathbf{\Sigma}_{\text{via}}$ is the covariance matrix.

<!-- chunk {"id": "body-0012", "role": "body", "section": "III-A Expert Via-Points Construction", "weight": 1.0} -->

Each sampled set of via-points generates a trajectory through the parameterization in Eq. 1 and is evaluated using the cost function in Eq. 2. CMA-ES then updates $\mu_{\text{via}}$ and $\mathbf{\Sigma}_{\text{via}}$ based on the evaluated costs, favoring candidate trajectories with lower costs and an optimal set of via-points $\mathbf{q}_{\text{via}}^{\ast}$.

<!-- chunk {"id": "body-0013", "role": "body", "section": "III-A Expert Via-Points Construction", "weight": 1.0} -->

Using noisy via-points ${\overset{\sim}{\mathbf{q}}}_{\text{via}}^{\ast}$, the B-splines are constructed with $\mathcal{C}_{3}^{i}{(t)}$ as cubic basis functions parametrized by time: Respectively, the first and second derivatives of $\mathbf{q}{(t)}$ are collected, which are velocities and accelerations profiles. This trajectory construction, therefore, serves as the expert motion distribution between two random pairs of points.

<!-- chunk {"id": "body-0014", "role": "body", "section": "III-B Conditional Motion Field", "weight": 1.0} -->

To ensure the warm start for robot motions, we learn the distributions of positions, $\mathbf{Q}$, of expert paths along with their derivatives of positions, $\overset{˙}{\mathbf{Q}}$ and $\overset{¨}{\mathbf{Q}}$ through conditional motion fields. We divide this motion field into velocity, acceleration, and jerk fields, corresponding to learning factors for position, velocity, and acceleration profiles of the trajectories, respectively. These conditional motion fields are learnable parameters that transition from noise to our target motion distributions via multiple probabilistic flow paths.

<!-- chunk {"id": "body-0015", "role": "body", "section": "III-B3 Conditional Jerk Field", "weight": 1.0} -->

\overset{¨}{\mathbf{q}} \middle| {\overset{¨}{\mathbf{q}}}_{1} \right.)}} = {{({{\overset{¨}{\mathbf{q}}}_{1} - \overset{¨}{\mathbf{q}}})}/{({1 - t})}}$ as the condition jerk field, resulting in the jerk field loss $\mathcal{L}{(\theta_{3})}$: Leveraging Eq. 7, Eq. 9, and Eq. 11, we simultaneously train velocity, acceleration, and jerk fields, so-called motion field, $\Upsilon = \left\{ \mathbf{u},\mathbf{v},\mathbf{w} \right\}$ as depicted in Alg.

<!-- chunk {"id": "body-0016", "role": "body", "section": "III-C Motion Field Inference", "weight": 1.0} -->

With the trained motion field prior distribution $\pi_{1}$ in an environment, we can sample the field from the posterior $p{(\left. \Upsilon \middle| \mathcal{O} \right.)}$ given a task objective $\mathcal{O}$. Let $p{(\left. \mathcal{O} \middle| \Upsilon \right.)}$ as the objective likelihood, we have: assumming the likelihood factorizes as with $\lambda_{j} > 0$: Assuming the likelihood having the exponential form ${p_{j}{(\left.

<!-- chunk {"id": "body-0017", "role": "body", "section": "III-C Motion Field Inference", "weight": 1.0} -->

\mathcal{O}_{j} \middle| \Upsilon \right.)}} \propto {\exp{({- {C_{j}{(\Upsilon)}}})}}$, we perform Maximum-a-Posteriori (MAP) on the trajectory posterior: with the gradient derived from $i^{th}$ inference step of Eq. 14: Figure 3: The conditional motion field is extended to 3D space, where collision-free paths are denoised along the time horizon t from 0 to 1 within a obstacle map from the initial noises covering the workspace. The model is trained on expert motion distributions with various task objectives in the pre-defined 3D space using Alg. 1. Three example motions are sampled with the generate_motion function, where Path 1 and Path 3 start from different initial positions but go to the same goal, whereas Path 2 follows a distinct trajectory with unique start and goal points. Velocity (blue, orange, and violet) and acceleration (green, yellow, and apricot) profiles on three axes are sampled from their respective noise distributions. At t = 1, the trajectories and their derivatives are smooth.

<!-- chunk {"id": "body-0018", "role": "body", "section": "III-C Motion Field Inference", "weight": 1.0} -->

Given that the expert prior distribution $\pi_{1}$ provides sufficient coverage of the objective distribution $\mathcal{O}$, and the learned motion field $\Upsilon_{t}^{\theta_{1},\theta_{2},\theta_{3}}$ is parameterized by trainable parameters $(\theta_{1},\theta_{2},\theta_{3})$ bridging $\pi_{0}$ and $\pi_{1}$, it follows that the learned motion field $\Upsilon$ acts as a transport operator mapping any sub-distribution of $\pi_{0}$ to a corresponding sub-distribution of $\pi_{1}$.

<!-- chunk {"id": "body-0019", "role": "body", "section": "III-C Motion Field Inference", "weight": 1.0} -->

In this case, the likelihood acts as an out-of-distribution guidance, straightforwardly leading to the posterior flow $\Upsilon_{t_{i}}^{\mathcal{O}} = {{\mathbf{g}}_{t_{i}} + {\lambda_{\text{prior}}\Upsilon_{t_{i}}^{\theta_{1},\theta_{2},\theta_{3}}}}$. Consequently, this guarantees that the optimization process preserves the statistical consistency required for task success, reinforcing the theoretical validity of the learned motion dynamics.

<!-- chunk {"id": "body-0020", "role": "body", "section": "III-C Motion Field Inference", "weight": 1.0} -->

In particular, the prior sampling mechanism (Eq. 13) can be formulated as a fourth-order Runge-Kutta integration that propagates the motion field over the specified time horizon: where $f = f_{\theta_{1},\theta_{2},\theta_{3}}$ represents our trained model leading $\pi_{0}$ to $\pi_{1}$, $t_{i}$ is timestamps from $0$ to $1$, and $\delta$ is the time step, which is equivalent to the underlying diffusion step in Eq. 13 in this context of motion field.

<!-- chunk {"id": "body-0021", "role": "body", "section": "III-C Motion Field Inference", "weight": 1.0} -->

Alg. 1 recaps the training and inference processes. A sampling example is shown under motion fields in Fig. 2, resulting in smooth trajectories, velocity, and acceleration profiles with different task objectives in a maze environment. Fig. 3 further illustrates the extension of a conditional motion field in 3D space, where initially scattered samples are progressively refined into structured, collision-free paths as time progresses from $t = 0$ to $t = 1$. The top row shows the denoising process, where samples converge towards feasible trajectories. Meanwhile, the bottom row presents velocity and acceleration profiles, sampled from their respective noise distributions, demonstrating how different motion objectives shape the resulting kinematics. Both Fig. 2 and Fig. 3 demonstrate denoised motions with a sampling size of 200.

<!-- chunk {"id": "body-0022", "role": "body", "section": "Evaluations & Experiments", "weight": 1.0} -->

We evaluate FlowMP against other baseline motion planners, including Stoch-GPMP and MPD in terms of planning feasibility, trajectory smoothness, integration error, and inference time on the NVIDIA RTX 4070 GPU. All methods are made to generate a batch of $25$ trajectories during inference. Each runs with different trajectory lengths: $64$, $128$, and $256$. Stoch-GPMP runs with 700 iterations with a $\sigma_{GP}$ of $0.1$ for 2D environments and a $\sigma_{GP}$ of $0.0007$ for 3D environments, MPD infers the paths with three of their variants: diffusion prior (DP), diffusion prior then guide (DG), and their original approach. Both Stoch-GPMP and MPD only generate trajectories with velocities. In contrast, FlowMP additionally infers acceleration profiles alongside positions and velocities. For MPD and FlowMP, we run them at the same denoising steps of $30$ for comparison fairness.

<!-- chunk {"id": "body-0023", "role": "body", "section": "IV-A Planning Feasibilty", "weight": 1.0} -->

First, we experiment with FlowMP, Stoch-GPMP, and MPD on RobotPointMass and PandaSphere environments to see their planning feasibility with varied-length paths. Table I and Table II show that Stoch-GPMP and FlowMP succeed in planning trajectories with diverse lengths. However, MPD raises scalability concerns as it collapses the trajectories with lengths of more than 64. This experiment proves that FlowMP is more scalable than MPD as a diffusion-based global planner while avoiding the myoptic failures of local planning-based methods.

<!-- chunk {"id": "body-0024", "role": "body", "section": "IV-B Trajectory Smoothness", "weight": 1.0} -->

Next, with generated valid collision-free trajectories, we evaluate their smoothness to guarantee that a robot can physically execute the motion while maintaining control feasibility. We simply compute the sum of point-to-point slopes from one end to another of a best generated trajectory. As shown in Table IV, the results show that our trajectories are smoother compared to MPD, achieving second-best in RobotPointMass environment and smoothest in PandaSphere environment.

<!-- chunk {"id": "body-0025", "role": "body", "section": "IV-C Integration Error", "weight": 1.0} -->

Furthermore, we utilize the Romberg quadrature method to quantify the integration error between the start and end points along dimensional axes of the best generated trajectory ($L = 64$) for all baselines and FlowMP, as shown in Table V. This metric depicts that FlowMP achieves lower integrative error than MPD in RobotPointMass and PandaSphere environments. Meanwhile, Stoch-GPMP has the least errors in both cases.

<!-- chunk {"id": "body-0026", "role": "body", "section": "IV-D Inference Time", "weight": 1.0} -->

Lastly, we inspect the average inference time with each experiment's standard deviation (in seconds). Table III reports that FlowMP achieves sub-$0.1$ seconds of mean inference time in RobotPointMass environment with all inspected trajectory lengths. Meanwhile, in PandaSphere environment, we achieve a slightly faster inference time than MPD diffusion prior inference. This experiment showcases that FlowMP is well-suited for real-time deployment with GPU-acceleration on a robot platform.

<!-- chunk {"id": "body-0027", "role": "body", "section": "IV-E Real-Robot Experiments", "weight": 1.0} -->

We input $20$ collision-free, dynamically feasible trajectories with $L = 256$ and state dimension ${\mathbf{ξ}} = {\{ q_{i},{\overset{˙}{q}}_{i},{\overset{¨}{q}}_{i}\}} \in {\mathbb{R}}^{21}$ to drive the Kinova Gen3 manipulator from the starting region to the goal region. FlowMP has a size of $4.5$ MB of $362,922$ trainble parameters. The inference runs on an Intel Core i9-14900 CPU and an NVIDIA RTX 4080S GPU, achieving an inference speed of approximately $0.1$ seconds. Fig. 1 presents the experimental results of executing a smooth, dynamically feasible motion on the Kinova Gen3 manipulator. Given the same start and goal configurations, FlowMP generates multiple valid solutions, demonstrating its ability to capture different modes of trajectory distribution.

<!-- chunk {"id": "body-0028", "role": "body", "section": "IV-E Real-Robot Experiments", "weight": 1.0} -->

Furthermore, when varying the start and goal within a close region, the resulting motions remain smooth and dynamically feasible, making them directly practical to the robotic system, as shown in Fig. 1. The demonstration video of the experiments can be seen in the supplementary document.

<!-- chunk {"id": "body-0029", "role": "body", "section": "Conclusions", "weight": 1.0} -->

We introduced FlowMP---a framework that leverages conditional flow matching to learn motion fields for generating smooth and dynamically feasible trajectories. Using flow matching to encode trajectory distribution and capture second-order trajectory dynamics, our approach directly models acceleration profiles alongside velocity, ensuring physically executable trajectories without requiring iterative denoising steps. Through evaluations, FlowMP demonstrated superior performance over MPD and bare trajectory optimizer in terms of trajectory quality, inference speed, and planning feasibility across both planar and robot environments. Our method not only achieves $\times 2$ faster inference times with scaling trajectory horizon but also maintains trajectory smoothness and scalability for varying trajectory lengths, addressing key limitations in prior diffusion-based approaches. Furthermore, real-robot experiments confirm FlowMP's practical applicability in robotic manipulation tasks with very few or no blending steps, highlighting its potential for real-world deployment, even sampling directly from prior.
