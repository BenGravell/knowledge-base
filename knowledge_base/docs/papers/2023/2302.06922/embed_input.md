<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Autotuning Symbolic Optimization Fabrics for Trajectory Generation

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

In this paper, we present an automated parameter optimization method for trajectory generation. We formulate parameter optimization as a constrained optimization problem that can be effectively solved using Bayesian optimization. While the approach is generic to any trajectory generation method, we showcase it using optimization fabrics. Optimization fabrics are a geometric trajectory generation method based on non-Riemannian geometry. By symbolically pre-solving the structure of the tree of fabrics, we obtain a parameterized trajectory generator, called symbolic fabrics. We show that autotuned symbolic fabrics reach expert-level performance in a few trials. Additionally, we show that tuning transfers across different robots, motion planning problems and between simulation and real world. Finally, we qualitatively showcase that the framework could be used for coupled mobile manipulation.

<!-- chunk {"id": "body-0003", "role": "body", "section": "Introduction", "weight": 1.5} -->

Mobile manipulation is the field of robotics concerned with highly capable robots characterized by their locomotion and manipulation ability. Such robots are getting ever more attention as they will be deployed to human-shared environments, like households or warehouses. In such dynamic environments, fast trajectory generation is crucial to avoid collisions and react quickly to changing goal definitions.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

Trajectory generation is often addressed by solving an optimization problem that consists of a scalar objective function -- the dynamics or transition function -- and several constraints. As the degrees of freedom and number of constraints increase, solving that problem in real-time becomes challenging. This is especially limiting in the case of mobile manipulation. Optimization fabrics represent a different approach to the problem, as they formulate trajectory generation as the shortest-geodesic-problem in a manifold of the configuration space.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

With optimization fabrics, different components, or desired behaviors, such as collision avoidance and joint limit avoidance, are combined using Riemannian metrics. As the structure of the resulting trajectory generation methods remains unchanged across all time steps, it can be composed before runtime, thus saving computational costs during executing. Optimization fabrics, but also their predecessor Riemannian Motion Policies (RMPs), have shown impressive results for several manipulator applications, including dynamic and crowded environments. However, despite their theoretical properties of inherent collision avoidance and convergence, these methods require expertise and intuition to tune individual components to generate smooth and well-behaving trajectories.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

To address this issue, we formulate optimization fabrics as a symbolic trajectory generation method. Precisely, the combination of the individual components (joint limit avoidance, goal reaching, collision avoidance, etc.) is performed in a parameterized way before runtime. Separating composition and evaluation allows for changing the individual parameters at runtime while achieving low computational costs. Additionally, this allows formulating parameter-tuning as a constrained optimization problem. Solving this problem effectively automates the tuning process systematically using Bayesian optimization. We show that automated tuning requires only few trials to achieve similar performance to an expert in the field, and systematically outperforms a randomized parameter setting. Moreover, we show that one parameter tuning generalizes across different robots, to some extent, across different tasks and between simulation and real world. Finally, we demonstrate how coupled mobile manipulation with a differential drive can be achieved using autotuned optimization fabrics for in-store order-picking integrating visual servoing.

<!-- chunk {"id": "body-0007", "role": "body", "section": "II-A Geometric control for trajectory generation", "weight": 1.0} -->

Operational space control was the first control method that imposed a desired dynamical system onto a robotic system. The concept was an important step toward naturally controlling kinematically redundant robots. The concept was formalized in the field of geometric control, where the study of differential geometry leads to stable and converging behavior under geometric conditions. More recently, RMPs for manipulation tasks offered a highly reactive trajectory generation method. This method achieves composable behavior by introducing a split between the importance metric and the forcing term. Using the pullback and pushforward operator to change between manifolds of the configuration space, individual components, such as collision avoidance and goal attraction, can be designed iteratively. However, RMPs require intuition and experience when being designed, and convergence can only be proven conditionally. Later, optimization fabrics were introduced that are able to completely decouple importance metrics and the defining geometry. Under simple construction rules for these two components, convergence can be easily guaranteed. In our prior work on optimization fabrics, the framework was first applied to mobile manipulation and generalized to more dynamic environments..

<!-- chunk {"id": "body-0008", "role": "body", "section": "II-B Autotuning for trajectory generation", "weight": 1.0} -->

Autotuning can be beneficial for trajectory generation when using model predictive control. In, an autotuned model predictive controller has outperformed a manual tuned controller of the same kind by 25%. Jointly optimizing parameters and the model of the controller, AutoMPC showed the benefit of parameter tuning in the context of simultaneous system identification and control. These methods are explicitly formulated for model predictive control and do not transfer easily to other trajectory generation methods. In contrast, we propose a generic parameter optimization approach to trajectory generation.

<!-- chunk {"id": "body-0009", "role": "body", "section": "II-C Hyperparameter tuning in machine learning", "weight": 1.0} -->

Within the machine-learning field, hyperparameter tuning has shown to be highly important for all different kinds of applications. Parameter optimization aims to minimize training costs while achieving the best possible performance. Hyperparameter tuning is most valuable in extremely costly applications such as reinforcement learning. Generally, two different search algorithms have been investigated: grid search and random search. Current state-of-the-art methods for parameter search are based on random search with a Bayesian optimizer. While the machine-learning community has largely agreed on the importance of parameter tuning, systematic tuning of trajectory generation methods are not well established. In this paper, we showcase, with the example of optimization fabrics, how important parameter tuning is and how trajectory generation can benefit from it.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Overview", "weight": 1.0} -->

In this paper, we first recall very briefly the theory of optimization fabrics and the steps to use it for trajectory generation (Section IV). Then, we formulate optimization fabrics as a symbolic trajectory generator, so that combining of individual components is only performed once (Section V). Then, we formulate parameter tuning for trajectory generation as a constrained optimization problem and propose Bayesian optimization for effective autotuning (Section VI). As an example, we apply this autotuning to symbolic optimization fabrics (Section VII), but it is generally independent of the trajectory generator at hand.

<!-- chunk {"id": "body-0011", "role": "body", "section": "IV-A Configurations and task variables", "weight": 1.0} -->

We denote ${\mathbf{q}} \in \mathcal{Q} \subset {\mathbb{R}}^{n}$ a configuration of the robot with $n$ its degrees of freedom; $\mathcal{Q}$ is the configuration space of the generalized coordinates of the system. Generally, ${\mathbf{q}}{(t)}$ defines the robot's configuration at time $t$, so that $\overset{˙}{\mathbf{q}}$, $\overset{¨}{\mathbf{q}}$ define the instantaneous derivatives of the robot's configuration. Similarly, we assume that there is a set of task variables ${\mathbf{x}}_{j} \in \mathcal{X}_{j} \subset {\mathbb{R}}^{m_{j}}$ with variable dimension $m_{j} \leq n$.

<!-- chunk {"id": "body-0012", "role": "body", "section": "IV-A Configurations and task variables", "weight": 1.0} -->

The task space $\mathcal{X}_{j}$ defines an arbitrary manifold of the configuration space $\mathcal{Q}$ in which a robotic task can be represented. Further, we assume that there is a differential map $\phi_{j}:{{\mathbb{R}}^{n}\rightarrow{\mathbb{R}}^{m_{j}}}$ that relates the configuration space to the $j^{th}$ task space. For example, when a task variable is defined as the end-effector position, then $\phi_{j}$ is the positional part of the forward kinematics. On the other hand, if a task variable is defined to be the joint position, then $\phi_{j}$ is the identity function. In the following, we drop the subscript $j$ in most cases for readability when the context is clear.

<!-- chunk {"id": "body-0013", "role": "body", "section": "IV-B Spectral semi-sprays", "weight": 1.0} -->

Inspired by simple mechanics (e.g., the simple pendulum), the framework of optimization fabrics designs motion policies as second-order dynamical systems $\overset{¨}{\mathbf{x}} = {\pi{({\mathbf{x}},\overset{˙}{\mathbf{x}})}}$. The motion policy is defined by the differential equation ${{{\mathbf{M}}\overset{¨}{\mathbf{x}}} + {\mathbf{f}}} = 0$, where ${\mathbf{M}}{({\mathbf{x}},\overset{˙}{\mathbf{x}})}$ and ${\mathbf{f}}{({\mathbf{x}},\overset{˙}{\mathbf{x}})}$ are functions of position and velocity. Besides, $\mathbf{M}$ is symmetric and invertible.

<!-- chunk {"id": "body-0014", "role": "body", "section": "IV-B Spectral semi-sprays", "weight": 1.0} -->

We denote such systems as $\mathcal{S} = ({\mathbf{M}},{\mathbf{f}})_{\mathcal{X}}$ and refer to them as spectral semi-sprays, or specs for short. When the space of the task variable is clear from the context, we drop the subscript.

<!-- chunk {"id": "body-0015", "role": "body", "section": "IV-C Operations on specs", "weight": 1.0} -->

Complex trajectory generation is composed of multiple components, such as collision avoidance, joint limits avoidance, etc. The power of optimization fabrics lies in the metric-weighted sum to combine multiple components from different manifolds. These operations are derived from operations on specs and are briefly recalled here.

<!-- chunk {"id": "body-0016", "role": "body", "section": "IV-C Operations on specs", "weight": 1.0} -->

Given a differential map $\phi:{\mathcal{Q}\rightarrow\mathcal{X}}$ and a spec $({\mathbf{M}},{\mathbf{f}})_{\mathcal{X}}$, the pullback is defined as The pullback allows converting between two distinct manifolds (e.g. a spec could be defined in the robot's workspace and pulled into the robot's configuration space using the pullback with $\phi$ being the forward kinematics).

<!-- chunk {"id": "body-0017", "role": "body", "section": "IV-C Operations on specs", "weight": 1.0} -->

With spectral semi-sprays and the presented operations, avoidance behavior, such as joint limit avoidance, collision avoidance or self-collision avoidance, can be realized.

<!-- chunk {"id": "body-0018", "role": "body", "section": "IV-D Optimization fabrics", "weight": 1.0} -->

In the previous subsection, we explained how different avoidance behaviors can be combined. Spectral semi-sprays can additionally be forced by a potential, denoted as the forced variant of form $\mathcal{S}_{\mathbf{ψ}} = \left( {\mathbf{M}},{{\mathbf{f}} + {\partial_{\mathbf{x}}{\mathbf{ψ}}}} \right)$. This forcing term clearly changes the behavior of the system. Optimization fabrics introduce construction rules to make sure that the solution path ${\mathbf{x}}{(t)}$ of $\mathcal{S}_{\mathbf{ψ}}$ converges towards the minimum of ${\mathbf{ψ}}{({\mathbf{x}})}$. Then, the potential is designed in such a way that its minimum represents a goal state of the motion planning problem.

<!-- chunk {"id": "body-0019", "role": "body", "section": "IV-D Optimization fabrics", "weight": 1.0} -->

The property of homogeneity of degree 2 and the energization with the Finsler structure guarantees, according to \[11, Theorem 4.29\], that the energized spec forms a frictionless fabric. A frictionless fabric is defined to optimize the forcing potential $\mathbf{ψ}$ when being damped by a positive definite damping term \[11, Definition 4.4\]. Thirdly, all avoidance components are combined in the configuration space of the robot using the pullback and summation operation (Combination). Note, that both operations are closed under the algebra designed by these operations, i.e. every pulled optimization fabric or the sum of two optimization fabrics is, itself, an optimization fabric. In the last step, the combined spec is forced by the potential $\mathbf{ψ}$ with the desired minimum and damped with a positive definite damping term (Forcing).

<!-- chunk {"id": "body-0020", "role": "body", "section": "Symbolic fabrics", "weight": 1.0} -->

A trajectory generator that is based on optimization fabrics is composed of several components, such as collision avoidance, joint limit avoidance, goal attraction, etc. Each component contributes to the resulting optimization fabric through the metric-weighted summation that creates the tree of fabrics. The trajectory generator is parameterized by the individual terms of the components. Here, we lay out the parameterization for collision avoidance, joint limit avoidance, self-collision avoidance, and speed-control. In our framework, the tree of fabrics is generated before runtime as a symbolic expression, to which the parameters are set at runtime. Note that the approach of symbolic pre-solving results in much higher planning frequencies. In the following, we explain the individual parameters that we exposed symbolically. The form of the individual terms is adapted from but written in a symbolic form.

<!-- chunk {"id": "body-0021", "role": "body", "section": "Basic inertia", "weight": 1.0} -->

The final tree of fabrics is equipped with a basic inertia metric that indicates how reactive the entire motion is. This basic inertia metric is derived from the symbolic Finsler structure: $\mathcal{L}_{e} = {0.5m_{\text{base}}{\overset{˙}{\mathbf{q}}}^{T}{\mathbf{I}}\overset{˙}{\mathbf{q}}}$.

<!-- chunk {"id": "body-0022", "role": "body", "section": "Collision avoidance", "weight": 1.0} -->

For collision avoidance, the task manifold $\mathcal{X}$ is defined by the distance function between an obstacle and a robot link. The differential map used is defined as where $\text{fk}_{\text{i}}{({\mathbf{q}})}$ is the positional forward kinematics for link $i$ in a configuration $\mathbf{q}$, $r_{\text{obst}}$ and $r_{\text{i}}$ are the radii of the englobing spheres for the obstacle and the link respectively. While this mapping between configuration space and task manifold is different for each obstacle and each collision link of the robot, the geometry and metric are the same for all of them.

<!-- chunk {"id": "body-0023", "role": "body", "section": "Collision avoidance", "weight": 1.0} -->

For the geometry ${\overset{¨}{\mathbf{x}} + {{\mathbf{h}}{({\mathbf{x}},\overset{˙}{\mathbf{x}})}}} = \mathbf{0}$, we use the parameterized forcing term where $k_{\text{geo,col}}$ and $\beta_{\text{geo,col}}$ are parameters of the trajectory generator. Generally, we use $k$ and $\beta$ for proportional parameters and exponential parameters. The Finsler structure for collision avoidance is parameterized as where $\text{sgn}{(\overset{˙}{\mathbf{x}})}$ is the signum-operator returning the sign of $\overset{˙}{\mathbf{x}}$.

<!-- chunk {"id": "body-0024", "role": "body", "section": "Self-collision avoidance", "weight": 1.0} -->

For self-collision avoidance, the task manifold $\mathcal{X}$ is defined similarly to collision avoidance: where $\text{fk}_{i}{({\mathbf{q}})}$ and $\text{fk}_{j}{({\mathbf{q}})}$ are the positional forward kinematics of the two links for a self-collision pair and $r_{i}$ and $r_{j}$ are the radii for both englobing spheres. The geometries are defined analogously The Finsler structure for collision avoidance is parameterized as

<!-- chunk {"id": "body-0025", "role": "body", "section": "Joint limit avoidance", "weight": 1.0} -->

For joint-limit avoidance, two simple differential maps denoting the distance to the joint limits are used, specifically Similar to collision avoidance, we use the parameterized forcing term and the Finsler structure

<!-- chunk {"id": "body-0026", "role": "body", "section": "Speed control", "weight": 1.0} -->

As the root of the tree of fabrics is a frictionless fabric, it only converges if damped. Constant damping is sufficient to achieve the theoretical properties that are needed for trajectory generation. However, proposed enhanced damping under the name of speedcontrol. We employ the same damping strategy while adding parameterization. The technique is based on a dynamic damping modification based on the distance to the goal.

<!-- chunk {"id": "body-0027", "role": "body", "section": "Speed control", "weight": 1.0} -->

Specifically, the final optimization fabric is damped according to where ${\mathbf{h}}_{2}$ is the sum of all pulled forcing terms, $\mathbf{M}$ is the sum of all metrics of the individual geometries, $\partial_{\mathbf{q}}{\mathbf{ψ}}$ is the goal attraction term pulled in the configuration space, $\alpha_{\text{ex}}$ is a weighted sum of $\alpha_{\text{ex}}^{0}$ that maintains constant execution energy without goal attraction and $\alpha_{\text{ex}}^{\mathbf{ψ}}$ that maintains constant execution energy with goal attraction: Then, $\beta$ is the damping term, computed as: where ${\mathbf{B}}_{\text{max}}$ and ${\mathbf{B}}_{\text{min}}$ are the upper and lower damping values and $\alpha_{\mathcal{L}_{e}}$ is the energization coefficient maintaining constant system energy (not execution

<!-- chunk {"id": "body-0028", "role": "body", "section": "Speed control", "weight": 1.0} -->

The switching functions ${\mathbf{s}}_{\beta}{({\mathbf{q}})}$, ${\mathbf{s}}_{\eta}{({\mathbf{q}})}$ are further parameterized as where $r_{shift}$ determines the distance to the goal at which the switch between ${\mathbf{B}}_{\text{min}}$ and ${\mathbf{B}}_{\text{max}}$ occurs, $\alpha_{\beta}$ is the steepness of that switching, $\mathcal{L}_{ex}$ is the user-defined execution energy (usually a simple kinetic energy in joint space) and $v_{ex}$ is the execution energy factor, i.e. it determines the desired speed of motion. For a detailed discussion on speed control with optimization fabrics, we refer to previous works on optimization fabrics.

<!-- chunk {"id": "body-0029", "role": "body", "section": "Speed control", "weight": 1.0} -->

We group all parameters resulting from the symbolic fabrics defined here into a vector of parameters $\mathbf{\Theta}$. All parameters are listed in Table I.

<!-- chunk {"id": "body-0030", "role": "body", "section": "Parameter tuning as an optimization problem", "weight": 1.0} -->

We define parameter tuning as a constrained optimization problem: where $\mathbf{\Theta}_{\text{max}}$ and $\mathbf{\Theta}_{\text{min}}$ are the upper and lower bounds of the parameters. The objective $c{(\mathbf{\Theta})}$ is a function of the parameters specifying the tree of fabrics and can be evaluated after one trajectory planning problem has finished. We call the evaluation of one parameter set a trial. Next, we propose an objective function that is flexible as different scenarios may require different parameter tuning.

<!-- chunk {"id": "body-0031", "role": "body", "section": "VI-A Objective", "weight": 1.0} -->

The objective function $c{(\mathbf{\Theta})}$ is a weighted sum of several metrics, that are invariant to the robot: $c_{\text{distance}}$ accounts for the normalized, summed distance to the goal over one trial and is defined as where $i \in {\lbrack 0,T\rbrack}$ are the discretized time steps and ${\mathbf{x}}_{\text{goal}}$ is the goal of the motion planning problem. $c_{\text{path}}$ accounts for the normalized path length over one trial and is defined as $c_{\text{clearance}}$ accounts for the average clearance to obstacles over one trial and is defined as where $o_{i}^{j}$ is the position of obstacle $j$ at time step $i$. Each of these terms is evaluated after an entire trial that was obtained by a specific set of parameters.

<!-- chunk {"id": "body-0032", "role": "body", "section": "VI-A Objective", "weight": 1.0} -->

1Formulate trajectory generator with parameters Θ 2 Define parameter space by Θmin, Θmax 4 Initialize objective function estimate $\overset{\sim}{c}{(\mathbf{\Theta})}$ 6 Suggest parameter Θi based on $\overset{\sim}{c}{(\mathbf{\Theta})}$ 8 Compute action with parameter set Θi 9 Apply action to robot 10 Store observation relevant for metrics 14 Update $\overset{\sim}{c}{(\mathbf{\Theta})}$ 17Extract the best parameter set Θbest Algorithm 1 Autotuning for trajectory generators

<!-- chunk {"id": "body-0033", "role": "body", "section": "VI-B Bayesian optimization", "weight": 1.0} -->

In the tuning phase, the problem specification for the investigated scenario, e.g., the goal and obstacle positions, across all trials during tuning remains the same while $\mathbf{\Theta}$ are optimized according to the objective. To solve the Bayesian optimization we employ the Tree-structured Parzen Estimator as it has shown improved performance over grid-search and conventional random search in machine learning applications. To deploy this technique we used Optuna, a hyperparameter optimization framework initially designed for machine learning applications. The general setup for one trial is shown in Fig. 1 and the procedure is summarized in Algorithm 1.

<!-- chunk {"id": "body-0034", "role": "body", "section": "Experimental Results", "weight": 1.0} -->

We showcase our parameter optimization method for symbolic fabrics. The search space for the parameters is summarized in Table I.

<!-- chunk {"id": "body-0035", "role": "body", "section": "Experimental Results", "weight": 1.0} -->

We first analyze the importance of tuning for optimization fabrics on the performance of trajectory generation. Then, we investigate how tuned parameters can be transferred across different robots (Section VII-C), different scenarios (Section VII-D), and between simulation and real world (Section VII-E).

<!-- chunk {"id": "body-0036", "role": "body", "section": "VII-A Experimental setup", "weight": 1.0} -->

The method was tested in simulation and in the real world on a Panda robot and a mobile manipulator composed of a Clearpath Boxer and a Panda robot. The simulation uses the pybullet physics engine with an interface through OpenAI-gym. The different motion planning goals evaluated in this paper are: (a) reaching an end-effector pose inside a ring of obstacles (Fig. 3(a)) (similar to the experiment in ) and (b) reaching an end-effector pose above a surface with random obstacles (Fig. 3(b)). The two scenarios will be referred to as reaching-in-ring and reaching-on-table, see Fig. 3(b). Unless stated otherwise, the weights are set to ${w_{\text{path}} = 0.1},{{w_{\text{clearance}} = 0.2},{w_{\text{distance}} = 0.7}}$. We also use this weighted sum as the performance metric.

<!-- chunk {"id": "body-0037", "role": "body", "section": "VII-A Experimental setup", "weight": 1.0} -->

While these weights are chosen arbitrarily in this work to demonstrate the usefulness of autotuning, they should be derived from a human evaluator in a more realistic scenario. We refer with manual to an expert-tuning, see Table I for specific parameters. During testing, the trial was randomized with changing obstacles and goals. For autotuning on the robotic arms, we consistently used $N = 60$ trials, although the best parameter set is usually reached earlier, see Fig. 4.

<!-- chunk {"id": "body-0038", "role": "body", "section": "VII-B Importance of tuning", "weight": 1.0} -->

We compare the autotuned parameters with seven random parameter sets from the search space and a manually tuned parameter set that we obtained through expertise in previous works like. In this experiment, tuning and testing are performed on the test scenario reaching-in-ring. Tuning is crucial for optimization fabrics, as the performance with a random parameter set cannot compete with tuning, Fig. 5. This result was expected and should only demonstrate that the right parameter set is required to deploy this method. Autotuned parameters reach a similar performance to the expert. This result highlights the importance of tuning for optimization fabrics and shows that autotuning is an effective way to obtain parameter sets for novice users of optimization fabrics.

<!-- chunk {"id": "body-0039", "role": "body", "section": "VII-C Cross validation: Transfer across robots", "weight": 1.0} -->

Without any retuning, we deploy the symbolic optimization fabrics planner tuned on the Panda robot on two other robots with similar specifications (Kuka LBR IIwa 7, Universal Robot UR5) and compare the performance with tuning performed on the respective robot. Specifically, we do not change the leaf geometries and energies but change differential maps according to relevant collision links on the robot at hand. From Fig. 6, we conclude that tuning is independent of the robot. This can be explained by the fact, that optimization fabrics are a purely geometric approach to trajectory generation and the different dimension of the robots do not change the dynamical system enforced onto the robot.

<!-- chunk {"id": "body-0040", "role": "body", "section": "VII-D Cross Validation: Transfer across scenarios", "weight": 1.0} -->

In the third experiment, we evaluate how well an autotuned parameter set transfers to a different scenario. In the specific example, we use the tuning obtained from the reaching-in-ring case and test it on reaching-on-table. Performance can be transferred smoothly if the objective remains the same, see Fig. 6. However, note that different scenario might require generally slower motion because of a more crowded environment. Such a step would require to retune the parameters according to the new objective.

<!-- chunk {"id": "body-0041", "role": "body", "section": "VII-E Cross Validation: Transfer real world", "weight": 1.0} -->

As optimization fabrics are a geometric method, they should be independent of the robot embodiment. Relying on the low-level controller. In this paper, we investigate how the performance is affected by the transfer from the simulation environment to the real world. Performance benefits from tuning in the real world highlight that low-level controller differences affect the behavior, see Fig. 6. Specifically, the accumulated distance to the goal is increased ($0.14$m tuned in the real world vs $0.16$m tuned in simulation) when tuning is transferred between simulation and real world. Thus, there is added value in tuning in the real world. Our framework offers to quickly tune fabrics in the real-world using the fabrics-ros-bridge. With relaxed performance requirements, it is sufficient to tune in simulation.

<!-- chunk {"id": "body-0042", "role": "body", "section": "VII-F Cross Validation: Transfer mobile manipulator", "weight": 1.0} -->

Finally, we qualitatively test the performance of the tuning method on a real mobile manipulator with 10 degrees of freedom. After only $N = 30$ trials, the robot was able to perform coupled mobile manipulation based on a visual servoing approach. Symbolic optimization fabrics are especially suited for visual servoing as their symbolic character allows them to constantly update the position of the goal. A video of this experiment is attached to the paper.

<!-- chunk {"id": "body-0043", "role": "body", "section": "Conclusion", "weight": 1.5} -->

We formulated parameter tuning for trajectory generation as a constrained optimization problem. Additionally, we introduced symbolic optimization fabrics that implement optimization fabrics in a parameterized way, for which the general structure is pre-solved. The trajectory generator obtained with this technique is parameterized and achieves low computational costs at runtime. We showed that parameter tuning for symbolic optimization fabrics can be effectively solved using Bayesian optimization. Additionally, we have shown that the tuning generalized across different robots, tasks, and between simulation and the real world. Finally, we qualitatively demonstrated that the method applies to mobile manipulators. While we aim at developing a method-agnostic autotuning framework for motion generation, symbolic optimization fabrics were selected as an example in this work.
