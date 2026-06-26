<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Cost-Driven Representation Learning for Linear Quadratic Gaussian Control: Part I

Topics include Reinforcement learning, Partial observability, Optimal control, Representation learning, Control, Learning, Linear quadratic Gaussian, Linear quadratic Gaussian control, State space.

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

We study the task of learning state representations from potentially high-dimensional observations, with the goal of controlling an unknown partially observable system. We pursue a cost-driven approach, where a dynamic model in some latent state space is learned by predicting the costs without predicting the observations or actions. In particular, we focus on an intuitive cost-driven state representation learning method for solving Linear Quadratic Gaussian (LQG) control, one of the most fundamental partially observable control problems. As our main results, we establish finite-sample guarantees of finding a near-optimal state representation function and a near-optimal controller using the directly learned latent model, for finite-horizon time-varying LQG control problems. To the best of our knowledge, despite various empirical successes, finite-sample guarantees of such a cost-driven approach remain elusive. Our result underscores the value of predicting multi-step costs, an idea that is key to our theory, and notably also an idea that is known to be empirically valuable for learning state representations.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

A second part of this work, that is to appear as Part II, addresses the infinite-horizon linear time-invariant setting; it also extends the results to an approach that implicitly learns the latent dynamics, inspired by the recent empirical breakthrough of MuZero in model-based reinforcement learning.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

We consider state representation learning for control in partially observable systems, inspired by the recent successes of *control from pixels*. Control from pixels is an everyday task for human beings, but it remains challenging for learning agents. Methods to achieve it generally fall into two main categories: *model-free* and *model-based* ones. Model-free methods directly learn a visuomotor policy, also known as direct reinforcement learning (RL). On the other hand, model-based methods, also known as indirect RL, attempt to learn a *latent model* that is a compact representation of the system, and to synthesize a policy in the latent model. Compared with model-free methods, model-based ones facilitate generalization across tasks and enable efficient planning, and are sometimes more sample efficient than the model-free ones.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

In latent-model-based control, the state of the latent model is also referred to as a *state representation* in the deep RL literature, and the mapping from an observed history to a latent state is referred to as the (state) representation function. *Reconstructing the observation* often serves as a supervision for representation learning for control in the empirical RL literature. This is in sharp contrast to model-free methods, where the policy improvement step is completely *cost-driven*. Reconstructing observations provides a rich supervision signal for learning a task-agnostic world model, but they are high-dimensional and noisy, so the reconstruction requires an expressive reconstruction function; latent states learned by reconstruction contain irrelevant information for control, which can distract RL algorithms. This is especially the case for practical visuomotor control tasks, e.g., robotic manipulation and self-driving cars, where the visual images contain predominately task-irrelevant objects and backgrounds.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

Various empirical attempts have been made to bypass observation reconstruction. Apart from observation, the interaction involves two other variables: actions (control inputs) and costs. Inverse model methods reconstruct actions; while other methods rely on costs. We argue that since neither the reconstruction function nor the inverse model is used for policy learning, cost-driven state representation learning is the most *direct* one, in that costs are directly relevant for control purposes. In this work, we aim to examine the soundness of this methodology in linear quadratic Gaussian (LQG) control, one of the most fundamental partially observable control models.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

Parallel to the empirical advances of learning for control from pixels, partially observable linear systems has been extensively studied in the context of learning for dynamic control. In this context, the state representation function is more formally referred to as a *filter*, the optimal one being the Kalman filter. Most existing *model-based* learning approaches for LQG control focus on the linear time-invariant (LTI) case, and are based on the idea of *learning Markov parameters*, the mapping from control inputs to observations. Hence, they need to predict observations by definition. Motivated by the empirical successes in control from pixels, we take a different, cost-driven route, in hope of avoiding reconstructing observations or control inputs.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Introduction", "weight": 1.5} -->

We focus on finite-horizon time-varying LQG control and address the following question: *Can cost-driven state representation learning provably solve LQG control?* This work answers the question in the affirmative, by establishing finite-sample guarantees for a cost-driven state representation learning method. We address the finite-horizon linear time-varying (LTV) setting in this Part I, and will move on to the infinite-horizon linear time-invariant (LTI) setting with additional technical challenges in Part II of the work.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Introduction", "weight": 1.5} -->

Challenges & Our techniques. To establish finite-sample guarantees, a major technical challenge is to deal with the *quadratic regression* problem in cost prediction, arising from the inherent quadratic form of the LQG cost. Directly solving for the state representation function involves *quartic* optimization; instead, we propose to solve a quadratic regression problem, followed by low-rank approximate factorization. The quadratic regression problem also appears in identifying the cost matrices, involving the concentration for random variables that are fourth powers of Gaussians. Our techniques to address these challenges may be of independent interest.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Introduction", "weight": 1.5} -->

Moreover, the first $\ell$-step *latent* states may not be adequately *excited* (with full-rank covariance), which results in the identification of the latent model only in *partial directions*. This poses a significant challenge for certifying the performance of the learned controller, as the learned latent model from which we synthesize the controller may be neither stable nor controllable. We overcome this challenge by analyzing state covariance mismatch using induction, showing that identifying only the *relevant directions* suffices for learning a near-optimal controller. This fact is reflected in the dependence on $\ell$ in the statement of Theorem 1.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Introduction", "weight": 1.5} -->

Lastly, the learned latent states and the errors in the learned latent states are *correlated* as they are both functions of the same observed trajectory. This challenge arises both in analyzing latent model identification and in certifying the performance of the learned controller. We tackle this challenge by modeling the errors as general correlated perturbations whose magnitudes are controlled by the errors in the learned state representation function.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Introduction", "weight": 1.5} -->

Implications. For practitioners, one takeaway is the benefit of predicting *multi-step cumulative* costs in cost-driven state representation learning. Whereas the cost at a single time step may not be revealing enough of the latent state, the cumulative cost across multiple steps can be. This is an intuitive idea for the control community, given the multi-step nature in the classical definitions of controllability and observability. Its effectiveness has also been empirically observed in MuZero in state representation learning for control, and our work can be viewed as a formal understanding of it in the LQG setting.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Assumption 1 (Uniform exponential stability)", "weight": 1.0} -->

Assumption 1. ‣ 2 Problem setup ‣ Cost-Driven Representation Learning for Linear Quadratic Gaussian Control: Part I") is standard in controlling LTV systems, satisfied by a stable LTI system. It essentially says that zero control is a stabilizing controller, and can be potentially relaxed to the assumption of *being given a stabilizing controller* as, where one can excite the system using the stabilizing controller plus Gaussian random noises.

<!-- chunk {"id": "body-0014", "role": "body", "section": "Assumption 1 (Uniform exponential stability)", "weight": 1.0} -->

Define the $\ell$-step controllability matrix for $\ell-1\leq t\leq T-1$, which reduces to the standard controllability matrix $[B,\ldots,A^{\ell-1}B]$ in the LTI setting. We make the following controllability assumption.

<!-- chunk {"id": "body-0015", "role": "body", "section": "Assumption 2 (Controllability)", "weight": 1.0} -->

Under zero noise, we have so Assumption 2. ‣ 2 Problem setup ‣ Cost-Driven Representation Learning for Linear Quadratic Gaussian Control: Part I") ensures that from any state $x$, there exist control inputs that drive the state to $0$ in $\ell$ steps, and $\nu$ ensures that the equation leading to them is well conditioned. We do not assume controllability for $0\leq t<\ell-1$, since we do not want to impose the constraint that $d_{u}>d_{x}$. This turns out to present a significant challenge for analyzing state representation function learning, latent model identification, and the performance of the overall policy, resulting in the separation at step $\ell$ in the sample complexity guarantees (see Theorem 1).

<!-- chunk {"id": "body-0016", "role": "body", "section": "Assumption 2 (Controllability)", "weight": 1.0} -->

The observability assumptions on $(A,C)$ and $(A,Q^{1/2})$ are standard in controlling LTI systems. To differentiate from the former, we call the latter *cost observability*, since it implies the states are observable through costs. Whereas Markov-parameter-based approaches need to assume $(A,C)$ observability to identify the system, our cost-driven approach does not. Here we deal with the more difficult problem of having only the scalar cost as the supervision signal (instead of the concatenation of all observations, as in Markov-parameter-based ones). Nevertheless, the notion of cost observability is still important for our approach, formally defined as follows.

<!-- chunk {"id": "body-0017", "role": "body", "section": "Assumption 3 (Cost observability)", "weight": 1.0} -->

For all $0\leq t\leq\ell-1$, $Q^{\ast}_{t}\succcurlyeq\mu^{2}I$. For all $\ell\leq t\leq T$, there exists $m>0$ such that the cost observability Gram matrix where $k=m\wedge(T-t+1)$.

<!-- chunk {"id": "body-0018", "role": "body", "section": "Assumption 3 (Cost observability)", "weight": 1.0} -->

This assumption ensures that without noises, if we start with a nonzero state, the cumulative cost becomes positive in $m$ steps. The special requirement for $0\leq t\leq\ell-1$ results from the difficulty in lacking controllability in these time steps. The following is a regularity assumption on system parameters.

<!-- chunk {"id": "body-0019", "role": "body", "section": "Assumption 4", "weight": 1.0} -->

Along with Assumption 1. ‣ 2 Problem setup ‣ Cost-Driven Representation Learning for Linear Quadratic Gaussian Control: Part I"), this assumption ensures that under control $u_{t}\sim\mathcal{N}(0,\sigma_{u}^{2}I)$ for all $t\geq 0$ with $\sigma_{u}=\mathcal{O}$, the covariance matrices $\mathrm{Cov}(x_{t})$ and $\mathrm{Cov}(y_{t})$ have operator norms bounded by $\mathcal{O}$ for all $t\geq 0$.

<!-- chunk {"id": "body-0020", "role": "body", "section": "Assumption 4", "weight": 1.0} -->

Then, $J(\pi):=\mathbb{E}^{\pi}[\sum_{t=0}^{T}c_{t}]$ is the expected cumulative cost under policy $\pi$, where the expectation is taken over the randomness in the process noises, observation noises, and controls (if the policy $\pi$ is stochastic). The objective of LQG control is to find a policy $\pi$ such that $J(\pi)$ is minimized.

<!-- chunk {"id": "body-0021", "role": "body", "section": "Assumption 4", "weight": 1.0} -->

We consider data-driven control in a partially observable LTV system (2.1) with unknown cost matrices $(Q^{\ast}_{t})_{t=0}^{T}$. For simplicity, we assume $(R^{\ast}_{t})_{t=0}^{T}$ is known, though our approaches can be readily generalized to the case where they are unknown; one can identify them in the quadratic regression (3.3).

<!-- chunk {"id": "body-0022", "role": "body", "section": "Latent model of finite-horizon time-varying LQG", "weight": 1.0} -->

Under the Kalman filter, the observation prediction error $i_{t+1}:=y_{t+1}-C^{\ast}_{t+1}(A^{\ast}_{t}z^{\ast}_{t}+B^{\ast}_{t}u_{t})$ is called an *innovation*. It is known that $i_{t}$ is independent of history $h_{t}$ and $(i_{t})_{t=1}^{T}$ are independent. Now we are ready to present the following proposition that represents the system in terms of the state estimates by the Kalman filter, which we shall refer to as the *latent model*.

<!-- chunk {"id": "body-0023", "role": "body", "section": "Methodology: Cost-driven state representation learning", "weight": 1.0} -->

State representation learning involves history data that contains samples of three variables: observation, control input, and cost. Each of them can potentially be used as a *supervision* signal, and be used to define a type of state representation learning algorithms. We summarize our categorization of the methods in the literature as follows.

<!-- chunk {"id": "body-0024", "role": "body", "section": "Methodology: Cost-driven state representation learning", "weight": 1.0} -->

*Predicting observations* defines the class of *observation-reconstruction-based* methods, including methods based on Markov parameters (mapping from control actions to observations) in linear systems and methods that learn a mapping from states to observations in more complex systems. This type of method tends to recover all state components.

<!-- chunk {"id": "body-0025", "role": "body", "section": "Methodology: Cost-driven state representation learning", "weight": 1.0} -->

*Predicting actions* defines the class of *inverse model* methods, where the control is predicted from states across different time steps. This type of method tends to recover the control-relevant state components.

<!-- chunk {"id": "body-0026", "role": "body", "section": "Methodology: Cost-driven state representation learning", "weight": 1.0} -->

*Predicting (cumulative) costs* defines the class of *cost-driven state representation learning* methods. This type of methods tend to recover the state components relevant to the cost.

<!-- chunk {"id": "body-0027", "role": "body", "section": "Methodology: Cost-driven state representation learning", "weight": 1.0} -->

Our method falls into the cost-driven category. Compared with Markov parameter-based approaches for linear systems, our approach directly parameterizes the state representation function, without exploiting the structure of the Kalman filter, making our approach closer to empirical practice that was designed for general RL settings.

<!-- chunk {"id": "body-0028", "role": "body", "section": "Methodology: Cost-driven state representation learning", "weight": 1.0} -->

Subramanian et al. propose to optimize a simple combination of cost and transition prediction errors to learn what they call the *approximate information state*.

<!-- chunk {"id": "body-0029", "role": "body", "section": "Methodology: Cost-driven state representation learning", "weight": 1.0} -->

The optimization problem (3.1) is nonconvex; even if we can find a global minimizer, it is unclear how to establish finite-sample guarantees for it. A main finding of this work is that for LQG, we can solve the cost and transition loss optimization problems *sequentially*, with the caveat of using *cumulative* costs.

<!-- chunk {"id": "body-0030", "role": "body", "section": "Methodology: Cost-driven state representation learning", "weight": 1.0} -->

1:Input: sample size n, input noise magnitude σu = Θ, singular value threshold θ = Θ(n−1/4) (hiding dependence on other problem parameters) 2:Collect n trajectories using ut ∼ 𝒩(0, σu2I), for 0 ≤ t ≤ T − 1, to obtain data in the form of $\displaystyle\mathcal{D}_{\textnormal{raw}}=(y_{0}^{(i)},u_{0}^{(i)},c_{0}^{(i)},\ldots,y_{T-1}^{(i)},u_{T-1}^{(i)},c_{T-1}^{(i)},y_{T}^{(i)},c_{T}^{(i)})_{i=1}^{n}$ 3:Run Algorithm 2 with $\mathcal{D}_{\textnormal{raw}}$ and θ to obtain state representation function estimate (M̂t)t = 0T and latent

<!-- chunk {"id": "body-0031", "role": "body", "section": "Methodology: Cost-driven state representation learning", "weight": 1.0} -->

Rt*)t = 0T − 1, (Q̂t)t = 0T) by RDE (2.6) Algorithm 1 CoReL: Cost-driven state representation learning Our method is summarized in CoReL (Algorithm 1). It has three steps: cost-driven state representation function learning (Algorithm 2), latent system identification (Algorithm 3), and planning by RDE (2.6).

<!-- chunk {"id": "body-0032", "role": "body", "section": "Methodology: Cost-driven state representation learning", "weight": 1.0} -->

This three-step approach is very similar to the World Model approach used in empirical RL, except that in the first step, instead of using an autoencoder to learn the state representation function, we use cost values to supervise the representation learning. Most empirical state representation learning methods use cost supervision as one loss term; the special structure of LQG allows us to use it alone and have theoretical guarantees.

<!-- chunk {"id": "body-0033", "role": "body", "section": "Methodology: Cost-driven state representation learning", "weight": 1.0} -->

Algorithm 2 is the core of our algorithm. Once the state representation function $(\hat{M}_{t})_{t=0}^{T}$ is obtained, Algorithm 3 identifies the latent model using linear and quadratic regressions, followed by planning using RDE (2.6) to obtain the controller $(\hat{K}_{t})_{t=0}^{T-1}$ from $((\hat{A}_{t},\hat{B}_{t},R^{\ast}_{t})_{t=0}^{T-1},(\hat{Q}_{t})_{t=0}^{T})$. Algorithm 3 consists of the standard regression procedures. We explain Algorithm 2 below.

<!-- chunk {"id": "body-0034", "role": "body", "section": "Learning the state representation function", "weight": 1.0} -->

1:Input: raw data $\mathcal{D}_{\textnormal{raw}}$, singular value threshold θ 2:Estimate the state representation function and cost constants by solving (N̂t, b̂t)t = 0T∈

<!-- chunk {"id": "body-0035", "role": "body", "section": "Learning the state representation function", "weight": 1.0} -->

argminM ∈ ℝdx × ((t + 1)dy + tdu)∥M⊤M − N̂t∥F 4:For all 0 ≤ t ≤ ℓ − 1, set $\hat{M}_{t}=\textsc{TruncSV}{}(\widetilde{M}_{t},\theta)$; for all ℓ ≤ t ≤ T, set M̂t = M̃t 5:Compute ẑt(i) = M̂t[y0: t(i); u0: (t − 1)(i)] for all t = 0, …, T and i = 1, …, n 6:Return: state representation function estimate (M̂t)t = 0T and latent state estimates (ẑt(i))t = 0, i = 1T, n Algorithm 2 Cost-driven state representation function learning 1:Input: data in the form of (ẑ0(i), u0(i), c0(i), …, ẑT − 1(i), uT − 1(i), cT − 1(i), ẑT(i), cT(i))i = 1n 2:Estimate the

<!-- chunk {"id": "body-0036", "role": "body", "section": "Learning the state representation function", "weight": 1.0} -->

$\displaystyle\operatorname*{argmin}_{Q_{t}=Q_{t}^{\top},b_{t}}\sum_{i=1}^{n}(\|\hat{z}_{t}^{(i)}\|_{Q_{t}}^{2}+\|u_{t}^{(i)}\|_{R^{\ast}_{t}}^{2}+b_{t}-c_{t}^{(i)})^{2},$ and set Q̂t = Umax (Λ, 0)U⊤, where Q̃t = UΛU⊤ is its eigenvalue decomposition 5:Return: system parameters ((Ât, B̂t)t = 0T − 1, (Q̂t)t = 0T) Algorithm 3 Latent model identification The state representation function is learned via Algorithm 2. Given the raw data consisting of $n$ trajectories, Algorithm 2 first solves the regression problem (3.3) to recover the symmetric matrix

<!-- chunk {"id": "body-0037", "role": "body", "section": "Learning the state representation function", "weight": 1.0} -->

The target $\overline{c}_{t}$ of regression (3.3) is defined by where $k=1$ for $0\leq t\leq\ell-1$ and $k=m\wedge(T-t+1)$ for $\ell\leq t\leq T$. The superscript in $\overline{c}_{t}^{(i)}$ denotes the observed $\overline{c}_{t}$ in the $i$th trajectory. The quadratic regression has a closed-form solution, by converting it to linear regression using $\|v\|_{P}^{2}=\left\langle vv^{\top},P\right\rangle_{F}=\left\langle\mathrm{svec}(vv^{\top}),\mathrm{svec}(P)\right\rangle$.

<!-- chunk {"id": "body-0038", "role": "body", "section": "Learning the state representation function", "weight": 1.0} -->

The normalized parameterization. Still, since $\overline{Q}^{\ast}_{t}$ is unknown, even if we recover $(M^{\ast}_{t})^{\top}\overline{Q}^{\ast}_{t}M^{\ast}_{t}$ as a whole, it is not viable to extract $M^{\ast}_{t}$ and $\overline{Q}^{\ast}_{t}$. Such ambiguity is unavoidable; in fact, for every $\overline{Q}^{\ast}_{t}$ we choose, there is an equivalent parameterization of the system such that the system response is exactly the same. In partially observable LTI systems, it is well-known that the system parameters can only be recovered up to a similarity transform. Since every parameterization is correct, we simply choose $\overline{Q}^{\ast}_{t}=I$, which we refer to as the *normalized parameterization*.

<!-- chunk {"id": "body-0039", "role": "body", "section": "Learning the state representation function", "weight": 1.0} -->

Concretely, let us define $x^{\prime}_{t}=(\overline{Q}^{\ast}_{t})^{1/2}x_{t}$. Then, the new parameterization is given by and $c^{\prime}_{T}(x^{\prime})=\|x^{\prime}\|_{(Q^{\ast}_{T})^{\prime}}^{2}$, where for all $t\geq 0$, One can verify that under the normalized parameterization, the system satisfies Assumptions 1. ‣ 2 Problem setup ‣ Cost-Driven Representation Learning for Linear Quadratic Gaussian Control: Part I"), 2. ‣ 2 Problem setup ‣ Cost-Driven Representation Learning for Linear Quadratic Gaussian Control: Part I"), 3. ‣ 2 Problem setup ‣ Cost-Driven Representation Learning for Linear Quadratic Gaussian Control: Part I"), and 4, up to a change of some constants in the bounds.

<!-- chunk {"id": "body-0040", "role": "body", "section": "Learning the state representation function", "weight": 1.0} -->

Without loss of generality, we assume system (2.1) is in the normalized parameterization.

<!-- chunk {"id": "body-0041", "role": "body", "section": "Learning the state representation function", "weight": 1.0} -->

Why singular value truncation in the first $\ell$ steps? The latent states are used to identify the latent system dynamics, so whether they are sufficiently excited, namely having full-rank covariance, makes a big difference: if not, the system matrices can only be identified partially. Proposition 2 below confirms that the optimal latent state $z^{\ast}_{t}=M^{\ast}_{t}h_{t}$ indeed has full-rank covariance for $t\geq\ell$.

<!-- chunk {"id": "body-0042", "role": "body", "section": "Assumption 5", "weight": 1.0} -->

Still, for $0\leq t\leq\ell-1$, Assumption 5 does not guarantee the full-rankness of $\mathrm{Cov}(\widetilde{M}_{t}h_{t})$, not even a lower bound on its minimum positive singular value; that is why we introduce TruncSV that truncates the singular values of $\widetilde{M}_{t}$ by a threshold $\theta>0$. Concretely, we take $\hat{M}_{t}=(\mathbb{I}_{\theta,+\infty)}(\Sigma_{d_{x}}^{1/2})\odot\Sigma_{d_{x}}^{1/2})U_{d_{x}}^{\top}$. Then, $\hat{M}_{t}$ has the same singular values as $\widetilde{M}_{t}$ except that those below $\theta$ are zeroed.

<!-- chunk {"id": "body-0043", "role": "body", "section": "Assumption 5", "weight": 1.0} -->

We take $\theta=\Theta(\ell^{3/2}(d_{y}+d_{u})d_{x}^{3/4}n^{-1/4}\log^{1/4}(\ell/p))$ to ensure a sufficient lower bound on the minimum positive singular value of $\hat{M}_{t}$, without increasing the statistical errors.

<!-- chunk {"id": "body-0044", "role": "body", "section": "Theoretical guarantees and proofs", "weight": 1.0} -->

Theorem [1 below offers a finite-sample guarantee for our approach, confirming cost-driven state representation learning (Algorithm 1) as a viable path to solving LQG control.

<!-- chunk {"id": "body-0045", "role": "body", "section": "Quadratic regression bound", "weight": 1.0} -->

As noted in §3.1, the quadratic regression can be converted to linear regression using $\|h\|_{P}^{2}=\left\langle hh^{\top},P\right\rangle_{F}=\left\langle\mathrm{svec}(hh^{\top}),\mathrm{svec}(P)\right\rangle$. To analyze this linear regression with an intercept, we need the following lemma. We note that a similar lemma without considering the intercept has been proved.

<!-- chunk {"id": "body-0046", "role": "body", "section": "Matrix factorization bound", "weight": 1.0} -->

Given two $m\times n$ matrices $A,B$, we are interested in bounding $\min_{S^{\top}S=I}\|SA-B\|_{F}$ using $\|A^{\top}A-B^{\top}B\|_{F}$. The minimum problem is known as the orthogonal Procrustes problem, solved. Specifically, the minimum is attained at $S=UV^{\top}$, where $U\Sigma V^{\top}=BA^{\top}$ is its singular value decomposition.

<!-- chunk {"id": "body-0047", "role": "body", "section": "Matrix factorization bound", "weight": 1.0} -->

If $m\leq n$ and $\mathrm{rank}(A)=m$, then the following lemma from establishes that the distance between $A$ and $B$ is of the same order of $\|A^{\top}A-B^{\top}B\|_{F}$.

<!-- chunk {"id": "body-0048", "role": "body", "section": "Perturbed linear regression bound", "weight": 1.0} -->

Identifying the dynamics of the latent model requires solving linear regression (3.4). A standard assumption in analyzing linear regression $y=A^{\ast}x+e$ is that $\mathrm{Cov}(x)$ has *full rank*. However, as discussed in §3.1, we need to handle rank-deficient $\mathrm{Cov}(x)$ in the first $\ell$ steps of system identification. Moreover, the latent state estimates $\hat{z}_{t}$ contain errors. Both issues are addressed in the following lemma.

<!-- chunk {"id": "body-0049", "role": "body", "section": "Claim 1", "weight": 1.0} -->

As long as $n\geq 16(d_{1}+d_{2}+\log(1/p))$, with probability at least $1-4p$, The proof of Claim 1 is deferred to §4.4.1, where we analyze the inversion of $X^{\top}X$. Note that we may also bound $\|\hat{A}\|_{2}$ by analyzing the inversion of $DG^{\top}GD^{\top}$, potentially without the requirement on $\theta$, but this requires stronger condition on $\epsilon_{x}$ and $\epsilon_{y}$, and the bound is not directly applicable to the minimum Frobenius norm solution. The requirement on $\theta$ remains beneficial for numerical stability.

<!-- chunk {"id": "body-0050", "role": "body", "section": "Certainty equivalent linear quadratic control", "weight": 1.0} -->

As shown in Lemma 5. ‣ 4.4 Perturbed linear regression bound ‣ 4 Theoretical guarantees and proofs ‣ Cost-Driven Representation Learning for Linear Quadratic Gaussian Control: Part I"), if the input of linear regression does not have full-rank covariance, then the parameters can only be identified in certain directions. The following lemma studies the performance of the certainty equivalent optimal controller in this case.

<!-- chunk {"id": "body-0051", "role": "body", "section": "Claim 2", "weight": 1.0} -->

For any $K$ and $t\geq 0$, there exists some dimension-free $\varrho_{t}>0$ that depends on $K$ and other problem parameters, such that $\Xi_{t}(K)\preccurlyeq\varrho_{t}\Sigma_{t}$.

<!-- chunk {"id": "body-0052", "role": "body", "section": "Claim 3", "weight": 1.0} -->

The proof of Claim 3 is deferred to §4.5.2. A core idea of the proof is to use inverse telescoping to express $\Xi_{t}(K)-\hat{\Xi}_{t}(K)$.

<!-- chunk {"id": "body-0053", "role": "body", "section": "Concluding remarks", "weight": 1.0} -->

We examined the cost-driven state representation learning methods in time-varying LQG control. With a finite-sample analysis, we showed that a direct, cost-driven state representation learning algorithm effectively solves LQG. In the analysis, we revealed the importance of using multi-step cumulative costs as the supervision signal, and the dependence on $\ell$, the controllability index, due to early-stage insufficient excitement of the system. For the same reason, our policy suboptimality gap has a significantly worsened dependence on $\ell$, as the latent model can only be partially identified, and the learned latent model may not be stable. Hence, an immediate question is how we can learn a stable latent model to improve the dependence on $\ell$. A major limitation of our method is the use of history-based state representation functions; recovering the recursive Kalman filter would be ideal.

<!-- chunk {"id": "body-0054", "role": "body", "section": "Concluding remarks", "weight": 1.0} -->

In Part II of this work, we will explore how the cost-driven state representation learning approach performs in the infinite-horizon LTI setting, as well as discuss more opportunities that this work has opened up for future research.
