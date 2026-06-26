<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

First-Order Pontryagin Maximum Principle for Risk-Averse Stochastic Optimal Control Problems

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

In this paper, we derive first-order Pontryagin optimality conditions for risk-averse stochastic optimal control problems subject to final time inequality constraints, and whose costs are general, possibly non-smooth finite coherent risk measures. Unlike preexisting contributions covering this situation, our analysis holds for classical stochastic differential equations driven by standard Brownian motions. In addition, it presents the advantages of neither involving second-order adjoint equations, nor leading to the so-called weak version of the PMP, in which the maximization condition with respect to the control variable is replaced by the stationarity of the Hamiltonian.

<!-- chunk {"id": "body-0003", "role": "body", "section": "Introduction", "weight": 1.5} -->

In the last decades, risk-averse stochastic optimal control has seen a surge of interest as a tool for designing control laws that enjoy robustness properties against uncertainties. Relevant applications of this theory encompass broad research fields, ranging from risk-averse financial investments to the safe control of autonomous systems, as evidenced e.g. by the recent monographs and their bibliography. In this context, first-order necessary conditions for optimality in the form of Pontryagin's Maximum Principle (we will refer to these latter as "risk-averse PMP" in the sequel) are bound to play a key role in characterizing and numerically computing optimal control strategies, as it is known to be the case for classical stochastic optimal control problems in which only expectation-based costs and constraints are considered. However, extending the PMP in its general form to more involved risk-averse settings still requires substantial investigations.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

To the best of our knowledge, the derivation of a risk-averse PMP was attempted firstly, where appropriate adjoint equations and maximality conditions formulated in terms of the so-called $G$-Stochastic calculus are introduced in order to cope with the presence of risk measures. This framework was originally introduced by Peng, and developed by the stochastic control community later, see e.g.. In this setting, the standard Brownian motion is replaced by a so-called $G$-Brownian motion, which is modelled as a stochastic process whose distribution is the product of a standard Gaussian and a Lipschitz map, and whose role is to transform the coherent risk measure into a standard, though non-linear expectation. While practical for some applications, this procedure requires to change the dynamics of the system, which is not always natural e.g. when the diffusion term aims at rendering an unknown uncertainty exerted on the system by the environment. Therefore, for certain classes of problems, it is still relevant to investigate optimality conditions relying on standard stochastic calculus, and which do not require to infuse additional uncertainty in the formulation of the control problem.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

Along this line, a risk-averse PMP for problems which are subject to stochastic differential equations stemming from classical Wiener processes is proposed, though no final constraints are included therein and the underlying risk measures are assumed to be continuously Fréchet differentiable. From a different standpoint, first-order necessary optimality conditions for convex risk-averse optimization problems subject to partial differential equations and general subdifferentiable risk-measure-based costs are derived, by leveraging classical tools from convex analysis. Nevertheless, final constraints are also ruled out in this work, and the necessary conditions for optimality are written down as simple Euler conditions and not as a general Karush-Kuhn-Tucker system, which would be the natural "static" counterpart of the PMP.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

In this paper, we propose a first step towards bridging the aforedescribed gap by establishing a first-order risk-averse PMP for a class of finite-dimensional constrained stochastic optimal control problems. Therein, one aims at minimizing a final cost modelled as a general subdifferentiable coherent risk measure over a class of admissible trajectories driven by a controlled stochastic differential equations involving standard Wiener processes, and subject to final time inequality constraints. Our proof leverages a general methodology that was first developed, allowing for a natural extension of the first-order PMP for stochastic optimal control problems with expectation-based costs discussed in to the risk-averse setting. Specifically, the main advantages offered by this approach over more classical needle-like variations or Ekeland's principle-based methods are twofold. Firstly, no additional second-order adjoint variables (nor related second-order adjoint equations) are required to establish a fully informative PMP. Secondly, it permits the derivation of the so-called strong maximum principle, in which the optimal controls are characterized as being pointwise maximizers of the Hamiltonian.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

This is in contrast with some reference contributions in stochastic optimal control that establish weaker variants of the PMP in which the maximization condition is relaxed by requiring the stationarity of the Hamiltonian. In what follows, we propose two separate sets of optimality conditions for the class of optimal control problems at hand, depending on whether the control variable appears in the diffusion term or not. When the control acts only on the deterministic drift, the variational linearization techniques subtending the proof of the maximum principle can be performed much like in the deterministic case, by considering perturbations which are tangent to the set of relaxed velocities. When the diffusion is controlled, however, it is not possible to replicate such a strategy as the Itô integral does not exhibit the nice convexifying effects of the Lebesgue or Bochner integrals -- a fact which is expounded by an original example in Remark 2.15.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Introduction", "weight": 1.5} -->

‣ 2.4 Stochastic Differential Inclusions ‣ 2 Preliminaries ‣ First-Order Pontryagin Maximum Principle for Risk-Averse Stochastic Optimal Control Problems") --, and one thus needs to impose an a priori convexity assumptions on the sets of admissible drift and diffusion pairs, similar to that considered e.g..

<!-- chunk {"id": "body-0009", "role": "body", "section": "Introduction", "weight": 1.5} -->

The paper is organized as follows. In Section 2, we recollect known concepts of stochastic calculus and set-valued analysis, which feature a counterexample to Aumann's theorem for the Itô integral that we believe to be of independent interest. In Section 3, we expose the main contributions of this article, which are first-order Pontryagin optimality conditions for risk-averse stochastic optimal control problems. We start in Section 3.1 with the case in which the diffusion term of the driving stochastic dynamics is controlled, and expose the proof in great details in this context. We then show in Section 3.2 how the aforeproposed methodology can be used to prove the PMP under more general assumptions when the diffusion term is control-free, and close the paper with Sections 4 and 5 which respectively contain some application examples and important perspectives.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Stochastic Calculus", "weight": 1.0} -->

Throughout this article, we will consider random variables defined over a probability space $(\Omega,\mathcal{G},{\mathbb{P}})$. For any sub $\sigma$-algebra $\mathcal{S} \subset \mathcal{G}$, we denote by $L_{\mathcal{S}}^{\beta}{(\Omega,{\mathbb{R}}^{n})}$ the Banach space of random variables $z:{\Omega\rightarrow{\mathbb{R}}^{n}}$ which are $\mathcal{S}$-measurable and such that where $\parallel \cdot \parallel$ denotes the Euclidean norm.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Stochastic Calculus", "weight": 1.0} -->

In the sequel given $t \in {\lbrack 0,T\rbrack}$, we will often use the standard notation ${x{(t)}}:{\Omega\rightarrow{\mathbb{R}}^{n}}$ to refer to progressively measurable processes. In addition, when we say that a property holds "almost everywhere", it shall always be understood with respect to the progressive $\sigma$-algebra generated by the filtration $\mathcal{F}$ on ${\lbrack 0,T\rbrack} \times \Omega$.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Stochastic Differential Equations", "weight": 1.0} -->

In what follows, we detail the setting in which we study controlled stochastic dynamics. Let $U \subset {\mathbb{R}}^{m}$ be a compact set representing admissible control values, and consider a stochastic drift mapping $f:{{{\lbrack 0,T\rbrack} \times \Omega \times {\mathbb{R}}^{n} \times U}\rightarrow{\mathbb{R}}^{n}}$ as well as a stochastic diffusion mapping $\sigma:{{{\lbrack 0,T\rbrack} \times \Omega \times {\mathbb{R}}^{n} \times U}\rightarrow{\mathbb{R}}^{n \times d}}$ which satisfy the following series of standard assumptions (see e.g. \[22, Chapter 3.3\]).

<!-- chunk {"id": "body-0013", "role": "body", "section": "Main Assumptions on the Stochastic Dynamics -- (MSD)", "weight": 1.0} -->

are progressively measurable for every ${(x,u)} \in {{\mathbb{R}}^{n} \times U}$ and the maps are continuous for almost every ${(t,\omega)} \in {{\lbrack 0,T\rbrack} \times \Omega}$.

<!-- chunk {"id": "body-0014", "role": "body", "section": "Main Assumptions on the Stochastic Dynamics -- (MSD)", "weight": 1.0} -->

There exists a map $k \in {L_{\mathcal{F}}^{2}{({{\lbrack 0,T\rbrack} \times \Omega},{\mathbb{R}}_{+})}}$ such that ^11^1Note that since $U \subset {\mathbb{R}}^{m}$ is compact, this assumption encompasses control-affine dynamics. for almost every ${(t,\omega)} \in {{\lbrack 0,T\rbrack} \times \Omega}$ and each $u \in U$.

<!-- chunk {"id": "body-0015", "role": "body", "section": "Main Assumptions on the Stochastic Dynamics -- (MSD)", "weight": 1.0} -->

For almost every ${(t,\omega)} \in {{\lbrack 0,T\rbrack} \times \Omega}$ and all $u \in U$, the mappings are Fréchet differentiable, and there exists a constant $L > 0$ such that for almost every ${(t,\omega)} \in {{\lbrack 0,T\rbrack} \times \Omega}$, any $u \in U$ and all ${x,y} \in {\mathbb{R}}^{n}$.

<!-- chunk {"id": "body-0016", "role": "body", "section": "Main Assumptions on the Stochastic Dynamics -- (MSD)", "weight": 1.0} -->

From now, we fix an initial condition $x_{0} \in {L_{\mathcal{F}_{0}}^{2}{(\Omega,{\mathbb{R}}^{n})}}$. Under hypotheses (MSD). ‣ 2.2 Stochastic Differential Equations ‣ 2 Preliminaries ‣ First-Order Pontryagin Maximum Principle for Risk-Averse Stochastic Optimal Control Problems"), the stochastic differential equation has a unique (up to stochastic indistinguishability) solution $x_{u} \in {C_{\mathcal{F}}^{2}{({{\lbrack 0,T\rbrack} \times \Omega},{\mathbb{R}}^{n})}}$ for every progressively measurable control $u:{{{\lbrack 0,T\rbrack} \times \Omega}\rightarrow U}$.

<!-- chunk {"id": "body-0017", "role": "body", "section": "Main Assumptions on the Stochastic Dynamics -- (MSD)", "weight": 1.0} -->

In the following lemma, we recall a useful estimate for this class of dynamics (see e.g. \[14, Proposition 2.1\]).

<!-- chunk {"id": "body-0018", "role": "body", "section": "Set-valued Analysis", "weight": 1.0} -->

In the sequel given a closed set $K \subset {\mathbb{R}}^{n}$, we define its closed convex hull by If the set $K$ is convex, we shall denote its tangent cone at some $x \in K$ by where ${\text{dist}_{K}{(x)}}:={\inf_{y \in K}{\|{x - y}\|}}$ denotes the distance from a point $x \in {\mathbb{R}}^{n}$ to $K$.

<!-- chunk {"id": "body-0019", "role": "body", "section": "Set-valued Analysis", "weight": 1.0} -->

We will write $F:{{{\lbrack 0,T\rbrack} \times \Omega}\rightrightarrows{\mathbb{R}}^{n}}$ to denote a set-valued map -- or multifunction -- from ${\lbrack 0,T\rbrack} \times \Omega$ into ${\mathbb{R}}^{n}$, namely a mapping valued in the subsets of ${\mathbb{R}}^{n}$. In this context, we shall say that $F$ has closed, compact or convex images if its values are closed, compact or convex sets respectively.

<!-- chunk {"id": "body-0020", "role": "body", "section": "Remark 2.10 (Concerning progressively measurable selections)", "weight": 1.0} -->

Observe that since ${\mathcal{B}{({\lbrack 0,T\rbrack})}} \otimes \mathcal{G}$ endowed with the progressive $\sigma$-algebra induced by the filtration $\mathcal{F}$ is not a complete measure space, one cannot directly apply \[2, Corollary 8.2.13, Theorem 8.5.1 and Corollary 8.5.2\] to derive Theorem 2.9. ‣ 2.3 Set-valued Analysis ‣ 2 Preliminaries ‣ First-Order Pontryagin Maximum Principle for Risk-Averse Stochastic Optimal Control Problems").

<!-- chunk {"id": "body-0021", "role": "body", "section": "Remark 2.10 (Concerning progressively measurable selections)", "weight": 1.0} -->

To overcome this difficulty, one needs first to apply these latter results to the measure-theoretic completion $\overline{{\mathcal{B}{({\lbrack 0,T\rbrack})}}\otimes\mathcal{G}}$ to obtain measurable selections, and modify them on a negligible set so that they become measurable in ${\mathcal{B}{({\lbrack 0,T\rbrack})}} \otimes \mathcal{G}$ (see also \[8, Theorem 4.1\]).

<!-- chunk {"id": "body-0022", "role": "body", "section": "Remark 2.11 (Shorter notation for stochastic processes)", "weight": 1.0} -->

For the sake of conciseness, we will often drop the dependence with respect to the parameter $\omega \in \Omega$ and write $t \in {\lbrack 0,T\rbrack}\mapsto{f{(t)}} \in {F{(t,{x{(t)}})}}$ for progressively measurable selections and maps.

<!-- chunk {"id": "body-0023", "role": "body", "section": "Remark 2.11 (Shorter notation for stochastic processes)", "weight": 1.0} -->

We end this preliminary section by recalling an adaptation of a general minimax theorem due to Sion.

<!-- chunk {"id": "body-0024", "role": "body", "section": "Stochastic Differential Inclusions", "weight": 1.0} -->

In this section, we recollect some facts concerning set-valued stochastic dynamics.

<!-- chunk {"id": "body-0025", "role": "body", "section": "Stochastic Differential Inclusions", "weight": 1.0} -->

Given a progressively measurable-Lipschitz set-valued map $F:{{{\lbrack 0,T\rbrack} \times \Omega \times {\mathbb{R}}^{n}}\rightrightarrows{\mathbb{R}}^{n + {d \times n}}}$ with nonempty compact images, we say that $x \in {C_{\mathcal{F}}^{2}{({{\lbrack 0,T\rbrack} \times \Omega},{\mathbb{R}}^{n})}}$ solves the stochastic differential inclusion if there exists a progressively measurable selection $t \in {\lbrack 0,T\rbrack}\rightrightarrows{({f{(t)}},{\sigma{(t)}})} \in {F{(t,{x{(t)}})}}$ such that As for deterministic differential inclusion, this class of dynamics enjoys an existence result "à la Filippov", which incorporates handy a

<!-- chunk {"id": "body-0026", "role": "body", "section": "Stochastic Differential Inclusions", "weight": 1.0} -->

priori distance estimates with respect to a given process. This is the object of the following theorem, whose proof can be established up to a small variation of the arguments proposed.

<!-- chunk {"id": "body-0027", "role": "body", "section": "Remark 2.15 (Obstruction to relaxation for general stochastic inclusions)", "weight": 1.0} -->

The relaxation theorem for stochastic differential inclusions of the form (SDI') stems from Aumann's famed convexity principle for the Lebesgue -- or more generally the Bochner -- integral (see e.g. \[2, Theorem 8.6.4\]).

<!-- chunk {"id": "body-0028", "role": "body", "section": "Remark 2.15 (Obstruction to relaxation for general stochastic inclusions)", "weight": 1.0} -->

The latter asserts that, given a Borel set $I \subset {\lbrack 0,T\rbrack}$, a real number $\beta \in {\lbrack 1,{+ \infty})}$, an integrably bounded progressively measurable set-valued map $F:{{I \times \Omega}\rightrightarrows{\mathbb{R}}^{n}}$ with closed nonempty images and a progressive selection $t \in I\mapsto{f{(t)}} \in {\overline{\text{co}}F{(t)}}$, there exists for each $\varepsilon > 0$ another progressively measurable selection $t \in I\mapsto f_{\varepsilon} \in {F{(t)}}$ such that Unfortunately, as evidenced by the following elementary counterexample, such an identity does not hold for the Itô integral.

<!-- chunk {"id": "body-0029", "role": "body", "section": "Remark 2.15 (Obstruction to relaxation for general stochastic inclusions)", "weight": 1.0} -->

Indeed, consider the constant set-valued map ${(t,\omega)} \in {{\lbrack 0,1\rbrack} \times \Omega}\rightrightarrows F \subset {\mathbb{R}}^{2}$ defined by which is clearly integrably bounded with nonempty compact images. Fixing the constant selection $t \in {\lbrack 0,1\rbrack}\mapsto{f{(t)}}:={(\frac{1}{2},1)} \in {\overline{\text{co}}F{(t)}}$, it follows from Itô's isometry formula (see e.g. \[13, Expression (5.8)\]) that for each $\varepsilon > 0$ and any progressively measurable selection $t \in {\lbrack 0,1\rbrack}\mapsto{f_{\varepsilon}{(t)}} \in {F{(t)}}$. This violates (2.5.

<!-- chunk {"id": "body-0030", "role": "body", "section": "Remark 2.15 (Obstruction to relaxation for general stochastic inclusions)", "weight": 1.0} -->

‣ 2.4 Stochastic Differential Inclusions ‣ 2 Preliminaries ‣ First-Order Pontryagin Maximum Principle for Risk-Averse Stochastic Optimal Control Problems")) for each $\beta \in {\lbrack 2,{+ \infty})}$ by Hölder's inequality, whereas a simple contradiction argument based on both reverse dominated convergence and Egoroff theorems also yields the obstruction for $\beta \in {\lbrack 1,2)}$.

<!-- chunk {"id": "body-0031", "role": "body", "section": "Remark 2.15 (Obstruction to relaxation for general stochastic inclusions)", "weight": 1.0} -->

To illustrate the contrast with the Lebesgue integral, notice that in this example one can very easily find progressively measurable selections $t \in {\lbrack 0,T\rbrack}\mapsto{\overset{\sim}{f}{(t)}} \in {F{(t)}}$ which satisfy by choosing for instance ${\overset{\sim}{f}{(t)}}:={{\mathbb{1}_{\lbrack 0,{1/2}\rbrack}{(t)}{}} + {\mathbb{1}_{\lbrack{1/2},1\rbrack}{(t)}{}}}$ for all times $t \in {\lbrack 0,1\rbrack}$.

<!-- chunk {"id": "body-0032", "role": "body", "section": "Risk-Averse Optimal Control and Pontryagin Maximum Principle", "weight": 1.0} -->

In the sequel, we will investigate Pontryagin optimality conditions for the following class of risk-averse stochastic optimal control problems Therein, the minimization is taken over the set of curves $x_{u} \in {C_{\mathcal{F}}^{2}{({{\lbrack 0,T\rbrack} \times \Omega},{\mathbb{R}}^{n})}}$ solution of (SDE) for some admissible control $u \in \mathcal{U}$, where The mapping $\rho:{{L_{\mathcal{F}_{T}}^{1}{(\Omega,{\mathbb{R}})}}\rightarrow{\mathbb{R}}}$ is a finite coherent risk measure, while $\varphi_{i}:{{\Omega \times {\mathbb{R}}^{n}}\rightarrow{\mathbb{R}}}$ for $i \in {\{

<!-- chunk {"id": "body-0033", "role": "body", "section": "Risk-Averse Optimal Control and Pontryagin Maximum Principle", "weight": 1.0} -->

0,{\ldots\ell}\}}$ represent a cost and functional constraints at the final time.

<!-- chunk {"id": "body-0034", "role": "body", "section": "Risk-Averse Optimal Control and Pontryagin Maximum Principle", "weight": 1.0} -->

From now, we assume that the maps $f:{{{\lbrack 0,T\rbrack} \times \Omega \times {\mathbb{R}}^{n} \times U}\rightarrow{\mathbb{R}}^{n}}$ and $\sigma:{{{\lbrack 0,T\rbrack} \times \Omega \times {\mathbb{R}}^{n} \times U}\rightarrow{\mathbb{R}}^{d \times n}}$ satisfy hypotheses (MSD). ‣ 2.2 Stochastic Differential Equations ‣ 2 Preliminaries ‣ First-Order Pontryagin Maximum Principle for Risk-Averse Stochastic Optimal Control Problems"), and posit that the cost and constraint mappings satisfy the following assumptions.

<!-- chunk {"id": "body-0035", "role": "body", "section": "Main Assumptions on the Cost and Constraints -- (MCC)", "weight": 1.0} -->

For every $i \in {\{ 0,\ldots,\ell\}}$ and almost every $\omega \in \Omega$, the application ${\varphi_{i}{(\omega, \cdot)}}:{{\mathbb{R}}^{n}\rightarrow{\mathbb{R}}}$ is Fréchet differentiable, with for all ${x,y} \in {\mathbb{R}}^{n}$, where the constant $L > 0$ is the same as in (MSD). ‣ 2.2 Stochastic Differential Equations ‣ 2 Preliminaries ‣ First-Order Pontryagin Maximum Principle for Risk-Averse Stochastic Optimal Control Problems")-(iii).

<!-- chunk {"id": "body-0036", "role": "body", "section": "Remark 3.1 (On the equivalence between Bolza and Mayer problems)", "weight": 1.0} -->

It is a standard fact in optimal control theory that every Bolza problem involving a running cost can be recast as a Mayer problem in which one only minimizes a final cost. Hence, the results that we prove in this article for Mayer problems still apply to Bolza problems under appropriate assumptions. Besides, one could then relax the compactness assumption on $U \subset {\mathbb{R}}^{m}$ by simply requiring that the latter be closed, provided that the running cost satisfies a Tonelli-type growth condition with respect to the control variable.

<!-- chunk {"id": "body-0037", "role": "body", "section": "Remark 3.1 (On the equivalence between Bolza and Mayer problems)", "weight": 1.0} -->

Throughout this article, we will use the following terminology to refer to solutions of (OCP) using the following terminology.

<!-- chunk {"id": "body-0038", "role": "body", "section": "The PMP with Controlled Diffusion", "weight": 1.0} -->

In the case where the control variable acts on both the drift and the diffusion terms, we need to supplement hypotheses (MSD). ‣ 2.2 Stochastic Differential Equations ‣ 2 Preliminaries ‣ First-Order Pontryagin Maximum Principle for Risk-Averse Stochastic Optimal Control Problems") and (MCC). ‣ 3 Risk-Averse Optimal Control and Pontryagin Maximum Principle ‣ First-Order Pontryagin Maximum Principle for Risk-Averse Stochastic Optimal Control Problems") with the following assumption.

<!-- chunk {"id": "body-0039", "role": "body", "section": "Remark 3.3", "weight": 1.0} -->

The above assumption, which has already been considered in in a similar setting, is standard in deterministic optimal control, where it is very useful to guarantee the existence of optimal controls. In particular, (ACD). ‣ 3.1 The PMP with Controlled Diffusion ‣ 3 Risk-Averse Optimal Control and Pontryagin Maximum Principle ‣ First-Order Pontryagin Maximum Principle for Risk-Averse Stochastic Optimal Control Problems") holds true e.g. when $f$ and $\sigma$ are affine in the control variable and $U$ is convex.

<!-- chunk {"id": "body-0040", "role": "body", "section": "Uncontrolled Diffusion", "weight": 1.0} -->

We now turn our attention towards the simpler scenario in which the control variable does not appear in the diffusion, namely ${\sigma{(t,\omega,x,u)}} \equiv {\sigma{(t,\omega,x)}}$. Unlike the previous situation, we may relax our assumptions and obtain the PMP without hypothesis (ACD). ‣ 3.1 The PMP with Controlled Diffusion ‣ 3 Risk-Averse Optimal Control and Pontryagin Maximum Principle ‣ First-Order Pontryagin Maximum Principle for Risk-Averse Stochastic Optimal Control Problems").

<!-- chunk {"id": "body-0041", "role": "body", "section": "Examples of application", "weight": 1.0} -->

In this section, we briefly discuss general examples of risk functions and risk-averse stochastic optimal control problems which are encompassed by our results. In this context, we will consider the simple case in which $(x^{\ast},u^{\ast})$ is a local minimum for (OCP) in the case where there is no control in the diffusion and no final-time constraints. Then, Theorem 3.8 with uncontrolled diffusion).

<!-- chunk {"id": "body-0042", "role": "body", "section": "Examples of application", "weight": 1.0} -->

‣ 3.2 Uncontrolled Diffusion ‣ 3 Risk-Averse Optimal Control and Pontryagin Maximum Principle ‣ First-Order Pontryagin Maximum Principle for Risk-Averse Stochastic Optimal Control Problems") shall provide us with the existence of stochastic processes ${(p^{\ast},q^{\ast})} \in {{{C_{\mathcal{F}}^{2}{({{\lbrack 0,T\rbrack} \times \Omega},{\mathbb{R}}^{n})}} \times L_{\mathcal{F}}^{2}}{({{\lbrack 0,T\rbrack} \times \Omega},{\mathbb{R}}^{d \times n})}}$ and a risk parameter $\xi^{\ast} \in {\partial{\rho\left( {\varphi_{0}{({x^{\ast}{(T)}})}} \right)}}$ for which (3.3

<!-- chunk {"id": "body-0043", "role": "body", "section": "Examples of application", "weight": 1.0} -->

‣ Theorem 3.4 (Risk-averse PMP for (OCP) with controlled diffusion).

<!-- chunk {"id": "body-0044", "role": "body", "section": "Examples of application", "weight": 1.0} -->

‣ 3.1 The PMP with Controlled Diffusion ‣ 3 Risk-Averse Optimal Control and Pontryagin Maximum Principle ‣ First-Order Pontryagin Maximum Principle for Risk-Averse Stochastic Optimal Control Problems")), (3.4 ‣ Theorem 3.4 (Risk-averse PMP for (OCP) with controlled diffusion). ‣ 3.1 The PMP with Controlled Diffusion ‣ 3 Risk-Averse Optimal Control and Pontryagin Maximum Principle ‣ First-Order Pontryagin Maximum Principle for Risk-Averse Stochastic Optimal Control Problems")), and (3.5 ‣ Theorem 3.4 (Risk-averse PMP for (OCP) with controlled diffusion).

<!-- chunk {"id": "body-0045", "role": "body", "section": "Examples of application", "weight": 1.0} -->

‣ 3.1 The PMP with Controlled Diffusion ‣ 3 Risk-Averse Optimal Control and Pontryagin Maximum Principle ‣ First-Order Pontryagin Maximum Principle for Risk-Averse Stochastic Optimal Control Problems")) hold with ${({\mathfrak{p}}_{0},\ldots,{\mathfrak{p}}_{\ell})} = {({- 1},0,\ldots,0)}$.

<!-- chunk {"id": "body-0046", "role": "body", "section": "Examples of risk-parameters characterization", "weight": 1.0} -->

Suppose at first that $\rho:{{L_{\mathcal{F}_{T}}^{1}{(\Omega,{\mathbb{R}})}}\rightarrow{\mathbb{R}}}$ is Fréchet differentiable, as it was for instance assumed. This situation includes for instance the $\log$-$\exp$ utility function and the mean-variance risk measures, see e.g.. In that case, ${\partial{\rho{(Z)}}} = {\{{{\nabla\rho}{(Z)}}\}}$ for every $Z \in {L_{\mathcal{F}_{T}}^{1}{(\Omega,{\mathbb{R}})}}$, and the result of Theorem 3.4 with controlled diffusion).

<!-- chunk {"id": "body-0047", "role": "body", "section": "Examples of risk-parameters characterization", "weight": 1.0} -->

‣ 3.1 The PMP with Controlled Diffusion ‣ 3 Risk-Averse Optimal Control and Pontryagin Maximum Principle ‣ First-Order Pontryagin Maximum Principle for Risk-Averse Stochastic Optimal Control Problems") hold with the uniquely determined risk parameter Suppose now that $\rho:{{L_{\mathcal{F}_{T}}^{1}{(\Omega,{\mathbb{R}})}}\rightarrow{\mathbb{R}}}$ is the prototypical example of subdifferentiable risk measure given by the Average-Value-at-Risk of a random variable $Z \in {L_{\mathcal{F}_{T}}^{1}{(\Omega,{\mathbb{R}})}}$ with level $\alpha \in {(0,1\rbrack}$, namely In that case, the results of Theorem 3.4 with controlled diffusion).

<!-- chunk {"id": "body-0048", "role": "body", "section": "Examples of risk-parameters characterization", "weight": 1.0} -->

‣ 3.1 The PMP with Controlled Diffusion ‣ 3 Risk-Averse Optimal Control and Pontryagin Maximum Principle ‣ First-Order Pontryagin Maximum Principle for Risk-Averse Stochastic Optimal Control Problems") hold for some $\xi^{\ast} \in {\partial{\rho\left({\varphi_{0}{({x^{\ast}{(T)}})}} \right)}}$, which satisfies in particular (3.3 ‣ Theorem 3.4 (Risk-averse PMP for (OCP) with controlled diffusion). ‣ 3.1 The PMP with Controlled Diffusion ‣ 3 Risk-Averse Optimal Control and Pontryagin Maximum Principle ‣ First-Order Pontryagin Maximum Principle for Risk-Averse Stochastic Optimal Control Problems")).

<!-- chunk {"id": "body-0049", "role": "body", "section": "The risk-averse double integrator problem", "weight": 1.0} -->

In addition to the computational examples provided hereinabove, we discuss the application of the PMP of Theorem 3.8 with uncontrolled diffusion). ‣ 3.2 Uncontrolled Diffusion ‣ 3 Risk-Averse Optimal Control and Pontryagin Maximum Principle ‣ First-Order Pontryagin Maximum Principle for Risk-Averse Stochastic Optimal Control Problems") to the following stochastic optimal planning problem in which ${y_{0},v_{0},y_{T}} \in {\mathbb{R}}$ are given such that $y_{0} < y_{T}$, the control set is defined by $\mathcal{U}:=L^{2}{({\lbrack 0,T\rbrack},{\lbrack - 1,1\rbrack}}$), and the average value-at-risk is defined as in (4.1).

<!-- chunk {"id": "body-0050", "role": "body", "section": "The risk-averse double integrator problem", "weight": 1.0} -->

In what follows, we show that the PMP of Theorem 3.8 with uncontrolled diffusion). ‣ 3.2 Uncontrolled Diffusion ‣ 3 Risk-Averse Optimal Control and Pontryagin Maximum Principle ‣ First-Order Pontryagin Maximum Principle for Risk-Averse Stochastic Optimal Control Problems") provides a necessary condition for optimal solutions of (SOP) to be safe, in the sense Our definition of safe optimal solutions to (SOP) is driven by the applications, and the rationale behind it is the following. Imagine for instance that (SOP) models a one-dimensional traffic lane over which one aims at steering a vehicle from some station $y_{0}$ to a point which lies as close as possible to the end of the lane $y_{T}$. It is then of paramount importance that the vehicle stops with high probability at a point which is strictly located on the left of $y_{T}$.

<!-- chunk {"id": "body-0051", "role": "body", "section": "Conclusion and perspectives", "weight": 1.5} -->

In this paper, we developed a new method for proving a first-order version of the Pontryagin Maximum Principle for non-smooth risk-averse optimal control problems, based on set-valued linearisations. The main incentive to do so was to produce optimality conditions that could encompass typical risk functions such as the AV@R, which is merely directionally differentiable. In the future, we aim at furthering these investigations in three main directions.

<!-- chunk {"id": "body-0052", "role": "body", "section": "Conclusion and perspectives", "weight": 1.5} -->

Firstly, we want to see whether it is feasible to weaken or remove the convexity assumptions on the dynamics. Owing to the lack of relaxation property for sollutions of (SDI) illustrated in Remark 2.15. ‣ 2.4 Stochastic Differential Inclusions ‣ 2 Preliminaries ‣ First-Order Pontryagin Maximum Principle for Risk-Averse Stochastic Optimal Control Problems"), this will most likely call for innovative proof strategies. Secondly, we want to leverage the optimality conditions proposed here to design efficient numerical methods for solving risk-averse optimal control problems, such as indirect risk-averse shooting methods. Lastly, we plan to investigate whether the optimality conditions discussed in this article might yield other important structure properties on risk-averse optimal controls, such as semi-Markovianity. Usually, the fact that optimal controls exhibit a Markovian dependance with respect to the state variable usually stems from the dynamic programming and HJB equations. While these latter are still largely unavailable in the risk-averse settings, we hope that our risk-averse PMP may take over and be sufficiently powerful to carry out the analysis.
