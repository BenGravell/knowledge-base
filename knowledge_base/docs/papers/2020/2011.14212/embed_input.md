<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Approximate Midpoint Policy Iteration for Linear Quadratic Control

Topics include Policy iteration, Dynamic programming, Approximate dynamic programming, Reinforcement learning, Newton's method, Midpoint method, Linear systems, Linear quadratic regulator, Control, Least squares, Temporal difference learning.

<!-- chunk {"id": "summary-0002", "role": "summary", "section": "Summary", "weight": 2.0} -->

By viewing policy iteration as Newton's method for solving MDPs and extending the analogy to the midpoint method, the work shows that policies can be solved for more efficiently, both in the model-known and model-unknown settings.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

We present a midpoint policy iteration algorithm to solve linear quadratic optimal control problems in both model-based and model-free settings. The algorithm is a variation of Newton's method, and we show that in the model-based setting it achieves cubic convergence, which is superior to standard policy iteration and policy gradient algorithms that achieve quadratic and linear convergence, respectively. We also demonstrate that the algorithm can be approximately implemented without knowledge of the dynamics model by using least-squares estimates of the state-action value function from trajectory data, from which policy improvements can be obtained. With sufficient trajectory data, the policy iterates converge cubically to approximately optimal policies, and this occurs with the same available sample budget as the approximate standard policy iteration. Numerical experiments demonstrate effectiveness of the proposed algorithms.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

With the recent confluence of reinforcement learning and data-driven optimal control, there is renewed interest in fully understanding convergence, sample complexity, and robustness in both "model-based" and "model-free" algorithms. Linear quadratic problems in continuous spaces provide benchmarks where strong theoretical statements can be made. In practice, it is often difficult or impossible to develop a model of a system from first-principles. In this case, one may use so-called "model-based" system identification methods which attempt to estimate a model of the dynamics from observed sample data, then solve the Riccati equation using the identified system matrices. An approximately optimal control policy is then computed assuming certainty-equivalence \[Mania et al.Mania, Tu, and Recht, Oymak and Ozay, Coppens and Patrinos\] or using robust control approaches to explicitly account for model uncertainty \[Dean et al.Dean, Mania, Matni, Recht, and Tu, Dean et al.Dean, Mania, Matni, Recht, and Tu, Gravell and Summers, Coppens et al.Coppens, Schuurmans, and Patrinos\].

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

The analyses in these recent works has focused on providing finite-sample performance/suboptimality guarantees.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

As an alternative, so-called "model-free" methods may also be used, which do not attempt to learn a model of the dynamics. The category of policy optimization methods which directly attempt to optimize the control policy, including policy gradient, has received significant attention recently for standard LQR \[Fazel et al.Fazel, Ge, Kakade, and Mesbahi, Bu et al.Bu, Mesbahi, and Mesbahi\], multiplicative-noise LQR \[Gravell et al.Gravell, Esfahani, and Summers\], Markov jump LQR \[Jansch-Porto et al.Jansch-Porto, Hu, and Dullerud\], and LQ games related to $\mathcal{H}_{\infty}$ robust control \[Zhang et al.Zhang, Yang, and Basar, Bu et al.Bu, Ratliff, and Mesbahi\].

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

Between the fully model-based system identification approaches and the fully model-free policy optimization approaches lies another category of methods, which we denote as value function approximation methods. These methods attempt to estimate value functions then compute policies which are optimal with respect to these value functions. This class of methods includes approximate dynamic programming, exemplified by approximate value iteration, which estimates state-value functions, and approximate policy iteration, which estimates state-action value functions. In particular, for LQR problems, approximate policy iteration was studied by \[Bradtke et al.Bradtke, Ydstie, and Barto, Krauth et al.Krauth, Tu, and Recht\] and by \[Fazel et al.Fazel, Ge, Kakade, and Mesbahi, Bu et al.Bu, Mesbahi, and Mesbahi\] under the guise of a quasi-Newton method.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Introduction", "weight": 1.5} -->

For LQ games, approximate policy iteration was studied by \[Al-Tamimi et al.Al-Tamimi, Lewis, and Abu-Khalaf\] under the guise of Q-learning, and by \[Luo et al.Luo, Yang, and Liu, Gravell et al.Gravell, Ganapathy, and Summers\]. Note that approximate policy iteration is sometimes called quasi-Newton or Q-learning.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Introduction", "weight": 1.5} -->

In stochastic optimal control, the functional Bellman equation gives a sufficient and necessary condition for optimality of a control policy (\[Bellman\]). It has been long-known, but perhaps underappreciated, that application of Newton's method to find the root of the functional Bellman equation in stochastic optimal control is equivalent to the dynamic programming algorithm of policy iteration (\[Puterman and Brumelle, Madani\]). In this most general setting, conditions for and rates of convergence are available (\[Puterman and Brumelle, Madani\]), but may be difficult or impossible to verify in practice. Furthermore, even representing the value functions and policies and executing the policy iteration updates may be intractable. This motivates the basic approximation of such problems by linear dynamics and quadratic costs over finite-dimensional, infinite-cardinality state and action spaces.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Introduction", "weight": 1.5} -->

In linear-quadratic problems, the Bellman equation becomes a matrix algebraic Riccati equation, and application of the Newton method to the Riccati equation yields the well-known Kleinman-Hewer algorithm.^11^1\[Kleinman\] introduced this for continuous-time systems, and \[Hewer\] studied it for discrete-time systems. The Newton method has many variations devised to improve the convergence rate and information efficiency, including higher-order methods (such as Halley (\[Cuyt and Rall\]), super-Halley (\[Gutiérrez and Hernández\]), and Chebyshev (\[Argyros and Chen\])), and multi-point methods (\[Traub\]), which compute derivatives at multiple points and of which the midpoint method is the simplest member. Some of these have been applied to solving Riccati equations by \[Anderson, Guo and Laub, Damm and Hinrichsen, Freiling and Hochhaus, Hernández-Verón and Romero\], but without consideration of the situation when the dynamics are not perfectly known.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Introduction", "weight": 1.5} -->

We present a midpoint policy iteration algorithm to solve linear quadratic optimal control problems when the dynamics are both known (Algorithm 1) and unknown (Algorithm 4).

<!-- chunk {"id": "body-0012", "role": "body", "section": "Introduction", "weight": 1.5} -->

We demonstrate that the method converges, and does so at a faster *cubic* rate than standard policy iteration or policy gradient, which converge at quadratic and linear rates, respectively.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Introduction", "weight": 1.5} -->

We show that approximate midpoint policy iteration converges faster in the model-free setting even with the same available sample budget as the approximate standard policy iteration.

<!-- chunk {"id": "body-0014", "role": "body", "section": "Introduction", "weight": 1.5} -->

We present numerical experiments that illustrate and demonstrate the effectiveness of the algorithms and provide an open-source implementation to facilitate their wider use.

<!-- chunk {"id": "body-0015", "role": "body", "section": "Derivatives of the Riccati operator", "weight": 1.0} -->

The first total derivative ^22^2In infinite dimensions, the first total derivative is called the *Fréchet* derivative, and the first directional derivative is called the *Gateaux* derivative. As we are only considering finite-dimensional systems, we do not need the full generality of these objects. of the Riccati operator evaluated at point $P \in {\mathbb{S}}^{n}$ is denoted as ${\mathcal{R}^{\prime}{(P)}} \in {{\mathbb{S}}^{n} \times {\mathbb{S}}^{n}}$. With a slight abuse of notation, the first directional derivative of the Riccati operator evaluated at point $P$ in direction $X$ is denoted as ${\mathcal{R}^{\prime}{(P,X)}} \in {\mathbb{S}}^{n}$. Computation of the first directional derivative is straightforward and follows e.g. the derivation given by \[Luo et al.Luo, Yang, and Liu\]. The general limit definition of this derivative is

<!-- chunk {"id": "body-0016", "role": "body", "section": "Derivatives of the Riccati operator", "weight": 1.0} -->

where we used the rule for a derivative of a matrix inverse e.g. as in \[Selby\]. Continuing with the first derivative,

<!-- chunk {"id": "body-0017", "role": "body", "section": "Derivatives of the Riccati operator", "weight": 1.0} -->

where we used the product rule for matrix derivatives.

<!-- chunk {"id": "body-0018", "role": "body", "section": "Identities", "weight": 1.0} -->

Considering two symmetric matrices $P,X$ and the related gains

<!-- chunk {"id": "body-0019", "role": "body", "section": "Identities", "weight": 1.0} -->

Thus the Riccati operator $\mathcal{R}{(P)}$ can be rewritten as

<!-- chunk {"id": "body-0020", "role": "body", "section": "Identities", "weight": 1.0} -->

and the derivative $\mathcal{R}^{\prime}{(X,P)}$ can be written using as

<!-- chunk {"id": "body-0021", "role": "body", "section": "Newton method", "weight": 1.0} -->

The Newton method, due originally in heavily modified form to \[Newton, Raphson\] and originally in the general differential form to \[Simpson\] (see the historical notes of \[Kollerstrom, Deuflhard\]), begins with an initial guess $x_{0}$ then proceeds with iterations

<!-- chunk {"id": "body-0022", "role": "body", "section": "Newton method", "weight": 1.0} -->

until convergence. Intuitively, the Newton method forms a linear approximation ${f{(x_{k})}} + {f^{\prime}{(x_{k})}{({x - x_{k}})}}$ to the function $f$ at $x_{k}$, and assigns the point where the linear approximation crosses $0$ as the next iterate. The Newton method can be derived from by using left rectangular integration.

<!-- chunk {"id": "body-0023", "role": "body", "section": "Newton method", "weight": 1.0} -->

The Newton update can be rearranged into the Newton equation

<!-- chunk {"id": "body-0024", "role": "body", "section": "Newton method", "weight": 1.0} -->

where the left-hand side is recognized as the *directional derivative* of $f$ evaluated at point $x_{k}$ in direction $x_{k + 1} - x_{k}$. This rearrangement implies that the Newton method *does not require explicit evaluation of the entire total derivative $f^{\prime}{(x_{k})}$* so long as a suitable direction $x_{k + 1} - x_{k}$ can be found which solves the Newton equation. This will become important in the LQR setting as we use this fact to avoid notating and computing large order-4 tensors.

<!-- chunk {"id": "body-0025", "role": "body", "section": "Newton method", "weight": 1.0} -->

This technique uses derivative information at a single point and is known to achieve quadratic convergence in a neighborhood of the root (\[Kantorovich\]). In the setting of both continuous- and discrete-time LQR, this algorithm is known to achieve quadratic convergence globally, as shown by \[Kleinman, Hewer, Bu et al.Bu, Mesbahi, and Mesbahi\].

<!-- chunk {"id": "body-0026", "role": "body", "section": "Mid-point Newton method", "weight": 1.0} -->

The midpoint Newton method, due originally to \[Traub\], begins with an initial guess $x_{0}$ then proceeds with iterations

<!-- chunk {"id": "body-0027", "role": "body", "section": "Mid-point Newton method", "weight": 1.0} -->

until convergence. The midpoint Newton method can be derived from by using midpoint rectangular integration. Intuitively, much like the Newton method, the midpoint Newton method forms a linear approximation ${f{(x_{k})}} + {f^{\prime}{(x_{k}^{M})}{({x - x_{k}})}}$ to the function $f$ at $x_{k}$, and assigns the point where the linear approximation crosses $0$ as the next iterate. The distinction is that the slope of the linear approximation is not evaluated at $x_{k}$ as in the Newton method, but rather at the midpoint $x_{k}^{M} = {\frac{1}{2}{({x_{k} + x_{k + 1}^{N}})}}$ where $x_{k + 1}^{N}$ is the Newton iterate.

<!-- chunk {"id": "body-0028", "role": "body", "section": "Mid-point Newton method", "weight": 1.0} -->

The updates can be rearranged into the Newton equations

<!-- chunk {"id": "body-0029", "role": "body", "section": "Mid-point Newton method", "weight": 1.0} -->

where the left-hand side of the first equation is recognized as the *directional derivative* of $f$ evaluated at point $x_{k}$ in direction $x_{k + 1}^{N} - x_{k}$; the second equation is of the same form. This rearrangement implies that the midpoint Newton method *does not require explicit evaluation of the entire total derivative $f^{\prime}{(x_{k})}$* so long as a suitable direction $x_{k + 1} - x_{k}$ can be found which solves the Newton equation. This will become important in the LQR setting as we use this fact to avoid notating and computing large order-4 tensors.

<!-- chunk {"id": "body-0030", "role": "body", "section": "Mid-point Newton method", "weight": 1.0} -->

Each iteration in this technique uses derivative information at two points, $x_{k}$ and $x_{k}^{M}$. This method has been shown to achieve cubic convergence in a neighborhood of the root by \[Nedzhibov, Homeier, Babajee and Dauhoo\].

<!-- chunk {"id": "body-0031", "role": "body", "section": "Exact midpoint policy iteration", "weight": 1.0} -->

We now consider application of the midpoint Newton method to the Riccati equation. Although could be brought to the vector form ${f{(x)}} = 0$ by vectorization with $x = {{svec}{(P)}}$ and ${f{(x)}} = {{svec}{({\mathcal{R}{({{smat}{(x)}})}})}}$, it will be simpler to leave the equations in matrix form, which is possible due to the special form of the Newton-type updates, which only involve directional derivatives (and not total derivatives). Applying the midpoint Newton update to yields

<!-- chunk {"id": "body-0032", "role": "body", "section": "Exact midpoint policy iteration", "weight": 1.0} -->

The updates can be rearranged into the Newton equations

<!-- chunk {"id": "body-0033", "role": "body", "section": "Exact midpoint policy iteration", "weight": 1.0} -->

and further by linearity of $\mathcal{R}^{\prime}{( \cdot,X)}$ in $X$ to

<!-- chunk {"id": "body-0034", "role": "body", "section": "Exact midpoint policy iteration", "weight": 1.0} -->

Recalling the expression for $\mathcal{R}^{\prime}$in for the left-hand sides and applying the identities in and to the right-hand sides, these become the Lyapunov equations

<!-- chunk {"id": "body-0035", "role": "body", "section": "Exact midpoint policy iteration", "weight": 1.0} -->

These updates are collected in the full midpoint policy iteration in Algorithm 1.

<!-- chunk {"id": "body-0036", "role": "body", "section": "Exact midpoint policy iteration", "weight": 1.0} -->

0: System matrices A, B, penalty matrix Q, initial stabilizing gain K0, tolerance ε
1: Initialize: k = 0, P−1 = ∞ In, and P0 = DLYAP (F,S) where F = A + B K0 and ${S = {\begin{bmatrix}
\end{bmatrix}Q\begin{bmatrix}
4: Compute FN = A + B Kk, and ${S^{N} = {\begin{bmatrix}
\end{bmatrix}Q\begin{bmatrix}
6: Compute $M_{k} = {\frac{1}{2}{({P_{k} + P_{k + 1}^{N}})}}$ and Lk = 𝒦 (Mk).
7: Compute FM = A + B Lk, and${S^{M} = {{{\begin{bmatrix}
\end{bmatrix}Q\begin{bmatrix}
Algorithm 1 Exact midpoint policy iteration (MPI)

<!-- chunk {"id": "body-0037", "role": "body", "section": "Approximate midpoint policy iteration", "weight": 1.0} -->

In the model-free setting we do not have access to the dynamics matrices $(A,B)$, so we cannot execute the updates in Algorithm 1. However, the gain $K = {\mathcal{K}{(P)}}$ can be computed solely from the state-action value matrix $H = {\mathcal{H}{(P)}}$ as $K = {- {H_{uu}^{- 1}H_{ux}}}$. Thus, if we can obtain accurate estimates of $H$, we can use the estimate of $H$ to compute $K$ and we need not perform any other updates that depend explicitly on $(A,B)$. We begin by summarizing an existing method in the literature for estimating state-action value functions from observed state-and-input trajectories.

<!-- chunk {"id": "body-0038", "role": "body", "section": "State-action value estimation", "weight": 1.0} -->

From this expression it is clear that a state-input trajectory, or "rollout," $\mathcal{D} = {\{ x_{t},u_{t}\}}_{t = 0}^{\ell}$ must satisfy this cost relationship, which can be used to estimate $H$. In particular, least-squares temporal difference learning for $\mathcal{Q}$-functions (LSTDQ) was originally introduced by \[Lagoudakis and Parr\] and analyzed by \[Abbasi-Yadkori et al.Abbasi-Yadkori, Lazic, and Szepesvári, Krauth et al.Krauth, Tu, and Recht\], and is known to be a consistent and unbiased estimator of $H$. Following the development of \[Krauth et al.Krauth, Tu, and Recht\], the LSTDQ estimator is summarized in Algorithm 2.

<!-- chunk {"id": "body-0039", "role": "body", "section": "State-action value estimation", "weight": 1.0} -->

We collect rollouts to feed into Algorithm 2 via Algorithm 3, i.e. by initializing the state with $x_{0}$ drawn from the given initial state distribution $\mathcal{X}_{0}$, then generating control inputs according to $u_{t} = {{K^{\text{play}}x_{t}} + u_{t}^{\text{explore}}}$ where $K^{\text{play}}$ is a stabilizing gain matrix, and $u_{t}^{\text{explore}}$ is an exploration noise drawn from a distribution $\mathcal{U}_{t}$, assumed Gaussian in this work, to ensure persistence of excitation.

<!-- chunk {"id": "body-0040", "role": "body", "section": "State-action value estimation", "weight": 1.0} -->

0: Gain Kplay, rollout length ℓ, initial state distribution 𝒳0, exploration distributions {𝒰t}t = 0ℓ.
3: Sample exploratory control input utexplore ∼ 𝒰t and disturbance wt ∼ W
4: Generate control input ut = Kplay xt + utexplore
5: Record state xt and input ut
6: Update state according to xt + 1 = A xt + B ut + wt
Algorithm 3 ROLLOUT: Rollout collection

<!-- chunk {"id": "body-0041", "role": "body", "section": "State-action value estimation", "weight": 1.0} -->

Note that LSTDQ is an off-policy method, and thus the gain $K^{\text{play}}$ used to generate the data in Algorithm 3 and the gain $K^{\text{eval}}$ whose state-action value matrix is estimated in Algorithm 2 need not be identical. We will use this fact in the next section to give an off-policy, offline (OFF) and on-policy, online (ON) version of our algorithm. Likewise, the penalty matrix $Q$ used in Algorithm 2 need not be the same as the one in the original problem statement, which is critical to developing the model-free midpoint update in the next section.

<!-- chunk {"id": "body-0042", "role": "body", "section": "Derivation of approximate midpoint policy iteration", "weight": 1.0} -->

We have shown that estimates of the state-action value matrix $H$ can be obtained by LSTDQ using either off-policy or on-policy data. In the following development, (OFF) denotes a variant where a single off-policy rollout $\mathcal{D}$ is collected offline before running the system, and (ON) denotes a variant where new on-policy rollouts are collected at each iteration. Also, an overhat symbol " $\hat{}$ " denotes an estimated quantity while the absence of one denotes an exact quantity.

<!-- chunk {"id": "body-0043", "role": "body", "section": "Derivation of approximate midpoint policy iteration", "weight": 1.0} -->

In approximate policy iteration, we can simply form the estimate ${\hat{H}}_{k}$ using LSTDQ (see \[Krauth et al.Krauth, Tu, and Recht\]). For approximate midpoint policy iteration, the form of ${\hat{H}}_{k}$ is more complicated and requires multiple steps. To derive approximate midpoint policy iteration, we will re-order some of the steps in the loop of Algorithm 1. Specifically, move the gain calculation in step 3 to the end after step 9. We will also replace explicit computation of the value function matrices with estimation of state-action value matrices, i.e. subsume the pairs of steps 4, 5 and 8,9 into single steps, and work with $H$ instead of $P$.

<!-- chunk {"id": "body-0044", "role": "body", "section": "Derivation of approximate midpoint policy iteration", "weight": 1.0} -->

First we translate steps 4, 5, 6, and 7 to a model-free version. Working backwards starting with step 7, in order to estimate $L_{k}$, it suffices to estimate $\mathcal{H}{(M_{k})}$ since $L_{k} = {- {\mathcal{H}{(M_{k})}_{uu}^{- 1}\mathcal{H}{(M_{k})}_{ux}}}$. In order to find $\mathcal{H}{(M_{k})}$, notice that the operator $\mathcal{H}{(X)}$ is linear in $X$, so

<!-- chunk {"id": "body-0045", "role": "body", "section": "Derivation of approximate midpoint policy iteration", "weight": 1.0} -->

Now we translate steps 8, 9, and 2 to a model-free version. Working backwards, starting with step 2, in order to estimate $K_{k + 1}$, it suffices to find an estimate ${\hat{H}}_{k + 1}$ of matrix $\mathcal{H}{(P_{k + 1})}$ since $K_{k + 1} = {- {\mathcal{H}{(P_{k + 1})}_{uu}^{- 1}\mathcal{H}{(P_{k + 1})}_{ux}}}$. From steps 8 and 9, we want to estimate

<!-- chunk {"id": "body-0046", "role": "body", "section": "Derivation of approximate midpoint policy iteration", "weight": 1.0} -->

Comparing the two arguments to $\text{DLYAP}{( \cdot, \cdot )}$ in and, we desire both

<!-- chunk {"id": "body-0047", "role": "body", "section": "Derivation of approximate midpoint policy iteration", "weight": 1.0} -->

Clearly it suffices to take $K = L_{k}$. Notice that, critically, all quantities in $S^{M}$ on the right-hand side of have been estimated already, i.e. ${\hat{K}}_{k}$, ${\hat{L}}_{k}$, ${\hat{H}}_{k}$ have been calculated already and

<!-- chunk {"id": "body-0048", "role": "body", "section": "Derivation of approximate midpoint policy iteration", "weight": 1.0} -->

Substituting $K = L_{k}$ in and comparing coefficients, it suffices to estimate $Q^{M}$ by

<!-- chunk {"id": "body-0049", "role": "body", "section": "Derivation of approximate midpoint policy iteration", "weight": 1.0} -->

At this point, establish the rollout $\mathcal{D}^{M}$ either by

<!-- chunk {"id": "body-0050", "role": "body", "section": "Derivation of approximate midpoint policy iteration", "weight": 1.0} -->

estimates $H_{k + 1}$. One further consideration to address is the initial estimate ${\hat{H}}_{0}$; since we do not have a prior iterate to use, we simply collect $\mathcal{D} = {\text{ROLLOUT}{({\hat{K}}_{0},\ell,\mathcal{X}_{0},{\{\mathcal{U}_{t}\}}_{t = 0}^{\ell})}}$ and estimate ${\hat{H}}_{0} = {\text{LSTDQ}{(\mathcal{D},{\hat{K}}_{0},Q)}}$ i.e. the first iteration will be a standard approximate policy iteration/Newton step. Importantly, the initial gain ${\hat{K}}_{0}$ must stabilize the system so that the value functions are finite-valued.

<!-- chunk {"id": "body-0051", "role": "body", "section": "Derivation of approximate midpoint policy iteration", "weight": 1.0} -->

Also, although a convergence criterion such as ${\|{{\hat{H}}_{k} - {\hat{H}}_{k - 1}}\|} > \varepsilon$ could be used, it is more straightforward to use a fixed number of iterations $N$ so that the influence of stochastic errors in ${\hat{H}}_{k}$ does not lead to premature termination of the program. Likewise, a schedule of increasing rollout lengths $\ell$ could be used for the (ON) variant to achieve increasing accuracy, but finding a meaningful schedule which properly matches the fast convergence rate of the algorithm requires more extensive analysis. The full set of updates are compiled in Algorithm 4.

<!-- chunk {"id": "body-0052", "role": "body", "section": "Derivation of approximate midpoint policy iteration", "weight": 1.0} -->

0: Penalty Q, gain K̂0, number of iterations N, rollout length ℓ, distributions 𝒳0, {𝒰t}t = 0ℓ. 3: Estimate value matrix Ĥ0 = LSTDQ (𝒟,K0,Q). 5: Set 𝒟N = 𝒟 (OFF), or collect 𝒟N = ROLLOUT (K̂k,ℓ,𝒳0,{𝒰t}t = 0ℓ) (ON)
6: Estimate value matrix Ĥk + 1N = LSTDQ (𝒟N,K̂k,Q). 7: Form the midpoint value estimate ${{\hat{H}}_{k}^{M} = {\frac{1}{2}{({{\hat{H}}_{k} + {\hat{H}}_{k + 1}^{N}})}}}.$
8: Compute the midpoint gain ${{\hat{L}}_{k} = {- {{\hat{H}}_{{uu},k}^{M}{{}_{}^{- 1}\left.

<!-- chunk {"id": "body-0053", "role": "body", "section": "Derivation of approximate midpoint policy iteration", "weight": 1.0} -->

H \right.\hat{}_{{ux},k}^{}}}}}.$
9: Set 𝒟M = 𝒟 (OFF), or collect 𝒟M = ROLLOUT (L̂k,ℓ,𝒳0,{𝒰t}t = 0ℓ) (ON)
10: Estimate Ĥk + 1O = LSTDQ (𝒟M,L̂k,Q̂M) where ${Q^{M} = {\begin{bmatrix}
\end{bmatrix}^{}{\hat{H}}_{k}\begin{bmatrix}
\end{bmatrix}} &amp; 0 \\
\end{bmatrix} - {({{\hat{H}}_{k} - Q})}}}.$
11: Compute the estimated value matrix Ĥk + 1 = Ĥk + 1O + (Q−Q̂M). 12: Compute the gain K̂k + 1 = −Ĥu u, k + 1−1 Ĥu x, k + 1.

<!-- chunk {"id": "body-0054", "role": "body", "section": "Derivation of approximate midpoint policy iteration", "weight": 1.0} -->

Algorithm 4 Approximate midpoint policy iteration (AMPI)

<!-- chunk {"id": "body-0055", "role": "body", "section": "Numerical experiments", "weight": 1.0} -->

In this section we compare the empirical performance of proposed midpoint policy iteration (MPI) with standard policy iteration (PI), as well as their approximate versions (AMPI) and (API). In all experiments, regardless of whether the exact or approximate algorithm is used, we evaluated the value matrix $P_{k}$ associated to the policy gains $K_{k}$ at each iteration $k$ on the true system, i.e. the solution to $P_{k} = {\text{DLYAP}\left( {A + {BK_{k}}},{\begin{bmatrix}
\end{bmatrix}Q\begin{bmatrix}
\end{bmatrix}^{}} \right)}$. We then normalized the deviation $\|{P_{k} - P^{\ast}}\|$, where $P^{\ast}$ solves the Riccati equation, by the quantity $\| P^{\ast}\|$. This gives a meaningful metric to compare different suboptimal gains.

<!-- chunk {"id": "body-0056", "role": "body", "section": "Numerical experiments", "weight": 1.0} -->

We also elected to focus on the off-policy version (OFF) of AMPI and API in order to achieve a more direct and fair comparison between the midpoint and standard methods; each is given access to precisely the same sample data and initial policy, so differences in convergence are entirely due to the algorithms. Nevertheless, similar results were observed in the on-policy online setting (ON), albeit with more variation between Monte Carlo runs due to differing sample data. Python code which implements the proposed algorithms and reproduces the experimental results is available at

<!-- chunk {"id": "body-0057", "role": "body", "section": "Representative example", "weight": 1.0} -->

Here we consider one of the simplest tasks in the control discipline: regulating an inertial mass using a force input. The stochastic continuous-time dynamics of the second-order system are

<!-- chunk {"id": "body-0058", "role": "body", "section": "Representative example", "weight": 1.0} -->

with mass $\mu > 0$, state $x \in {\mathbb{R}}^{2}$ where the first state is the position and the second state is the velocity, force input $u \in {\mathbb{R}}$, and ${dw} \in {\mathbb{R}}^{2}$ is a Wiener process with covariance $W_{c} \succeq 0$. Forward-Euler discretization of the continuous-time dynamics with sampling time $\Deltat$ yields the discrete-time dynamics

<!-- chunk {"id": "body-0059", "role": "body", "section": "Representative example", "weight": 1.0} -->

The results of applying midpoint policy iteration and the standard policy iteration are plotted in Figure LABEL:fig:inertial_mass_convergence. Clearly MPI and AMPI converge more quickly to the (approximate) optimal policy than PI and API, with MPI converging to machine precision in 7 iterations vs 9 iterations for PI, and AMPI converging to noise precision in 6 iterations vs 8 iterations for API.

<!-- chunk {"id": "body-0060", "role": "body", "section": "Representative example", "weight": 1.0} -->

fig:inertial_mass_convergence
Figure 1: Relative value error ∥Pk − P*∥/∥P*∥ vs iteration count k using PI and MPI on the inertial mass control problem.

<!-- chunk {"id": "body-0061", "role": "body", "section": "Randomized examples", "weight": 1.0} -->

Next we apply the exact and approximate PI algorithms on $10000$ unique problem instances in a Monte Carlo-style approach, where problem data was generated randomly with $n = 4$, $m = 2$, entries of $A$ drawn from $\mathcal{N}{}$ and $A$ scaled so ${\rho{(A)}} \sim {\text{Unif}{({\lbrack 0,2\rbrack})}}$, entries of $B$ drawn from $\text{Unif}{({\lbrack 0,1\rbrack})}$, and $Q = {U\LambdaU^{}} \succ 0$ with $\Lambda$ diagonal with entries drawn from $\text{Unif}{({\lbrack 0,1\rbrack})}$ and $U$ orthogonal by taking the QR-factorization of a square matrix with entries drawn from $\mathcal{N}{}$, where we denote the uniform distribution on the interval $\lbrack a,b\rbrack$ by

<!-- chunk {"id": "body-0062", "role": "body", "section": "Randomized examples", "weight": 1.0} -->

$\text{Unif}{({\lbrack a,b\rbrack})}$ and the multivariate Gaussian distribution with mean $\mu$ and variance $\Sigma$ by $\mathcal{N}{(\mu,\Sigma)}$.

<!-- chunk {"id": "body-0063", "role": "body", "section": "Randomized examples", "weight": 1.0} -->

We used a small process noise covariance of $W = {10^{- 6}I_{4}}$ to avoid unstable iterates due to excessive data-based approximation error of $H$, over all problem instances. All initial gains $K_{0}$ were chosen by perturbing the optimal gain $K^{\ast}$ in a random direction such that the initial relative error ${{\|{P_{k} - P^{\ast}}\|}/{\| P^{\ast}\|}} = 10$. For the approximate algorithms, we used the hyperparameters $\ell = 100$, $\mathcal{X}_{0} = {\mathcal{N}{(0,I_{2})}}$, $\mathcal{U}_{t} = {\mathcal{N}{(0,I_{2})}}$ for $t = {0,1,\ldots,\ell}$.

<!-- chunk {"id": "body-0064", "role": "body", "section": "Randomized examples", "weight": 1.0} -->

In Figures LABEL:fig:plot_error_monte_carlo_true_scatter, LABEL:fig:plot_error_monte_carlo_false_scatter, LABEL:fig:plot_error_monte_carlo_false_scatter_on we plot the relative value error ${\|{P_{k} - P^{\ast}}\|}/{\| P^{\ast}\|}$ over iterations, and each scatter point represents a unique Monte Carlo sample, i.e. a unique problem instance, initial gain, and rollout. Each plot shows the empirical distribution of errors at the iteration count $k$ labeled in the subplot titles above each plot. The x-axis is the spectral radius of $A$ which characterizes open-loop stability.

<!-- chunk {"id": "body-0065", "role": "body", "section": "Randomized examples", "weight": 1.0} -->

In sub-Figures LABEL:fig:plot_error_monte_carlo_true_scatter (b), LABEL:fig:plot_error_monte_carlo_false_scatter (b), LABEL:fig:plot_error_monte_carlo_false_scatter_on (b), scatter points lying below 1.0 on the y-axis indicate that the midpoint method achieves lower error than the standard method on the same problem instance.

<!-- chunk {"id": "body-0066", "role": "body", "section": "Randomized examples", "weight": 1.0} -->

From Figure LABEL:fig:plot_error_monte_carlo_true_scatter (a), it is clear that MPI achieves extremely fast convergence to the optimal gain, with the relative error being less than $10^{- 13}$, essentially machine precision, on almost all problem instances after just 5 iterations. From Figure LABEL:fig:plot_error_monte_carlo_true_scatter (b), we see that MPI achieves significantly lower error than PI on iteration counts $2,3,4,5$ for almost all problem instances. The relative differences in error on iteration counts $6,7$ are due to machine precision error and are negligible for the purposes of comparison i.e. after 6 iterations both algorithms have effectively converged to the same solution.

<!-- chunk {"id": "body-0067", "role": "body", "section": "Randomized examples", "weight": 1.0} -->

We observe very similar results using the approximate algorithms. From Figure LABEL:fig:plot_error_monte_carlo_false_scatter (a), it is clear that AMPI achieves extremely fast convergence to a good approximation of the optimal gain, with the relative error being less than $10^{- 6}$ on almost all problem instances after just 4 iterations. From Figure LABEL:fig:plot_error_monte_carlo_false_scatter (b), we see that AMPI achieves significantly lower error than API on iteration counts $2,3,4,5$ for almost all problem instances; recall that Algorithm 4 takes a standard PI step on the first iteration, explaining the identical performance on $k = 1$. Similar trends are observed in Figure LABEL:fig:plot_error_monte_carlo_false_scatter_on with the online variant (ON), but the variation is much greater. Nevertheless, AMPI provides a clear advantage on iteration counts $2,3,4,5$, beating API in terms of relative error most of the time.

<!-- chunk {"id": "body-0068", "role": "body", "section": "Randomized examples", "weight": 1.0} -->

fig:plot_error_monte_carlo_true_scatter \subfigure[Relative error using MPI]

<!-- chunk {"id": "body-0069", "role": "body", "section": "Randomized examples", "weight": 1.0} -->

\subfigure[Ratio of relative errors using MPI/PI]
Figure 2: (a) Relative value error ∥Pk − P*∥/∥P*∥ using MPI and (b) ratio of relative error using MPI divided by that using PI.

<!-- chunk {"id": "body-0070", "role": "body", "section": "Randomized examples", "weight": 1.0} -->

fig:plot_error_monte_carlo_false_scatter \subfigure[Relative error using AMPI (OFF)]

<!-- chunk {"id": "body-0071", "role": "body", "section": "Randomized examples", "weight": 1.0} -->

\subfigure[Ratio of relative errors using AMPI/API (OFF)]
Figure 3: (a) Relative value error ∥Pk − P*∥/∥P*∥ using AMPI and (b) ratio of relative error using AMPI divided by that using API, all with the offline algorithm variant (OFF).

<!-- chunk {"id": "body-0072", "role": "body", "section": "Randomized examples", "weight": 1.0} -->

fig:plot_error_monte_carlo_false_scatter_on \subfigure[Relative error using AMPI (ON)]

<!-- chunk {"id": "body-0073", "role": "body", "section": "Randomized examples", "weight": 1.0} -->

\subfigure[Ratio of relative errors using AMPI/API (ON)]
Figure 4: (a) Relative value error ∥Pk − P*∥/∥P*∥ using AMPI and (b) ratio of relative error using AMPI divided by that using API, all with the offline algorithm variant (ON).

<!-- chunk {"id": "body-0074", "role": "body", "section": "Conclusions and future work", "weight": 1.0} -->

Empirically, we found that regardless of the stabilizing initial policy chosen, convergence to the optimum always occurred when using the exact midpoint method. Likewise, we also found that approximate midpoint and standard PI converge to the same approximately optimal policy, and hence value matrix $P$, after enough iterations when evaluated on the same fixed off-policy rollout data $\mathcal{D}$. We conjecture that such robust, finite-data convergence properties can be proven rigorously, which we leave to future work.

<!-- chunk {"id": "body-0075", "role": "body", "section": "Conclusions and future work", "weight": 1.0} -->

This algorithm is perhaps most useful in the regime of practical problems in the online setting where it is relatively expensive to collect data and relatively cheap to perform the computations required to execute the updates. In such scenarios, the goal is to converge in as few iterations as possible, and MPI shows a clear advantage. Both the exact and approximate midpoint PI incur a computation cost *double* that of their standard PI counterparts. Theoretically, the faster *cubic* convergence rate of MPI over the *quadratic* convergence rate of PI should dominate this order constant (2$\times$) cost with sufficiently many iterations. However, unfortunately, due to finite machine precision, the total number of useful iterations that increase the precision of the optimal policy is limited, and the per-iteration cost largely counteracts the faster over-iteration convergence of MPI. This phenomenon becomes even more apparent in the model-free case where the "noise floor" is even higher. However, this disadvantage may be reduced by employing iterative Lyapunov equation solvers in Algorithm 1 or iterative (recursive) least-squares solvers in Algorithm 4 and warm-starting the midpoint equation with the Newton solution.

<!-- chunk {"id": "body-0076", "role": "body", "section": "Conclusions and future work", "weight": 1.0} -->

Furthermore, the benefit of the faster convergence of the midpoint PI may become more important in extensions to nonlinear systems, where the order constants in Propositions 4.1 and 5.1 are smaller.

<!-- chunk {"id": "body-0077", "role": "body", "section": "Conclusions and future work", "weight": 1.0} -->

The current methodology is certainty-equivalent in the sense that we treat the estimated value functions as correct. Future work will explore ways to estimate and account for uncertainty in the value function estimate explicitly to minimize regret risk in the initial transient stage of learning when the amount of information is low and uncertainty is high.
