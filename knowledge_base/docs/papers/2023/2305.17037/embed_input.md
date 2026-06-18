<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Distributionally Robust Linear Quadratic Control

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Linear-Quadratic-Gaussian (LQG) control is a fundamental control paradigm that is studied in various fields such as engineering, computer science, economics, and neuroscience. It involves controlling a system with linear dynamics and imperfect observations, subject to additive noise, with the goal of minimizing a quadratic cost function for the state and control variables. In this work, we consider a generalization of the discrete-time, finite-horizon LQG problem, where the noise distributions are unknown and belong to Wasserstein ambiguity sets centered at nominal (Gaussian) distributions. The objective is to minimize a worst-case cost across all distributions in the ambiguity set, including non-Gaussian distributions. Despite the added complexity, we prove that a control policy that is linear in the observations is optimal for this problem, as in the classic LQG problem. We propose a numerical solution method that efficiently characterizes this optimal control policy. Our method uses the Frank-Wolfe algorithm to identify the least-favorable distributions within the Wasserstein ambiguity sets and computes the controller's optimal policy using Kalman filter estimation under these distributions.

<!-- chunk {"id": "body-0003", "role": "body", "section": "Introduction", "weight": 1.5} -->

The Linear Quadratic Regulator (LQR) is a classic control problem that has served as a building block for numerous applications in engineering and computer science, economics, or neuroscience. It involves controlling a system with linear dynamics and imperfect observations affected by additive noise, with the goal of minimizing a quadratic state and control cost. Under the assumption that noise terms are independent and normally distributed (a case referred to as Linear-Quadratic-Gaussian, or LQG), it is well known that the optimal control policy depends linearly on the observations and can be obtained efficiently by using the Kalman filtering procedure and dynamic programming.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

Motivated by practical settings where noise distributions may not be readily available or may not be Gaussian, this paper considers a discrete-time, finite-horizon generalization of the LQG setting where noise distributions are unknown and are chosen adversarially from ambiguity sets characterized by a Wasserstein distance and centered around nominal (Gaussian) distributions.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

We show that, even under distributional ambiguity, the optimal control policy remains linear in the system's observations. Our proof is novel and does not rely on traditional recursive dynamic programming arguments. Instead, we re-parametrize the control policy in terms of the purified state observations and we derive an upper bound for the resulting minimax formulation by relaxing the ambiguity set (from a Wasserstein ball into a Gelbrich ball) while simultaneously restricting the controller to linear dependencies. We then use convex duality to prove that this upper bound matches a lower bound obtained by restricting the ambiguity set in the dual of the minimax formulation. This implies the optimality of linear output feedback controllers, thus generalizing the classic results to a distributionally robust setting.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

We also find that the worst-case distribution is actually Gaussian, which leads to a very efficient algorithm for finding optimal controllers. Specifically, we propose an algorithm based on the Frank-Wolfe first-order method that at every step solves sub-problems corresponding to classic LQG control problems, using Kalman filtering and dynamic programming. We show that this algorithm enjoys a sublinear convergence rate and is susceptible to parallelization. Lastly, we implement the algorithm leveraging PyTorch's automatic differentiation module and we find that it yields uniformly lower runtimes than a direct method (based on solving semidefinite programs) across all problem horizons.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Literature Review", "weight": 1.0} -->

This paper is related to the ample literature in control theory and engineering aimed at designing controllers that are robust to noise. The classic LQR/LQG theory, developed in the 1960s, examined linear dynamical systems in either time or frequency domain, seeking to minimize a combination of quadratic state and control costs (in time-domain) or the $\mathcal{H}_{2}$ norm of the system's transfer function (in frequency domain). Motivated by findings that LQG controllers do not provide the guaranteed robust stability properties of LQR controllers, much effort has been devoted subsequently to designing controllers that are robust to worst-case perturbations, typically evaluated in terms of the $\mathcal{H}_{\infty}$ norm of the system's transfer function (see, e.g., for a comprehensive review of $\mathcal{H}_{\infty}$ and $\mathcal{H}_{2}$ controllers).

<!-- chunk {"id": "body-0008", "role": "body", "section": "Literature Review", "weight": 1.0} -->

Because $\mathcal{H}_{\infty}$ controllers tend to be overly conservative, various approaches have been proposed to balance the performance of nominal and robust controllers, e.g., by combining $\mathcal{H}_{2}$ and $\mathcal{H}_{\infty}$ approaches. A parallel stream of literature has considered risk-sensitive control, which minimizes an entropic risk measure instead of the expected quadratic cost. Although risk-sensitive control has a distributionally robust flavor (as the entropic risk measure is equivalent to a distributionally robust quadratic objective penalized via Kullback-Leibler divergence), risk-sensitive control models do not admit a distributionally robust formulation because the entropic risk measure is convex, but not coherent. In contrast, our distributionally robust model provides a direct interpretation of the exact set of noise distributions against which the controller provides safeguards, and leads to a computationally tractable framework for finding the optimal controller.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Literature Review", "weight": 1.0} -->

In this sense, our work is more directly related to the literature on distributionally robust control, which seeks controllers that minimize expected costs under worst-case noise distributions. Closest to our work are. proves the optimality of linear state-feedback control policies for a related minimax LQR model with a Wasserstein distance but with perfect state observations. With perfect observations, the optimal policies in the classic LQR formulation are independent of the noise distribution and are thus inherently already robust, so considering imperfect observations is what makes the problem significantly more challenging in our case. studies a minimax formulation based on the Wasserstein distance with both state and observation noise but without any control policy, and focuses solely on the problem of estimating the states. Several papers have considered robust formulations with imperfect observations but for constrained systems, which are more challenging; the common approach is to restrict attention to linear feedback policies for computational tractability, and without proving their optimality.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Literature Review", "weight": 1.0} -->

Also related is the recent literature stream on distributionally robust optimization using the Wasserstein distance. Within this stream, the closest work is, which consider the problem of minimax mean-squared-error estimation when ambiguity is modeled with a Wasserstein distance from a nominal Gaussian distribution. Our proof builds on some ideas from these papers (e.g., relying on the Gelbrich distance in the construction of the upper bound), which it combines with ideas from control theory on purified output-feedback to obtain the overall construction. Also related is, which studies multistage distributionally robust problems with ambiguity sets given by a nested Wasserstein distance for stochastic processes and identifies computationally tractable cases. For a broader overview of developments related to optimal transport and Wasserstein distance with an emphasis on computational tractability and applications in machine learning, we refer to.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Literature Review", "weight": 1.0} -->

Finally, our paper is also related to literature that documents the optimality of linear/affine policies in (distributionally) robust dynamic optimization models. prove optimality for one-dimensional linear systems affected by additive noise and with perfect state observations, but with general (convex) state and/or control costs, provide computationally tractable approaches to quantifying the suboptimality of affine controllers in finite or infinite-horizon settings, and characterize the performance of affine policies in two-stage (distributionally) robust dynamic models.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Problem Definition", "weight": 1.0} -->

We consider a discrete-time linear dynamical system

<!-- chunk {"id": "body-0013", "role": "body", "section": "Problem Definition", "weight": 1.0} -->

corrupted by observation noise $v_{t} \in {\mathbb{R}}^{p}$, where $C_{t} \in {\mathbb{R}}^{p \times n}$ and usually $p \leq n$ (so that observing $y_{t}$ would not allow reconstructing $x_{t}$ even if there were no observation noise). The control inputs $u_{t}$ are causal, i.e., depend on the past observations $y_{0},\ldots,y_{t}$ but not on the future observations $y_{t + 1},\ldots,y_{T - 1}$.

<!-- chunk {"id": "body-0014", "role": "body", "section": "Problem Definition", "weight": 1.0} -->

In this context, the classic LQG model assumes that $\mathbb{P}$ is known and Gaussian, and seeks $u \in \mathcal{U}_{y}$ that minimizes ${\mathbb{E}}_{\mathbb{P}}{\lbrack J\rbrack}$. Appendix §A reviews the standard approach for computing optimal control inputs by estimating states through Kalman filtering techniques and using dynamic programming.

<!-- chunk {"id": "body-0015", "role": "body", "section": "Problem Definition", "weight": 1.0} -->

and $\mathbb{W}$ is the 2-Wasserstein distance. Thus, by construction, all exogenous random variables $x_{0},w_{0},\ldots,w_{T - 1},v_{0},\ldots,v_{T - 1}$ are independent under every distribution in $\mathcal{W}$.

<!-- chunk {"id": "body-0016", "role": "body", "section": "Nash Equilibrium and Optimality of Linear Output Feedback Controllers", "weight": 1.0} -->

We henceforth view the distributionally robust LQG problem as a zero-sum game between the controller, who chooses causal control inputs, and nature, who chooses a distribution ${\mathbb{P}} \in \mathcal{W}$. In this section we show that this game admits a Nash equilibrium, where nature's Nash strategy is a Gaussian distribution ${\mathbb{P}}^{\star} \in \mathcal{W}$ and the controller's Nash strategy is a linear output feedback policy based on the Kalman filter evaluated under ${\mathbb{P}}^{\star}$.

<!-- chunk {"id": "body-0017", "role": "body", "section": "Purified Observations", "weight": 1.0} -->

Before outlining our proof strategy, we first simplify the problem formulation by re-parametrizing the control inputs in a more convenient form (following ). Note that the control inputs in the LQG formulation are subject to cyclic dependencies, as $u_{t}$ depends on $y_{t}$, while $y_{t}$ depends on $x_{t}$ through, and $x_{t}$ depends again on $u_{t}$ through, etc. Because these dependencies make the problem hard to analyze, it is preferable to instead consider the controls as functions of a new set of so-called purified observations instead of the actual observations $y_{t}$.

<!-- chunk {"id": "body-0018", "role": "body", "section": "Purified Observations", "weight": 1.0} -->

Specifically, we first introduce a fictitious noise-free system

<!-- chunk {"id": "body-0019", "role": "body", "section": "Purified Observations", "weight": 1.0} -->

In view of this, we can rewrite the distributionally robust LQG problem equivalently as

<!-- chunk {"id": "body-0020", "role": "body", "section": "Purified Observations", "weight": 1.0} -->

Indeed, by recursively combining the equations of the original and the noise-free systems, one can show that $\eta = {{Dw} + v}$ for some block triangular matrix $D$ (see Appendix §B for its construction). This shows that the purified observations depend (linearly) on the exogenous uncertainties but not on the control inputs. Hence, the cyclic dependencies complicating the original system are eliminated.

<!-- chunk {"id": "body-0021", "role": "body", "section": "Purified Observations", "weight": 1.0} -->

Subsequently, we also study the dual of, defined as

<!-- chunk {"id": "body-0022", "role": "body", "section": "Purified Observations", "weight": 1.0} -->

The classic minimax inequality implies that $p^{\star} \geq d^{\star}$. If we can prove that $p^{\star} = d^{\star}$, that has a solution $u^{\star}$ and that has a solution ${\mathbb{P}}^{\star}$, then $(u^{\star},{\mathbb{P}}^{\star})$ must be a Nash equilibrium of the zero-sum game at hand \[43, Theorem 2\]. However, because $\mathcal{U}_{\eta}$ is an infinite-dimensional function space and $\mathcal{W}$ is an infinite-dimensional, non-convex set of non-parametric distributions, the existence of a Nash equilibrium (in pure strategies) is not at all evident. Instead, our proof strategy will rely on constructing an upper bound for $p^{\star}$ and a lower bound for $d^{\star}$, and showing that these match.

<!-- chunk {"id": "body-0023", "role": "body", "section": "Upper Bound for $p^{\\star}$", "weight": 1.0} -->

We obtain an upper bound for $p^{\star}$ by suitably *enlarging* the ambiguity set $\mathcal{W}$ and *restricting* the controllers $u_{t}$ to linear dependencies. We enlarge $\mathcal{W}$ by ignoring all information about the distributions in $\mathcal{W}$ except for their covariance matrices, and by replacing the Wasserstein distance with the Gelbrich distance. To that end, we first define the Gelbrich distance on the space of covariance matrices.

<!-- chunk {"id": "body-0024", "role": "body", "section": "Lower Bound for $d^{\\star}$", "weight": 1.0} -->

To derive a tractable lower bound on $d^{\star}$, we restrict nature's feasible set to the family $\mathcal{W}_{\mathcal{N}}$ of all normal distributions in the Wasserstein ambiguity set $\mathcal{W}$. The resulting bounding problem is thus given by

<!-- chunk {"id": "body-0025", "role": "body", "section": "Lower Bound for $d^{\\star}$", "weight": 1.0} -->

As we obtained by restricting the feasible set of the outer maximization problem, it is clear that ${\underset{¯}{d}}^{\star} \leq d^{\star}$. Next, we show that can be recast as a finite-dimensional zero-sum game. This result critically relies on the following known fact regarding the 2-Wasserstein distance between two normal distributions, which coincides with the Gelbrich distance between their covariance matrices.

<!-- chunk {"id": "body-0026", "role": "body", "section": "Conclusions", "weight": 1.0} -->

Propositions 3.2 and 3.4 reveal that problems and are dual to each other, that is, they can be transformed into one another by interchanging minimization and maximization. The following main theorem shows that strong duality holds irrespective of the problem data.

<!-- chunk {"id": "body-0027", "role": "body", "section": "Efficient Numerical Solution of Distributionally Robust LQG Problems", "weight": 1.0} -->

Having proven these structural results, we next turn attention to the problem of finding the optimal strategies. Our next result shows that, under a mild regularity condition, the optimal controller $u^{\star}$ of the distributionally robust LQG problem can be computed efficiently from ${\mathbb{P}}^{\star}$.

<!-- chunk {"id": "body-0028", "role": "body", "section": "Remark 1 (Automatic differentiation)", "weight": 1.0} -->

Recall that $f{(W,V)}$ coincides with the optimal value of the LQG problem corresponding to the normal distribution $\mathbb{P}$ determined by the covariance matrices $W$ and $V$. By using the underlying dynamic programming equations, $f{(W,V)}$ can thus be expressed in closed form as a serial composition of $\mathcal{O}{(T)}$ rational functions (see Appendix §A for details). Hence, ${\nabla_{Z}f}{(W,V)}$ can be calculated symbolically for any $Z \in {\{ X_{0},W_{0},\ldots,W_{T - 1},V_{0},\ldots,V_{T - 1}\}}$ by repeatedly applying the chain and product rules. However, the resulting formulas are lengthy and cumbersome. We thus compute the gradients numerically using backpropagation.

<!-- chunk {"id": "body-0029", "role": "body", "section": "Remark 1 (Automatic differentiation)", "weight": 1.0} -->

The cost of evaluating ${\nabla_{Z}f}{(W,V)}$ is then of the same order of magnitude as the cost of evaluating $f{(W,V)}$.

<!-- chunk {"id": "body-0030", "role": "body", "section": "Remark 1 (Automatic differentiation)", "weight": 1.0} -->

A detailed description of the proposed Frank-Wolfe method is given in Algorithm 1 below.

<!-- chunk {"id": "body-0031", "role": "body", "section": "Remark 1 (Automatic differentiation)", "weight": 1.0} -->

Input: initial iterates W, V, nominal covariance matrices Ŵ, V̂, oracle precision δ ∈
1:set initial iteration counter k = 0
2:while stopping criterion is not met do
5: find a δ-approximate solution LZδ of
Algorithm 1 Frank-Wolfe algorithm for solving

<!-- chunk {"id": "body-0032", "role": "body", "section": "Remark 1 (Automatic differentiation)", "weight": 1.0} -->

By \[31, Theorem 1 and Lemma 7\], which applies thanks to the structural properties of $f{(W,V)}$ established in Proposition 4.2, Algorithm 1 attains a suboptimality gap of $\epsilon$ within $\mathcal{O}{({1/\epsilon})}$ iterations.

<!-- chunk {"id": "body-0033", "role": "body", "section": "Numerical Experiments", "weight": 1.0} -->

All experiments are run on an Intel i7-8700 CPU (3.2 GHz) machine with 16GB RAM. All linear SDP problems are modeled in Python 3.8.6 using CVXPY and solved with MOSEK. The gradients of $f{(W,V)}$ are computed via Pymanopt with PyTorch's automated differentiation module.

<!-- chunk {"id": "body-0034", "role": "body", "section": "Numerical Experiments", "weight": 1.0} -->

Consider a class of distributionally robust LQG problems with $n = m = p = 10$. We set $A_{t} = {0.1 \times A}$ to have ones on the main diagonal and the superdiagonal and zeroes everywhere else ($A_{i,j} = 1$ if $i = j$ or $i = {j - 1}$ and $A_{i,j} = 0$ otherwise), and the other matrices to $B_{t} = C_{t} = Q_{t} = R_{t} = I_{d}$. The Wasserstein radii are set to $\rho_{x_{0}} = \rho_{w_{t}} = \rho_{v_{t}} = 10^{- 1}$. The nominal covariance matrices of the exogenous uncertainties are constructed randomly and with eigenvalues in the interval $\lbrack 1,2\rbrack$ (so as to ensure they are positive definite). The code is publicly available in the Github repository

<!-- chunk {"id": "body-0035", "role": "body", "section": "Numerical Experiments", "weight": 1.0} -->

The optimal value of the distributionally robust LQG problem can be computed by directly solving the SDP reformulation of with MOSEK or by solving the nonlinear SDP with our Frank-Wolfe method detailed in Algorithm 1. We next compare these two approaches in 10 independent simulation runs, where we set a stopping criterion corresponding to an optimality gap below $10^{- 3}$ and we run the Frank-Wolfe method with $\delta = 0.95$. Figure 1(a) illustrates the execution time for both approaches as a function of the planning horizon $T$; runs where MOSEK exceeds $100$s are not reported. Figure 1(b) visualizes the empirical convergence behavior of the Frank-Wolfe algorithm. The results highlight that the Frank-Wolfe algorithm achieves running times that are uniformly lower than MOSEK across all problem horizons and is able to find highly accurate solutions already after a small number of iterations (50 iterations for problem instances of time horizon $T = 10$).

<!-- chunk {"id": "body-0036", "role": "body", "section": "Concluding Remarks and Limitations", "weight": 1.0} -->

In view of the popularity of LQG models, the results in this work carry important theoretical and practical implications. Despite considering a generalization of the classic LQG setting where the noise affecting the system dynamics and the observations follows unknown (and potentially non-Gaussian) distributions, our findings suggest that certain classic structural results continue to hold and that highly efficient methods can be adapted to tackle this more realistic (and more challenging) problem. Specifically, that control policies depending linearly on observations continue to be optimal and that the worst-case distribution turns out to be Gaussian is surprising from a theoretical angle and also has direct practical implications, because it allows leveraging the highly efficient Kalman filter in conjunction with dynamic programming and a Frank-Wolfe method to design an efficient computational procedure for solving the problem.

<!-- chunk {"id": "body-0037", "role": "body", "section": "Concluding Remarks and Limitations", "weight": 1.0} -->

The results also raise several important questions that warrant future exploration. First, it would be highly relevant to consider extensions where the system matrices are also affected by uncertainty, as this captures many applications of practical interest, e.g., reinforcement learning or revenue management. Second, it would be worth exploring an infinite horizon setting or relaxing the assumption that the nominal distribution is Gaussian, as both assumptions may be limiting the practical appeal of the framework. Third, one could also attempt to prove structural optimality results or design novel algorithms for generating high-quality suboptimal solutions for the more general setting involving constraints on states and/or control inputs. Lastly, one could improve the present algorithmic proposal by exploiting topological properties of the objective so as to guarantee linear convergence rates in the Frank-Wolfe procedure.
