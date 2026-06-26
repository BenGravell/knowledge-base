<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

On the Smoothness of Nonlinear System Identification

Topics include System identification, Neural networks, Datasets, Online algorithms, Optimization, Nonlinear systems, Parameter space.

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

We shed new light on the \textit{smoothness} of optimization problems arising in prediction error parameter estimation of linear and nonlinear systems. We show that for regions of the parameter space where the model is not contractive, the Lipschitz constant and beta-smoothness of the objective function might blow up exponentially with the simulation length, making it hard to numerically find minima within those regions or, even, to escape from them. In addition to providing theoretical understanding of this problem, this paper also proposes the use of multiple shooting as a viable solution. The proposed method minimizes the error between a prediction model and the observed values. Rather than running the prediction model over the entire dataset, multiple shooting splits the data into smaller subsets and runs the prediction model over each subset, making the simulation length a design parameter and making it possible to solve problems that would be infeasible using a standard approach. The equivalence to the original problem is obtained by including constraints in the optimization. The new method is illustrated by estimating the parameters of nonlinear systems with chaotic or unstable behavior, as well as neural networks. We also present a comparative analysis of the proposed method with multi-step-ahead prediction error minimization.

<!-- chunk {"id": "body-0003", "role": "body", "section": "Introduction", "weight": 1.5} -->

Prediction error methods are a widespread class of methods for parameter estimation of dynamic models, which estimate the parameters by minimizing the error between predicted and measured trajectories. Many well-known estimation methods fit into this framework, such as minimizing the one-step-ahead prediction error or the free-run-simulation error. While the classical literature focuses primarily on the estimation of linear systems, the framework is general and enjoys appealing asymptotic properties for the general nonlinear setup.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

Minimizing the one-step-ahead prediction usually yields an easier optimization problem, the minimization of the free-run simulation error or other recurrent structures, however, may produce more accurate models. These recurrent models often have a smaller generalization error, and better capability when it comes to long-term prediction. Minimizing recurrent structures is used, for instance, to improve the model structure selection of polynomial models, fine-tune parameters of nonlinear state-space and block-oriented models.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

It is common knowledge among practitioners that the optimization problem resulting from a recurrent model structure is harder to solve. For linearly parametrized models and convex loss functions, minimization of one-step-ahead prediction error leads to a convex optimization problem; for recurrent model structures, the ensuing optimization is, in general, non-convex, complicating the search for global optima. Even during local optimization, recurrent model structures can lead to cost functions with poor smoothness properties, including many 'jagged' local minima, cf. Fig. 2(a) for an illustration. The current understanding of the relationship between model internal dynamics and the smoothness properties of the cost function is, however, imprecise and provides little insight into ways of circumventing the problem. Furthermore, the few studies that do investigate the objective function properties in this context are focused on linear systems, see e.g..

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

The purpose of this paper is twofold. First, we aim to provide insight into the properties of the objective function arising in prediction error estimation problems in a general nonlinear setup. Specifically, we show how the smoothness of the objective function depends on two factors: the simulation length and the decay rate of the recurrent part of the prediction model. Second, we illustrate how this theoretical insight might be leveraged for the design and analysis of practical system identification methods.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

The use of multiple shooting is analyzed in the context of prediction error minimization. This technique reformulates the optimization problem that arises from minimizing the difference between the output of a prediction model and the observed values. Rather than running the prediction model over the entire dataset, the multiple shooting formulation splits the dataset into smaller subsets and runs the prediction model over each subset. The equivalence with the original problem is obtained by including equality constraints in the optimization problem. This method results in a smoother objective function since it works with shorter simulations and prevents trajectories from diverging too much.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Introduction", "weight": 1.5} -->

The multiple shooting formulation has reportedly provided improvements in the parameter estimation of ordinary differential equations and in the solution of optimal control. In the context of system identification, multiple shooting has been used for estimating polynomial nonlinear space-state models and output error models in settings where conventional methods fail to provide good solutions. Here, we extend this method to the entire class of prediction error methods. In addition, theoretical arguments are put forward to help understand why and when the proposed method is useful. We also present a comparative analysis with multi-step-ahead prediction error minimization showing strengths and weaknesses of each method at a conceptual level and, also, with numerical examples.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Prediction error methods", "weight": 1.0} -->

While prediction error methods are widely known, they are often introduced from a linear perspective. In the present section, this is accomplished in a nonlinear setting.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Prediction error methods", "weight": 1.0} -->

Consider the dataset $\mathcal{Z}^{N} = {\{{(\mathbf{u}{\lbrack k\rbrack},\mathbf{y}{\lbrack k\rbrack})},k = 1,2,\cdots,N\}}$ containing $N$ measured inputs and outputs of a dynamical system. Prediction error methods assume an internal model that delivers output predictions $\hat{\mathbf{y}}{\lbrack k\rbrack}$, $k = {1,2,\cdots,N}$. A cost function is defined as the distance between predictions and measured values: The prediction model is, usually, parametrized by a parameter vector $\mathbf{θ}$ and, although such a dependence is not made explicit in the notation, $\hat{\mathbf{y}}{\lbrack k\rbrack}$ depends upon $\mathbf{θ}$. An estimate $\hat{\mathbf{θ}}$ of the parameter vector may be obtained by minimizing $V$.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Prediction error methods", "weight": 1.0} -->

Next we assume a dynamical, stochastic, discrete-time system as the data generating process. Let: where $n_{y}$, $n_{u}$ are the maximum input and output lags. The examples we give next will differ in how they account for the noise in the model. But, in a noiseless situation, the data generating process for all of them corresponds to a difference equation ${\mathbf{y}{\lbrack k\rbrack}} = {\mathbf{f}^{\ast}{({\underset{¯}{\mathbf{y}}{\lbrack{k - 1}\rbrack}},{\underset{¯}{\mathbf{u}}{\lbrack k\rbrack}})}}$.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Prediction error methods", "weight": 1.0} -->

The parametrized function $\mathbf{f}_{\mathbf{θ}}$ is defined and, if the noise assumption and model structure are correct, the minimization of the cost function $V$ would yield the estimate $\hat{\mathbf{θ}}$ such that, as $N\rightarrow\infty$, then $\mathbf{f}_{\hat{\mathbf{θ}}}\rightarrow\mathbf{f}^{\ast}$ (or to a function with different structure but the same performance in predicting the training dataset). See Appendix D for a more precise description of the asymptotic properties of nonlinear prediction error methods.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Prediction error methods", "weight": 1.0} -->

Choosing the "true" model structure (one for which there exists a ${\mathbf{θ}}^{\ast}$ such that $\mathbf{f}_{{\mathbf{θ}}^{\ast}} = \mathbf{f}^{\ast}$) might be impossible in a practical application. Nevertheless the assumption is not so restrictive as it might appear, since there exist families of universal approximator functions (e.g. neural networks and polynomials) for which the distance $\|{\mathbf{f}_{\mathbf{θ}} - \mathbf{f}^{\ast}}\|$ might be made arbitrarily small within a compact set.

<!-- chunk {"id": "body-0014", "role": "body", "section": "Nonlinear ARX models", "weight": 1.0} -->

The nonlinear ARX (autoregressive with exogenous input) model encodes an output that is corrupted by white process noise. That is, it assumes the data were generated by the stochastic discrete-time system: where $\mathbf{v}{\lbrack k\rbrack}$ is a zero-mean white noise. This assumption yields (cf. Appendix D) the prediction model: The minimization of the cost function in Eq. for this prediction model yields an estimator with the desired asymptotic properties.

<!-- chunk {"id": "body-0015", "role": "body", "section": "Nonlinear OE models", "weight": 1.0} -->

The OE (output error) model encodes an output that is corrupted by white measurement noise. That is, it is assumed that the data were generated: where, again, $\mathbf{v}{\lbrack k\rbrack}$ is zero-mean white noise and $\overline{\mathbf{y}}{\lbrack k\rbrack}$ represents the noiseless output. This assumption yields the following prediction model: Here $\overset{\sim}{\mathbf{y}}{\lbrack k\rbrack}$ represents an estimate of the noiseless output $\overline{\mathbf{y}}{\lbrack k\rbrack}$, which should approach the true value as ${\mathbf{θ}}\rightarrow{\mathbf{θ}}^{\ast}$.

<!-- chunk {"id": "body-0016", "role": "body", "section": "Nonlinear ARMAX models", "weight": 1.0} -->

The nonlinear ARMAX (autoregressive moving average with exogenous input) model encodes an output that is corrupted by additive zero-mean process noise. In this case, the propagation equation allows the noise term $\mathbf{v}{\lbrack k\rbrack}$ to be propagated by the dynamics: This assumption allows the model to account for some forms of colored process noise and results in the following prediction model: Here $\overset{\sim}{\mathbf{v}}{\lbrack k\rbrack}$ represents an estimate of the noise corrupting the system and will approach the true noise if the estimated parameter vector approaches the true parameter value ${\mathbf{θ}}^{\ast}$.

<!-- chunk {"id": "body-0017", "role": "body", "section": "General nonlinear state-space framework", "weight": 1.0} -->

From now, we will focus on a state-space representation that is general enough to encompass the prediction model from the above examples (for an appropriate choice of the functions $\mathbf{h}$ and $\mathbf{g}$). For this representation, the predicted output is given: where $\text{x}{\lbrack k\rbrack}$ denotes the internal state vector at instant $k$.

<!-- chunk {"id": "body-0018", "role": "body", "section": "General nonlinear state-space framework", "weight": 1.0} -->

Here ${\underset{¯}{\mathbf{z}}{\lbrack k\rbrack}} = {({\underset{¯}{\mathbf{y}}{\lbrack{k - 1}\rbrack}},{\underset{¯}{\mathbf{u}}{\lbrack k\rbrack}})}$. Using both inputs $\underset{¯}{\mathbf{u}}{\lbrack k\rbrack}$ and autoregressive terms $\underset{¯}{\mathbf{y}}{\lbrack{k - 1}\rbrack}$ is what allows this state-space representation to encompass ARX, ARMAX and OE models, and also other representations such as the polynomial greybox models proposed.

<!-- chunk {"id": "body-0019", "role": "body", "section": "Initial conditions", "weight": 1.0} -->

In order to guarantee the desirable asymptotic properties, the prediction model needs to be simulated starting with the appropriate initial conditions $\mathbf{x}_{0}$. Since the true initial condition $\mathbf{x}_{0}^{\ast}$ is unknown, there are two possible approaches when estimating the parameters.

<!-- chunk {"id": "body-0020", "role": "body", "section": "Initial conditions", "weight": 1.0} -->

The first approach is to fix $\mathbf{x}_{0}$, for some $\mathbf{x}_{0} \approx \mathbf{x}_{0}^{\ast}$, and minimize the cost function. This approach is based on the idea that, for an asymptotically stable system, the influence of the initial conditions on the output will decrease over time for many cases of interest and, hence, even if $\mathbf{x}_{0} \neq \mathbf{x}_{0}^{\ast}$ we can still obtain a good estimate of the parameters. In this case the first samples may be discarded, to make sure the transient errors are not too large.

<!-- chunk {"id": "body-0021", "role": "body", "section": "Initial conditions", "weight": 1.0} -->

The second approach consists in including $\mathbf{x}_{0}$ in the optimization problem, so it converges to $\mathbf{x}_{0}^{\ast}$ and improves the quality of the parameter estimates.

<!-- chunk {"id": "body-0022", "role": "body", "section": "Smoothness of prediction error methods", "weight": 1.0} -->

The theorem below relates the Lipschitz constant of $V$, and its gradient (i.e. $\beta$-smoothness), to the simulation length $N$. The Lipschitz constant of the cost function and the $\beta$-smoothness both play a crucial role in optimization. Lower values imply that local (Taylor) expansions of the cost function are more predictive of the cost function, and that the optimization algorithm can still converge while taking larger steps. It also gives an upper bound on how distinct in performance two close local minima may be.

<!-- chunk {"id": "body-0023", "role": "body", "section": "Smoothness of prediction error methods", "weight": 1.0} -->

The first part of the theorem below can be seen as a formalization of the exploding gradient problem, often studied in the context of neural networks. The second part provides information about the explosion of second-order derivatives and curvature and it is, to the best of our knowledge, novel. As a result of the analysis, it is found that not only walls (resulting from large first-order derivatives) might be formed in non-contractive regions of the parameter space, but also regions with exploding curvature with multiple close local minima (cf. Fig. 2(a)). A recurrent neural network-oriented perspective of these results is discussed in a concurrent work from our group.

<!-- chunk {"id": "body-0024", "role": "body", "section": "Multiple shooting", "weight": 1.0} -->

The theoretical results from the previous section suggest that long simulation lengths might yield regions of the parameter space where the cost function is intricate, hence hard for the optimization algorithm to navigate.

<!-- chunk {"id": "body-0025", "role": "body", "section": "Multiple shooting", "weight": 1.0} -->

In this section, we propose the application, in the context of prediction error methods, of a technique called multiple shooting for which the maximum simulation length is a design parameter. This enables solving problems that would be impossible or very hard to solve in the setting of Section 2, which will be named single shooting from now.

<!-- chunk {"id": "body-0026", "role": "body", "section": "Method formulation", "weight": 1.0} -->

For the multiple shooting formulation, rather than simulating the prediction model through the entire dataset from a single initial condition vector $\mathbf{x}_{0}$, the data is split into $M$ intervals $\{{\lbrack{m_{i} + 1},m_{i + 1}\rbrack}\mid{i = {1,\cdots,M}}\}$, $0 = m_{1} < m_{2} < \cdots < m_{M} < m_{M + 1} = N$, each one with its own set of initial conditions $\mathbf{x}_{0}^{i} \in {\mathbb{R}}^{N_{x}}$.

<!-- chunk {"id": "body-0027", "role": "body", "section": "Method formulation", "weight": 1.0} -->

The $i$-th vector of initial conditions $\mathbf{x}_{0}^{i}$ is used to compute ${\hat{\mathbf{y}}}^{i}{\lbrack k\rbrack}$ over ${m_{i} + 1} \leq k \leq m_{i + 1}$: Since the length of the simulation is limited to the shorter interval $\lbrack{m_{i} + 1},m_{i + 1}\rbrack$, the trajectory is less likely to strongly diverge and this typically helps the optimization procedure by making the objective function smoother.

<!-- chunk {"id": "body-0028", "role": "body", "section": "Method formulation", "weight": 1.0} -->

Let ${\Deltam_{i}} = {m_{i + 1} - m_{i}}$, we define: to be the cost function associated with the $i$-th interval, where the prediction ${\hat{\mathbf{y}}}^{i}{\lbrack k\rbrack}$ depends upon $\mathbf{θ}$ and $\mathbf{x}_{0}^{i}$, according to. The multiple shooting formulation makes use of the following objective function: This objective function includes states $\mathbf{x}_{0}^{1},\cdots,\mathbf{x}_{0}^{M}$ as free variables in the optimization.

<!-- chunk {"id": "body-0029", "role": "body", "section": "Method formulation", "weight": 1.0} -->

Hence, rather than reinforcing the cohesion of the states $\mathbf{x}{\lbrack k\rbrack}$ by defining them through a recurrence relation that casts a dependency of $\mathbf{x}{\lbrack k\rbrack}$ all the way back to the initial condition $\mathbf{x}_{0}$, as in the single shooting formulation, the cohesion between subsequent states is achieved through optimization constraints, resulting in the following problem: The next theorem provides the equivalence between and. The theorem and its corollary are a formalization of the intuition provided in Fig. 1 and they give further insight into how the constraints in the multiple shooting formulation are used to imitate a single simulation throughout the entire dataset.

<!-- chunk {"id": "body-0030", "role": "body", "section": "Properties of the cost function", "weight": 1.0} -->

For the multiple shooting method, the Lipschitz constant of $V^{M}$ and of its gradient, $L_{V^{M}}$ and $L_{V^{M}}'$ depend asymptotically on ${\Delta\text{m}_{\max}} = {\max_{1 \leq i \leq M}{\Delta\text{m}_{i}}}$ rather than on $N$ (See Appendix C). For instance, if $L_{h} > 1$: Since $\Deltam_{\max}$ is a design parameter, it is possible to have some control over the Lipschitzness and $\beta$-smoothness of the objective function in the non-contractive region of the parameter space ($L_{h} \geq 1$).

<!-- chunk {"id": "body-0031", "role": "body", "section": "Implementation and numerical examples", "weight": 1.0} -->

In this section, numerical examples are presented. The cost function smoothness is investigated through the lens of the theoretical results in Section 3 and it is shown how multiple-shooting might help mitigate some problems.

<!-- chunk {"id": "body-0032", "role": "body", "section": "Implementation and numerical examples", "weight": 1.0} -->

The equality-constrained problem, which arises from the multiple shooting formulation, is solved using an implementation of the sequential quadratic programming solver originally described in available in the SciPy library ^33^3 scipy.optimize.minimize(method='trust-constr'). The procedure used for computing the derivatives is explained in Appendix A. Additional numerical examples are provided in Appendix F.

<!-- chunk {"id": "body-0033", "role": "body", "section": "OE model for a chaotic system", "weight": 1.0} -->

This example illustrates how multiple shooting makes prediction error methods more robust w.r.t. the choice of initial conditions for the optimization. A dataset with $N = 200$ samples is generated using the logistic map: with $\theta = 3.78$. From the generated dataset we try to estimate an output error model with the same structure.

<!-- chunk {"id": "body-0034", "role": "body", "section": "OE model for a chaotic system", "weight": 1.0} -->

(a) Δ mmax = N (Single Shooting) Figure 2: Logistic map parameter estimation. Cost function of the optimization problem for x0i fixed in its true values (in black) and for disturbed versions of the these initial conditions (in blue). We present the result for four values of Δ mmax, and omit disturbed initial condition objective functions for the single shooting case (Δ mmax = N) to make it easier to visualize. The green circles indicate the pair (θ, V) corresponding to a solution found by the solver. There are 15 circles in each figure (some of them overlapping), the circles correspond to solutions for different initial guesses. As initial guesses we picked values of θ uniformly spaced between 3.2 and 3.9, with x0i picked from randomly disturbed versions of the true initial conditions (which are known because we generated the data ourselves). The true value θ = 3.78 is indicated by the dotted red vertical line.

<!-- chunk {"id": "body-0035", "role": "body", "section": "OE model for a chaotic system", "weight": 1.0} -->

Fig. 2(a) illustrates the objective function for the single shooting case. The data generating system, Eq., presents chaotic behavior for $\theta \in {\lbrack 3.57,4\rbrack}$, which explains the very intricate objective function in this region. For chaotic systems, small variations in the parameters may cause large variations in the system trajectory and, consequently, abrupt changes in the free-run simulation error. This explains why the cost function used in estimating an OE model has many local minima for this problem.

<!-- chunk {"id": "body-0036", "role": "body", "section": "OE model for a chaotic system", "weight": 1.0} -->

The solutions found by the solver, for different initial guesses, are also displayed in Fig. 2(a). Notice that the solver fails to find the true solution because it always gets trapped in local stationary points near the initial guess. Even in this noiseless scenario, the estimation problem is very challenging due to the chaotic nature of the system. Hence, for a simulation that is sufficiently long, the trajectories will differ significantly even for small parameter variations.

<!-- chunk {"id": "body-0037", "role": "body", "section": "OE model for a chaotic system", "weight": 1.0} -->

Multiple shooting makes the problem easier by limiting the maximum simulation length. Fig. 2 (b), (c) and (d) display the objective function and the solutions found by the solver starting from different initial guesses. The estimation procedure becomes easier as $\Deltam_{\max}$ is made smaller. For Fig. 2(c) the solver already converges to the true parameter for some initial guesses, but not for all of them. For Fig. 2(d), the solver converges to the true solution for all initial guesses that have been tested.

<!-- chunk {"id": "body-0038", "role": "body", "section": "OE model for a chaotic system", "weight": 1.0} -->

For the multiple shooting case, besides $\theta$, the initial conditions are also optimization parameters. To help with the visualization of this multidimensional problem, Fig. 2(b), (c) and (d) display the main curve corresponding to the objective function for the true initial conditions and faded lines corresponding to the objective function for perturbed initial conditions. Another consequence of the problem having more parameters than displayed in the figure is that the cost function found by the solver does not need to lie on any of the objective function curves displayed in the figure, since it may have a different set of initial conditions $\mathbf{x}_{0}^{i}$.

<!-- chunk {"id": "body-0039", "role": "body", "section": "OE model for a chaotic system", "weight": 1.0} -->

It is important to highlight that the mechanism used here is not to take the system outside of the chaotic regime, but rather avoid simulating the system for too long. By doing that, we avoid the major problem that arises in the identification of chaotic systems, i.e. the high sensitivity to parameters and initial conditions. This results in a better behaved objective function (cf. Fig. 2). The constraints allow the equivalence with the original prediction error problem (according to Theorem 2 and Corollary 3).

<!-- chunk {"id": "body-0040", "role": "body", "section": "OE model for a chaotic system", "weight": 1.0} -->

Table 1 gives the number of function evaluations and the running time for the four situations displayed in Fig. 2. The convergence happens within just a few iterations for ${\Deltam_{\max}} = N$ (single shooting) because any initial point is probably very close to some optimal local solution. As we reduce $\Deltam_{\max}$ the objective function becomes less intricate and this is reflected in the convergence of the solver. For ${\Deltam_{\max}} = 10$ the solver takes much longer to converge. We believe this happens because the local solution is not so close in the parameter space to the initial guess anymore. As $\Deltam_{\max}$ is further decreased, however, the convergence becomes faster because it is dealing, what is believed to be, a smoother problem that can be handled more accurately by low order approximations.

<!-- chunk {"id": "body-0041", "role": "body", "section": "Pendulum and inverted pendulum", "weight": 1.0} -->

Consider the following discrete-time nonlinear system: which corresponds to a pendulum model, discretized using the Euler approximation ${\overset{˙}{x}{(t)}} \approx \frac{{x{({{({k + 1})}\delta})}} - {x{({k\delta})}}}{\delta}$, where $g$ is the gravity acceleration, $m$ is the mass connected to the extremity of the pendulum, $l$ is the length of the (massless) rod connecting the mass to the pivot point, and $k_{a}$ is the linear friction constant. It has two states: the angle of the mass ($x_{1}$) and the angular velocity ($x_{2}$). The input $u{\lbrack k\rbrack}$ is the force applied to the mass.

<!-- chunk {"id": "body-0042", "role": "body", "section": "Pendulum and inverted pendulum", "weight": 1.0} -->

For this system, with $g = 9.8$, $l = 0.3$, $m = 3$, $k_{a} = 2$ and $\delta = 0.01$, we define three different datasets: (a) A dataset for which small inputs are applied to the system, that stays under the influence of the stable point ${(x_{1},x_{2})} = {}$ and $y{\lbrack k\rbrack}$ stays, approximately, inside the range $\left\lbrack {- \frac{\pi}{2}},{+ \frac{\pi}{2}} \right\rbrack$; (b) A dataset for which the system is maintained close to the unstable point ${(x_{1},x_{2})} = {(\pi,0)}$ by a linear controller; and, (c) A dataset for which the input is large enough to drive the pendulum to full rotations around its center. The output corresponding to those three situations are displayed in Fig. 3.

<!-- chunk {"id": "body-0043", "role": "body", "section": "Pendulum and inverted pendulum", "weight": 1.0} -->

Fixing $m = 3$ and $\delta = 0.01$ parameters $\frac{g}{l}$ and $k_{a}$ of an output error model with the structure presented in were estimated from the data. A visualization of the cost function is presented in Fig. 4 together with numerical solutions found by means of the single shooting and multiple shooting formulation starting from different initial conditions.

<!-- chunk {"id": "body-0044", "role": "body", "section": "Pendulum and inverted pendulum", "weight": 1.0} -->

For dataset (a), the single shooting formulation is able to recover the true parameters from data for most of the initial conditions. Some exceptions occur when initialized far away from the correct initial conditions. For datasets (b) and (c), for which the system needs, respectively, to operate close to the unstable dynamics or to account for the existence of multiple fixed points, the cost function is highly intricate and full of local minima. In this case, the optimization algorithm, even when initialized close to the local solution, fails to converge to reasonable solutions. This result is consistent with Theorem 1 and how the smoothness of the objective function degenerates (exponentially) on sets of the parameter space for which the prediction model is non-contractive, such as the trajectories close to the unstable fixed point of the system. The use of multiple shooting yields an objective function that looks similar to a paraboloid in the region of interest for the three cases and the optimization procedure converges to the true parameter regardless of the initialization.

<!-- chunk {"id": "body-0045", "role": "body", "section": "Pendulum and inverted pendulum", "weight": 1.0} -->

For nonlinear ARX, ARMAX or OE models the states are directly measured (possibly with some noise contamination) and the initialization of the optimization parameters $\mathbf{x}_{0}^{i}$ follows naturally from the considerations in Section 2.5. Here, however, the state variable $x_{2}$ is not measured. This variable can be interpreted as the derivative of $x_{1}$, so a finite difference approximation was used in the initialization of the intermediary initial conditions $\mathbf{x}_{0}^{i}$. Although the high-pass behavior of the derivative amplifies the noise, this choice was still better than a completely arbitrary one.

<!-- chunk {"id": "body-0046", "role": "body", "section": "Multi-step-ahead prediction error minimization", "weight": 1.0} -->

Multiple-shooting is presented here as a possible way of limiting the simulation interval $\Deltam_{\max}$. A method that appears in the system identification literature that also has a similar effect is the multi-step-ahead prediction error minimization (MSA-PEM),. The approach fits well into the moving horizon framework and is popular for system identification in model predictive control application. The method has been studied primarily in a linear model setting, nevertheless it can be extended to a nonlinear setting.

<!-- chunk {"id": "body-0047", "role": "body", "section": "Multi-step-ahead prediction error minimization", "weight": 1.0} -->

Multiple shooting is equivalent, in the sense of Theorem 2 and Corollary 3, to solving the original (single shooting) problem regardless of the choice of simulation interval $\Deltam_{\text{max}}$. MSA-PEM, on the other hand, is equivalent to the original formulation only if $K = N$. The next example illustrates how the statistical properties of the method change as $K$ varies from $1$ to $N$.

<!-- chunk {"id": "body-0048", "role": "body", "section": "Example: estimating the output error model for second-order under-damped system", "weight": 1.0} -->

A dataset with $N = 300$ samples is generated using the equation: Here $\overline{y}$ represents the noiseless output, and $v$ represents the white output noise that is introduced during the data generation. At each $k$, $v{\lbrack k\rbrack}$ is a Gaussian random variable with standard deviation $\sigma_{v} = 0.05$.

<!-- chunk {"id": "body-0049", "role": "body", "section": "Example: estimating the output error model for second-order under-damped system", "weight": 1.0} -->

Let ${\mathbf{θ}} = {(\theta_{1},\theta_{2},\theta_{3})}$ denote the parameter vector used for the data generation. Three different settings are considered: (a) ${\mathbf{θ}} = {(0.5,{- 0.2},2)}$; (b) ${\mathbf{θ}} = {(1.5,{- 0.7},0.5)}$; and, (c) ${\mathbf{θ}} = {(1.8,{- 0.95},0.1)}$. The three settings correspond to underdamped linear systems with different response-times: in (a) the system responds fast to input changes and has a time constant $\tau = 0.25$; in (c), it responds slowly and $\tau = 0.9$; and, (b) is an intermediate setting with $\tau = 0.75$.

<!-- chunk {"id": "body-0050", "role": "body", "section": "Example: estimating the output error model for second-order under-damped system", "weight": 1.0} -->

From the synthetically generated data, the parameters of a model with the same structure are estimated. The experiment is repeated 100 times, each time corresponding to a different realization (i.e., different random seed) of the data generation. The result of the Monte Carlo procedure is displayed in Fig. 5 for the parameter estimation using ARX, standard (single shooting) output error, multiple shooting, and MSA-PEM. We show the difference between estimated and true values for the first parameter, $\hat{\theta_{1}} - \theta_{1}$. Similar results have been obtained for ${\hat{\theta}}_{2}$ and ${\hat{\theta}}_{3}$.

<!-- chunk {"id": "body-0051", "role": "body", "section": "Example: estimating the output error model for second-order under-damped system", "weight": 1.0} -->

Due to the presence of white output error, using output error estimation yields consistent and well-behaved results. ARX estimation, on the other hand, is biased, and its histogram is not centered around zero. This is more evident either in 5(b) or in 5(c). In Fig. 5(a), which correspond to the fast response system, there is not much difference between the two estimation procedures, mostly because any disturbance fade away very quickly, yielding similar statistical properties for the two estimators.

<!-- chunk {"id": "body-0052", "role": "body", "section": "Example: estimating the output error model for second-order under-damped system", "weight": 1.0} -->

Multiple shooting estimation results are similar to the (single shooting) output error estimation. For some choices of $\Deltam_{\max}$, the optimization problem might actually be made harder due to the increase in the problem dimension. In this case, the algorithm seems to fail a few times, which can be observed in the histogram as a few outliers in the estimated parameter distribution. Except for these outliers, all the different choices of $\Deltam_{\max}$ yield very similar distributions for the estimated parameters.

<!-- chunk {"id": "body-0053", "role": "body", "section": "Example: estimating the output error model for second-order under-damped system", "weight": 1.0} -->

For MSA-PEM, the estimation results vary qualitatively among the three settings. For the intermediate setting, midway qualitative behavior between ARX and output error estimation is obtained, approaching that of output error estimation as $K$ increases. For the fast-response system, a similar interpretation is possible, however, there is not much difference between using ARX and output error estimation to begin with (cf. Fig 5 (a)), hence all $K$-step-ahead choices yield similar results. Finally, for the slow-response setting, minimizing the multi-step-ahead prediction error does not offer a direct compromise between ARX and output error estimation and, for $K = 10$ or $K = 20$, it is possible to observe a bimodal distribution with one peak distant from zero. And $K = 7$ yields the best results.

<!-- chunk {"id": "body-0054", "role": "body", "section": "Example: estimating the output error model for second-order under-damped system", "weight": 1.0} -->

In Fig. 6, the computational cost of multiple shooting and MSA-PEM are compared. The average running time divided by the number of function evaluations is displayed in Fig. 6(a) and (b). This accounts for the computational cost of computing the cost function, derivatives, and performing the matrix factorizations needed by the optimization algorithm at each iteration. Figure 6(c) and (d) display the number of cost function evaluations needed for the optimization algorithm to converge. The next section studies time and memory complexity of the methods and explains the obtained results in a more general context.

<!-- chunk {"id": "body-0055", "role": "body", "section": "Computational cost", "weight": 1.0} -->

As observed in Fig. 6(b), MSA-PEM has an average running time per iteration that grows linearly with the number of stages. Since the problem dimension and the factorization cost per iteration remain constant, it is the time complexity of computing the cost function $V$ (and its derivatives) that accounts for the linear growth. In Appendix E, we discuss in detail the computation of $V$ and arrive at the time complexity of $\mathcal{O}{({NK{({n_{y} + n_{u}})}})}$.

<!-- chunk {"id": "body-0056", "role": "body", "section": "Computational cost", "weight": 1.0} -->

Multiple shooting estimation, on the other hand, has an average running time per iteration that decreases with the maximum simulation length $\Deltam_{\max}$. This is displayed in Fig. 6(a). In this case, the cost of computing $V$ is $\mathcal{O}{({N{({n_{y} + n_{u}})}})}$ and does not depend on the simulation length. The increase in the problem dimension, however, yields more costly factorizations (cf. Appendix A), which results in the increased computational cost per iteration.

<!-- chunk {"id": "body-0057", "role": "body", "section": "Computational cost", "weight": 1.0} -->

For multiple shooting, shorter simulation lengths $\Deltam_{\max}$ allow the solver to converge with fewer function evaluations. This is in agreement with the theory presented in this paper, which suggests longer simulation lengths might result in poor smoothness properties and make the optimization problem harder to solve. Applying the same reasoning to MSA-PEM, it is natural to expect that smaller values of $K$ would yield convergence with fewer iterations. This, however, does not seem to be the case for the slow time-response setting, maybe because MSA-PEM often converges to the wrong parameters in this setting (as shown in Fig. 5(i)).

<!-- chunk {"id": "body-0058", "role": "body", "section": "Computational cost", "weight": 1.0} -->

In general, the number of function evaluations for MSA-PEM is lower than for multiple shooting because the resulting problem is unconstrained, rather than constrained, for which more efficient procedures are available.

<!-- chunk {"id": "body-0059", "role": "body", "section": "Computational cost", "weight": 1.0} -->

Finally, MSA-PEM and multiple shooting are both amenable to parallelization, even though this is not explored in the examples. During MSA-PEM implementation, it is possible to instantiate $N$ different processes (or threads) for computing each prediction $\hat{y}{\lbrack k\rbrack}$ (and the corresponding derivatives) in parallel. Multiple shooting, on the other hand, subdivides the problem into $({{N/\Delta}m_{\max}})$ independent subproblems.

<!-- chunk {"id": "body-0060", "role": "body", "section": "of constraints", "weight": 1.0} -->

${\frac{N}{\Deltam_{\max}} \cdot N_{x}} - 1$ Asymp. statistical properties Approach expected properties as K → N

<!-- chunk {"id": "body-0061", "role": "body", "section": "of independent subproblems", "weight": 1.0} -->

$\frac{N}{\Deltam_{\max}}$ Table 2: Tradeoffs: multiple shooting vs MSA-PEM. Nθ is the number of parameters. Nx is the number of states that need to be propagated through the simulation (Nx = ny = 2). Δ mmax is the maximum simulation length used for multiple shooting and K is the number of steps ahead predicted in the MSA-PEM.

<!-- chunk {"id": "body-0062", "role": "body", "section": "of independent subproblems", "weight": 1.0} -->

Both MSA-PEM and multiple shooting allow the user to control the maximum simulation length, hence the smoothness of the cost function (cf. Section 3), by setting $K$ for the MSA-PEM and $\Deltam_{\max}$ for the multiple shooting. These parameters, however, affect diverse aspects of the estimation problem, which are summarized in Table 2. Multiple shooting has an exact equivalence with the original single shooting problem regardless of the simulation length and the parameter $\Deltam_{\max}$ offers a tradeoff between the problem dimension and smoothness properties of the cost function. MSA-PEM keeps the problem dimension fixed, and, as $K$ increases, it is possible to approach the behavior of methods with distinct statistical properties (not always in a smooth way, as shown in Fig. 5(i)), at the expense of an increased computational cost and worse smoothness properties.

<!-- chunk {"id": "body-0063", "role": "body", "section": "of independent subproblems", "weight": 1.0} -->

Some refinements are proposed in the literature. For instance, propose to average over different values of $K$, to obtain a slower but smoother convergence to output error estimation as $K\rightarrow N$. In, on the other hand, the method starts from the one-step-ahead prediction solution and increases $K$ by one in each iteration until convergence. We give an numerical example using such approach in Appendix F.

<!-- chunk {"id": "body-0064", "role": "body", "section": "Conclusion", "weight": 1.5} -->

The relevance of this paper lies in the rather general setting for which the proposed methods and results hold. The main technical contribution is to show that for dynamic prediction models that are non-contractive (i.e. do not converge asymptotically to a single stable point) in the region of interest, the upper bound for the Lipschitz constant and the $\beta$-smoothness blows up exponentially with the simulation length, and this can make the optimization problem very hard to solve. This was illustrated using numerical examples with systems that are non-contractive due to the presence of chaotic regions and unstable equilibrium points. Because of these regimes, the objective function becomes very intricate in some regions of the parameter space and the optimization algorithm fails to find a good solution. Even for problems that are contractive in the region of interest, multiple shooting might help in preventing the solver from getting stuck in undesirable regions of the parameter space, hence facilitating the convergence to a good solution (cf. Section 5.2).

<!-- chunk {"id": "body-0065", "role": "body", "section": "Conclusion", "weight": 1.5} -->

Multiple shooting makes the simulation length a design parameter and hence allows solving optimization problems that would be infeasible in a single shooting setting. The price paid compared to single shooting methods is that a nonlinear constrained optimization problem must be solved instead of an unconstrained one. It also makes it harder to generalize to situations other than batch training, such as online training. MSA-PEM is another approach that allows some control over the smoothness of the cost function, but with different tradeoffs (see Table 2) between smoothness, asymptotical properties and computational cost to be taken into consideration.
