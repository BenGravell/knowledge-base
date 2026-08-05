<!-- arxiv-full-text:v1 {"arxiv_id": "2302.06922", "source": "ar5iv"} -->

## Introduction

Mobile manipulation is the field of robotics concerned with highly capable robots characterized by their locomotion and manipulation ability. Such robots are getting ever more attention as they will be deployed to human-shared environments, like households or warehouses. In such dynamic environments, fast trajectory generation is crucial to avoid collisions and react quickly to changing goal definitions.

Trajectory generation is often addressed by solving an optimization problem that consists of a scalar objective function -- the dynamics or transition function -- and several constraints. As the degrees of freedom and number of constraints increase, solving that problem in real-time becomes challenging. This is especially limiting in the case of mobile manipulation. Optimization fabrics represent a different approach to the problem, as they formulate trajectory generation as the shortest-geodesic-problem in a manifold of the configuration space.

With optimization fabrics, different components, or desired behaviors, such as collision avoidance and joint limit avoidance, are combined using Riemannian metrics. As the structure of the resulting trajectory generation methods remains unchanged across all time steps, it can be composed before runtime, thus saving computational costs during executing. Optimization fabrics, but also their predecessor Riemannian Motion Policies (RMPs), have shown impressive results for several manipulator applications, including dynamic and crowded environments. However, despite their theoretical properties of inherent collision avoidance and convergence, these methods require expertise and intuition to tune individual components to generate smooth and well-behaving trajectories.

Figure 1: Overview of one trial in the tuning pipeline for symbolic optimization fabrics. The objective function is evaluated after an entire trial run is simulated. Using Bayesian optimization, a new parameter set is suggested based on the history of trials. The best parameter set is extracted from all trials.

To address this issue, we formulate optimization fabrics as a symbolic trajectory generation method. Precisely, the combination of the individual components (joint limit avoidance, goal reaching, collision avoidance, etc.) is performed in a parameterized way before runtime. Separating composition and evaluation allows for changing the individual parameters at runtime while achieving low computational costs. Additionally, this allows formulating parameter-tuning as a constrained optimization problem. Solving this problem effectively automates the tuning process systematically using Bayesian optimization. We show that automated tuning requires only few trials to achieve similar performance to an expert in the field, and systematically outperforms a randomized parameter setting. Moreover, we show that one parameter tuning generalizes across different robots, to some extent, across different tasks and between simulation and real world. Finally, we demonstrate how coupled mobile manipulation with a differential drive can be achieved using autotuned optimization fabrics for in-store order-picking integrating visual servoing.

## Related Works

### II-A Geometric control for trajectory generation

Operational space control was the first control method that imposed a desired dynamical system onto a robotic system. The concept was an important step toward naturally controlling kinematically redundant robots. The concept was formalized in the field of geometric control, where the study of differential geometry leads to stable and converging behavior under geometric conditions. More recently, RMPs for manipulation tasks offered a highly reactive trajectory generation method. This method achieves composable behavior by introducing a split between the importance metric and the forcing term. Using the pullback and pushforward operator to change between manifolds of the configuration space, individual components, such as collision avoidance and goal attraction, can be designed iteratively. However, RMPs require intuition and experience when being designed, and convergence can only be proven conditionally. Later, optimization fabrics were introduced that are able to completely decouple importance metrics and the defining geometry. Under simple construction rules for these two components, convergence can be easily guaranteed. In our prior work on optimization fabrics, the framework was first applied to mobile manipulation and generalized to more dynamic environments..

Figure 2: Two different parameter sets for optimization fabrics given the same problem. While the greedy tuning is more aggressive (purple), the more conservative tuning results in a smoother trajectory (green).

### II-B Autotuning for trajectory generation

Autotuning can be beneficial for trajectory generation when using model predictive control. In, an autotuned model predictive controller has outperformed a manual tuned controller of the same kind by 25%. Jointly optimizing parameters and the model of the controller, AutoMPC showed the benefit of parameter tuning in the context of simultaneous system identification and control. These methods are explicitly formulated for model predictive control and do not transfer easily to other trajectory generation methods. In contrast, we propose a generic parameter optimization approach to trajectory generation.

### II-C Hyperparameter tuning in machine learning

Within the machine-learning field, hyperparameter tuning has shown to be highly important for all different kinds of applications. Parameter optimization aims to minimize training costs while achieving the best possible performance. Hyperparameter tuning is most valuable in extremely costly applications such as reinforcement learning. Generally, two different search algorithms have been investigated: grid search and random search. Current state-of-the-art methods for parameter search are based on random search with a Bayesian optimizer. While the machine-learning community has largely agreed on the importance of parameter tuning, systematic tuning of trajectory generation methods are not well established. In this paper, we showcase, with the example of optimization fabrics, how important parameter tuning is and how trajectory generation can benefit from it.

## Overview

In this paper, we first recall very briefly the theory of optimization fabrics and the steps to use it for trajectory generation (Section IV). Then, we formulate optimization fabrics as a symbolic trajectory generator, so that combining of individual components is only performed once (Section V). Then, we formulate parameter tuning for trajectory generation as a constrained optimization problem and propose Bayesian optimization for effective autotuning (Section VI). As an example, we apply this autotuning to symbolic optimization fabrics (Section VII), but it is generally independent of the trajectory generator at hand.

## Background

In this section, we very briefly introduce the concepts required for trajectory generation with optimization fabrics. For a more in-depth introduction to optimization fabrics and its foundations in differential geometry, the reader is referred to.

### IV-A Configurations and task variables

We denote ${\mathbf{q}} \in \mathcal{Q} \subset {\mathbb{R}}^{n}$ a configuration of the robot with $n$ its degrees of freedom; $\mathcal{Q}$ is the configuration space of the generalized coordinates of the system. Generally, ${\mathbf{q}}{(t)}$ defines the robot's configuration at time $t$, so that $\overset{˙}{\mathbf{q}}$, $\overset{¨}{\mathbf{q}}$ define the instantaneous derivatives of the robot's configuration. Similarly, we assume that there is a set of task variables ${\mathbf{x}}_{j} \in \mathcal{X}_{j} \subset {\mathbb{R}}^{m_{j}}$ with variable dimension $m_{j} \leq n$. The task space $\mathcal{X}_{j}$ defines an arbitrary manifold of the configuration space $\mathcal{Q}$ in which a robotic task can be represented. Further, we assume that there is a differential map $\phi_{j}:{{\mathbb{R}}^{n}\rightarrow{\mathbb{R}}^{m_{j}}}$ that relates the configuration space to the $j^{th}$ task space. For example, when a task variable is defined as the end-effector position, then $\phi_{j}$ is the positional part of the forward kinematics. On the other hand, if a task variable is defined to be the joint position, then $\phi_{j}$ is the identity function. In the following, we drop the subscript $j$ in most cases for readability when the context is clear.

We assume that $\phi$ is in $\mathcal{C}^{1}$ so that the Jacobian is defined as or ${\mathbf{J}}_{\phi} = {\partial_{\mathbf{q}}\phi}$ for short. Thus, we can write the total time derivatives of $\mathbf{x}$ as $\overset{˙}{\mathbf{x}} = {{\mathbf{J}}_{\phi}\overset{˙}{\mathbf{q}}}$ and $\overset{¨}{\mathbf{x}} = {{{\mathbf{J}}_{\phi}\overset{¨}{\mathbf{q}}} + {{\overset{˙}{\mathbf{J}}}_{\phi}\overset{˙}{\mathbf{q}}}}$.

### IV-B Spectral semi-sprays

Inspired by simple mechanics (e.g., the simple pendulum), the framework of optimization fabrics designs motion policies as second-order dynamical systems $\overset{¨}{\mathbf{x}} = {\pi{({\mathbf{x}},\overset{˙}{\mathbf{x}})}}$. The motion policy is defined by the differential equation ${{{\mathbf{M}}\overset{¨}{\mathbf{x}}} + {\mathbf{f}}} = 0$, where ${\mathbf{M}}{({\mathbf{x}},\overset{˙}{\mathbf{x}})}$ and ${\mathbf{f}}{({\mathbf{x}},\overset{˙}{\mathbf{x}})}$ are functions of position and velocity. Besides, $\mathbf{M}$ is symmetric and invertible. We denote such systems as $\mathcal{S} = ({\mathbf{M}},{\mathbf{f}})_{\mathcal{X}}$ and refer to them as spectral semi-sprays, or specs for short. When the space of the task variable is clear from the context, we drop the subscript.

### IV-C Operations on specs

Complex trajectory generation is composed of multiple components, such as collision avoidance, joint limits avoidance, etc. The power of optimization fabrics lies in the metric-weighted sum to combine multiple components from different manifolds. These operations are derived from operations on specs and are briefly recalled here.

Given a differential map $\phi:{\mathcal{Q}\rightarrow\mathcal{X}}$ and a spec $({\mathbf{M}},{\mathbf{f}})_{\mathcal{X}}$, the pullback is defined as The pullback allows converting between two distinct manifolds (e.g. a spec could be defined in the robot's workspace and pulled into the robot's configuration space using the pullback with $\phi$ being the forward kinematics).

For two specs, $\mathcal{S}_{1} = \left({\mathbf{M}}_{1},{\mathbf{f}}_{1} \right)_{\mathcal{X}}$ and $\mathcal{S}_{2} = \left({\mathbf{M}}_{2},{\mathbf{f}}_{2} \right)_{\mathcal{X}}$, their summation is defined: Additionally, a spec can be energized by a Lagrangian energy. Effectively, this equips the spec with a metric. Specifically, given a spec of form $\mathcal{S}_{\mathbf{h}} = {({\mathbf{I}},{\mathbf{h}})}$ and an energy Lagrangian $\mathcal{L}_{e}$ with the derived equations of motion ${{{\mathbf{M}}_{\mathcal{L}_{e}}\overset{¨}{\mathbf{x}}} + {\mathbf{f}}_{\mathcal{L}_{e}}} = 0$, we can define the operation where ${\mathbf{P}}_{\mathcal{L}_{e}} = {{\mathbf{M}}_{\mathcal{L}_{e}}\left({{\mathbf{M}}_{\mathcal{L}_{e}}^{- 1} - \frac{\overset{˙}{\mathbf{x}}{\overset{˙}{\mathbf{x}}}^{T}}{{\overset{˙}{\mathbf{x}}}^{T}{\mathbf{M}}_{\mathcal{L}_{e}}\overset{˙}{\mathbf{x}}}} \right)}$ is an orthogonal projector. The resulting spec is an energized spec and we call the operation energization.

With spectral semi-sprays and the presented operations, avoidance behavior, such as joint limit avoidance, collision avoidance or self-collision avoidance, can be realized.

### IV-D Optimization fabrics

In the previous subsection, we explained how different avoidance behaviors can be combined. Spectral semi-sprays can additionally be forced by a potential, denoted as the forced variant of form $\mathcal{S}_{\mathbf{ψ}} = \left( {\mathbf{M}},{{\mathbf{f}} + {\partial_{\mathbf{x}}{\mathbf{ψ}}}} \right)$. This forcing term clearly changes the behavior of the system. Optimization fabrics introduce construction rules to make sure that the solution path ${\mathbf{x}}{(t)}$ of $\mathcal{S}_{\mathbf{ψ}}$ converges towards the minimum of ${\mathbf{ψ}}{({\mathbf{x}})}$. Then, the potential is designed in such a way that its minimum represents a goal state of the motion planning problem.

First, the initial spec that represents an avoidance component is written in the form ${\overset{¨}{\mathbf{x}} + {{\mathbf{h}}{({\mathbf{x}},\overset{˙}{\mathbf{x}})}}} = 0$, such that $\mathbf{h}$ is homogeneous of degree 2: ${{\mathbf{h}}{({\mathbf{x}},{\alpha\overset{˙}{\mathbf{x}}})}} = {\alpha^{2}{\mathbf{h}}{({\mathbf{x}},\overset{˙}{\mathbf{x}})}}$ (Creation). Secondly, the geometry is energized (Eq. 4) with a Finsler structure \[11, Definition 5.4\] (Energization). The property of homogeneity of degree 2 and the energization with the Finsler structure guarantees, according to \[11, Theorem 4.29\], that the energized spec forms a frictionless fabric. A frictionless fabric is defined to optimize the forcing potential $\mathbf{ψ}$ when being damped by a positive definite damping term \[11, Definition 4.4\]. Thirdly, all avoidance components are combined in the configuration space of the robot using the pullback and summation operation (Combination). Note, that both operations are closed under the algebra designed by these operations, i.e. every pulled optimization fabric or the sum of two optimization fabrics is, itself, an optimization fabric. In the last step, the combined spec is forced by the potential $\mathbf{ψ}$ with the desired minimum and damped with a positive definite damping term (Forcing). This resulting system of form ${{{\mathbf{M}}\overset{¨}{\mathbf{q}}} + {{\mathbf{f}}{({\mathbf{q}},\overset{˙}{\mathbf{q}})}} + {\partial_{\mathbf{q}}{\mathbf{ψ}}} + {\beta\overset{˙}{\mathbf{q}}}} = 0$ is solved to obtain the trajectory generation policy in acceleration form $\overset{¨}{\mathbf{q}} = {\pi{({\mathbf{q}},\overset{˙}{\mathbf{q}})}}$.

## Symbolic fabrics

A trajectory generator that is based on optimization fabrics is composed of several components, such as collision avoidance, joint limit avoidance, goal attraction, etc. Each component contributes to the resulting optimization fabric through the metric-weighted summation that creates the tree of fabrics. The trajectory generator is parameterized by the individual terms of the components. Here, we lay out the parameterization for collision avoidance, joint limit avoidance, self-collision avoidance, and speed-control. In our framework, the tree of fabrics is generated before runtime as a symbolic expression, to which the parameters are set at runtime. Note that the approach of symbolic pre-solving results in much higher planning frequencies. In the following, we explain the individual parameters that we exposed symbolically. The form of the individual terms is adapted from but written in a symbolic form.

### Basic inertia

The final tree of fabrics is equipped with a basic inertia metric that indicates how reactive the entire motion is. This basic inertia metric is derived from the symbolic Finsler structure: $\mathcal{L}_{e} = {0.5m_{\text{base}}{\overset{˙}{\mathbf{q}}}^{T}{\mathbf{I}}\overset{˙}{\mathbf{q}}}$.

### Collision avoidance

For collision avoidance, the task manifold $\mathcal{X}$ is defined by the distance function between an obstacle and a robot link. The differential map used is defined as where $\text{fk}_{\text{i}}{({\mathbf{q}})}$ is the positional forward kinematics for link $i$ in a configuration $\mathbf{q}$, $r_{\text{obst}}$ and $r_{\text{i}}$ are the radii of the englobing spheres for the obstacle and the link respectively. While this mapping between configuration space and task manifold is different for each obstacle and each collision link of the robot, the geometry and metric are the same for all of them. For the geometry ${\overset{¨}{\mathbf{x}} + {{\mathbf{h}}{({\mathbf{x}},\overset{˙}{\mathbf{x}})}}} = \mathbf{0}$, we use the parameterized forcing term where $k_{\text{geo,col}}$ and $\beta_{\text{geo,col}}$ are parameters of the trajectory generator. Generally, we use $k$ and $\beta$ for proportional parameters and exponential parameters. The Finsler structure for collision avoidance is parameterized as where $\text{sgn}{(\overset{˙}{\mathbf{x}})}$ is the signum-operator returning the sign of $\overset{˙}{\mathbf{x}}$.

### Self-collision avoidance

For self-collision avoidance, the task manifold $\mathcal{X}$ is defined similarly to collision avoidance: where $\text{fk}_{i}{({\mathbf{q}})}$ and $\text{fk}_{j}{({\mathbf{q}})}$ are the positional forward kinematics of the two links for a self-collision pair and $r_{i}$ and $r_{j}$ are the radii for both englobing spheres. The geometries are defined analogously The Finsler structure for collision avoidance is parameterized as

### Joint limit avoidance

For joint-limit avoidance, two simple differential maps denoting the distance to the joint limits are used, specifically Similar to collision avoidance, we use the parameterized forcing term and the Finsler structure

### Speed control

As the root of the tree of fabrics is a frictionless fabric, it only converges if damped. Constant damping is sufficient to achieve the theoretical properties that are needed for trajectory generation. However, proposed enhanced damping under the name of speedcontrol. We employ the same damping strategy while adding parameterization. The technique is based on a dynamic damping modification based on the distance to the goal. Specifically, the final optimization fabric is damped according to where ${\mathbf{h}}_{2}$ is the sum of all pulled forcing terms, $\mathbf{M}$ is the sum of all metrics of the individual geometries, $\partial_{\mathbf{q}}{\mathbf{ψ}}$ is the goal attraction term pulled in the configuration space, $\alpha_{\text{ex}}$ is a weighted sum of $\alpha_{\text{ex}}^{0}$ that maintains constant execution energy without goal attraction and $\alpha_{\text{ex}}^{\mathbf{ψ}}$ that maintains constant execution energy with goal attraction: Then, $\beta$ is the damping term, computed as: where ${\mathbf{B}}_{\text{max}}$ and ${\mathbf{B}}_{\text{min}}$ are the upper and lower damping values and $\alpha_{\mathcal{L}_{e}}$ is the energization coefficient maintaining constant system energy (not execution energy) without goal attraction. The switching functions ${\mathbf{s}}_{\beta}{({\mathbf{q}})}$, ${\mathbf{s}}_{\eta}{({\mathbf{q}})}$ are further parameterized as where $r_{shift}$ determines the distance to the goal at which the switch between ${\mathbf{B}}_{\text{min}}$ and ${\mathbf{B}}_{\text{max}}$ occurs, $\alpha_{\beta}$ is the steepness of that switching, $\mathcal{L}_{ex}$ is the user-defined execution energy (usually a simple kinetic energy in joint space) and $v_{ex}$ is the execution energy factor, i.e. it determines the desired speed of motion. For a detailed discussion on speed control with optimization fabrics, we refer to previous works on optimization fabrics.

We group all parameters resulting from the symbolic fabrics defined here into a vector of parameters $\mathbf{\Theta}$. All parameters are listed in Table I.

## Parameter tuning as an optimization problem

We define parameter tuning as a constrained optimization problem: where $\mathbf{\Theta}_{\text{max}}$ and $\mathbf{\Theta}_{\text{min}}$ are the upper and lower bounds of the parameters. The objective $c{(\mathbf{\Theta})}$ is a function of the parameters specifying the tree of fabrics and can be evaluated after one trajectory planning problem has finished. We call the evaluation of one parameter set a trial. Next, we propose an objective function that is flexible as different scenarios may require different parameter tuning.

### VI-A Objective

The objective function $c{(\mathbf{\Theta})}$ is a weighted sum of several metrics, that are invariant to the robot: $c_{\text{distance}}$ accounts for the normalized, summed distance to the goal over one trial and is defined as where $i \in {\lbrack 0,T\rbrack}$ are the discretized time steps and ${\mathbf{x}}_{\text{goal}}$ is the goal of the motion planning problem. $c_{\text{path}}$ accounts for the normalized path length over one trial and is defined as $c_{\text{clearance}}$ accounts for the average clearance to obstacles over one trial and is defined as where $o_{i}^{j}$ is the position of obstacle $j$ at time step $i$. Each of these terms is evaluated after an entire trial that was obtained by a specific set of parameters.

1Formulate trajectory generator with parameters Θ 2 Define parameter space by Θmin, Θmax 4 Initialize objective function estimate $\overset{\sim}{c}{(\mathbf{\Theta})}$ 6 Suggest parameter Θi based on $\overset{\sim}{c}{(\mathbf{\Theta})}$ 8 Compute action with parameter set Θi 9 Apply action to robot 10 Store observation relevant for metrics 14 Update $\overset{\sim}{c}{(\mathbf{\Theta})}$ 17Extract the best parameter set Θbest Algorithm 1 Autotuning for trajectory generators

### VI-B Bayesian optimization

In the tuning phase, the problem specification for the investigated scenario, e.g., the goal and obstacle positions, across all trials during tuning remains the same while $\mathbf{\Theta}$ are optimized according to the objective. To solve the Bayesian optimization we employ the Tree-structured Parzen Estimator as it has shown improved performance over grid-search and conventional random search in machine learning applications. To deploy this technique we used Optuna, a hyperparameter optimization framework initially designed for machine learning applications. The general setup for one trial is shown in Fig. 1 and the procedure is summarized in Algorithm 1.

## Experimental Results

We showcase our parameter optimization method for symbolic fabrics. The search space for the parameters is summarized in Table I.

TABLE I: Search space for parameters. Some parameters are restricted to integers, and for some a log-distribution is applied.

We first analyze the importance of tuning for optimization fabrics on the performance of trajectory generation. Then, we investigate how tuned parameters can be transferred across different robots (Section VII-C), different scenarios (Section VII-D), and between simulation and real world (Section VII-E).

### VII-A Experimental setup

The method was tested in simulation and in the real world on a Panda robot and a mobile manipulator composed of a Clearpath Boxer and a Panda robot. The simulation uses the pybullet physics engine with an interface through OpenAI-gym. The different motion planning goals evaluated in this paper are: (a) reaching an end-effector pose inside a ring of obstacles (Fig. 3(a)) (similar to the experiment in ) and (b) reaching an end-effector pose above a surface with random obstacles (Fig. 3(b)). The two scenarios will be referred to as reaching-in-ring and reaching-on-table, see Fig. 3(b). Unless stated otherwise, the weights are set to ${w_{\text{path}} = 0.1},{{w_{\text{clearance}} = 0.2},{w_{\text{distance}} = 0.7}}$. We also use this weighted sum as the performance metric. While these weights are chosen arbitrarily in this work to demonstrate the usefulness of autotuning, they should be derived from a human evaluator in a more realistic scenario. We refer with manual to an expert-tuning, see Table I for specific parameters. During testing, the trial was randomized with changing obstacles and goals. For autotuning on the robotic arms, we consistently used $N = 60$ trials, although the best parameter set is usually reached earlier, see Fig. 4.

Figure 4: Optimization history for simulation (left) and real world (right) for panda robot in reaching-in-ring scenario.

### VII-B Importance of tuning

We compare the autotuned parameters with seven random parameter sets from the search space and a manually tuned parameter set that we obtained through expertise in previous works like. In this experiment, tuning and testing are performed on the test scenario reaching-in-ring. Tuning is crucial for optimization fabrics, as the performance with a random parameter set cannot compete with tuning, Fig. 5. This result was expected and should only demonstrate that the right parameter set is required to deploy this method. Autotuned parameters reach a similar performance to the expert. This result highlights the importance of tuning for optimization fabrics and shows that autotuning is an effective way to obtain parameter sets for novice users of optimization fabrics.

Figure 5: Evaluation for scenario reaching-in-ring autotuned parameters and compared to random parameter selection and manual tuning. Autotuning is able to systematically outperform random parameter sets and reach expert level tuning.

Figure 6: The autotuned for the panda robot in simulation for the reaching-in-ring scenario on modified scenarios (blue) is compared to autotuned parameter sets obtained on these scenarios directly (green). Exchanging the robot (ur5, iiwa) and changing the scenario (reaching-on-table) results in a very small loss in performance, while the loss is higher when parameters are transferred between simulation and real world (real-world).

### VII-C Cross validation: Transfer across robots

Without any retuning, we deploy the symbolic optimization fabrics planner tuned on the Panda robot on two other robots with similar specifications (Kuka LBR IIwa 7, Universal Robot UR5) and compare the performance with tuning performed on the respective robot. Specifically, we do not change the leaf geometries and energies but change differential maps according to relevant collision links on the robot at hand. From Fig. 6, we conclude that tuning is independent of the robot. This can be explained by the fact, that optimization fabrics are a purely geometric approach to trajectory generation and the different dimension of the robots do not change the dynamical system enforced onto the robot.

### VII-D Cross Validation: Transfer across scenarios

In the third experiment, we evaluate how well an autotuned parameter set transfers to a different scenario. In the specific example, we use the tuning obtained from the reaching-in-ring case and test it on reaching-on-table. Performance can be transferred smoothly if the objective remains the same, see Fig. 6. However, note that different scenario might require generally slower motion because of a more crowded environment. Such a step would require to retune the parameters according to the new objective.

### VII-E Cross Validation: Transfer real world

As optimization fabrics are a geometric method, they should be independent of the robot embodiment. Relying on the low-level controller. In this paper, we investigate how the performance is affected by the transfer from the simulation environment to the real world. Performance benefits from tuning in the real world highlight that low-level controller differences affect the behavior, see Fig. 6. Specifically, the accumulated distance to the goal is increased ($0.14$m tuned in the real world vs $0.16$m tuned in simulation) when tuning is transferred between simulation and real world. Thus, there is added value in tuning in the real world. Our framework offers to quickly tune fabrics in the real-world using the fabrics-ros-bridge. With relaxed performance requirements, it is sufficient to tune in simulation.

### VII-F Cross Validation: Transfer mobile manipulator

Finally, we qualitatively test the performance of the tuning method on a real mobile manipulator with 10 degrees of freedom. After only $N = 30$ trials, the robot was able to perform coupled mobile manipulation based on a visual servoing approach. Symbolic optimization fabrics are especially suited for visual servoing as their symbolic character allows them to constantly update the position of the goal. A video of this experiment is attached to the paper.

Figure 7: Trajectory generation with optimization fabrics for mobile manipulator using visual serving for product picking.

## Conclusion

We formulated parameter tuning for trajectory generation as a constrained optimization problem. Additionally, we introduced symbolic optimization fabrics that implement optimization fabrics in a parameterized way, for which the general structure is pre-solved. The trajectory generator obtained with this technique is parameterized and achieves low computational costs at runtime. We showed that parameter tuning for symbolic optimization fabrics can be effectively solved using Bayesian optimization. Additionally, we have shown that the tuning generalized across different robots, tasks, and between simulation and the real world. Finally, we qualitatively demonstrated that the method applies to mobile manipulators. While we aim at developing a method-agnostic autotuning framework for motion generation, symbolic optimization fabrics were selected as an example in this work.
