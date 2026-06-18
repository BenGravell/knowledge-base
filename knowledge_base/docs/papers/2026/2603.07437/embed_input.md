<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Cost-Driven Representation Learning for Linear Quadratic Gaussian Control: Part II

Topics include Reinforcement learning, Optimal control, Representation learning, Regression, Control, Learning, Linear quadratic Gaussian, State space, Linear quadratic Gaussian control.

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

We study the problem of state representation learning for control from partial and potentially high-dimensional observations. We approach this problem via cost-driven state representation learning, in which we learn a dynamical model in a latent state space by predicting cumulative costs. In particular, we establish finite-sample guarantees on finding a near-optimal representation function and a near-optimal controller using the learned latent model for infinite-horizon time-invariant Linear Quadratic Gaussian (LQG) control. We study two approaches to cost-driven representation learning, which differ in whether the transition function of the latent state is learned explicitly or implicitly. The first approach has also been investigated in Part I of this work, for finite-horizon time-varying LQG control. The second approach closely resembles MuZero, a recent breakthrough in empirical reinforcement learning, in that it learns latent dynamics implicitly by predicting cumulative costs. A key technical contribution of this Part II is to prove persistency of excitation for a new stochastic process that arises from the analysis of quadratic regression in our approach, and may be of independent interest.

<!-- chunk {"id": "body-0003", "role": "body", "section": "Introduction", "weight": 1.5} -->

Control with a *learned* latent model has achieved state-of-the-art performance in several reinforcement learning (RL) benchmarks, including board games, Atari games, and visuomotor control. To better understand this machinery in RL, we introduce it to a classical optimal control problem, namely the linear quadratic Gaussian (LQG) control, and study its theoretical, in particular, finite-sample performance. Essential to this approach is the learning of two components: a *state representation* function that maps an observed history to some latent state, and a *latent model* that predicts the transition and cost in the latent state space. The latent model is usually a Markov decision process, using which we obtain a policy in the latent space or execute online planning.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

What is the correct objective to optimize for learning a good latent model? One popular choice is to learn a function that *reconstructs the observation* from the latent state. A latent model learned this way is *agnostic to control tasks* and retains all the information about the environment. This class of approaches may achieve satisfactory performance empirically, but are prone to background distraction and control-irrelevant information. The second class of methods learn an *inverse model* that infers actions from latent states at different time steps. A latent model learned with this methodology is also task-agnostic but can extract *control-relevant* information. In contrast, the third class of methods learn *task-relevant* representations by *predicting costs* in the control task. The concept that a good latent state should be able to predict costs is intuitive, as the costs are directly relevant to optimal control. This class of methods is the focus of this work, which aims to examine the soundness of this methodology in classical partially observable control problems, e.g., the LQG control.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

In Part I of this work, we have studied provable cost-driven state representation learning in LQG for the *finite-horizon, time-varying* setting. In this Part II, we build upon it and complement it by studying the same question for the *infinite-horizon, time-invariant* setting. In this setting, both the representation function and the latent model are *stationary*, which is usually the case in empirical RL practice. This allows us to formulate a new approach that draws an even closer connection to the state representation learning in MuZero, an RL algorithm that matches the superhuman performance of AlphaZero in Go, shogi and chess, while outperforming model-free RL algorithms in Atari games.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

We show that two cost-driven state representation learning methods provably solve infinite-horizon time-invariant LQG control, with finite-sample guarantees. Both methods only need a single trajectory; one resembles the method in Part I of this work, and the other resembles the state representation learning in MuZero.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

By analyzing the MuZero-style algorithm, we notice the potential issue of *coordinate misalignment*: Costs can be invariant to orthogonal transformations of the latent states, and implicit dynamics learning by predicting one-step transition may not recover the latent state coordinates consistently. This insight suggests the need to predict multi-step latent transition or other coordinate alignment procedures in the MuZero-style, implicit dynamics learning approaches.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Introduction", "weight": 1.5} -->

Technically, we overcome the difficulty of having *correlated* data in a single trajectory for latent model learning, as we are dealing with the time-invariant setting and need to aggregate samples across time steps in contrast to the Part I of this work. To achieve so, on one hand, we prove a new result about the persistency of excitation for a stochastic process that arises from the analysis of the quadratic regression subroutine in both of our methods; on the other hand, to prove concentration beyond martingale difference sequences, we build on the idea that widely separated sample points in a mixing process are *almost* independent, and introduce a new analysis method by partitioning the sequence and applying the Gram-Schmidt process.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Problem setup", "weight": 1.0} -->

A partially observable linear time-invariant (LTI) dynamical system is described by

<!-- chunk {"id": "body-0010", "role": "body", "section": "Problem setup", "weight": 1.0} -->

A policy/controller $\pi$ determines an action/control input $u_{t}$ at time step $t$ based on the history $\lbrack y_{0:t};u_{0:{({t - 1})}}\rbrack$ up to this time step. For $t \geq 0$, let $c_{t}:={c{(x_{t},u_{t})}}$ denote the cost at time step $t$. Given a policy $\pi$, let

<!-- chunk {"id": "body-0011", "role": "body", "section": "Problem setup", "weight": 1.0} -->

denote the infinite-horizon time-averaged expected cost. The goal of LQG control is to find a policy $\pi$ that minimizes $J{(\pi)}$.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Problem setup", "weight": 1.0} -->

We make the following standard assumptions.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Assumption 1", "weight": 1.0} -->

$(A^{\ast},B^{\ast})$ is $\nu$-controllable for some $\nu > 0$, that is, the controllability matrix

<!-- chunk {"id": "body-0014", "role": "body", "section": "Assumption 1", "weight": 1.0} -->

$(A^{\ast},C^{\ast})$ is $\omega$-observable for some $\omega > 0$, that is, the observability matrix

<!-- chunk {"id": "body-0015", "role": "body", "section": "Assumption 1", "weight": 1.0} -->

$\Sigma_{v} \succcurlyeq {\sigma_{v}^{2}I}$ for some $\sigma_{v} > 0$; this can always be achieved by inserting Gaussian noises with full-rank covariance matrices to the observations.

<!-- chunk {"id": "body-0016", "role": "body", "section": "Assumption 1", "weight": 1.0} -->

If the system parameters $(A^{\ast},B^{\ast},C^{\ast},Q^{\ast},R^{\ast},\Sigma_{w},\Sigma_{v})$ are known, the optimal policy is obtained by combining the Kalman filter

<!-- chunk {"id": "body-0017", "role": "body", "section": "Assumption 1", "weight": 1.0} -->

with the optimal feedback gain $K^{\ast}$ of the linear quadratic regulator such that $u_{t} = {K^{\ast}z_{t}^{\ast}}$, where $L^{\ast}$ is the Kalman gain, and at the initial time step, we can set, e.g., $z_{0}^{\ast} = {L^{\ast}y_{0}}$. This fact is known as the *separation principle*, and the Kalman gain and optimal feedback gain are given by

<!-- chunk {"id": "body-0018", "role": "body", "section": "Assumption 1", "weight": 1.0} -->

We consider the data-driven control setting, where the LQG model $(A^{\ast},B^{\ast},C^{\ast},Q^{\ast},\Sigma_{w},\Sigma_{v})$ is unknown. For simplicity, we assume $R^{\ast}$ is known, though our approaches can be readily extended to the case where it is unknown, which we discuss in more detail in §3.1.

<!-- chunk {"id": "body-0019", "role": "body", "section": "Latent model of infinite-horizon time-invariant LQG", "weight": 1.0} -->

The stationary Kalman filter (2.4) asymptotically produces the optimal *state estimation* in the sense of minimum mean squared errors. With a finite horizon, however, the optimal state estimator is time-varying, given by

<!-- chunk {"id": "body-0020", "role": "body", "section": "Latent model of infinite-horizon time-invariant LQG", "weight": 1.0} -->

where $L_{t}^{\ast}$ is the time-varying Kalman gain, converging to $L^{\ast}$ as $t\rightarrow\infty$. This convergence is equivalent to that of the error covariance matrix ${\mathbb{E}}{\lbrack{{({x_{t} - z_{t}^{\ast}})}{({x_{t} - z_{t}^{\ast}})}^{\top}}\rbrack}$, which is exponentially fast. Hence, for simplicity, we assume this error covariance matrix is stationary at the initial time step by the choice of $z_{0}^{\ast}$ so that $L_{t}^{\ast} = L^{\ast}$ for $t \geq 1$; this assumption has also been adopted in the literature.

<!-- chunk {"id": "body-0021", "role": "body", "section": "Latent model of infinite-horizon time-invariant LQG", "weight": 1.0} -->

The *innovation* term $i_{t + 1}:={y_{t + 1} - {C^{\ast}{({{A^{\ast}z_{t}^{\ast}} + {B^{\ast}u_{t}}})}}}$ is independent of $z_{0}^{\ast}$ and the history $(u_{0},y_{1},\ldots,u_{t - 1},y_{t})$ and ${(i_{t})}_{t \geq 1}$ are mutually independent. The following proposition, taken, represents the system in terms of the state estimates obtained by the Kalman filter, which we refer to as the *latent model*.

<!-- chunk {"id": "body-0022", "role": "body", "section": "Method", "weight": 1.0} -->

In practice, latent model learning methods collect trajectories by interacting with the system online using some policy; the trajectories are used to improve the learned latent model, which in turn improves the policy. In LQG control, it is known that one can learn a good latent model from a single trajectory, collected using zero-mean Gaussian control inputs, by viewing this procedure as a classical *system identification* problem; see e.g.,. This is also how we assume the data are collected. We note that our results also apply to data from multiple independent trajectories using control inputs from the same zero-mean Gaussian distribution.

<!-- chunk {"id": "body-0023", "role": "body", "section": "Method", "weight": 1.0} -->

1:Input: length T, history length H, noise magnitude σu
2:Collect trajectories of length T + H using ut ∼ 𝒩 (0,σu2 I), for t ≥ 0, to obtain

<!-- chunk {"id": "body-0024", "role": "body", "section": "Method", "weight": 1.0} -->

3:Estimate the state representation function and cost constants by solving

<!-- chunk {"id": "body-0025", "role": "body", "section": "Method", "weight": 1.0} -->

6:Run SysId (3.4) or CoSysId (Algorithm 2) to obtain system dynamics matrices (Â,B̂)
7:Estimate the cost function by solving

<!-- chunk {"id": "body-0026", "role": "body", "section": "Method", "weight": 1.0} -->

8:Truncate negative eigenvalues of $\overset{\sim}{Q}$ to 0 to obtain Q̂ ≽ 0
9:Find feedback gain K̂ from (Â,B̂,Q̂,R*) by solving DARE (2.8) and (2.6)
Algorithm 1 Cost-driven state representation learning

<!-- chunk {"id": "body-0027", "role": "body", "section": "Method", "weight": 1.0} -->

In our cost-driven state representation learning approach, state representations are learned by predicting costs. To learn the transition function in the latent model, two approaches have been explored in the literature. The first approach explicitly minimizes the transition prediction error. Algorithmically, the overall loss is a combination of cost prediction and transition prediction errors.

<!-- chunk {"id": "body-0028", "role": "body", "section": "Method", "weight": 1.0} -->

The second approach, as taken by MuZero, learns the transition dynamics *implicitly*, by minimizing cost prediction errors at future states generated from the transition function. Algorithmically, the overall loss aggregates the cost prediction errors *across multiple time steps*. In both approaches, the coupling of different terms in the loss makes finite-sample analysis difficult. As observed in Part I of this work, the structure of LQG allows us to learn the representation function independently of learning the transition function. This allows us to formulate both approaches under the same cost-driven state representation learning framework (Algorithm 1).

<!-- chunk {"id": "body-0029", "role": "body", "section": "Method", "weight": 1.0} -->

Algorithm 1 consists of three main steps. Lines 3 to 5 correspond to cost-driven representation function learning. Lines 6 to 8 correspond to latent model learning, where the system dynamics can be identified either explicitly, by ordinary least squares (SysId), or implicitly, by future cost prediction (CoSysId, Algorithm 2 ‣ 3 Method ‣ Cost-Driven Representation Learning for Linear Quadratic Gaussian Control: Part II")). Line 9 corresponds to the policy optimization procedure in the latent model; in LQG this amounts to solving DAREs. Below we elaborate on cost-driven representation learning, SysId, and CoSysId in order.

<!-- chunk {"id": "body-0030", "role": "body", "section": "Cost-driven representation function learning", "weight": 1.0} -->

The procedure of cost-driven representation function learning is consistent with Part I of this work. The main idea is to perform quadratic regression (3.2) to the $d_{x}$-step cumulative costs; this step corresponds to the value prediction in MuZero. By the $\mu$-observability of $(A^{\ast},{(Q^{\ast})}^{1/2})$ (Assumption 1.5), the cost observability Gram matrix satisfies

<!-- chunk {"id": "body-0031", "role": "body", "section": "Cost-driven representation function learning", "weight": 1.0} -->

Under zero control and zero noise, starting from $x$, the $d_{x}$-step cumulative cost is precisely ${\| x\|}_{{\overline{Q}}^{\ast}}^{2}$. Hence, with the impact of zero-mean actions and zero-mean noises averaged out, $\hat{N}$ estimates $N^{\ast}:={{(M^{\ast})}^{\top}{\overline{Q}}^{\ast}M^{\ast}}$; up to an orthogonal transformation, $\hat{M}$ recovers $M^{\ast \prime}:={{({\overline{Q}}^{\ast})}^{1/2}M^{\ast}}$, the representation function under an equivalent parameterization, termed as the *normalized parameterization* in Part I of this work, where

<!-- chunk {"id": "body-0032", "role": "body", "section": "Cost-driven representation function learning", "weight": 1.0} -->

Without loss of generality, we assume that system (2.1) is in the normalized parameterization.

<!-- chunk {"id": "body-0033", "role": "body", "section": "Cost-driven representation function learning", "weight": 1.0} -->

Note that with a known $R^{\ast}$, we subtract $\sum_{\tau = t}^{{t + d_{x}} - 1}{\| u_{\tau}\|}_{R^{\ast}}^{2}$ from ${\overline{c}}_{t}$ in (3.2) to reduce its variance for the benefit of regression. However, the subtraction is not necessary if $R^{\ast}$ is unknown, as Proposition 3 still holds without it. In this case, we can learn $R^{\ast}$ subsequently in (3.3).

<!-- chunk {"id": "body-0034", "role": "body", "section": "Cost-driven representation function learning", "weight": 1.0} -->

Due to the following proposition, the algorithm does not need to know the dimension $d_{x}$ of the latent model; it can discover $d_{x}$ from the eigenvalues of $\hat{N}$.

<!-- chunk {"id": "body-0035", "role": "body", "section": "Explicit learning of system dynamics", "weight": 1.0} -->

Explicit learning of the system dynamics simply minimizes the *transition prediction error* in the latent space, or more generally, the statistical distances between the predicted and estimated distributions of the next latent state, like the KL divergence. In linear systems, it suffices to use the ordinary least squares as the SysId procedure, that is, to solve

<!-- chunk {"id": "body-0036", "role": "body", "section": "Explicit learning of system dynamics", "weight": 1.0} -->

In this linear regression, if ${({\hat{z}}_{t})}_{t \geq H}$ are the optimal state estimates ${(z_{t}^{\ast})}_{t \geq H}$ (2.9), then has shown finite-sample guarantees for obtaining $(\hat{A},\hat{B})$. Here, however, ${\hat{z}}_{t}$ contains errors resulting from the representation function $\hat{M}$ and the residual error $\delta_{t}$ in (2.10), but as long as $T$ and $H$ are large enough, SysId still has a finite-sample guarantee, as will be shown in Lemma 5. We refer to the algorithm that instantiates Algorithm 1 with SysId as CoReL-E (Cost-driven state Representation Learning). As the time-varying counterpart in Part I of this work, this algorithm provably solves LQG control without model knowledge, as will be shown in Theorem 1.

<!-- chunk {"id": "body-0037", "role": "body", "section": "Implicit learning of system dynamics (MuZero-style)", "weight": 1.0} -->

An important ingredient of latent model learning in MuZero is to *implicitly* learn the transition function by minimizing the cost prediction error at future latent states generated from the transition function. Let $z_{t} = {Mh_{t}}$ denote the latent state given by the representation function parameter $M$ at step $t$. Let $z_{t,0} = z_{t}$ and $z_{t,i} = {{Az_{t,{i - 1}}} + {Bu_{{t + i} - 1}}}$ for $i \geq 1$ be the future latent state predicted by dynamics $(A,B)$ from $z_{t}$ after $i$ steps of transition. For a trajectory of length $T + H$ like (3.1), the loss that considers $\ell$ steps into the future is given by

<!-- chunk {"id": "body-0038", "role": "body", "section": "Implicit learning of system dynamics (MuZero-style)", "weight": 1.0} -->

This loss involves powers of $A$ up to $A^{\ell}$; with the squared norm, the powers double, making the minimization over $A$ hard to solve and analyze for $\ell \geq 2$. In LQG control, as we shall discuss, it suffices to take $\ell = 1$. The MuZero algorithm also predicts optimal values and optimal actions; in LQG, to handle the case $Q^{\ast} \nsucc 0$, like cost-driven representation learning (see §3.1), we adopt the *cumulative costs* and use the normalized parameterization. Recall that in Algorithm 1 we define ${\overline{c}}_{t}:={\sum_{\tau = t}^{{t + d_{x}} - 1}{({c_{\tau} - {\| u_{\tau}\|}_{R^{\ast}}^{2}})}}$. Then, the optimization problem we aim to solve is given by

<!-- chunk {"id": "body-0039", "role": "body", "section": "Implicit learning of system dynamics (MuZero-style)", "weight": 1.0} -->

To convexify the optimization problem (3.5 ‣ 3 Method ‣ Cost-Driven Representation Learning for Linear Quadratic Gaussian Control: Part II")), we define $N:={M^{\top}M}$ and $N_{1}:={{\lbrack{AM},B\rbrack}^{\top}{\lbrack{AM},B\rbrack}}$. Then, (3.5 ‣ 3 Method ‣ Cost-Driven Representation Learning for Linear Quadratic Gaussian Control: Part II")) becomes

<!-- chunk {"id": "body-0040", "role": "body", "section": "Implicit learning of system dynamics (MuZero-style)", "weight": 1.0} -->

This minimization problem is convex in $N$, $N_{1}$, and $b$, and has a closed-form solution; essentially, it consists of two linear regression problems coupled by $b$. As a relaxation, we can decouple the two regression problems by allowing $b$ to take different values in them, as $b$ is a term accounting for the estimation error, not part of the representation function. This decoupling further simplifies the analysis: the first regression problem is exactly cost-driven representation learning (§3.1), and the second is cost-driven system identification (CoSysId, Algorithm 2 ‣ 3 Method ‣ Cost-Driven Representation Learning for Linear Quadratic Gaussian Control: Part II")). The algorithm that instantiates Algorithm 1 with CoSysId will be referred to as CoReL-I (Cost-driven state Representation and Dynamic Learning). Like CoReL-E, this MuZero-style latent model learning method provably solves LQG, as we will show next.

<!-- chunk {"id": "body-0041", "role": "body", "section": "Implicit learning of system dynamics (MuZero-style)", "weight": 1.0} -->

1:Input: data 𝒟raw from Algorithm 1, representation function parameter M̂
2:Estimate the system dynamics by

<!-- chunk {"id": "body-0042", "role": "body", "section": "Implicit learning of system dynamics (MuZero-style)", "weight": 1.0} -->

CoSysId has similar steps as cost-driven representation learning (§3.1), except that in Line 5 of Algorithm 2 ‣ 3 Method ‣ Cost-Driven Representation Learning for Linear Quadratic Gaussian Control: Part II"), it requires fitting a matrix ${\hat{S}}_{0}$. This is because the cost is invariant to the orthogonal transformations of latent states, and the approximate factorization steps recover $M^{\ast}$ and $M_{1}^{\ast}$ up to orthogonal transformations $S$ and $S_{1}$, but there is no guarantee for the two transformations to be the same. MuZero bypasses this problem by predicting *multiple* steps of costs into the future, but analyzing such an optimization function involves the additional complexity of dealing with higher-order powers of $A$. Here, we instead estimate the $S_{0} = {SS_{1}^{\top}}$ to align such two transformations.

<!-- chunk {"id": "body-0043", "role": "body", "section": "Implicit learning of system dynamics (MuZero-style)", "weight": 1.0} -->

We note that although CoSysId needs the output $\hat{M}$ from cost-driven representation learning, the two quadratic regressions (3.2) and (3.7 ‣ 3 Method ‣ Cost-Driven Representation Learning for Linear Quadratic Gaussian Control: Part II")) are not coupled and can be solved in parallel.

<!-- chunk {"id": "body-0044", "role": "body", "section": "Implicit learning of system dynamics (MuZero-style)", "weight": 1.0} -->

Discussion on CoSysId. In CoSysId (Algorithm 2 ‣ 3 Method ‣ Cost-Driven Representation Learning for Linear Quadratic Gaussian Control: Part II")), the covariates of the quadratic regression in (3.7 ‣ 3 Method ‣ Cost-Driven Representation Learning for Linear Quadratic Gaussian Control: Part II")) are ${({\lbrack h_{t};u_{t}\rbrack})}_{t \geq H}$. One may wonder if we can pursue an alternative approach by fixing $M$ to be $\hat{M}$, and using ${({\lbrack{\hat{z}}_{t};u_{t}\rbrack})}_{t \geq H}$ as covariates, which have a much lower dimension, though the two quadratic regressions cannot be solved in parallel anymore.

<!-- chunk {"id": "body-0045", "role": "body", "section": "Implicit learning of system dynamics (MuZero-style)", "weight": 1.0} -->

Specifically, the new quadratic regression we need to solve is given by

<!-- chunk {"id": "body-0046", "role": "body", "section": "Implicit learning of system dynamics (MuZero-style)", "weight": 1.0} -->

On the other hand, for CoSysId (Algorithm 2 ‣ 3 Method ‣ Cost-Driven Representation Learning for Linear Quadratic Gaussian Control: Part II")), the ground truth of ${\hat{M}}_{1}$ is $M_{1}^{\ast} = {\lbrack{A^{\ast}M^{\ast}},B^{\ast}\rbrack}$, which is guaranteed to have full row rank by the same argument as the proof of Proposition 2, since $M_{1}^{\ast}{\lbrack h_{t};u_{t}\rbrack}$ estimates $z_{t + 1}^{\ast}$, which has full-rank covariance. Hence, recovering $S_{0} = {SS_{1}^{\top}}$ is feasible.

<!-- chunk {"id": "body-0047", "role": "body", "section": "Theoretical guarantees and proofs", "weight": 1.0} -->

The following Theorem 1 shows that both CoReL-E and CoReL-I can provably solve unknown LQG control.

<!-- chunk {"id": "body-0048", "role": "body", "section": "Persistency of excitation", "weight": 1.0} -->

Central to the analysis of CoReL-E and CoReL-I is the finite-sample characterization of the *quadratic regression* problem (3.2). To this end, notice that

<!-- chunk {"id": "body-0049", "role": "body", "section": "Persistency of excitation", "weight": 1.0} -->

which means that this quadratic regression is essentially a linear regression problem in terms of $\lbrack{{svec}{(N)}};b_{0}\rbrack$. A major difficulty in the analysis is to establish persistency of excitation for ${({\lbrack{{svec}{({h_{t}h_{t}^{\top}})}};1\rbrack})}_{t \geq H}$, meaning that the minimum eigenvalue of the Gram matrix

<!-- chunk {"id": "body-0050", "role": "body", "section": "Persistency of excitation", "weight": 1.0} -->

grows linearly in the data size $T$. This is needed to ensure the uniqueness and convergence of the parameter estimation.

<!-- chunk {"id": "body-0051", "role": "body", "section": "Persistency of excitation", "weight": 1.0} -->

A linear lower bound on $\lambda_{\min}{({\sum_{t = H}^{{T + H} - 1}{h_{t}h_{t}^{\top}}})}$ is a known result for the identification of partially observable linear dynamical systems, see the recent overview. In our case, however, elements of ${svec}{({h_{t}h_{t}^{\top}})}$ are *products* of Gaussians, making the analysis difficult. If ${(h_{t})}_{t \geq H}$ are independent, which is the case if they are from multiple independent trajectories, the result has been established in and Part I of this work. It can also be proved with the matrix Azuma inequality. Here, by contrast, we need to aggregate *correlated* data to estimate a set of *stationary* parameters. In sum, the difficulty we face results from both products of Gaussians and the data dependence.

<!-- chunk {"id": "body-0052", "role": "body", "section": "Persistency of excitation", "weight": 1.0} -->

In principle, given enough burn-in time, the state $x_{t}$, and hence the observation $y_{t}$ and the truncated history $h_{t}$, converge to the steady-state distributions, and samples with an interval of the order of mixing time are approximately independent; our proof of Propositions 3 has been built upon this idea. Hence, a linear lower bound is expected. However, the bound yielded by such an analysis deteriorates as the system becomes less stable and the mixing time increases. To eschew such dependence, the so-called *small-ball* method is introduced. We take the same route, while establishing different arguments to handle the products of Gaussian random variables.

<!-- chunk {"id": "body-0053", "role": "body", "section": "Persistency of excitation", "weight": 1.0} -->

Let us first recall the block martingale small-ball condition.

<!-- chunk {"id": "body-0054", "role": "body", "section": "Quadratic regression bound", "weight": 1.0} -->

The following quadratic regression bound is at the core of proving Theorem 1. Its proof builds on the new persistency of excitation result (Lemma 1). We retain ${(e_{t})}_{t \geq 1}$ in the bound, as in our problem ${(e_{t})}_{t \geq 1}$ may not correspond to a martingale, and may contain an additional small error term resulting from using $M^{\ast}h_{t}$ to approximate $z_{t}^{\ast}$. For notational convenience, we note that the $h_{t},c_{t},\mathcal{F}_{t}$ in Lemma 4 and its proof slightly abuse the notation, which uses different variables from the rest of the paper. Hence, the indices start with $t = 1$, rather than $t = H$ as in the CoReL-E and CoReL-I algorithms.

<!-- chunk {"id": "body-0055", "role": "body", "section": "Perturbed linear regression bound", "weight": 1.0} -->

Identifying the time-invariant latent dynamics involves linear regression with *correlated data* and *perturbed measurements*. The following Lemma 5 extends the previous linear system identification result in to the case with noises in both input and output variables. In Lemma 5, $\gamma$ and $q$ are treated as dimension-free constants (in contrast to Lemma 4), which is indeed the case in our application of Lemma 5 to ${(z_{t}^{\ast})}_{t \geq H}$ in analyzing SysId (3.4) for CoReL-E and in analyzing the alignment matrix estimation (3.8 ‣ 3 Method ‣ Cost-Driven Representation Learning for Linear Quadratic Gaussian Control: Part II")) in Algorithm 2 ‣ 3 Method ‣ Cost-Driven Representation Learning for Linear Quadratic Gaussian Control: Part II") for CoReL-I in §4.6. Note that the bound in Lemma 5 is worse than that in the time-varying setting in Part I of this work, due to the treatment of correlated data.

<!-- chunk {"id": "body-0056", "role": "body", "section": "Stable linear system under small perturbations", "weight": 1.0} -->

To quantify the impact of the truncation error $\delta_{t}$ on the state covariance and the cost, we introduce the following lemma that bounds the state covariance difference for a stable linear system under small perturbations.

<!-- chunk {"id": "body-0057", "role": "body", "section": "Additional discussion on MuZero", "weight": 1.0} -->

In this section, we discuss MuZero in more detail, given its impressive performance and connection to this work. Announced by DeepMind in 2019, MuZero extends the line of works including AlphaGo, AlphaGo Zero, and AlphaZero by obviating the knowledge of the game rules. MuZero matches the superhuman performance of AlphaZero in Go, shogi and chess, while outperforming model-free RL algorithms in Atari games. MuZero builds upon the powerful planning procedure of Monte Carlo Tree Search, with the major innovation being *learning a latent model*. The latent model replaces the rule-based simulator during planning, and avoids the burdensome planning in pixel space for Atari games.

<!-- chunk {"id": "body-0058", "role": "body", "section": "Additional discussion on MuZero", "weight": 1.0} -->

MuZero is a milestone algorithm in representation learning for control. Intuitively, the algorithm design makes sense, but its complexity has so far inhibited a formal theoretical study. On the other hand, statistical learning theory for linear dynamical systems and control has evolved rapidly in recent years; for partially observable linear dynamical systems, much of the work relies on learning *Markov parameters*, lacking a direct connection to the empirical methods used in practice for possibly nonlinear systems. In this work, we aim to bridge the two areas by studying provable MuZero-style latent model learning in LQG control. In a sense, this work can be seen as a case study of the state representation learning algorithm of MuZero in linear systems.

<!-- chunk {"id": "body-0059", "role": "body", "section": "Additional discussion on MuZero", "weight": 1.0} -->

The state representation learning algorithm of MuZero features three ingredients: 1) stacking frames, i.e., observations, as input to the representation function; 2) predicting costs, "optimal" values, and "optimal" actions from latent states; and 3) implicit learning of latent dynamics by predicting these quantities from latent states at future time steps. These are the defining characteristics of the MuZero-style algorithm that we shall consider. In this work, we also handle partial observability by using a finite-length history, but we use a history of observations and actions, rather than only observations. In MuZero, the "optimal" values and actions are found by the powerful online planning procedure. In this work, we simplify the setup by considering data collected using random actions, which are known to suffice for identifying a partially observable linear dynamical system. In this setup, the values become those associated with this trivial policy and we do not predict actions since they are simply random noises. Note that although our study of the above ingredients is directly motivated by MuZero, previous empirical works have also explored them.

<!-- chunk {"id": "body-0060", "role": "body", "section": "Additional discussion on MuZero", "weight": 1.0} -->

For example, frame stacking has been a widely used technique to handle partial observability; predicting values for learning a latent model has been studied, which also learns the latent state transition implicitly.

<!-- chunk {"id": "body-0061", "role": "body", "section": "Concluding remarks", "weight": 1.0} -->

We studied cost-driven state representation learning for solving unknown infinite-horizon time-invariant LQG control. We established finite-sample guarantees for two methods, which differ in whether the latent state dynamics is learned *explicitly* by minimizing the transition prediction errors, or *implicitly* by using the transition for future cost predictions, with the latter being motivated by that used in MuZero. For MuZero-style latent model learning, our analysis identified a coordinate misalignment problem in the latent state space, suggesting the value of *multi-step* future cost prediction. A limitation of this work is that we only considered state representation based on truncated histories, i.e., frame stacking, as used in MuZero; the *recursive form* of the representation function, as in the Kalman filter, is also used empirically, and might be worth further investigation.

<!-- chunk {"id": "body-0062", "role": "body", "section": "Concluding remarks", "weight": 1.0} -->

Together with Part I of this work, we have established a theoretical framework for analyzing cost-driven state representation learning for control. This opens up many opportunities for future research. For example, one may wonder about the extent to which cost-driven state representation learning provably generalizes to nonlinear observations or systems. Besides, one argument for favoring latent-model-based over model-free methods is their ability to generalize across different tasks; our framework may offer a perspective to formalize this intuition. Moreover, given the ubiquity of visual perception in real-world control systems, it is of practical value to study state representation learning with a time-varying observation function or multiple observation functions, modeling images taken from different angles.
