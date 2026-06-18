<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Global Convergence of Policy Gradient Methods for the Linear Quadratic Regulator

Topics include Convex optimization, Policy gradients, Reinforcement learning, Optimal control, System identification, Optimization, Planning, Control, Learning, Linear quadratic regulator, Gradient method.

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Direct policy gradient methods for reinforcement learning and continuous control problems are a popular approach for a variety of reasons: 1) they are easy to implement without explicit knowledge of the underlying model 2) they are an "end-to-end" approach, directly optimizing the performance metric of interest 3) they inherently allow for richly parameterized policies. A notable drawback is that even in the most basic continuous control problem (that of linear quadratic regulators), these methods must solve a non-convex optimization problem, where little is understood about their efficiency from both computational and statistical perspectives. In contrast, system identification and model based planning in optimal control theory have a much more solid theoretical footing, where much is known with regards to their computational and statistical properties. This work bridges this gap showing that (model free) policy gradient methods globally converge to the optimal solution and are efficient (polynomially so in relevant problem dependent quantities) with regards to their sample and computational complexities.

<!-- chunk {"id": "body-0003", "role": "body", "section": "Introduction", "weight": 1.5} -->

Recent years have seen major advances in the control of uncertain dynamical systems using reinforcement learning and data-driven approaches; examples range from allowing robots to perform more sophisticated controls tasks such as robotic hand manipulation, to sequential decision making in game domains, e.g., AlphaGo and Atari game playing. Deep reinforcement learning (DeepRL) is becoming increasingly popular for tackling such challenging sequential decision making problems.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

Many of these successes have relied on sampling based reinforcement learning algorithms such as policy gradient methods, including the DeepRL approaches. For these approaches, there is little theoretical understanding of their efficiency, either from a statistical or a computational perspective. In contrast, control theory (optimal and adaptive control) has a rich body of tools, with provable guarantees, for related sequential decision making problems, particularly those that involve continuous control. These latter techniques are often model-based---they estimate an explicit dynamical model first (via system identification) and then design optimal controllers.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

This work builds bridges between these two lines of work, namely, between optimal control theory and sample based reinforcement learning methods, using ideas from mathematical optimization.

<!-- chunk {"id": "body-0006", "role": "body", "section": "The optimal control problem", "weight": 1.0} -->

In the standard optimal control problem, a dynamical system is described as

<!-- chunk {"id": "body-0007", "role": "body", "section": "The optimal control problem", "weight": 1.0} -->

where $f_{t}$ maps a state $x_{t} \in {\mathbb{R}}^{d}$, a control (the action) $u_{t} \in {\mathbb{R}}^{k}$, and a disturbance $w_{t}$, to the next state $x_{t + 1} \in {\mathbb{R}}^{d}$, starting from an initial state $x_{0}$. The objective is to find the control input $u_{t}$ which minimizes the long term cost,

<!-- chunk {"id": "body-0008", "role": "body", "section": "The optimal control problem", "weight": 1.0} -->

Here the $u_{t}$ are allowed to depend on the history of observed states, and $T$ is the time horizon (which can be finite or infinite). In practice, this is often solved by considering the linearized control (sub-)problem where the dynamics are approximated by

<!-- chunk {"id": "body-0009", "role": "body", "section": "The optimal control problem", "weight": 1.0} -->

and the costs are approximated by a quadratic function in $x_{t}$ and $u_{t}$, e.g.. The present paper considers an important special case: the time homogenous, infinite horizon problem referred to as the linear quadratic regulator (LQR) problem. The results herein can also be extended to the finite horizon, time inhomogenous setting, discussed in Section 5.

<!-- chunk {"id": "body-0010", "role": "body", "section": "The optimal control problem", "weight": 1.0} -->

We consider the following infinite horizon LQR problem,

<!-- chunk {"id": "body-0011", "role": "body", "section": "The optimal control problem", "weight": 1.0} -->

where initial state $x_{0} \sim \mathcal{D}$ is assumed to be randomly distributed according to distribution $\mathcal{D}$; the matrices $A \in {\mathbb{R}}^{d \times d}$ and $B \in {\mathbb{R}}^{d \times k}$ are referred to as system (or transition) matrices; $Q \in {\mathbb{R}}^{d \times d}$ and $R \in {\mathbb{R}}^{k \times k}$ are both positive definite matrices that parameterize the quadratic costs. For clarity, this work does not consider a noise disturbance but only a random initial state. The importance of (some) randomization for analyzing direct methods is discussed in Section 3 Optimization Landscape ‣ Global Convergence of Policy Gradient Methods for the Linear Quadratic Regulator").

<!-- chunk {"id": "body-0012", "role": "body", "section": "The optimal control problem", "weight": 1.0} -->

Throughout, assume that $A$ and $B$ are such that the optimal cost is finite (for example, the controllability of the pair $(A,B)$ would ensure this). Optimal control theory shows that the optimal control input can be written as a linear function in the state,

<!-- chunk {"id": "body-0013", "role": "body", "section": "The optimal control problem", "weight": 1.0} -->

Planning with a known model. For the infinite horizon LQR problem, planning can be achieved by solving the Algebraic Riccati Equation (ARE),

<!-- chunk {"id": "body-0014", "role": "body", "section": "The optimal control problem", "weight": 1.0} -->

for a positive definite matrix $P$ which parameterizes the "cost-to-go" (the optimal cost from a state going forward).

<!-- chunk {"id": "body-0015", "role": "body", "section": "The optimal control problem", "weight": 1.0} -->

To find $P$, there are iterative methods, algebraic solution methods, and (convex) SDP formulations. Solving the ARE is extensively studied; one approach due to (for continuous time) and (for discrete time) is to simply run the recursion $P_{k + 1} = {{Q + {A^{T}P_{k}A}} - {A^{T}P_{k}B{({R + {B^{T}P_{k}B}})}^{- 1}B^{T}P_{k}A}}$ where $P_{1} = Q$, which converges to the unique positive semidefinite solution of the ARE (since the fixed-point iteration is contractive). Other approaches are direct and are based on linear algebra, which carry out an eigenvalue decomposition on a certain block matrix (called the Hamiltonian matrix) followed by a matrix inversion. The LQR problem can also be expressed as a semidefinite program (SDP) with variable $P$ as given in (see Section A in the supplement).

<!-- chunk {"id": "body-0016", "role": "body", "section": "The optimal control problem", "weight": 1.0} -->

However, these formulations: 1) do not directly parameterize the policy, 2) are not "end-to-end" approaches, in that they are not directly optimizing the cost function of interest, and 3) it is not immediately clear how to utilize these approaches in the model-free setting, where the agent only has simulation access. These issues are outlined in Section A of the supplement.

<!-- chunk {"id": "body-0017", "role": "body", "section": "Contributions of this work", "weight": 1.0} -->

Even in the most basic case of the standard linear quadratic regulator model, little is understood as to how direct (model-free) policy gradient methods fare. This work provides rigorous guarantees, showing that, while in fact the approach deals with a non-convex problem, directly using (model free) local search methods leads to finding the globally optimal policy (i.e., a policy whose objective value is $\epsilon$-close to the optimal).

<!-- chunk {"id": "body-0018", "role": "body", "section": "Contributions of this work", "weight": 1.0} -->

(Exact case) Even with access to exact gradient evaluation, little is understood about whether or not convergence to the optimal policy occurs, even in the limit, due to the non-convexity of the problem. This work shows that global convergence does indeed occur (and does so efficiently) for gradient descent methods.

<!-- chunk {"id": "body-0019", "role": "body", "section": "Contributions of this work", "weight": 1.0} -->

(Model free case) Without a model, this work shows how one can use simulated trajectories (as opposed to having knowledge of the model) in a stochastic policy gradient method, where provable convergence to a globally optimal policy is guaranteed, with (polynomially) efficient computational and sample complexities.

<!-- chunk {"id": "body-0020", "role": "body", "section": "Contributions of this work", "weight": 1.0} -->

(The natural policy gradient) Natural policy gradient methods --- and related algorithms such as Trust Region Policy Optimization and the natural actor critic --- are some of the most widely used and effective policy gradient methods (see Duan et al. ). While many results argue in favor of this method based on either information geometry or based on connections to actor-critic methods, these results do not provably show an improved convergence rate. This work is the first to provide a guarantee that the natural gradient method enjoys a considerably improved convergence rate over its naive gradient counterpart.

<!-- chunk {"id": "body-0021", "role": "body", "section": "Contributions of this work", "weight": 1.0} -->

More broadly, the techniques in this work merge ideas from optimal control theory, mathematical optimization (first order and zeroth order), and sample based reinforcement learning methods. These techniques may ultimately help in improving upon the existing set of algorithms, addressing issues such as variance reduction or improving upon the natural policy gradient method (, say, a Gauss-Newton method as in Theorem 7). The Discussion section touches upon some of these issues.

<!-- chunk {"id": "body-0022", "role": "body", "section": "Exact Gradient Descent", "weight": 1.0} -->

where $\{ x_{t},u_{t}\}$ is the trajectory induced by following $K$, starting with $x_{0} \sim \mathcal{D}$. The importance of (some) randomization, either in $x_{0}$ or noise through having a disturbance, for analyzing gradient methods is discussed in Section 3 Optimization Landscape ‣ Global Convergence of Policy Gradient Methods for the Linear Quadratic Regulator"). Here, $K^{\ast}$ is a minimizer of $C{( \cdot )}$.

<!-- chunk {"id": "body-0023", "role": "body", "section": "Exact Gradient Descent", "weight": 1.0} -->

It is helpful to explicitly write out the functional form of the gradient.

<!-- chunk {"id": "body-0024", "role": "body", "section": "Exact Gradient Descent", "weight": 1.0} -->

Also, define $\Sigma_{K}$ as the (un-normalized) state correlation matrix, i.e.

<!-- chunk {"id": "body-0025", "role": "body", "section": "Review: (Model free) sample based policy gradient methods", "weight": 1.0} -->

Sample based policy gradient methods introduce some randomization for estimating the gradient.

<!-- chunk {"id": "body-0026", "role": "body", "section": "Review: (Model free) sample based policy gradient methods", "weight": 1.0} -->

REINFORCE. Let $\pi_{\theta}{(\left. u \middle| x \right.)}$ be a parametric stochastic policy, where $u \sim \pi_{\theta}{( \cdot |x)}$.

<!-- chunk {"id": "body-0027", "role": "body", "section": "Review: (Model free) sample based policy gradient methods", "weight": 1.0} -->

where the expectation is with respect to the trajectory $\{ x_{t},u_{t}\}$ induced under the policy $\pi_{\theta}$ and where $Q_{\pi_{\theta}}{(x,u)}$ is referred to as the state-action value. The REINFORCE algorithm uses Monte Carlo estimates of the gradient obtained by simulating $\pi_{\theta}$.

<!-- chunk {"id": "body-0028", "role": "body", "section": "Review: (Model free) sample based policy gradient methods", "weight": 1.0} -->

where $G_{\theta}$ is the Fisher information matrix. There are numerous succesful related approaches. An important special case is using a linear policy with additive Gaussian noise, i.e.

<!-- chunk {"id": "body-0029", "role": "body", "section": "Review: (Model free) sample based policy gradient methods", "weight": 1.0} -->

To see this, one can verify that the Fisher matrix of size ${{kd} \times k}d$, which is indexed as ${\lbrack G_{K}\rbrack}_{{(i,j)},{(i^{\prime},j^{\prime})}}$ where ${i,i^{\prime}} \in {\{ 1,{\ldotsk}\}}$ and ${j,j^{\prime}} \in {\{ 1,{\ldotsd}\}}$, has a block diagonal form where the only non-zeros blocks are ${\lbrack G_{K}\rbrack}_{{(i, \cdot )},{(i, \cdot )}} = \Sigma_{K}$ (this is the block corresponding to the $i$-th coordinate of the action, as $i$ ranges from $1$ to $k$). This form holds more generally, for any diagonal noise.

<!-- chunk {"id": "body-0030", "role": "body", "section": "Review: (Model free) sample based policy gradient methods", "weight": 1.0} -->

Zeroth order optimization. Zeroth order optimization is a generic procedure for optimizing a function $f{(x)}$, using only query access to the function values of $f{( \cdot )}$ at input points $x$ (and without explicit query access to the gradients of $f$). This is also the approach in using "evolutionary strategies" for reinforcement learning. The generic approach can be described as follows: define the perturbed function as

<!-- chunk {"id": "body-0031", "role": "body", "section": "Review: (Model free) sample based policy gradient methods", "weight": 1.0} -->

For small $\sigma$, the smooth function is a good approximation to the original function. Due to the Gaussian smoothing, the gradient has the particularly simple functional form (see Conn et al.;

<!-- chunk {"id": "body-0032", "role": "body", "section": "Review: (Model free) sample based policy gradient methods", "weight": 1.0} -->

This expression implies a straightforward method to obtain an unbiased estimate of the ${\nabla f_{\sigma^{2}}}{(x)}$, through obtaining only the function values $f{({x + \varepsilon})}$ for random $\varepsilon$.

<!-- chunk {"id": "body-0033", "role": "body", "section": "The (non-convex) Optimization Landscape", "weight": 1.0} -->

This section provides a brief characterization of the optimization landscape, in order to help provide intuition as to why global convergence is possible and as to where the analysis difficulties lie.

<!-- chunk {"id": "body-0034", "role": "body", "section": "Main Results", "weight": 1.0} -->

First, results on exact gradient methods are provided. From an analysis perspective, this is the natural starting point; once global convergence is established for exact methods, the question of using simulation-based, model-free methods can be approached with zeroth-order optimization methods (where gradients are not available, and can only be approximated using samples of the function value).

<!-- chunk {"id": "body-0035", "role": "body", "section": "Model-based optimization: exact gradient methods", "weight": 1.0} -->

We consider three exact update rules. For gradient descent, the update is

<!-- chunk {"id": "body-0036", "role": "body", "section": "Model-based optimization: exact gradient methods", "weight": 1.0} -->

The standard policy iteration algorithm that tries to optimize a one-step deviation from the current policy is equivalent to a special case of the Gauss-Newton method when $\eta = 1$ (for the case of policy iteration, convergence in the limit is provided in Todorov and Li; Ng et al.; Liao and Shoemaker, along with local convergence rates.)

<!-- chunk {"id": "body-0037", "role": "body", "section": "Model-based optimization: exact gradient methods", "weight": 1.0} -->

The Gauss-Newton method requires the most complex oracle to implement: it requires access to ${\nabla C}{(K)}$, $\Sigma_{K}$, and $R + {B^{\top}P_{K}B}$; it also enjoys the strongest convergence rate guarantee. At the other extreme, gradient descent requires oracle access to only ${\nabla C}{(K)}$ and has the slowest convergence rate. The natural policy gradient sits in between, requiring oracle access to ${\nabla C}{(K)}$ and $\Sigma_{K}$, and having a convergence rate between the other two methods.

<!-- chunk {"id": "body-0038", "role": "body", "section": "Model free optimization: sample based policy gradient methods", "weight": 1.0} -->

1: Input: K, number of trajectories m, roll out length ℓ, smoothing parameter r, dimension d
3: Sample a policy K̂i = K + Ui, where Ui is drawn uniformly at random over matrices whose (Frobenius) norm is r.
4: Simulate K̂i for ℓ steps starting from x0 ∼ 𝒟.

<!-- chunk {"id": "body-0039", "role": "body", "section": "Model free optimization: sample based policy gradient methods", "weight": 1.0} -->

where ct and xt are the costs and states on this trajectory.

<!-- chunk {"id": "body-0040", "role": "body", "section": "Model free optimization: sample based policy gradient methods", "weight": 1.0} -->

Algorithm 1 Model-Free Policy Gradient (and Natural Policy Gradient) Estimation

<!-- chunk {"id": "body-0041", "role": "body", "section": "Model free optimization: sample based policy gradient methods", "weight": 1.0} -->

In the model free setting, the controller has only simulation access to the model; the model parameters, $A$, $B$, $Q$ and $R$, are unknown. The standard optimal control theory approach is to use system identification to learn the model, and then plan with this learned model This section proves that model-free, policy gradient methods also lead to globally optimal policies, with both polynomial computational and sample complexities (in the relevant quantities).

<!-- chunk {"id": "body-0042", "role": "body", "section": "Model free optimization: sample based policy gradient methods", "weight": 1.0} -->

Using a zeroth-order optimization approach (see Section 2.2 sample based policy gradient methods ‣ 2 Preliminaries and Background ‣ Global Convergence of Policy Gradient Methods for the Linear Quadratic Regulator")), Algorithm 1 provides a procedure to find (bounded bias) estimates, $\hat{{\nabla C}{(K)}}$ and ${\hat{\Sigma}}_{K}$, of both ${\nabla C}{(K)}$ and $\Sigma_{K}$. These can then be used in the policy gradient and natural policy gradient updates. For policy gradient we have

<!-- chunk {"id": "body-0043", "role": "body", "section": "Model free optimization: sample based policy gradient methods", "weight": 1.0} -->

In both Equations and, Algorithm 1 is called at every iteration to provide the estimates of ${\nabla C}{(K_{n})}$ and $\Sigma_{K_{n}}$.

<!-- chunk {"id": "body-0044", "role": "body", "section": "Model free optimization: sample based policy gradient methods", "weight": 1.0} -->

The choice of using zeroth order optimization vs using REINFORCE (with Gaussian additive noise, as in Equation 3 sample based policy gradient methods ‣ 2 Preliminaries and Background ‣ Global Convergence of Policy Gradient Methods for the Linear Quadratic Regulator")) is primarily for technical reasons^22^2The correlations in the state-action value estimates in REINFORCE are more challenging to analyze.. It is plausible that the REINFORCE estimation procedure has lower variance. One additional minor difference, again for technical reasons, is that Algorithm 1 uses a perturbation from the surface of a sphere (as opposed to a Gaussian perturbation).

<!-- chunk {"id": "body-0045", "role": "body", "section": "Conclusions and Discussion", "weight": 1.0} -->

This work has provided provable guarantees that model-based gradient methods and model-free (sample based) policy gradient methods convergence to the globally optimal solution, with finite polynomial computational and sample complexities. Taken together, the results herein place these popular and practical policy gradient approaches on a firm theoretical footing, making them comparable to other principled approaches (e.g., subspace system identification methods and algebraic iterative approaches).

<!-- chunk {"id": "body-0046", "role": "body", "section": "Conclusions and Discussion", "weight": 1.0} -->

Finite $C{(K_{0})}$ assumption, noisy case, and finite horizon case. These methods allow for extensions to the noisy case and the finite horizon case. This work also made the assumption that $C{(K_{0})}$ is finite, which may not be easy to achieve in some infinite horizon problems. The simplest way to address this is to model the infinite horizon problem with a finite horizon one; the techniques developed in Section D.1 and Σ_𝐾 with finite horizon ‣ Appendix D Analysis: the Model-free case ‣ Global Convergence of Policy Gradient Methods for the Linear Quadratic Regulator") shows this is possible. This is an important direction for future work.

<!-- chunk {"id": "body-0047", "role": "body", "section": "Conclusions and Discussion", "weight": 1.0} -->

Variance reduction: This work only proved efficiency from a polynomial sample size perspective. An interesting future direction would be in how to rigorously combine variance reduction methods and model-based methods to further decrease the sample size.

<!-- chunk {"id": "body-0048", "role": "body", "section": "Conclusions and Discussion", "weight": 1.0} -->

A sample based Gauss-Newton approach: This work showed how the Gauss-Newton algorithm improves over even the natural policy gradient method, in the exact case. A practically relevant question for the Gauss-Newton method would be how to both: a) construct a sample based estimator b) extend this scheme to deal with (non-linear) parametric policies.

<!-- chunk {"id": "body-0049", "role": "body", "section": "Conclusions and Discussion", "weight": 1.0} -->

Robust control: In model based approaches, optimal control theory provides efficient procedures to deal with (bounded) model mis-specification. An important question is how to provably understand robustness in a model free setting.
