<!-- arxiv-full-text:v1 {"arxiv_id": "2202.11659", "source": "ar5iv"} -->

### Introduction

Data used for prediction and control of real world dynamical systems is almost always noisy and incomplete (partially observed). Sensors and other measurement procedures inevitably introduce errors into the datasets, so designing reliable learning algorithms for these noisy or partially observed domains requires confronting fundamental questions of disturbance filtering and state estimation. Despite the ubiquity of partial observation in practice, these concerns are often underexplored in modern analyses of learning for control that assume perfect observations of the underlying dynamics.

In this work, we study the output estimation (OE) problem or learning to predict in partially observed linear dynamical systems. The output estimation problem is one of the most fundamental problems in theoretical statistics and learning theory. Both in theory and in practice, advances in predicting partially observed linear systems have led to successes in a variety of areas from controls to biology and economics, (c.f. e.g. Athans; Lillacci and Khammash; Gautier and Poignet ). We revisit this classical problem from a modern optimization perspective, and study the possibility of learning the optimal predictor via model-free procedures and direct policy search.

Relative to model-based procedures, which first estimate the underlying dynamics and then return a policy by solving an optimization problem using the estimated model, model-free methods offer several potential advantages. First, direct policy search allows one to easily specify the complexity of the policy class over which one searches. For example, the vast majority of industrial control systems are built upon proportional-integral-derivative (PID) controllers. Each PID controller comprises three scalar variables (gains) yet successfully regulates complex feedback loops in high-dimensional systems (e.g chemical plants). In addition, model-free policy search optimizes for performance directly on the true system, rather than an approximate model. As such, there is no gap between the model used for synthesis and the system on which the controller is deployed. Such gaps are typically covered by robust control techniques, which may introduce conservatism.

In light of these advantages, there has recently been significant interest from both theoreticians and practitioners in understanding the foundations of model-free control. However, so far, this attention has been mostly focused on problems with full-state observation such as the linear quadratic regulator (LQR) or fully-observed Markov Decision Processes (MDPs) which admit *static* policies. Progress in dealing with partially observed problems has been complicated by the difficulties associated with optimizing over *dynamic* policies that maintain internal state to summarize past observations. In this paper, we provide the first policy search algorithm which provably converges to the globally optimal filter for the OE problem, and shed new light on the intricacies of the underlying optimization landscape.

### The Output Estimation problem

We study one of the simplest and most basic problems with partial observability: the *output estimation* (OE) problem. In brief, the goal is to search for a predictor of the output $\mathbf{z}{(t)}$ of a linear dynamical system given partial measurements $\mathbf{y}{(t)}$. For the *true system* with states $\mathbf{x}{(t)}$ and dynamics that evolve according to, | | | ${{{\frac{d}{dt}\mathbf{x}{(t)}} = {{{\mathbf{A}\mathbf{x}}{(t)}} + {\mathbf{w}{(t)}}}},{{{\mathbf{y}{(t)}} = {{{\mathbf{C}\mathbf{x}}{(t)}} + {\mathbf{v}{(t)}}}},{{{\mathbf{z}{(t)}} = {{\mathbf{G}\mathbf{x}}{(t)}}},{{\mathbf{x}{}} = 0}}}},$ | | (1.1) | | | | ${{\mathbf{w}{(t)}\overset{i.i.d}{\sim}\mathcal{N}{(0,\mathbf{W}_{1})}},{\mathbf{v}{(t)}\overset{i.i.d}{\sim}\mathcal{N}{(0,\mathbf{W}_{2})}}},$ | | | the goal is to find the parameters $\mathsf{K} = {(\mathbf{A}_{\mathsf{K}},\mathbf{B}_{\mathsf{K}},\mathbf{C}_{\mathsf{K}})}$ of the *filter* (interchangably, *policy*), that minimizes the steady-state prediction error, In this paper, we study solving the OE problem via model-free methods, where the goal is to search for the optimal filter parameters $\mathsf{K} = {(\mathbf{A}_{\mathsf{K}},\mathbf{B}_{\mathsf{K}},\mathbf{C}_{\mathsf{K}})}$ using direct policy search without knowledge or estimation of the true system parameters $\mathbf{A},\mathbf{C},\mathbf{G},\mathbf{W}_{1},\mathbf{W}_{2}$; cf. Section 2 for a detailed problem description.

### Contributions

In this paper, we propose a novel policy search method which provably converges to a globally optimal $\mathcal{L}_{\text{OE}}$ cost. Despite extensive prior work on *static* policy search (e.g. Fazel et al.; Agarwal et al., our result constitutes the first rigorous guarantee for policy search over *dynamic* policies.

A key concept underpinning our results is the notion of *informativity*, which requires each component of the internal filter state $\hat{\mathbf{x}}$ to capture some information about the true state $\mathbf{x}$ of the system. More precisely, a policy is said to be *informative* if the steady-state correlation matrix $\mathbf{\Sigma}_{12}:={\lim_{T\rightarrow\infty}{\frac{1}{T}{\lbrack{\int_{0}^{T}{\mathbf{x}{(t)}\hat{\mathbf{x}}{(t)}^{\top}{dt}}}\rbrack}}}$ is full-rank.^11^1For simplicity, we assume knowledge of the *dimension* of the true system state, and policies are parameterized so that $\mathbf{x}$ and $\hat{\mathbf{x}}$ are of the same dimension. Our contributions are summarized as follows:

### Limitations of direct policy search

Through simulations and counterexamples, we show that gradient descent on the prediction loss $\mathcal{L}_{\mathtt{O}\mathtt{E}}{( \cdot )}$ can fail to recover the optimal filter for OE problem. While consistent with prior work, the failure of gradient descent remains puzzling, as the OE problem admits a convex reformulation, a fact which at first glance seems to rule out suboptimal stationary points.

### Structure of the OE optimization landscape

We reconcile this apparent contradiction - the existence of convex reformulations and the failure of policy search - by studying cases in which the former breaks down. We show that suboptimal stationary points can arise when the internal state $\hat{\mathbf{x}}$ of the filter is non-informative about the state $\mathbf{x}$ of the true system, in the sense described above. These are precisely the points at which the convex reformulation breaks down. We also establish the converse: when $\hat{\mathbf{x}}$ is "uniformly informative" about $\mathbf{x}$, all stationary points are globally optimal.

### A provably convergent policy search algorithm

Building on this insight, we propose a regularizer $\mathcal{R}$ that ensures the internal state of the learned policy remains "uniformly informative" about the state of the true system. We prove that gradient descent on the regularized objective ${\mathcal{L}_{\mathtt{O}\mathtt{E}}{( \cdot )}} + {\lambda\mathcal{R}{( \cdot )}}$ converges at a $\mathcal{O}\left( {1/T} \right)$ rate to an optimal policy.

### Our techniques

Searching over dynamic policies introduces two key challenges: spurious critical points can arise when one or more factors become "degenerate" in a certain way; changes of basis produce a continuum of "equivalent realizations" of the filter $\mathsf{K}$, some of which are poorly conditioned. Similar challenges have been observed in problems with rotational symmetries, e.g. nonconvex matrix factorization. Neither challenge arises when searching over static policies.

Departing from prior literature on nonconvex factorization problems, which often either leverages closed-form gradient computations and/or the presence of strict-saddles, our approach is centered around the idea of *convex reformulations* of control synthesis problems, and the following fact regarding functions which admit these reformulations, cf. Section H.1 for proof.

### Fact 1.1

Let $f:{{\mathbb{R}}^{n_{x}}\rightarrow{\mathbb{R}}}$ be a differentiable, possibly nonconvex function such that ${\min_{\mathbf{x}}f}{({\mathbf{x}})}$ is finite. There exists a differentiable function $\Psi:{{\mathbb{R}}^{n_{\nu}}\rightarrow{\mathbb{R}}^{n_{x}}}$ satisfying the following two properties: (i) the mapping $\Psi$ is surjective, i.e. for all ${\mathbf{x}} \in {\mathbb{R}}^{n_{x}}$ there exists ${\mathbf{ν}} \in {\mathbb{R}}^{n_{\nu}}$ such that ${\mathbf{x}} = {\Psi{({\mathbf{ν}})}}$, (ii) under the change of variables the function ${f_{cvx}{({\mathbf{ν}})}}:={f{({\Psi{({\mathbf{ν}})}})}}$ is differentiable and *convex*. Then all first-order stationary points, $\mathbf{x}$ s.t ${{\nabla f}{({\mathbf{x}})}} = 0$, are globally optimal.

The OE problem, LQG, and many other related control tasks admit convex reformulations. Given that gradient descent (under additional mild regularity assumptions) converges to stationary points, we might hope that 1.1 guarantees that direct policy search on the OE filter will succeed at finding an optimal policy, when applied to loss functions admitting such convex reformulations. Somewhat surprisingly, we find that this is emphatically not the case: gradient descent on the $\mathcal{L}_{\mathtt{O}\mathtt{E}}$ objective fails to reliably converge to optimal solutions (see Section 3.1).^22^2Failure modes for the LQG problem were presented by Tang et al..

To resolve this paradox, we show that the surjectivity condition of 1.1 may fail for the convex reparametrization of OE: there are filters $\mathsf{K}$ with finite cost $\mathcal{L}_{\mathtt{O}\mathtt{E}}{(\mathsf{K})}$, which are not in the image of the reformulation map $\Psi{( \cdot )}$. We find that degeneracy occurs precisely when *informativity*, defined in Section 1.1 as $\mathbf{\Sigma}_{12,\mathsf{K}}$ having full rank, fails to hold. Conversely, when $\mathbf{\Sigma}_{12,\mathsf{K}}$ is full-rank, the conditions of 1.1 are met and the parametrization behaves as needed. Thus, we identify *non-informativity* - rank deficiency of $\mathbf{\Sigma}_{12,\mathsf{K}}$ - as the fundamental notion of degeneracy corresponding to challenge. Motivated by this observation, we introduce a novel "informativity regularizer" $\mathcal{R}_{\mathtt{i}\mathtt{n}\mathtt{f}\mathtt{o}}{( \cdot )}$ which enforces that $\mathbf{\Sigma}_{12,\mathsf{K}}$ is full rank. Our proposed algorithm, IR-PG alternates between gradient updates on the regularized loss ${\mathcal{L}_{\lambda}{( \cdot )}}:={{\mathcal{L}_{\mathtt{O}\mathtt{E}}{( \cdot )}} + {\lambda\mathcal{R}_{\mathtt{i}\mathtt{n}\mathtt{f}\mathtt{o}}{( \cdot )}}}$, and "reconditioning" steps to ensure well-conditioned realizations of the filters $\mathsf{K}$, thereby addressing challenge above. We stress that our notion of informativity differs from the *minimality* criterion emphasized in Tang et al., whose limitations we discuss in Section 3.1.

In order to achieve our quantitative converge guarantees, we establish numerous results which may be of independent interest, including a quantitative analysis of the OE convex reformulation due to Scherer, and novel bounds on the magnitude of solution to Lyapunov equations under the closed-loop OE filter dynamics. Both arguments appeal to a (quantitative measure of) informativity, suggesting informativity is somehow natural for the OE landscape.

We also develop a quantitative analogue of 1.1 via a paradigm we call *differentiable convex liftings*, or DCLs. Informally, a DCL "lifts" the nonconvex $f$ to a possibly nonconvex, non-smooth function $f_{\mathtt{l}\mathtt{f}\mathtt{t}}$ with $n_{y} \geq n_{x}$ parameters, which may take values in the extended reals so as incorporate constraints. We stress that both the 'lifting' and accommodation of constraints are essential to capture the OE convex reformulation. A DCL further requires existence of a map $\Phi$ and a convex function $f_{cvx}$ with $n_{\nu} \leq n_{y}$ parameters such that ${f_{\mathtt{l}\mathtt{f}\mathtt{t}}{( \cdot )}}:={f_{cvx}{({\Phi{( \cdot )}})}}$. Intuitively, $\Phi$ corresponds to the inverse of the map $\Psi$ in 1.1, though this parameterization allows more flexibility because $n_{y} > n_{\nu}$ may be permitted. For such liftings, the following result strengthens and refines 1.1:

### Theorem 1 (Informal)

Let $f$ be a smooth nonconvex function which admits a *differentiable convex lifting* $(f_{\mathtt{l}\mathtt{f}\mathtt{t}},f_{cvx},\Phi)$ such that $\sigma_{d_{z}}{({{\nabla\Phi}{( \cdot )}})}$ is bounded away from zero. If $f_{cvx}{({\Phi{( \cdot )}})}$ has compact level sets, then any $\mathbf{x}$ such that ${\|{{\nabla f}{(\mathbf{x})}}\|}_{2} \leq \varepsilon$, satisfies ${{f{(\mathbf{x})}} - f_{\star}} \leq {\mathcal{O}(\varepsilon)}$. Here, $f_{\mathtt{l}\mathtt{f}\mathtt{t}}$ and $f_{cvx}$ need not be differentiable, and may only be defined (or finite) on restricted domains.

### Related work

### Solution of the OE problem & Convex reformulation

The solution to the OE problem^33^3Kalman addressed the discrete-time problem, with $\mathbf{G} = \mathbf{C}$. is given by the celebrated *Kalman filter*. The problem is also a special case of LQG, cf. Doyle et al.. Solution methods based on linear matrix inequalities (LMI) for OE - as well as many other control problems, including $\mathcal{H}_{2}$, $\mathcal{H}_{\infty}$, and mixed $\mathcal{H}_{2}/\mathcal{H}_{\infty}$ synthesis - were developed, concurrently and independently, by Scherer et al. and Masubuchi et al.. The methods were based on convex reformulations of the variety described in Section 1.2, and represent non-trivial generalizations of the well-known change of variables used to obtain LMI formulations of static state feedback problems, cf. Thorp and Barmish; Bernussou et al.. It has long been appreciated that most cost functions optimized for controller synthesis are *nonconvex*. Such problems are usually solved indirectly, e.g. by reconstructing policies from the solutions of Riccati equations or LMIs, or by using (model-based) policy parametrizations that make the cost function convex, e.g. Youla et al.; Kučera.

### Direct policy search for control with full state observation

Recent years have witnessed a resurgence of interest in direct policy search, driven perhaps in part by the success of such approaches in reinforcement learning, e.g. Schulman et al.; Andrychowicz et al.. Specifically, Fazel et al. established global convergence of policy gradient methods on the discrete-time linear quadratic regulator (LQR) problem, the simplest continuous state-action optimal control problem. Subsequent work has sharpened rates, analyzed convergence under more general frameworks, and extended the analysis to work in continuous-time. Beyond LQR, Zhang et al. analyzed global convergence of policy search for mixed $\mathcal{H}_{2}/\mathcal{H}_{\infty}$ control and risk-sensitive control. Furieri et al. and Li et al. established the convergence of policy search for certain distributed control problems. Sun and Fazel also considered analysis via convex reformulations, for state feedback problems. For discrete state-action (discounted) Markov decision processes (MDPs), Agarwal et al. established convergence rates for a variety of policy gradient methods with both tabular and parametric policies, cf. also Bhandari and Russo. All of these works considered *static* state-feedback policies, with perfect state information.

### Problems with partial observation

For problems with partial observation, optimal policies are typically dynamic, so as to incorporate information from the entire past history of observations. The most relevant related work is Tang et al., which studied the optimization landscape of the LQG problem. They establish that all stationary points corresponding to controllable and observable controllers are globally optimal. They also show (both empirically and via theoretical counterexamples) that gradient descent may fail to converge to globally optimal policies; a finding that, as we shall show, remains valid even for the simpler OE problem. Fatkhullin and Polyak also considered linear quadratic control in the partially observed setting, but restrict their attention to *static* output feedback policies, and provide conditions under which gradient descent converges to (possibly suboptimal) stationary points.

### Organization

This paper is organized as follows. Section 2 provides the relevant preliminaries and assumptions for our setting, as well as details for our interaction protocol. Section 3 provides our main results: first, a number of counterexample examples explaining the challenges of policy search over dynamic filters, and limitations of past work; second, a detailed distribution of our algorithm, IR-PG; third, a rigorous convergence guarantee. Section 4 presents the numerical examples that illustrate the performance of our algorithm. Section 5 describes our main technical hammer - DCLs - and how they afford quantitative convergence guarantees for gradient descent. Finally, Section 6 provides the skeleton of the proofs of our main theorems. We provide concluding remarks in Section 7, and detail the organization of the appendix in Appendix A.

### Preliminaries

Before presenting our main results in Section 3, we first introduce some of the relevant definitions, and provide the reader with some the relevant background on prediction in partially-observed dynamical systems.

### Notation

We let lower case variables in script font $({\mathbf{x}},{\mathbf{y}},{\mathbf{z}})$ denote abstract parameters for optimization; standard vectors $(\mathbf{x},\mathbf{y},\mathbf{z})$ are reserved for random variables and/or dynamical quantities. Matrices are denoted in bold, e.g $\mathbf{X},\mathbf{Y},\mathbf{Z}$. For vectors, $\|\mathbf{x}\|$ denotes the Euclidean norm, $\|\mathbf{X}\|$ denotes the matrix operator norm and ${\|\mathbf{X}\|}_{F}$, the Frobenius norm.

We let $\mathcal{S}^{n - 1}$ denote the unit sphere in ${\mathbb{R}}^{n}$. We denote the set of symmetric $n \times n$ matrices as ${\mathbb{S}}^{n}$; the set of nonstrictly positive semidefinite (PSD) matrices as ${\mathbb{S}}_{+}^{n}$, strictly positive definite (PD) matrices as ${\mathbb{S}}_{+ +}^{n}$, and invertible matrices as ${\mathbb{G}}{\mathbb{L}}{(n)}$. Given ${\mathbf{X}_{1},\mathbf{X}_{2}} \in {\mathbb{S}}^{n}$, we let $\mathbf{X}_{1} \preceq \mathbf{X}_{2}$ denote nonstrict PSD inequality, with $\mathbf{X}_{1} \prec \mathbf{X}_{2}$ denoting strict inequality. Given a square matrix $\mathbf{A} \in {\mathbb{R}}^{n \times n}$, $\exp{(\mathbf{A})}$ denotes the matrix exponential. For $\mathbf{A}$ with real eigenvalues, ${{{\lambda_{i}{(\mathbf{A})}},i} = 1},{\ldots,n}$ denotes its eigenvalues in descending order, with ${\lambda_{\max}{(\mathbf{A})}} = {\lambda_{1}{(\mathbf{A})}}$ and ${\lambda_{\min}{(\mathbf{A})}} = {\lambda_{n}{(\mathbf{A})}}$; when $\mathbf{A}$ has complex eigenvalues, $\lambda_{i}{(\mathbf{A})}$ are arranged in an arbitrary order. For general rectangular matrices $\mathbf{A} \in {\mathbb{R}}^{m \times n}$, ${{{\sigma_{i}{(\mathbf{A})}},i} = 1},{\ldots,n}$ denotes its singular values in descending order. We use $\mathbf{I}_{n}$ to denote the identity matrix with dimension $n \times n$, and omit $n$ when the dimension is clear from context.

We use parentheses to denote parameter concatenation: e.g. $\overline{\mathbf{X}} = {(\mathbf{X}_{1},\mathbf{X}_{2},\mathbf{X}_{3})} \in {{\mathbb{R}}^{n_{1} \times m_{1}} \times {\mathbb{R}}^{n_{2} \times m_{2}} \times {\mathbb{R}}^{n_{3} \times m_{3}}}$ for $\mathbf{X}_{i} \in {\mathbb{R}}^{n_{i} \times m_{i}}$, and we define Euclidean norms of concatenation in the natural way (e.g. ${\|\overline{\mathbf{X}}\|}_{\ell_{2}} = \sqrt{\sum_{i}{\|\mathbf{X}_{i}\|}_{F}^{2}}$ for the previous example $\overline{\mathbf{X}} = {(\mathbf{X}_{1},\mathbf{X}_{2},\mathbf{X}_{3})}$).

### Output Estimation (OE)

As outlined in the introduction, we consider the problem of predicting the outputs of a partially observed linear dynamical system. We refer to the dynamical system defined in Eq. 1.1 as the *true system*, with states ${\mathbf{x}{(t)}} \in {\mathbb{R}}^{n}$, observations ${\mathbf{y}{(t)}} \in {\mathbb{R}}^{m}$, and performance outputs ${\mathbf{z}{(t)}} \in {\mathbb{R}}^{p}$. To ensure the dynamics have a well-defined steady-state, we assume that $\mathbf{A}$ is stable.

### Assumption 2.1

The matrix $\mathbf{A}$ is *Hurwitz stable*. That is, the real components of all its eigenvalues are strictly negative: ${\Re{\lbrack{\lambda_{i}{(\mathbf{A})}}\rbrack}} < 0$ for $i \in {\lbrack n\rbrack}$.

Because these policies only access the system outputs, and are only evaluated in relation to system outputs, we assume that the true system state is *observable*. Further, we assume that dynamics are subject to sufficiently rich noise excitations.

### Assumption 2.2

The pair $(\mathbf{A},\mathbf{C})$ in Eq. 1.1 is observable. That is, the observability Gramian defined as is strictly positive definite.

### Assumption 2.3

We assume that the noise matrices $\mathbf{W}_{1}$ and $\mathbf{W}_{2}$ are strictly positive definite.^44^4We may relax this assumption to $(\mathbf{A},\mathbf{W}_{1})$ controllable.

As stated previously, we restrict our attention to finding the best dynamic filter within the parametric family described in Eq. 1.2. Note that this family contains the *Bayes optimal predictor* for the $\mathcal{L}_{\mathtt{O}\mathtt{E}}$ objective, as we will later describe in more detail. We review a number of basic facts:

### Steady state distributions

We define $\mathcal{K}_{\mathtt{s}\mathtt{t}\mathtt{a}\mathtt{b}}:=\left\{ \mathsf{K}:{\mathbf{A}_{\mathsf{K}}\text{~is Hurwitz-stable}} \right\}$ to be the set of filters such that $\mathbf{A}_{\mathsf{K}}$ is stable. Under Assumption 2.1 ‣ 2 Preliminaries ‣ Globally Convergent Policy Search over Dynamic Filters for Output Estimation"), Section E.1 shows this equivalent to stability of the closed-loop matrix $\mathbf{A}_{{cl},\mathsf{K}}$.

Stability of $\mathbf{A}_{{cl},\mathsf{K}}$ is a sufficient condition for $\mathcal{L}_{\mathtt{O}\mathtt{E}}{(\mathsf{K})}$ to be finite, and for the following limiting covariance to be well defined, This steady-state covariance is given by the solution to the continuous-time Lyapunov equation, Notice that $\mathbf{\Sigma}_{\mathsf{K}}$ depends only on $(\mathbf{A}_{\mathsf{K}},\mathbf{B}_{\mathsf{K}})$, but not on $\mathbf{C}_{\mathsf{K}}$, and that the first $n \times n$ block of $\mathbf{\Sigma}_{\mathsf{K}}$ does not depend on the choice of filter $\mathsf{K}$ at all. To highlight these distinctions, we partition matrices $\mathbf{\Sigma} \in {\mathbb{R}}^{{{2n} \times 2}n}$ as and define $\mathcal{K}_{\mathtt{c}\mathtt{t}\mathtt{r}\mathtt{b}}:={\{{\mathsf{K} \in \mathcal{K}_{\mathtt{s}\mathtt{t}\mathtt{a}\mathtt{b}}}:{\mathbf{\Sigma}_{22,\mathsf{K}} \succ 0}\}}$ as the set of filters whose internal state covariance is full rank. We refer to these as the *controllable* policies, as these are precise the policies for which the pair $(\mathbf{A}_{\mathsf{K}},\mathbf{B}_{\mathsf{K}})$ is controllable.^55^5Controllability is the "dual" of observabilitity, and is equivalent to observability of $(\mathbf{A}_{\mathsf{K}}^{\top},\mathbf{B}_{\mathsf{K}}^{\top})$, cf. Section E.1.

### Equivalent realizations

Contrary to static feedback policies, such as LQR,there are many different ways of parametrizing a given *dynamic* feedback policy, all of which have exactly the same input-output behavior. In particular, given an invertible matrix $\mathbf{S} \in {{\mathbb{G}}{\mathbb{L}}{(n)}}$, the OE loss of a filter $\mathsf{K}$ is invariant under the following class of similarity transforms: Formally, for any $\mathsf{K} \in \mathcal{K}_{\mathtt{s}\mathtt{t}\mathtt{a}\mathtt{b}}$ and any $\mathbf{S} \in {{\mathbb{G}}{\mathbb{L}}{(n)}}$, ${\mathcal{L}_{\mathtt{O}\mathtt{E}}{(\mathsf{K})}} = {\mathcal{L}_{\mathtt{O}\mathtt{E}}{({{\mathsf{S}\mathsf{i}\mathsf{m}}_{\mathbf{S}}{(\mathsf{K})}})}}$. We say that $\mathsf{K}$ and $\mathsf{K}'$ are *equivalent realizations* if they are related by a similarity transformation ${{\mathsf{S}\mathsf{i}\mathsf{m}}_{\mathbf{S}}{(\mathsf{K})}} = \mathsf{K}'$ for some $\mathbf{S} \in {{\mathbb{G}}{\mathbb{L}}{(n)}}$.^66^6This is a symmetric relationship, since then ${{\mathsf{S}\mathsf{i}\mathsf{m}}_{\mathbf{S}^{- 1}}{(\mathsf{K}')}} = \mathsf{K}$, and hence equivalent policies form an equivalence class. Note that the set $\mathcal{K}_{\mathtt{c}\mathtt{t}\mathtt{r}\mathtt{b}}$ is also preserved under similarity transformation.

### Optimal policies

The landmark result by Kalman shows that for the system defined by $(\mathbf{A},\mathbf{C},\mathbf{W}_{1},\mathbf{W}_{2})$ the Kalman filter $\mathsf{K}_{\star} = {({\mathbf{A} - {\mathbf{L}_{\star}\mathbf{C}}},\mathbf{L}_{\star},\mathbf{G})}$ achieves minimal $\mathcal{L}_{\mathtt{O}\mathtt{E}}$ loss. Here, $\mathbf{L}_{\star}$ is the Kalman gain which is defined in terms of the solution of the following Riccati equation: We define the set of optimal filters $\mathcal{K}_{\mathtt{o}\mathtt{p}\mathtt{t}}$ to be those which are equivalent to the Kalman filter:

### Restricted problem setting

The problem description outlined in Section 2.2 ‣ 2 Preliminaries ‣ Globally Convergent Policy Search over Dynamic Filters for Output Estimation"), including Assumptions 2.1 ‣ 2 Preliminaries ‣ Globally Convergent Policy Search over Dynamic Filters for Output Estimation"), 2.2 ‣ 2 Preliminaries ‣ Globally Convergent Policy Search over Dynamic Filters for Output Estimation") and 2.3 ‣ 2 Preliminaries ‣ Globally Convergent Policy Search over Dynamic Filters for Output Estimation"), constitutes the standard OE problem, well-known in control theory, cf.. In this paper, we will make the following additional assumption that restricts the class of OE problems we consider. Further discussion on the utility and necessity of this assumption (for our analysis) is provided in Section 3.2 and Appendix D; the latter also shows that Assumption 2.4 holds for "generic" problem instances.

### Assumption 2.4

The optimal policy is itself controllable, i.e. for all ${(\mathbf{A}_{\mathsf{K}_{\star}},\mathbf{B}_{\mathsf{K}_{\star}},\mathbf{C}_{\mathsf{K}_{\star}})} \in \mathcal{K}_{\mathtt{o}\mathtt{p}\mathtt{t}}$ we have that $(\mathbf{A}_{\mathsf{K}_{\star}},\mathbf{B}_{\mathsf{K}_{\star}})$ is controllable.

Here, we simply remark that Assumption 2.4 ensures that the regularizer $\mathcal{R}_{\mathtt{i}\mathtt{n}\mathtt{f}\mathtt{o}}{(\mathsf{K})}$, responsible for maintaining informativity of the policy $\mathsf{K}$, is well-defined at the optimal policy.

### Interaction protocol

In the spirit of model-free methods, we introduce algorithms which work only assuming access to cost and gradient evaluation oracles. We abstract away the particular implementation of these oracles to simplify our presentation and assume that they are exact, in order to focus on the overall optimization landscape of the OE problem. More formally, for any filter $\mathsf{K} \in \mathcal{K}_{\mathtt{s}\mathtt{t}\mathtt{a}\mathtt{b}}$, ${\mathsf{E}\mathsf{v}\mathsf{a}\mathsf{l}}{(\mathsf{K},\mathcal{L}_{\mathtt{O}\mathtt{E}})}$ returns the OE cost, $\mathcal{L}_{\mathtt{O}\mathtt{E}}{(\mathsf{K})}$. ${\mathsf{G}\mathsf{r}\mathsf{a}\mathsf{d}}{(\mathsf{K},\mathcal{L}_{\mathtt{O}\mathtt{E}})}$ return the gradient of the OE cost, ${\nabla\mathcal{L}_{\mathtt{O}\mathtt{E}}}{(\mathsf{K})}$.

Despite this simplification, we would like to again emphasize that these can be efficiently approximated in finite samples, and purely on the basis of *observations* $\mathbf{y}_{t}$ subsampled in in discrete intervals. For further discussion, please see Appendix C.

Lastly, in addition to standard cost and gradient evaluations of the $\mathcal{L}_{\mathtt{O}\mathtt{E}}$ loss, as part of our algorithm, we further require access to gradient and cost evaluations of smooth functions of the stationary-state covariance. Specifically, if $f:{{\mathbb{S}}_{+}^{2n}\rightarrow{\mathbb{R}}}$ is a function of the covariance matrix $\mathsf{K}$, we assume we can compute ${\mathsf{E}\mathsf{v}\mathsf{a}\mathsf{l}}_{cov}{(\mathsf{K},f)}$ which returns the $f{(\mathbf{\Sigma}_{\mathsf{K}})}$ and ${\mathsf{G}\mathsf{r}\mathsf{a}\mathsf{d}}_{cov}{(\mathsf{K},f)}$ which returns ${\nabla_{\mathsf{K}}f}{(\mathbf{\Sigma}_{\mathsf{K}})}$. In Section C.2, we show that these oracles can be implemented without direct state access by "subsampling" multiple observations at different time increments.

### Main Results

In this section, we present the main contributions of our work. After demonstrating that the OE cost function contains stationary points that are not globally optimal, we present informativity-regularized policy gradient (IR-PG), a direct policy search algorithm based on a novel regularization strategy to preserve *informativity*, introduced in Section 1.2. We state a formal convergence result showing that IR-PG converges to a globally optimal filter at a $\mathcal{O}\left( {1/T} \right)$ rate.

### Existence of suboptimal stationary points

Perhaps the simplest model-free approach to the OE problem is to run gradient descent on the loss function: for some stepsize(s) $\eta_{t} > 0$. Under mild assumptions on the loss function $\mathcal{L}_{\mathtt{O}\mathtt{E}}$, gradient descent will converge to a first-order stationary point of $\mathcal{L}_{\mathtt{O}\mathtt{E}}$. Unfortunately, despite the existence of a convex reformulation and 1.1, the $\mathcal{L}_{\mathtt{O}\mathtt{E}}$ loss function contains suboptimal stationary points:

### Example 3.1

Consider the OE instance given by $\mathbf{A} = {- \mathbf{I}_{2}}$, $\mathbf{C} = \mathbf{I}_{2}$, $\mathbf{W}_{1} = {3 \times \mathbf{I}_{2}}$, $\mathbf{W}_{2} = \mathbf{I}_{2}$, and the filter $\mathsf{K}_{bad}$ given by $\mathbf{A}_{bad} = {- {\varepsilon \times \mathbf{I}_{2}}}$, $\varepsilon > 0$, $\mathbf{B}_{bad} = \mathbf{0}_{2}$, $\mathbf{C}_{bad} = \mathbf{0}_{2}$. $\mathsf{K}_{bad}$ constitutes a suboptimal stationary point of $\mathcal{L}_{\mathtt{O}\mathtt{E}}$ for this OE instance.

A formal proof of this claim is given in Section F.1, however, one can easily verify that the cost is invariant under perturbations to any single parameter of the filter. Specifically: (i) perturbations to $\mathbf{A}_{bad}$ and $\mathbf{B}_{bad}$ do not change the cost, because $\mathbf{C}_{bad} = \mathbf{0}$ and thus the filter output $\mathbf{z}{(t)}$ is always zero, and (ii) perturbations to $\mathbf{C}_{bad}$ do not change the cost either, because $\mathbf{B}_{bad} = \mathbf{0}$ means that the internal state $\hat{\mathbf{x}}$ of the filter is always zero, which again implies ${\mathbf{z}{(t)}} \equiv 0$. Consequently, the gradient at $\mathsf{K}_{bad}$ is zero. Suboptimality can be seen by noticing that $\mathsf{K}_{bad}$ cannot be transformed to the non-zero $\mathsf{K}_{\star}$ under any similarity transformation. The same is true for any OE instance: every filter with $\mathbf{B}_{bad} = \mathbf{0}$, $\mathbf{C}_{bad} = \mathbf{0}$, and $\mathbf{A}_{bad}$ being stable is a suboptimal stationary point of $\mathcal{L}_{\mathtt{O}\mathtt{E}}$. The existence of such suboptimal stationary points cautions against running simple gradient descent, and motivates our proposed regularization strategy.

### The perils of enforcing minimality

A filter $\mathsf{K}$ is *minimal* if $(\mathbf{A}_{\mathsf{K}},\mathbf{B}_{\mathsf{K}})$ is controllable, and $(\mathbf{A}_{\mathsf{K}},\mathbf{C}_{\mathsf{K}})$ is observable. Example 3.1 is the extreme case of a *non-minimal* filter, since $\mathbf{B}_{bad} = \mathbf{C}_{bad} = \mathbf{0}_{2}$. Conversely, as a special case of LQG, the OE problem inherits the property that all stationary points corresponding to *minimal* filters are globally optimal. Therefore, it may be natural to ask: *can a local search algorithm enforce minimality to avoid suboptimal stationary points?* A classical result due to Brockett suggests not: the set of minimal $n$-th order single-input-single-output transfer functions (e.g. filters) is the disjoint union of $n + 1$ open sets. Thus it is impossible for a continuous path to pass from one of these open sets to another without entering a region corresponding to a non-minimal filter, suggesting that a local search algorithm regularized to ensure minimality at every iteration may never converge to the optimal solution. See Section F.2 for further discussion and supporting numerical experiments.

### Suboptimal controllable stationary points

Given the drawbacks of enforcing minimality, one may wonder whether it is sufficient to enforce controllability alone. In Example 3.1 above - and indeed, for all the examples in Tang et al. of suboptimal stationary points in the LQG landscape - there is a loss of both observability ($\mathbf{C}_{bad} = \mathbf{0}$) and controllability ($\mathbf{B}_{bad} = \mathbf{0}$). Do suboptimal *controllable* stationary points exist? Unfortunately, the answer is affirmative, as the following example demonstrates:

### Example 3.2

Consider the same OE instance from Example 3.1, i.e. $\mathbf{A} = {- \mathbf{I}_{2}}$, $\mathbf{C} = \mathbf{I}_{2}$, $\mathbf{W}_{1} = {3 \times \mathbf{I}_{2}}$, $\mathbf{W}_{2} = \mathbf{I}_{2}$. Consider the (family of) filter(s) $\mathsf{K}_{bad}$ given by For any $\gamma > 0$ the followings are true: (i) $\mathsf{K}_{bad}$ is stable: $\mathsf{K}_{bad} \in \mathcal{K}_{\mathtt{s}\mathtt{t}\mathtt{a}\mathtt{b}}$, (ii) $\mathsf{K}_{bad}$ is controllable: $\mathsf{K}_{bad} \in \mathcal{K}_{\mathtt{c}\mathtt{t}\mathtt{r}\mathtt{b}}$, $\Sigma_{\mathsf{K}_{bad},22} \succ 0$, (iii) $\mathsf{K}_{bad}$ is a first-order stationary point: ${{\nabla\mathcal{L}_{\mathtt{O}\mathtt{E}}}{(\mathsf{K}_{bad})}} = 0$, (iv) $\mathsf{K}_{bad}$ is strictly suboptimal: $\mathsf{K}_{bad} \notin \mathcal{K}_{\mathtt{o}\mathtt{p}\mathtt{t}}$, and (v) $\mathsf{K}_{bad}$ is not informative: $\mathbf{\Sigma}_{12,\mathsf{K}_{bad}}$ is not full-rank. See Proposition F.1 for proof.

Though $\mathsf{K}_{bad}$ in Eq. 3.2 is controllable, because $\mathbf{\Sigma}_{12,\mathsf{K}_{bad}}$ is rank deficient it corresponds to a suboptimal stationary point. This IR-PG circumvents such points by enforcing informativity ($\mathbf{\Sigma}_{12,\mathsf{K}}$ being full-rank) at all iterations, via the regularizer $\mathcal{R}_{\mathtt{i}\mathtt{n}\mathtt{f}\mathtt{o}}$.

### Difficulty of escaping suboptimal saddle points

The existence of suboptimal stationary points does not necessarily rule out the efficacy of gradient descent. Recent work has established that variations of gradient descent - e.g. with appropriate random perturbations or acceleration - efficiently escape strict saddle-points, i.e. points at which the minimum eigenvalue of the Hessian is strictly negative. In light of such results, it is reasonable to ask whether suboptimal stationary points of the kind identified in Example 3.2 are problematic for gradient descent. Specifically, are such stationary points strict saddles? It turns out that $\mathsf{K}_{bad}$ in Example 3.2 *does* correspond to a strict saddle point; however, the minimum eigenvalue of the Hessian can be made arbitrarily close to zero by making $\gamma$ sufficiently large. See Section F.3 for details.

### A provably convergent algorithm

The previous discussion puts us in a bind: we cannot regularize to preserve minimality because of path-disconnectedness. Yet, controllability is not enough to rule out suboptimal stationary points. The construction of Example 3.2 hinges on point (v): the cross covariance $\mathbf{\Sigma}_{12,\mathsf{K}_{bad}}$ between the true system state $\mathbf{x}{(t)}$ and internal policy state $\hat{\mathbf{x}}{(t)}$ is *rank deficient*. We call such filters *non-informative*. Under Assumption 2.4, however, all optimal policies $\mathsf{K} \in \mathcal{K}_{\mathtt{o}\mathtt{p}\mathtt{t}}$ must be *informative*, that is, lie in the set $\mathcal{K}_{\mathtt{i}\mathtt{n}\mathtt{f}\mathtt{o}}:={\{{\mathsf{K} \in \mathcal{K}_{\mathtt{s}\mathtt{t}\mathtt{a}\mathtt{b}}}:{{{rank}{(\mathbf{\Sigma}_{12,\mathsf{K}})}} = n}\}}$ (see Section E.3 for proof).

### Lemma 3.1

Under Assumptions 2.2 ‣ 2 Preliminaries ‣ Globally Convergent Policy Search over Dynamic Filters for Output Estimation"), 2.1 ‣ 2 Preliminaries ‣ Globally Convergent Policy Search over Dynamic Filters for Output Estimation"), 2.3 ‣ 2 Preliminaries ‣ Globally Convergent Policy Search over Dynamic Filters for Output Estimation") and 2.4, then $\mathcal{K}_{\mathtt{o}\mathtt{p}\mathtt{t}} \subset \mathcal{K}_{\mathtt{i}\mathtt{n}\mathtt{f}\mathtt{o}} \subset \mathcal{K}_{\mathtt{c}\mathtt{t}\mathtt{r}\mathtt{b}}$, and $\mathcal{K}_{\mathtt{i}\mathtt{n}\mathtt{f}\mathtt{o}}$ is an open set.

Our key insight is that informativity is also *sufficient* to ensure optimality of stationary points, but does not cause path-connectedness issues as it did for minimality (see Section 6.3 for the proof).

### Theorem 2

Let $\mathsf{K} \in \mathcal{K}_{\mathtt{i}\mathtt{n}\mathtt{f}\mathtt{o}}$; then (i) there is a continuous path lying in $\mathcal{K}_{\mathtt{i}\mathtt{n}\mathtt{f}\mathtt{o}}$ connecting $\mathsf{K}$ to some $\mathsf{K}_{\star} \in \mathcal{K}_{\mathtt{o}\mathtt{p}\mathtt{t}}$ and (ii) if ${{\nabla\mathcal{L}_{\mathtt{O}\mathtt{E}}}{(\mathsf{K})}} = \mathbf{0}$, then $\mathsf{K} \in \mathcal{K}_{\mathtt{o}\mathtt{p}\mathtt{t}}$.

Theorem 2 suggests that gradient descent with enforced informativity should converge to optimal filters. It is not, however, implied by the landscape analysis of Tang et al., which focuses solely on *minimal* stationary points. But numerous challenges remain: how can one enforce informativity in a smooth fashion? what quantitative measure of informativity provides quantitative suboptimality guarantees on approximate first-order stationary points? Given that $\mathcal{L}_{\mathtt{O}\mathtt{E}}{(\mathsf{K})}$ need not have compact level sets (see Section F.3), how does one ensure that the iterates of policy search do not escape to infinity, or reach regions where the loss of smoothness is arbitrarily poor?

### The explained covariance matrix

In light of Theorem 2, we design a policy search algorithm which ensures that $\mathbf{\Sigma}_{12,\mathsf{K}}$ remains full-rank throughout the search, but does so in a quantitative fashion. Our central object is the *explained covariance matrix*, which measures how much of the covariance of the steady-state system $\mathbf{x}{(t)}$ is explained by the internal filter state ${\hat{\mathbf{x}}}_{\mathsf{K}}{(t)}$ in the large $t$ limit: $\mathbf{Z}_{\mathsf{K}}:={\lim_{t\rightarrow\infty}\left({{\operatorname{Cov}{\lbrack{\mathbf{x}{(t)}}\rbrack}} - {{\mathbb{E}}{\lbrack{\operatorname{Cov}{\lbrack{{\mathbf{x}{(t)}} \mid {{\hat{\mathbf{x}}}_{\mathsf{K}}{(t)}}}\rbrack}}\rbrack}}} \right)}$. When $\mathsf{K} \in \mathcal{K}_{\mathtt{c}\mathtt{t}\mathtt{r}\mathtt{b}}$, $\mathbf{Z}_{\mathsf{K}}$ admits an elegant closed-form expression, which provides an alternative definition of $\mathcal{K}_{\mathtt{i}\mathtt{n}\mathtt{f}\mathtt{o}}$: Since $\mathbf{Z}_{\mathsf{K}}$ is invariant under similarity transformations, as per Eq. 2.3 ‣ 2 Preliminaries ‣ Globally Convergent Policy Search over Dynamic Filters for Output Estimation"), $\mathbf{Z}_{\mathsf{K}}$ can be interpreted as a normalized analogue of $\mathbf{\Sigma}_{12,\mathsf{K}}$. Informally, the quadratic form $v^{\top}\mathbf{Z}_{\mathsf{K}}v$ is a sufficient statistic for how much information $\hat{\mathbf{x}}{(t)}$ contains about the "$v$-direction" of $\mathbf{x}{(t)}$; see Section E.6 for a precise statement.

### Explained-covariance regularization

We preserve informativity by ensuring our iterates satisfy $\mathbf{Z}_{\mathsf{K}} \succ 0$. To this end, we run gradient descent on the regularized objective for some $\lambda > 0$: This choice of regularizer has several important properties. First, $\mathcal{R}_{\mathtt{i}\mathtt{n}\mathtt{f}\mathtt{o}}$ is always non-negative, and tends to $\infty$ as $\mathbf{Z}_{\mathsf{K}}$ approaches singularity. Furthermore, the value of the regularizer is invariant under similarity transformations(as per Eq. 2.3 ‣ 2 Preliminaries ‣ Globally Convergent Policy Search over Dynamic Filters for Output Estimation")). Next, many of the essential quantities arising in our analysis can be bounded in terms of $\mathbf{Z}_{\mathsf{K}}^{- 1}$, justifying $\mathbf{Z}_{\mathsf{K}}$ is a natural quantitative measure of informativity. Lastly, the set of global-minimizers of $\mathcal{R}_{\mathtt{i}\mathtt{n}\mathtt{f}\mathtt{o}}{(\cdot)}$ are precisely the optimal filters for the OE problem, as per the following lemma (see Section E.3 for proof).

### Lemma 3.2 (Existence of maximal $\mathbf{Z}_{\mathsf{K}}$)

Under Assumptions 2.1 ‣ 2 Preliminaries ‣ Globally Convergent Policy Search over Dynamic Filters for Output Estimation"), 2.2 ‣ 2 Preliminaries ‣ Globally Convergent Policy Search over Dynamic Filters for Output Estimation") and 2.3 ‣ 2 Preliminaries ‣ Globally Convergent Policy Search over Dynamic Filters for Output Estimation"), there exists a unique $\mathbf{Z}_{\star} \succ 0$ such that $\mathbf{Z}_{\star} = \mathbf{Z}_{\mathsf{K}}$ if and only if $\mathsf{K} \in \mathcal{K}_{\mathtt{o}\mathtt{p}\mathtt{t}}$, and $\mathbf{Z}_{\star} \succeq \mathbf{Z}_{\mathsf{K}}$ for all $\mathsf{K} \in {\mathcal{K}_{\mathtt{c}\mathtt{t}\mathtt{r}\mathtt{b}} \smallsetminus \mathcal{K}_{\mathtt{o}\mathtt{p}\mathtt{t}}}$. Consequently, Lemma 3.2. ‣ Explained-covariance regularization. ‣ 3.2 A provably convergent algorithm ‣ 3 Main Results ‣ Globally Convergent Policy Search over Dynamic Filters for Output Estimation") directly implies that the suboptimality of $\mathcal{L}_{\lambda}{(\cdot)}$ upper bounds the suboptimality in $\mathcal{L}_{\mathtt{O}\mathtt{E}}{(\cdot)}$, so we can minimize $\mathcal{L}_{\lambda}$ as a proxy for minimizing $\mathcal{L}_{\mathtt{O}\mathtt{E}}$.

### Corollary 3.1

For any $\mathsf{K}$, we have ${{\mathcal{L}_{\mathtt{O}\mathtt{E}}{(\mathsf{K})}} - {{\min_{\mathsf{K}'}\mathcal{L}_{\mathtt{O}\mathtt{E}}}{(\mathsf{K}')}}} \leq {{\mathcal{L}_{\lambda}{(\mathsf{K})}} - {{\min_{\mathsf{K}'}\mathcal{L}_{\lambda}}{(\mathsf{K}')}}}$.

### Reconditioning

In addition to regularization, we introduce an additional normalization step between policy updates to ensure the iterates produced by our algorithm have well-conditioned covariance matrices; this in turn ensures the iterates produced by our algorithm remain in a compact set, and that the smoothness of $\mathcal{L}_{\lambda}$ is uniformly bounded. For any filter $\mathsf{K} \in \mathcal{K}_{\mathtt{c}\mathtt{t}\mathtt{r}\mathtt{b}}$ such that $\mathbf{\Sigma}_{22,\mathsf{K}} \succ 0$, the reconditioning operator ${\mathsf{r}\mathsf{e}\mathsf{c}\mathsf{o}\mathsf{n}\mathsf{d}}{(\mathsf{K})}$ returns a filter $\mathsf{K}'$ which is equivalent to $\mathsf{K}$, but for which $\mathbf{\Sigma}_{22,\mathsf{K}'} = \mathbf{I}_{n}$. Formally^77^7Our proposed algorithm also works with an approximate balancing $\overset{\sim}{\mathsf{r}\mathsf{e}\mathsf{c}\mathsf{o}\mathsf{n}\mathsf{d}}{(\cdot)}$, where $\overset{\sim}{\mathsf{r}\mathsf{e}\mathsf{c}\mathsf{o}\mathsf{n}\mathsf{d}}{(\mathsf{K})}$ returns a $\mathsf{K}'$ which is equivalent to $\mathsf{K}$, and ${\|{\mathbf{\Sigma}_{22,\mathsf{K}'} - \mathbf{I}_{n}}\|} \leq \varepsilon$ for some tolerance $\varepsilon > 0$ (e.g. $\varepsilon = {1/8}$)., Since $\mathsf{K}$ and $\mathsf{K}' = {{\mathsf{r}\mathsf{e}\mathsf{c}\mathsf{o}\mathsf{n}\mathsf{d}}{(\mathsf{K})}}$ are equivalent realizations, we have ${\mathcal{L}_{\mathtt{O}\mathtt{E}}{(\mathsf{K})}} = {\mathcal{L}_{\mathtt{O}\mathtt{E}}{(\mathsf{K}')}}$, ${\mathcal{R}_{\mathtt{i}\mathtt{n}\mathtt{f}\mathtt{o}}{(\mathsf{K})}} = {\mathcal{R}_{\mathtt{i}\mathtt{n}\mathtt{f}\mathtt{o}}{(\mathsf{K}')}}$, and thus ${\mathcal{L}_{\lambda}{(\mathsf{K})}} = {\mathcal{L}_{\lambda}{(\mathsf{K}')}}$.

### Statement of IR-PG

We can now describe IR-PG, whose pseudocode is displayed in Algorithm 1. IR-PG applies gradient descent on the regularized $\mathcal{L}_{\mathtt{O}\mathtt{E}}$ objective, with an additional balancing step between gradient updates. Section B.1 provides a variant where the step size is chosen by backtracking line-search, which enjoys the same rigorous convergence guarantees.

To guarantee convergence to an optimal filter (and finiteness of $\mathcal{L}_{\lambda}$), we need to initialize at a filter such that $\mathbf{Z}_{\mathsf{K}_{0}} \succ 0$, i.e. $\mathsf{K}_{0} \in \mathcal{K}_{\mathtt{i}\mathtt{n}\mathtt{f}\mathtt{o}}$. Fortunately, random initializations from a continuous distribution satisfy this condition with probability $1$ (see Section E.7 for a formal statement and proof).

1:Input: Initial K0 ∈ 𝒦info, step size η > 0, regularization parameter λ > 0 3:for each iteration s = 0, 1, 2, … do 4: Recondition ${\overset{\sim}{\mathsf{K}}}_{t} = {{\mathsf{r}\mathsf{e}\mathsf{c}\mathsf{o}\mathsf{n}\mathsf{d}}{(\mathsf{K}_{t})}}$, where recond (⋅) is defined in Eq. 3.4. 5: Compute $\nabla_{s} = {{\nabla\mathcal{L}_{\lambda}}{({\overset{\sim}{\mathsf{K}}}_{t})}}$. 6: Update $\mathsf{K}_{t + 1}\leftarrow{{\overset{\sim}{\mathsf{K}}}_{t} - {\eta\nabla_{t}}}$. Algorithm 1 Informativity-regularized Policy Gradient (IR-PG)

### Formal guarantees

We conclude this section by stating the formal convergence guarantee for IR-PG. Our results depend on natural problem quantities, among which is the minimum singular value of $\mathbf{P}_{\star}$ (as defined in Eq. 2.4 ‣ 2 Preliminaries ‣ Globally Convergent Policy Search over Dynamic Filters for Output Estimation")), which we show is always strictly positive.

### Lemma 3.3

Let $\mathbf{P}_{\star}$ be the solution to the Riccati equation in Eq. 2.4 ‣ 2 Preliminaries ‣ Globally Convergent Policy Search over Dynamic Filters for Output Estimation"). Then under Assumptions 2.1 ‣ 2 Preliminaries ‣ Globally Convergent Policy Search over Dynamic Filters for Output Estimation"), 2.2 ‣ 2 Preliminaries ‣ Globally Convergent Policy Search over Dynamic Filters for Output Estimation") and 2.3 ‣ 2 Preliminaries ‣ Globally Convergent Policy Search over Dynamic Filters for Output Estimation"), $\sigma_{\star}:={\lambda_{\min}{(\mathbf{P}_{\star})}}$ is strictly positive. Moreover, $\mathbf{P}_{\star} = {\mathbf{\Sigma}_{11,{sys}} - \mathbf{Z}_{\star}}$.

In other words, $\mathbf{P}_{\star}$ is the limiting conditional covariance of the true state $\mathbf{x}{(t)}$ given the policy-state ${\hat{\mathbf{x}}}_{\mathsf{K}}{(t)}$ under (any) optimal policy. Lemma 3.3 states that this covariance is nonsingular, i.e. not even optimal policies contain perfect information about any mode of $\mathbf{x}{(t)}$. Given an initialization $\mathsf{K}_{0}$, our convergence rate depends polynomially on the following problem parameters:

### Theorem 3

Fix $\lambda > 0$, $\mathsf{K}_{0} \in \mathcal{K}_{\mathtt{i}\mathtt{n}\mathtt{f}\mathtt{o}}$. There are terms ${\mathcal{C}_{1},\mathcal{C}_{2}} \geq 1$, which are at most polynomial in $n,m,C_{\mathtt{s}\mathtt{y}\mathtt{s}},\lambda,\lambda^{- 1}$ and $\mathcal{L}_{\lambda}{(\mathsf{K}_{0})}$, such that the iterates of IR-PG with any stepsize $\eta \leq \frac{1}{\mathcal{C}_{1}}$ satisfy The formal guarantee for back-tracking stepsizes is nearly analogous, and given in Section B.1.

### Oracle complexity

At each iteration, one can compute the derivative of $\mathcal{L}_{\lambda}$ using one call to ${\mathsf{o}\mathsf{r}\mathsf{a}\mathsf{c}}_{eval}$ (which evaluates $\mathcal{L}_{\mathtt{O}\mathtt{E}}{(\mathsf{K}_{s})}$ and $\mathbf{\Sigma}_{\mathsf{K}}$), and one call to ${\mathsf{o}\mathsf{r}\mathsf{a}\mathsf{c}}_{grad}$, which computes the gradients of these quantities. This is true because ${\nabla{tr}}{\lbrack\mathbf{Z}_{\mathsf{K}}^{- 1}\rbrack}$ admits a closed form in terms of $\mathbf{\Sigma}_{\mathsf{K}}$ and its gradient. The balancing step also requires only evaluation $\mathbf{\Sigma}_{\mathsf{K}}$, and can use an evaluation query called for the gradient. Lastly, the backtracking step requires an evaluation query for all $|\mathcal{S}_{bkt}|$ filters of the form ${\overset{\sim}{\mathsf{K}}}_{s} - {\eta\nabla_{s}}$. In total, therefore, each iteration uses $1$ call to ${\mathsf{o}\mathsf{r}\mathsf{a}\mathsf{c}}_{grad}$, and ${|\mathcal{S}_{bkt}|} + 2$ calls to ${\mathsf{o}\mathsf{r}\mathsf{a}\mathsf{c}}_{eval}$. We sketch the highlights of the proof in the following section, after introducing our DCL framework. A rigorous proof overview, with statements of the constituent results, is deferred to Section 6.2.

### Numerical Experiments

In this subsection we present the results of a number of additional numerical experiments illustrating the performance of IR-PG.

### Random generation of true systems

Each experimental trial begins with the random generation of a *true system* of the form Eq. 1.1. System parameters $\mathbf{A},\mathbf{C}$ are randomly generated using Matlab's rss function, with state dimension $n = 2$ and output dimension $m = 1$. The matrix $\mathbf{G}$ defining the mapping from state to performance output $\mathbf{z}$ is set to $\mathbf{G} = I$. The intensity of the system disturbances is randomly generated as $\mathbf{W}_{1} = {\mathbf{M}^{\top}\mathbf{M}}$ with each entry of $\mathbf{M} \in {\mathbb{R}}^{n \times n}$ sampled from $\mathcal{N}{}$. The intensity of the measurement noise is normalized to $\mathbf{W}_{2} = 1$. To select suitable systems, we then reject samples according to the following criteria: (i) $\mathbf{A}$ must be strictly stable, and the observability Gramian $\mathcal{O}$ corresponding to $(\mathbf{A},\mathbf{C})$ must satisfy $10^{- 4} \leq {\lambda_{\min}{(\mathcal{O})}} \leq 10^{- 2}$; (ii) $\mathbf{W}_{1}$ must satisfy ${\lambda_{\max}{(\mathbf{W}_{1})}} \leq 5$; (iii) the optimal cost must satisfy ${\mathcal{L}_{\mathtt{O}\mathtt{E}}{(\mathsf{K}_{\star})}} \leq 10^{3}$. The first criterion regulates the observability of the true system, which sets the difficulty of the filtering problem; the second ensures that the ratio between the disturbances and measurement noise remains "reasonable"; and the third ensures that the problem instance is not "pathological", as determined by excessively high cost of the optimal filter.

### Remark 4.1 (Choice of $\mathbf{G} = \mathbf{I}$)

As detailed in Section 3.2, IR-PG makes use of the regularizer $\mathcal{R}_{\mathtt{i}\mathtt{n}\mathtt{f}\mathtt{o}}$, defined in Eq. 3.3, the computation of which requires access to the true system states $\mathbf{x}$, as described in Section 2. To facilitate a more fair comparison with direct minimization of $\mathcal{L}_{\mathtt{O}\mathtt{E}}$, we selected $\mathbf{G} = \mathbf{I}$ to effectively give the optimizer of $\mathcal{L}_{\mathtt{O}\mathtt{E}}$ access to the true system states $\mathbf{x}$ as well. As a result, all algorithms compared in this section have access to the same information concerning the true system.

### Random generation of initial filters

Next we randomly generate a filter $\mathsf{K}_{0}$ from which to initialize gradient descent. To do so, we take the optimal (Kalman) filter $\mathsf{K}_{\star}$, and randomly perturb each of the parameters; specifically, we set ${(\mathsf{K}_{0})}_{i} = {{(\mathsf{K}_{\star})}_{i} + \delta_{i}}$ with $\delta_{i} \sim {\mathcal{N}{}}$ for the $i$th parameter. Before accepting this $\mathsf{K}_{0}$, we rejection sample based on the following criteria: (i) $\mathbf{\Sigma}_{\mathsf{K}_{0}}$ must satisfy $10^{- 5} \leq {\sigma_{\min}{(\mathbf{\Sigma}_{12,\mathsf{K}_{0}})}} \leq 10^{- 3}$; (ii) $\mathbf{\Sigma}_{\mathsf{K}_{0}}$ must satisfy $10^{- 3} \leq {\sigma_{\min}{(\mathbf{\Sigma}_{22,\mathsf{K}_{0}})}} \leq 1$; (iii) the initial suboptimality must satisfy ${\mathcal{L}_{\mathtt{O}\mathtt{E}}{(\mathsf{K}_{0})}} \leq {{100 \times \mathcal{L}_{\mathtt{O}\mathtt{E}}}{(\mathsf{K}_{\star})}}$. The first criterion ensures that we do not begin from an initial guess for which the informativity is too low, nor a guess for which it is too high (which makes the search easier). The second criterion ensures that the initial filter is sufficiently controllable, to avoid initializations that are too close to suboptimal stationary points. The final criterion ensures that the initial guess is, in all other ways, "reasonable", as measured by suboptimality.

### Optimization methods compared

Given a randomly generated true system, and random initial filter $\mathsf{K}_{0}$, we then apply the following three optimization algorithms: (i) gradient descent on $\mathcal{L}_{\mathtt{O}\mathtt{E}}{(\mathsf{K})}$; (ii) gradient descent on $\mathcal{L}_{\mathtt{O}\mathtt{E}}{(\mathsf{K})}$ with filter state normalization performed before each gradient step, cf. Eq. 3.4; (iii) IR-PG, as detailed in Algorithm 1, with regularization parameter $\lambda = 10^{- 4}$. See below for further discussion on the selection of $\lambda$. All methods are initialized from the same $\mathsf{K}_{0}$, and make use of the same backtracking line search to select step sizes. Moreover, all algorithms have the same termination criteria. Each algorithm terminates when either: (i) the Frobenius norm of the gradient of the cost function being minimized (either $\mathcal{L}_{\mathtt{O}\mathtt{E}}$ or $\mathcal{L}_{\lambda}$) falls below a tolerance of $10^{- 8}$; (ii) the step size selected by the line search falls below a tolerance of $10^{- 16}$ for more than three consecutive iterations; or (iii) the number of iterations (gradient descent steps) exceeds $100,000$.

### Results

The results of 60 such experimental trials are depicted in Fig. 1. It is evident that simple "unregularized" gradient descent on $\mathcal{L}_{\mathtt{O}\mathtt{E}}$ routinely fails to converge to the global optimum, in the allotted number of iterations. In fact, the median (normalized) suboptimality gap $\frac{{\mathcal{L}_{\mathtt{O}\mathtt{E}}{(\mathsf{K})}} - {\mathcal{L}_{\mathtt{O}\mathtt{E}}{(\mathsf{K}_{\star})}}}{\mathcal{L}_{\mathtt{O}\mathtt{E}}{(\mathsf{K}_{\star})}}$ exceeds $10^{- 4}$, and only a single trial achieves suboptimality less than $10^{- 7}$. Loss of informativity in these trials can be seen clearly in Fig. 2. The addition of the filter state reconditioning procedure of Eq. 3.4 offers only minimal improvement. In contrast, IR-PG converges reliably to high-quality solutions that are extremely close to the global optimum; the median normalized suboptimality gap was zero, to numerical precision. In fact, for one third of trials, the suboptimality gap was actually *negative* (by very small margins, e.g. $10^{- 17}$) indicating that IR-PG has reached the limits of numerical precision with which Matlab's icare solves Riccati equations (used to compute $\mathsf{K}_{\star}$).

(a) Normalized suboptimality at the termination of each algorithm.

(b) Normalized suboptimality as a function of iteration for each algorithm.

Figure 1: Performance of each algorithm as measured by the normalized suboptimality of the output estimation cost, $\frac{{\mathcal{L}_{\mathtt{O}\mathtt{E}}{(\mathsf{K})}} - {\mathcal{L}_{\mathtt{O}\mathtt{E}}{(\mathsf{K}_{\star})}}}{\mathcal{L}_{\mathtt{O}\mathtt{E}}{(\mathsf{K}_{\star})}}$. 60 trials of the experimental procedure described in Section 4 are plotted. In (b), the lightly shaded region covers the 10th to 90th percentiles, and the darker region covers the 25th to 75th percentiles.

### Selection of regularization parameter $\lambda$

Performance of IR-PG is in many instances insensitive to the value of $\lambda$ selected. However, we observed that a handful of experimental trails required $\lambda$ to be chosen more judiciously, in particular, when the spectral properties of $\nabla^{2}\mathcal{R}_{\mathtt{i}\mathtt{n}\mathtt{f}\mathtt{o}}$ differ significantly from those of $\nabla^{2}\mathcal{L}_{\mathtt{O}\mathtt{E}}$. Very small stepsizes may be required when $\lambda_{\max}{({\nabla^{2}\mathcal{R}_{\mathtt{i}\mathtt{n}\mathtt{f}\mathtt{o}}})}$ is very large, which means the search may make slow progress in updating $\mathbf{C}_{\mathsf{K}}$, as $\mathcal{R}_{\mathtt{i}\mathtt{n}\mathtt{f}\mathtt{o}}$ is independent of $\mathbf{C}_{\mathsf{K}}$. We have observed good performance in practice by simply "turning off" the regularizer (i.e. setting $\lambda = 0$) when the stepsize becomes excessively small (e.g. drops below $10^{- 16}$).

(a) Informativity, as measured by σmin (Σ12).

(b) Conditioning, as measured by σmin (Σ22).

Figure 2: Properties of Σ for the same 60 trials plotted in Fig. 1. The lightly shaded region covers the 10th to 90th percentiles, and the darker region covers the 25th to 75th percentiles.

### Analysis Framework

This section introduces *differentiable convex liftings* (DCLs), a rigorous and flexible framework for operationalizing convex reformulations of nonconvex objectives.

### Preliminaries

To neatly accommodate optimization over constrained domains, we express functions $f:{{\mathbb{R}}^{d}\rightarrow\overline{\mathbb{R}}}$ as taking values in the extended reals $\overline{\mathbb{R}}:={{\mathbb{R}} \cup {\{\infty\}}}$.^88^8Because we solely consider minimizations, $\overline{\mathbb{R}}$ does not include $- \infty$ Given such an $f$, we denote its domain ${{\mathsf{d}\mathsf{o}\mathsf{m}}{(f)}}:{\{ x:{{f{({\mathbf{z}})}} \neq \infty}\}}$ as the set on which $f$ is finite; we say $f$ is *proper* if ${{\mathsf{d}\mathsf{o}\mathsf{m}}{(f)}} \neq \varnothing$; we define its minimal value ${\inf{(f)}} = {\inf_{{\mathbf{x}} \in {\mathbb{R}}^{d}}{f{({\mathbf{x}})}}}$. All functions are assumed to take extended real values, and are infinite outside their domain when not otherwise defined (for example, in the case of an ill-posed inverse).e say $f \in {\mathcal{C}^{k}{(\mathcal{K})}}$ on a if $f$ is $k$-times continuously differentiable (and finite) on some open set containing $\mathcal{K} \subset {\mathbb{R}}^{d}$.

DCLs. The DCL is a generic template for convex reformulation that significantly generalizes the setup in 1.1. Rather than relating $f$ directly to a convex $f_{\mathtt{c}\mathtt{v}\mathtt{x}}$, we "lift" $f$ to a function $f_{\mathtt{l}\mathtt{f}\mathtt{t}}$ by appending auxiliary variables. We then assume a reparametrization $\Phi$ mapping the domain of $f_{\mathtt{l}\mathtt{f}\mathtt{t}}$ to that of $f_{\mathtt{c}\mathtt{v}\mathtt{x}}$ in this higher dimensional space; intuitively, $\Phi$ is the "inverse" of $\Psi$ in 1.1.

### Definition 5.1

A triplet of functions $(f_{\mathtt{c}\mathtt{v}\mathtt{x}},f_{\mathtt{l}\mathtt{f}\mathtt{t}},\Phi)$ is a DCL of a proper function $f:{{\mathbb{R}}^{d}\rightarrow\overline{\mathbb{R}}}$ if $f_{\mathtt{c}\mathtt{v}\mathtt{x}}:{{\mathbb{R}}^{d_{z}}\rightarrow\overline{\mathbb{R}}}$ is an (extended-real valued) convex function whose minimum is attained by some ${\mathbf{z}}^{\star}$, ${f_{\mathtt{c}\mathtt{v}\mathtt{x}}{({\mathbf{z}}^{\star})}} = {\inf{(f_{\mathtt{c}\mathtt{v}\mathtt{x}})}} > {- \infty}$.

For some additional number of parameters $d_{\xi} \geq 0$, $f_{\mathtt{l}\mathtt{f}\mathtt{t}}:{{\mathbb{R}}^{d + d_{\xi}}\rightarrow\overline{\mathbb{R}}}$ is related to $f$ via partial minimization: ${f{({\mathbf{x}})}} = {{\min_{{\mathbf{ξ}} \in {\mathbb{R}}^{d_{\xi}}}f_{\mathtt{l}\mathtt{f}\mathtt{t}}}{({\mathbf{x}},{\mathbf{ξ}})}}$.

For an open set $\mathcal{Y}$ containing ${\mathsf{d}\mathsf{o}\mathsf{m}}{(f_{\mathtt{l}\mathtt{f}\mathtt{t}})}$, $\Phi:{\mathcal{Y}\rightarrow{{\mathsf{d}\mathsf{o}\mathsf{m}}{(f_{\mathtt{c}\mathtt{v}\mathtt{x}})}}}$, is $\mathcal{C}^{1}{(\mathcal{Y})}$, and relates $f_{\mathtt{l}\mathtt{f}\mathtt{t}}$ to $f_{\mathtt{c}\mathtt{v}\mathtt{x}}$ via ${f_{\mathtt{l}\mathtt{f}\mathtt{t}}{( \cdot )}} = {f_{\mathtt{c}\mathtt{v}\mathtt{x}}{({\Phi{( \cdot )}})}}$.

The mere existence of a DCL implies that approximate stationary points of $f$ are also approximate minimizers, under conditions elaborated on below:

### Theorem 4

Let $f:{{\mathbb{R}}^{d}\rightarrow\overline{\mathbb{R}}}$ be a proper function with DCL $(f_{\mathtt{c}\mathtt{v}\mathtt{x}},f_{\mathtt{l}\mathtt{f}\mathtt{t}},\Phi)$. Then, for any $\mathbf{x} \in {{\mathsf{d}\mathsf{o}\mathsf{m}}{(f)}}$ at which $f$ is differentiable, $f$ satisfies the weak-PL condition: Theorem 4 strengthens 1.1 in two respects. For one, it does not impose any smoothness restrictions on $f_{\mathtt{l}\mathtt{f}\mathtt{t}}$ or $f_{\mathtt{c}\mathtt{v}\mathtt{x}}$; in particular $f_{\mathtt{c}\mathtt{v}\mathtt{x}}$ can be highly non-smooth and, due to the extended-real function formulation, can also include constraints. And second, the lifting $f_{\mathtt{l}\mathtt{f}\mathtt{t}}$ adds considerable flexibility, which we show is necessary to capture the convex reformulation of OE (Section 6.4 ‣ 6 Proof of Theorems 3 and 2 ‣ Globally Convergent Policy Search over Dynamic Filters for Output Estimation")).

The factor $\alpha_{\text{dcl}}{({\mathbf{x}})}$ depends on two quantities. The numerator is the $d_{z}$-th singular value of ${\nabla\Phi}{({\mathbf{x}},{\mathbf{ξ}})}$ for any ${\mathbf{ξ}} \in {{{\arg\min}f_{\mathtt{l}\mathtt{f}\mathtt{t}}}{({\mathbf{x}}, \cdot )}}$. This captures how large perturbations of $f_{\mathtt{l}\mathtt{f}\mathtt{t}}$'s arguments must be in order to achieve a desired perturbation of the arguments of $f_{\mathtt{c}\mathtt{v}\mathtt{x}}$, under the reparameterization $\Phi$. The additional arguments in $f_{\mathtt{l}\mathtt{f}\mathtt{t}}$ compared to $f$ adds additional columns to $\nabla\Phi$ thereby making it easier to ensure ${\sigma_{d_{z}}{({{\nabla\Phi}{( \cdot )}})}} > 0$. On the other hand, the denominator measures the Euclidean distance between any minimizer of the convex function $f_{\mathtt{c}\mathtt{v}\mathtt{x}}{( \cdot )}$ and image of $({\mathbf{x}},{\mathbf{ξ}})$ under the reparameterization $\Phi$, and can be bounded under quite benign conditions.

### Proof Sketch of Theorem 4

The formal proof of Theorem 4 (given in Section H.2) takes special care to handle that allow $f_{\mathtt{l}\mathtt{f}\mathtt{t}}$ and $f_{\mathtt{c}\mathtt{v}\mathtt{x}}$ to be finite only on restricted domains, and possible non-smoothness; still, the main ideas behind are intuitive.

For $f_{\mathtt{c}\mathtt{v}\mathtt{x}}$ convex, ${{f_{\mathtt{c}\mathtt{v}\mathtt{x}}{({\mathbf{z}})}} - {\inf{(f_{\mathtt{c}\mathtt{v}\mathtt{x}})}}} = {\mathcal{O}{({\|{{\nabla f_{\mathtt{c}\mathtt{v}\mathtt{x}}}{({\mathbf{z}})}}\|})}}$. Using the DCL definition and analyzing the inverse image of a point under $\Phi$, we can also establish a gradient domination result for $f_{\mathtt{l}\mathtt{f}\mathtt{t}}$. Weak-PL result for the original function $f$ follows since $f$ is related to $f_{\mathtt{l}\mathtt{f}\mathtt{t}}$ by partial minimization, so its gradients must be larger than those of $f_{\mathtt{l}\mathtt{f}\mathtt{t}}$. ∎

### Gradient descent with DCLs

We now describe how DCLs yield quantitative convergence guarantees for gradient descent. A more general guarantee accommodating the reconditioning step in IR-PG is deferred to Section 5.2, and encompasses the bound below as a special case. Given $\alpha > 0$, we say that proper $f:{{\mathbb{R}}^{d}\rightarrow\overline{\mathbb{R}}}$ satisfies $\alpha$-*weak-PL* (named after the stronger Polyak-Łojasiewicz condition) on a domain $\mathcal{K} \subset {\mathbb{R}}^{d}$ if $f \in {\mathcal{C}^{1}{(\mathcal{K})}}$ and From Theorem 4, we see $f$ satisfies $\alpha_{\mathcal{K}}$-weak PL on $\mathcal{K}$ if $f$ has a DCL and $\alpha_{\mathcal{K}}:={\inf_{{\mathbf{x}} \in \mathcal{K}}{\alpha_{\text{dcl}}{({\mathbf{x}})}}} > 0$. To analyze gradient descent, we also require smoothness: we say $f$ is *$\beta$-upper-smooth* on $\mathcal{K}$ if $f \in {\mathcal{C}^{2}{(\mathcal{K})}}$ and for all ${\mathbf{x}} \in \mathcal{K}$, The following follows from a standard descent lemma for smooth (though possibly nonconvex) functions.

### Proposition 5.1

Let $\mathbf{x}_{0} \in {{\mathsf{d}\mathsf{o}\mathsf{m}}{(f)}}$, and suppose that the level set ${\mathcal{K}{(\mathbf{x}_{0})}}:={\{\mathbf{x}:{{f{(\mathbf{x})}} \leq {f{(\mathbf{x}_{0})}}}\}}$ is compact, and $f$ satisfies $\alpha_{\mathbf{x}_{0}} > 0$-weak PL and $\beta_{\mathbf{x}_{0}} > 0$-upper smoothness on $\mathcal{K}{(\mathbf{x})}$. Then, $\mathbf{x}_{0}$ lies in the same path-connected component of some minimizer of $f$, and for any $\eta \leq {1/\beta_{\mathbf{x}_{0}}}$ the updates $\mathbf{x}_{k + 1} = {\mathbf{x}_{k} - {\eta{\nabla f}{(\mathbf{x}_{k})}}}$ satisfy ${{f{(\mathbf{x}_{k})}} - {\inf{(f)}}} \leq {2/{({{k \cdot \alpha_{\mathbf{x}_{0}}^{2}}\eta})}}$.

### Gradient descent with reconditioning

We now extend Proposition 5.1 to accommodate the reconditioning step in IR-PG (Algorithm 1). Here, we state guarantees which establish both quantitative convergence rates and, under slightly stronger conditions, path-connectedness to global minimizers. All proofs are deferred to Section H.3.

### Definition 5.2 (Reconditioning matrix)

Given $f:{{\mathbb{R}}^{d}\rightarrow\overline{\mathbb{R}}}$, we say that $\mathbf{\Lambda}:{{{\mathsf{d}\mathsf{o}\mathsf{m}}{(f)}}\rightarrow{\mathbb{S}}_{+}^{n}}$ is a reconditioning matrix for $f$ if it is continuous on ${\mathsf{d}\mathsf{o}\mathsf{m}}{(f)}$, and for every ${\mathbf{x}} \in {{\mathsf{d}\mathsf{o}\mathsf{m}}{(f)}}$ such that ${\mathbf{\Lambda}{({\mathbf{x}})}} \succ 0$, there exists an ${\mathbf{x}}' \in {{\mathsf{d}\mathsf{o}\mathsf{m}}{(f)}}$ such that ${\mathbf{\Lambda}{({\mathbf{x}}')}} = \mathbf{I}_{n}$ and ${f{({\mathbf{x}}')}} = {f{({\mathbf{x}})}}$. We define the set ${{\mathsf{r}\mathsf{e}\mathsf{c}\mathsf{o}\mathsf{n}\mathsf{d}}_{\mathbf{\Lambda}}{({\mathbf{x}})}}:={\{{\mathbf{x}}':{{{f{({\mathbf{x}}')}} = {f{({\mathbf{x}})}}},{{\mathbf{\Lambda}{({\mathbf{x}})}} = \mathbf{I}_{n}}}\}}$ as the set of such points. We say $\mathbf{x}$ is reconditioned if ${\mathbf{\Lambda}{({\mathbf{x}})}} = \mathbf{I}_{n}$.

### Observation 5.2

${\mathbf{\Lambda}{(\mathsf{K})}} = \mathbf{\Sigma}_{\mathsf{K},22}$ is a reconditioning matrix for the loss $\mathcal{L}_{\lambda{( \cdot )}}$.

### Proof

Since ${{\mathsf{d}\mathsf{o}\mathsf{m}}{(\mathcal{L}_{\lambda})}} = \mathcal{K}_{\mathtt{i}\mathtt{n}\mathtt{f}\mathtt{o}} \subset \mathcal{K}_{\mathtt{c}\mathtt{t}\mathtt{r}\mathtt{b}}$, $\mathbf{\Sigma}_{22,\mathsf{K}} \succ 0$ on ${\mathsf{d}\mathsf{o}\mathsf{m}}{(\mathcal{L}_{\lambda})}$. As observed in Eq. 3.4, there is a similarity transformation mapping $\mathsf{K} \in \mathcal{K}_{\mathtt{i}\mathtt{n}\mathtt{f}\mathtt{o}}$ some $\mathsf{K}'$ with $\mathbf{\Sigma}_{\mathsf{K}',22} = \mathbf{I}_{n}$. Since $\mathcal{L}_{\lambda}$ is invariant under similarity transformation, it follows ${\mathcal{L}_{\lambda}{(\mathsf{K}')}} = {\mathcal{L}_{\lambda}{(\mathsf{K})}}$. ∎ Reconditioning serves to ensure that $f$ need only be well-behaved (i.e. satisfy upper-smoothness and weak-PL for suitable constants) on a restricted set of approximately reconditioned parameters ${\mathbf{x}}:{{\mathbf{\Lambda}{({\mathbf{x}})}} \approx \mathbf{I}_{n}}$.

The following proposition is the guiding template for the overall convergence analysis. Its proof is given in Section H.3.1.

### Proposition 5.3

Let $f:{{\mathbb{R}}^{d}\rightarrow\overline{\mathbb{R}}}$, $\mathbf{x}_{0} \in {{\mathsf{d}\mathsf{o}\mathsf{m}}{(f)}}$, and let $\mathbf{\Lambda}$ be a reconditioning matrix for $f$ such that ${\mathbf{\Lambda}{(\mathbf{x}_{0})}} \succ 0$. Define $\mathcal{K}{(\mathbf{x}_{0})}$ as the following reconditioned level set, which we assume is closed: Assume that the function $\mathbf{x}\mapsto{\mathbf{\Lambda}{(\mathbf{x})}}$ is $L_{{cond},\mathbf{x}_{0}}$-Lipschitz as a mapping from ${({\mathbb{R}}^{d}, \parallel \cdot \parallel)}\rightarrow{({\mathbb{S}}_{+}^{n}, \parallel \cdot \parallel_{op})}$ and that $f$ is $\beta_{\mathbf{x}_{0}}$-upper-smooth, $L_{f,\mathbf{x}_{0}}$-Lipschitz, and satisfies the $\alpha_{\mathbf{x}_{0}}$-weak PL condition for points in $\mathcal{K}{(\mathbf{x}_{0})}$. Lastly, let ${\{\eta_{k}\}}_{k = 0}^{\infty}$ be a series of step sizes such that $0 < {\inf_{k}\eta_{k}} \leq {\sup_{k}\eta_{k}} \leq {\min{\{\frac{1}{\beta_{\mathbf{x}_{0}}},\frac{1}{2L_{f,\mathbf{x}_{0}}L_{{cond},\mathbf{x}_{0}}}\}}}$. If iterates are chosen according to, or the more general condition, then for all $k \geq 1$ it holds that Proposition 5.3 can also be used to establish that every ${\mathbf{x}}_{0} \in {{\mathsf{d}\mathsf{o}\mathsf{m}}{(f)}}$ is in the path-connected component of some ${\mathbf{x}}^{\star} \in {{\arg\min}{(f)}}$. To do so, we need the matrix operator to be connected in the following sense:

### Definition 5.3

We say that a reconditioning matrix $\mathbf{\Lambda}:{{{\mathsf{d}\mathsf{o}\mathsf{m}}{(f)}}\rightarrow{\mathbb{S}}_{+}^{n}}$ is *connected* if there exists a parametrized operator ${{\overline{\mathsf{r}\mathsf{e}\mathsf{c}\mathsf{o}\mathsf{n}\mathsf{d}}}_{\mathbf{\Lambda}}{( \cdot, \cdot )}}:{{{{\mathsf{d}\mathsf{o}\mathsf{m}}{(f)}} \times {\lbrack 0,1\rbrack}}\rightarrow{\mathbb{S}}_{+}^{n}}$ such that (a) ${{\overline{\mathsf{r}\mathsf{e}\mathsf{c}\mathsf{o}\mathsf{n}\mathsf{d}}}_{\mathbf{\Lambda}}{( \cdot, \cdot )}{({\mathbf{x}},0)}} = {\mathbf{x}}$ (b) ${\overline{\mathsf{r}\mathsf{e}\mathsf{c}\mathsf{o}\mathsf{n}\mathsf{d}}{({\mathbf{x}},1)}} = {{\mathsf{r}\mathsf{e}\mathsf{c}\mathsf{o}\mathsf{n}\mathsf{d}}{({\mathbf{x}})}}$, and (c) for all ${\mathbf{x}} \in {{\mathsf{d}\mathsf{o}\mathsf{m}}{(f)}}$, $t\mapsto{\overline{\mathsf{r}\mathsf{e}\mathsf{c}\mathsf{o}\mathsf{n}\mathsf{d}}{({\mathbf{x}},t)}}$ is connected, and its image lies in ${\mathsf{d}\mathsf{o}\mathsf{m}}{(f)}$.

### Observation 5.4

The reconditioning matrix ${\mathbf{\Lambda}{(\mathsf{K})}} = \mathbf{\Sigma}_{\mathsf{K},22}$ for the loss $\mathcal{L}_{\lambda{( \cdot )}}$ is connected.

### Proof

Define ${\overline{\mathsf{r}\mathsf{e}\mathsf{c}\mathsf{o}\mathsf{n}\mathsf{d}}{(\mathsf{K},t)}}:={{\mathsf{S}\mathsf{i}\mathsf{m}}_{\mathbf{S}_{t}}{(\mathbf{A}_{\mathsf{K}},\mathbf{B}_{\mathsf{K}},\mathbf{C}_{\mathsf{K}})}}$, where $\mathbf{S}_{t} = \mathbf{\Sigma}_{22,\mathsf{K}}^{- {t/2}}$. Since similarity transforms preserve membership in $\mathcal{K}_{\mathtt{i}\mathtt{n}\mathtt{f}\mathtt{o}}$, and since $t\mapsto{\overline{\mathsf{r}\mathsf{e}\mathsf{c}\mathsf{o}\mathsf{n}\mathsf{d}}{(\mathsf{K},t)}}$ is continuous and coincides with $\mathsf{K}$ at $t = 0$ (resp. ${\mathsf{r}\mathsf{e}\mathsf{c}\mathsf{o}\mathsf{n}\mathsf{d}}{(\mathsf{K})}$ at $t = 1$), the observation follows. ∎ The following proposition, proved in Section H.3.2, establishes path-connectedness for connected reconditioning matrices.

### Proposition 5.5

Consider the set up of Proposition 5.3 with $\mathbf{x}_{0} \in {{\mathsf{d}\mathsf{o}\mathsf{m}}{(f)}}$, and in addition, suppose (a) that $\mathbf{\Lambda}{( \cdot )}$ is continuous reconditioning matrix and (b) the set $\mathcal{K}{(\mathbf{x}_{0})}$ is compact. Then, there exists an $\mathbf{x}^{\star} \in {{\arg\min}{(f)}}$ and a path $\gamma:{{\lbrack 0,1\rbrack}\rightarrow{{\mathsf{d}\mathsf{o}\mathsf{m}}{(f)}}}$ such that ${\gamma{}} = \mathbf{x}_{0}$ and ${\gamma{}} = \mathbf{x}^{\star}$.

Proposition 5.1 can be recovered as the special case when the reconditioning matrix ${{\mathsf{r}\mathsf{e}\mathsf{c}\mathsf{o}\mathsf{n}\mathsf{d}}_{\mathbf{\Lambda}}{({\mathbf{x}})}} \equiv \mathbf{I}_{d}$ is always the identity. In this case, the reconditioning step is vacuous. Moreover $L_{{cond},{\mathbf{x}}_{0}} = 0$ (${\mathsf{r}\mathsf{e}\mathsf{c}\mathsf{o}\mathsf{n}\mathsf{d}}_{\mathbf{\Lambda}}$ is constant), and it is straightforward to modify the proof of Proposition 5.3 to dispense with the dependence on $L_{f,{\mathbf{x}}_{0}}$.

### Proof of Theorems 3 and 2

Before providing the exact details, we begin with a high-level overview of Theorem 3 in Section 6.1 to emphasize the key ideas. The formal proof skeleton is given in the following section, Section 6.2, and Section 6.3 proves Theorem 2. Lastly, Section 6.4 ‣ 6 Proof of Theorems 3 and 2 ‣ Globally Convergent Policy Search over Dynamic Filters for Output Estimation") specifies the construction of the DCL for OE. The proof of all the constituent results are deferred to the appendix.

### Proof sketch of Theorem 3

In light of Proposition 5.3, it suffices to establish both the weak-PL and smoothness of the loss $\mathcal{L}_{\lambda}{( \cdot )}$ on the well-conditioned sublevel set $\mathcal{K}_{0}:={\{\mathsf{K}:{{{\mathcal{L}_{\lambda}{(\mathsf{K})}} \leq {\mathcal{L}_{\lambda}{(\mathsf{K}_{0})}}},{{\frac{1}{2}\mathbf{I}_{n}} \preceq \mathbf{\Sigma}_{22,\mathsf{K}} \preceq {2\mathbf{I}_{n}}}}\}}$ (as well as some Lipschitz bounds on $\mathcal{L}_{\lambda}$ and $\mathsf{K}\mapsto\mathbf{\Sigma}_{22,\mathsf{K}}$).

To establish weak-PL, we exhibit a DCL for which $\alpha_{\text{DCL}}{(\mathsf{K})}$ depends only on the operator norms of $\mathbf{\Sigma}_{\mathsf{K}},\mathbf{\Sigma}_{\mathsf{K}}^{- 1},\mathbf{Z}_{\mathsf{K}}$, as well as other system-quantities (Propositions 6.1 and 6.1. ‣ A DCL for the regularized OE objective. ‣ 6.2 Proof of Theorem 3 ‣ 6 Proof of Theorems 3 and 2 ‣ Globally Convergent Policy Search over Dynamic Filters for Output Estimation")); smoothness and Lipschitz bounds ared established in (Proposition 6.3. ‣ Smoothness and Lipschitzness of ℒ_𝜆⁢(𝖪). ‣ 6.2 Proof of Theorem 3 ‣ 6 Proof of Theorems 3 and 2 ‣ Globally Convergent Policy Search over Dynamic Filters for Output Estimation")), which relies on a novel bound on the solutions to Lyapunov equations involving $\mathbf{A}_{{cl},\mathsf{K}}$ (Proposition 6.2. ‣ Smoothness and Lipschitzness of ℒ_𝜆⁢(𝖪). ‣ 6.2 Proof of Theorem 3 ‣ 6 Proof of Theorems 3 and 2 ‣ Globally Convergent Policy Search over Dynamic Filters for Output Estimation")), also in terms of ${\|\mathbf{\Sigma}_{\mathsf{K}}\|},{\|\mathbf{\Sigma}_{\mathsf{K}}^{- 1}\|},{\|\mathbf{Z}_{\mathsf{K}}^{- 1}\|}$.

The regularization $\mathcal{R}_{\mathtt{i}\mathtt{n}\mathtt{f}\mathtt{o}}{(\mathsf{K})}$ ensures $\|\mathbf{Z}_{\mathsf{K}}^{- 1}\|$ remains bounded on the sublevel $\mathcal{K}_{0}$; we further show (Lemma 6.5) that ${\frac{1}{2}\mathbf{I}_{n}} \preceq \mathbf{\Sigma}_{22,\mathsf{K}} \preceq {\frac{3}{2}\mathbf{I}_{n}}$ implies $\mathbf{\Sigma}_{\mathsf{K}}$ is invertible, and ensures ${\|\mathbf{\Sigma}_{\mathsf{K}}\|},{\|\mathbf{\Sigma}_{\mathsf{K}}^{- 1}\|}$ are uniformly bounded. Thus, the weak-PL constant and smoothness parameters are uniformly bounded on $\mathcal{K}_{0}$, concluding the proof. We stress that the proofs of Proposition 6.1 and Proposition 6.2. ‣ Smoothness and Lipschitzness of ℒ_𝜆⁢(𝖪). ‣ 6.2 Proof of Theorem 3 ‣ 6 Proof of Theorems 3 and 2 ‣ Globally Convergent Policy Search over Dynamic Filters for Output Estimation") require several novel technical arguments, which may be of independent interest.

The fact that ${\|\mathbf{\Sigma}_{\mathsf{K}}\|},{\|\mathbf{\Sigma}_{\mathsf{K}}^{- 1}\|},{\|\mathbf{Z}_{\mathsf{K}}^{- 1}\|}$ appear throughout the analysis suggests that (a) informativity as measured by $\mathbf{Z}_{\mathsf{K}}^{- 1}$, and (b) the conditioning of $\mathbf{\Sigma}_{22,\mathsf{K}}$ may be fundamental to the OE landscape.

### Proof of Theorem 3

With key ingredients of the analysis in mind, we now finish the proof of Theorem 3 by illustrating the existence of a DCL for the regularized OE problem, and establishing smoothness and Lipschitzness of the objective when restricted to the reconditioned set so as to apply Proposition 5.3. More specifically, we first establish the relevant properties "locally", in that they depend on the choice of the filter $\mathsf{K}$, and then prove a uniform bound over all $\mathsf{K}$ in the reconditioned set at the very end. A recurring theme is that both the weak-PL and the smoothness properties are controlled by the informativity, as measured by $\|\mathbf{Z}_{\mathsf{K}}^{- 1}\|$. These are terms are also controlled by ${\|\mathbf{\Sigma}_{\mathsf{K}}\|},{\|\mathbf{\Sigma}_{\mathsf{K}}^{- 1}\|}$, which we show below are bounded in terms of ${\|\mathbf{\Sigma}_{22,\mathsf{K}}\|},{\|\mathbf{\Sigma}_{22,\mathsf{K}}^{- 1}\|}$, which are both bounded due to the reconditioning step.

As shorthand, we let ${poly}_{op}{(\mathbf{X}_{1},\mathbf{X}_{2},\ldots,\kappa)}$ denote a term which is at most a polynomial function of the operator norm of the matrix arguments ${\|\mathbf{X}_{1}\|},{{\|\mathbf{X}_{2}\|}_{,}\ldots}$, and a polynomial in the scalar argument $\kappa$; $\parallel \cdot \parallel_{\ell_{2}}$ denotes the Euclidean norm (e.g. on parameters $\mathsf{K} = {(\mathbf{A}_{\mathsf{K}},\mathbf{B}_{\mathsf{K}},\mathbf{C}_{\mathsf{K}})}$). All results below assume $\mathsf{K} \in \mathcal{K}_{\mathtt{i}\mathtt{n}\mathtt{f}\mathtt{o}}$, and that $\mathbf{\Sigma}_{\mathsf{K}}$ is invertible (we verify this condition in Lemma 6.5 below.)

### DCL for the regularized OE objective

While it is by now well-known within the controls community that the OE problem admits a convex reformulation, we prove a stronger result showing that this reformulation is in fact a DCL. We prove the following result in Section 6.4 ‣ 6 Proof of Theorems 3 and 2 ‣ Globally Convergent Policy Search over Dynamic Filters for Output Estimation").

### Proposition 6.1

For any $\lambda \geq 0$ (non-strict), the objective $\mathcal{L}_{\lambda}{(\mathsf{K})}$ admits a DCL $(f_{\mathtt{c}\mathtt{v}\mathtt{x}},f_{\mathtt{l}\mathtt{f}\mathtt{t}},\Phi)$ where the lifted parameter takes the form ${(\mathsf{K},\mathbf{\Sigma}_{\mathsf{K}})} \in {\mathcal{K}_{\mathtt{i}\mathtt{n}\mathtt{f}\mathtt{o}} \times {\mathbb{S}}_{+ +}^{2n}}$, ${\mathcal{L}_{\lambda}{(\mathsf{K})}} = {f_{\mathtt{l}\mathtt{f}\mathtt{t}}{(\mathsf{K},\mathbf{\Sigma}_{\mathsf{K}})}} = {{\min_{\mathbf{\Sigma} \in {\mathbb{S}}_{+}^{2n}}f_{\mathtt{l}\mathtt{f}\mathtt{t}}}{(\mathsf{K},\mathbf{\Sigma})}}$, and where Furthermore, the norms of the parameters $\mathbf{A}_{\mathsf{K}},\mathbf{B}_{\mathsf{K}},\mathbf{C}_{\mathsf{K}}$ satisfy the following bounds: Recall that the domain of $\mathcal{L}_{\lambda}{(\mathsf{K})}$ is the set $\mathcal{K}_{\mathtt{i}\mathtt{n}\mathtt{f}\mathtt{o}}$, on which $\mathbf{Z}_{\mathsf{K}}$ and (as noted above) $\mathbf{\Sigma}_{\mathsf{K}}$ are invertible. Hence, all quantities in the above lemma are well-defined. Having established the existence of a DCL, a direct application of Theorem 4 shows that this objective satisfies the weak-PL property.

### Corollary 6.1 (Weak-PL Property of $\mathcal{L}_{\lambda}$)

For any $\lambda \geq 0$ and $\mathsf{K} \in \mathcal{K}_{\mathtt{i}\mathtt{n}\mathtt{f}\mathtt{o}}$, | | | ${\|{{\nabla\mathcal{L}_{\lambda}}{(\mathsf{K})}}\|} \geq {{\frac{1}{{C_{\mathtt{P}\mathtt{L}}{(\mathsf{K})}} \cdot {\max{\{ n,\sqrt{mn}\}}}} \cdot \left({{\mathcal{L}_{\lambda}{(\mathsf{K})}} - {\inf{(\mathcal{L}_{\lambda})}}} \right)},\text{where}}$ | | (6.2) | | | | ${{C_{\mathtt{P}\mathtt{L}}{(\mathsf{K})}} = {{poly}_{op}\left(\mathbf{A},\mathbf{C},\mathbf{W}_{2}^{- 1},\mathbf{Z}_{\mathsf{K}}^{- 1},\mathbf{\Sigma}_{\mathsf{K}},\mathbf{\Sigma}_{\mathsf{K}}^{- 1},{\mathcal{L}_{\mathtt{O}\mathtt{E}}{(\mathsf{K})}} \right)}}.$ | | |

### Smoothness and Lipschitzness of $\mathcal{L}_{\lambda}{(\mathsf{K})}$

To verify these regularity conditions, we need to bound the norms of various quantities, which are themselves the solutions to Lyapunov equations involving the closed-loop system matrix $\mathbf{A}_{{cl},\mathsf{K}}$ (defined in Eq. 2.1 ‣ 2 Preliminaries ‣ Globally Convergent Policy Search over Dynamic Filters for Output Estimation")). The main step is therefore to show that the solutions to these Lyapunov equations are uniformly bounded, as per the following lemma (proof in Appendix J ‣ Part II Proofs for Convergence Guarantee ‣ Globally Convergent Policy Search over Dynamic Filters for Output Estimation")).

### Proposition 6.2 (Stability of $\mathbf{A}_{{cl},\mathsf{K}}$)

Suppose that $\mathsf{K} \in \mathcal{K}_{\mathtt{i}\mathtt{n}\mathtt{f}\mathtt{o}}$. Then, for any matrix $\mathbf{Y} \in {\mathbb{S}}^{2n}$, the solution $\mathbf{\Sigma}_{\mathsf{K},\mathbf{Y}}$ to the Lyapunov equation ${{\mathbf{A}_{{cl},\mathsf{K}}\mathbf{\Sigma}_{\mathsf{K},\mathbf{Y}}} + {\mathbf{\Sigma}_{\mathsf{K},\mathbf{Y}}\mathbf{A}_{{cl},\mathsf{K}}^{\top}} + \mathbf{Y}} = 0$ satisfies and where $\parallel \cdot \parallel_{\circ}$ denotes either the operator, Frobenius, or nuclear norm.

Using this intermediate result, we can bound the norms of the various derivatives which govern the smoothness and Lipschitz constants for the regularized OE problem. We present the proof of the following result in Appendix K ‣ Part II Proofs for Convergence Guarantee ‣ Globally Convergent Policy Search over Dynamic Filters for Output Estimation"), as well as formal explanations of the notation of the norms below.

### Proposition 6.3 (Smoothness and Lipschitzness)

For any $\mathsf{K} \in \mathcal{K}_{\mathtt{i}\mathtt{n}\mathtt{f}\mathtt{o}}$, $\mathcal{L}_{\lambda}{(\cdot)}$ is $\mathcal{C}^{2}$ in an open neighorhood containing $\mathcal{K}$, and where ${C_{\Sigma,1}{(\mathsf{K})}} = {{poly}_{op}{(\mathbf{\Sigma}_{\mathsf{K}},\mathbf{B}_{\mathsf{K}},\mathbf{C},\mathbf{W}_{2})}}$, where where $C_{\mathtt{l}\mathtt{y}\mathtt{a}\mathtt{p}}{(\mathsf{K})}$ is as in Proposition 6.2. ‣ Smoothness and Lipschitzness of ℒ_𝜆⁢(𝖪). ‣ 6.2 Proof of Theorem 3 ‣ 6 Proof of Theorems 3 and 2 ‣ Globally Convergent Policy Search over Dynamic Filters for Output Estimation"), and where the gradient norms are in the Euclidean geometry.

### Concluding the proof: uniform parameter bounds

Note again that bounds above are local, in that they depend on the choice of filter $\mathsf{K}$. To finish the proof of Theorem 3, we prove a uniform bound over all filters $\mathsf{K}$ which lie in the set considered by Proposition 5.3, namely.

Immediately, we see that on this set ${\|\mathbf{\Sigma}_{22,\mathsf{K}}^{- 1}\|} \leq 2$, and that As a consequence, we can bound the terms appear in the bounds above as follows (see Section G.2):

### Lemma 6.4

The terms ${C_{\mathtt{P}\mathtt{L}}{(\mathsf{K})}},{C_{\mathtt{l}\mathtt{y}\mathtt{a}\mathtt{p}}{(\mathsf{K})}},{C_{\Sigma,1}{(\mathsf{K})}},{C_{{\mathtt{g}\mathtt{r}\mathtt{a}\mathtt{d}},1}{(\mathsf{K})}},{C_{{\mathtt{g}\mathtt{r}\mathtt{a}\mathtt{d}},2}{(\mathsf{K})}}$ appearing above are all bounded by at most ${poly}_{op}{(\mathbf{\Sigma}_{\mathsf{K}}^{- 1},\mathbf{\Sigma}_{\mathsf{K}},\mathbf{A},\mathbf{C},\mathbf{G},\mathbf{W}_{2},\mathbf{W}_{2}^{- 1},\mathbf{W}_{1}^{- 1},{\mathcal{L}_{\lambda}{(\mathsf{K}_{0})}},\frac{1}{\lambda})}$.

Lastly, we control the dependence on $\mathbf{\Sigma}_{\mathsf{K}}$ and $\mathbf{\Sigma}_{\mathsf{K}}^{- 1}$. The follow lemma is proven in Section G.3 ‣ Appendix G Supporting Lemmas in Proof of Theorems 3 and 2 ‣ Part II Proofs for Convergence Guarantee ‣ Globally Convergent Policy Search over Dynamic Filters for Output Estimation").

### Lemma 6.5

Let $\sigma_{\star} > 0$ be as in we mean Lemma 3.3. Then, for any $\mathsf{K} \in \mathcal{K}_{\mathtt{c}\mathtt{t}\mathtt{r}\mathtt{b}}$, it holds that: (a) $\mathbf{\Sigma}_{\mathsf{K}} \succ 0$ is invertible, (b) ${\|\mathbf{\Sigma}_{\mathsf{K}}^{- 1}\|} \leq {{2{\|\mathbf{\Sigma}_{22,\mathsf{K}}^{- 1}\|}} + {2\sigma_{\star}^{- 1}{\max{\{ 1,{{\|\mathbf{\Sigma}_{22,\mathsf{K}}^{- 1}\|}{\|\mathbf{\Sigma}_{11,{sys}}\|}}\}}}}}$, and (c) ${\|\mathbf{\Sigma}_{\mathsf{K}}\|} \leq {2{\max{\{{\|\mathbf{\Sigma}_{22,\mathsf{K}}\|},{\|\mathbf{\Sigma}_{11,{sys}}\|}\}}}}$.

In particular, on $\mathcal{K}_{0}$, where ${{\|\mathbf{\Sigma}_{22,\mathsf{K}}^{- 1}\|},{\|\mathbf{\Sigma}_{22,\mathsf{K}}\|}} \leq 2$, we have ${{\|\mathbf{\Sigma}_{\mathsf{K}}\|},{\|\mathbf{\Sigma}_{\mathsf{K}}^{- 1}\|}} \leq {{poly}_{op}{({\|\mathbf{\Sigma}_{11,{sys}}\|},\sigma_{\star}^{- 1})}}$, so that the terms ${C_{\mathtt{P}\mathtt{L}}{(\mathsf{K})}},{C_{\mathtt{l}\mathtt{y}\mathtt{a}\mathtt{p}}{(\mathsf{K})}},{C_{\Sigma,1}{(\mathsf{K})}},{C_{{\mathtt{g}\mathtt{r}\mathtt{a}\mathtt{d}},1}{(\mathsf{K})}},{C_{{\mathtt{g}\mathtt{r}\mathtt{a}\mathtt{d}},2}{(\mathsf{K})}}$ are all at most polynomial in as well as in ${\mathcal{L}_{\lambda}{(\mathsf{K}_{0})}},\frac{1}{\lambda}$. Thus, from Corollaries 6.1. ‣ A DCL for the regularized OE objective. ‣ 6.2 Proof of Theorem 3 ‣ 6 Proof of Theorems 3 and 2 ‣ Globally Convergent Policy Search over Dynamic Filters for Output Estimation") and 6.3. ‣ Smoothness and Lipschitzness of ℒ_𝜆⁢(𝖪). ‣ 6.2 Proof of Theorem 3 ‣ 6 Proof of Theorems 3 and 2 ‣ Globally Convergent Policy Search over Dynamic Filters for Output Estimation"), we verify the conditions of Proposition 5.3 uniformly on the set $\mathcal{K}_{0}$.

### Corollary 6.2

The loss function $\mathcal{L}_{\lambda}$ satisfies $\alpha$-weak PL and $\beta$-upper smoothness on $\mathcal{K}_{0}$ with where $C_{\mathtt{s}\mathtt{y}\mathtt{s}}$ is defined in Eq. 6.4. In addition, on $\mathcal{K}_{0}$, $\mathcal{L}_{\lambda}$ is $L \leq {\sqrt{n}{poly}{(C_{\mathtt{s}\mathtt{y}\mathtt{s}},{\mathcal{L}_{\lambda}{(\mathsf{K}_{0})}},\lambda,\frac{1}{\lambda})}}$ Lipschitz, and $\mathsf{K}\mapsto\mathbf{\Sigma}_{22,\mathsf{K}}$ is at most $L_{\Sigma} \leq {{poly}{(C_{\mathtt{s}\mathtt{y}\mathtt{s}},{\mathcal{L}_{\lambda}{(\mathsf{K}_{0})}},\frac{1}{\lambda},\lambda)}}$ Lipschitz as a mapping from ${(\mathcal{K}_{\mathtt{i}\mathtt{n}\mathtt{f}\mathtt{o}}, \parallel \cdot \parallel_{\ell_{2}})}\rightarrow{({\mathbb{S}}^{n}, \parallel \cdot \parallel_{op})}$.

Lastly, we establish compact level sets. The subtlely here is not only showing that $\mathcal{K}_{0}$ is bounded (this is rather direct from Proposition 6.1), but also closed.

### Lemma 6.6

Let set $\mathcal{K}_{0}$ in Eq. 6.3 is compact.

The upper bound on ${\mathcal{L}_{\lambda}{(\mathsf{K}_{s})}} - {{\min_{\mathsf{K}}\mathcal{L}_{\lambda}}{(\mathsf{K})}}$ in Theorem 3 is now a direct consequence of instantiating Proposition 5.3 $\eta = \eta_{s}$ with the bounds in the above Corollary 6.2, and noting that $\mathcal{K}_{0}$ is closed by Lemma 6.6.

The inequality ${{\mathcal{L}_{\mathtt{O}\mathtt{E}}{(\mathsf{K}_{s})}} - {{\min_{\mathsf{K}}\mathcal{L}_{\mathtt{O}\mathtt{E}}}{(\mathsf{K})}}} \leq {{\mathcal{L}_{\lambda}{(\mathsf{K}_{s})}} - {{\min_{\mathsf{K}}\mathcal{L}_{\lambda}}{(\mathsf{K})}}}$ is just a consequence of Corollary 3.1. ∎

### Proof of Theorem 2

Due to the DCL exhbited by Proposition 6.1, and in particular Corollary 6.1. ‣ A DCL for the regularized OE objective. ‣ 6.2 Proof of Theorem 3 ‣ 6 Proof of Theorems 3 and 2 ‣ Globally Convergent Policy Search over Dynamic Filters for Output Estimation"), we find that any $\lambda \geq 0$ and $\mathsf{K} \in \mathcal{K}_{\mathtt{i}\mathtt{n}\mathtt{f}\mathtt{o}}$ for which ${{\nabla\mathcal{L}_{\lambda}}{(\mathsf{K})}} = 0$ must be optimal (in applying the corollary, we again note that $\mathbf{Z}_{\mathsf{K}}$ is guaranteed to be invertible of $\mathsf{K} \in \mathcal{K}_{\mathtt{i}\mathtt{n}\mathtt{f}\mathtt{o}}$, and $\mathbf{\Sigma}_{\mathsf{K}}$ invertible by Lemma 6.5). By taking $\lambda = 0$, we have ${{\nabla\mathcal{L}_{\lambda}}{(\mathsf{K})}} = {{\nabla\mathcal{L}_{\mathtt{O}\mathtt{E}}}{(\mathsf{K})}}$, proving the theorem. Path connectedness follows from Proposition 5.5, again noting that $\mathcal{K}_{0}$ is compact (Lemma 6.6). ∎

### DCL for Output Estimation (Proposition 6.1)

In this section, we establish the weak-PL property of our regularized loss function ${\mathcal{L}_{\lambda}{( \cdot )}} = {{\mathcal{L}_{\mathtt{O}\mathtt{E}}{( \cdot )}} + {\lambda\mathcal{R}_{\mathtt{i}\mathtt{n}\mathtt{f}\mathtt{o}}{( \cdot )}}}$. Our strategy is to show that $\mathcal{L}_{\lambda}{( \cdot )}$ admits a DCL, which leads to a weak-PL constant $\alpha{(\mathsf{K})}$ for each $\mathsf{K}$, whose parameters are themselves bounded in terms of $\mathcal{L}_{\lambda}{( \cdot )}$. Before continuing, we recall that $n$ denotes the dimension of the system state $\mathbf{x}$ (and internal state $\hat{\mathbf{x}}$), $m$ of the observation $\mathbf{y}$, and $p$ the output $\mathbf{z}$, and that ${poly}_{op}{(\mathbf{X}_{1},\mathbf{X}_{2},\ldots,\kappa)}$ denote a (universal) polynomial function of operator norm of matrix, arguments ${\|\mathbf{X}_{1}\|},{{\|\mathbf{X}_{2}\|}_{,}\ldots}$, and a polynomial in scalar argument $\kappa$. We use ${\mathbb{I}}_{\infty}$ to denote the $1$-$\infty$ indicator, i.e. for some event $\mathcal{E}$, ${{\mathbb{I}}_{\infty}{\{\mathcal{E}\}}} = 1$ if $\mathcal{E}$ is true, and ${{\mathbb{I}}_{\infty}{\{\mathcal{E}\}}} = {+ \infty}$ otherwise.

All proofs of the lemmas that follow are deferred to Appendix I ‣ Part II Proofs for Convergence Guarantee ‣ Globally Convergent Policy Search over Dynamic Filters for Output Estimation"). To proceed, we need to invoke Theorem 4 by specifying the DCL of the function Throughout, given a matrix $\mathbf{\Sigma} \succ 0$ partitioned in $2 \times 2$ blocks, we more generally define With the above notation, we can express This leads to the following notion of the lifted function.

### Definition 6.1 (The lifted function)

We define the lifted function on the space of parameters ${(\mathsf{K},\mathbf{\Sigma})} \in {\mathcal{K}_{\mathtt{i}\mathtt{n}\mathtt{f}\mathtt{o}} \times {\mathbb{S}}^{2n}}$ as follows We extend $f_{\mathtt{l}\mathtt{f}\mathtt{t}}{(\mathsf{K},\mathbf{\Sigma})}$ to the space of all (unconstrained, even possible unstable) filters $\mathsf{K} = {(\mathbf{A}_{\mathsf{K}},\mathbf{B}_{\mathsf{K}},\mathbf{C}_{\mathsf{K}})}$ by setting the lifted function to be infinte when $\mathsf{K} \notin \mathcal{K}_{\mathtt{i}\mathtt{n}\mathtt{f}\mathtt{o}}$: ${f_{\mathtt{l}\mathtt{f}\mathtt{t}}{(\mathsf{K},\mathbf{\Sigma})}} = {f_{\mathtt{l}\mathtt{f}\mathtt{t}}{(\mathsf{K},\mathbf{\Sigma})}{\mathbb{I}}_{\infty}{\{{\mathsf{K} \in \mathcal{K}_{\mathtt{i}\mathtt{n}\mathtt{f}\mathtt{o}}}\}}}$.^99^9This formalism is just to accomodate for the fact that we encode constraints on domains in the function in general DCL framework.

### Step 1. Verifying the lifting

We first verify that $f_{\mathtt{l}\mathtt{f}\mathtt{t}}$ is indeed a lifted function of $\mathcal{L}_{\lambda}$.

### Lemma 6.7

For any feasible $\mathsf{K} \in \mathcal{K}_{\mathtt{i}\mathtt{n}\mathtt{f}\mathtt{o}}$, and this minimum is attained for $\mathbf{\Sigma} = \mathbf{\Sigma}_{\mathsf{K}}$.

### Step 2. Convex reparametrization

Next, we introduce the transformation $\Phi$:

### Definition 6.2

We define the convex parameter ${\mathbf{ν}}:={(\mathbf{L}_{1},\mathbf{L}_{2},\mathbf{L}_{3},\mathbf{M}_{1},\mathbf{M}_{2})}$ and the transformation We let $d_{\nu}$ denote the dimension of the parameter $\mathbf{ν}$ and let $d_{y}$ denote the dimension of the parameters $(\mathsf{K},\mathbf{\Sigma})$, both as Euclidean vectors. One can then verify that $d_{\nu} \leq d_{y}$; that is, the lifted function indeed has more parameters than the convex one. The following shows that there exists a convex function $f_{\mathtt{c}\mathtt{v}\mathtt{x}}$, which completes the DCL:

### Lemma 6.8

There exists a convex function $f_{\mathtt{c}\mathtt{v}\mathtt{x}}:{{\mathbb{R}}^{d_{\nu}}\rightarrow\overline{\mathbb{R}}}$ such that The transformation $\Phi$ and associated convex function $f_{\mathtt{c}\mathtt{v}\mathtt{x}}$ was first developed by Scherer et al., cf. also Masubuchi et al. for contemporaneous independent work.

### Step 3. Controlling the weak-PL constant

Lastly, we show that the DCL lends itself to a bounded PL constant by invoking Theorem 4. To do this, we need to show that the image of $\Phi{(\mathsf{K},\mathbf{\Sigma})}$ is not too large, and that ${\nabla\Phi}{( \cdot )}$ has rank at least $d_{\nu}$. We establish both in sequence. Let $\mathbf{U}_{\mathsf{K}}$ and $\mathbf{V}_{\mathsf{K}}$ be corresponding to Eq. 6.8b ‣ 6 Proof of Theorems 3 and 2 ‣ Globally Convergent Policy Search over Dynamic Filters for Output Estimation") with $\mathbf{\Sigma} = \mathbf{\Sigma}_{\mathsf{K}}$, i.e.

### Lemma 6.9 (Parameter compactness)

Consider $(\mathsf{K},\mathbf{\Sigma}_{\mathsf{K}})$, where $\mathbf{\Sigma}_{\mathsf{K}}$ is the stationary covariance associated with $\mathsf{K}$. Then, where ${\|{\mathbf{ν}}\|}_{\ell_{2}}:=\sqrt{{\sum_{i = 1}^{3}{\|\mathbf{L}_{i}\|}_{F}^{2}} + {\sum_{j = 1}^{2}{\|\mathbf{M}_{i}\|}_{F}^{2}}}$ denotes the Euclidean norm of the parameter $\mathbf{ν}$. Moreover, if $\mathbf{U}_{\mathsf{K}}$ and $\mathbf{V}_{\mathsf{K}}$ are invertible, then the filter parameters are bounded by

### Lemma 6.10 (Conditioning of $\nabla\Phi$)

Suppose that $\mathsf{K} \in \mathcal{K}_{\mathtt{i}\mathtt{n}\mathtt{f}\mathtt{o}}$. Then, $\Phi$ is differentiable in an open neighborhood of $(\mathsf{K},\mathbf{\Sigma}_{\mathsf{K}})$, and if $\mathbf{U}_{\mathsf{K}}$ and $\mathbf{V}_{\mathsf{K}}$ are invertible, where the last line is a consequence of Lemma 6.9. ‣ Step 3. Controlling the weak-PL constant. ‣ 6.4 DCL for Output Estimation (Proposition 6.1) ‣ 6 Proof of Theorems 3 and 2 ‣ Globally Convergent Policy Search over Dynamic Filters for Output Estimation").

To conclude, we eliminate dependencies on $\mathbf{U}_{\mathsf{K}}$ and $\mathbf{V}_{\mathsf{K}}$:

### Lemma 6.11

If $\mathbf{Z} = {\mathbf{Z}{(\mathbf{\Sigma})}}$ is invertible, the matrices $\mathbf{U} = {(\mathbf{\Sigma}^{- 1})}_{12}$ and $\mathbf{V} = \mathbf{\Sigma}_{12}$ are invertible, and their inverses are bounded in operator norm as As a consequence of Lemmas 6.10. ‣ Step 3. Controlling the weak-PL constant. ‣ 6.4 DCL for Output Estimation (Proposition 6.1) ‣ 6 Proof of Theorems 3 and 2 ‣ Globally Convergent Policy Search over Dynamic Filters for Output Estimation") and 6.9. ‣ Step 3. Controlling the weak-PL constant. ‣ 6.4 DCL for Output Estimation (Proposition 6.1) ‣ 6 Proof of Theorems 3 and 2 ‣ Globally Convergent Policy Search over Dynamic Filters for Output Estimation"), The conclusion of Eq. 6.12 ‣ 6 Proof of Theorems 3 and 2 ‣ Globally Convergent Policy Search over Dynamic Filters for Output Estimation") and the bound ${\|\mathbf{C}_{\mathsf{K}}\|}_{F} \leq \sqrt{{\mathcal{L}_{\mathtt{O}\mathtt{E}}{(\mathsf{K})}}/{\|\mathbf{\Sigma}_{\mathsf{K}}^{- 1}\|}}$ from Lemma 6.9. ‣ Step 3. Controlling the weak-PL constant. ‣ 6.4 DCL for Output Estimation (Proposition 6.1) ‣ 6 Proof of Theorems 3 and 2 ‣ Globally Convergent Policy Search over Dynamic Filters for Output Estimation") are precisely the conclusions of Proposition 6.1. ∎

### Conclusion

The work introduces the first policy search algorithm which converges to the globally optimal *dynamic* filter for the output estimation problem. We hope that our analysis serves as a valuable starting point to study direct policy search for reinforcement learning and control problems with partial observations, in which the relevant class of policies are dynamic and maintain internal state. We also hope that both our proposed principle of informativity, and our technical contributions around convex reformulations, continue to prove useful in future work.
