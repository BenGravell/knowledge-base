<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Learning Multiple Initial Solutions to Optimization Problems

Topics include Trajectory optimization, Learning, Warm-starting, Multi-modal optimization, Neural networks.

<!-- chunk {"id": "summary-0002", "role": "summary", "section": "Summary", "weight": 2.0} -->

Learns a generative model that produces multiple diverse initial solutions for optimization problems, enabling warm-started solvers to explore different basins of attraction and improve the probability of finding high-quality global optima.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Sequentially solving similar optimization problems under strict runtime constraints is essential for many applications, such as robot control, autonomous driving, and portfolio management. The performance of local optimization methods in these settings is sensitive to the initial solution: poor initialization can lead to slow convergence or suboptimal solutions. To address this challenge, we propose learning to predict multiple diverse initial solutions given parameters that define the problem instance. We introduce two strategies for utilizing multiple initial solutions: (i) a single-optimizer approach, where the most promising initial solution is chosen using a selection function, and (ii) a multiple-optimizers approach, where several optimizers, potentially run in parallel, are each initialized with a different solution, with the best solution chosen afterward. Notably, by including a default initialization among predicted ones, the cost of the final output is guaranteed to be equal or lower than with the default initialization. We validate our method on three optimal control benchmark tasks: cart-pole, reacher, and autonomous driving, using different optimizers: DDP, MPPI, and iLQR. We find significant and consistent improvement with our method across all evaluation settings and demonstrate that it efficiently scales with the number of initial solutions required.

<!-- chunk {"id": "abstract-0004", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

The code is available at

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

Many applications, ranging from trajectory optimization in robotics and autonomous driving to portfolio management in finance, require solving similar optimization problems sequentially under tight runtime constraints. The performance of local optimizers in these contexts is often highly sensitive to the initial solution provided, where poor initialization can result in suboptimal solutions or failure to converge within the allowed time. The ability to consistently generate high-quality initial solutions is, therefore, essential for ensuring both performance and safety guarantees.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

Conventional methods for selecting these initial solutions typically rely on heuristics or warm-starting, where the solution from a previously solved, related problem instance is reused. More recently, learning-based solutions have also been proposed, where neural networks are used to predict an initial solution. However, in more challenging cases, where the optimization landscape is highly non-convex or when consecutive problem instances rapidly change, predicting a single good initial solution is inherently difficult.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

To this end, we propose *Learning Multiple Initial Solutions (MISO)* (Figure 1), in which we train a neural network to predict *multiple* initial solutions. Our approach facilitates two key settings: (i) a single-optimizer method, where a selection function leverages prior knowledge of the problem instance to identify the most promising initial solution, which is then supplied to the optimizer; and (ii) a multiple-optimizers method, where multiple initial solutions are generated jointly to support the execution of several optimizers, potentially running in parallel, with the best solution chosen afterward.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Introduction", "weight": 1.5} -->

More specifically, our neural network receives a parameter vector that characterizes the problem instance and outputs $K$ candidate initial solutions. The network is trained on a dataset of problem instances paired with (near-)optimal solutions and is evaluated on previously unseen instances. Crucially, the network is designed not only to predict *good* initial solutions---those close to the optimal---but also to ensure that these solutions are sufficiently diverse, potentially spanning all underlying modes of the problem in hand. To actively encourage this multimodality, we implement training strategies such as a winner-takes-all loss that penalizes only the candidate with the lowest loss, a dispersion-based loss term to promote dispersion among solutions, and a combination of both.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Introduction", "weight": 1.5} -->

We evaluate MISO across three distinct local optimization algorithms applied to separate robot control tasks: First-order Box Differential Dynamic Programming (DDP), which utilizes first-order linearization for the cart-pole swing-up task; Model Predictive Path Integral (MPPI) control, a sampling-based method, for the reacher task; and the Iterative Linear Quadratic Regulator (iLQR), a trajectory optimization algorithm, for an autonomous driving task. Our results show that MISO significantly outperforms existing initialization methods that rely on heuristics, learn to predict a single initial solution or use ensembles of independently learned models.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Introduction", "weight": 1.5} -->

In summary, our key contributions are as follows: We present a novel framework for predicting *multiple* initial solutions for optimizers.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Introduction", "weight": 1.5} -->

We introduce two distinct strategies for utilizing the predicted initial solutions: (i) *single-optimizer*, where the most promising solution is chosen based on a selection function, and (ii) *multiple-optimizers*, where multiple optimizers are initialized, potentially in parallel, with the best solution chosen afterward.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Introduction", "weight": 1.5} -->

We design and implement specific training objectives to prevent mode collapse and ensure that the predicted solutions remain multimodal.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Introduction", "weight": 1.5} -->

We apply our framework to three distinct sequential optimization tasks and perform extensive evaluation.

<!-- chunk {"id": "body-0014", "role": "body", "section": "Learning for optimization", "weight": 1.0} -->

Advancements in machine learning have introduced numerous learning-based approaches to optimization problems. Early work by Gregor & LeCun replaced components of classical convex optimization algorithms with neural networks. More recent works aim to replace optimization methods entirely with end-to-end neural networks or generate new optimization algorithms for specific classes of problems. Other works enhance optimization-based control algorithms, learn constraints, or learn objective functions and system dynamics.

<!-- chunk {"id": "body-0015", "role": "body", "section": "Learning initial solutions", "weight": 1.0} -->

Previous studies have proposed heuristic approaches to generate initial solutions for optimizers. More recently, learning-based methods for initializing optimizers have gained attention in various fields, aiming to enhance both computational efficiency and resulting solutions quality. In mixed-integer programming, neural networks have enhanced solver performance by predicting variable assignments, branching decisions, and integer variables. Baker employed Random Forests to predict solutions for AC optimal power flow problems. Kang et al. utilized nearest neighbor search to warm-start tight convex relaxations in nonconvex trajectory optimization problems. In robot control, neural networks were used to predict initializations for trajectory optimizers or Model Predictive Control (MPC). An exciting line of recent work developed *differentiable* optimization algorithms, which allow jointly learning objectives, constraints, and initializations by backpropagating through the optimization process. In contrast, we learn multiple initializations instead of one, and we do so without strong assumptions about the task or the optimizer. Notably, Bouzidi et al. used multiple initializations by repurposing a motion prediction model and Bézier curve fitting for a downstream MPC; however, this approach is specifically tailored for autonomous driving, incorporating a dedicated motion prediction module.

<!-- chunk {"id": "body-0016", "role": "body", "section": "Parallel optimizers", "weight": 1.0} -->

Leveraging parallelism has a long history in optimization research. With recent advances in parallel computing hardware, such as GPUs, methods that execute multiple optimizers in parallel have also emerged. For example, Sundaralingam et al. introduced cuRobo, a GPU-accelerated method combining L-BFGS and particle-based optimization for robotic manipulators. Similarly, Huang et al. utilized massive parallel GPU computation for efficient inverse kinematics and trajectory optimization. de Groot et al. proposed a topology-driven method that plans for multiple evasive maneuvers in parallel. Barcelos et al. focused on initializing parallel optimizers through rough paths. However, these works have not utilized learning. Lembono et al. explored learning-based strategies for initializing trajectory optimizers based on a database of previous solutions and ensemble-learned models, particularly in manipulation and humanoid control tasks. In contrast, we propose a single neural network to generate multiple initializations, which, as shown in our experiments, significantly outperforms the ensemble-based approach.

<!-- chunk {"id": "body-0017", "role": "body", "section": "Problem setup", "weight": 1.0} -->

In the most general form, we need to solve instances of a parameterized optimization problem, where ${\mathbf{x}} \in {\mathbb{R}}^{n}$ is the variable vector to be optimized, $J$ is the objective function, $\mathbf{g}$ and $\mathbf{h}$ are collections of inequality and equality constraints, and ${\mathbf{ψ}} \in {\mathbb{R}}^{m}$ is a parameter vector that defines the problem instance, e.g., parameters of the objective function and constraints that differ across problem instances. A local optimization algorithm, $\mathbf{O}\mathbf{p}\mathbf{t}$, attempts to find an optimum of $J$, namely, where ${\mathbf{x}}^{init}$ is initial solution provided to the optimizer, and $t_{\lim}$ is the runtime limit.

<!-- chunk {"id": "body-0018", "role": "body", "section": "Heuristic methods", "weight": 1.0} -->

A common choice of the initial solution, ${\mathbf{x}}_{init}$, is the solution to a previously solved similar problem instance, referred to as a *warm-start*. For example, in optimal control the warm-start is typically the solution from the previous timestep, shifted and padded with zeros, ${\mathbf{x}}^{{w.s}.}:={\{{\{{\mathbf{x}}_{t + k}^{cand}\}}_{k = 1}^{H - 2},\mathbf{0}\}}$. This heuristic often works well in practice, however, it can struggle when large changes in the problem instance, $\mathbf{ψ}$, occur between consecutive time steps, leading to significant shifts in the optimal solution. For example, in autonomous driving, abrupt events like a traffic light switch or the sudden appearance of a pedestrian might drastically alter the reference trajectory or constraints. In such cases, the previous solution becomes a poor initialization, and the optimizer may fail to find a good solution within the allocated time frame.

<!-- chunk {"id": "body-0019", "role": "body", "section": "Learning Multiple Initial Solutions (\\\\scalerel\\*O MISO)", "weight": 1.0} -->

The main idea of MISO is to train a single neural network to predict multiple initial solutions to an optimization problem, such that the initial solutions cover promising regions of the optimization landscape, eventually allowing a local optimizer to find a solution close to the global optimum. The key questions are then how to design a multi-output predictor; how to utilize multiple initial solutions in existing optimizers; and how to train the predictor to output a diverse set of initial solutions. In the following, we discuss our proposed solutions to these questions, illustrate the need for multimodality with a toy example, and discuss applications to optimal control.

<!-- chunk {"id": "body-0020", "role": "body", "section": "Multi-output predictor", "weight": 1.0} -->

Our multi-output predictor is a neural network that takes the problem instance, $\mathbf{ψ}$, as input and outputs $K$ initial solutions for the optimization problem, where $\mathbf{θ}$ are the learned parameters of the network. We train the network on a dataset of problem instances and their corresponding (near-)optimal solutions, ${\{{({\mathbf{ψ}}_{i},{\mathbf{x}}_{i}^{\star})}\}}_{i = 1}^{n}$. Such dataset can be generated offline, for example, by running a slow yet globally optimal solver, or allowing the same local optimizer to run with longer time limits, potentially many times from different initial solutions.

<!-- chunk {"id": "body-0021", "role": "body", "section": "Optimization with multiple initial solutions", "weight": 1.0} -->

We propose two distinct settings to leverage multiple initial solutions: *single-optimizer* and *multiple-optimizers*. The resulting frameworks are illustrated in Fig. 1.

<!-- chunk {"id": "body-0022", "role": "body", "section": "Single optimizer", "weight": 1.0} -->

A reasonable choice for $\mathbf{\Lambda}$ used in our experiments is selecting the candidate that minimizes the objective function the optimizer aims to minimize, i.e., $\mathbf{\Lambda}:={{\arg{\min_{k}J}}{({\hat{\mathbf{x}}}_{k}^{init};{\mathbf{ψ}})}}$. Other possibilities include risk measures, metrics based on performance stability, robustness, exploration, or domain-specific metrics that align with the objectives of the overall task.

<!-- chunk {"id": "body-0023", "role": "body", "section": "Multiple optimizers", "weight": 1.0} -->

In the multiple-optimizers setting, we assume multiple instances of the optimizer can be executed in parallel. We then initialize each optimizer with a different initial solution, ${{{\mathbf{x}}_{k}^{\star} = {{\mathbf{O}\mathbf{p}\mathbf{t}}_{k}{(J,{\mathbf{ψ}},t_{limit};{\hat{\mathbf{x}}}_{k}^{init})}}},{k \in {\{ 1,\ldots,K\}}}}.$ To select a single solution from the outputs of the optimizers, we can use the same selection function $\mathbf{\Lambda}$, as in the previous case, e.g., the solution that minimizes the objective function.

<!-- chunk {"id": "body-0024", "role": "body", "section": "Multiple optimizers", "weight": 1.0} -->

Our framework can be trivially generalized to allow a different number of optimizers and initial solution predictions, as well as using a heterogeneous set of optimization methods. Further, to maintain performance guarantees, one may include the default, e.g., warm-start, solution as one of the considered initial solutions, which ensures that even with poor predictions, the final solution quality does not degrade.

<!-- chunk {"id": "body-0025", "role": "body", "section": "Training strategies", "weight": 1.0} -->

The ultimate goal is to predict multiple initial solutions so that the downstream optimizer can find a solution close to the global optima, i.e., ${J{({\hat{\mathbf{x}}}^{\star};{\mathbf{ψ}})}} \approx {J{({\mathbf{x}}^{\star};{\mathbf{ψ}})}}$. Training a neural network directly for this objective is not feasible in general.

<!-- chunk {"id": "body-0026", "role": "body", "section": "Training strategies", "weight": 1.0} -->

Instead, we propose proxy training objectives that combine two terms: a regression term that encourages outputs to be close to the global optimum, e.g., ${\mathcal{L}_{reg}{({\hat{\mathbf{x}}}_{k}^{init},{\mathbf{x}}^{\star})}} = {\|{{\hat{\mathbf{x}}}_{init} - {\mathbf{x}}^{\star}}\|}$, where $\parallel \cdot \parallel$ is a distance metric; along with a *diversity* term that promotes outputs being different from each other, thereby covering various regions of the solution space. An illustrative example is in Sect. 4.4 ‣ Learning Multiple Initial Solutions to Optimization Problems"). In the following, we present three simple training strategies promoting diversity and preventing mode collapse. We discuss alternative formulations, with probabilistic modeling and reinforcement learning, in Sect. 7.

<!-- chunk {"id": "body-0027", "role": "body", "section": "Pairwise distance loss", "weight": 1.0} -->

A simple method to encourage the model's outputs to differ from each other is to penalize the pairwise distance between all outputs. The overall loss combines this dispersion-promoting term with the regression loss, where $\alpha_{K}$ is a hyperparameter that balances the trade-off between accuracy and dispersion.

<!-- chunk {"id": "body-0028", "role": "body", "section": "Winner-takes-all loss", "weight": 1.0} -->

A more interesting way to encourage multimodality is to select the best-predicted output at training time and only minimize the regression loss for this specific prediction, Intuitively, the model only needs one of its outputs to be close to the ground truth, while the other predictions are not penalized for deviating, potentially aligning with different regions of the underlying distribution. Similar losses have been used, e.g., in multiple-choice learning. One advantage of this approach is that it is hyperparameter-free.

<!-- chunk {"id": "body-0029", "role": "body", "section": "Mixture loss", "weight": 1.0} -->

Lastly, we consider a combination of the previous two approaches to potentially enhance performance, as it provides some measure of dispersion we can tune, here, $\Phi$ is an upper-bounded function, such as $\min$ or $\tanh$, designed to limit the contribution of the pairwise distance term.

<!-- chunk {"id": "body-0030", "role": "body", "section": "Mixture loss", "weight": 1.0} -->

Beyond the losses above, MISO could be integrated with other training paradigms, such as reinforcement learning or probabilistic modeling. We discuss these options in Sect. 7 but differ investigation to future work.

<!-- chunk {"id": "body-0031", "role": "body", "section": "Illustrative example", "weight": 1.0} -->

To illustrate the advantage of using a single model with multimodal outputs compared to regression models or ensembles of regressors, we examine a straightforward one-dimensional optimization problem aimed at minimizing the cost function $c{(x)}$ shown in Fig. 2 ‣ Learning Multiple Initial Solutions to Optimization Problems") (top). The function features two global minima, denoted as $\mathbf{A}$ and $\mathbf{C}$, with a local minimum located between them at $\mathbf{B}$.

<!-- chunk {"id": "body-0032", "role": "body", "section": "Illustrative example", "weight": 1.0} -->

Applying our learning framework to this simple problem, the dataset of optimal solutions includes instances of $\mathbf{A}$ and $\mathbf{C}$. A single-output regression model has no means to distinguish the two modes and inevitably learns to predict the mean of examples in the dataset, somewhere near $\mathbf{B}$. Consequently, the local optimizer is likely to converge to the suboptimal local minimum at $\mathbf{B}$. Constructing an ensemble of such models to generate multiple initial solutions does not mitigate this issue, as each ensemble member tends to be biased toward the mean of the two modes near $\mathbf{B}$. We implemented the optimization problem and showed the predictions for different training strategies in Fig. 2 ‣ Learning Multiple Initial Solutions to Optimization Problems") (bottom). Details are in Appendix A.5. Indeed, an ensemble of single-output predictors fails to predict a global optimum, while our multi-output predictor succeeds with winner-takes-all and mixture losses.

<!-- chunk {"id": "body-0033", "role": "body", "section": "Illustrative example", "weight": 1.0} -->

While the problem considered here is purposefully simplistic, the existence of local minima is the key challenge in most optimization problems.

<!-- chunk {"id": "body-0034", "role": "body", "section": "Application to optimal control", "weight": 1.0} -->

MISO is applicable to a broad class of sequential optimization problems; however, for the sake of evaluation, we focus on optimal control problems. Optimal control has a wide range of applications, e.g., in robotics, autonomous driving, and many other domains with strict runtime requirements, and due to the complexity induced by constraints and non-convex costs, local optimization algorithms are highly sensitive to the initial solution.

<!-- chunk {"id": "body-0035", "role": "body", "section": "Application to optimal control", "weight": 1.0} -->

The constraints involve adhering to the system dynamics ${{\mathbf{f}}_{d}{({\mathbf{s}}_{t + 1},{\mathbf{s}}_{t},{\mathbf{u}}_{t})}} = \mathbf{0}$, starting from an initial state ${\mathbf{s}}_{0} = {\mathbf{s}}_{\text{curr}}$, where ${\mathbf{s}}_{\text{curr}}$ represents the system's current state. The problem instance parameters $\mathbf{ψ}$ encompass the initial state ${\mathbf{s}}_{0}$, and other domain-specific variables that parameterize the objective function or constraints, such as target states, reference trajectories, obstacle positions, friction coefficients, temperature, etc.

<!-- chunk {"id": "body-0036", "role": "body", "section": "Application to optimal control", "weight": 1.0} -->

A specific property of optimal control problems is that the relationship between optimization variables, states ${\mathbf{s}}_{t}$ and controls ${\mathbf{u}}_{t}$, are defined by the dynamics constraint ${\mathbf{f}}_{d}$; and the initial state ${\mathbf{s}}_{0}$ is given. Therefore, a sequence of controls uniquely defines an (initial) solution. We can leverage this property by learning to predict only a sequence of controls instead of the full optimization variable of state-control sequences. Further, one can define the training loss over either control, state, or state-control sequences and backpropagate gradients through the dynamics constraint as long as it is differentiable. In our experiments, we use state-control loss by default as we found it to improve both our and baseline learning methods. In Appendix A.7, we show that our conclusions hold with control-only loss as well.

<!-- chunk {"id": "body-0037", "role": "body", "section": "Tasks", "weight": 1.0} -->

We evaluated our method on the three robot control benchmark tasks shown in Fig. 3 ‣ Learning Multiple Initial Solutions to Optimization Problems"), each employing a distinct local optimization algorithm. Cart-pole. This task involves balancing a pole upright while moving a cart toward a randomly selected target position, using a first-order box Differential Dynamic Programming (DDP) optimizer. Reacher. In this task, a two-link planar robotic arm needs to reach a target placed at a random positon, using a Model Predictive Path Integral (MPPI) optimizer. Autonomous Driving. Based on the nuPlan benchmark, this task focuses on trajectory tracking in complex urban environments by following a reference trajectory generated by a Predictive Driver Model (PDM) planner, using the Iterative Linear Quadratic Regulator (iLQR) optimizer. Further details are in Appendix A.1 and Appendix A.2.

<!-- chunk {"id": "body-0038", "role": "body", "section": "Baselines", "weight": 1.0} -->

We compare MISO to a range of alternative methods to provide single or multiple initial solutions. For a single initial solution, we considered: Warm-start, the default method that uses the optimizer output from the last problem instance; Regression, a single-output regression model (the $K$ = 1 version of MISO); Oracle Proxy, optimization with unlimited runtime, which we also used to generate our training data. For methods that generate multiple initial solutions, we considered: Warm-start with perturbations, which extends the warm-start approach by adding Gaussian noise to the optimizer output from the last problem instance; Regression with perturbations, where Gaussian noise is introduced to the predictions of the single-output regression model; Multi-output regression, a naive multi-output regression model without a diversity-promoting objective; and Ensemble, which trains multiple single-output neural networks with different random initializations. Finally, we assessed variants of our proposed method with the different training losses discussed in Sect. 4.3 ‣ Learning Multiple Initial Solutions to Optimization Problems"): pairwise distance, winner-takes-all, and mix.

<!-- chunk {"id": "body-0039", "role": "body", "section": "Evaluation settings", "weight": 1.0} -->

We employ two evaluation modes. (i) One-off, where the optimization task is treated as an isolated problem with the objective of finding the minimum of a given function. This mode serves as the default configuration for training neural networks, where data is replayed to the model, and the optimizer's solution is recorded but not executed. Methods are assessed by the mean cost of the optimizer's output over problem instances. (ii) Sequential, which involves solving a series of related optimization problems, executing each proposed solution, and starting the subsequent optimization from the resulting state. This setting simulates real-world conditions where the optimizer continuously interacts with a dynamic environment in a closed loop. We evaluate performance by taking the mean cost over problems in a sequence, and then the mean over sequences.

<!-- chunk {"id": "body-0040", "role": "body", "section": "Evaluation settings", "weight": 1.0} -->

To account for the additional time required to predict initial solutions, we assumed that all models perform inference in under 0.85ms, which was the case for all methods on both CPU and GPU, except for the ensemble (see Appendix A.6). In the autonomous driving task, we then reduced the runtime allocated to the optimizer accordingly.

<!-- chunk {"id": "body-0041", "role": "body", "section": "Implementation details", "weight": 1.0} -->

To generate the training data, we first create a set of problem instances by sequentially executing the optimizer initialized with the default warm-start strategy. The problem instances are then fed again to an "oracle" version of the optimizer with a significantly increased runtime limit, and the resulting solutions are recorded. After training, evaluation is done on a separate unseen set of problem instances. All experiments are conducted on an Intel Core i9-13900KF CPU and an NVIDIA RTX 4090 GPU. Further implementation details, including hyperparameters and training procedures, are in Appendix A.4 and Appendix A.3.

<!-- chunk {"id": "body-0042", "role": "body", "section": "Results", "weight": 1.0} -->

Our main results for optimization with different initial solutions are reported in Table 1 and Table 2 for single optimizer and multiple optimizers settings, respectively. Figure 4 shows the effect of the number of predicted initial solutions. Figure 5 provides qualitative results. More detailed results, including inference times, are in the Appendix.

<!-- chunk {"id": "body-0043", "role": "body", "section": "Single optimizer", "weight": 1.0} -->

. In the single-optimizer setting, Table 1, we first observe that even one learned initialization outperforms heuristic solutions (regression vs. warm-start), in almost all settings, and in particular in the most challenging autonomous driving task. We then examine the impact of generating multiple initial solutions. Perturbations-based methods show some improvement over their single-initialization counterparts in most cases, and ensembles of independently learned models perform consistently better than single models. Finally, our proposed multi-output methods demonstrate substantial improvements over all baselines because they can learn to predict diverse multimodal initial solutions. Specifically, MISO winner-takes-all or MISO mix achieve the lowest mean costs across all tasks. Considering the pairwise distance term alone proves insufficient to ensure adequate diversity, whereas incorporating it with MISO winner-takes-all often boosts performance, yet, its effectiveness varies, which underscores the challenge of selecting optimal hyperparameters. As expected, improvements are consistently larger in the more important sequential optimization setting, where errors over time compound.

<!-- chunk {"id": "body-0044", "role": "body", "section": "Multiple optimizers", "weight": 1.0} -->

. When considering the multiple-optimizers setting, we observe the same trend. Learning-based methods outperform heuristic ones, and multi-output approaches yield further enhancements. As expected, the use of multiple optimizers leads to consistently better results compared to the single-optimizer setting due to increased exploration of the solution space.

<!-- chunk {"id": "body-0045", "role": "body", "section": "Summary", "weight": 1.0} -->

Overall, our methods significantly outperform the other baselines in both settings. The consistent superiority of the MISO mix and MISO winner-takes-all methods across different tasks and configurations underscores the advantages of using learning-based multi-output strategies for generating initial solutions. These findings demonstrate that promoting diversity among multiple initializations is crucial for improving optimization outcomes, especially when combined with multiple optimizers.

<!-- chunk {"id": "body-0046", "role": "body", "section": "Conclusions and Future Work", "weight": 1.0} -->

We introduced Learning Multiple Initial Solutions (MISO), a novel framework for learning multiple diverse initial solutions that significantly enhance the reliability and efficiency of local optimization algorithms across various settings. Extensive experiments in optimal control demonstrated that our method consistently outperforms baseline approaches and scales efficiently with the number of initializations.

<!-- chunk {"id": "body-0047", "role": "body", "section": "Limitations", "weight": 1.5} -->

Our approach is not without limitations. First, to train a useful model, we rely on the coverage and quality of the training data, as the method does not directly interact with the optimizer or the underlying objective function. Second, the underlying assumption of our regression loss is that initial solutions closer to the global optimum increase the likelihood of successful optimization may not hold in complex optimization landscapes with intricate constraints. Third, in highly complex optimization problems where each solution constitutes a high-dimensional and intricate structure, accurately learning initial solution candidates can become exceedingly challenging, potentially diminishing the effectiveness of our approach.

<!-- chunk {"id": "body-0048", "role": "body", "section": "Future work", "weight": 1.5} -->

There are several promising directions for future research. To address the aforementioned limitations, one may simply incorporate the optimization objective into the model training loss, thus creating a direct link to the final optimization goal. Alternatively, using reinforcement learning (RL) to train MISO is a particularly exciting opportunity. By framing the problem in an RL context, e.g., where the reward is the negative cost of the optimizer's final solution, models would be directly trained to maximize the probability of the optimizer finding the global optima and may learn to specialize to the specific optimizer. One challenge would be computational, as RL would require running the optimizer numerous times during training.

<!-- chunk {"id": "body-0049", "role": "body", "section": "Future work", "weight": 1.5} -->

Other extensions of our approach include probabilistic modeling, e.g., Gaussian mixture models, variational autoencoders, or diffusion models; however, preventing mode collapse and promoting diversity would remain a challenge. Future work may explore alternative selection functions, such as risk measures or criteria based on stability, robustness, exploration, or other domain-specific metrics; as well as using a heterogeneous set of parallel optimizers. Finally, we are excited about various possible applications in optimal control and beyond, where sequences of similar optimization problems need to be solved, for example, localization and mapping in robotics, financial optimization, traffic routing optimization, or even training neural networks with different initial weights, e.g., for meta-learning, or scene representation learning with Neural Radiance Fields or 3D Gaussian splatting.

<!-- chunk {"id": "body-0050", "role": "body", "section": "Ethics statement", "weight": 1.0} -->

Our work is concerned with a general class of optimization problems that do not raise particular ethical considerations.
