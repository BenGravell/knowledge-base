## Introduction

The Linear Quadratic Regulator (LQG) is a cornerstone of control theory, and has been applied across several domains ranging from engineering, to economics, to computer science. It involves controlling a linear system subject to additive disturbances via the design of a control policy that minimizes a quadratic cost function. For linear systems, quadratic costs and additive Gaussian noise, it is well-known that the resulting optimal policy is linear in the observations. However, in practice, the system dynamics are often only approximately known, and the noise is not necessarily Gaussian. This leads to a mismatch between the nominal model and the true system, which can adversely affect performances \[(https://arxiv.org/html/2505.08370v2#bib.bib1)\].

We consider a generalization of the finite-horizon LQG framework for discrete-time linear stochastic systems subject to model mismatch. We interpret the problem as a zero-sum game between the controller and a distribution chosen from an ambiguity set that may change at each time step. Each ambiguity set is represented as a ball defined in the Kullback-Leibler (KL) divergence centered at a nominal Gaussian distribution. The goal of the control designer is then to synthesize a control policy that minimizes the worst-case expected cost. We refer to this problem as the Distributionally Robust LQG (DR-LQG) problem with KL ambiguity sets.

For the DR-LGQ problem, we show that, even under distributional ambiguity, the optimal control policy is linear in the observations, as in the standard LQG. Following \[(https://arxiv.org/html/2505.08370v2#bib.bib2), (https://arxiv.org/html/2505.08370v2#bib.bib3)\] we re-parametrize the control policy in terms of purified observations and propose a novel \"sandwich\" argument to show that the DR-LQG is optimally solved by a linear policy and that the worst-case distribution is still Gaussian. We show that the resulting game admits a Nash equilibrium and provide a numerical scheme based on regularized best response that converges linearly to the set of saddle points of the DR-LQG. The best responses admits closed-form expression, making the algorithm computationally attractive. We further consider the case of endogenous uncertainty captured via decision-dependent ambiguity sets, well suited to capture perturbations in the system matrices. We derive an approximated closed-form recursion based on dynamic programming, and use it within a coordinate gradient descent scheme to solve the problem with linear convergence rate guarantees. Finally, we provide numerical simulations to illustrate the effectiveness of our approaches.

### Literature review

Traditionally, the optimal control of systems subject to uncertainty has been studied through the LQR/LQG theory by synthesizing policies that either minimize a quadratic functional in the state and control action pair, or the $\mathcal{H}_{2}$ norm of the system's transfer function \[(https://arxiv.org/html/2505.08370v2#bib.bib4)\]. Motivated by the fragility of the LQG against model mismatch \[(https://arxiv.org/html/2505.08370v2#bib.bib1)\], several robustification approaches were suggested in the literature. For example, if the perturbation is modeled as adversarial with known finite energy bound, the $\mathcal{H}_{\infty}$ synthesis approach can be used to minimize the infinity norm of the transfer function mapping disturbances to a measurable performance metric \[(https://arxiv.org/html/2505.08370v2#bib.bib5)\]. While stability is guaranteed under any allowable process noise signal, the $\mathcal{H}_{\infty}$ controller might result in conservative behaviors as it plans for the worst uncertainty. This motivated the development of combined $\mathcal{H}_{2}/\mathcal{H}_{\infty}$ strategies, trying to alleviate part of the conservatism. A different approach is represented by risk-sensitive control that incorporates risk sensitivity into the control design task by minimizing the entropic risk measure of the cost, rather than its expected value \[(https://arxiv.org/html/2505.08370v2#bib.bib6), (https://arxiv.org/html/2505.08370v2#bib.bib7)\].

Distributional robust control (DRC) is an alternative paradigm that is gaining momentum \[(https://arxiv.org/html/2505.08370v2#bib.bib8), (https://arxiv.org/html/2505.08370v2#bib.bib9), (https://arxiv.org/html/2505.08370v2#bib.bib10), (https://arxiv.org/html/2505.08370v2#bib.bib11), (https://arxiv.org/html/2505.08370v2#bib.bib12), (https://arxiv.org/html/2505.08370v2#bib.bib13), (https://arxiv.org/html/2505.08370v2#bib.bib14), (https://arxiv.org/html/2505.08370v2#bib.bib15)\]. The DRC problem seeks a control policy that minimizes the expected cost under the worst-case noise distribution in an ambiguity set, i.e., a set of probability distributions among which we can reasonably expect to find the true noise distribution. DRC robustifies against model misspecifications in the space of probabilities. Different types of ambiguity sets have been proposed in the literature based on moment constraints \[(https://arxiv.org/html/2505.08370v2#bib.bib8)\], total variation distance \[(https://arxiv.org/html/2505.08370v2#bib.bib16)\], Wasserstein distance \[(https://arxiv.org/html/2505.08370v2#bib.bib11)\] (or, more broadly, optimal transport distances), and $\phi -$divergences \[(https://arxiv.org/html/2505.08370v2#bib.bib12)\].

In \[(https://arxiv.org/html/2505.08370v2#bib.bib2)\] a DR-LQG problem similar to the one considered here is solved by considering ambiguity sets defined on the basis of the Wasserstein distance. Compared to \[(https://arxiv.org/html/2505.08370v2#bib.bib2)\], (i) we motivate the choice of the KL distance by providing interesting connections with system identification and risk measure theory, (ii) we prove optimality of the linear policies for the DR-LQG problem with KL ambiguity sets, and (iii) we provide a novel best response algorithm that exploits the availability of closed-form expressions for the best responses, unlike the gradient-based method suggested in \[(https://arxiv.org/html/2505.08370v2#bib.bib2)\] that relies on automatic differentiation.

The dynamic-programming based recursion for decision-dependent ambiguity sets, is related to the approaches in \[(https://arxiv.org/html/2505.08370v2#bib.bib13)\] and \[(https://arxiv.org/html/2505.08370v2#bib.bib9)\]. These works address a regularized relaxed problem with a fixed penalty value in the objective function; hence, there are no guarantees that the worst-case distribution, against which the controller is hedging, belongs to the specified ambiguity set. On the contrary, our formulation addresses the exact constrained formulation. Additionally, in \[(https://arxiv.org/html/2505.08370v2#bib.bib13)\] and \[(https://arxiv.org/html/2505.08370v2#bib.bib9)\] distributed uncertainty modeling is not considered. Finally, in \[(https://arxiv.org/html/2505.08370v2#bib.bib13)\] and \[(https://arxiv.org/html/2505.08370v2#bib.bib9)\] the problem is solved by neglecting a crucial non-linear dependence in the optimality equations; we tackle this problem by linearizing this dependence (instead of disregarding it) with obvious advantages in terms of performances, as demonstrated in the numerical section.

### Outline

In Section II we present the necessary background, while in Section III we describe the problem statement. In Section IV the theoretical properties of the DR-LQG are analyzed and in Section V a computational framework is presented. Section VI considers the case with endogenous ambiguity sets, while in Section VII simulation results are reported. Finally, we draw our conclusions in Section VIII. We relegate all proofs to the appendix.

## Preliminaries

### Notation

${\mathbb{R}}^{n},{\mathbb{R}}_{+}^{n},{\mathbb{R}}_{+ +}^{n}$ denote the set of reals, nonnegative reals, and positive reals, respectively. ${\mathbb{S}}_{+}^{n}$ (resp. ${\mathbb{S}}_{+ +}^{n}$) denotes the cone of $n \times n$ symmetric positive semi-definite (resp. positive definite) matrices. For any ${A,B} \in {\mathbb{S}}_{+}^{n}$, the relation $A \succeq B$ ($A \succ B$) means that ${A - B} \in {\mathbb{S}}_{+}^{n}$(${A - B} \in {\mathbb{S}}_{+ +}^{n}$). Given a matrix $A$, $A^{\top}$ denotes its transpose and $|A|$ its determinant. All random object are defined on a probability space $(\Omega,\mathcal{F},{\mathbb{P}})$; thus, the distribution of a random vector $\xi:{\Omega\rightarrow{\mathbb{R}}^{n}}$ is given by the pushforward distribution ${\mathbb{P}}_{\xi} = {{\mathbb{P}} \circ \xi^{- 1}}$ of $\mathbb{P}$ with respect to $\xi$. We denote as $\mathcal{P}{({\mathbb{R}}^{n})}$ the set of absolutely continuous probability distributions on ${\mathbb{R}}^{n}$, and as $\mathcal{P}_{\mathcal{G}}{({\mathbb{R}}^{n})}$ its restriction to the set of Gaussians on ${\mathbb{R}}^{n}$. Finally, we denote as $\mathcal{N}{(\mu,\Sigma)}$ a Gaussian distribution with mean $\mu$ and covariance $\Sigma$.

### Relative entropy ambiguity sets

Given any two probability distributions ${{\mathbb{P}}_{1},{\mathbb{P}}_{2}} \in {\mathcal{P}{({\mathbb{R}}^{n})}}$, a KL-ambiguity set of radius $\rho > 0$ centered at ${\mathbb{P}}_{1}$ is

where $R{({\mathbb{P}}_{2}||{\mathbb{P}}_{1})}$ is the KL divergence from distribution ${\mathbb{P}}_{2}$ to the centre ${\mathbb{P}}_{1}$. For ${\mathbb{P}}_{1},{\mathbb{P}}_{2}$ admitting densities ${p_{1}{(x)}},{p_{2}{(x)}}$, respectively, then

We do not differentiate between ${\mathbb{P}}_{i}$ and its density $p_{i}{(x)}$ in the following, when clear from the context.

It is known that $R{({\mathbb{P}}_{2}||{\mathbb{P}}_{1})}$ is not a distance since it is not symmetric and does not obey the triangular inequality; however, it is a pseudo-distance since it satisfies (i) $R{({\mathbb{P}}_{2}||{\mathbb{P}}_{1})} \geq 0$ and (ii) $R{({\mathbb{P}}_{2}||{\mathbb{P}}_{1})} = 0$ if and only if ${\mathbb{P}}_{2} = {\mathbb{P}}_{1}$. Moreover, for a given ${\mathbb{P}}_{1}$, $R{({\mathbb{P}}_{2}||{\mathbb{P}}_{1})}$ is a strictly convex function of ${\mathbb{P}}_{2}$ on $\mathcal{P}{({\mathbb{R}}^{n})}$. When restricted to Gaussian distributions, the KL divergence admits a closed form expression \[(https://arxiv.org/html/2505.08370v2#bib.bib17)\]: For ${\mathbb{P}}_{1} \triangleq {\mathcal{N}{(\mu_{1},\Sigma_{1})}}$ and ${\mathbb{P}}_{2} \triangleq {\mathcal{N}{(\mu_{2},\Sigma_{2})}} \in {\mathcal{P}_{\mathcal{G}}{({\mathbb{R}}^{n})}}$, with ${\Sigma_{1},\Sigma_{2}} \succ 0$, it reads

### Convex optimization

Finally, we recall some results from convex optimization.

### Lemma 1 (Pointwise maximization \[[18](https://arxiv.org/html/2505.08370v2#bib.bib18)\], p. 81)

Let $X$ be a normed space and $\left. \{{h_{i}{(x)}} \middle| {i \in I}\} \right.$ be a collection of functions with the same domain $\mathcal{H}$. Assume that $\mathcal{H}$ is a convex subset of $X$ and that $h_{i}{(x)}$ is convex for each $i$. Then ${g{(x)}} ≔ {\sup_{i \in I}{h_{i}{(x)}}}$ is also convex.

### Lemma 2 (Partial minimization rule \[[18](https://arxiv.org/html/2505.08370v2#bib.bib18)\], p. 87)

Let $h{(x,y)}$ be jointly convex in $(x,y)$ and $K$ be a convex non-empty set. Then, the function ${g{(x)}} = {\inf_{y \in K}{h{(x,y)}}}$ is convex in $x.$

## Problem setup

Consider a discrete-time stochastic linear system

where ${x_{t} \in {\mathbb{R}}^{n}},{{u_{t} \in {\mathbb{R}}^{m}},{y_{t} \in {\mathbb{R}}^{p}}}$ are the system state, input and output, respectively, and ${A \in {\mathbb{R}}^{n \times n}},{{B \in {\mathbb{R}}^{n \times m}},{C \in {\mathbb{R}}^{p \times n}}}$ are the corresponding system matrices, that we assume to be time-invariant to streamline the presentation^11^1The theory remains valid in the case of time-dependant parameters.. The exogenous random vectors $x_{0}$, ${\{ w_{t}\}}_{t = 0}^{T - 1}$ and ${\{ v_{t}\}}_{t = 0}^{T - 1}$, corresponding to the initial condition and the process and measurement noises, are assumed to be mutually independent and follow probability distributions ${\mathbb{P}}_{x_{0}}$, $\left\{ {\mathbb{P}}_{w_{t}} \right\}_{t = 0}^{T - 1}$, and $\left\{ {\mathbb{P}}_{v_{t}} \right\}_{t = 0}^{T - 1}$, respectively. We assume without loss of generality that $\Omega = {{\mathbb{R}}^{n} \times {\mathbb{R}}^{nT} \times {\mathbb{R}}^{pT}}$ is the space of realizations of the exogenous uncertainties, $\mathcal{F}$ is the Borel $\sigma$-algebra on $\Omega$ and ${\mathbb{P}} = {\mathbb{P}}_{x_{0}} \times \left( \otimes_{t = 0}^{T - 1}{\mathbb{P}}_{w_{t}} \right) \otimes \left( \otimes_{t = 0}^{T}{\mathbb{P}}_{v_{t}} \right)$, where ${\mathbb{P}}_{1} \otimes {\mathbb{P}}_{2}$ denotes the independent coupling of the distributions ${\mathbb{P}}_{1}$ and ${\mathbb{P}}_{2}$. Further, for $t \geq 0$, let $\mathcal{F}_{t} = {\sigma{(y_{0:t})}}$ be the $\sigma$-algebra generated by all observations up to time $t$, and let $\mathcal{F}_{- 1}$ be the trivial $\sigma$-algebra. We restrict attention to inputs $u_{t}$ that are $\mathcal{F}_{t}$-measurable with respect to the observations up to time $t$ and assume that there exists a measurable function $\pi_{t}$ such that $u_{t} = {\pi_{t}{(y_{0:t})}}$. The control policy $\pi \triangleq {\{\pi_{t}\}}_{t = 0}^{T - 1} \in \mathcal{U}_{\mathbf{y}}$ is the collection of all such functions.

We depart from the standard LQG framework, and assume that $\mathbb{P}$ is unknown. Instead, one has only access to a nominal model $\hat{\mathbb{P}}$, for example retrieved via statistical analysis of expert knowledge, that is assumed to be of the form $\hat{\mathbb{P}} = {\hat{\mathbb{P}}}_{x_{0}} \otimes \left( \otimes_{t = 0}^{T - 1}{\hat{\mathbb{P}}}_{w_{t}} \right) \otimes \left( \otimes_{t = 0}^{T}{\hat{\mathbb{P}}}_{v_{t}} \right)$, where ${{\hat{\mathbb{P}}}_{x_{0}} \triangleq {\mathcal{N}{(0,{\hat{W}}_{- 1})}}},{{{\hat{\mathbb{P}}}_{w_{t}} \triangleq {\mathcal{N}{(0,{\hat{W}}_{t})}}},{{\hat{\mathbb{P}}}_{v_{t}} \triangleq {\mathcal{N}{(0,{\hat{V}}_{t})}}}}$ for ${{\hat{W}}_{t},{\hat{V}}_{t}} \succ 0$. For ${Q,Q_{T}} \in {\mathbb{S}}_{+}^{n}$ and $R \in {\mathbb{S}}_{+ +}^{m}$, our aim is to solve the following minimax problem:

where $\mathcal{B}$ is an ambiguity set is defined as

for user-defined ${\rho_{x_{0}},\rho_{w_{t}},\rho_{v_{t}}} \geq 0$. Note that by construction all exogenous random variables $x_{0},w_{0},\ldots,w_{T - 1},v_{0},\ldots,v_{T - 1}$ are mutually independent under every distribution in $\mathcal{B}$. The restriction to zero-mean distributions, both in the nominal and in the perturbed distributions, is done to simplify the presentation; the results can be extended to the case of non-zero mean distributions with minor modifications. Note also that the DR-LQG problem ((https://arxiv.org/html/2505.08370v2#S3.E4 "Equation 4 ‣ III Problem setup ‣ Distributionally Robust LQG with Kullback-Leibler Ambiguity Sets")) constitutes a zero-sum game between the control policy and a fictitious adversary that selects $\mathcal{B}$.

### III-A On the choice of the KL-divergence

We briefly review some benefits of the use of KL divergence to define ambiguity sets.

Connection with system identification. Consider the problem of estimating the parameters $\theta = {(A,B,C)}$ of a linear system of the form ((https://arxiv.org/html/2505.08370v2#S3.E3 "Equation 3 ‣ III Problem setup ‣ Distributionally Robust LQG with Kullback-Leibler Ambiguity Sets")) from noisy input-output data $\{{(u_{t},y_{t})}\}$. One of the most widely used paradigms to accomplish this task is maximum likelihood estimation (MLE), where the log-likelihood $\mathcal{L}{(\theta)}$ is maximized with respect to $\theta$. \[(https://arxiv.org/html/2505.08370v2#bib.bib19)\] provides an attractive interpretation of the MLE problem as the search for a model that minimizes the KL-divergence to the true system. Building on this interpretation, we can directly employ $\mathcal{L}{(\theta^{\star})}$ to provide a meaningful estimate of the size of the KL ambiguity sets.

Connection with risk measures. For $p \in {\lbrack 1,\infty)}$, let $\mathcal{L}_{p}{(\Omega,\mathcal{F},{\mathbb{P}})}$ be the space of random variables $\xi:{\Omega\rightarrow{\mathbb{R}}}$ with finite $p -$th moment with respect to the measure $\mathbb{P}$. Then, a risk measure $\rho{(\xi)}$ with $\rho:{{\mathcal{L}_{p}{(\Omega,\mathcal{F},{\mathbb{P}})}}\rightarrow{{\mathbb{R}} \cup {\{\infty\}}}}$ is a mapping that maps $\xi$ to the extended real line, quantifying its \"riskiness\". Originating in economics, risk measures are now popular in the control community to allow for a systematic approach to risk assessment (e.g., for safety-critical systems) \[(https://arxiv.org/html/2505.08370v2#bib.bib20)\]. Among them, the class of coherent risk measures is the most widespread thanks to their appealing properties \[(https://arxiv.org/html/2505.08370v2#bib.bib21), Chapter 6, p.231\]. Exploiting the Fenchel-Moreau theorem, it is possible to show that any coherent risk measure can be written as

where $\mathcal{A}$ is a set of probability density functions, and the measure $\mathbb{Q}$ is such that ${\mathbb{Q}}\operatorname{<<}{\mathbb{P}}$. This provides a clear connection with distributionally robust optimization with KL-based ambiguity sets.

### Example 1 (Conditional Value at Risk)

The CVaR of level $\beta \in {}$ can be described as in ((https://arxiv.org/html/2505.08370v2#S3.E6 "Equation 6 ‣ III-A On the choice of the KL-divergence ‣ III Problem setup ‣ Distributionally Robust LQG with Kullback-Leibler Ambiguity Sets")) with \[(https://arxiv.org/html/2505.08370v2#bib.bib21)\]

Let ${p{(x)}},{q{(x)}}$ be the densities of ${\mathbb{P}},{\mathbb{Q}}$. We have:

since ${\int{q{(x)}{dx}}} = 1$. Consider now the LQG functional in ((https://arxiv.org/html/2505.08370v2#S3.E4 "Equation 4 ‣ III Problem setup ‣ Distributionally Robust LQG with Kullback-Leibler Ambiguity Sets")), and assume that instead of the expectation we want to consider the CVaR as we are interested in accounting for the tail-risk. Then, the cost functional becomes

where for the second line we borrow the stacked notation from the upcoming Section [IV](https://arxiv.org/html/2505.08370v2#S4 "IV Theoretical analysis of the DR-LQG ‣ Distributionally Robust LQG with Kullback-Leibler Ambiguity Sets"), and the system evolves as in ((https://arxiv.org/html/2505.08370v2#S3.E3 "Equation 3 ‣ III Problem setup ‣ Distributionally Robust LQG with Kullback-Leibler Ambiguity Sets")). For $\xi = {{\mathbf{u}^{\top}{\mathbf{R}\mathbf{u}}} + {\mathbf{x}^{\top}{\mathbf{Q}\mathbf{x}}}}$, we then conclude that $\sup_{{\mathbb{Q}} \in \mathcal{B}_{\rho}}{{\mathbb{E}}_{\mathbb{Q}}{\lbrack\xi\rbrack}}$, with $\rho = {\log\left( \frac{1}{\beta} \right)}$, represents a conservative approximation of ((https://arxiv.org/html/2505.08370v2#S3.E7 "Equation 7 ‣ Example 1 (Conditional Value at Risk). ‣ III-A On the choice of the KL-divergence ‣ III Problem setup ‣ Distributionally Robust LQG with Kullback-Leibler Ambiguity Sets")). While solving ((https://arxiv.org/html/2505.08370v2#S3.E7 "Equation 7 ‣ Example 1 (Conditional Value at Risk). ‣ III-A On the choice of the KL-divergence ‣ III Problem setup ‣ Distributionally Robust LQG with Kullback-Leibler Ambiguity Sets")) is challenging \[(https://arxiv.org/html/2505.08370v2#bib.bib22)\], we will show that ((https://arxiv.org/html/2505.08370v2#S3.E4 "Equation 4 ‣ III Problem setup ‣ Distributionally Robust LQG with Kullback-Leibler Ambiguity Sets")) can be solved effectively, thus paving the way for novel risk-aware formulations as \[(https://arxiv.org/html/2505.08370v2#bib.bib23)\]. $\bigtriangleup$

## Theoretical analysis of the DR-LQG

### IV-A Problem re-parametrization

As pointed out in \[(https://arxiv.org/html/2505.08370v2#bib.bib2)\], in the LQG formulation the inputs are subject to a cyclic dependence, which makes the analysis of ((https://arxiv.org/html/2505.08370v2#S3.E4 "Equation 4 ‣ III Problem setup ‣ Distributionally Robust LQG with Kullback-Leibler Ambiguity Sets")) hard. To break this dependency, we proceed as in \[(https://arxiv.org/html/2505.08370v2#bib.bib2)\] and introduce a \"fictitious\" noise-free system

with states ${\hat{x}}_{t} \in {\mathbb{R}}^{n}$ and outputs ${\hat{y}}_{t} \in {\mathbb{R}}^{p}$, initialized with ${\hat{x}}_{0} = 0$ and subject to the same inputs $u_{t}$ as the original system ((https://arxiv.org/html/2505.08370v2#S3.E3 "Equation 3 ‣ III Problem setup ‣ Distributionally Robust LQG with Kullback-Leibler Ambiguity Sets")). We define the purified observation at time $t$ as $\eta_{t} = {y_{t} - {\hat{y}}_{t}}$ and use ${\mathbf{η}} = \left( \eta_{0},\ldots,\eta_{T - 1} \right)$ to denote the sequence of purified observations. Note that since the inputs $u_{t}$ are causal, we can compute ${\hat{x}}_{t}$ and ${\hat{y}}_{t}$ from $y_{0},\ldots,y_{t}$. Thus, $\eta_{t}$ can be represented as a function of $y_{0},\ldots,y_{t}$. Conversely, $y_{t}$ can also be represented as a function of $\eta_{0},\ldots,\eta_{t}$. Moreover, any measurable function of $y_{0},\ldots,y_{t}$ can be expressed as a measurable function of $\eta_{0},\ldots,\eta_{t}$ and viceversa \[(https://arxiv.org/html/2505.08370v2#bib.bib24), Proposition II.1\]. Let $\mathcal{U}_{\mathbf{η}}$ be the sequence of control inputs $\mathbf{u} = \left( u_{0},u_{1},\ldots,u_{T - 1} \right)$ so that $u_{t} = {{\overset{\sim}{\pi}}_{t}\left( \eta_{0},\ldots,\eta_{t} \right)}$ for some measurable function ${\overset{\sim}{\pi}}_{t}:{{\mathbb{R}}^{p{({t + 1})}}\rightarrow{\mathbb{R}}^{m}}$ for every $t = {\{ 0,\ldots,{T - 1}\}}$. Then, \[(https://arxiv.org/html/2505.08370v2#bib.bib24), Proposition II.1\] implies that $\mathcal{U}_{\mathbf{η}} = \mathcal{U}_{\mathbf{y}}$.

Let ${\mathbf{Q} \in {\mathbb{S}}^{n{({T + 1})}}},{{\mathbf{R} \in {\mathbb{S}}^{mT}},{{\mathbf{C} \in {\mathbb{R}}^{{{pT} \times n}{({T + 1})}}},{\mathbf{G} \in {\mathbb{R}}^{{{n{({T + 1})}} \times n}{({T + 1})}}}}}$ and $\mathbf{H} \in {\mathbb{R}}^{{{n{({T + 1})}} \times m}T}$ be block matrices as defined in the Appendix A. Further, let ${\mathbf{x} = {(x_{0},\ldots,x_{T})}},{{\mathbf{u} = {(u_{0},\ldots,u_{T - 1})}},{{\mathbf{y} = {(y_{0},\ldots,y_{T - 1})}},{{\mathbf{w} = {(x_{0},w_{0},\ldots,w_{T - 1})}},{\mathbf{v} = {(v_{0},\ldots,v_{T - 1})}}}}}$. Using the stacked system matrices, we can now express the purified observation process $\eta$ as a linear function of the exogenous uncertainties $w$ and $v$. Specifically, one can easily verify that ${\mathbf{η}} = {{\mathbf{D}\mathbf{w}} + \mathbf{v}}$, where $\mathbf{D} = {\mathbf{C}\mathbf{G}}$. Note that the purified observations are independent of the inputs, hence breaking the initial cyclic dependence. In view of this re-parametrization, ((https://arxiv.org/html/2505.08370v2#S3.E4 "Equation 4 ‣ III Problem setup ‣ Distributionally Robust LQG with Kullback-Leibler Ambiguity Sets")) is equivalent to

In the remainder, we will then focus without loss of generality on the re-parametrized problem $(P)$.

### IV-B Analysis of the upper bound

Consider the following problem

where $\overset{\sim}{\mathcal{B}}$ is an ambiguity set (to be defined next) such that $\mathcal{B} \subseteq \overset{\sim}{\mathcal{B}}$, and $\mathcal{U}_{\mathbf{η}}^{\text{lin}}$ denotes the class of affine policies of the form $\mathbf{u} = {{\mathbf{U}{\mathbf{η}}} + \mathbf{q}}$ with $\mathbf{U} \in {\mathbb{R}}^{{{mT} \times p}T}$ being block lower triangular to enforce causality and $\mathbf{q} \in {\mathbb{R}}^{mT}$. Clearly, $(U)$ is an upper bound to $(P)$ since we are simultaneously restricting the feasible space of the controller, while enlarging the one of the adversary. We begin by defining $\overset{\sim}{\mathcal{B}}$.

### Proposition 3

Consider an arbitrary zero-mean distribution ${\mathbb{P}} \in {\mathcal{P}{({\mathbb{R}}^{n})}}$ with covariance $\Sigma_{p}$ and a Gaussian distribution ${\mathbb{Q}} \triangleq {\mathcal{N}{(0,\Sigma_{q})}} \in {\mathcal{P}_{\mathcal{G}}{({\mathbb{R}}^{n})}}$. Then,

The bound in Proposition (https://arxiv.org/html/2505.08370v2#Thmtheorem3 "Proposition 3. ‣ IV-B Analysis of the upper bound ‣ IV Theoretical analysis of the DR-LQG ‣ Distributionally Robust LQG with Kullback-Leibler Ambiguity Sets") depends only on the covariance matrices $\Sigma_{p}$ and $\Sigma_{q}$, making it analogous to the Gelbrich bound for the type-2 Wasserstein distance. Further, the derivation can be easily extended to the case of non-zero mean distributions, since the differential entropy is translation invariant. Consider the setting of Proposition (https://arxiv.org/html/2505.08370v2#Thmtheorem3 "Proposition 3. ‣ IV-B Analysis of the upper bound ‣ IV Theoretical analysis of the DR-LQG ‣ Distributionally Robust LQG with Kullback-Leibler Ambiguity Sets") and let $\mathcal{B} = {\{{\mathbb{P}}:{{R{({{\mathbb{P}} \parallel {\mathbb{Q}}})}} \leq \rho}\}}$ and $\overset{\sim}{\mathcal{B}} = {\{{\mathbb{P}}:{{\frac{1}{2}\left( {{{\text{Tr}{({\Sigma_{q}^{- 1}\Sigma_{p}})}} - n} + {\log\frac{\det\Sigma_{q}}{\det\Sigma_{p}}}} \right)} \leq \rho}\}}$. It immediately follows

Next, we turn our attention to the minimization problem. By the definition of $\mathbf{η}$ and the restriction to linear policies,

Taking the expectation of the quadratic form and by definition of $\overset{\sim}{\mathcal{B}}$, the upper bound $(U)$ becomes^22^2To simplify the notation, we shift the index $i$ of $W_{i}$ by one.

### IV-C Analysis of the lower bound

Consider now the problem

where $\mathcal{G}$ is defined as

Note that $\mathcal{G}$ only contains Gaussian distributions, hence $\mathcal{G} \subseteq \mathcal{B}$ and $(L)$ is a lower bound for $(P)$. Moreover, notice that for any ${\mathbb{P}} \in \mathcal{G}$, from classical LQG theory, the optimal policy is affine in the observations so we can rewrite $(L)$ as

Invoking ((https://arxiv.org/html/2505.08370v2#S2.E2 "Equation 2 ‣ Relative entropy ambiguity sets ‣ II Preliminaries ‣ Distributionally Robust LQG with Kullback-Leibler Ambiguity Sets")), the lower bound $(L)$ becomes

### IV-D Optimality of linear policies

The analysis of the upper and lower bounds culminates with the following result, which represents our first contribution.

### Theorem 4

Problem (P) is solved by an affine policy $\mathbf{u}^{\star} = {{\mathbf{U}^{\star}\mathbf{y}} + \mathbf{q}^{\star}}$ and a Gaussian distribution ${\mathbb{P}}^{\star} \in \mathcal{G}$.

Theorem (https://arxiv.org/html/2505.08370v2#Thmtheorem4 "Theorem 4. ‣ IV-D Optimality of linear policies ‣ IV Theoretical analysis of the DR-LQG ‣ Distributionally Robust LQG with Kullback-Leibler Ambiguity Sets") establishes that the optimal policy for the DR-LQG problem is linear in the observations, as in the standard LQG setting. Moreover, the worst-case distribution is still a Gaussian distribution even though the ambiguity set $\mathcal{B}$ contains different types of distributions.

## Computational framework for the DR-LQG

In search of methods for computing the optimal $u^{\star}$ and ${\mathbb{P}}^{\star}$, we start by showing that problem $(L)$ admits a Nash equilibrium. Then we devise a best response algorithm that provably converges to te set of saddle points of ((https://arxiv.org/html/2505.08370v2#S4.E15 "Equation 15 ‣ IV-C Analysis of the lower bound ‣ IV Theoretical analysis of the DR-LQG ‣ Distributionally Robust LQG with Kullback-Leibler Ambiguity Sets")). Note that from the structure of (U) and (L), we directly infer that $\mathbf{q}^{\star} = \mathbf{0}$ when the nominal distribution is zero-mean. To simplify the results presentation, we will drop $\mathbf{q}$ in the remainder. All our results can be easily extended to the case of non-zero mean distributions, e.g., $\mathbf{q}^{\star} \neq \mathbf{0}$ with minor modifications.

### V-A Existence of a Nash equilibrium

Consider problem ((https://arxiv.org/html/2505.08370v2#S4.E15 "Equation 15 ‣ IV-C Analysis of the lower bound ‣ IV Theoretical analysis of the DR-LQG ‣ Distributionally Robust LQG with Kullback-Leibler Ambiguity Sets")) and its dual

The next result shows that strong duality among the two problems holds.

### Proposition 5

Problem ((https://arxiv.org/html/2505.08370v2#S5.E16 "Equation 16 ‣ V-A Existence of a Nash equilibrium ‣ V Computational framework for the DR-LQG ‣ Distributionally Robust LQG with Kullback-Leibler Ambiguity Sets")) is a strong dual for ((https://arxiv.org/html/2505.08370v2#S4.E15 "Equation 15 ‣ IV-C Analysis of the lower bound ‣ IV Theoretical analysis of the DR-LQG ‣ Distributionally Robust LQG with Kullback-Leibler Ambiguity Sets")).

As a consequence of Proposition (https://arxiv.org/html/2505.08370v2#Thmtheorem5 "Proposition 5. ‣ V-A Existence of a Nash equilibrium ‣ V Computational framework for the DR-LQG ‣ Distributionally Robust LQG with Kullback-Leibler Ambiguity Sets"), ((https://arxiv.org/html/2505.08370v2#S4.E13 "Equation 13 ‣ IV-B Analysis of the upper bound ‣ IV Theoretical analysis of the DR-LQG ‣ Distributionally Robust LQG with Kullback-Leibler Ambiguity Sets")) admits a saddle point $(\mathbf{u}^{\star},{\mathbb{P}}^{\star})$.

### V-B Regularized best response scheme

Let $\mathbf{\Sigma} = {\text{diag}{(\mathbf{W},\mathbf{V})}}$ and ${\mathbf{F}{(\mathbf{U})}} = {\text{diag}{({\mathbf{F}_{1}{(\mathbf{U})}},{\mathbf{F}_{2}{(\mathbf{U})}})}}$, where we stress the dependence of $F$ from $\mathbf{U}$. Further, let ${\mathcal{J}{(\mathbf{U},\mathbf{\Sigma})}}:={\text{Tr}\left( {\mathbf{F}{(\mathbf{U})}\mathbf{\Sigma}} \right)}$ be the \"payoff\" function of the zero-sum game described by ((https://arxiv.org/html/2505.08370v2#S4.E15 "Equation 15 ‣ IV-C Analysis of the lower bound ‣ IV Theoretical analysis of the DR-LQG ‣ Distributionally Robust LQG with Kullback-Leibler Ambiguity Sets")) and set

Since $\mathcal{J}$ is convex in $\mathbf{U}$ and concave in $\mathbf{\Sigma}$, by Berge's Maximum theorem $\mathcal{A}$ is convex and continuous in $\mathbf{U}$ and $\mathcal{C}$ is concave and continuous in $\mathbf{\Sigma}$. Additionally, one has ${\mathcal{C}{(\mathbf{\Sigma})}} \leq {\mathcal{J}{(\mathbf{U},\mathbf{\Sigma})}} \leq {\mathcal{A}{(\mathbf{U})}}$, hence

be the residual duality gap. Then: $\Phi:{{{\mathbb{R}}^{{{mT} \times p}T} \times \mathcal{G}}\rightarrow{\mathbb{R}}}$ is continuous, jointly convex and nonnegative, and its minimum ${\overline{\mathcal{V}} - \underset{¯}{\mathcal{V}}} \geq 0$ is reached in ${\mathbb{R}}^{{{mT} \times p}T} \times \mathcal{G}$. If the minimum is 0, then the zero-sum game is said to have a value $\mathcal{V} = \overline{\mathcal{V}} = \underset{¯}{\mathcal{V}}$. More precisely, ${\Phi{(\mathbf{U},\mathbf{\Sigma})}} = 0$ if and only if ${\mathcal{A}{(\mathbf{U})}} = {\mathcal{C}{(\mathbf{\Sigma})}}$, or equivalently, $(\mathbf{U},\mathbf{\Sigma})$ is a saddle point of the game.

Let us introduce the best response (BR) correspondences

$\text{BR}_{1}{(\mathbf{\Sigma})}$ $\in {\text{argmin}_{\mathbf{U}}\mathcal{J}{(\mathbf{U},\mathbf{\Sigma})}}$ (18a)
$\text{BR}_{2}{(\mathbf{U})}$ ${\in {\text{argmax}_{\mathbf{\Sigma} \in \mathcal{G}}\mathcal{J}{(\mathbf{U},\mathbf{\Sigma})}}}.$ (18b)

Before proceeding, we show that ([18a](https://arxiv.org/html/2505.08370v2#S5.E18.1 "Equation 18a ‣ Equation 18 ‣ V-B Regularized best response scheme ‣ V Computational framework for the DR-LQG ‣ Distributionally Robust LQG with Kullback-Leibler Ambiguity Sets")) is equivalently obtained by restricting $\mathbf{U}$ to live in a compact set $\mathcal{S} \subseteq {\mathbb{R}}^{{{mT} \times p}T}$.

### Lemma 6

There exists a compact and convex set $\mathcal{S} \subseteq {\mathbb{R}}^{{{mT} \times p}T}$ independent of $\mathbf{\Sigma}$ such that ${\text{BR}_{1}{(\mathbf{\Sigma})}} = {\text{argmin}_{\mathbf{U} \in \mathcal{S}}\mathcal{J}{(\mathbf{U},\mathbf{\Sigma})}}$ for all $\mathbf{\Sigma} \in \mathcal{G}$.

Since $\mathcal{J}{(\mathbf{U},\mathbf{\Sigma})}$ is continuous in both arguments, Maximum theorem implies that $\text{BR}_{1},\text{BR}_{2}$ are upper semi-continuous correspondences from $\mathcal{G}$ to $\mathcal{S}$ and from $\mathcal{S}$ to $\mathcal{G}$ respectively, with nonempty closed convex values. Consider the continuous-time best response dynamics on $\mathcal{S} \times \mathcal{G}$:

$\overset{˙}{\mathbf{U}}{(\lambda)}$ $\in {{\text{BR}_{2}{({\mathbf{\Sigma}{(\lambda)}})}} - {\mathbf{U}{(\lambda)}}}$ (19a)
$\overset{˙}{\mathbf{\Sigma}}{(\lambda)}$ ${\in {{\text{BR}_{1}{({\mathbf{U}{(\lambda)}})}} - {\mathbf{\Sigma}{(\lambda)}}}}.$ (19b)

We can interpret ((https://arxiv.org/html/2505.08370v2#S5.E19 "Equation 19 ‣ V-B Regularized best response scheme ‣ V Computational framework for the DR-LQG ‣ Distributionally Robust LQG with Kullback-Leibler Ambiguity Sets")) as a regularized best response scheme, where the regularization, given by the negative of the best response of the corresponding player, is added to dampen oscillations and promote convergence. Denote ${v{(\lambda)}} = {\Phi{({\mathbf{U}{(\lambda)}},{\mathbf{\Sigma}{(\lambda)}})}}$. We have the following result.

### Theorem 7

The following facts holds:

((https://arxiv.org/html/2505.08370v2#S5.E19 "Equation 19 ‣ V-B Regularized best response scheme ‣ V Computational framework for the DR-LQG ‣ Distributionally Robust LQG with Kullback-Leibler Ambiguity Sets")) has a solution for every initial condition ${({\mathbf{U}{}},{\mathbf{\Sigma}{}})} \in {\mathcal{S} \times \mathcal{G}}$.

Along every solution of ((https://arxiv.org/html/2505.08370v2#S5.E19 "Equation 19 ‣ V-B Regularized best response scheme ‣ V Computational framework for the DR-LQG ‣ Distributionally Robust LQG with Kullback-Leibler Ambiguity Sets")), $v{(\lambda)}$ is a Lyapunov function with ${{\overset{˙}{v}{(\lambda)}} \leq {{- {v{(\lambda)}}}\quad{\text{for almost all~}\lambda}}},$ hence

Thus, the zero-game has a value and every solution of ((https://arxiv.org/html/2505.08370v2#S5.E19 "Equation 19 ‣ V-B Regularized best response scheme ‣ V Computational framework for the DR-LQG ‣ Distributionally Robust LQG with Kullback-Leibler Ambiguity Sets")) converges to the non-empty set of saddle points, which is a uniform global attractor for ((https://arxiv.org/html/2505.08370v2#S5.E19 "Equation 19 ‣ V-B Regularized best response scheme ‣ V Computational framework for the DR-LQG ‣ Distributionally Robust LQG with Kullback-Leibler Ambiguity Sets")).

Theorem (https://arxiv.org/html/2505.08370v2#Thmtheorem7 "Theorem 7. ‣ V-B Regularized best response scheme ‣ V Computational framework for the DR-LQG ‣ Distributionally Robust LQG with Kullback-Leibler Ambiguity Sets") establishes that the (regularized) best response scheme in ((https://arxiv.org/html/2505.08370v2#S5.E19 "Equation 19 ‣ V-B Regularized best response scheme ‣ V Computational framework for the DR-LQG ‣ Distributionally Robust LQG with Kullback-Leibler Ambiguity Sets")) converges at an exponential rate to the set of saddle points of the DR-LQG problem.

Moreover, we notice that both best responses admits a computationally cheap solution, making our scheme attractive from a computational point of view. Namely, the best response of the minimizing player can be solved via a closed-form dynamic programming recursion coupled with a Kalman filter, as in standard LQG. In turn, we show the best response of the maximizing player can be decomposed as a sum of ${2T} + 1$ independent convex optimization problems in a single scalar variable $\tau_{i} \in {\mathbb{R}}_{+}$ each of the form

where $\mathbf{F}_{i}$ is the $i$-th digoanl block of $\mathbf{F}{(\mathbf{U})}$ and ${\hat{\mathbf{\Sigma}}}_{i}$ the $i$-th diagonal block of $\hat{\mathbf{\Sigma}} = {\text{diag}{({\hat{W}}_{0},\ldots,{\hat{W}}_{T},{\hat{V}}_{0},\ldots,{\hat{V}}_{T - 1})}}$.

We show that ((https://arxiv.org/html/2505.08370v2#S5.E21 "Equation 21 ‣ V-B Regularized best response scheme ‣ V Computational framework for the DR-LQG ‣ Distributionally Robust LQG with Kullback-Leibler Ambiguity Sets")) admits a closed-form solution. Exploiting Lemma (https://arxiv.org/html/2505.08370v2# "Lemma 12. ‣ Appendix B: Auxiliary results ‣ Distributionally Robust LQG with Kullback-Leibler Ambiguity Sets") since each ${\mathbf{F}_{i}{(\mathbf{U})}} \in {\mathbb{S}}_{+}^{n}$ for any $\mathbf{U}$, the maximizer of ((https://arxiv.org/html/2505.08370v2#S5.E21 "Equation 21 ‣ V-B Regularized best response scheme ‣ V Computational framework for the DR-LQG ‣ Distributionally Robust LQG with Kullback-Leibler Ambiguity Sets")) is given by

where by Lagrange duality $\tau_{i}^{\star}$ is chosen such that complementarity slackness holds, i.e.,

Note that ((https://arxiv.org/html/2505.08370v2#S5.E22 "Equation 22 ‣ V-B Regularized best response scheme ‣ V Computational framework for the DR-LQG ‣ Distributionally Robust LQG with Kullback-Leibler Ambiguity Sets")) represents an algebraic equation in the scalar variable $\tau_{i} \in {\mathbb{R}}_{+}$. In practice, it can be efficiently solved by bisection to any desired tolerance.

## DR-LQG with endogenous ambiguity sets

The problem formulation considered up to here assumes exogenous disturbances resulting in ambiguity sets that are defined a priori, i.e., before the control task, and are not influenced by the controller's actions. In this section, we extend the results to the case where the ambiguity sets are endogenously determined by the controller's actions.

Consider the standard Linear Fractional Transformation (LFT) model in Fig. (https://arxiv.org/html/2505.08370v2#S6.F1 "Figure 1 ‣ VI DR-LQG with endogenous ambiguity sets ‣ Distributionally Robust LQG with Kullback-Leibler Ambiguity Sets"): the source of uncertainty in the system dynamics, represented by the uncertainty operator $\Delta$ that is assumed to be unknown but of bounded magnitude, might depend on the system states and inputs. Consequently, to adequately represent the distributional ambiguity affecting the system, we shall resort to a state and decision-dependent ambiguity set of the form

for a nominal Gaussian distribution ${\mathbb{Q}}_{t}$, with $z_{t} = {{E_{1}x_{t}} + {E_{2}u_{t}}}$ where $E_{1} \in {\mathbb{R}}^{q \times n}$ and ${E_{2} \in {\mathbb{R}}^{q \times m}}.$ For simplicity, we assume that ${{E_{1}^{\top}E_{2}} = 0}.$

Figure 1: LFT uncertain model. It separates the nominal dynamics from the uncertainty, represented by the operator Δ in a feedback interconnection. By suitably selecting the admissible structure and magnitude of Δ, the LFT model can represent various sources of uncertainty.

While the theoretical analysis of Section IV carries over, the convergence of the best response dynamics in ((https://arxiv.org/html/2505.08370v2#S5.E19 "Equation 19 ‣ V-B Regularized best response scheme ‣ V Computational framework for the DR-LQG ‣ Distributionally Robust LQG with Kullback-Leibler Ambiguity Sets")) is no longer guaranteed, since the endogenous disturbance introduces a coupling among the feasible sets of the players. Thus, Theorem (https://arxiv.org/html/2505.08370v2#Thmtheorem7 "Theorem 7. ‣ V-B Regularized best response scheme ‣ V Computational framework for the DR-LQG ‣ Distributionally Robust LQG with Kullback-Leibler Ambiguity Sets") does no longer necessarily hold.

To overcome this issue, we devise a different approximated scheme that retain convergence guarantees despite the additional complexity introduced by the endogenous ambiguity sets. Differently from the previous sections, this approximated scheme is grounded on standard tools from dynamic programming. In this sense, the approach used here is therefore more closely related to \[(https://arxiv.org/html/2505.08370v2#bib.bib12), (https://arxiv.org/html/2505.08370v2#bib.bib9), (https://arxiv.org/html/2505.08370v2#bib.bib13), (https://arxiv.org/html/2505.08370v2#bib.bib25), (https://arxiv.org/html/2505.08370v2#bib.bib15)\].

### VI-A Relaxed problem

To simplify the derivation, in this section we only consider distributional ambiguity on the process noise $w_{t}$, while ${\mathbb{P}}_{x_{0}},{\mathbb{P}}_{v_{t}}$ are assumed to be known and equal to the their nominal distributions, i.e., we set ${\rho_{x_{0}} = \rho_{v_{t}} = 0},{\forall t}$. Let us denote the information collected up to time $t$ as

with $I_{0} = y_{0}$, and we call it the information vector. When a new control action is computed, the information vector is updated as ${I_{t + 1} = {(I_{t},y_{t + 1},u_{t})}}.$ It is well-known in stochastic optimal control theory that $I_{t}$ serves as sufficient statistics. Thus, the policies of the two players can be writtem as $u_{t} = {\pi_{t}{(I_{t})}}$ and, similarly, ${{\mathbb{P}}_{w_{t}} = {\gamma_{t}{(I_{t})}}},$ where $\gamma_{t}$ is a measurable function that maps the information vector $I_{t}$ to a distribution ${\mathbb{P}}_{w_{t}}$ in $\mathcal{B}_{t}{(x_{t},u_{t})}$.

Let $\Sigma_{t}:={{\mathbb{E}}_{{\mathbb{P}}_{w_{t}}}\left\lbrack {\left( {x_{t} - {{\mathbb{E}}_{{\mathbb{P}}_{w_{t}}}{\lbrack\left. x_{t} \middle| I_{t} \right.\rbrack}}} \right)^{\top}{({x_{t} - {{\mathbb{E}}_{{\mathbb{P}}_{w_{t}}}{\lbrack\left. x_{t} \middle| I_{t} \right.\rbrack}}})}} \middle| I_{t} \right\rbrack}$ be the prediction error covariance matrix of the state $x_{t}$ assuming that system ((https://arxiv.org/html/2505.08370v2#S3.E3 "Equation 3 ‣ III Problem setup ‣ Distributionally Robust LQG with Kullback-Leibler Ambiguity Sets")) evolves according to the distribution ${\mathbb{P}}_{w_{t}}$ selected by the adversary. Similarly, we denote ${\hat{\Sigma}}_{t}$ the corresponding nominal quantity, i.e., computed with respect to the nominal distribution ${\hat{\mathbb{P}}}_{w_{t}}$. Consequently the DR-LQG problem with endogenous ambiguity sets can be formulated as

where $\Gamma ≔ \left. \{{\gamma = {(\gamma_{0},\ldots,\gamma_{N})}} \middle| {\gamma_{t}:{{{\mathbb{R}}^{{({p + m})}t}\rightarrow{\mathcal{P}_{\mathcal{G}}{({\mathbb{R}}^{n})}}},{{\gamma_{t}{(I_{t})}} \in {\mathcal{B}_{t}{(x_{t},u_{t})}}}}}\} \right.$.

We begin by focusing on a relaxed version of Problem ((https://arxiv.org/html/2505.08370v2#S6.E24 "Equation 24 ‣ VI-A Relaxed problem ‣ VI DR-LQG with endogenous ambiguity sets ‣ Distributionally Robust LQG with Kullback-Leibler Ambiguity Sets")) where, instead of constraining the adversary to select a distribution from the ambiguity sets ${\{{\mathcal{B}_{t}{(x_{t},u_{t})}}\}}_{t = 0}^{T - 1}$, we simply penalize the deviation of the distributions ${\mathbb{P}}_{w_{t}}$ from their nominal ones. In other words, we focus on the relaxed regularized problem. Let us use for brevity $R{({\mathbb{P}}||{\mathbb{Q}}_{t})} \equiv \mathcal{R}_{t}$. The relaxed problem reads

where $J^{\tau}{(\pi,\gamma)}$ is defined as

for fixed ${\{\tau_{t}\}}_{t = 0}^{N}$ with $\tau_{t} \in {\mathbb{R}}_{+}$. We address ((https://arxiv.org/html/2505.08370v2#S6.E25 "Equation 25 ‣ VI-A Relaxed problem ‣ VI DR-LQG with endogenous ambiguity sets ‣ Distributionally Robust LQG with Kullback-Leibler Ambiguity Sets")) by resorting to the dynamic programming technique. To this end, we derive the following instrumental result.

### Proposition 8

Let ${{\overset{\sim}{x}}_{t}:={{\mathbb{E}}_{{\mathbb{P}}_{w_{t}}}{\lbrack\left. x_{t} \middle| I_{t} \right.\rbrack}}},$ $\xi_{t}:={x_{t} - {\overset{\sim}{x}}_{t}}$ and $\Sigma_{t}:={{\mathbb{E}}_{{\mathbb{P}}_{w_{t}}}{\lbrack\left. {\xi_{t}\xi_{t}^{\top}} \middle| I_{t} \right.\rbrack}}$ for ${t \in {\mathbb{N}}}.$ Given $P_{t + 1} \in {\mathbb{S}}_{+ +}^{n}$, $S_{t + 1} \in {\mathbb{S}}_{n}$, $z_{t + 1} \in {\mathbb{R}}$, define the function $r_{t}:{{\mathbb{S}}_{+ +}^{n}\rightarrow{\mathbb{R}}}$ as

Moreover, let $H_{t + 1}{(I_{t + 1})}$ be defined as

Consider the optimization problem

where the penalty parameter $\tau_{t} \geq 0$ is fixed and satisfies

The optimal solutions of ((https://arxiv.org/html/2505.08370v2#S6.E27 "Equation 27 ‣ Proposition 8. ‣ VI-A Relaxed problem ‣ VI DR-LQG with endogenous ambiguity sets ‣ Distributionally Robust LQG with Kullback-Leibler Ambiguity Sets")) are $u_{t}^{o} = {K_{t}^{o}{\overset{\sim}{x}}_{t}}$ with

The function $H_{t}{(I_{t})}$ in ((https://arxiv.org/html/2505.08370v2#S6.E27 "Equation 27 ‣ Proposition 8. ‣ VI-A Relaxed problem ‣ VI DR-LQG with endogenous ambiguity sets ‣ Distributionally Robust LQG with Kullback-Leibler Ambiguity Sets")) is given by

Our aim is to apply Proposition (https://arxiv.org/html/2505.08370v2#Thmtheorem8 "Proposition 8. ‣ VI-A Relaxed problem ‣ VI DR-LQG with endogenous ambiguity sets ‣ Distributionally Robust LQG with Kullback-Leibler Ambiguity Sets") to derive an iterative scheme to solve ((https://arxiv.org/html/2505.08370v2#S6.E24 "Equation 24 ‣ VI-A Relaxed problem ‣ VI DR-LQG with endogenous ambiguity sets ‣ Distributionally Robust LQG with Kullback-Leibler Ambiguity Sets")). To this end, let

be the value function satisfying the recursion

with ${{\mathcal{V}_{T}{(I_{T})}} = {{\mathbb{E}}_{{\mathbb{P}}_{w_{T - 1}}}{\lbrack\left. {\frac{1}{2}x_{T}^{\top}Q_{T}x_{T}} \middle| I_{T} \right.\rbrack}}}.$ By Bellman's principle of optimality \[(https://arxiv.org/html/2505.08370v2#bib.bib26)\], it holds

Unfortunately, a rapid inspection of ((https://arxiv.org/html/2505.08370v2#S6.E36 "Equation 36 ‣ VI-A Relaxed problem ‣ VI DR-LQG with endogenous ambiguity sets ‣ Distributionally Robust LQG with Kullback-Leibler Ambiguity Sets")) reveals that this value function is not amenabe to the closed-form recursion provided by Theorem (https://arxiv.org/html/2505.08370v2#Thmtheorem8 "Proposition 8. ‣ VI-A Relaxed problem ‣ VI DR-LQG with endogenous ambiguity sets ‣ Distributionally Robust LQG with Kullback-Leibler Ambiguity Sets"). This is due to the non-linearity introduced by $r_{t}{(\Sigma_{t})}$ appearing in the recursion for $\mathcal{V}_{t}{(I_{t})}$. Indeed, $r_{t}{(\Sigma_{t})}$ is a non-linear function of $\Sigma_{t}$ which in turns depends on the decision variable $W_{t - 1}$ throught the relation^33^3This relation follows from established principles in filtering theory addressing the propagation of uncertainties in state estimation.

breaking the recursion. To overcome these challenge, we approximate $r_{t}{(X)}$ in ((https://arxiv.org/html/2505.08370v2#S6.E26 "Equation 26 ‣ Proposition 8. ‣ VI-A Relaxed problem ‣ VI DR-LQG with endogenous ambiguity sets ‣ Distributionally Robust LQG with Kullback-Leibler Ambiguity Sets")) with a first-order approximation around the nominal prediction error covariance ${\hat{\Sigma}}_{t}:$

Considering now ((https://arxiv.org/html/2505.08370v2#S6.E38 "Equation 38 ‣ VI-A Relaxed problem ‣ VI DR-LQG with endogenous ambiguity sets ‣ Distributionally Robust LQG with Kullback-Leibler Ambiguity Sets")) leads to the linearized value function

It is now easy to see that the value function ${\overline{\mathcal{V}}}_{t}$ in ((https://arxiv.org/html/2505.08370v2#S6.E39 "Equation 39 ‣ VI-A Relaxed problem ‣ VI DR-LQG with endogenous ambiguity sets ‣ Distributionally Robust LQG with Kullback-Leibler Ambiguity Sets")) satisfies the dynamic programming recursion in Proposition (https://arxiv.org/html/2505.08370v2#Thmtheorem8 "Proposition 8. ‣ VI-A Relaxed problem ‣ VI DR-LQG with endogenous ambiguity sets ‣ Distributionally Robust LQG with Kullback-Leibler Ambiguity Sets"), leading us to define the following solution scheme.

*Solution scheme:* Let ${P_{N + 1} = Q_{N + 1}},{{{\overline{S}}_{N + 1} = 0},{{{\overline{z}}_{N + 1} = 0},{{\overline{c}}_{N + 1} = 0}}}$ and consider the recursions

Let $\tau = {(\tau_{0},\ldots,\tau_{T - 1})}$ and assume $\tau \in \mathcal{T}:={\mathcal{T}_{0} \times \cdots \times \mathcal{T}_{T - 1}}$ with

At each time step $t,$ the approximated value function of problem ((https://arxiv.org/html/2505.08370v2#S6.E25 "Equation 25 ‣ VI-A Relaxed problem ‣ VI DR-LQG with endogenous ambiguity sets ‣ Distributionally Robust LQG with Kullback-Leibler Ambiguity Sets")) (computed by using the linearized ${\overline{r}}_{t}{(X)}$ in ((https://arxiv.org/html/2505.08370v2#S6.E38 "Equation 38 ‣ VI-A Relaxed problem ‣ VI DR-LQG with endogenous ambiguity sets ‣ Distributionally Robust LQG with Kullback-Leibler Ambiguity Sets"))) is given by

with $\xi_{t} = {x_{t} - {\overset{\sim}{x}}_{t}}$ and ${\overset{\sim}{x}}_{t} = {{\mathbb{E}}^{o}{\lbrack\left. x_{t} \middle| I_{t} \right.\rbrack}}$ where ${\mathbb{E}}^{o}$ denotes the expectation with respect to the worst-case distribution $\mathcal{N}{(\mu_{t}^{o},W_{t}^{o})}$, whose moments are given by ((https://arxiv.org/html/2505.08370v2#S6.E30 "Equation 30 ‣ Item i. ‣ Proposition 8. ‣ VI-A Relaxed problem ‣ VI DR-LQG with endogenous ambiguity sets ‣ Distributionally Robust LQG with Kullback-Leibler Ambiguity Sets")) and ((https://arxiv.org/html/2505.08370v2#S6.E31 "Equation 31 ‣ Item i. ‣ Proposition 8. ‣ VI-A Relaxed problem ‣ VI DR-LQG with endogenous ambiguity sets ‣ Distributionally Robust LQG with Kullback-Leibler Ambiguity Sets")) upon substituting $S_{t + 1}$ with ${\overline{S}}_{t + 1}$. Finally, the optimal control input (for the approximated value function) is

with $K_{t}^{o}$ defined in ((https://arxiv.org/html/2505.08370v2#S6.E29 "Equation 29 ‣ Item i. ‣ Proposition 8. ‣ VI-A Relaxed problem ‣ VI DR-LQG with endogenous ambiguity sets ‣ Distributionally Robust LQG with Kullback-Leibler Ambiguity Sets")). Notice that ${\overset{\sim}{x}}_{t}$ can be recursively computed as

for $t = {0,{{\ldotsT} - 1}}$ where the Kalman gain is

Here, $\Sigma_{t}^{o}$ is the worst-case prediction error covariance matrix at time $t$ and it is recursively computed as

### Remark 1 (On approximating $r_{t}\hspace{0pt}{(\Sigma_{t})}$)

The non-linear dependence of $r_{t}$ on $\Sigma_{t}$ is also present in other distributionally robust control formulations, such as the data-driven Wasserstein-based approach discussed in \[(https://arxiv.org/html/2505.08370v2#bib.bib9), (https://arxiv.org/html/2505.08370v2#bib.bib13)\]. In the search for closed-form recursions, \[(https://arxiv.org/html/2505.08370v2#bib.bib9), (https://arxiv.org/html/2505.08370v2#bib.bib13)\] disregard such dependence. Conversely, we account for it via a suitable approximation, while retaining tractability. For completeness, we show the benefits of our formulation compared to the one in \[(https://arxiv.org/html/2505.08370v2#bib.bib9), (https://arxiv.org/html/2505.08370v2#bib.bib13)\] in Appendix E on a simplified setting amenable to both algorithms. Finally, we notice that other linear approximation of $r_{t}{(\Sigma_{t})}$ are possible; for example, one can consider ${{\overline{\overline{r}}}_{t}{(X)}} = {\frac{1}{2}{{Tr}\left( {S_{t + 1}AXA^{\top}} \right)}}$. In this case, since ${r_{t}{(X)}} \leq {{\overline{\overline{r}}}_{t}{(X)}}$ for any $X \in {\mathbb{S}}^{n}$, the resulting approximated value function ${\overline{\overline{\mathcal{V}}}}_{t}$ satisfies ${\mathcal{V}_{t}{(I_{t})}} \leq {{\overline{\overline{\mathcal{V}}}}_{t}{(I_{t})}}$ for any $I_{t}$ and $t = {T,\ldots,0}$, returning a valid upper bound for the control problem ((https://arxiv.org/html/2505.08370v2#S6.E25 "Equation 25 ‣ VI-A Relaxed problem ‣ VI DR-LQG with endogenous ambiguity sets ‣ Distributionally Robust LQG with Kullback-Leibler Ambiguity Sets")).

### VI-B Constrained problem

Next, we extend the results of Subsection [VI-A](https://arxiv.org/html/2505.08370v2#S6.SS1 "VI-A Relaxed problem ‣ VI DR-LQG with endogenous ambiguity sets ‣ Distributionally Robust LQG with Kullback-Leibler Ambiguity Sets") to the constrained minimax Problem (https://arxiv.org/html/2505.08370v2#S6.E24 "Equation 24 ‣ VI-A Relaxed problem ‣ VI DR-LQG with endogenous ambiguity sets ‣ Distributionally Robust LQG with Kullback-Leibler Ambiguity Sets") resorting to the Lagrange duality theory. Let $\tau = {(\tau_{0},\ldots,\tau_{T - 1})}$ be the Lagrangian multipliers vector; the dual problem associated to ((https://arxiv.org/html/2505.08370v2#S6.E24 "Equation 24 ‣ VI-A Relaxed problem ‣ VI DR-LQG with endogenous ambiguity sets ‣ Distributionally Robust LQG with Kullback-Leibler Ambiguity Sets")) is^44^4Contrary to Subsection [VI-A](https://arxiv.org/html/2505.08370v2#S6.SS1 "VI-A Relaxed problem ‣ VI DR-LQG with endogenous ambiguity sets ‣ Distributionally Robust LQG with Kullback-Leibler Ambiguity Sets"), we will consider optimizing over $\tau$, hence we use the notation $\mathcal{V}_{t}{(I_{t},\tau)}$ to emphasize such dependence.

where the equivalence follows from ((https://arxiv.org/html/2505.08370v2#S6.E24 "Equation 24 ‣ VI-A Relaxed problem ‣ VI DR-LQG with endogenous ambiguity sets ‣ Distributionally Robust LQG with Kullback-Leibler Ambiguity Sets")). We consider the linearized dual problem

with ${\overline{\mathcal{V}}}_{0}{(I_{0},\tau)}$ defined in ((https://arxiv.org/html/2505.08370v2#S6.E45 "Equation 45 ‣ VI-A Relaxed problem ‣ VI DR-LQG with endogenous ambiguity sets ‣ Distributionally Robust LQG with Kullback-Leibler Ambiguity Sets")).

Consider the coordinate gradient descent scheme, where at each iteration $t \in {\mathbb{N}}$ we update each $i$-th component of the vector $\tau$ sequentially^55^5One might also randomly select the order of the updates at each iteration $t$ rather than considering a cyclic pattern. Randomized updates might enhance numerical stability. for $i = {\{ 0,\ldots,{T - 1}\}}$ by solving the one-dimensional subproblem

The overall procedure to solve ((https://arxiv.org/html/2505.08370v2#S6.E24 "Equation 24 ‣ VI-A Relaxed problem ‣ VI DR-LQG with endogenous ambiguity sets ‣ Distributionally Robust LQG with Kullback-Leibler Ambiguity Sets")) is summarized in Algorithm 1. We get the following result.

### Theorem 9

Let $\tau^{t}$ be the sequence generated by the coordinate gradient descent scheme ta time $t$ using the updates in ((https://arxiv.org/html/2505.08370v2#S6.E50 "Equation 50 ‣ VI-B Constrained problem ‣ VI DR-LQG with endogenous ambiguity sets ‣ Distributionally Robust LQG with Kullback-Leibler Ambiguity Sets")). Then, the sequence ${\{{{\overline{\mathcal{W}}}_{0}{(I_{0},\tau^{t})}}\}}_{t = 0}^{\infty}$ converges to the optimal value of the dual problem ((https://arxiv.org/html/2505.08370v2#S6.E49 "Equation 49 ‣ VI-B Constrained problem ‣ VI DR-LQG with endogenous ambiguity sets ‣ Distributionally Robust LQG with Kullback-Leibler Ambiguity Sets")) at a rate no worse than ${\mathcal{O}\left( \frac{1}{t} \right)}.$

Initialize {τt}t = 0T − 1 and set j = 0
${{\overline{\mathcal{W}}}_{0}{(I_{0},{\{\tau_{t}^{(j)}\}}_{t = 0}^{T - 1})}}\leftarrow$ Recurs(sys, {τt(j)}t = 0T − 1)
$\tau_{i}^{({j + 1})} ≔ {{{\arg\min}_{z}{\overline{\mathcal{W}}}_{0}}\left. (I_{0},\left\lbrack \left\{ \tau_{t}^{(j)} \right\}_{t = 0}^{i - 1},z,\left\{ \tau_{t}^{(j)} \right\}_{t = {i + 1}}^{T - 1} \right\rbrack \right)}$
Apply $u_{t}^{\star} = {K_{t}^{\star}{\overset{\sim}{x}}_{t}}$ to system
Measure yt + 1 and estimate ${\overset{\sim}{x}}_{t + 1}$ via
Algorithm 1 DR-LQG with endogenous ambiguity sets

system/cost matrices, V̂t, Ŵt, ρt, {τt(j)}t = 0N
total cost ${\overline{\mathcal{W}}}_{0}{(I_{0},{\{\tau_{t}^{(j)}\}}_{t = 0}^{T - 1})}$
for t = T to t = 0 do ⊳ Backward pass
Compute recursion matrices via -
Compute control gain via
Compute worst-case distribution via,
for t = 0 to t = T do ⊳ Foreward pass
Compute Kalman gain via
Compute worst-case prediction covariance via

## Simulations

### VII-A Example 1

We consider a linear model ((https://arxiv.org/html/2505.08370v2#S3.E3 "Equation 3 ‣ III Problem setup ‣ Distributionally Robust LQG with Kullback-Leibler Ambiguity Sets")) with

We set the radii to be $\rho_{x_{0}} = \rho_{w_{t}} = \rho_{v_{t}} = 1$ and the nominal covariances to ${\hat{W}}_{t} = {0.001I_{2}}$, ${\hat{V}}_{t} = 0.001$ for all times $t$, and $W_{- 1} = 0_{2}$. We set ${Q = I_{2}},{{Q_{t} = {10I_{2}}},{R = 0.1}}$, $T = 20$, and $\hat{x_{0}} = {\lbrack 0,0\rbrack}^{\top}$. We implement the iterative best response dynamics in ((https://arxiv.org/html/2505.08370v2#S5.E19 "Equation 19 ‣ V-B Regularized best response scheme ‣ V Computational framework for the DR-LQG ‣ Distributionally Robust LQG with Kullback-Leibler Ambiguity Sets")) in Python 3.8.6 using the Scipy package and the ODE solver. Fig. (https://arxiv.org/html/2505.08370v2#S7.F2 "Figure 2 ‣ VII-A Example 1 ‣ VII Simulations ‣ Distributionally Robust LQG with Kullback-Leibler Ambiguity Sets") shows the empirical convergence behavior of the best response dynamics, confirming the exponential convergence rate from Theorem (https://arxiv.org/html/2505.08370v2#Thmtheorem7 "Theorem 7. ‣ V-B Regularized best response scheme ‣ V Computational framework for the DR-LQG ‣ Distributionally Robust LQG with Kullback-Leibler Ambiguity Sets").

The DR-LQG controller was benchmarked against a standard LQG based on the nominal distributions. We carried out 5000 Montecarlo simulations with exogenous disturbances distributed according to the true distributions ${\mathbb{P}}_{x_{0}},{\mathbb{P}}_{w_{t}},{\mathbb{P}}_{v_{t}}$ selected randomly from the ambiguity sets. The DR-LQG controller led to an average cost across the Montecarlo run of 0.6287 and a standard deviation of 0.7125, while the standard LQG led to an average cost of 0.6587 and a standard deviation of 0.7588. The results confirm the effectiveness of the proposed approach to provide robustification against distributional ambiguity.

Figure 2: Example 1: Convergence of the optimality gap for the best response dynamics.

### VII-B Example 2

We show the benefits of our DR-LQG controller with endogenous ambiguity sets ((https://arxiv.org/html/2505.08370v2#S6.E24 "Equation 24 ‣ VI-A Relaxed problem ‣ VI DR-LQG with endogenous ambiguity sets ‣ Distributionally Robust LQG with Kullback-Leibler Ambiguity Sets")). Consider the linear model ((https://arxiv.org/html/2505.08370v2#S3.E3 "Equation 3 ‣ III Problem setup ‣ Distributionally Robust LQG with Kullback-Leibler Ambiguity Sets")) with

We assume that, for all $t$, $w_{t}$ follows a Gaussian distribution with zero-mean and nominal covariance

while $v_{t}$ follows a zero-mean Gaussian distribution with covariance ${{\hat{V}}_{t} = I}.$ We set ${{{\hat{x}}_{0} = {\lbrack 0.1\;\;0.1\rbrack}^{\top}},{W_{- 1} = {10^{- 4}I_{2}}}}.$ We consider a horizon $T = 50$ and use the cost matrices

and ${R = {10^{- 3}I}}.$ We assume that the matrix $A$ contains some uncertainty and that the real underlying system evolves with a dynamics matrix $\overset{\sim}{A} = {A + {\DeltaA}}$ where

The coefficients $a$ and $b$ are unknown parameters with ${|a|} \leq a_{M}:=0.047$ and ${{|b|} \leq b_{M}:=0.03}.$ In other words, the real underlying system evolves according to the dynamics $x_{t + 1} = {{Ax_{t}} + {Bu_{t}} + {\overset{\sim}{w}}_{t}}$ where ${{\overset{\sim}{w}}_{t} = {{\DeltaAx_{t}} + w_{t}} \sim {\mathcal{N}{({\DeltaAx_{t}},\hat{W})}}}.$ For the ambiguity set, we use $z_{t} = {E_{1}x_{t}}$ with

and ${\rho_{t} = 10^{- 5}}.$ We compare our controller, which we term D^2^O-LQG controller, with the standard LQG controller. Additionally, we consider the DRC controller with a single relative-entropy constraint (D-LQG) from \[(https://arxiv.org/html/2505.08370v2#bib.bib27)\], using ${\rho = {\sum_{t = 0}^{T - 1}\rho_{t}}}.$ We consider two scenarios: (i) Nominal scenario, with ${\DeltaA} = 0$; (ii) Perturbed scenario, with $a = 0.03$ and ${b = 0.02}.$ The results of the simulations are summarized in Figg. (https://arxiv.org/html/2505.08370v2#S7.F3 "Figure 3 ‣ VII-B Example 2 ‣ VII Simulations ‣ Distributionally Robust LQG with Kullback-Leibler Ambiguity Sets") and (https://arxiv.org/html/2505.08370v2#S7.F4 "Figure 4 ‣ VII-B Example 2 ‣ VII Simulations ‣ Distributionally Robust LQG with Kullback-Leibler Ambiguity Sets"). The standard LQG technique is not able to stabilize the system in the perturbed scenario, causing the cost index to increase dramatically. The D-LQG controller with a single constraint has not a satisfactory behaviour: this is due to the fact that the maximizing player is allowed to allocate most of the mismatch budget to few (or even one) time intervals. On the other hands, D^2^O-LQG control in able to trade off optimality and robustness. In the nominal scenario the average closed-loop cost is slightly larger than the pure LQG optimum. This cost remains almost constant when ${{\DeltaA} \neq 0},$ giving evidence to the robustness properties of the control system.

Figure 3: Example 2: nominal scenario with Δ A = 0. Histogram of the cost distribution across 1000 Monte Carlo experiments. The dashed lines represent the sample means of the costs.

Figure 4: Example 2: perturbed scenario with Δ A ≠ 0. Histogram of the cost distribution across 1000 Monte Carlo experiments. The dashed lines represent the sample means of the costs. Notice the different x-axis scale.

### VII-C Example 3

In the last example, we aim to show that the scheme proposed in Section [VI](https://arxiv.org/html/2505.08370v2#S6 "VI DR-LQG with endogenous ambiguity sets ‣ Distributionally Robust LQG with Kullback-Leibler Ambiguity Sets") outperforms the one in \[(https://arxiv.org/html/2505.08370v2#bib.bib13)\] based on the Wasserstein distance. As \[(https://arxiv.org/html/2505.08370v2#bib.bib13)\] does not directly handle decision-dependent ambiguity sets, we consider a simplified setting with exogenous uncertainty and adapt the recursions in Proposition ((https://arxiv.org/html/2505.08370v2#Thmtheorem8 "Proposition 8. ‣ VI-A Relaxed problem ‣ VI DR-LQG with endogenous ambiguity sets ‣ Distributionally Robust LQG with Kullback-Leibler Ambiguity Sets")) accordingly by setting $E_{1} = E_{2} = 0$. We consider a building temperature control problem using a state-space model borrowed from \[(https://arxiv.org/html/2505.08370v2#bib.bib28)\] and affected by uncertainty in the ambient temperature $T_{t}^{a} \sim {\mathcal{N}{({{\overline{T}}_{t}^{a} + {\hat{\mu}}_{t}},{\hat{W}}_{t})}}$^66^6The recursions in this case are slightly different; but can be easilly derived using the same reasoning as in Proposition (https://arxiv.org/html/2505.08370v2#Thmtheorem8 "Proposition 8. ‣ VI-A Relaxed problem ‣ VI DR-LQG with endogenous ambiguity sets ‣ Distributionally Robust LQG with Kullback-Leibler Ambiguity Sets").. The control problem seeks to regulate the rooms temperature to a reference $r = 21^{\circ}$C at the minimum power consumption via the stage cost ${\|{x_{t} - r}\|}_{Q}^{2} + {\| u_{t}\|}_{R}^{2}$.

To fit the building temperature control problem into the presented framework, we define the error state $e_{t} = {x_{t} - r}$ and consider the error dynamics

with $w_{t} \sim {\mathcal{N}{({{F{\overline{w}}_{t}} + {({{Ar} - r})} + {F{\hat{\mu}}_{t}}},{F{\hat{W}}_{t}F^{\top}})}}$, $v_{t} \sim {\mathcal{N}{({Cr},V)}}$, and $e_{0} \sim {\mathcal{N}{({{\hat{x}}_{0} - r},\Sigma_{0})}}$. We let $W = I_{2}$, ${\hat{x}}_{0} = \begin{bmatrix}
\end{bmatrix}^{\top}$ and $\Sigma_{0} = {0.1I_{2}}$. For the sake of the simulation, we set the uncertainty budget $\rho_{t}$ a-posteriori based on the knowledge of the true process noise distribution, considering $d_{t} = {1.1\mathcal{R}_{t}}$ where $\mathcal{R}_{t}$ is the relative entropy between the nominal and the true distribution at time $t$. We compare the proposed D^2^O-LQG controller with the standard LQG controller and the DRC controller with a constant distributional ambiguity budget $\theta$ per each time step proposed in \[(https://arxiv.org/html/2505.08370v2#bib.bib13)\]^77^7We use the public code from the authors accessible at https://github.com/CORE-SNU/PO-WDRC. (W-DRC). As before, we set $\theta = {\frac{1}{N}{\sum_{t = 0}^{N - 1}{({1.1d_{t}^{\text{W}}})}}}$, where $d_{t}^{\text{W}}$ is the a-posteriori Wasserstein distance between the true and the nominal distribution. Results are summarized in Fig. (https://arxiv.org/html/2505.08370v2#S7.F5 "Figure 5 ‣ VII-C Example 3 ‣ VII Simulations ‣ Distributionally Robust LQG with Kullback-Leibler Ambiguity Sets"). Again, the standard LQG controller does not offer any robustness against model misspecification; thus, its performance rapidly deteriorates in the presence of distributional ambiguity. On the other hand, while the W-DRC controller from \[(https://arxiv.org/html/2505.08370v2#bib.bib13)\] offers a degree of robustness, its practical performance is hindered by the requirement for the same ambiguity set size (e.g., the same $\theta$) throughout the entire control task.

Figure 5: Example 1. Histogram of the cost distribution across 1000 Monte Carlo experiments. The dashed lines represent the sample means of the costs.

## Conclusions

For discrete-time stochastic linear systems, we propose an output feedback controller capable of robustifying the standard LQG approach against distributional ambiguity affecting both process and measurement noise by relying on KL ambiguity sets. Our analysis shows that linear policies are still optimal despite the added complexity; moreover, the worst-case distribution is still a Gaussian. These insights led us to design an iterated best response dyanmics scheme that provably convergences to the set of saddle points and admits closed-form expressions. Further, we consider the case of decision-dependent ambiguity sets to capture model perturbations. For this setting, we devise a tailored approximated recursive scheme based on dynamic programming and coordinate gradient descent.
