<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Data-enabled Policy Optimization for the Linear Quadratic Regulator

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Policy optimization (PO), an essential approach of reinforcement learning for a broad range of system classes, requires significantly more system data than indirect (identification-followed-by-control) methods or behavioral-based direct methods even in the simplest linear quadratic regulator (LQR) problem. In this paper, we take an initial step towards bridging this gap by proposing the data-enabled policy optimization (DeePO) method, which requires only a finite number of sufficiently exciting data to iteratively solve the LQR problem via PO. Based on a data-driven closed-loop parameterization, we are able to directly compute the policy gradient from a batch of persistently exciting data. Next, we show that the nonconvex PO problem satisfies a projected gradient dominance property by relating it to an equivalent convex program, leading to the global convergence of DeePO. Moreover, we apply regularization methods to enhance certainty-equivalence and robustness of the resulting controller and show an implicit regularization property. Finally, we perform simulations to validate our results.

<!-- chunk {"id": "body-0003", "role": "body", "section": "Introduction", "weight": 1.5} -->

As a cornerstone of modern control theory, the linear quadratic regulator (LQR) problem has been the benchmark for data-driven control methods that seek to design a controller from raw system data. The manifold approaches to data-driven control can be broadly categorized as indirect (when identifying a dynamical model followed by model-based control design) versus direct (when bypassing the identification step). The use of direct data-driven control is usually motivated when the dynamical model is difficult to establish, or is too complex for model-based control design. As an end-to-end approach, the direct methods are conceptually simple and easy to implement in practice.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

A representative instance of direct data-driven control is policy optimization (PO), an essential approach for applications of reinforcement learning (RL). As an iterative method, PO directly searches over the policy space to optimize a performance metric of interest. Based on zeroth-order optimization techniques, it uses multiple system trajectories to estimate the policy gradient. There has been a resurgent interest in studying theoretical properties of PO on the LQR problem such as convergence and sample complexity; see e.g., and the comprehensive survey. Even though global convergence has been shown for the nonconvex PO problem by a gradient dominance property, there exists a considerable gap in the sample complexity between PO and indirect methods, which have proved themselves to be more sample-efficient for solving the LQR problem. This gap is due to the exploration or trial-and-error nature of RL, or more specifically, that the cost used for gradient estimate can only be evaluated after a whole trajectory is observed. Thus, the existing PO methods require numerous system trajectories to find an optimal policy, even in the simplest LQR setting.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

Recent years have witnessed an emerging line of direct methods inspired by the Fundamental Lemma, which states that the behavior of a linear time-invariant (LTI) system can be characterized by the range space of raw data matrices. This result implies a non-parametric representation of LTI systems, giving rise to a notable implicit design called data-enabled predictive control (DeePC), which has seen many successful implementations in different practical scenarios. The fundamental lemma has also been utilized to solve various explicit control design and analysis problems. In particular, it has been shown in that using subspace relations, the closed-loop LTI system can be parameterized by input-state data, leading to a data-based convex reformulation of the LQR problem. Compared with PO, this approach is significantly more sample-efficient as it only requires a batch of persistently exciting (PE) data. Indeed, the PE condition is equivalent to identifiability for LTI systems and should be a minimal assumption for most control design problems, e.g., the LQR problem.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

There have been many recent works leveraging regularization methods to promote certainty-equivalence and robustness of the LQR, and to bridge behavioral-based direct and indirect methods. All these methods use only a small batch of PE data compared to data-hungry zeroth-order PO methods. This leads to a natural question: does there exist a data-efficient PO method for solving the LQR problem?

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

In this paper, we provide an affirmative answer to the above question. By leveraging the data-driven closed-loop parameterization, we propose an iterative method called data-enabled policy optimization (DeePO) to solve the LQR problem. Instead of estimating the policy gradient from the cost of observed trajectories, we show that after a change of optimization variables, the gradient can be directly characterized from a batch of PE data. Even though the resulting optimization problem is nonconvex, it can be parameterized as a data-based convex program. By exploiting this relation and using a recent PO result, we further show that the LQR cost is projected gradient dominated, while it is only gradient dominated. By establishing that the cost is also locally smooth, we show that the projected gradient method converges to the global optimum. We also investigate how regularization affects the convergence of DeePO. In particular, we show that the certainty-equivalence regularizer leads to an implicit regularization property, meaning that the DeePO algorithm without regularization behaves as if it is regularized. This property has been advocated as an important feature of gradient-based methods for solving many nonconvex problems.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Introduction", "weight": 1.5} -->

Finally, we perform a numerical case study to validate our theoretical results. We are hopeful that the discovered DeePO method with significantly relaxed data requirements offers a possible path towards direct adaptive LQR control.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Problem Formulation", "weight": 1.0} -->

In this section, we first revisit the model-based LQR problem. By recapitulating its direct data-driven formulation, we then propose our PO reformulation.

<!-- chunk {"id": "body-0010", "role": "body", "section": "II-A The Model-based LQR problem", "weight": 1.0} -->

where ${x{(t)}} \in {\mathbb{R}}^{n}$ and ${u{(t)}} \in {\mathbb{R}}^{m}$ are the state and control input, respectively. We assume that $(A,B)$ are controllable.

<!-- chunk {"id": "body-0011", "role": "body", "section": "II-A The Model-based LQR problem", "weight": 1.0} -->

The LQR problem is phrased as finding a state-feedback gain $K \in {\mathbb{R}}^{m \times n}$ to minimize the quadratic cost

<!-- chunk {"id": "body-0012", "role": "body", "section": "II-A The Model-based LQR problem", "weight": 1.0} -->

where $P^{\ast}$ is the unique positive semi-definite solution to the algebraic Riccati equation

<!-- chunk {"id": "body-0013", "role": "body", "section": "II-A The Model-based LQR problem", "weight": 1.0} -->

We aim to solve the LQR problem in a direct data-driven approach when $(A,B)$ are unknown, but we assume the access to a $T$-length dataset of states and control inputs.

<!-- chunk {"id": "body-0014", "role": "body", "section": "II-B Direct data-driven formulation", "weight": 1.0} -->

Define the offline data matrices

<!-- chunk {"id": "body-0015", "role": "body", "section": "II-B Direct data-driven formulation", "weight": 1.0} -->

which satisfy the system dynamics

<!-- chunk {"id": "body-0016", "role": "body", "section": "II-B Direct data-driven formulation", "weight": 1.0} -->

Throughout the paper, we assume that the following block matrix of input and state data

<!-- chunk {"id": "body-0017", "role": "body", "section": "II-B Direct data-driven formulation", "weight": 1.0} -->

i.e., the information in the data is sufficiently rich. This condition is necessary for identifying $(A,B)$ from data and for solving the data-driven LQR problem. As shown, it can be ensured provided that the input data $U_{-}$ is PE of order $n + 1$. Note that the columns of $(X_{-},U_{-},X_{+})$ are not necessarily consecutive data samples. In fact, they could be from independent or multiple averaged experiments as long as they satisfy and.

<!-- chunk {"id": "body-0018", "role": "body", "section": "II-B Direct data-driven formulation", "weight": 1.0} -->

Under the rank condition, there exists a matrix $G \in {\mathbb{R}}^{T \times n}$ that satisfies

<!-- chunk {"id": "body-0019", "role": "body", "section": "II-B Direct data-driven formulation", "weight": 1.0} -->

for any given $K$. That is, $K$ can be parameterized by $K = {U_{-}G}$ where $G$ satisfies a linear constraint ${X_{-}G} = I_{n}$. Then, the closed-loop matrix can be expressed in a data-driven fashion as

<!-- chunk {"id": "body-0020", "role": "body", "section": "II-B Direct data-driven formulation", "weight": 1.0} -->

leading to the following closed-loop system

<!-- chunk {"id": "body-0021", "role": "body", "section": "II-B Direct data-driven formulation", "weight": 1.0} -->

Furthermore, the LQR problem becomes

<!-- chunk {"id": "body-0022", "role": "body", "section": "II-B Direct data-driven formulation", "weight": 1.0} -->

Here, $J{(G)}$ is the LQR cost following and ${u{(t)}} = {U_{-}Gx{(t)}}$, and $\mathcal{S}_{G}$ is the feasible set. In contrast to the model-based LQR, the problem is characterized by raw data matrices. Though can be reformulated as a semi-definite program (SDP) using techniques, it is computationally challenging to solve for a large data size.

<!-- chunk {"id": "body-0023", "role": "body", "section": "II-B Direct data-driven formulation", "weight": 1.0} -->

In this paper, we take an iterative PO perspective to solve viewing $G$ as the optimization matrix. We aim to design a gradient-based method to find an optimal $G$ while maintaining feasibility, and recover the control from as $K = {U_{-}G}$. Since is a challenging constrained nonconvex problem, we leverage a novel convex parameterization to establish the global convergence.

<!-- chunk {"id": "body-0024", "role": "body", "section": "Data-enabled policy optimization", "weight": 1.0} -->

In this section, we first present our novel PO method for solving. Then, we propose a convex parameterization of to derive the projected gradient dominance property of $J{(G)}$. By establishing that $J{(G)}$ is locally smooth over any sublevel set, we are able to show the global convergence of our method.

<!-- chunk {"id": "body-0025", "role": "body", "section": "III-A Data-enabled policy optimization to solve", "weight": 1.0} -->

For $G \in \mathcal{S}_{G}$, the cost $J{(G)}$ is finite and has the following closed-form expressions

<!-- chunk {"id": "body-0026", "role": "body", "section": "III-A Data-enabled policy optimization to solve", "weight": 1.0} -->

where $P_{G}$ satisfies the Lyapunov equation

<!-- chunk {"id": "body-0027", "role": "body", "section": "III-A Data-enabled policy optimization to solve", "weight": 1.0} -->

We have the following gradient expression for $J{(G)}$.

<!-- chunk {"id": "body-0028", "role": "body", "section": "III-B Optimality via a convex parameterization", "weight": 1.0} -->

We first relate to a convex parameterization via a change of variables $G = {L\Sigma^{- 1}}$ as

<!-- chunk {"id": "body-0029", "role": "body", "section": "III-B Optimality via a convex parameterization", "weight": 1.0} -->

Let $\mathcal{S}$ be its feasible set. The equivalence between the two problems and are established below.

<!-- chunk {"id": "body-0030", "role": "body", "section": "DeePO for the regularized LQR", "weight": 1.0} -->

For the direct data-driven LQR formulation, regularization plays an important role in promoting certainty-equivalence and robust stability when the data is corrupted with noise. This section investigates how regularization affects the convergence of DeePO.

<!-- chunk {"id": "body-0031", "role": "body", "section": "IV-A Certainty-equivalence regularizer", "weight": 1.0} -->

Consider the regularized LQR problem

<!-- chunk {"id": "body-0032", "role": "body", "section": "IV-A Certainty-equivalence regularizer", "weight": 1.0} -->

where $\lambda \geq 0$ is a user-defined constant and $\Pi_{D_{-}}:={I - {D_{-}^{\dagger}D_{-}}}$ is the projection matrix onto the nullspace of $D_{-}$. For the noiseless data $(X_{-},U_{-},X_{+})$ here, the orthogonality regularizer in does not change the optimal cost but only singles out a solution $G^{\ast}$ satisfying ${\Pi_{D_{-}}G^{\ast}} = 0$ from the solution set in (11 ‣ III Data-enabled policy optimization ‣ Data-enabled Policy Optimization for the Linear Quadratic Regulator")). When the data is corrupted with noises, it promotes certainty-equivalence, i.e., when $\lambda$ tends to infinity the solution of coincides with that of indirect data-driven control with an underlying maximum likelihood system identification attenuating the effect of noise; we refer interested readers to \[20, Section III\] for more discussions.

<!-- chunk {"id": "body-0033", "role": "body", "section": "IV-A Certainty-equivalence regularizer", "weight": 1.0} -->

Note that we have added the weighting $\Sigma_{G}^{1/2}$ to the regularizer (c.f. ) to make it compatible with the convex parameterization. As a result, can be formulated with ${L\Sigma^{- 1}} = G$ as the following convex problem

<!-- chunk {"id": "body-0034", "role": "body", "section": "IV-A Certainty-equivalence regularizer", "weight": 1.0} -->

Comparing, we see that $f_{\lambda}{(L,\Sigma)}$ upon amounts to $f{(L,\Sigma)}$ adding a convex regularizer, and hence $f_{\lambda}{(L,\Sigma)}$ is convex. Indeed, by standard matrix analysis, its Hessian acting on the direction $(\overset{\sim}{L},\overset{\sim}{\Sigma})$ satisfies

<!-- chunk {"id": "body-0035", "role": "body", "section": "IV-A Certainty-equivalence regularizer", "weight": 1.0} -->

Moreover, following analogous arguments as in Section III, $J_{\lambda}{(G)}$ can also be shown to be locally smooth. Based on previous analysis, the projected gradient update

<!-- chunk {"id": "body-0036", "role": "body", "section": "IV-A Certainty-equivalence regularizer", "weight": 1.0} -->

converges to the optimal solution of under a proper stepsize selection.

<!-- chunk {"id": "body-0037", "role": "body", "section": "IV-B Robustness-promoting regularizer", "weight": 1.0} -->

Regularization can also be used to enhance robust stability. Consider the following regularized LQR problem

<!-- chunk {"id": "body-0038", "role": "body", "section": "IV-B Robustness-promoting regularizer", "weight": 1.0} -->

where $\gamma \geq 0$ is a user-defined constant. To see why it promotes the robust stability for noisy data, we note that the state covariance matrix is given by

<!-- chunk {"id": "body-0039", "role": "body", "section": "IV-B Robustness-promoting regularizer", "weight": 1.0} -->

Thus, a small $\text{Tr}{\{{G\Sigma_{G}G^{\top}}\}}$ can reduce the effect of noises in $X_{+}$. Different from the certainty-equivalence regularization, the regularizer in bias the LQR solution even when the data is noiseless, reflecting a trade-off between performance and robustness.

<!-- chunk {"id": "body-0040", "role": "body", "section": "IV-B Robustness-promoting regularizer", "weight": 1.0} -->

The problem can be formulated with ${L\Sigma^{- 1}} = G$ as

<!-- chunk {"id": "body-0041", "role": "body", "section": "IV-B Robustness-promoting regularizer", "weight": 1.0} -->

Clearly, $f_{\lambda}{(L,\Sigma)}$ is also convex since

<!-- chunk {"id": "body-0042", "role": "body", "section": "IV-B Robustness-promoting regularizer", "weight": 1.0} -->

By analogous reasoning and combining the smoothness of the regularizer, the projected gradient update

<!-- chunk {"id": "body-0043", "role": "body", "section": "IV-B Robustness-promoting regularizer", "weight": 1.0} -->

converges to the optimal solution of under a proper stepsize selection.

<!-- chunk {"id": "body-0044", "role": "body", "section": "IV-C Implicit regularization", "weight": 1.0} -->

Apart from the convergence, we observe an interesting implicit regularization property of the certainty-equivalence regularized LQR problem formally defined below.

<!-- chunk {"id": "body-0045", "role": "body", "section": "Simulations", "weight": 1.0} -->

In this section, we perform simulations to validate the convergence of DeePO and the effects of regularization.

<!-- chunk {"id": "body-0046", "role": "body", "section": "V-A Numerical example", "weight": 1.0} -->

We randomly generate a dynamical model $(A,B)$ with ${n = 4},{m = 2}$ from a standard normal distribution and normalize $A$ such that ${\rho{(A)}} = 0.8$, i.e., the open-loop system is stable. The resulting model parameters $(A,B)$ are

<!-- chunk {"id": "body-0047", "role": "body", "section": "V-A Numerical example", "weight": 1.0} -->

It is straightforward to check that $(A,B)$ is controllable. Let $Q = I_{4}$ and $R = I_{2}$. We use Gaussian distribution to generate a batch of sufficiently exciting data $(U_{-},X_{-})$ with $T = 10$ that satisfies, and compute $X_{+}$. In the sequel, we only use $(U_{-},X_{-},X_{+})$ to perform the DeePO methods and validate the convergence.

<!-- chunk {"id": "body-0048", "role": "body", "section": "V-B Convergence of the DeePO methods", "weight": 1.0} -->

We consider three algorithms, i.e, DeePO in (10 ‣ III Data-enabled policy optimization ‣ Data-enabled Policy Optimization for the Linear Quadratic Regulator")), DeePO with the certainty-equivalence regularizer in and with the robustness regularizer. For all the three algorithms, we set the stepsize to $\eta = {2 \times 10^{- 3}}$ for a fair comparison. For DeePO and DeePO with robustness regularizer, we set the initial policy as

<!-- chunk {"id": "body-0049", "role": "body", "section": "V-B Convergence of the DeePO methods", "weight": 1.0} -->

with $K^{0} = 0$ since the system is open-loop stable. For DeePO with certainty-equivalence regularizer, we set

<!-- chunk {"id": "body-0050", "role": "body", "section": "V-B Convergence of the DeePO methods", "weight": 1.0} -->

where the elements of $M \in {\mathbb{R}}^{T \times n}$ are randomly sampled from a Gaussian distribution $\mathcal{N}{(0,0.01)}$ (otherwise due to the implicit regularization, there will be no difference in the convergence curve compared with DeePO). To see how regularization parameters affect the performance, we select $\lambda = {1,10}$ for the certainty-equivalence regularizer and $\gamma = {1,10}$ for the robustness regularizer.

<!-- chunk {"id": "body-0051", "role": "body", "section": "V-B Convergence of the DeePO methods", "weight": 1.0} -->

We illustrate the performance of the three algorithms in Fig. 2, where their relative errors are defined as ${({{J{(G^{k})}} - J^{\ast}})}/J^{\ast}$, ${({{J_{\lambda}{(G^{k})}} - J_{\lambda}^{\ast}})}/J_{\lambda}^{\ast}$, and ${({{J_{\gamma}{(G^{k})}} - J_{\gamma}^{\ast}})}/J_{\gamma}^{\ast}$, respectively. While Theorem 1 ‣ III-C Global convergence of DeePO ‣ III Data-enabled policy optimization ‣ Data-enabled Policy Optimization for the Linear Quadratic Regulator") only shows a more conservative sublinear convergence rate, all the three algorithms converge linearly in the simulation. The DeePO algorithm with certainty-equivalence regularizer (denoted by CE in Fig. 2) has the slowest convergence.

<!-- chunk {"id": "body-0052", "role": "body", "section": "V-B Convergence of the DeePO methods", "weight": 1.0} -->

The case for $\lambda = 10$ converges faster than the case $\lambda = 1$ due to the faster decay of the regularizer $\lambda{\|{\Pi_{D_{-}}G\Sigma_{G}^{1/2}}\|}^{2}$, and it achieves the same rate as the unregularized DeePO algorithm. Under the robustness regularizer, the DeePO algorithm has the fastest convergence, and $\gamma = 10$ leads to a larger convergence rate. Nevertheless, the resulted policy is different from those of the other two algorithms as discussed in Section IV-B. Finally, we note that all the algorithms only use $10$ pairs of state-input data to achieve an arbitrary relative error. In sharp contrast, the zeroth-order optimization method in uses $10^{5}$ trajectories (of manually tuned length to approximate the cost well) to achieve $0.01$ relative error for an LTI system with $m = n = 3$.

<!-- chunk {"id": "body-0053", "role": "body", "section": "Conclusion", "weight": 1.5} -->

In this paper, we have proposed the DeePO method that only requires a finite number of PE data to solve the LQR problem. By relating the nonconvex optimization problem to a convex program, we have shown the global convergence of DeePO. Furthermore, we have shown that the regularization method can be applied to enhance certainty-equivalence and robust stability without affecting its convergence. The implicit regularization property has also provided an insightful understanding on the optimization landscape of DeePO.

<!-- chunk {"id": "body-0054", "role": "body", "section": "Conclusion", "weight": 1.5} -->

In future, it would be valuable to discover a strongly convex reparameterization of, which may improve the sublinear convergence rate to linear. It would also be interesting to study DeePO in a more general setting, e.g., the LQR with noisy inputs. Since DeePO is an efficient iterative method, it is expected to be able to applied to online control, where the control performance is constantly improved by collecting more real-time data. We are also hopeful that it can be used to solve the adaptive LQR for time-varying systems.
