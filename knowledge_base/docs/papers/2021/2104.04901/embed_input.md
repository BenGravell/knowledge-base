<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Global Convergence of Policy Gradient Primal-dual Methods for Risk-constrained LQRs

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

While the techniques in optimal control theory are often model-based, the policy optimization (PO) approach directly optimizes the performance metric of interest. Even though it has been an essential approach for reinforcement learning problems, there is little theoretical understanding on its performance. In this paper, we focus on the risk-constrained linear quadratic regulator (RC-LQR) problem via the PO approach, which requires addressing a challenging non-convex constrained optimization problem. To solve it, we first build on our earlier result that an optimal policy has a time-invariant affine structure to show that the associated Lagrangian function is coercive, locally gradient dominated and has local Lipschitz continuous gradient, based on which we establish strong duality. Then, we design policy gradient primal-dual methods with global convergence guarantees in both model-based and sample-based settings. Finally, we use samples of system trajectories in simulations to validate our methods.

<!-- chunk {"id": "body-0003", "role": "body", "section": "Introduction", "weight": 1.5} -->

The techniques in conventional optimal control theory often require an explicit dynamical model. Such a model-based idea is relatively easy to provide theoretical guarantees but is usually sensitive to modeling inaccuracy. Policy optimization (PO) methods, as an end-to-end approach, directly search for an optimal control policy to minimize a performance metric of interest and has advantages in scenarios where the dynamical model is complex and difficult to identify. In fact, it has been proved to be an essential approach for applications of reinforcement learning (RL), e.g., robotic in-hand manipulation.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

However, there are only a few theoretical guarantees on PO methods as they often involve challenging non-convex optimization problems. To study their convergence and sample complexities, there has recently been a resurgent interest in PO methods for classical control problems. For example, the seminal work studies the well-known linear quadratic regulator (LQR) problem via PO methods. Though an optimal policy can be simply parameterized by a gain matrix, the quadratic cost is non-convex in the gain matrix space. A major contribution of shows that the cost function is globally gradient dominated (aka Polyak-Lojasiewicz condition ) with respect to (w.r.t.) the policy gain, which is indispensable to prove the global convergence of their PO methods.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

Since the LQR problem only focuses on the quadratic regulation performance, the closed-loop system may be largely jeopardized by low-probability yet significant events, which is not allowed for safety-critical applications. To remedy it, risk-aware controllers have become natural choices. In, a finite-horizon LQR problem with a variance-like constraint was first proposed, which is then extended to the infinite-horizon version in our previous work. While both are solved via the model-based dynamic programming (DP), this paper studies the risk-constrained LQR (RC-LQR) problem of under the PO framework in both model-based and sample-based settings. In fact, various constrained LQ problems have also been studied via PO methods, e.g., the LEQG and distributed LQG.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

In sharp contrast to those PO works, the non-convex variance-like constraint results in a fundamentally different optimization landscape. In particular, we lack the global gradient dominance property. Thus, a natural question is whether there still exists a good PO method that yields a globally optimal policy for the infinite-horizon RC-LQR problem. We provide a positive answer in this paper. As the finite-horizon version, an optimal policy has also been shown in to have an affine structure in the form of ${u^{\ast}{(x)}} = {{- {K^{\ast}x}} + l^{\ast}}$ with a gain matrix $K^{\ast}$ and a vector $l^{\ast}$. We take this as a starting point, and propose here a novel primal-dual method where the primal and dual iterations alternatively compute an optimal policy-multiplier pair.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

Even though the primal-dual method is conceptually simple, it is challenging to establish theoretical guarantees since (a) the optimization landscape of the Lagrangian function is yet unclear (in fact, we only obtain that the Lagrangian under a fixed multiplier is locally gradient dominated, meaning that there may exist multiple optimal policies for the Lagrangian); (b) the strong duality does not trivially hold in a non-convex constrained optimization problem (note that the strong duality is the key to primal-dual methods and is usually established for convex problems ); and (c) exact gradients of both the Lagrangian and the dual function are unavailable. Our main contribution here lies in satisfactorily addressing the above issues, and further showing that the Lagrangian is also coercive with locally Lipschitz gradient, which along with local gradient dominance establishes the global convergence of our primal-dual method.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Introduction", "weight": 1.5} -->

Clearly, the RC-LQR can be regarded as a special case of the long-studied constrained Markov decision problems (CMDPs). Strong duality for CMDPs has been proved, but only if the state-action space is finite or the cost is uniformly bounded, neither of which holds in the RC-LQR of this paper. To the best of our knowledge, we are the first to formally prove the strong duality for such a class of continuous CMDPs with quadratic costs.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Introduction", "weight": 1.5} -->

Even though a similar policy gradient primal-dual framework has been adopted to solve continuous CMDPs, none of them can achieve global convergence. For example, the primal-dual methods in have only been shown to converge to a neighborhood of the global optimum and can even lead to constraint violations. Even though it has been resolved, their optimization landscape lends them resort to function approximations for optimal policies and thus can only achieve local convergence. In comparison, an optimal policy of our RC-LQR problem has an exact affine structure in the state feedback. While for finite CMDPs, the primal-dual methods are relatively easy and can ensure the convergence to a globally optimal policy. It is worth mentioning that there are also other PO-based works that do not follow a primal-dual framework, e.g., they leverage the interior-point method and trust region method to directly solve the constrained problem. Again, they still lack provable global convergence.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Introduction", "weight": 1.5} -->

The remainder of this paper is organized as follows. In Section II, we formulate the infinite-horizon RC-LQR problem. In Section III, we approach it by proposing policy gradient primal-dual methods and recognizing the local gradient dominance property, based on which we prove the strong duality. In Section IV and Section V, we propose primal-dual methods with convergence guarantees in model-based and sample-based settings, respectively. In Section VI, we conduct simulations to validate our theoretical results. Concluding remarks of Section VII and five appendices complete the paper.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Problem Formulation", "weight": 1.0} -->

Consider a discrete-time linear time-invariant stochastic system where $x_{t} \in {\mathbb{R}}^{n}$ and $u_{t} \in {\mathbb{R}}^{m}$ are the state and control vectors, and $\{ w_{t}\}$ is an independently and identically distributed noise sequence.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Assumption 1", "weight": 1.0} -->

$Q$ is positive semi-definite and $R$ is positive definite. The pair $(A,B)$ is controllable and $(A,Q^{1/2})$ is observable.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Assumption 1", "weight": 1.0} -->

The PO method for the risk-neutral LQR in is shown to be globally convergent by random search and policy gradient methods. However, the non-convex constraint in renders our problem much more involved and we resort to the duality theory to establish global convergence.

<!-- chunk {"id": "body-0014", "role": "body", "section": "Primal-dual Methods for the Risk-constrained LQR", "weight": 1.0} -->

In this section, we solve the RC-LQR problem via the primal-dual method. We first show that its Lagrangian function is coercive and locally gradient dominated. Then, we establish strong duality.

<!-- chunk {"id": "body-0015", "role": "body", "section": "III-A Overview of Our Policy Gradient Primal-dual Method", "weight": 1.0} -->

Let $X = {\lbrack K,l\rbrack}$ be the decision vector of and define the set of stabilizing policy by Let $\mu \geq 0$ denote a Lagrange multiplier of, $Q_{\mu} = {Q + {4\muQWQ}}$ and $S = {2\muQM_{3}}$. Then, the Lagrangian is given as | | | ${= {\lim\limits_{T\rightarrow\infty}{\frac{1}{T}{\mathbb{E}}\left\lbrack {\sum\limits_{t = 0}^{T - 1}{c_{\mu}{(x_{t},u_{t})}}} \right\rbrack}}},$ | | | is a reshaped cost with a non-negative weight $\mu$ to balance the quadratic cost and the risk. Define the dual function as In the sequel, we refer to as the primal problem and as its dual problem.

<!-- chunk {"id": "body-0016", "role": "body", "section": "III-A Overview of Our Policy Gradient Primal-dual Method", "weight": 1.0} -->

To achieve its global convergence, the strong duality property between the primal problem and the dual problem is essential. Since is non-convex, it does not trivially hold. Even though the Lagrangian in is the LQR cost with a linear term, its non-convex optimization landscape is yet unclear. Thus, computing the primal update in (11a) is itself challenging. In the rest of this section, we show that: (a) $\mathcal{L}{(X,\mu)}$ is coercive over $\mathcal{S}$ and locally gradient dominated in Section III-B, which is key to establish that a critical point of (11a) is globally optimal; (b) $\mathcal{L}{(X,\mu)}$ and its gradient are locally Lipschitz in Section III-C, which implies a linear convergence rate of gradient methods for solving (11a); (c) The strong duality property indeed holds in Section III-D. Combining these results prove the global convergence of. Note that all the proofs on the properties of the Lagrangian are provided in Appendix A and B.

<!-- chunk {"id": "body-0017", "role": "body", "section": "III-B Coercivity and Local Gradient Dominance of the Lagrangian", "weight": 1.0} -->

We first derive closed-form expressions for the Lagrangian and its gradient. For any $X \in \mathcal{S}$, the state of the system has a stationary distribution, the mean ${\overline{x}}_{X}$ and covariance $\Sigma_{K}$ of which satisfy Then, we define the value function under $X$ associated with the reshaped cost $c_{\mu}{(x_{t},u_{t})}$ as where ${\mathbb{E}}{\lbrack \cdot \rbrack}$ takes expectation under a fixed policy $X \in \mathcal{S}$. Moreover, let $P_{K} \geq 0$ satisfy the following Lyapunov equation We show that $V_{X}{(x)}$ is quadratic and provide a closed-form of $\mathcal{L}{(X,\mu)}$.

<!-- chunk {"id": "body-0018", "role": "body", "section": "III-C Locally Lipschitz Gradient of the Lagrangian", "weight": 1.0} -->

For a fixed $\mu$, we show in this subsection that both $\mathcal{L}{(X,\mu)}$ and its gradient are locally Lipschitz continuous.

<!-- chunk {"id": "body-0019", "role": "body", "section": "III-D Strong Duality", "weight": 1.0} -->

In this subsection, we show that the strong duality between the primal problem and dual problem holds.

<!-- chunk {"id": "body-0020", "role": "body", "section": "Policy Gradient Primal-dual Algorithm for the Model-based Setting", "weight": 1.0} -->

In the model-based setting, we assume that all the parameters in is known and propose three gradient-based methods with linear convergence to solve (11a). Then, we develop a primal-dual method in the form of with global convergence to solve.

<!-- chunk {"id": "body-0021", "role": "body", "section": "IV-A Policy Gradient Methods for Solving (11a)", "weight": 1.0} -->

To solve (11a), we consider three widely-used policy gradient methods. Let $X'$ be the one-step updated policy and $\eta$ be the stepsize.

<!-- chunk {"id": "body-0022", "role": "body", "section": "IV-A Policy Gradient Methods for Solving (11a)", "weight": 1.0} -->

The NPG update is related to the gradient over a Riemannian manifold, while the GN update is one type of quasi-Newton update.

<!-- chunk {"id": "body-0023", "role": "body", "section": "IV-A Policy Gradient Methods for Solving (11a)", "weight": 1.0} -->

The key to the linear convergence of (23 ‣ IV Policy Gradient Primal-dual Algorithm for the Model-based Setting ‣ Global Convergence of Policy Gradient Primal-dual Methods for Risk-constrained LQRs Research of the first two authors was supported by National Natural Science Foundation of China under Grant no. 62033006. Research of the third author was supported by the ONR MURI Grant N00014-16-1-2710. F. Zhao and K. You are with the Department of Automation and BNRist, Tsinghua University, Beijing 100084, China. e-mail: zhaofr18@mails.tsinghua.edu.cn, youky@tsinghua.edu.cn. Tamer Başar is with the Coordinated Science Laboratory, University of Illinois at Urbana-Champaign, Urbana, IL 61801 USA.

<!-- chunk {"id": "body-0024", "role": "body", "section": "IV-A Policy Gradient Methods for Solving (11a)", "weight": 1.0} -->

e-mail: basar1@illinois.edu.")) is to find an appropriate stepsize such that (23 ‣ IV Policy Gradient Primal-dual Algorithm for the Model-based Setting ‣ Global Convergence of Policy Gradient Primal-dual Methods for Risk-constrained LQRs Research of the first two authors was supported by National Natural Science Foundation of China under Grant no. 62033006. Research of the third author was supported by the ONR MURI Grant N00014-16-1-2710. F. Zhao and K. You are with the Department of Automation and BNRist, Tsinghua University, Beijing 100084, China. e-mail: zhaofr18@mails.tsinghua.edu.cn, youky@tsinghua.edu.cn. Tamer Başar is with the Coordinated Science Laboratory, University of Illinois at Urbana-Champaign, Urbana, IL 61801 USA. e-mail: basar1@illinois.edu.")) yields a stabilizing $X'$ and decreases the Lagrangian per iteration, which is formally stated below. Note that the proof is given in Appendix C.

<!-- chunk {"id": "body-0025", "role": "body", "section": "IV-B A Model-based Primal-dual Algorithm", "weight": 1.0} -->

1:A randomly initialized multiplier μ1 ≥ 0, and a set of stepsizes {ζk}. 3: Solve Xk = argminX ∈ 𝒮 ℒ (X, μk) via. 4: Compute a subgradient dk by and Lemma 10. 5: Update the multiplier by μk + 1 = [μk + ζk ⋅ dk]+. Algorithm 1 The model-based primal-dual algorithm for the risk-constrained LQR By duality theory, a subgradient in (11b) is where $X^{k}$ is given in (11a) and $J_{c}{(X^{k})}$ is computed by the following lemma.

<!-- chunk {"id": "body-0026", "role": "body", "section": "Policy Gradient Primal-dual Algorithm for the Sample-based Setting", "weight": 1.0} -->

If $(A,B)$ in is unknown, both ${\nabla_{X}\mathcal{L}}{(X,\mu)}$ in and $d^{k}$ in cannot be computed directly. In the sample-based setting, we estimate them via system trajectories and develop a sampled-based primal-dual algorithm with global convergence.

<!-- chunk {"id": "body-0027", "role": "body", "section": "V-A Random Search for Solving (11a)", "weight": 1.0} -->

We adopt the random search of Algorithm 2 ‣ V Policy Gradient Primal-dual Algorithm for the Sample-based Setting ‣ Global Convergence of Policy Gradient Primal-dual Methods for Risk-constrained LQRs Research of the first two authors was supported by National Natural Science Foundation of China under Grant no. 62033006. Research of the third author was supported by the ONR MURI Grant N00014-16-1-2710. F. Zhao and K. You are with the Department of Automation and BNRist, Tsinghua University, Beijing 100084, China. e-mail: zhaofr18@mails.tsinghua.edu.cn, youky@tsinghua.edu.cn. Tamer Başar is with the Coordinated Science Laboratory, University of Illinois at Urbana-Champaign, Urbana, IL 61801 USA. e-mail: basar1@illinois.edu.") to estimate $\nabla_{X}\mathcal{L}$ via the oracle. The smoothing radius $r$ in Step 4 is used to control its estimation error.

<!-- chunk {"id": "body-0028", "role": "body", "section": "V-A Random Search for Solving (11a)", "weight": 1.0} -->

Motivated, we shall show that with a large probability, Algorithm 2 ‣ V Policy Gradient Primal-dual Algorithm for the Sample-based Setting ‣ Global Convergence of Policy Gradient Primal-dual Methods for Risk-constrained LQRs Research of the first two authors was supported by National Natural Science Foundation of China under Grant no. 62033006. Research of the third author was supported by the ONR MURI Grant N00014-16-1-2710. F. Zhao and K. You are with the Department of Automation and BNRist, Tsinghua University, Beijing 100084, China. e-mail: zhaofr18@mails.tsinghua.edu.cn, youky@tsinghua.edu.cn. Tamer Başar is with the Coordinated Science Laboratory, University of Illinois at Urbana-Champaign, Urbana, IL 61801 USA. e-mail: basar1@illinois.edu.") converges and $\{ X^{(i)}\}$ remains in the following compact sublevel set 1:An initial policy X ∈ 𝒮, the number of iterations N, a smoothing radius r, the stepsize η, a multiplier μ.

<!-- chunk {"id": "body-0029", "role": "body", "section": "Assumption 3", "weight": 1.0} -->

The noise sequence $\{ w_{t}\}$ is uniformly bounded, i.e., ${\| w_{t}\|} \leq v$, where $v$ is a positive constant.

<!-- chunk {"id": "body-0030", "role": "body", "section": "Assumption 3", "weight": 1.0} -->

Science Foundation of China under Grant no.

<!-- chunk {"id": "body-0031", "role": "body", "section": "Assumption 3", "weight": 1.0} -->

62033006. Research of the third author was supported by the ONR MURI Grant N00014-16-1-2710. F. Zhao and K. You are with the Department of Automation and BNRist, Tsinghua University, Beijing 100084, China. e-mail: zhaofr18@mails.tsinghua.edu.cn, youky@tsinghua.edu.cn. Tamer Başar is with the Coordinated Science Laboratory, University of Illinois at Urbana-Champaign, Urbana, IL 61801 USA. e-mail: basar1@illinois.edu.").

<!-- chunk {"id": "body-0032", "role": "body", "section": "V-B A Sample-based Primal-dual Algorithm", "weight": 1.0} -->

In this subsection, we let ${\hat{X}}^{k} = X^{(N)}$ and assume that (28 ‣ V Policy Gradient Primal-dual Algorithm for the Sample-based Setting ‣ Global Convergence of Policy Gradient Primal-dual Methods for Risk-constrained LQRs Research of the first two authors was supported by National Natural Science Foundation of China under Grant no. 62033006. Research of the third author was supported by the ONR MURI Grant N00014-16-1-2710. F. Zhao and K. You are with the Department of Automation and BNRist, Tsinghua University, Beijing 100084, China. e-mail: zhaofr18@mails.tsinghua.edu.cn, youky@tsinghua.edu.cn. Tamer Başar is with the Coordinated Science Laboratory, University of Illinois at Urbana-Champaign, Urbana, IL 61801 USA. e-mail: basar1@illinois.edu.")) holds for the sake of simplifying our presentation; see also e.g.,.

<!-- chunk {"id": "body-0033", "role": "body", "section": "V-B A Sample-based Primal-dual Algorithm", "weight": 1.0} -->

The oracle is adopted to compute a subgradient estimate with the estimation error resulting from the oracle computation and the gap between ${\hat{X}}^{k}$ and $X^{k}$.

<!-- chunk {"id": "body-0034", "role": "body", "section": "V-B A Sample-based Primal-dual Algorithm", "weight": 1.0} -->

Now, we present our sample-based primal-dual method in Algorithm 3 ‣ V Policy Gradient Primal-dual Algorithm for the Sample-based Setting ‣ Global Convergence of Policy Gradient Primal-dual Methods for Risk-constrained LQRs Research of the first two authors was supported by National Natural Science Foundation of China under Grant no. 62033006. Research of the third author was supported by the ONR MURI Grant N00014-16-1-2710. F. Zhao and K. You are with the Department of Automation and BNRist, Tsinghua University, Beijing 100084, China. e-mail: zhaofr18@mails.tsinghua.edu.cn, youky@tsinghua.edu.cn. Tamer Başar is with the Coordinated Science Laboratory, University of Illinois at Urbana-Champaign, Urbana, IL 61801 USA. e-mail: basar1@illinois.edu."). Due to the use of biased subgradient estimate, we can obtain the global convergence to a value close to $D^{\ast}$.

<!-- chunk {"id": "body-0035", "role": "body", "section": "Simulation", "weight": 1.0} -->

In this section, we use simulation to illustrate the effectiveness of our RC-LQR, and the convergence of the policy gradient primal-dual methods in both model-based and sample-based settings.

<!-- chunk {"id": "body-0036", "role": "body", "section": "VI-A The performance of RC-LQR", "weight": 1.0} -->

$\{ v_{t}\}$ is an independent sequence and satisfies that (a) $v_{t,1}$ follows a mixed Gaussian distribution of $\mathcal{N}{}$ and $\mathcal{N}{}$ with weights 0.2 and 0.8, respectively; (b) $v_{t,2}$ follows $\mathcal{N}{(0,0.01)}$. $\{ e_{t}\}$ is another Gaussian independent sequence and follows $\mathcal{N}{(0,{0.01 \times I_{4}})}$. The operator $\text{clip}{(\cdot)}$ is used to ensure a uniform bound of $w_{t}$ in Assumption 3 ‣ V Policy Gradient Primal-dual Algorithm for the Sample-based Setting ‣ Global Convergence of Policy Gradient Primal-dual Methods for Risk-constrained LQRs Research of the first two authors was supported by National Natural Science Foundation of China under Grant no.

<!-- chunk {"id": "body-0037", "role": "body", "section": "VI-A The performance of RC-LQR", "weight": 1.0} -->

62033006. Research of the third author was supported by the ONR MURI Grant N00014-16-1-2710. F. Zhao and K. You are with the Department of Automation and BNRist, Tsinghua University, Beijing 100084, China. e-mail: zhaofr18@mails.tsinghua.edu.cn, youky@tsinghua.edu.cn. Tamer Başar is with the Coordinated Science Laboratory, University of Illinois at Urbana-Champaign, Urbana, IL 61801 USA. e-mail: basar1@illinois.edu."), and projects each argurment onto the interval $\lbrack{- 10^{4}},10^{4}\rbrack$. Here the statistics of $\{ w_{t}\}$ are evaluated by the Monte Carlo method and the risk tolerance is set as $\overline{\rho} = 15$.

<!-- chunk {"id": "body-0038", "role": "body", "section": "VI-A The performance of RC-LQR", "weight": 1.0} -->

To illustrate the effectiveness of the RC-LQR, we compare it with the standard LQR and the LEQG with $\theta = 0.01$. Fig. 1 depicts the evolution of their controlled states $x_{k,1}$ under the same noise realization, and confirms that our RC-LQR controller compensates the risk better than that of the LQR and LEQG. A similar observation can also be found.

<!-- chunk {"id": "body-0039", "role": "body", "section": "VI-B Model-based Setting", "weight": 1.0} -->

In the model-based setting, we assume that all the parameters in the model are known. Since the system is open-loop unstable, we select an initial policy such that ${\rho{({A - {BK^{}}})}} < 1$. Since the bounds for the stepsizes in Theorem 3 ‣ IV Policy Gradient Primal-dual Algorithm for the Model-based Setting ‣ Global Convergence of Policy Gradient Primal-dual Methods for Risk-constrained LQRs Research of the first two authors was supported by National Natural Science Foundation of China under Grant no. 62033006. Research of the third author was supported by the ONR MURI Grant N00014-16-1-2710. F. Zhao and K. You are with the Department of Automation and BNRist, Tsinghua University, Beijing 100084, China. e-mail: zhaofr18@mails.tsinghua.edu.cn, youky@tsinghua.edu.cn. Tamer Başar is with the Coordinated Science Laboratory, University of Illinois at Urbana-Champaign, Urbana, IL 61801 USA.

<!-- chunk {"id": "body-0040", "role": "body", "section": "VI-B Model-based Setting", "weight": 1.0} -->

e-mail: basar1@illinois.edu.") could be conservative in practice, we manually tune them to be large before divergence of (23 ‣ IV Policy Gradient Primal-dual Algorithm for the Model-based Setting ‣ Global Convergence of Policy Gradient Primal-dual Methods for Risk-constrained LQRs Research of the first two authors was supported by National Natural Science Foundation of China under Grant no. 62033006. Research of the third author was supported by the ONR MURI Grant N00014-16-1-2710. F. Zhao and K. You are with the Department of Automation and BNRist, Tsinghua University, Beijing 100084, China. e-mail: zhaofr18@mails.tsinghua.edu.cn, youky@tsinghua.edu.cn. Tamer Başar is with the Coordinated Science Laboratory, University of Illinois at Urbana-Champaign, Urbana, IL 61801 USA.

<!-- chunk {"id": "body-0041", "role": "body", "section": "VI-B Model-based Setting", "weight": 1.0} -->

e-mail: basar1@illinois.edu.")) and obtain that $\eta = {3 \times 10^{- 3}}$ for the PG, $\eta = 0.02$ for the NPG and $\eta = 0.5$ for the GN. We also consider the backtracking line search with ${\alpha = 0.25},{\beta = 0.5}$ for the PG and NPG where an initial stepsize is set to $\eta = 0.01$ for the PG and $\eta = 0.05$ for the NPG. Note that $\eta = 0.5$ is already an optimal stepsize for the GN; see the end of Section IV-A ‣ IV Policy Gradient Primal-dual Algorithm for the Model-based Setting ‣ Global Convergence of Policy Gradient Primal-dual Methods for Risk-constrained LQRs Research of the first two authors was supported by National Natural Science Foundation of China under Grant no.

<!-- chunk {"id": "body-0042", "role": "body", "section": "VI-B Model-based Setting", "weight": 1.0} -->

62033006. Research of the third author was supported by the ONR MURI Grant N00014-16-1-2710. F. Zhao and K. You are with the Department of Automation and BNRist, Tsinghua University, Beijing 100084, China. e-mail: zhaofr18@mails.tsinghua.edu.cn, youky@tsinghua.edu.cn. Tamer Başar is with the Coordinated Science Laboratory, University of Illinois at Urbana-Champaign, Urbana, IL 61801 USA. e-mail: basar1@illinois.edu.").

<!-- chunk {"id": "body-0043", "role": "body", "section": "VI-B Model-based Setting", "weight": 1.0} -->

First, we validate the convergence results in Theorem 3 ‣ IV Policy Gradient Primal-dual Algorithm for the Model-based Setting ‣ Global Convergence of Policy Gradient Primal-dual Methods for Risk-constrained LQRs Research of the first two authors was supported by National Natural Science Foundation of China under Grant no. 62033006. Research of the third author was supported by the ONR MURI Grant N00014-16-1-2710. F. Zhao and K. You are with the Department of Automation and BNRist, Tsinghua University, Beijing 100084, China. e-mail: zhaofr18@mails.tsinghua.edu.cn, youky@tsinghua.edu.cn. Tamer Başar is with the Coordinated Science Laboratory, University of Illinois at Urbana-Champaign, Urbana, IL 61801 USA. e-mail: basar1@illinois.edu.") on the three gradient methods in (23 ‣ IV Policy Gradient Primal-dual Algorithm for the Model-based Setting ‣ Global Convergence of Policy Gradient Primal-dual Methods for Risk-constrained LQRs Research of the first two authors was supported by National Natural Science Foundation of China under Grant no.

<!-- chunk {"id": "body-0044", "role": "body", "section": "VI-B Model-based Setting", "weight": 1.0} -->

62033006. Research of the third author was supported by the ONR MURI Grant N00014-16-1-2710. F. Zhao and K. You are with the Department of Automation and BNRist, Tsinghua University, Beijing 100084, China. e-mail: zhaofr18@mails.tsinghua.edu.cn, youky@tsinghua.edu.cn. Tamer Başar is with the Coordinated Science Laboratory, University of Illinois at Urbana-Champaign, Urbana, IL 61801 USA. e-mail: basar1@illinois.edu.")).

<!-- chunk {"id": "body-0045", "role": "body", "section": "VI-B Model-based Setting", "weight": 1.0} -->

We adopt the relative Lagrangian error ${{({{\mathcal{L}{(X^{(i)},\mu)}} - {\mathcal{L}^{\ast}{(\mu)}}})}/\mathcal{L}^{\ast}}{(\mu)}$ to examine the convergence behaviors of (23 ‣ IV Policy Gradient Primal-dual Algorithm for the Model-based Setting ‣ Global Convergence of Policy Gradient Primal-dual Methods for Risk-constrained LQRs Research of the first two authors was supported by National Natural Science Foundation of China under Grant no. 62033006. Research of the third author was supported by the ONR MURI Grant N00014-16-1-2710. F. Zhao and K. You are with the Department of Automation and BNRist, Tsinghua University, Beijing 100084, China. e-mail: zhaofr18@mails.tsinghua.edu.cn, youky@tsinghua.edu.cn.

<!-- chunk {"id": "body-0046", "role": "body", "section": "VI-B Model-based Setting", "weight": 1.0} -->

Tamer Başar is with the Coordinated Science Laboratory, University of Illinois at Urbana-Champaign, Urbana, IL 61801 USA. e-mail: basar1@illinois.edu.")). Fig. 2 validates their linear convergence rates of Theorem 3 ‣ IV Policy Gradient Primal-dual Algorithm for the Model-based Setting ‣ Global Convergence of Policy Gradient Primal-dual Methods for Risk-constrained LQRs Research of the first two authors was supported by National Natural Science Foundation of China under Grant no. 62033006. Research of the third author was supported by the ONR MURI Grant N00014-16-1-2710. F. Zhao and K. You are with the Department of Automation and BNRist, Tsinghua University, Beijing 100084, China. e-mail: zhaofr18@mails.tsinghua.edu.cn, youky@tsinghua.edu.cn. Tamer Başar is with the Coordinated Science Laboratory, University of Illinois at Urbana-Champaign, Urbana, IL 61801 USA.

<!-- chunk {"id": "body-0047", "role": "body", "section": "VI-B Model-based Setting", "weight": 1.0} -->

e-mail: basar1@illinois.edu.") and Table I ‣ IV Policy Gradient Primal-dual Algorithm for the Model-based Setting ‣ Global Convergence of Policy Gradient Primal-dual Methods for Risk-constrained LQRs Research of the first two authors was supported by National Natural Science Foundation of China under Grant no. 62033006. Research of the third author was supported by the ONR MURI Grant N00014-16-1-2710. F. Zhao and K. You are with the Department of Automation and BNRist, Tsinghua University, Beijing 100084, China. e-mail: zhaofr18@mails.tsinghua.edu.cn, youky@tsinghua.edu.cn. Tamer Başar is with the Coordinated Science Laboratory, University of Illinois at Urbana-Champaign, Urbana, IL 61801 USA. e-mail: basar1@illinois.edu."). As expected, it is also observed that the use of a backtracking line search increases the convergence rate.

<!-- chunk {"id": "body-0048", "role": "body", "section": "VI-B Model-based Setting", "weight": 1.0} -->

Then, we validate the sublinear convergence result in Theorem 4, where the GN is applied to minimize the Lagrangian in Algorithm 1. Let the initial multiplier be $\mu_{1} = 0$ and the diminishing stepsize be $\zeta^{k} = {1/{({15\sqrt{k}})}}$. Fig. 3 displays how the relative optimality gap ${{|{{J{(X^{k})}} - {J{(X^{\ast})}}}|}/J}{(X^{\ast})}$ and the constraint violation ${\max{\{{{J_{c}{(X^{k})}} - \overline{\rho}},0\}}}/\overline{\rho}$ decrease to zero. Clearly, both converge fast under our model-based policy gradient primal-dual method.

<!-- chunk {"id": "body-0049", "role": "body", "section": "VI-B Model-based Setting", "weight": 1.0} -->

Note that both the objective function $J{(X)}$ and the constraint function $J_{c}{(X)}$ are quadratic, and converge with a similar behavior.

<!-- chunk {"id": "body-0050", "role": "body", "section": "VI-C Sample-based Setting", "weight": 1.0} -->

In the sample-based setting, we use trajectory samples of the system to compute and conduct $20$ independent trials. First, we examine the convergence performance of Algorithm 2 ‣ V Policy Gradient Primal-dual Algorithm for the Sample-based Setting ‣ Global Convergence of Policy Gradient Primal-dual Methods for Risk-constrained LQRs Research of the first two authors was supported by National Natural Science Foundation of China under Grant no. 62033006. Research of the third author was supported by the ONR MURI Grant N00014-16-1-2710. F. Zhao and K. You are with the Department of Automation and BNRist, Tsinghua University, Beijing 100084, China. e-mail: zhaofr18@mails.tsinghua.edu.cn, youky@tsinghua.edu.cn. Tamer Başar is with the Coordinated Science Laboratory, University of Illinois at Urbana-Champaign, Urbana, IL 61801 USA.

<!-- chunk {"id": "body-0051", "role": "body", "section": "VI-C Sample-based Setting", "weight": 1.0} -->

e-mail: basar1@illinois.edu.") and set the smoothing radius to $r = 0.2$, the sample horizon of the oracle $T = 100$ and the constant stepsize $\eta = {1 \times 10^{- 5}}$. Moreover, we display the relative Lagrangian error for $\mu = 2$ in Fig. 4, where the bold centerline denotes the trial mean and the shaded region indicates the variance size. As expected by Theorem 5 ‣ V Policy Gradient Primal-dual Algorithm for the Sample-based Setting ‣ Global Convergence of Policy Gradient Primal-dual Methods for Risk-constrained LQRs Research of the first two authors was supported by National Natural Science Foundation of China under Grant no. 62033006. Research of the third author was supported by the ONR MURI Grant N00014-16-1-2710. F. Zhao and K. You are with the Department of Automation and BNRist, Tsinghua University, Beijing 100084, China. e-mail: zhaofr18@mails.tsinghua.edu.cn, youky@tsinghua.edu.cn.

<!-- chunk {"id": "body-0052", "role": "body", "section": "VI-C Sample-based Setting", "weight": 1.0} -->

Tamer Başar is with the Coordinated Science Laboratory, University of Illinois at Urbana-Champaign, Urbana, IL 61801 USA. e-mail: basar1@illinois.edu."), Algorithm 2 ‣ V Policy Gradient Primal-dual Algorithm for the Sample-based Setting ‣ Global Convergence of Policy Gradient Primal-dual Methods for Risk-constrained LQRs Research of the first two authors was supported by National Natural Science Foundation of China under Grant no. 62033006. Research of the third author was supported by the ONR MURI Grant N00014-16-1-2710. F. Zhao and K. You are with the Department of Automation and BNRist, Tsinghua University, Beijing 100084, China. e-mail: zhaofr18@mails.tsinghua.edu.cn, youky@tsinghua.edu.cn. Tamer Başar is with the Coordinated Science Laboratory, University of Illinois at Urbana-Champaign, Urbana, IL 61801 USA. e-mail: basar1@illinois.edu.") converges to a small relative error of $3\%$ with a small variance.

<!-- chunk {"id": "body-0053", "role": "body", "section": "VI-C Sample-based Setting", "weight": 1.0} -->

Then, we verify the convergence result of our sample-based primal-dual method in Theorem 6 by performing Algorithm 3 ‣ V Policy Gradient Primal-dual Algorithm for the Sample-based Setting ‣ Global Convergence of Policy Gradient Primal-dual Methods for Risk-constrained LQRs Research of the first two authors was supported by National Natural Science Foundation of China under Grant no. 62033006. Research of the third author was supported by the ONR MURI Grant N00014-16-1-2710. F. Zhao and K. You are with the Department of Automation and BNRist, Tsinghua University, Beijing 100084, China. e-mail: zhaofr18@mails.tsinghua.edu.cn, youky@tsinghua.edu.cn. Tamer Başar is with the Coordinated Science Laboratory, University of Illinois at Urbana-Champaign, Urbana, IL 61801 USA. e-mail: basar1@illinois.edu.").

<!-- chunk {"id": "body-0054", "role": "body", "section": "VI-C Sample-based Setting", "weight": 1.0} -->

Let the initial multiplier be $\mu^{1} = 0$ and the diminishing stepsize be $\zeta^{k} = {1/{({15\sqrt{k}})}}$. Fig. 5 illustrates that both the relative optimality gap and the constraint violation eventually are close to zero.

<!-- chunk {"id": "body-0055", "role": "body", "section": "Concluding Remarks", "weight": 1.0} -->

In this paper, we have proposed a policy gradient primal-dual framework with global convergence guarantees to solve the RC-LQR problem with a variance-like constraint. Specifically, we have shown here strong duality, to establish the global convergence, which in fact can be extended to the case of multiple constraints. Such a framework can also be utilized to study linear quadratic tracking.
