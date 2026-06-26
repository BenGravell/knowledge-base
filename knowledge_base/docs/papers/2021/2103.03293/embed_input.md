<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Accelerating Second-Order Differential Dynamic Programming for Rigid-Body Systems

Topics include Differential dynamic programming, Second-order methods, Rigid-body dynamics, Trajectory optimization.

<!-- chunk {"id": "summary-0002", "role": "summary", "section": "Summary", "weight": 2.0} -->

Shows how to efficiently evaluate the second-order dynamics derivatives required by full DDP for rigid-body systems via recursive algorithms. This can make full DDP computationally competitive with or faster than iLQR. Also provides a clear derivation of DDP.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

This letter presents a method to reduce the computational demands of including second-order dynamics sensitivity information into the Differential Dynamic Programming (DDP) trajectory optimization algorithm. An approach to DDP is developed where all the necessary derivatives are computed with the same complexity as in the iterative Linear Quadratic Regulator (iLQR). Compared to linearized models used in iLQR, DDP more accurately represents the dynamics locally, but it is not often used since the second-order derivatives of the dynamics are tensorial and expensive to compute. This work shows how to avoid the need for computing the derivative tensor by instead leveraging reverse-mode accumulation of derivative information to compute a key vector-tensor product directly. We also show how the structure of the dynamics can be used to further accelerate these computations in rigid-body systems. Benchmarks of this approach for trajectory optimization with multi-link manipulators show that the benefits of DDP can often be included without sacrificing evaluation time, and can be done in fewer iterations than iLQR.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

In recent years, online optimal control strategies have gained widespread interest in many applications from motion planning of robots to control of chemical processes. Rather than relying on manually derived policies, these control strategies optimize a metric of cost that encodes desired task goals. This approach then allows online control performance that is generalizable across tasks or environments. For example, online optimization may enable legged systems to tailor their gaits to sensed terrains and inevitable disturbances or may enable manipulators to rapidly synthesize efficient motions when transporting new objects.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

However, for robots with even a few links, the underlying system dynamics are complex, nonlinear, and expensive to evaluate. These features challenge the ability to solve trajectory optimization problems online, particularly in systems with a large number of degrees of freedom (DoFs). Yet, the motivation to perform online optimization is often greater for these very systems, since a high DoF morphology gives the needed flexibility and mobility to adapt to a wider range of situations. Since the curse of dimensionality precludes the ability of exploring the full state space, online optimal control strategies often settle on exploring within a local neighborhood. Even then, the optimization of trajectories is often orders of magnitude slower than real-time. For many years, control approaches in the legged robotics literature have sidestepped this burden by employing simple models to enable faster computation.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

Recently, whole-body trajectory optimization is becoming more feasible and has gained increased interest as computation power progresses. For example, used DDP for a humanoid to perform complex tasks such as getting up from an arbitrary pose. DDP exploits the sparsity of an optimal control problem (OCP), and its output includes an optimal trajectory along with a locally optimal feedback policy that can be used to handle disturbances. While DDP natively does not address constraints, many recent approaches using Augmented Lagrangian, interior point, and relaxed barrier strategies have been proposed to handle general state and control constraints, with specialized approaches considered for control limit constraints. Other work has considered multi-threading and parallelization of the DDP algorithm to accelerate its computation. Finally, Li et al. combine the advantages of whole-body DDP and simple models by sequentially considering both over the horizon. Collectively, these previous works show broad potential impact from advances to numerical methods for DDP.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

Originally described, DDP uses a second-order approximation of the dynamics when constructing a second-order approximation of the optimal cost-to-go. However, in practice (e.g., ) many researchers have opted to use a first-order dynamics approximation due to its faster evaluation time, giving rise to the iterative Linear Quadratic Regulator (iLQR). While the second-order dynamics information retains higher fidelity to the full model locally, it is represented by a rank three tensor and is expensive to compute. In this work, we alleviate these computational demands by describing a new approach that avoids the evaluation of the dynamics derivative tensor (Fig. 1).

<!-- chunk {"id": "body-0008", "role": "body", "section": "I-A Specific Contributions", "weight": 1.0} -->

This work presents and combines several advances for reducing the computational complexity of computing second-order dynamics sensitivity information in DDP. The final result is a method for computing this information with the same computational complexity as first-order dynamics derivatives (e.g., as in iLQR). The contributions are (I) the use of reverse-mode automatic differentiation (AD) to compute second-order derivatives needed in DDP. This contribution is general to discrete-time dynamic systems and enables computation reductions compared to methods that explicitly evaluate a derivative tensor for the dynamics. Further, we show (II) how second-order information related to the forward dynamics can be related to associated information from the inverse dynamics, akin to first-order results; this contribution is specific to rigid-body models. Lastly, we (III) introduce a modification to the Recursive-Newton-Euler Algorithm (RNEA) that supports this process and further reduces computational demands. Figure 1 overviews a benchmark of the proposed methods against iLQR and against DDP approaches that explicitly compute derivative tensors.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Trajectory Optimization via DDP/iLQR", "weight": 1.0} -->

This work considers the efficient solution of a finite-horizon OCP for a rigid-body system such as an articulated robot. This section reviews background on dynamics and trajectory optimization with a focus on the DDP algorithm.

<!-- chunk {"id": "body-0010", "role": "body", "section": "II-A Dynamics", "weight": 1.0} -->

The RNEA can evaluate $ID$ with $\mathcal{O}{(n)}$ complexity where $n$ is the number of DoFs in the system. The forward dynamics (FD) of the system can be formulated as When the fourth argument is omitted for $ID$ or $FD$, gravity of $9.81$ m/s^2^ downward is assumed. The Articulated-Body Algorithm (ABA) can compute $FD$ in $\mathcal{O}{(n)}$ complexity and is an efficient alternative to $\mathcal{O}{(n^{3})}$ algorithms that calculate and invert the mass matrix to carry out $FD$ (e.g.,). Continuous trajectories for the state $\mathbf{x} = {\lbrack\mathbf{q}^{T},{\overset{˙}{\mathbf{q}}}^{T}\rbrack}^{T}$ and control input $\mathbf{τ}$ are discretized herein using a numerical integration scheme.

<!-- chunk {"id": "body-0011", "role": "body", "section": "II-A Dynamics", "weight": 1.0} -->

While the strategies proposed are applicable for use with any explicit integration scheme, forward Euler integration is assumed to simplify the remaining development such that: | | \mathbf{x}_{k + 1} & {= {\mathbf{f}{(\mathbf{x}_{k},\mathbf{u}_{k})}} \triangleq {\mathbf{x}_{k} + {h\begin{bmatrix} | | | | | {{FD}{(\mathbf{q},\overset{˙}{\mathbf{q}},{\mathbf{τ}})}} | | | where $h$ is the integration stepsize.

<!-- chunk {"id": "body-0012", "role": "body", "section": "II-B Differential Dynamic Programming", "weight": 1.0} -->

Herein, DDP and iLQR are used to solve an OCP with a cost function of the form where $\ell_{k}{(\mathbf{x}_{k},\mathbf{u}_{k})}$ represents the running cost, $\ell_{f}{(\mathbf{x}_{N})}$ represents the terminal cost incurred at the end of a horizon, and $\mathbf{U}_{0} = {\lbrack\mathbf{u}_{0},\mathbf{u}_{1},\ldots,\mathbf{u}_{N - 1}\rbrack}$ is the control sequence over the horizon. A cost-to-go function $V_{k}{(\mathbf{x}_{k},\mathbf{U}_{k})}$ can be similarly defined from any time point as the partial sum of costs from time $k$ to $N$.

<!-- chunk {"id": "body-0013", "role": "body", "section": "II-B Differential Dynamic Programming", "weight": 1.0} -->

The cost-to-go function $V_{0}{(\mathbf{x}_{0},\mathbf{U}_{0})}$ in is minimized with respect to $\mathbf{U}_{0}$, with states subject to the discrete system dynamics, providing Throughout the paper, the star superscript refers to an optimal value.

<!-- chunk {"id": "body-0014", "role": "body", "section": "II-B Differential Dynamic Programming", "weight": 1.0} -->

Omitting the time index $k$ for conciseness, these quantities are given: The prime in denotes the next time step, i.e., $V_{\mathbf{x}\mathbf{x}}' = {V_{\mathbf{x}\mathbf{x}}{({k + 1})}}$. The last terms in (6c - 6e) denote contraction with a tensor and are ignored in iLQR, representing the main difference between DDP and iLQR. These coefficients could alternatively be viewed through derivatives of the Hamiltonian where ${\mathbf{λ}} \triangleq V_{\mathbf{x}}'$ is the co-state vector.

<!-- chunk {"id": "body-0015", "role": "body", "section": "II-B Differential Dynamic Programming", "weight": 1.0} -->

When this control is substituted, the quadratic approximation of the value function can be constructed as where the $\text{ER}{(k)}$ is the expected reduction in cost-to-go if ${\delta\mathbf{x}_{k}} = 0$ and $\mathbf{U}_{k}$ were chosen optimally. This process is repeated until a value function approximation is obtained at time $k = 0$, constituting the backward sweep of DDP.

<!-- chunk {"id": "body-0016", "role": "body", "section": "II-B Differential Dynamic Programming", "weight": 1.0} -->

Following this backward sweep, a forward sweep proceeds by simulating the system forward in time under the incremental control policy, resulting in a new state-control trajectory. This optimal control law is typically modified by a backtracking line-search parameter, $0 < \epsilon < 1$ such that $\mathbf{u}_{k} = {{\overline{\mathbf{u}}}_{k} - {\epsilon{\mathbf{κ}}_{k}} - {\mathbf{K}_{k}\delta\mathbf{x}_{k}}}$. The line-search parameter ensures that DDP/iLQR takes steps that result in a reduction of the total cost. The resulting trajectory serves as a new nominal trajectory, with the above backward and forward sweeps repeated until some convergence criteria is met.

<!-- chunk {"id": "body-0017", "role": "body", "section": "II-C DDP and iLQR: Conceptual Comparison", "weight": 1.0} -->

Many factors influence the relative performance of iLQR and DDP, with the main difference again being that the tensorial terms in (6c - 6e) are ignored in iLQR. The effect is that while DDP experiences quadratic convergence for trajectories that are sufficiently close to local optimality, iLQR only experiences super-linear convergence (i.e., it converges more slowly). However, if the running and terminal costs are strictly convex, iLQR can be simplified relative to DDP since the terms (6c - 6e) in iLQR then ensure that $Q_{\mathbf{u}\mathbf{u}}$ is always positive definite. By comparison, the addition of the tensor terms (6c - 6e) in DDP can render $Q_{\mathbf{u}\mathbf{u}}$ indefinite, requiring regularization, which incurs additional computational cost. The choice of DDP and iLQR in application then becomes a cost-benefit analysis among these differences with iLQR favored in recent work.

<!-- chunk {"id": "body-0018", "role": "body", "section": "II-C DDP and iLQR: Conceptual Comparison", "weight": 1.0} -->

The derivatives of the dynamics are the most computationally expensive terms in DDP, motivating methods for their efficient evaluation.

<!-- chunk {"id": "body-0019", "role": "body", "section": "Efficient Computation of Second-Order Derivatives for DDP", "weight": 1.0} -->

This section considers how dynamics partials enter the partials of the Hamiltonian. The co-state vector is partitioned as ${\mathbf{λ}} = {\lbrack{\mathbf{ξ}}^{T},{\mathbf{η}}^{T}\rbrack}^{T}$ where $\mathbf{ξ}$ and $\mathbf{η}$ are the co-states associated with $\mathbf{q}$ and $\overset{˙}{\mathbf{q}}$ respectively. Via, the Hamiltonian is then: Focusing on the second-order partials of $H_{k}{(\mathbf{x},\mathbf{u},{\mathbf{λ}})}$ with respect to $\mathbf{q}$, and dropping the arguments for conciseness, the partials can be written as where the simplification occurs since ${\partial{\overset{˙}{\mathbf{q}}/{\partial q_{j}}}} = 0$.

<!-- chunk {"id": "body-0020", "role": "body", "section": "Efficient Computation of Second-Order Derivatives for DDP", "weight": 1.0} -->

In, the second-order partial of $FD$ is the most expensive term to compute. It represents a bottleneck in DDP since computing it for all possible $i$ and $j$ results in a tensor $\frac{\partial^{2}{FD}}{\partial\mathbf{q}^{2}}$ with $n^{3}$ elements. These elements can be computed with total complexity $\mathcal{O}{(n^{3})}$ before being contracted with $\mathbf{η}$ at an additional $\mathcal{O}{(n^{3})}$ total cost. This conventional strategy is denoted as *DDP via Tensor Contraction*.

<!-- chunk {"id": "body-0021", "role": "body", "section": "III-A Reverse-mode Accumulation to Efficiently Compute", "weight": 1.0} -->

Returning to, since the partials of $FD$ are contracted with the vector $\mathbf{η}$ on the left, the desired partials can be computed efficiently using reverse-mode approaches, as diagrammed in Fig. 2 ‣ III Efficient Computation of Second-Order Derivatives for DDP ‣ \titled"). Since $FD$ can be calculated in $\mathcal{O}{(n)}$, reverse-mode AD can be used to compute ${\mathbf{η}}^{T}\frac{\partial{FD}}{\partial\mathbf{q}}$ in $\mathcal{O}{(n)}$ operations as well.

<!-- chunk {"id": "body-0022", "role": "body", "section": "III-A Reverse-mode Accumulation to Efficiently Compute", "weight": 1.0} -->

This result is then differentiated further, achieving the necessary result $\frac{\partial}{\partial\mathbf{q}}\left\lbrack {{\mathbf{η}}^{T}\frac{\partial{FD}}{\partial\mathbf{q}}} \right\rbrack$ in $\mathcal{O}{(n^{2})}$ operations -- the same complexity as the first-order partials for $FD$ itself. When partials for DDP are obtained with this approach, we denote the method as *DDP via ABA* since ABA is first used to evaluate $FD$.

<!-- chunk {"id": "body-0023", "role": "body", "section": "III-A Reverse-mode Accumulation to Efficiently Compute", "weight": 1.0} -->

This general strategy also applies to any dynamic system $\mathbf{x}_{k + 1} = {\mathbf{f}{(\mathbf{x}_{k},\mathbf{u}_{k})}}$ for computing ${\frac{\partial}{\partial\mathbf{x}}{\lbrack{{\mathbf{λ}}^{T}\mathbf{f}_{\mathbf{x}}}\rbrack}} = {{\mathbf{λ}} \cdot \mathbf{f}_{\mathbf{x}\mathbf{x}}}$ in DDP. While the use of reverse-mode accumulation to compute Hessians is a standard option in AD packages, its use to accelerate DDP here is new.

<!-- chunk {"id": "body-0024", "role": "body", "section": "III-B First-Order Derivatives of Rigid-Body Dynamics", "weight": 1.0} -->

The structure of rigid-body dynamics further enables efficiency gains for derivative evaluation. The iLQR and DDP algorithms require first-order derivatives of the dynamics, and these can be computed in $\mathcal{O}{(n^{2})}$ operations with AD tools applied to the ABA. When dynamics derivatives are computed in this manner, the resulting iLQR algorithm is denoted as *iLQR via ABA*. This approach is diagrammed on the left side of Fig. 2 ‣ III Efficient Computation of Second-Order Derivatives for DDP ‣ \titled").

<!-- chunk {"id": "body-0025", "role": "body", "section": "III-B First-Order Derivatives of Rigid-Body Dynamics", "weight": 1.0} -->

These relationships provide alternate methods for the first-order partials of $FD$, shown on the left side of Fig. 3. The term $\frac{\partial{ID}}{\partial\mathbf{z}}$ can be computed in $\mathcal{O}{(n^{2})}$ complexity with AD tools or specialized algorithms (e.g., ). The explicit computation of the mass matrix inverse can be avoided in by instead applying it indirectly via $n$ calls to the ABA algorithm ($\mathcal{O}{(n)}$) with the columns of $\frac{\partial{ID}}{\partial\mathbf{z}}$ as inputs for $\mathbf{τ}$. This approach evaluates with total complexity $\mathcal{O}{(n^{2})}$. Since relies on RNEA to obtain $ID$, we denote this method as *iLQR via RNEA*. As an alternate approach, the partials of $FD$ are computed via with $O{(n^{3})}$ complexity as follows.

<!-- chunk {"id": "body-0026", "role": "body", "section": "III-B First-Order Derivatives of Rigid-Body Dynamics", "weight": 1.0} -->

The partials of $ID$ are computed with $O{(n^{2})}$ complexity, the mass matrix inverse is computed once with $O{(n^{2})}$ complexity (e.g., via ), and a dense matrix-matrix multiply in finally sets the complexity at $O{(n^{3})}$. Since matrix multiplications are optimized on modern hardware, this approach can be faster than the lower-order one. We next extend the relation to the second-order case.

<!-- chunk {"id": "body-0027", "role": "body", "section": "III-C Second-Order Partials of Rigid-Body Dynamics", "weight": 1.0} -->

As the main technical contribution of the paper, this section presents an efficient way to include the second-order dynamics partials in DDP by employing reverse-mode AD and the relationship between first-order sensitivities. Figure 3 is diagrammed as a companion road-map to the following technical development. The derivation makes use of the identity and the fact that for a fixed $\mathbf{q}$, $\overset{˙}{\mathbf{q}}$, and $\mathbf{τ}$, ${ID}{(\mathbf{q},\overset{˙}{\mathbf{q}},\overset{¨}{\mathbf{q}})}$ is implicitly dependent on $FD$ through composition via $\overset{¨}{\mathbf{q}} = {{FD}{(\mathbf{q},\overset{˙}{\mathbf{q}},{\mathbf{τ}})}}$. Therefore, the partials of $ID$ include the partials of $FD$ through chain rule.

<!-- chunk {"id": "body-0028", "role": "body", "section": "III-C Second-Order Partials of Rigid-Body Dynamics", "weight": 1.0} -->

We start by using reconsidering the second order partial in via the use of: where we used that ${\partial{\mathbf{M}^{- 1}/{\partial q_{j}}}} = {- {\mathbf{M}^{- 1}{({\partial{\mathbf{M}/{\partial q_{j}}}})}\mathbf{M}^{- 1}}}$, and the last term in the overall result is from the chain rule for the second-order partials of $ID$. The identity allows for the rewrite of (III-C) such that The matrix-vector product $\mathbf{M}^{- 1}{\mathbf{η}}$ can be computed efficiently using the ABA algorithm by ignoring gravity and the Coriolis term and using $\mathbf{η}$ as an input in place of $\mathbf{τ}$.

<!-- chunk {"id": "body-0029", "role": "body", "section": "III-C Second-Order Partials of Rigid-Body Dynamics", "weight": 1.0} -->

Formulas for the other second-order partials are as follows. Using the same approach as before, we can show that For the mixed partials of $\mathbf{q}$ and $\overset{˙}{\mathbf{q}}$, we can show that where $\mathbf{\Psi} = \frac{\partial{FD}}{\partial\overset{˙}{\mathbf{q}}}$. Finally, for the mixed partials of $\mathbf{q}$ and $\mathbf{τ}$, the resulting relationship is where $\mathbf{\Xi} = \frac{\partial{FD}}{\partial{\mathbf{τ}}}$. Using reverse-mode tools, all these partials can be computed with $\mathcal{O}{(n^{2})}$ complexity. We denote DDP algorithms that use this approach as *DDP via RNEA*.

<!-- chunk {"id": "body-0030", "role": "body", "section": "III-C Second-Order Partials of Rigid-Body Dynamics", "weight": 1.0} -->

Across these derivations, the term ${\mathbf{μ}}^{T}\frac{\partial{ID}}{\partial\mathbf{q}}$ is common. To evaluate ${\mathbf{μ}}^{T}\frac{\partial{ID}}{\partial\mathbf{q}}$ we can either use reverse AD with the RNEA to calculate result or provide a method to compute the term ${\mathbf{μ}}^{T}{ID}$, and then calculate its gradient with AD. While the two approaches are similar, we present a refactoring of the RNEA to reduce computation requirements for ${\mathbf{μ}}^{T}{ID}$ before applying AD.

<!-- chunk {"id": "body-0031", "role": "body", "section": "III-D Modified RNEA Algorithm", "weight": 1.0} -->

Here, we follow spatial vector algebra, notation, and body numbering conventions. Consider a poly-articulated tree-structured system of $N_{B}$ rigid bodies. We denote $p{(i)}$ as the parent body of body $i$, and use the notation $j \succeq i$ to indicate when body $j$ is after body $i$ in the kinematic tree. Sums over pairs of related bodies can be carried out in either of the following ways: The modified RNEA output ${\mathbf{μ}}^{T}{ID}$ satisfies ${{\mathbf{μ}}^{T}{\mathbf{τ}}} = {\sum_{i = 1}^{N}{{\mathbf{μ}}_{i}^{T}{\mathbf{τ}}_{i}}}$.

<!-- chunk {"id": "body-0032", "role": "body", "section": "III-D Modified RNEA Algorithm", "weight": 1.0} -->

The torque ${\mathbf{τ}}_{i}$ at joint $i$ is given as where $\mathbf{S}_{i}$ gives joint $i$'s free-modes, ${{\mathcal{F}_{|}\Im\mathcal{I}_{|}\dashv_{|}\Downarrow\Leftarrow\sqsubseteq_{|}} \times^{\Uparrow}\Rightarrow}\mathcal{I}_{|}\sqsubseteq_{|}$ the inertial force of body $j$, $\mathbf{v}_{j}$ its spatial velocity, $\mathbf{a}_{j}$ its spatial acceleration, and $\times^{\ast}$ a cross product for spatial vectors. The term ${\mathbf{μ}}^{T}{\mathbf{τ}}$ then satisfies The summation above is then refactored using as This refactoring leads to the modified RNEA algorithm (see Algo. 1).

<!-- chunk {"id": "body-0033", "role": "body", "section": "III-D Modified RNEA Algorithm", "weight": 1.0} -->

The result is that ${\mathbf{μ}}^{T}{ID}$ can be computed in a single pass rather than two passes as in RNEA. The algorithm is still an $\mathcal{O}{(n)}$ algorithm but leads to a simpler computation graph for reverse-mode AD. Whenever this method is used in DDP, it is referred to as *DDP via Modified RNEA*. The computation workflow in this case is given as in Fig. 3, where the modified RNEA is used to accelerate the blocks highlighted in green.

<!-- chunk {"id": "body-0034", "role": "body", "section": "III-E Summary", "weight": 1.0} -->

Before proceeding to the presentation of comparative results, we briefly review the methods introduced for incorporating partials into iLQR and DDP. When only using first-order dynamics partials, we have *iLQR via ABA* and *iLQR via RNEA*. For full second-order methods, we have *DDP via ABA*, *DDP via RNEA*, and *DDP via Modified RNEA* methods, all avoiding explicitly computing the second-order dynamics derivative tensor. Finally the conventional DDP method *DDP via Tensor Contraction* involves computing the second-order derivative tensor. The computation approaches of these methods have been diagrammed in Fig. 2 ‣ III Efficient Computation of Second-Order Derivatives for DDP ‣ \titled") and Fig. 3.

<!-- chunk {"id": "body-0035", "role": "body", "section": "Results", "weight": 1.0} -->

To test the performance and scalability of our proposed methods, we evaluate their application to solve an OCP for an underactuated $n$-link pendubot. The trajectory optimization problem here was a swing-up problem and this goal was encoded via design of running and terminal costs. These costs were similar for all proposed methods regardless of the number of links in the model. As the number of links is increased, their nonlinear couplings on one another present additional challenge for solving the OCP. To further make the control problem challenging, the final link in the system was left un-actuated. For all the proposed methods, the same convergence criteria was used with convergence indicated by a negligible ($< 10^{- 9}$) reduction in the cost function between iterations. We first compare the computation time of the dynamics partials (Section IV-A) using the methods described previously and then compare the addition of those partials within DDP/iLQR optimization frameworks as appropriate (see Section IV-B). This work was implemented in Matlab^11^1Open-source code: alongside the CasADi Toolkit which allows for rapid and efficient testing of AD approaches.

<!-- chunk {"id": "body-0036", "role": "body", "section": "Results", "weight": 1.0} -->

Since the partials are evaluated in the CasADi virtual machine through MATLAB, merits of the methods should be assessed via comparison between them, while future work will study improving absolute timing numbers via C/C++ implementation.

<!-- chunk {"id": "body-0037", "role": "body", "section": "IV-A Dynamics Partials", "weight": 1.0} -->

Within DDP/iLQR, the computation of the partials of the dynamics is the most computationally expensive part of the optimization process. Figure 4 compares the computation time of the different methods for evaluating these partials. As shown, evaluation of the second-order partials by tensor contraction takes the longest time whereas all other second-order partials have the same computational complexity as the first-order dynamic partials (as indicated by the slope on the log-log plot). The most competitive second-order approach requires approximately only $2.5$ times more computation time than first-order partials. Second-order partials via RNEA/modified RNEA were faster than second-order partials via ABA since RNEA is simpler than ABA, with the modified RNEA outperforming RNEA. These results indicate that when compared to conventional second-order tensorial dynamic partials, the proposed methods have the potential to reduce the computational overhead of DDP to be competitive with iLQR.

<!-- chunk {"id": "body-0038", "role": "body", "section": "IV-B Trajectory Optimization: DDP/iLQR Framework", "weight": 1.0} -->

We then include the dynamics partials in DDP/iLQR as appropriate and evaluate the OCP for the pendubot. Note that for an OCP with a horizon of $N$ timesteps, each iteration of iLQR/DDP must evaluate the derivatives $N$ times, motivating the need for their rapid evaluation. Figure 5 illustrates the time required to solve the OCP to convergence with DDP and iLQR variants. Tensor-free DDP variants had evaluation times comparable to the iLQR ones, while DDP via Tensor Contraction takes longer to optimize due to its higher cost of evaluating derivatives. The comparative performance of the fastest iLQR and DDP variants depends on the problem instance. Trajectory updates performed for either algorithm depend on the non-linearity of the system considered, and on the initial guess, which prevents uniformly recommending iLQR or DDP over the other.

<!-- chunk {"id": "body-0039", "role": "body", "section": "IV-B Trajectory Optimization: DDP/iLQR Framework", "weight": 1.0} -->

We also evaluate the mean time to compute the DDP/iLQR variants for a $7$-link pendubot model. We use a dissipative controller as the initial control trajectory and randomize the initial state vector around the downward configuration of the pendubot. This is a difficult problem, as it forces the control to pump energy into the system in order to drive it to the upright configuration. Figure 6 illustrates the time to solve the OCP with DDP/iLQR variants. As shown, *DDP via Tensor Contraction* took the longest time to converge, whereas the tensor-free DDP strategies took more time compared to iLQR in this case. A portion of the additional time for DDP is attributed to repeats of the backward sweep due to the regularization needed for DDP in this case. While this motivates focus on these aspects in future work, it is worth noting that the running cost in this case was convex, and this provides benefit to iLQR in terms of avoiding regularization.

<!-- chunk {"id": "body-0040", "role": "body", "section": "IV-B Trajectory Optimization: DDP/iLQR Framework", "weight": 1.0} -->

Finally, we optimize a trajectory for a $7 -$link KUKA LBR manipulator (available in Matlab's Robotics Toolbox) using DDP/iLQR methods. Figure 7 illustrates suboptimality vs. iterations for iLQR and DDP when applied to the manipulator. The suboptimality measures the difference between the current cost function value and its value at the end of the iterations. As illustrated, the DDP variants featured quadratic convergence whereas the iLQR variants featured super-linear convergence. This figure also illustrates that the DDP variants took fewer iterations compared to iLQR counterparts.

<!-- chunk {"id": "body-0041", "role": "body", "section": "IV-B Trajectory Optimization: DDP/iLQR Framework", "weight": 1.0} -->

Since the solution of an OCP is dependent on the initial conditions, we randomize the initial controller using Ornstein-Uhlenbeck process noise for the $7 -$link KUKA LBR manipulator and solved the OCP problem using either iLQR/DDP in $40$ separate instances. The first pane of Fig. 8 illustrates the progression of that manipulator from an initial configuration to the balanced upright configuration along an optimal trajectory. Subplot (a) of Fig. 8 illustrates the empirical probability density function (pdf) of the number of iterations over those optimizations. Subplot (b) illustrates the pdf of the log of the final cost of each optimal solution. As illustrated in subplot (a), in $95\%$ of the simulations, iLQR had a higher number of iterations. On average, iLQR had three times as many iterations as DDP. From subplot (b), we note that most of the simulations regardless of DDP/iLQR converged to similar solution; in fact, DDP converged to a different solution than iLQR in only three instances.

<!-- chunk {"id": "body-0042", "role": "body", "section": "IV-B Trajectory Optimization: DDP/iLQR Framework", "weight": 1.0} -->

Figure 8 illustrates that the inclusion of second-order information in DDP will result in similar converged solution and in fewer iterations. This result is powerful in that the addition of second-order information results in algorithm that converges in less iterations and to the same minima.

<!-- chunk {"id": "body-0043", "role": "body", "section": "IV-C Discussion", "weight": 1.0} -->

As compared to conventional approaches to DDP that explicitly compute second-order derivatives of the dynamics, the proposed DDP variants presented herein show a marked improvement in their computational complexity and computation time. This is especially important as second-order information retains better local fidelity to the original model and therefore a second-order approximation better captures the nonlinear effects of the system. This feature is expected to be important for complex systems such as quadrupeds whose coupled nonlinear dynamics might not be accurately captured by a first-order approximation. This second-order information could be of value in critical circumstances, for example, the increased fidelity could help a quadruped prevent falls or handle disturbances when traversing unstructured terrain.

<!-- chunk {"id": "body-0044", "role": "body", "section": "IV-C Discussion", "weight": 1.0} -->

We noted previously that DDP includes a regularization scheme to ensure that $Q_{\mathbf{u}\mathbf{u}}$ remains positive-definite during the backward pass. This regularization incurs additional computational cost as compared to iLQR methods, and this additional cost cannot be anticipated before running the optimization. In Fig. 6, the proposed DDP variants needed more computation time than the iLQR variants, though we expected those evaluation times to be more similar based on other tests (Fig. 1). We attribute a portion of the computational cost to repeats of the backward sweep when regularization fails, as most of the computation in DDP is spent evaluating the backward sweep.

<!-- chunk {"id": "body-0045", "role": "body", "section": "IV-C Discussion", "weight": 1.0} -->

Lastly, our results showed that iLQR typically has more iterations but overall had comparable computation time as proposed DDP variants. Therefore, the benefits of DDP can be included in trajectory optimization without the previously significant sacrifice in evaluation time, and can be done in fewer iterations. This may lead to more robust model-predictive control wherein warm staring online may keep DDP iterations within the quadratic convergence well.

<!-- chunk {"id": "body-0046", "role": "body", "section": "Conclusion and Future Directions", "weight": 1.5} -->

This work has made use of reverse-mode AD tools to quickly evaluate different approaches for obtaining the derivatives needed by DDP. We also extended the relationship between the first-order sensitivities of $ID$ and $FD$ for rigid-body systems to the second-order case. The combination of this new approach and AD tools allows for the evaluation of the needed derivatives in DDP with the same complexity as iLQR. Lastly, we introduce a restructuring of RNEA to derive a modified RNEA that returns $\mu^{T}{ID}$ in $\mathcal{O}{(n)}$ complexity, and enables the fastest DDP algorithm.

<!-- chunk {"id": "body-0047", "role": "body", "section": "Conclusion and Future Directions", "weight": 1.5} -->

While AD tools are convenient, they are general purpose, and thus may not be optimal. Alternative analytical methods for taking derivatives of rigid-body dynamics can accumulate the derivatives recursively, as. Recently, we extended the modified RNEA algorithm with an analytical accumulation of its first-order partials in a reverse-mode fashion, and further evaluation of this result is of immediate interest. Moreover, we aim to extend this work to address rigid-body dynamics with contacts by using similar approaches as in this paper. This generalization would then allow for use with hybrid dynamic systems that arise in legged locomotion problems.

<!-- chunk {"id": "body-0048", "role": "body", "section": "Conclusion and Future Directions", "weight": 1.5} -->

There are many other opportunities that this work motivates as next steps. While we noted that the presented work is general for any explicit integration scheme, we also see opportunity to extend this work for implicit integration and implicit DDP. Further, while the DDP used here was a single-shooting solver, our contributions could be used in multi-shooting DDP and other numerical optimal control solvers. Finally, our work may find applicability when working to control soft robots. Many multi-segment soft-body robots can be modeled assuming piece-wise constant curvature (PCC), approximating PCC with a high-DoF augmented rigid model, or considering discrete Cosserat models. The ideas herein may find applicability for these models due to their dynamics equations taking a similar structural form (e.g., ) as rigid-body systems. Augmented rigid models are most directly applicable in 2D, but generalizations of the RNEA and ABA for the 3D continuum case also present interesting future avenues to broaden the application of this work.
