<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Convex Structured Controller Design

Topics include Structured control, Convex controller synthesis, Finite-horizon control, Decentralized control, Feedback constraints, Variable impedance, Nonlinear extensions.

<!-- chunk {"id": "summary-0002", "role": "summary", "section": "Summary", "weight": 2.0} -->

Proposes a finite-horizon control objective that makes linear feedback synthesis convex even under arbitrary convex structure constraints on the feedback matrices. The paper is important because it sidesteps the usual nonconvexity of structured LQR, H2, and Hinf-like design by optimizing a surrogate tied to the inverse closed-loop map, enabling sparse, delayed, decentralized, and variable-impedance feedback designs with global solutions for the surrogate.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

We consider the problem of synthesizing optimal linear feedback policies subject to arbitrary convex constraints on the feedback matrix. This is known to be a hard problem in the usual formulations (Htwo,Hinf,LQR) and previous works have focused on characterizing classes of structural constraints that allow efficient solution through convex optimization or dynamic programming techniques. In this paper, we propose a new control objective and show that this formulation makes the problem of computing optimal linear feedback matrices convex under arbitrary convex constraints on the feedback matrix. This allows us to solve problems in decentralized control (sparsity in the feedback matrices), control with delays and variable impedance control. Although the control objective is nonstandard, we present theoretical and empirical evidence that it agrees well with standard notions of control. We also present an extension to nonlinear control affine systems. We present numerical experiments validating our approach.

<!-- chunk {"id": "body-0004", "role": "body", "section": "INTRODUCTION", "weight": 1.5} -->

Linear feedback control synthesis is a classical topic in control theory and has been extensively studied in the literature. From the perspective of stochastic optimal control theory, the classical result is the existence of an optimal linear feedback controller for systems with linear dynamics, quadratic costs and gaussian noise (LQG systems) that can be computed via dynamic programming. However, if one imposes additional constraints on the feedback matrix (such as a sparse structure arising from the need to implement control in a decentralized fashion), the dynamic programming approach is no longer applicable. In fact, it has been shown that the optimal control policy may not even be linear and that the general problem of designing linear feedback gains subject to constraints is NP-hard.\
Previous approaches to synthesizing structured controllers can be broadly categorized into three types: Frequency Domain Approaches, Dynamic Programming Approaches and Nonconvex optimization methods. The first two classes of approaches find *exact* solutions to structured control problems for special cases.

<!-- chunk {"id": "body-0005", "role": "body", "section": "INTRODUCTION", "weight": 1.5} -->

The third class of approaches tries to directly solve the optimal control problem (minimizing the $\mathcal{H}_{2}$,$\mathcal{H}_{\infty}$ norm) subject to constraints on the controller, using nonconvex optimization techniques. These are generally applicable, but are susceptible to local minima and slow convergence (especially for nonsmooth norms such as $\mathcal{H}_{\infty}$).\
In this paper, we take a different approach: We reformulate the structured control problem using a family of new control objectives (section II). We develop these bounds as follows: The $\mathcal{H}_{2}$ and $\mathcal{H}_{\infty}$ norms can be expressed as functions of singular values of the linear mapping from disturbance trajectories to state trajectories. This mapping is a highly nonlinear function of the feedback gains. However, the inverse of this mapping has a simple linear dependence on the feedback gains.

<!-- chunk {"id": "body-0006", "role": "body", "section": "INTRODUCTION", "weight": 1.5} -->

Further, the determinant of the mapping has a fixed value independent of the closed loop dynamics - this is in fact a finite horizon version of Bode's sensitivity integral and has been studied. By exploiting both these facts, we develop upper bounds on the $\mathcal{H}_{2},\mathcal{H}_{\infty}$ norms in terms of the singular values of the inverse mapping. We show that these upper bounds have several properties that make them desirable control objectives. For the new family of objectives, we show that the resulting problem of designing an optimal linear state feedback matrix, under arbitrary convex constraints, is convex (section III). Further, we prove suboptimality bounds on how the solutions of the convex problems compare to the optima of the original problem. Our approach is directly formulated in state space terminology and does not make any reference to frequency domain concepts. Thus, it applies directly to time-varying systems. We validate our approach numerically and show that the controllers synthesized by our approach achieve good performance (section V).\
The work presented here is an extension of a recent conference publication.

<!-- chunk {"id": "body-0007", "role": "body", "section": "INTRODUCTION", "weight": 1.5} -->

However, this paper contains a significant reformulation of the results presented there and also has new results. The conference paper was formulated in terms of the eigenvalues of the covariance matrix of trajectories. In this paper, we look at the linear map from noise to state trajectories (denoted by $F$ in this paper), which is a Cholesky factor of the covariance matrix. This allows us to produce simpler proofs of convexity and deal with a more general class of objectives. For example, the nuclear norm (and more generally Ky-Fan norms) of $F$ is a valid objective in our formulation while it was not, since it is equal to the sum of square roots of eigenvalues of the covariance matrix which is a nonconvex function. Further, we provide an analysis quantifying how well the solutions to our convex objectives perform in terms of the original nonconvex $\mathcal{H}_{2},\mathcal{H}_{\infty}$ objectives. We present numerical results comparing results of our formulation to other nonconvex approaches for structured controller synthesis.

<!-- chunk {"id": "body-0008", "role": "body", "section": "INTRODUCTION", "weight": 1.5} -->

Finally, we also present a generalization of our approach to nonlinear systems.

<!-- chunk {"id": "body-0009", "role": "body", "section": "PROBLEM FORMULATION", "weight": 1.0} -->

$z_{\lbrack i\rbrack}$ is the $i$-th largest component of $z$ and $|z|$ the vector with entries ${|z_{1}|},\ldots,{|z_{n}|}$. Finally, $\mathcal{N}{(\mu,\Sigma)}$ denotes a Gaussian distribution with mean $\mu$ and covariance matrix $\Sigma$.

<!-- chunk {"id": "body-0010", "role": "body", "section": "PROBLEM FORMULATION", "weight": 1.0} -->

There is a linear mapping between disturbance and state trajectories for a linear system. This will play a key role in our paper, and we denote it by

<!-- chunk {"id": "body-0011", "role": "body", "section": "PROBLEM FORMULATION", "weight": 1.0} -->

We assume that the controller performance is measured in terms the norm of the system trajectory $\mathbf{x}^{T}\mathbf{x}$ (see section IX-A for an extension that includes control costs).

<!-- chunk {"id": "body-0012", "role": "body", "section": "PROBLEM FORMULATION", "weight": 1.0} -->

As mentioned earlier, we restrict ourselves to have static state feedback $u_{t} = {K_{t}x_{t}}$ (section IX-B discusses dynamic output feedback).

<!-- chunk {"id": "body-0013", "role": "body", "section": "PROBLEM FORMULATION", "weight": 1.0} -->

We assume that $D_{t}$ is square and invertible.

<!-- chunk {"id": "body-0014", "role": "body", "section": "PROBLEM FORMULATION", "weight": 1.0} -->

If there are no constraints on $\mathbf{K}$, these problems can be solved using standard dynamic programming techniques. However, we are interested in synthesizing structured controllers. We formulate this very generally: We allow *arbitrary* convex constraints on the set of feedback matrices: $\mathbf{K} \in \mathcal{C}$ for some convex set $\mathcal{C}$. Then, the control synthesis problem becomes

<!-- chunk {"id": "body-0015", "role": "body", "section": "PROBLEM FORMULATION", "weight": 1.0} -->

The general problem of synthesizing stabilizing linear feedback control, subject even to simple bound constraints on the entries of $K$, is known to be hard. Several hardness results on linear controller design can be found. Although these results do not cover the problems, they suggest that are hard optimization problems. In this paper, we propose an alternate objective function based on the singular values of the inverse mapping $F(\mathbf{K})^{- 1}$ and prove that this objective can be optimized using convex programming techniques under *arbitrary* convex constraints on the feedback matrices $\mathbf{K} = {\{ K_{t}\}}$. Given the above hardness results, it is clear that the optimal solution to the convex problem will not match the optimal solution to the original problem. However, we present theoretical and numerical evidence to suggest that the solutions of the convex problem we propose approximate the solution to the original problems well for several problems.

<!-- chunk {"id": "body-0016", "role": "body", "section": "II-A Control Objective", "weight": 1.0} -->

The problems, are non-convex optimization problems, because of the nonlinear dependence of $F(\mathbf{K})$ on $\mathbf{K}$. In this section, we will derive convex upper bounds on the singular values of $F(\mathbf{K})$ that can be optimized under arbitrary convex constraints $\mathcal{C}$. We have the following results (section IX, theorems IX.1, IX.2):

<!-- chunk {"id": "body-0017", "role": "body", "section": "II-A Control Objective", "weight": 1.0} -->

To illustrate the behavior of these upper bounds (denoted ${UB_{\infty}},{UB_{2}}$), we plot them for a scalar linear system

<!-- chunk {"id": "body-0018", "role": "body", "section": "II-A Control Objective", "weight": 1.0} -->

over a horizon $N = 100$ in figure 1. When ${|k|} < 1$, this system is unstable and otherwise it is stable. Thus, $|k|$ is a measure of the "degree of instability" of the system. As expected, the original objectives grow slowly to the point of instability and then blow up. The convex upper bounds are fairly loose upper bounds and increase steadily. However, the rate of growth increases with degree of instability. Similar results are observed for $n > 1$.

<!-- chunk {"id": "body-0019", "role": "body", "section": "II-B A General Class of Control Objectives", "weight": 1.0} -->

The objectives, are just two of the control objectives that are allowed in our framework. We can actually allow a general class of objectives that can be minimized for control design. From, we know that for any *absolutely invariant* convex function $f{(x)}$ on $\mathbf{R}^{n}$, the function ${g{(X)}} = {f{({\sigma(X)})}}$ on $\mathbf{R}^{n \times n}$ is convex.

<!-- chunk {"id": "body-0020", "role": "body", "section": "II-B A General Class of Control Objectives", "weight": 1.0} -->

where $\mathcal{C}$ is a convex set encoding the structural constraints on $\mathbf{K}$ and $R(\mathbf{K})$ is a convex penalty on the feedback gains $\mathbf{K}$. We show (in theorem III.1) that this problem is a convex optimization problem.

<!-- chunk {"id": "body-0021", "role": "body", "section": "II-B A General Class of Control Objectives", "weight": 1.0} -->

A common choice for $R(\mathbf{K})$ is ${\parallel\mathbf{K}\parallel}^{2}$. For decentralized control, $\mathcal{C}$ would be of the form $\mathcal{C} = {\{\mathbf{K}:{\mathbf{K}_{t} \in S}\}}$ where $S$ is the set of matrices with a certain sparsity pattern corresponding to the decentralization structure required. We now present our main theorem proving the convexity of the generalized problem.

<!-- chunk {"id": "body-0022", "role": "body", "section": "III-B SUBOPTIMALITY BOUNDS", "weight": 1.0} -->

We are using convex surrogates for the $q_{2},q_{\infty}$ norms. Thus, it makes sense to ask the question: How far are the optimal solutions to the convex surrogates from those of the original problem? We answer this question by proving multiplicative suboptimality bounds: We prove that the ratio of the $q_{2}$ norm of the convex surrogate solution and the $q_{2}$-optimal solution is bounded above by a quantity that decreases as the variance of the singular vector of $\left( {F(\mathbf{K})} \right)^{- 1}$ at the optimum. Although these bounds may be quite loose, they provide qualitative guidance about when the algorithm would perform well.

<!-- chunk {"id": "body-0023", "role": "body", "section": "III-C INTERPRETATION OF BOUNDS", "weight": 1.0} -->

The bounds have the following interpretation: Since the product of singular values is constrained to be fixed, stable systems (with small $\mathcal{H}_{2},\mathcal{H}_{\infty}$ norm) would have all of their singular values close to each other. Thus, if the singular values at the solution discovered by our algorithm are close to each other, we can expect that our solution is close to the true optimum. Further, the bounds say that the only thing that matters is the spread of the singular values relative to the spread of singular values at the optimal solution. A side-effect of the analysis is that it suggests that the spectral norm of $\left( {F(\mathbf{K})} \right)^{- 1}$ be used as a surrogate for the $q_{2}$ norm and the nuclear norm be a surrogate for the $q_{\infty}$ norm, since optimizing these surrogates produces solutions with suboptimality bounds on the original objectives.

<!-- chunk {"id": "body-0024", "role": "body", "section": "III-C INTERPRETATION OF BOUNDS", "weight": 1.0} -->

Finally note that although the bounds depend on the (unknown) optimal solution $\mathbf{K}^{\ast}$, we can still get a useful bound for the $q_{2}$ case by simply dropping the effect of the negative term so that

<!-- chunk {"id": "body-0025", "role": "body", "section": "III-C INTERPRETATION OF BOUNDS", "weight": 1.0} -->

which can be computed after solving the convex problem to get ${}_{}^{}$. A finer analysis may be possible by looking at the minimum possible value of ${Var}\left( \sigma^{\ast} \right)$, just based on the block-bidiagonal structure of the matrix $F(\mathbf{K})^{- 1}$, but we leave this for future work.

<!-- chunk {"id": "body-0026", "role": "body", "section": "ALGORITHMS AND COMPUTATION", "weight": 1.0} -->

In this paper, our primary focus is to discuss the properties of the new convex formulation of structured controller synthesis we developed here. Algorithms for solving the resulting convex optimization problem is a topic we will investigate in depth in future work. In most cases, problem can be reformulated as a semidefinite programming problem and solved using off-the-shelf interior point methods. However, although theoretically polynomial time, off-the-shelf solvers tend to be inefficient in practice and do not scale. In this section, we lay out some algorithmic options including the one we used in our numerical experiments (section V).

<!-- chunk {"id": "body-0027", "role": "body", "section": "ALGORITHMS AND COMPUTATION", "weight": 1.0} -->

When the objective used is the nuclear norm, $\sum_{i = 1}^{nN}{\sigma_{i}\left( \left( {F(\mathbf{K})} \right)^{- 1} \right)}$, we show that it is possible to optimize the objective using standard Quasi-Newton approaches. The nuclear norm is a nonsmooth function in general, but given the special structure of the matrices appearing in our problem, we show that it is differentiable. For a matrix $X$, the subdifferential of the nuclear norm ${\parallel X\parallel}_{\ast}$ at $X$ is given by

<!-- chunk {"id": "body-0028", "role": "body", "section": "ALGORITHMS AND COMPUTATION", "weight": 1.0} -->

where $X = {U\SigmaV^{T}}$ is the singular value decomposition of $X$. For our problem $X = {F(\mathbf{K})^{- 1}}$, which has a non-zero determinant and hence is a nonsingular square matrix irrespective of the value of $\mathbf{K}$. Thus, the subdifferential is a singleton (${U^{T}W} = 0\Longrightarrow W = 0$ as $U$ is full rank and square). This means that the nuclear norm is a differentiable function in our problem and one can use standard gradient descent and Quasi Newton methods to minimize it. These methods are orders of magnitude more efficient than other approaches (reformulating as an SDP and using off-the-shelf interior point methods). They still require computing the SVD of an ${{nN} \times n}N$ matrix at every iteration, which will get prohibitively expensive when $nN$ is of the order of several thousands.

<!-- chunk {"id": "body-0029", "role": "body", "section": "ALGORITHMS AND COMPUTATION", "weight": 1.0} -->

However, the structure of $F(\mathbf{K})^{T}F(\mathbf{K})$ is block-tridiagonal and efficient algorithms have been proposed for computing the eigenvalues of such matrices (see and the references therein). Since the singular values of $F(\mathbf{K})$ are simply square roots of eigenvalues of $F(\mathbf{K})^{T}F(\mathbf{K})$, this approach could give us efficient algorithms for computing the SVD of $F(\mathbf{K})$.

<!-- chunk {"id": "body-0030", "role": "body", "section": "ALGORITHMS AND COMPUTATION", "weight": 1.0} -->

The log-barrier for the semidefinite constraint can be rewritten as $\log\left( {\det\left( {t^{2} - {F(\mathbf{K})_{}^{- 1}F(\mathbf{K})^{- 1}}} \right)} \right)$ using Schur complements. The matrix $\left( {F(\mathbf{K})} \right)_{}^{- 1}\left( {F(\mathbf{K})} \right)^{- 1}$ is a symmetric positive definite block-tridiagonal matrix, which is a special case of a chordal sparsity pattern. This means that computing the gradient and Newton step for the log-barrier is efficient, with complexity growing as $O{(N)}$. Thus, at least for the case where the objective is the spectral norm, we can develop efficient interior point methods.

<!-- chunk {"id": "body-0031", "role": "body", "section": "V-A Comparing Algorithms: Decentralized Control", "weight": 1.0} -->

In this section, we compare different approaches to controller synthesis. We work with discrete-time LTI systems over a fixed horizon $N$ with ${{A_{t} = A},{B_{t} = B = I}},{D_{t} = D = I}$. Further, we will use $\mathcal{C} = {\{ K:{K_{ij} = 0 \notin S}\}}$, where $S$ is the set of non-zero indices of $K$. The control design methodologies we compare are:\
*NCON:* This refers to nonconvex approaches for both the $q_{2}$ and $q_{\infty}$ norms. The $q_{2}$ norm is a differentiable function and we use a standard LBFGS method to minimize it. The $q_{\infty}$ norm is nondifferentiable, but only at points where the maximum singular value of $F(\mathbf{K})$ is not unique.

<!-- chunk {"id": "body-0032", "role": "body", "section": "V-A Comparing Algorithms: Decentralized Control", "weight": 1.0} -->

We use a nonsmooth Quasi Newton method to minimize it (using the freely available software implementation HANSO ).\
*CON:* The convex control synthesis described here.

<!-- chunk {"id": "body-0033", "role": "body", "section": "V-A Comparing Algorithms: Decentralized Control", "weight": 1.0} -->

with $m = {{nN} - 1}$ as a surrogate for the $q_{\infty}$ norm and $m = 1$ for the $q_{2}$ norm. Although these objectives are non differentiable, we find that an off-the-shelf LBFGS optimizer works well and use it in our experiments here.\
*OPT*: The optimal solution to the problem in the absence of the constraint $\mathcal{C}$. This is simply the solution to a standard LQR problem for the $q_{2}$ case.

<!-- chunk {"id": "body-0034", "role": "body", "section": "V-A Comparing Algorithms: Decentralized Control", "weight": 1.0} -->

where the controller chooses $u$ to minimize the cost while an adversary chooses $w_{t}$ so as to maximize the cost. There is critical value of $\gamma$ below which the upper value of this game is unbounded. This critical value of $\gamma$ is precisely the $q_{\infty}$ norm and the resulting policies for the controller at this value of $\gamma$ is the $q_{\infty}$-optimal control policy. For any value of $\gamma$, the solution of the game can be computed by solving a set of Ricatti equations backward in time.\
We work with a dynamical system formed by coupling a set of systems with unstable dynamics $A^{i} \in \mathbf{R}^{2 \times 2}$.

<!-- chunk {"id": "body-0035", "role": "body", "section": "V-A Comparing Algorithms: Decentralized Control", "weight": 1.0} -->

where $x^{i}$ denotes the state of the $i$-th system and $\eta_{ij}$ is a coupling coefficient between systems $i$ and $j$. The objective is to design controls $u = {\{ u^{i}\}}$, in order to stabilize the overall system. In our examples, we use $N = 5$ systems giving us a 10 dimensional state space. The $A^{i},\eta_{ij}$ are generated randomly, with each entry having a Gaussian distribution with mean $0$ and variance $10$. The sparsity pattern $S$ is also generated randomly by picking $20\%$ of the off-diagonal entries of $K$ and setting them to $0$. For both the ${CON},{NCON}$ problems, we initialize the optimizer at the same point $\mathbf{K} = 0$.

<!-- chunk {"id": "body-0036", "role": "body", "section": "V-A Comparing Algorithms: Decentralized Control", "weight": 1.0} -->

For the $q_{\infty}$ norm, we present results comparing the approaches over 100 trials. The $q_{\infty}$ norm of the solution obtained by the $CON$ approach to that found by ${NCON},{OPT}$ in figure 2. We plot histograms of how the $q_{\infty}$ compares between the ${CON},{NCON}$ and $OPT$ approaches. The red curves show kernel-density estimates of the distribution of values being plotted. The results show that $CON$ consistently outperforms $NCON$ and often achieves performance close to the centralized $OPT$ solution. The x-axis denotes the ratio between objectives on a log scale. The y-axis shows the frequency with which a particular ratio is attained (out of a 100 trials). We also plot a histogram of computation times with the log of ratio of CPU times for the CON and NCON algorithms on the x-axis. Again, in terms of CPU times, the CON approach is consistently superior except for a small number of outliers.

<!-- chunk {"id": "body-0037", "role": "body", "section": "V-A Comparing Algorithms: Decentralized Control", "weight": 1.0} -->

For the $q_{2}$ norm, we plot the results in figure 3. Here, the NCON approach does better and beats the CON approach for most trials. However, in more than $70\%$ of the trials the $q_{2}$ norm of the solution found by CON is within $2\%$ of that found by NCON. In terms of computation time, the CON approach retains superiority.

<!-- chunk {"id": "body-0038", "role": "body", "section": "V-A Comparing Algorithms: Decentralized Control", "weight": 1.0} -->

The numerical results indicate that the convex surrogates work well in many cases. However, they do fail in particular cases. In general, the surrogates seem to perform better on the $q_{\infty}$ norm than the $q_{2}$ norm. The initial results are promising but we believe that further analytical and numerical work is required to exactly understand when the convex objectives proposed in this paper are good surrogates for the original nonconvex $q_{2}$ and $q_{\infty}$ objectives.

<!-- chunk {"id": "body-0039", "role": "body", "section": "GENERALIZATION TO NONLINEAR SYSTEMS", "weight": 1.0} -->

We now present a generalization of our approach to nonlinear systems. The essential idea is to study a nonlinear system in terms of sensitivities of system trajectories with respect to disturbances.

<!-- chunk {"id": "body-0040", "role": "body", "section": "GENERALIZATION TO NONLINEAR SYSTEMS", "weight": 1.0} -->

Now we seek to design a controller $u_{t} = {K_{t}\phi{(x_{t})}}$ where $\phi$ is any set of fixed "features" of the state on which we want the control to depend that minimizes deviations from the constant trajectory $\lbrack 0,0,\ldots,0\rbrack$.

<!-- chunk {"id": "body-0041", "role": "body", "section": "GENERALIZATION TO NONLINEAR SYSTEMS", "weight": 1.0} -->

Given a state trajectory $\mathbf{x} = {\lbrack x_{1},\ldots,x_{N}\rbrack}$, we can recover the noise sequence as

<!-- chunk {"id": "body-0042", "role": "body", "section": "GENERALIZATION TO NONLINEAR SYSTEMS", "weight": 1.0} -->

Thus the map $F(\mathbf{K})$ is invertible. Let $F(\mathbf{K})^{- 1}$ denote the inverse. It can be shown (theorem IX.4) that the objective (assuming it is finite) can be bounded above by

<!-- chunk {"id": "body-0043", "role": "body", "section": "GENERALIZATION TO NONLINEAR SYSTEMS", "weight": 1.0} -->

In the linear case, the maximization over $\mathbf{x}$ is unnecessary since the term being maximized is independent of $\mathbf{x}$. However, for a nonlinear system, the Jacobian of $\left( {F(\mathbf{K})} \right)^{- 1}{(\mathbf{x})}$ is a function of $\mathbf{x}$ and an explicit maximization needs to be performed to compute the objective. Thus, we can formulate the control design problem as

<!-- chunk {"id": "body-0044", "role": "body", "section": "GENERALIZATION TO NONLINEAR SYSTEMS", "weight": 1.0} -->

The convexity of the above objective follows using a very similar proof as the linear case (see theorem IX.3). Computing the objective (maximizing over $\mathbf{x}$) in general would be a hard problem, so this result is only of theoretical interest in its current form. However, in future work, we hope to explore the computational aspects of this formulation more carefully.

<!-- chunk {"id": "body-0045", "role": "body", "section": "Discussion and Related Work", "weight": 1.5} -->

There have been three major classes of prior work in synthesizing structured controllers: Frequency domain approaches, dynamic programming and nonconvex optimization approaches. We compare the relative merits of the different approaches in this section.

<!-- chunk {"id": "body-0046", "role": "body", "section": "Discussion and Related Work", "weight": 1.5} -->

where $\parallel \cdot \parallel$ is typically the $\mathcal{H}_{2}$ or $\mathcal{H}_{\infty}$ norm. In general, these are solved by reparameterizing the problem in terms of a Youla parameter (via a nonlinear transformation), and imposing special conditions on $\mathcal{C}$ (like quadratic invariance) that guarantee that the constraints $\mathcal{C}$ can be translated into convex constraints on the Youla parameter. There are multiple limitations of these approaches:\
Only specific kinds of constraints can be imposed on the controller. Many of the examples have the restriction that the structure of the controller mirrors that of the plant.\
They result in infinite dimensional convex programs in general.

<!-- chunk {"id": "body-0047", "role": "body", "section": "Discussion and Related Work", "weight": 1.5} -->

One can solve them using a sequence of convex programming problems, but these approaches are susceptible to numerical issues and the degree of the resulting controllers may be ill-behaved, leading to practical problems in terms of implementing them.\
The approaches rely on frequency domain notions and cannot handle time-varying systems.\
In the special case of poset-causal systems (where the structure of the plant and controller can be described in terms of a partial order ), the problem can be decomposed when the performance metric is the $\mathcal{H}_{2}$ norm and explicit state-space solutions are available by solving Ricatti equations for subsystems and combining the results. For the $\mathcal{H}_{\infty}$ norm, a state-space solution using an LMI approach was developed.

<!-- chunk {"id": "body-0048", "role": "body", "section": "Discussion and Related Work", "weight": 1.5} -->

Another thread of work on decentralized control looks at special cases where dynamic programming techniques can be used in spite of the decentralization constraints. The advantage of these approaches is that they directly handle finite horizon and time-varying approaches. For the LEQG cost-criterion, a dynamic programming approach was developed in for the case of 1-step delay in a 2-agent decentralized control problem. In, the authors show that for the case of 2 agents (a block-lower triangular structure in $A,B$ with 2 blocks) can be solved via dynamic programming. In, the authors develop a dynamic programming solution that generalizes this and applies to general "partially-nested" systems allowing for both sparsity and delays.

<!-- chunk {"id": "body-0049", "role": "body", "section": "Discussion and Related Work", "weight": 1.5} -->

All the above methods work for special structures on the plant and controller (quadratic invariance/partial nestedness) under which decentralized controllers can be synthesized using either convex optimization or dynamic programming methods.

<!-- chunk {"id": "body-0050", "role": "body", "section": "Discussion and Related Work", "weight": 1.5} -->

In very recent work, the authors pose decentralized control (in the discrete-time, finite horizon, linear quadratic setting) as a rank-constrained semidefinite programming problem. By dropping the rank constraint, one can obtain a convex relaxation of the problem. The relaxed problem provides a solution to the original problem only when the relaxed problem has a rank-1 solution. However, it is unknown when this can be guaranteed, and how a useful controller can be recovered from a higher-rank solution. Further, the SDP posed in this work grows very quickly with the problem dimension.

<!-- chunk {"id": "body-0051", "role": "body", "section": "Discussion and Related Work", "weight": 1.5} -->

Our work differs from these previous works in one fundamental way: Rather than looking for special decentralization structures that can be solved tractably under standard control objectives, we formulate a new control objective that helps us solve problems with *arbitrary* decentralization constraints. In fact, we can handle *arbitrary convex constraints* - decentralization constraints that impose a sparsity pattern on $\mathbf{K}$ are a special case of this. We can also handle time-varying linear systems. Although the objective is nonstandard, we have provided theoretical and numerical evidence that it is a sensible control objective. The only other approaches that handle all these problems are nonconvex approaches. We have shown that our approach outperforms a standard nonconvex approach, both in terms of performance of resulting controller and in computation times.

<!-- chunk {"id": "body-0052", "role": "body", "section": "Discussion and Related Work", "weight": 1.5} -->

We also believe that this was the first approach to exploit a fundamental limitation (Bode's sensitivity integral) to develop efficient control design algorithms. The fact that the spectrum of the input output map satisfies a conservation law (the sum of the logs of singular values is fixed) is a limitation which says that reducing some of the singular values is bound to increase the others. However, this limitation allows us to approximate the difficult problem of minimizing the $\mathcal{H}_{2}$ or $\mathcal{H}_{\infty}$ norm with the easier problem of minimizing a convex surrogate, leading to efficient solution.

<!-- chunk {"id": "body-0053", "role": "body", "section": "CONCLUSION", "weight": 1.5} -->

We have argued that the framework developed seems promising and overcomes limitations of previous works on computationally tractable approaches to structured controller synthesis. Although the control objective used is non-standard, we have argued why it is a sensible objective, and we also presented numerical examples showing that it produces controllers outperforming other nonconvex approaches. Further, we proved suboptimality bounds that give guidance on when our solution is good even with respect to the original ($\mathcal{H}_{2}/\mathcal{H}_{\infty}$) metrics. There are three major directions for future work: 1) Investigating the effect of various objectives in our family of control objectives, 2) Developing efficient solvers for the resulting convex optimization problems and 3) Deriving computationally efficient algorithms for nonlinear systems.
