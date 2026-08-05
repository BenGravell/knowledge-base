<!-- arxiv-full-text:v1 {"arxiv_id": "1801.05039", "source": "ar5iv"} -->

## Introduction

Recent years have seen major advances in the control of uncertain dynamical systems using reinforcement learning and data-driven approaches; examples range from allowing robots to perform more sophisticated controls tasks such as robotic hand manipulation, to sequential decision making in game domains, e.g., AlphaGo and Atari game playing. Deep reinforcement learning (DeepRL) is becoming increasingly popular for tackling such challenging sequential decision making problems.

Many of these successes have relied on sampling based reinforcement learning algorithms such as policy gradient methods, including the DeepRL approaches. For these approaches, there is little theoretical understanding of their efficiency, either from a statistical or a computational perspective. In contrast, control theory (optimal and adaptive control) has a rich body of tools, with provable guarantees, for related sequential decision making problems, particularly those that involve continuous control. These latter techniques are often model-based---they estimate an explicit dynamical model first (via system identification) and then design optimal controllers.

This work builds bridges between these two lines of work, namely, between optimal control theory and sample based reinforcement learning methods, using ideas from mathematical optimization.

### The optimal control problem

In the standard optimal control problem, a dynamical system is described as where $f_{t}$ maps a state $x_{t} \in {\mathbb{R}}^{d}$, a control (the action) $u_{t} \in {\mathbb{R}}^{k}$, and a disturbance $w_{t}$, to the next state $x_{t + 1} \in {\mathbb{R}}^{d}$, starting from an initial state $x_{0}$. The objective is to find the control input $u_{t}$ which minimizes the long term cost, Here the $u_{t}$ are allowed to depend on the history of observed states, and $T$ is the time horizon (which can be finite or infinite). In practice, this is often solved by considering the linearized control (sub-)problem where the dynamics are approximated by and the costs are approximated by a quadratic function in $x_{t}$ and $u_{t}$, e.g.. The present paper considers an important special case: the time homogenous, infinite horizon problem referred to as the linear quadratic regulator (LQR) problem. The results herein can also be extended to the finite horizon, time inhomogenous setting, discussed in Section 5.

We consider the following infinite horizon LQR problem, where initial state $x_{0} \sim \mathcal{D}$ is assumed to be randomly distributed according to distribution $\mathcal{D}$; the matrices $A \in {\mathbb{R}}^{d \times d}$ and $B \in {\mathbb{R}}^{d \times k}$ are referred to as system (or transition) matrices; $Q \in {\mathbb{R}}^{d \times d}$ and $R \in {\mathbb{R}}^{k \times k}$ are both positive definite matrices that parameterize the quadratic costs. For clarity, this work does not consider a noise disturbance but only a random initial state. The importance of (some) randomization for analyzing direct methods is discussed in Section 3 Optimization Landscape ‣ Global Convergence of Policy Gradient Methods for the Linear Quadratic Regulator").

Throughout, assume that $A$ and $B$ are such that the optimal cost is finite (for example, the controllability of the pair $(A,B)$ would ensure this). Optimal control theory shows that the optimal control input can be written as a linear function in the state, where $K^{\ast} \in {\mathbb{R}}^{k \times d}$.

Planning with a known model. For the infinite horizon LQR problem, planning can be achieved by solving the Algebraic Riccati Equation (ARE), for a positive definite matrix $P$ which parameterizes the "cost-to-go" (the optimal cost from a state going forward). The optimal control gain is then given as: To find $P$, there are iterative methods, algebraic solution methods, and (convex) SDP formulations. Solving the ARE is extensively studied; one approach due to (for continuous time) and (for discrete time) is to simply run the recursion $P_{k + 1} = {{Q + {A^{T}P_{k}A}} - {A^{T}P_{k}B{({R + {B^{T}P_{k}B}})}^{- 1}B^{T}P_{k}A}}$ where $P_{1} = Q$, which converges to the unique positive semidefinite solution of the ARE (since the fixed-point iteration is contractive). Other approaches are direct and are based on linear algebra, which carry out an eigenvalue decomposition on a certain block matrix (called the Hamiltonian matrix) followed by a matrix inversion. The LQR problem can also be expressed as a semidefinite program (SDP) with variable $P$ as given in (see Section A in the supplement).

However, these formulations: 1) do not directly parameterize the policy, 2) are not "end-to-end" approaches, in that they are not directly optimizing the cost function of interest, and 3) it is not immediately clear how to utilize these approaches in the model-free setting, where the agent only has simulation access. These issues are outlined in Section A of the supplement.

### Contributions of this work

Even in the most basic case of the standard linear quadratic regulator model, little is understood as to how direct (model-free) policy gradient methods fare. This work provides rigorous guarantees, showing that, while in fact the approach deals with a non-convex problem, directly using (model free) local search methods leads to finding the globally optimal policy (i.e., a policy whose objective value is $\epsilon$-close to the optimal). The main contributions are as follows: (Exact case) Even with access to exact gradient evaluation, little is understood about whether or not convergence to the optimal policy occurs, even in the limit, due to the non-convexity of the problem. This work shows that global convergence does indeed occur (and does so efficiently) for gradient descent methods.

(Model free case) Without a model, this work shows how one can use simulated trajectories (as opposed to having knowledge of the model) in a stochastic policy gradient method, where provable convergence to a globally optimal policy is guaranteed, with (polynomially) efficient computational and sample complexities.

(The natural policy gradient) Natural policy gradient methods --- and related algorithms such as Trust Region Policy Optimization and the natural actor critic --- are some of the most widely used and effective policy gradient methods (see Duan et al. ). While many results argue in favor of this method based on either information geometry or based on connections to actor-critic methods, these results do not provably show an improved convergence rate. This work is the first to provide a guarantee that the natural gradient method enjoys a considerably improved convergence rate over its naive gradient counterpart.

More broadly, the techniques in this work merge ideas from optimal control theory, mathematical optimization (first order and zeroth order), and sample based reinforcement learning methods. These techniques may ultimately help in improving upon the existing set of algorithms, addressing issues such as variance reduction or improving upon the natural policy gradient method (, say, a Gauss-Newton method as in Theorem 7). The Discussion section touches upon some of these issues.

### Related work

In the reinforcement learning setting, the model is unknown, and the agent must learn to act through its interactions with the environment. Here, solution concepts are typically divided into: model-based approaches, where the agent attempts to learn a model of the world, and model-free approaches, where the agent directly learns to act and does not explicitly learn a model of the world. The related work on provably learning LQRs is reviewed from this perspective.

Model-based learning approaches. In the context of LQRs, the agent can attempt to learn the dynamics of "the plant" (i.e., the model) and then plan, using this model, for control synthesis. Here, the classical approach is to learn the model with subspace-based system identification. Fiechter provides a provable learning (and non-asymptotic) result, where the quality of the policy obtained is shown to be near optimal (efficiency is in terms of the persistence of the training data and the controllability Gramian). Abbasi-Yadkori and Szepesvári also provides provable, non-asymptotic learning results in a regret context, using a bandit algorithm that achieves lower sample complexity (by balancing exploration-exploitation more effectively); the computational efficiency of this approach is less clear.

More recently, Dean et al. expands on an explicit system identification process, where a robust control synthesis procedure is adopted that relies on a coarse model of the plant matrices ($A$ and $B$ are estimated up to some accuracy level, naturally leading to a "robust control" setup to then design the controller based in the coarse model). Tighter analysis for sample complexity was given in Tu and Recht; Simchowitz et al.. Arguably, this is the most general (and non-asymptotic) result that is efficient from a statistical perspective. Computationally, the method works with a finite horizon to approximate the infinite horizon. This result only needs the plant to be controllable; the work herein needs the stronger assumption that the initial policy in the local search procedure is a stable controller (an assumption which may be inherent to local search procedures, discussed in Section 5). Another recent line of work treat the problem of learning a linear dynamical system as an online learning problem. are restricted to systems with symmetric dynamics (symmetric $A$ matrix), while handles a more general setting. This line of work can handle the case when there are latent states (i.e., when the observed output is a linear function of the state, and the state is not observed directly) and does not need to do system identification first. On the other hand, they don't output a succinct linear policy as Dean et al. or this paper.

Model-free learning approaches. Model-free approaches that do not rely on an explicit system identification step typically either: 1) estimate value functions (or state-action values) through Monte Carlo simulation which are then used in some approximate dynamic programming variant, or 2) directly optimize a (parameterized) policy, also through Monte Carlo simulation. Model-free approaches for learning optimal controllers are not well understood from a theoretical perspective. Here, Bradtke et al. provides an asymptotic learnability result using a value function approach, namely $Q$-learning.

## Preliminaries and Background

### Exact Gradient Descent

This work seeks to characterize the behavior of (direct) policy gradient methods, where the policy is linearly parameterized, as specified by a matrix $K \in {\mathbb{R}}^{k \times d}$ which generates the controls: for $t \geq 0$. The cost of this $K$ is denoted as: where $\{ x_{t},u_{t}\}$ is the trajectory induced by following $K$, starting with $x_{0} \sim \mathcal{D}$. The importance of (some) randomization, either in $x_{0}$ or noise through having a disturbance, for analyzing gradient methods is discussed in Section 3 Optimization Landscape ‣ Global Convergence of Policy Gradient Methods for the Linear Quadratic Regulator"). Here, $K^{\ast}$ is a minimizer of $C{(\cdot)}$.

Gradient descent on $C{(K)}$, with a fixed stepsize $\eta$, follows the update rule: It is helpful to explicitly write out the functional form of the gradient. Define $P_{K}$ as the solution to: and, under this definition, it follows that $C{(K)}$ can be written as: Also, define $\Sigma_{K}$ as the (un-normalized) state correlation matrix, i.e.

### Lemma 1

(Policy Gradient Expression) The policy gradient is: Later for simplicity, define $E_{K}$ to be as a result the gradient can be written as ${{\nabla C}{(K)}} = {2E_{K}\Sigma_{K}}$.

### Proof

Let $\nabla$ denote the gradient with respect to $K$, note that ${\nabla C_{K}}{({{({A - {BK}})}x_{0}})}$ has two terms (one with respect to $K$ in the subscript and one with respect to the input ${({A - {BK}})}x_{0}$), this implies using recursion and that $x_{1} = {{({A - {BK}})}x_{0}}$. Taking expectations completes the proof. ∎

### Review: (Model free) sample based policy gradient methods

Sample based policy gradient methods introduce some randomization for estimating the gradient.

REINFORCE. Let $\pi_{\theta}{(\left. u \middle| x \right.)}$ be a parametric stochastic policy, where $u \sim \pi_{\theta}{(\cdot |x)}$. The policy gradient of the cost, $C{(\theta)}$, is: where the expectation is with respect to the trajectory $\{ x_{t},u_{t}\}$ induced under the policy $\pi_{\theta}$ and where $Q_{\pi_{\theta}}{(x,u)}$ is referred to as the state-action value. The REINFORCE algorithm uses Monte Carlo estimates of the gradient obtained by simulating $\pi_{\theta}$.

The natural policy gradient. The natural policy gradient follows the update: where $G_{\theta}$ is the Fisher information matrix. There are numerous succesful related approaches. An important special case is using a linear policy with additive Gaussian noise, i.e. where $K \in {\mathbb{R}}^{k \times d}$ and $\sigma^{2}$ is the noise variance. Here, the natural policy gradient of $K$ (when $\sigma$ is considered fixed) takes the form: To see this, one can verify that the Fisher matrix of size ${{kd} \times k}d$, which is indexed as ${\lbrack G_{K}\rbrack}_{{(i,j)},{(i',j')}}$ where ${i,i'} \in {\{ 1,{\ldotsk}\}}$ and ${j,j'} \in {\{ 1,{\ldotsd}\}}$, has a block diagonal form where the only non-zeros blocks are ${\lbrack G_{K}\rbrack}_{{(i, \cdot)},{(i, \cdot)}} = \Sigma_{K}$ (this is the block corresponding to the $i$-th coordinate of the action, as $i$ ranges from $1$ to $k$). This form holds more generally, for any diagonal noise.

Zeroth order optimization. Zeroth order optimization is a generic procedure for optimizing a function $f{(x)}$, using only query access to the function values of $f{(\cdot)}$ at input points $x$ (and without explicit query access to the gradients of $f$). This is also the approach in using "evolutionary strategies" for reinforcement learning. The generic approach can be described as follows: define the perturbed function as For small $\sigma$, the smooth function is a good approximation to the original function. Due to the Gaussian smoothing, the gradient has the particularly simple functional form (see Conn et al.; Nesterov and Spokoiny): This expression implies a straightforward method to obtain an unbiased estimate of the ${\nabla f_{\sigma^{2}}}{(x)}$, through obtaining only the function values $f{({x + \varepsilon})}$ for random $\varepsilon$.

## The (non-convex) Optimization Landscape

This section provides a brief characterization of the optimization landscape, in order to help provide intuition as to why global convergence is possible and as to where the analysis difficulties lie.

### Lemma 2

(Non-convexity) If $d \geq 3$, there exists an LQR optimization problem, ${\min_{K}C}{(K)}$, which is not convex, quasi-convex, and star-convex.

The specific example is given in supplementary material (Section B). In particular, there can be two matrices $K$ and $K'$ where both $C{(K)}$ and $C{(K')}$ are finite, but $C{({{({K + K'})}/2})}$ is infinite.

For a general non-convex optimization problem, gradient descent may not even converge to the global optima in the limit. The optimization problem of LQR satisfies a special gradient domination condition, which makes it much easier to optimize:

### Lemma 3

(Gradient domination) Let $K^{\ast}$ be an optimal policy. Suppose $K$ has finite cost and ${\sigma_{\text{min}}{(\Sigma_{K})}} > 0$. It holds that This lemma can be proved by analyzing the "advantage" of the optimal policy $\Sigma^{\ast}$ to $\Sigma$ in every step. The detailed lemma and the full proof is deferred to supplementary material.

As a corollary, this lemma provides a characterization of the stationary points.

### Corollary 4

(Stationary point characterization) If ${{\nabla C}{(K)}} = 0$, then either $K$ is an optimal policy or $\Sigma_{K}$ is rank deficient.

Note that the covariance $\Sigma_{K} \succeq \Sigma_{0}:={{\mathbb{E}}_{x_{0} \sim \mathcal{D}}x_{0}x_{0}^{\top}}$. Therefore, this lemma is the motivation for using a distribution over $x_{0}$ (as opposed to a deterministic starting point): ${\mathbb{E}}_{x_{0} \sim \mathcal{D}}x_{0}x_{0}^{\top}$ being full rank guarantees that $\Sigma_{K}$ is full rank, which implies all stationary points are a global optima. An additive disturbance in the dynamics model also suffices.

The concept of gradient domination is important in the non-convex optimization literature. A function $f:{{\mathbb{R}}^{d}\rightarrow{\mathbb{R}}}$ is said to be gradient dominated if there exists some constant $\lambda$, such that for all $x$, If a function is gradient dominated, this implies that if the magnitude of the gradient is small at some $x$, then the function value at $x$ will be close to that of the optimal function value.

Using the fact that $\Sigma_{K} \succeq \Sigma_{0}$, the following corollary of Lemma 3 Optimization Landscape ‣ Global Convergence of Policy Gradient Methods for the Linear Quadratic Regulator") shows that $C{(K)}$ is gradient dominated.

### Corollary 5

(Gradient Domination) Suppose ${\mathbb{E}}_{x_{0} \sim \mathcal{D}}x_{0}x_{0}^{\top}$ is full rank. Then $C{(K)}$ is gradient dominated, i.e. where $\lambda = \frac{\|\Sigma_{K^{\ast}}\|}{\sigma_{\text{min}}{(\Sigma_{0})}^{2}\sigma_{\text{min}}{(R)}}$ is a problem dependent constant (and $\langle \cdot, \cdot \rangle$ denotes the trace inner product).

Naively, one may hope that gradient domination immediately implies that gradient descent converges quickly to the global optima. This would indeed be the case if the $C{(K)}$ were a smooth function^11^1A differentiable function $f{(x)}$ is said to be smooth if the gradients of $f$ are continuous. Equivalently, see the definition in Equation 13.: if it were the case that $C{(K)}$ is both gradient dominated *and* smooth, then classical mathematical optimization results would not only immediately imply global convergence, these results would also imply convergence at a linear rate. These results are not immediately applicable due to it is not straightforward to characterize the (local) smoothness properties of $C{(K)}$; this is a difficulty well studied in the optimal control theory literature, related to robustness and stability.

Similarly, one may hope that recent results on escaping saddle points immediately imply that gradient descent converges quickly to the global optima, due to that there are no (spurious) local optima. Again, for reasons related to smoothness this is not the case.

The main reason that the LQR objective cannot satisfy the smoothness condition globally is that the objective becomes infinity when the matrix $A - {BK}$ becomes unstable (i.e. has an eigenvalue that is outside of the unit circle in the complex plane). At the boundary between stable and unstable policies, the objective function quickly becomes infinity, which violates the traditional smoothness conditions because smoothness conditions would imply quadratic upper-bounds for the objective function.

To solve this problem, it is observed that when the policy $K$ is not too close to the boundary, the objective satisfies an almost-smoothness condition:

### Lemma 6

("Almost" smoothness) $C{(K)}$ satisfies: To see why this is related to smoothness (e.g. compare to Equation 13), suppose $K'$ is sufficiently close to $K$ so that: and the leading order term $2Tr{({\Sigma_{K'}{({K' - K})}^{\top}E_{K}})}$ would then behave as ${Tr}{({{({K' - K})}^{\top}{\nabla C}{(K)}})}$, and the remaining terms will be second order in $K - K'$.

Quantify the Taylor approximation $\Sigma_{K'} \approx {\Sigma_{K} + {O{({\|{K - K'}\|})}}}$ is one of the key steps in proving the convergence of policy gradient.

## Main Results

First, results on exact gradient methods are provided. From an analysis perspective, this is the natural starting point; once global convergence is established for exact methods, the question of using simulation-based, model-free methods can be approached with zeroth-order optimization methods (where gradients are not available, and can only be approximated using samples of the function value).

Notation. $\| Z\|$ denotes the spectral norm of a matrix $Z$; ${Tr}{(Z)}$ denotes the trace of a square matrix; $\sigma_{\text{min}}{(Z)}$ denotes the minimal singular value of a square matrix $Z$. Also, it is helpful to define

### Model-based optimization: exact gradient methods

We consider three exact update rules. For gradient descent, the update is For natural policy gradient descent, the direction is defined so that it is consistent with the stochastic case, as per Equation 4 sample based policy gradient methods ‣ 2 Preliminaries and Background ‣ Global Convergence of Policy Gradient Methods for the Linear Quadratic Regulator"), in the exact case the update is: For Gauss-Newton method, the update is: The standard policy iteration algorithm that tries to optimize a one-step deviation from the current policy is equivalent to a special case of the Gauss-Newton method when $\eta = 1$ (for the case of policy iteration, convergence in the limit is provided in Todorov and Li; Ng et al.; Liao and Shoemaker, along with local convergence rates.)

The Gauss-Newton method requires the most complex oracle to implement: it requires access to ${\nabla C}{(K)}$, $\Sigma_{K}$, and $R + {B^{\top}P_{K}B}$; it also enjoys the strongest convergence rate guarantee. At the other extreme, gradient descent requires oracle access to only ${\nabla C}{(K)}$ and has the slowest convergence rate. The natural policy gradient sits in between, requiring oracle access to ${\nabla C}{(K)}$ and $\Sigma_{K}$, and having a convergence rate between the other two methods.

### Theorem 7

(Global Convergence of Gradient Methods) Suppose $C{(K_{0})}$ is finite and $\mu > 0$.

Gauss-Newton case: For a stepsize $\eta = 1$ and for the Gauss-Newton algorithm (Equation 7) enjoys the following performance bound: Natural policy gradient case: For a stepsize natural policy gradient descent (Equation 6) enjoys the following performance bound: Gradient descent case: For an appropriate (constant) setting of the stepsize $\eta$, gradient descent (Equation 5) enjoys the following performance bound: In comparison to model-based approaches, these results require the (possibly) stronger assumption that the initial policy is a stable controller, i.e. $C{(K_{0})}$ is finite (an assumption which may be inherent to local search procedures). The Discussion mentions this as direction of future work.

The proof for Gauss-Newton algorithm is simple based on the characterizations in Lemma 3 Optimization Landscape ‣ Global Convergence of Policy Gradient Methods for the Linear Quadratic Regulator") and Lemma 6 Optimization Landscape ‣ Global Convergence of Policy Gradient Methods for the Linear Quadratic Regulator"), and is given below. The proof for natural policy gradient and gradient descent are more involved, and are deferred to supplementary material.

### Lemma 8

If $\eta \leq 1$, then

### Proof

Observe $K' = {K - {\eta{({R + {B^{\top}P_{K}B}})}^{- 1}E_{K}}}$. Using Lemma 6 Optimization Landscape ‣ Global Convergence of Policy Gradient Methods for the Linear Quadratic Regulator") and the condition on $\eta$, where the last step uses Lemma 3 Optimization Landscape ‣ Global Convergence of Policy Gradient Methods for the Linear Quadratic Regulator"). ∎ With this lemma, the proof of the convergence rate of the Gauss Newton algorithm is immediate.

### Proof

(of Theorem 7, Gauss-Newton case) The theorem is due to that $\eta = 1$ leads to a contraction of $1 - \frac{\eta\mu}{\|\Sigma_{K^{\ast}}\|}$ at every step. ∎

### Model free optimization: sample based policy gradient methods

1: Input: K, number of trajectories m, roll out length ℓ, smoothing parameter r, dimension d 3: Sample a policy K̂i = K + Ui, where Ui is drawn uniformly at random over matrices whose (Frobenius) norm is r. 4: Simulate K̂i for ℓ steps starting from x0 ∼ 𝒟. Let Ĉi and Σ̂i be the empirical estimates: $${{\hat{C}}_{i} = {\sum\limits_{t = 1}^{\ell}c_{t}}},{{\hat{\Sigma}}_{i} = {\sum\limits_{t = 1}^{\ell}{x_{t}x_{t}^{\top}}}}$$ where ct and xt are the costs and states on this trajectory. 6: Return the (biased) estimates: $${\hat{{\nabla C}{(K)}} = {\frac{1}{m}{\sum\limits_{i = 1}^{m}{\frac{d}{r^{2}}{\hat{C}}_{i}U_{i}}}}},{\hat{\Sigma_{K}} = {\frac{1}{m}{\sum\limits_{i = 1}^{m}{\hat{\Sigma}}_{i}}}}$$ Algorithm 1 Model-Free Policy Gradient (and Natural Policy Gradient) Estimation In the model free setting, the controller has only simulation access to the model; the model parameters, $A$, $B$, $Q$ and $R$, are unknown. The standard optimal control theory approach is to use system identification to learn the model, and then plan with this learned model This section proves that model-free, policy gradient methods also lead to globally optimal policies, with both polynomial computational and sample complexities (in the relevant quantities).

Using a zeroth-order optimization approach (see Section 2.2 sample based policy gradient methods ‣ 2 Preliminaries and Background ‣ Global Convergence of Policy Gradient Methods for the Linear Quadratic Regulator")), Algorithm 1 provides a procedure to find (bounded bias) estimates, $\hat{{\nabla C}{(K)}}$ and ${\hat{\Sigma}}_{K}$, of both ${\nabla C}{(K)}$ and $\Sigma_{K}$. These can then be used in the policy gradient and natural policy gradient updates. For policy gradient we have For natural policy gradient we have: In both Equations and, Algorithm 1 is called at every iteration to provide the estimates of ${\nabla C}{(K_{n})}$ and $\Sigma_{K_{n}}$.

The choice of using zeroth order optimization vs using REINFORCE (with Gaussian additive noise, as in Equation 3 sample based policy gradient methods ‣ 2 Preliminaries and Background ‣ Global Convergence of Policy Gradient Methods for the Linear Quadratic Regulator")) is primarily for technical reasons^22^2The correlations in the state-action value estimates in REINFORCE are more challenging to analyze.. It is plausible that the REINFORCE estimation procedure has lower variance. One additional minor difference, again for technical reasons, is that Algorithm 1 uses a perturbation from the surface of a sphere (as opposed to a Gaussian perturbation).

### Theorem 9

(Global Convergence in the Model Free Setting) Suppose $C{(K_{0})}$ is finite, $\mu > 0$, and that $x_{0} \sim \mathcal{D}$ has norm bounded by $L$ almost surely. Also, for both the policy gradient method and the natural policy gradient method, suppose Algorithm 1 is called with parameters: Natural policy gradient case: For a stepsize then, with high probability, i.e. with probability greater than $1 - {\exp{({- d})}}$, the natural policy gradient descent update (Equation 9) enjoys the following performance bound: Gradient descent case: For an appropriate (constant) setting of the stepsize $\eta$, then, with high probability, gradient descent (Equation 8) enjoys the following performance bound: This theorem gives the first polynomial time guarantee for policy gradient and natural policy gradient algorithms in the LQR problem.

### Proof Sketch

The model free results (Theorem 9) are proved in the following three steps: Prove that when the roll out length $\ell$ is large enough, the cost function $C$ and the covariance $\Sigma$ are approximately equal to the corresponding quantities at infinite steps.

Show that with enough samples, Algorithm 1 can estimate both the gradient and covariance matrix within the desired accuracy.

Prove that both gradient descent and natural gradient descent can converge with a similar rate, even if the gradient/natural gradient estimates have some bounded perturbations.

The proofs are technical and are deferred to supplementary material. We have focused on proving polynomial relationships in our complexity bounds, and did not optimize for the best dependence on the relevant parameters.

## Conclusions and Discussion

This work has provided provable guarantees that model-based gradient methods and model-free (sample based) policy gradient methods convergence to the globally optimal solution, with finite polynomial computational and sample complexities. Taken together, the results herein place these popular and practical policy gradient approaches on a firm theoretical footing, making them comparable to other principled approaches (e.g., subspace system identification methods and algebraic iterative approaches).

Finite $C{(K_{0})}$ assumption, noisy case, and finite horizon case. These methods allow for extensions to the noisy case and the finite horizon case. This work also made the assumption that $C{(K_{0})}$ is finite, which may not be easy to achieve in some infinite horizon problems. The simplest way to address this is to model the infinite horizon problem with a finite horizon one; the techniques developed in Section D.1 and Σ_𝐾 with finite horizon ‣ Appendix D Analysis: the Model-free case ‣ Global Convergence of Policy Gradient Methods for the Linear Quadratic Regulator") shows this is possible. This is an important direction for future work.

Variance reduction: This work only proved efficiency from a polynomial sample size perspective. An interesting future direction would be in how to rigorously combine variance reduction methods and model-based methods to further decrease the sample size.

A sample based Gauss-Newton approach: This work showed how the Gauss-Newton algorithm improves over even the natural policy gradient method, in the exact case. A practically relevant question for the Gauss-Newton method would be how to both: a) construct a sample based estimator b) extend this scheme to deal with (non-linear) parametric policies.

Robust control: In model based approaches, optimal control theory provides efficient procedures to deal with (bounded) model mis-specification. An important question is how to provably understand robustness in a model free setting.
