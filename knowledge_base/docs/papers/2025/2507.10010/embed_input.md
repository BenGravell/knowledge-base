<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Probabilistic Robustness in the Gap Metric

Topics include Stability analysis, Robustness, Uncertainty, Probabilistic models, Control, Robust control, Random variable.

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Uncertainties influencing the dynamical systems pose a significant challenge in estimating the achievable performance of a controller aiming to control such uncertain systems. When the uncertainties are of stochastic nature, obtaining hard guarantees for the robustness of a controller aiming to hedge against the uncertainty is not possible. This issue set the platform for the development of probabilistic robust control approaches. In this work, we utilise the gap metric between the known nominal model and the unknown perturbed model of the uncertain system as a tool to gauge the robustness of a controller and formulate the gap as a random variable in the setting with stochastic uncertainties. The main results of this paper include giving a probabilistic bound on the gap exceeding a known threshold, followed by bounds on the expected gap value and probabilistic robust stability and performance guarantees in terms of the gap metric. We also provide a probabilistic controller performance certification under gap uncertainty and probabilistic guarantee on the achievable H_infinity robustness. Numerical simulations are provided to demonstrate the proposed approach.

<!-- chunk {"id": "body-0003", "role": "body", "section": "Introduction", "weight": 1.5} -->

Robust control stands to be one of the most mature control methodologies to be ever developed mainly due to the strong guarantees that comes with it (interested readers are referred to and the references therein). Vinnicombe in describes robust control approaches as the ones where we try to come up with a control input for a system using what we know about the system so that the control input renders the system insensitive to what we do not know about the system. To illustrate that thought, consider the Figure 1, where $\overline{\Sigma}$ denotes the known nominal model of the system and $\overset{\sim}{\Sigma}$ as the (true and possibly unknown) perturbed model of the system. The perturbed model $\overset{\sim}{\Sigma}$ is obtained by combining $\overline{\Sigma}$ and the uncertainty $\Delta$ that encapsulates what we do not know about the system as per Vinnicombe's description.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

Then, informally speaking, one can describe where, $\mathbf{\Delta}$ denotes the set of possible uncertainties and it is allowed to be structured, unstructured, parametric, static, dynamic, time invariant and even time-varying in nature.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

The description of perturbed model of the system $\overset{\sim}{\Sigma}$ using naturally led several people to conceive the concept of measuring the distance between systems (specifically between Linear Time Invariant (LTI) systems which is of interest to us in this paper). Vidyasagar in proposed the graph metric, followed by gap metric which was proposed. Since the graph metric was difficult to compute, Georgiou in came up with an elegant formula to compute the gap metric and subsequently the optimal robustness in the gap metric was established. Meanwhile, Glover in had extended the famous small-gain theorem in to handle perturbation in $\mathcal{L}_{\infty}$ rather than only in $\mathcal{H}_{\infty}$. Vinnicombe leveraged this development and proposed a new metric called the $\nu$-gap in by building upon the gap metric. Authors in proposed a generalised distance measure for LTI systems by taking into account the information about several uncertainty structures. While all these metrics can be used for proposing probabilistic robustness, we shall be employing only the gap metric in this paper.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

Though gap metric has also been extensively studied for linear time varying (LTV) systems setting too, we shall restrict our study in this manuscript to LTI systems and leave the extension to LTV systems for future work.\Probabilistic Robust Control (PRC) approaches have been explored before and the interested readers are referred to and the references therein. In connection with the scenario-based approaches for robust control design, see and the references therein for more details. Having said that, the approach proposed in this paper involves metric between dynamical systems and casting them as random quantities, while the existing PRC approaches define robustness guarantees in terms of the volume of destabilizing perturbations or equivalently probability of violation of robust stability and performance conditions. Though our approach presumably aims to solve the same problem, the underlying methodology is certainly different from the existing PRC approaches. In this paper, we shall be using the gap metric for gauging the robustness and use the tools from high dimensional statistics for giving probabilistic guarantees.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

It was already noted by authors in that the gap metric may be not suitable for evaluating the closeness of systems having uncertain poles and zeros on or near the imaginary axis resulting in the difficulty of the stability of the perturbed plant with a stabilizing controller designed for the nominal plant not being guaranteed through the existing stability theorems involving the gap metric. Our developments using probabilistic gap based problem formulation in this manuscript will aim to investigate along with their findings in the sense of probabilistic guarantees.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Contributions", "weight": 1.0} -->

This work is an extension of where probabilistic robustness in terms of the $\nu$-gap metric in the frequency domain was initiated. In this work, a similar extension is sought albeit in the time domain using the gap metric. We believe our new perspective on PRC theory using gap between dynamical systems will further strengthen the existing theory on PRC and will open new doors for further exploration. The main contributions of this article are as follows: When a random parameter affects a linear system, we study the satisfaction of the Bézout Identity governing the normalised co-prime factors of the uncertain system transfer function under that parameter uncertainty (See Lemma 2 ‣ 3 Solution Methodology ‣ Probabilistic Robustness in the Gap Metric")) and subsequently we investigate the probabilistic guarantee associated with the randomness in the coprime factor uncertainty in Theorem 3.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Contributions", "weight": 1.0} -->

When the perturbed model $\overset{\sim}{\Sigma}$ is not known exactly due to the random parameters, we formulate the associated gap metric between the known nominal model $\overline{\Sigma}$ and $\overset{\sim}{\Sigma}$ as a random variable and study the probability of the random gap exceeding a known threshold in Theorem 4 ‣ 3 Solution Methodology ‣ Probabilistic Robustness in the Gap Metric") and its corollaries and give bounds on its expected value in Lemma 6 ‣ 3 Solution Methodology ‣ Probabilistic Robustness in the Gap Metric") and its associated corollary.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Contributions", "weight": 1.0} -->

We formulate the randomness in the perturbed model $\overset{\sim}{\Sigma}$ by resulting it from the stochastic parametric uncertainty for the LTI system and we discuss probabilistic robust stability result in Theorem 7 and we provide probabilistic closed loop deviation (in the $\mathcal{H}_{\infty}$ norm) guarantees due to the action of a nominal controller aiming to control the perturbed model (See Theorem 8).

<!-- chunk {"id": "body-0011", "role": "body", "section": "Contributions", "weight": 1.0} -->

We give probabilistic $\mathcal{H}_{\infty}$ performance bound for the perturbed system under uncertainty in Theorem 9 and give probabilistic guarantee of meeting a desired $\mathcal{H}_{\infty}$ performance in Corollary 9.1. We also give a rather conservative bound on the expected value of the $\mathcal{H}_{\infty}$ norm of the random perturbed system in Theorem 12.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Contributions", "weight": 1.0} -->

We connect the random gap metric problem formulation with the scenario based robustness approach to give probabilistic robust stability result in terms of the gap metric based performance measure in Theorem 13 Theory ‣ Probabilistic Robustness in the Gap Metric").

<!-- chunk {"id": "body-0013", "role": "body", "section": "Contributions", "weight": 1.0} -->

Numerical simulations are given at many places along the manuscript to demonstrate the idea proposed in this paper. The Matlab codes to reproduce the results provided in this manuscript are available at

<!-- chunk {"id": "body-0014", "role": "body", "section": "Notations", "weight": 1.0} -->

The cardinality of the set $A$ is denoted by $|A|$. Given two sets $A,B$ such that $A \subset B$, the notation $A^{c}$ denotes the complement of set $A$ in $B$ meaning that $A^{c}:={\{{x \in B}\mid{x \notin A}\}} \subset B$. The set of real numbers, integers and the natural numbers are denoted by ${\mathbb{R}},{\mathbb{Z}},{\mathbb{N}}$ respectively and the subset of real numbers greater than a given constant say $a \in {\mathbb{R}}$ is denoted by ${\mathbb{R}}_{> a}$. The subset of natural numbers between two constants ${a,b} \in {\mathbb{N}}$ with $a < b$ is denoted by $\lbrack{a:b}\rbrack$.

<!-- chunk {"id": "body-0015", "role": "body", "section": "Notations", "weight": 1.0} -->

For a matrix $A \in {\mathbb{R}}^{n \times n}$, we denote its transpose and its trace by $A^{\top}$ and ${\mathbf{T}\mathbf{r}}{(A)}$ respectively. An identity matrix of dimension $n$ is denoted by $I_{n}$. We denote by ${\mathbb{S}}^{n}$ the set of symmetric matrices in ${\mathbb{R}}^{n \times n}$. For $A \in {\mathbb{S}}^{n}$, we denote by $A \succ {0{({A \succeq 0})}}$ to mean that $A$ is positive definite (positive semi-definite). Given $x \in {\mathbb{R}}^{n}$, the notation $\left. \parallel x\parallel \right.$ denotes the $\mathcal{L}_{2}$ norm and is given by $\sqrt{x^{\top}x}$.

<!-- chunk {"id": "body-0016", "role": "body", "section": "Notations", "weight": 1.0} -->

For brevity of notation, multi-variate functions like $g{({x{(t)}},{y{(t)}})}$ shall be abbreviated as $g{(t;x,y)}$. For a subspace $S \subset {\mathbb{R}}^{n}$, its orthogonal complement is denoted by $S^{\perp}$.

<!-- chunk {"id": "body-0017", "role": "body", "section": "Notations", "weight": 1.0} -->

The angle between two vectors ${x,y} \in {\mathbb{R}}^{n}$ and the angle between two subspaces ${M,N} \subset {\mathbb{R}}^{n}$ are denoted by $\angle{(x,y)}$ and $\angle{(M,N)}$ respectively.\The probability space is defined using a triplet $(\Omega,\mathcal{F},{\mathbb{P}})$, where $\Omega,\mathcal{F}$, and $\mathbb{P}$ denote the sample space, event space, and the probability function, respectively, with ${\mathbb{P}}:{\Omega\rightarrow{\lbrack 0,1\rbrack}}$.

<!-- chunk {"id": "body-0018", "role": "body", "section": "Notations", "weight": 1.0} -->

A real random vector $x \in {\mathbb{R}}^{n}$ following a probability density function $\mathbf{f}_{\mathbf{x}}$ is denoted by $x \sim \mathbf{f}_{\mathbf{x}}$ and its expectation is denoted by ${\mathbb{E}}{\lbrack x\rbrack}$. A zero-mean random vector $x \in {\mathbb{R}}^{n}$ following a Gaussian distribution with covariance $I_{n} \succ 0$ is denoted by $x \sim {\mathcal{N}{(0,I_{n})}}$. Similarly, a random variable $x$ following a Chi-squared distribution with parameter $p > 0$ is denoted by $x \sim \chi_{p}^{2}$.

<!-- chunk {"id": "body-0019", "role": "body", "section": "Notations", "weight": 1.0} -->

The covariance of a random vector $x \in {\mathbb{R}}^{n}$ is denoted by ${\mathbf{C}\mathbf{o}\mathbf{v}}{(x)}$.\Let $\mathbf{R}{(s)}$ denote the set of rational functions in $s \in {\mathbb{C}}$ with real coefficients. We use ${\mathcal{P}{(s)}} \subset {\mathbf{R}{(s)}}$ to denote the set of proper rational functions whose poles are in the open left half-plane. Conceptually speaking, $\mathcal{P}{(s)}$ denotes the set of all finite-dimensional stable systems.

<!-- chunk {"id": "body-0020", "role": "body", "section": "Notations", "weight": 1.0} -->

Let us denote the set of matrices with elements in $\mathbf{R}{(s)}$ as ${mat}{({\mathbf{R}{(s)}})}$ and similarly, let us denote the set of matrices with elements in $\mathcal{P}{(s)}$ as ${mat}{({\mathcal{P}{(s)}})}$. Let $\mathcal{L}_{2}$ denote the space of all signals, or vectors of signals with bounded energy. In the frequency domain, the space $\mathcal{L}_{2}$ can be decomposed into $\mathcal{H}_{2}$ and $\mathcal{H}_{2}^{\perp}$, where $\mathcal{H}_{2}$ denotes the space of the Fourier transforms of signals defined for positive time and zero for negative time and $\mathcal{H}_{2}^{\perp}$ denotes the space of the Fourier transforms of signals defined for negative time and zero for positive time.

<!-- chunk {"id": "body-0021", "role": "body", "section": "Notations", "weight": 1.0} -->

The Hardy space consisting of transfer functions of stable LTI continuous time systems is denoted by $\mathcal{H}_{\infty}$ and is equipped with the $\mathcal{H}_{\infty}$ norm ${\forall{P{(s)}}} \in {{mat}{({\mathcal{P}{(s)}})}}$ given by with $\overline{\sigma}{({G{({j\omega})}})}$ denoting the maximum singular value. It happens that, $\mathcal{H}_{\infty}$ norm equals the induced norm. That is, The notation $\mathbf{R}\mathcal{H}_{\infty}$ denotes the set of all stable rational transfer functions.

<!-- chunk {"id": "body-0022", "role": "body", "section": "Uncertain Dynamical System", "weight": 1.0} -->

Consider the nominal model of the continuous time LTI dynamical system of the following form: where we refer to the system states as $x \in {\mathbb{R}}^{n}$ and the control inputs to the system as $u \in {\mathbb{R}}^{m}$, and system outputs as $y \in {\mathbb{R}}^{l}$ and the matrices $(A,B,C)$ are of appropriate dimensions. Real-world dynamical systems usually have some form of uncertainties associated with them either due to the lack of modelling tools or due to the inaccuracies of the modelling framework. Hence, in practise, all systems have inherent uncertainties affecting their evolution.

<!-- chunk {"id": "body-0023", "role": "body", "section": "Uncertain Dynamical System", "weight": 1.0} -->

We model the uncertainty affecting the evolution of such uncertain systems using $\theta \in {\mathbb{R}}^{p}$ with $p \leq {({n + m + l})}$ and $\theta$ directly affects the evolution of the perturbed system described as follows: We will assume that $\theta \sim \mathbf{f}_{\theta}$ where, $\mathbf{f}_{\theta}$ denotes the distribution of the parameter $\theta$. For instance, we can assume that $\mathbf{f}_{\theta}$ is unknown but is believed to be belonging to a moment based ambiguity set $\mathcal{P}^{\theta}$ consistent with mean $\mu_{\theta} \in {\mathbb{R}}^{p}$ and covariance ${\sigma_{\theta}^{2}I_{p}} \succ 0$.

<!-- chunk {"id": "body-0024", "role": "body", "section": "Uncertain Dynamical System", "weight": 1.0} -->

However, for the ease of exposition, we will assume that $\theta \sim \mathbf{f}_{\theta} = {\mathcal{N}{(\mu_{\theta},{\sigma_{\theta}^{2}I_{p}})}}$ as this will aid the formulation of the associated gap to become sub-Gaussian which is favourable for obtaining bounds on tail probability (as a Lipschitz function of a Gaussian random variable is sub-Gaussian). Further, we note here that ${\overset{\sim}{\Sigma}{(\theta_{0})}} = \overline{\Sigma}$ meaning that the uncertainties of the perturbed system vanish at $\theta = \theta_{0}$ and the resulting system equals the nominal system (in sense of Figure 1 with $\Delta = 0$). This does not imply that $\mu_{\theta} = \theta_{0}$.

<!-- chunk {"id": "body-0025", "role": "body", "section": "Uncertain Dynamical System", "weight": 1.0} -->

The only nominal and valid requirement that is needed is that $\theta_{0} \in \mathbf{f}_{\theta}$ (perfectly fine even if the containment happens asymptotically) so that when uncertainties of the perturbed system vanish, it results in the nominal system. It would be interesting to investigate the randomness in uncertainties by taking into account their structural information as done, but we reserve that research direction for future work. While we don't take into account the structural information about the uncertainties in this research, we establish guarantees by incorporating further knowledge as to where in the model ambiguity set the system model is more likely to be in the space of (LTI) dynamical systems. We believe that by leveraging this additional knowledge on the space of dynamical systems, we can create new perspective for the field of PRC theory.

<!-- chunk {"id": "body-0026", "role": "body", "section": "Gap Between Nominal & Perturbed Models", "weight": 1.0} -->

Having defined the evolution of the nominal model $\overline{\Sigma}$ using and perturbed model $\overset{\sim}{\Sigma}{(\theta)}$ in for the system $\Sigma$, we denote the closed loop complementary sensitivity transfer function (from $w$ to $z$ in Figure 1) of the system $\Sigma$ as $\mathbf{T}$. Then, the gap between the nominal model of the system $\overline{\Sigma}$ and the perturbed model of the system $\overset{\sim}{\Sigma}{(\theta)}$ denoted by ${Gap}{(\theta)}$ can be defined using as Note that for a fixed $\theta$ value, ${Gap}{(\theta)}$ can be computed using.

<!-- chunk {"id": "body-0027", "role": "body", "section": "Gap Between Nominal & Perturbed Models", "weight": 1.0} -->

Note that for every realization of $\theta$ say $\overline{\theta}$ from $\mathbf{f}_{\theta}$, we get a deterministic graph subspace $\mathcal{G}_{\overset{\sim}{\Sigma}{(\overline{\theta})}}$ and hence a deterministic projection $\Pi_{\mathcal{G}_{\overset{\sim}{\Sigma}{(\overline{\theta})}}}$. But in general, the randomness in $\overset{\sim}{\Sigma}{(\theta)}$ due to $\theta$ manifests itself as the randomness in the graph subspace $\mathcal{G}_{\overset{\sim}{\Sigma}{(\theta)}}$ and this results in the corresponding projection operator $\Pi_{\mathcal{G}_{\overset{\sim}{\Sigma}{(\theta)}}}$ becoming random as well.

<!-- chunk {"id": "body-0028", "role": "body", "section": "Gap Between Nominal & Perturbed Models", "weight": 1.0} -->

Specifically, the projection $\Pi_{\mathcal{G}_{\overset{\sim}{\Sigma}{(\theta)}}}$ is a random operator-valued function of $\theta$. While we certainly want to investigate the above randomness of the projection operator and hence the randomness of the associated ${Gap}{(\theta)}$ using and in detail, we reserve that exciting research direction as a future work. In this manuscript, we will aim to establish the fact that ${Gap}{(\theta)}$ is a sub-Gaussian random variable and leverage the tools from high dimensional statistics to give probabilistic guarantees. Let $\Theta \subseteq {\mathbb{R}}^{p}$ denote the set of all possible values of $\theta$ such that, $\theta \sim {\mathcal{N}{(\mu_{\theta},{\sigma_{\theta}^{2}I_{p}})}}$. We now state the main problems of interests that are being addressed in this manuscript.

<!-- chunk {"id": "body-0029", "role": "body", "section": "Problem 2", "weight": 1.0} -->

Given nominal system model $\overline{\Sigma}$ and the perturbed system model $\overset{\sim}{\Sigma}{(\theta)}$ with $\theta \sim {\mathcal{N}{(\mu_{\theta},{\sigma_{\theta}^{2}I_{p}})}}$ resulting in ${Gap}{(\theta)}$ becoming random, address the following questions: how to guarantee for a given desired performance level $\gamma > 0$ and a violation probability $\beta \in {}$ that obtain a bound for ${\mathbb{E}}\left\lbrack \left. \parallel{\mathbf{T}{({\overset{\sim}{\Sigma}{(\theta)}})}}\parallel \right._{\mathcal{H}_{\infty}} \right\rbrack$.

<!-- chunk {"id": "body-0030", "role": "body", "section": "Solution Methodology", "weight": 1.0} -->

Let us denote the normalized RCFs of the nominal model $\overline{\Sigma}$ and the perturbed model $\overset{\sim}{\Sigma}{(\theta)}$ of the system as $(\overline{N},\overline{D})$ and $({\overset{\sim}{N}{(\theta)}},{\overline{D}{(\theta)}})$ respectively and further their respective graph symbols by $\overline{G}$ and $\overset{\sim}{G}{(\theta)}$. We begin the discussion in this section by analysing how should one understand the randomness associated with the normalised RCFs $\overset{\sim}{G}{(\theta)}$. Most of the work presented in the section would work for the case of ${{Gap}{(\theta)}} < 1$.

<!-- chunk {"id": "body-0031", "role": "body", "section": "Solution Methodology", "weight": 1.0} -->

The case of ${{Gap}{(\theta)}} = 1$ corresponds to unstable perturbed plant $\overline{\Sigma}{(\theta)}$ and we do not consider such cases ($\nu$-Gap is equipped to handle such cases and it is clearly out of the scope of this paper). Similarly, all the developments in this paper shall assume (unless otherwise specified) that the nominal plant $\overline{\Sigma}$ and the nominal controller $\overline{C}$ belong to the $\mathcal{H}_{\infty}$ space. Though depending upon the strength of the perturbation, the perturbed plant $\overset{\sim}{\Sigma}{(\theta)}$ may become open-loop stable or unstable and hence it may or may not belong to the $\mathcal{H}_{\infty}$ space, we only consider the ones that are in the $\mathcal{H}_{\infty}$ space so that ${{Gap}{(\theta)}} < 1$.

<!-- chunk {"id": "body-0032", "role": "body", "section": "Solution Methodology", "weight": 1.0} -->

Though, we can write analogous theorem and lemma statements with guarantees in terms of the Left co-prime factors (LCFs), we will be sticking to the RCFs based statements without loss of generality in this manuscript.

<!-- chunk {"id": "body-0033", "role": "body", "section": "About the Randomness of Graph Operator $\\overset{\\sim}{G}{(\\theta)}$", "weight": 1.0} -->

We begin our discussion about the randomness associated with the graph operator of the perturbed plant $\overset{\sim}{G}{(\theta)}$ where the uncertainty stems from the associated uncertainty of the parameter $\theta$. We have the following assumption in place concerned with the dependence of $\overset{\sim}{G}{(\theta)}$ on $\theta$.

<!-- chunk {"id": "body-0034", "role": "body", "section": "Assumption 1", "weight": 1.0} -->

The following lemma analyses the case when $\mathbf{f}_{\theta}$ is a Gaussian distribution^11^1In principle, any $\mathbf{f}_{\theta}$ with mean $\mu_{\theta}$ and covariance $\sigma_{\theta}^{2}I_{p}$ would suffice. However, it would need more investigation further down the line for giving probabilistic guarantees. So, Gaussian distribution is preferred for the ease of exposition. and shows that the Bézout identity still holds under Gaussian parameter uncertainty.

<!-- chunk {"id": "body-0035", "role": "body", "section": "Assumption 2", "weight": 1.0} -->

The mapping $\theta\mapsto{\overset{\sim}{G}{(\theta)}}$ is Lipschitz in terms of the $\mathcal{H}_{\infty}$ norm with constant $\mathbf{L}_{\overset{\sim}{G}} > 0$, such that From assumption 2 ‣ 3 Solution Methodology ‣ Probabilistic Robustness in the Gap Metric"), we immediately see that the projection operator $\Pi_{\mathcal{G}_{\overset{\sim}{\Sigma}{(\theta)}}}$ also continuously varies with respect to $\theta$. Hence, it's operator norm would be well-defined. Having mentioned all the assumptions needed, we will begin our study about giving probabilistic guarantees for robust performance and robust stability in terms of the gap metric.

<!-- chunk {"id": "body-0036", "role": "body", "section": "Probabilistic Guarantee for Coprime Factor Uncertainty", "weight": 1.0} -->

Coprime factor uncertainty can be understood as a combination of multiplicative and inverse multiplicative type uncertainties and the trade off between them is determined by the nominal plant. As a precursor to the gap metric, we will first demonstrate how the randomness in the co-prime factor uncertainty affects the robust stability associated with the nominal controller stabilising the nominal plant. The following theorem (probabilistic extension of Theorem 1 in ) gives probabilistic guarantees on the nominal controller stabilising the perturbed plant under random coprime factor uncertainty.

<!-- chunk {"id": "body-0037", "role": "body", "section": "Inferring the Lipschitz Constant of ${Gap}{(\\theta)}$", "weight": 1.0} -->

When ${Gap}{(\theta)}$ is random, it essentially reflects the uncertainty in how the two graph subspaces $\mathcal{G}_{\overline{\Sigma}},\mathcal{G}_{\overset{\sim}{\Sigma}{(\theta)}}$ are aligned with each other. Towards this perspective, we will now study about the Lipschitz constant associated with the gap ${Gap}{(\theta)}$ in the following theorem.

<!-- chunk {"id": "body-0038", "role": "body", "section": "Inferring the Expected Value of ${Gap}{(\\theta)}$", "weight": 1.0} -->

Given that $\theta \sim {\mathcal{N}{(\mu_{\theta},{\sigma_{\theta}^{2}I_{p}})}}$, we leverage the fact that mean $\mu_{\theta}$ and covariance $\sigma_{\theta}^{2}I_{p}$ are deterministic known quantities to get an upper bound for the expected gap in terms of the them. We state the following proposition using the Jensen's inequality from which we will use later.

<!-- chunk {"id": "body-0039", "role": "body", "section": "Probabilistic Robust Stability Guarantees", "weight": 1.0} -->

Having explored the bounds on the expected value of the ${Gap}{(\theta)}$, we are interested in studying about a nominal controller's robust stability property while stabilising a nominal plant. Particularly, we will investigate the probability of a nominal controller stabilising a random plant using the above obtained gap metric bounds. This will provide probabilistic controller certification under non-zero mean gap uncertainty.

<!-- chunk {"id": "body-0040", "role": "body", "section": "Connecting Robust Stability & Violation Probability", "weight": 1.0} -->

If we want the stabilisation of $\overset{\sim}{\Sigma}{(\theta)}$ by nominal controller $\overline{C}$ to happen with a probability of at least $1 - \beta$, where $\beta \in {}$ denotes the violation probability, then using Theorem 7, we can find a corresponding condition on the expected value of the ${Gap}{(\theta)}$ in terms of $\beta$. The following corollary formally establishes that result.

<!-- chunk {"id": "body-0041", "role": "body", "section": "Numerical Demonstration", "weight": 1.0} -->

To demonstrate the probabilistic robust stability guarantees obtained in this subsection, we considered a nominal system $\overline{\Sigma}:{{(A,B,C,D)} = {({- 1},1,1,0)}}$. We sampled $N = 10^{4}$ values of the uncertain parameter $\theta \sim {\mathcal{N}{(\begin{bmatrix} \end{bmatrix},{0.25^{2}I_{2}})}}$. The perturbed plants were formed as ${\overset{\sim}{\Sigma}{(\theta^{(i)})}} = {({{- 1} + \theta_{1}^{(i)}},1,{1 + \theta_{2}^{(i)}},0)}$ for $i = {1,\ldots,N}$.

<!-- chunk {"id": "body-0042", "role": "body", "section": "Numerical Demonstration", "weight": 1.0} -->

After doing a Monte-carlo simulation using $N$ independent trials involving samples of $\theta$, the results are shown in Figure 2. Using (41 ‣ 3 Solution Methodology ‣ Probabilistic Robustness in the Gap Metric")), we estimated ${{\mathbb{E}}{\lbrack{{Gap}{(\theta)}}\rbrack}} = 0.3032$. The performance measure was $b_{\overline{\Sigma},\overline{C}} = 0.7071$ for the nominal controller $\overline{C}$ that placed the closed loop poles at $- 2$. Empirically, we found ${{\mathbb{P}}{({{{Gap}{(\theta)}} < b_{\overline{\Sigma},\overline{C}}})}} = 0.9777$ which was greater than the lower bound of $0.5561$ from and thereby validating the claims of Theorem 7.

<!-- chunk {"id": "body-0043", "role": "body", "section": "Probabilistic Closed Loop Deviation Guarantees", "weight": 1.0} -->

Given that we have investigated the probabilistic guarantees of the gap ${Gap}{(\theta)}$ greater than some threshold in Theorem 4 ‣ 3 Solution Methodology ‣ Probabilistic Robustness in the Gap Metric") and probabilistic robust stability guarantees in Theorem 7, we now turn our attention to give probabilistic closed loop deviation guarantees. Before proceeding further, we require an assumption on the Lipschitz continuity of $\left. \parallel{Q{({\overset{\sim}{\Sigma}{(\theta)}},\overline{C})}}\parallel \right._{\mathcal{H}_{\infty}}$ with respect to parameter $\theta \sim {\mathcal{N}{(\mu_{\theta},{\sigma_{\theta}^{2}I_{p}})}}$.

<!-- chunk {"id": "body-0044", "role": "body", "section": "Assumption 3", "weight": 1.0} -->

Remarks: This is a mild and valid assumption to make as usually the system matrices ${A{(\theta)}},{B{(\theta)}},{C{(\theta)}}$ of the perturbed model $\overset{\sim}{\Sigma}{(\theta)}$ depend smoothly on $\theta$ (are Fréchet differentiable in $\mathcal{H}_{\infty}$ norm with respect to $\theta$), and the function $\mathbf{f}_{\mathbf{Q}}{(\theta)}$ is formed through algebraic and analytic operations on these matrices. Further, we had also earlier restricted our study to the case where the closed-loop remains internally stable over all realizations of $\theta \sim {\mathcal{N}{(\mu_{\theta},{\sigma_{\theta}^{2}I_{p}})}}$.

<!-- chunk {"id": "body-0045", "role": "body", "section": "Assumption 3", "weight": 1.0} -->

Hence, the map $\theta\mapsto{\mathbf{f}_{\mathbf{Q}}{(\theta)}}$ is differentiable and hence Lipschitz on the space of $\theta$. Since Gaussian distributions concentrate their mass near the mean, any potential growth in the Lipschitz constant outside compact sets has negligible impact. Thus, global Lipschitz continuity of $\mathbf{f}_{\mathbf{Q}}{(\theta)}$ is a conservative yet reasonable assumption to make and it enables rigorous probabilistic analysis.

<!-- chunk {"id": "body-0046", "role": "body", "section": "Assumption 3", "weight": 1.0} -->

Using the following theorem, we will now give probabilistic closed loop deviation bound under the action of controller $\overline{C}$.

<!-- chunk {"id": "body-0047", "role": "body", "section": "Probabilistic $\\mathcal{H}_{\\infty}$ Performance Guarantees", "weight": 1.0} -->

We will now connect all the above results with Problem 2 in the below theorem.

<!-- chunk {"id": "body-0048", "role": "body", "section": "Numerical Simulation", "weight": 1.0} -->

Consider the following nominal SISO system model $\overline{\Sigma}:{{(A,B,C,D)} = {({- 1},1,1,0)}}$ which corresponds to the following state space form: We obtained the nominal controller $\overline{C}$ by placing the poles of $\overline{\Sigma}$ at $- 2$. The value of performance measure was found to be $b_{\overline{\Sigma},\overline{C}} = 0.7071$ and $\gamma$ values were varied between $\lbrack 1.01,3\rbrack$. We obtained $N = 10^{4}$ samples of $\theta \sim {\mathcal{N}\left(\begin{bmatrix} \end{bmatrix},{\sigma_{\theta}^{2}I_{2}} \right)}$, with $\sigma_{\theta} = 0.5$.

<!-- chunk {"id": "body-0049", "role": "body", "section": "Numerical Simulation", "weight": 1.0} -->

The result is shown in Figure 3.\Doing a Monte-carlo style simulation by generating $N = 10^{4}$ different independent instances of the perturbed plant models $\overset{\sim}{\Sigma}{(\theta)}$, we estimated the Lipschitz constant of the perturbed model $\overset{\sim}{\Sigma}{(\theta)}$ with respect to $\theta$ as $\mathbf{L}_{gap} = 0.5308$. Further, we estimated ${{\mathbb{E}}\left\lbrack {{Gap}{(\theta)}} \right\rbrack} = 0.3204$ and its upper bound $C_{gap} = 0.4023$ using (39 ‣ 3 Solution Methodology ‣ Probabilistic Robustness in the Gap Metric")). Further, the ${\mathbb{E}}\left\lbrack \left.

<!-- chunk {"id": "body-0050", "role": "body", "section": "Numerical Simulation", "weight": 1.0} -->

\parallel{T_{zw}{({\overset{\sim}{\Sigma}{(\theta)}},\overline{C})}}\parallel \right._{\mathcal{H}_{\infty}} \right\rbrack$ was estimated to be $0.5557$ and its conservative upper bound from in Theorem 12 was $4.8592$. As noted previously, this is a conservative estimate given the simple upper bound used in Theorem 12.

<!-- chunk {"id": "body-0051", "role": "body", "section": "Connections to Existing Probabilistic Robust Control (PRC) Theory", "weight": 1.0} -->

The analysis of stochastic robustness of LTI systems started in where authors studied a very similar problem as in and gave estimates of stability probability density functions for systems affected by uncertain parameters. On the other hand, PRC approaches gained traction further later on using probabilistic methods to give guarantees on system stability and performance (see and the references therein for further details on this topic.). Having said that one might be interested on seeing what is new with the approach proposed in this paper regarding PRC and what new perspectives does this bring to the already existing table of approaches for PRC theory. Existing PRC theories utilise the stability margins to gauge the stability of the controller-plant pair, while the approach considered in this paper ties everything like stability and performance nicely with the ${Gap}{(\theta)}$ and gives probabilistic guarantees.

<!-- chunk {"id": "body-0052", "role": "body", "section": "Connecting Random Gap & Scenario-Based Robustness", "weight": 1.0} -->

In scenario-based approaches, one works with just the finite number of samples of uncertainties possibly from an unknown generating distribution to do both the reliability estimation and performance estimation in the context of PRC setting considered. To connect the scenario-based approach with our random gap based problem formulation, we will deviate from the assumption that the distribution of the uncertain parameter $\theta$ is known in this section meaning that $\mathbf{f}_{\theta}$ is not necessarily equal to $\mathcal{N}{(\mu_{\theta},{\sigma_{\theta}^{2}I_{p}})}$. We have the following assumption in place in regards to that.

<!-- chunk {"id": "body-0053", "role": "body", "section": "Assumption 4", "weight": 1.0} -->

Assumption 4 Theory ‣ Probabilistic Robustness in the Gap Metric") just says that we have $N$ samples of $\theta$ available for decision making. We know that if $N\rightarrow\infty$, it means that we essentially know the distribution $\mathbf{f}_{\theta}$ exactly and thereby getting rid of the uncertainty associated with distribution of $\theta$ in assumption 4 Theory ‣ Probabilistic Robustness in the Gap Metric"). On the other hand, if we were to give probabilistic guarantees on the nominal controller stabilising a random plant based on just the available $N$ samples of $\theta$, then the resulting probability will be determined by $N$. Usually, a failure or a violation probability is given apriori and we need to find a connection between that violation probability and the number of samples $N$ to give probabilistic guarantees. The following theorem nicely establishes a connection by leveraging the power of scenario-based approaches to give finite sample-based guarantees on the gap-metric based robust stability.

<!-- chunk {"id": "body-0054", "role": "body", "section": "Interpretation of Confidence and Probabilistic Robustness", "weight": 1.0} -->

The probabilistic robustness guarantee obtained through scenario-based method in (65 Theory ‣ Probabilistic Robustness in the Gap Metric")) of Theorem 13 Theory ‣ Probabilistic Robustness in the Gap Metric") involves two distinct sources of randomness namely, *Randomness from $\mathbf{f}_{\theta}$ (Probabilistic Robustness):* The term ${{\mathbb{P}}\left({{{Gap}{(\theta)}} > {\hat{\alpha}}_{N}} \right)} \leq \epsilon$ describes the probability (under the unknown $\mathbf{f}_{\theta}$ of $\theta$) that a randomly chosen uncertain plant model $\overset{\sim}{\Sigma}{(\theta)}$ results in the gap exceeding threshold ${\hat{\alpha}}_{N}$.

<!-- chunk {"id": "body-0055", "role": "body", "section": "Interpretation of Confidence and Probabilistic Robustness", "weight": 1.0} -->

*Randomness from Scenario Sampling (Confidence):* Since the scenarios ${\{\theta^{(i)}\}}_{i = 1}^{N}$ are drawn randomly from the unknown $\mathbf{f}_{\theta}$, the scenario-based gap threshold ${\hat{\alpha}}_{N}$ given by (68 Theory ‣ Probabilistic Robustness in the Gap Metric")) itself is random. Hence, the event ${{\mathbb{P}}\left( {{{Gap}{(\theta)}} > {\hat{\alpha}}_{N}} \right)} \leq \epsilon$ is also random. The confidence level $1 - \beta$ quantifies the probability (over repeated scenario samplings) that the scenario-based threshold correctly achieves the probabilistic robustness guarantee.

<!-- chunk {"id": "body-0056", "role": "body", "section": "Interpretation of Confidence and Probabilistic Robustness", "weight": 1.0} -->

Thus, the probabilistic robustness guarantee is itself a random quantity due to scenario sampling, and the confidence level quantifies our trust to obtain a good scenario-based threshold.

<!-- chunk {"id": "body-0057", "role": "body", "section": "Numerical Simulation", "weight": 1.0} -->

In order to demonstrate the connection of the random gap with the scenario-based robustness established in Theorem 13 Theory ‣ Probabilistic Robustness in the Gap Metric"), we considered a nominal system $\overline{\Sigma}:\frac{1}{s + 1}$ and a perturbed system ${\overset{\sim}{\Sigma}{(\theta)}} = \frac{1}{s + {({1 + \theta})}}$, where $10^{4}$ samples of $\theta$ were sampled from $\mathcal{N}{(0,0.25^{2})}$. We chose a violation probability of $\epsilon = 0.05$ and a confidence level parameter of $\beta = 0.01$. For the nominal controller $\overline{C} = \frac{({s + 2})}{2{({s + 3})}}$, the performance measure was $b_{\overline{\Sigma},\overline{C}} = 0.8944$.

<!-- chunk {"id": "body-0058", "role": "body", "section": "Numerical Simulation", "weight": 1.0} -->

Given a violation probability of $\epsilon = 0.05$ and a confidence level of $\beta = 0.01$, the sample size condition from (64 Theory ‣ Probabilistic Robustness in the Gap Metric")) resulted in $N \geq 90$. By running a Monte-carlo simulation using $10^{4}$ instances of $\theta$ generated as mentioned above, the results are plotted in Figure 4 Theory ‣ Probabilistic Robustness in the Gap Metric").

<!-- chunk {"id": "body-0059", "role": "body", "section": "Numerical Simulation", "weight": 1.0} -->

We observed that ${\hat{\alpha}}_{N} = 0.7019$ which was less than $b_{\overline{\Sigma},\overline{C}} = 0.8944$. This ensured that from Theorem 13 Theory ‣ Probabilistic Robustness in the Gap Metric") that the condition ${{Gap}{(\theta)}} \leq {\hat{\alpha}}_{N}$ holding with probability of at least ${1 - \epsilon} = 0.95$ implied that the nominal controller $\overline{C}$ would stabilise the random plant $\overset{\sim}{\Sigma}{(\theta)}$ with probability of at least the same value of ${1 - \epsilon} = 0.95$. As mentioned earlier, the confidence level $1 - \beta$ quantifies the probability (over repeated scenario samplings) that the scenario-based threshold correctly achieves the probabilistic robustness guarantee.

<!-- chunk {"id": "body-0060", "role": "body", "section": "Numerical Simulation", "weight": 1.0} -->

That is, if we repeatedly draw new sets of $N \geq 90$ samples, then in at least $100{{({1 - \beta})}\%}$ of these repetitions, the computed scenario threshold ${\hat{\alpha}}_{N}$ will ensure a true violation probability no greater than $\epsilon$. On the other hand, when the covariance strength of $\theta$ was increased to $0.5^{2}$ from $0.25^{2}$, we were able to see some unstable perturbed plants being generated meaning that ${Gap}{(\theta)}$ and hence ${\hat{\alpha}}_{N}$ became equal to $1$ for those samples of $\theta$.

<!-- chunk {"id": "body-0061", "role": "body", "section": "Numerical Simulation", "weight": 1.0} -->

Note that even under such unstable case, (65 Theory ‣ Probabilistic Robustness in the Gap Metric")) would hold true but unfortunately (66 Theory ‣ Probabilistic Robustness in the Gap Metric")) will not hold as $\underset{= 1}{\underbrace{{\max_{i={1,\ldots,N}}⁡{Gap}}⁢{(\theta^{(i)})}}} > \underset{= 0.8944}{\underbrace{b_{\overline{\Sigma},\overline{C}}}}$.

<!-- chunk {"id": "body-0062", "role": "body", "section": "Conclusion & Future Outlook", "weight": 1.5} -->

When a random parameter affects a linear system, we studied how it manifested itself as the associated random gap between the nominal model of the system (without any uncertainty) and the perturbed model of the system (with uncertainty). The randomness in the associated gap resulted in probabilistic versions of the corresponding performance guarantees and stability margins guarantees measured in terms of the gap. This new perspective on PRC using the random gap provides us information about upper bounds on the expected gap quantity and the expected $\mathcal{H}_{\infty}$ achievable performance level apriori for any stabilising controller. A connection to the existing tools on PRC using scenario-based approach was also presented in this paper. The results obtained in this paper nicely blends the high dimensional statistics tool with the random gap problem formulation and gives probabilistic guarantees on both gap metric based robust performance and robust stability.\The aim of this paper is to revive the research on PRC theory. Future research prospects look very promising and there are many interesting open research questions along the lines of the research presented in this paper. We list here few of them which we believe can be immediately pursued given the existing developments done in this manuscript.

<!-- chunk {"id": "body-0063", "role": "body", "section": "Conclusion & Future Outlook", "weight": 1.5} -->

Obtain probabilistic guarantees on gap metric by investigating the randomness in the projection operator.

<!-- chunk {"id": "body-0064", "role": "body", "section": "Conclusion & Future Outlook", "weight": 1.5} -->

Investigate and give bounds on the expected distance between $\delta_{g}{(\overline{C},{C{(\theta)}})}$, where $C{(\theta)}$ would be the controller which will result in same performance measure for the perturbed system $\overset{\sim}{\Sigma}{(\theta)}$ as $\overline{C}$ did for the nominal system $\overline{\Sigma}$ meaning that $b_{{\overset{\sim}{\Sigma}{(\theta)}},{C{(\theta)}}} = b_{\overline{\Sigma},\overline{C}}$. This would inform us how much the respective controllers that guarantee same performance level for the nominal and perturbed plants are further apart in the expected sense.

<!-- chunk {"id": "body-0065", "role": "body", "section": "Conclusion & Future Outlook", "weight": 1.5} -->

An important future research direction would be to formulate and compute the distance between two stochastic dynamical systems $\delta_{gap}{({{\overset{\sim}{\Sigma}}_{1}{(\theta)}},{{\overset{\sim}{\Sigma}}_{2}{(\theta)}})}$ where the uncertainty in each system is described using the random gap metric between its respective nominal model and the perturbed model.

<!-- chunk {"id": "body-0066", "role": "body", "section": "Conclusion & Future Outlook", "weight": 1.5} -->

Another important research direction will be to extend the problem setting to both linear time varying systems and to nonlinear systems by formulating the quantity of interest namely the gap between the nominal and the corresponding perturbed system models as random.

<!-- chunk {"id": "body-0067", "role": "body", "section": "Conclusion & Future Outlook", "weight": 1.5} -->

Another interesting direction is to first develop gap metric based robust tube model predictive control (MPC). The uncertainty around the system trajectories from the true but unknown perturbed model different from the nominal model is characterised along the prediction horizon using the assumed gap between the nominal $(\overline{P})$ and the perturbed system $(P)$ (by formulating linear matrix inequality (LMI) constraints for the condition ${\delta_{g}{(P,\overline{P})}} \leq \alpha$ for a given $\alpha \in {}$). Using the random gap based problem formulation considered in this manuscript, the deterministic gap metric based robust tube MPC can be even extended further to gap metric based stochastic tube MPC setting.
