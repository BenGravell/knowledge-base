<!-- arxiv-full-text:v1 {"arxiv_id": "2211.07411", "source": "ar5iv"} -->

## Introduction

A number of real-world problems can be cast into the framework of agents making optimal decisions under uncertainty and/or adversarial disturbances. In this setting, the agent has an associated dynamical system and at each timestep suffers an *a priori* unknown cost that depends on its state and input. In the case of perfect knowledge of the dynamics and the future costs, this can be turned into an optimal control problem and solved with one of the plethora of available methods. As is often the case, however, the dynamics, disturbances, and/or future costs are either entirely unknown or only partially known. This is the setting, for example, in reinforcement learning and approximate dynamic programming.

As agents make decisions "on-the-go", there is a need to quantify and compare the performance of various algorithms. Considering a closed-loop system with a given, possibly time-varying policy, one can study its asymptotic stability as an asymptotic metric. Another approach is to look into the problem through the lens of online optimization. An important metric in the literature of the latter is the notion of regret. Given a policy $\mu$, its regret $\mathcal{R}_{T}$, is defined as the difference between its accumulated cost over some time horizon $T$ and that of some benchmark policy $\pi$. It is often desirable to have sublinear growth of $\mathcal{R}_{T}$ with respect to $T$, which will achieve average convergence to the benchmark in the limit.

A special case of the optimal control problem, the linear quadratic regulator (LQR) has been extensively studied in this context. The results in show that the certainty equivalence approach can synthesize stable linear state feedback controllers as long as the model estimate errors are small enough. In the same spirit of certainty equivalence, the algorithms proposed in yield sublinear regret bounds by sequentially solving Riccati equations. The LQR problem with adversarial disturbances has been studied in in the presence of a prediction window, in to quantify the regret of robustness in the sense of $\mathcal{H}_{\infty}$ control, and in a regret-optimal setting in for unconstrained and in for constrained cases. The setting with general convex and differentiable cost functions with adversarial disturbances has been studied for linear time-invariant (LTI) and for linear time-varying (LTV) systems; algorithms that achieve sublinear regret bounds have been proposed for both classes of systems.

To study and analyze algorithms in both the control theoretic and online learning contexts, one needs to understand the relationship between regret and stability. While most online learning-inspired works seek sublinear regret in pursuit of suboptimality guarantees, it is unclear whether good performance in this aspect also implies stability. Conversely, it is not known what the absence of such guarantees means even for linear dynamical systems. In a recent work, the authors study the interconnection between bounded regret and closed-loop stability for non-linear systems in the absence of noise. In the current work, we consider linear systems subject to process noise and study the relationship between linear regret and stability. Our goal is to develop sufficient conditions under which regret guarantees of an algorithm imply stability of the closed-loop system and vice versa.

In particular, we consider generic, time-varying costs, LTV systems subject to adversarial disturbances with LTV state feedback policies, and also LTI systems as a special case. We study the connection between the regret of such policies and their closed-loop stability in the sense of bounded input-bounded state (BIBS) stability with respect to disturbances and asymptotic stability in the absence of disturbances. Under suitable assumptions, we show the following: For LTV systems and LTV state feedback policies linear regret implies asymptotic stability of the closed-loop system. Conversely, BIBS stability and absolute summability of the state transition matrices imply linear regret.

For LTI systems and LTI state feedback policies linear regret is attained if and only if the closed-loop system is asymptotically stable.

An essential requirement for the results to hold is the "observability" of the state with respect to costs. We provide a counterexample of a notable case where the asymptotic stability implication of linear regret fails to hold when this assumption is violated. A numerical example to showcase the result for the LTI case is provided.

Notation: For a square matrix $A$ the spectral radius and the spectral norm are denoted by $\rho{(A)}$, and $\| A\|$, respectively. For a vector $w \in {\mathbb{R}}^{n}$, $\| w\|$ denotes its Euclidean norm. ${\mathbb{R}}_{+}$ is the set of positive real numbers and $\mathbb{N}$ that of non-negative integers.

## Problem Setup

### Preliminaries

Consider discrete-time LTV systems of the form evolving over non-negative times $t \in {\mathbb{N}}$, where $A_{t} \in {\mathbb{R}}^{n \times n}$, $B_{t} \in {\mathbb{R}}^{n \times m}$ are real matrices, and ${x_{t},w_{t}} \in {\mathbb{R}}^{n}$, $u_{t} \in {\mathbb{R}}^{m}$ are, respectively, the state, disturbance and input signals at timestep $t$. The disturbances are treated as adversarial and are assumed to be norm bounded, that is, there exists $W \in {\mathbb{R}}_{+}$ such that ${\| w_{t}\|} \leq W$ for all $t$. The objective of the optimal control problem is to minimize the cost function where ${c_{t}{(x_{t},u_{t})}}:{{{\mathbb{R}}^{n} \times {\mathbb{R}}^{m}}\rightarrow{\mathbb{R}}}$ is the stage cost function at $t$ and ${\mathbf{u}}:={\lbrack{u_{0}^{\top}\ldotsu_{T - 1}^{\top}}\rbrack}^{\top}$, ${\mathbf{w}}:={\lbrack{w_{0}^{\top}\ldotsw_{T - 1}^{\top}}\rbrack}^{\top}$.

Benchmark Controller: If the system matrices $(A_{t},B_{t})$, the stage costs ${\{ c_{t}\}}_{t = 0}^{T}$ and the disturbance signal $\mathbf{w}$ are known at time $0$, then the control input signal ${\mathbf{u}}^{\star}$ that minimises can be obtained by solving the following optimization problem Note that ${\mathbf{u}}^{\star}$ is referred to as the optimal input signal in hindsight, obtained with full knowledge of the uncertainty.

Linear Policies: In this work, we consider linear time-varying policies of the form^11^1When the context is clear, we drop the subscript $t$ and/or the argument when referring to the linear policy $\mu_{t}{(x_{t})}$. ${\mu_{t}{(x_{t})}} = {- {K_{t}x_{t}}}$ for some $K_{t} \in {\mathbb{R}}^{m \times n}$ for all $t \in {\mathbb{N}}$, where the matrices $K_{t}$ are independent of the state and input history. This covers the class of offline linear policies discussed . Moreover, we note that the considered policies also cover the case where the time-varying parameters of the stage costs are revealed sequentially, thus generating $K_{t}$ online. For example, consider the LQR problem with time-varying cost matrices $Q_{t}$, $R_{t}$, that depend only on time $t$ and are revealed in the form of predictions, studied . The future cost functions, disturbances, as well as the system matrices may be unknown to the policy.

For a given noise signal realisation $\mathbf{w}$ and cost functions ${\{ c_{t}\}}_{t = 0}^{T}$, we define the regret of a given policy $\mu$ to be where ${\mathbf{u}}^{\mu} \in {\mathbb{R}}^{Tm}$ is the input signal generated by $\mu$.

Whereas the regret provides intuition on the performance of the given policy with respect to the best possible cost, its implication for the stability of the associated closed-loop system is unclear. Though several works, e.g. in the stochastic setting, also provide stability guarantees for the online policies, there is no clear relationship between the order of regret and the notion of stability; the results below attempt to address this shortcoming.

We start by defining linear regret to show the conditions under which it implies stability and vice versa.

### Definition 2.1

A policy $\mu$ is said to have linear regret if for given ${W,X} \in {\mathbb{R}}_{+}$, and class of stage costs ^22^2For example, the one defined later in Assumption 2.7., there exist ${C_{w},C_{0}} \in {\mathbb{R}}_{+}$ such that for all $x_{0} \in {\mathbb{R}}^{n}$ with ${\| x_{0}\|} \leq X$, and for all admissible sequences ${\{ c_{t}\}}_{t = 0}^{T}$ and ${\{ w_{t}\}}_{t = 0}^{T - 1}$ In the rest of this section, we review some notions of stability and provide the assumptions required to show the points a and b.

The LTV system in takes the following closed-loop form for considered policies ${\mu_{t}{(x_{t})}} = {- {K_{t}x_{t}}}$ where $F_{t} = {A_{t} - {B_{t}K_{t}}}$. We refer to as the closed-loop system for the considered policy; for questions of asymptotic or exponential stability, we consider the unforced version of with $w_{t} = 0$ for all $t$.

Let ${\Phi{(t,t_{0})}} \in {\mathbb{R}}^{n \times n}$ denote the state transition matrix of the free system $x_{t + 1} = {F_{t}x_{t}}$ at time $t$, starting at some initial time $t_{0}$. In the following, we provide the definitions of asymptotic, exponential, and BIBS stability, specialized for LTV systems.

### Definition 2.2

(Asymptotic Stability). The LTV system is asymptotically stable if and only if for all $x_{0} \in {\mathbb{R}}^{n}$ and for all $t_{0} \in {\mathbb{N}}$ There exists $b \in {\mathbb{R}}_{+}$, such that ${{\|{\Phi{(t,t_{0})}x_{0}}\|} \leq b}\quad$ for all $t \geq t_{0}$, ${\lim_{t\rightarrow\infty}{\Phi{(t,t_{0})}x_{0}}} = \mathbf{0}$.\

### Definition 2.3

(BIBS stability). The LTV system is BIBS stable if and only if

### Definition 2.4

(Exponential Stability). The LTV system is exponentially stable if and only if there exist $\delta \in {\lbrack 0,1)}$ and $d \in {\mathbb{R}}_{+}$, such that for all $t_{0} \in {\mathbb{N}}$ We make the following assumptions on the dynamics.

### Assumption 2.5

There exists a policy ${{\overline{\mu}}_{t}{(x_{t})}} = {- {{\overline{K}}_{t}x_{t}}}$, such that the closed-loop system with $F_{t} = {\overline{F}}_{t}:={A_{t} - {B_{t}{\overline{K}}_{t}}}$ is exponentially stable.

The state transition matrix for satisfies either of the following, ${\lim\limits_{T\rightarrow\infty}{\|{\Phi{(T,0)}}\|}} \in {{\mathbb{R}} \cup {\{\infty\}}}$\${0{<\operatorname{lim\ inf}\limits_{T\rightarrow\infty}\parallel}\Phi{(T,0)}{\|{{<\operatorname{lim\ sup}\limits_{T\rightarrow\infty}\parallel}\Phi{(T,0)}}\|}} < \infty$.

The considered linear state feedback policies are such that the system matrix $F_{t}$ is full rank for all $t \in {\mathbb{N}}$.

We note that Assumption 2.5.i. is required for performance guarantees of the benchmark policy and corresponds to the stabilizability in the LTI case. Assumption 2.5.ii. excludes chaotic LTV systems in the sense of Li-Yorke and is always satisfied for LTI systems. It can be relaxed, but we introduce it here to keep the discussion simple. Assumption 2.5.iii. is standard in the discrete-time case to avoid deadbeat-type responses that imply a lack of uniqueness of the solutions backward in time.

Assumption 2.5.iii. leads to the following lemma.

### Lemma 2.6

Assume that Assumption 2.5.iii. holds, then the LTV system is asymptotically stable if and only if We also introduce the following assumption for the costs.

### Assumption 2.7

(Stage Costs). There exist positive ${\overline{M},\underset{¯}{M}} \in {\mathbb{R}}_{+}$ and ${\overline{s},\underset{¯}{s}} \geq 1$, such that^33^3We consider throughout $\underset{¯}{s} = \overline{s} = 2$ without loss of generality. for all ${x \in {\mathbb{R}}^{n}},{u \in {\mathbb{R}}^{m}}$ and $t \in {\mathbb{N}}$,\The lower bound in the above assumption, which we refer to as the "observability" of the state with respect to cost, excludes cases when unstable states can be "hidden" in the cost. This condition is common in the literature and is also referred to as positive definiteness or detectability of the system with respect to stage costs.

### Relation to Tracking Problems

For completeness, we also point out a connection between the stability discussion below and tracking problems. Consider the problem of tracking an unknown, bounded, time-varying reference signal $r_{t} \in {\mathbb{R}}^{n}$ given system dynamics, where the agent has access to $r_{t}$ at timestep $t$, but not before. We can then write the state evolution of the tracking error ${\overset{\sim}{x}}_{t}:={x_{t} - r_{t}}$ as where $\nu_{t} \in {\mathbb{R}}^{n}$ can be considered as the disturbance of the modified system; note that $r_{t + 1}$ and $w_{t}$ are unknown at time $t$. If the assumptions above are satisfied the tracking problem can be treated as the regulation under the adversarial noise problem in Section 2.1.

## Main Results

In this section, we derive our main results for LTV and LTI systems. We start with the following motivating example of discounted LQR as a particular case when an unstable system attains linear regret if Assumption 2.7 is violated.

### Example 3.1

Consider the dynamics, with $A_{t} = A$, $B_{t} = B$ for all $t \in {\mathbb{N}}$, and the following cost function where $\alpha \in {}$ is a discount factor, $Q \in {\mathbb{R}}^{n \times n}$, $R \in {\mathbb{R}}^{m \times m}$ are positive definite matrices, and $P_{\alpha} \in {\mathbb{R}}^{n \times n}$ satisfies the following equation The above is the discrete algebraic Riccati equation (DARE) for the modified system $({\sqrt{\alpha}A},B)$ with cost matrices $Q$ and $\frac{R}{\alpha}$. The stage costs do not satisfy the condition in Assumption 2.7 as there exists no uniform lower bound. Consider now the certainty equivalent controller that minimises the cost assuming ${w_{t} = \mathbf{0}}\mspace{21mu}{{\forall t} \in {\mathbb{N}}}$. The optimal policy $\mu_{t}$ in this setting is then a linear state feedback, given by $\mu_{t} = {- {K_{\alpha}x_{t}}}$, where We make the hypothesis that the value function (cost-to-go) at time step $t$ associated with this policy is given by where $v_{t} \in {\mathbb{R}}^{n}$, $q_{t} \in {\mathbb{R}}$. At timestep $T$, it is easily verified with $v_{T} = \mathbf{0}$, $q_{T} = 0$. Assuming the hypothesis is true for $t + 1$, the cost-to-go at $t$ is One can verify that the induction hypothesis is verified only if $P_{\alpha}$ satisfies the DARE for the modified system, and The cost under this linear state feedback policy can then be attained by applying the preceding recursion repeatedly and $F_{\alpha}:={A - {BK_{\alpha}}}$. It is known that for $\alpha$ small enough the closed-loop system matrix $F_{\alpha}$ may in fact be unstable. Consider the set, Then for some $\overline{\alpha} \in \Gamma$, and for $\sigma:={\overline{\alpha}{\| F_{\alpha}\|}}$ It is then evident that there exist ${C_{w},C_{0}} \in {\mathbb{R}}_{+}$, such that Moreover, such $C_{0}$ and $C_{w}$ exist for all costs of the form. Hence, for all such ${\{ c_{t}\}}_{t = 0}^{T}$, the regret will also attain the same bound. Thus, while the considered policy achieves linear regret, the closed-loop with the system is unstable.

This example shows how the violation of Assumption 2.7 can make regret hide the instability of the system.

### Linear Time-Varying Systems

The following theorem establishes the regret-stability relation for the time-varying policy ${\mu_{t}{(x_{t})}} = {- {K_{t}x_{t}}}$.

### Theorem 3.2

Assume that Assumption 2.7 holds. Given the cost function and LTV system, consider a linear time-varying state feedback policy ${\mu_{t}{(x_{t})}} = {- {K_{t}x_{t}}}$. If the closed-loop system under this policy is BIBS stable, and if there exists $D \in {\mathbb{R}}_{+}$ such that then the policy $\mu$ attains linear regret.

### Proof

Using the condition in Assumption 2.7 and defining $M:={\overline{M}{({1 + {\max_{0 \leq t < T}{\| K_{t}\|}^{2}}})}}$ where ${\overline{D},\overline{H}} \in {\mathbb{R}}_{+}$ are such that The limit in exists due to the condition in and the fact that the series contains only non-negative terms. The limit in exists due to the BIBS assumption and the series of non-negative terms only. Since ${J_{T}{(x_{0},{\mathbf{u}};{\mathbf{w}})}} \geq 0$ for all $\mathbf{u}$, the regret will necessarily attain the same bound with $C_{w} = {2M\overline{H}W^{2}}$ and $C_{0} = {2M\overline{D}X^{2}}$. ∎ We note that given Assumption 2.5.iii. holds, the condition in is stronger than asymptotic stability. In fact, if is satisfied, then Assumption 2.5.iii. implies asymptotic stability of the closed-loop system.

The following theorem establishes the implication of linear regret on the stability of the closed-loop system with linear time-varying state feedback policies.

### Theorem 3.3

Assume that Assumptions 2.5 and 2.7 hold. Given the cost function and LTV system, if a linear time-varying state feedback policy ${\mu_{t}{(x_{t})}} = {- {K_{t}x_{t}}}$ attains linear regret, then the closed-loop system under this policy is asymptotically stable.

### Proof

Given Assumption 2.5.i. holds, there exists a policy ${\overline{\mu}}_{t} = {- {{\overline{K}}_{t}x_{t}}}$ such that the closed-loop system under this policy is exponentially stable. It can be shown that this implies BIBS stability, and the bound in is always satisfied. Specifically, from the definition of exponential stability, it can be inferred that taking $t_{0} = 0$ and $D = \frac{d}{1 - \delta}$ the bound in is achieved. Therefore, from Theorem 3.2 there exist some ${C_{w}^{\star},C_{0}^{\star}} \in {\mathbb{R}}_{+}$, such that where the first inequality follows from the definition of ${\mathbf{u}}^{\star}$. Then, linear regret of any policy $\mu$ is equivalent to where ${\overline{C}}_{w} = {({C_{w}^{\star} + C_{w}})}$ and ${\overline{C}}_{0} = {({C_{0}^{\star} + C_{0}})}$. Assume, for the sake of contradiction, that there exists a policy ${\mu_{t}{(x_{t})}} = {- {K_{t}x_{t}}}$, that attains the bound in but the associated closed-loop system is not asymptotically stable. This is equivalent (Lemma 5 and Assumption 2.5.ii.) to assuming that either the limit in does not exist or it is greater than zero, or equivalently Using the lower bound in Assumption 2.7, we then have Consider first the case when ${\operatorname{lim\ inf}\limits_{T\rightarrow\infty}{\|{\Phi{(T,0)}}\|}} = \infty$. Then, necessarily there exists a ${\overline{x}}_{0} \neq \mathbf{0}$, such, that ${\operatorname{lim\ inf}\limits_{T\rightarrow\infty}{\|{\Phi{(T,0)}{\overline{x}}_{0}}\|}} = \infty$. For $x_{0} = {\overline{x}}_{0}$ and $w_{t} = \mathbf{0}$ for all $t \in {\mathbb{N}}$, one can take the time-averaged limit of the above where the last inequality follows from the Stolz-Césaro theorem. This leads to a contradiction with the upper bound in Given Assumption 2.5.ii., the only other remaining case is when the upper and lower limits in are finite (whether equal or not) and non-zero. For this case, consider $x_{0} = \mathbf{0}$ and $w_{k - 1} = {C\Phi{(k,0)}{\overline{w}}_{0}}$, where and the vector ${\overline{w}}_{0} \in {\mathbb{R}}^{n}$ is non-zero. Since $\operatorname{lim\ sup}\limits_{T\rightarrow\infty}{\|{\Phi{(T,0)}}\|}$ is finite, such a $C \in {\mathbb{R}}_{+}$ exists. Then By taking the time-averaged limits of both sides of the inequality and applying the Stolz-Césaro theorem again The lower bound becomes unbounded, contradicting and completing the proof by contraposition. ∎ Thus, under suitable conditions, linear regret guarantees asymptotic stability. However, as shown in Theorem 3.2 and also pointed out in for a similar setting, the converse is not always the case, i.e. asymptotic stability alone does not imply linear regret.

### Remark 3.1

The results can be generalized to affine policies of the form ${\mu{(x_{t})}} = {{- {K_{t}x_{t}}} + d_{t}}$, for some $d_{t} \in {\mathbb{R}}^{m}$, given that $d_{t}$ are bounded for all $t \in {\mathbb{N}}$.

### Remark 3.2

Note that inferring stability from regret requires not only stabilizability (Assumption 2.5.i.) but also certain conditions on the benchmark. Indeed to guarantee, it is necessary that a stabilizing policy exists in the feasible space of the benchmark. This holds here since the benchmark is the non-causal controller $\mathbf{u}^{\star}$ (dynamic regret), but weaker benchmarks that are constrained to specific policy classes can also be considered (policy regret).

### Linear Time-Invariant Systems

In this section, we consider the optimal control problem of minimizing the cost subject to the LTI dynamics where $A \in {\mathbb{R}}^{n \times n}$, $B \in {\mathbb{R}}^{n \times m}$. The following establishes the relation between linear regret and stability in this setting.

### Theorem 3.4

Assume that Assumptions 2.5.i., and 2.7 hold. Given the cost function and LTI system, a linear stationary state feedback policy ${\mu{(x_{t})}} = {- {Kx_{t}}}$ attains linear regret if and only if the closed-loop system $x_{t + 1} = {Fx_{t}}$ under this policy is asymptotically stable.

### Proof

To show that the required regret bound is achieved for an asymptotically stabilizing stationary policy, consider the state at timestep $0 \leq t < T$, given by taking $w_{- 1} = \mathbf{0}$. Using the cost bounds in Assumption 2.7 and denoting $M:={\overline{M}{({1 + {\| K\|}^{2}})}}$ where we used the fact that for ${\rho{(F)}} < 1$ there exists a $g \in {\mathbb{R}}_{+}$, such that ${\| F^{k}\|} \leq {g\varepsilon^{k}}$ for all $k > 0$, where $\varepsilon:=\frac{1 + {\rho{(F)}}}{2} \in {}$. Since costs are non-negative, regret attains the same bound.

To prove the reverse statement, assume, for the sake of contradiction, that there exists a matrix $K'$ such that ${\rho{({A - {BK'}})}} \geq 1$ attaining linear regret. From the previous analysis, any stabilizing state feedback matrix $K$ attains a cost that scales linearly with the time horizon. Moreover, such a matrix exists as for LTI systems Assumption 2.5.i. corresponds to the stabilizability of the pair $(A,B)$. Then, using the same arguments as in the proof of Theorem 3.3, there exist ${{\overline{C}}_{w},{\overline{C}}_{0}} \in {\mathbb{R}}_{+}$ such that From Assumption 2.7 it is true that Since the result should hold for any initial state and any disturbance within the defined Euclidian ball, consider $x_{0} = \mathbf{0}$ and ${w_{t} = \overline{w}}\mspace{21mu}{{\forall t} \in {\mathbb{N}}}$ such that ${\|\overline{w}\|} = W$ and ${F'\overline{w}} = {\rho{(F')}\overline{w}}$. We then have In contrast to the LTV case, in the LTI setting, asymptotic and exponential stability are equivalent, leading to an equivalency between linear regret and stability.

## Numerical Example

To visualize the necessary and sufficient condition in Theorem 3.4, a simple two-dimensional system with single input is considered. In particular, for $A = {\lbrack 1\quad 1;0\quad 1\rbrack}$ and $B = {\lbrack 1;0.5\rbrack}$, three LTI state feedback controllers are considered, $K_{1} = {\lbrack 0.2\quad 0.4\rbrack}$, $K_{2} = {\lbrack 0\quad 1\rbrack}$, and $K_{3} = {\lbrack{- 0.02}\quad 0.5\rbrack}$. These produce respectively, stable, marginally stable, and unstable closed-loop systems. The cost function is taken to be quadratic with $Q = {\lbrack 1.5\quad 0;0\quad 1.5\rbrack}$ and $R = 1$ as the state and input weighting matrices, respectively. The disturbance $w_{t}$ for all $0 \leq t < T$ is taken to be the normalized eigenvector of the closed-loop system matrix corresponding to the largest eigenvalue, to approximate the worst-case regret for the given policy. The time-averaged regret for each of the controllers is calculated for a time horizon ranging from $1$ to $100$ and is plotted in a logarithmic scale in Figure 1. Specifically, the average regret of the stable controller can be upper bounded by a constant, that of the marginally stable controller scales with $T$ and for the unstable one with a higher order of $T$.

Figure 1: Time-averaged regret, $\frac{\mathcal{R}_{T}}{T}$ for a LTI system on a semilog scale. The stable system can be upper bounded by a constant while the marginally stable and unstable ones scale with an order of l o g (T).

## Conclusions

In this work, we studied the interconnection of the notion of regret coming from online optimization and the control theoretic concept of stability. Given a linear state feedback policy that attains linear regret, and certain upper and lower bounds on the objective stage costs, we show that the closed-loop system is necessarily asymptotically stable, both for the time-varying and time-invariant cases. The converse result also holds given that the closed-loop system is BIBS stable and has absolute summable norms of its state transition matrices. The results can be used to directly prove the stability of algorithms with regret guarantees and vice versa. This work can be a stepping stone for the consideration of adaptive policies, under which the considered setting is no longer linear; this will allow the analysis of a wider range of online algorithms.
