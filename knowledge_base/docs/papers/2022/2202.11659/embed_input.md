<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Globally Convergent Policy Search over Dynamic Filters for Output Estimation

Topics include Gradient descent, Reinforcement learning, Lyapunov methods, Learning, Linear dynamical system, Dynamical systems.

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

We introduce the first direct policy search algorithm which provably converges to the globally optimal dynamic filter for the classical problem of predicting the outputs of a linear dynamical system, given noisy, partial observations. Despite the ubiquity of partial observability in practice, theoretical guarantees for direct policy search algorithms, one of the backbones of modern reinforcement learning, have proven difficult to achieve. This is primarily due to the degeneracies which arise when optimizing over filters that maintain internal state. In this paper, we provide a new perspective on this challenging problem based on the notion of informativity, which intuitively requires that all components of a filter's internal state are representative of the true state of the underlying dynamical system. We show that informativity overcomes the aforementioned degeneracy. Specifically, we propose a regularizer which explicitly enforces informativity, and establish that gradient descent on this regularized objective - combined with a ``reconditioning step'' - converges to the globally optimal cost a O(1/T) rate.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Our analysis relies on several new results which may be of independent interest, including a new framework for analyzing non-convex gradient descent via convex reformulation, and novel bounds on the solution to linear Lyapunov equations in terms of (our quantitative measure of) informativity.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

Data used for prediction and control of real world dynamical systems is almost always noisy and incomplete (partially observed). Sensors and other measurement procedures inevitably introduce errors into the datasets, so designing reliable learning algorithms for these noisy or partially observed domains requires confronting fundamental questions of disturbance filtering and state estimation. Despite the ubiquity of partial observation in practice, these concerns are often underexplored in modern analyses of learning for control that assume perfect observations of the underlying dynamics.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

In this work, we study the output estimation (OE) problem or learning to predict in partially observed linear dynamical systems. The output estimation problem is one of the most fundamental problems in theoretical statistics and learning theory. Both in theory and in practice, advances in predicting partially observed linear systems have led to successes in a variety of areas from controls to biology and economics, (c.f. e.g. Athans; Lillacci and Khammash; Gautier and Poignet ). We revisit this classical problem from a modern optimization perspective, and study the possibility of learning the optimal predictor via model-free procedures and direct policy search.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

Relative to model-based procedures, which first estimate the underlying dynamics and then return a policy by solving an optimization problem using the estimated model, model-free methods offer several potential advantages. First, direct policy search allows one to easily specify the complexity of the policy class over which one searches. For example, the vast majority of industrial control systems are built upon proportional-integral-derivative (PID) controllers. Each PID controller comprises three scalar variables (gains) yet successfully regulates complex feedback loops in high-dimensional systems (e.g chemical plants). In addition, model-free policy search optimizes for performance directly on the true system, rather than an approximate model. As such, there is no gap between the model used for synthesis and the system on which the controller is deployed. Such gaps are typically covered by robust control techniques, which may introduce conservatism.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

In light of these advantages, there has recently been significant interest from both theoreticians and practitioners in understanding the foundations of model-free control. However, so far, this attention has been mostly focused on problems with full-state observation such as the linear quadratic regulator (LQR) or fully-observed Markov Decision Processes (MDPs) which admit *static* policies. Progress in dealing with partially observed problems has been complicated by the difficulties associated with optimizing over *dynamic* policies that maintain internal state to summarize past observations. In this paper, we provide the first policy search algorithm which provably converges to the globally optimal filter for the OE problem, and shed new light on the intricacies of the underlying optimization landscape.

<!-- chunk {"id": "body-0008", "role": "body", "section": "The Output Estimation problem", "weight": 1.0} -->

We study one of the simplest and most basic problems with partial observability: the *output estimation* (OE) problem. In brief, the goal is to search for a predictor of the output $\mathbf{z}{(t)}$ of a linear dynamical system given partial measurements $\mathbf{y}{(t)}$.

<!-- chunk {"id": "body-0009", "role": "body", "section": "The Output Estimation problem", "weight": 1.0} -->

${{\mathbf{w}{(t)}\overset{i.i.d}{\sim}\mathcal{N}{(0,\mathbf{W}_{1})}},{\mathbf{v}{(t)}\overset{i.i.d}{\sim}\mathcal{N}{(0,\mathbf{W}_{2})}}},$ | | | the goal is to find the parameters $\mathsf{K} = {(\mathbf{A}_{\mathsf{K}},\mathbf{B}_{\mathsf{K}},\mathbf{C}_{\mathsf{K}})}$ of the *filter* (interchangably, *policy*), that minimizes the steady-state prediction error, In this paper, we study solving the OE problem via model-free methods, where the goal is to search for the optimal filter parameters $\mathsf{K} =

<!-- chunk {"id": "body-0010", "role": "body", "section": "The Output Estimation problem", "weight": 1.0} -->

{(\mathbf{A}_{\mathsf{K}},\mathbf{B}_{\mathsf{K}},\mathbf{C}_{\mathsf{K}})}$ using direct policy search without knowledge or estimation of the true system parameters $\mathbf{A},\mathbf{C},\mathbf{G},\mathbf{W}_{1},\mathbf{W}_{2}$; cf. Section 2 for a detailed problem description.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Contributions", "weight": 1.0} -->

In this paper, we propose a novel policy search method which provably converges to a globally optimal $\mathcal{L}_{\text{OE}}$ cost. Despite extensive prior work on *static* policy search (e.g. Fazel et al.; Agarwal et al., our result constitutes the first rigorous guarantee for policy search over *dynamic* policies.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Contributions", "weight": 1.0} -->

A key concept underpinning our results is the notion of *informativity*, which requires each component of the internal filter state $\hat{\mathbf{x}}$ to capture some information about the true state $\mathbf{x}$ of the system. More precisely, a policy is said to be *informative* if the steady-state correlation matrix $\mathbf{\Sigma}_{12}:={\lim_{T\rightarrow\infty}{\frac{1}{T}{\lbrack{\int_{0}^{T}{\mathbf{x}{(t)}\hat{\mathbf{x}}{(t)}^{\top}{dt}}}\rbrack}}}$ is full-rank.^11^1For simplicity, we assume knowledge of the *dimension* of the true system state, and policies are parameterized so that $\mathbf{x}$ and $\hat{\mathbf{x}}$ are of the same dimension.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Limitations of direct policy search", "weight": 1.5} -->

Through simulations and counterexamples, we show that gradient descent on the prediction loss $\mathcal{L}_{\mathtt{O}\mathtt{E}}{( \cdot )}$ can fail to recover the optimal filter for OE problem. While consistent with prior work, the failure of gradient descent remains puzzling, as the OE problem admits a convex reformulation, a fact which at first glance seems to rule out suboptimal stationary points.

<!-- chunk {"id": "body-0014", "role": "body", "section": "Structure of the OE optimization landscape", "weight": 1.0} -->

We reconcile this apparent contradiction - the existence of convex reformulations and the failure of policy search - by studying cases in which the former breaks down. We show that suboptimal stationary points can arise when the internal state $\hat{\mathbf{x}}$ of the filter is non-informative about the state $\mathbf{x}$ of the true system, in the sense described above. These are precisely the points at which the convex reformulation breaks down. We also establish the converse: when $\hat{\mathbf{x}}$ is "uniformly informative" about $\mathbf{x}$, all stationary points are globally optimal.

<!-- chunk {"id": "body-0015", "role": "body", "section": "A provably convergent policy search algorithm", "weight": 1.0} -->

Building on this insight, we propose a regularizer $\mathcal{R}$ that ensures the internal state of the learned policy remains "uniformly informative" about the state of the true system. We prove that gradient descent on the regularized objective ${\mathcal{L}_{\mathtt{O}\mathtt{E}}{( \cdot )}} + {\lambda\mathcal{R}{( \cdot )}}$ converges at a $\mathcal{O}\left( {1/T} \right)$ rate to an optimal policy.

<!-- chunk {"id": "body-0016", "role": "body", "section": "Our techniques", "weight": 1.0} -->

Searching over dynamic policies introduces two key challenges: spurious critical points can arise when one or more factors become "degenerate" in a certain way; changes of basis produce a continuum of "equivalent realizations" of the filter $\mathsf{K}$, some of which are poorly conditioned. Similar challenges have been observed in problems with rotational symmetries, e.g. nonconvex matrix factorization. Neither challenge arises when searching over static policies.

<!-- chunk {"id": "body-0017", "role": "body", "section": "Our techniques", "weight": 1.0} -->

Departing from prior literature on nonconvex factorization problems, which often either leverages closed-form gradient computations and/or the presence of strict-saddles, our approach is centered around the idea of *convex reformulations* of control synthesis problems, and the following fact regarding functions which admit these reformulations, cf. Section H.1 for proof.

<!-- chunk {"id": "body-0018", "role": "body", "section": "Fact 1.1", "weight": 1.0} -->

The OE problem, LQG, and many other related control tasks admit convex reformulations. Given that gradient descent (under additional mild regularity assumptions) converges to stationary points, we might hope that 1.1 guarantees that direct policy search on the OE filter will succeed at finding an optimal policy, when applied to loss functions admitting such convex reformulations. Somewhat surprisingly, we find that this is emphatically not the case: gradient descent on the $\mathcal{L}_{\mathtt{O}\mathtt{E}}$ objective fails to reliably converge to optimal solutions (see Section 3.1).^22^2Failure modes for the LQG problem were presented by Tang et al..

<!-- chunk {"id": "body-0019", "role": "body", "section": "Fact 1.1", "weight": 1.0} -->

To resolve this paradox, we show that the surjectivity condition of 1.1 may fail for the convex reparametrization of OE: there are filters $\mathsf{K}$ with finite cost $\mathcal{L}_{\mathtt{O}\mathtt{E}}{(\mathsf{K})}$, which are not in the image of the reformulation map $\Psi{( \cdot )}$. We find that degeneracy occurs precisely when *informativity*, defined in Section 1.1 as $\mathbf{\Sigma}_{12,\mathsf{K}}$ having full rank, fails to hold. Conversely, when $\mathbf{\Sigma}_{12,\mathsf{K}}$ is full-rank, the conditions of 1.1 are met and the parametrization behaves as needed. Thus, we identify *non-informativity* - rank deficiency of $\mathbf{\Sigma}_{12,\mathsf{K}}$ - as the fundamental notion of degeneracy corresponding to challenge.

<!-- chunk {"id": "body-0020", "role": "body", "section": "Fact 1.1", "weight": 1.0} -->

Motivated by this observation, we introduce a novel "informativity regularizer" $\mathcal{R}_{\mathtt{i}\mathtt{n}\mathtt{f}\mathtt{o}}{( \cdot )}$ which enforces that $\mathbf{\Sigma}_{12,\mathsf{K}}$ is full rank. Our proposed algorithm, IR-PG alternates between gradient updates on the regularized loss ${\mathcal{L}_{\lambda}{( \cdot )}}:={{\mathcal{L}_{\mathtt{O}\mathtt{E}}{( \cdot )}} + {\lambda\mathcal{R}_{\mathtt{i}\mathtt{n}\mathtt{f}\mathtt{o}}{( \cdot )}}}$, and "reconditioning" steps to ensure well-conditioned realizations of the filters $\mathsf{K}$, thereby addressing challenge above.

<!-- chunk {"id": "body-0021", "role": "body", "section": "Fact 1.1", "weight": 1.0} -->

We stress that our notion of informativity differs from the *minimality* criterion emphasized in Tang et al., whose limitations we discuss in Section 3.1.

<!-- chunk {"id": "body-0022", "role": "body", "section": "Fact 1.1", "weight": 1.0} -->

In order to achieve our quantitative converge guarantees, we establish numerous results which may be of independent interest, including a quantitative analysis of the OE convex reformulation due to Scherer, and novel bounds on the magnitude of solution to Lyapunov equations under the closed-loop OE filter dynamics. Both arguments appeal to a (quantitative measure of) informativity, suggesting informativity is somehow natural for the OE landscape.

<!-- chunk {"id": "body-0023", "role": "body", "section": "Fact 1.1", "weight": 1.0} -->

We also develop a quantitative analogue of 1.1 via a paradigm we call *differentiable convex liftings*, or DCLs. Informally, a DCL "lifts" the nonconvex $f$ to a possibly nonconvex, non-smooth function $f_{\mathtt{l}\mathtt{f}\mathtt{t}}$ with $n_{y} \geq n_{x}$ parameters, which may take values in the extended reals so as incorporate constraints. We stress that both the 'lifting' and accommodation of constraints are essential to capture the OE convex reformulation. A DCL further requires existence of a map $\Phi$ and a convex function $f_{cvx}$ with $n_{\nu} \leq n_{y}$ parameters such that ${f_{\mathtt{l}\mathtt{f}\mathtt{t}}{( \cdot )}}:={f_{cvx}{({\Phi{( \cdot )}})}}$.

<!-- chunk {"id": "body-0024", "role": "body", "section": "Fact 1.1", "weight": 1.0} -->

Intuitively, $\Phi$ corresponds to the inverse of the map $\Psi$ in 1.1, though this parameterization allows more flexibility because $n_{y} > n_{\nu}$ may be permitted. For such liftings, the following result strengthens and refines 1.1:

<!-- chunk {"id": "body-0025", "role": "body", "section": "Solution of the OE problem & Convex reformulation", "weight": 1.0} -->

The solution to the OE problem^33^3Kalman addressed the discrete-time problem, with $\mathbf{G} = \mathbf{C}$. is given by the celebrated *Kalman filter*. The problem is also a special case of LQG, cf. Doyle et al.. Solution methods based on linear matrix inequalities (LMI) for OE - as well as many other control problems, including $\mathcal{H}_{2}$, $\mathcal{H}_{\infty}$, and mixed $\mathcal{H}_{2}/\mathcal{H}_{\infty}$ synthesis - were developed, concurrently and independently, by Scherer et al. and Masubuchi et al.. The methods were based on convex reformulations of the variety described in Section 1.2, and represent non-trivial generalizations of the well-known change of variables used to obtain LMI formulations of static state feedback problems, cf. Thorp and Barmish; Bernussou et al..

<!-- chunk {"id": "body-0026", "role": "body", "section": "Solution of the OE problem & Convex reformulation", "weight": 1.0} -->

It has long been appreciated that most cost functions optimized for controller synthesis are *nonconvex*. Such problems are usually solved indirectly, e.g. by reconstructing policies from the solutions of Riccati equations or LMIs, or by using (model-based) policy parametrizations that make the cost function convex, e.g. Youla et al.; Kučera.

<!-- chunk {"id": "body-0027", "role": "body", "section": "Direct policy search for control with full state observation", "weight": 1.0} -->

Recent years have witnessed a resurgence of interest in direct policy search, driven perhaps in part by the success of such approaches in reinforcement learning, e.g. Schulman et al.; Andrychowicz et al.. Specifically, Fazel et al. established global convergence of policy gradient methods on the discrete-time linear quadratic regulator (LQR) problem, the simplest continuous state-action optimal control problem. Subsequent work has sharpened rates, analyzed convergence under more general frameworks, and extended the analysis to work in continuous-time. Beyond LQR, Zhang et al. analyzed global convergence of policy search for mixed $\mathcal{H}_{2}/\mathcal{H}_{\infty}$ control and risk-sensitive control. Furieri et al. and Li et al. established the convergence of policy search for certain distributed control problems. Sun and Fazel also considered analysis via convex reformulations, for state feedback problems. For discrete state-action (discounted) Markov decision processes (MDPs), Agarwal et al. established convergence rates for a variety of policy gradient methods with both tabular and parametric policies, cf. also Bhandari and Russo.

<!-- chunk {"id": "body-0028", "role": "body", "section": "Direct policy search for control with full state observation", "weight": 1.0} -->

All of these works considered *static* state-feedback policies, with perfect state information.

<!-- chunk {"id": "body-0029", "role": "body", "section": "Problems with partial observation", "weight": 1.0} -->

For problems with partial observation, optimal policies are typically dynamic, so as to incorporate information from the entire past history of observations. The most relevant related work is Tang et al., which studied the optimization landscape of the LQG problem. They establish that all stationary points corresponding to controllable and observable controllers are globally optimal. They also show (both empirically and via theoretical counterexamples) that gradient descent may fail to converge to globally optimal policies; a finding that, as we shall show, remains valid even for the simpler OE problem. Fatkhullin and Polyak also considered linear quadratic control in the partially observed setting, but restrict their attention to *static* output feedback policies, and provide conditions under which gradient descent converges to (possibly suboptimal) stationary points.

<!-- chunk {"id": "body-0030", "role": "body", "section": "Organization", "weight": 1.0} -->

This paper is organized as follows. Section 2 provides the relevant preliminaries and assumptions for our setting, as well as details for our interaction protocol. Section 3 provides our main results: first, a number of counterexample examples explaining the challenges of policy search over dynamic filters, and limitations of past work; second, a detailed distribution of our algorithm, IR-PG; third, a rigorous convergence guarantee. Section 4 presents the numerical examples that illustrate the performance of our algorithm. Section 5 describes our main technical hammer - DCLs - and how they afford quantitative convergence guarantees for gradient descent. Finally, Section 6 provides the skeleton of the proofs of our main theorems. We provide concluding remarks in Section 7, and detail the organization of the appendix in Appendix A.

<!-- chunk {"id": "body-0031", "role": "body", "section": "Output Estimation (OE)", "weight": 1.0} -->

As outlined in the introduction, we consider the problem of predicting the outputs of a partially observed linear dynamical system. We refer to the dynamical system defined in Eq. 1.1 as the *true system*, with states ${\mathbf{x}{(t)}} \in {\mathbb{R}}^{n}$, observations ${\mathbf{y}{(t)}} \in {\mathbb{R}}^{m}$, and performance outputs ${\mathbf{z}{(t)}} \in {\mathbb{R}}^{p}$. To ensure the dynamics have a well-defined steady-state, we assume that $\mathbf{A}$ is stable.

<!-- chunk {"id": "body-0032", "role": "body", "section": "Assumption 2.1", "weight": 1.0} -->

The matrix $\mathbf{A}$ is *Hurwitz stable*. That is, the real components of all its eigenvalues are strictly negative: ${\Re{\lbrack{\lambda_{i}{(\mathbf{A})}}\rbrack}} < 0$ for $i \in {\lbrack n\rbrack}$.

<!-- chunk {"id": "body-0033", "role": "body", "section": "Assumption 2.1", "weight": 1.0} -->

Because these policies only access the system outputs, and are only evaluated in relation to system outputs, we assume that the true system state is *observable*. Further, we assume that dynamics are subject to sufficiently rich noise excitations.

<!-- chunk {"id": "body-0034", "role": "body", "section": "Assumption 2.2", "weight": 1.0} -->

The pair $(\mathbf{A},\mathbf{C})$ in Eq. 1.1 is observable. That is, the observability Gramian defined as is strictly positive definite.

<!-- chunk {"id": "body-0035", "role": "body", "section": "Assumption 2.3", "weight": 1.0} -->

We assume that the noise matrices $\mathbf{W}_{1}$ and $\mathbf{W}_{2}$ are strictly positive definite.^44^4We may relax this assumption to $(\mathbf{A},\mathbf{W}_{1})$ controllable.

<!-- chunk {"id": "body-0036", "role": "body", "section": "Assumption 2.3", "weight": 1.0} -->

As stated previously, we restrict our attention to finding the best dynamic filter within the parametric family described in Eq. 1.2. Note that this family contains the *Bayes optimal predictor* for the $\mathcal{L}_{\mathtt{O}\mathtt{E}}$ objective, as we will later describe in more detail.

<!-- chunk {"id": "body-0037", "role": "body", "section": "Steady state distributions", "weight": 1.0} -->

We define $\mathcal{K}_{\mathtt{s}\mathtt{t}\mathtt{a}\mathtt{b}}:=\left\{ \mathsf{K}:{\mathbf{A}_{\mathsf{K}}\text{~is Hurwitz-stable}} \right\}$ to be the set of filters such that $\mathbf{A}_{\mathsf{K}}$ is stable. Under Assumption 2.1 ‣ 2 Preliminaries ‣ Globally Convergent Policy Search over Dynamic Filters for Output Estimation"), Section E.1 shows this equivalent to stability of the closed-loop matrix $\mathbf{A}_{{cl},\mathsf{K}}$.

<!-- chunk {"id": "body-0038", "role": "body", "section": "Steady state distributions", "weight": 1.0} -->

Stability of $\mathbf{A}_{{cl},\mathsf{K}}$ is a sufficient condition for $\mathcal{L}_{\mathtt{O}\mathtt{E}}{(\mathsf{K})}$ to be finite, and for the following limiting covariance to be well defined, This steady-state covariance is given by the solution to the continuous-time Lyapunov equation, Notice that $\mathbf{\Sigma}_{\mathsf{K}}$ depends only on $(\mathbf{A}_{\mathsf{K}},\mathbf{B}_{\mathsf{K}})$, but not on $\mathbf{C}_{\mathsf{K}}$, and that the first $n \times n$ block of $\mathbf{\Sigma}_{\mathsf{K}}$ does not depend on the choice of filter $\mathsf{K}$ at all.

<!-- chunk {"id": "body-0039", "role": "body", "section": "Steady state distributions", "weight": 1.0} -->

We refer to these as the *controllable* policies, as these are precise the policies for which the pair $(\mathbf{A}_{\mathsf{K}},\mathbf{B}_{\mathsf{K}})$ is controllable.^55^5Controllability is the "dual" of observabilitity, and is equivalent to observability of $(\mathbf{A}_{\mathsf{K}}^{\top},\mathbf{B}_{\mathsf{K}}^{\top})$, cf. Section E.1.

<!-- chunk {"id": "body-0040", "role": "body", "section": "Equivalent realizations", "weight": 1.0} -->

Contrary to static feedback policies, such as LQR,there are many different ways of parametrizing a given *dynamic* feedback policy, all of which have exactly the same input-output behavior.

<!-- chunk {"id": "body-0041", "role": "body", "section": "Equivalent realizations", "weight": 1.0} -->

We say that $\mathsf{K}$ and $\mathsf{K}'$ are *equivalent realizations* if they are related by a similarity transformation ${{\mathsf{S}\mathsf{i}\mathsf{m}}_{\mathbf{S}}{(\mathsf{K})}} = \mathsf{K}'$ for some $\mathbf{S} \in {{\mathbb{G}}{\mathbb{L}}{(n)}}$.^66^6This is a symmetric relationship, since then ${{\mathsf{S}\mathsf{i}\mathsf{m}}_{\mathbf{S}^{- 1}}{(\mathsf{K}')}} = \mathsf{K}$, and hence equivalent policies form an equivalence class. Note that the set $\mathcal{K}_{\mathtt{c}\mathtt{t}\mathtt{r}\mathtt{b}}$ is also preserved under similarity transformation.

<!-- chunk {"id": "body-0042", "role": "body", "section": "Restricted problem setting", "weight": 1.0} -->

The problem description outlined in Section 2.2 ‣ 2 Preliminaries ‣ Globally Convergent Policy Search over Dynamic Filters for Output Estimation"), including Assumptions 2.1 ‣ 2 Preliminaries ‣ Globally Convergent Policy Search over Dynamic Filters for Output Estimation"), 2.2 ‣ 2 Preliminaries ‣ Globally Convergent Policy Search over Dynamic Filters for Output Estimation") and 2.3 ‣ 2 Preliminaries ‣ Globally Convergent Policy Search over Dynamic Filters for Output Estimation"), constitutes the standard OE problem, well-known in control theory, cf.. In this paper, we will make the following additional assumption that restricts the class of OE problems we consider. Further discussion on the utility and necessity of this assumption (for our analysis) is provided in Section 3.2 and Appendix D; the latter also shows that Assumption 2.4 holds for "generic" problem instances.

<!-- chunk {"id": "body-0043", "role": "body", "section": "Assumption 2.4", "weight": 1.0} -->

Here, we simply remark that Assumption 2.4 ensures that the regularizer $\mathcal{R}_{\mathtt{i}\mathtt{n}\mathtt{f}\mathtt{o}}{(\mathsf{K})}$, responsible for maintaining informativity of the policy $\mathsf{K}$, is well-defined at the optimal policy.

<!-- chunk {"id": "body-0044", "role": "body", "section": "Interaction protocol", "weight": 1.0} -->

In the spirit of model-free methods, we introduce algorithms which work only assuming access to cost and gradient evaluation oracles. We abstract away the particular implementation of these oracles to simplify our presentation and assume that they are exact, in order to focus on the overall optimization landscape of the OE problem. More formally, for any filter $\mathsf{K} \in \mathcal{K}_{\mathtt{s}\mathtt{t}\mathtt{a}\mathtt{b}}$, ${\mathsf{E}\mathsf{v}\mathsf{a}\mathsf{l}}{(\mathsf{K},\mathcal{L}_{\mathtt{O}\mathtt{E}})}$ returns the OE cost, $\mathcal{L}_{\mathtt{O}\mathtt{E}}{(\mathsf{K})}$.

<!-- chunk {"id": "body-0045", "role": "body", "section": "Interaction protocol", "weight": 1.0} -->

Despite this simplification, we would like to again emphasize that these can be efficiently approximated in finite samples, and purely on the basis of *observations* $\mathbf{y}_{t}$ subsampled in in discrete intervals. For further discussion, please see Appendix C.

<!-- chunk {"id": "body-0046", "role": "body", "section": "Interaction protocol", "weight": 1.0} -->

Lastly, in addition to standard cost and gradient evaluations of the $\mathcal{L}_{\mathtt{O}\mathtt{E}}$ loss, as part of our algorithm, we further require access to gradient and cost evaluations of smooth functions of the stationary-state covariance.

<!-- chunk {"id": "body-0047", "role": "body", "section": "Interaction protocol", "weight": 1.0} -->

Specifically, if $f:{{\mathbb{S}}_{+}^{2n}\rightarrow{\mathbb{R}}}$ is a function of the covariance matrix $\mathsf{K}$, we assume we can compute ${\mathsf{E}\mathsf{v}\mathsf{a}\mathsf{l}}_{cov}{(\mathsf{K},f)}$ which returns the $f{(\mathbf{\Sigma}_{\mathsf{K}})}$ and ${\mathsf{G}\mathsf{r}\mathsf{a}\mathsf{d}}_{cov}{(\mathsf{K},f)}$ which returns ${\nabla_{\mathsf{K}}f}{(\mathbf{\Sigma}_{\mathsf{K}})}$. In Section C.2, we show that these oracles can be implemented without direct state access by "subsampling" multiple observations at different time increments.

<!-- chunk {"id": "body-0048", "role": "body", "section": "Main Results", "weight": 1.0} -->

In this section, we present the main contributions of our work. After demonstrating that the OE cost function contains stationary points that are not globally optimal, we present informativity-regularized policy gradient (IR-PG), a direct policy search algorithm based on a novel regularization strategy to preserve *informativity*, introduced in Section 1.2. We state a formal convergence result showing that IR-PG converges to a globally optimal filter at a $\mathcal{O}\left( {1/T} \right)$ rate.

<!-- chunk {"id": "body-0049", "role": "body", "section": "Existence of suboptimal stationary points", "weight": 1.0} -->

Perhaps the simplest model-free approach to the OE problem is to run gradient descent on the loss function: for some stepsize(s) $\eta_{t} > 0$. Under mild assumptions on the loss function $\mathcal{L}_{\mathtt{O}\mathtt{E}}$, gradient descent will converge to a first-order stationary point of $\mathcal{L}_{\mathtt{O}\mathtt{E}}$. Unfortunately, despite the existence of a convex reformulation and 1.1,

<!-- chunk {"id": "body-0050", "role": "body", "section": "Example 3.1", "weight": 1.0} -->

A formal proof of this claim is given in Section F.1, however, one can easily verify that the cost is invariant under perturbations to any single parameter of the filter. Specifically: (i) perturbations to $\mathbf{A}_{bad}$ and $\mathbf{B}_{bad}$ do not change the cost, because $\mathbf{C}_{bad} = \mathbf{0}$ and thus the filter output $\mathbf{z}{(t)}$ is always zero, and (ii) perturbations to $\mathbf{C}_{bad}$ do not change the cost either, because $\mathbf{B}_{bad} = \mathbf{0}$ means that the internal state $\hat{\mathbf{x}}$ of the filter is always zero, which again implies ${\mathbf{z}{(t)}} \equiv 0$. Consequently, the gradient at $\mathsf{K}_{bad}$ is zero.

<!-- chunk {"id": "body-0051", "role": "body", "section": "Example 3.1", "weight": 1.0} -->

Suboptimality can be seen by noticing that $\mathsf{K}_{bad}$ cannot be transformed to the non-zero $\mathsf{K}_{\star}$ under any similarity transformation. The same is true for any OE instance: every filter with $\mathbf{B}_{bad} = \mathbf{0}$, $\mathbf{C}_{bad} = \mathbf{0}$, and $\mathbf{A}_{bad}$ being stable is a suboptimal stationary point of $\mathcal{L}_{\mathtt{O}\mathtt{E}}$. The existence of such suboptimal stationary points cautions against running simple gradient descent, and motivates our proposed regularization strategy.

<!-- chunk {"id": "body-0052", "role": "body", "section": "The perils of enforcing minimality", "weight": 1.0} -->

A filter $\mathsf{K}$ is *minimal* if $(\mathbf{A}_{\mathsf{K}},\mathbf{B}_{\mathsf{K}})$ is controllable, and $(\mathbf{A}_{\mathsf{K}},\mathbf{C}_{\mathsf{K}})$ is observable. Example 3.1 is the extreme case of a *non-minimal* filter, since $\mathbf{B}_{bad} = \mathbf{C}_{bad} = \mathbf{0}_{2}$. Conversely, as a special case of LQG, the OE problem inherits the property that all stationary points corresponding to *minimal* filters are globally optimal.

<!-- chunk {"id": "body-0053", "role": "body", "section": "The perils of enforcing minimality", "weight": 1.0} -->

Therefore, it may be natural to ask: *can a local search algorithm enforce minimality to avoid suboptimal stationary points?* A classical result due to Brockett suggests not: the set of minimal $n$-th order single-input-single-output transfer functions (e.g. filters) is the disjoint union of $n + 1$ open sets. Thus it is impossible for a continuous path to pass from one of these open sets to another without entering a region corresponding to a non-minimal filter, suggesting that a local search algorithm regularized to ensure minimality at every iteration may never converge to the optimal solution. See Section F.2 for further discussion and supporting numerical experiments.

<!-- chunk {"id": "body-0054", "role": "body", "section": "Suboptimal controllable stationary points", "weight": 1.0} -->

Given the drawbacks of enforcing minimality, one may wonder whether it is sufficient to enforce controllability alone. In Example 3.1 above - and indeed, for all the examples in Tang et al. of suboptimal stationary points in the LQG landscape - there is a loss of both observability ($\mathbf{C}_{bad} = \mathbf{0}$) and controllability ($\mathbf{B}_{bad} = \mathbf{0}$). Do suboptimal *controllable* stationary points exist?

<!-- chunk {"id": "body-0055", "role": "body", "section": "Example 3.2", "weight": 1.0} -->

Though $\mathsf{K}_{bad}$ in Eq. 3.2 is controllable, because $\mathbf{\Sigma}_{12,\mathsf{K}_{bad}}$ is rank deficient it corresponds to a suboptimal stationary point. This IR-PG circumvents such points by enforcing informativity ($\mathbf{\Sigma}_{12,\mathsf{K}}$ being full-rank) at all iterations, via the regularizer $\mathcal{R}_{\mathtt{i}\mathtt{n}\mathtt{f}\mathtt{o}}$.

<!-- chunk {"id": "body-0056", "role": "body", "section": "Difficulty of escaping suboptimal saddle points", "weight": 1.0} -->

The existence of suboptimal stationary points does not necessarily rule out the efficacy of gradient descent. Recent work has established that variations of gradient descent - e.g. with appropriate random perturbations or acceleration - efficiently escape strict saddle-points, i.e. points at which the minimum eigenvalue of the Hessian is strictly negative. In light of such results, it is reasonable to ask whether suboptimal stationary points of the kind identified in Example 3.2 are problematic for gradient descent. Specifically, are such stationary points strict saddles? It turns out that $\mathsf{K}_{bad}$ in Example 3.2 *does* correspond to a strict saddle point; however, the minimum eigenvalue of the Hessian can be made arbitrarily close to zero by making $\gamma$ sufficiently large. See Section F.3 for details.

<!-- chunk {"id": "body-0057", "role": "body", "section": "A provably convergent algorithm", "weight": 1.0} -->

The previous discussion puts us in a bind: we cannot regularize to preserve minimality because of path-disconnectedness. Yet, controllability is not enough to rule out suboptimal stationary points. The construction of Example 3.2 hinges on point (v): the cross covariance $\mathbf{\Sigma}_{12,\mathsf{K}_{bad}}$ between the true system state $\mathbf{x}{(t)}$ and internal policy state $\hat{\mathbf{x}}{(t)}$ is *rank deficient*. We call such filters *non-informative*.

<!-- chunk {"id": "body-0058", "role": "body", "section": "The explained covariance matrix", "weight": 1.0} -->

In light of Theorem 2, we design a policy search algorithm which ensures that $\mathbf{\Sigma}_{12,\mathsf{K}}$ remains full-rank throughout the search, but does so in a quantitative fashion.

<!-- chunk {"id": "body-0059", "role": "body", "section": "The explained covariance matrix", "weight": 1.0} -->

When $\mathsf{K} \in \mathcal{K}_{\mathtt{c}\mathtt{t}\mathtt{r}\mathtt{b}}$, $\mathbf{Z}_{\mathsf{K}}$ admits an elegant closed-form expression, which provides an alternative definition of $\mathcal{K}_{\mathtt{i}\mathtt{n}\mathtt{f}\mathtt{o}}$: Since $\mathbf{Z}_{\mathsf{K}}$ is invariant under similarity transformations, as per Eq. 2.3 ‣ 2 Preliminaries ‣ Globally Convergent Policy Search over Dynamic Filters for Output Estimation"), $\mathbf{Z}_{\mathsf{K}}$ can be interpreted as a normalized analogue of $\mathbf{\Sigma}_{12,\mathsf{K}}$.

<!-- chunk {"id": "body-0060", "role": "body", "section": "The explained covariance matrix", "weight": 1.0} -->

Informally, the quadratic form $v^{\top}\mathbf{Z}_{\mathsf{K}}v$ is a sufficient statistic for how much information $\hat{\mathbf{x}}{(t)}$ contains about the "$v$-direction" of $\mathbf{x}{(t)}$; see Section E.6 for a precise statement.

<!-- chunk {"id": "body-0061", "role": "body", "section": "Explained-covariance regularization", "weight": 1.0} -->

We preserve informativity by ensuring our iterates satisfy $\mathbf{Z}_{\mathsf{K}} \succ 0$. To this end, we run gradient descent on the regularized objective for some $\lambda > 0$: This choice of regularizer has several important properties. First, $\mathcal{R}_{\mathtt{i}\mathtt{n}\mathtt{f}\mathtt{o}}$ is always non-negative, and tends to $\infty$ as $\mathbf{Z}_{\mathsf{K}}$ approaches singularity. Furthermore, the value of the regularizer is invariant under similarity transformations(as per Eq. 2.3 ‣ 2 Preliminaries ‣ Globally Convergent Policy Search over Dynamic Filters for Output Estimation")). Next, many of the essential quantities arising in our analysis can be bounded in terms of $\mathbf{Z}_{\mathsf{K}}^{- 1}$, justifying $\mathbf{Z}_{\mathsf{K}}$ is a natural quantitative measure of informativity.

<!-- chunk {"id": "body-0062", "role": "body", "section": "Explained-covariance regularization", "weight": 1.0} -->

Lastly, the set of global-minimizers of $\mathcal{R}_{\mathtt{i}\mathtt{n}\mathtt{f}\mathtt{o}}{(\cdot)}$ are precisely the optimal filters for the OE problem, as per the following lemma (see Section E.3 for proof).

<!-- chunk {"id": "body-0063", "role": "body", "section": "Statement of IR-PG", "weight": 1.0} -->

We can now describe IR-PG, whose pseudocode is displayed in Algorithm 1. IR-PG applies gradient descent on the regularized $\mathcal{L}_{\mathtt{O}\mathtt{E}}$ objective, with an additional balancing step between gradient updates. Section B.1 provides a variant where the step size is chosen by backtracking line-search, which enjoys the same rigorous convergence guarantees.

<!-- chunk {"id": "body-0064", "role": "body", "section": "Statement of IR-PG", "weight": 1.0} -->

To guarantee convergence to an optimal filter (and finiteness of $\mathcal{L}_{\lambda}$), we need to initialize at a filter such that $\mathbf{Z}_{\mathsf{K}_{0}} \succ 0$, i.e. $\mathsf{K}_{0} \in \mathcal{K}_{\mathtt{i}\mathtt{n}\mathtt{f}\mathtt{o}}$. Fortunately, random initializations from a continuous distribution satisfy this condition with probability $1$ (see Section E.7 for a formal statement and proof).

<!-- chunk {"id": "body-0065", "role": "body", "section": "Formal guarantees", "weight": 1.0} -->

We conclude this section by stating the formal convergence guarantee for IR-PG. Our results depend on natural problem quantities, among which is the minimum singular value of $\mathbf{P}_{\star}$ (as defined in Eq. 2.4 ‣ 2 Preliminaries ‣ Globally Convergent Policy Search over Dynamic Filters for Output Estimation")), which we show is always strictly positive.

<!-- chunk {"id": "body-0066", "role": "body", "section": "Oracle complexity", "weight": 1.0} -->

The balancing step also requires only evaluation $\mathbf{\Sigma}_{\mathsf{K}}$, and can use an evaluation query called for the gradient. Lastly, the backtracking step requires an evaluation query for all $|\mathcal{S}_{bkt}|$ filters of the form ${\overset{\sim}{\mathsf{K}}}_{s} - {\eta\nabla_{s}}$. In total, therefore, each iteration uses $1$ call to ${\mathsf{o}\mathsf{r}\mathsf{a}\mathsf{c}}_{grad}$, and ${|\mathcal{S}_{bkt}|} + 2$ calls to ${\mathsf{o}\mathsf{r}\mathsf{a}\mathsf{c}}_{eval}$. We sketch the highlights of the proof in the following section, after introducing our DCL framework. A rigorous proof overview, with statements of the constituent results, is deferred to Section 6.2.

<!-- chunk {"id": "body-0067", "role": "body", "section": "Numerical Experiments", "weight": 1.0} -->

In this subsection we present the results of a number of additional numerical experiments illustrating the performance of IR-PG.

<!-- chunk {"id": "body-0068", "role": "body", "section": "Random generation of true systems", "weight": 1.0} -->

Each experimental trial begins with the random generation of a *true system* of the form Eq. 1.1. System parameters $\mathbf{A},\mathbf{C}$ are randomly generated using Matlab's rss function, with state dimension $n = 2$ and output dimension $m = 1$. The matrix $\mathbf{G}$ defining the mapping from state to performance output $\mathbf{z}$ is set to $\mathbf{G} = I$. The intensity of the system disturbances is randomly generated as $\mathbf{W}_{1} = {\mathbf{M}^{\top}\mathbf{M}}$ with each entry of $\mathbf{M} \in {\mathbb{R}}^{n \times n}$ sampled from $\mathcal{N}{}$. The intensity of the measurement noise is normalized to $\mathbf{W}_{2} = 1$.

<!-- chunk {"id": "body-0069", "role": "body", "section": "Random generation of true systems", "weight": 1.0} -->

To select suitable systems, we then reject samples according to the following criteria: (i) $\mathbf{A}$ must be strictly stable, and the observability Gramian $\mathcal{O}$ corresponding to $(\mathbf{A},\mathbf{C})$ must satisfy $10^{- 4} \leq {\lambda_{\min}{(\mathcal{O})}} \leq 10^{- 2}$; (ii) $\mathbf{W}_{1}$ must satisfy ${\lambda_{\max}{(\mathbf{W}_{1})}} \leq 5$; (iii) the optimal cost must satisfy ${\mathcal{L}_{\mathtt{O}\mathtt{E}}{(\mathsf{K}_{\star})}} \leq 10^{3}$.

<!-- chunk {"id": "body-0070", "role": "body", "section": "Random generation of true systems", "weight": 1.0} -->

The first criterion regulates the observability of the true system, which sets the difficulty of the filtering problem; the second ensures that the ratio between the disturbances and measurement noise remains "reasonable"; and the third ensures that the problem instance is not "pathological", as determined by excessively high cost of the optimal filter.

<!-- chunk {"id": "body-0071", "role": "body", "section": "Remark 4.1 (Choice of $\\mathbf{G} = \\mathbf{I}$)", "weight": 1.0} -->

As detailed in Section 3.2, IR-PG makes use of the regularizer $\mathcal{R}_{\mathtt{i}\mathtt{n}\mathtt{f}\mathtt{o}}$, defined in Eq. 3.3, the computation of which requires access to the true system states $\mathbf{x}$, as described in Section 2. To facilitate a more fair comparison with direct minimization of $\mathcal{L}_{\mathtt{O}\mathtt{E}}$, we selected $\mathbf{G} = \mathbf{I}$ to effectively give the optimizer of $\mathcal{L}_{\mathtt{O}\mathtt{E}}$ access to the true system states $\mathbf{x}$ as well. As a result, all algorithms compared in this section have access to the same information concerning the true system.

<!-- chunk {"id": "body-0072", "role": "body", "section": "Random generation of initial filters", "weight": 1.0} -->

Next we randomly generate a filter $\mathsf{K}_{0}$ from which to initialize gradient descent. To do so, we take the optimal (Kalman) filter $\mathsf{K}_{\star}$, and randomly perturb each of the parameters; specifically, we set ${(\mathsf{K}_{0})}_{i} = {{(\mathsf{K}_{\star})}_{i} + \delta_{i}}$ with $\delta_{i} \sim {\mathcal{N}{}}$ for the $i$th parameter.

<!-- chunk {"id": "body-0073", "role": "body", "section": "Random generation of initial filters", "weight": 1.0} -->

The first criterion ensures that we do not begin from an initial guess for which the informativity is too low, nor a guess for which it is too high (which makes the search easier). The second criterion ensures that the initial filter is sufficiently controllable, to avoid initializations that are too close to suboptimal stationary points. The final criterion ensures that the initial guess is, in all other ways, "reasonable", as measured by suboptimality.

<!-- chunk {"id": "body-0074", "role": "body", "section": "Optimization methods compared", "weight": 1.0} -->

Given a randomly generated true system, and random initial filter $\mathsf{K}_{0}$, we then apply the following three optimization algorithms: (i) gradient descent on $\mathcal{L}_{\mathtt{O}\mathtt{E}}{(\mathsf{K})}$; (ii) gradient descent on $\mathcal{L}_{\mathtt{O}\mathtt{E}}{(\mathsf{K})}$ with filter state normalization performed before each gradient step, cf. Eq. 3.4; (iii) IR-PG, as detailed in Algorithm 1, with regularization parameter $\lambda = 10^{- 4}$. See below for further discussion on the selection of $\lambda$. All methods are initialized from the same $\mathsf{K}_{0}$, and make use of the same backtracking line search to select step sizes. Moreover, all algorithms have the same termination criteria.

<!-- chunk {"id": "body-0075", "role": "body", "section": "Optimization methods compared", "weight": 1.0} -->

Each algorithm terminates when either: (i) the Frobenius norm of the gradient of the cost function being minimized (either $\mathcal{L}_{\mathtt{O}\mathtt{E}}$ or $\mathcal{L}_{\lambda}$) falls below a tolerance of $10^{- 8}$; (ii) the step size selected by the line search falls below a tolerance of $10^{- 16}$ for more than three consecutive iterations; or (iii) the number of iterations (gradient descent steps) exceeds $100,000$.

<!-- chunk {"id": "body-0076", "role": "body", "section": "Results", "weight": 1.0} -->

The results of 60 such experimental trials are depicted in Fig. 1. It is evident that simple "unregularized" gradient descent on $\mathcal{L}_{\mathtt{O}\mathtt{E}}$ routinely fails to converge to the global optimum, in the allotted number of iterations. In fact, the median (normalized) suboptimality gap $\frac{{\mathcal{L}_{\mathtt{O}\mathtt{E}}{(\mathsf{K})}} - {\mathcal{L}_{\mathtt{O}\mathtt{E}}{(\mathsf{K}_{\star})}}}{\mathcal{L}_{\mathtt{O}\mathtt{E}}{(\mathsf{K}_{\star})}}$ exceeds $10^{- 4}$, and only a single trial achieves suboptimality less than $10^{- 7}$.

<!-- chunk {"id": "body-0077", "role": "body", "section": "Results", "weight": 1.0} -->

Loss of informativity in these trials can be seen clearly in Fig. 2. The addition of the filter state reconditioning procedure of Eq. 3.4 offers only minimal improvement. In contrast, IR-PG converges reliably to high-quality solutions that are extremely close to the global optimum; the median normalized suboptimality gap was zero, to numerical precision. In fact, for one third of trials, the suboptimality gap was actually *negative* (by very small margins, e.g. $10^{- 17}$) indicating that IR-PG has reached the limits of numerical precision with which Matlab's icare solves Riccati equations (used to compute $\mathsf{K}_{\star}$).

<!-- chunk {"id": "body-0078", "role": "body", "section": "Results", "weight": 1.0} -->

(a) Normalized suboptimality at the termination of each algorithm.

<!-- chunk {"id": "body-0079", "role": "body", "section": "Results", "weight": 1.0} -->

(b) Normalized suboptimality as a function of iteration for each algorithm.

<!-- chunk {"id": "body-0080", "role": "body", "section": "Selection of regularization parameter $\\lambda$", "weight": 1.0} -->

Performance of IR-PG is in many instances insensitive to the value of $\lambda$ selected. However, we observed that a handful of experimental trails required $\lambda$ to be chosen more judiciously, in particular, when the spectral properties of $\nabla^{2}\mathcal{R}_{\mathtt{i}\mathtt{n}\mathtt{f}\mathtt{o}}$ differ significantly from those of $\nabla^{2}\mathcal{L}_{\mathtt{O}\mathtt{E}}$.

<!-- chunk {"id": "body-0081", "role": "body", "section": "Selection of regularization parameter $\\lambda$", "weight": 1.0} -->

Very small stepsizes may be required when $\lambda_{\max}{({\nabla^{2}\mathcal{R}_{\mathtt{i}\mathtt{n}\mathtt{f}\mathtt{o}}})}$ is very large, which means the search may make slow progress in updating $\mathbf{C}_{\mathsf{K}}$, as $\mathcal{R}_{\mathtt{i}\mathtt{n}\mathtt{f}\mathtt{o}}$ is independent of $\mathbf{C}_{\mathsf{K}}$. We have observed good performance in practice by simply "turning off" the regularizer (i.e. setting $\lambda = 0$) when the stepsize becomes excessively small (e.g. drops below $10^{- 16}$).

<!-- chunk {"id": "body-0082", "role": "body", "section": "Analysis Framework", "weight": 1.0} -->

This section introduces *differentiable convex liftings* (DCLs), a rigorous and flexible framework for operationalizing convex reformulations of nonconvex objectives.

<!-- chunk {"id": "body-0083", "role": "body", "section": "Gradient descent with DCLs", "weight": 1.0} -->

We now describe how DCLs yield quantitative convergence guarantees for gradient descent. A more general guarantee accommodating the reconditioning step in IR-PG is deferred to Section 5.2, and encompasses the bound below as a special case.

<!-- chunk {"id": "body-0084", "role": "body", "section": "Gradient descent with DCLs", "weight": 1.0} -->

To analyze gradient descent, we also require smoothness: we say $f$ is *$\beta$-upper-smooth* on $\mathcal{K}$ if $f \in {\mathcal{C}^{2}{(\mathcal{K})}}$ and for all ${\mathbf{x}} \in \mathcal{K}$, The following follows from a standard descent lemma for smooth (though possibly nonconvex) functions.

<!-- chunk {"id": "body-0085", "role": "body", "section": "Gradient descent with reconditioning", "weight": 1.0} -->

We now extend Proposition 5.1 to accommodate the reconditioning step in IR-PG (Algorithm 1). Here, we state guarantees which establish both quantitative convergence rates and, under slightly stronger conditions, path-connectedness to global minimizers. All proofs are deferred to Section H.3.

<!-- chunk {"id": "body-0086", "role": "body", "section": "for the regularized OE objective", "weight": 1.0} -->

While it is by now well-known within the controls community that the OE problem admits a convex reformulation, we prove a stronger result showing that this reformulation is in fact a DCL. We prove the following result in Section 6.4 ‣ 6 Proof of Theorems 3 and 2 ‣ Globally Convergent Policy Search over Dynamic Filters for Output Estimation").

<!-- chunk {"id": "body-0087", "role": "body", "section": "Smoothness and Lipschitzness of $\\mathcal{L}_{\\lambda}{(\\mathsf{K})}$", "weight": 1.0} -->

To verify these regularity conditions, we need to bound the norms of various quantities, which are themselves the solutions to Lyapunov equations involving the closed-loop system matrix $\mathbf{A}_{{cl},\mathsf{K}}$ (defined in Eq. 2.1 ‣ 2 Preliminaries ‣ Globally Convergent Policy Search over Dynamic Filters for Output Estimation")). The main step is therefore to show that the solutions to these Lyapunov equations are uniformly bounded, as per the following lemma (proof in Appendix J ‣ Part II Proofs for Convergence Guarantee ‣ Globally Convergent Policy Search over Dynamic Filters for Output Estimation")).

<!-- chunk {"id": "body-0088", "role": "body", "section": "Concluding the proof: uniform parameter bounds", "weight": 1.0} -->

Note again that bounds above are local, in that they depend on the choice of filter $\mathsf{K}$. To finish the proof of Theorem 3, we prove a uniform bound over all filters $\mathsf{K}$ which lie in the set considered by Proposition 5.3, namely.

<!-- chunk {"id": "body-0089", "role": "body", "section": "Concluding the proof: uniform parameter bounds", "weight": 1.0} -->

Immediately, we see that on this set ${\|\mathbf{\Sigma}_{22,\mathsf{K}}^{- 1}\|} \leq 2$, and that As a consequence, we can bound the terms appear in the bounds above as follows (see Section G.2):

<!-- chunk {"id": "body-0090", "role": "body", "section": "for Output Estimation (Proposition 6.1)", "weight": 1.0} -->

All proofs of the lemmas that follow are deferred to Appendix I ‣ Part II Proofs for Convergence Guarantee ‣ Globally Convergent Policy Search over Dynamic Filters for Output Estimation"). To proceed, we need to invoke Theorem 4 by specifying the DCL of the function Throughout, given a matrix $\mathbf{\Sigma} \succ 0$ partitioned in $2 \times 2$ blocks, we more generally define With the above notation, we can express This leads to the following notion of the lifted function.

<!-- chunk {"id": "body-0091", "role": "body", "section": "Step 3. Controlling the weak-PL constant", "weight": 1.0} -->

Lastly, we show that the DCL lends itself to a bounded PL constant by invoking Theorem 4. To do this, we need to show that the image of $\Phi{(\mathsf{K},\mathbf{\Sigma})}$ is not too large, and that ${\nabla\Phi}{( \cdot )}$ has rank at least $d_{\nu}$. We establish both in sequence. Let $\mathbf{U}_{\mathsf{K}}$ and $\mathbf{V}_{\mathsf{K}}$ be corresponding to Eq. 6.8b ‣ 6 Proof of Theorems 3 and 2 ‣ Globally Convergent Policy Search over Dynamic Filters for Output Estimation") with $\mathbf{\Sigma} = \mathbf{\Sigma}_{\mathsf{K}}$, i.e.

<!-- chunk {"id": "body-0092", "role": "body", "section": "Conclusion", "weight": 1.5} -->

The work introduces the first policy search algorithm which converges to the globally optimal *dynamic* filter for the output estimation problem. We hope that our analysis serves as a valuable starting point to study direct policy search for reinforcement learning and control problems with partial observations, in which the relevant class of policies are dynamic and maintain internal state. We also hope that both our proposed principle of informativity, and our technical contributions around convex reformulations, continue to prove useful in future work.
