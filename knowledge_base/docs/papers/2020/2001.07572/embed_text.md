## Introduction

### Fitting a linear policy to demonstrations

^††^footnotetext: \*Equal contribution.

Typically, we find a control policy for a task as follows. We first design a cost function that encodes the desired outcomes of the task, then find a control policy that minimizes that cost function, and finally we observe or simulate the behavior of this control policy on the true system. We repeat this process until we are content with the control policy's performance, either in simulation or in the real world.

This procedure (optimization-based control) has been successfully applied to many tasks. However, for complex tasks, it is often difficult to find a cost function that precisely captures the desired task outcomes and can be optimized effectively. For example, in autonomous driving, it is difficult, if not impossible, to construct a cost function that reliably generates "comfortable" driving behavior. For such tasks, the established procedure mentioned above is very expensive, time-consuming, and tedious, if it works at all.

Returning to the autonomous driving example, while it may be difficult to choose a cost function that captures "comfortable" driving behavior, it is relatively straightforward for human operators to provide demonstrations of such behavior. Similarly, for many other tasks, it is easier to collect demonstrations of (nearly) optimal behavior than it is to define a good cost function. This line of thought has motivated a long line of research on learning from demonstrations.

Despite this, there has been comparatively little work on learning from demonstrations in linear systems. This is surprising, since there are many practical applications of linear systems. Indeed, many systems can be modeled as linear systems, and we typically find control policies for nonlinear systems by first approximating these systems as linear systems. Much progress in control theory has come from studying linear systems, and we aim to continue that tradition here by considering the problem of learning a policy from demonstrations on a linear system.

In this paper, we consider the problem of learning a linear policy for a known stochastic linear system from demonstrations of an expert regulating the system (i.e., trying to keep the state and input small). The simplest method to fit a linear policy to demonstrations is (linear) policy fitting, where we minimize a loss function that measures our fit to the demonstrations plus a regularization function over linear policies. Despite its simplicity, policy fitting can lead to unstable and highly undesirable linear policies when there are few demonstrations.

Our key insight is the following: since we are trying to learn a policy for a linear system, the learned policy should be optimal for *some* quadratic cost function, i.e., some linear quadratic regulator (LQR) problem. To standard policy fitting we add a *Kalman constraint*, which requires that the policy be optimal for some LQR problem. Our name for this constraint refers to the famous paper by Kalman, *"When is a control system optimal?"*, which poses the question of determining when a given linear control policy is LQR optimal for some choice of weights. This procedure guarantees that the learned policy will retain all the desirable properties of optimal policies for LQR problems, such as stability and robustness. We can think of the Kalman constraint as a very specific form of regularization, one that is highly tuned to learning a linear control policy that is meant to regulate a system.

We formulate policy fitting with a Kalman constraint as a bi-convex optimization problem, with a convex objective and bi-affine constraints. From this formulation we derive a heuristic, based on the alternating direction method of multipliers (ADMM), that can (approximately) solve this problem by solving a small number of convex optimization problems. We show through numerical experiments that this method can recover stable, low-cost policies using very few demonstrations.

### Related work

In learning from demonstrations, the goal is to learn a policy from noisy observations of the optimal policy. This goal is shared by a few other bodies of work, namely "inverse optimal control", "inverse reinforcement learning", and "imitation learning"; each of these topics vary somewhat in the types of problems that they consider, the methods that they employ, and their notation, although there is considerable overlap. Below, we discuss some relevant work from each of these topics, as well as the related idea of incorporating stability in system identification. (For a more complete survey, see, e.g.,.)

### Inverse optimal control

In optimal control, we are given the cost function and our goal is to find the optimal policy. In inverse optimal control, we are given the optimal policy and asked to find the cost function. This topic dates back to Kalman's seminal work in 1964, where he characterized a sufficient and necessary condition for a linear policy to be optimal for a given LQR problem. (Our idea of using a Kalman constraint to regularize the policy learning procedure is directly inspired by this work.) More recently, it was shown that we can recover the cost function associated with an optimal policy for an LQR problem by solving a particular semidefinite program (SDP) \[7, §10.6\]. Unlike these methods, we do not assume access to the optimal policy and our focus is not on recovering the cost function but on learning an effective policy.

### Inverse reinforcement learning

In inverse reinforcement learning, the goal is to learn a cost function from (noisy) demonstrations of the optimal policy. We can then find a policy by optimizing the learned cost function. (Some argue that by learning the cost function first, we get the added benefit of interpretability.) Unlike in inverse optimal control however, here, we do not assume access to the system dynamics. Much of the work in this space considers systems with a finite number of states and inputs. More recent work has extended this work to the continuous state and input space setting by leveraging advances in deep learning. These methods demonstrate astonishing results at times but make very few (if any) assumptions and thus typically require large numbers of demonstrations to produce sensible results. Instead, our focus here is specifically on known linear systems and the low data regime.

### Imitation learning

In imitation learning, which we refer to as policy fitting, the goal is to find a policy directly from (noisy) demonstrations of the optimal policy. Imitation learning (or direct policy learning or behavior cloning) typically involves learning a mapping from states to inputs via supervised learning. However, standard imitation learning methods are prone to instability when only a few demonstrations are available -- a fact we confirm empirically in this work. Much like standard imitation learning methods, we attempt to learn a policy directly from states to inputs in this work; however, unlike prior work, we focus specifically on linear systems, leveraging their structure to add prior knowledge. Indeed, our method can be interpreted as a stability-regularized imitation learning method for linear systems.

### Stable system identification

Another related problem is learning dynamics from measurements of a dynamical system. The standard approach to this problem, system identification, frames this problem as a regression task. Recent work in this space has explored the idea of leveraging prior knowledge that the system to be identified is stable. For example, in the problem of fitting dynamics matrices, subject to the constraint that the dynamics are asymptotically stable, is framed as a convex optimization problem. This work has also been extended to nonlinear systems.

### Outline

In §2, we introduce the problem of learning from demonstrations on a linear system via policy fitting. In §3, we introduce the Kalman constraint, combine policy fitting with the Kalman constraint, and give an approximate solution method. In §4, we illustrate our method on several numerical examples. In §5, we describe some natural extensions and variations. In §6, we conclude.

## Linear policy fitting

### Dynamics

We consider a fully-observable linear dynamical system of the form

where, at time $t$, $x_{t} \in \text{R}^{n}$ is the system state, $u_{t} \in \text{R}^{m}$ is the control input, and $\omega_{t} \in \text{R}^{n}$ is a (random) disturbance. The (known) dynamics matrices are $A \in \text{R}^{n \times n}$ and $B \in \text{R}^{n \times m}$, and we assume that $(A,B)$ is controllable. We assume that ${\mathbf{E}{\lbrack\omega_{t}\rbrack}} = 0$, ${\mathbf{E}{\lbrack{\omega_{t}\omega_{t}^{T}}\rbrack}} = W$, and that $\omega_{t}$ is independent of the state $x_{t}$, the control input $u_{t}$, and $\omega_{\tau}$ for $\tau \neq t$.

### Policy

A *policy* $\pi:{\text{R}^{n}\rightarrow\text{R}^{m}}$ is a function that maps the current state $x_{t}$ to the control input $u_{t}$ that we will apply to the system,

Equations and together define the closed-loop system. We will consider the case where $\pi$ is linear, or

where $K \in \text{R}^{m \times n}$ in the gain matrix. The closed-loop dynamics are then

### "Expert" demonstrations

We consider the case where we observe some "expert" regulating the system, i.e., trying to keep the state $x_{t}$ and input $u_{t}$ small. We receive $N$ demonstrations, $(x^{i},u^{i})$, $i = {1,\ldots,N}$. These state input pairs need not be ordered in time, optimal in any sense, or even deterministic (i.e., we can have pairs with the same state and different inputs). We do assume, however, that the expert is attempting in good faith to regulate the system, i.e., keep $x_{t}$ and $u_{t}$ small, in some sense.

### Linear policy fitting

The goal in linear policy fitting is to fit a linear policy $K$ to the demonstrations. To that end, we consider the average of some loss function $l:{{\text{R}^{m} \times \text{R}^{m}}\rightarrow\text{R}}$ (convex in its first argument) across the demonstrations:

We also assume that we have a convex regularization function $r:{\text{R}^{m \times n}\rightarrow{\text{R} \cup {\{{+ \infty}\}}}}$ that encodes prior knowledge on $K$. Infinite values of $r$ can be interpreted as constraints on $K$.

To fit the policy, we solve the problem

with variable $K$. This optimization problem is convex, and so can be solved efficiently. We denote a solution to by $K^{pf}$.

The objective function in consists of two parts: the demonstration loss $L$ and the regularization function $r$. The first term here encourages a good fit to the demonstrations, and the second term encourages the policy to be simpler or to be consistent with prior knowledge.

If the expert is indeed using a linear policy, i.e., $x^{i} = {K^{expert}u^{i}}$, then we will recover $K^{expert}$ using $n$ demonstrations with high probability, with any reasonable choice of $l$, and without regularization. However, in general, policy fitting does not perform well when there are only a few demonstrations. Often, $K^{pf}$ does not even stabilize the system, let alone mimic the expert's policy well in closed-loop simulation (see §4 and ).

## Policy fitting with a Kalman constraint

### Linear quadratic regulator

The well-known linear quadratic regulator (LQR) problem chooses a policy $\pi$ that minimizes the average of a quadratic cost function,

where $Q \in \text{S}_{+}^{n}$ (the set of symmetric $n \times n$ positive semi-definite matrices) and $R \in \text{S}_{+ +}^{m}$ (the set of symmetric $m \times m$ positive definite matrices) are the state and control weight matrices, respectively, subject to the dynamics and $u_{t} = {\pi{(x_{t})}}$. Here the expectation is taken over the initial state $x_{0}$ and disturbances $\omega_{0},\omega_{1},\ldots$.

It is well known that (assuming some reasonable technical conditions hold) the optimal policy $\pi$ is linear, of the form

where $K^{\star} \in \text{R}^{m \times n}$ is the *optimal gain matrix*. The optimal gain matrix $K^{\star}$ depends on $Q$ and $R$, as well as $A$ and $B$, but not $W$.

### When is a linear policy optimal for given $Q$ and $R$?

Suppose we are given a linear policy $K$, and want to know if $K$ is optimal for the cost, given the quadratic cost matrices $Q$ and $R$. This is the case when

where $P$ is the unique positive semi-definite solution of the algebraic Riccati equation

### When is a linear policy optimal for *some* $Q$ and $R$?

Suppose we are given a linear policy $K$, and want to know if $K$ is optimal for the cost for *some* quadratic cost matrices $Q$ and $R$, which we are free to choose. This question was addressed in \[7, §10.6\], where the authors showed that we can answer this question, and get $Q$ and $R$, by solving the (convex) semidefinite feasibility problem

with variables $P$, $Q$, and $R$, where $\succeq$ denotes matrix inequality, i.e., with respect to the semidefinite cone. If problem is feasible, then $K$ is optimal for the quadratic cost matrices $Q$ and $R$. On the other hand, if is infeasible, then $K$ is not optimal for any LQR problem.

### Kalman constraint

We refer to the constraints in as a *Kalman constraint* on $K$, in tribute to Kalman's seminal work on optimal control, entitled "*When is a linear control system optimal?*". A Kalman constraint on $K$ implies that $K$ must be optimal for some quadratic cost matrices $Q$ and $R$. Policies that satisfy a Kalman constraint retain all the desirable properties of an LQR-optimal policy, such as stability and robustness.

### Policy fitting with a Kalman constraint

We add a Kalman constraint to the regularization function $r$ in the standard policy fitting problem. This new policy fitting problem has the form

with variables $P$, $Q$, $R$, and $K$. Note that the optimal gain matrix $K^{\star}$ is invariant to the relative scale of the $(Q,R)$ matrices, i.e., if $K$ is optimal for $(Q,R)$, it is also optimal for $({\alphaQ},{\alphaR})$ for any $\alpha > 0$. Thus, we can replace the (open) constraint $R \succ 0$ in with the (closed) constraint $R \succeq I$ by suitable scaling.

This problem is nonconvex and so, in general, difficult to solve exactly. However, we note that this problem is bi-convex in $(P,Q,R)$ and $K$. In §3.3, we derive a heuristic method that finds an approximate or local solution.

### Interpretability

Previous work in inverse reinforcement learning suggests that by recovering the (unknown) cost function, we will be able to better interpret the expert's policy. Indeed, our method does recover a cost function that, at least approximately, explains the observed demonstrations. However, we note that, even in linear systems, for a given linear policy, the quadratic cost function is not unique, even up to a scale factor. The problem of recovering a cost function from a given policy is under-determined, so even if we recover the true policy, the stage cost coefficients $Q$ and $R$, and the cost-to-go matrix $P$ may not converge to the true $Q$ and $R$, if they even exist. Therefore, all we can hope to do is recover a stable and desirable policy. (If we do care about the recovered $Q$ and $R$, and have some prior knowledge about them, we can add a suitable regularization term on $Q$, $R$, or $P$.)

### Solution method

### ADMM

We observe that the objective in is convex, and that the bi-convexity of the problem comes from the bi-affine constraints. Therefore, we propose to use the alternating direction method of multipliers (ADMM), which is guaranteed to converge to a (not necessarily optimal) stationary point for this problem, provided the penalty parameter is sufficiently large.

The augmented Lagrangian of is the extended function

where $Y$ is the dual variable for the constraints in,

and $\rho > 0$ is an algorithm parameter.

The ADMM algorithm alternates between minimizing the augmented Lagrangian over $K$, minimizing the augmented Lagrangian over $(P,Q,R)$, and performing a dual update to $Y$. The full procedure is summarized in algorithm 3.3 below.

Algorithm 3.1 *Learning from demonstrations in linear systems via ADMM.*

### $K$ step

The update for $K$ can be expressed as the solution to the convex optimization problem

where $Y^{k} = {(Y_{1}^{k},Y_{2}^{k})}$. This step can be interpreted as performing policy fitting with an additional term in the regularization function that suggests that $K$ should be approximately optimal for the LQR control problem with cost matrices $Q^{k}$, $R^{k}$, and cost-to-go matrix $P^{k}$.

### $(P,Q,R)$ step

The update for $(P,Q,R)$ can be expressed as the solution to the convex optimization problem

which can be interpreted as finding the cost matrices and cost-to-go-matrix of an LQR problem such that $K^{k + 1}$ is approximately optimal for that problem.

### Termination criterion

We can either run the algorithm for a fixed number of iterations ($n_{iter}$ in algorithm 3.3) or until the Frobenius between successive values of $K$ is less than some chosen value $\epsilon$.

### Convergence

This algorithm is only guaranteed to converge if the penalty parameter is large enough; even when it does converge, it need not converge to an optimal value. It is simply a sophisticated heuristic for finding an effective, stable policy.

## Examples

We illustrate our method and compare it with linear regression on several problems. In all of our experiments we use $\rho = 1$, and run ADMM with a zero initialization and 5 random initializations, ultimately using the $K$ with the lowest value of ${L{(K)}} + {r{(K)}}$. We use CVXPY to implement algorithm 3.3.

### Imperfect LQR

We first consider the case where the expert is performing imperfect regulation in an LQR problem. That is, our demonstrations have the form

where $K^{\star}$ is the solution to an LQR problem with cost matrices $Q^{true}$ and $R^{true}$ and $\Sigma \succ 0$. We consider loss and regularization functions

### Small random example

We consider a system with $n = 4$ states and $m = 2$ inputs. The data is generated according to

and the matrix $A$ is scaled so that its spectral radius is one. We ran policy fitting with and without a Kalman constraint on varying numbers of demonstrations, and averaged the results over ten random seeds. In figure 1 we show the expected cost (when it is finite) of policy fitting and our method versus the number of demonstrations, as well as the expected cost incurred by the expert and the optimal policy. Whereas our method never incurred infinite cost, standard policy fitting did; figure 2 shows the fraction of the time that the cost for policy fitting was finite.

Figure 1: Small random example: The expected cost of policy fitting and our method for a range of numbers of demonstrations. Infinite values are ignored.

Figure 2: Small random example: The fraction of simulations for which the cost for policy fitting was infinite. Our method always attained finite cost.

### Aircraft example

We consider the control of a 747 aircraft during level flight at an elevation of 40000 feet, traveling at 774 feet per second. The states and inputs represent deviations from operating or trim conditions. The states are $u$, the velocity of the aircraft along the body axis (in ft/s), $v$, the velocity of the aircraft perpendicular to the body axis (in ft/s), $\theta$, the angle between the body axis and horizontal (in crad), and $q = \overset{˙}{\theta}$, the pitch rate (in crad/s). The inputs are $\delta_{e}$, the elevator angle (in crad), and $\delta_{t}$, the thrust.

The linearized dynamics, discretized at an interval of 0.01 seconds, have the form

where the disturbance $\omega_{t}$ is caused by wind, with covariance

We use the cost matrices $Q = I$, $R = I$, incentivizing us to keep the 747 at the trim condition while keeping the thrust and elevator angle at the nominal levels. We also use the observation noise $\Sigma = {{}I}$. We ran policy fitting with and without a Kalman constraint on varying numbers of demonstrations, and averaged the results over ten random seeds. In figure 3 we show the expected cost (when it is finite) of policy fitting (PF) and our method versus the number of demonstrations, as well as the expected cost incurred by the expert and the optimal policy. Whereas our method never incurred infinite cost, standard policy fitting did; figure 4 shows the fraction of the time that the cost for policy fitting was finite.

Figure 3: Aircraft control example: The expected cost of policy fitting and our method for a range of numbers of demonstrations. Infinite values are ignored.

Figure 4: Aircraft control example: The fraction of simulations for which the cost for policy fitting was infinite. Our method always attained finite cost.

### LQR with outliers

We consider an LQR problem, with demonstrations generated according to

where $K^{\star}$ is the solution to an LQR problem with cost matrices $Q^{true}$ and $R^{true}$, and $\Sigma \succ 0$. For each entry of $u^{i}$, $i = {1,\ldots,N}$, we flip its sign with probability $0.1$. (The entries that are flipped are called outliers.)

We employ the following loss and regularization functions

where $\phi$ is the Huber penalty function, with parameter $M$,

(We use the Huber loss function because it is robust to outliers \[8, §6.1\].)

### Numerical example

We consider the same data as the small random problem in §4.1, and with $M = 0.5$. We ran policy fitting with and without a Kalman constraint on varying numbers of demonstrations, and averaged the results over ten random seeds. In figure 5 we show the expected cost (when it is finite) of policy fitting and our method versus the number of demonstrations, as well as the expected cost incurred by the expert and the optimal policy. Whereas our method never incurred infinite cost, standard policy fitting did; figure 6 shows the fraction of the time that the cost for policy fitting was finite.

Figure 5: LQR with outliers: The expected cost of policy fitting and our method for a range of numbers of demonstrations. Infinite values are ignored.

Figure 6: LQR with outliers: The fraction of simulations for which the cost for policy fitting was infinite. Our method always attained finite cost.

## Extensions and variations

### General quadratic cost problem

In this paper, in the interest of clarity, we focused on the regulation of linear systems, where the goal is to keep the state and input small. However, our method can be easily adapted for a more general class of problems, such as tracking problems, where the goal is not to keep the state and input small but to keep the state close to a given trajectory. To do so, we simply need to define the quadratic stage cost in its more general form

where $Q \in \text{S}_{+}^{n + m + 1}$. We can then replace the constraints in with the appropriate Riccati equation.

### Finite-horizon problem

Similarly, in this paper, we only considered the time-invariant, infinite horizon problem, where the dynamics function is as given in. However, our method can be easily extended for time-varying, finite-horizon problems, where the dynamics function is given by

where $T$ is the horizon of the problem. (In this problem, the cost function is similarly truncated to T steps and is also time-varying). Here, our goal is to learn a policy for each time-step, $K_{0}^{\star},K_{1}^{\star},\ldots,K_{T}^{\star}$ instead of a single policy.

To solve this problem using our method, we first need replace the constraints in with constraints for each time-step. (There are thus $T$ times as many constraints.) We can then adapt our algorithm to solve this problem by following the same steps outlined in §3.3.

## Conclusion

In this paper, we introduced a method for learning policies from demonstrations in linear systems and showed in numerical experiments that this method outperforms a widely-used baseline. Our method, which is based on convex optimization, is easy to implement and consistently produces reliable results, in contrast to gradient-based methods that are difficult to make work. We believe that this method and its extensions (see §5) have wide-ranging practical applications, especially in the domain of autonomous driving; indeed, a rigorous examination of this claim is the subject of future work. We are very optimistic about the potential of convex optimization to solve modern control problems and believe that this space will re-emerge as a fruitful area for research in the coming years.
