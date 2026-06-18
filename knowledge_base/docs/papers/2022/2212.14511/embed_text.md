## Introduction

We consider state representation learning for control in partially observable systems, inspired by the recent successes of *control from pixels*. Control from pixels is an everyday task for human beings, but it remains challenging for learning agents. Methods to achieve it generally fall into two main categories: *model-free* and *model-based* ones. Model-free methods directly learn a visuomotor policy, also known as direct reinforcement learning (RL). On the other hand, model-based methods, also known as indirect RL, attempt to learn a *latent model* that is a compact representation of the system, and to synthesize a policy in the latent model. Compared with model-free methods, model-based ones facilitate generalization across tasks and enable efficient planning, and are sometimes more sample efficient than the model-free ones.

In latent-model-based control, the state of the latent model is also referred to as a *state representation* in the deep RL literature, and the mapping from an observed history to a latent state is referred to as the (state) representation function. *Reconstructing the observation* often serves as a supervision for representation learning for control in the empirical RL literature. This is in sharp contrast to model-free methods, where the policy improvement step is completely *cost-driven*. Reconstructing observations provides a rich supervision signal for learning a task-agnostic world model, but they are high-dimensional and noisy, so the reconstruction requires an expressive reconstruction function; latent states learned by reconstruction contain irrelevant information for control, which can distract RL algorithms. This is especially the case for practical visuomotor control tasks, e.g., robotic manipulation and self-driving cars, where the visual images contain predominately task-irrelevant objects and backgrounds.

Various empirical attempts have been made to bypass observation reconstruction. Apart from observation, the interaction involves two other variables: actions (control inputs) and costs. Inverse model methods reconstruct actions; while other methods rely on costs. We argue that since neither the reconstruction function nor the inverse model is used for policy learning, cost-driven state representation learning is the most *direct* one, in that costs are directly relevant for control purposes. In this work, we aim to examine the soundness of this methodology in linear quadratic Gaussian (LQG) control, one of the most fundamental partially observable control models.

Parallel to the empirical advances of learning for control from pixels, partially observable linear systems has been extensively studied in the context of learning for dynamic control. In this context, the state representation function is more formally referred to as a *filter*, the optimal one being the Kalman filter. Most existing *model-based* learning approaches for LQG control focus on the linear time-invariant (LTI) case, and are based on the idea of *learning Markov parameters*, the mapping from control inputs to observations. Hence, they need to predict observations by definition. Motivated by the empirical successes in control from pixels, we take a different, cost-driven route, in hope of avoiding reconstructing observations or control inputs.

We focus on finite-horizon time-varying LQG control and address the following question:

*Can cost-driven state representation learning provably solve LQG control?*

This work answers the question in the affirmative, by establishing finite-sample guarantees for a cost-driven state representation learning method. We address the finite-horizon linear time-varying (LTV) setting in this Part I, and will move on to the infinite-horizon linear time-invariant (LTI) setting with additional technical challenges in Part II of the work.

Challenges & Our techniques. To establish finite-sample guarantees, a major technical challenge is to deal with the *quadratic regression* problem in cost prediction, arising from the inherent quadratic form of the LQG cost. Directly solving for the state representation function involves *quartic* optimization; instead, we propose to solve a quadratic regression problem, followed by low-rank approximate factorization. The quadratic regression problem also appears in identifying the cost matrices, involving the concentration for random variables that are fourth powers of Gaussians. Our techniques to address these challenges may be of independent interest.

Moreover, the first $\ell$-step *latent* states may not be adequately *excited* (with full-rank covariance), which results in the identification of the latent model only in *partial directions*. This poses a significant challenge for certifying the performance of the learned controller, as the learned latent model from which we synthesize the controller may be neither stable nor controllable. We overcome this challenge by analyzing state covariance mismatch using induction, showing that identifying only the *relevant directions* suffices for learning a near-optimal controller. This fact is reflected in the dependence on $\ell$ in the statement of Theorem 1.

Lastly, the learned latent states and the errors in the learned latent states are *correlated* as they are both functions of the same observed trajectory. This challenge arises both in analyzing latent model identification and in certifying the performance of the learned controller. We tackle this challenge by modeling the errors as general correlated perturbations whose magnitudes are controlled by the errors in the learned state representation function.

Implications. For practitioners, one takeaway is the benefit of predicting *multi-step cumulative* costs in cost-driven state representation learning. Whereas the cost at a single time step may not be revealing enough of the latent state, the cumulative cost across multiple steps can be. This is an intuitive idea for the control community, given the multi-step nature in the classical definitions of controllability and observability. Its effectiveness has also been empirically observed in MuZero in state representation learning for control, and our work can be viewed as a formal understanding of it in the LQG setting.

Notation. We use $0$ (resp. $1$) to denote either the scalar or a matrix consisting of all zeros (resp. all ones); we use $I$ to denote an identity matrix. The dimension, when emphasized, is specified in subscripts, e.g., $0_{d_{x} \times d_{x}},1_{d_{x}},I_{d_{x}}$. Let ${\mathbb{I}}_{S}$ denote the indicator function for set $S$ and ${\mathbb{I}}_{S}{(A)}$ apply to matrix $A$ elementwise. For some positive semidefinite $P$, we define ${\| v\|}_{P}:={({v^{\top}Pv})}^{1/2}$. Semicolon ";" denotes stacking vectors or matrices vertically. For a collection of $d$-dimensional vectors ${(v_{t})}_{t = i}^{j}$, let $v_{i:j}:={\lbrack v_{i};v_{i + 1};\ldots;v_{j}\rbrack} \in {\mathbb{R}}^{d{({{j - i} + 1})}}$ denote the concatenation along the column. For random variable $\eta$, let ${\|\eta\|}_{\psi_{\beta}}$ denote its $\beta$-sub-Weibull norm, a special case of Orlicz norms, with $\beta = {1,2}$ corresponding to subexponential and sub-Gaussian norms. For matrix $A$, let ${\sigma_{i}{(A)}},{\sigma_{\min}{(A)}},{\sigma_{\min}^{+}{(A)}},{\sigma_{\max}{(A)}}$ denote its $i$th largest, minimum, minimum positive, maximum singular values, respectively. ${\| A\|}_{2},{\| A\|}_{F},{\| A\|}_{\ast}$ denote the operator (induced by vector $2$-norms), Frobenius, nuclear norms of matrix $A$, respectively. $\left\langle \cdot, \cdot \right\rangle_{F}$ denotes the Frobenius inner product between matrices. For square matrix $A$, let $\lambda_{\min}{(A)}$ be its minimum eigenvalue. The Kronecker, symmetric Kronecker, and Hadamard products between matrices are denoted by "$\otimes$", "$\otimes_{s}$" and "$\odot$", respectively. ${vec}{( \cdot )}$ and ${svec}{( \cdot )}$ denote flattening a matrix and a symmetric matrix by stacking their columns; ${svec}{( \cdot )}$ does not repeat the off-diagonal elements, but scales them by $\sqrt{2}$. Let $\text{diag}{( \cdot )}$ denote the block diagonal matrix formed by the matrices inside the parentheses. For $\Sigma_{i = a}^{b}$, we define the sum to be zero if the lower index $a$ is greater than the upper index $b$.

## Problem setup

We study a partially observable linear dynamical system

for $t = {0,1,\ldots,{T - 1}}$ and $y_{T} = {{C_{T}^{\ast}x_{T}} + v_{T}}$. For all $t \geq 0$, we have the notation of state $x_{t} \in {\mathbb{R}}^{d_{x}}$, observation $y_{t} \in {\mathbb{R}}^{d_{y}}$, and control input $u_{t} \in {\mathbb{R}}^{d_{u}}$. Process noises ${(w_{t})}_{t = 0}^{T - 1}$ and observation noises ${(v_{t})}_{t = 0}^{T}$ are i.i.d. sampled from $\mathcal{N}{(0,\Sigma_{w_{t}})}$ and $\mathcal{N}{(0,\Sigma_{v_{t}})}$, respectively. Let initial state $x_{0}$ be sampled from $\mathcal{N}{(0,\Sigma_{0})}$.

Let $\Phi_{t,t_{0}} = {A_{t - 1}^{\ast}A_{t - 2}^{\ast}\cdotsA_{t_{0}}^{\ast}}$ for $t > t_{0}$ and $\Phi_{t,t} = I$. Then $x_{t} = {{\Phi_{t,t_{0}}x_{t_{0}}} + {\sum_{\tau = t_{0}}^{t - 1}{\Phi_{t,{\tau + 1}}w_{\tau}}}}$ under zero control input. To ensure the state and the cumulative noise do not grow with time, we make the following uniform exponential stability assumption.

### Assumption 1 (Uniform exponential stability)

The system is uniformly exponentially stable, i.e., there exists ${\alpha > 0},{\rho \in {}}$ such that for any $0 \leq t_{0} < t \leq T$, ${\|\Phi_{t,t_{0}}\|}_{2} \leq {\alpha\rho^{t - t_{0}}}$.

Assumption 1. ‣ 2 Problem setup ‣ Cost-Driven Representation Learning for Linear Quadratic Gaussian Control: Part I") is standard in controlling LTV systems, satisfied by a stable LTI system. It essentially says that zero control is a stabilizing controller, and can be potentially relaxed to the assumption of *being given a stabilizing controller* as in, where one can excite the system using the stabilizing controller plus Gaussian random noises.

Define the $\ell$-step controllability matrix

for ${\ell - 1} \leq t \leq {T - 1}$, which reduces to the standard controllability matrix $\lbrack B,\ldots,{A^{\ell - 1}B}\rbrack$ in the LTI setting. We make the following controllability assumption.

### Assumption 2 (Controllability)

For all ${\ell - 1} \leq t \leq {T - 1}$, ${{rank}{(\Phi_{t,\ell}^{c})}} = d_{x}$, ${\sigma_{\min}{(\Phi_{t,\ell}^{c})}} \geq \nu > 0$.

Under zero noise, we have

so Assumption 2. ‣ 2 Problem setup ‣ Cost-Driven Representation Learning for Linear Quadratic Gaussian Control: Part I") ensures that from any state $x$, there exist control inputs that drive the state to $0$ in $\ell$ steps, and $\nu$ ensures that the equation leading to them is well conditioned. We do not assume controllability for $0 \leq t < {\ell - 1}$, since we do not want to impose the constraint that $d_{u} > d_{x}$. This turns out to present a significant challenge for analyzing state representation function learning, latent model identification, and the performance of the overall policy, resulting in the separation at step $\ell$ in the sample complexity guarantees (see Theorem 1).

The quadratic cost functions are given by

where ${(Q_{t}^{\ast})}_{t = 0}^{T}$ are positive semidefinite matrices and ${(R_{t}^{\ast})}_{t = 0}^{T - 1}$ are positive definite matrices. Sometimes the cost is defined as a function of the observation $y$. Since the quadratic form ${y^{\top}Q_{t}^{\ast}y} = {x^{\top}{(C_{t}^{\ast})}^{\top}Q_{t}^{\ast}C_{t}^{\ast}x}$, our analysis still applies if the assumptions on ${(Q_{t}^{\ast})}_{t = 0}^{T}$ hold for ${({{(C_{t}^{\ast})}^{\top}Q_{t}^{\ast}C_{t}^{\ast}})}_{t = 0}^{T}$ instead.

The observability assumptions on $(A,C)$ and $(A,Q^{1/2})$ are standard in controlling LTI systems. To differentiate from the former, we call the latter *cost observability*, since it implies the states are observable through costs. Whereas Markov-parameter-based approaches need to assume $(A,C)$ observability to identify the system, our cost-driven approach does not. Here we deal with the more difficult problem of having only the scalar cost as the supervision signal (instead of the concatenation of all observations, as in Markov-parameter-based ones). Nevertheless, the notion of cost observability is still important for our approach, formally defined as follows.

### Assumption 3 (Cost observability)

For all $0 \leq t \leq {\ell - 1}$, $Q_{t}^{\ast} \succcurlyeq {\mu^{2}I}$. For all $\ell \leq t \leq T$, there exists $m > 0$ such that the cost observability Gram matrix

This assumption ensures that without noises, if we start with a nonzero state, the cumulative cost becomes positive in $m$ steps. The special requirement for $0 \leq t \leq {\ell - 1}$ results from the difficulty in lacking controllability in these time steps. The following is a regularity assumption on system parameters.

### Assumption 4

${({\lambda_{\min}{(\Sigma_{v_{t}})}})}_{t = 0}^{T}$ and ${({\lambda_{\min}{(R_{t}^{\ast})}})}_{t = 0}^{T - 1}$ are uniformly lower bounded; that is, they are all $\Omega{}$. The operator norms of all matrices in the problem definition and ${(M_{t}^{\ast})}_{t = 0}^{T}$ to be defined in §2.1 are uniformly upper bounded, including ${(A_{t}^{\ast},B_{t}^{\ast},R_{t}^{\ast},\Sigma_{w_{t}})}_{t = 0}^{T - 1}$, ${(C_{t}^{\ast},Q_{t}^{\ast},\Sigma_{v_{t}})}_{t = 0}^{T}$; that is, they are all $\mathcal{O}{}$.

Along with Assumption 1. ‣ 2 Problem setup ‣ Cost-Driven Representation Learning for Linear Quadratic Gaussian Control: Part I"), this assumption ensures that under control $u_{t} \sim {\mathcal{N}{(0,{\sigma_{u}^{2}I})}}$ for all $t \geq 0$ with $\sigma_{u} = {\mathcal{O}{}}$, the covariance matrices ${Cov}{(x_{t})}$ and ${Cov}{(y_{t})}$ have operator norms bounded by $\mathcal{O}{}$ for all $t \geq 0$. Moreover, ${(S_{t}^{\ast},L_{t}^{\ast},P_{t}^{\ast})}_{t = 0}^{T}$ and ${(K_{t}^{\ast})}_{t = 0}^{T - 1}$, to be defined shortly in (2.3) to (2.6) in the optimal solution, have $\mathcal{O}{}$ operator norms.

Let $h_{t}:={\lbrack y_{0:t};u_{0:{({t - 1})}}\rbrack} \in {\mathbb{R}}^{{{({t + 1})}d_{y}} + {td_{u}}}$ denote the available history before deciding control $u_{t}$ for $t \geq 1$ and define $h_{0}:=y_{0}$. A policy $\pi = {(\pi_{t}:h_{t}\mapsto u_{t})}_{t = 0}^{T - 1}$ determines at time $t$ a control input $u_{t}$ based on history $h_{t}$. With a slight abuse of notation, let $c_{t}:={c_{t}{(x_{t},u_{t})}}$ for $0 \leq t \leq {T - 1}$ and $c_{T}:={c_{T}{(x_{T})}}$ denote the cost at each time step. Then, ${J{(\pi)}}:={{\mathbb{E}}^{\pi}{\lbrack{\sum_{t = 0}^{T}c_{t}}\rbrack}}$ is the expected cumulative cost under policy $\pi$, where the expectation is taken over the randomness in the process noises, observation noises, and controls (if the policy $\pi$ is stochastic). The objective of LQG control is to find a policy $\pi$ such that $J{(\pi)}$ is minimized.

If the system parameters $({(A_{t}^{\ast},B_{t}^{\ast},R_{t}^{\ast})}_{t = 0}^{T - 1},{(C_{t}^{\ast},Q_{t}^{\ast})}_{t = 0}^{T})$ are known, optimal control is obtained by combining the Kalman filter $z_{0}^{\ast} = {L_{0}^{\ast}y_{0}}$,

for $0 \leq t \leq {T - 1}$, with the optimal feedback control gains of the linear quadratic regulator (LQR) ${(K_{t}^{\ast})}_{t = 0}^{T - 1}$ such that $u_{t}^{\ast} = {K_{t}^{\ast}z_{t}^{\ast}}$, where ${(L_{t}^{\ast})}_{t = 0}^{T}$ are the Kalman gains; this is known as the *separation principle*. The Kalman gains and optimal feedback control gains are given by

where $S_{t}^{\ast}$ and $P_{t}^{\ast}$ are determined by their corresponding Riccati difference equations (RDEs):

with $S_{0}^{\ast} = \Sigma_{0}$ and $P_{T}^{\ast} = Q_{T}^{\ast}$.

We consider data-driven control in a partially observable LTV system (2.1) with unknown cost matrices ${(Q_{t}^{\ast})}_{t = 0}^{T}$. For simplicity, we assume ${(R_{t}^{\ast})}_{t = 0}^{T}$ is known, though our approaches can be readily generalized to the case where they are unknown; one can identify them in the quadratic regression (3.3).

### Latent model of finite-horizon time-varying LQG

Under the Kalman filter, the observation prediction error $i_{t + 1}:={y_{t + 1} - {C_{t + 1}^{\ast}{({{A_{t}^{\ast}z_{t}^{\ast}} + {B_{t}^{\ast}u_{t}}})}}}$ is called an *innovation*. It is known that $i_{t}$ is independent of history $h_{t}$ and ${(i_{t})}_{t = 1}^{T}$ are independent. Now we are ready to present the following proposition that represents the system in terms of the state estimates by the Kalman filter, which we shall refer to as the *latent model*.

### Proposition 1

Let ${(z_{t}^{\ast})}_{t = 0}^{T}$ be state estimates given by the Kalman filter. Then,

where $L_{t + 1}^{\ast}i_{t + 1}$ is independent of $z_{t}^{\ast}$ and $u_{t}$, i.e., the state estimates follow the same linear dynamics as the underlying state, with noises $L_{t + 1}^{\ast}i_{t + 1}$. The cost at step $t$ can then be reformulated as functions of the state estimates by

where $b_{t} > 0$ is a problem-dependent constant, and $\gamma_{t} = {{\|{x_{t} - z_{t}^{\ast}}\|}_{Q_{t}^{\ast}}^{2} - b_{t}}$, $\eta_{t} = {2\left\langle z_{t}^{\ast},{x_{t} - z_{t}^{\ast}} \right\rangle_{Q_{t}^{\ast}}}$ are both zero-mean subexponential random variables. Under Assumptions 1. ‣ 2 Problem setup ‣ Cost-Driven Representation Learning for Linear Quadratic Gaussian Control: Part I") and 4, $b_{t} = {\mathcal{O}{}}$ and ${\|\gamma_{t}\|}_{\psi_{1}} = {\mathcal{O}{(d_{x}^{1/2})}}$; moreover, if control $u_{t} \sim {\mathcal{N}{(0,{\sigma_{u}^{2}I})}}$ for $0 \leq t \leq T$, then ${\|\eta_{t}\|}_{\psi_{1}} = {\mathcal{O}{(d_{x}^{1/2})}}$.

### Proof

By the property of the Kalman filter, $z_{t}^{\ast} = {{\mathbb{E}}{\lbrack\left. x_{t} \middle| {y_{0:t},u_{0:{({t - 1})}}} \right.\rbrack}}$ is a function of the past history $(y_{0:t},u_{0:{({t - 1})}})$. Action $u_{t}$ is a function of the past history $(y_{0:t},u_{0:{({t - 1})}})$ and may contain noise independent of all other random variables. Innovation $i_{t + 1} = {{C_{t + 1}^{\ast}{({{A_{t}^{\ast}{({x_{t} - z_{t}^{\ast}})}} + w_{t}})}} + v_{t + 1}}$ is independent of the past history $(y_{0:t},u_{0:{({t - 1})}})$; hence, it is independent of $z_{t}^{\ast}$ and $u_{t}$. For the cost function,

Let $b_{t} = {{\mathbb{E}}{\lbrack{\|{x_{t} - z_{t}^{\ast}}\|}_{Q_{t}^{\ast}}^{2}\rbrack}}$ be a constant that depends on system parameters ${(A_{t}^{\ast},B_{t}^{\ast},\Sigma_{w_{t}})}_{t = 0}^{T - 1}$, ${(C_{t}^{\ast},\Sigma_{v_{t}})}_{t = 0}^{T}$ and $\Sigma_{0}$. Then, random variable $\gamma_{t}:={{\|{x_{t} - z_{t}^{\ast}}\|}_{Q_{t}^{\ast}}^{2} - b_{t}}$ has zero mean. Since $({x_{t} - z_{t}^{\ast}})$ is Gaussian, its squared norm is subexponential. Since $z_{t}^{\ast}$ and $({x_{t} - z_{t}^{\ast}})$ are independent zero-mean Gaussian random vectors, their inner product, and hence $\eta_{t}$, are zero-mean subexponential random variables.

If the system is uniformly exponentially stable (Assumption 1. ‣ 2 Problem setup ‣ Cost-Driven Representation Learning for Linear Quadratic Gaussian Control: Part I")) and the system parameters are regular (Assumption 4), then ${(S_{t}^{\ast})}_{t = 0}^{T}$ given by RDE (2.5) has a bounded operator norm determined by system parameters ${(A_{t}^{\ast},B_{t}^{\ast},C_{t}^{\ast},\Sigma_{w_{t}})}_{t = 0}^{T - 1}$, ${(\Sigma_{v_{t}})}_{t = 0}^{T}$ and $\Sigma_{0}$. Since $S_{t}^{\ast} = {{Cov}{({x_{t} - z_{t}^{\ast}})}}$, ${\|\gamma_{t}\|}_{\psi_{1}} = {\mathcal{O}{(d_{x}^{1/2})}}$ by Lemma 11. By Assumption 1. ‣ 2 Problem setup ‣ Cost-Driven Representation Learning for Linear Quadratic Gaussian Control: Part I"), if we apply zero control to the system, then ${\|{{Cov}{(z_{t}^{\ast})}}\|}_{2} = {\mathcal{O}{}}$. By Lemma 11, $\eta_{t} = {2\left\langle z_{t}^{\ast},{x_{t} - z_{t}^{\ast}} \right\rangle_{Q_{t}^{\ast}}}$ satisfies ${\|\eta_{t}\|}_{\psi_{1}} = {\mathcal{O}{(d_{x}^{1/2})}}$. ∎

Proposition 1 states that: 1) the dynamics of the state estimates produced by the Kalman filter remains the same as the original system up to noises, determined by ${(A_{t}^{\ast},B_{t}^{\ast})}_{t = 0}^{T - 1}$; 2) the costs (of the latent model) are still determined by ${(Q_{t}^{\ast})}_{t = 0}^{T}$ and ${(R_{t}^{\ast})}_{t = 0}^{T - 1}$, up to constants and noises. Hence, a latent model can be parameterized by $({(A_{t},B_{t})}_{t = 0}^{T - 1},{(Q_{t})}_{t = 0}^{T})$ (recall that we assume ${(R_{t}^{\ast})}_{t = 0}^{T}$ is known for convenience). Note that observation matrices ${(C_{t}^{\ast})}_{t = 0}^{T}$ are *not* involved.

Now let us take a closer look at the state representation function. The Kalman filter can be written as $z_{t + 1}^{\ast} = {{{\overline{A}}_{t}^{\ast}z_{t}^{\ast}} + {{\overline{B}}_{t}^{\ast}u_{t}} + {L_{t + 1}^{\ast}y_{t + 1}}}$, where ${\overline{A}}_{t}^{\ast} = {{({I - {L_{t + 1}^{\ast}C_{t + 1}^{\ast}}})}A_{t}^{\ast}}$ and ${\overline{B}}_{t}^{\ast} = {{({I - {L_{t + 1}^{\ast}C_{t + 1}^{\ast}}})}B_{t}^{\ast}}$. For $0 \leq t \leq T$, unrolling the recursion yields

where $M_{t}^{\ast} \in {\mathbb{R}}^{d_{x} \times {({{{({t + 1})}d_{y}} + {td_{u}}})}}$. This means the optimal state representation function is *linear* in the history of observations and controls. A state representation function can then be parameterized by matrices ${(M_{t})}_{t = 0}^{T}$, and the latent state at step $t$ is given by $z_{t} = {M_{t}h_{t}}$.

Overall, a policy $\pi$ is a combination of state representation function ${(M_{t})}_{t = 0}^{T - 1}$ ($M_{T}$ is not needed) and feedback gain ${(K_{t})}_{t = 0}^{T - 1}$ in the latent model, so we write $\pi = {(M_{t},K_{t})}_{t = 0}^{T - 1}$ as the composition of the two, and let $\pi^{\ast} = {(M_{t}^{\ast},K_{t}^{\ast})}_{t = 0}^{T - 1}$ denote the optimal policy.

## Methodology: Cost-driven state representation learning

State representation learning involves history data that contains samples of three variables: observation, control input, and cost. Each of them can potentially be used as a *supervision* signal, and be used to define a type of state representation learning algorithms. We summarize our categorization of the methods in the literature as follows.

*Predicting observations* defines the class of *observation-reconstruction-based* methods, including methods based on Markov parameters (mapping from control actions to observations) in linear systems and methods that learn a mapping from states to observations in more complex systems. This type of method tends to recover all state components.

*Predicting actions* defines the class of *inverse model* methods, where the control is predicted from states across different time steps. This type of method tends to recover the control-relevant state components.

*Predicting (cumulative) costs* defines the class of *cost-driven state representation learning* methods. This type of methods tend to recover the state components relevant to the cost.

Our method falls into the cost-driven category. Compared with Markov parameter-based approaches for linear systems, our approach directly parameterizes the state representation function, without exploiting the structure of the Kalman filter, making our approach closer to empirical practice that was designed for general RL settings.

Subramanian et al. propose to optimize a simple combination of cost and transition prediction errors to learn what they call the *approximate information state*. That is, we parameterize a state representation function by matrices ${(M_{t})}_{t = 0}^{T}$ and a latent model by matrices $({(A_{t},B_{t})}_{t = 0}^{T - 1},{(Q_{t})}_{t = 0}^{T})$ and then solve

where ${(b_{t})}_{t = 0}^{T}$ are additional scalar parameters to account for noises, and the loss at step $t$ for trajectory $i$ is defined by

for $0 \leq t \leq {T - 1}$ and $l_{T}^{(i)} = \left( {{{\|{M_{T}h_{T}^{(i)}}\|}_{Q_{T}}^{2} + b_{T}} - c_{T}^{(i)}} \right)^{2}$. The optimization problem (3.1) is nonconvex; even if we can find a global minimizer, it is unclear how to establish finite-sample guarantees for it. A main finding of this work is that for LQG, we can solve the cost and transition loss optimization problems *sequentially*, with the caveat of using *cumulative* costs.

1:Input: sample size n, input noise magnitude σu = Θ, singular value threshold θ = Θ (n−1/4) (hiding dependence on other problem parameters)
2:Collect n trajectories using ut ∼ 𝒩 (0,σu2 I), for 0 ≤ t ≤ T − 1, to obtain data in the form of

3:Run Algorithm 2 with 𝒟raw and θ to obtain state representation function estimate (M̂t)t = 0T and latent state estimates (ẑt(i))t = 0, i = 1T, n, so that the data are converted to

4:Run Algorithm 3 with 𝒟state to obtain system parameter estimates ((Ât,B̂t)t = 0T − 1,(Q̂t)t = 0T)
5:Find feedback gains (K̂t)t = 0T − 1 from ((Ât,B̂t,Rt*)t = 0T − 1,(Q̂t)t = 0T) by RDE (2.6)
Algorithm 1 CoReL: Cost-driven state representation learning

Our method is summarized in CoReL (Algorithm 1). It has three steps: cost-driven state representation function learning (Algorithm 2), latent system identification (Algorithm 3), and planning by RDE (2.6).

This three-step approach is very similar to the World Model approach used in empirical RL, except that in the first step, instead of using an autoencoder to learn the state representation function, we use cost values to supervise the representation learning. Most empirical state representation learning methods use cost supervision as one loss term; the special structure of LQG allows us to use it alone and have theoretical guarantees.

Algorithm 2 is the core of our algorithm. Once the state representation function ${({\hat{M}}_{t})}_{t = 0}^{T}$ is obtained, Algorithm 3 identifies the latent model using linear and quadratic regressions, followed by planning using RDE (2.6) to obtain the controller ${({\hat{K}}_{t})}_{t = 0}^{T - 1}$ from $({({\hat{A}}_{t},{\hat{B}}_{t},R_{t}^{\ast})}_{t = 0}^{T - 1},{({\hat{Q}}_{t})}_{t = 0}^{T})$. Algorithm 3 consists of the standard regression procedures. We explain Algorithm 2 below.

### Learning the state representation function

1:Input: raw data 𝒟raw, singular value threshold θ
2:Estimate the state representation function and cost constants by solving (N̂t,b̂t)t = 0T∈

$${\operatorname{argmin}\limits_{{({N_{t} = {N_{t}^{\top},b_{t}}})}_{t = 0}^{T}}{\sum\limits_{t = 0}^{T}{\sum\limits_{i = 1}^{n}\left( {{\left\| {\lbrack y_{0:t}^{(i)};u_{0:{({t - 1})}}^{(i)}\rbrack} \right\|_{N_{t}}^{2} + {\sum\limits_{\tau = t}^{{t + k} - 1}{\| u_{\tau}^{(i)}\|}_{R_{\tau}^{\ast}}^{2}} + b_{t}} - {\overline{c}}_{t}^{(i)}} \right)^{2}}}},$$

where k = 1 for 0 ≤ t ≤ l − 1 and k = m ∧ (T − t+1) for ℓ ≤ t ≤ T
3:Find ${\overset{\sim}{M}}_{t} \in {\operatorname{argmin}_{M \in {\mathbb{R}}^{d_{x} \times {({{{({t + 1})}d_{y}} + {td_{u}}})}}}{\|{{M^{\top}M} - {\hat{N}}_{t}}\|}_{F}}$
4:For all 0 ≤ t ≤ ℓ − 1, set ${\hat{M}}_{t} = {\text{TruncSV}{({\overset{\sim}{M}}_{t},\theta)}}$; for all ℓ ≤ t ≤ T, set ${\hat{M}}_{t} = {\overset{\sim}{M}}_{t}$
5:Compute ẑt(i) = M̂t [y0: t(i); u0: (t−1)(i)] for all t = 0, …, T and i = 1, …, n
6:Return: state representation function estimate (M̂t)t = 0T and latent state estimates (ẑt(i))t = 0, i = 1T, n
Algorithm 2 Cost-driven state representation function learning

1:Input: data in the form of (ẑ0(i),u0(i),c0(i),…,ẑT − 1(i),uT − 1(i),cT − 1(i),ẑT(i),cT(i))i = 1n
2:Estimate the system dynamics by (Ât,B̂t)t = 0T − 1∈

picking the minimal-Frobenius-norm solution by pseudoinverse, as in (4.6)
3:For all 0 ≤ t ≤ ℓ − 1 and t = T, set Q̂t = Idx
4:For all ℓ ≤ t ≤ T − 1, obtain ${\overset{\sim}{Q}}_{t}$ by ${{\overset{\sim}{Q}}_{t},{\hat{b}}_{t}} \in$

and set Q̂t = U max (Λ,0) U⊤, where ${\overset{\sim}{Q}}_{t} = {U\LambdaU^{\top}}$ is its eigenvalue decomposition
5:Return: system parameters ((Ât,B̂t)t = 0T − 1,(Q̂t)t = 0T)
Algorithm 3 Latent model identification

The state representation function is learned via Algorithm 2. Given the raw data consisting of $n$ trajectories, Algorithm 2 first solves the regression problem (3.3) to recover the symmetric matrix ${\hat{N}}_{t}$. The target ${\overline{c}}_{t}$ of regression (3.3) is defined by

where $k = 1$ for $0 \leq t \leq {\ell - 1}$ and $k = {m \land {({{T - t} + 1})}}$ for $\ell \leq t \leq T$. The superscript in ${\overline{c}}_{t}^{(i)}$ denotes the observed ${\overline{c}}_{t}$ in the $i$th trajectory. The quadratic regression has a closed-form solution, by converting it to linear regression using ${\| v\|}_{P}^{2} = \left\langle {vv^{\top}},P \right\rangle_{F} = \left\langle {{svec}{({vv^{\top}})}},{{svec}{(P)}} \right\rangle$.

Why cumulative cost? The state representation function is parameterized by ${(M_{t})}_{t = 0}^{T}$ and the latent state at step $t$ is given by $z_{t} = {M_{t}h_{t}}$. The single-step cost prediction (neglecting control cost ${\| u_{t}\|}_{R_{t}^{\ast}}^{2}$ and constant $b_{t}$) is given by ${\| z_{t}\|}_{Q_{t}}^{2} = {h_{t}^{\top}M_{t}^{\top}Q_{t}M_{t}h_{t}}$. The regression recovers ${(M_{t}^{\ast})}^{\top}Q_{t}^{\ast}M_{t}^{\ast}$ as a whole, from which we can recover ${(Q_{t}^{\ast})}^{1/2}M_{t}^{\ast}$ up to an orthogonal transformation. If $Q_{t}^{\ast}$ is positive definite and known, then we can further recover $M_{t}^{\ast}$ from it. However, if $Q_{t}^{\ast}$ does not have full rank, information about $M_{t}^{\ast}$ is partially lost, and there is no way to fully recover $M_{t}^{\ast}$ even if $Q_{t}^{\ast}$ is known. To see why multi-step cumulative cost helps, define ${\overline{Q}}_{t}^{\ast}:={\sum_{\tau = t}^{{t + k} - 1}{\Phi_{\tau,t}^{\top}Q_{\tau}^{\ast}\Phi_{\tau,t}}}$ for the same $k$ above. Under zero control and zero noise, starting from $x_{t}$ at step $t$, the $k$-step cumulative cost is precisely ${\| x_{t}\|}_{{\overline{Q}}_{t}^{\ast}}^{2}$. Under the cost observability assumption (Assumption 3. ‣ 2 Problem setup ‣ Cost-Driven Representation Learning for Linear Quadratic Gaussian Control: Part I")), ${({\overline{Q}}_{t}^{\ast})}_{t = 0}^{T}$ are positive definite.

The normalized parameterization. Still, since ${\overline{Q}}_{t}^{\ast}$ is unknown, even if we recover ${(M_{t}^{\ast})}^{\top}{\overline{Q}}_{t}^{\ast}M_{t}^{\ast}$ as a whole, it is not viable to extract $M_{t}^{\ast}$ and ${\overline{Q}}_{t}^{\ast}$. Such ambiguity is unavoidable; in fact, for every ${\overline{Q}}_{t}^{\ast}$ we choose, there is an equivalent parameterization of the system such that the system response is exactly the same. In partially observable LTI systems, it is well-known that the system parameters can only be recovered up to a similarity transform. Since every parameterization is correct, we simply choose ${\overline{Q}}_{t}^{\ast} = I$, which we refer to as the *normalized parameterization*. Concretely, let us define $x_{t}^{\prime} = {{({\overline{Q}}_{t}^{\ast})}^{1/2}x_{t}}$. Then, the new parameterization is given by

and ${c_{T}^{\prime}{(x^{\prime})}} = {\| x^{\prime}\|}_{{(Q_{T}^{\ast})}^{\prime}}^{2}$, where for all $t \geq 0$,

One can verify that under the normalized parameterization, the system satisfies Assumptions 1. ‣ 2 Problem setup ‣ Cost-Driven Representation Learning for Linear Quadratic Gaussian Control: Part I"), 2. ‣ 2 Problem setup ‣ Cost-Driven Representation Learning for Linear Quadratic Gaussian Control: Part I"), 3. ‣ 2 Problem setup ‣ Cost-Driven Representation Learning for Linear Quadratic Gaussian Control: Part I"), and 4, up to a change of some constants in the bounds. Without loss of generality, we assume system (2.1) is in the normalized parameterization.

Low-rank approximate factorization. Regression (3.3) has a closed-form solution ${({\hat{N}}_{t},{\hat{b}}_{t})}_{t = 0}^{T}$. Constants ${({\hat{b}}_{t})}_{t = 0}^{T}$ account for the variance of the state estimation error, and are not part of the state representation function; $d_{h} \times d_{h}$ symmetric matrices ${({\hat{N}}_{t})}_{t = 0}^{T}$ are estimates of ${(M_{t}^{\ast})}^{\top}M_{t}^{\ast}$ under the normalized parameterization, where $d_{h} = {{{({t + 1})}d_{y}} + {td_{u}}}$. $M_{t}^{\ast}$ can only be recovered up to an orthogonal transformation, as for any orthogonal $S \in {\mathbb{R}}^{d_{x} \times d_{x}}$, ${{({SM_{t}^{\ast}})}^{\top}SM_{t}^{\ast}} = {{(M_{t}^{\ast})}^{\top}M_{t}^{\ast}}$.

We want to recover ${\overset{\sim}{M}}_{t}$ from ${\hat{N}}_{t}$ such that ${\hat{N}}_{t} = {{\overset{\sim}{M}}_{t}^{\top}{\overset{\sim}{M}}_{t}}$. Let ${U\LambdaU^{\top}} = {\hat{N}}_{t}$ be its eigenvalue decomposition. Let $\Sigma:={\max{(\Lambda,0)}}$ be the positive semidefinite diagonal matrix with nonnegative eigenvalues, where "$\max$" applies elementwise. If $d_{h} \leq d_{x}$, we can construct ${\overset{\sim}{M}}_{t} = {\lbrack{\Sigma^{1/2}U^{\top}};0_{{({d_{x} - d_{h}})} \times d_{h}}\rbrack}$ by padding zeros. If $d_{h} > d_{x}$, however, ${rank}{({\hat{N}}_{t})}$ may exceed $d_{x}$. Without loss of generality, assume that the diagonal elements of $\Sigma$ are in descending order. Let $\Sigma_{d_{x}}$ be the top-left $d_{x} \times d_{x}$ block of $\Sigma$ and $U_{d_{x}}$ be the left $d_{x}$ columns of $U$. By the Eckart-Young-Mirsky theorem, ${\overset{\sim}{M}}_{t} = {\Sigma_{d_{x}}^{1/2}U_{d_{x}}^{\top}}$ provides the best approximation of ${\hat{N}}_{t}$ with ${\overset{\sim}{M}}_{t}^{\top}{\overset{\sim}{M}}_{t}$ among $d_{x} \times d_{h}$ matrices in terms of the Frobenius norm distance.

Why singular value truncation in the first $\ell$ steps? The latent states are used to identify the latent system dynamics, so whether they are sufficiently excited, namely having full-rank covariance, makes a big difference: if not, the system matrices can only be identified partially. Proposition 2 below confirms that the optimal latent state $z_{t}^{\ast} = {M_{t}^{\ast}h_{t}}$ indeed has full-rank covariance for $t \geq \ell$.

### Proposition 2

If system (2.1) satisfies Assumptions 2. ‣ 2 Problem setup ‣ Cost-Driven Representation Learning for Linear Quadratic Gaussian Control: Part I") (controllability) and 4 (regularity), then under control ${(u_{t})}_{t = 0}^{T - 1}$, where $u_{t} \sim {\mathcal{N}{(0,{\sigma_{u}^{2}I})}}$, ${\sigma_{\min}{({{Cov}{(z_{t}^{\ast})}})}} = {\Omega{(\nu^{2})}}$, $M_{t}^{\ast}$ has rank $d_{x}$ and ${\sigma_{\min}{(M_{t}^{\ast})}} = {\Omega{({\nut^{- {1/2}}})}}$ for all $\ell \leq t \leq T$.

### Proof

For $\ell \leq t \leq T$, unrolling the Kalman filter gives

where ${(u_{\tau})}_{\tau = {t - \ell}}^{t - 1}$, $z_{t - \ell}^{\ast}$ and ${(i_{\tau})}_{\tau = {{t - \ell} + 1}}^{t}$ are independent. The matrix multiplied by $\lbrack u_{t - 1};\ldots;u_{t - \ell}\rbrack$ is precisely the controllability matrix $\Phi_{{t - 1},\ell}^{c}$. Then

By the controllability assumption (Assumption 2. ‣ 2 Problem setup ‣ Cost-Driven Representation Learning for Linear Quadratic Gaussian Control: Part I")), ${Cov}{(z_{t}^{\ast})}$ has full rank and

On the other hand, since $z_{t}^{\ast} = {M_{t}^{\ast}h_{t}}$,

Since $h_{t} = {\lbrack y_{0:t};u_{0:{({t - 1})}}\rbrack}$ and ${({{Cov}{(y_{t})}})}_{t = 0}^{T},{({{Cov}{(u_{t})}})}_{t = 0}^{T - 1}$ have $\mathcal{O}{}$ operator norms by Lemma 12, ${\|{{Cov}{(h_{t})}}\|} = {\|{{\mathbb{E}}{\lbrack{h_{t}h_{t}^{\top}}\rbrack}}\|} = {\mathcal{O}{(t)}}$. Hence,

This implies that ${{rank}{(M_{t}^{\ast})}} = d_{x}$ and ${\sigma_{\min}{(M_{t}^{\ast})}} = {\Omega{({\nut^{- {1/2}}})}}$. ∎

Proposition 2 implies that for all $\ell \leq t \leq T$, $N_{t}^{\ast}$ has rank $d_{x}$, so if $d_{x}$ is not provided, this gives a way to discover it. For $\ell \leq t \leq T$, Proposition 2 guarantees that as long as ${\overset{\sim}{M}}_{t}$ is close enough to $M_{t}^{\ast}$, it also has full rank, and so does ${Cov}{({{\overset{\sim}{M}}_{t}h_{t}})}$. Hence, we simply take the final estimate ${\hat{M}}_{t} = {\overset{\sim}{M}}_{t}$. Without further assumptions, however, there is no such a full-rank guarantee for ${({{Cov}{(z_{t}^{\ast})}})}_{t = 0}^{\ell - 1}$ and ${(M_{t}^{\ast})}_{t = 0}^{\ell - 1}$. We make the following minimal assumption to ensure that the minimum positive singular values ${({\sigma_{\min}^{+}{({{Cov}{(z_{t}^{\ast})}})}})}_{t = 0}^{\ell - 1}$ are uniformly lower bounded. Note that ${({{Cov}{(z_{t}^{\ast})}})}_{t = 0}^{\ell - 1}$ are not required to have full rank.

### Assumption 5

For $0 \leq t \leq {\ell - 1}$, ${\sigma_{\min}^{+}{(M_{t}^{\ast})}} \geq \beta > 0$.

Still, for $0 \leq t \leq {\ell - 1}$, Assumption 5 does not guarantee the full-rankness of ${Cov}{({{\overset{\sim}{M}}_{t}h_{t}})}$, not even a lower bound on its minimum positive singular value; that is why we introduce TruncSV that truncates the singular values of ${\overset{\sim}{M}}_{t}$ by a threshold $\theta > 0$. Concretely, we take ${\hat{M}}_{t} = {{({{{\mathbb{I}}_{\lbrack\theta,{+ \infty})}{(\Sigma_{d_{x}}^{1/2})}} \odot \Sigma_{d_{x}}^{1/2}})}U_{d_{x}}^{\top}}$. Then, ${\hat{M}}_{t}$ has the same singular values as ${\overset{\sim}{M}}_{t}$ except that those below $\theta$ are zeroed. We take $\theta = {\Theta{({\ell^{3/2}{({d_{y} + d_{u}})}d_{x}^{3/4}n^{- {1/4}}{\log^{1/4}{({\ell/p})}}})}}$ to ensure a sufficient lower bound on the minimum positive singular value of ${\hat{M}}_{t}$, without increasing the statistical errors.

## Theoretical guarantees and proofs

Theorem 1 below offers a finite-sample guarantee for our approach, confirming cost-driven state representation learning (Algorithm 1) as a viable path to solving LQG control.

### Theorem 1

Given an unknown LQG control problem defined by (2.1) and (2.2), under Assumptions 1. ‣ 2 Problem setup ‣ Cost-Driven Representation Learning for Linear Quadratic Gaussian Control: Part I"), 2. ‣ 2 Problem setup ‣ Cost-Driven Representation Learning for Linear Quadratic Gaussian Control: Part I"), 3. ‣ 2 Problem setup ‣ Cost-Driven Representation Learning for Linear Quadratic Gaussian Control: Part I"), 4 and 5, for a given $p \in {}$, if we run CoReL (Algorithm 1) for $n \geq {{poly}{(T,d_{x},d_{y},d_{u},{\log{({1/p})}})}}$, then with probability at least $1 - p$, state representation function ${({\hat{M}}_{t})}_{t = 0}^{T}$ is ${poly}{(\ell,d_{x},d_{y},d_{u},{\log{({\ell/p})}})}n^{- {1/4}}$-optimal in the first $\ell$ steps, and ${poly}{(\nu^{- 1},T,d_{x},d_{y},d_{u},{\log{({T/p})}})}n^{- {1/2}}$-optimal in the next $({T - \ell})$ steps. In addition, the overall output policy $\hat{\pi} = {({\hat{M}}_{t},{\hat{K}}_{t})}_{t = 0}^{T - 1}$ satisties

where $c > 1$ is a dimension-free constant depending polynomially on $\ell$ and other problem parameters.

Theorem 1 provides finite-sample guarantees for both the state representation function ${({\hat{M}}_{t})}_{t = 0}^{T}$ and the overall policy $\hat{\pi} = {({\hat{M}}_{t},{\hat{K}}_{t})}_{t = 0}^{T}$. From Theorem 1, we observe a separation of the sample complexities *before* and *after* time step $\ell$ for the state representation function, resulting from the loss of the full-rankness of ${({{Cov}{(z_{t}^{\ast})}})}_{t = 0}^{\ell - 1}$ and ${(M_{t}^{\ast})}_{t = 0}^{\ell - 1}$.

Specifically, quadratic regression guarantees that ${\hat{N}}_{t}$ converges to $N_{t}^{\ast}$ at a rate of $n^{- {1/2}}$ for all $0 \leq t \leq T$ (Lemma 2. ‣ Proof. ‣ 4.2 Quadratic regression bound ‣ 4 Theoretical guarantees and proofs ‣ Cost-Driven Representation Learning for Linear Quadratic Gaussian Control: Part I")). Before time step $\ell$, ${\hat{M}}_{t}$ suffers a square root decay of the rate $n^{- {1/4}}$ because $M_{t}^{\ast}$ may not have rank $d_{x}$ (Lemma 4). Since ${({\hat{z}}_{t})}_{t = 0}^{\ell - 1}$ may not have full-rank covariances, ${(A_{t}^{\ast})}_{t = 0}^{\ell - 1}$ are only recovered partially. As a result, ${({\hat{K}}_{t})}_{t = 0}^{\ell - 1}$ may not stabilize ${(A_{t}^{\ast},B_{t}^{\ast})}_{t = 0}^{\ell - 1}$. This issue poses a significant challenge for the analysis and significantly worsens dependence on $\ell$ in the policy suboptimality gap (Lemma 7. ‣ 4.5 Certainty equivalent linear quadratic control ‣ 4 Theoretical guarantees and proofs ‣ Cost-Driven Representation Learning for Linear Quadratic Gaussian Control: Part I")), which implies that if $n$ is not large enough, the policy may be inferior to zero control in the first $\ell$ steps, as system ${(A_{t}^{\ast},B_{t}^{\ast})}_{t = 0}^{\ell - 1}$ is uniformly exponential stable (Assumption 1. ‣ 2 Problem setup ‣ Cost-Driven Representation Learning for Linear Quadratic Gaussian Control: Part I")), while zero control has a suboptimality gap linear in $\ell$. After time step $\ell$, ${\hat{M}}_{t}$ retains the $n^{- {1/2}}$ sample complexity, from which the same order of sample complexity guarantee for $({\hat{A}}_{t},{\hat{B}}_{t})$ follows, resulting in the ${poly}{(T)}n^{- 1}$ term in the policy suboptimality gap.

Next, we provide a key proposition and several technical lemmas for analyzing our algorithm, before we present the proof of Theorem 1, which contains the exact polynomial orders of the finite-sample guarantees.

### Proposition on multi-step cumulative costs

The following proposition establishes the relationship between the multi-step cumulative costs and the state estimates by the Kalman filter.

### Proposition 3

Let ${(z_{t}^{\ast \prime})}_{t = 0}^{T}$ be the state estimates by the Kalman filter under the normalized parameterization. If we apply $u_{t} \sim {\mathcal{N}{(0,{\sigma_{u}^{2}I})}}$ for all $0 \leq t \leq {T - 1}$, then for $0 \leq t \leq T$,

where $k = 1$ for $0 \leq t \leq {\ell - 1}$ and $k = {m \land {({{T - t} + 1})}}$ for $\ell \leq t \leq T$, ${\overline{b}}_{t} = {\mathcal{O}{(k)}}$, and ${\overline{e}}_{t}$ is a zero-mean subexponential random variable with ${\|{\overline{e}}_{t}\|}_{\psi_{1}} = {\mathcal{O}{({kd_{x}^{1/2}})}}$.

### Proof

By Proposition 1, $z_{t + 1}^{\ast \prime} = {{A_{t}^{\ast \prime}z_{t}^{\ast \prime}} + {B_{t}^{\ast \prime}u_{t}} + {L_{t + 1}^{\ast \prime}i_{t + 1}^{\prime}}}$, where $L_{t + 1}^{\ast \prime},i_{t + 1}^{\prime}$ are the Kalman gain and the innovation under the normalized parameterization, respectively. Under Assumptions 1. ‣ 2 Problem setup ‣ Cost-Driven Representation Learning for Linear Quadratic Gaussian Control: Part I") and 4, ${(i_{t}^{\prime})}_{t = 0}^{T}$ are Gaussian random vectors whose covariances have $\mathcal{O}{}$ operator norms, and ${(L_{t}^{\ast \prime})}_{t = 0}^{T}$ have $\mathcal{O}{}$ operator norms. Hence, The covariance of $L_{t + 1}^{\ast \prime}i_{t + 1}^{\prime}$ has $\mathcal{O}{}$ operator norm. Since $u_{t} \sim {\mathcal{N}{(0,{\sigma_{u}^{2}I})}}$, $j_{t}:={{B_{t}^{\ast \prime}u_{t}} + i_{t}^{\prime}}$ can be viewed as a Gaussian noise vector whose covariance has $\mathcal{O}{}$ operator norm. By Proposition 1,

where $e_{t}^{\prime}:={\gamma_{t}^{\prime} + \eta_{t}^{\prime}}$ is subexponential with ${\| e_{t}^{\prime}\|}_{\psi_{1}} = {\mathcal{O}{(d_{x}^{1/2})}}$. Let $\Phi_{t,t_{0}}^{\prime} = {A_{t - 1}^{\ast \prime}A_{t - 2}^{\ast \prime}\cdotsA_{t_{0}}^{\ast \prime}}$ for $t > t_{0}$ and $\Phi_{t,t}^{\prime} = I$. Then, for $\tau \geq t$,

where $j_{t,t}^{\prime} = 0$ and for $\tau > t$, $j_{\tau,t}^{\prime}$ is a Gaussian random vector with bounded covariance due to uniform exponential stability (Assumption 1. ‣ 2 Problem setup ‣ Cost-Driven Representation Learning for Linear Quadratic Gaussian Control: Part I")). Therefore,

where ${\sum_{\tau = t}^{{t + k} - 1}{{(\Phi_{\tau,t}^{\prime})}^{\top}Q_{t}^{\ast \prime}\Phi_{\tau,t}^{\prime}}} = I$ is due to the normalized parameterization, ${\overline{b}}_{t}:={\sum_{\tau = t}^{{t + k} - 1}{({b_{\tau} + {{\mathbb{E}}{\lbrack{\| j_{\tau}^{\prime}\|}_{Q_{\tau}^{\ast \prime}}^{2}\rbrack}}})}} = {\mathcal{O}{(k)}}$, and

has zero mean and is subexponential with ${\|{\overline{e}}_{t}\|}_{\psi_{1}} = {\mathcal{O}{({kd_{x}^{1/2}})}}$. ∎

### Quadratic regression bound

As noted in §3.1, the quadratic regression can be converted to linear regression using ${\| h\|}_{P}^{2} = \left\langle {hh^{\top}},P \right\rangle_{F} = \left\langle {{svec}{({hh^{\top}})}},{{svec}{(P)}} \right\rangle$. To analyze this linear regression with an intercept, we need the following lemma. We note that a similar lemma without considering the intercept has been proved in.

### Lemma 1

Let ${(h_{0}^{(i)})}_{i = 1}^{n}$ be $n$ independent observations of the $d$-dimensional random vector $h_{0} \sim {\mathcal{N}{(0,I_{d})}}$. Let $f_{0}^{(i)}:={{svec}{({h_{0}^{(i)}{(h_{0}^{(i)})}^{\top}})}}$ and ${\overline{f}}_{0}^{(i)}:={\lbrack f_{0}^{(i)};1\rbrack}$. There exists an absolute constant $a > 0$, such that as long as $n \geq {ar^{4}{\log{({{ar^{2}}/p})}}}$, with probability at least $1 - p$,

### Proof

Let $f_{0} = {{svec}{({h_{0}h_{0}^{\top}})}}$ and ${\overline{f}}_{0} = {\lbrack f_{0};1\rbrack}$. We first show that $\lambda_{\min}{({{\mathbb{E}}{\lbrack{{\overline{f}}_{0}{\overline{f}}_{0}^{\top}}\rbrack}})}$ is lower bounded. Consider

To lower bound its smallest eigenvalue, let us compute its inverse. By the Sherman-Morrison formula,

Then, by the inverse of a block matrix,

Then, with the similar concentration arguments to those in, we can show that with probability at least $1 - p$,

which completes the proof. ∎

Lemma 1 lower bounds the minimum singular value of a matrix that contains the fourth powers of elements in standard Gaussian random vectors. The following lemma is the main result in § 4.2.

### Lemma 2 (Quadratic regression)

Define random variable $c:={{{(h^{\ast})}^{\top}N^{\ast}h^{\ast}} + b^{\ast} + e}$, where $h^{\ast} \sim {\mathcal{N}{(0,\Sigma_{\ast})}}$ is a $d$-dimensional Gaussian random vector, $N^{\ast} \in {\mathbb{R}}^{d \times d}$ is a positive semidefinite matrix, $b^{\ast} \in {\mathbb{R}}$ is a constant and $e$ is a zero-mean subexponential random variable with ${\| e\|}_{\psi_{1}} \leq E$. Assume that ${\| N^{\ast}\|}_{2} = {\mathcal{O}{}}$ and that ${\lambda_{\min}{(\Sigma_{\ast}^{1/2})}} \geq \beta = {\Omega{}}$. Define $h:={h^{\ast} + \delta}$ where the perturbation vector $\delta$ can be correlated with $h^{\ast}$ and its $\ell_{2}$ norm is sub-Gaussian with ${{\mathbb{E}}{\lbrack{\|\delta\|}\rbrack}} \leq \epsilon$, ${\|{\|\delta\|}\|}_{\psi_{2}} \leq \epsilon$. Assume that $\epsilon \leq {\min{({({d{\|\Sigma_{\ast}\|}_{2}})}^{1/2},{a{({\beta \land 1})}d^{- {3/2}}{\|\Sigma_{\ast}\|}_{2}^{- {1/2}}{({\log{({n/p})}})}^{- 1}})}}$ for some absolute constant $a > 0$. Suppose we get $n$ observations $h^{(i)}$ and $c^{(i)}$ of $h$ and $c$, where ${({(h^{\ast})}^{(i)})}_{i = 1}^{n}$ are independent and ${(\delta^{(i)})}_{i = 1}^{n}$ can be correlated. Consider the regression problem

There exists an absolute constant $a_{0} > 0$, such that as long as $n \geq {a_{0}d^{4}{\log{({{a_{0}d^{2}}/p})}}{\log{({1/p})}}}$, with probability at least $1 - p$, ${\|{\hat{N} - N^{\ast}}\|}_{F}$ and $|{\hat{b} - b^{\ast}}|$ are bounded by

### Proof

Regression (4.1. ‣ Proof. ‣ 4.2 Quadratic regression bound ‣ 4 Theoretical guarantees and proofs ‣ Cost-Driven Representation Learning for Linear Quadratic Gaussian Control: Part I")) can be written as

Let $f^{(i)}:={{svec}{({h^{(i)}{(h^{(i)})}^{\top}})}}$ denote the covariates and ${\overline{f}}^{(i)}:={\lbrack f^{(i)};1\rbrack}$ denote the extended covariates. Define ${(f^{\ast})}^{(i)}$ and ${({\overline{f}}^{\ast})}^{(i)}$ similarly by replacing $h^{(i)}$ with ${(h^{\ast})}^{(i)}$. Then, regression (4.1. ‣ Proof. ‣ 4.2 Quadratic regression bound ‣ 4 Theoretical guarantees and proofs ‣ Cost-Driven Representation Learning for Linear Quadratic Gaussian Control: Part I")) can be written as

Let $\overline{F}:={\lbrack{\overline{f}}^{},\ldots,{\overline{f}}^{(n)}\rbrack}^{\top}$ be the $n \times \frac{d{({d + 3})}}{2}$ matrix whose $i$th row is ${({\overline{f}}^{(i)})}^{\top}$. Define ${\overline{F}}^{\ast}$ similarly by replacing ${\overline{f}}^{(i)}$ with ${({\overline{f}}^{\ast})}^{(i)}$. Solving linear regression (4.2) gives

Substituting $c^{(i)} = {{{({({\overline{f}}^{\ast})}^{(i)})}^{\top}{\lbrack{{svec}{(N^{\ast})}};b^{\ast}\rbrack}} + e^{(i)}}$ into the above equation yields

where $\xi$ denotes the vector whose $i$th element is $e^{(i)}$. Rearranging the terms, we have

Next, we show that ${\overline{F}}^{\top}\overline{F}$ is invertible with high probability. We can represent $h^{\ast}$ by $\Sigma_{\ast}^{1/2}h_{0}$, where $h_{0} \sim {\mathcal{N}{(0,I_{d})}}$ is an $d$-dimensional standard Gaussian random vector. Correspondingly, an independent observation ${(h^{\ast})}^{(i)}$ can be expressed as $\Sigma_{\ast}^{1/2}h_{0}^{(i)}$, where $h_{0}^{(i)}$ is an independent observation of $h_{0}$. It follows that ${h^{\ast}{(h^{\ast})}^{\top}} = {\Sigma_{\ast}^{1/2}h_{0}h_{0}^{\top}\Sigma_{\ast}^{1/2}}$ and ${{(h^{\ast})}^{(i)}{({(h^{\ast})}^{(i)})}^{\top}} = {\Sigma_{\ast}^{1/2}h_{0}^{(i)}{(h_{0}^{(i)})}^{\top}\Sigma_{\ast}^{1/2}}$. Define $f_{0}:={{svec}{({h_{0}h_{0}^{\top}})}}$, $f_{0}^{(i)}:={{svec}{({h_{0}^{(i)}{(h_{0}^{(i)})}^{\top}})}}$, and $F_{0}:={\lbrack f_{0}^{},\ldots,f_{0}^{(n)}\rbrack}^{\top}$ be an $n \times \frac{r{({r + 1})}}{2}$ matrix whose $i$th row is ${(f_{0}^{(i)})}^{\top}$. Define ${\overline{f}}_{0}$, ${\overline{f}}_{0}^{(i)}$ and ${\overline{F}}_{0}$ as the extended counterparts. Then,

where $\Phi^{\ast}:={\Sigma_{\ast}^{1/2} \otimes_{s}\Sigma_{\ast}^{1/2}}$ is a $\frac{d{({d + 1})}}{2} \times \frac{d{({d + 1})}}{2}$ matrix. Then, $F^{\ast} = {F_{0}{(\Phi^{\ast})}^{\top}}$. By the properties of the symmetric Kronecker product,

By Lemma 1, there exist absolute constants ${a_{0},a_{1}} > 0$, such that if $n \geq {a_{0}d^{4}{\log{({{a_{0}d^{2}}/p})}}}$, with probability at least $1 - p$, ${\lambda_{\min}{({{\overline{F}}_{0}^{\top}{\overline{F}}_{0}})}} \geq {a_{1}d^{- 1}n}$. Since $\overline{f} = {\text{diag}{(\Phi^{\ast},1)}{\overline{f}}_{0}}$ and ${\overline{F}}^{\ast} = {{\overline{F}}_{0}\text{diag}{({(\Phi^{\ast})}^{\top},1)}}$,

By Weyl's inequality for singular values,

Hence, we want to bound ${\|{F^{\ast} - F}\|}_{2}$, which satisfies

Since ${h^{\ast}{(h^{\ast})}^{\top}} - {hh^{\top}}$ has at most rank two, we have

Since $h^{\ast} \sim {\mathcal{N}{(0,\Sigma_{\ast})}}$, $\| h^{\ast}\|$ is sub-Gaussian with its mean and sub-Gaussian norm bounded by $\mathcal{O}{({({d{\|\Sigma_{\ast}\|}})}^{1/2})}$. Since $\|\delta\|$ is sub-Gaussian with its mean and sub-Gaussian norm bounded by $\epsilon \leq {({d{\|\Sigma_{\ast}\|}})}^{1/2}$, we conclude that ${\|{{h^{\ast}{(h^{\ast})}^{\top}} - {hh^{\top}}}\|}_{F}$ is subexponential with its mean and subexponential norm bounded by $\mathcal{O}{({\epsilon{({d{\|\Sigma_{\ast}\|}})}^{1/2}})}$. Hence, with probability at least $1 - p$,

Therefore, by the union bound over $n$ observations,

which implies that

Hence, there exists some absolute constant $a > 0$, such that as long as

Therefore, we further have

Now, we return to (4.4). By inverting ${\overline{F}}^{\top}\overline{F}$, we obtain

Term $(a)$ is upper bounded by

Using arguments similar to those in, we have

where $\left\langle \cdot, \cdot \right\rangle_{F}$ denotes the Frobenius product between matrices in $(i)$, $\parallel \cdot \parallel_{\ast}$ denotes the nuclear norm in $({ii})$, and $({iii})$ follows from the fact that the matrix ${{(h^{\ast})}^{(i)}{({(h^{\ast})}^{(i)})}^{\top}} - {h^{(i)}{(h^{(i)})}^{\top}}$ has at most rank two. Hence, term $(a)$ in (4.5) is bounded by

Now we consider term $(b)$ in (4.5):

Since $\xi$ is a vector of zero-mean subexponential variables with subexponential norms bounded by $E$, ${\|\xi\|} = {\mathcal{O}{({En^{1/2}{\log{({n/p})}}})}}$. Hence, we have

To bound ${\|{{({\overline{F}}^{\ast})}^{\top}\xi}\|} = {\|{\text{diag}{(\Phi^{\ast},1)}{\overline{F}}_{0}^{\top}\xi}\|}$, note that ${\|{{\overline{F}}_{0}^{\top}\xi}\|} = {\|{\sum_{i = 1}^{n}{{\overline{f}}_{0}^{(i)}e^{(i)}}}\|}$. Consider the $j$th component in the summation $\sum_{i = 1}^{n}{{\lbrack{\overline{f}}_{0}^{(i)}\rbrack}_{j}{(e^{\prime})}^{(i)}}$. Recall that $f_{0} = {{svec}{({h_{0}h_{0}^{\top}})}}$, so ${\lbrack{\overline{f}}_{0}\rbrack}_{j}$ is either the square of a standard Gaussian random variable, $\sqrt{2}$ times the product of two independent standard Gaussian random variables, or one. Hence, ${\lbrack f_{0}\rbrack}_{j}$ is subexponential with mean and ${\|{\lbrack f_{0}\rbrack}_{j}\|}_{\psi_{1}}$ both bounded by $\mathcal{O}{}$. As a result, the product ${\lbrack f_{0}\rbrack}_{j}e$ is $\frac{1}{2}$-sub-Weibull, with the sub-Weibull norm being $\mathcal{O}{(E)}$. By,

Hence, the norm of the ${d{({d + 1})}}/2$-dimensional vector $F_{0}^{\top}\xi$ is $\mathcal{O}{({dEn^{1/2}{\log^{1/2}{({1/p})}}})}$. By the properties of the symmetric Kronecker product, ${\|\Phi^{\ast}\|}_{2} = {\|\Sigma_{\ast}^{1/2}\|}_{2}^{2} = {\|\Sigma_{\ast}\|}_{2}$. Then,

Eventually, term $(b)$ is bounded by

Combining the bounds on $(a)$ and $(b)$, we have

which concludes the proof. ∎

### Matrix factorization bound

Given two $m \times n$ matrices $A,B$, we are interested in bounding $\min_{{S^{\top}S} = I}{\|{{SA} - B}\|}_{F}$ using ${\|{{A^{\top}A} - {B^{\top}B}}\|}_{F}$. The minimum problem is known as the orthogonal Procrustes problem, solved in. Specifically, the minimum is attained at $S = {UV^{\top}}$, where ${U\SigmaV^{\top}} = {BA^{\top}}$ is its singular value decomposition.

If $m \leq n$ and ${{rank}{(A)}} = m$, then the following lemma from establishes that the distance between $A$ and $B$ is of the same order of ${\|{{A^{\top}A} - {B^{\top}B}}\|}_{F}$.

### Lemma 3 ((Tu et al., 2016, Lemma 5.4))

For $m \times n$ matrices $A,B$, let $\sigma_{m}{(A)}$ denote its $m$th largest singular value. Then

If $\sigma_{\min}{(A)}$ equals zero, the above bound becomes vacuous. In general, the following lemma shows that the distance is of the order of the square root of the ${\|{{A^{\top}A} - {B^{\top}B}}\|}_{F}$, with a multiplicative $\sqrt{d}$ factor, where $d = {\min{({2m},n)}}$.

### Lemma 4

For $m \times n$ matrices $A,B$, ${\min_{{S^{\top}S} = I}{\|{{SA} - B}\|}_{F}^{2}} \leq {\sqrt{d}{\|{{A^{\top}A} - {B^{\top}B}}\|}_{F}}$, where $d = {\min{({2m},n)}}$.

### Proof

Let ${U\SigmaV^{\top}} = {BA^{\top}}$ be its singular value decomposition. By substituting the solution $UV^{\top}$ of the orthogonal Procrustes problem, the square of the attained minimum equals

where $(i)$ is due to the property of $U,V$.

To establish the relationship between ${{\|{A^{\top}A}\|}_{\ast} + {\|{B^{\top}B}\|}_{\ast}} - {2{\|{BA^{\top}}\|}_{\ast}}$ and ${\|{{A^{\top}A} - {B^{\top}B}}\|}_{F}$, we need to operate in the space of singular values. For $m \times n$ matrix $M$, let $({\sigma_{1}{(M)}},\ldots,{\sigma_{d^{\prime}}{(M)}})$ be its singular values in descending order, where $d^{\prime} = {m \land n}$.

In terms of singular values,

where $(i)$ holds since $A^{\top}A$ and $B^{\top}B$ are positive semidefinite matrices, and in $({ii})$ $d:={\min{({2m},n)}}$ since ${{rank}{({{A^{\top}A} + {B^{\top}B}})}} \leq n$ and ${{rank}{({{A^{\top}A} + {B^{\top}B}})}} \leq {{{rank}{({A^{\top}A})}} + {{rank}{({B^{\top}B})}}} \leq {2m}$. If $x \geq y > 0$, then ${x - y} \leq \sqrt{x^{2} - y^{2}}$. For all $1 \leq i \leq d$, ${2\sigma_{i}{({BA^{\top}})}} \leq {\sigma_{i}{({{A^{\top}A} + {B^{\top}B}})}}$. Take $\sigma_{i}{({{A^{\top}A} + {B^{\top}B}})}$ as $x$ and $2\sigma_{i}{({BA^{\top}})}$ as $y$; it follows that

Let ${\sigma_{i}{({BA^{\top}})}}:=0$ for $d^{\prime} < i \leq d$. Combining the above yields

where $(i)$ is due to the Cauchy-Schwarz inequality, and $({ii})$ uses

This completes the proof. ∎

### Perturbed linear regression bound

Identifying the dynamics of the latent model requires solving linear regression (3.4). A standard assumption in analyzing linear regression $y = {{A^{\ast}x} + e}$ is that ${Cov}{(x)}$ has *full rank*. However, as discussed in §3.1, we need to handle rank-deficient ${Cov}{(x)}$ in the first $\ell$ steps of system identification. Moreover, the latent state estimates ${\hat{z}}_{t}$ contain errors. Both issues are addressed in the following lemma.

### Lemma 5 (Perturbed rank-deficient linear regression)

Define random vector $y^{\ast}:={{A^{\ast}x^{\ast}} + e}$, where $x^{\ast} \sim {\mathcal{N}{(0,\Sigma_{\ast})}}$ and $e \sim {\mathcal{N}{(0,\Sigma_{e})}}$ are $d_{1}$ and $d_{2}$ dimensional Gaussian random vectors, respectively. Define $x:={x^{\ast} + \delta_{x}}$ and $y:={y^{\ast} + \delta_{y}}$ where the perturbation vectors $\delta_{x}$ and $\delta_{y}$ can be correlated with $x^{\ast}$ and $y^{\ast}$. Assume that ${\| A^{\ast}\|}_{2}$, ${\|\Sigma_{\ast}\|}_{2}$ and ${\|\Sigma_{e}\|}_{2}$ are $\mathcal{O}{}$. Let ${\sigma_{\min}^{+}{(\Sigma_{\ast}^{1/2})}} \geq \beta > 0$. Suppose we get $n$ observations $x^{(i)}$ and $y^{(i)}$ of $x$ and $y$, where ${({(x^{\ast})}^{(i)})}_{i = 1}^{n}$ are independent and ${(\delta_{x}^{(i)},\delta_{y}^{(i)})}_{i = 1}^{n}$ can be correlated. Assume that ${\sigma_{\min}^{+}{({\sum_{i = 1}^{n}{x^{(i)}{(x^{(i)})}^{\top}}})}} \geq {\theta^{2}n}$ for some $\theta > 0$ that has at least $n^{- {1/4}}$ dependence on $n$, and that ${\|{\sum_{i = 1}^{n}{\delta_{x}^{(i)}{(\delta_{x}^{(i)})}^{\top}}}\|}_{2} = {\mathcal{O}{({\epsilon_{x}^{2}n})}}$, ${\|{\sum_{i = 1}^{n}{\delta_{y}^{(i)}{(\delta_{y}^{(i)})}^{\top}}}\|}_{2} = {\mathcal{O}{({\epsilon_{y}^{2}n})}}$ for ${\epsilon_{x},\epsilon_{y}} > 0$. Consider the minimum Frobenius norm solution

Then, there exists an absolute constant $c > 0$, such that if $n \geq {c{({d_{1} + d_{2} + {\log{({1/p})}}})}}$, with probability at least $1 - p$,

### Proof

Let $r = {{rank}{(\Sigma_{\ast})}}$ and $\Sigma_{\ast} = {DD^{\top}}$ where $D \in {\mathbb{R}}^{d_{1} \times r}$. We can view $x^{\ast}$ as generated from an $r$-dimensional standard Gaussian $g \sim {\mathcal{N}{(0,I_{r})}}$, by $x^{\ast} = {Dg}$; $x^{(i)}$ can then be viewed as ${Dg^{(i)}} + \delta_{x}^{(i)}$, where ${(g^{(i)})}_{i = 1}^{n}$ are independent observations of $g$. Let $X$ denote the matrix whose $i$th row is ${(x^{(i)})}^{\top}$; $X^{\ast},Y,G,E,\Delta_{x},\Delta_{y}$ are defined similarly.

To solve the regression problem, we set its gradient to be zero and substitute $Y = {{X^{\ast}{(A^{\ast})}^{\top}} + E + \Delta_{y}}$ to obtain

Substituting $X$ by ${GD^{\top}} + \Delta_{x}$ gives

By rearranging the terms, we have

For ${\|\hat{A}\|}_{2}$, we make the following claim, whose proof is deferred to §4.4.1.

### Claim 1

As long as $n \geq {16{({d_{1} + d_{2} + {\log{({1/p})}}})}}$, with probability at least $1 - {4p}$,

The proof of Claim 1 is deferred to §4.4.1, where we analyze the inversion of $X^{\top}X$. Note that we may also bound ${\|\hat{A}\|}_{2}$ by analyzing the inversion of $DG^{\top}GD^{\top}$, potentially without the requirement on $\theta$, but this requires stronger condition on $\epsilon_{x}$ and $\epsilon_{y}$, and the bound is not directly applicable to the minimum Frobenius norm solution. The requirement on $\theta$ remains beneficial for numerical stability.

Then, since ${\| D^{\dagger}\|}_{2} = {({\sigma_{\min}^{+}{(\Sigma_{\ast}^{1/2})}})}^{- 1} \leq \beta^{- 1}$,

By, the Gaussian ensemble $G$ satisfies that with probability at least $1 - p$,

Since $n \geq {{8d_{1}} + {16{\log{({1/p})}}}}$, we have ${\| G\|}_{2} = {\mathcal{O}{(n^{1/2})}}$ and ${\sigma_{\min}{(G)}} = {\Omega{(n^{1/2})}}$. It follows that ${\|{({G^{\top}G})}^{- 1}\|}_{2} = {\mathcal{O}{(n^{- 1})}}$ and ${\| G^{\dagger}\|}_{2} = {\mathcal{O}{(n^{- {1/2}})}}$. Similarly, ${\| E\|}_{2} = {\mathcal{O}{({({{\|\Sigma_{e}\|}_{2}n})}^{1/2})}}$. Note that ${\Delta_{x}^{\top}\Delta_{x}} = {\sum_{i = 1}^{n}{\delta_{x}^{(i)}{(\delta_{x}^{(i)})}^{\top}}}$. By our assumption, ${\|\Delta_{x}\|}_{2} = {\mathcal{O}{({\epsilon_{x}n^{1/2}})}}$. Similarly, ${\|\Delta_{y}\|}_{2} = {\mathcal{O}{({\epsilon_{y}n^{1/2}})}}$. Hence,

where we consider $\epsilon_{x}$ and $\epsilon_{y}$ as quantities much smaller than one such that terms like $\epsilon_{x}^{2},{\epsilon_{x}\epsilon_{y}}$ are absorbed into $\epsilon_{x},\epsilon_{y}$. It remains to control ${\|{G^{\dagger}E}\|}_{2}$. It is proved in via a covering number argument that with probability at least $1 - p$,

Overall, we obtain that

which completes the proof. ∎

### Proof of Claim 1

The minimum Frobenius norm solution $\hat{A}$ is given by the following closed-form expression in terms of the pseudoinverse (Moore-Penrose inverse):

where we note that ${\| X^{\dagger}\|}_{2} = {\sigma_{\min}^{+}{(X)}^{- 1}}$ when $X \neq 0$. Since ${\sigma_{\min}^{+}{(X)}} = {({\sigma_{\min}^{+}{({X^{\top}X})}})}^{1/2} \geq {\thetan^{1/2}}$,

Similar to the proof of Lemma 5. ‣ 4.4 Perturbed linear regression bound ‣ 4 Theoretical guarantees and proofs ‣ Cost-Driven Representation Learning for Linear Quadratic Gaussian Control: Part I"), by, with probability at least $1 - p$,

Combining the bounds above, we obtain

Hence, as long as $\theta$ has at least $n^{- {1/4}}$ dependence on $n$,

In Lemma 5. ‣ 4.4 Perturbed linear regression bound ‣ 4 Theoretical guarantees and proofs ‣ Cost-Driven Representation Learning for Linear Quadratic Gaussian Control: Part I"), if $\Sigma_{\ast}$ has full rank and ${\lambda_{\min}{(\Sigma_{\ast})}} \geq \beta > 0$ and ${\lambda_{\min}{({\sum_{i = 1}^{n}{x^{(i)}{(x^{(i)})}^{\top}}})}} = {\Omega{({\beta^{2}n})}}$, then

The following lemma shows that we can strengthen the result by removing the $\beta^{- 1}$ factor before $\epsilon_{x}$.

### Lemma 6 (Perturbed linear regression)

Define random variable $y^{\ast} = {{A^{\ast}x^{\ast}} + e}$, where $x^{\ast} \sim {\mathcal{N}{(0,\Sigma_{\ast})}}$ and $e \sim {\mathcal{N}{(0,\Sigma_{e})}}$ are $d_{1}$ and $d_{2}$ dimensional random vectors. Assume that ${\| A^{\ast}\|}_{2}$, ${\|\Sigma_{\ast}\|}_{2}$ and ${\|\Sigma_{e}\|}_{2}$ are $\mathcal{O}{}$, and ${\lambda_{\min}{(\Sigma_{\ast}^{1/2})}} \geq \beta > 0$. Define $x:={x^{\ast} + \delta_{x}}$ and $y:={y^{\ast} + \delta_{y}}$ where the perturbation vectors $\delta_{x}$ and $\delta_{y}$ can be correlated with $x^{\ast}$ and $y^{\ast}$. Suppose we get $n$ independent observations $x^{(i)},y^{(i)}$ of $x$ and $y$. Assume that ${\lambda_{\min}{({\sum_{i = 1}^{n}{x^{(i)}{(x^{(i)})}^{\top}}})}} = {\Omega{({\beta^{2}n})}}$, ${\|{\sum_{i = 1}^{n}{\delta_{x}^{(i)}{(\delta_{x}^{(i)})}^{\top}}}\|}_{2} = {\mathcal{O}{({\epsilon_{x}^{2}n})}}$, ${\|{\sum_{i = 1}^{n}{\delta_{y}^{(i)}{(\delta_{y}^{(i)})}^{\top}}}\|}_{2} = {\mathcal{O}{({\epsilon_{y}^{2}n})}}$ for ${\beta,\epsilon_{x},\epsilon_{y}} > 0$. Consider the minimum Frobenius norm solution

Then, there exists an absolute constant $c > 0$, such that if $n \geq {c{({d_{1} + d_{2} + {\log{({1/p})}}})}}$, with probability at least $1 - p$,

### Proof

Following the proof of Claim 1, we have

Combining with the bounds on ${\|{X^{\dagger}\Delta_{x}}\|}_{2}$, ${\|{X^{\dagger}\Delta_{y}}\|}_{2}$ and ${\|{X^{\dagger}E}\|}_{2}$ concludes the proof. ∎

### Certainty equivalent linear quadratic control

As shown in Lemma 5. ‣ 4.4 Perturbed linear regression bound ‣ 4 Theoretical guarantees and proofs ‣ Cost-Driven Representation Learning for Linear Quadratic Gaussian Control: Part I"), if the input of linear regression does not have full-rank covariance, then the parameters can only be identified in certain directions. The following lemma studies the performance of the certainty equivalent optimal controller in this case.

### Lemma 7 (Rank deficient linear quadratic control)

Consider the finite-horizon time-varying linear dynamical system given by the first equation in (2.1) with quadratic costs given by (2.2), under Assumption 1. ‣ 2 Problem setup ‣ Cost-Driven Representation Learning for Linear Quadratic Gaussian Control: Part I"), Assumption 3. ‣ 2 Problem setup ‣ Cost-Driven Representation Learning for Linear Quadratic Gaussian Control: Part I") with $\ell = T$, and Assumption 4 on relevant problem parameters. Let $\Sigma_{t}:={{Cov}{(x_{t})}}$ under control $u_{t} \sim {\mathcal{N}{(0,{\sigma_{u}^{2}I})}}$ for all $t \geq 0$, which may not have full rank. Let ${({\hat{A}}_{t},{\hat{B}}_{t})}_{t = 0}^{T - 1},{({\hat{Q}}_{t})}_{t = 0}^{T}$ satisfy ${\|{{({{\hat{A}}_{t} - A_{t}^{\ast}})}{(\Sigma_{t})}^{1/2}}\|}_{2} \leq \varepsilon$, ${\|{{\hat{B}}_{t} - B_{t}^{\ast}}\|}_{2} \leq \varepsilon$, and ${\|{{\hat{Q}}_{t} - Q_{t}^{\ast}}\|}_{2} \leq \varepsilon$, ${\|{\hat{A}}_{t}\|}_{2} \leq c$ for dimension-free constant $c > 0$, and ${\hat{Q}}_{t} \succ 0$ for all $t \geq 0$. Let ${(K_{t}^{\ast})}_{t = 0}^{T - 1}$ and ${({\hat{K}}_{t})}_{t = 0}^{T - 1}$ be the optimal feedback gains of system $({(A_{t}^{\ast},B_{t}^{\ast},R_{t}^{\ast})}_{t = 0}^{T - 1},{(Q_{t}^{\ast})}_{t = 0}^{T})$ and system $({({\hat{A}}_{t},{\hat{B}}_{t},R_{t}^{\ast})}_{t = 0}^{T - 1},{({\hat{Q}}_{t})}_{t = 0}^{T})$, respectively.

Let $J{(K)}$ denote the expected cumulative cost in system $({(A_{t}^{\ast},B_{t}^{\ast},R_{t}^{\ast})}_{t = 0}^{T - 1},{(Q_{t}^{\ast})}_{t = 0}^{T})$ under state feedback control $u_{t} = {K_{t}x_{t}}$ for $t \geq 0$, and $J^{\delta}{(\hat{K})}$ denote the the expected cumulative cost in system $({(A_{t}^{\ast},B_{t}^{\ast},R_{t}^{\ast})}_{t = 0}^{T - 1},{(Q_{t}^{\ast})}_{t = 0}^{T})$ under control $u_{t} = {K_{t}{({x_{t} + \delta_{t}})}}$, where $\delta_{t}$ is a perturbation, for $t \geq 0$. Under control $u_{t} = {K_{t}{({x_{t} + \delta_{t}})}}$ for all $t \geq 0$, let ${\Xi_{t}{(K)}}:={{Cov}{(x_{t})}}$ in system $({(A_{t}^{\ast},B_{t}^{\ast},R_{t}^{\ast})}_{t = 0}^{T - 1},{(Q_{t}^{\ast})}_{t = 0}^{T})$, and assume that $\delta_{t}$ follows an arbitrary zero-mean Gaussian distribution, can be correlated with $x_{t}$, and satisfies ${\|{{Cov}{(\delta_{t})}}\|}_{2}^{1/2} \leq {\varphi{\max_{\tau \leq t}{\|{\Xi_{\tau}{(K)}}\|}_{2}^{1/2}}}$ for $t \geq 0$. There exist dimension-free constants ${\kappa,a_{2},a_{3},a_{4}} > 1$ that depends polynomially on $c$ and other problem parameters, such that under the condition of $\varepsilon,\varphi$ being small enough to ensure ${\|{\hat{B}}_{t}\|}_{2},{\|{\hat{Q}}_{t}\|}_{2}$ are of order $\mathcal{O}{}$, ${\lambda_{\min}{({\hat{Q}}_{t})}} = {\Omega{}}$ for all $t \geq 0$ and ${\varepsilon + \varphi} = {\mathcal{O}{({({{\kappaa_{2}} + a_{3}^{2}})}^{- T})}}$, we have

### Proof

First of all, we note that $\Sigma_{t}$, the covariance of $x_{t}$ under control $u_{t} \sim {\mathcal{N}{(0,{\sigma_{u}^{2}I})}}$ in system ${(A_{t}^{\ast},B_{t}^{\ast})}_{t = 0}^{T - 1}$, has $\mathcal{O}{}$ operator norm due to Assumption 1. ‣ 2 Problem setup ‣ Cost-Driven Representation Learning for Linear Quadratic Gaussian Control: Part I") and has covered all the possible directions of the state covariance $\Xi_{t}{(K)}$ in system ${(A_{t}^{\ast},B_{t}^{\ast})}_{t = 0}^{T - 1}$ under control $u_{t} = {K_{t}{({x_{t} + \delta_{t}})}}$, for all $t \geq 0$ for any $K$. Concretely, we claim the following.

### Claim 2

For any $K$ and $t \geq 0$, there exists some dimension-free $\varrho_{t} > 0$ that depends on $K$ and other problem parameters, such that ${\Xi_{t}{(K)}} \preccurlyeq {\varrho_{t}\Sigma_{t}}$.

The proof of Claim 2 is deferred to §4.5.1, which also applies to more general control inputs ${(u_{t})}_{t \geq 0}$. Now that $\varrho_{t}$ exists, a sufficiently large $\varrho_{t}$ is given by

as ${\Xi_{t}{(K)}} \preccurlyeq {{\|{\Xi_{t}{(K)}}\|}_{2}I}$ and ${\sigma_{\min}^{+}{(\Sigma_{t})}I} \preccurlyeq \Sigma_{t}$. We shall revisit the bounds on ${(\varrho_{t})}_{t \geq 0}$ later in the proof of Claim 3 in §4.5.2. By the definition of the operator norm, we have ${\|{{({{\hat{A}}_{t} - A_{t}^{\ast}})}\Xi_{t}^{1/2}{(\hat{K})}}\|}_{2} \leq {\|{{({{\hat{A}}_{t} - A_{t}^{\ast}})}{({\varrho_{t}\Sigma_{t}})}^{1/2}}\|}_{2} = {\mathcal{O}{({\varepsilon\varrho_{t}^{1/2}})}}$ for all $0 \leq t \leq {T - 1}$.

Next, we establish bounds on ${(K_{t}^{\ast})}_{t = 0}^{T - 1}$ and ${({\hat{K}}_{t})}_{t = 0}^{T - 1}$. Since ${(A_{t}^{\ast})}_{t = 0}^{T - 1}$ is uniformly exponentially stable, the optimal feedback gains ${(K_{t}^{\ast})}_{t = 0}^{T - 1}$ have $\mathcal{O}{}$ operator norms, due to the backward recursion with ${(A_{t}^{\ast})}_{t = 0}^{T - 1}$ as multipliers in (2.6) and (2.4). However, as ${({\hat{A}}_{t})}_{t = 0}^{T - 1}$ may not be uniformly exponentially stable, such arguments do not apply to ${({\hat{K}}_{t})}_{t = 0}^{T - 1}$; in the worse case, since $({({\hat{A}}_{t},{\hat{B}}_{t},R_{t}^{\ast})}_{t = 0}^{T - 1},{({\hat{Q}}_{t})}_{t = 0}^{T})$ have $\mathcal{O}{}$ operator norms, we can only guarantee that there exists a dimension-free constant $\kappa > 1$ that depends polynomially on $c$ and other problem parameters, such that ${\|{\hat{K}}_{t}\|}_{2} = {\mathcal{O}{(\kappa^{T - t})}}$, from the backward recursion in (2.6) and (2.4).

Let ${\hat{\Xi}}_{t}{(K)}$ denote the covariance of $x_{t}$ under feedback controller $u_{t} = {K_{t}{({x_{t} + \delta_{t}})}}$ in system ${({\hat{A}}_{t},{\hat{B}}_{t})}_{t = 0}^{T - 1}$. To bound $\Xi_{t}{(K)}$, ${\hat{\Xi}}_{t}{(K)}$ and their difference for either $K = K^{\ast}$ and $K = \hat{K}$, let us define for $t > t_{0}$,

with ${{\hat{\Phi}}_{t,t}{(K)}} = {\Phi_{t,t}^{\ast}{(K)}}:=I$, ${{\hat{\Phi}}_{t,t_{0}}{(K)}} = {\Phi_{t,t_{0}}^{\ast}{(K)}} = 0$ for $t < t_{0}$, and introduce the notation $x_{t}{(\tau,t_{0},x,K)}$, where $\tau \in {\lbrack t_{0},t\rbrack}$ denotes the time step at which the system dynamics *switch* from ${(A_{t}^{\ast},B_{t}^{\ast})}_{t = 0}^{T - 1}$ to ${({\hat{A}}_{t},{\hat{B}}_{t})}_{t = 0}^{T - 1}$, as:

Then, we can precisely relate and define

For bounding $\Xi_{t}{(K)}$, ${\hat{\Xi}}_{t}{(K)}$ and their difference, we have the following claim.

### Claim 3

There exists dimension-free constants ${a_{2},a_{3}} > 1$ that depend polynomially on $c$ and other problem parameters, such that for $K = \hat{K}$, for all $t \geq 0$, ${\|{\Xi_{t}{(\hat{K})}}\|}_{2} = {\mathcal{O}{(a_{2}^{T})}}$, ${\|{{\hat{\Xi}}_{t}{(\hat{K})}}\|}_{2} = {\mathcal{O}{(a_{2}^{T})}}$, and ${\|{{\Xi_{t}{(\hat{K})}} - {{\hat{\Xi}}_{t}{(\hat{K})}}}\|}_{2} = {\mathcal{O}{({{({\varepsilon\varphi})}{({\kappaa_{2}^{2}})}^{T}})}}$; and that for $K = K^{\ast}$, for all $t \geq 0$, ${\|{\Xi_{t}{(K^{\ast})}}\|}_{2} = {\mathcal{O}{(t)}}$, ${\|{{\hat{\Xi}}_{t}{(K^{\ast})}}\|}_{2} = {\mathcal{O}{(t)}}$, and ${\|{{\Xi_{t}{(K^{\ast})}} - {{\hat{\Xi}}_{t}{(K^{\ast})}}}\|}_{2} = {\mathcal{O}{({{({\varepsilon + \varphi})}ta_{3}^{2t}})}}$.

The proof of Claim 3 is deferred to §4.5.2. A core idea of the proof is to use inverse telescoping to express ${\Xi_{t}{(K)}} - {{\hat{\Xi}}_{t}{(K)}}$.

Recall that $J^{\delta}{(K)}$ denotes the expected cumulative cost in system $({(A_{t}^{\ast},B_{t}^{\ast},R_{t}^{\ast})}_{t = 0}^{T - 1},{(Q_{t}^{\ast})}_{t = 0}^{T})$ under state feedback controller $u_{t} = {K_{t}{({x_{t} + \delta_{t}})}}$ for $t \geq 0$. Similarly, let ${\hat{J}}^{\delta}{(K)}$ denote the corresponding expected cumulative cost in system $({({\hat{A}}_{t},{\hat{B}}_{t},R_{t}^{\ast})}_{t = 0}^{T - 1},{({\hat{Q}}_{t})}_{t = 0}^{T})$. Notice that

where ${(Q_{t}^{\ast})}^{\prime}:={({Q_{t}^{\ast} + {K_{t}^{\top}R_{t}^{\ast}K_{t}}})}$ for $0 \leq t \leq {T - 1}$, ${(Q_{T}^{\ast})}^{\prime}:=Q_{T}^{\ast}$, and

where ${\hat{Q}}_{t}^{\prime} = {{\hat{Q}}_{t} + {K_{t}^{\top}R_{t}^{\ast}K_{t}}}$ for $0 \leq t \leq {T - 1}$, ${\hat{Q}}_{T}^{\prime} = {\hat{Q}}_{T}$, and

Hence, for $K = \hat{K}$, we have

where $(i)$ uses the fact that ${\|{\hat{Q}}_{t}^{\prime}\|}_{2} = {\mathcal{O}{({\|{\hat{K}}_{t}\|}_{2}^{2})}} = {\mathcal{O}{(\kappa^{2{({T - t})}})}}$. For $K = K^{\ast}$, we have

where $(i)$ uses the fact that ${\|{\hat{Q}}_{t}^{\prime}\|}_{2} = {\mathcal{O}{({\| K_{t}^{\ast}\|}_{2}^{2})}} = {\mathcal{O}{}}$. Define $a_{4} = {\max{({\kappa^{3}a_{2}^{2}},a_{3}^{3})}}$. Then, whether $K = K^{\ast}$ or $K = \hat{K}$, we have

Let ${\hat{\Xi}}_{t}^{0}{(K)}$ denote the covariance of $x_{t}$ under feedback controller $u_{t} = {K_{t}x_{t}}$ in system ${({\hat{A}}_{t},{\hat{B}}_{t})}_{t = 0}^{T - 1}$, without perturbation. To bridge the difference in the expected cumulative costs with and without perturbations, we claim the following.

### Claim 4

For all $t \geq 0$,

The proof of Claim 4, similar to that of Claim 3, is deferred to §4.5.3. Hence,

Combining the above results, we have

where ${{\hat{J}{(\hat{K})}} - {\hat{J}{(K^{\ast})}}} \leq 0$ in $(i)$ due to the optimality of $\hat{K}$ in the system $({({\hat{A}}_{t},{\hat{B}}_{t},R_{t}^{\ast})}_{t = 0}^{T - 1},{({\hat{Q}}_{t})}_{t = 0}^{T})$.

### Proof of Claim 2

We prove the claim by induction. For time step $0$, clearly, $\Xi_{0} = \Sigma_{0}$ and $\varrho_{0} = 1$. Suppose for time step $t$, $\Xi_{t} \preccurlyeq {\varrho_{t}\Sigma_{t}}$. Since $x_{t + 1} = {{{({A_{t}^{\ast} + {B_{t}^{\ast}K_{t}}})}x_{t}} + {B_{t}^{\ast}K_{t}\delta_{t}} + w_{t}}$, we have that for step $t + 1$,

Since for any $F,G$ and positive semidefinite $P$, we have ${{FPG^{\top}} + {GPF^{\top}}} \preccurlyeq {{FPF^{\top}} + {GPG^{\top}}}$ as ${{({F - G})}P{({F - G})}^{\top}} \succcurlyeq 0$. Then,

Hence, for $\varrho_{t + 1} \geq 1$,

To ensure ${\varrho_{t + 1}\Sigma_{t + 1}} \succcurlyeq {\Xi_{t + 1}{(K)}}$, it suffices to take $\varrho_{t + 1} \geq {{4\varrho_{t}{({1 + {\sigma_{u}^{- 2}{\| K_{t}\|}_{2}^{2}{\|\Sigma_{t}\|}_{2}}})}} + {2\sigma_{u}^{- 2}{\| K_{t}\|}_{2}^{2}{\|{{Cov}{(\delta_{t})}}\|}_{2}}}$, which completes the proof. ∎

### Proof of Claim 3

By the definition of $x_{t}{(\tau,t_{0},x,K)}$, we have that for $t_{2} \leq t_{1} \leq t$,

Hence, for $0 \leq \tau < t$,

As $x_{t}{(\tau,0,x_{0},K)}$ and ${(w_{t_{0}})}_{t_{0} \geq \tau}$ have the same distributions in the above expressions of $x_{t}{({\tau + 1},\tau,{x_{\tau}{(\tau,0,x_{0},K)}},K)}$ and $x_{t}{(\tau,\tau,{x_{\tau}{(\tau,0,x_{0},K)}},K)}$, and covariances are expectations, we can couple $x_{t}{(\tau,0,x_{0},K)}$ and ${(w_{t_{0}})}_{t_{0} \geq \tau}$ therein without changing the two covariances. On the other hand, ${(\delta_{t_{0}})}_{t_{0} \geq \tau}$ may not have the same distributions in the two trajectories generating $x_{t}{({\tau + 1},\tau,{x_{\tau}{(\tau,0,x_{0},K)}},K)}$ and $x_{t}{(\tau,\tau,{x_{\tau}{(\tau,0,x_{0},K)}},K)}$, and we let ${(\delta_{t_{0}}^{({\tau + 1})})}_{t_{0} \geq \tau},{(\delta_{t_{0}}^{(\tau)})}_{t_{0} \geq \tau}$ denote the perturbations in the respective trajectory. As a shorthand, define

Next, we consider $K = \hat{K}$ and $K = K^{\ast}$ separately.

For $K = \hat{K}$, let ${({\hat{P}}_{t})}_{t = 0}^{T}$ be the optimal value matrices for system $({({\hat{A}}_{t},{\hat{B}}_{t},R_{t}^{\ast})}_{t = 0}^{T - 1},{({\hat{Q}}_{t})}_{t = 0}^{T})$, given by (2.6) with the system matrices $({(A_{t}^{\ast},B_{t}^{\ast},R_{t}^{\ast})}_{t = 0}^{T - 1},{(Q_{t}^{\ast})}_{t = 0}^{T})$ replaced. Since ${\|{\hat{A}}_{t}\|}_{2} \leq c$ and ${\|{\hat{B}}_{t}\|}_{2},{\| R_{t}^{\ast}\|}_{2},{\|{\hat{Q}}_{t}\|}_{2}$ are of order $\mathcal{O}{}$ for all $t \geq 0$, there exists some dimension-free constant $a_{2} > 1$ depending polynomially on $c$ and other problem parameters, such that ${\|{\hat{P}}_{t}\|}_{2} = {\mathcal{O}{(a_{2}^{T - t})}}$, due to the backward recursion in (2.6). For any $0 \leq \tau \leq t$ and $x_{\tau} \in {\mathbb{R}}^{d_{x}}$, by the definition of ${({\hat{P}}_{t})}_{t \geq 0}$,

Maximizing both sides for $x_{\tau} \in {\mathbb{S}}^{d_{x} - 1}$ and by the definition of the operator norm, we have

Since ${\lambda_{\min}{({\hat{Q}}_{t})}} = {\Omega{}}$, ${\lambda_{\min}{({\hat{P}}_{t})}} = {\Omega{}}$. Hence,

Now we are ready to bound $\Xi_{t}{(\hat{K})}$, $\varrho_{t}$, ${\|{{\Xi_{t}{(\hat{K})}} - {{\hat{\Xi}}_{t}{(\hat{K})}}}\|}_{2}$ and ${\hat{\Xi}}_{t}{(\hat{K})}$ by induction. First, ${\|{\Xi_{0}{(\hat{K})}}\|}_{2} = {\|\Sigma_{0}\|}_{2} = {\mathcal{O}{}} = {\mathcal{O}{(a_{2}^{T})}}$ and $\varrho_{0} = 1 = {\mathcal{O}{(a_{2}^{T})}}$. Suppose ${\|{\Xi_{\tau}{(\hat{K})}}\|}_{2} = {\mathcal{O}{(a_{2}^{T})}}$ and $\varrho_{\tau} = {\mathcal{O}{(a_{5}^{T})}}$ for all $\tau < t$. Then, for all $\tau < t$, ${\|{{Cov}{(\delta_{\tau})}}\|}_{2} = {\mathcal{O}{({\varphi^{2}{\max_{t_{0} \leq \tau}{\|{\Xi_{t_{0}}{(\hat{K})}}\|}_{2}}})}} = {\mathcal{O}{({\varphi^{2}a_{2}^{T}})}}$, and (4.9) is bounded by

where we recall that ${\|{\hat{K}}_{t}\|}_{2} = {\mathcal{O}{(\kappa^{T - t})}}$ and the assumption that ${\|{{\hat{B}}_{t} - B_{t}^{\ast}}\|}_{2} \leq \varepsilon = {\mathcal{O}{({({\kappaa_{2}})}^{- T})}} = {\mathcal{O}{}}$. Similarly, for $\tau < t$, we have (4.10) is bounded by

due to ${\|\Sigma_{w_{t}}\|}_{2} = {\mathcal{O}{}}$ and $\varphi = {\mathcal{O}{({({\kappaa_{2}})}^{- T})}} = {\mathcal{O}{(\kappa^{- T})}}$. Hence, by (4.8) and our assumption that ${\varepsilon + \varphi} = {\mathcal{O}{({({\kappaa_{2}})}^{- T})}} = {\mathcal{O}{(\kappa^{- T})}}$, we have

Using inverse telescoping, we have

On the other hand, since

and the operator norms of $\Sigma_{0}$ and ${(\Sigma_{w_{t}})}_{t \geq 0}$ are $\mathcal{O}{}$, by Lemma 15, we have

due to $\varphi = {\mathcal{O}{({({\kappaa_{2}})}^{- T})}} = {\mathcal{O}{({({\kappaa_{2}^{1/2}})}^{- T})}}$.

Therefore, ${\|{\Xi_{t}{(\hat{K})}}\|}_{2} \leq {{\|{{\hat{\Xi}}_{t}{(\hat{K})}}\|}_{2} + {\|{{\Xi_{t}{(\hat{K})}} - {{\hat{\Xi}}_{t}{(\hat{K})}}}\|}_{2}} = {\mathcal{O}{({a_{5}^{T} + {{({\varepsilon + \varphi})}{({\kappaa_{2}^{2}})}^{T}}})}}$. Since ${\varepsilon + \varphi} = {\mathcal{O}{({({\kappaa_{2}})}^{- T})}}$, we have ${\|{\Xi_{t}{(\hat{K})}}\|}_{2} = {\mathcal{O}{(a_{5}^{T})}}$. Then, by (4.7), $\varrho_{t} = {\mathcal{O}{({\|{\Xi_{t}{(\hat{K})}}\|}_{2})}} = {\mathcal{O}{(a_{5}^{T})}}$. By induction, we have that for all $0 \leq t \leq T$, $\varrho_{t} = {\mathcal{O}{(a_{2}^{T})}}$ and ${\|{{{\hat{\Xi}}_{t}{(\hat{K})}} - {\Xi_{t}{(\hat{K})}}}\|}_{2} = {\mathcal{O}{({{({\varepsilon + \varphi})}{({\kappaa_{2}^{2}})}^{T}})}}$.

For $K = K^{\ast}$, we first bound $\Xi_{t}{(K^{\ast})}$. Let ${(P_{t}^{\ast})}_{t = 0}^{T}$ be the optimal value matrices for system $({(A_{t}^{\ast},B_{t}^{\ast},R_{t}^{\ast})}_{t = 0}^{T - 1},{(Q_{t}^{\ast})}_{t = 0}^{T})$, given by (2.6). Since $({(A_{t}^{\ast},B_{t}^{\ast},R_{t}^{\ast})}_{t = 0}^{T - 1},{(Q_{t}^{\ast})}_{t = 0}^{T})$ have $\mathcal{O}{}$ operator norms and ${(A_{t}^{\ast})}_{t = 0}^{T - 1}$ is uniformly exponentially stable, ${\| P_{t}^{\ast}\|}_{2} = {\mathcal{O}{}}$ for all $t \geq 0$, due to the backward recursion given by (2.6). For any $0 \leq \tau \leq t$ and $x_{\tau} \in {\mathbb{R}}^{d_{x}}$, since the value at time step $\tau$ is no less than the value at time step $t \geq \tau$, we have that

Maximizing both sides for $x_{\tau} \in {\mathbb{S}}^{d_{x} - 1}$ and by the definition of the operator norm, we have

Since ${\lambda_{\min}{(Q_{t}^{\ast})}} = {\Omega{}}$, ${\lambda_{\min}{(P_{t}^{\ast})}} = {\Omega{}}$. Hence,

Now we show that ${\|{\Xi_{t}{(K^{\ast})}}\|}_{2} = {\mathcal{O}{(t)}}$ by induction. First, ${\|{\Xi_{0}{(K^{\ast})}}\|}_{2} = {\|\Sigma_{0}\|}_{2} = {\mathcal{O}{}}$. Assume ${\|{\Xi_{\tau}{(K^{\ast})}}\|}_{2} = {\mathcal{O}{(\tau^{1/2})}}$ for all $\tau < t$. Then, since

Since the operator norms of $\Sigma_{0}$, ${(\Sigma_{w_{t}})}_{t \geq 0}$ are $\mathcal{O}{}$, by the independence of $x_{0}$ and ${(w_{\tau})}_{\tau \geq 0}$, we have

Note that here we leverage independence instead of applying Lemma 15, which yields a worse bound of $\mathcal{O}{(t)}$. Then, since $\varphi = {\mathcal{O}{({({\kappaa_{2}})}^{- T})}} = {\mathcal{O}{(t^{- 1})}}$, we have

Hence, for all $t \geq 0$, ${\|{\Xi_{t}{(K^{\ast})}}\|}_{2} = {\mathcal{O}{(t)}}$. Then, by (4.7), ${\Xi_{t}{(K^{\ast})}} \leq {\varrho_{t}\Sigma_{t}}$ for $\varrho_{t} = {\mathcal{O}{({\|{\Xi_{t}{(K^{\ast})}}\|}_{2})}} = {\mathcal{O}{(t)}}$.

Next, we bound ${\hat{\Phi}}_{t,\tau}{(K^{\ast})}$ in order to bound (4.9) and (4.10). Since ${\|{\hat{A}}_{t}\|}_{2} \leq c$ and ${\|{\hat{B}}_{t}\|}_{2},{\| K_{t}^{\ast}\|}_{2}$ are order $\mathcal{O}{}$, there exists a dimension-free constant $a_{3} > 1$ depending polynomially on $c$ and other problem parameters, such that ${\|{{\hat{\Phi}}_{t,\tau}{(K^{\ast})}}\|}_{2} = {\mathcal{O}{(a_{3}^{t - \tau})}}$. Then, (4.9) is bounded by

Using inverse telescoping, we have

Finally, since ${\varepsilon + \varphi} = {\mathcal{O}{(a_{3}^{- {2T}})}}$, we have

completing the proof. ∎

### Proof of Claim 4

where $\tau \leq t$ denotes the time step at which the controller switches from $u_{t} = {{\hat{K}}_{t}{({x_{t} + \delta_{t}})}}$ to $u_{t} = {{\hat{K}}_{t}x_{t}}$, $t_{0} \leq \tau$ denotes the initial time step, and $x$ is the state at $t_{0}$. Then, we know

By definition, for $t_{2} \leq t_{1} < t$,

Hence, for $0 \leq \tau < t$,

where we couple the $x_{\tau}{(\tau,0,x_{0})}$ and ${(w_{t_{0}})}_{t_{0} \geq \tau}$ in the two trajectories generating $x_{t}{({\tau + 1},\tau,{x_{\tau}{(\tau,0,x_{0})}})}$ and $x_{t}{(\tau,\tau,{x_{\tau}{(\tau,0,x_{0})}})}$. Then, by Lemma 14,

Since ${\|{\Xi_{t}{(\hat{K})}}\|}_{2} = {\mathcal{O}{(a_{2}^{T})}}$ by Claim 3,

where $(i)$ follows from ${\|{\hat{\Xi}{(\hat{K})}}\|}_{2} = {\mathcal{O}{(a_{2}^{T})}}$ by Claim 3. Hence, by our assumption that $\varphi = {\mathcal{O}{({({\kappaa_{2}})}^{- T})}} = {\mathcal{O}{(\kappa^{- T})}}$,

Finally, using inverse telescoping, we have

which completes the proof. ∎

If the input of linear regression has full-rank covariance, then by Lemma 6. ‣ 4.4.1 Proof of Claim 1 ‣ 4.4 Perturbed linear regression bound ‣ 4 Theoretical guarantees and proofs ‣ Cost-Driven Representation Learning for Linear Quadratic Gaussian Control: Part I"), the system parameters can be fully identified. To certify the performance of the certainty equivalent optimal controller, we need the performance difference lemma. To specify it for our LQR problem, we define the value function $V_{t}^{K}{(x)}$ as the expected cumulative cost starting from state $x$ at time step $t$ under control $u_{t} = {K_{t}x_{t}}$ for $t \geq 0$. Let $P_{T}^{K} = Q_{T}$, and for $t \geq 0$, define value matrices $P_{t}^{K}$ through the backward recursion

Then, it is easy to verify that $V_{t}^{K}{(x)}$ satisfies

The following lemma is the counterpart of in the LTV setting with system noises.

### Lemma 8 (Performance difference lemma)

Consider the finite-horizon linear quadratic control problem $({(A_{t}^{\ast},B_{t}^{\ast},R_{t}^{\ast})}_{t = 0}^{T - 1},{(Q_{t}^{\ast})}_{t = 0}^{T})$. Let $V_{t}^{u}{(x)}$ be the expected cumulative cost starting from state $x$ at time step $t$ under control ${(u_{t})}_{t \geq 0}$. Define $E_{t}^{K}:={{{({R_{t}^{\ast} + {{(B_{t}^{\ast})}^{\top}P_{t + 1}^{K}B_{t}^{\ast}}})}K_{t}} + {{(B_{t}^{\ast})}^{\top}P_{t + 1}^{K}A_{t}^{\ast}}}$ for $t \geq 0$. Then, for all $t \geq 0$ and $x \in {\mathbb{R}}^{d_{x}}$,

where $x_{\tau}^{u}$ denotes the state at time step $\tau \geq t$ under control ${(u_{t})}_{t \geq 0}$ starting from $x_{t}^{u} = x$, and for $0 \leq t \leq {T - 1}$,

### Proof

For $\tau \geq t$, let $c_{\tau}^{u}$ denote the cost at time step $t$ under control ${(u_{t})}_{t \geq 0}$ starting from $x_{t}^{u} = x$. Then, by the definition of $V_{t}^{u}{(x)}$, we have

Then, by the law of total expectation, ${{V_{t}^{u}{(x)}} - {V_{t}^{K}{(x)}}} = {\sum_{\tau = t}^{T - 1}{{\mathbb{E}}{\lbrack{D_{\tau}^{K}{(x_{\tau}^{u},u_{t})}}\rbrack}}}$. Notice that

The following lemma shows that the certainty equivalent optimal controller for LQ control in the full-rank case has a much better guarantee compared to the rank-deficient case.

### Lemma 9 (Linear quadratic control)

Consider the finite-horizon time-varying linear dynamical system given by the first equation in (2.1) with quadratic costs given by (2.2), under Assumption 3. ‣ 2 Problem setup ‣ Cost-Driven Representation Learning for Linear Quadratic Gaussian Control: Part I") with $\ell = 1$ and Assumption 4 on the relevant problem parameters. Let ${(K_{t}^{\ast})}_{t = 0}^{T - 1}$ be the optimal feedback gains and ${(P_{t}^{\ast})}_{t = 0}^{T}$ be the solution to the RDE (2.6) of system $({(A_{t}^{\ast},B_{t}^{\ast},R_{t}^{\ast})}_{t = 0}^{T - 1},{(Q_{t}^{\ast})}_{t = 0}^{T})$. Let ${({\hat{K}}_{t})}_{t = 0}^{T - 1}$ be the optimal feedback gains and ${({\hat{P}}_{t})}_{t = 0}^{T}$ be the solution to the RDE (2.6) of system $({({\hat{A}}_{t},{\hat{B}}_{t},R_{t}^{\ast})}_{t = 0}^{T - 1},{({\hat{Q}}_{t})}_{t = 0}^{T})$, where ${\|{{\hat{A}}_{t} - A_{t}^{\ast}}\|}_{2} \leq \varepsilon$, ${\|{{\hat{B}}_{t} - B_{t}^{\ast}}\|}_{2} \leq \varepsilon$, ${\|{{\hat{Q}}_{t} - Q_{t}^{\ast}}\|}_{2} \leq \varepsilon$, and ${({\hat{Q}}_{t})}_{t = 0}^{T}$ are positive semidefinite. For any feedback gains ${(K_{t})}_{t = 0}^{T - 1}$, let $J{(\hat{K})}$ denote the expected cumulative cost in system $({(A_{t}^{\ast},B_{t}^{\ast},R_{t}^{\ast})}_{t = 0}^{T - 1},{(Q_{t}^{\ast})}_{t = 0}^{T})$ under the state feedback control $u_{t} = {K_{t}x_{t}}$ for $t \geq 0$. Then, there exists a dimension-free constant $\varepsilon_{0} > 0$ with $\varepsilon_{0}^{- 1}$ depending polynomially on problem parameters, such that as long as $\varepsilon \leq \varepsilon_{0}$, ${\|{{\hat{P}}_{t} - P_{t}^{\ast}}\|}_{2} = {\mathcal{O}{(\varepsilon)}}$, ${\|{{\hat{K}}_{t} - K_{t}^{\ast}}\|}_{2} = {\mathcal{O}{(\varepsilon)}}$ for all $t \geq 0$, and

### Proof

This problem is studied in for the infinite-horizon LTI setting; here we extend their result to the finite-horizon LTV setting.

We adopt the following compact formulation of a finite-horizon LTV system, as introduced in, to reduce our setting to the infinite-horizon LTI one:

The control inputs using state feedback controller ${(K_{t})}_{t = 0}^{T - 1}$ can be characterized by $u = {Kx}$. Let ${(P_{t}^{K})}_{t = 0}^{T}$ be the associated value matrix starting from step $t$. Then

and $P^{K}:={\text{diag}{(P_{0}^{K},\ldots,P_{T}^{K})}}$ is the solution to

Similarly, the optimal value matrix

produced by the RDE (2.6) in system $(A^{\ast},B^{\ast},R^{\ast},Q^{\ast})$, satisfies

Let $\hat{P} = {\text{diag}{({\hat{P}}_{0},\ldots,{\hat{P}}_{T})}}$ be the optimal cumulative cost matrices in system $(\hat{A},\hat{B},\hat{Q},R^{\ast})$ by the RDE (2.6). With a slight abuse of notation, define $K^{\ast}:={\lbrack{\text{diag}{(K_{0}^{\ast},\ldots,K_{T - 1}^{\ast})}},0_{{d_{u}T} \times d_{x}}\rbrack}$, where ${(K_{t}^{\ast})}_{t = 0}^{T - 1}$ is the optimal controller in system $(A^{\ast},B^{\ast},Q^{\ast},R^{\ast})$, and define $\hat{K}$ similarly for system $(\hat{A},\hat{B},\hat{Q},R^{\ast})$. By definition, $A^{\ast}$ is stable (hence, stabilizable), $(A^{\ast},Q^{\ast})$ is observable in the sense of LTI systems, and $R^{\ast} \succ 0$. Therefore, by, there exists a dimension-free constant $\varepsilon_{0} > 0$ with $\varepsilon_{0}^{- 1}$ depending polynomially on problem parameters such that as long as $\varepsilon \leq \varepsilon_{0}$,

and that $\hat{K}$ stabilizes system $(A^{\ast},B^{\ast})$. By Lemma 8. ‣ 4.5.3 Proof of Claim 4 ‣ 4.5 Certainty equivalent linear quadratic control ‣ 4 Theoretical guarantees and proofs ‣ Cost-Driven Representation Learning for Linear Quadratic Gaussian Control: Part I"),

where in $(i)$ the term $E_{t}^{K} = 0$ in Lemma 8. ‣ 4.5.3 Proof of Claim 4 ‣ 4.5 Certainty equivalent linear quadratic control ‣ 4 Theoretical guarantees and proofs ‣ Cost-Driven Representation Learning for Linear Quadratic Gaussian Control: Part I") for $K = K^{\ast}$, and in $({ii})$ we define $\Sigma:={\text{diag}{(\Sigma_{0},\ldots,\Sigma_{T})}}$ with $\Sigma_{t}$ being ${\mathbb{E}}{\lbrack{x_{t}x_{t}^{\top}}\rbrack}$ in system $(A^{\ast},B^{\ast})$ under state feedback controller $\hat{K}$. As a result,

Since $\hat{K}$ stabilizes system $(A^{\ast},B^{\ast})$, ${\|\Sigma\|}_{2} = {\mathcal{O}{}}$. Since

and thus complete the proof. ∎

Finally, we are ready to present the main lemma of this section below, which combines Lemmas 7. ‣ 4.5 Certainty equivalent linear quadratic control ‣ 4 Theoretical guarantees and proofs ‣ Cost-Driven Representation Learning for Linear Quadratic Gaussian Control: Part I") to 9. ‣ Proof. ‣ 4.5.3 Proof of Claim 4 ‣ 4.5 Certainty equivalent linear quadratic control ‣ 4 Theoretical guarantees and proofs ‣ Cost-Driven Representation Learning for Linear Quadratic Gaussian Control: Part I") to provide an end-to-end guarantee for the certainty equivalent optimal controller in linear quadratic control with both rank-deficient and full-rank stages.

### Lemma 10

Consider the finite-horizon linear time-varying system given by the first equation in (2.1) with quadratic costs given by (2.2), under Assumption 1. ‣ 2 Problem setup ‣ Cost-Driven Representation Learning for Linear Quadratic Gaussian Control: Part I"), Assumption 3. ‣ 2 Problem setup ‣ Cost-Driven Representation Learning for Linear Quadratic Gaussian Control: Part I") and Assumption 4 on the relevant problem parameters. Let $\Sigma_{t}:={{Cov}{(x_{t})}}$ under control $u_{t} \sim {\mathcal{N}{(0,{\sigma_{u}^{2}I})}}$ for all $t \geq 0$, which may not have full rank. Let ${({\hat{A}}_{t},{\hat{B}}_{t})}_{t = 0}^{T - 1},{({\hat{Q}}_{t})}_{t = 0}^{T}$ satisfy ${\|{{({{\hat{A}}_{t} - A_{t}^{\ast}})}\Sigma_{t}}\|}_{2} \leq \varepsilon_{1}$, ${\|{{\hat{B}}_{t} - B_{t}^{\ast}}\|}_{2} \leq \varepsilon_{1}$, ${\|{{\hat{Q}}_{t} - Q_{t}^{\ast}}\|}_{2} \leq \varepsilon_{1}$, ${\|{\hat{A}}_{t}\|}_{2} \leq c$ for dimension-free constant $c > 0$, ${\hat{Q}}_{t} \succ 0$ for $0 \leq t \leq {\ell - 1}$, and ${\|{{\hat{A}}_{t} - A_{t}^{\ast}}\|}_{2} \leq \varepsilon_{2}$, ${\|{{\hat{B}}_{t} - B_{t}^{\ast}}\|}_{2} \leq \varepsilon_{2}$, ${\|{{\hat{Q}}_{t} - Q_{t}^{\ast}}\|}_{2} \leq \varepsilon_{2}$, ${\hat{Q}}_{t} \succcurlyeq 0$ for $t \geq \ell$, where ${\varepsilon_{1},\varepsilon_{2}} \geq 0$. Let ${(K_{t}^{\ast})}_{t = 0}^{T - 1}$ and ${({\hat{K}}_{t})}_{t = 0}^{T - 1}$ be the optimal feedback gains of system $({(A_{t}^{\ast},B_{t}^{\ast},R_{t}^{\ast})}_{t = 0}^{T - 1},{(Q_{t}^{\ast})}_{t = 0}^{T})$ and system $({({\hat{A}}_{t},{\hat{B}}_{t},R_{t}^{\ast})}_{t = 0}^{T - 1},{({\hat{Q}}_{t})}_{t = 0}^{T})$, respectively.

For any feedback gains ${(K_{t})}_{t = 0}^{T - 1}$, let $J{(K)}$ denote the expected cumulative cost in system $({(A_{t}^{\ast},B_{t}^{\ast},R_{t}^{\ast})}_{t = 0}^{T - 1}$, ${(Q_{t}^{\ast})}_{t = 0}^{T})$ under state feedback control $u_{t} = {K_{t}x_{t}}$ for $t \geq 0$, and $J^{\delta}{(K)}$ denote the expected cumulative cost in system $({(A_{t}^{\ast},B_{t}^{\ast},R_{t}^{\ast})}_{t = 0}^{T - 1},{(Q_{t}^{\ast})}_{t = 0}^{T})$ under control $u_{t} = {K_{t}{({x_{t} + \delta_{t}})}}$, where $\delta_{t}$ is a perturbation, for $t \geq 0$. Under control $u_{t} = {K_{t}{({x_{t} + \delta_{t}})}}$ for all $t \geq 0$, let ${\Xi_{t}{(K)}}:={{Cov}{(x_{t})}}$ in the system $({(A_{t}^{\ast},B_{t}^{\ast},R_{t}^{\ast})}_{t = 0}^{T - 1},{(Q_{t}^{\ast})}_{t = 0}^{T})$, and assume that $\delta_{t}$ follows an arbitrary zero-mean Gaussian distribution, can be correlated with $x_{t}$, and satisfies ${\|{{Cov}{(\delta_{t})}}\|}_{2}^{1/2} \leq {\varphi_{1}{\max_{\tau \leq t}{\|{\Xi_{\tau}{(K)}}\|}_{2}^{1/2}}}$ for $0 \leq t \leq {\ell - 1}$ and ${\|{{Cov}{(\delta_{t})}}\|}_{2}^{1/2} \leq {\varphi_{2}{\max_{\tau \leq t}{\|{\Xi_{\tau}{(K)}}\|}_{2}^{1/2}}}$ for $t \geq \ell$.

There exist dimension-free constants ${\kappa,a_{2},a_{3},a_{4}} > 1$ that depend polynomially on $c$ and other problem parameters and dimension-free constant $\varepsilon_{0} > 0$ with $\varepsilon_{0}^{- 1}$ depending polynomially on problem parameters, such that under the conditions that 1) $\varepsilon_{1},\varphi_{1}$ are small enough to ensure ${\|{\hat{B}}_{t}\|}_{2},{\|{\hat{Q}}_{t}\|}_{2}$ are of order $\mathcal{O}{}$, ${\lambda_{\min}{({\hat{Q}}_{t})}} = {\Omega{}}$ for $0 \leq t \leq {\ell - 1}$ and ${\varepsilon_{1} + \varphi_{1}} = {\mathcal{O}{({({{\kappaa_{2}} + a_{3}^{2}})}^{- T})}}$, and that 2) $\varepsilon_{2},\varphi_{2}$ are small enough to ensure $\varepsilon_{2} \leq \varepsilon_{0}$ and ${\varepsilon_{2} + \varphi_{2}} = {\mathcal{O}{({\varepsilon_{1} + \varphi_{1}})}} = {\mathcal{O}{(T^{- 1})}}$, we have

### Proof

Let us begin by introducing some notation. For feedback gains ${(K_{t})}_{t = 0}^{T - 1}$ and $d_{x} \times d_{x}$ matrix $P_{\ell} \succ 0$, let $J_{1}^{\delta}{(K,P_{\ell})}$ denote the expected cumulative cost under $u_{t} = {K_{t}{({x_{t} + \delta_{t}})}}$ for $t \geq 0$, in system $({(A_{t}^{\ast},B_{t}^{\ast},R_{t}^{\ast})}_{t = 0}^{T - 1},{(Q_{t}^{\ast})}_{t = 0}^{T})$ for $0 \leq t \leq \ell$, with $c_{\ell} = {\| x_{\ell}\|}_{P_{\ell}}^{2}$; let $J_{1}{(K,P_{\ell})}$ denote the corresponding expected cumulative cost under $u_{t} = {K_{t}x_{t}}$ for $t \geq 0$. Let $x_{t}^{\delta}$ denote the state at step $t$ in system $({(A_{t}^{\ast},B_{t}^{\ast},R_{t}^{\ast})}_{t = 0}^{T - 1},{(Q_{t}^{\ast})}_{t = 0}^{T})$ under control $u_{t} = {{\hat{K}}_{t}{({x_{t} + \delta_{t}})}}$. For feedback gains ${(K_{t})}_{t = 0}^{T - 1}$, let $J_{2}^{\delta}{(K)}$ denote the expected cumulative cost under $u_{t} = {K_{t}{({x_{t} + \delta_{t}})}}$ for $t \geq \ell$, in system $({(A_{t}^{\ast},B_{t}^{\ast},R_{t}^{\ast})}_{t = 0}^{T - 1},{(Q_{t}^{\ast})}_{t = 0}^{T})$ starting from $x_{\ell}^{\delta}$; let $J_{2}{(K)}$ denote the corresponding expected cumulative cost under $u_{t} = {K_{t}x_{t}}$ for $t \geq \ell$.

Let ${(P_{t}^{\hat{K}})}_{t = 0}^{T}$ denote the value matrices in system $({(A_{t}^{\ast},B_{t}^{\ast},R_{t}^{\ast})}_{t = 0}^{T - 1},{(Q_{t}^{\ast})}_{t = 0}^{T})$ under control $u_{t} = {{\hat{K}}_{t}x_{t}}$ for $t \geq 0$, given by recursion (4.12). By definition, we have

By the property of the value function given in (4.13),

Then, by substituting ${\mathbb{E}}\left\lbrack {\| x_{\ell}^{\delta}\|}_{P_{\ell}^{\hat{K}}}^{2} \right\rbrack$ from the above equation into (4.14), we have

On the other hand, let ${(P_{t}^{\ast})}_{t = 0}^{T}$ and ${({\hat{P}}_{t})}_{t = 0}^{T}$ denote the optimal value matrices in system $({(A_{t}^{\ast},B_{t}^{\ast},R_{t}^{\ast})}_{t = 0}^{T - 1}$, ${(Q_{t}^{\ast})}_{t = 0}^{T})$ and system $({({\hat{A}}_{t},{\hat{B}}_{t},R_{t}^{\ast})}_{t = 0}^{T - 1},{({\hat{Q}}_{t})}_{t = 0}^{T})$, respectively, given by RDE (2.6). Similarly, we have

Let $\varepsilon_{0}$ be the one required in Lemma 9. ‣ Proof. ‣ 4.5.3 Proof of Claim 4 ‣ 4.5 Certainty equivalent linear quadratic control ‣ 4 Theoretical guarantees and proofs ‣ Cost-Driven Representation Learning for Linear Quadratic Gaussian Control: Part I"). Then, applying Lemma 9. ‣ Proof. ‣ 4.5.3 Proof of Claim 4 ‣ 4.5 Certainty equivalent linear quadratic control ‣ 4 Theoretical guarantees and proofs ‣ Cost-Driven Representation Learning for Linear Quadratic Gaussian Control: Part I") to the last $T - \ell$ steps, we have ${\|{{\hat{P}}_{\ell} - P_{\ell}^{\ast}}\|}_{2} = {\mathcal{O}{(\varepsilon_{2})}} = {\mathcal{O}{(\varepsilon_{1})}}$. Hence, for the first $\ell$ steps, by Lemma 7. ‣ 4.5 Certainty equivalent linear quadratic control ‣ 4 Theoretical guarantees and proofs ‣ Cost-Driven Representation Learning for Linear Quadratic Gaussian Control: Part I"), there exists a dimension-free constant $a_{4} > 1$ that depends polynomially on problem parameters, such that

Given feedback gains ${(K_{t})}_{t = 0}^{T - 1}$, for $t > \tau$, define ${\Phi_{t,\tau}^{\ast}{(K)}}:={{({A_{t - 1}^{\ast} + {B_{t - 1}^{\ast}K_{t - 1}}})}\cdots{({A_{\tau}^{\ast} + {B_{\tau}^{\ast}K_{\tau}}})}}$ and define ${\Phi_{\tau,\tau}^{\ast}{(K)}}:=I$. By the arguments for deriving (4.11) in §4.5.2 for the case of $K = K^{\ast}$, we have that ${\|{\Phi_{t,\ell}^{\ast}{(K^{\ast})}}\|}_{2} = {\mathcal{O}{}}$ for all $t \geq \ell$. Applying Lemma 9. ‣ Proof. ‣ 4.5.3 Proof of Claim 4 ‣ 4.5 Certainty equivalent linear quadratic control ‣ 4 Theoretical guarantees and proofs ‣ Cost-Driven Representation Learning for Linear Quadratic Gaussian Control: Part I") to the last $T - \ell$ steps, we have ${\|{{\hat{K}}_{t} - K_{t}^{\ast}}\|}_{2} = {\mathcal{O}{(\varepsilon_{2})}}$ for $t \geq \ell$. Hence, using $\varepsilon_{2} = {\mathcal{O}{(T^{- 1})}}$ and the expression that

we can show by induction that ${\|{\Phi_{t,\ell}^{\ast}{(\hat{K})}}\|}_{2} = {\mathcal{O}{}}$. By the performance difference lemma (Lemma 8. ‣ 4.5.3 Proof of Claim 4 ‣ 4.5 Certainty equivalent linear quadratic control ‣ 4 Theoretical guarantees and proofs ‣ Cost-Driven Representation Learning for Linear Quadratic Gaussian Control: Part I")), for any $x \in {\mathbb{R}}^{d_{x}}$,

where the term $E_{t}^{K} = 0$ in Lemma 8. ‣ 4.5.3 Proof of Claim 4 ‣ 4.5 Certainty equivalent linear quadratic control ‣ 4 Theoretical guarantees and proofs ‣ Cost-Driven Representation Learning for Linear Quadratic Gaussian Control: Part I") for $K = K^{\ast}$. Hence,

where we note that ${(R_{t}^{\ast},B_{t}^{\ast},P_{t + 1}^{\ast})}_{t \geq \ell}$ have $\mathcal{O}{}$ operator norms. On the other hand, ${\|{P_{\ell}^{\ast} - {\hat{P}}_{\ell}}\|}_{2} = {\mathcal{O}{(\varepsilon_{2})}}$, following which we have

Since $\varepsilon_{2} = {\mathcal{O}{(T^{- 1})}}$, combining the above two bounds yields

Note that we can also bound $(b)$ using the simulation lemma, which yields a worse bound.

Next, since ${J_{2}{(\hat{K})}} \geq {J_{2}{(K^{\ast})}}$ due to the optimality of $K^{\ast}$, we have

By Lemma 8. ‣ 4.5.3 Proof of Claim 4 ‣ 4.5 Certainty equivalent linear quadratic control ‣ 4 Theoretical guarantees and proofs ‣ Cost-Driven Representation Learning for Linear Quadratic Gaussian Control: Part I"),

where in $(i)$ the term $E_{t}^{K} = 0$ in Lemma 8. ‣ 4.5.3 Proof of Claim 4 ‣ 4.5 Certainty equivalent linear quadratic control ‣ 4 Theoretical guarantees and proofs ‣ Cost-Driven Representation Learning for Linear Quadratic Gaussian Control: Part I") for $K = K^{\ast}$, $({ii})$ follows from that for $t \geq \ell$, ${\|{\hat{K}}_{t}\|}_{2} = {\mathcal{O}{({\| K_{t}^{\ast}\|}_{2})}}$ due to ${\|{{\hat{K}}_{t} - K_{t}^{\ast}}\|}_{2} = {\mathcal{O}{(\varepsilon_{2})}}$ and that ${\| K_{t}^{\ast}\|}_{2} = {\mathcal{O}{}}$ as argued in the proof of Lemma 7. ‣ 4.5 Certainty equivalent linear quadratic control ‣ 4 Theoretical guarantees and proofs ‣ Cost-Driven Representation Learning for Linear Quadratic Gaussian Control: Part I"), and in $({iii})$ we use ${\|{{Cov}{(x_{t}^{\delta})}}\|}_{2} = {\mathcal{O}{(a_{2}^{\ell})}}$ for $t \leq \ell$, ${\|{{Cov}{(\delta_{t})}}\|}_{2} \leq {\varphi_{2}^{2}{\max_{\tau \leq t}{\|{{Cov}{(x_{\tau}^{\delta})}}\|}_{2}}}$ for $t \geq \ell$, and that due to Lemma 15 and $\varphi_{2} = {\mathcal{O}{(T^{- 1})}}$, for $t \geq \ell$,

For $(d)$, by (4.15), we have ${\|{P_{t}^{\hat{K}} - P_{t}^{\ast}}\|}_{2} = {\mathcal{O}{({\varepsilon_{2}^{2}{({T - \ell})}})}}$ for $t \geq \ell$. Hence,

Finally, combining the above bounds on ${(a)},{(b)},{(c)},{(d)}$, we have

which completes the proof. ∎

### Proof of Theorem 1

Now we are ready to prove Theorem 1. Algorithm 1 has three main steps: state representation function learning (Algorithm 2), latent model identification (Algorithm 3), and planning by RDE (2.6). Correspondingly, the analysis below is organized around these three steps.

Recovery of the state representation function. By Proposition 3, with $u_{t} = {\mathcal{N}{(0,{\sigma_{u}^{2}I})}}$ for all $0 \leq t \leq {T - 1}$ to system (2.1), the $k$-step cumulative cost starting from step $t$, where $k = 1$ for $0 \leq t \leq {\ell - 1}$ and $k = {m \land {({{T - t} + 1})}}$ for $\ell \leq t \leq T$, is given under the normalized parameterization by

where ${\overline{b}}_{t} = {\mathcal{O}{(k)}}$, and ${\overline{e}}_{t}$ is a zero-mean subexponential random variable with ${\|{\overline{e}}_{t}\|}_{\psi_{1}} = {\mathcal{O}{({kd_{x}^{1/2}})}}$.

Then, it is clear that Algorithm 2 recovers latent states $z_{t}^{\ast \prime} = {M_{t}^{\ast \prime}h_{t}}$, where $0 \leq t \leq T$, by a combination of quadratic regression and low-rank approximate factorization. Below we drop the superscript prime for notational simplicity, but keep in mind that the optimal state representation function ${(M_{t}^{\ast})}_{t = 0}^{T}$, the corresponding latent states ${(z_{t}^{\ast})}_{t = 0}^{T}$, and the true latent system parameters $({(A_{t}^{\ast},B_{t}^{\ast})}_{t = 0}^{T - 1},{(Q_{t}^{\ast})}_{t = 0}^{T})$ are all with respect to the normalized parameterization.

For all $0 \leq t \leq T$, let $N_{t}^{\ast}:={{(M_{t}^{\ast})}^{\top}M_{t}^{\ast}}$. By Assumption 4, ${\| N_{t}^{\ast}\|}_{2} = {\mathcal{O}{}}$. Since $h_{t} = {\lbrack y_{0:t};u_{0:{({t - 1})}}\rbrack}$ and ${({{Cov}{(y_{t})}})}_{t = 0}^{T},{({{Cov}{(u_{t})}})}_{t = 0}^{T - 1}$ have $\mathcal{O}{}$ operator norms due to Assumptions 1. ‣ 2 Problem setup ‣ Cost-Driven Representation Learning for Linear Quadratic Gaussian Control: Part I") and 4, by Lemma 12, ${{Cov}{(h_{t})}} = {{\mathbb{E}}{\lbrack{h_{t}h_{t}^{\top}}\rbrack}} = {\mathcal{O}{(t)}}$. Hence, for quadratic regression, Lemma 2. ‣ Proof. ‣ 4.2 Quadratic regression bound ‣ 4 Theoretical guarantees and proofs ‣ Cost-Driven Representation Learning for Linear Quadratic Gaussian Control: Part I") (detailed later) and the union bound over time steps guarantee that as long as $n \geq {aT^{4}{({d_{y} + d_{u}})}^{4}{\log{({{aT^{3}{({d_{y} + d_{u}})}^{2}}/p})}}{\log{({T/p})}}}$ for an absolute constant $a > 0$, with probability at least $1 - p$, for all $0 \leq t \leq {\ell - 1}$,

and for all $\ell \leq t \leq T$,

Now let us bound the distance between ${\hat{M}}_{t}$ and $M_{t}^{\ast}$. Recall that we use $d_{h} = {{{({t + 1})}d_{y}} + {td_{u}}}$ as a shorthand. The estimate ${\hat{N}}_{t}$ may not be positive semidefinite. Let ${\hat{N}}_{t} = {U\LambdaU^{\top}}$ be its eigenvalue decomposition, with the $d_{h} \times d_{h}$ matrix $\Lambda$ having descending diagonal elements. Let $\Sigma:={\max{(\Lambda,0)}}$. Then ${\overset{\sim}{N}}_{t} =:U\Sigma U^{\top}$ is the projection of ${\hat{N}}_{t}$ onto the positive semidefinite cone with respect to the Frobenius norm. Since $N_{t}^{\ast} \succcurlyeq 0$,

The low-rank factorization is essentially a combination of low-rank approximation and matrix factorization. For $d_{h} < d_{x}$, ${\overset{\sim}{M}}_{t} =:{\lbrack\Sigma^{1/2}U^{\top};0_{{({d_{x} - d_{h}})} \times d_{h}}\rbrack}$ constructed by padding zeros satisfies ${{\overset{\sim}{M}}_{t}^{\top}{\overset{\sim}{M}}_{t}} = {\overset{\sim}{N}}_{t}$. For $d_{h} \geq d_{x}$, construct ${\overset{\sim}{M}}_{t} =:\Sigma_{d_{x}}^{1/2}U_{d_{x}}^{\top}$, where $\Sigma_{d_{x}}$ is the top-left $d_{x} \times d_{x}$ block in $\Sigma$ and $U_{d_{x}}$ consists of $d_{x}$ columns of $U$ from the left. By the Eckart-Young-Mirsky theorem, ${{\overset{\sim}{M}}_{t}^{\top}{\overset{\sim}{M}}_{t}} = {U_{d_{x}}\Sigma_{d_{x}}U_{d_{x}}^{\top}}$ satisfies

From now on, we consider $0 \leq t \leq {\ell - 1}$ and $\ell \leq t \leq T$ separately, since, as we will show, in the latter case we have the additional condition that ${{rank}{(M_{t}^{\ast})}} = d_{x}$.

For $0 \leq t \leq {\ell - 1}$, $k = 1$. By Lemma 4 (detailed later), there exists a $d_{x} \times d_{x}$ orthogonal matrix $S_{t}$, such that ${\|{{\overset{\sim}{M}}_{t} - {S_{t}M_{t}^{\ast}}}\|}_{2} \leq {\|{{\overset{\sim}{M}}_{t} - {S_{t}M_{t}^{\ast}}}\|}_{F} = {\mathcal{O}{({{({t \vee 1})}^{3/2}{({d_{y} + d_{u}})}d_{x}^{3/4}n^{- {1/4}}{\log^{1/4}{({\ell/p})}}})}}$. Recall that ${\hat{M}}_{t} = {\text{TruncSV}{({\overset{\sim}{M}}_{t},\theta)}} = {\left( {{{\mathbb{I}}_{\lbrack\theta,{+ \infty})}{(\Sigma_{d_{x}}^{1/2})}} \odot \Sigma_{d_{x}}^{1/2}} \right)U_{d_{x}}^{\top}}$. Then,

Hence, the distance between ${\hat{M}}_{t}$ and $M_{t}^{\ast}$ satisfies

by the choice of $\theta = {\Theta{({\ell^{3/2}{({d_{y} + d_{u}})}d_{x}^{3/4}n^{- {1/4}}{\log^{1/4}{({\ell/p})}}})}}$. As a result, since ${\hat{z}}_{t} = {{\hat{M}}_{t}h_{t}}$ and $z_{t}^{\ast} = {M_{t}^{\ast}h_{t}}$,

By, with probability at least $1 - p$, as long as $n \geq {{{({t \vee 1})}{({d_{y} + d_{u}})}} + {\log{({1/p})}}}$,

Hence, define $\epsilon_{z}:={\ell^{2}{({d_{y} + d_{u}})}d_{x}^{3/4}n^{- {1/4}}{\log^{1/4}{({1/p})}}}$. Then, with probability at least $1 - p$,

On the other hand, threshold $\theta$ ensures a lower bound on $\sigma_{\min}^{+}{({\sum_{i = 1}^{n}{{\hat{z}}_{t}^{(i)}{({\hat{z}}_{t}^{(i)})}^{\top}}})}$. As shown in the proof of Lemma 5. ‣ 4.4 Perturbed linear regression bound ‣ 4 Theoretical guarantees and proofs ‣ Cost-Driven Representation Learning for Linear Quadratic Gaussian Control: Part I"), this property is important for ensuring the system identification outputs ${\hat{A}}_{t}$ and ${\hat{B}}_{t}$ have bounded norms. Specifically,

where $(i)$ is due to and that the minimum positive singular values of $\sum_{i = 1}^{n}{{\hat{M}}_{t}h_{t}^{(i)}{(h_{t}^{(i)})}^{\top}{\hat{M}}_{t}^{\top}}$ and ${\hat{M}}_{t}$ are both their $k$th singular value, where $k$ is the rank of ${\hat{M}}_{t}$, by considering the singular value decomposition of ${\hat{M}}_{t}$. By standard concentration in analyzing linear regression, with probability at least $1 - p$, as long as $n \geq {a{\log{({1/p})}}}$ for some absolute constant $a > 0$, ${\sigma_{\min}\left( {\sum_{i = 1}^{n}{h_{t}^{(i)}{(h_{t}^{(i)})}^{\top}}} \right)} = {\Omega{(n)}}$. Hence,

For $\ell \leq t \leq T$, $k \leq m$. By Proposition 2, ${Cov}{(z_{t}^{\ast})}$ has full rank, ${\sigma_{\min}{({{Cov}{(z_{t}^{\ast})}})}} = {\Omega{(\nu^{2})}}$ and ${\sigma_{\min}{(M_{t}^{\ast})}} = {\Omega{({\nut^{- {1/2}}})}}$. Recall that for $\ell \leq t \leq T$, we simply set ${\hat{M}}_{t} = {\overset{\sim}{M}}_{t}$. Then, by Lemma 3). ‣ 4.3 Matrix factorization bound ‣ 4 Theoretical guarantees and proofs ‣ Cost-Driven Representation Learning for Linear Quadratic Gaussian Control: Part I"), there exists a $d_{x} \times d_{x}$ orthogonal matrix $S_{t}$, such that

which is also an upper bound on ${\|{{\hat{M}}_{t} - {S_{t}M_{t}^{\ast}}}\|}_{2}$. As a result,

where $(i)$ holds with probability $1 - p$. Hence, there exists an absolute constant $c > 0$, such that if $n \geq {c\nu^{- 6}m^{2}T^{6}{({d_{y} + d_{u}})}^{5}d_{x}^{2}{\log^{2}{({n/p})}}}$,

This is needed for the analysis of estimating ${\hat{A}}_{t},{\hat{B}}_{t}$ in the next step. For the analysis of estimating $Q_{t}^{\ast}$ by quadratic regression in Lemma 2. ‣ Proof. ‣ 4.2 Quadratic regression bound ‣ 4 Theoretical guarantees and proofs ‣ Cost-Driven Representation Learning for Linear Quadratic Gaussian Control: Part I"), we need the sub-Gaussianity of ${\|{{\hat{z}}_{t} - {S_{t}z_{t}^{\ast}}}\|}_{2}$. Notice that

Since the $\ell_{2}$-norm of $h_{t} = {\lbrack y_{0:t};u_{0:{({t - 1})}}\rbrack}$ is sub-Gaussian with its mean and sub-Gaussian norm bounded by $\mathcal{O}{({({t{({d_{y} + d_{u}})}})}^{1/2})}$, we have that ${\|{{\hat{z}}_{t} - {S_{t}z_{t}^{\ast}}}\|}_{2}$ is sub-Gaussian with its mean and sub-Gaussian norm bounded by

Identification of the latent model. The latent dynamics ${(A_{t}^{\ast},B_{t}^{\ast})}_{t = 0}^{T - 1}$ is identified in Algorithm 3, using ${({\hat{z}}_{t}^{(i)})}_{{i = 1},{t = 0}}^{N,T}$ produced by Algorithm 2, by ordinary least squares. Recall from Proposition 1 that $z_{t + 1}^{\ast} = {{A_{t}^{\ast}z_{t}^{\ast}} + {B_{t}^{\ast}u_{t}} + {L_{t + 1}i_{t + 1}}}$. With the transforms on $z_{t}^{\ast}$ and $z_{t + 1}^{\ast}$, we have

and ${{(z_{t}^{\ast})}^{\top}Q_{t}^{\ast}z_{t}^{\ast}} = {{({S_{t}z_{t}^{\ast}})}^{\top}S_{t}Q_{t}^{\ast}S_{t}^{\top}S_{t}z_{t}^{\ast}}$. Under control $u_{t} \sim {\mathcal{N}{(0,{\sigma_{u}^{2}I_{d_{u}}})}}$ for $0 \leq t \leq {T - 1}$, we know that $z_{t}^{\ast}$ is a zero-mean Gaussian random vector; so is $S_{t}z_{t}^{\ast}$. Let $\Sigma_{t}^{\ast} = {{\mathbb{E}}{\lbrack{S_{t}z_{t}^{\ast}{(z_{t}^{\ast})}^{\top}S_{t}^{\top}}\rbrack}}$ be its covariance. By Assumptions 1. ‣ 2 Problem setup ‣ Cost-Driven Representation Learning for Linear Quadratic Gaussian Control: Part I") and 4, ${(\Sigma_{t}^{\ast})}_{t = 0}^{T}$ and ${({L_{t + 1}i_{t + 1}})}_{t = 0}^{T - 1}$ have $\mathcal{O}{}$ operator norms.

For $0 \leq t \leq {\ell - 1}$, we need a bound for the estimation error of rank-deficient and perturbed linear regression. By Lemma 5. ‣ 4.4 Perturbed linear regression bound ‣ 4 Theoretical guarantees and proofs ‣ Cost-Driven Representation Learning for Linear Quadratic Gaussian Control: Part I"), there exists an absolute constant $c > 0$, such that as long as $n \geq {c{({d_{x} + d_{u} + {\log{({1/p})}}})}}$, with probability at least $1 - p$,

By substituting the expressions for $\epsilon_{z}$ and $\theta$, we have

which is also a bound on ${\|{{\hat{B}}_{t} - {S_{t + 1}B_{t}^{\ast}}}\|}_{2}$. Meanwhile, by Claim 1, ${\|{\hat{A}}_{t}\|}_{2} = {\mathcal{O}{(\ell)}}$.

For $\ell \leq t \leq {T - 1}$, by Lemma 6. ‣ 4.4.1 Proof of Claim 1 ‣ 4.4 Perturbed linear regression bound ‣ 4 Theoretical guarantees and proofs ‣ Cost-Driven Representation Learning for Linear Quadratic Gaussian Control: Part I") and the union bound over time steps, with probability at least $1 - p$,

By substituting the expression for ${\|{{\hat{M}}_{t} - {S_{t}M_{t}^{\ast}}}\|}_{2}$ in (4.17), we have

which is also a bound on ${\|{{\hat{B}}_{t} - {S_{t + 1}B_{t}^{\ast}}}\|}_{2}$.

By Assumption 3. ‣ 2 Problem setup ‣ Cost-Driven Representation Learning for Linear Quadratic Gaussian Control: Part I"), ${(Q_{t}^{\ast})}_{t = 0}^{\ell - 1}$ and $Q_{T}^{\ast}$ are positive definite; they are identity matrices under the normalized parameterization. For ${(Q_{t}^{\ast})}_{t = \ell}^{T - 1}$, which may not be positive definite, we identify them in Algorithm 3 by (3.5). By Lemma 2. ‣ Proof. ‣ 4.2 Quadratic regression bound ‣ 4 Theoretical guarantees and proofs ‣ Cost-Driven Representation Learning for Linear Quadratic Gaussian Control: Part I"),

where we have used $\nu = {\Omega{}}$. By construction, ${\hat{Q}}_{t}$ is the projection of ${\overset{\sim}{Q}}_{t}$ onto the positive semidefinite cone with respect to the Frobenius norm. Since ${S_{t}Q_{t}^{\ast}S_{t}^{\top}} \succcurlyeq 0$, we have

Certainty equivalent linear quadratic control. The last step of Algorithm 1 is to compute the optimal controller in the estimated system $({({\hat{A}}_{t},{\hat{B}}_{t},R_{t}^{\ast})}_{t = 0}^{T - 1},{({\hat{Q}}_{t})}_{t = 0}^{T})$ by RDE (2.6).

Since $z_{t}^{\ast} = {{\mathbb{E}}{\lbrack\left. x_{t} \middle| h_{t} \right.\rbrack}}$, the residual $z_{t}^{\ast} - x_{t}$ is independent of $h_{t}$ and $z_{t}^{\ast}$. Hence, we have

where ${\mathbb{E}}{\lbrack{{({x_{t} - z_{t}^{\ast}})}{({x_{t} - z_{t}^{\ast}})}^{\top}}\rbrack}$ is a constant matrix regardless of actions ${(u_{\tau})}_{\tau \leq t}$. Hence,

is a constant, and it suffices to consider the latent state space for studying the policy suboptimality gap.

In the latent state space, action $u_{t} = {{\hat{K}}_{t}{\hat{M}}_{t}h_{t}} = {{\hat{K}}_{t}{({{S_{t}z_{t}^{\ast}} + \delta_{t}})}}$, where $\delta_{t}:={{({{\hat{M}}_{t} - {S_{t}M_{t}^{\ast}}})}h_{t}}$ is a Gaussian noise vector correlated with $z_{t}^{\ast}$. Since $h_{0} = y_{0} = {{C_{0}^{\ast}z_{0}^{\ast}} + {C_{0}^{\ast}{({x_{0} - z_{0}^{\ast}})}} + v_{0}}$, we have ${\|{{Cov}{(y_{0})}}\|}_{2} = {\mathcal{O}{({\|{{Cov}{(z_{0}^{\ast})}}\|}_{2})}}$ and ${\|{{Cov}{(\delta_{0})}}\|}_{2} = {\mathcal{O}{({{\|{{\hat{M}}_{0} - {S_{0}M_{0}^{\ast}}}\|}_{2}^{2}{\|{{Cov}{(z_{0}^{\ast})}}\|}_{2}})}}$. Define $\iota_{0}:={\|{{\hat{M}}_{0} - {S_{0}M_{0}^{\ast}}}\|}_{2}$ and $\iota_{t}:={t^{1/2}{({1 + {\max_{\tau \leq {t - 1}}{\|{\hat{K}}_{\tau}\|}_{2}}})}{\|{{\hat{M}}_{t} - {S_{t}M_{t}^{\ast}}}\|}_{2}}$ for $1 \leq t \leq {T - 1}$. Below we use induction to show that as long as ${({\|{{\hat{M}}_{t} - {S_{t}M_{t}^{\ast}}}\|}_{2})}_{0 \leq t \leq {T - 1}}$ are small enough, ${\|{{Cov}{(\delta_{t})}}\|}_{2} \leq {\iota_{t}^{2}{\max_{\tau \leq t}{\|{{Cov}{(z_{\tau}^{\ast})}}\|}_{2}}}$ for all $0 \leq t \leq {T - 1}$.

Suppose that ${\|{{Cov}{(\delta_{t})}}\|}_{2} \leq {\iota_{t}^{2}{\max_{\tau \leq t}{\|{{Cov}{(z_{\tau}^{\ast})}}\|}_{2}}}$ for all $t \leq t_{1}$. For any $t \geq 1$, by the definition of the innovation term $i_{t}$ and the dynamics of $z_{t}^{\ast}$ in Proposition 1, we have

Hence, for any $t \geq 0$, ${\|{{Cov}{(y_{t})}}\|}_{2} = {\mathcal{O}{({\|{{Cov}{(z_{t}^{\ast})}}\|}_{2})}}$ as ${\|{{Cov}{(i_{t})}}\|}_{2} = {\mathcal{O}{}}$. For any $t \geq 0$, we also have

By Lemma 12, we further have

By the induction hypothesis on ${\|{{Cov}{(\delta_{t})}}\|}_{2}$, we have

Hence, as long as ${\|{{\hat{M}}_{t} - {S_{t}M_{t}^{\ast}}}\|}_{2} = {\mathcal{O}{({t^{- {1/2}}{({1 + {\max_{\tau \leq {t - 1}}{\|{\hat{K}}_{\tau}\|}_{2}}})}^{- 1}})}}$ for all $t \leq t_{1}$ such that ${\max_{t \leq t_{1}}\iota_{t}^{2}} = {\mathcal{O}{}}$, we complete the induction by

where we use the definition of $\iota_{t_{1} + 1}$.

Now let us bound the operator norms of ${(K_{t})}_{t = 0}^{T - 1}$. For $0 \leq t \leq {\ell - 1}$, from the backward recursion in (2.6) and (2.4), there exists a dimension-free constant $\kappa > 1$ that depends polynomially on $\ell$ and other problem parameters, such that ${\|{\hat{K}}_{t}\|}_{2} = {\mathcal{O}{(\kappa^{\ell - t})}}$. For $\ell \leq t \leq {T - 1}$, let $\varepsilon_{2}$ be the maximum of ${\|{{\hat{A}}_{t} - {S_{t + 1}A_{t}^{\ast}S_{t}^{\top}}}\|}_{2},{\|{{\hat{B}}_{t} - {S_{t + 1}B_{t}^{\ast}}}\|}_{2},{\|{{\hat{Q}}_{t} - {S_{t}Q_{t}^{\ast}S_{t}^{\top}}}\|}_{2}$ for all $t \geq \ell$. Then,

Applying Lemma 9. ‣ Proof. ‣ 4.5.3 Proof of Claim 4 ‣ 4.5 Certainty equivalent linear quadratic control ‣ 4 Theoretical guarantees and proofs ‣ Cost-Driven Representation Learning for Linear Quadratic Gaussian Control: Part I") to the last $T - \ell$ steps, we have ${\|{{\hat{K}}_{t} - {K_{t}^{\ast}S_{t}^{\top}}}\|}_{2} = {\mathcal{O}{(\varepsilon_{2})}}$. Hence, we have ${\|{\hat{K}}_{t}\|}_{2} = {\mathcal{O}{({\| K_{t}^{\ast}\|}_{2})}} = {\mathcal{O}{}}$.

We have shown in (4.16) that for $0 \leq t \leq {\ell - 1}$,

and in (4.17) that for $t \geq \ell$,

Let $n$ be large enough such that ${\|{{\hat{M}}_{t} - {S_{t}M_{t}^{\ast}}}\|}_{2} = {\mathcal{O}{({t^{- {1/2}}{({1 + {\max_{\tau \leq {t - 1}}{\|{\hat{K}}_{t}\|}_{2}}})}^{- 1}})}}$ is satisfied for all $t \geq 1$, and the conditions in Lemma 10 are satisfied, with $\varepsilon_{2}$ satisfying (4.18) and $\varepsilon_{1}$, $\varphi_{1}$, $\varphi_{2}$ satisfying

Hence, by Lemma 10, there exists dimension-free constant $a_{4} > 1$ depending polynomially on $\ell$ and other problem parameters, such that with probability at least $1 - p$,

where $J{(\hat{\pi})}$, $J{(\pi^{\ast})}$ correspond to $J^{\delta}{(\hat{K})}$, $J{(K^{\ast})}$ in Lemma 10, respectively, in the latent state space.

## Concluding remarks

We examined the cost-driven state representation learning methods in time-varying LQG control. With a finite-sample analysis, we showed that a direct, cost-driven state representation learning algorithm effectively solves LQG. In the analysis, we revealed the importance of using multi-step cumulative costs as the supervision signal, and the dependence on $\ell$, the controllability index, due to early-stage insufficient excitement of the system. For the same reason, our policy suboptimality gap has a significantly worsened dependence on $\ell$, as the latent model can only be partially identified, and the learned latent model may not be stable. Hence, an immediate question is how we can learn a stable latent model to improve the dependence on $\ell$. A major limitation of our method is the use of history-based state representation functions; recovering the recursive Kalman filter would be ideal.

In Part II of this work, we will explore how the cost-driven state representation learning approach performs in the infinite-horizon LTI setting, as well as discuss more opportunities that this work has opened up for future research.
