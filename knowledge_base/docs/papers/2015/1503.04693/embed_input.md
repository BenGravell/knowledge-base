<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Minimal Actuator Placement with Optimal Control Constraints

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

We introduce the problem of minimal actuator placement in a linear control system so that a bound on the minimum control effort for a given state transfer is satisfied while controllability is ensured. We first show that this is an NP-hard problem following the recent work of Olshevsky. Next, we prove that this problem has a supermodular structure. Afterwards, we provide an efficient algorithm that approximates up to a multiplicative factor of O(logn), where n is the size of the multi-agent network, any optimal actuator set that meets the specified energy criterion. Moreover, we show that this is the best approximation factor one can achieve in polynomial-time for the worst case. Finally, we test this algorithm over large Erdos-Renyi random networks to further demonstrate its efficiency.

<!-- chunk {"id": "body-0003", "role": "body", "section": "Introduction", "weight": 1.5} -->

During the past decade, control scientists have developed various tools for the regulation of large-scale systems, with the notable examples of for the control of biological systems, for the regulation of brain and neural networks, for network protection against spreading processes, and for load management in smart grid. On the other hand, the enormous size of these systems and the need for cost-effective control make the identification of a small fraction of their nodes to steer them around the state space a central problem within the control community.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

This is a combinatorial task of formidable complexity; as it is shown, identifying a small set of actuator nodes so that the resultant system is controllable alone is NP-hard. Nonetheless, a controllable system may be practically uncontrollable if the required input energy for the desired state transfers is forbidding, as when the controllability matrix is close to singularity. Therefore, by choosing input nodes to ensure controllability alone, one may not achieve a cost-effective control for the involved state transfers. In this paper, we aim to address this important requirement, by introducing a best-approximation polynomial-time algorithm to actuate a small fraction of a system's states so that controllability is ensured and a specified control energy performance is guaranteed.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

In particular, we consider the selection of a minimal number of actuators such that a bound on the minimum control effort for a given transfer is satisfied while controllability is ensured. Finding the appropriate choice of such a subset of nodes is a challenging task, since the search for a subset satisfying certain criteria constitutes a combinatorial optimization problem that can be computationally intensive. Indeed, it is shown in that identifying the minimum number of actuators for inducing controllability alone is NP-hard. Therefore, we extend this computationally hard problem by imposing an energy constraint on the choice of the actuator set, and we solve it with an efficient approximation algorithm.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

Specifically, we first generalize the involved energy objective to an $\epsilon$-close one, which remains well-defined even when the controllability matrix is non-invertible. Then, we make use of this metric and we relax the controllability constraint of the original problem. Notwithstanding, we show that for certain values of $\epsilon$ all solutions of this auxiliary program still render the system controllable. This fact, along with a supermodularity property of the generalized objective that we establish, leads to a polynomial-time algorithm that approximates up to a multiplicative factor of $O{({\log n})}$ any optimal actuator set that meets the specified energy bound, when the latter lies in a certain range with respect to $n$. Moreover, we show that this is the best approximation factor one can achieve in polynomial-time for the worst case.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

Hence, with this algorithm we aim to address the open problem of actuator placement with energy performance guarantees. To the best of our knowledge, we are the first to study the selection of a minimal number of actuators so that a bound on the minimum control effort for a given transfer is satisfied. Our results are also applicable to the case of average control energy metrics and can be extended to the cardinality-constrained actuator placement for minimum control effort, where the optimal actuator set is selected so that these metrics are minimized, while its cardinality is upper bounded by a given value. These and other relevant extensions are explored in the companion manuscript.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Introduction", "weight": 1.5} -->

The remainder of this paper is organized as follows. The formulation and model for the actuator selection problem are set forth in Section II. In Section III we discuss our main results, including the intractability of this problem, as well as the supermodularity of the involved control energy objective. Then, we provide an efficient approximation algorithm for its solution. Finally, in Section IV we illustrate our analytical findings on an integrator chain network and we test their performance over large Erdős-Rényi random networks. Section V concludes the paper. All proofs can be found in the Appendix.

<!-- chunk {"id": "body-0009", "role": "body", "section": "II-A Actuator Placement Model", "weight": 1.0} -->

Consider a linear system of $n$ states, $x_{1},x_{2},\ldots,x_{n}$, whose evolution is described by

<!-- chunk {"id": "body-0010", "role": "body", "section": "II-A Actuator Placement Model", "weight": 1.0} -->

where $t_{0} \in {\mathbb{R}}$ is fixed, $x \equiv {\{ x_{1},x_{2},\ldots,x_{n}\}}$, ${\overset{˙}{x}{(t)}} \equiv {{{dx}/d}t}$, while $u$ is the corresponding input vector. The matrices $A$ and $B$ are of appropriate dimension. Without loss of generality, we also refer to as a network of $n$ agents, $1,2,\ldots,n$, which we associate with the states $x_{1},x_{2},\ldots,x_{n}$, respectively. Moreover, we denote their collection as $\mathcal{V} \equiv {\lbrack n\rbrack}$. Henceforth, the interaction matrix $A$ is fixed, while a special structure is assumed for the input matrix $B$.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Assumption 1", "weight": 1.0} -->

Each choice of the binary vector $\delta$ in Assumption 1 signifies a particular selection of agents as actuators. Hence, if $\delta_{i} = 1$, state $i$ may receive an input, while if $\delta_{i} = 0$, receives none. We collect the above and others into the next definition.

<!-- chunk {"id": "body-0012", "role": "body", "section": "II-B Controllability and the Minimum Energy Transfer Problem", "weight": 1.0} -->

We consider the notion of controllability and relate it to the problem of selecting a minimum number of actuators for the satisfaction of a control energy constraint.

<!-- chunk {"id": "body-0013", "role": "body", "section": "II-B Controllability and the Minimum Energy Transfer Problem", "weight": 1.0} -->

Recall that is controllable if for any finite $t_{1} > t_{0}$ and any initial state $x_{0} \equiv {x{(t_{0})}}$, the system can be steered to any other state $x_{1} \equiv {x{(t_{1})}}$, by some input $u{(t)}$ defined over $\lbrack t_{0},t_{1}\rbrack$. Moreover, for general matrices $A$ and $B$, the controllability condition is equivalent to the matrix

<!-- chunk {"id": "body-0014", "role": "body", "section": "II-B Controllability and the Minimum Energy Transfer Problem", "weight": 1.0} -->

being positive definite for any $t_{1} > t_{0}$. Therefore, we refer to $\Gamma{(t_{0},t_{1})}$ as the controllability matrix of.

<!-- chunk {"id": "body-0015", "role": "body", "section": "II-B Controllability and the Minimum Energy Transfer Problem", "weight": 1.0} -->

The controllability of a linear system is of great interest, because it is related to the solution of the following minimum energy transfer problem

<!-- chunk {"id": "body-0016", "role": "body", "section": "II-B Controllability and the Minimum Energy Transfer Problem", "weight": 1.0} -->

where $A$ and $B$ are any matrices of appropriate dimension. In particular, if is controllable for the given $A$ and $B$, the resulting minimum control energy is given by

<!-- chunk {"id": "body-0017", "role": "body", "section": "II-B Controllability and the Minimum Energy Transfer Problem", "weight": 1.0} -->

where $\tau = {t_{1} - t_{0}}$. Therefore, if $x_{1} - {e^{A\tau}x_{0}}$ is spanned by the eigenvectors of $\Gamma{(t_{0},t_{1})}$ corresponding to its smallest eigenvalues, the minimum control effort may be forbiddingly high. Hence, when we choose the actuators of a network so that controllability is ensured and an input energy constraint for a specified state transfer is satisfied, we should take into account their effect on $\Gamma{(t_{0},t_{1})}^{- 1}$.

<!-- chunk {"id": "body-0018", "role": "body", "section": "II-B Controllability and the Minimum Energy Transfer Problem", "weight": 1.0} -->

Moreover, controllability is an indispensable property for any linear system, while in many cases is viewed as a structural attribute of the involved system that holds true even by any single input nodes, as in large-scale neural networks. This motivates further the setting of this paper, where the actuators are chosen so that a bound on the minimum control effort for a given transfer is satisfied and overall controllability is respected.

<!-- chunk {"id": "body-0019", "role": "body", "section": "II-B Controllability and the Minimum Energy Transfer Problem", "weight": 1.0} -->

Per Assumption 1 some further properties for the controllability matrix are due. First, given an actuator set $\Delta$, associated with some $\delta$, let $\Gamma_{\Delta} \equiv {\Gamma{(t_{0},t_{1})}}$; then,

<!-- chunk {"id": "body-0020", "role": "body", "section": "II-C Actuator Placement Problem", "weight": 1.0} -->

We consider the problem of actuating a small number of system's states so that the minimum control energy for a given transfer meets some specified criterion and controllability is ensured. The challenge is in doing so using as few actuators as possible. This is an important improvement over the existing literature where the goal of actuator placement problems have either been to ensure just controllability or the weaker property of structural controllability. Other relevant results consider the task of leader-selection, where the leaders, i.e. actuated agents, are chosen so as to minimize an appropriate mean-square convergence error of the remaining agents. Our work also departs from a set of works that study average energy metrics, such as the minimum eigenvalue of the controllability Gramian or the trace of its inverse. Instead, here we consider an exact energy objective and require it to satisfy a particular upper bound.

<!-- chunk {"id": "body-0021", "role": "body", "section": "II-C Actuator Placement Problem", "weight": 1.0} -->

Let $\mathcal{C}_{r} \equiv {\{{\Delta \subseteq \mathcal{V}}:{{{|\Delta|} \leq r},{\Gamma_{\Delta} \succ 0}}\}}$ be the actuator sets of cardinality at most $r$ that render controllable. Then, for any $\Delta \subseteq \mathcal{V}$, we write $\Delta \in \mathcal{C}_{|\Delta|}$ to denote that $\Delta$ achieves controllability. Furthermore, we set

<!-- chunk {"id": "body-0022", "role": "body", "section": "II-C Actuator Placement Problem", "weight": 1.0} -->

for some positive constant $E$. This problem is a generalized version of the minimal controllability problem considered, so that its solution not only ensures controllability, but also provides a guarantee in terms of the minimum input energy required for the normalized transfer from $x_{0}$ to $x_{1}$; indeed, for $E\rightarrow\infty$, we recover the problem of.

<!-- chunk {"id": "body-0023", "role": "body", "section": "II-C Actuator Placement Problem", "weight": 1.0} -->

Observe that this lower bound depends only on $A$ and $v$, i.e. also on $n$, as well as on $t_{0}$ and $t_{1}$.

<!-- chunk {"id": "body-0024", "role": "body", "section": "II-C Actuator Placement Problem", "weight": 1.0} -->

Moreover, (I) is NP-hard, since it looks for a minimal solution and so it asks if $\mathcal{C}_{r} \neq \varnothing$ for any $r < n$. Thus, we need to identify an efficient approximation algorithm for its solution, which is the subject of the next section.

<!-- chunk {"id": "body-0025", "role": "body", "section": "Minimal Actuator Sets with Constrained Minimum Energy Performance", "weight": 1.0} -->

We present an efficient polynomial-time approximation algorithm for (I). To this end, we first generalize the involved energy objective to an $\epsilon$-close one, that remains well-defined even when the controllability matrix is non-invertible. Next, we relax (I) by introducing a program that makes use of this objective and ignores controllability constraint of (I). Nonetheless, we show that for certain values of $\epsilon$ all solutions of this auxiliary program still render the system controllable. This fact, along with the supermodularity property of the generalized objective that we establish, leads to our proposed approximation algorithm. The discussion of its efficiency ends the analysis of (I).

<!-- chunk {"id": "body-0026", "role": "body", "section": "III-A An $\\epsilon$-close Auxiliary Problem", "weight": 1.0} -->

Consider the following approximation to Problem (I)

<!-- chunk {"id": "body-0027", "role": "body", "section": "III-A An $\\epsilon$-close Auxiliary Problem", "weight": 1.0} -->

The $\epsilon$-closeness is evident, since for any $\Delta \in \mathcal{C}_{|\Delta|}$, ${\phi{(\Delta)}}\rightarrow{v^{T}\Gamma_{\Delta}^{- 1}v}$ as $\epsilon\rightarrow 0$. Notice that we can take $\epsilon\rightarrow 0$, since we assume any positive $\epsilon \leq {1/E}$.

<!-- chunk {"id": "body-0028", "role": "body", "section": "III-B Approximation Algorithm for Problem (I^′^)", "weight": 1.0} -->

We first prove that all solutions of (I^′^) for $0 < \epsilon \leq {1/E}$, render the system controllable, notwithstanding that no controllability constraint is imposed by this program on the choice of the actuator sets. Moreover, we show that the involved $\epsilon$-close energy objective is supermodular, and then we present our approximation algorithm, followed by a discussion of its efficiency, which ends this subsection.

<!-- chunk {"id": "body-0029", "role": "body", "section": "III-C Quality of Approximation of Algorithm 1 ‣ III Minimal Actuator Sets with Constrained Minimum Energy Performance ‣ Minimal Actuator Placement with Optimal Control Constraints\") for Problem (I^′^)", "weight": 1.0} -->

The result in (10. ‣ III-B Approximation Algorithm for Problem (I′) ‣ III Minimal Actuator Sets with Constrained Minimum Energy Performance ‣ Minimal Actuator Placement with Optimal Control Constraints")) was expected from a design perspective: Increasing the network size $n$ or improving the accuracy by decreasing $\epsilon$, as well as demanding a better energy guarantee by decreasing $E$, should all push the cardinality of the selected actuator set upwards. Also, note that $\log\epsilon^{- 1}$ is the design cost for circumventing the difficulty to satisfy controllability constraint of Problem (I) directly.

<!-- chunk {"id": "body-0030", "role": "body", "section": "III-C Quality of Approximation of Algorithm 1 ‣ III Minimal Actuator Sets with Constrained Minimum Energy Performance ‣ Minimal Actuator Placement with Optimal Control Constraints\") for Problem (I^′^)", "weight": 1.0} -->

Furthermore, per (10. ‣ III-B Approximation Algorithm for Problem (I′) ‣ III Minimal Actuator Sets with Constrained Minimum Energy Performance ‣ Minimal Actuator Placement with Optimal Control Constraints")) and with $E - {\phi{(\mathcal{V})}}$ and $\epsilon$ both fixed, the cardinality of the actuator set that Algorithm 1 ‣ III Minimal Actuator Sets with Constrained Minimum Energy Performance ‣ Minimal Actuator Placement with Optimal Control Constraints") returns is up to a multiplicative factor of $O{({\log n})}$ from the minimum cardinality actuator sets that meet the same performance criterion. We note that this is the best achievable bound in polynomial-time for the set covering problem in the worst case, while (I^′^) is a generalization of it (cf. ).

<!-- chunk {"id": "body-0031", "role": "body", "section": "III-D Approximation Algorithm for Problem (I)", "weight": 1.0} -->

We present an efficient approximation algorithm for Problem (I) that is based on Algorithm 1 ‣ III Minimal Actuator Sets with Constrained Minimum Energy Performance ‣ Minimal Actuator Placement with Optimal Control Constraints"). To this end, let $\Delta$ be the actuator set returned by Algorithm 1 ‣ III Minimal Actuator Sets with Constrained Minimum Energy Performance ‣ Minimal Actuator Placement with Optimal Control Constraints"), i.e. $\Delta \in \mathcal{C}_{|\Delta|}$ and ${\phi{(\Delta)}} \leq E$. Moreover, denote as $\lambda_{1}$, $\lambda_{2}$, $\ldots$, $\lambda_{n}$ and $q_{1}$, $q_{2}$, $\ldots$, $q_{n}$ the eigenvalues and the corresponding orthonormal eigenvectors of $\Gamma_{\Delta}$, respectively.

<!-- chunk {"id": "body-0032", "role": "body", "section": "III-D Approximation Algorithm for Problem (I)", "weight": 1.0} -->

where we derived (12 ‣ III Minimal Actuator Sets with Constrained Minimum Energy Performance ‣ Minimal Actuator Placement with Optimal Control Constraints")) from (11 ‣ III Minimal Actuator Sets with Constrained Minimum Energy Performance ‣ Minimal Actuator Placement with Optimal Control Constraints")) using the fact that for any $x \geq 0$, ${1/{({1 + x})}} \geq {1 - x}$, while the rest follow from the definition of $\lambda_{m}$ and $q_{M}$, as well as the assumption ${{n\epsilon{({v^{T}q_{M}})}^{2}}/\lambda_{m}^{2}} \leq {cE}$. Moreover, it is also true that ${\phi{(\Delta)}} \leq E$ by the definition of $\Delta$, and therefore from (13 ‣ III Minimal Actuator Sets with Constrained Minimum Energy Performance ‣ Minimal Actuator Placement with Optimal Control Constraints")) we get

<!-- chunk {"id": "body-0033", "role": "body", "section": "III-D Approximation Algorithm for Problem (I)", "weight": 1.0} -->

On the other hand, $\lambda_{m}$ and $q_{M}$ are not in general known in advance. Hence, we need to search for a sufficiently small value of $\epsilon$ so that (14 ‣ III Minimal Actuator Sets with Constrained Minimum Energy Performance ‣ Minimal Actuator Placement with Optimal Control Constraints")) holds. One way to achieve this, since $\epsilon$ is lower and upper bounded by $0$ and $1/E$, respectively, is to perform a binary search. We implement this procedure in Algorithm 2 ‣ III Minimal Actuator Sets with Constrained Minimum Energy Performance ‣ Minimal Actuator Placement with Optimal Control Constraints"), where we denote as ${\lbrack{\text{Algorithm}}\rbrack}{(E,\epsilon)}$ the set that Algorithm 1 ‣ III Minimal Actuator Sets with Constrained Minimum Energy Performance ‣ Minimal Actuator Placement with Optimal Control Constraints") returns, for given $E$ and $\epsilon$.

<!-- chunk {"id": "body-0034", "role": "body", "section": "III-D Approximation Algorithm for Problem (I)", "weight": 1.0} -->

Upper bound E, approximation error c, bisection’s accuracy level a, matrices Γ1, Γ2, …, Γn, vector v.
Algorithm 2 Approximation Algorithm for the Problem (I).

<!-- chunk {"id": "body-0035", "role": "body", "section": "III-D Approximation Algorithm for Problem (I)", "weight": 1.0} -->

Note that in the worst case, when we first enter the while loop, the if condition is not satisfied and as a result, $\epsilon$ is set to a lower value. This process continues until the if condition is satisfied for the first time, from which point and, the algorithm converges, up to the accuracy level $a$, to the largest value $\overline{\epsilon}$ of $\epsilon$ such that ${{v^{T}\Gamma_{\Delta}^{- 1}v} - {v^{T}{({\Gamma_{\Delta} + {\epsilonI}})}^{- 1}v}} \leq {cE}$; specifically, ${|{\epsilon - \overline{\epsilon}}|} \leq {a/2}$, due to the mechanics of the bisection.

<!-- chunk {"id": "body-0036", "role": "body", "section": "III-D Approximation Algorithm for Problem (I)", "weight": 1.0} -->

Then, Algorithm 2 ‣ III Minimal Actuator Sets with Constrained Minimum Energy Performance ‣ Minimal Actuator Placement with Optimal Control Constraints") exits the while loop and the last if statement ensures that $\epsilon$ is set below $\overline{\epsilon}$ so that ${{v^{T}\Gamma_{\Delta}^{- 1}v} - {v^{T}{({\Gamma_{\Delta} + {\epsilonI}})}^{- 1}v}} \leq {cE}$. The efficiency of this algorithm for Problem (I) is summarized below.

<!-- chunk {"id": "body-0037", "role": "body", "section": "Examples and Discussion", "weight": 1.0} -->

We test the performance of the proposed algorithm over various systems, starting with an integrator chain in Subsection IV-A and following up with Erdős-Rényi random networks in Subsection IV-B.

<!-- chunk {"id": "body-0038", "role": "body", "section": "IV-A The Case of an Integrator Chain", "weight": 1.0} -->

We first illustrate the mechanics and efficiency of Algorithm 2 ‣ III Minimal Actuator Sets with Constrained Minimum Energy Performance ‣ Minimal Actuator Placement with Optimal Control Constraints") using the integrator chain in Fig. 1, where we let

<!-- chunk {"id": "body-0039", "role": "body", "section": "IV-A The Case of an Integrator Chain", "weight": 1.0} -->

We first run Algorithm 2 ‣ III Minimal Actuator Sets with Constrained Minimum Energy Performance ‣ Minimal Actuator Placement with Optimal Control Constraints") with $E\leftarrow{v^{T}\Gamma_{\{ 1,5\}}^{- 1}v}$ and ${a,c}\leftarrow.001$ and examine the transfer from ${x{}}\leftarrow{\lbrack 0,0,0,0,0\rbrack}^{T}$ to ${x{}}\leftarrow{\lbrack 1,1,1,1,1\rbrack}^{T}$. The algorithm returned the actuator set $\{ 1,4\}$. As expected, node $1$ is chosen, and this remains true for any other value of $x{}$, since for a chain network to be controllable, it is necessary and sufficient that node $1$ be actuated. Additionally, $\{ 1,4\}$ is the exact best actuator set for achieving this transfer.

<!-- chunk {"id": "body-0040", "role": "body", "section": "IV-A The Case of an Integrator Chain", "weight": 1.0} -->

This is true because using MATLAB^®^ we can compute

<!-- chunk {"id": "body-0041", "role": "body", "section": "IV-A The Case of an Integrator Chain", "weight": 1.0} -->

Hence, node $1$ alone does not satisfy the upper bound $E$, while $v^{T}\Gamma_{\{ 1,4\}}^{- 1}v$ not only satisfies this bound, but it also takes the smallest value among all the actuators sets of cardinality two that induce controllability. Therefore, $\{ 1,4\}$ is the best minimal actuator set to achieve the given transfer.

<!-- chunk {"id": "body-0042", "role": "body", "section": "IV-A The Case of an Integrator Chain", "weight": 1.0} -->

Next, we set ${x{}}\leftarrow{\lbrack 0,0,0,1,0\rbrack}^{T}$ in Algorithm 2 ‣ III Minimal Actuator Sets with Constrained Minimum Energy Performance ‣ Minimal Actuator Placement with Optimal Control Constraints"), which led again to the selection $\{ 1,4\}$, as one would expect for any transfer that involves only the movement of the fourth node, while controllability is desired. In other words, even though we chose $E\leftarrow{v^{T}\Gamma_{\{ 1,5\}}^{- 1}v}$, Algorithm 2 ‣ III Minimal Actuator Sets with Constrained Minimum Energy Performance ‣ Minimal Actuator Placement with Optimal Control Constraints") respected this energy bound and with the best possible actuator set for the given transfer, which is $\{ 1,4\}$, as verified in the following

<!-- chunk {"id": "body-0043", "role": "body", "section": "IV-A The Case of an Integrator Chain", "weight": 1.0} -->

Moreover, note that although node $1$ is selected as an actuator, in this case its corresponding input signal is zero. Thus, one may choose not to implement an actuator at this node, at the expense, however, of losing the overall network controllability. This observation motivates the analysis of (I) when no controllability constraint is placed on the end actuator set.

<!-- chunk {"id": "body-0044", "role": "body", "section": "IV-A The Case of an Integrator Chain", "weight": 1.0} -->

Finally, by setting $E$ large enough in Algorithm 2 ‣ III Minimal Actuator Sets with Constrained Minimum Energy Performance ‣ Minimal Actuator Placement with Optimal Control Constraints"), so that any actuator set respects this energy bound, we observe that only node $1$ is selected, as expected for the satisfaction of the controllability constraint.

<!-- chunk {"id": "body-0045", "role": "body", "section": "IV-B Erdős-Rényi Random Networks", "weight": 1.0} -->

Erdős-Rényi random graphs are commonly used to model real-world networked systems. According to this model, each edge is included in the generated graph with some probability $p$, independently of every other edge.

<!-- chunk {"id": "body-0046", "role": "body", "section": "IV-B Erdős-Rényi Random Networks", "weight": 1.0} -->

We implemented this model for varying network sizes $n$, as shown in Fig. 2, where the directed edge probabilities were set to $p = {{2{\log{(n)}}}/n}$, following. In particular, we first generated the binary adjacency matrices for each network size so that every edge is present independently with probability $p$, and then we replaced every non-zero entry with an independent standard normal variable to generate a randomly weighted graph.

<!-- chunk {"id": "body-0047", "role": "body", "section": "IV-B Erdős-Rényi Random Networks", "weight": 1.0} -->

To avoid the computational difficulties associated with the integral equation we worked with the controllability Gramian instead, which for a stable system can be efficiently calculated from the Lyapunov equation ${{AG} + {GA^{T}}} = {- {BB^{T}}}$ and is given in closed-form by

<!-- chunk {"id": "body-0048", "role": "body", "section": "IV-B Erdős-Rényi Random Networks", "weight": 1.0} -->

Using the controllability Gramian in corresponds to the minimum state transfer energy with no time constraints. Therefore, we stabilized each random instances of $A$ by subtracting $1.1$ times the real part of their right-most eigenvalue and then we used the MATLAB^®^ function gram to compute the corresponding controllability Gramians.

<!-- chunk {"id": "body-0049", "role": "body", "section": "IV-B Erdős-Rényi Random Networks", "weight": 1.0} -->

Next, we set $x_{0}$ to be the zero vector and $x_{1}$ the vector of all ones. We also set $c\leftarrow 0.1$ and $a\leftarrow 1$. Finally, for each instance of $n$ we first computed the corresponding lower bound of $E$ so that (I) is feasible, $v^{T}G_{\mathcal{V}}^{- 1}v$, and then run Algorithm 2 ‣ III Minimal Actuator Sets with Constrained Minimum Energy Performance ‣ Minimal Actuator Placement with Optimal Control Constraints") for $E$ equal to $kv^{T}G_{\mathcal{V}}^{- 1}v$, where $k$ ranged from $2$ to $2^{25}$.

<!-- chunk {"id": "body-0050", "role": "body", "section": "IV-B Erdős-Rényi Random Networks", "weight": 1.0} -->

The number of selected actuator nodes by Algorithm 2 ‣ III Minimal Actuator Sets with Constrained Minimum Energy Performance ‣ Minimal Actuator Placement with Optimal Control Constraints") for each $n$ with respect to $k$ is shown in Fig. 2. We observe that as $k$ increases the number of actuators decreases, as one would expect when the energy bound of (I) is relaxed. In addition, we notice that for $k$ large enough, so that (I) becomes equivalent to the minimal controllability problem of, the number of chosen actuators is one, as it was generally observed in for a similar set of simulations.

<!-- chunk {"id": "body-0051", "role": "body", "section": "Concluding Remarks", "weight": 1.0} -->

We introduced the problem of minimal actuator placement in a linear system so that a bound on the minimum control effort for a given state transfer is satisfied while controllability is ensured. This problem was shown to be NP-hard and to have a supermodular structure. Moreover, an efficient algorithm was provided for its solution. Finally, the efficiency of this algorithm was illustrated over large Erdős-Rényi random networks. Our future work is focused on investigating the case where no controllability constraint is placed on the end actuator set, as well as, on exploring the effects that the network topology has on this selection.
