## Introduction

As a cornerstone of modern control theory, the linear quadratic regulator (LQR) problem has been the benchmark for data-driven control methods that seek to design a controller from raw system data. The manifold approaches to data-driven control can be broadly categorized as indirect (when identifying a dynamical model followed by model-based control design) versus direct (when bypassing the identification step). The use of direct data-driven control is usually motivated when the dynamical model is difficult to establish, or is too complex for model-based control design. As an end-to-end approach, the direct methods are conceptually simple and easy to implement in practice.

A representative instance of direct data-driven control is policy optimization (PO), an essential approach for applications of reinforcement learning (RL). As an iterative method, PO directly searches over the policy space to optimize a performance metric of interest. Based on zeroth-order optimization techniques, it uses multiple system trajectories to estimate the policy gradient. There has been a resurgent interest in studying theoretical properties of PO on the LQR problem such as convergence and sample complexity; see e.g., and the comprehensive survey. Even though global convergence has been shown for the nonconvex PO problem by a gradient dominance property, there exists a considerable gap in the sample complexity between PO and indirect methods, which have proved themselves to be more sample-efficient for solving the LQR problem. This gap is due to the exploration or trial-and-error nature of RL, or more specifically, that the cost used for gradient estimate can only be evaluated after a whole trajectory is observed. Thus, the existing PO methods require numerous system trajectories to find an optimal policy, even in the simplest LQR setting.

Recent years have witnessed an emerging line of direct methods inspired by the Fundamental Lemma, which states that the behavior of a linear time-invariant (LTI) system can be characterized by the range space of raw data matrices. This result implies a non-parametric representation of LTI systems, giving rise to a notable implicit design called data-enabled predictive control (DeePC), which has seen many successful implementations in different practical scenarios. The fundamental lemma has also been utilized to solve various explicit control design and analysis problems. In particular, it has been shown in that using subspace relations, the closed-loop LTI system can be parameterized by input-state data, leading to a data-based convex reformulation of the LQR problem. Compared with PO, this approach is significantly more sample-efficient as it only requires a batch of persistently exciting (PE) data. Indeed, the PE condition is equivalent to identifiability for LTI systems and should be a minimal assumption for most control design problems, e.g., the LQR problem. There have been many recent works leveraging regularization methods to promote certainty-equivalence and robustness of the LQR, and to bridge behavioral-based direct and indirect methods. All these methods use only a small batch of PE data compared to data-hungry zeroth-order PO methods. This leads to a natural question: does there exist a data-efficient PO method for solving the LQR problem?

In this paper, we provide an affirmative answer to the above question. By leveraging the data-driven closed-loop parameterization, we propose an iterative method called data-enabled policy optimization (DeePO) to solve the LQR problem. Instead of estimating the policy gradient from the cost of observed trajectories, we show that after a change of optimization variables, the gradient can be directly characterized from a batch of PE data. Even though the resulting optimization problem is nonconvex, it can be parameterized as a data-based convex program. By exploiting this relation and using a recent PO result, we further show that the LQR cost is projected gradient dominated, while it is only gradient dominated in. By establishing that the cost is also locally smooth, we show that the projected gradient method converges to the global optimum. We also investigate how regularization affects the convergence of DeePO. In particular, we show that the certainty-equivalence regularizer leads to an implicit regularization property, meaning that the DeePO algorithm without regularization behaves as if it is regularized. This property has been advocated as an important feature of gradient-based methods for solving many nonconvex problems. Finally, we perform a numerical case study to validate our theoretical results. We are hopeful that the discovered DeePO method with significantly relaxed data requirements offers a possible path towards direct adaptive LQR control.

The rest of this paper is organized as follows. In Section II, we revisit the LQR problem and recapitulate the data-driven LQR formulation. In Section III, we propose the DeePO method to iteratively solve the LQR problem and show its global convergence. Section IV studies the effects of two regularizers on the convergence of DeePO. Section V uses a numerical example to validate our main results. Conclusion and future work in Section VI complete this paper.

Notation. We use $I_{n}$ to denote the $n$-by-$n$ identity matrix. We use $\underset{¯}{\sigma}{( \cdot )}$ to denote the minimal singular value of a matrix. We use $\parallel \cdot \parallel$ to denote the $2$-norm of a vector or a matrix, and $\parallel \cdot \parallel_{F}$ the Frobenius norm. We use $\rho{( \cdot )}$ to denote the spectral radius of a square matrix. We use $\text{poly}{( \cdot )}$ to denote a polynomial function. We use $\dagger$ to denote the right inverse of a full row rank matrix.

## Problem Formulation

In this section, we first revisit the model-based LQR problem. By recapitulating its direct data-driven formulation from, we then propose our PO reformulation.

### II-A The Model-based LQR problem

Consider a discrete-time LTI system

where ${x{(t)}} \in {\mathbb{R}}^{n}$ and ${u{(t)}} \in {\mathbb{R}}^{m}$ are the state and control input, respectively. We assume that $(A,B)$ are controllable.

The LQR problem is phrased as finding a state-feedback gain $K \in {\mathbb{R}}^{m \times n}$ to minimize the quadratic cost

where ${Q \succ 0},{R \succ 0}$ are penalty matrices, and $\{{x{(t)}},{u{(t)}}\}$ is the trajectory following and ${u{(t)}} = {Kx{(t)}}$ starting from the initial state $x{}$. The distribution $\mathcal{D}$ of $x{}$ satisfies ${{\mathbb{E}}{\lbrack{x{}}\rbrack}} = 0$ and ${{\mathbb{E}}{\lbrack{x{}x{}^{\top}}\rbrack}} = I_{n}$. It is well-known that the unique optimal gain to is

where $P^{\ast}$ is the unique positive semi-definite solution to the algebraic Riccati equation

We aim to solve the LQR problem in a direct data-driven approach when $(A,B)$ are unknown, but we assume the access to a $T$-length dataset of states and control inputs.

### II-B Direct data-driven formulation

Define the offline data matrices

which satisfy the system dynamics

Throughout the paper, we assume that the following block matrix of input and state data

has full row rank

i.e., the information in the data is sufficiently rich. This condition is necessary for identifying $(A,B)$ from data and for solving the data-driven LQR problem. As shown in, it can be ensured provided that the input data $U_{-}$ is PE of order $n + 1$. Note that the columns of $(X_{-},U_{-},X_{+})$ are not necessarily consecutive data samples. In fact, they could be from independent or multiple averaged experiments as long as they satisfy and.

Under the rank condition, there exists a matrix $G \in {\mathbb{R}}^{T \times n}$ that satisfies

for any given $K$. That is, $K$ can be parameterized by $K = {U_{-}G}$ where $G$ satisfies a linear constraint ${X_{-}G} = I_{n}$. Then, the closed-loop matrix can be expressed in a data-driven fashion as

leading to the following closed-loop system

Furthermore, the LQR problem becomes

Here, $J{(G)}$ is the LQR cost following and ${u{(t)}} = {U_{-}Gx{(t)}}$, and $\mathcal{S}_{G}$ is the feasible set. In contrast to the model-based LQR, the problem is characterized by raw data matrices. Though can be reformulated as a semi-definite program (SDP) using techniques from, it is computationally challenging to solve for a large data size.

In this paper, we take an iterative PO perspective to solve viewing $G$ as the optimization matrix. We aim to design a gradient-based method to find an optimal $G$ while maintaining feasibility, and recover the control from as $K = {U_{-}G}$. Since is a challenging constrained nonconvex problem, we leverage a novel convex parameterization to establish the global convergence.

## Data-enabled policy optimization

In this section, we first present our novel PO method for solving. Then, we propose a convex parameterization of to derive the projected gradient dominance property of $J{(G)}$. By establishing that $J{(G)}$ is locally smooth over any sublevel set, we are able to show the global convergence of our method.

### III-A Data-enabled policy optimization to solve (7)

For $G \in \mathcal{S}_{G}$, the cost $J{(G)}$ is finite and has the following closed-form expressions

where $P_{G}$ satisfies the Lyapunov equation

and $\Sigma_{G}:={{\mathbb{E}}_{{x{}} \sim \mathcal{D}}{\lbrack{\sum_{t = 0}^{\infty}{x{(t)}x{(t)}^{\top}}}\rbrack}}$ is the state covariance matrix of the closed-loop system satisfying

We have the following gradient expression for $J{(G)}$.

### Lemma 1

For $G \in \mathcal{S}_{G}$, the gradient of $J{(G)}$ is

with $E_{G}:={{({{U_{-}^{\top}RU_{-}} + {X_{+}^{\top}P_{G}X_{+}}})}G}$.

### Proof

The proof follows from standard matrix analysis and is similar to that of \[4, Lemma 1\]. ∎

The expression of ${\nabla J}{(G)}$ is data-driven since both $E_{G}$ and $\Sigma_{G}$ can be computed using raw data matrices under the rank condition.

The feasible set $\mathcal{S}_{G}$ contains a linear constraint ${X_{-}G} = I_{n}$, which motivates the use of projected gradient methods to ensure feasibility. Define the nullspace of $X_{-}$ as

and the projection operator $\Pi_{X_{-}}:={I_{T} - {X_{-}^{\dagger}X_{-}}}$ onto $\mathcal{N}{(X_{-})}$. The projected gradient update is then given by

where $\eta \geq 0$ is the stepsize. We refer to this method as data-enabled policy optimization (DeePO) since the update (10 ‣ III Data-enabled policy optimization ‣ Data-enabled Policy Optimization for the Linear Quadratic Regulator")) can be efficiently computed by raw data matrices, and the control can be recovered from as $K = {U_{-}G}$. As an iterative search method, the initial policy $G^{0}$ requires to satisfy $G^{0} \in \mathcal{S}_{G}$.

Due to non-convexity of both the objective $J{(G)}$ and the constraint $\mathcal{S}_{G}$, it is challenging to provide global convergence guarantees for DeePO. Moreover, an optimal solution to is not unique. In fact, it has been shown in \[20, Lemma 2.1\] that the solution set is

which contains a considerable nullspace. Nevertheless, based on a recent work that proves optimality via convex parameterization, we are able to show a projected gradient dominance property of $J{(G)}$.

### III-B Optimality via a convex parameterization

We first relate to a convex parameterization via a change of variables $G = {L\Sigma^{- 1}}$ as

Let $\mathcal{S}$ be its feasible set. The equivalence between the two problems and are established below.

### Lemma 2

For any ${(L,\Sigma)} \in \mathcal{S}$, $\Sigma$ is invertible and ${L\Sigma^{- 1}} \in \mathcal{S}_{G}$. Moreover, for $G \in \mathcal{S}_{G}$ it holds that

### Proof

Applying the Schur complement to the LMI constraint in yields $\Sigma \succ 0$ and

Due to non-singularity of $\Sigma$, let $G = {L\Sigma^{- 1}}$. Then, a substitution of $L = {G\Sigma}$ into the above inequality yields

Thus, $X_{+}G$ is stable, i.e., ${\rho{({X_{+}G})}} < 1$. Since the first constraint of implies ${X_{-}G} = {X_{-}L\Sigma^{- 1}} = {\Sigma\Sigma^{- 1}} = I_{n}$, it holds that $G = {L\Sigma^{- 1}} \in \mathcal{S}_{G}$.

Next, we prove the second statement. Using the constraint $G = {L\Sigma^{- 1}}$ and the Schur complement, the right-hand side of becomes

Let $\Sigma{(\Theta)}$ be the unique positive definite solution of the Lyapunov equation

with $\Theta \succeq I_{n}$. By monotonicity of $\Sigma{(\Theta)}$, we have ${\Sigma{(\Theta)}} \succeq {\Sigma{(I_{n})}}$. Since ${Q + {G^{\top}U_{-}^{\top}RU_{-}G}} \succ 0$, the minimum of is attained at $\Sigma{(I_{n})}$, which is $\text{Tr}{({{({Q + {G^{\top}U_{-}^{\top}RU_{-}G}})}\Sigma{(I_{n})}})}$ with ${X_{-}G} = I_{n}$. This is the definition of $J{(G)}$ in (8 ‣ III Data-enabled policy optimization ‣ Data-enabled Policy Optimization for the Linear Quadratic Regulator")). ∎

In the following lemma, we show the convexity of the parameterization.

### Lemma 3

The feasible set $\mathcal{S}$ of is convex in $(L,\Sigma)$, and $f{(L,\Sigma)}$ is differentiable over an open domain that contains $\mathcal{S}$. Moreover, $f{(L,\Sigma)}$ is convex over $\mathcal{S}$.

### Proof

Since the constraints in are linear in $(L,\Sigma)$, the feasible set $\mathcal{S}$ is convex. Clearly, $f{(L,\Sigma)}$ is differential over $\mathcal{S}$. Define the Hessian operator acting on the direction $(\overset{\sim}{L},\overset{\sim}{\Sigma})$:

which by standard matrix analysis can be written as

Thus, $f$ is convex over $\mathcal{S}$. ∎

We now formally define the gradient dominance property.

### Definition 1

A differentiable function ${g{(x)}}:{{\mathbb{R}}^{n}\rightarrow{\mathbb{R}}}$ with a finite global minimum $g^{\ast}$ is gradient dominated of degree $p$ over a set $\mathcal{X} \subseteq {\text{dom}{(g)}}$ if

The gradient dominance property means that all the stationary points are optimal. Moreover, the convergence rate of gradient-based methods usually depends on the values of the degree $p$. Particularly, for smooth objective function $p = 1$ leads to a sublinear rate and $p = 2$ leads to a linear rate.

Equipped with Lemmas 2 and 3, we apply \[22, Theorem 1\] to show the gradient dominance property of $J{(G)}$ over any sublevel set ${S_{G}{(a)}}:=\left. \{{G \in {\mathbb{R}}^{T \times n}} \middle| {{J{(G)}} \leq a}\} \right.$ with $a > 0$.

### Lemma 4 (Projected gradient dominance of degree 1)

For $G \in {\mathcal{S}_{G}{(a)}}$, there exists ${\mu{(a)}} > 0$ such that

where $J^{\ast}$ is the optimal LQR cost to.

### Proof

By Lemmas 2 and 3, the data-driven LQR problem and its convex parameterization satisfy the assumptions required to apply \[22, Theorem 1\]. Then, there exists ${c{(a)}} > 0$ and a direction $V \in {\mathcal{N}{(X_{-})}}$ with ${\| V\|}_{F} = 1$ in the descent cone of $\mathcal{S}_{G}{(a)}$ such that

where $J^{\prime}{(G)}{\lbrack V\rbrack}$ denotes the derivative along the direction $V$. Let $V^{\prime} = {{\Pi_{X_{-}}{\nabla J}{(G)}}/{\|{\Pi_{X_{-}}{\nabla J}{(G)}}\|}_{F}}$ be the normalized projected gradient. Then, we have ${J^{\prime}{(G)}{\lbrack V^{\prime}\rbrack}} \leq {J^{\prime}{(G)}{\lbrack V\rbrack}}$ since both $V$ and $V^{\prime}$ are in $\mathcal{N}{(X_{-})}$, and $V^{\prime}$ is the direction of the projection of the gradient. Thus, we have ${{J{(G)}} - J^{\ast}} \leq {\mu{(a)}{\|{\Pi_{X_{-}}{\nabla J}{(G)}}\|}}$ with ${\mu{(a)}} = {{1/c}{(a)}}$.

Next, we derive an explicit upper bound of $\mu{(a)}$ over $G \in {\mathcal{S}_{G}{(a)}}$. By \[28, Theorem 1\], $c{(a)}$ is given by

where $(L^{\ast},\Sigma^{\ast})$ is an optimal point and ${(L,\Sigma)} = {{\arg{\min_{L^{\prime},\Sigma^{\prime}}f}}{(L^{\prime},\Sigma^{\prime})}}$ subject to ${{(L^{\prime},\Sigma^{\prime})} \in \mathcal{S}},{{L^{\prime}{(\Sigma^{\prime})}^{- 1}} = G}$. We now provide upper bounds for ${{\underset{¯}{\sigma}}^{- 1}{(\Sigma)}},{\| L\|}_{F},{\|\Sigma\|}_{F}$. Since ${\underset{¯}{\sigma}{(\Sigma)}} \geq 1$, it holds ${{\underset{¯}{\sigma}}^{- 1}{(\Sigma)}} \leq 1$. The sublevel set gives ${\text{Tr}{\{{Q\Sigma}\}}} \leq a$, and hence ${\|\Sigma\|}_{F} \leq {{a/\underset{¯}{\sigma}}{(Q)}}$. Since

an upper bound of ${\| L\|}_{F}$ is given by

Those bounds are also true for $L^{\ast},\Sigma^{\ast}$. Furthermore, we can provide an upper bound of $\mu{(a)}$ as

The proof is completed. ∎

In contrast to the existing literature on PO for the LQR, the cost $J{(G)}$ here is projected gradient dominated, meaning that $G$ is optimal if the projected gradient $\Pi_{X_{-}}{\nabla J}{(G)}$ is equal to zero. By using Lemma 4 ‣ III-B Optimality via a convex parameterization ‣ III Data-enabled policy optimization ‣ Data-enabled Policy Optimization for the Linear Quadratic Regulator"), we next show global convergence of the projected gradient descent in (10 ‣ III Data-enabled policy optimization ‣ Data-enabled Policy Optimization for the Linear Quadratic Regulator")).

### III-C Global convergence of DeePO

We first prove the smoothness of $J{(G)}$. Since $J{(G)}$ tends extremely to infinity as $G$ approaches the boundary $\partial\mathcal{S}_{G}$, we can only show that $J{(G)}$ is locally smooth over any sublevel set. Define the Hessian acting on the direction $Z \in {\mathbb{R}}^{T \times n}$ as ${{{\nabla^{2}J}{(G)}{\lbrack Z,Z\rbrack}}:=\left. {\frac{d^{2}}{dt^{2}}J{({G + {tZ}})}} \right|_{t = 0}},$ and the directional derivative of $P_{G}$ as ${{P_{G}^{\prime}{\lbrack Z\rbrack}}:=\left. {\frac{d}{dt}P_{G + {tZ}}} \right|_{t = 0}}.$ Then, we have the following closed-form expression for the Hessian.

### Lemma 5

For $G \in \mathcal{S}_{G}$ and a feasible direction $Z \in {\mathbb{R}}^{T \times n}$, the Hessian of $J{(G)}$ is characterized by

where ${P_{G}^{\prime}{\lbrack Z\rbrack}} = {\sum_{i = 0}^{\infty}{{({G^{\top}X_{+}^{\top}})}^{i}{({{Z^{\top}E_{G}} + {E_{G}^{\top}Z}})}{({X_{+}G})}^{i}}}$.

### Proof

The proof follows from standard matrix analysis and is omitted due to space limitation. ∎

Define ${\|{{\nabla^{2}J}{(G)}}\|}:={\sup_{{\| Z\|}_{F} = 1}\left| {{\nabla^{2}J}{(G)}{\lbrack Z,Z\rbrack}} \right|}$. We show an upper bound for $\|{{\nabla^{2}J}{(G)}}\|$ over a sublevel set.

### Lemma 6 (Local smoothness)

For $G \in {\mathcal{S}_{G}{(a)}}$, it holds

where $l{(a)}$ is the smoothness constant of $J{(G)}$ over $\mathcal{S}_{G}{(a)}$. That is, for any ${G,G^{\prime}} \in {\mathcal{S}_{G}{(a)}}$ satisfying ${{G + {\delta{({G^{\prime} - G})}}} \in {\mathcal{S}_{G}{(a)}}},{{\forall\delta} \in {\lbrack 0,1\rbrack}}$, the following inequality holds

The proof is technical and provided in Appendix A.

Under the gradient dominance property of degree 1 in Lemma 4 ‣ III-B Optimality via a convex parameterization ‣ III Data-enabled policy optimization ‣ Data-enabled Policy Optimization for the Linear Quadratic Regulator") and the local smoothness in Lemma 6 ‣ III-C Global convergence of DeePO ‣ III Data-enabled policy optimization ‣ Data-enabled Policy Optimization for the Linear Quadratic Regulator"), we now show the global sublinear convergence of DeePO. The key is to select an appropriate stepsize such that the policy sequence is feasible and stays in the sublevel set associated with the initial policy $G^{0} \in \mathcal{S}_{G}$. For simplicity, let $\mu_{0}$ and $l_{0}$ denote the projected gradient dominance and smoothness constants of $J{(G)}$ over $\mathcal{S}_{G}{({J{(G^{0})}})}$, respectively. We present our convergence result in the following theorem.

### Theorem 1 (Global convergence)

For $G^{0} \in \mathcal{S}_{G}$ and a stepsize $\eta \in {(0,{1/l_{0}}\rbrack}$, the update (10 ‣ III Data-enabled policy optimization ‣ Data-enabled Policy Optimization for the Linear Quadratic Regulator")) leads to ${G^{k} \in {\mathcal{S}_{G}{({J{(G^{0})}})}}},{{\forall k} \in {\mathbb{N}}}$. Moreover, for any $\epsilon > 0$ and

the update (10 ‣ III Data-enabled policy optimization ‣ Data-enabled Policy Optimization for the Linear Quadratic Regulator")) enjoys the following performance bound

### Proof

Define $G_{\eta}:={G - {\eta\Pi_{X_{-}}{\nabla J}{(G)}}}$. We first show that for a non-optimal $G \in {\mathcal{S}_{G}{(a)}}$ and any $\eta \in {\lbrack 0,{{1/l}{(a)}}\rbrack}$, it holds $G_{\eta} \in {\mathcal{S}_{G}{(a)}}$.

Define ${\mathcal{S}_{G}^{o}{(a)}}:=\left. \{{G \in \mathcal{S}_{G}} \middle| {{J{(G)}} < a}\} \right.$, and its complement as ${({\mathcal{S}_{G}^{o}{(a)}})}^{c}$, which is closed. By Lemma 6 ‣ III-C Global convergence of DeePO ‣ III Data-enabled policy optimization ‣ Data-enabled Policy Optimization for the Linear Quadratic Regulator"), given $\phi \in {}$, there exists $b > 0$ such that ${\|{{\nabla^{2}J}{(G)}}\|} \leq {{({1 + \phi})}l{(a)}}$ for $G \in {\mathcal{S}_{G}{({a + b})}}$. Clearly, ${{\mathcal{S}_{G}{(a)}} \cap {({\mathcal{S}_{G}^{o}{({a + b})}})}^{c}} = \varnothing$. Then, the distance between them $d:=\inf{\{ \parallel G^{\prime} - G \parallel,\forall G \in \mathcal{S}_{G}{(a)},G^{\prime} \in {(\mathcal{S}_{G}^{o}{(a + b)})}^{c}\}}$ is positive.

Let $\overline{N} \in {\mathbb{N}}_{+}$ be large enough such that ${2/{({\overline{N}{({1 + \phi})}l{(a)}})}} < {d/{\|{\Pi_{X_{-}}{\nabla J}{(G)}}\|}}$, which is well-defined since $G$ is not optimal. Define a stepsize $\tau \in {\lbrack 0,{2/{({\overline{N}{({1 + \phi})}l{(a)}})}}\rbrack}$. Since $\tau < {d/{\|{\Pi_{X_{-}}{\nabla J}{(G)}}\|}}$, we have ${\|{G_{\tau} - G}\|} < d$, i.e., $G_{\tau} \in {\mathcal{S}_{G}{({a + b})}}$. Thus, we can apply Lemma 6 ‣ III-C Global convergence of DeePO ‣ III Data-enabled policy optimization ‣ Data-enabled Policy Optimization for the Linear Quadratic Regulator") over $\mathcal{S}_{G}{({a + b})}$ to show

where the last inequality follows from $\tau \leq {{2/{({1 + \phi})}}l{(a)}}$. This implies that the segment between $G$ and $G_{\tau}$ is contained in $\mathcal{S}_{G}{(a)}$. It is also clear that $G_{2\tau} \in {\mathcal{S}_{G}{({a + b})}}$ since ${\|{G_{2\tau} - G_{\tau}}\|} < d$. Then, we can use induction to show that the segment between $G$ and $G_{N\tau}$ for $N \in {\mathbb{N}}_{+}$ is in $\mathcal{S}_{G}{(a)}$ as long as ${N\tau} \leq {{2/{({1 + \phi})}}l{(a)}}$. Since $\phi \in {}$, we let $\eta \leq {{1/l}{(a)}}$ to ensure the segment between $G$ and $G_{\eta}$ to be contained in $\mathcal{S}_{G}{(a)}$.

Then, a simple induction leads to that for $\eta \in {\lbrack 0,{1/l_{0}}\rbrack}$, the update (10 ‣ III Data-enabled policy optimization ‣ Data-enabled Policy Optimization for the Linear Quadratic Regulator")) satisfies ${G^{k} \in {\mathcal{S}_{G}{({J{(G^{0})}})}}},{{\forall k} \in {\mathbb{N}}}$. Moreover, the cost satisfies

Using Lemma 4 ‣ III-B Optimality via a convex parameterization ‣ III Data-enabled policy optimization ‣ Data-enabled Policy Optimization for the Linear Quadratic Regulator") and subtracting $J^{\ast}$ in both sides yields

Let $e^{k} = {{J{(G^{k})}} - J^{\ast}}$. Dividing by $e^{k}e^{k + 1}$ in both sides and noting $e^{k + 1} \leq e^{k}$ leads to

Summing up both sides over $0,1,\ldots,{k - 1}$ and using telescopic cancellation yields that

Letting the right-hand side of the above inequality equal $\epsilon$ and solving $k$ yields (15 ‣ III-C Global convergence of DeePO ‣ III Data-enabled policy optimization ‣ Data-enabled Policy Optimization for the Linear Quadratic Regulator")) under $\eta \in {(0,{1/l_{0}}\rbrack}$. ∎

We compare with the traditional PO for the LQR. Their approach relies on a zeroth-order estimate of the policy gradient, which inevitably requires numerous system trajectories to approximate the cost. In sharp contrast, DeePO directly computes the gradient from a batch of raw data matrices based on a data-based representation of the closed-loop system. This remarkable feature enables DeePO to work with only a small set of PE data. Moreover, the state-of-the-art sample complexity (in terms of number of sampled trajectories, the length of which can be very long) of PO in is $\mathcal{O}{({\log{({1/\epsilon})}})}$, while our sample complexity (in terms of number of state-input pairs) is independent of $\epsilon$. Even though both two approaches achieve global convergence (albeit with vastly different amounts of data), DeePO is more flexible as it is compatible with regularization methods used to enhance the robustness to noisy data, which will be shown in the next section. To the best of our knowledge, there are no robustifying regularization methods that have been applied to the PO method for the LQR problem.

## DeePO for the regularized LQR

For the direct data-driven LQR formulation, regularization plays an important role in promoting certainty-equivalence and robust stability when the data is corrupted with noise. This section investigates how regularization affects the convergence of DeePO.

### IV-A Certainty-equivalence regularizer

Consider the regularized LQR problem

where $\lambda \geq 0$ is a user-defined constant and $\Pi_{D_{-}}:={I - {D_{-}^{\dagger}D_{-}}}$ is the projection matrix onto the nullspace of $D_{-}$. For the noiseless data $(X_{-},U_{-},X_{+})$ here, the orthogonality regularizer in does not change the optimal cost but only singles out a solution $G^{\ast}$ satisfying ${\Pi_{D_{-}}G^{\ast}} = 0$ from the solution set in (11 ‣ III Data-enabled policy optimization ‣ Data-enabled Policy Optimization for the Linear Quadratic Regulator")). When the data is corrupted with noises, it promotes certainty-equivalence, i.e., when $\lambda$ tends to infinity the solution of coincides with that of indirect data-driven control with an underlying maximum likelihood system identification attenuating the effect of noise; we refer interested readers to \[20, Section III\] for more discussions.

Note that we have added the weighting $\Sigma_{G}^{1/2}$ to the regularizer (c.f. \[20, \]) to make it compatible with the convex parameterization. As a result, can be formulated with ${L\Sigma^{- 1}} = G$ as the following convex problem

Comparing with, we see that $f_{\lambda}{(L,\Sigma)}$ upon amounts to $f{(L,\Sigma)}$ adding a convex regularizer, and hence $f_{\lambda}{(L,\Sigma)}$ is convex. Indeed, by standard matrix analysis, its Hessian acting on the direction $(\overset{\sim}{L},\overset{\sim}{\Sigma})$ satisfies

Moreover, following analogous arguments as in Section III, $J_{\lambda}{(G)}$ can also be shown to be locally smooth. Based on previous analysis, the projected gradient update

converges to the optimal solution of under a proper stepsize selection.

### IV-B Robustness-promoting regularizer

Regularization can also be used to enhance robust stability. Consider the following regularized LQR problem

where $\gamma \geq 0$ is a user-defined constant. To see why it promotes the robust stability for noisy data, we note that the state covariance matrix is given by

Thus, a small $\text{Tr}{\{{G\Sigma_{G}G^{\top}}\}}$ can reduce the effect of noises in $X_{+}$. Different from the certainty-equivalence regularization, the regularizer in bias the LQR solution even when the data is noiseless, reflecting a trade-off between performance and robustness.

The problem can be formulated with ${L\Sigma^{- 1}} = G$ as

Clearly, $f_{\lambda}{(L,\Sigma)}$ is also convex since

By analogous reasoning and combining the smoothness of the regularizer, the projected gradient update

converges to the optimal solution of under a proper stepsize selection.

### IV-C Implicit regularization

Apart from the convergence, we observe an interesting implicit regularization property of the certainty-equivalence regularized LQR problem formally defined below.

### Definition 2 (Implicit regularization)

For the regularized LQR problem, suppose that a convergent algorithm generates a sequence of $\{ G^{k}\}$. If $G^{\infty}:={\lim\limits_{k\rightarrow\infty}G^{k}}$ satisfies ${\Pi_{D_{-}}G^{\infty}} = 0$, then the algorithm is called regularized; If it is regularized with $\lambda = 0$, then it is called implicitly regularized.

The concept of implicit regularization has been adopted in many recent works on nonconvex optimization, including deep learning, matrix factorization, and also PO for robust LQR problems. As its name suggests, it means that the algorithm without regularization behaves as if it is regularized. Note that implicit regularization is a property of a certain algorithm for solving a certain nonconvex problem. In the following theorem, we specify the conditions for the update to be implicitly regularized for problem.

Figure 1: Supspace relations among 𝒩 (D−), ΠX− ∇J (G), and G*.

### Theorem 2 (Implicit regularization)

Consider with $\lambda = 0$ and suppose that $G^{0}$ satisfies ${\Pi_{D_{-}}G^{0}} = 0$. Then, the update leads to ${{\Pi_{D_{-}}G^{k}} = 0},{k \in {\{ 0,1,\ldots\}}}$.

### Proof

Since $\lambda = 0$, it suffices to show that $\Pi_{X_{-}}{\nabla J}{(G)}$ is orthogonal to the nullspace of $D_{-}$.

By using Lemma 1 ‣ III Data-enabled policy optimization ‣ Data-enabled Policy Optimization for the Linear Quadratic Regulator"), the gradient of $J{(G)}$ is written as

We also have the following observation

Thus, $\Pi_{X_{-}}{\nabla J}{(G)}$ is in the range space of $D_{-} = \begin{bmatrix}
\end{bmatrix}^{\top}$, and hence ${{\Pi_{D_{-}}\Pi_{X_{-}}{\nabla J}{(G)}} = 0}.$ The update further leads to ${\Pi_{D_{-}}G^{k + 1}} = {{\Pi_{D_{-}}G^{k}} - {\eta\Pi_{D_{-}}\Pi_{X_{-}}{\nabla J}{(G^{k})}}} = {\Pi_{D_{-}}G^{k}} = 0$. ∎

By Theorem 2 ‣ IV-C Implicit regularization ‣ IV DeePO for the regularized LQR ‣ Data-enabled Policy Optimization for the Linear Quadratic Regulator"), a sufficient condition for implicit regularization is

provided with a stabilizing policy $K^{0}$. Theorem 2 ‣ IV-C Implicit regularization ‣ IV DeePO for the regularized LQR ‣ Data-enabled Policy Optimization for the Linear Quadratic Regulator") also helps understand the optimization landscape of DeePO. Fig. 1 illustrates the relations among the nullspace $\mathcal{N}{(D_{-})}$, the projected gradient, and an optimal solution $G^{\ast}$. Since $\Pi_{X_{-}}{\nabla J}{(G)}$ is orthogonal to $\mathcal{N}{(D_{-})}$, the resulted policy of DeePO can be read as ${G^{\infty} = {{\Pi_{D_{-}}G^{0}} + G^{\ast}}}.$

## Simulations

In this section, we perform simulations to validate the convergence of DeePO and the effects of regularization.

### V-A Numerical example

We randomly generate a dynamical model $(A,B)$ with ${n = 4},{m = 2}$ from a standard normal distribution and normalize $A$ such that ${\rho{(A)}} = 0.8$, i.e., the open-loop system is stable. The resulting model parameters $(A,B)$ are

It is straightforward to check that $(A,B)$ is controllable. Let $Q = I_{4}$ and $R = I_{2}$. We use Gaussian distribution to generate a batch of sufficiently exciting data $(U_{-},X_{-})$ with $T = 10$ that satisfies, and compute $X_{+}$ by. In the sequel, we only use $(U_{-},X_{-},X_{+})$ to perform the DeePO methods and validate the convergence.

Figure 2: Convergence of the DeePO methods.

### V-B Convergence of the DeePO methods

We consider three algorithms, i.e, DeePO in (10 ‣ III Data-enabled policy optimization ‣ Data-enabled Policy Optimization for the Linear Quadratic Regulator")), DeePO with the certainty-equivalence regularizer in and with the robustness regularizer in. For all the three algorithms, we set the stepsize to $\eta = {2 \times 10^{- 3}}$ for a fair comparison. For DeePO and DeePO with robustness regularizer, we set the initial policy as

with $K^{0} = 0$ since the system is open-loop stable. For DeePO with certainty-equivalence regularizer, we set

where the elements of $M \in {\mathbb{R}}^{T \times n}$ are randomly sampled from a Gaussian distribution $\mathcal{N}{(0,0.01)}$ (otherwise due to the implicit regularization, there will be no difference in the convergence curve compared with DeePO). To see how regularization parameters affect the performance, we select $\lambda = {1,10}$ for the certainty-equivalence regularizer and $\gamma = {1,10}$ for the robustness regularizer.

We illustrate the performance of the three algorithms in Fig. 2, where their relative errors are defined as ${({{J{(G^{k})}} - J^{\ast}})}/J^{\ast}$, ${({{J_{\lambda}{(G^{k})}} - J_{\lambda}^{\ast}})}/J_{\lambda}^{\ast}$, and ${({{J_{\gamma}{(G^{k})}} - J_{\gamma}^{\ast}})}/J_{\gamma}^{\ast}$, respectively. While Theorem 1 ‣ III-C Global convergence of DeePO ‣ III Data-enabled policy optimization ‣ Data-enabled Policy Optimization for the Linear Quadratic Regulator") only shows a more conservative sublinear convergence rate, all the three algorithms converge linearly in the simulation. The DeePO algorithm with certainty-equivalence regularizer (denoted by CE in Fig. 2) has the slowest convergence. The case for $\lambda = 10$ converges faster than the case $\lambda = 1$ due to the faster decay of the regularizer $\lambda{\|{\Pi_{D_{-}}G\Sigma_{G}^{1/2}}\|}^{2}$, and it achieves the same rate as the unregularized DeePO algorithm. Under the robustness regularizer, the DeePO algorithm has the fastest convergence, and $\gamma = 10$ leads to a larger convergence rate. Nevertheless, the resulted policy is different from those of the other two algorithms as discussed in Section IV-B. Finally, we note that all the algorithms only use $10$ pairs of state-input data to achieve an arbitrary relative error. In sharp contrast, the zeroth-order optimization method in uses $10^{5}$ trajectories (of manually tuned length to approximate the cost well) to achieve $0.01$ relative error for an LTI system with $m = n = 3$.

## Conclusion

In this paper, we have proposed the DeePO method that only requires a finite number of PE data to solve the LQR problem. By relating the nonconvex optimization problem to a convex program, we have shown the global convergence of DeePO. Furthermore, we have shown that the regularization method can be applied to enhance certainty-equivalence and robust stability without affecting its convergence. The implicit regularization property has also provided an insightful understanding on the optimization landscape of DeePO.

In future, it would be valuable to discover a strongly convex reparameterization of, which may improve the sublinear convergence rate to linear. It would also be interesting to study DeePO in a more general setting, e.g., the LQR with noisy inputs. Since DeePO is an efficient iterative method, it is expected to be able to applied to online control, where the control performance is constantly improved by collecting more real-time data. We are also hopeful that it can be used to solve the adaptive LQR for time-varying systems.
