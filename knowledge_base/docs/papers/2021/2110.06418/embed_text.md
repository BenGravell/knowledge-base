## Introduction

Stabilizing an unknown control system is one of the most fundamental problems in control systems engineering. A wide variety of tasks - from maintaining a dynamical system around a desired equilibrium point, to tracking a reference signal (e.g a pilot's input to a plane) - can be recast in terms of stability. More generally, synthesizing an initial stabilizing controller is often a necessary first step towards solving more complex tasks, such as adaptive or robust control design.

In this work, we consider the problem of finding a stabilizing controller for an unknown dynamical system via direct policy search methods. We introduce a simple procedure based off policy gradients which provably stabilizes a dynamical system around an equilibrium point. Our algorithm only requires access to a simulator which can return rollouts of the system under different control policies, and can efficiently stabilize both linear and smooth, nonlinear systems.

Relative to model-based approaches, model-free procedures, such as policy gradients, have two key advantages: they are conceptually simple to implement, and they are easily adaptable; that is, the same method can be applied in a wide variety of domains without much regard to the intricacies of the underlying dynamics. Due to their simplicity and flexibility, direct policy search methods have become increasingly popular amongst practitioners, especially in settings with complex, nonlinear dynamics which may be challenging to model. In particular, they have served as the main workhorse for recent breakthroughs in reinforcement learning and control.

Despite their popularity amongst practitioners, model-free approaches for continuous control have only recently started to receive attention from the theory community. While these analyses have begun to map out the computational and statistical tradeoffs that emerge in choosing between model-based and model-free approaches, they all share a common assumption: that the unknown dynamical system in question is stable, or that an initial stabilizing controller is known. As such, they do not address the perhaps more basic question, *how do we arrive at a stabilizing controller in the first place?*

### Contributions

We establish a reduction from stabilizing an unknown dynamical system to solving a series of discounted, infinite-horizon LQR problems via policy gradients, for which no knowledge of an initial stable controller is needed. Our approach, which we call *discount annealing*, gradually increases the discount factor and yields a control policy which is near optimal for the undiscounted LQR objective. To the best of our knowledge, our algorithm is the first model-free procedure shown to provably stabilize unknown dynamical systems, thereby solving an open problem from Fazel et al..

We begin by studying linear, time-invariant dynamical systems with full state observation and assume access to *inexact* cost and gradient evaluations of the discounted, infinite-horizon LQR cost of a state-feedback controller $K$. Previous analyses (e.g., ) establish how such evaluations can be implemented with access to (finitely many, finite horizon) trajectories sampled from a simulator. We show that our method recovers the controller $K_{\star}$ which is the optimal solution of the *undiscounted* LQR problem in a bounded number of iterations, up to optimization and simulator error. The stability of the resulting $K_{\star}$ is guaranteed by known stability margin results for LQR. In short, we prove the following guarantee:

### Theorem 1. ‣ 2 Stabilizing Linear Dynamical Systems ‣ Stabilizing Dynamical Systems via Policy Gradient Methods") (informal)

For linear systems, discount annealing returns a stabilizing state-feedback controller which is also near-optimal for the LQR problem. It uses at most polynomially many, $\varepsilon$-inexact gradient and cost evaluations, where the tolerance $\varepsilon$ also depends polynomially on the relevant problem parameters.

Since both the number of queries and error tolerance are polynomial, discount annealing can be efficiently implemented using at most polynomially many samples from a simulator.

Furthermore, our results extend to smooth, *nonlinear* dynamical systems. Given access to a simulator that can return damped system rollouts, we show that our algorithm finds a controller that attains near-optimal LQR cost for the Jacobian linearization of the nonlinear dynamics at the equilibrium. We then show that this controller stabilizes the nonlinear system within a neighborhood of its equilibrium.

### Theorem 2. ‣ 3 Stabilizing Nonlinear Dynamical Systems ‣ Stabilizing Dynamical Systems via Policy Gradient Methods") (informal)

Discount annealing returns a state-feedback controller which is exponentially stabilizing for smooth, nonlinear systems within a neighborhood of their equilibrium, using again only polynomially many samples drawn from a simulator.

In each case, the algorithm returns a near optimal solution $K$ to the relevant LQR problem (or local approximation thereof). Hence, the stability properties of $K$ are, in theory, no better than those of the optimal LQR controller $K_{\star}$. Importantly, the latter may have worse stability guarantees than the optimal solution of a corresponding robust control objective (e.g. $\mathcal{H}_{\infty}$ synthesis). Nevertheless, we focus on the LQR subroutine in the interest of simplicity, clarity, and in order to leverage prior analyses of model-free methods for LQR. Extending our procedure to robust-control objectives is an exciting direction for future work.

Lastly, while our theoretical analysis only guarantees that the resulting controller will be stabilizing within a small neighborhood of the equilibrium, our simulations on nonlinear systems, such as the nonlinear cartpole, illustrate that discount annealing produces controllers that are competitive with established robust control procedures, such as $\mathcal{H}_{\infty}$ synthesis, without requiring any knowledge of the underlying dynamics.

### Related work

Given its central importance to the field, stabilization of unknown and uncertain dynamical systems has received extensive attention within the controls literature. We review some of the relevant literature and point the reader towards classical texts for a more comprehensive treatment.

Model-based approaches. Model-based methods construct approximate system models in order to synthesize stabilizing control policies. Traditional analyses consider stabilization of both linear and nonlinear dynamical systems in the asymptotic limit of sufficient data. More recent, non-asymptotic studies have focused almost entirely on *linear* systems, where the controller is generated using data from multiple independent trajectories. Assuming the model is known, stabilizing policies may also be synthesized via convex optimization by combining a 'dual Lyapunov theorem' with sum-of-squares programming. Relative to these analysis our focus is on strengthening the theoretical foundations of model-free procedures and establishing rigorous guarantees that policy gradient methods can also be used to generate stabilizing controllers.

Online control. Online control studies the problem of adaptively *fine-tuning* the performance of an already-stabilizing control policy on a *single* trajectory. Though early papers in this direction consider systems without pre-given stabilizing controllers, their guarantees degrade exponentially in the system dimension (a penalty ultimately shown to be unavoidable by Chen and Hazan ). Rather than fine-tuning an already stabilizing controller, we focus on the more basic problem of finding a controller which is stabilizing in the first place, and allow for the use of multiple independent trajectories.

Model-free approaches. Model-free approaches eschew trying to approximate the underlying dynamics and instead directly search over the space of control policies. The landmark paper of Fazel et al. proves that, despite the non-convexity of the problem, direct policy search on the infinite-horizon LQR objective efficiently converges to the globally optimal policy, assuming the search is initialized at an already stabilizing controller. Fazel et al. pose the synthesis of this initial stabilizing controller via policy gradients as an open problem; one that we solve in this work.

Following this result, there have been a large number of works studying policy gradients procedures in continuous control, see for example Feng and Lavaei; Malik et al.; Mohammadi et al.; Zhang et al. just to name a few. Relative to our analysis, these papers consider questions of policy finite-tuning, derivative-free methods, and robust (or distributed) control which are important, yet somewhat orthogonal to the stabilization question considered herein. The recent analysis by Lamperski is perhaps the most closely related piece of prior work. It proposes a model-free, off-policy algorithm for computing a stabilizing controller for deterministic LQR systems. Much like discount annealing, the algorithm also works by alternating between policy optimization (in their case by a closed-form policy improvement step based on the Riccati update) and increasing a damping factor. However, whereas we provide precise finite-time convergence guarantees to a stabilizing controller for both linear and nonlinear systems, the guarantees in Lamperski are entirely asymptotic and restricted to linear systems. Furthermore, we pay special attention to quantifying the various error tolerances in the gradient and cost queries to ensure that the algorithm can be efficiently implemented in finite samples.

### Background on stability of dynamical systems

Before introducing our results, we first review some of the basic concepts and definitions regarding stability of dynamical systems. In this paper, we study discrete-time, noiseless, time-invariant dynamical systems with states $\mathbf{x}_{t} \in {\mathbb{R}}^{d_{x}}$ and control inputs $\mathbf{u}_{t} \in {\mathbb{R}}^{d_{u}}$. In particular, given an initial state $\mathbf{x}_{0}$, the dynamics evolves according to $\mathbf{x}_{t + 1} = {G{(\mathbf{x}_{t},\mathbf{u}_{t})}}$ where $G:{{{\mathbb{R}}^{d_{x}} \times {\mathbb{R}}^{d_{u}}}\rightarrow{\mathbb{R}}^{d_{x}}}$ is a state transition map. An equilibrium point of a dynamical system is a state $\mathbf{x}_{\star} \in {\mathbb{R}}^{d_{x}}$ such that ${G{(\mathbf{x}_{\star},0)}} = \mathbf{x}_{\star}$. As per convention, we assume that the origin $\mathbf{x}_{\star} = 0$ is the desired equilibrium point around which we wish to stabilize the system.

This paper restricts its attention to static state-feedback policies of the form $\mathbf{u}_{t} = {K\mathbf{x}_{t}}$ for a fixed matrix $K \in {\mathbb{R}}^{d_{u} \times d_{x}}$. Abusing notation slightly, we conflate the matrix $K$ with its induced policy. Our aim is to find a policy $K$ which is *exponentially stabilizing* around the equilbrium point.

Time-invariant, linear systems, where ${G{(\mathbf{x},\mathbf{u})}} = {{A\mathbf{x}} + {B\mathbf{u}}}$ are stabilizable if and only if there exists a $K$ such that $A + {BK}$ is a stable matrix. That is if ${\rho{({A + {BK}})}} < 1$, where $\rho{(X)}$ denotes the spectral radius, or the largest eigenvalue magnitude, of a matrix $X$. For general nonlinear systems, our goal is to find controllers which satisfy the following general, quantitative definition of exponential stability (e.g Chapter 5.2 in Sastry ). Throughout, $\parallel \cdot \parallel$ denotes the Euclidean norm.

### Definition 1.1

A controller $K$ is *$(m,\alpha)$-exponentially stable* for dynamics $G$ if there exist constants ${m,\alpha} > 0$ such that if inputs are chosen according to $\mathbf{u}_{t} = {K\mathbf{x}_{t}}$, the sequence of states $\mathbf{x}_{t + 1} = {G{(\mathbf{x}_{t},\mathbf{u}_{t})}}$ satisfy

Likewise, $K$ is *$(m,\alpha)$-exponentially stable on radius $r > 0$* if (1.1) holds for all $\mathbf{x}_{0}$ such that ${\|\mathbf{x}_{0}\|} \leq r$.

For linear systems, a controller $K$ is stabilizing if and only if it is stable over the entire state space, however, the restriction to stabilization over a particular radius is in general needed for nonlinear systems. Our approach for stabilizing nonlinear systems relies on analyzing their *Jacobian linearization* about the origin equilibrium. Given a continuously differentiable transition operator $G$, the local dynamics can be approximated by the Jacobian linearization $(A_{jac},B_{jac})$ of $G$ about the zero equilibrium; that is

In particular, for $\mathbf{x}$ and $\mathbf{u}$ sufficiently small, ${G{(\mathbf{x},\mathbf{u})}} = {{A_{jac}\mathbf{x}} + {B_{jac}\mathbf{u}} + {f_{nl}{(\mathbf{x},\mathbf{u})}}}$, where $f_{nl}{(\mathbf{x},\mathbf{u})}$ is a nonlinear remainder from the Taylor expansion of $G$. To ensure stabilization via state-feedback is feasible, we assume throughout our presentation that the linearized dynamics $(A_{jac},B_{jac})$ are stabilizable.

## Stabilizing Linear Dynamical Systems

We now present our main results establishing how our algorithm, discount annealing, provably stabilizes linear dynamical systems via a reduction to direct policy search methods. We begin with the following preliminaries on the Linear Quadratic Regulator (LQR).

### Definition 2.1 (LQR Objective)

For a given starting state $\mathbf{x}$, we define the LQR problem $J_{lin}$ with discount factor $\gamma \in {(0,1\rbrack}$, dynamic matrices $(A,B)$, and state feedback controller $K$ as,

Here, $\mathbf{x}_{t} \in {\mathbb{R}}^{d_{x}}$, $\mathbf{u}_{t} \in {\mathbb{R}}^{d_{u}}$, and $Q,R$ are positive definite matrices. Slightly overloading notation, we define

to be the same as the problem above, but where the initial state is now drawn from the uniform distribution over the sphere in ${\mathbb{R}}^{d_{x}}$ of radius $\sqrt{d_{x}}$.^11^1This scaling is chosen so that the initial state distribution has identity covariance, and yields cost equivalent to $\mathbf{x}_{0} \sim {\mathcal{N}{(0,I)}}$.

To simplify our presentation, we adopt the shorthand ${J_{lin}{({K \mid \gamma})}}:={J_{lin}{({K \mid {\gamma,A,B}})}}$ in cases where the system dynamics $(A,B)$ are understood from context. Furthermore, we assume that $(A,B)$ is stabilizable and that ${{\lambda_{\min}{(Q)}},{\lambda_{\min}{(R)}}} \geq 1$. It is a well-known fact that $K_{\star,\gamma}:={{{\arg\min}_{K}J_{lin}}{({K \mid {\gamma,A,B}})}}$ achieves the minimum LQR cost over all possible control laws. We begin our analysis with the observation that the discounted LQR problem is equivalent to the undiscounted LQR problem with damped dynamics matrices.^22^2This lemma is folklore within the controls community, see e.g. Lamperski.

### Lemma 2.1

For all controllers $K$ such that ${J_{lin}{({K \mid {\gamma,A,B}})}} < \infty$,

From this equivalence, it follows from basic facts about LQR that a controller $K$ satisfies ${J_{lin}{({0 \mid {\gamma,A,B}})}} < \infty$ if and only if $\sqrt{\gamma}{({A + {BK}})}$ is stable. Consequently, for $\gamma < {\rho{(A)}^{- 2}}$, the zero controller is stabilizing and one can solve the discounted LQR problem via direct policy search initialized at $K$ = 0. At this point, one may wonder whether the solution to this highly discounted problem yields a controller which stabilizes the undiscounted system. If this were true, running policy gradients (defined in Eq. 2.1) to convergence, on a single discounted LQR problem, would suffice to find a stabilizing controller.

Unfortunately, the following proposition shows that this is not the case.

### Proposition 2.2 (Impossibility of Reward Shaping)

Fix $A = {{diag}{}}$. For any positive definite cost matrices $Q,R$ and discount factor $\gamma$ such that $\sqrt{\gamma}A$ is stable, there exists a matrix $B$ such that $(A,B)$ is controllable (and thus stabilizable), yet the optimal controller $K_{\star,\gamma}:={{{\arg\min}_{K}J}{({K \mid {\gamma,A,B}})}}$ on the discounted problem is such that $A + {BK_{\star,\gamma}}$ is unstable.

Discount Annealing Initialize: Objective J(⋅∣⋅), γ0 ∈ (0,ρ (A)−2), K0 ← 0, and Q ← I, R ← I For t = 0, 1, … 1. If γt = 1, run policy gradients once more as in Step 2, break, and return the resulting K′. 2. Using policy gradients (see Eq. 2.1) initialized at Kt, find K′ such that: ${{{J_{lin}{({K^{\prime} \mid \gamma_{t}})}} - {{\min\limits_{K}J_{lin}}{({K \mid \gamma_{t}})}}} \leq d_{x}}.$ (2.2) 3. Update initial controller Kt + 1 ← K′. 4. Using binary or random search, find a discount factor γ′ ∈ [γt, 1] such that 2.5 J (Kt + 1∣γt) ≤ J (Kt + 1∣γ′) ≤ 8 J (Kt + 1∣γt). (2.3) 5. Update the discount factor γt + 1 ← γ′.
Figure 1: Discount annealing algorithm. The procedure is identical for both linear and nonlinear systems. For linear, we initialize J = Jlin(⋅∣γ0) and for nonlinear J = Jnl(⋅∣γ0,r⋆) where r⋆ is chosen as in Theorem 2. See Theorem 1, Theorem 2, and Appendix C for details regarding policy gradients and binary (or random) search. The constants above are chosen for convenience, any constants c1, c2 such that 1 &lt; c1 &lt; c2 suffice.

We now describe the discount annealing procedure for linear systems (Figure 1), which provably recovers a stabilizing controller $K$. For simplicity, we present the algorithm assuming access to noisy, bounded cost and gradient evaluations which satisfy the following definition. Employing standard arguments from, we illustrate how these evaluations can be efficiently implemented using polynomially many samples drawn from a simulator in Appendix C.

### Definition 2.2 (Gradient and Cost Queries)

Given an error parameter $\varepsilon > 0$ and a function $J:{{\mathbb{R}}^{d}\rightarrow{\mathbb{R}}}$, $\varepsilon\text{-}{\mathtt{G}\mathtt{r}\mathtt{a}\mathtt{d}}{(J,\mathbf{z})}$ returns a vector $\overset{\sim}{\nabla}$ such that ${\|{\overset{\sim}{\nabla} - {{\nabla J}{(\mathbf{z})}}}\|}_{F} \leq \varepsilon$. Similarly, $\varepsilon\text{-}{\mathtt{E}\mathtt{v}\mathtt{a}\mathtt{l}}{(J,\mathbf{z},c)}$ returns a scalar $v$ such that ${|{v - {\min{\{{J{(\mathbf{z})}},c\}}}}|} \leq \varepsilon$.

The procedure leverages the equivalence (Lemma 2.1) between discounted costs and damped dynamics for LQR, and the consequence that the zero controller is stabilizing if we choose $\gamma_{0}$ sufficiently small. Hence, for this discount factor, we may apply policy gradients initialized at the zero controller in order to recover a controller $K_{1}$ which is near-optimal for the $\gamma_{0}$ discounted objective.

Our key insight is that, due to known stability margins for LQR controllers, $K_{1}$ is stabilizing for the $\gamma_{1}$ discounted dynamics for some discount factor $\gamma_{1} > {{({1 + c})}\gamma_{0}}$, where $c$ is a small constant that has a uniform lower bound. Therefore, $K_{1}$ has finite cost on the $\gamma_{1}$ discounted problem, so that we may again use policy gradients initialized at $K_{1}$ to compute a near-optimal controller $K_{2}$ for this larger discount factor. By iterating, we have that $\gamma_{t} \geq {{({1 + c})}^{t}\gamma_{0}}$ and can increase the discount factor up to 1, yielding a near-optimal stabilizing controller for the undiscounted LQR objective.

The rate at which we can increase the discount factors $\gamma_{t}$ depends on certain properties of the (unknown) dynamical system. Therefore, we opt for binary search to compute the desired $\gamma$ in the absence of system knowledge. This yields the following guarantee, which we state in terms of properties of the matrix $P_{\star}$, the optimal value function for the undiscounted LQR problem, which satisfies ${{\min_{K}J_{lin}}{({K \mid 1})}} = {{tr}\left\lbrack P_{\star} \right\rbrack}$ (see Appendix A for further details).

### Theorem 1 (Linear Systems)

Let $M_{lin}:={\max{\{{16tr\left\lbrack P_{\star} \right\rbrack},{J_{lin}{({K_{0} \mid \gamma_{0}})}}\}}}$. The following statements are true regarding the discount annealing algorithm when run on linear dynamical systems:

Discount annealing returns a controller $\hat{K}$ which is $(\sqrt{2tr{\lbrack P_{\star}\rbrack}},{({4tr\left\lbrack P_{\star} \right\rbrack})}^{- 1})$-exponentially stable.

If $\gamma_{0} < 1$, the algorithm is guaranteed to halt whenever $t$ is greater than $64tr\left\lbrack P_{\star} \right\rbrack^{4}{\log{({1/\gamma_{0}})}}$.

Furthermore, at each iteration $t$:

Policy gradients as defined in Eq. 2.1 achieves the guarantee in Eq. 2.2 using only ${poly}{(M_{lin},{\| A\|}_{op},{\| B\|}_{op})}$ many queries to $\varepsilon\text{-}{\mathtt{G}\mathtt{r}\mathtt{a}\mathtt{d}}{( \cdot,J_{lin}{( \cdot \mid \gamma)})}$ as long as $\varepsilon$ is less than ${poly}{(M_{lin}^{- 1},{\| A\|}_{op}^{- 1},{\| B\|}_{op}^{- 1})}$.

The noisy binary search algorithm (see Figure 2) returns a discount factor $\gamma^{\prime}$ satisfying Eq. 2.3 using at most ${\lceil{4{\log{({{tr}\left\lbrack P_{\star} \right\rbrack})}}}\rceil} + 10$ many queries to $\varepsilon\text{-}{\mathtt{E}\mathtt{v}\mathtt{a}\mathtt{l}}{( \cdot,J_{lin}{( \cdot \mid \gamma)})}$ for $\varepsilon = d_{x}}$.

We remark that since $\varepsilon$ need only be polynomially small in the relevant problem parameters, each call to $\varepsilon\text{-}{\mathtt{G}\mathtt{r}\mathtt{a}\mathtt{d}}$ and $\varepsilon\text{-}{\mathtt{E}\mathtt{v}\mathtt{a}\mathtt{l}}$ can be carried out using only polynomially many samples from a simulator which returns finite horizon system trajectories under various control policies. We make this claim formal in Appendix C.

### Proof

We prove part $b)$ of the theorem and defer the proofs of the remaining parts of to Appendix A. Define $P_{K,\gamma}$ to be the solution to the discrete-time Lyapunov equation. That is for $\sqrt{\gamma}{({A + {BK}})}$ stable, $P_{K,\gamma}$ solves:

Using this notation, $P_{\star} = P_{K_{\star},1}$ is the solution to the above Lyapunov equation with $\gamma = 1$. The key step of the proof is Proposition A.4, which uses Lyapunov theory to verify the following: given the current discount factor $\gamma_{t}$, an idealized discount factor $\gamma_{t + 1}^{\prime}$ defined by

satisfies ${J_{lin}{({K_{t + 1} \mid \gamma_{t + 1}^{\prime}})}} = {{tr}{\lbrack P_{K_{t + 1},\gamma_{t + 1}^{\prime}}\rbrack}} \leq {2tr\left\lbrack P_{K_{t + 1},\gamma_{t}} \right\rbrack} = {2J_{lin}{({K_{t + 1} \mid \gamma_{t}})}}$. Since the control cost is non-decreasing in $\gamma$, the binary search update in Step 4 ensures that the actual $\gamma_{t + 1}$ also satisfies

The following calculation (which uses $d_{x} \leq {{tr}\left\lbrack P_{\star} \right\rbrack}$ for ${\lambda_{\min}{(Q)}} \geq 1$) justifies the second inequality above:

Therefore, $\gamma_{t} \geq {{({{1/{({128tr\left\lbrack P_{\star} \right\rbrack^{4}})}} + 1})}^{2t}\gamma_{0}}$. The precise bound follows from taking logs of both sides and using the numerical inequality ${\log{({1 + x})}} \leq x$ to simplify the denominator.

## Stabilizing Nonlinear Dynamical Systems

We now extend the guarantees of the discount annealing algorithm to smooth, nonlinear systems. Whereas our study of linear systems explicitly leveraged the equivalence of discounted costs and damped dynamics, our analysis for nonlinear systems *requires* access to system rollouts under damped dynamics, since the previous equivalence between discounting and damping breaks down in nonlinear settings.

More specifically, in this section, we assume access to a simulator which given a controller $K$, returns trajectories generated according to $\mathbf{x}_{t + 1} = {\sqrt{\gamma}G_{nl}{(\mathbf{x}_{t},{K\mathbf{x}_{t}})}}$ for any damping factor $\gamma \in {(0,1\rbrack}$, where $G_{nl}$ is the transition operator for the nonlinear system. While such trajectories may be infeasible to generate on a physical system, we believe these are reasonable to consider when dynamics are represented using software simulators, as is often the case in practice.

The discount annealing algorithm for nonlinear systems is almost identical to the algorithm for linear systems. It again works by repeatedly solving a series of quadratic cost objectives on the nonlinear dynamics as defined below, and progressively increasing the damping factor $\gamma$.

### Definition 3.1 (Nonlinear Objective)

For a statefeedback controller $K:{{\mathbb{R}}^{d_{x}}\rightarrow{\mathbb{R}}^{d_{u}}}$, damping factor $\gamma \in {(0,1\rbrack}$, and an initial state $\mathbf{x}$, we define:

Overloading notation as before, we let ${J_{nl}{({K \mid {\gamma,r}})}}:={{{\mathbb{E}}_{\mathbf{x} \sim {r \cdot \mathcal{S}^{d_{x} - 1}}}\left\lbrack {J_{nl}{({K \mid {\gamma,\mathbf{x}}})}} \right\rbrack} \times \frac{d_{x}}{r^{2}}}$.

The normalization by $d_{x}/r^{2}$ above is chosen so that the nonlinear objective coincides with the LQR objective when $G_{nl}$ is in fact linear. Relative to the linear case, the only algorithmic difference for nonlinear systems is that we introduce an extra parameter $r$ which determines the radius for the initial state distribution. As established in Theorem 2. ‣ 3 Stabilizing Nonlinear Dynamical Systems ‣ Stabilizing Dynamical Systems via Policy Gradient Methods"), this parameter must be chosen small enough to ensure that discount annealing succeeds. Our analysis pertains to dynamics which satisfy the following smoothness definition.

### Assumption 1 (Local Smoothness)

The transition map $G_{nl}$ is continuously differentiable. Furthermore, there exist ${r_{nl},\beta_{nl}} > 0$ such that for all ${(\mathbf{x},\mathbf{u})} \in {\mathbb{R}}^{d_{x} + d_{u}}$ with ${{\|\mathbf{x}\|} + {\|\mathbf{u}\|}} \leq r_{nl}$,

For simplicity, we assume $\beta_{nl} \geq 1$ and $r_{nl} \leq 1$. Using Assumption 1. ‣ 3 Stabilizing Nonlinear Dynamical Systems ‣ Stabilizing Dynamical Systems via Policy Gradient Methods"), we can apply Taylor's theorem to rewrite $G_{nl}$ as its Jacobian linearization around the equilibrium point, plus a nonlinear remainder term.

### Lemma 3.1

If $G_{nl}$ satisfies Assumption 1. ‣ 3 Stabilizing Nonlinear Dynamical Systems ‣ Stabilizing Dynamical Systems via Policy Gradient Methods"), then all $\mathbf{x},\mathbf{u}$ for which ${{\|\mathbf{x}\|} + {\|\mathbf{u}\|}} \leq r_{nl}$,

where ${\|{f_{nl}{(\mathbf{x},\mathbf{u})}}\|} \leq {\beta_{nl}{({{\|\mathbf{x}\|}^{2} + {\|\mathbf{u}\|}^{2}})}}$, ${\|{{\nabla f_{nl}}{(\mathbf{x},\mathbf{u})}}\|} \leq {\beta_{nl}{({{\|\mathbf{x}\|} + {\|\mathbf{u}\|}})}}$, and where $(A_{jac},B_{jac})$ are the system's Jacobian linearization matrices defined in Eq. 1.2.

Rather than trying to directly understand the behavior of stabilization procedures on the nonlinear system, the key insight of our nonlinear analysis is that we can reason about the performance of a state-feedback controller on the nonlinear system via its behavior on the system's Jacobian linearization. In particular, the following lemma establishes how any controller which achieves finite discounted LQR cost for the Jacobian linearization is guaranteed to be exponentially stabilizing on the damped nonlinear system for initial states that are small enough. Throughout the remainder of this section, we define $J_{lin}{( \cdot \mid \gamma)}:=J_{lin}{( \cdot \mid \gamma,A_{jac},B_{jac})}$ as the LQR objective from Definition 2.1. ‣ 2 Stabilizing Linear Dynamical Systems ‣ Stabilizing Dynamical Systems via Policy Gradient Methods") where ${(A,B)} = {(A_{jac},B_{jac})}$.

### Lemma 3.2 (Restatement of Lemma B.2)

Suppose that $\mathcal{C}_{J} = {J_{lin}{({K \mid \gamma})}} < \infty$, then $K$ is $(\mathcal{C}_{J}^{1/2},{({4\mathcal{C}_{J}})}^{- 1})$ exponentially stable on the damped system $\sqrt{\gamma}G_{nl}$ over radius $r = {r_{nl}/{({\beta_{nl}\mathcal{C}_{J}^{3/2}})}}$.

The second main building block of our nonlinear analysis is the observation that if the dynamics are locally smooth around the equilibrium point, then by Lemma 3.1, decreasing the radius $r$ of the initial state distribution $\mathbf{x}_{0} \sim {r \cdot \mathcal{S}^{d_{x} - 1}}$ reduces the magnitude of the nonlinear remainder term $f_{nl}$. Hence, the nonlinear system smoothly approximates its Jacobian linearization. More precisely, we establish that the difference in gradients and costs between $J_{nl}{({K \mid {\gamma,r}})}$ and $J_{lin}{({K \mid \gamma})}$ decrease linearly with the radius $r$.

### Proposition 3.3

Assume ${J_{lin}{({K \mid \gamma})}} < \infty$. Then, for $P_{K,\gamma}$ defined as in Eq. 2.4:

If $r \leq \frac{r_{nl}}{2\beta_{nl}{\| P_{K,\gamma}\|}_{op}^{2}}$, then $\left| J_{nl}{(K \mid \gamma,r)} - J_{lin}{(K \mid \gamma)} \middle| \leq 8d_{x}\beta_{nl} \parallel P_{K,\gamma} \parallel_{op}^{4} \cdot r. \right.$

If $r \leq \frac{1}{12\beta_{nl}{\| P_{K,\gamma}\|}_{op}^{5/2}}$, then, $\parallel \nabla_{K}J_{nl}{(K \mid \gamma,r)} - \nabla_{K}J_{lin}{(K \mid \gamma)} \parallel_{F} \leq 48d_{x}\beta_{nl}{(1 + \parallel B \parallel_{op})} \parallel P_{K,\gamma} \parallel_{op}^{7} \cdot r$

Lastly, because policy gradients on linear dynamical systems is robust to inexact gradient queries, we show that for $r$ sufficiently small, running policy gradients on $J_{nl}$ converges to a controller which has performance close to the optimal controller for the LQR problem with dynamic matrices $(A_{jac},B_{jac})$. As noted previously, we can then use Lemma 3.2. ‣ 3 Stabilizing Nonlinear Dynamical Systems ‣ Stabilizing Dynamical Systems via Policy Gradient Methods") to translate the performance of the optimal LQR controller for the Jacobian linearization to an exponential stability guarantee for the nonlinear dynamics. Using these insights, we establish the following theorem regarding discount annealing for nonlinear dynamics.

### Theorem 2 (Nonlinear Systems)

Let $M_{nl}:={\max{\{{21tr\left\lbrack P_{\star} \right\rbrack},{J_{lin}{({K_{0} \mid \gamma_{0}})}}\}}}$. The following statements are true regarding the discount annealing algorithm for nonlinear dynamical systems when $r_{\star}$ is less than a fixed quantity that is ${poly}{({1/M_{nl}},{1/{\| A\|}_{op}},{1/{\| B\|}_{op}},{r_{nl}/\beta_{nl}})}$

Discount annealing returns a controller $\hat{K}$ which is $(\sqrt{2tr{\lbrack P_{\star}\rbrack}},{({8tr\left\lbrack P_{\star} \right\rbrack})}^{- 1})$-exponentially stable over a radius $r = {r_{nl}/{({8\beta_{nl}{tr}\left\lbrack P_{\star} \right\rbrack^{2}})}}$

If $\gamma_{0} < 1$, the algorithm is guaranteed to halt whenever $t$ is greater than $64tr\left\lbrack P_{\star} \right\rbrack^{4}{\log{({1/\gamma_{0}})}}$.

Furthermore, at each iteration $t$:

Policy gradients achieves the guarantee in Eq. 2.2 using only ${poly}{(M_{nl},{\| A\|}_{op},{\| B\|}_{op})}$ many queries to $\varepsilon\text{-}{\mathtt{G}\mathtt{r}\mathtt{a}\mathtt{d}}{( \cdot,J_{nl}{( \cdot \mid \gamma)})}$ as long as $\varepsilon$ is less than some fixed polynomial ${poly}{(M_{nl}^{- 1},{\| A\|}_{op}^{- 1},{\| B\|}_{op}^{- 1})}$.

Let $c_{0}$ denote a universal constant. With probability $1 - \delta$, the noisy random search algorithm (see Figure 2) returns a discount factor $\gamma^{\prime}$ satisfying Eq. 2.3 using at most ${c_{0} \cdot {tr}}\left\lbrack P_{\star} \right\rbrack^{4}{\log{({1/\delta})}}$ queries to $\varepsilon\text{-}{\mathtt{E}\mathtt{v}\mathtt{a}\mathtt{l}}{( \cdot,J_{nl}{( \cdot \mid \gamma,r_{\star})})}$ for $\varepsilon = d_{x}}$.

We note that while our theorem only guarantees that the controller is stabilizing around a polynomially small neighborhood of the equilibrium, in experiments, we find that the resulting controller successfully stabilizes the dynamics for a wide range of initial conditions. Relative to the case of linear systems where we leveraged the monotonicity of the LQR cost to search for discount factors using binary search, this monotonicity breaks down in the case of nonlinear systems and we instead analyze a random search algorithm to simplify the analysis.

## Experiments

In this section, we evaluate the ability of the discount annealing algorithm to stabilize a simulated nonlinear system. Specifically, we consider the familiar cart-pole, with $d_{x} = 4$ (positions and velocities of the cart and pole), and $d_{u} = 1$ (horizontal force applied to the cart). The goal is to stabilize the system with the pole in the unstable 'upright' equilibrium position. For further details, including the precise dynamics, see Section D.1. The system was simulated in discrete-time with a simple forward Euler discretization, i.e., $\mathbf{x}_{t + 1} = {\mathbf{x}_{t} + {T_{s}{\overset{˙}{\mathbf{x}}}_{t}}}$, where ${\overset{˙}{\mathbf{x}}}_{t}$ is given by the continuous time dynamics, and $T_{s} = 0.05$ (20Hz). Simulations were carried out in PyTorch and run on a single GPU.

Setup. The discounted annealing algorithm of Figure 1 was implemented as follows. In place of the true infinite horizon discounted cost $J_{nl}{({K \mid {\gamma,r}})}$ in Eq. C.4 we use a finite horizon, finite sample Monte Carlo approximation as described in Appendix C,

Here, ${J_{nl}^{(H)}{({K \mid {\gamma,\mathbf{x}}})}} = {{\sum_{j = 0}^{H - 1}{\mathbf{x}_{t}^{\top}Q\mathbf{x}_{t}}} + {\mathbf{u}_{t}^{\top}R\mathbf{u}_{t}}}$, is the length $H$, finite horizon cost of a controller $K$ in which the states evolve according to the $\sqrt{\gamma}$ damped dynamics from Eq. C.5 and $\mathbf{u}_{t} = {K\mathbf{x}_{t}}$. We used $N = 5000$ and $H = 1000$ in our experiments. For the cost function, we used $Q = {T_{s} \cdot I}$ and $R = T_{s}$. We compute unbiased approximations of the gradients using automatic differentiation on the finite horizon objective $J_{nl}^{(H)}$.

Table 1: Final region of attraction radius rroa as a function of the initial state radius r used during training (discount annealing). We report the [min, max] values of rroa over 5 independent trials. The optimal LQR policy for the linearized system achieved rroa = 0.703 when applied to the nonlinear system. We also synthesized an ℋ∞ optimal controller for the linearized dynamics, which achieved rroa = 0.506.

Instead of using SGD updates for policy gradients, we use Adam with a learning rate of $\eta = {0.01/r}$. Furthermore, we replace the policy gradient termination criteria in Step 2 (Eq. 2.2) by instead halting after a fixed number $({M = 200})$ of gradient descent steps. We wish to emphasize that the hyperparameters $(N,H,\eta,M)$ were not optimized for performance. In particular, for $r = 0.1$, we found that as few as $M = 40$ iterations of policy gradient and horizons as short as $H = 400$ were sufficient. Finally, we used an initial discount factor $\gamma_{0} = {0.9 \cdot {\| A_{jac}\|}_{2}^{- 2}}$, where $A_{jac}$ denotes the linearization of the (discrete-time) cart-pole about the vertical equilibrium.

Results. We now proceed to discuss the performance of the algorithm, focusing on three main properties of interest: i) the number of iterations of discount annealing required to find a stabilizing controller (that is, increase $\gamma_{t}$ to 1), ii) the maximum radius $r$ of the ball of initial conditions $\mathbf{x}_{0} \sim {r \cdot \mathcal{S}^{d_{x} - 1}}$ for which discount annealing succeeds at stabilizing the system, and iii) the radius $r_{\text{roa}}$ of the largest ball contained within the region of attraction (ROA) for the policy returned by discount annealing. Although the true ROA (the set of all initial conditions such that the closed-loop system converges asymptotically to the equilibrium point) is not necessarily shaped like a ball (as the system is more sensitive to perturbations in the position and velocity of the pole than the cart), we use the term region of attraction radius to refer to the radius of the largest ball contained in the ROA.

Concerning (i), discount annealing reliably returned a stabilizing policy in less than 9 iterations. Specifically, over 5 independent trials for each initial radius $r \in {\{ 0.1,0.3,0.5,0.7\}}$ (giving 20 independent trials, in total) the algorithm never required more than 9 iterations to return a stabilizing policy.

Concerning (ii), discount annealing reliably stabilized the system for $r \leq 0.7$. For $r \approx 0.75$, we observed trials in which the state of the damped system ($\gamma < 1$) diverged to infinity. For such a rollout, the gradient of the cost is not well-defined, and policy gradient is unable to improve the policy, which prevents discount annealing from finding a stabilizing policy.

Concerning (iii), in Table 1 we report the final radius $r_{\text{roa}}$ for the region of attraction of the final controller returned by discount annealing as a function of the training radius $r$. We make the following observations. Foremost, the policy returned by discount annealing extends the radius of the ROA beyond the radius used during training, i.e. $r_{\text{roa}} > r$. Moreover, for each $r >.1$, the $r_{\text{roa}}$ achieved by discount annealing is greater than the $r_{\text{roa}} = 0.703$ achieved by the exact optimal LQR controller *and* the $r_{\text{roa}} = 0.506$ achieved by the exact optimal $\mathcal{H}_{\infty}$ controller for the system's Jacobian linearization (see Table 1). (The $\mathcal{H}_{\infty}$ optimal controller mitigates the effect of worst-case additive state disturbances on the cost; cf. Section D.2 for details).

One may hypothesize that this is due to the fact that discount annealing directly operates on the true nonlinear dynamics whereas the other baselines (LQR and $\mathcal{H}_{\infty}$ control), find the optimal controller for an idealized linearization of the dynamics. Indeed, there is evidence to support this hypothesis. In Figure 3 presented in Appendix D, we plot the error ${\|{{K_{\text{pg}}^{\star}{(\gamma_{t})}} - {K_{\text{lin}}^{\star}{(\gamma_{t})}}}\|}_{F}$ between the policy $K_{\text{pg}}^{\star}{(\gamma_{t})}$ returned by policy gradients, and the optimal LQR policy $K_{\text{lin}}^{\star}{(\gamma_{t})}$ for the (damped) linearized system, as a function of the discount factor $\gamma_{t}$ used in each iteration of the discount annealing algorithm. For small training radius, such as $r = 0.05$, ${K_{\text{pg}}^{\star}{(\gamma_{t})}} \approx {K_{\text{lin}}^{\star}{(\gamma_{t})}}$ for all $\gamma_{t}$. However, for larger radii (i.e $r = 0.7$), we see that ${\|{{K_{\text{pg}}^{\star}{(\gamma_{t})}} - {K_{\text{lin}}^{\star}{(\gamma_{t})}}}\|}_{F}$ steadily increases as $\gamma_{t}$ increases.

That is, as discount annealing increases the discount factor $\gamma$ and the closed-loop trajectories explore regions of the state space where the dynamics are increasingly nonlinear, $K_{\text{pg}}^{\star}$ begins to diverge from $K_{\text{lin}}^{\star}$. Moreover, at the conclusion of discount annealing $K_{\text{pg}}^{\star}{}$ achieves a lower cost, namely \[15.2, 15.4\] vs \[16.5, 16.8\] (here $\lbrack a,b\rbrack$ denotes \[$\min$, $\max$\] over 5 trials) and larger $r_{\text{roa}}$, namely \[0.769, 0.777\] vs \[0.702, 0.703\], than $K_{\text{lin}}^{\star}{}$, suggesting that the method has indeed adapted to the nonlinearity of the system. Similar observations as to the behavior of controllers fine tuned via policy gradient methods are predicted by the theoretical results from Qu et al..

## Discussion

This works illustrates how one can provably stabilize a broad class of dynamical systems via a simple model-free procedure based off policy gradients. In line with the simplicity and flexibility that have made model-free methods so popular in practice, our algorithm works under relatively weak assumptions and with little knowledge of the underlying dynamics. Furthermore, we solve an open problem from previous work and take a step towards placing model-free methods on more solid theoretical footing. We believe that our results raise a number of interesting questions and directions for future work.

In particular, our theoretical analysis states that discount annealing returns a controller whose stability properties are similar to those of the optimal LQR controller for the system's Jacobian linearization. We were therefore quite surprised when in experiments, the resulting controller had a significantly better radius of attraction than the exact optimal LQR and $\mathcal{H}_{\infty}$ controllers for the linearization of the dynamics. It is an interesting and important direction for future work to gain a better understanding of exactly when and how model-free procedures are adaptive to the nonlinearities of the system and improve upon these model-based baselines. Furthermore, for our analysis of nonlinear systems, we require access to damped system trajectories. It would be valuable to understand whether this is indeed necessary or whether our analysis could be extended to work without access to damped trajectories.

As a final note, in this work we reduce the problem of stabilizing dynamical systems to running policy gradients on a discounted LQR objective. This choice of reducing to LQR was in part made for simplicity to leverage previous analyses. However, it is possible that overall performance could be improved if rather than reducing to LQR, we instead attempted to run a model-free method that directly tries to optimize a robust control objective (which explicitly deals with uncertainty in the system dynamics). We believe that understanding these tradeoffs in objectives and their relevant sample complexities is an interesting avenue for future inquiry.
