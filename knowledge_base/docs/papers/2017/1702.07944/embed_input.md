<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Stochastic Variance Reduction Methods for Policy Evaluation

Topics include Datasets, Benchmarks, Learning, Variance reduction, Saddle point, Reinforcement learning.

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Policy evaluation is a crucial step in many reinforcement-learning procedures, which estimates a value function that predicts states' long-term value under a given policy. In this paper, we focus on policy evaluation with linear function approximation over a fixed dataset. We first transform the empirical policy evaluation problem into a (quadratic) convex-concave saddle point problem, and then present a primal-dual batch gradient method, as well as two stochastic variance reduction methods for solving the problem. These algorithms scale linearly in both sample size and feature dimension. Moreover, they achieve linear convergence even when the saddle-point problem has only strong concavity in the dual variables but no strong convexity in the primal variables. Numerical experiments on benchmark problems demonstrate the effectiveness of our methods.

<!-- chunk {"id": "body-0003", "role": "body", "section": "Introduction", "weight": 1.5} -->

Reinforcement learning (RL) is a powerful learning paradigm for sequential decision making. An RL agent interacts with the environment by repeatedly observing the current state, taking an action according to a certain policy, receiving a reward signal and transitioning to a next state. A policy specifies which action to take given the current state. *Policy evaluation* estimates a value function that predicts expected cumulative reward the agent would receive by following a fixed policy starting at a certain state. In addition to quantifying long-term values of states, which can be of interest on its own, value functions also provide important information for the agent to optimize its policy. For example, *policy-iteration* algorithms iterate between policy-evaluation steps and policy-*improvement* steps, until a (near-)optimal policy is found. Therefore, estimating the value function efficiently and accurately is essential in RL.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

There has been substantial work on policy evaluation, with *temporal-difference* (TD) methods being perhaps the most popular. These methods use the Bellman equation to bootstrap the estimation process. Different cost functions are formulated to exploit this idea, leading to different policy evaluation algorithms; see Dann et al. for a comprehensive survey. In this paper, we study policy evaluation by minimizing the mean squared projected Bellman error (MSPBE) with linear approximation of the value function. We focus on the batch setting where a fixed, finite dataset is given. This fixed-data setting is not only important in itself, but also an important component in other RL methods such as *experience replay*.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

The finite-data regime makes it possible to solve policy evaluation more efficiently with recently developed fast optimization methods based on *stochastic variance reduction*, such as SVRG and SAGA. For minimizing strongly convex functions with a finite-sum structure, such methods enjoy the same low computational cost per iteration as the classical stochastic gradient method, but also achieve fast, linear convergence rates (i.e., exponential decay of the optimality gap in the objective). However, they cannot be applied directly to minimize the MSPBE, whose objective does not have the finite-sum structure. In this paper, we overcome this obstacle by transforming the empirical MSPBE problem to an *equivalent* convex-concave saddle-point problem that possesses the desired finite-sum structure.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

In the saddle-point problem, we consider the model parameters as the primal variables, which are coupled with the dual variables through a bilinear term. Moreover, without an $\ell_{2}$-regularization on the model parameters, the objective is only strongly concave in the dual variables, but *not* in the primal variables. We propose a primal-dual batch gradient method, as well as two stochastic variance-reduction methods based on SVRG and SAGA, respectively. Surprisingly, we show that when the coupling matrix is full rank, these algorithms achieve linear convergence in both the primal and dual spaces, despite the lack of strong convexity of the objective in the primal variables. Our results also extend to *off-policy* learning and TD with *eligibility traces*.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

We note that Balamurugan & Bach have extended both SVRG and SAGA to solve convex-concave saddle-point problems with linear-convergence guarantees. The main difference between our results and theirs are

<!-- chunk {"id": "body-0008", "role": "body", "section": "Introduction", "weight": 1.5} -->

Linear convergence in Balamurugan & Bach relies on the assumption that the objective is strongly convex in the primal variables and strongly concave in the dual. Our results show, somewhat surprisingly, that only one of them is necessary if the primal-dual coupling is bilinear and the coupling matrix is full rank. In fact, we are not aware of similar previous results even for the primal-dual batch gradient method, which we show in this paper.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Introduction", "weight": 1.5} -->

Even if a strongly convex regularization on the primal variables is introduced to the MSPBE objective, the algorithms in Balamurugan & Bach cannot be applied efficiently. Their algorithms require that the proximal mappings of the strongly convex and concave regularization functions be computed efficiently. In our saddle-point formulation, the strong concavity of the dual variables comes from a quadratic function defined by the feature covariance matrix, which cannot be inverted efficiently and makes the proximal mapping costly to compute. Instead, our algorithms only use its (stochastic) gradients and hence are much more efficient.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Introduction", "weight": 1.5} -->

We compare various gradient based algorithms on a Random MDP and Mountain Car data sets. The experiments demonstrate the effectiveness of our proposed methods.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Mean squared projected Bellman error (MSPBE)", "weight": 1.0} -->

One approach to scale up when the state space size $|\mathcal{S}|$ is large or infinite is to use a linear approximation for $V^{\pi}$. Formally, we use a feature map $\phi:{\mathcal{S}\rightarrow{\mathbb{R}}^{d}}$ and approximate the value function by ${{\hat{V}}^{\pi}(s)} = {\phi{(s)}^{T}\theta}$, where $\theta \in {\mathbb{R}}^{d}$ is the model parameter to be estimated.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Mean squared projected Bellman error (MSPBE)", "weight": 1.0} -->

where $\Xi$ is a diagonal matrix with diagonal elements being the stationary distribution over $\mathcal{S}$ induced by the policy $\pi$, and $\Pi$ is the weighted projection matrix onto the linear space spanned by ${\phi{}},\ldots,{\phi{({|\mathcal{S}|})}}$, that is,

<!-- chunk {"id": "body-0013", "role": "body", "section": "Mean squared projected Bellman error (MSPBE)", "weight": 1.0} -->

where $\Phi \triangleq {\lbrack{\phi^{T}{}},\ldots,{\phi^{T}{({|\mathcal{S}|})}}\rbrack}$ is the matrix obtained by stacking the feature vectors row by row. Substituting (3 ‣ 2 Preliminaries ‣ Stochastic Variance Reduction Methods for Policy Evaluation")) and into (2 ‣ 2 Preliminaries ‣ Stochastic Variance Reduction Methods for Policy Evaluation")), we obtain

<!-- chunk {"id": "body-0014", "role": "body", "section": "Mean squared projected Bellman error (MSPBE)", "weight": 1.0} -->

with properly defined $A$, $b$ and $C$, described as follows. Suppose the MDP under policy $\pi$ settles at its stationary distribution and generates an infinite transition sequence $\left\{ \left( s_{t},a_{t},r_{t},s_{t + 1} \right) \right\}_{t = 1}^{\infty}$, where $s_{t}$ is the current state, $a_{t}$ is the action, $r_{t}$ is the reward, and $s_{t + 1}$ is the next state. Then with the definitions $\phi_{t} \triangleq {\phi{(s_{t})}}$ and $\phi_{t}^{\prime} \triangleq {\phi{(s_{t + 1})}}$, we have

<!-- chunk {"id": "body-0015", "role": "body", "section": "Mean squared projected Bellman error (MSPBE)", "weight": 1.0} -->

where ${\mathbb{E}}{\lbrack \cdot \rbrack}$ are with respect to the stationary distribution. Many TD solutions converge to a minimizer of MSPBE in the limit.

<!-- chunk {"id": "body-0016", "role": "body", "section": "Empirical MSPBE", "weight": 1.0} -->

In practice, quantities in (4 ‣ 2 Preliminaries ‣ Stochastic Variance Reduction Methods for Policy Evaluation")) are often unknown, and we only have access to a finite dataset with $n$ transitions $\mathcal{D} = \left\{ \left( s_{t},a_{t},r_{t},s_{t + 1} \right) \right\}_{t = 1}^{n}$. By replacing the unknown statistics with their finite-sample estimates, we obtain the Empirical MSPBE, or EM-MSPBE. Specifically, let

<!-- chunk {"id": "body-0017", "role": "body", "section": "Empirical MSPBE", "weight": 1.0} -->

where $\rho \geq 0$ is a regularization factor.

<!-- chunk {"id": "body-0018", "role": "body", "section": "Empirical MSPBE", "weight": 1.0} -->

Observe that is a (regularized) weighted least squares problem. Assuming $\hat{C}$ is invertible, its optimal solution is

<!-- chunk {"id": "body-0019", "role": "body", "section": "Empirical MSPBE", "weight": 1.0} -->

Computing $\theta^{\star}$ directly requires $O{({nd^{2}})}$ operations to form the matrices $\hat{A}$, $\hat{b}$ and $\hat{C}$, and then $O{(d^{3})}$ operations to complete the calculation. This method, known as least-squares temporal difference or LSTD, can be very expensive when $n$ and $d$ are large. One can also skip forming the matrices explicitly and compute $\theta^{\star}$ using $n$ recusive rank-one updates. Since each rank-one update costs $O{(d^{2})}$, the total cost is $O{({nd^{2}})}$.

<!-- chunk {"id": "body-0020", "role": "body", "section": "Empirical MSPBE", "weight": 1.0} -->

In the sequel, we develop efficient algorithms to minimize EM-MSPBE by using stochastic variance reduction methods, which samples one $(\phi_{t},\phi_{t}^{\prime})$ per update without pre-computing $\hat{A}$, $\hat{b}$ and $\hat{C}$. These algorithms not only maintain a low $O{(d)}$ per-iteration computation cost, but also attain fast linear convergence rates with a $\log{({1/\epsilon})}$ dependence on the desired accuracy $\epsilon$.

<!-- chunk {"id": "body-0021", "role": "body", "section": "Saddle-Point Formulation of EM-MSPBE", "weight": 1.0} -->

Our algorithms (in Section 5) are based on the stochastic variance reduction techniques developed for minimizing a finite sum of convex functions, more specifically, SVRG and SAGA. They deal with problems of the form

<!-- chunk {"id": "body-0022", "role": "body", "section": "Saddle-Point Formulation of EM-MSPBE", "weight": 1.0} -->

where each $f_{i}$ is convex. We immediately notice that the EM-MSPBE in *cannot* be put into such a form, even though the matrices $\hat{A}$, $\hat{b}$ and $\hat{C}$ have the finite-sum structure given. Thus, extending variance reduction techniques to EM-MSPBE minimization is not straightforward.

<!-- chunk {"id": "body-0023", "role": "body", "section": "Saddle-Point Formulation of EM-MSPBE", "weight": 1.0} -->

With this relation, we can rewrite EM-MSPBE in as

<!-- chunk {"id": "body-0024", "role": "body", "section": "Saddle-Point Formulation of EM-MSPBE", "weight": 1.0} -->

so that minimizing EM-MSPBE is equivalent to solving

<!-- chunk {"id": "body-0025", "role": "body", "section": "Saddle-Point Formulation of EM-MSPBE", "weight": 1.0} -->

Therefore, minimizing the EM-MSPBE is equivalent to solving the saddle-point problem, which is convex in the primal variable $\theta$ and concave in the dual variable $w$. Moreover, it has a finite-sum structure similar to.

<!-- chunk {"id": "body-0026", "role": "body", "section": "Saddle-Point Formulation of EM-MSPBE", "weight": 1.0} -->

Liu et al. and Valcarcel Macua et al. independently showed that the GTD2 algorithm is indeed a *stochastic gradient* method for solving the saddle-point problem, although they obtained the saddle-point formulation with different derivations. More recently, Dai et al. used the conjugate function approach to obtain saddle-point formulations for a more general class of problems and derived primal-dual stochastic gradient algorithms for solving them. However, these algorithms have sublinear convergence rates, which leaves much room to improve when applied to problems with finite datasets. Recently, Lian et al. developed SVRG methods for a general finite-sum composition optimization that achieve linear convergence rate. Different from our methods, their stochastic gradients are biased and they have worse dependency on the condition numbers ($\kappa^{3}$ and $\kappa^{4}$).

<!-- chunk {"id": "body-0027", "role": "body", "section": "Assumption 1", "weight": 1.0} -->

$\hat{A}$ has full rank, $\hat{C}$ is strictly positive definite, and the feature vector $\phi_{t}$ is uniformly bounded.

<!-- chunk {"id": "body-0028", "role": "body", "section": "Assumption 1", "weight": 1.0} -->

Under mild regularity conditions, we have $\hat{A}$ and $\hat{C}$ converge in probability to $A$ and $C$ defined in (4 ‣ 2 Preliminaries ‣ Stochastic Variance Reduction Methods for Policy Evaluation")), respectively. Thus, if the true statistics $A$ is non-singular and $C$ is positive definite, and we have enough training samples, these assumptions are usually satisfied. They have been widely used in previous works on gradient-based algorithms.

<!-- chunk {"id": "body-0029", "role": "body", "section": "Assumption 1", "weight": 1.0} -->

A direct consequence of Assumption 1 is that $\theta^{\star}$ in is the unique minimizer of the EM-MSPBE, even without any strongly convex regularization on $\theta$ (i.e., even if $\rho = 0$). However, if $\rho = 0$, then the Lagrangian $\mathcal{L}{(\theta,w)}$ is only strongly concave in $w$, but not strongly convex in $\theta$. In this case, we will show that non-singularity of the coupling matrix $\hat{A}$ can "pass" an implicit strong convexity on $\theta$, which is exploited by our algorithms to obtain linear convergence in both the primal and dual spaces.

<!-- chunk {"id": "body-0030", "role": "body", "section": "Primal-Dual Batch Gradient Method", "weight": 1.0} -->

Before diving into the stochastic variance reduction algorithms, we first present Algorithm 1, which is a primal-dual *batch* gradient (PDBG) algorithm for solving the saddle-point problem.

<!-- chunk {"id": "body-0031", "role": "body", "section": "Primal-Dual Batch Gradient Method", "weight": 1.0} -->

Some notation is needed in order to characterize the convergence rate of Algorithm 1. For any symmetric and positive definite matrix $S$, let $\lambda_{\max}{(S)}$ and $\lambda_{\min}{(S)}$ denote its maximum and minimum eigenvalues respectively, and define its condition number to be ${\kappa{(S)}} \triangleq {{{\lambda_{\max}{(S)}}/\lambda_{\min}}{(S)}}$.

<!-- chunk {"id": "body-0032", "role": "body", "section": "Primal-Dual Batch Gradient Method", "weight": 1.0} -->

By Assumption 1, we have $L_{\rho} \geq \mu_{\rho} > 0$. The following theorem is proved in Appendix B.

<!-- chunk {"id": "body-0033", "role": "body", "section": "Stochastic Variance Reduction Methods", "weight": 1.0} -->

If we replace $B{(\theta,w)}$ in Algorithm 1 (line 2) by the stochastic gradient $B_{t}{(\theta,w)}$, then we recover the GTD2 algorithm of Sutton et al., applied to a fixed dataset, possibly with *multiple passes*. It has a low per-iteration cost but a slow, *sublinear* convergence rate. In this section, we provide two stochastic variance reduction methods and show they achieve fast linear convergence.

<!-- chunk {"id": "body-0034", "role": "body", "section": "SVRG for policy evaluation", "weight": 1.0} -->

Algorithm 2 is adapted from the stochastic variance reduction gradient (SVRG) method. It uses two layers of loops and maintains two sets of parameters $(\overset{\sim}{\theta},\overset{\sim}{w})$ and $(\theta,w)$. In the outer loop, the algorithm computes a full gradient $B{(\overset{\sim}{\theta},\overset{\sim}{w})}$ using $(\overset{\sim}{\theta},\overset{\sim}{w})$, which takes $O{({nd})}$ operations.

<!-- chunk {"id": "body-0035", "role": "body", "section": "SVRG for policy evaluation", "weight": 1.0} -->

Since $B{(\overset{\sim}{\theta},\overset{\sim}{w})}$ is computed once during each iteration of the outer loop with cost $O{({nd})}$ (as explained at the end of Section 4), and each of the $N$ iterations of the inner loop cost $O{(d)}$ operations, the total computational cost of for each outer loop is $O{({{nd} + {Nd}})}$. We will present the overall complexity analysis of Algorithm 2 in Section 5.3.

<!-- chunk {"id": "body-0036", "role": "body", "section": "SAGA for policy evaluation", "weight": 1.0} -->

0: initial point (θ,w), step sizes σθ and σw, and number of iterations M.
1: Compute each gt = Bt (θ,w) for t = 1, …, n.
2: Compute $B = {B{(\theta,w)}} = {\frac{1}{n}{\sum_{t = 1}^{n}g_{t}}}$.
4: Sample an index tm from {1,⋯,n}.
5: Compute htm = Btm (θ,w).
\end{bmatrix}\leftarrow{\begin{bmatrix}
\end{bmatrix} - {\begin{bmatrix}
\sigma_{\theta} &amp; 0 \\
\end{bmatrix}\left( {{B + h_{t_{m}}} - g_{t_{m}}} \right)}}$.
Algorithm 3 SAGA for Policy Evaluation

<!-- chunk {"id": "body-0037", "role": "body", "section": "SAGA for policy evaluation", "weight": 1.0} -->

The second stochastic variance reduction method for policy evaluation is adapted from SAGA; see Algorithm 3. It uses a single loop, and maintains a single set of parameters $(\theta,w)$. Algorithm 3 starts by first computing each component gradients $g_{t} = {B_{t}{(\theta,w)}}$ at the initial point, and also form their average $B = {\sum_{t}^{n}g_{t}}$. At each iteration, the algorithm randomly picks an index $t_{m} \in {\{ 1,\ldots,n\}}$ and computes the stochastic gradient $h_{t_{m}} = {B_{t_{m}}{(\theta,w)}}$.

<!-- chunk {"id": "body-0038", "role": "body", "section": "SAGA for policy evaluation", "weight": 1.0} -->

Then, it updates $(\theta,w)$ using a variance reduced stochastic gradient: ${B + h_{t_{m}}} - g_{t_{m}}$, where $g_{t_{m}}$ is the previously computed stochastic gradient using the $t_{m}$-th sample (associated with certain past values of $\theta$ and $w$). Afterwards, it updates the batch gradient estimate $B$ as $B + {\frac{1}{n}{({h_{t_{m}} - g_{t_{m}}})}}$ and replaces $g_{t_{m}}$ with $h_{t_{m}}$.

<!-- chunk {"id": "body-0039", "role": "body", "section": "SAGA for policy evaluation", "weight": 1.0} -->

As Algorithm 3 proceeds, different vectors $g_{t}$ are computed using different values of $\theta$ and $w$ (depending on when the index $t$ was sampled). So in general we need to store all vectors $g_{t}$, for $t = {1,\ldots,n}$, to facilitate individual updates, which will cost additional $O{({nd})}$ storage. However, by exploiting the rank-one structure, we only need to store three scalars ${({\phi_{t} - \gamma_{\phi}^{\prime}})}^{T}\theta$, ${({\phi_{t} - \gamma_{\phi}^{\prime}})}^{T}w$, and $\phi_{t}^{T}w$, and form $g_{t_{m}}$ on the fly using $O{(d)}$ computation. Overall, each iteration of SAGA costs $O{(d)}$ operations.

<!-- chunk {"id": "body-0040", "role": "body", "section": "Theoretical analyses of SVRG and SAGA", "weight": 1.0} -->

In order to study the convergence properties of SVRG and SAGA for policy evaluation, we introduce a smoothness parameter $L_{G}$ based on the stochastic gradients $B_{t}{(\theta,w)}$. Let $\beta = {\sigma_{w}/\sigma_{\theta}}$ be the ratio between the primal and dual step-sizes, and define a pair of weighted Euclidean norms

<!-- chunk {"id": "body-0041", "role": "body", "section": "Theoretical analyses of SVRG and SAGA", "weight": 1.0} -->

This definition is similar to the smoothness constant $\overline{L}$ used in Balamurugan & Bach except that we used the step-size ratio $\beta$ rather than the strong convexity and concavity parameters of the Lagrangian to define $\Omega$ and $\Omega^{\ast}$.^11^1Since our saddle-point problem is not necessarily strongly convex in $\theta$ (when $\rho = 0$), we could not define $\Omega$ and $\Omega^{\ast}$ in the same way as Balamurugan & Bach. Substituting the definition of $B_{t}{(\theta,w)}$, we have

<!-- chunk {"id": "body-0042", "role": "body", "section": "Theoretical analyses of SVRG and SAGA", "weight": 1.0} -->

With the above definitions, we characterize the convergence of $\Omega{({\theta_{m} - \theta_{\star}},{w_{m} - w_{\star}})}$, where $(\theta_{\star},w_{\star})$ is the solution of, and $(\theta_{m},w_{m})$ is the output of the algorithms after the $m$-th iteration. For SVRG, it is the $m$-th *outer* iteration in Algorithm 2. The following two theorems are proved in Appendices C and D, respectively.

<!-- chunk {"id": "body-0043", "role": "body", "section": "Comparison of Different Algorithms", "weight": 1.0} -->

This section compares the computation complexities of several representative policy-evaluation algorithms that minimize EM-MSPBE, as summarized in Table 1.

<!-- chunk {"id": "body-0044", "role": "body", "section": "Comparison of Different Algorithms", "weight": 1.0} -->

The upper part of the table lists algorithms whose complexity is linear in feature dimension $d$, including the two new algorithms presented in the previous section. We can also apply GTD2 to a finite dataset with samples drawn uniformly at random with replacement. It costs $O{(d)}$ per iteration, but has a sublinear convergence rate regarding $\epsilon$. In practice, people may choose $\epsilon = {\Omega{({1/n})}}$ for generalization reasons (see, e.g., Lazaric et al. ), leading to an $O{({\kappa^{\prime}nd})}$ overall complexity for GTD2, where $\kappa^{\prime}$ is a condition number related to the algorithm. However, as verified by our experiments, the bounds in the table show that our SVRG/SAGA-based algorithms are much faster as their effective condition numbers vanish when $n$ becomes large. TDC has a similar complexity to GTD2.

<!-- chunk {"id": "body-0045", "role": "body", "section": "Comparison of Different Algorithms", "weight": 1.0} -->

In the table, we list two different implementations of PDBG. PDBG-(I) computes the gradients by averaging the stochastic gradients over the entire dataset at each iteration, which costs $O{({nd})}$ operations; see discussions at the end of Section 4. PDBG-(II) first pre-computes the matrices $\hat{A}$, $\hat{b}$ and $\hat{C}$ using $O{({nd^{2}})}$ operations, then computes the batch gradient at each iteration with $O{(d^{2})}$ operations. If $d$ is very large (e.g., when $d \gg n$), then PDBG-(I) would have an advantage over PDBG-(II). The lower part of the table also includes LSTD, which has $O{({nd^{2}})}$ complexity if rank-one updates are used.

<!-- chunk {"id": "body-0046", "role": "body", "section": "Comparison of Different Algorithms", "weight": 1.0} -->

SVRG and SAGA are more efficient than the other algorithms, when either $d$ or $n$ is very large. In particular, they have a lower complexity than LSTD when $d > {{({1 + \frac{\kappa{(\hat{C})}\kappa_{G}^{2}}{n}})}{\log\left( \frac{1}{\epsilon} \right)}}$, This condition is easy to satisfy, when $n$ is very large. On the other hand, SVRG and SAGA algorithms are more efficient than PDBG-(I) if $n$ is large, say $n > \left. {\kappa{(\hat{C})}\kappa_{G}^{2}}/\left( {{\kappa{(\hat{C})}\kappa} - 1} \right) \right.$, where $\kappa$ and $\kappa_{G}$ are described in the caption of Table 1.

<!-- chunk {"id": "body-0047", "role": "body", "section": "Comparison of Different Algorithms", "weight": 1.0} -->

There are other algorithms whose complexity scales linearly with $n$ and $d$, including iLSTD, and TDC, fLSTD-SA, and the more recent algorithms of Wang et al. and Dai et al.. However, their convergence is slow: the number of iterations required to reach a desired accuracy $\epsilon$ grows as $1/\epsilon$ or worse. The CTD algorithm uses a similar idea as SVRG to reduce variance in TD updates. This algorithm is shown to have a similar linear convergence rate in an *online* setting where the data stream is generated by a Markov process with *finite* states and *exponential* mixing. The method solves for a fixed-point solution by stochastic approximation. As a result, they can be non-convergent in off-policy learning, while our algorithms remain stable (c.f., Section 7.1).

<!-- chunk {"id": "body-0048", "role": "body", "section": "Extensions", "weight": 1.0} -->

It is possible to extend our approach to accelerate optimization of other objectives such as MSBE and NEU. In this section, we briefly describe two extensions of the algorithms developed earlier.

<!-- chunk {"id": "body-0049", "role": "body", "section": "Off-policy learning", "weight": 1.0} -->

In some cases, we may want to estimate the value function of a policy $\pi$ from a set of data $\mathcal{D}$ generated by a different "behavior" policy $\pi_{b}$. This is called *off-policy learning*.

<!-- chunk {"id": "body-0050", "role": "body", "section": "Off-policy learning", "weight": 1.0} -->

In the off-policy case, samples are generated from the distribution induced by the behavior policy $\pi_{b}$, not the the target policy $\pi$. While such a mismatch often causes stochastic-approximation-based methods to diverge, our gradient-based algorithms remain convergent with the same (fast) convergence rate.

<!-- chunk {"id": "body-0051", "role": "body", "section": "Off-policy learning", "weight": 1.0} -->

The EM-MSPBE for off-policy learning has the same expression as in except that $A_{t}$, $b_{t}$ and $C_{t}$ are modified by the weight factor $\rho_{t}$, as listed in Table 2; see also Liu et al. for a related discussion.) Algorithms 1--3 remain the same for the off-policy case after $A_{t}$, $b_{t}$ and $C_{t}$ are modified correspondingly.

<!-- chunk {"id": "body-0052", "role": "body", "section": "Learning with eligibility traces", "weight": 1.0} -->

Eligibility traces are a useful technique to trade off bias and variance in TD learning. When they are used, we can pre-compute $z_{t}$ in Table 2 before running our new algorithms. Note that EM-MSPBE with eligibility traces has the same form of, with $A_{t}$, $b_{t}$ and $C_{t}$ defined differently according to the last row of Table 2. At the $m$-th step of the learning process, the algorithm randomly samples $z_{t_{m}},\phi_{t_{m}},\phi_{t_{m}}^{\prime}$ and $r_{t_{m}}$ from the fixed dataset and computes the corresponding stochastic gradients, where the index $t_{m}$ is uniformly distributed over $\{ 1,\ldots,n\}$ and are independent for different values of $m$. Algorithms 1--3 immediately work for this case, enjoying a similar linear convergence rate and a computation complexity linear in $n$ and $d$.

<!-- chunk {"id": "body-0053", "role": "body", "section": "Learning with eligibility traces", "weight": 1.0} -->

We need additional $O{({nd})}$ operations to pre-compute $z_{t}$ recursively and an additional $O{({nd})}$ storage for $z_{t}$. However, it does not change the order of the total complexity for SVRG/SAGA.

<!-- chunk {"id": "body-0054", "role": "body", "section": "Experiments", "weight": 1.0} -->

In this section, we compare the following algorithms on two benchmark problems: (i) PDBG (Algorithm 1); (ii) GTD2 with samples drawn randomly with replacement from a dataset; (iii) TD: the fLSTD-SA algorithm of Prashanth et al.; (iv) SVRG (Algorithm 2); and (v) SAGA (Algorithm 3). Note that when $\rho > 0$, the TD solution and EM-MSPBE minimizer differ, so we do not include TD. For step size tuning, $\sigma_{\theta}$ is chosen from $\left\{ 10^{- 1},10^{- 2},\ldots,10^{- 6} \right\}\frac{1}{L_{\rho}\kappa{(\hat{C})}}$ and $\sigma_{w}$ is chosen from $\left\{ 1,10^{- 1},10^{- 2} \right\}\frac{1}{\lambda_{\max}{(\hat{C})}}$.

<!-- chunk {"id": "body-0055", "role": "body", "section": "Experiments", "weight": 1.0} -->

We only report the results of each algorithm which correspond to the best-tuned step sizes; for SVRG we choose $N = {2n}$.

<!-- chunk {"id": "body-0056", "role": "body", "section": "Experiments", "weight": 1.0} -->

In the first task, we consider a randomly generated MDP with $400$ states and $10$ actions. The transition probabilities are defined as ${P\left( s^{\prime} \middle| {a,s} \right)} \propto {p_{ss^{\prime}}^{a} + 10^{- 5}}$, where $p_{ss^{\prime}}^{a} \sim {U{\lbrack 0,1\rbrack}}$. The data-generating policy and start distribution were generated in a similar way. Each state is represented by a $201$-dimensional feature vector, where $200$ of the features were sampled from a uniform distribution, and the last feature was constant one. We chose $\gamma = 0.95$. Fig. 1 shows the performance of various algorithms for $n = 20000$. First, notice that the stochastic variance methods converge much faster than others. In fact, our proposed methods achieve linear convergence.

<!-- chunk {"id": "body-0057", "role": "body", "section": "Experiments", "weight": 1.0} -->

Second, as we increase $\rho$, the performances of PDBG, SVRG and SAGA improve significantly due to better conditioning, as predicted by our theoretical results.

<!-- chunk {"id": "body-0058", "role": "body", "section": "Experiments", "weight": 1.0} -->

Next, we test these algorithms on Mountain Car. To collect the dataset, we first ran Sarsa with $d = 300$ CMAC features to obtain a good policy. Then, we ran this policy to collect trajectories that comprise the dataset. Figs. 2 and 3 show our proposed stochastic variance reduction methods dominate other first-order methods. Moreover, with better conditioning (through a larger $\rho$), PDBG, SVRG and SAGA achieve faster convergence rate. Finally, as we increase sample size $n$, SVRG and SAGA converge faster. This simulation verifies our theoretical finding in Table 1 that SVRG/SAGA need fewer epochs for large $n$.

<!-- chunk {"id": "body-0059", "role": "body", "section": "Conclusions", "weight": 1.0} -->

In this paper, we reformulated the EM-MSPBE minimization problem in policy evaluation into an empirical saddle-point problem, and developed and analyzed a batch gradient method and two first-order stochastic variance reduction methods to solve the problem. An important result we obtained is that even when the reformulated saddle-point problem lacks strong convexity in primal variables and has only strong concavity in dual variables, the proposed algorithms are still able to achieve a linear convergence rate. We are not aware of any similar results for primal-dual batch gradient methods or stochastic variance reduction methods. Furthermore, we showed that when both the feature dimension $d$ and the number of samples $n$ are large, the developed stochastic variance reduction methods are more efficient than any other gradient-based methods which are convergent in off-policy settings.

<!-- chunk {"id": "body-0060", "role": "body", "section": "Conclusions", "weight": 1.0} -->

This work leads to several interesting directions for research. First, we believe it is important to extend the stochastic variance reduction methods to nonlinear approximation paradigms, especially with deep neural networks. Moreover, it remains an important open problem how to apply stochastic variance reduction techniques to policy optimization.
