<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Memory of Motion for Warm-starting Trajectory Optimization

Topics include Trajectory optimization, Motion planning, Robotics, Bayesian methods, Nearest neighbors, Regression, Optimization, Planning, Humanoid robot, Gaussian processes.

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Trajectory optimization for motion planning requires good initial guesses to obtain good performance. In our proposed approach, we build a memory of motion based on a database of robot paths to provide good initial guesses. The memory of motion relies on function approximators and dimensionality reduction techniques to learn the mapping between the tasks and the robot paths. Three function approximators are compared: k-Nearest Neighbor, Gaussian Process Regression, and Bayesian Gaussian Mixture Regression. In addition, we show that the memory can be used as a metric to choose between several possible goals, and using an ensemble method to combine different function approximators results in a significantly improved warm-starting performance. We demonstrate the proposed approach with motion planning examples on the dual-arm robot PR2 and the humanoid robot Atlas.

<!-- chunk {"id": "body-0003", "role": "body", "section": "Introduction", "weight": 1.5} -->

Motion planning for robots with high Degree-of-Freedoms (DoFs) presents many challenges, especially in the presence of constraints such as obstacle avoidance, joint limits, etc. To handle the high-dimensionality and the various constraints, many works focus on *trajectory optimization* methods that attempt to find a locally optimal solution. In this approach, the motion planning problem is formulated as an optimization problem where ${\mathbf{q}}_{0:T}$ denotes the robot's configurations from time step $t = 0$ to $t = T$; $\ell{(\cdot)}$, ${\mathbf{g}}{(\cdot)}$ and ${\mathbf{h}}{(\cdot)}$ are the cost, the inequality and the equality constraints.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

As an example, consider the planning problem depicted in Fig. 1, where the PR2 robot has to move its base around an object or to perform a dual-arm motion to pick items from the shelves. If the task ${\mathbf{x}} = {({\mathbf{q}}_{\text{init}}^{\top},{\mathbf{q}}_{\text{goal}}^{\top})}^{\top}$ is to move from an initial configuration ${\mathbf{q}}_{\text{init}}$ to a goal configuration ${\mathbf{q}}_{\text{goal}}$ while minimizing the total joint velocity, the optimization problem can be written as Other constraints can also be added, e.g. to avoid collisions, to comply with joint limits, etc.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

Such optimization problems are in general non-convex, especially due to the collision constraints, which makes finding the global optimum very difficult. Trajectory optimization methods such as TrajOpt, CHOMP, or STOMP solve the non-convex problem by iteratively optimizing around the current solution. While such approach is very popular and yields good practical results, the convergence and the quality of the solution are very sensitive to the choice of the initial guess. If it is far from the optimal solution, the method can get stuck at a poor local optimum.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

To overcome this problem, our approach builds a *memory of motion* that learns how to provide good initializations (i.e., a *warm-start*) to the solver based on previously solved problems. Functionally, the memory of motion is expected to learn the mapping ${\mathbf{f}}:{{\mathbf{x}}\rightarrow{\mathbf{y}}}$ that maps each task $\mathbf{x}$ to the robot path $\mathbf{y}$. Such mapping can be highly nonlinear and *multimodal* (i.e., one task $\mathbf{x}$ can be associated to several robot paths $\mathbf{y}$), and the dimension of $\mathbf{y}$ is typically very high. Our proposed method relies on machine learning techniques such as function approximation and dimensionality reduction to learn this mapping effectively. We use the term *memory of motion* to include both the database of motions and the algorithms to query the warm-starts from the database.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

We point out that while other techniques such as sampling-based motion planners can also be used to warm-start the solver (e.g. in ), such methods typically require a considerable computation time (i.e. in the order of seconds) that is comparable to the solver's convergence time itself, given the very high dimensional problems considered here. In contrast, querying the memory of motion can be done very fast, in the order of milliseconds. Additionally, our proposed method produces initial guesses that are close to the optimal solutions, reducing the convergence time.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Introduction", "weight": 1.5} -->

The contribution of this paper is the following. First, we propose the use of function approximation methods to learn the mapping ${\mathbf{f}}{({\mathbf{x}})}$. We consider three methods: $k$-Nearest Neighbor ($k$-NN), Gaussian Process Regressor (GPR) and Bayesian Gaussian Mixture Regression (BGMR), and discuss their different characteristics on various planning problems. We show in particular that BGMR handles multimodal output very well. Furthermore, we show that the memory of motion can be also be used as a metric for choosing optimally between several possible goals. Finally, we demonstrate that using an ensemble of function approximators to provide warm-starts boosts the success rate significantly.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Introduction", "weight": 1.5} -->

The paper is organized as follows. In Section II we discuss the related work that use the concept of memory of motion for various problems. Section III explains the methods for constructing and using the memory of motion. The experimental results are presented and discussed in Section IV and V. Finally, Section VI concludes the paper.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Method", "weight": 1.0} -->

Section III-A discusses the main idea of building the memory of motion using function approximation and dimensionality reduction techniques to learn the mapping between the task and the associated robot path. Section III-B explains how the memory of motion can be used as a metric for choosing between different goals. Finally, Section III-C explains how the warm-starting performance can be improved significantly using an ensemble method.

<!-- chunk {"id": "body-0011", "role": "body", "section": "III-A Building a Memory of Motion", "weight": 1.0} -->

The mapping $\mathbf{f}$ can be learned by training function approximators using the database $\{{\mathbf{X}},{\mathbf{Y}}\}$. In this paper we consider three function approximators: $k$-NN, GPR, and BGMR.

<!-- chunk {"id": "body-0012", "role": "body", "section": "III-A1 $k$-Nearest Neighbor ($k$-NN)", "weight": 1.0} -->

It then predicts the corresponding robot path ${\mathbf{y}}^{\ast}$ by taking the average ${\mathbf{y}}^{\ast} = {\frac{1}{K}{\sum_{k = 1}^{K}{\mathbf{y}}_{k}}}$. The method is very simple to implement and it works well if there is a sufficiently dense dataset, but it suffers from the curse of dimensionality; as the dimension of $\mathbf{x}$ increases, the number of data that needs to be stored increases exponentially. This method is mainly considered as the baseline against the next two methods.

<!-- chunk {"id": "body-0013", "role": "body", "section": "III-A2 Gaussian Process Regressor (GPR)", "weight": 1.0} -->

Like $k$-NN, GPR is a non-parametric method which improves its accuracy as the number of data increases. While having higher computational complexity as compared to $k$-NN, GPR tends to better interpolate, resulting in higher approximation accuracy. Given the database $\{{\mathbf{X}},{\mathbf{Y}}\}$, GPR assigns a Gaussian prior to the joint probability of $\mathbf{Y}$, i.e., ${p{(\left. {\mathbf{Y}} \middle| {\mathbf{X}} \right.)}} = {\mathcal{N}\left( {{\mathbf{μ}}{({\mathbf{X}})}},{{\mathbf{K}}{({\mathbf{X}},{\mathbf{X}})}} \right)}$.

<!-- chunk {"id": "body-0014", "role": "body", "section": "III-A2 Gaussian Process Regressor (GPR)", "weight": 1.0} -->

To predict the output ${\mathbf{y}}^{\ast}$ given a new input ${\mathbf{x}}^{\ast}$, GPR constructs the joint probability distribution of the training data and the prediction, and then conditions on the training data to obtain the predictive distribution of the output, ${p{(\left. {\mathbf{y}}^{\ast} \middle| {\mathbf{x}}^{\ast} \right.)}} \sim {\mathcal{N}{({\mathbf{m}},\mathbf{\Sigma})}}$, where $\mathbf{m}$ is the posterior mean computed as and $\mathbf{\Sigma}$ is the posterior covariance which provides a measure of uncertainty on the output. In this work we simply use the posterior mean $\mathbf{m}$ as the output, i.e., ${\mathbf{y}}^{\ast} = {\mathbf{m}}$.

<!-- chunk {"id": "body-0015", "role": "body", "section": "III-A2 Gaussian Process Regressor (GPR)", "weight": 1.0} -->

While having good approximation accuracy, one major limitation with GPR is that it does not scale well with very large datasets. There are variants of GPR that attempt to overcome this problem, e.g., sparse GPR or using Stochastic Variational Inference (SVI). More details on GPR can be found in and.

<!-- chunk {"id": "body-0016", "role": "body", "section": "III-A3 Bayesian Gaussian Mixture Regression (BGMR)", "weight": 1.0} -->

When using RBF as the covariance function, GPR assumes that the mapping from $\mathbf{x}$ to $\mathbf{y}$ is smooth and continuous. When this assumption is met, it performs very well, but otherwise it will yield poor results. For example, when there is discontinuity in the mapping or there are multimodal outputs, GPR tends to average the solutions from both sides of the discontinuity or from both modes. This characteristic is also shared by many other function approximators. To handle discontinuity and multimodality problems, using local models is one of the possible solutions. Each local model can be fit to each side of the discontinuity or to each mode.

<!-- chunk {"id": "body-0017", "role": "body", "section": "III-A3 Bayesian Gaussian Mixture Regression (BGMR)", "weight": 1.0} -->

Gaussian Mixture Regression (GMR) is an example of such local models approaches. It can be seen as a probabilistic mixture of linear regressions. Given the database $\{{\mathbf{X}},{\mathbf{Y}}\}$ it can be used to construct the joint probability of $({\mathbf{x}},{\mathbf{y}})$ as a mixture of Gaussians where $\pi_{k}$, ${\mathbf{μ}}_{k}$, and $\mathbf{\Sigma}_{k}$ are the $k$-th component's mixing coefficient, mean, and covariance, respectively. Given a query ${\mathbf{x}}^{\ast}$, the conditional probability of the output ${\mathbf{y}}^{\ast}$ is also a mixture of Gaussians.

<!-- chunk {"id": "body-0018", "role": "body", "section": "III-A3 Bayesian Gaussian Mixture Regression (BGMR)", "weight": 1.0} -->

In GMR, the parameters $\pi_{k}$, ${\mathbf{μ}}_{k}$ and $\mathbf{\Sigma}_{k}$ are determined from the data by Expectation-Maximization method, while the number of Gaussians $K$ is usually determined by the user. Bayesian GMR (BGMR) is a Bayesian extension of GMR that allows us to estimate the posterior distribution of the mixture parameters (instead of relying on a single point estimate as in GMR). The number of components $K$ can also be automatically determined from the data. As a Bayesian model, BGMR gives priors to the parameters $\pi_{k}$, ${\mathbf{μ}}_{k}$ and $\mathbf{\Sigma}_{k}$, and computes the posterior distribution of those parameters given the data. In high dimensional problems, the prior reduces the overfitting that commonly occurs with GMR.

<!-- chunk {"id": "body-0019", "role": "body", "section": "III-A3 Bayesian Gaussian Mixture Regression (BGMR)", "weight": 1.0} -->

The prediction ${\mathbf{y}}^{\ast}$, given the input ${\mathbf{x}}^{\ast}$, is then computed by marginalizing over the posterior distribution and conditioning on ${\mathbf{x}}^{\ast}$. The resulting predictive distribution of $\mathbf{y}$ is a mixture of t-distributions, where $p{(\left. k \middle| {{\mathbf{x}}^{\ast},{\mathbf{X}},{\mathbf{Y}}} \right.)}$ is the probability of ${\mathbf{x}}^{\ast}$ belonging to the $k$-th component of the mixture, and $p{(\left.

<!-- chunk {"id": "body-0020", "role": "body", "section": "III-A3 Bayesian Gaussian Mixture Regression (BGMR)", "weight": 1.0} -->

{\mathbf{y}}^{\ast} \middle| {k,{\mathbf{x}}^{\ast},{\mathbf{X}},{\mathbf{Y}}} \right.)}$ is a multivariate t-distribution, the mean of which is linear in ${\mathbf{x}}^{\ast}$. We can interpret (5 ‣ III-A Building a Memory of Motion ‣ III Method ‣ Memory of Motion for Warm-starting Trajectory Optimization")) as $K$ probabilistic linear regression models, each of which has the probability of $p{(\left. k \middle| {{\mathbf{x}}^{\ast},{\mathbf{X}},{\mathbf{Y}}} \right.)}$. More details about BGMR can be found.

<!-- chunk {"id": "body-0021", "role": "body", "section": "III-A3 Bayesian Gaussian Mixture Regression (BGMR)", "weight": 1.0} -->

To obtain a point-prediction ${\mathbf{y}}^{\ast}$ from (5 ‣ III-A Building a Memory of Motion ‣ III Method ‣ Memory of Motion for Warm-starting Trajectory Optimization")), there are several approaches. One of the most used is to take the mean of the predictive distribution in (5 ‣ III-A Building a Memory of Motion ‣ III Method ‣ Memory of Motion for Warm-starting Trajectory Optimization")) using moment matching. While this approach can provide smooth estimates (as required in many applications), the same problems as in GPR will appear in the case of discontinuity and multimodality; taking average in those cases will give us poor results. Instead, we propose to take, as the point prediction, the mean^11^1As in Gaussian distribution, the mean of a multivariate t-distribution is also its mode. of the component in (5 ‣ III-A Building a Memory of Motion ‣ III Method ‣ Memory of Motion for Warm-starting Trajectory Optimization")) having the highest probability, which approximately corresponds to the mode of the multimodal distribution.

<!-- chunk {"id": "body-0022", "role": "body", "section": "III-A3 Bayesian Gaussian Mixture Regression (BGMR)", "weight": 1.0} -->

Alternatively, we can also use the mean of each t-distributions as separate predictions, which gives us several possible solutions. In some cases (e.g., when we would like to retrieve all possible solutions) this approach can be very useful, as will be presented in Section IV-A.

<!-- chunk {"id": "body-0023", "role": "body", "section": "III-A4 Dimensionality reduction", "weight": 1.0} -->

In our problem, the path ${\mathbf{y}} \in {\mathbb{R}}^{DT}$ is a vector consisting of the sequence of configurations with dimension $D$ during $T$ time steps, which can be very high. This motivates us to use dimensionality reduction techniques to reduce the dimension of $\mathbf{y}$. For example, when $T$ is large and the time interval is small, RBF can be used to represent the evolution of each variable as weights of the basis functions. Techniques such as Principal Component Analysis (PCA), Independent Component Analysis, Factor Analysis, and Variational Autoencoder can also be used. The mapping to be learned then becomes the mapping from $\mathbf{x}$ to $\hat{\mathbf{y}}$, where $\hat{\mathbf{y}}$ is the projection of $\mathbf{y}$ to the lower dimensional subspace. The advantage is that the memory required to store the data is reduced significantly, while the approximation performance is maintained or even improved because the important correlations between the variables are preserved.

<!-- chunk {"id": "body-0024", "role": "body", "section": "III-A4 Dimensionality reduction", "weight": 1.0} -->

In this work, since the number of time steps is not large, we use PCA to reduce the dimension of $\mathbf{y}$.

<!-- chunk {"id": "body-0025", "role": "body", "section": "III-A4 Dimensionality reduction", "weight": 1.0} -->

INPUT: number of samples N OUTPUT: the database {X, Y} and the function approximator f 3: sample a random task xi 4: compute the initial guess ${\overset{\sim}{\mathbf{y}}}_{i}$ to achieve xi by straight-line motion 5: solve xi using TrajOpt warm-started by ${\overset{\sim}{\mathbf{y}}}_{i}$, to obtain the path yi 10:apply PCA to Y to obtain $\hat{\mathbf{Y}}$ (Optional) 11:train the function approximator f on {X, Y} (or on $\left\{ {\mathbf{X}},\hat{\mathbf{Y}} \right\}$ if PCA is used) Algorithm 1 Building a Memory of Motion INPUT: A list of goals {xj}j = 1M, a function approximator f OUTPUT: The optimal goal x* and the corresponding path y* 2: compute the initial guess

<!-- chunk {"id": "body-0026", "role": "body", "section": "III-A4 Dimensionality reduction", "weight": 1.0} -->

1:for all j = 1, 2, …, M do in parallel 2: compute the initial guess ${\overset{\sim}{\mathbf{y}}}_{j}$ = fj (x*) 3: solve x* using TrajOpt warm-started by ${\overset{\sim}{\mathbf{y}}}_{j}$, to obtain the path yj 6: Terminate the parallel execution Algorithm 3 Ensemble Method

<!-- chunk {"id": "body-0027", "role": "body", "section": "III-B Using the Memory as a Metric", "weight": 1.0} -->

In some planning problems, there can be several alternative goals to be achieved. For example, in robot drilling task, the orientation around the drilling axis is free (the number of possible goals is infinite). A naive way is to choose one of the goals randomly, plan the motion, and if it fails then select another goal. While this is simple to implement, it does not make use of the benefit of having multiple goals. Another method is to plan the paths to each goal and select the one having the smallest cost, but this is computationally expensive. It will be useful, therefore, to have a metric that measures the cost to a given goal. Our idea is to use the memory of motion as the metric.

<!-- chunk {"id": "body-0028", "role": "body", "section": "III-B Using the Memory as a Metric", "weight": 1.0} -->

In Section III-A, function approximators were trained to predict an initial guess to achieve a task $\mathbf{x}$. The possible goals can then be formulated as multiple tasks $\{{\mathbf{x}}_{0},{\mathbf{x}}_{1},\ldots,{\mathbf{x}}_{M - 1}\}$. For each task ${\mathbf{x}}_{i}$, the function approximator predicts the initial guess ${\overset{\sim}{\mathbf{y}}}_{i}$ corresponding to the task, and the cost $\ell{({\overset{\sim}{\mathbf{y}}}_{i})}$ can be computed.

<!-- chunk {"id": "body-0029", "role": "body", "section": "III-B Using the Memory as a Metric", "weight": 1.0} -->

The initial guess ${\overset{\sim}{\mathbf{y}}}_{i}^{\ast}$ and the corresponding task ${\mathbf{x}}_{i}^{\ast}$ with the lowest cost is then taken as the chosen goal to be given to the trajectory optimizer. Since the cost computation (the total discrete velocity in ) can be done quickly relative to optimization time, this approach can yield significant improvements to the trajectory optimizer performance.

<!-- chunk {"id": "body-0030", "role": "body", "section": "III-C Using Ensemble Method to Provide Warm-Start", "weight": 1.0} -->

In machine learning, methods such as AdaBoost and Random Forests have shown that using an ensemble of methods often yields improved performances as compared to choosing a single method. We propose to use an ensemble method where we run multiple trajectory optimizations in parallel, each one warm-started by one of the function approximators in Section III-A, and once one of them finds a successful path the others are terminated. Since each function approximator has different learning characteristics, combining them in this way can significantly improve the motion planning performance. The method in Section III-B can also be used as one of the ensemble's component.

<!-- chunk {"id": "body-0031", "role": "body", "section": "Experiments", "weight": 1.0} -->

To evaluate the proposed method, we consider several examples of motion planning for PR2 and Atlas robots. TrajOpt is used as the trajectory optimizer to be warm-started. The output is the robot path that accomplishes the given task. In this paper we only work with robot path as the output, but the method can also be applied to robot trajectory.

<!-- chunk {"id": "body-0032", "role": "body", "section": "Experiments", "weight": 1.0} -->

We consider 5 motion planning cases presented in ascending order of complexity. Each case is chosen to demonstrate certain characteristics of the proposed method. For each case, we follow the following procedures. First we generate the dataset by randomly sampling $N_{\text{train}}$ tasks from a uniform distribution and run TrajOpt to find the paths achieving the tasks. The number of time steps $T$ is set to $30$, except for Atlas ($T = 15$). In all cases, the cost is defined as the discrete velocity of the states, as defined. The number of $N_{\text{train}}$ is different for each case, depending on the complexity of the task. The function approximators are then trained with or without PCA using the dataset. We heuristically set $50$ components for the PCA; for the $k$-NN, we use $K = 1$.

<!-- chunk {"id": "body-0033", "role": "body", "section": "Experiments", "weight": 1.0} -->

To validate the performance, we sample $N_{\text{test}}$ random tasks and use the various methods to warm-start TrajOpt. The solutions are compared in terms of *convergence time*, *success rate* and *cost*. The planning is considered successful if the solution is feasible. The comparison results are presented in the Tables I-VI. The values are averaged over $N_{\text{test}}$ tasks, and the standard deviation is also given for the convergence time and the cost. In the presented results, we use the label 'STD' to refer to the solution obtained by warm-starting the solver with a straight-line path (via waypoint, if any), and the names of the function approximators for the rest. The subscript 'PCA' is added when PCA is used. The query time for predicting the warm-starts by each method is negligible w.r.t. the convergence time, i.e. less than 5 ms for most methods, except for BGMR without PCA (around 20ms), so they are not included in the comparison.

<!-- chunk {"id": "body-0034", "role": "body", "section": "Experiments", "weight": 1.0} -->

The codes to run the experiments are provided in and the videos are submitted as supplementary file.

<!-- chunk {"id": "body-0035", "role": "body", "section": "IV-A Base motion planning", "weight": 1.0} -->

The task is to plan the motion for the PR2 mobile base from a random pose in front of the kitchen to another random pose behind the kitchen (Fig. 1a). In this case, the state $\mathbf{q}$ is the 3 DoF planar pose of the base. The task descriptor is then ${\mathbf{x}} = {({\mathbf{q}}_{\text{init}}^{\top},{\mathbf{q}}_{\text{goal}}^{\top})}^{\top}$. The database is constructed with $N_{\text{train}} = 200$ samples and the evaluation is performed with $N_{\text{test}} = 100$. Although this is an easy problem, TrajOpt actually finds it difficult to solve without a proper initialization.

<!-- chunk {"id": "body-0036", "role": "body", "section": "IV-A Base motion planning", "weight": 1.0} -->

For example, initializing TrajOpt with a straight-line interpolation from ${\mathbf{q}}_{\text{init}}$ to ${\mathbf{q}}_{\text{goal}}$ never manages to find a feasible solution because it results in a path that moves the robot through the kitchen while colliding, and the solver get stuck in poor local optima due to the conflicting gradients. To obtain better initialization for building the database, we initialize TrajOpt with two manually chosen waypoints on the left and on the right of the kitchen (${\mathbf{q}}_{\text{left}}$ and ${\mathbf{q}}_{\text{right}}$, respectively).

<!-- chunk {"id": "body-0037", "role": "body", "section": "IV-A Base motion planning", "weight": 1.0} -->

We consider two cases of building the database: in the first one, we only use ${\mathbf{q}}_{\text{right}}$ as waypoint, while in the second we use both ${\mathbf{q}}_{\text{left}}$ and ${\mathbf{q}}_{\text{right}}$. We initialize TrajOpt with the straight-line motion from ${\mathbf{q}}_{\text{init}}$ to the waypoint and from the waypoint to ${\mathbf{q}}_{\text{goal}}$. With this setting we build the database, train the function approximators, and obtain the results as shown in Table I and II.

<!-- chunk {"id": "body-0038", "role": "body", "section": "IV-A Base motion planning", "weight": 1.0} -->

In the first case, the mapping from $\mathbf{x}$ to $\mathbf{y}$ is unimodal because all movements go through the right. Table I shows that the performance of $k$-NN, GPR and BGMR are quite similar. In the second case, however, the output is multimodal because the database contains two possible ways (modes) to accomplish the same task. This affects GPR significantly (see Table II), as GPR averages both modes and outputs a path that goes through the kitchen, while $k$-NN and BGMR are not affected. $k$-NN does not average the modes because we use $K = 1$, while BGMR overcomes the multimodality by constructing local models for each mode automatically.

<!-- chunk {"id": "body-0039", "role": "body", "section": "IV-A Base motion planning", "weight": 1.0} -->

Fig. 2 shows the examples of warm-starts produced by each method in the second case. As expected, GPR provides a warm-start that goes through the kitchen (hence 0 success rate). With BGMR, if we retrieve the components with the two highest probability, both possible solutions are obtained.

<!-- chunk {"id": "body-0040", "role": "body", "section": "IV-B Planning from a fixed initial configuration to a random goal configuration", "weight": 1.0} -->

Here $\mathbf{q}$ consists of $14$ joint angles of the two $7$ DoFs arms of PR2. The task $\mathbf{x}$ is to move from a fixed ${\mathbf{q}}_{\text{init}}$ to a random goal configuration ${\mathbf{q}}_{\text{goal}}$ (i.e. ${\mathbf{x}} = {\mathbf{q}}_{\text{goal}}$). The database is constructed with $N_{\text{train}} = 500$, and the evaluation results with $N_{\text{test}} = 250$ are presented in Table III.

<!-- chunk {"id": "body-0041", "role": "body", "section": "IV-B Planning from a fixed initial configuration to a random goal configuration", "weight": 1.0} -->

Since each PR2 arm is redundant, the path from ${\mathbf{q}}_{\text{init}}$ to ${\mathbf{q}}_{\text{goal}}$ can be multimodal, which may pose a problem for GPR. However, Table III shows that GPR and BGMR perform similarly. This is due to the fact that although redundant robots can achieve a goal configuration in many different ways, planning using optimization here results in similar motions for similar goal configurations. The use of PCA does not improve the performance significantly, but it still helps to reduce the size of the data. In this case, for each path it reduces the number of variables from $30 \times 14$ ($D \times T$) to $50$ (number of PCA components), more than 8 times reduction while maintaining the performance.

<!-- chunk {"id": "body-0042", "role": "body", "section": "IV-C Planning from a random initial configuration to a random goal configuration", "weight": 1.0} -->

To proceed with a more complex case, the task here is to plan a path from a random initial configuration ${\mathbf{q}}_{\text{init}}$ to a random target ${\mathbf{q}}_{\text{goal}}$. The task $\mathbf{x}$ consists of the initial and goal configurations, ${\mathbf{x}} = {({\mathbf{q}}_{\text{init}}^{\top},{\mathbf{q}}_{\text{goal}}^{\top})}^{\top}$. The database is constructed with $N_{\text{train}} = 500$ and evaluated with $N_{\text{test}} = 250$. The result is presented in Table IV. $k$-NN performs poorly here, similar to STD, due to the dimension of the input space $\mathbf{x}$ that is much larger as compared to Section IV-B. To achieve good performance, $k$-NN requires a much denser dataset.

<!-- chunk {"id": "body-0043", "role": "body", "section": "IV-C Planning from a random initial configuration to a random goal configuration", "weight": 1.0} -->

GPR outperforms BGMR by a wide margin.

<!-- chunk {"id": "body-0044", "role": "body", "section": "IV-C Planning from a random initial configuration to a random goal configuration", "weight": 1.0} -->

The last row of Table IV shows the result of the ensemble method described in Section III-C. Given an input ${\mathbf{x}}^{\ast}$, the method uses all function approximators to provide different warm-starts, each of which is used to initialize an instance of TrajOpt in parallel. Once a valid solution is obtained, the other instances of TrajOpt are terminated. This method results in a huge boost of the success rate, with comparable convergence time and cost to the other methods. As comparison, we also include here the standard multiple initializations suggested by TrajOpt (labeled as 'waypoints'). Each initialization is created by interpolating through a waypoint that is manually defined. While the success rate is high, the convergence time and the cost increase significantly. On the contrary, each initialization in the ensemble method has a good probability of being close to the optimal solution, resulting in lower cost and convergence time.

<!-- chunk {"id": "body-0045", "role": "body", "section": "IV-D Planning to Cartesian goals from a fixed initial configuration", "weight": 1.0} -->

In Section IV-B and IV-C, we use TrajOpt to plan to goals in configuration space. In practical situations, however, the task is often to reach a certain Cartesian pose using the end-effector (e.g., to pick an object on the shelf), instead of planning to a specific joint configuration. One way to solve this problem is to first compute a configuration that achieves the Cartesian pose using an inverse kinematic solver and plan to this configuration, but it does not make use of the flexibility inherent in the task. TrajOpt has an option to plan directly to a Cartesian goal, but it typically requires longer convergence time and lower success rate than planning to a joint configuration goal.

<!-- chunk {"id": "body-0046", "role": "body", "section": "IV-D Planning to Cartesian goals from a fixed initial configuration", "weight": 1.0} -->

We present two approaches to use the memory of motion in this problem. In the first approach, we rely on the similar procedure as in previous cases: we formulate the task as ${\mathbf{x}} = {({\mathbf{p}}_{\text{left}}^{\top},{\mathbf{p}}_{\text{right}}^{\top})}^{\top}$ where ${\mathbf{p}}_{\text{left}}$ and ${\mathbf{p}}_{\text{right}}$ are the Cartesian positions of the right and left hand of PR2. The database is then constructed with $N_{\text{train}} = 1000$ and the function approximators are trained. In this approach, TrajOpt plans to a Cartesian goal directly. The second approach relies on the fact that a Cartesian goal corresponds to multiple goals in configuration space.

<!-- chunk {"id": "body-0047", "role": "body", "section": "IV-D Planning to Cartesian goals from a fixed initial configuration", "weight": 1.0} -->

In Section IV-B we have already constructed several function approximators that can predict an initial guess $\overset{\sim}{\mathbf{y}} = {\overset{\sim}{\mathbf{q}}}_{0:T}$, given a goal ${\mathbf{q}}_{\text{goal}}$ in configuration space. The second approach uses one of them as a metric (Sect. III-B) to choose between the different goals in configuration space. First, given a Cartesian goal $\mathbf{x}$, we run an inverse kinematic solver to find $M = 5$ joint configurations that satisfy this pose. For each joint configuration, we use the function approximator to predict the initial guess of the robot path to reach that configuration, and we compute the cost of that path. Finally, the goal configuration and the path with the lowest cost are chosen, and TrajOpt is run to reach this goal configuration with the given path as the warm-start. Note that in this second approach, TrajOpt plans to a joint configuration instead of a Cartesian goal.

<!-- chunk {"id": "body-0048", "role": "body", "section": "IV-D Planning to Cartesian goals from a fixed initial configuration", "weight": 1.0} -->

For this approach we choose the method $\text{GPR}_{\text{PCA}}$ from the Section IV-B, and use the term '$\text{METRIC GPR}_{\text{PCA}}$' to differentiate from the first approach (denoted in standard notation).

<!-- chunk {"id": "body-0049", "role": "body", "section": "IV-D Planning to Cartesian goals from a fixed initial configuration", "weight": 1.0} -->

We present the results in Table V with $N_{\text{test}} = 250$. Among the methods using the first approach, we note that BGMR yields better result than GPR because the mapping from the Cartesian goal $\mathbf{x}$ to the robot path $\mathbf{y}$ here is multimodal, as planning to a Cartesian pose has more redundancy as compared to planning to a joint configuration. This again demonstrates that BGMR handles multimodal output better than GPR. However, the second approach $\text{METRIC GPR}_{\text{PCA}}$ outperforms even BGMR. The improvement over the first approach is very significant in all three criteria. This demonstrates that using the memory as a metric to choose the optimal goal results in large improvements. We point out that the additional computational time required to find $M = 5$ IK solutions and the corresponding warm-starts is only around $0.1$ s, which is negligible compared to the convergence time.

<!-- chunk {"id": "body-0050", "role": "body", "section": "IV-D Planning to Cartesian goals from a fixed initial configuration", "weight": 1.0} -->

Finally, we use the ensemble method that uses all function approximators in parallel, including $\text{METRIC GPR}_{\text{PCA}}$. This boosts the success rate to 98%.

<!-- chunk {"id": "body-0051", "role": "body", "section": "IV-E Planning whole-body motion for an Atlas robot", "weight": 1.0} -->

Finally, we also applied our method for planning the motion of the 34-DoFs Atlas robot (28-DoFs joints and 6-DoFs root pose). We consider the same task as in Section IV-D, i.e. planning from a fixed initial configuration to a random Cartesian pose, in this case chosen to be the location of Atlas' right hand. The task ${\mathbf{x}} = {(p_{x},p_{y},p_{z})}^{\top}$ corresponds to the target position of Atlas' right hand, while the orientation is not constrained. The feet location are fixed, while the Zero Moment Point (ZMP) is constrained to be between the two feet location. We use here the first approach as explained in Section IV-D, i.e. treating it as a regression problem where the input $\mathbf{x}$ is the Cartesian goal and the output $\mathbf{y}$ is the trajectory, and use the various function approximators to predict the initial guesses.

<!-- chunk {"id": "body-0052", "role": "body", "section": "IV-E Planning whole-body motion for an Atlas robot", "weight": 1.0} -->

The database is constructed with $N_{\text{train}} = 1000$ and the evaluation is performed with $N_{\text{test}} = 250$. The results are presented in Table VI. $k$-NN performs quite well, as the input size of $\mathbf{x}$ is small (the position of the hand is constrained to be inside the shelf). Unlike in Section IV-D, the performance of GPR and BGMR are quite similar, although the goals are also in the Cartesian space. This is due to the difference in the implementation; in Section IV-D, given a Cartesian goal, we use an inverse kinematic solver to calculate the joint configuration that satisfies this goal, and calculate the initial guess as straight-line interpolation from the fixed initial configuration to the goal configuration. This initial guess is used when building the database. Due to the redundancy of the PR2 dual arm, similar Cartesian goals can correspond to very different joint configurations, resulting in the multimodality of the solutions in the database.

<!-- chunk {"id": "body-0053", "role": "body", "section": "IV-E Planning whole-body motion for an Atlas robot", "weight": 1.0} -->

In this Atlas experiment, however, we do not provide initial guesses to TrajOpt when building the database, so TrajOpt always tries to solve the problem with zero initialization. This results in more uniform solutions, and hence GPR can still perform quite well. Finally, using the ensembe method again shows superior results, giving us an increase of the success rate by more than 10%.

<!-- chunk {"id": "body-0054", "role": "body", "section": "IV-E Planning whole-body motion for an Atlas robot", "weight": 1.0} -->

Planning for such high DoFs problem with many constraints (feet location, ZMP constraint, kinematic constraint) requires quite a lot of computational time ($\sim$ 6.3 s in average without warm-start). Using the memory of motion in this complex task further exemplify the benefit of the approach, as our method speeds up the computational time significantly by more than four times faster. We note that the tasks are sampled randomly, and there is no guarantee that the task is indeed feasible. This explains why even the best method (i.e. the ensemble method) only achieves $\sim$ 70% success rates.

<!-- chunk {"id": "body-0055", "role": "body", "section": "V-A Choice of function approximators", "weight": 1.0} -->

In Section IV, we have compared the performance of $k$-NN, GPR and BGMR over different tasks, and shown that they have different characteristics. When the dataset is quite dense or the input space is small, $k$-NN usually manages to obtain good performance (as shown in Section IV-A, IV-B, and IV-D), while for larger input space (Section IV-D) it does not yield good results. GPR performs the best when the output is unimodal (Section IV-B and IV-C), while for multimodal output BGMR has a better performance than GPR (Section IV-D). This comparison can guide us to select the best method for each task. However, it may not be obvious whether a given task (and its solution) is unimodal or multimodal (e.g. compare Section IV-D and IV-E). A better way is to combine the different methods via an ensemble method, as we have shown in this paper.

<!-- chunk {"id": "body-0056", "role": "body", "section": "V-B Data requirement", "weight": 1.0} -->

In Fig. 3, we plot the performance of various methods against the number of training samples, with STD given as the baseline. We choose the task in Section IV-C, since it has the largest input space among the other tasks. It is interesting that when the training size is small, GPR performs quite well, while $k$-NN and BGMR are even worse than STD. As training size increases, $k$-NN and BGMR start to approach the performance of GPR. On the contrary, the performance of the ensemble method is quite stable even when the training size is small. As the training size grows, its convergence time decreases, while the success rate is already high even when the training size is small.

<!-- chunk {"id": "body-0057", "role": "body", "section": "V-C Ensemble method", "weight": 1.0} -->

Using an ensemble method for motion planning has been explored, which uses an ensemble of motion planners. While such approach also manages to boost the performance successfully, it is not easy to design and set up several motion planners for a given task. On the contrary, many function approximators are available and can be used easily, since our problem is formulated as a standard regression problem. We only need to configure one motion planner (in this work, TrajOpt, but other optimization frameworks can also be used) for a given task, unlike. Another benefit of our ensemble method is that each of the ensemble's component starts from an initial guess that has good probability of being close to the optimal solution. This reduces the average computational time, as we have shown by comparing it against the multiple waypoints initialization in Table IV.

<!-- chunk {"id": "body-0058", "role": "body", "section": "V-D Dynamic environment", "weight": 1.0} -->

In this work we assume that the environment is static, so that the trajectories previously planned remain valid. When the environment changes, a new memory of motion has to be built. For the simple example in Section IV-A, building the memory takes only $\sim$`<!-- -->`{=html}3 minutes of computational time, but complex example such as Section IV-E takes $\sim$`<!-- -->`{=html}3 hours. While paralellization can be used to speed up the building process, more effective strategies would be interesting to explore. In, an efficient way of updating a dynamic roadmap when the environment changes is presented. Such method can possibly be used to modify the existing memory of motion, so that we do not have re-build from scratch but only modify those affected. Alternatively, when the environment largely remain the same but a few obstacles are moving (as in many real tasks), we can include these obstacles' locations as additional inputs to the regression problem, at the expense of larger input size. We will explore these ideas in our future work.

<!-- chunk {"id": "body-0059", "role": "body", "section": "Conclusion", "weight": 1.5} -->

We have presented an approach to build a memory of motion to warm-start trajectory optimization solver, and demonstrate through experiments with PR2 and Atlas robots that the warm-start can improve the solver's performance. Function approximators and dimensionality reduction are used to learn the mapping between the task descriptor and the corresponding robot path. Three function approximators are considered: $k$-NN as baseline, GPR, and BGMR, and their different characteristics have been discussed. The use of PCA also improves the solution, although not very significantly, while reducing the memory storage. We have also shown that we can use the memory of motion as a metric to choose optimally between several alternative goals, and this results in a significantly improved performance for the case of Cartesian goal planning. Finally, the different function approximators can be combined as an ensemble method, which boosts the success rate significantly.
