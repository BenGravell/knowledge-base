<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

From Convex Optimization to MDPs: A Review of First-Order, Second-Order and Quasi-Newton Methods for MDPs

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

In this paper we present a review of the connections between classical algorithms for solving Markov Decision Processes (MDPs) and classical gradient-based algorithms in convex optimization. Some of these connections date as far back as the 1980s, but they have gained momentum in recent years and have lead to faster algorithms for solving MDPs. In particular, two of the most popular methods for solving MDPs, Value Iteration and Policy Iteration, can be linked to first-order and second-order methods in convex optimization. In addition, recent results in quasi-Newton methods lead to novel algorithms for MDPs, such as Anderson acceleration. By explicitly classifying algorithms for MDPs as first-order, second-order, and quasi-Newton methods, we hope to provide a better understanding of these algorithms, and, further expanding this analogy, to help to develop novel algorithms for MDPs, based on recent advances in convex optimization.

<!-- chunk {"id": "body-0003", "role": "body", "section": "Introduction", "weight": 1.5} -->

Markov Decision Process (MDP) is a common framework modeling dynamic optimization problems, with applications ranging from reinforcement learning to healthcare and wireless sensor networks. Most of the algorithms for computing an optimal control policy are variants of two algorithms: Value Iteration (VI) and Policy Iteration (PI). Over the last 40 years, a number of works have highlighted the strong connections between these algorithms and methods from convex optimization, even though computing an optimal policy is a non-convex problem. Most algorithms in convex optimization can naturally be classified as first-order, second-order and quasi-Newton methods, if the iterates rely on gradients and/or Hessian computations. The goal of this paper is to outline a unifying framework for the classification of algorithms for solving MDPs. In particular, we present a systematic review of the connections between Value Iteration and first-order methods, between Policy Iteration and second-order methods, and between variants of Value Iteration and quasi-Newton methods. We hope that this unifying view can help to develop novel fast algorithms for solving MDPs, by extending the latest advances in convex optimization to the MDP framework.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

On the other hand, solving MDPs through the lens of convex optimization motivates novel interesting questions and challenges in optimization, as the operators and objective functions do not satisfy classical structural properties (e.g, convexity and/or differentiability).

<!-- chunk {"id": "body-0005", "role": "body", "section": "Outline", "weight": 1.0} -->

We introduce the MDP framework as well as the classical Value Iteration and Policy Iteration algorithms in Section 2 ‣ From Convex Optimization to MDPs: A Review of First-Order, Second-Order and Quasi-Newton Methods for MDPs"). We highlight the recent connections between Value Iteration and first-order methods (Gradient Descent) in Section 3. The relations between Policy Iteration and second-order methods (Newton's method) are presented in Section 4. We review Anderson Value Iteration, a quasi-Newton methods for MDPs, in Section 5. For the sake of completeness, in Appendix A, we present a detailed review of the results for Gradient Descent (along with acceleration and momentum), Newton's method and quasi-Newton methods in convex optimization.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Notations", "weight": 1.0} -->

In this paper, $n$ and $A$ denote integers in $\mathbb{N}$. The notation $\Delta{(A)}$ refers to the simplex of size $A$. We write $\lbrack n\rbrack$ for the set $\{ 1,\ldots,n\}$.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Setting and notations", "weight": 1.0} -->

A (stationary) policy $\pi \in \left({\Delta{(A)}} \right)^{n}$ maps each state to a probability distribution over the set of actions $\mathbb{A}$. For each policy $\pi$, the value vector ${\mathbf{v}}^{\pi} \in {\mathbb{R}}^{n}$ is defined as where $(s_{t},a_{t})$ is the state-action pair visited at time $t$. From the dynamic programming principle, ${\mathbf{v}}^{\pi}$ satisfies the following recursion: where ${\mathbf{P}}_{sa} \in {\Delta{(n)}}$ is the probability distribution over the next state given a state-action pair $(s,a)$.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Setting and notations", "weight": 1.0} -->

We simply reformulate the previous equality as where ${{\mathbf{P}}_{\pi} \in {\mathbb{R}}^{n \times n}},{{\mathbf{r}}_{\pi} \in {\mathbb{R}}^{n}}$ are the transition matrix and the one-step expected reward vector induced by the policy $\pi$: The goal of the decision-maker is to compute a policy $\pi^{\ast}$ that maximizes the infinite horizon expected discounted reward, defined as ${{R{(\pi)}} = {{\mathbf{p}}_{0}^{\top}{\mathbf{v}}^{\pi}}}.$ In this review we focus on Value Iteration (VI) and Policy Iteration (PI) algorithms to compute an optimal policy; we refer the reader to Puterman for a detailed discussion about other algorithms.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Value Iteration", "weight": 1.0} -->

Value Iteration was introduced by Bellman.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Value Iteration", "weight": 1.0} -->

The value iteration (VI) algorithm is defined as follows: The following theorem gives the convergence rate and stopping criterion for VI ‣ From Convex Optimization to MDPs: A Review of First-Order, Second-Order and Quasi-Newton Methods for MDPs").

<!-- chunk {"id": "body-0011", "role": "body", "section": "Value Computation", "weight": 1.0} -->

The problem of computing the value vector of a policy is also crucial, see for instance the Policy Evaluation step in the Policy Iteration algorithm, presented in the next section. The operator $T_{\pi}:{{\mathbb{R}}^{n}\rightarrow{\mathbb{R}}^{n}}$ associated with a policy $\pi$ is defined as Note that $T_{\pi}$ is an affine operator and a contraction for $\parallel \cdot \parallel_{\infty}$. The unique fixed point of $T_{\pi}$ is ${\mathbf{v}}^{\pi}$, the value vector of the policy $\pi$.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Value Computation", "weight": 1.0} -->

Therefore, the following algorithm is called Value Computation (VC): For the same reason as Algorithm VI ‣ From Convex Optimization to MDPs: A Review of First-Order, Second-Order and Quasi-Newton Methods for MDPs"), the sequence of vectors $\left({T_{\pi}^{t}{({\mathbf{v}}_{0})}} \right)_{t \geq 0}$ generated by VC ‣ From Convex Optimization to MDPs: A Review of First-Order, Second-Order and Quasi-Newton Methods for MDPs") converges linearly to ${\mathbf{v}}^{\pi}$ with a rate of $\lambda$, for any initial vector ${\mathbf{v}}_{0}$.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Policy Iteration", "weight": 1.0} -->

Policy Iteration was developed by Howard and Bellman. The algorithm runs as follow.

<!-- chunk {"id": "body-0014", "role": "body", "section": "Policy Iteration", "weight": 1.0} -->

3: (Policy Evaluation) Choose vt = vπt the value vector of πt. 4: (Policy Improvement) Choose πt + 1 with πt + 1, s ∈ Δ (A) solving maxπ ∑a ∈ 𝔸πa (rs a + λ Ps a⊤ vt), ∀s ∈ 𝕊. 5: (Stopping Criterion) Stop when πt + 1 = πt. Algorithm 1 Policy Iteration (PI) In the Policy Improvement step, Policy Iteration computes $\pi_{t + 1}$ as a greedy one-step update, given the value vector ${\mathbf{v}}^{\pi_{t}}$ related to $\pi_{t}$. Prior to Ye, the proofs of convergence of Policy Iteration relied on the fact that the policies $\pi_{1},\ldots,\pi_{t}$ monotonically improve the objective function. In particular, the Policy Improvement step guarantees that $\pi_{t + 1}$ is a strictly better policy than $\pi_{t}$, unless $\pi_{t + 1} = \pi_{t}$.

<!-- chunk {"id": "body-0015", "role": "body", "section": "Policy Iteration", "weight": 1.0} -->

As there are only finitely many policies (in the case of finite numbers of states and actions sets), the Policy Iteration algorithm terminates. As a side note, Policy Iteration is equivalent to a block-wise update rule when running the simplex algorithm on the linear programming reformulation of MDPs.

<!-- chunk {"id": "body-0016", "role": "body", "section": "Policy Iteration", "weight": 1.0} -->

In Theorem 4.2 in Ye, the author proves that the number of iterations of Policy Iteration is bounded from above by Note that this bound does not depend of the order of magnitude of the rewards $r_{sa}$, so that the worst-case complexity of Policy Iteration is actually strongly polynomial (for fixed discount factor $\lambda$). It is remarkable that even though the proofs presented in Ye rely on simple tools from the theory of linear programming. These results have been further improved in Scherrer for MDPs and extended to two-player games in Hansen et al..

<!-- chunk {"id": "body-0017", "role": "body", "section": "Value Iteration as a first-order method", "weight": 1.0} -->

From Section 2.2 ‣ From Convex Optimization to MDPs: A Review of First-Order, Second-Order and Quasi-Newton Methods for MDPs"), finding an optimal policy is equivalent to solving ${\mathbf{v}} = {T{({\mathbf{v}})}}$. It has been noted since as far back as Bertsekas that the operator ${\mathbf{v}}\mapsto{\left( {{\mathbf{I}} - T} \right){({\mathbf{v}})}}$ can be treated as the gradient of an unknown function. We review here the results from Goyal and Grand-Clément, where the authors build upon this analogy to define first-order methods for MDPs, extend Nesterov's acceleration and Polyak's momentum to MDPs and present novel lower bounds on the performances of value iteration algorithms. We also review novel connections between Mirror Descent, Primal-Dual Algorithm, and Value Iteration at the end of this section. A review of the classical results for first-order methods in convex optimization can be found in Appendix A.1.

<!-- chunk {"id": "body-0018", "role": "body", "section": "First-order methods for MDPs", "weight": 1.0} -->

Considering that ${\mathbf{v}}\mapsto{\left( {{\mathbf{I}} - T} \right){({\mathbf{v}})}}$ as the gradient of an unknown function, Goyal and Grand-Clément define first-order methods for MDPs as follows.

<!-- chunk {"id": "body-0019", "role": "body", "section": "Choice of parameters", "weight": 1.0} -->

Recall that for a differentiable, $\mu$-strongly convex, $L$-Lipschitz continuous function $f:{{\mathbb{R}}^{n}\rightarrow{\mathbb{R}}}$, the following inequalities hold: for all vectors ${{{\mathbf{v}},{\mathbf{w}}} \in {\mathbb{R}}^{n}},$ In the case of the Bellman operator $T$, for any vectors ${{{\mathbf{v}},{\mathbf{w}}} \in {\mathbb{R}}^{n}},$ the triangle inequality gives In convex optimization, the constant $\mu$ and $L$ can be used to tune the step sizes of the algorithms. Because of the analogy between the last four equations, the choice of $\mu = {1 - \lambda}$ and $L = {1 + \lambda}$ will be used to tune the step sizes of the novel algorithms for MDPs, inspired from first-order methods in convex optimization.

<!-- chunk {"id": "body-0020", "role": "body", "section": "Choice of parameters", "weight": 1.0} -->

We also use the notation $\kappa = {\mu/L}$.

<!-- chunk {"id": "body-0021", "role": "body", "section": "Relaxed Value Iteration", "weight": 1.0} -->

For $\alpha > 0$, Goyal and Grand-Clément consider the following Relaxed Value Iteration (RVI) algorithm: Note the analogy with the Gradient Descent algorithm GD (presented in Appendix A.1), when ${\mathbf{v}}\mapsto{{({{\mathbf{I}} - T})}{({\mathbf{v}})}}$ is the gradient of an unknown function. RVI is also considered in Kushner and Kleinman; Porteus and Totten without an explicit connection to GD. Formal convergence guarantees are provided in Goyal and Grand-Clément; the main difficulty is the use of $\parallel \cdot \parallel_{\infty}$ instead of $\parallel \cdot \parallel_{2}$ in the properties that characterize the Bellman operator $T$.

<!-- chunk {"id": "body-0022", "role": "body", "section": "Nesterov Accelerated Value Iteration", "weight": 1.0} -->

Still considering ${\mathbf{v}} - {T{({\mathbf{v}})}}$ as the gradient of some unknown function, it is possible to write an Accelerated Value Iteration (AVI), building upon Accelerated Gradient Descent AGD (see Appendix A.1 for the exact definition and convergence rates of AGD). In particular, Goyal and Grand-Clément consider the following algorithm.

<!-- chunk {"id": "body-0023", "role": "body", "section": "Nesterov Accelerated Value Iteration", "weight": 1.0} -->

The choice of step sizes for AVI is the same as for AGD in convex optimization (e.g., Theorem A.4. ‣ Acceleration and Momentum in convex optimization. ‣ A.1 First-order methods ‣ Appendix A A short review of gradient-based methods in convex optimization ‣ From Convex Optimization to MDPs: A Review of First-Order, Second-Order and Quasi-Newton Methods for MDPs") in Appendix A.1) but here ${\mu = {({1 - \lambda})}},{L = {({1 + \lambda})}}$. This yields

<!-- chunk {"id": "body-0024", "role": "body", "section": "Polyak's Momentum Value Iteration", "weight": 1.0} -->

It is also possible to write a Momentum Value Iteration algorithm (MVI): The same choice as for Momentum Gradient Descent (MGD, see Theorem A.4. ‣ Acceleration and Momentum in convex optimization. ‣ A.1 First-order methods ‣ Appendix A A short review of gradient-based methods in convex optimization ‣ From Convex Optimization to MDPs: A Review of First-Order, Second-Order and Quasi-Newton Methods for MDPs") in Appendix A.1)

<!-- chunk {"id": "body-0025", "role": "body", "section": "Properties for non-affine operators", "weight": 1.0} -->

Unfortunately, algorithms AVI and MVI may diverge on some MDP instances. In all generality, the analysis of AVI and MVI is related to the computation of the joint spectral radius of a specific set of matrices, which is usually a hard problem. Vieillard et al. obtain convergence of a momentum variant of $Q$-learning, under a strong assumption on the sequence of iterates (Assumption 1 in Vieillard et al., closely related to the joint spectral radius of the visited matrices), and study this assumption empirically. Despite this, the analysis of the case where $T$ is an affine operator reveals some interesting connections on the convergence properties of AVI and MVI compared to AGD and MGD.

<!-- chunk {"id": "body-0026", "role": "body", "section": "Convergence rate for affine operators", "weight": 1.0} -->

Let $\pi$ be a policy and consider Algorithm AVI and Algorithm MVI where the Bellman operator $T$ is replaced with the Bellman recursion operator $T_{\pi}$, defined in (2.2 ‣ From Convex Optimization to MDPs: A Review of First-Order, Second-Order and Quasi-Newton Methods for MDPs")). Goyal and Grand-Clément refer to these new algorithms as Accelerated Value Computation (AVC) and Momentum Value Computation (MVC), in reference to Algorithm VC ‣ From Convex Optimization to MDPs: A Review of First-Order, Second-Order and Quasi-Newton Methods for MDPs"). Under conditions on the spectral radius of ${\mathbf{P}}_{\pi}$, Goyal and Grand-Clément provide the following convergence rates.

<!-- chunk {"id": "body-0027", "role": "body", "section": "Lower bound on any first-order method for MDP", "weight": 1.0} -->

While in convex optimization, AGD achieves the best worst-case convergence rate over the class of smooth, convex functions, this is not the case for AVI for MDPs. In particular, Goyal and Grand-Clément prove the following lower-bound on any first-order method for MDPs.

<!-- chunk {"id": "body-0028", "role": "body", "section": "Connections with mirror descent and other first-order methods", "weight": 1.0} -->

We review here some other algorithms from first-order convex optimization that have been recently used to design novel Value Iteration algorithms.

<!-- chunk {"id": "body-0029", "role": "body", "section": "Mirror Descent", "weight": 1.0} -->

The authors in Geist et al. show that adding a regularization term in the Bellman update (2.1 ‣ From Convex Optimization to MDPs: A Review of First-Order, Second-Order and Quasi-Newton Methods for MDPs")) yields an algorithm resembling Mirror Descent (MD,). In particular, let ${\mathbf{c}}_{s,{\mathbf{v}}} = \left({r_{sa} + {\lambda{\mathbf{P}}_{sa}^{\top}{\mathbf{v}}}} \right)_{a \in {\mathbb{A}}} \in {\mathbb{R}}^{n}$ for ${\mathbf{v}} \in {\mathbb{R}}^{n}$.

<!-- chunk {"id": "body-0030", "role": "body", "section": "Mirror Descent", "weight": 1.0} -->

Geist et al. define an algorithm resembling Mirror Descent and Value Iteration MD-VI as follows: It is also possible to replace the update on the value vector by i.e., to include the regularization term in the update on ${\mathbf{v}}_{t + 1}$. Geist et al. provide the convergence rate of MD-VI and a detailed discussion on the connection of MD-VI and other classical algorithms for reinforcement learning, e.g., Trust Region Policy Optimization (TRPO, see Section 5.1 in Geist et al.).

<!-- chunk {"id": "body-0031", "role": "body", "section": "Other approaches", "weight": 1.0} -->

(Stochastic) Mirror Descent can also be used to solve the linear programming formulation of MDPs in min-max form. In Grand-Clément and Kroer the authors adapt the Primal-Dual Algorithm of Chambolle and Pock for solving robust MDPs and distributionally robust MDPs. While these papers provide new algorithms for solving MDPs, they do not highlight a novel connection between classical algorithms for MDPs and classical algorithms for convex optimization. The interested reader can find a concise presentation of connections between Franck-Wolfe algorithm, Mirror Descent, dual averaging and algorithms for reinforcement learning in the review of Vieillard et al.. We note that the algorithms for MDPs in Vieillard et al. are optimizing in the space of policies ($\pi \in \left( {\Delta{(A)}} \right)^{n}$), thereby relying on methods from constrained convex optimization.

<!-- chunk {"id": "body-0032", "role": "body", "section": "Other approaches", "weight": 1.0} -->

In contrast, in this review we consider that Value Iteration and Policy Iteration are optimizing over the space of value vectors (${\mathbf{v}} \in {\mathbb{R}}^{n}$), thereby relying on methods from unconstrained convex optimization.

<!-- chunk {"id": "body-0033", "role": "body", "section": "Newton-Raphson with the Bellman operator", "weight": 1.0} -->

The relation between Policy Iteration and Newton-Raphson method dates as far back as Kalaba and Pollatschek and Avi-Itzhak. We adapt here the presentation of Puterman and Brumelle. A review of the classical results for second-order methods in convex optimization can be found in Appendix A.2.

<!-- chunk {"id": "body-0034", "role": "body", "section": "Jacobian of the gradient operator", "weight": 1.0} -->

We introduce the following notations, which greatly simplify the exposition of the results. Let us write $F:{{\mathbf{v}}\mapsto{\left( {{\mathbf{I}} - T} \right){({\mathbf{v}})}}}$. Note that in Section 3, we interpreted $F$ as the gradient of an unknown function $f:{{\mathbb{R}}^{n}\rightarrow{\mathbb{R}}}$. In order to develop second-order methods, one uses second-order information, i.e., the Hessian of the unknown function $f:{{\mathbb{R}}^{n}\rightarrow{\mathbb{R}}}$, which is the Jacobian of the gradient operator $F:{{\mathbb{R}}^{n}\rightarrow{\mathbb{R}}^{n}}$. However, the map $F$ may not be differentiable at any vector $\mathbf{v}$.

<!-- chunk {"id": "body-0035", "role": "body", "section": "Jacobian of the gradient operator", "weight": 1.0} -->

This is because the Bellman operator itself is not necessarily differentiable, as the maximum of some linear forms. Still, it is possible to give a closed-form expression for the Jacobian of $F$, where it is differentiable. In particular, we have the following lemma.

<!-- chunk {"id": "body-0036", "role": "body", "section": "Smoothing the Bellman operator", "weight": 1.0} -->

Replacing the $\max$ in the Bellman operator with a log-sum-exp reformulation, Kamanchi et al. obtain convergence of a log-sum-exp version of Policy Iteration directly from the convergence of the Newton-Raphson method. In particular, for $\beta > 0$, define $T_{\beta}:{{\mathbb{R}}^{n}\rightarrow{\mathbb{R}}^{n}}$ such that The authors in Kamanchi et al. prove the following results. Note that the same type of results can be obtained by replacing the log-sum-exp transformation with a soft-max.

<!-- chunk {"id": "body-0037", "role": "body", "section": "Quasi-Newton method for MDP: Anderson acceleration", "weight": 1.0} -->

Specific applications of Anderson accelerations to MDPs has been considered in Geist and Scherrer and Zhang et al.. We give here some motivations, the relation with Anderson acceleration in convex optimization and review the convergence results of Zhang et al.. A review of the classical results for quasi-Newton methods in convex optimization can be found in Appendix A.3.

<!-- chunk {"id": "body-0038", "role": "body", "section": "Relation to Anderson Acceleration in Convex Optimization", "weight": 1.0} -->

Zhang et al. present a stabilized version of the vanilla Anderson algorithm AndVI-I. This results in ${\lim_{t\rightarrow{+ \infty}}{\mathbf{v}}_{t}} = {\mathbf{v}}^{\ast}$, but the convergence rate is not known (Theorem 3.1 in Zhang et al. ), even though the algorithm enjoys good empirical performances, typically outperforming VI ‣ From Convex Optimization to MDPs: A Review of First-Order, Second-Order and Quasi-Newton Methods for MDPs"). Note that this is the first result on the convergence of Anderson Acceleration, without differentiability of the operator $T$ (and with fixed-memory, i.e., with $m$ fixed). There are many other quasi-Newton methods aside from Anderson acceleration, see Appendix A.3 for a short review of some classical methods. Note that in the practical implementation of Anderson acceleration, one typically chooses $1 \leq m \leq 5$. Therefore, algorithms based on information on only the last two iterates may still perform well.

<!-- chunk {"id": "body-0039", "role": "body", "section": "Relation to Anderson Acceleration in Convex Optimization", "weight": 1.0} -->

In particular, it could be possible to develop algorithms for MDPs, based on Broyden or BFGS updates. The convergence of AndVI-II for non-differentiable operators (or a stabilized version of AndVI-II) also remains an open question.
