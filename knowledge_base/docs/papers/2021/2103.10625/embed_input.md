<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

On the Value of Preview Information for Safety Control

Topics include Safety control, Preview information, Lookahead, Nonlinear systems, Brunovsky canonical form, Controlled invariance.

<!-- chunk {"id": "summary-0002", "role": "summary", "section": "Summary", "weight": 2.0} -->

Analyzes when predictions of future disturbances or external inputs improve safety-control performance. The paper gives general preview-time guidance for nonlinear systems and sharper structural results for Brunovsky-form systems, clarifying when lookahead is worth using in continuous-state safety controllers.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Incorporating predictions of external inputs, which can otherwise be treated as disturbances, has been widely studied in control and computer science communities. These predictions are commonly referred to as preview in optimal control and lookahead in temporal logic synthesis. However, little work has been done for analyzing the value of preview information for safety control for systems with continuous state spaces. In this work, we start from showing general properties for discrete-time nonlinear systems with preview and strategies on how to determine a good preview time, and then we study a special class of linear systems, called systems in Brunovsky canonical form, and show special properties for this class of systems. In the end, we provide two numerical examples to further illustrate the value of preview in safety control.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

In a typical feedback control framework, the control input $u{(t)}$ is determined based on the current state $x{(t)}$, or more generally the initial state $x{}$ and the sequence of the past disturbances^11^1The concept of disturbance in this work can be quite general and it essentially captures any external input for which we might have predictions of future values. For instance, the reference signal in a tracking problem can be treated as "disturbance" if error dynamics are used to include the reference signal in system equations (see examples in ). $d{}$, $d{}$,..., $d{({t - 1})}$. However, in this work, we allow $u{(t)}$ to be determined not only by $x{}$, $d{}$,..., $d{({t - 1})}$, but also by future disturbances $d{(t)}$,..., $d{({t + p})}$, called the preview information, for some preview time $p$.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

This is a fair assumption in many modern control systems, enabled by the advances in sensing technologies. Examples of applying preview information in real-world systems include autonomous vehicles, power systems and robotics.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

The above mentioned systems are all safety-critical, where controllers should be designed to ensure safety specifications. The safety specifications considered in this work are to have the system state avoid visiting a user-defined unsafe region, or equivalently have the state stay within a safe region indefinitely. A standard way to achieve safety in this sense is via robust controlled invariant sets. Then, a fundamental question to ask is how to measure the improvement due to preview in safety control and how the change of preview time affects the quality of safety control.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

The majority of literature on preview control focuses on incorporating preview information into optimal control formulation. A prime example is model predictive control (MPC), where preview information is naturally incorporated into the state propagation constraints. In this case, the improvement due to preview is measured by the amount of cost reduction after increasing preview time. A recent work proves in theory that the cost reduction in both the linear quadratic control and MPC formulations decays exponentially fast as the preview time increases. However, those results are not applicable to our question, as they do not incorporate safety constraints.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Introduction", "weight": 1.5} -->

Our previous work addressed variants of this problem: incorporates preview on mode switching into safety control of switched systems, and studies the structure of controlled invariant sets for linear systems with delay in input and preview in disturbance. A significant implication of is that for linear systems, the negative impact of input delay to safety control can be compensated by the positive impact of preview on disturbances. But references rather focus on algorithmic scalability and do not consider general systems. Therefore, they provide little theory in how different preview times affect the controlled invariant sets.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Introduction", "weight": 1.5} -->

Notably, the impact of preview time is a relatively well-studied problem in reactive synthesis, where preview is called lookahead. provides, by checking the universal satisfiability of the linear temporal logic (LTL) formula encoding specifications, some extreme case analysis, which is analogous to our results on disturbance-collaborative systems in Section III. provides upper and lower bounds on the preview time necessary for the existence of a controller that realizes a LTL specification, which sheds light on the impact of different preview times. But those results are for finite-state transition systems only. In our work, we are also interested in systems with continuous state spaces.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Introduction", "weight": 1.5} -->

To summarize, to the best of our knowledge, there is little work in the literature that analyzes the value of preview for safety control of general discrete-time systems. This work is a first step in this direction. Our main contributions are: (i) We provide ways to compute inner and outer approximations of robust controlled invariant sets for general systems with preview and show how these approximation can be used to determine a good preview time. (ii) We derive a closed-form expression of the maximal controlled invariant set for systems in Brunovsky canonical form, one of the canonical forms of controllable systems, within a hyperbox safe set. Based on this closed-form expression, we characterize critical preview time over which additional preview information cannot improve safety.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Introduction", "weight": 1.5} -->

In the remainder of this work, the preliminaries of controlled invariant sets and a formal definition of systems with preview are introduced in Section II. Then in Section III, we study analytical properties of the controlled invariant sets for general systems with preview and how those properties lead to strategies of selecting preview time. In Section IV, we develop the theory for systems in Brunovsky canonical form. After that, we illustrate the value of preview using two numerical examples in Section V and conclude the paper in Section VI. The proofs of the theorems and details of the examples can be found in Appendix.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Example 1", "weight": 1.0} -->

Consider the following $2$-dimensional system

<!-- chunk {"id": "body-0013", "role": "body", "section": "Example 1", "weight": 1.0} -->

For arbitrarily large $K > 0$ in Method 2, $X_{K,p} = X_{0,p}$ is strictly contained by the maximal controlled invariant set. $\blacksquare$

<!-- chunk {"id": "body-0014", "role": "body", "section": "Example 1", "weight": 1.0} -->

It is worth noting that if we use $C_{max}{(\Sigma,S_{xu})}$ as the terminal state constraints in a model predictive control formulation with the planning horizon $p$, the feasible set of the initial states and the disturbances is equal to the controlled invariant set obtained by taking $K = p$ in Method 2 with the seed set ${C_{max}{(\Sigma,S_{xu})}} \times D^{p}$. In other words, this model predictive control formulation implicitly embeds the results of Method 2.

<!-- chunk {"id": "body-0015", "role": "body", "section": "Example 1", "weight": 1.0} -->

In this work, we want to study the general properties of controlled invariant sets of $\Sigma_{p}$. For instance, is a longer preview always a better choice? How does the maximal controlled invariant set change as the preview time $p$ increases? Then, we study a special class of systems where the closed-form expression of the maximal controlled invariant set of the $p$-augmented systems can be derived analytically.

<!-- chunk {"id": "body-0016", "role": "body", "section": "Analytical Results", "weight": 1.0} -->

In this section, we present analytical inner and outer approximations of controlled invariant sets for systems with different preview times. We also provide examples where the approximations are tight or not tight. Moreover, based on the approximations, we discuss strategies to choose the preview time $p$. An intuitive strategy is to select $p$ as large as possible, since a longer preview time provides more information than a shorter preview. However, since the dimension of $\Sigma_{p}$ is proportional to $p$, the existing methods suffer from the curse of dimensionality if the preview time is too long. Thus, we need a good strategy to select $p$, balancing between the computational cost and the performance.

<!-- chunk {"id": "body-0017", "role": "body", "section": "Analytical Results", "weight": 1.0} -->

First, the following theorem allows us to compare controlled invariant sets for systems with different preview times.

<!-- chunk {"id": "body-0018", "role": "body", "section": "Example 2", "weight": 1.0} -->

Suppose that the parameters $a$, $\gamma$, $\beta$ and $p$ satisfy $a > 1$, $r \geq {{({\beta + \gamma})}/{({a - 1})}}$ and ${a^{p - 1}\beta} \geq \gamma$. Then, the maximal controlled invariant set $C_{{max},p}$ of the $p$-augmented system within the augmented safe set ${\lbrack{- r},r\rbrack} \times {\lbrack{- \gamma},\gamma\rbrack}^{p} \times {\lbrack{- \beta},\beta\rbrack}$ is the set of points $(x,d_{1},\cdots,d_{p})$ satisfying^33^3The proof can be found in Appendix.

<!-- chunk {"id": "body-0019", "role": "body", "section": "Example 2", "weight": 1.0} -->

Example 2 reveals that the maximal controlled invariant set may not converge at finite $p_{0}$ in the sense of $C_{{max},p} = {C_{{max},p_{0}} \times D^{p - p_{0}}}$ for $p \geq p_{0}$.

<!-- chunk {"id": "body-0020", "role": "body", "section": "Example 2", "weight": 1.0} -->

We denote the maximal controlled invariant set $C_{max}{({\mathcal{D}{(\Sigma)}},S_{{xu},{co}})}$ by $C_{{max},{co}}{(\Sigma,S_{xu})}$, or $C_{{max},{co}}$ when $\Sigma$ and $S_{xu}$ are clear from the context. Intuitively, $C_{{max},{co}}$ contains all the possible initial states $x$ from which the future state-input pairs of $\Sigma$ can stay in $S_{xu}$ indefinitely, when we have infinite preview time.

<!-- chunk {"id": "body-0021", "role": "body", "section": "Example 3", "weight": 1.0} -->

We consider the same dynamics and safe set in Example 2. The projection of the maximal controlled invariant set onto the first coordinate is

<!-- chunk {"id": "body-0022", "role": "body", "section": "Example 3", "weight": 1.0} -->

However, the Hausdorff distance between the projection $PROJ_{1:n}{(C_{{max},p})}$ and $C_{{max},{co}}$ does not always converge to $0$ as $p$ goes to infinity, shown by the following example.

<!-- chunk {"id": "body-0023", "role": "body", "section": "Example 4", "weight": 1.0} -->

Combining Theorems 1 and 2, given any $p$, the maximal controlled invariant set $C_{{max},p}$ of $\Sigma_{p}$ within $S_{{xu},p}$ is bounded by

<!-- chunk {"id": "body-0024", "role": "body", "section": "Example 4", "weight": 1.0} -->

In practice, according to, if we already compute $C_{{max},p^{\prime}}$ for some $p^{\prime}$ and wonder if it is worth taking more cost to compute $C_{{max},p}$ for $p$ larger than $p^{\prime}$, a useful strategy is to compare the volumes of $C_{{max},p^{\prime}} \times D^{p - p^{\prime}}$ and $C_{{max},{co}} \times D^{p}$. The volume difference of the two sets indicates what we can gain at most by further increasing preview time.

<!-- chunk {"id": "body-0025", "role": "body", "section": "Example 4", "weight": 1.0} -->

Another significant implication of is that for any initial state not in $C_{{max},{co}}$, the future state-input trajectory of the system $\Sigma$ cannot stay within $S_{xu}$ indefinitely no matter how long the preview time $p$ is. In other words, $C_{{max},{co}}$ shows the limits of safety control with preview in terms of the allowable initial states.

<!-- chunk {"id": "body-0026", "role": "body", "section": "Systems in Brunovsky canonical form with hyperbox safe sets", "weight": 1.0} -->

In this section, we study systems in Brunovsky canonical form with a single input^55^5The results in this section apply to multiple-input case, since in Brunovsky canonical form, a system with multiple inputs can be decoupled into several systems with single input.. Due to the simple structure of the systems in Brunovsky canonical form, we can derive a closed-form expression of the maximal controlled invariant set within hyperbox safe sets. Next, based on the closed-form expression, we show convergence properties of the maximal controlled invariant set as the preview time increases. In terms of generality, any controllable system can be converted to a system in Brunovsky canonical form via an invertible transformation (see ), and thus our results on systems in Brunovsky canonical form is also useful for controllable systems.

<!-- chunk {"id": "body-0027", "role": "body", "section": "Systems in Brunovsky canonical form with hyperbox safe sets", "weight": 1.0} -->

The dynamics of a system $\Sigma_{B}$ in Brunovsky canonical form is

<!-- chunk {"id": "body-0028", "role": "body", "section": "Systems in Brunovsky canonical form with hyperbox safe sets", "weight": 1.0} -->

We first derive a necessary condition for the existence of nonempty controlled invariant sets of $\Sigma_{\mathbf{B},p}$ within $\mathbf{B} \times D^{p} \times {\mathbb{R}}$. The idea is based on the following observation: Given an input $u{(t)}$ at time $t \geq 0$, due to the special structure of $\overline{A}$ and $\overline{B}$, the $({{n - k} + 1})$ th entry $x_{{n - k} + 1}{({t + k})}$ of the state at time $t + k$ for $k$ with $1 \leq k \leq n$ can be exactly expressed as

<!-- chunk {"id": "body-0029", "role": "body", "section": "Systems in Brunovsky canonical form with hyperbox safe sets", "weight": 1.0} -->

Suppose there exists a nonempty controlled invariant set in $\mathbf{B} \times D^{p} \times {\mathbb{R}}$. Then, there exists at least one safe input ${u{(t)}} \in {\mathbb{R}}$ such that for all $k$ from $1$ to $n$, the right hand side of satisfies the constraints on $x_{{n - k} + 1}{({t + k})}$ from $\mathbf{B}$, robust to all possible future disturbances, that is, for $k$ from $1$ to $n$,

<!-- chunk {"id": "body-0030", "role": "body", "section": "Systems in Brunovsky canonical form with hyperbox safe sets", "weight": 1.0} -->

Note that if $i < p$, $d_{1,{n - i}}{({t + i})}$ is a scalar known from preview at time $t$; otherwise $d_{1,{n - i}}{({t + i})}$ takes arbitrary values in $\lbrack c_{{n - i},1},c_{{n - i},2}\rbrack$. Based on this observation, the condition of the existence of a safe input $u{(t)}$ satisfying is given in Theorem 3, which is necessary for the existence of a nonempty controlled invariant set.

<!-- chunk {"id": "body-0031", "role": "body", "section": "Remark 1", "weight": 1.0} -->

Adopting the idea, for a more general safe set in form of $P \times {\mathbb{R}}$, where $P$ is a polytope, we can construct a controlled invariant set of $\Sigma_{B,p}$ within $P \times D^{p} \times {\mathbb{R}}$ in $2$ moves: First, we construct a polytope in a lifted space that encodes all hyperboxes $\mathbf{B}$ in $P$ and all states $(x,d_{1:p})$ within the maximal controlled invariant set within $\mathbf{B} \times D^{p} \times {\mathbb{R}}$, based on the nonemptyness condition and the closed-form expression of $C_{p}$.

<!-- chunk {"id": "body-0032", "role": "body", "section": "Remark 1", "weight": 1.0} -->

Then, we project this lifted set onto its first $n{({p + 1})}$ coodinates, equal to the union of the maximal controlled invariant set within $\mathbf{B} \times D^{p} \times {\mathbb{R}}$ for all hyperboxes $\mathbf{B}$ contained by $P$. By construction, this set is a controlled invariant set in $P \times D^{p} \times {\mathbb{R}}$.

<!-- chunk {"id": "body-0033", "role": "body", "section": "Remark 1", "weight": 1.0} -->

Furthermore, as stated in Remark 1 of, any controllable system with a polytopic safe set (including input constraints) can be transformed into system in Brunovsky canonical form with a safe set in form of $P \times {\mathbb{R}}$. Thus, our results in this section can be used to compute controlled invariant sets for $p$-augmented systems of a controllable system. $\blacksquare$

<!-- chunk {"id": "body-0034", "role": "body", "section": "Remark 1", "weight": 1.0} -->

According to the closed-form expression of the maximal controlled invariant set $C_{p}$, we show the convergence property of $C_{p}$ for $p \geq n$ in the following theorem.

<!-- chunk {"id": "body-0035", "role": "body", "section": "Example 5", "weight": 1.0} -->

Consider the $1$-dimensional system $\Sigma$ and the safe set $S_{xu}$ defined in Example 2. We replace $u{(t)}$ in $\Sigma$ by ${{u{(t)}} = {{- {ax{(t)}}} + {v{(t)}}}},$ where $v{(t)}$ is the new control input. Then, the $1$-dimensional dynamics $\Sigma^{\prime}$ with respect to the state $x$ and the input $v$ is in Brunovsky canonical form. The safe set for this new dynamics is $S_{xu}^{\prime} = {\{{(x,v)}\mid{{(x,{{- {ax}} + v})} \in S_{xu}}\}}$.

<!-- chunk {"id": "body-0036", "role": "body", "section": "Example 5", "weight": 1.0} -->

Finally, recall that an outer bound on controlled invariant sets of $\Sigma_{B,p}$ is given in Section II by the Cartesian product of the maximal controlled invariant set of the disturbance-collaborative system and the set $D^{p}$, that is the right hand set of. We wonder the relation between $C_{n}$ and this outer bound, which is revealed by the next theorem.

<!-- chunk {"id": "body-0037", "role": "body", "section": "Illustrative Examples", "weight": 1.0} -->

In this section, we want to study the benefits of preview on disturbances via several concrete examples.

<!-- chunk {"id": "body-0038", "role": "body", "section": "V-A Impact of Preview on Disturbance Tolerance", "weight": 1.0} -->

We demonstrate the impact of preview on disturbance tolerance via our results on systems in Brunovksy canonical form. We fix the state dimension $n = 10$ and the safe set $\mathbf{B} = {\Pi_{i = 1}^{n}{\lbrack{- 1},1\rbrack}}$. Then, we parametrize the disturbance set $D = {\Pi_{i = 1}^{n}{\lbrack{- c},c\rbrack}}$ by a positive number $c > 0$. We are interested in the largest $c$ for the augmented system $\Sigma_{B,p}$ to have nonempty controlled invariant sets within $\mathbf{B} \times D^{p} \times {\mathbb{R}}$. According to Corollary 1, we can utilize the condition on nonempty controlled invariant set given by to determine the largest possible $c$.

<!-- chunk {"id": "body-0039", "role": "body", "section": "V-A Impact of Preview on Disturbance Tolerance", "weight": 1.0} -->

By plugging $b_{k,1} = {- 1}$, $b_{k,2} = 1$, $c_{k,1} = {- c}$ and $c_{k,2} = c$ for all $k$ from $1$ to $n$ into, we obtain an upper bound on $c$ such that holds. The largest $c$ computed for different preview time $p$ are shown in Fig. 1. As we expect, when the preview time increases, a larger disturbance set can be handled, due to the power of preview.

<!-- chunk {"id": "body-0040", "role": "body", "section": "V-A Impact of Preview on Disturbance Tolerance", "weight": 1.0} -->

In addition, we observe in Fig. 1 that the largest $c$ stops increasing after $p \geq 6$. This observation suggests that a disturbance set with $c > 0.2222$ may lead to an empty controlled invariant set for any preview time $p$. With some calculation, it can be verified that for $c > {2/9}$, the necessary condition does not hold for all $p \geq 0$ and thus the maximal controlled invariant set is always empty no matter how large the $p$ is.

<!-- chunk {"id": "body-0041", "role": "body", "section": "V-B Lane Keeping Control with Preview", "weight": 1.0} -->

To show the usefulness of preview, we present how preview helps the driver-assist system to keep a vehicle within lanes. We use a $4$-dimensional linearized bicycle model with respect to constant longitudinal speed ${30m}/s$. The state space consists of lateral displacement $y$, lateral velocity $v$, yaw angle $\Delta\Psi$ and yaw rate $r$. The disturbance $r_{d}$ with ${|r_{d}|} \leq 0.04$ considered in this simplified model is a quantity related to the road curvature that perturbs the yaw angle. The control input $u$ is the steering angle, with constraints $u \in {\lbrack{- {\pi/2}},{\pi/2}\rbrack}$.

<!-- chunk {"id": "body-0042", "role": "body", "section": "V-B Lane Keeping Control with Preview", "weight": 1.0} -->

The safe set $S_{xu}$ is the set of state-input pairs within bounds ${|y|} \leq 0.9$, ${|v|} \leq 1.2$, ${|{\Delta\Phi}|} \leq 0.05$ and ${|r|} \leq 0.3$, and ${|u|} \leq {\pi/2}$. We set the preview time $p = 5$. We first compute the maximal controlled invariant set within $S_{xu}$ for system without preview, denoted by $C_{{max},0}$. Then, we use Method 2 to grow the seed set $C_{{max},0} \times D^{5}$ for the $p$-augmented system over $10$ iterations, the result of which is denoted by $C_{{io},5}$. Numerically we find that $C_{{io},5}$ strictly contains $C_{{max},0} \times D^{5}$.

<!-- chunk {"id": "body-0043", "role": "body", "section": "V-B Lane Keeping Control with Preview", "weight": 1.0} -->

We also try the idea in Remark 1 to obtain a controlled invariant set based on our results in Section IV, but the resulting set is contained by $C_{{max},0} \times D^{p}$, which is too conservative to be useful.

<!-- chunk {"id": "body-0044", "role": "body", "section": "V-B Lane Keeping Control with Preview", "weight": 1.0} -->

Next, we find a point $(x_{0},d_{1},\cdots,d_{5})$ belonging to the set difference $C_{{io},5} \smallsetminus {C_{{max},0} \times D^{5}}$ and simulate $2$ trajectories starting at $x_{0}$ with the first $5$ disturbances $d_{1:5}$, using the two controlled invariant sets $C_{{max},0}$ and $C_{{io},5}$ respectively. The controller consists of $2$ parts: First, we have a nominal state feedback controller, designed via linear quadratic regulator for the $p$-augmented system. Then, at each time instant, we supervise the control input from the nominal controller by projecting that input onto the admissible input set at current state with respect to $C_{{max},0}$ or $C_{{io},5}$.

<!-- chunk {"id": "body-0045", "role": "body", "section": "V-B Lane Keeping Control with Preview", "weight": 1.0} -->

If the admissible input set happens to be empty at some time instants, then we project the nominal input onto the input constraint set $\lbrack{- {\pi/2}},{\pi/2}\rbrack$. The resulting vehicle maneuvers are shown by Fig. 2, where we find that the trajectory under the supervision of the admissible input set with respect to $C_{{io},5}$ stays within the lane as required by the safety constraints during the simulation time span, but the trajectory under the supervision with respect to $C_{{max},0}$ violates the constraints on lateral displacement $y$ and drives out of the lane at the $2$nd time step. This observation meets our expectation since the initial condition was not in $C_{{max},0}$. This example demonstrates how the preview on future disturbances enables controllers to operate safely from a larger set of initial conditions.

<!-- chunk {"id": "body-0046", "role": "body", "section": "Conclusion", "weight": 1.5} -->

In the first part of this work, we study general properties of controlled invariant sets for systems with preview and the implications of those properties, including a strategy to choose a preview time. In the second part, we study systems in Brunovsky canonical form with hyperbox safe sets, for which we derive the maximal controlled invariant set of the $p$-augmented system in closed form. The impact of preview on the controlled invariant sets can be directly analyzed using this closed-form expression, by help of which we prove the existence of a critical preview time for this class of systems. In future work, we plan to study noisy preview information.
