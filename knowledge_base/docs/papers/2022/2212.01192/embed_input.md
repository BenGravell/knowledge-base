<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Policy Iteration Using Q-functions: Linear Dynamics with Multiplicative Noise

Topics include Policy gradients, Policy iteration, System identification, Q-functions, Multiplicative noise, Instrumental variable, Markov decision process.

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

This paper presents a novel model-free and fully data-driven policy iteration scheme for quadratic regulation of linear dynamics with state- and input-multiplicative noise. The implementation is similar to the least-squares temporal difference scheme for Markov decision processes, estimating Q-functions by solving a least-squares problem with instrumental variables. The scheme is compared with a model-based system identification scheme and natural policy gradient through numerical experiments.

<!-- chunk {"id": "body-0003", "role": "body", "section": "Introduction", "weight": 1.5} -->

The success story of AlphaZero in [Silver2017a] and similar reinforcement learning strategies in a variety of applications has reinvigorated the interest of the control community in learning schemes. Many of these fall under the general framework of dynamic programming, policy iteration, etc. (see [Bertsekas2022, Bertsekas2022a] for a good overview). Hence understanding the performance of such schemes in simple settings can generalize to more complex problems. One setting under investigation has been Linear Quadratic Regulation (LQR). For example [Recht2018,Mania2019,Dean2019] consider model-based approaches where system identification is performed separately from control synthesis. In [Bradtke1994,Lewis2009,Bu2019b] meanwhile model-free approaches more akin to usual reinforcement learning like policy iteration and policy gradient were investigated.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

A setting with similar potential is quadratic regulation of linear dynamics with multiplicative noise [Wonham1967]. Here analytical solutions are still available, yet several challenges absent from classical LQR present themselves. For example, the optimal controller depends on the first and second moment of the noise unlike in LQR with additive noise and the separation principle does not hold. Moreover, as we will see, data-driven policy evaluation is not possible through normal least-squares as in [Bradtke1994] and instead requires instrumental variables as is the case with Markov decision processes [Bradtke1996]. Multiplicative noise also arises naturally in aerospace and vehicle control applications [Damm2004], biological applications [Todorov2005,Mohler1980b] and communication channels [Wang2002] among others. Finally, the inclusion of multiplicative noise also induces robustness against parametric uncertainty [Coppens2022,Gravell2020], which is especially helpful in data-driven applications.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

For multiplicative noise the model-based setting has already been investigated in [Coppens2019, Coppens2020, Coppens2022, Xing2021]. Policy gradient was investigated in [Gravell2021] and policy iteration in [Wang2018, Gravell2022]. The last two results however assumed the possibility of exact policy evaluation, which is only possible for known dynamics.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

In this work we provide a data-driven scheme for policy iteration applied to linear dynamics with multiplicative noise. The approximate policy evaluation step is based on Q-functions as in [Bradtke1994] with the instrumental variables used for least squares temporal difference (LSTD) learning in [Bradtke1996]. Our scheme can both operate in an off-policy setting where data-generation happens with some fixed, pre-determined policy and in an on-policysetting, where the last policy iterate is applied to the dynamics with some additive noise to enable exploration.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

The remainder of this paper begins with a problem definition in sec:problem. Next, in sec:approximate-policy-evaluation a novel approximate policy evaluation scheme using Q-functions is derived, which is integrated in a policy iteration scheme in sec:algorithms. We also review an existing model-based scheme [Coppens2022] and a policy gradient scheme [Gravell2021]. In sec:numerical we we then compare the performance and applicability of these three data-driven control schemes. In sec:conclusionwe then conclude the paper and suggest further work.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Introduction", "weight": 1.5} -->

Let $\Re$ denote the reals and $\N$ the naturals. For $Z \in \Re^{m \times n}$ let $\trans{Z}$ denote the transpose and let $\nrm{Z}_2$ ($\nrm{Z}_F$) be the spectral (Frobenius) norm. When $Z \in \Re^{n \times n}$ let $\lambda(Z) = (\lambda_1, \dots, \lambda_m)$ denote the vector of eigenvalues in descending order of modulus and $\rho(Z) = |\lambda_1(X)|$ the spectral radius. For a vector $x \in \Re^d$ let $\nrm{x}_2$ denote the Euclidean norm. Let $\E[\cdot]$denote the expectation. $\sym{d}$ the set of symmetric $d$ by $d$ matrices and by $\sym{d}_{++}$ ($\sym{d}_{+}$) the positive (semi)definite matrices.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Introduction", "weight": 1.5} -->

For matrices of conformable size $X, Y$ we use $[X, Y]$ for horizontal concatenation, let $(x, y)$ denote vertical concatenation between (column) vectors and let $I_d \in \Re^{d\times d}$ be the identity. Elements of matrices $X \in \Re^{m \times n}$ (and vectors $x \in \Re^d$) are indexed using $X_{ij}$ ($x_i$) for $i \in \{1, \dots, m\}$, $j \in \{1, \dots, n\}$ ($i \in \{1, \dots, d\}$). For a matrix-valued operator $\op{E} \colon \sym{n} \to \sym{m}$ we similarly write $\op{E}_{ij} \colon \sym{n} \to \Re$.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Problem Setup", "weight": 1.0} -->

The goal is to solve $$\minimize_{u_0, u_1, \dots} \quad \E \left[\sum_{t=0}^{\infty} \trans{x_t} Q x_t + \trans{u_t} R u_t \right],$$ subject to [eq:dyn] with $Q \sgt 0$ and $R \sgt 0$ when only given access to trajectories $\{(x_t, u_t)\}_{t=0}^{T}$ of [eq:dyn]. The way in which these trajectories are generated (e.g. what policy to use) will be discussed in sec:data-generation.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Problem Setup", "weight": 1.0} -->

Often it is more convenient to consider the evolution of the second moments $X_t \dfn \E[x_t \trans{x_t}]$, $Z_t \dfn \E[z_t \trans{z_t}]$, with $z_t = (x_t, u_t)$ the augmented state, when solving [eq:lqr]. These follow the dynamics $$X_{t+1} = \op{E}(Z_t) \dfn \sum_{i,j=1}^{n_w} W_{ij} [A_i, B_i] Z_t \trans{[A_j, B_j]},$$ with $W \dfn \E[w_t \trans{w_t}]$ independent of $t$ due to the i.i.d. assumption.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Problem Setup", "weight": 1.0} -->

The LQR problem [eq:lqr] then becomes $$J_\star(X_0) \dfn \minimize_{Z_0, Z_1, \dots} \quad \sum_{t=0}^{\infty} \tr[H Z_t],$$ subject to $Z_t \sgeq 0$ and [eq:dynsm] starting from $X_0$ and where $H = \diag(Q, R) \sgt 0$. We refer to $J(X_0)$ as the value function. Equivalence of [eq:lqr] and [eq:lqrsm] was shown in [Coppens2022], where the properties of $\op{E}$ a completely positive (CP) operator were studied.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Problem Setup", "weight": 1.0} -->

Since we will often deal with partitionings of matrices like $Z \in \sym{n_z}$ we introduce the subscripts: where $Z_{xx} \in \sym{n_x}$and analogously for the other terms.

<!-- chunk {"id": "body-0014", "role": "body", "section": "Approximate Policy Evaluation", "weight": 1.0} -->

It is well known that the optimal policy solving eq:lqr is linear (cf. [Coppens2022]). In terms of moments such policies look like $$Z_t = \pi(X_t) \dfn \trans{[I, \, \trans{K}]} X_t [I, \, \trans{K}],$$ We will refer to $K$ and $\pi$interchangeably as the policy.

<!-- chunk {"id": "body-0015", "role": "body", "section": "Approximate Policy Evaluation", "weight": 1.0} -->

As usual, to derive our policy iteration algorithm we need to consider the Bellman operator $$(\op{T}_\pi J)(X) = \tr[\pi(X) H] + J[\op{E}(\pi(X))], \quad \forall X \sgeq 0.$$ and $\op{T} J \dfn \min_{\pi} \op{T}_\pi J$, operating on $J \colon \sym{n_x} \to \Re$.

<!-- chunk {"id": "body-0016", "role": "body", "section": "Approximate Policy Evaluation", "weight": 1.0} -->

If the dynamics are stabilizable (i.e. there exists a mean-square stabilizing controller), then the optimal value of eq:lqrsm is given as the fixed-point of $\op{T}$. Moreover the optimal controller is then $\argmin_{\pi} \op{T}_{\pi} J_\star$ of [eq:bellman] with $J_\star = \op{T} J_\star$ [Coppens2022].

<!-- chunk {"id": "body-0017", "role": "body", "section": "Approximate Policy Evaluation", "weight": 1.0} -->

In our case we know that the value function is linear in the second moment It is thus quadratic in the state, i.e. $J(X) = \tr[XP]$ for some $P \sgt 0$. Plugging in this parametrization and eq:policy and using the definition of the adjoint gives: $$(\op{T} J)(X) = \min_{K}\, \tr[X [I, \, \trans{K}](H + \adj{\op{E}}(P))\trans{[I, \, \trans{K}]}].$$ The minimizer, stated using the subscripts in eq:partitioning, is given as $K_{\star} = -(R + \adj{\op{E}}_{uu}(P))^{-1} \adj{\op{E}_{ux}}(P)$.

<!-- chunk {"id": "body-0018", "role": "body", "section": "Approximate Policy Evaluation", "weight": 1.0} -->

This generalized Riccati equation is derived in detail and solved using a SDP in [Coppens2022]. $K_\star$ through policy iteration, which repeatedly updates $\pi$ by finding a $\pi_+$ such that $$\pi_{+} = \argmin_{\pi'} T_{\pi'} J_{\pi}, \text{ with } J_{\pi} = T_{\pi} J_{\pi}.$$ Finding $J_{\pi}$ is called policy evaluation and requires solving a Lyapunov equation. Again using a parametrization $J_\pi(X) = \tr[P_\pi X]$, we write $J_\pi = T_\pi J_\pi$ as: &= \tr[X \adj{\pi} \left(H + \adj{\op{E}}(P_\pi) \right)], \nonumber for all $X$, where we used the definition of the adjoint.

<!-- chunk {"id": "body-0019", "role": "body", "section": "Approximate Policy Evaluation", "weight": 1.0} -->

Thus we recover the following Lyapunov equation For a proof of invertibility when $\pi$ is mean-square stabilizing see.

<!-- chunk {"id": "body-0020", "role": "body", "section": "Approximate Policy Evaluation", "weight": 1.0} -->

Several schemes exist to solve such equations using data (cf. [Bertsekas2012V2] and [Bradtke1996] for MDPs) However, even after finding $J_\pi$, computing the minimizer in eq:policy-iterationrequires the dynamics. Hence we use Q-functions.

<!-- chunk {"id": "body-0021", "role": "body", "section": "Q-functions", "weight": 1.0} -->

A Q-function in this setting maps $Z$ to some real number. We consider the Bellman operator on Q-functions: and $\op{F}\op{Q} \dfn \min_\pi \op{F}_\pi \op{Q}$. For some policy $\pi$ we define $\op{Q}_\pi$ as where $J_\pi$ solves $J_\pi = \op{T}_\pi J_\pi$ (cf. eq:lyapunov). We can show that this choice of $\op{Q}_\pi$ is a fixed-point of $\op{F}_\pi$: where we used the definition of $\op{T}_\pi$ for the second equality and $J_\pi = \op{T}_\pi J_\pi$for the third.

<!-- chunk {"id": "body-0022", "role": "body", "section": "Q-functions", "weight": 1.0} -->

$\op{Q}_\pi$ we implement policy iteration as: which is equivalent to $\pi_{+} = \argmin_{\pi'} \op{F}_{\pi'} \op{Q}_{\pi}$ (and thus eq:policy-iteration) yet requires no knowledge about the dynamics. Using a linear parametrization $\op{Q}_\pi = \tr[\Theta_\pi Z]$ we get Comparing with $K_\star$ from the previous section further confirms that the optimal gain can be recovered by selecting the correct value for $\Theta_\pi$.

<!-- chunk {"id": "body-0023", "role": "body", "section": "Least-Squares", "weight": 1.0} -->

In our data-driven setting, solving [eq:lyapunov] to perform the policy evaluation is challenging, since we need to evaluate $\op{E}$. In [Wang2018] it was assumed that it could be evaluated exactly, which requires knowing the true dynamics. Instead, similarly to [Bradtke1994], we opt to estimate $Q_\pi$directly from data. We begin by discussing constraints on the data and then derive a model equation used for a least-squares estimator.

<!-- chunk {"id": "body-0024", "role": "body", "section": "Least-Squares", "weight": 1.0} -->

We assume access to samples of subsequent moments $$\op{E}_i(Z_i) \dfn \sum_{j,\ell=1}^{n_w} \left(w_{i, j} w_{i,\ell}\right) [A_j, B_j] Z_i \trans{[A_\ell, B_\ell]}.$$ Such data can be generated by taking some $z_i$ and evaluating $x_{i+}$ with [eq:dyn]. Then let $Z_i = z_i \trans{z}_i$ and $Z_{i+} = \pi(x_{i+} \trans{x_{i+}})$. We give a detailed data-generation procedure in sec:data-generation.

<!-- chunk {"id": "body-0025", "role": "body", "section": "Least-Squares", "weight": 1.0} -->

$\op{Q}_\pi$ such that $\op{Q}_{\pi}(Z) = (\op{F}_\pi \op{Q}_{\pi})(Z)$ for all $Z \in \psd{n_z}$. which we can use to construct a model equation: Using the parametrization $\op{Q}_{\pi}(Z) = \tr[\Theta_\pi Z]$ results: \tr[\Theta_\pi Z_i] &= \tr[Z_i H] + \tr[\Theta_\pi Z_{i+}] \nonumber\\which is linear in the parameter $\Theta_\pi$ with zero-mean error. Note that [eq:model-equation] involves a temporal differences as in [Bradtke1996].

<!-- chunk {"id": "body-0026", "role": "body", "section": "Least-Squares", "weight": 1.0} -->

We reframe the model using the symmetric $\svec \colon \sym{n} \mapsto \Re^{\sd{n}}$ with $\sd{n} \dfn n(n+1)/2$ (cf. [Coppens2022]), which satisfies $\tr[X Y] = \trans{\svec{(X)}} \svec{(Y)}$. Its inverse is denoted as $\unsvec$. with $\theta_\pi = \svec(\Theta_\pi)$, $b_i = \tr[H Z_i]$, $a_i = \svec(Z_i - Z_{i+})$ and $e_i = \svec(Z_{i+} - \pi(\op{E}(Z_{i})))$. This is known as the error-in-variables setting.

<!-- chunk {"id": "body-0027", "role": "body", "section": "Least-Squares", "weight": 1.0} -->

The challenge is that both $a_i$ and $e_i$ linearly depend on $w_i \trans{w_i}$ through $Z_{i+} = \pi(\op{E}_i(Z_i))$. Hence $\E[a_i \trans{e}_i] \neq 0$, which makes a classical least-squares estimate inconsistent.

<!-- chunk {"id": "body-0028", "role": "body", "section": "Least-Squares", "weight": 1.0} -->

This is the classical motivation for instrumental variables (IVs) [Young2011]. We use $g_i \dfn \svec(Z_i)$ as IVs similarly to [Bradtke1996]. This choice is independent of the error $e_i$ (i.e. $\E[g_i \trans{e_i}] = 0$), yet is correlated with $a_i + e_i$ as desired of an IV. Intuitively, $g_i$ can be viewed as its best estimate without any additional information on the dynamics $\op{E}$. We further motivate the choice by linking it to a projected Bellman equation in app:ekf.

<!-- chunk {"id": "body-0029", "role": "body", "section": "Learning Control Schemes", "weight": 1.0} -->

We provide an overview of learning control schemes for the dynamics eq:dyn. To enable consistent comparisons we first describe a general scheme for gathering data. Then we describe our new policy iteration algorithm. Next we briefly summarize the system identification procedure of [Coppens2022] and the policy gradient scheme of [Gravell2021]. Sample complexity guarantees are reported whenever they exist.

<!-- chunk {"id": "body-0030", "role": "body", "section": "Data-generation", "weight": 1.0} -->

We describe the data generation process. To enable comparison of the presented algorithms we view them as all iteratively updating the policy, where $M$ trajectories (or rollouts) of length $T$ for a total of $N = MT$ new data points satisfying [eq:def-et] are used each iteration.

<!-- chunk {"id": "body-0031", "role": "body", "section": "Data-generation", "weight": 1.0} -->

The controller perturbation $U^{j}$ is sampled at the start of a trajectory and $\nu_k^{j}$ at each time step. Moreover $U^j$ is distributed over a sphere, instead of a ball, since in policy gradient, it is used to estimate the gradient of the infinite horizon cost through finite differences as explained in Alg.[alg:pg] later. We sample $\nu^j_k$from a ball to avoid over-excitation of the system, while keeping the trajectories informative enough.

<!-- chunk {"id": "body-0032", "role": "body", "section": "Data-generation", "weight": 1.0} -->

We depict the procedure in Since only states and inputs are gathered, the functional form of the dynamics is not required. Only a simulator or experiments are required.

<!-- chunk {"id": "body-0033", "role": "body", "section": "Data-generation", "weight": 1.0} -->

hobby,decorations.pathreplacing,arrows.meta show curve controls/.style=decoration=show path construction, curveto code=[blue, -Circle[black,open]]; [blue, Circle[black,open]-] decorate, confidence=None created_by=None text='\\begin{tikzpicture}\n \\begin{axis}[\n xmin=0, xmax=12,\n ymin=-2.5, ymax=2.5,\n axis x line=bottom,\n axis y line=none,\n height=0.4\\columnwidth,\n width=\\columnwidth,\n xtick={2.0, 6.0, 10.0},\n xticklabels={iteration $0$, iteration $1$, iteration $2$},\n]\n\n % first epoch\n \\draw [use Hobby shortcut] \n ([out angle=20, in angle=180]0.0, 0.4)..

<!-- chunk {"id": "body-0034", "role": "body", "section": "Data-generation", "weight": 1.0} -->

\n (1.0, 1.0).. \n (2.0, 1.5).. \n (3.0, 1.2).. \n (4.0, 2.0);\n \n \\node (v1) at (2.0, 1.5) [circle, fill=red, draw=red, inner sep=0.03cm, node contents={}, label={[label distance=-0.15cm]above right:\\footnotesize$x_i$}];\n \\node (v2) at (3.0, 1.2) [circle, fill=red, draw=red, inner sep=0.03cm, node contents={}, label={[label distance=-0.15cm]below right:\\footnotesize$x_{i+}$}];\n\n \\draw [use Hobby shortcut] \n ([out angle=-20, in angle=200]0.0, 0.0).. \n (1.0, 0.0)..

<!-- chunk {"id": "body-0035", "role": "body", "section": "Data-generation", "weight": 1.0} -->

\n (12.0, -1.1);\n \n \\draw [dashed] (4.0, -2.5) -- (4.0, 2.5);\n \\draw [dashed] (8.0, -2.5) -- (8.0, 2.5);\n\n \\end{axis}\n\n\\end{tikzpicture}' language=<CodeLanguageLabel.TIKZ: 'Tikz'> Rollouts used for data-generation.

<!-- chunk {"id": "body-0036", "role": "body", "section": "Data-generation", "weight": 1.0} -->

Each trajectory has to be initialized at the start of a new controller iteration. We can either continue trajectories from the previous iteration (henceforth referred to as we sample $\{x_0^{j}\}_{j=1}^{M}$ uniformly from $\{x \colon \nrm{x}_2 \leq r_x\}$.

<!-- chunk {"id": "body-0037", "role": "body", "section": "Data-generation", "weight": 1.0} -->

We estimate the moments $X_{k}^{j}$ and $Z_{k}^{j}$ for each (augmented) state vector by taking an outer product. When the specific trajectory does not affect the identification procedure (as in policy iteration and system identification) we write $(Z_i, X_{i+})$ to index the pairs $(Z_{k}^{j}, X_{k+1}^{j})$, for $k$ and $j$ varying within their range. These pairs all satisfy eq:def-et.

<!-- chunk {"id": "body-0038", "role": "body", "section": "Policy Iteration (PI)", "weight": 1.0} -->

Based on the discussion in the previous section we can now state the full approximate policy iteration algorithm.

<!-- chunk {"id": "body-0039", "role": "body", "section": "Policy Iteration (PI)", "weight": 1.0} -->

Generate pairrefers to the rollouts described in the previous section.

<!-- chunk {"id": "body-0040", "role": "body", "section": "Policy Iteration (PI)", "weight": 1.0} -->

Note how we use the confidence at the end of the previous policy iteration to initialize the next. This on a high-level corresponds to keeping a summary of the data from past policies and is contrasted by [Bradtke1994], where $S_{\pi_k, 0}$ in eq:recursive-ivs is reset to $\beta_0 I$ at the start of each policy iteration. Our approach enables the scheme to keep improving its estimate of the Q-function as is confirmed in the numerical experiments. To theoretical back this decision we provide an alternative interpretation as an Extended Kalman Filter [Bertsekas2016] applied to a projected Bellman equation in app:ekf

<!-- chunk {"id": "body-0041", "role": "body", "section": "System Identification (SI)", "weight": 1.0} -->

The data generated for the policy iteration scheme in the previous section can also be used to identify the dynamics. We have the following model equation for $i=1, \dots, N$: with $\op{E}_i$ as in eq:def-et. The model equation is linear in the matrix representing the linear map $\op{E}$ and has a zero-mean error. Hence we can estimate $\op{E}$ using least-squares as in [Coppens2022]. The resulting least-squares problem has $N \sd{n_x}$ equations and $\sd{n_z}\sd{n_x}$ parameters describing the matrix of the linear map $\op{E} \colon \sym{n_z} \to \sym{n_x}$. The advantage of this scheme is that prior knowledge about the dynamics, like the mode matrices $A_i$ and $B_i$, can be included to reduce the problem complexity. In this case we estimate $\E[w \trans{w}]$ instead of $\op{E}$.

<!-- chunk {"id": "body-0042", "role": "body", "section": "System Identification (SI)", "weight": 1.0} -->

Given the dynamics, the optimal controller can be computed by solving a semi-definite program [Coppens2022]. In the experiments below we do this once per iteration, where the least-square estimate is updated recursively using [Bertsekas2016].

<!-- chunk {"id": "body-0043", "role": "body", "section": "System Identification (SI)", "weight": 1.0} -->

Theoretical guarantees are provided in [Coppens2022], which states The theoretical guarantees only hold for trajectories of length one or when only the final transition of each trajectory is used. The rate was verified empirically for more sub-optimality $\epsilon$ the required number of samples is of order $1/\epsilon$.

<!-- chunk {"id": "body-0044", "role": "body", "section": "Policy Gradient (PG)", "weight": 1.0} -->

We summarize the model-free policy gradient scheme described in [Gravell2021]. Given some $\eta$ and initial guess $K_0$ we can compute the optimal controller directly via natural gradient descent: $$K_{k+1} = K_{k} - \eta \nabla \widehat{J(K)} \Sigma_K,$$ where the gradient and $\Sigma_K \dfn \sum_{t=0}^{\infty} X_t$ with $X_t$ the closed-loop trajectory with gain $K$is computed in data-driven fashion using the following algorithm: Gain matrix $K$, number of rollouts $M$, rollout length $T$ and exploration radius $r_U$. Generate $\{Z^{j}_t\}$ for $j = 1, \dots M$, $k = 1, \dots, T$ with policy [eq:pie] for $r_\nu = 0$, $r_U$ and $K$ as provided.

<!-- chunk {"id": "body-0045", "role": "body", "section": "Policy Gradient (PG)", "weight": 1.0} -->

Note that this algorithm requires on-policy exploration. Moreover multiple rollouts should be generated to get a suitable estimate of $\widehat{J}_j$in each iteration. So policy gradient restricts data-generation more than the Theoretical guarantees for classical gradient (i.e. using are available in [Gravell2021]. Given some desired accuracy $\epsilon$, one should select $M = \mathcal{O}(1/\epsilon^2)$, $T = \mathcal{O}(1/\epsilon^2)$ and $r_U = \mathcal{O}(\epsilon)$ in the gradient evaluation step. The gradient descent scheme will then converge at a linear rate to some $K$ such that the sub-optimality is bounded by $\epsilon$. Hence the total sample complexity is of order $1/\epsilon^4$. In later experiments we illustrate a case with $1/\epsilon$sample complexity. The stated rates are however asymptotic and for classical gradient descent. So the observed gap could disappear for larger sample counts or is caused by natural gradient descent outperforming classical gradient descent. Further analysis would thus be interesting.

<!-- chunk {"id": "body-0046", "role": "body", "section": "Numerical Experiments", "weight": 1.0} -->

We will evaluate the presented methods on a dynamical system with multiplicative noise as in eq:dyn and modes \end{bmatrix}, \, B_1 = \begin{bmatrix} \end{bmatrix} \, A_2 = \begin{bmatrix} with $v_t$ sampled uniformly from an ellipsoid such that $\E[v_t \trans{v}_t] = \diag(0.2, 0.5)$. The dynamics were motivated by a control problem of the pitch of a satellite (cf. [Damm2003]), which was discretized using a trapezoid method [Schurz1999].

<!-- chunk {"id": "body-0047", "role": "body", "section": "Numerical Experiments", "weight": 1.0} -->

We begin with a setup that works best for PI and compare it to SI. Next we compare PG, PI and SI when data is generated as prescribed by Alg. [alg:pg]. Afterwards PI is evaluated in an on-policy setting and finally we examine the effect of the tuning parameter $\beta_0$on PI.

<!-- chunk {"id": "body-0048", "role": "body", "section": "Off-policy PI", "weight": 1.0} -->

First we investigate the effect of the number of rollouts on the performance of our policy iteration scheme. Following the notation of sec:data-generation, take the additive noise radius $r_\nu = 0.1$ and no controller perturbation (i.e. $r_U = 0$). Each policy update uses $M = 30$ trajectories of length $T = 100$ are generated,starting from states distributed with $r_x = 1$.

<!-- chunk {"id": "body-0049", "role": "body", "section": "Off-policy PI", "weight": 1.0} -->

A fixed, stabilizing control gain is used to generate the samples. When data is generated using an unstable controller, PI and PG would fail to converge. Both schemes would also encounter numerical issues. These can be reduced by using more rollouts with a reduced horizon. Further discussion on the effect of stability on PI specifically due to unstable controllers being generated by the algorithm is provided at the end of this section. unless mentioned otherwise. The optimal controller for this initial Q-function equals $K_0$and is thus stabilizing. Note that SI requires no initial guess, which can be considered an advantage. $5000$ iterations and repeat the whole process $25$ times to evaluate variances. fig:add depicts the comparison between SI and PI. For each control gain $K$ and associated $\pi$ we solve the Lyapunov equation eq:lyap-solve for the true $\op{E}$ to find value function $J_\pi$. We then compare $J_\pi(I)$ to the optimal $J_\star(I)$ from eq:lqrsm.

<!-- chunk {"id": "body-0050", "role": "body", "section": "Off-policy PI", "weight": 1.0} -->

This is equivalent to comparing the trace of the associated hessians or the expected infinite closed-loop horizon cost starting from a random $x_0$ with $\E[x_0 \trans{x_0}] = I$. The top plots depict the relative error. The bottom plots show $\nrm{K - K_\star}_2 / \nrm{K_\star}_2$, i.e. the relative spectral norm error with the optimal gain.

<!-- chunk {"id": "body-0051", "role": "body", "section": "Off-policy PI", "weight": 1.0} -->

Observe how the suboptimality acts like $1/N$ with $N$ the number of samples, while the controller error acts like $1/\sqrt{N}$ for both PI and SI (the dashed lines follow these rates exactly). This corresponds to the rates predicted in [Coppens2022].

<!-- chunk {"id": "body-0052", "role": "body", "section": "Off-policy PI", "weight": 1.0} -->

For future experiments we will depict the suboptimality only. The which decreases at $1/\sqrt{N}$ for all experiments whenever the suboptimality decreases at $1/N$ is omitted hereafter.

<!-- chunk {"id": "body-0053", "role": "body", "section": "Off-policy PI", "weight": 1.0} -->

(1,0.35964357)\dimexpr\f@size pt\relax1\dimexpr\f@size pt\relax \dimexpr\f@size pt\relax1.25\dimexpr\f@size pt\relax \dimexpr\f@size pt\relax1.25\dimexpr\f@size pt\relax \dimexpr\f@size pt\relax1.25\dimexpr\f@size pt\relax \dimexpr\f@size pt\relax1.25\dimexpr\f@size pt\relax \dimexpr\f@size pt\relax1.25\dimexpr\f@size pt\relax \dimexpr\f@size pt\relax1.25\dimexpr\f@size pt\relax \dimexpr\f@size pt\relax1.25\dimexpr\f@size pt\relax \dimexpr\f@size pt\relax1.25\dimexpr\f@size pt\relax [t]@size pt1.25@size pt]crel.

<!-- chunk {"id": "body-0054", "role": "body", "section": "Off-policy PI", "weight": 1.0} -->

suboptimality \dimexpr\f@size pt\relax1.25\dimexpr\f@size pt\relax \dimexpr\f@size pt\relax1.25\dimexpr\f@size pt\relax \dimexpr\f@size pt\relax1.25\dimexpr\f@size pt\relax \dimexpr\f@size pt\relax1.25\dimexpr\f@size pt\relax \dimexpr\f@size pt\relax1.25\dimexpr\f@size pt\relax \dimexpr\f@size pt\relax1.25\dimexpr\f@size pt\relax [t]@size pt1.25@size pt]crel.

<!-- chunk {"id": "body-0055", "role": "body", "section": "Off-policy PI", "weight": 1.0} -->

gain error \dimexpr\f@size pt\relax1.25\dimexpr\f@size pt\relax \dimexpr\f@size pt\relax1.25\dimexpr\f@size pt\relax \dimexpr\f@size pt\relax1.25\dimexpr\f@size pt\relax Suboptimality and controller error for off-policy SI and PI with additive exploration noise and $M = 30$. The colored area depicts a $80\%$ two-sided empirical confidence interval.

<!-- chunk {"id": "body-0056", "role": "body", "section": "Evaluation of PG", "weight": 1.0} -->

Next we consider natural PG. We tune the data-generation such that PG performs well and then pass the data to SI and PI to compare. Here $r_\nu = 0$ and $r_U = 0.15$ produced good results for PG. As before we take $M = 3000$ and $T = 100$. We initialize PG with $K_0 = [0.5\,-0.75]$ and use the PG gain in later iterations as described in Alg.[alg:pg]. The step size is set to $7.5\cdot 10^{-3}$. We initialize PI with $\beta_0 = 5.0$. This change compensates for the absence of additive noise, which makes the data less informative. It corresponds to more trust in the initial guess to avoid generating unstable controllers, which causes PI to diverge. Another experiment below expands on this intuition. We continue for $250$ iterations. The rest of the procedure is identical to before and the result is depicted in fig:pg-compare.

<!-- chunk {"id": "body-0057", "role": "body", "section": "Evaluation of PG", "weight": 1.0} -->

(1,0.36168467)\dimexpr\f@size pt\relax1\dimexpr\f@size pt\relax \dimexpr\f@size pt\relax1.25\dimexpr\f@size pt\relax \dimexpr\f@size pt\relax1.25\dimexpr\f@size pt\relax \dimexpr\f@size pt\relax1.25\dimexpr\f@size pt\relax \dimexpr\f@size pt\relax1.25\dimexpr\f@size pt\relax \dimexpr\f@size pt\relax1.25\dimexpr\f@size pt\relax \dimexpr\f@size pt\relax1.25\dimexpr\f@size pt\relax \dimexpr\f@size pt\relax1.25\dimexpr\f@size pt\relax [t]@size pt1.25@size pt]crel.

<!-- chunk {"id": "body-0058", "role": "body", "section": "Evaluation of PG", "weight": 1.0} -->

suboptimality \dimexpr\f@size pt\relax1.25\dimexpr\f@size pt\relax \dimexpr\f@size pt\relax1.25\dimexpr\f@size pt\relax \dimexpr\f@size pt\relax1.25\dimexpr\f@size pt\relax Median relative suboptimality SI, PI and PG.

<!-- chunk {"id": "body-0059", "role": "body", "section": "Evaluation of PG", "weight": 1.0} -->

Note how SI and PI act similarly to before, while PG stagnates after a certain number of iterations. This is also predicted by the theory in [Gravell2021]. We can evaluate the sample complexity by repeating the same experiment, but with $M = 300$, $3000$ and $30\,000$. We plot the number of iterations on the horizontal axis to ease visual comparison, keeping in mind that the number of samples observed per iteration differs. The result in fig:pg-samples indicates that the suboptimality improves with $1/M$. So overall the rate is the same as SI and PI, but it manifests in terms of the number of rollouts per gradient evaluation, instead of the cumulative sample count.

<!-- chunk {"id": "body-0060", "role": "body", "section": "Evaluation of PG", "weight": 1.0} -->

Moreover, while SI and PI put no requirements on data generation, (1,0.35495612)\dimexpr\f@size pt\relax1\dimexpr\f@size pt\relax \dimexpr\f@size pt\relax1.25\dimexpr\f@size pt\relax \dimexpr\f@size pt\relax1.25\dimexpr\f@size pt\relax \dimexpr\f@size pt\relax1.25\dimexpr\f@size pt\relax \dimexpr\f@size pt\relax1.25\dimexpr\f@size pt\relax \dimexpr\f@size pt\relax1.25\dimexpr\f@size pt\relax \dimexpr\f@size pt\relax1.25\dimexpr\f@size pt\relax \dimexpr\f@size pt\relax1.25\dimexpr\f@size pt\relax \dimexpr\f@size pt\relax1.25\dimexpr\f@size pt\relax [t]@size

<!-- chunk {"id": "body-0061", "role": "body", "section": "Evaluation of PG", "weight": 1.0} -->

suboptimality \dimexpr\f@size pt\relax1.25\dimexpr\f@size pt\relax \dimexpr\f@size pt\relax1.25\dimexpr\f@size pt\relax \dimexpr\f@size pt\relax1.25\dimexpr\f@size pt\relax Evaluation of sample complexity of PG. Plots show median relative suboptimality.

<!-- chunk {"id": "body-0062", "role": "body", "section": "On-policy PI", "weight": 1.0} -->

We can run PI in an on-policy setting with one rollout each iteration. Taking $T=100$, $M=1$ and $x_0$ distributed with $r_x = 1$, while using the final state of the latest iteration afterwards (c.f. continuous mode in sec:data-generation). We initialize PI with $\beta_0 = 100$ and run the scheme for $1000$ iterations. The rest of the setup is identical to the first experiment, but now instead of applying $K_0$ for every iteration, the latest PI control gain is used instead. The result, manifesting the same sample complexity as before, is depicted in fig:on-policy. Interestingly the suboptimality is reduced compared to fig:add, potentially indicating that this method of data-generation is more informative.

<!-- chunk {"id": "body-0063", "role": "body", "section": "On-policy PI", "weight": 1.0} -->

(1,0.35822874)\dimexpr\f@size pt\relax1\dimexpr\f@size pt\relax \dimexpr\f@size pt\relax1.25\dimexpr\f@size pt\relax \dimexpr\f@size pt\relax1.25\dimexpr\f@size pt\relax \dimexpr\f@size pt\relax1.25\dimexpr\f@size pt\relax \dimexpr\f@size pt\relax1.25\dimexpr\f@size pt\relax \dimexpr\f@size pt\relax1.25\dimexpr\f@size pt\relax \dimexpr\f@size pt\relax1.25\dimexpr\f@size pt\relax \dimexpr\f@size pt\relax1.25\dimexpr\f@size pt\relax \dimexpr\f@size pt\relax1.25\dimexpr\f@size pt\relax \dimexpr\f@size

<!-- chunk {"id": "body-0064", "role": "body", "section": "On-policy PI", "weight": 1.0} -->

pt\relax1.25\dimexpr\f@size pt\relax [t]@size pt1.25@size pt]crel.

<!-- chunk {"id": "body-0065", "role": "body", "section": "On-policy PI", "weight": 1.0} -->

suboptimality \dimexpr\f@size pt\relax1.25\dimexpr\f@size pt\relax \dimexpr\f@size pt\relax1.25\dimexpr\f@size pt\relax The colored area depicts a $80\%$ two-sided empirical confidence interval.

<!-- chunk {"id": "body-0066", "role": "body", "section": "Tuning of PI", "weight": 1.0} -->

When a small number of samples are provided per iteration in PI, unstable control gains can be generated. This can cause the algorithm to diverge.

<!-- chunk {"id": "body-0067", "role": "body", "section": "Tuning of PI", "weight": 1.0} -->

See, which proves convergence of PI over the class of stable policies and illustrates what happens when an unstable policy is used instead.

<!-- chunk {"id": "body-0068", "role": "body", "section": "Tuning of PI", "weight": 1.0} -->

To examine the effect of tuning we set $T = 10$ and $M = 5$ and run the algorithm $1000$ times for $100$ iterations. The remainder of the setup is the same as the first experiment of this section. The data-generation uses the same stabilizing policy $K_0 = [0.5 \, -0.75]$for each iteration.

<!-- chunk {"id": "body-0069", "role": "body", "section": "Tuning of PI", "weight": 1.0} -->

The percentage of unstable policies per iteration is depicted in fig:pi-fail. Note how unstable policies are produced in the first iterations due to the small amount of data and mostly remain unstable afterwards. Low values for $\beta_0$ reduces the number of unstable policies since the algorithm trusts the initial guess more. For $\beta_0 = 0.1$no unstable policies occur. Alternatively, performing system identification separately from control synthesis does not encounter stability issues and requires no tuning.

<!-- chunk {"id": "body-0070", "role": "body", "section": "Tuning of PI", "weight": 1.0} -->

(1,0.36926667)\dimexpr\f@size pt\relax1\dimexpr\f@size pt\relax \dimexpr\f@size pt\relax1.25\dimexpr\f@size pt\relax \dimexpr\f@size pt\relax1.25\dimexpr\f@size pt\relax \dimexpr\f@size pt\relax1.25\dimexpr\f@size pt\relax \dimexpr\f@size pt\relax1.25\dimexpr\f@size pt\relax \dimexpr\f@size pt\relax1.25\dimexpr\f@size pt\relax \dimexpr\f@size pt\relax1.25\dimexpr\f@size pt\relax \dimexpr\f@size pt\relax1.25\dimexpr\f@size pt\relax \dimexpr\f@size pt\relax1.25\dimexpr\f@size pt\relax \dimexpr\f@size

<!-- chunk {"id": "body-0071", "role": "body", "section": "Tuning of PI", "weight": 1.0} -->

pt\relax1.25\dimexpr\f@size pt\relax \dimexpr\f@size pt\relax1.25\dimexpr\f@size pt\relax \dimexpr\f@size pt\relax1.25\dimexpr\f@size pt\relax \dimexpr\f@size pt\relax1.25\dimexpr\f@size pt\relax [t]@size pt1.25@size pt]cunstable \dimexpr\f@size pt\relax1.25\dimexpr\f@size pt\relax \dimexpr\f@size pt\relax1.25\dimexpr\f@size pt\relax \dimexpr\f@size pt\relax1.25\dimexpr\f@size pt\relax \dimexpr\f@size pt\relax1.25\dimexpr\f@size pt\relax Percentage of unstable policies produced by PI for different tunings.

<!-- chunk {"id": "body-0072", "role": "body", "section": "Conclusion", "weight": 1.5} -->

From the experiments in the previous section one can conclude a pay-off between a simple implementation and robustness. The policy gradient scheme requires the most effort to tune and requires the most specific data, yet is simple to implement. Meanwhile the model-based approach requires solving a large least-squares problem and a generalized algebraic Riccati equation usually formulated as a SDP. However it requires no tuning and can handle almost all data-generation schemes. The presented policy iteration scheme meanwhile also solves a smaller least-squares problem, yet avoids the Riccati equation. However as shown in fig:pi-fail, with limited data the scheme can require some tuning to work.

<!-- chunk {"id": "body-0073", "role": "body", "section": "Conclusion", "weight": 1.5} -->

In future work we will investigate adaptive iteration lengths to avoid such tuning issues. After all, problems often occur in the first iterations. Hence gathering more data there would aid in stabilizing the algorithm. The connection with EKF in app:ekfwill also be exploited further to find stability and convergence guarantees. Such a theoretical analysis would also aid in improving tuning.

<!-- chunk {"id": "body-0074", "role": "body", "section": "Conclusion", "weight": 1.5} -->

We thank Jean-Louis Carron for performing an initial comparison of learning control schemes for multiplicative noise during their master thesis, motivating the developments presented here.

<!-- chunk {"id": "body-0075", "role": "body", "section": "EKF Interpretation", "weight": 1.0} -->

*Introduction to Extended Kalman Filters: Classically an EKF is applied to a nonlinear least-squares problem: $$\minimize_{\theta} \quad \frac{1}{2} \nrm{g(\theta)}_2^2 = \frac{1}{2} \sum_{i=1}^{N} \nrm{f_i(\theta)}_2^2.$$ It linearizes $f_i(\theta)$ around recursive estimates of the minimizer $\theta_k$, denoted as $\tilde{f}_i(\theta | \theta_k) \dfn f_i(\theta_k) + \trans{\nabla f_i(\theta_k)} (\theta - \theta_k)$.

<!-- chunk {"id": "body-0076", "role": "body", "section": "EKF Interpretation", "weight": 1.0} -->

\tilde{h}_i(\hat{\theta}_k \mid \theta_{\ell-1})}_2^2.$$ Instead of linearizing each time step however we split the data up into batches and linearize at the start of each batch. Next, this reasoning is applied to our setting.

<!-- chunk {"id": "body-0077", "role": "body", "section": "EKF Interpretation", "weight": 1.0} -->

This corresponds to the normal equation of least-squares with IVs, hence motivating their use in sec:ls. We can use the recursion eq:recursive-ivsto generate solutions iteratively without computing inverses.

<!-- chunk {"id": "body-0078", "role": "body", "section": "EKF Interpretation", "weight": 1.0} -->

eq:ivs-deriv-1 we can show that eq:single-stage-ivs $$S_{\pi_k, i}^{-1} (\hat{\theta}_{\pi_k} - \hat{\theta}_{\pi_k, i}) = 0.$$ So we can equivalently process the next terms in eq:projected-equation-ls by adding the left-hand side of eq:regularization-final as a regularization term. As such we have derived the recursion in eq:recursive-ivs.
