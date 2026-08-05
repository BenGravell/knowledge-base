<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Nonlinear Covariance Control via Differential Dynamic Programming

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

We consider covariance control problems for nonlinear stochastic systems. Our objective is to find an optimal control strategy to steer the state from an initial distribution to a terminal one with specified mean and covariance. This problem is considerably more complicated than previous studies on covariance control for linear systems. We leverage a widely used technique - differential dynamic programming - in nonlinear optimal control to achieve our goal. In particular, we adopt the stochastic differential dynamic programming framework to handle the stochastic dynamics. Additionally, to enforce the terminal statistical constraints, we construct a Lagrangian and apply a primal-dual type algorithm. Several examples are presented to demonstrate the effectiveness of our framework.

<!-- chunk {"id": "body-0003", "role": "body", "section": "Introduction", "weight": 1.5} -->

The theory of covariance control/assignment was first studied by Hotz and Skelton in the 80's and further developed. The original goal was to find an optimal control strategy for a linear time-invariant system to achieve some specified stationary state covariance. Recently, the covariance control theory was extended to a finite horizon control setting where the goal was to steer the state covariance of a continuous-time linear dynamic system from an initial value to a terminal one. This finite-horizon perspective was further extended to cases with discrete-time dynamics, nonlinear dynamics, multiple systems etc. The basic idea of covariance control is to relax the hard constraints in classical optimal control with soft probabilistic constraints; the former is usually unrealistically strong due to the stochastic disturbance. This relaxation makes it suitable for a range of applications in the presence of large uncertainties. Indeed, the covariance control theory has been applied to in aerospace, robotics and sensing etc.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

Most previous works on covariance control focused on linear systems. The goal of this paper is to generalize this framework to nonlinear stochastic dynamics. This will greatly expand the application domain as most real-world systems in robotics, autonomy, etc cannot be described within the linear dynamics regime. It turns out that the methods developed for linear system covariance control are not applicable to nonlinear problems. For one thing, the mean and the covariance in the linear system have independent dynamics and can be controlled separately and independently; this is no longer the case in nonlinear problems.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

In this work, we develop an efficient algorithm for nonlinear covariance control based on differential dynamic programming (DDP), or more precisely, stochastic differential dynamic programming (SDDP). To ensure the terminal constraint on the state mean and covariance, we adopt a Lagrangian multiplier method. A primal-dual method is used to update the primal and dual variables iteratively. More specifically, for the given Lagrangian multiplier, SDDP is executed first to obtain the nominal trajectory and control. The multiplier is then updated following gradient direction, which is computed through propagating the dynamics forward under optimal control.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

The nonlinear covariance control problem was recently studied in under different assumptions with a different method. In particular, the cost function used in is quadratic. In addition, assumes additive noise whose intensity is independent of state and control. In contrast, we consider more general cost functions and dynamics. A case of particular interest to us is multiplicative noise which is ubiquitous in robotics. On another topic, even though differential dynamic programming has been developed for a long time, the literature with terminal constraints is relatively scarce and all of them are for deterministic dynamics. How to generalize the methods to stochastic dynamics was not clear. It turns out that for problems with terminal constraints, there is a significant difference between stochastic settings and deterministic settings, as can be seen later in Section III.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

The paper is organized as follows. In Section II we provide the background on covariance control, differential dynamic programming, and Lagrangian multiplier method. The main result and the algorithm are presented in Section III. We present two examples in Section IV to illustrate the framework. This follows by a short concluding remark in Section V.

<!-- chunk {"id": "body-0008", "role": "body", "section": "II-A Covariance Control", "weight": 1.0} -->

The motivation stems from classical linear quadratic control problems, in which, the objective is to steer the state of the system to the desired one in a way that strikes a balance between keeping the deviations of the system's state tolerable on average while also using affordable control effort.

<!-- chunk {"id": "body-0009", "role": "body", "section": "II-A Covariance Control", "weight": 1.0} -->

Covariance control provides enormous benefits in the integration of modeling, and control problems. In a general control task, except for controller, identification and state estimation also use covariances as a measure of performance as well. Therefore, a theory which steer covariance allows fusing the entire class of problems (modeling and control) of concern in systems via the same measure of performance.

<!-- chunk {"id": "body-0010", "role": "body", "section": "II-A Covariance Control", "weight": 1.0} -->

As for the linear system, the mean and the covariance have independent dynamics. Open-loop control is used to control the mean and the covariance is controlled by close-loop state feedback gain. However, in nonlinear system or constrained cases, the mean and covariance are usually coupled.

<!-- chunk {"id": "body-0011", "role": "body", "section": "II-B Differential Dynamic Programming", "weight": 1.0} -->

Differential dynamic programming (DDP) is an iterative algorithm for nonlinear optimal control problem, which has high execution speed so that is widely adopted. Consider a system with discrete-time dynamics and cost function where $N$ is the final time step, $x \in {\mathbb{R}}^{n}$ is the state of the system, $u \in {\mathbb{R}}^{m}$ is the control input, $\ell$ is the running cost, and $\ell_{f}$ is the final cost. Then, we define the value function at time i is the optimal cost-to-go starting at ${x{(i)}} = x$ where $V{({f{(x,u,i)}},{i + 1})}$ is value function at time $i + 1$.

<!-- chunk {"id": "body-0012", "role": "body", "section": "II-B Differential Dynamic Programming", "weight": 1.0} -->

The algorithm begins with a nominal trajectory, which is sequence of states $({\overline{x}}_{0},{\overline{x}}_{1},\cdots,{\overline{x}}_{N})$ and corresponding controls $({\overline{u}}_{0},{\overline{u}}_{1},\cdots,{\overline{u}}_{N - 1})$, and then executes a backward pass and a forward pass at each iteration. In the backward pass, the algorithm expands value function to second-order around the nominal trajectory^11^1A modification of DDP with only first-order approximation of the dynamics was developed in under the name iLQR/iLQG.. In the forward pass, the nominal trajectory will be updated using the optimal control law from the backward pass. The process will be repeated until convergence.

<!-- chunk {"id": "body-0013", "role": "body", "section": "II-B1 Backward pass", "weight": 1.0} -->

{\frac{1}{2}\deltax^{T}Q_{xu}{(i)}\deltau}},$ | | | When $\kappa = 1$, 2nd order expansion of the dynamics is used; When $\kappa = 0$, 1st order expansion of dynamics is used. The parameter $\kappa$ is introduced to unify the results derived from the first and second-order expansion of the dynamics.

<!-- chunk {"id": "body-0014", "role": "body", "section": "II-B1 Backward pass", "weight": 1.0} -->

The optimal control law $\deltau^{\ast}$ of minimizing the quadratic approximation with respect to $\deltau$ is | | $\deltau^{\ast}$ | $= {\underset{\deltau}{argmin}Q{({\deltax},{\deltau})}}$ | | \(6\) | Substitute $\deltau^{\ast}$ into the expansion of $Q$, we get a quadratic model of $V$ The backward pass begins by initializing the value function with the terminal cost also value function ${V{(N)}} = {\ell_{f}{(x_{N})}}$ and its derivatives, then calculate the value at each time.

<!-- chunk {"id": "body-0015", "role": "body", "section": "II-B2 Forward pass", "weight": 1.0} -->

After backward pass, we update the nominal trajectory using the optimal feedback control law got from the previous backward pass with the given initial condition Finally, the backward pass and forward pass will be repeated until convergence when $k$ tends to be zero vector.

<!-- chunk {"id": "body-0016", "role": "body", "section": "II-C Lagrange multiplier", "weight": 1.0} -->

The method of Lagrange multipliers is a strategy for finding the maxima or minima of a function with constraints The basic idea is to convert a constrained problem into a form such that the derivative test of an unconstrained problem can still be applied.

<!-- chunk {"id": "body-0017", "role": "body", "section": "II-C Lagrange multiplier", "weight": 1.0} -->

The Lagrangian dual problem is obtained by forming the Lagrangian of a minimization problem by using Lagrange multipliers to add the constraints to the objective function and then solving for the primal variable values that minimize the original objective function where $f_{0}$ is an original problem, $g$ is the unconstrained problem, $\lambda$ represents the Lagrange multiplier. This solution gives the primal variables as functions of the Lagrange multipliers, which are called dual variables so that the new problem is to maximize the objective function with respect to the dual variables under the derived constraints on the dual variables.

<!-- chunk {"id": "body-0018", "role": "body", "section": "II-C Lagrange multiplier", "weight": 1.0} -->

In the past decades, several general methods for designing approximation algorithms for tricky optimization problems have arisen, including the primal-dual method. The primal dual-algorithm, which is a standard tool in the design of algorithms for combinatorial optimization problems, while not a good general purpose LP solution technique, is valuable because it is easy to customize for a particular problem. Any feasible solution to the dual system can be used to initiate the algorithm. Associated with the dual solution is a "restricted" primal problem that requires optimization. When the solution of the restricted primal problem has been accomplished, and improved solution to the dual system can be obtained. This, in turn, gives rise to a new restricted problem to be optimized. Optimizing iteratively and the optimum is obtained for both primal and dual systems. The method has been used to solve problems that can be modeled as linear programs. The constrained primal problem in our case is solved from a dual side also.

<!-- chunk {"id": "body-0019", "role": "body", "section": "Nonlinear covariance control", "weight": 1.0} -->

We consider a class of nonlinear stochastic optimal control problems with cost subject to the stochastic system described by the following stochastic differential equation where $x \in {\mathbb{R}}^{n}$ is the state, $u \in {\mathbb{R}}^{m}$ is the control, $\omega \in {\mathbb{R}}^{p}$ is standard Brownian motion noise. The dynamic functions are $f:{{{\mathbb{R}}^{n} \times {\mathbb{R}}^{m}}\rightarrow{\mathbb{R}}^{n}}$ and $F:{{{\mathbb{R}}^{n} \times {\mathbb{R}}^{m}}\rightarrow{\mathbb{R}}^{n \times p}}$.

<!-- chunk {"id": "body-0020", "role": "body", "section": "Nonlinear covariance control", "weight": 1.0} -->

The overall value function $V{(x,t)}$ is defined as the optimal expected cost accumulated over the time horizon starting from the initial state $x$ at $t$ under optimal control.

<!-- chunk {"id": "body-0021", "role": "body", "section": "Nonlinear covariance control", "weight": 1.0} -->

To solve the adjoint problem concerning $u,\lambda,\gamma$ we may take the Lagrange multiplier into consideration in DDP and solve their optimal together to get a second order convergence rate. Another way is to use the duality, first solve u for the minima $g{(\lambda,\gamma)}$ then update the multiplier to find the optimal value for the dual problem with gradient ascend. After that solve the optimal u again, back and forth. Due to the existence of the Brownian motion term in dynamics, the introduction of the second order term with respect to $\lambda,\gamma$ will recursively bring higher order terms of the value function. In particular, $Q_{\lambda\lambda}$ contains $V_{xx\lambda\lambda}$, because of the noise term in the expansion of $\deltax{({t + {\deltat}})}$. As a result, second order convergence rate is not achievable. Therefore we recommend the second option. Extra attention should be paid that the value function must be convex at the ending point, therefore $\gamma$ should be positive definite in each iteration.

<!-- chunk {"id": "body-0022", "role": "body", "section": "III-B Multiplier Update", "weight": 1.0} -->

We continue with the control value we get from with fixed $\lambda$ and $\gamma$ and extract the control policy for each time step. Notice that what we get is not only a open loop control value $u_{0}$ but also a closed loop policy ${\deltau} = {k + {K\deltax}}$. When we execute the SDDP method to convergence we will get $Q_{u} = 0$ at each time step. Therefore ${\deltau} = {Q_{uu}^{- 1}Q_{ux}\deltax}$. When the algorithm converges, ${\deltax} = 0$ but the control policy is still valuable and provides the closed loop part which represented as $K = {Q_{uu}^{- 1}Q_{ux}}$ here. The overall control policy can be expressed as where $\overline{x}$ is the trajectory which we propagate according to dynamics without noise as in SDDP. $\overline{u}$ is what we solved for in SDDP.

<!-- chunk {"id": "body-0023", "role": "body", "section": "III-B Multiplier Update", "weight": 1.0} -->

When convergence is reached for fixed $\lambda$ and $\gamma$, we compute ${\mathbb{E}}{\lbrack{x{(T)}}\rbrack}$ and ${\mathbb{E}}{\lbrack{x{(T)}x{(T)}^{T}}\rbrack}$, and then update the multipliers with gradient ascend method | | $V_{\gamma}{(T)}$ | ${= {{{\mathbb{E}}{\lbrack{x{(T)}x{(T)}^{T}}\rbrack}} - {\mu_{T}\mu_{T}^{T}} - \Sigma_{T}}}.$ | | | There are two ways to compute the above terms. In the first one, we sample the noise, propagate the stochastic dynamics and calculate the expectation in a statistic way.

<!-- chunk {"id": "body-0024", "role": "body", "section": "III-B Multiplier Update", "weight": 1.0} -->

The feedback law is employed with each step, where $x$ in the control law is the actual state we propagate with real noise. The second method is to propagate the mean and covariance half analytically. The first way has better feasibility but will oscillate slightly even at the fixing point. Consider the samples as i.i.d. and the covariance of ${\mathbb{E}}{\lbrack x\rbrack}$ and ${\mathbb{E}}{\lbrack{xx^{T}}\rbrack}$ are of $1/\sqrt{n}$ order of magnitude. The required number of samples is proportional to the square of resolution. For higher resolution, increasing the number of samples is necessary, which will also decrease the randomness in gradient descent, therefore decrease the number of steps to convergence. However, there is always a trade-off between computation speed and precision, which we recommend a combination of several hundred samples and a ten percent resolution.

<!-- chunk {"id": "body-0025", "role": "body", "section": "III-B Multiplier Update", "weight": 1.0} -->

As for the second method, the problem is that for some highly nonlinear cases it may be hard to propagate analytically and the approximation of each state to be Gaussian may have an unneglectable offset for some certain cases especially after many steps. The proposed algorithm is summarized in Algorithm 1.

<!-- chunk {"id": "body-0026", "role": "body", "section": "III-B Multiplier Update", "weight": 1.0} -->

1 Given: Initial state mean μ0 and covariance Σ0, total time step N, control sequence $\overline{u}$, initial Lagrange multiplier λ0 and γ0, and target mean μT and covariance ΣT. Set κ = 1 for the case of 2nd order dynamics expansion and κ = 0 for 1st order expansion of dynamics.

<!-- chunk {"id": "body-0027", "role": "body", "section": "III-B Multiplier Update", "weight": 1.0} -->

2 Goal: Optimal control sequence u*, corresponding state trajectory x* and local state feedback control strategy Ki, i = 1, ⋯, N − 1 4 Get initial trajectory $\overline{x}$ by integrating the dynamics forward with ${\overline{x}}_{0}$ and $\overline{u}$; 5 while not convergence, do 6 Differentiate value function at final time, get Vx (N), Vx x (N); 8 Compute the value of Qx, Qu, Qx x, Qx u, Qu x, Qu u at time i according to; 9 Compute the value of Vx, Vx x at time i according to; 12 Update control sequence $\overline{u} = {\overline{u} + {\deltau^{\ast}}}$ with control policy δ u* = k + K δ x at time i; 13 Update state trajectory $\overline{x}$ at time i without noise; 15 if SDDP not convergence, then 18 Sample trajectories from initial state mean μ0 and covariance Σ0 using forward dynamics with noise; 19 Get statistic final state’s

<!-- chunk {"id": "body-0028", "role": "body", "section": "III-B Multiplier Update", "weight": 1.0} -->

mean μ (N) and covariance Σ (N); 20 Compute the gradients of Lagrange multiplier λ and γ according to and update Lagrange multiplier λ = λ + η1 Vλ (T) and γ = γ + η2 Vγ (T), where η1 ∈ and η2 ∈ are search parameters; Algorithm 0 Covariance Control with SDDP

<!-- chunk {"id": "body-0029", "role": "body", "section": "Numerical Examples", "weight": 1.0} -->

In this section, we demonstrate the algorithm's performance with the specified terminal constraint on two different systems. We focus on the final state mean and covariance to meet the terminal constraint.

<!-- chunk {"id": "body-0030", "role": "body", "section": "IV-A One-Dimensional Dynamics", "weight": 1.0} -->

First, we consider one-dimensional stochastic nonlinear system of the form Our goal is to manipulate the system with a state dependent noise to reach a final state $x{(T)}$ with zero mean and covariance $0.03$. The initial state has mean $0$ and covariance $0.25$. The running cost is $\ell = {{\mathbb{E}}\left\lbrack {\int_{0}^{T}{ru^{2}{d\tau}}} \right\rbrack}$.

<!-- chunk {"id": "body-0031", "role": "body", "section": "IV-A One-Dimensional Dynamics", "weight": 1.0} -->

We sample the noise and get several trajectories to calculate gradients ${V_{\lambda}{(T)}} = {{{\mathbb{E}}{\lbrack{x{(T)}}\rbrack}} - \mu_{T}}$, and ${V_{\gamma}{(T)}} = {{\mathbb{E}}{\lbrack{{x{(T)}^{2}} - \mu_{T}^{2} - \Sigma_{T}}\rbrack}}$ statistically, while the number of sample is related to the distance to the optimal point. It's worth noting that $\gamma$ should be positive during the updating process to guarantee the convexity of the terminal cost.

<!-- chunk {"id": "body-0032", "role": "body", "section": "IV-A One-Dimensional Dynamics", "weight": 1.0} -->

In the beginning, only a rough direction is needed for those $\lambda$ and $\gamma$ who are distant from the optimal point, i.e. $V_{\lambda}$ and $V_{\gamma}$ are rather large, thus the number of samples can be small, in our case we choose 80. While for those $\lambda$ and $\gamma$ which are rather close to the optimum, i.e. $V_{\lambda}$ and $V_{\gamma}$ are rather small, the gradient ascent direction and length should be relatively precise. So that the next step will get towards the optimum instead of drifting around because of the uncertainty in the calculation of mean and covariance.

<!-- chunk {"id": "body-0033", "role": "body", "section": "IV-A One-Dimensional Dynamics", "weight": 1.0} -->

From the experiment, the resolution of the final state is about 0.01 for both mean and covariance with 800 samples around the neighborhood. Also the covariance becomes much smaller under the feedback control while starting with $\Sigma_{0} = 0.25$ and ending with $\Sigma_{T} = 0.01$. As a comparison, for the uncontrolled case, the mean and covariance nearly remain the same. Fig. 1 display the nominal state trajectory under feedback control with some sampled trajectories. Fig. 2 illustrates the nominal trajectory's shift with covariance which corresponds to our controlled system well.

<!-- chunk {"id": "body-0034", "role": "body", "section": "IV-B Simple Inverted Pendulum", "weight": 1.0} -->

The second model we study is an inverted pendulum, with constraints on both final state mean and covariance. The stochastic nonlinear dynamics is where the state variables are ${x_{1} = \theta},{x_{2} = \overset{˙}{\theta}}$, the measurement parameter of noise $\alpha = 0.04$, the time step is $10$ msec and time horizon is $T = 4$ sec. The goal is to let the suspended pendulum swing up from initial condition (corresponding to a -180 deg angle) to an inverted position (corresponding to a 0 deg angle) and stay static at the final time $T$. The first step is to find the optimal trajectory and the corresponding feedback control strategy with the following cost function when the Lagrange multipliers are fixed As in the previous example, we sample the noise and get some trajectories to calculate gradients. Now it's necessary to guarantee that the multiplier matrix $\gamma$ should be positive define. In this case, we choose 800 for the number of samples.

<!-- chunk {"id": "body-0035", "role": "body", "section": "IV-B Simple Inverted Pendulum", "weight": 1.0} -->

Fig. 3 demonstrates the variety of the mean and covariance with several sampled trajectories. Fig. 4 displays the control sequences of the sampled trajectories in Fig. 3. Fig. 5 illustrates all nominal trajectory, sampled trajectories, mean and covariance variety in a phase graph.

<!-- chunk {"id": "body-0036", "role": "body", "section": "Conclusion", "weight": 1.5} -->

In this paper, we developed an algorithm for covariance control of nonlinear stochastic systems. Our method is based on stochastic differential dynamic programming. In order to achieve targeted state mean and covariance, SDDP is combined with the Lagrangian multiplier method to handle the terminal constraints. We remark that DDP with terminal constraints for deterministic systems doesn't apply in a stochastic setting. We tested our algorithm on severally examples and observed satisfying performance. The next step is to apply this algorithm for high-dimensional robotics path/trajectory planning problems. There are also several potential directions to improve the performance of our algorithm including working on belief space.
