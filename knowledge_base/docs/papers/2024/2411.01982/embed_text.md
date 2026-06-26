## Introduction

Modeling complex dynamical systems is pivotal across various fields, enabling tasks such as analysis, prediction, simulation, control, optimization, and fault detection. Deriving models from first principles---such as physical, electrical, mechanical, chemical, biological, or economic laws---requires extensive knowledge, which is often lacking in practice. In response, the literature has seen the emergence of data-driven modeling approaches since at least the 1970s, utilizing input-output data sets to identify the most suitable model within a hypothesis set of possible models.

Stochastic differential equations (SDEs) are a general mathematical tool for modeling dynamical systems subject to random fluctuations. Let $X{(t)}$ be a controlled $n$-dimensional stochastic process whose dynamics are governed by the controlled SDE with coefficients ${(b,\sigma^{2})}:{{{\lbrack 0,T\rbrack} \times {\mathbb{R}}^{n} \times {\mathbb{R}}^{d}}\rightarrow{\mathbb{R}}^{n + n^{2}}}$, where $W{(t)}$ is a standard Brownian motion, $p_{0}$ a probability density over ${\mathbb{R}}^{n}$, and $\mathcal{H} \subset {\mathcal{F}{({\lbrack 0,T\rbrack},{\mathbb{R}}^{d})}}$ a set of deterministic controls.

We consider the problem of estimating a controlled SDE from a data set of sample paths generated under various controls from $\mathcal{H}$. Namely, our goal is to estimate $(b,\sigma^{2})$ from a data set where $X_{u_{k}}$ denotes the solution of Eq. under the control $u_{k}:{{\lbrack 0,T\rbrack}\mapsto{\mathbb{R}}^{d}}$. By treating controls as inputs and sample paths as outputs, we frame system identification as a supervised learning problem.

While controlled SDEs cover a wide range of scenarios, estimating them poses significant statistical and computational challenges. Consequently, the existing literature on dynamical systems (see Section 1.1) imposes various limitations to develop practical methods. These include deterministic assumptions (e.g., using ordinary differential equations, omitting diffusion), discrete assumptions (e.g., using difference equations), dimensional assumptions (e.g., one-dimensional systems), and structural assumptions on the coefficients (e.g., linearity or parametric models).

### Contributions

This paper introduces a novel method addressing the controlled SDE estimation problem in its most general setting while enjoying strong theoretical guarantees. Our approach builds on recent advances in SDE estimation and kernel representation. More precisely, we establish finite-sample learning bounds for our method, featuring statistical rates that are adaptive to standard regularity assumptions on the learning problem. Specifically, we prove $L^{2}$ learning rates between the probability density of the true SDE and that of the estimated coefficients, offering guarantees in expectation over controls, times, and positions. We then derive $L^{\infty}$ learning rates, ensuring accuracy almost surely over times and controls---particularly relevant for optimal control. From these $L^{\infty}$ rates, we establish CVaR learning rates, ensuring accuracy in tail estimation, crucial for risk-averse applications, such as risk-averse optimal control. For clarity of exposition, we focus on deterministic controls throughout the paper, with extensions to stochastic controls presented in a dedicated result. Furthermore, we provide implementations and experimental evaluations of the method proposed in for estimating uncontrolled SDEs ---as an insightful limit case of our approach where the control space reduces to a singleton--- as well as of our method for controlled SDEs. Both implementations are available as open-source Python libraries on the GitHub repositories lmotte/sde-learn and lmotte/controlled-sde-learn. Experimental results underscore the statistical and computational performance of the methods.

### Related work

### System identification

The foundation of system identification theory was established in the 1960s by and further strengthened in the 1990s by works such as. A wide variety of methods for identifying dynamical systems exists. These methods are generally categorized based on three key aspects: the model, the fitting method (which includes fitting criteria and optimization techniques), and---distinctly from standard supervised learning---the strategy for selecting inputs, referred to as experiment design. Given the extensive literature on system identification, we provide only a brief overview of the most prevalent methods in the field as they relate to our work and refer the reader to for detailed presentations of these methods.

(Models). Dynamical systems modeling can be characterized by how states and controls interact over time (see, e.g., state-space, ARX, ARMAX models) and the form of these interactions. Common models include linear, polynomial, lookup tables, neural network (e.g., RNN, LSTM, CNN ), and fuzzy models. Nonlinear modeling, while more involved, addressess a broader spectrum of engineering challenges by enabling capturing more complex dynamics. More recently, models based on the Koopman operator have emerged.

(Fitting methods). Models are typically fitted by optimizing a criterion that matches the outputs of the true and estimated systems across a selected set of inputs. Common methods include least-squares, Bayesian, and maximum likelihood estimations. For models that are linear in their parameters, optimization is often solved with closed-form solutions. For models that are nonlinear in their parameters, iterative optimization is commonly used.

(Experiment design). Selecting inputs that generate the most informative data for accurate model estimation poses a significant challenge. Typically, this involves obtaining data sets that allow discrimination between any two functions within the hypothesis set. This leads for instance to concepts such as persistence of excitation, and maximization of Fisher information, as discussed in the literature. Besides traditional experiment design strategies, there is a growing interest in using reinforcement learning and active learning techniques to dynamically select inputs in ways that maximize information gain for model identification.

Regarding learning guarantees, substantial research exists on the identification of linear dynamical systems. In contrast, the identification of nonlinear dynamical systems has received much less attention, and sample complexity in nonlinear system identification remains largely underexplored. Several studies, such as Oymak, Bahmani and Romberg, Foster et al., Sattar and Oymak, investigate generalized linear dynamical systems of the form $x_{t + 1} = {\phi{({{Ax_{t}} + {Bu_{t}}})}}$, where $\phi$ is a specified function. Mania et al. analyze a parametric model defined as $x_{t + 1} = {{A\phi{(x_{t},u_{t})}} + w_{t}}$. Their approach, however, is constrained by several assumptions, including a "warm start" (an informed initial model guess), the availability of a computational oracle bypassing trajectory planning intractability, and controllability (the ability to drive the system from any state to a target-aligned feature vector). While these results contribute valuable insights, they also highlight the necessity for a statistical theory designed specifically for nonparametric models, as developed in this work.

### Online learning in system identification

Online learning refers to methods in which models are incrementally updated as new data becomes available, rather than being trained once on a static dataset. There is a substantial literature on online learning methods for system identification. These methods primarily focus on refining pre-existing nominal models, typically learned offline, by leveraging data gathered during system operation. The goal is to improve control performance by addressing uncertainties and adapting to environmental changes, rather than learning the system dynamics entirely from scratch. This is particularly important in many practical systems where the dynamics are only partially known, with time-varying or uncertain parameters (e.g., payloads or environmental conditions), necessitating adaptive methods that can handle these evolving conditions. A key assumption in these approaches is that the nominal model provides a reasonable approximation of the true system, ensuring safe data collection and refinement. In contrast, this work focuses on offline data collection and learning the system's dynamics from the ground up.

### Uncontrolled SDE estimation

The literature on learning SDE coefficients primarily focuses on autonomous systems, which operate independently of any control inputs. There is a broad range of methods for learning SDE coefficients. In terms of learning guarantees, most literature has focused on deriving guarantees for coefficient estimation by observing a single process up to time $T$ at discrete intervals of size $\Delta$, and then studying convergence rates as $T\rightarrow{+ \infty}$ and $\Delta\rightarrow 0$ under ergodicity assumptions. Such settings do not align with our needs in the control setting, where short time horizons are critical. Specifically, we aim to obtain arbitrarily accurate coefficients within a fixed time horizon as the number of observations increases. More recent studies consider the i.i.d. setting, where data consists of i.i.d. sample paths with fixed horizons. Comte and Genon-Catalot considers continuous observation of a one-dimensional process and provides risk bounds that hold in expectation. Bonalli and Rudi, Nüske et al., Zhang and Zuazua addresses a more realistic setting involving $n$-dimensional processes and discrete sampling observations, providing finite-sample bounds.

### Controlled SDE estimation

Despite the extensive literature on system identification and SDE estimation, to our knowledge, the study by Nüske et al. stands as the sole finite-data error analysis in the controlled setting. Their method is tailored for nonlinear control-affine SDEs, particularly under the structural assumption ${b{(t,x,{u_{\theta}{(t)}})}} = {{b_{0}{(x)}} + {B_{1}{(x)}\theta}}$, where $b_{0}:{{\mathbb{R}}^{n}\rightarrow{\mathbb{R}}^{n}}$, $B_{1}:{{\mathbb{R}}^{n}\rightarrow{\mathbb{R}}^{n \times m}}$ and the control space is parametrized by $\theta \in {\mathbb{R}}^{m}$ for $m \in {\mathbb{N}}^{\ast}$. Additionally, they assume that the diffusion $\sigma$ does not depend on $u$ and $t$. Importantly, their methodology does not provide explicit estimates of the drift and diffusion coefficients. In contrast, our approach provides explicit coefficient estimates, relying only on regularity assumptions and offering learning rates adaptive to coefficient regularity.

### Paper organisation

The paper is organized as follows. In Section 2, we formulate the learning problem addressed in this work. In Section 3, we introduce our controlled SDEs estimation method. In Section 4, we provide the learning guarantees for this method. In Section 5, we present numerical experiments.

### Paper notations

Let ${q,r,s,d,n} \in {\mathbb{N}}_{+}$. Let $\mathcal{F}{(A,B)}$ denote the set of all functions from the set $A$ to the set $B$. Let $\mathcal{M}{(A,B)}$ denote the set of all measurable functions from the measurable space $(A,\mathcal{A})$ to $(B,\mathcal{B})$, where $\mathcal{A}$ and $\mathcal{B}$ are the Borel $\sigma$-algebras on $A$ and $B$, respectively. Let $W^{q}{(A,B)}$ denote the Sobolev Hilbert space from $A$ to $B$ whose weak derivatives are defined up to order $q$. In this work, $A$ is either ${\mathbb{R}}^{r}$ or the cylindrical domain ${\lbrack 0,T\rbrack} \times {\mathbb{R}}^{r}$, and $B = {\mathbb{R}}^{s}$, ensuring well-definition. We denote the Loewner partial ordering by $\preceq$, such that for any two bounded linear operators $A$ and $B$, $A \preceq B$ if and only if $B - A$ is positive. For any vectors $u,v$, $u \otimes v$ denotes the tensor product. Let $\mathcal{H} \subset {\mathcal{F}{({\lbrack 0,T\rbrack},{\mathbb{R}}^{d})}}$ denotes the space of possible controls, then for any sets $A,C$, $u \in \mathcal{H}$, and $f:{{\mathcal{H} \times A}\rightarrow C}$, we denote $f{(u)} \triangleq f{(u{(\cdot)}, \cdot)})$. We denote ${a \land b} \triangleq {\min{(a,b)}}$, and ${a \vee b} \triangleq {\max{(a,b)}}$. Throughout this work, $p_{c}$ denotes a probability measure on the control space $\mathcal{H}$. The following mixed norms are used where ${{ess}\sup}_{u \sim p_{c}}$ denotes the essential supremum taken $p_{c}$-almost surely over $\mathcal{H}$, ignoring sets of $p_{c}$-measure zero.

## Problem setting

In this section, we introduce and discuss the learning problem addressed in this work.

### Controlled SDE identification

Our goal is to estimate the coefficients ${(b,\sigma^{2})}:{{{\lbrack 0,T\rbrack} \times {\mathbb{R}}^{n} \times {\mathbb{R}}^{d}}\rightarrow{\mathbb{R}}^{n + n^{2}}}$ of a $n$-dimensional and nonlinear controlled SDE given by where $T > 0$ is a fixed time horizon, $W{(t)}$ is a standard Brownian motion, $p_{0}$ is a probability density over ${\mathbb{R}}^{n}$, $\mathcal{H} \subset {\mathcal{F}{({\lbrack 0,T\rbrack},{\mathbb{R}}^{d})}}$ is a set of possible controls, thanks to a data set of controlled sample paths where $X_{u_{k}}$ denotes the solution of Eq. under control $u_{k}:{{\lbrack 0,T\rbrack}\rightarrow{\mathbb{R}}^{d}}$.

### Probability density associated with $(b,\sigma^{2})$

For any coefficients ${(b,\sigma^{2})}:{{{\lbrack 0,T\rbrack} \times {\mathbb{R}}^{n} \times {\mathbb{R}}^{d}}\rightarrow{\mathbb{R}}^{n + n^{2}}}$, we define the map such that $p_{b,\sigma}{(u,t,.)}$ represents the probability density of $X_{u}{(t)}$ governed by Eq..

### Learning problem

Given a hypothesis space $\mathcal{F} \subset {\mathcal{M}{({{\lbrack 0,T\rbrack} \times {\mathbb{R}}^{n} \times {\mathbb{R}}^{d}},{\mathbb{R}}^{n + n^{2}})}}$ for the SDE coefficients, the controlled SDE identification problem can be formulated as where $p \triangleq p_{b,\sigma}$ represents the probability density associated with the true controlled stochastic process.

The learning problem defined by Eq. is both statistically and computationally challenging due to the complex mapping ${\hat{b},{\hat{\sigma}}^{2}}\mapsto p_{\hat{b},\hat{\sigma}}$. In Section 3, we overcome this challenge, following the approach of recent work by Bonalli and Rudi, by leveraging the Fokker-Planck equation to cast this non-convex learning objective into a convex least-squares objective. This transformation allows for efficient resolution, with strong learning guarantees, harnessing the well-established literature on least-squares.

### Experiment design

The choice of $(\mathcal{H},p_{c})$ will determine the controls over which the estimated SDE is accurate (see Theorem 4.1. ‣ 4.1 𝐿² learning rates ‣ 4 Learning guarantees ‣ Learning Controlled Stochastic Differential Equations")). Therefore, it should align with the intended usage of the estimated SDE, and depend on the specific application at hand. We leave this choice to users, based on their specific experimental context. Additionally, the choice of the initial distribution $p_{0}$ can also be considered part of the experiment design. Similar to the choice of $(\mathcal{H},p_{c})$, it will determine the initial positions over which the estimated controlled SDE is accurate (see Theorem 4.1. ‣ 4.1 𝐿² learning rates ‣ 4 Learning guarantees ‣ Learning Controlled Stochastic Differential Equations")). We refer the curious reader to the related work section for a brief review of existing experiment design methods.

### Remark 1 (Non-identifiability of SDE coefficients)

Estimating the true SDE coefficients $(b,\sigma^{2})$ from a set of sample paths, with $L^{2}$ norm guarantees such as ${\|{{(\hat{b},{\hat{\sigma}}^{2})} - {(b,\sigma^{2})}}\|}_{L^{2}{({{\lbrack 0,T\rbrack} \times {\mathbb{R}}^{n} \times {\mathbb{R}}^{d}})}} \leq {\epsilon{(K,M,Q,\delta)}}$, with probability at least $1 - \delta$, given sample sizes ${K,M,Q} \in {\mathbb{N}}^{\ast}$, is generally infeasible without additional assumptions. This stems from the fact that identifying the true coefficients $(b,\sigma^{2})$ solely from sample paths constitutes an ill-posed problem, as distinct SDE coefficients can result in identical probability distributions of the sample paths due to unexplored regions of ${\lbrack 0,T\rbrack} \times {\mathbb{R}}^{n}$. In contrast, recovering the probability density function ${t,x}\mapsto{p_{b,\sigma}{(t,x)}}$ from the sample paths is a well-posed problem. Then, from $p_{b,\sigma}$, one can identify coefficients $(\overset{\sim}{b},{\overset{\sim}{\sigma}}^{2})$ that, while potentially distinct from $(b,\sigma^{2})$, yield the same probability density, i.e., such that $p_{\overset{\sim}{b},\overset{\sim}{\sigma}} = p_{b,\sigma}$. See Example 1. ‣ Experiment design. ‣ 2 Problem setting ‣ Learning Controlled Stochastic Differential Equations") for a prototypical case where different SDE coefficients lead to the same probability density. Investigating the conditions under which the distribution $p_{b,\sigma}$ uniquely determines $(b,\sigma^{2})$ is an interesting and complex question, though it lies beyond the scope of this study. Finally, obtaining coefficients that accurately generate $p_{b,\sigma}$ is sufficient for many practical scenarios where the main goal is to accurately reproduce the true controlled dynamics. This justifies our learning problem proposed in Eq..

### Example 1 (Prototypical non-identifiable SDE coefficients)

We provide an example where different coefficients yield the same probability density. Here, a change in the diffusion coefficient is offset by a corresponding adjustment in the drift coefficient. Consider the (uncontrolled) Ornstein-Uhlenbeck process $X{(t)}$ governed by the SDE where $\theta > 0$, $\mu \in {\mathbb{R}}$, $\sigma > 0$, and $W{(t)}$ denotes standard Brownian motion. The process $X{(t)}$ follows a normal distribution, with its mean and variance evolving over time as If $m = \mu$ and $s^{2} = {\sigma^{2}/{({2\theta})}}$, any pair ${(\overset{\sim}{\theta},\overset{\sim}{\sigma})} \neq {(\theta,\sigma)}$ where $\frac{{\overset{\sim}{\sigma}}^{2}}{2\overset{\sim}{\theta}} = \frac{\sigma^{2}}{2\theta}$ yield the same probability density, specifically that of a stationary normal distribution with mean $m$ and variance $s^{2}$.

## Proposed method

In this section, we present our method for estimating controlled SDEs. We leverage the Fokker-Planck (FP) matching inequality to split the estimation into two more manageable problems: a) estimation of the dynamics for a finite set of controls, and b) estimation of coefficients that could govern these dynamics. Section 3.1 introduces the FP matching inequality, while Section 3.2 details the estimator leveraging the decomposition principle.

### Fokker-Planck matching inequality

We assume that the true SDE coefficients $(b,\sigma^{2})$, the initial probability density $p_{0}$, and the considered model $\mathcal{F}$ meet a minimal smoothness assumption, characterized by a sufficiently high order of Sobolev regularity, essential for the validity of both the Strong FP equation and the FP matching inequality.

### Assumption (A1) (Smooth SDE)

The initial density satisfies $p_{0} \in {W^{3}{({\mathbb{R}}^{n},{\mathbb{R}})}}$, and there exists $c > 0$ such that We assume a uniform ellipticity condition on $\sigma$, which is a standard requirement in SDE analysis to ensure that the diffusion coefficient $\sigma$ remains uniformly non-degenerate.

### Assumption (A2) (Uniform ellipticity)

There exists a constant $\kappa > 0$ such that, for all ${(t,x)} \in {{\lbrack 0,T\rbrack} \times {\mathbb{R}}^{n}}$, Additionally, we assume the ability to sample from a probability density $p_{s}$ over ${\lbrack 0,T\rbrack} \times {\mathbb{R}}^{n}$ that covers the supports of the true coefficients and their derivatives.

### Assumption (A3) (Calibrated sampling)

There exists a probability density $p_{s}$ over ${\lbrack 0,T\rbrack} \times {\mathbb{R}}^{n}$, and $a > 0$, such that Moreover, the bounded support of $p_{s}$ contains the support of $(b,\sigma^{2})$ and their derivatives. Namely, with the same conditions applied to the derivatives of $(b,\sigma^{2})$.

Under these assumptions, we derive the two following key lemmas for our method.

### Lemma 3.1 (SFP equation)

Let $\left(\mathcal{L}^{{(b,\sigma)}{(u)}} \right)^{\ast}$ denotes the dual of the Kolmogorov generator Under Assumptions (A1) (Smooth SDE). ‣ 3.1 Fokker-Planck matching inequality ‣ 3 Proposed method ‣ Learning Controlled Stochastic Differential Equations") and (A2) (Uniform ellipticity). ‣ 3.1 Fokker-Planck matching inequality ‣ 3 Proposed method ‣ Learning Controlled Stochastic Differential Equations"), the strong Fokker-Planck equation holds, namely,

### Lemma 3.2 (FP matching inequality)

Under Assumptions (A1) (Smooth SDE). ‣ 3.1 Fokker-Planck matching inequality ‣ 3 Proposed method ‣ Learning Controlled Stochastic Differential Equations"), (A2) (Uniform ellipticity). ‣ 3.1 Fokker-Planck matching inequality ‣ 3 Proposed method ‣ Learning Controlled Stochastic Differential Equations"), and (A3) (Calibrated sampling). ‣ 3.1 Fokker-Planck matching inequality ‣ 3 Proposed method ‣ Learning Controlled Stochastic Differential Equations"), there exists $c > 0$ such that where $\text{FP}{(\hat{b},{\hat{\sigma}}^{2})}$ is defined as Eq. (17. ‣ 3.1 Fokker-Planck matching inequality ‣ 3 Proposed method ‣ Learning Controlled Stochastic Differential Equations")) shows that our learning objective, as specified in Eq., can be bounded by the convex alternative described in Eq. (18. ‣ 3.1 Fokker-Planck matching inequality ‣ 3 Proposed method ‣ Learning Controlled Stochastic Differential Equations")), referred to as Fokker-Planck (FP) matching. This provides theoretical support for addressing FP matching in order to solve our initial learning problem. Specifically, it allows to infer $L^{2}$ learning rates for $p_{\hat{b},\hat{\sigma}}$ from FP matching learning rates for $(\hat{b},{\hat{\sigma}}^{2})$.

### Estimator

### Controlled SDE estimator

Consider a data set of controlled sample paths where the controls ${(u_{k})}_{k = 1}^{K}$ are i.i.d. from $p_{c}$, and the sample paths ${({X_{u_{k}}{(w_{i}^{k},t_{l})}})}_{{i \in {⟦1,Q⟧}},{l \in {⟦1,M⟧}}}$ are i.i.d. from $p{(u_{k},t_{l},.)}$. For each control $u_{k}$, we denote ${\hat{p}}_{k}$ as the estimator proposed by Bonalli and Rudi for uncontrolled SDE density estimation, trained on the following data Subsequently, from an i.i.d. set ${(z_{i})}_{i = 1}^{N} = {(t_{i},x_{i})}_{i = 1}^{N}$ sampled from $p_{s}$, we define the estimator

### Defining the hypothesis space $\mathcal{F}$ for $(b,\sigma^{2})$ with RKHSs

FP matching (Eq. (18. ‣ 3.1 Fokker-Planck matching inequality ‣ 3 Proposed method ‣ Learning Controlled Stochastic Differential Equations"))) constitutes a convex learning problem, specifically quadratic with respect to $(b,\sigma^{2})$. This stems from the linearity of the dual Kolmogorov generator with respect to $(b,\sigma^{2})$, which is a linear combination of the partial derivatives of $(b,\sigma^{2})$. Consequently, RKHSs are well-suited for solving FP matching. In particular, they meet the key properties of maintaining the convexity that facilitates empirical risk minimization (Eq. ) while being universal approximators, leading both to good computational and statistical performance. Their ability for closed-form differentiation also significantly facilitates the computation of the Kolmogorov generator.

### Uniformly elliptic diffusion $\sigma^{2}$

Meaningful diffusion coefficient $\sigma^{2}$ should satisfy the uniform ellipticity condition of Assumption (A2) (Uniform ellipticity). ‣ 3.1 Fokker-Planck matching inequality ‣ 3 Proposed method ‣ Learning Controlled Stochastic Differential Equations"). This requirement can be efficiently addressed as follows.

(Soft shape constraint). One approach is to enforce this via pointwise constraints on a set of training points. Specifically, for ${(z_{i})}_{i = 1}^{q} \in {({{\lbrack 0,T\rbrack} \times {\mathbb{R}}^{n} \times {\mathbb{R}}^{d}})}^{q}$ and ${(x_{j})}_{j = 1}^{r} \in {({\mathbb{R}}^{n})}^{r}$, the linear constraints ${{\forall{(i,j)}} \in {{⟦1,q⟧} \times {⟦1,r⟧}}},{{x_{j}^{T}\sigma^{2}{(z_{i})}x_{j}} \geq \kappa}$ are imposed. For uniform diffusion $\sigma^{2} = {\sigma_{0}^{2}I_{n}}$, this simplifies to ${{\forall i} \in {⟦1,q⟧}},{{\sigma_{0}^{2}{(z_{i})}} \geq \kappa}$.

(Hard shape constraint). A recently introduced class of kernel models has been designed to represent PSD-valued functions Marteau-Ferey et al., Muzellec et al., while maintaining the aforementioned key properties of standard kernel models. These models utilize cone constraints on model parameters and have been successfully applied across various applications. With a bounded positive definite kernel $k$ over ${\lbrack 0,T\rbrack} \times {\mathbb{R}}^{n} \times {\mathbb{R}}^{d}$, the corresponding reproducing kernel Hilbert space (RKHS) $\mathcal{G}$ has a feature map ${\phi{(t,x,v)}} \triangleq {k{({(t,x,v)}, \cdot )}}$. The hypothesis space $\mathcal{F}$ for $(b,\sigma^{2})$ is defined as $\mathcal{F} \triangleq {\mathcal{F}_{b} \times \mathcal{F}_{\sigma}}$. Here, $\mathcal{F}_{b} \triangleq {\{ b\mid{{{\forall i} \in {⟦1,n⟧}},{{b_{i} = {\langle w_{i},{\phi{( \cdot )}}\rangle}_{\mathcal{G}}},{w_{i} \in \mathcal{G}}}}\}}$, and $\mathcal{F}_{\sigma} \triangleq {\{{\sigma^{2} + {\kappa I_{{\mathbb{R}}^{n \times n}}}}\mid{{{{\forall i},j} \in {⟦1,n⟧}},{{\sigma_{ij}^{2} = {\langle{\phi{( \cdot )}},{w_{ij}\phi{( \cdot )}}\rangle}_{\mathcal{G}}},{{(w_{ij})}_{{i,j} = 1}^{n} \in \mathcal{S}}}}\}}$, where $\mathcal{S}$ is defined as $\{{W \in {\mathcal{G}^{n} \otimes \mathcal{G}^{n}}}\mid{{W^{\ast} = W},{W \succeq 0}}\}$.

For a detailed discussion on the advantages of various PSD models, refer to Marteau-Ferey et al., Muzellec et al..

## Learning guarantees

In Section 4.1, we provide $L^{2}$-in-time-control-and-position learning rates for the proposed method. In Section 4.2, we provide refined $L^{2}$ learning rates under refined regularity assumptions on the learning problem. In Section 4.3, we provide $L^{\infty}$-in-time-and-control, $L^{2}$-in-position learning rates. In Section 4.4, we provide CVaR learning rates. In Section 4.5, we illustrate our theoretical results by analyzing the special case of SDE coefficients in Sobolev spaces. In Section 4.6, we discuss the proposed method's adaptability to the regularity of the learning problem. Finally, in Section 4.7, we extend our approach to encompass a larger class of controls, expanding from deterministic to stochastic controls within closed-loop systems.

### $L^{2}$ learning rates

To establish finite-sample bounds for our estimator, it is necessary to impose regularity assumptions on the learning problem, as underpinned by the No-Free-Lunch Theorem (see Devroye et al. ).

### Assumption (A4) (Attainability assumption)

The true coefficients indeed belong to the chosen hypothesis space. Namely, This is a standard assumption in the literature of regularized least-squares regression. For concrete examples, refer to Section 4.5.

### Theorem 4.1 ($L^{2}$ Learning rates)

For any ${N,K} \in {\mathbb{N}}^{\ast}$, let $(\hat{b},{\hat{\sigma}}^{2})$ be the proposed estimator, with hard shape-constrained PSD diffusion, trained with $K$ controls ${(u_{k})}_{k = 1}^{K}$ i.i.d. from a probability measure $p_{c}$ over $\mathcal{H}$, and $N$ points ${(t_{i},x_{i})}_{i = 1}^{N}$ i.i.d. from a probability measure $p_{s}$ over ${\lbrack 0,T\rbrack} \times {\mathbb{R}}^{n}$. Assuming Assumptions (A1) (Smooth SDE). ‣ 3.1 Fokker-Planck matching inequality ‣ 3 Proposed method ‣ Learning Controlled Stochastic Differential Equations"), (A3) (Calibrated sampling). ‣ 3.1 Fokker-Planck matching inequality ‣ 3 Proposed method ‣ Learning Controlled Stochastic Differential Equations"), and (A4) (Attainability assumption). ‣ 4.1 𝐿² learning rates ‣ 4 Learning guarantees ‣ Learning Controlled Stochastic Differential Equations") hold true, then there exist constants ${c_{1},c_{2}} > 0$ that do not depend on $N$, $K$, or $\delta$, such that for any $\delta \in {(0,1\rbrack}$, defining $\varepsilon \triangleq {\sup_{k \in {⟦1,K⟧}}{L{({\hat{p}}_{k},{p{(u_{k})}})}}}$ where $L$ is a squared Sobolev norm defined in the appendix, and setting $\lambda = {c_{2}{({{N^{- 1}{\log{({N\delta^{- 1}})}}} + {K^{- 1}{\log{({K\delta^{- 1}})}}}})}}$, if then with probability $1 - \delta$,

### Sketch of the proof

The proof involves decomposing the error of the proposed estimator into three components: Error stemming from the estimation of the probability densities ${({\hat{p}}_{k})}_{k = 1}^{K} \approx {({p{(u_{k})}})}_{k = 1}^{K}$, Error stemming from the finite sampling approximation of times $\lbrack 0,T\rbrack$ and positions ${\mathbb{R}}^{n}$, Error stemming from the finite sampling approximation of the space of controls $\mathcal{H}$.

Each error component is then bounded by representing all quantities as norms of linear operators, followed by appropriate decomposition and the application of Bernstein inequalities for sums of operators. ∎ Theorem 4.1. ‣ 4.1 𝐿² learning rates ‣ 4 Learning guarantees ‣ Learning Controlled Stochastic Differential Equations") demonstrates that, with sufficiently accurate density estimation (small enough $\varepsilon$), the estimator for the coefficients of the controlled SDE achieves the standard learning rate of kernel ridge regression with respect to $K$ and $N$---without additional assumptions in the noiseless setting, where the output is unambiguous given the input.

### Remark 2 (Dependency in $K$ and $N$)

Note that despite utilizing $KN$ data points ${(u_{k},t_{i},x_{i})}_{{i \in {⟦1,N⟧}},{l \in {⟦1,K⟧}}}$ in $\mathcal{H} \times {\lbrack 0,T\rbrack} \times {\mathbb{R}}^{n}$, we do not achieve a convergence rate of ${({KN})}^{- {1/2}}$. Instead, the rate is $K^{- {1/2}} + N^{- {1/2}}$. This outcome is expected, as the points ${(u_{k},t_{i},x_{i})}_{i,k}$ are not sampled independently. In particular, for a given finite number of observed controls $K \in {\mathbb{N}}^{\ast}$, the bound does not approach zero as $N$ tends to infinity.

### Remark 3 (Dependency in the density estimation)

The proposed method employs the probability density estimation from Bonalli and Rudi. However, our Theorem 4.1. ‣ 4.1 𝐿² learning rates ‣ 4 Learning guarantees ‣ Learning Controlled Stochastic Differential Equations") remains valid regardless of the chosen density estimator. In particular, the learning accuracy of our method is independent of the specific choice of density estimator, given $\epsilon$.

### Remark 4 (Control-dependent sampling of ${\lbrack 0,T\rbrack} \times {\mathbb{R}}^{n}$)

For the sake of clarity, we present our method considering drawing the ${(t_{i},x_{i})}_{i = 1}^{N}$ independently from the control $u_{k}$. Nevertheless, for each $u_{k}$, it might be advantageous to draw distinct data sets ${(t_{k,i},x_{k,i})}_{i = 1}^{N}$ i.i.d. from $p_{s}{( \cdot |u_{k})}$, typically sampling with preference for the high-value regions of ${\hat{p}}_{k}$. In this case, our analysis and learning rates still apply, as we do not rely on this independence assumption in our proofs.

### Remark 5 (Soft shape Constraint)

When considering the soft shape constraint for the diffusion coefficient, the theoretical analysis involves examining kernel ridge regression under additional linear constraints, which is not expected to introduce significant difficulties. We anticipate that this approach could yield rates comparable to those obtained under hard shape constraints; nonetheless, rigorous investigation is necessary to confirm this. We leave this question for future investigation.

### Refined $L^{2}$ learning rates

Applying additional regularity conditions that finely measure the effective dimension of the learning problem generally enables the derivation of refined learning rates. In the context of kernel ridge regression, this is standardly achieved by measuring the regularity of the features and of the target, leading to learning rates that are adaptive to the strength of these regularities. This section focuses on such assumptions tailored to our specific least-squares problem: FP matching.

### Kernel-model for $\frac{\partial p}{\partial t}$ induced from $(b,\sigma^{2})$

Considering a RKHS modeling for the coefficients, as defined in Section 3, and based on Lemma 3.1. ‣ 3.1 Fokker-Planck matching inequality ‣ 3 Proposed method ‣ Learning Controlled Stochastic Differential Equations"), Lemma 3.2. ‣ 3.1 Fokker-Planck matching inequality ‣ 3 Proposed method ‣ Learning Controlled Stochastic Differential Equations"), and Assumption (A4) (Attainability assumption). ‣ 4.1 𝐿² learning rates ‣ 4 Learning guarantees ‣ Learning Controlled Stochastic Differential Equations"), then there exists $w \in \mathcal{G}_{n}$ such that for almost every ${(u,t,x)} \in {\mathcal{H} \times {\lbrack 0,T\rbrack} \times {\mathbb{R}}^{n}}$, where the feature map $\overset{\sim}{\phi}:{{\mathcal{H} \times {\lbrack 0,T\rbrack} \times {\mathbb{R}}^{n}}\rightarrow\mathcal{G}_{n}}$ and feature space $\mathcal{G}_{n}$ are defined in the appendix.

### Assumption (A5) (Regularity of $\frac{\partial p}{\partial t}$)

Define $C \triangleq {{\mathbb{E}}_{t,x,u}{\lbrack{{({\overset{\sim}{\phi} \otimes \overset{\sim}{\phi}})}{(u,t,x)}}\rbrack}}$. There exists $\alpha \in {\lbrack 0,1\rbrack}$ such that This condition is referred to as the source condition. Notably, Assumption (A5) (Regularity of ∂𝑝/∂𝑡). ‣ Kernel-model for ∂𝑝/∂𝑡 induced from (𝑏,𝜎²). ‣ 4.2 Refined 𝐿² learning rates ‣ 4 Learning guarantees ‣ Learning Controlled Stochastic Differential Equations") with $\alpha = 0$ corresponds to Assumption (A4) (Attainability assumption). ‣ 4.1 𝐿² learning rates ‣ 4 Learning guarantees ‣ Learning Controlled Stochastic Differential Equations"). It pertains to the regularity of $\frac{\partial p}{\partial t}$. For concrete examples, refer to Section 4.5.

### Assumption (A6) (Regularity of the features)

Define ${C{(u)}} \triangleq {{\mathbb{E}}_{t,x}{\lbrack{{({\overset{\sim}{\phi} \otimes \overset{\sim}{\phi}})}{(u,t,x)}}\rbrack}}$ and ${C{(x)}} \triangleq {{\mathbb{E}}_{u}{\lbrack{{({\overset{\sim}{\phi} \otimes \overset{\sim}{\phi}})}{(u,t,x)}}\rbrack}}$.

(A6.1) There exists $r \in {\lbrack 0,1\rbrack}$ and $c > 0$ such that (A6.2) There exists $s \in {\lbrack 0,1\rbrack}$ and $c > 0$ such that Assumptions (A6) (Regularity of the features). ‣ Kernel-model for ∂𝑝/∂𝑡 induced from (𝑏,𝜎²). ‣ 4.2 Refined 𝐿² learning rates ‣ 4 Learning guarantees ‣ Learning Controlled Stochastic Differential Equations"), known as embedding properties, are always satisfied for $r = s = 0$ (as $\overset{\sim}{\phi}$ is bounded) and become stricter as ${r,s} \in {\lbrack 0,1\rbrack}$ increase. The embedding property relates to the effective dimension of the input distribution through the RKHS (see Remark 7. ‣ Kernel-model for ∂𝑝/∂𝑡 induced from (𝑏,𝜎²). ‣ 4.2 Refined 𝐿² learning rates ‣ 4 Learning guarantees ‣ Learning Controlled Stochastic Differential Equations") below). Furthermore, by quantifying the minimal alignment of the covariance with any features almost surely over the input space, it measures of how well almost all input points are represented within the least-squares objective, indicating typically the presence or absence of low-probability regions. For concrete examples, refer to Section 4.5.

### Remark 6 (Decomposition of the embedding property)

Assumptions (A6) (Regularity of the features). ‣ Kernel-model for ∂𝑝/∂𝑡 induced from (𝑏,𝜎²). ‣ 4.2 Refined 𝐿² learning rates ‣ 4 Learning guarantees ‣ Learning Controlled Stochastic Differential Equations") can be viewed as decomposing the embedding property on ${\lbrack 0,T\rbrack} \times {\mathbb{R}}^{n} \times \mathcal{H}$ into two embedding properties on ${\lbrack 0,T\rbrack} \times {\mathbb{R}}^{n}$ and $\mathcal{H}$. In particular, Assumptions (A6) (Regularity of the features). ‣ Kernel-model for ∂𝑝/∂𝑡 induced from (𝑏,𝜎²). ‣ 4.2 Refined 𝐿² learning rates ‣ 4 Learning guarantees ‣ Learning Controlled Stochastic Differential Equations") imply ${\|{C^{- {{rs}/2}}\overset{\sim}{\phi}{(u,t,x)}}\|}_{\mathcal{G}_{n}} \leq c$ a.s. with $c > 0$. Indeed, using Jensen's operator inequality, we find ${C{(u)}} \preccurlyeq {c{\mathbb{E}}_{x}{\lbrack{C{(x)}^{s}}\rbrack}} \preccurlyeq {cC^{s}}$. Consequently, ${\|{C^{- {{rs}/2}}\overset{\sim}{\phi}{(u,t,x)}}\|}_{\mathcal{G}_{n}} \leq {{\|{C^{- {{rs}/2}}C{(u)}^{r/2}}\|}_{\mathcal{G}_{n}}{\|{C{(u)}^{- {r/2}}\overset{\sim}{\phi}{(u,t,x)}}\|}_{\mathcal{G}_{n}}} \leq c$, for $c > 0$.

### Remark 7 (Embedding property and capacity condition)

The embedding property is a finer assumption compared to the standard capacity condition. In particular, Assumptions (A6) (Regularity of the features). ‣ Kernel-model for ∂𝑝/∂𝑡 induced from (𝑏,𝜎²). ‣ 4.2 Refined 𝐿² learning rates ‣ 4 Learning guarantees ‣ Learning Controlled Stochastic Differential Equations") imply the capacity condition ${{Tr}{(C^{1 - {rs}})}} = {{\mathbb{E}}{\lbrack{\|{C^{- {{rs}/2}}\overset{\sim}{\phi}}\|}_{\mathcal{G}_{n}}^{2}\rbrack}} \leq c$ for $c > 0$. While the capacity condition allows refining learning rates from $n^{- {1/4}}$ to $n^{- {1/2}}$ in the noisy least-squares setting, Assumptions (A6) (Regularity of the features). ‣ Kernel-model for ∂𝑝/∂𝑡 induced from (𝑏,𝜎²). ‣ 4.2 Refined 𝐿² learning rates ‣ 4 Learning guarantees ‣ Learning Controlled Stochastic Differential Equations") allow refining learning rates from $n^{- {1/2}}$ to arbitrarily fast polynomial decay in the noiseless setting, as $r$ and $s$ transition from 0 to 1.

We derive refined learning rates for the proposed estimator.

### Theorem 4.2 (Refined $L^{2}$ learning rates)

Under the assumptions of Theorem 4.1. ‣ 4.1 𝐿² learning rates ‣ 4 Learning guarantees ‣ Learning Controlled Stochastic Differential Equations"), Assumption (A5) (Regularity of ∂𝑝/∂𝑡). ‣ Kernel-model for ∂𝑝/∂𝑡 induced from (𝑏,𝜎²). ‣ 4.2 Refined 𝐿² learning rates ‣ 4 Learning guarantees ‣ Learning Controlled Stochastic Differential Equations"), and Assumption (A6) (Regularity of the features). ‣ Kernel-model for ∂𝑝/∂𝑡 induced from (𝑏,𝜎²). ‣ 4.2 Refined 𝐿² learning rates ‣ 4 Learning guarantees ‣ Learning Controlled Stochastic Differential Equations"), then there exist constants ${c_{1},c_{2}} > 0$ that do not depend on $N,K,\delta$, such that for any $\delta \in {(0,1\rbrack}$, taking $\lambda = {c_{2}\left({\left({\frac{18c}{N}{\log^{2}\frac{N}{\delta}}} \right)^{\frac{1}{1 - r}} + \left({\frac{18c}{K}{\log^{2}\frac{K}{\delta}}} \right)^{\frac{1}{1 - s}}} \right)}$, if then with probability $1 - \delta$, where $\varepsilon_{\infty} \triangleq {\sup_{k \in {⟦1,K⟧}}{L_{\infty}{({\hat{p}}_{k},{p{(u_{k})}})}}}$ with $L_{\infty}$ a squared Sobolev norm defined in the appendix.

Theorem 4.2. ‣ Kernel-model for ∂𝑝/∂𝑡 induced from (𝑏,𝜎²). ‣ 4.2 Refined 𝐿² learning rates ‣ 4 Learning guarantees ‣ Learning Controlled Stochastic Differential Equations") shows that the rates of FP matching can improve at arbitrarily fast polynomial rates depending on the regularity of the learning problem. However, this improvement is constrained by the accuracy of ${\hat{p}}_{k}$. In particular, the error bound always exceeds the $L^{2}$ error of any ${\hat{p}}_{k}$. Furthermore, the lower of the two regularities measured by the parameters $r$ and $s$, acts as a bottleneck, limiting the rate of convergence.

### $L^{\infty}$ learning rates

From an optimal control perspective, it is relevant to establish learning guarantees almost surely over the control space rather than in expectation over the control space. $L^{2}$ rates can be casted into $L^{\infty}$ rates thanks to Assumption (A6) (Regularity of the features). ‣ Kernel-model for ∂𝑝/∂𝑡 induced from (𝑏,𝜎²). ‣ 4.2 Refined 𝐿² learning rates ‣ 4 Learning guarantees ‣ Learning Controlled Stochastic Differential Equations").

### Corollary 4.1 ($L^{\infty}$ learning rates)

Under the same conditions as Theorem 4.2. ‣ Kernel-model for ∂𝑝/∂𝑡 induced from (𝑏,𝜎²). ‣ 4.2 Refined 𝐿² learning rates ‣ 4 Learning guarantees ‣ Learning Controlled Stochastic Differential Equations"), for any $\delta \in {(0,1\rbrack}$, with probability at least $1 - \delta$, we have Corollary 4.1. ‣ 4.3 𝐿^∞ learning rates ‣ 4 Learning guarantees ‣ Learning Controlled Stochastic Differential Equations") provides accuracy guarantees almost surely over the set of possible controls $\mathcal{H}$, in contrast to Theorems 4.1. ‣ 4.1 𝐿² learning rates ‣ 4 Learning guarantees ‣ Learning Controlled Stochastic Differential Equations") and 4.2. ‣ Kernel-model for ∂𝑝/∂𝑡 induced from (𝑏,𝜎²). ‣ 4.2 Refined 𝐿² learning rates ‣ 4 Learning guarantees ‣ Learning Controlled Stochastic Differential Equations"), which offer guarantees only on average over $\mathcal{H}$. However, this stronger result comes at the cost of a reduced learning rate, ${({{\alpha + r} \land s})}/{({{1 - r} \land s})}$ with ${r \land s} \in {\lbrack 0,1\rbrack}$, instead of ${({\alpha + 1})}/{({{1 - r} \land s})}$, under the same assumptions.

### CVaR learning rates

### Conditional Value at Risk (CVaR)

For any $\alpha \in {\lbrack 0,1\rbrack}$, the conditional value at risk of a random variable $X:{\Omega\rightarrow{\mathbb{R}}}$ is defined as CVaR is a risk measure that can essentially be interpreted as the expected value conditional upon being within some percentage of the worst-case scenarios (i.e., high X).

### Remark 8 (Risk averse optimal control)

CVaR has applications in risk-averse optimal control, where methods typically involve solving where $D$ is a risk measure, $f$ the loss, and $\lambda > 0$ a trade-off parameter. Compared to the approach of choosing $\lambda = 0$, it allows minimizing the dispersion of the loss around its mean. Various risk can be defined depending on the application. Typically, one can defined the risk measure as the variance. However, if one does not want to treats the excess over the mean equally as the shortfall, one will prefer the VaR or CVaR over the variance. The latter, enjoying better mathematical properties than the former, has become a standard tool in the litterature for managing risk.

### Lemma 4.3

For any $f \in {L^{\infty}{({\mathbb{R}}^{n})}}$, $\alpha \in {\lbrack 0,1\rbrack}$, and two random variables ${X_{1},X_{2}}:{\Omega\rightarrow{\mathbb{R}}^{n}}$ with probability density functions $p_{1},p_{2}$, the following bound holds

### Lemma 4.4

For any $f \in {L^{2}{({\mathbb{R}}^{n})}}$, if there exists $\beta > 1$ such that ${\|{fx^{\beta}}\|}_{L^{1}{({\mathbb{R}}^{n})}} < {+ \infty}$, then we have

### Lemma 4.5

Let $X_{\hat{b},\hat{\sigma}}{(u)}$ be the solution to the SDE driven by the coefficients ${(\hat{b},\sigma^{2})} \in \mathcal{F}$ under control $u \in {W^{4 + {\lfloor\frac{n}{2}\rfloor}}{({\lbrack 0,T\rbrack},{\mathbb{R}}^{d})}}$. Under Assumption (A1) (Smooth SDE). ‣ 3.1 Fokker-Planck matching inequality ‣ 3 Proposed method ‣ Learning Controlled Stochastic Differential Equations") and (A3) (Calibrated sampling). ‣ 3.1 Fokker-Planck matching inequality ‣ 3 Proposed method ‣ Learning Controlled Stochastic Differential Equations"), if ${{\mathbb{E}}{\lbrack{\| X_{0}\|}^{\beta}\rbrack}} < \infty$ for some $\beta > 2$, then there exists a constant $C > 0$ such that, for all $t \in {\lbrack 0,T\rbrack}$, From Lemma 4.3. ‣ 4.4 CVaR learning rates ‣ 4 Learning guarantees ‣ Learning Controlled Stochastic Differential Equations"), Lemma 4.4. ‣ 4.4 CVaR learning rates ‣ 4 Learning guarantees ‣ Learning Controlled Stochastic Differential Equations"), and Lemma 4.5. ‣ 4.4 CVaR learning rates ‣ 4 Learning guarantees ‣ Learning Controlled Stochastic Differential Equations"), we derive the following result.

### Theorem 4.6

Under Assumptions (A1) (Smooth SDE). ‣ 3.1 Fokker-Planck matching inequality ‣ 3 Proposed method ‣ Learning Controlled Stochastic Differential Equations"), (A3) (Calibrated sampling). ‣ 3.1 Fokker-Planck matching inequality ‣ 3 Proposed method ‣ Learning Controlled Stochastic Differential Equations"), and (A4) (Attainability assumption). ‣ 4.1 𝐿² learning rates ‣ 4 Learning guarantees ‣ Learning Controlled Stochastic Differential Equations"), and with ${{\mathbb{E}}{\lbrack{\| X_{0}\|}^{\beta}\rbrack}} < \infty$ for some $\beta > 2$, given $u \in {W^{4 + {\lfloor\frac{n}{2}\rfloor}}{({\lbrack 0,T\rbrack},{\mathbb{R}}^{d})}}$, then for any $\alpha \in {\lbrack 0,1\rbrack}$, $f \in {L^{\infty}{({\mathbb{R}}^{n})}}$, $t \in {\lbrack 0,T\rbrack}$, we have where $c > 0$ is a constant that does not depend on $\hat{b}$, $\hat{\sigma}$, or $\alpha$.

Theorem 4.6. ‣ 4.4 CVaR learning rates ‣ 4 Learning guarantees ‣ Learning Controlled Stochastic Differential Equations"), in conjunction with the $L^{\infty}$ learning rates detailed in Corollary 4.1. ‣ 4.3 𝐿^∞ learning rates ‣ 4 Learning guarantees ‣ Learning Controlled Stochastic Differential Equations") enables the derivation of CVaR learning rates. Notably, this allows to derive accuracy guarantees for quantities expressed as which are crucial in scenarios such as risk-averse optimal control, among other applications. This contrasts with Corollary 4.1. ‣ 4.3 𝐿^∞ learning rates ‣ 4 Learning guarantees ‣ Learning Controlled Stochastic Differential Equations"), which allows to derive accuracy guarantees merely for quantities expressed as

### Application to Sobolev spaces

In this section, we analyze the example of SDE coefficients in Sobolev spaces.

In this lemma, we examine the extent to which all previously discussed assumptions are satisfied when considering $(b,\sigma^{2})$ within a Sobolev space.

### Lemma 4.7

Let $q > {\frac{1 + n + m}{2} + 4}$, and $\mathcal{H} = \left. \{ u_{\theta} \middle| {\theta \in {\mathbb{R}}^{m}}\} \right.$ with ${\theta,t}\mapsto{u_{\theta}{(t)}} \in {W^{q}{({{\mathbb{R}}^{m} \times {\lbrack 0,T\rbrack}})}}$. Assume $\sigma^{2}$ is uniformly elliptic, with ${\forall{(t,x)}} \in {{{\lbrack 0,T\rbrack} \times {\mathbb{R}}^{n}}\sigma^{2}{(t,x)}} \geq {\kappa I_{{\mathbb{R}}^{n \times n}}}$ with $\kappa > 0$, and ${(b,{\sigma^{2} - {\kappa I_{{\mathbb{R}}^{n \times n}}}})} \in {W^{q}{({{\lbrack 0,T\rbrack} \times {\mathbb{R}}^{n} \times {\mathbb{R}}^{d}},{\mathbb{R}}^{n + n^{2}})}}$. Assume further that ${\theta,t,x}\mapsto{p{(u_{\theta},t,x)}} \in {W^{q - 2}{({{\mathbb{R}}^{m} \times {\lbrack 0,T\rbrack} \times {\mathbb{R}}^{n}},{\mathbb{R}})}}$. Additionally, let $p_{s},p_{c}$ be such that there exist constants ${c_{1},c_{2},c_{3},c_{4}} > 0$ ensuring $c_{1} \leq {p_{s}{(t,x)}} \leq c_{2}$ holds $p_{s}$-almost surely and $c_{3} \leq {p_{c}{(u)}} \leq c_{4}$ holds $p_{c}$-almost surely, and assume that the partial derivatives of $(b,{\sigma^{2} - {\kappa I_{{\mathbb{R}}^{n \times n}}}})$ are supported within the bounded set $D \triangleq {\text{supp}{(p_{s})}}$. Then, using a kernel that induces the Sobolev RKHS $W^{q}{({D \times {\mathbb{R}}^{d}},{\mathbb{R}}^{n + n^{2}})}$, the Assumptions (A1) (Smooth SDE). ‣ 3.1 Fokker-Planck matching inequality ‣ 3 Proposed method ‣ Learning Controlled Stochastic Differential Equations"), (A2) (Uniform ellipticity). ‣ 3.1 Fokker-Planck matching inequality ‣ 3 Proposed method ‣ Learning Controlled Stochastic Differential Equations"), (A3) (Calibrated sampling). ‣ 3.1 Fokker-Planck matching inequality ‣ 3 Proposed method ‣ Learning Controlled Stochastic Differential Equations"), (A4) (Attainability assumption). ‣ 4.1 𝐿² learning rates ‣ 4 Learning guarantees ‣ Learning Controlled Stochastic Differential Equations") are met, Assumption (A5) (Regularity of ∂𝑝/∂𝑡). ‣ Kernel-model for ∂𝑝/∂𝑡 induced from (𝑏,𝜎²). ‣ 4.2 Refined 𝐿² learning rates ‣ 4 Learning guarantees ‣ Learning Controlled Stochastic Differential Equations") is satisfied with $\alpha = 0$, Assumptions (A6) (Regularity of the features). ‣ Kernel-model for ∂𝑝/∂𝑡 induced from (𝑏,𝜎²). ‣ 4.2 Refined 𝐿² learning rates ‣ 4 Learning guarantees ‣ Learning Controlled Stochastic Differential Equations") are satisfied with $r = {1 - \frac{m}{2{({q - 2})}}}$ and $s = {1 - \frac{n + 1}{2{({q - 2})}}}$.

### Remark 9 (Regularity of $p$)

In Lemma 4.7, we operate under the assumption that the probability density function ${u,t,x}\mapsto{p{(u,t,x)}}$ associated with the stochastic differential equation is regular, specifically that it belongs to a Sobolev space of order $q - 2$ with respect to the parameter $\theta$. This regularity assumption is typically valid when the coefficients ${t,x,\theta}\mapsto{{(b,\sigma^{2})}{(t,x,{u_{\theta}{(t)}})}}$ of the SDE are themselves sufficiently regular in $t,x,\theta$. Although a comprehensive proof of this regularity goes beyond the scope of this paper, the general validity of the assumption can be inferred from the regularity properties of the coefficients and controls. For further details on such regularity results, refer to the appropriate literature on stochastic calculus and Fokker-Planck equations (see, for example, Lunardi, specifically Section 8.3.1, and Friedman, Theorem 7).

From Lemma 4.7, we deduce learning rates for our controlled SDE coefficients estimation method in the case of coefficients in Sobolev spaces.

### Corollary 4.2 (Sobolev coefficients)

Under the assumptions of Lemma 4.7, the proposed controlled SDE estimation method verifies all learning rates provided in the previous sections for various risks. In particular, there exists a constant $c > 0$ that does not depend on $N$, $K$, or $\delta$, such that, with sufficiently accurate density estimation (small enough $\varepsilon_{\infty}$), with probability at least $1 - \delta$, we have

### Proof

Applying Lemma 4.7 and either Theorem 4.2. ‣ Kernel-model for ∂𝑝/∂𝑡 induced from (𝑏,𝜎²). ‣ 4.2 Refined 𝐿² learning rates ‣ 4 Learning guarantees ‣ Learning Controlled Stochastic Differential Equations") or Corollary 4.1. ‣ 4.3 𝐿^∞ learning rates ‣ 4 Learning guarantees ‣ Learning Controlled Stochastic Differential Equations") allows to conclude the proof. ∎ The key insight from Corollary 4.2. ‣ 4.5 Application to Sobolev spaces ‣ 4 Learning guarantees ‣ Learning Controlled Stochastic Differential Equations") is that although the proposed method's learning rates suffer from the curse of dimensionality---with accuracy decreasing exponentially as the dimensions of the state and control spaces increase---this impact is mitigated by the smoothness of the SDE coefficients.

### Remark 10 (Optimal learning rates)

Most existing literature focuses on the noisy regression setting. Nevertheless, in the noiseless setting, minimax rate in $L^{\infty}$-norm of $\mathcal{O}{({({\log^{1/2}{K/\sqrt{K}}})}^{\frac{2{({q - 2})}}{m}})}$ has been proven by Bauer et al. when estimating $q - 2$-times continuously differentiable function on ${\lbrack 0,1\rbrack}^{m}$ with $K$ i.i.d. data points. In comparison, our rates are $\mathcal{O}{({({\log{K/\sqrt{K}}})}^{\frac{2{({q - 2})}}{m}{({1 - \frac{m}{2{({q - 2})}}})}})}$ slower than their rates, but they converge closely as $q$ increases.

We derive the following results as a consequence of Corollary 4.2. ‣ 4.5 Application to Sobolev spaces ‣ 4 Learning guarantees ‣ Learning Controlled Stochastic Differential Equations").

### Corollary 4.3 (Computational complexity)

Under the assumptions of Lemma 4.7, let $N \geq K$. To achieve a precision level $\eta > 0$ with respect to the $L^{\infty}$-in-time-and-control norm and $L^{2}$-in-position norm, that is, the proposed controlled SDE estimation method requires a number of controls with a corresponding computational cost for the Fokker-Planck matching step of This result implies, for instance, that under sufficiently regular coefficients with $q \geq {{2 + m} \vee {({n + 1})}}$, the proposed controlled SDE estimation method achieves accuracy $\eta$ in the $L^{\infty}$-in-time-and-control and $L^{2}$-in-position norms using $K = {\mathcal{O}{(\eta^{- 2})}}$ controls and incurring a computational cost of $\mathcal{O}{(\eta^{- 12})}$.

### Remark 11 (Complexity analysis in $M$ and $Q$)

In our analysis, we assume that density estimation ${\hat{p}}_{k}$ for each $p{(u_{k})}$ is sufficiently accurate, and therefore omits a detailed examination of the computational complexity in terms of parameters $M$ and $Q$. While Bonalli and Rudi address this complexity in the case of $\varepsilon$, an extension is required for $\varepsilon_{\infty}$. Here, we focus on the number of controls required to reach a desired accuracy $\eta > 0$, and the computational cost of the Fokker-Planck step, which dominates the computational cost in our numerical experiments of Section 5.

### Adaptive learning rates

In Section 4.5, we examined Sobolev coefficients. While analyzing stronger assumptions could potentially lead to faster learning rates, this is not the primary focus of our paper. For illustrative purposes, we provide two examples of stronger assumptions in Examples 2. ‣ 4.6 Adaptive learning rates ‣ 4 Learning guarantees ‣ Learning Controlled Stochastic Differential Equations") and 3. ‣ 4.6 Adaptive learning rates ‣ 4 Learning guarantees ‣ Learning Controlled Stochastic Differential Equations"). However, a detailed analysis of these assumptions is beyond the scope of our study. The key result of this paper is the adaptability of the proposed method: it automatically benefits from the most favorable regularity assumptions, whether they pertain to Sobolev regularity or other types. Specifically, our method achieves the best learning rates based on the most advantageous parameters $r$ and $s$ in Assumptions (A6) (Regularity of the features). ‣ Kernel-model for ∂𝑝/∂𝑡 induced from (𝑏,𝜎²). ‣ 4.2 Refined 𝐿² learning rates ‣ 4 Learning guarantees ‣ Learning Controlled Stochastic Differential Equations"), without requiring prior knowledge of these optimal parameters.

### Example 2 (Parametric probability density)

Consider the scenario where $p{(u,t, \cdot)}$ lies, for all ${t,u} \in {{\lbrack 0,T\rbrack} \times \mathcal{H}}$, within a parametric family of dimension $m$. In this case, Fokker-Planck matching formulates as a least-squares problem over a space of dimension $m + 1 + n + d$, independent of the dimension of the control space $\mathcal{H}$. Specifically, by pushing forward ${p_{c}p_{s}}:{{\mathcal{H} \times {\lbrack 0,T\rbrack} \times {\mathbb{R}}^{n}}\rightarrow{\mathbb{R}}^{+}}$ through ${t,u}\mapsto{u{(t)}} \in {\mathbb{R}}^{d}$ and ${t,u}\mapsto{p{(u,t, \cdot)}}$, the FP matching least-squares problem over $\mathcal{H} \times {\lbrack 0,T\rbrack} \times {\mathbb{R}}^{n}$ can be reformulated as a least-squares problem over $\mathcal{P} \times {\mathbb{R}}^{d} \times {\lbrack 0,T\rbrack} \times {\mathbb{R}}^{n}$, where $\mathcal{P}$ is the set containing all distributions over ${\mathbb{R}}^{n}$ reached given the control space and initial distribution. Specifically, As an example, consider a controlled linear SDE. Given ${A,C} \in {L^{\infty}{({\lbrack 0,T\rbrack},{\mathbb{R}}^{n^{2}})}}$ and ${u,e} \in {L^{2}{({\lbrack 0,T\rbrack},{\mathbb{R}}^{n})}}$, the following controlled SDE where the explicit solution can be derived by means of the variation of constants formula, resulting in ${X{(t)}} \sim {\mathcal{N}{({\mu{(t)}},{\Sigma{(t)}})}}$, with $\mu$ and $\Sigma$ governed by linear ODEs. For more details, refer to Chapter 6.3. In this setting, $p{(u,t, \cdot)}$ for any control $u \in \mathcal{H} \triangleq {L^{2}{({\lbrack 0,T\rbrack},{\mathbb{R}}^{n})}}$ belongs to a parametric family of dimension $m = {n + {{n{({n - 1})}}/2}}$. Consequently, it is straightforward to show that Assumptions (A6) (Regularity of the features). ‣ Kernel-model for ∂𝑝/∂𝑡 induced from (𝑏,𝜎²). ‣ 4.2 Refined 𝐿² learning rates ‣ 4 Learning guarantees ‣ Learning Controlled Stochastic Differential Equations") are satisfied with $r = {1 - \frac{d + m}{2{({q - 2})}}}$ and $s = {1 - \frac{n + 1}{2{({q - 2})}}}$.

### Example 3 (Identifiability)

Consider a scenario where identifiability is assumed, characterized by constants ${c_{1},c_{2}} > 0$ and ${\nu_{1},\nu_{2}} > 0$ such that for any ${(\hat{b},{\hat{\sigma}}^{2})} \in \mathcal{F}$ we have, $p_{c}p_{s}$-almost surely, Equations (46. ‣ 4.6 Adaptive learning rates ‣ 4 Learning guarantees ‣ Learning Controlled Stochastic Differential Equations")) and (47. ‣ 4.6 Adaptive learning rates ‣ 4 Learning guarantees ‣ Learning Controlled Stochastic Differential Equations")) ensure that Assumptions (A6) (Regularity of the features). ‣ Kernel-model for ∂𝑝/∂𝑡 induced from (𝑏,𝜎²). ‣ 4.2 Refined 𝐿² learning rates ‣ 4 Learning guarantees ‣ Learning Controlled Stochastic Differential Equations") are satisfied with $r = {1 - \frac{\nu_{2}d}{2{({q - 2})}}}$ and $s = {1 - \frac{\nu_{1}{({n + 1})}}{2{({q - 2})}}}$, as they imply ${{\mathbb{E}}_{t,x}{\lbrack{{({\phi \otimes \phi})}{(t,x,{u{(t)}})}}\rbrack}} \preceq {c_{1}{\mathbb{E}}_{t,x}{\lbrack{{({\overset{\sim}{\phi} \otimes \overset{\sim}{\phi}})}{(u,t,x)}}\rbrack}^{\nu_{1}}}$ and ${{\mathbb{E}}_{u}{\lbrack{{({\phi \otimes \phi})}{(t,x,{u{(t)}})}}\rbrack}} \preceq {c_{2}{\mathbb{E}}_{u}{\lbrack{{({\overset{\sim}{\phi} \otimes \overset{\sim}{\phi}})}{(u,t,x)}}\rbrack}^{\nu_{2}}}$, and similar derivation than for Lemma 4.7 allows to conclude. This suggests that identifiability necessitates minimal mass conditions, such as avoiding regions of ${\lbrack 0,T\rbrack} \times {\mathbb{R}}^{n}$ that, while having non-zero Lebesgue measure, are explored with zero probability. However, note that deriving conditions to ensure identifiability is generally intricate.

### Extension to closed-loop control

For clarity in exposition, we considered position-independent (a.k.a. open-loop) controls in the previous sections. Nevertheless, our approach and results seamlessly extend to position-dependent controls $u{(t,x)}$, which is essential for control systems employing monitoring feedback. This extension involves updating the Fokker-Planck equation, specifically the Kolmogorov generator (or equivalently, $\overset{\sim}{\phi}$), to account for the dependencies on the system's state variables. From a practical standpoint, modifying $\hat{\phi}$ is straightforward, although it requires knowledge of the controls' partial derivatives. From a theoretical standpoint, the required modifications are limited to Lemma 7.10-ϕ̂_𝑘⁢(𝑡,𝑥)‖_𝒢_𝑛²]). ‣ 7.10 Auxiliary lemmas ‣ 7 Proofs ‣ Learning Controlled Stochastic Differential Equations") and are also straightforward. We expect the learning rates to remain the same, though the constants will be updated and will depend on the supremum bounds of the control's partial derivatives.

### Lemma 4.8

When the controls $u \in \mathcal{H}$ are position-dependent, specifically $\mathcal{H} \subset {\mathcal{F}{({{\lbrack 0,T\rbrack} \times {\mathbb{R}}^{n}},{\mathbb{R}}^{d})}}$, Assumption (A1) (Smooth SDE). ‣ 3.1 Fokker-Planck matching inequality ‣ 3 Proposed method ‣ Learning Controlled Stochastic Differential Equations") and (A4) (Attainability assumption). ‣ 4.1 𝐿² learning rates ‣ 4 Learning guarantees ‣ Learning Controlled Stochastic Differential Equations") yields, denoting $\phi^{2} \triangleq {\phi \otimes \phi}$,

### Proof

The proof follows directly from applying the chain rule. Compared to position-independent controls, additional terms arise due to $u$'s dependency on position $x$, impacting the derivatives of $\phi$. ∎

## Numerical experiments

In this section, we present numerical experiments on the problems of uncontrolled (Section 5.1) and controlled (Section 5.2) SDE estimation, illustrating the main behaviors of the evaluated methods.

### Uncontrolled SDE estimation

### Purpose of uncontrolled SDE experiments

We initiate our numerical study by implementing and evaluating the method proposed in Bonalli and Rudi for uncontrolled SDE estimation. Note that the method proposed in Bonalli and Rudi corresponds to our approach in the limit case where the control space is reduced to a singleton $\mathcal{H} = {\{ u\}}$. Therefore, this study provides important insights for the more intricate scenario of controlled SDEs considered in Section 5.2.

### Python open-source library

Our implementation is available as an open-source Python library on the GitHub repository lmotte/sde-learn. The library includes comprehensive documentation and example scripts demonstrating various use cases with light computational demands. In particular, our implementation supports the Nyström approximation, which aids in reducing the computational complexity of Fokker-Planck matching. Further details, including thorough derivations of all necessary formulas for implementing the proposed estimator and the computational complexity of each step, are provided in Section 8.

### Experimental setup

We consider uniform diffusion and use the soft-shape constraint presented in Section 3 for the diffusion coefficient. All kernels are Gaussian kernels ${k{(x,y)}} = {\exp{({- {\gamma{\|{x - y}\|}^{2}}})}}$ with different parameters $\gamma > 0$. We select all hyperparameters using grid search and validation sets. The selection metrics are the log-likelihood for the probability density estimation step, i.e., $\hat{p}\mapsto{\sum_{l = 1}^{M_{val}}{\sum_{i = 1}^{Q_{val}}{\log{({\hat{p}{(t_{l},x_{i})}})}}}}$, and the mean squared error for the Fokker-Planck matching step, i.e., ${(\hat{b},{\hat{\sigma}}^{2})}\mapsto{\sum_{i = 1}^{N}{\lbrack{{\frac{\partial p}{\partial t}{(t_{i},x_{i})}} - {{(\mathcal{L}^{\hat{b},\hat{\sigma}})}^{\ast}p{(t_{i},x_{i})}}}\rbrack}^{2}}$. Further details can be found in the code repository.

### Computational considerations

While the computational complexity of each step is provided in Section 8, we offer here a practical idea of the computational requirements by reporting the observed execution times from our experiments on the considered problem and data sets. These experiments were performed on a machine equipped with an Apple M3 Pro processor and 18 GB of RAM. For the 1D case, the probability density estimation step takes 0.015 seconds for training with 1000 sample paths and 100 time steps, and 0.11 seconds for prediction over a Fokker-Planck training set of size 2500. The Fokker-Planck matching step requires 6.0 seconds for training with 2500 data points and 3.7 seconds to generate 100 sample paths with 100 time steps. For the two 2D problems, probability density estimation training takes around 0.012 seconds for 3000 sample paths and 100 time steps, with prediction taking approximately 60 seconds over a Fokker-Planck training set of size 3000. The Fokker-Planck matching step requires about 10 seconds for training and 6 seconds to generate 100 sample paths with 100 time steps. These results indicate that, although the computational times are non-trivial, they remain manageable---ranging from a few seconds to just over a minute---demonstrating the practicality of the method for the problem sizes considered.

### Linear scalar SDE

To carry out our first experiments, we consider Ornstein--Uhlenbeck processes.

### Ornstein--Uhlenbeck process

The Ornstein-Uhlenbeck (OU) process is a simple example of stochastic process, which tends to revert to a mean over time under the influence of a mean-reverting term and a stochastic noise term. It is a useful tool, for example, for modeling phenomena such as price volatility. It is defined by the following SDE where $\mu$ is the mean to which the process reverts, $\theta$ is the mean-reverting coefficient giving the strength of revertion to $\mu$, and $\sigma$ is the amplitude of the stochastic noise. The probability density function of the OU process can be explicitly derived by solving the Fokker-Planck equation. Notably, if $X{}$ is initially Gaussian-distributed with mean $\mu_{0} \in {\mathbb{R}}$ and covariance $\sigma_{0}^{2} > 0$, then $X{(t)}$ will follow a Gaussian distribution with the mean and covariance given by

### Data sets

We consider an Ornstein-Uhlenbeck process with constant variance and a mean that increases from $0.5$ to $2.5$ from $t = 0$ to $t = 10$. Specifically, we set ${\mu = 2.5},{{\theta = 0.5},{{\sigma^{2} = {\theta/4}},{{\mu_{0} = 0.5},{\sigma_{0}^{2} = {\sigma^{2}/{({2\theta})}}}}}}$, and $T = 10$. In Figure 3, we plot 100 sample paths generated from this OU process. For the probability density estimation steps, we draw training and validation sets with ${Q/Q_{val}} = {1000/100}$ sample paths and ${M/M_{val}} = {100/100}$ time steps, respectively. For the Fokker-Planck matching step, we draw a training set ${(t_{i},x_{i})}_{i = 1}^{N} = {{\{ t_{i}\}}_{i = 1}^{50} \times {\{ x_{i}\}}_{i = 1}^{50}}$ by drawing times and positions uniformly within well-chosen intervals, and we draw a validation set with same size and distribution.

### Step 1 (probability density estimation)

In Figure 1. ‣ 5.1.1 Linear scalar SDE ‣ 5.1 Uncontrolled SDE estimation ‣ 5 Numerical experiments ‣ Learning Controlled Stochastic Differential Equations"), we plot the true and estimated probability densities, $p{(t,x)}$ and $\hat{p}{(t,x)}$, respectively. These densities are plotted on a uniformly spaced temporal grid, offset by $1/2$ unit from the training time discretization, and a spatial grid with positions randomly drawn from a uniform distribution within an interval. The estimated density reasonably approximates the true dynamics, as visually evident.

Figure 1: OU process. True and estimated probability densities, p(t, x) (left) and p̂(t, x) (right), w.r.t x for several t ∈.

### Step 2 (coefficients estimation via FP matching)

In Figure 2. ‣ 5.1.1 Linear scalar SDE ‣ 5.1 Uncontrolled SDE estimation ‣ 5 Numerical experiments ‣ Learning Controlled Stochastic Differential Equations"), we plot the estimated coefficients obtained via FP matching. Notice that these estimated coefficients differ significantly from the true coefficients. As discussed in Remark 1. ‣ Experiment design. ‣ 2 Problem setting ‣ Learning Controlled Stochastic Differential Equations"), measuring the accuracy of the estimated coefficients using the $L^{2}$ distance from the true coefficients is excluded due to the non-identifiability of the coefficients. Our learning guarantees do not ensure the recovery of the true coefficients but rather ensure that the estimated coefficients accurately replicate the true dynamics. Specifically, this involves obtaining an induced distribution $p_{\hat{b},\hat{\sigma}}$ that closely approximates the true distribution $p_{b,\sigma}$ in terms of $L^{2}$ distance.

Figure 2: OU process. Estimated coefficients b̂(t, x) (left) and σ̂(t, x)2 (right) w.r.t. x for several t ∈.

### Recovering the true dynamic

We draw and plot 100 sample paths from the true and estimated coefficients in Figure 3 to assess the recovery of the true dynamics. Notice that the estimated coefficients lead to visually comparable probability distributions, with close means and variances over time. Interestingly, while the distributions are similar, individual paths appear quite different.

Figure 3: OU process. 100 samples from the SDEs associated with the true (left) and estimated (right) coefficients.

### Nonlinear multivariate SDE

To carry out nonlinear multivariate SDE experiments, we consider two examples: Dubins process, and finite exponential sum process.

### Dubins process

The Dubins process is defined by the following SDE with ${u{(t)}} = {\theta{\sin{(\frac{\pi t}{10})}}}$, ${v,\theta} \in {\mathbb{R}}$, and $\sigma > 0$.

True SDE samples.

Estimated SDE samples.

Figure 4: Dubins process. 100 samples from the true and estimated SDEs.

### Finite exponential sum (FES) process

We introduce the process defined by the SDE associated with the following coefficients for ${{(b_{i})}_{i} \in {({\mathbb{R}}^{2})}^{n_{b}}},{{{(\sigma_{i})}_{i} \in {({\mathbb{R}}^{2})}^{n_{\sigma}}},{{\gamma > {0,n_{b}}},{n_{\sigma} \in {\mathbb{N}}^{\ast}}}}$.

True SDE samples.

Estimated SDE samples.

Figure 5: FES process. 100 samples from the true and estimated SDEs.

### Data sets

For the Dubins process, we set the parameters as follows: $T = 10$, $n = 2$, $M = 100$, $Q = 3000$, $v = 2$, $\theta = 3$, and $\sigma = 0.3$. For the probability density estimation steps, the training and validation sets consist of ${Q/Q_{val}} = {3000/100}$ sample paths and ${M/M_{val}} = {100/10}$ time steps, respectively. For the Fokker-Planck matching step, training and a validation set are drawn by sampling the set of training sample paths' time-position pairs, with size $N = {3000/N_{val}} = 1000$. For the finite exponential sum process, the parameters are $T = 3$, $n = 2$, $M = 100$, $Q = 3000$, $n_{b} = n_{\sigma} = 3$, $\gamma = 1$, and ${(t_{1},x_{1})} = {(0,{})}$, ${(t_{2},x_{2})} = {(1,{})}$, and ${(t_{3},x_{3})} = {(3,{})}$. For the probability density estimation steps, the training and validation sets consist of ${Q/Q_{val}} = {3000/100}$ sample paths and ${M/M_{val}} = {100/100}$ time steps, respectively. For the Fokker-Planck matching step, we use a training set ${\{ t_{i}\}}_{i = 1}^{30} \times {\{ x_{i}\}}_{i = 1}^{100}$ where the sets of times and positions are drawn uniformly in well-chosen interval and two-dimensional box, respectively. We use a validation set ${\{ t_{i}\}}_{i = 1}^{10} \times {\{ x_{i}\}}_{i = 1}^{100}$ where times and positions are uniform grids in well-chosen interval and two-dimensional box. For both processes, the initial condition is ${X{}} \sim {\mathcal{N}{(0,{{1/4}I_{{\mathbb{R}}^{2}}})}}$.

### Recovering the true dynamic

We perform density estimation and Fokker-Planck (FP) matching for both processes, selecting the hyperparameters based on the validation sets as previously. We draw and plot 100 sample paths from both the true and estimated coefficients in Figure 4 and in Figure 5 process. ‣ 5.1.2 Nonlinear multivariate SDE ‣ 5.1 Uncontrolled SDE estimation ‣ 5 Numerical experiments ‣ Learning Controlled Stochastic Differential Equations"). Notably, the estimated coefficients lead to probability distributions that are visually comparable to those of the true dynamics, with closely matching means and variances over time.

### Observations

Our experiments highlight key behaviors in the estimation of uncontrolled SDEs. Specifically, we observe the following phenomena.

Cumulative error. The accuracy of the density $p_{\hat{b},\hat{\sigma}}{(t,x)}$, associated with the estimated coefficients $(\hat{b},{\hat{\sigma}}^{2})$, decreases over time due to cumulative error. Even if the coefficients at a given time $t_{0}$ are accurate, earlier inaccuracies for $0 \leq t < t_{0}$ can lead to an inaccurate $p_{\hat{b},\hat{\sigma}}{(t_{0},x)}$.

Error amplification. Paths that enter regions of low probability, whether in time or space, where the accuracy of the coefficients is poor, experience error amplification. This often results in path divergence or termination. Increasing the variance of $X{}$ can facilitate a broader exploration of times and positions, thereby reducing this instability.

An illustrative analogy is a marble run: small deviations early on can lead to cumulative errors and amplified divergence, much like the behavior observed in the estimation of coefficients in SDEs.

### Controlled SDE estimation

### Python open-source library

Our implementation is available as an open-source Python library on the GitHub repository lmotte/controlled-sde-learn. The library includes comprehensive documentation and example scripts demonstrating various use cases with light computational demands. More details are provided in Section 9, including detailed derivations of all necessary formulas for implementing the proposed estimator.

### Experimental setup

We consider uniform diffusion and the soft-shape constraint presented in Section 3 for the diffusion coefficient. All kernels are Gaussian kernels ${k{(x,y)}} = {\exp{({- {\gamma{\|{x - y}\|}^{2}}})}}$ with different parameters $\gamma > 0$. For the 1D SDE, we select all hyperparameters using grid search and validation sets. The selection metrics are the log-likelihood for the probability density estimation step, i.e., $\hat{p}\mapsto{\sum_{l = 1}^{M_{val}}{\sum_{i = 1}^{Q_{val}}{\log{({\hat{p}{(t_{l},x_{i})}})}}}}$, and the mean squared error for the Fokker-Planck matching step, i.e., ${(\hat{b},\hat{\sigma})}\mapsto{\sum_{i = 1}^{N}{\lbrack{{\frac{\partial p}{\partial t}{(t_{i},x_{i})}} - {{(\mathcal{L}^{\hat{b},\hat{\sigma}})}^{\ast}p{(t_{i},x_{i})}}}\rbrack}^{2}}$. For the 2D SDE, to avoid excessive computation, we fix the hyperparameters for both the probability density estimation and the Fokker-Planck matching using previously selected hyperparameters for the estimation of uncontrolled Dubins process in Section 5.1.2. Further details can be found in the code repository.

### Computational considerations

While the computational complexity of each step is provided in Section 9, we offer here a practical idea of the computational requirements based on the observed execution times from our experiments on the considered problem and data sets, using a machine equipped with an Apple M3 Pro processor and 18 GB of RAM. For the 1D case, the probability density estimation step takes 5.6 seconds for training with 1000 sample paths, 100 time steps, and 10 training controls, and 1.0 seconds for prediction over a Fokker-Planck training set of size 10000. The Fokker-Planck matching step requires 190 seconds for training with 10000 data points and 150 seconds to generate 100 sample paths with 100 time steps for 10 different controls. For the 2D problem, probability density estimation training takes around 0.032 seconds for 3000 sample paths, 100 time steps, and 20 training controls, with prediction taking approximately 160 seconds over a Fokker-Planck training set of size 10000. The Fokker-Planck matching step requires about 490 seconds for training and 140 seconds to generate 100 sample paths with 100 time steps for 5 different controls. These results show that, while the computational demands are higher for controlled SDEs, they remain manageable. As expected, the computational requirements increase as the sizes of the data sets are multiplied by the number of training controls.

### Linear scalar SDE

To carry out our first experiments, we consider controlled Ornstein--Uhlenbeck processes.

### Controlled Ornstein--Uhlenbeck process

Let $X{(t)}$ be a Ornstein--Uhlenbeck process with controlled mean, defined by the SDE where ${\theta \in {\mathbb{R}}},{\sigma \in {\mathbb{R}}_{+}}$, and $u:{{\lbrack 0,T\rbrack}\rightarrow{\mathbb{R}} \in \mathcal{H}}$. Moreover, we define $\mathcal{H}$ as the space of two-step functions from $\lbrack 0,T\rbrack$ to $\mathbb{R}$, namely

### Data sets

We consider a controlled OU process, and set ${\theta = 0.5},{{\sigma^{2} = {\theta/4}},{{\mu_{0} = 0.5},{\sigma_{0}^{2} = {\sigma^{2}/{({2\theta})}}}}}$, $T = 10$, and ${X{}} \sim {\mathcal{N}{(\mu_{0},\sigma_{0}^{2})}}$. In Figure 7, we plot 100 sample paths generated from this OU process for three different controls. We draw a data set of $K = 10$ controls, as shown in Figure 6, by drawing $u_{0},u_{1},t_{1}$ independently and uniformly in $\lbrack{- 2},2\rbrack$, $\lbrack{- 2},2\rbrack$, and $\lbrack 3,7\rbrack$, respectively. For the probability density estimation steps, we draw training and validation sets with ${Q/Q_{val}} = {1000/100}$ sample paths and ${M/M_{val}} = {100/100}$ time steps, respectively. For the Fokker-Planck matching step, we draw a training set ${(t_{i},x_{i})}_{i = 1}^{N} = {{\{ t_{i}\}}_{i = 1}^{20} \times {\{ x_{i}\}}_{i = 1}^{50}}$ by drawing times and positions uniformly within well-chosen intervals, and we draw a validation set with same size and distribution.

Figure 6: Training set of 10 i.i.d. piecewise-constant controls.

### Recovering the true controlled dynamics

For $K_{te} = 3$ randomly drawn controls, we generate and plot 100 sample paths using both the true and estimated coefficients, as shown in Figure 7, to assess the recovery of the true controlled dynamics. The estimated coefficients produce probability distributions that are visually comparable to the true ones, with closely matching means and variances over time. It is important to note that the three controls used for evaluation are not part of the training data.

Figure 7: Controlled Ornstein–Uhlenbeck process. 100 samples from the true (center) and estimated (bottom) SDE coefficients for three random controls u1, u2, u3 (top).

### Nonlinear multivariate SDE

To conduct nonlinear multivariate SDE experiments, we consider controlled Dubins processes.

### Controlled Dubins process

Let $X{(t)}$ be a Dubins process with a controlled angle, defined by the SDE where $v \in {\mathbb{R}}$, $\sigma > 0$, and $u:{{\lbrack 0,T\rbrack}\rightarrow{\mathbb{R}} \in \mathcal{H}}$. We define sinusoidal controls by specifying $\mathcal{H}$ as Figure 8: Training set of 20 i.i.d. sinusoidal controls.

### Data sets

We consider a controlled Dubins process and set $v = 2$, $\sigma = 0.3$, $\mu_{0} = 0$, $\sigma_{0} = 0.5$, $T = 10$, and ${X{}} \sim {\mathcal{N}{(\mu_{0},{\sigma_{0}^{2}I_{{\mathbb{R}}^{2}}})}}$. In Figure 9, we plot 100 sample paths generated from this process for five different controls. We build a data set of $K = 20$ controls, as shown in Figure 8, by drawing $a$ independently and uniformly from $\lbrack{- 1.2},1.2\rbrack$. For the probability density estimation steps, we generate a training set with $Q = 3000$ sample paths and $M = 100$ time steps. For the Fokker-Planck matching step, we draw a training set ${(u_{k},t_{i},x_{i})}_{{k \in {⟦1,20⟧}},{i \in {⟦1,500⟧}}}$ of size $10^{4}$. To avoid sampling regions where $p{(u_{k},t,x)}$ is negligible, for each $u_{k}$, we draw a set of 500 pairs ${(t_{i},x_{i})}_{i = 1}^{500}$ from a set of 5 sample paths with 100 time steps, generated using the same parameters as the controlled Dubins process but with an initial variance of $\sigma_{0} = 2.5$.

Figure 9: Controlled Dubins process. 100 samples from the true (center) and estimated (bottom) SDE coefficients for five controls (top) with a = −1, −1/2, 0, 1/2, 1 (from left to right).

### Recovering the true controlled dynamics

For $K_{te} = 5$ controls with $a = {{- 1},{- {1/2}},0,{1/2},1}$, spanning the set of possible controls $\mathcal{H}$ with $a \in {\lbrack{- 1},1\rbrack}$, we generate and plot 100 sample paths using both the true and estimated coefficients, as shown in Figure 9, to evaluate the recovery of the true controlled dynamics. The estimated coefficients yield probability distributions that are visually comparable to the true ones, with matching means and variances over time. Notably, the five controls used for evaluation are not included in the training data.

## Conclusion

In this work, we address the problem of estimating continuous, multidimensional nonlinear controlled SDEs with non-uniform diffusion---a previously unaddressed challenge. We demonstrate how dynamical system identification can be approached through (a) density estimation of the dynamics for a finite set of controls, followed by (b) least-squares regression to estimate governing coefficients, using the Fokker-Planck matching inequality. This formulation enables us to derive strong theoretical guarantees by leveraging the rich and well-established literature on nonparametric least-squares regression. We believe this work lays a promising foundation for future research by providing a robust mathematical framework for identifying complex controlled dynamical systems, supporting further exploration of challenges such as experiment design, including online and safe exploration of the control space with theoretical guarantees. Although we illustrate our findings with prototype identification tasks, future research will focus on real-world applications, such as autonomous driving and space rendezvous.

## Proofs

### Notations

For the sake of readability, we employ the following notations.

For any set $\mathcal{X}$, map $f:{{\mathcal{X} \times {\mathbb{R}}^{d}}\rightarrow{\mathbb{R}}}$, and $u:{{\lbrack 0,T\rbrack}\rightarrow{\mathbb{R}}^{d}}$, we denote ${f{(u)}} \triangleq {f{( \cdot,{u{( \cdot )}})}}$.

For any set $\mathcal{X},\mathcal{Y}$, norm $\parallel \cdot \parallel_{\mathcal{Y}}$ over $\mathcal{Y}$, and bounded map $f:{\mathcal{X}\rightarrow\mathcal{Y}}$, we denote $\kappa_{f} \triangleq {\sup_{x \in \mathcal{X}}{\|{f{(x)}}\|}_{\mathcal{Y}}}$.

For any map $f:{{\mathbb{R}}^{n}\rightarrow{\mathbb{R}}}$ and any index $i \in {⟦1,n⟧}$, the first and second partial derivatives of $f$ are denoted by $f_{i} \triangleq \frac{\partial f}{\partial x_{i}}$ and $f_{ij} \triangleq \frac{\partial^{2}f}{\partial{x_{i}{\partial x_{j}}}}$, respectively. Alternatively, if context requires, these derivatives can be denoted as $f_{x_{i}} \triangleq \frac{\partial f}{\partial x_{i}}$ and $f_{x_{i}x_{j}} \triangleq \frac{\partial^{2}f}{\partial{x_{i}{\partial x_{j}}}}$.

### Organization of the proofs

The proofs are organized as follows.

Proof of the Fokker-Planck matching inequality. The FP matching inequality is proven in Section 7.3.

Proof of $L^{2}$ learning rates. We present necessary preliminary results in Section 7.4. The $L^{2}$ learning rates are then established in Section 7.5, based on four main lemmas detailed in Sections 7.6, 7.7, 7.8, and 7.9, respectively. These main lemmas are proven thanks to auxiliary lemmas, which are proven in Section 7.10. The auxiliary lemmas rely on concentration inequalities adapted to our needs, stated in Section 7.11.

Proof of refined $L^{2}$ learning rates. Refined $L^{2}$ learning rates are derived in Section 7.12 using a similar approach to the unrefined $L^{2}$ rates, but employing refined lemmas, which are proven in Section 7.13.

Proof of $L^{\infty}$ learning rates. The proofs for the $L^{\infty}$ learning rates are provided in Section 7.14.

Proof of CVaR learning rates. The proofs for deriving CVaR learning rates are detailed in Section 7.15.

Proofs for Sobolev coefficients. The embedding property of Fokker-Planck matching, when the coefficients belong to a Sobolev space, is derived in Section 7.16.

### Proof of Lemma 3.2. ‣ 3.1 Fokker-Planck matching inequality ‣ 3 Proposed method ‣ Learning Controlled Stochastic Differential Equations")

In this section, we prove the FP matching inequality.

### Lemma 7.1 (Fokker-Planck (FP) matching inequality for $L^{2}$ learning rates)

Let ${(\mathcal{L}^{{(b,\sigma)}{(u)}})}^{\ast}$ denotes the dual of the Kolmogorov generator Under Assumption (A1) (Smooth SDE). ‣ 3.1 Fokker-Planck matching inequality ‣ 3 Proposed method ‣ Learning Controlled Stochastic Differential Equations"), the strong Fokker-Planck equation holds. Namely, we have Moreover, under Assumption (A3) (Calibrated sampling). ‣ 3.1 Fokker-Planck matching inequality ‣ 3 Proposed method ‣ Learning Controlled Stochastic Differential Equations"), there exists a constant $c > 0$ such that for any ${(\hat{b},{\hat{\sigma}}^{2})} \in \mathcal{F}$,

### Proof

Define ${\rho{(u)}} \triangleq {({p_{{\hat{b}{(u)}},{\hat{\sigma}{(u)}}} - {p{(u)}}})}$. For any $\phi \in {C_{c}^{\infty}{({\mathbb{R}}^{n},{\mathbb{R}})}}$, we have where ${f{(u,t,x)}} \triangleq {{\left(\mathcal{L}^{{\hat{b}{(u)}},{\hat{\sigma}{(u)}}} \right)^{\ast}p{(u,t,x)}} - {\frac{\partial p}{\partial t}{(u,t,x)}}}$.

Since ${\rho{(u)}{(0, \cdot)}} = 0$, applying Theorem 3.4 from Bonalli and Rudi yields where the constant ${c{(u)}} > 0$ depends continuously on ${\|{{(\hat{b},{\hat{\sigma}}^{2})}{(u)}}\|}_{W^{4 + {\lfloor\frac{n}{2}\rfloor}}}$. where $c \triangleq {T{\sup_{u \in \mathcal{H}}{c{(u)}}}}$.

To conclude, we observe that under Assumptions (A1) (Smooth SDE). ‣ 3.1 Fokker-Planck matching inequality ‣ 3 Proposed method ‣ Learning Controlled Stochastic Differential Equations"), (A2) (Uniform ellipticity). ‣ 3.1 Fokker-Planck matching inequality ‣ 3 Proposed method ‣ Learning Controlled Stochastic Differential Equations"), and (A3) (Calibrated sampling). ‣ 3.1 Fokker-Planck matching inequality ‣ 3 Proposed method ‣ Learning Controlled Stochastic Differential Equations"), the following holds where we note that for almost every ${(u,t,x)} \in {\mathcal{H} \times {\lbrack 0,T\rbrack} \times {\mathbb{R}}^{n}}$, ${\frac{\partial p}{\partial t}{(u,t,x)}} = {{(\mathcal{L}^{{(b,\sigma)}{(u)}})}^{\ast}p{(u,t,x)}}$. Additionally ${{\left(\mathcal{L}^{{(b,\sigma)}{(u)}} \right)^{\ast}p{(u,t,x)}} - {\left(\mathcal{L}^{{(\hat{b},\hat{\sigma})}{(u)}} \right)^{\ast}p{(u,t,x)}}} = {\left({\left(\mathcal{L}^{{(b,{\sigma - {\kappa I}})}{(u)}} \right)^{\ast} - \left(\mathcal{L}^{{(\hat{b},{\hat{\sigma} - {\kappa I}})}{(u)}} \right)^{\ast}} \right)p{(u,t,x)}}$. Moreover, we have ${\left(\mathcal{L}^{{(b,{\sigma - {\kappa I}})}{(u)}} \right)^{\ast}p{(u,t,x)}} = {\left(\mathcal{L}^{{(\hat{b},{\hat{\sigma} - {\kappa I}})}{(u)}} \right)^{\ast}p{(u,t,x)}} = 0$ for any ${(t,x)} \notin D$, with ${(\hat{b},{\hat{\sigma}}^{2})} \in \mathcal{F}$.

### Lemma 7.2 (Fokker-Planck (FP) matching inequality for $L^{\infty}$ learning rates)

Under Assumptions (A1) (Smooth SDE). ‣ 3.1 Fokker-Planck matching inequality ‣ 3 Proposed method ‣ Learning Controlled Stochastic Differential Equations") and (A3) (Calibrated sampling). ‣ 3.1 Fokker-Planck matching inequality ‣ 3 Proposed method ‣ Learning Controlled Stochastic Differential Equations"), there exists a constant $c > 0$ such that for any ${(\hat{b},{\hat{\sigma}}^{2})} \in \mathcal{F}$,

### Proof

Similar proof as for the Fokker-Planck inequality for $L^{2}$ learning rates, noticing that where $c \triangleq {T{\sup_{u \in \mathcal{H}}{c{(u)}}}}$.

### Useful preliminary results for proving FP matching learning rates

In this section, we state necessary results to prove FP matching learning rates for the estimator proposed in Section 3 with hard shape-constrained PSD diffusion.

### FP matching as least-squares regression

The FP matching problem can be formulated as a least-squares regression problem, expressed as where $\overset{\sim}{\phi}{(u,t,x)}$ is defined as $\overset{\sim}{\phi}:{\mathcal{Z}\rightarrow\mathcal{F}}$ is well-defined from Lemma 4.34 in Steinwart and Christmann.

### Empirical FP matching as ridge regression

By denoting $w = \left. {(w_{i})}_{i = 1}^{n} \middle| {(w_{ij})}_{{i,j} = 1}^{n} \right. \in \mathcal{G}_{n}$ and defining regularized empirical FP matching (Eq.) can be formulated as a ridge regression, expressed as where $\hat{\phi}{(t,x)}$ is defined as:

### Useful ridge estimators for Theorem 4.1. ‣ 4.1 𝐿² learning rates ‣ 4 Learning guarantees ‣ Learning Controlled Stochastic Differential Equations") proof's decompositions

We define the ridge estimator $\hat{w}$ obtained from Eq. but without the cone constraint. Namely, Furthermore, we define the ridge estimator $\overset{\sim}{w}$ whose discrepancy from the target $w$ is due to the finite sampling of $\mathcal{H} \times {\lbrack 0,T\rbrack} \times {\mathbb{R}}^{n}$ (excluding estimation errors due to ${({\hat{p}}_{k})}_{k = 1}^{K} \approx {({p{(u_{k})}})}_{k = 1}^{K}$). Namely, Moreover, we define the ridge estimator $w_{K}$, whose discrepancy from the target $w$ arises from the finite sampling of $\mathcal{H}$. Formally, This proposition characterizes the ridge estimators as products and inverses of covariance operators.

### Proposition 7.3 ($\hat{w},\overset{\sim}{w},w_{K}$ expressions)

For any operator $A$, define $A_{\lambda} \triangleq {A + {\lambda I}}$, where $\otimes$ denotes the tensor product. $\hat{w}$ yields the standard ridge regression solution with $\hat{D} \triangleq {\frac{1}{KN}{\sum_{k = 1}^{K}{\sum_{i = 1}^{N}{\frac{\partial{\hat{p}}_{k}}{\partial t}{(t_{i},x_{i})}{\hat{\phi}}_{k}{(t_{i},x_{i})}}}}}$, and $\hat{C} \triangleq {\frac{1}{KN}{\sum_{k = 1}^{K}{\sum_{i = 1}^{N}{{{{\hat{\phi}}_{k}{(t_{i},x_{i})}} \otimes {\hat{\phi}}_{k}}{(t_{i},x_{i})}}}}}$.

Similarly, $\overset{\sim}{w} = {\overset{\sim}{D}{\overset{\sim}{C}}_{\lambda}^{- 1}}$ with We also have $w_{K} = {D_{K}C_{K,\lambda}^{- 1}}$ with

### Proposition 7.4 (Attainability of $\frac{\partial p}{\partial t}$ from Assumptions (A1) (Smooth SDE). ‣ 3.1 Fokker-Planck matching inequality ‣ 3 Proposed method ‣ Learning Controlled Stochastic Differential Equations") and (A4) (Attainability assumption). ‣ 4.1 𝐿² learning rates ‣ 4 Learning guarantees ‣ Learning Controlled Stochastic Differential Equations"))

Assumption (A4) (Attainability assumption). ‣ 4.1 𝐿² learning rates ‣ 4 Learning guarantees ‣ Learning Controlled Stochastic Differential Equations") is equivalent to the existence of $W_{b} \in {{\mathbb{R}}^{n} \otimes \mathcal{G}}$ and $W_{\sigma} \in {{\mathbb{R}}^{n^{2}} \otimes {({\mathcal{G} \otimes \mathcal{G}})}}$ such that and such that the representation ${\lbrack W_{\sigma}\rbrack}_{\mathcal{G}^{n} \otimes \mathcal{G}^{n}}$ of $W_{\sigma}$ in $\mathcal{G}^{n} \otimes \mathcal{G}^{n}$ satisfies Assumption (A1) (Smooth SDE). ‣ 3.1 Fokker-Planck matching inequality ‣ 3 Proposed method ‣ Learning Controlled Stochastic Differential Equations") further ensures the existence of $w \in \mathcal{S}_{n}$ such that Furthermore, the Fokker-Planck matching $L^{2}$-risk can be written as follows (see Ciliberto et al.) with $C \triangleq {{\mathbb{E}}_{u,t,x}{\lbrack{{{\overset{\sim}{\phi}{(u,t,x)}} \otimes \overset{\sim}{\phi}}{(u,t,x)}}\rbrack}}$.

### Remark 12 (Alternative assumptions to Assumptions (A6) (Regularity of the features). ‣ Kernel-model for ∂𝑝/∂𝑡 induced from (𝑏,𝜎²). ‣ 4.2 Refined 𝐿² learning rates ‣ 4 Learning guarantees ‣ Learning Controlled Stochastic Differential Equations"))

We denote $\overset{\sim}{\phi} \triangleq {\overset{\sim}{\phi}{(u,t,x)}}$. The three following assumptions can be found in the literature of least-squares regression as alternative conditions on the regularity of the feature space \(1\) There exists $r_{1} \in {\lbrack 0,1\rbrack}$ and $c > 0$ such that \(2\) There exists $r_{2} \in {\lbrack 0,1\rbrack}$ and $c > 0$ such that \(3\) There exists $r_{3} \in {\lbrack 0,1\rbrack}$ and $c > 0$ such that Assumptions and are known as the capacity condition and embedding property, respectively. Assumptions and provide progressively finer conditions on the regularity of the features $\overset{\sim}{\phi}{(u,t,x)}$. Indeed, it is straightforward to show that Assumption implies Assumption with $r_{2} = r_{1}$, and Assumption implies Assumption with $r_{3} = r_{2}$ (see Remark 3 in Berthier et al.). In the setting of noisy kernel ridge regression, Assumption allows to refine learning rates from $n^{- {1/4}}$ ($r_{1} = 0$) to $n^{- {1/2}}$ ($r_{1} = 1$). In the setting of noiseless kernel ridge regression, Assumption allows to refine learning rates from $n^{- {1/2}}$ ($r_{2} = 0$) to $n^{- 1}$ ($r_{2} = 1$), while Assumption allows to refine them from $n^{- 1}$ ($r_{3} = 0$) to arbitrarily fast polynomial decay as $r_{3}\rightarrow{+ \infty}$. For completeness, we present these three assumptions here; however, for clarity, in this work, we base our proofs on the more stringent Assumption (instead of considering Assumptions and).

### Proof of Theorem 4.1. ‣ 4.1 𝐿² learning rates ‣ 4 Learning guarantees ‣ Learning Controlled Stochastic Differential Equations")

### Theorem 7.5 ($L^{2}$ Learning rates)

For any ${N,K} \in {\mathbb{N}}^{\ast}$, let $(\hat{b},{\hat{\sigma}}^{2})$ be the proposed estimator, with hard shape-constrained PSD diffusion, trained with $K$ controls ${(u_{k})}_{k = 1}^{K}$ i.i.d. from a probability measure $p_{c}$ over $\mathcal{H}$, and $N$ points ${(t_{i},x_{i})}_{i = 1}^{N}$ i.i.d. from a probability measure $p_{s}$ over ${\lbrack 0,T\rbrack} \times {\mathbb{R}}^{n}$. Assuming Assumptions (A1) (Smooth SDE). ‣ 3.1 Fokker-Planck matching inequality ‣ 3 Proposed method ‣ Learning Controlled Stochastic Differential Equations"), (A4) (Attainability assumption). ‣ 4.1 𝐿² learning rates ‣ 4 Learning guarantees ‣ Learning Controlled Stochastic Differential Equations"), and (A3) (Calibrated sampling). ‣ 3.1 Fokker-Planck matching inequality ‣ 3 Proposed method ‣ Learning Controlled Stochastic Differential Equations") hold true, then there exist constants ${c_{1},c_{2}} > 0$ that do not depend on $N$, $K$, or $\delta$, such that for any $\delta \in {(0,1\rbrack}$, defining $\varepsilon \triangleq {\sup_{k \in {⟦1,K⟧}}{L{({\hat{p}}_{k},{p{(u_{k})}})}}}$ where $L$ is a squared Sobolev norm defined as then with probability $1 - \delta$,

### Sketch of the proof

The proof involves decomposing the error of the proposed estimator into three components: Error stemming from the estimation of the probability densities ${({\hat{p}}_{k})}_{k = 1}^{K} \approx {({p{(u_{k})}})}_{k = 1}^{K}$, Error due to the finite sampling approximation of times $\lbrack 0,T\rbrack$ and positions ${\mathbb{R}}^{n}$, Error due to the finite sampling approximation of the space of controls $\mathcal{H}$, and then bounding each error component.

Denoting $z = {(t,x)}$, $\overset{\sim}{\phi} = {\overset{\sim}{\phi}{(u,t,x)}}$, and $\hat{\mathbb{E}}{\lbrack \cdot \rbrack}$ as the empirical expectation over the training points, this corresponds to the following successive approximations.

### Proof

The definitions of Section 7.4 allow for the following decomposition Using Lemmas 7.6, 7.7⁢𝐶^{1/2}‖_𝒢_𝑛). ‣ 7.7 Proof of Lemma 7.7 ‣ 7 Proofs ‣ Learning Controlled Stochastic Differential Equations"), 7.8⁢𝐶^{1/2}‖_𝒢_𝑛). ‣ 7.8 Proof of Lemma 7.8 ‣ 7 Proofs ‣ Learning Controlled Stochastic Differential Equations"), and 7.9⁢𝐶^{1/2}‖_𝒢_𝑛). ‣ 7.9 Proof of Lemma 7.9 ‣ 7 Proofs ‣ Learning Controlled Stochastic Differential Equations"), and Lemma 7.14. ‣ Conclusion. ‣ 7.10 Auxiliary lemmas ‣ 7 Proofs ‣ Learning Controlled Stochastic Differential Equations"), we determine that for any $\delta \in {(0,1\rbrack}$, if $\lambda \geq {c_{2}{\log\frac{2}{\delta}}{({N^{- 1} + \varepsilon})}}$, $\lambda \geq {\frac{9\kappa_{\overset{\sim}{\phi}}^{2}}{N}{\log\frac{N}{\delta}}}$, and $\lambda \geq {\frac{9\kappa_{\overset{\sim}{\phi}}^{2}}{K}{\log\frac{K}{\delta}}}$, with probability $1 - \delta$, where constants ${c_{1},c_{2}} > 0$ are independent of $N$, $K$, and $\delta$. Therefore, setting $\lambda = {{\frac{9\kappa_{\overset{\sim}{\phi}}^{2}}{N}{\log^{2}\frac{N}{\delta}}} + {\frac{9\kappa_{\overset{\sim}{\phi}}^{2}}{K}{\log^{2}\frac{K}{\delta}}}}$, we find up to overloading $c_{1} > 0$. Then, assuming $\varepsilon \leq {{\frac{1}{N}{\log^{2}\frac{N}{\delta}}} + {\frac{1}{K}{\log^{2}\frac{K}{\delta}}}}$, the condition $\lambda \geq {c_{2}{\log\frac{2}{\delta}}{({N^{- 1} + \varepsilon})}}$ holds true up to multiplying $\lambda$ by a constant, and overloading the constant $c_{1}$. Finally, Lemma 3.2. ‣ 3.1 Fokker-Planck matching inequality ‣ 3 Proposed method ‣ Learning Controlled Stochastic Differential Equations") allows to conclude the proof. ∎

### Proof of Lemma 7.6

This lemma shows that the error of ${\hat{w}}_{S}$ can be bounded by that of the unconstrained ridge estimator $\hat{w}$. This stems from the fact that using the same empirical learning objective with a subset $\mathcal{S}_{n} \subset \mathcal{G}_{n}$, rather than the full set $\mathcal{G}_{n}$, cannot increase the error, provided that $w \in \mathcal{S}_{n}$.

### Lemma 7.6

Under Assumption (A4) (Attainability assumption). ‣ 4.1 𝐿² learning rates ‣ 4 Learning guarantees ‣ Learning Controlled Stochastic Differential Equations"), the following inequality holds true.

### Proof

Furthemore, it is straightforward to derive from the definition of ${\hat{w}}_{S}$ that However, from Assumption (A4) (Attainability assumption). ‣ 4.1 𝐿² learning rates ‣ 4 Learning guarantees ‣ Learning Controlled Stochastic Differential Equations"), we have $\hat{D} = {w\hat{C}{\hat{C}}_{\lambda}^{- 1}}$. Hence, Since $w \in \mathcal{S}_{n}$, we have

### Proof of Lemma 7.7⁢𝐶^{1/2}‖_𝒢_𝑛). ‣ 7.7 Proof of Lemma 7.7 ‣ 7 Proofs ‣ Learning Controlled Stochastic Differential Equations")

This lemma bounds the error stemming from the estimation of the probability densities ${({\hat{p}}_{k})}_{k = 1}^{K} \approx {({p{(u_{k})}})}_{k = 1}^{K}$.

### Lemma 7.7 (Bound ${\|{{({\hat{w} - \overset{\sim}{w}})}C^{1/2}}\|}_{\mathcal{G}_{n}}$)

There exist constants ${c_{1},c_{2}} > 0$ that do not depend on $N,K,\delta$, such that, for any $\delta \in {(0,1\rbrack}$, with probability at least $1 - \delta$ provided that $\lambda \geq {c_{2}{\log\frac{2}{\delta}}{({N^{- 1} + \varepsilon})}}$, $\lambda \geq {\frac{18c}{N}{\log\frac{N}{\delta}}}$ and $\lambda \geq {\frac{18c}{K}{\log\frac{K}{\delta}}}$.

### Proof

Furthermore, using ${A^{- 1} - B^{- 1}} = {B^{- 1}{({B - A})}A^{- 1}}$, we have

### Bound ${\|{\hat{D} - \overset{\sim}{D}}\|}_{\mathcal{G}_{n}}$

From Lemma 7.11. ‣ 7.10 Auxiliary lemmas ‣ 7 Proofs ‣ Learning Controlled Stochastic Differential Equations"), for any $\delta \in {(0,1\rbrack}$, with probability at least $1 - \delta$ where $c > 0$ is a constant that does not depend on $N,K,\delta$.

### Bound ${\|{{\hat{C}}_{\lambda}^{- 1}C^{1/2}}\|}_{\infty}$

By Lemmas 7.12. ‣ Conclusion. ‣ 7.10 Auxiliary lemmas ‣ 7 Proofs ‣ Learning Controlled Stochastic Differential Equations") and 7.13. ‣ Conclusion. ‣ 7.10 Auxiliary lemmas ‣ 7 Proofs ‣ Learning Controlled Stochastic Differential Equations"), for any $\delta \in {(0,1\rbrack}$, if $\lambda \geq {c{\log\frac{2}{\delta}}{({N^{- 1} + \varepsilon})}}$, $\lambda \geq {\frac{18c}{N}{\log\frac{N}{\delta}}}$ and $\lambda \geq {\frac{18c}{K}{\log\frac{K}{\delta}}}$, then with probability at least $1 - \delta$, where $c > 0$ is a constant that does not depend on $N,K,\delta$.

### Bound ${\|{\overset{\sim}{D}{\overset{\sim}{C}}_{\lambda}^{- 1}{({\overset{\sim}{C} - \hat{C}})}{\hat{C}}_{\lambda}^{- 1}C^{1/2}}\|}_{\mathcal{G}_{n}}$

From Assumption (A4) (Attainability assumption). ‣ 4.1 𝐿² learning rates ‣ 4 Learning guarantees ‣ Learning Controlled Stochastic Differential Equations"), we have Then, as for bound 2., from Lemma 7.12. ‣ Conclusion. ‣ 7.10 Auxiliary lemmas ‣ 7 Proofs ‣ Learning Controlled Stochastic Differential Equations") and Lemma 7.13. ‣ Conclusion. ‣ 7.10 Auxiliary lemmas ‣ 7 Proofs ‣ Learning Controlled Stochastic Differential Equations"), we have where $c > 0$ is a constant that does not depend on $N,K,\delta$.

### Conclusion

Combining all bounds, we conclude that there exist constants ${c_{1},c_{2}} > 0$ that do not depend on $N,K,\delta$, such that, for any $\delta \in {(0,1\rbrack}$, with probability at least $1 - \delta$ if $\lambda \geq {c_{2}{\log\frac{2}{\delta}}{({N^{- 1} + \varepsilon})}}$, $\lambda \geq {\frac{18c}{N}{\log\frac{N}{\delta}}}$ and $\lambda \geq {\frac{18c}{K}{\log\frac{K}{\delta}}}$. ∎

### Proof of Lemma 7.8⁢𝐶^{1/2}‖_𝒢_𝑛). ‣ 7.8 Proof of Lemma 7.8 ‣ 7 Proofs ‣ Learning Controlled Stochastic Differential Equations")

This lemma bounds the error resulting from the finite sampling approximation of ${\lbrack 0,T\rbrack} \times {\mathbb{R}}^{n}$.

### Lemma 7.8 (Bound ${\|{{({w_{K} - w})}C^{1/2}}\|}_{\mathcal{G}_{n}}$)

Under Assumption (A4) (Attainability assumption). ‣ 4.1 𝐿² learning rates ‣ 4 Learning guarantees ‣ Learning Controlled Stochastic Differential Equations"), there exist a constant $c > 0$ that does not depend on $N,K,\delta$, such that, for any $\delta \in {(0,1\rbrack}$, with probability at least $1 - \delta$ provided that $\lambda \geq {\frac{9\kappa_{\overset{\sim}{\phi}}^{2}}{N}{\log\frac{N}{\delta}}}$ and $\lambda \geq {\frac{9\kappa_{\overset{\sim}{\phi}}^{2}}{K}{\log\frac{K}{\delta}}}$.

### Proof

From Assumption (A4) (Attainability assumption). ‣ 4.1 𝐿² learning rates ‣ 4 Learning guarantees ‣ Learning Controlled Stochastic Differential Equations"), we have The error norm can be decomposed as follows Moreover, using ${A^{- 1} - B^{- 1}} = {B^{- 1}{({B - A})}A^{- 1}}$, we have

### Bound ${\|{C_{K,\lambda}^{- {1/2}}{({\overset{\sim}{C} - C_{K}})}C_{K,\lambda}^{- {1/2}}}\|}_{\infty}$

From Proposition 7.17. ‣ 7.11 Concentration inequalities ‣ 7 Proofs ‣ Learning Controlled Stochastic Differential Equations"), for any $\delta \in {(0,1\rbrack}$, with probability at least $1 - \delta$, with $\beta = {\log\frac{4{({{\| C_{K}\|}_{\infty} + \lambda})}{{Tr}{(C_{K})}}}{\delta\lambda{\| C_{K}\|}_{\infty}}}$. Moreover, Hence, if $N^{- 1} \leq \lambda \leq {\| C_{K}\|}_{\infty}$, it is straightforward to verify that $\beta \leq {\log{({4\kappa_{\overset{\sim}{\phi}}^{2}\lambda^{- 1}\delta^{- 1}})}}$, and that there exists a constant $c > 0$ that does not depends on $\delta,N,K$ such that and same proof as Proposition 7.17. ‣ 7.11 Concentration inequalities ‣ 7 Proofs ‣ Learning Controlled Stochastic Differential Equations") gives ${\|{C_{K} - C}\|}_{\infty} \leq {cK^{- {1/2}}{\log{({K\delta^{- 1}})}}}$ for a constant $c > 0$ that does not depend on $K,\delta$, if $K^{- 1} \leq \lambda \leq {\| C\|}_{\infty}$, such that ensures $\lambda \leq {\| C_{K}\|}_{\infty}$.

### Bound ${\|{{\overset{\sim}{C}}_{\lambda}^{- {1/2}}C_{K,\lambda}^{1/2}}\|}_{\infty}{\|{C_{K,\lambda}^{1/2}C^{1/2}}\|}_{\infty}$

From Lemma 7.13. ‣ Conclusion. ‣ 7.10 Auxiliary lemmas ‣ 7 Proofs ‣ Learning Controlled Stochastic Differential Equations"), for any $\delta \in {(0,1\rbrack}$, if $\lambda \geq {\frac{9\kappa_{\overset{\sim}{\phi}}^{2}}{N}{\log\frac{N}{\delta}}}$ and $\lambda \geq {\frac{9\kappa_{\overset{\sim}{\phi}}^{2}}{K}{\log\frac{K}{\delta}}}$, with probability at least $1 - \delta$,

### Conclusion

We conclude by combining all bounds that there exist a constant $c > 0$ that does not depend on $N,K,\delta$, such that, for any $\delta \in {(0,1\rbrack}$, with probability at least $1 - \delta$ if $\lambda \geq {\frac{9\kappa_{\overset{\sim}{\phi}}^{2}}{N}{\log\frac{N}{\delta}}}$ and $\lambda \geq {\frac{9\kappa_{\overset{\sim}{\phi}}^{2}}{K}{\log\frac{K}{\delta}}}$. ∎

### Proof of Lemma 7.9⁢𝐶^{1/2}‖_𝒢_𝑛). ‣ 7.9 Proof of Lemma 7.9 ‣ 7 Proofs ‣ Learning Controlled Stochastic Differential Equations")

This lemma bounds the error stemming from the finite sampling approximation of $\mathcal{H}$, and the RKHS norm regularization.

### Lemma 7.9 (Bound ${\|{{({\overset{\sim}{w} - w})}C^{1/2}}\|}_{\mathcal{G}_{n}}$)

Under assumption (A4) (Attainability assumption). ‣ 4.1 𝐿² learning rates ‣ 4 Learning guarantees ‣ Learning Controlled Stochastic Differential Equations"), there exist a constant $c > 0$ that does not depend on $K,\delta$, such that, for any $\delta \in {(0,1\rbrack}$, with probability at least $1 - \delta$ if $\lambda \geq {\frac{9\kappa_{\overset{\sim}{\phi}}^{2}}{K}{\log\frac{K}{\delta}}}$.

### Proof

defining $w_{\lambda} = {DC_{\lambda}^{- 1}}$.

### Bound ${\|{{({w_{K} - w_{\lambda}})}C^{1/2}}\|}_{\mathcal{G}_{n}}$

Employing the same reasoning as in Lemma 7.8⁢𝐶^{1/2}‖_𝒢_𝑛). ‣ 7.8 Proof of Lemma 7.8 ‣ 7 Proofs ‣ Learning Controlled Stochastic Differential Equations"), there exists a constant $c > 0$ that does not depend on $K,\delta$, such that, for any $\delta \in {(0,1\rbrack}$, with probability at least $1 - \delta$ if $\lambda \geq {\frac{9\kappa_{\overset{\sim}{\phi}}^{2}}{K}{\log\frac{K}{\delta}}}$.

### Bound ${\|{{({w_{\lambda} - w})}C^{1/2}}\|}_{\mathcal{G}_{n}}$

From Assumption (A4) (Attainability assumption). ‣ 4.1 𝐿² learning rates ‣ 4 Learning guarantees ‣ Learning Controlled Stochastic Differential Equations"), we have

### Conclusion

We conclude by combining all bounds, that there exist a constant $c > 0$ that does not depend on $K,\delta$, such that, for any $\delta \in {(0,1\rbrack}$, with probability at least $1 - \delta$ if $\lambda \geq {\frac{9\kappa_{\overset{\sim}{\phi}}^{2}}{K}{\log\frac{K}{\delta}}}$.

### Auxiliary lemmas

This section presents auxiliary lemmas used in the proofs of the main lemmas, along with their proofs.

This lemma bounds the $L^{2}$ descrepancy between each ${\hat{\phi}}_{k}{(t,x)}$ and $\overset{\sim}{\phi}{(u_{k}, \cdot, \cdot )}$ because of the use of ${\hat{p}}_{k}$ instead of $p{(u_{k})}$ in the expression of ${\hat{\phi}}_{k}{(t,x)}$.

### Lemma 7.10 (Bound ${\mathbb{E}}_{t,x}{\lbrack{\|{{\overset{\sim}{\phi}{(u_{k},t,x)}} - {{\hat{\phi}}_{k}{(t,x)}}}\|}_{\mathcal{G}_{n}}^{2}\rbrack}$)

For any $k \in {⟦1,K⟧}$, the following inequality holds with $L{(p_{1},p_{2})} \triangleq \int_{t = 0}^{T}\left(\parallel\frac{\partial p_{1}}{\partial t}{(t,.)} - \frac{\partial p_{2}}{\partial t}{(t,.)} \parallel_{L^{2}}^{2} + \parallel p_{1}{(t,.)} - p_{2}{(t,.)} \parallel_{W^{2}}^{2} \right)dt$,\and $\kappa_{tot} \triangleq {\sum_{{i,j} = 1}^{n}\left({\kappa_{\phi}^{2} + \kappa_{\phi_{i}}^{2} + \kappa_{\phi}^{4} + \kappa_{\phi_{i}}^{4} + \kappa_{\phi_{j}}^{4} + \kappa_{\phi_{ij}}^{4}} \right)}$.

### Proof

Then, one can obtain a similar bound for ${\|{{{\overset{\sim}{\phi}}_{ij}{(u_{k},t,x)}} - {{\hat{\phi}}_{ij}^{k}{(t,x,{u_{k}{(t)}})}}}\|}_{\mathcal{G}_{n}}^{2}$ involving a sum of the difference of the second order derivatives with respect to $x$. Using these two bounds, we obtain Lemma 7.10-ϕ̂_𝑘⁢(𝑡,𝑥)‖_𝒢_𝑛²]). ‣ 7.10 Auxiliary lemmas ‣ 7 Proofs ‣ Learning Controlled Stochastic Differential Equations") allows us to derive the three following lemmas which bounds the two error terms appearing in the main lemmas' proofs, which stem from the estimation ${\hat{p}}_{k}$ of $p{(u_{k})}$.

### Lemma 7.11 (Bound ${\|{\hat{D} - \overset{\sim}{D}}\|}_{\mathcal{G}_{n}}$)

For any $\delta \in {(0,1\rbrack}$, with probability at least $1 - \delta$ where $c > 0$ is a constant that does not depend on $N,K,\delta$.

### Proof

### Bound ${\|{{\hat{E}}_{1} - E_{1}}\|}_{\mathcal{G}_{n}}$

To apply Proposition 7.17. ‣ 7.11 Concentration inequalities ‣ 7 Proofs ‣ Learning Controlled Stochastic Differential Equations"), we define Then, denoting $\varepsilon \triangleq {\sup_{k}{L{({\hat{p}}_{k},{p{(u_{k})}})}}}$, from Proposition 7.17. ‣ 7.11 Concentration inequalities ‣ 7 Proofs ‣ Learning Controlled Stochastic Differential Equations"), we have, for any $\delta \in {(0,1\rbrack}$, with probability at least $1 - \delta$,

### Bound ${\|{{\hat{E}}_{2} - E_{2}}\|}_{\mathcal{G}_{n}}$

To apply Proposition 7.17. ‣ 7.11 Concentration inequalities ‣ 7 Proofs ‣ Learning Controlled Stochastic Differential Equations"), we define and, from Lemma 7.10-ϕ̂_𝑘⁢(𝑡,𝑥)‖_𝒢_𝑛²]). ‣ 7.10 Auxiliary lemmas ‣ 7 Proofs ‣ Learning Controlled Stochastic Differential Equations"), we obtain Then, from Proposition 7.17. ‣ 7.11 Concentration inequalities ‣ 7 Proofs ‣ Learning Controlled Stochastic Differential Equations"), we have, for any $\delta \in {(0,1\rbrack}$, with probability at least $1 - \delta$,

### Bound ${\| E_{1}\|}_{\mathcal{G}_{n}}$

### Bound ${\| E_{2}\|}_{\mathcal{G}_{n}}$

### Conclusion

We conclude by combining all bounds that there exists a constant $c > 0$ that does not depend on $N,K,\delta$, such that, for any $\delta \in {(0,1\rbrack}$, with probability at least $1 - \delta$

### Lemma 7.12 (Bound ${\|{\hat{C} - \overset{\sim}{C}}\|}_{\mathcal{G}_{n}}$)

For any $\delta \in {(0,1\rbrack}$, with probability at least $1 - \delta$, Moreover, if $\lambda \geq {2c{\log\frac{2}{\delta}}{({N^{- 1} + \varepsilon})}}$, where $c > 0$ is a constant that does not depend on $N,K,\delta$.

### Proof

Defining the operator $B_{n} = {{\overset{\sim}{C}}_{\lambda}^{- {1/2}}{({\overset{\sim}{C} - \hat{C}})}{\overset{\sim}{C}}_{\lambda}^{- {1/2}}}$, if ${\| B_{n}\|}_{\infty} < 1$, we have Then, following the same proof as for Lemma 7.11. ‣ 7.10 Auxiliary lemmas ‣ 7 Proofs ‣ Learning Controlled Stochastic Differential Equations") leads, for any $\delta \in {(0,1\rbrack}$, with probability at least $1 - \delta$ where $c > 0$ is a constant that does not depend on $N,K,\delta$.

Hence, if $\lambda \geq {2c{\log\frac{2}{\delta}}{({N^{- 1} + \varepsilon})}}$, we have

### Lemma 7.13 (Bound ${\|{{\overset{\sim}{C}}_{\lambda}^{- {1/2}}C^{1/2}}\|}_{\infty}$)

For any $\delta \in {(0,1\rbrack}$, if $\lambda \geq {\frac{9\kappa_{\overset{\sim}{\phi}}^{2}}{N}{\log\frac{N}{\delta}}}$ and $\lambda \geq {\frac{9\kappa_{\overset{\sim}{\phi}}^{2}}{K}{\log\frac{K}{\delta}}}$, with probability at least $1 - \delta$,

### Proof

Therefore, applying Lemma 7.18. ‣ 7.11 Concentration inequalities ‣ 7 Proofs ‣ Learning Controlled Stochastic Differential Equations") two times gives us, for any $\delta \in {(0,1\rbrack}$, if $\lambda \geq {\frac{9\kappa_{\overset{\sim}{\phi}}^{2}}{N}{\log\frac{N}{\delta}}}$ and $\lambda \geq {\frac{9\kappa_{\overset{\sim}{\phi}}^{2}}{K}{\log\frac{K}{\delta}}}$, then with probability at least $1 - \delta$, with $\kappa_{\overset{\sim}{\phi}} \triangleq {\sup_{{(u,t,x)} \in {\mathcal{H} \times {\lbrack 0,T\rbrack} \times {\mathbb{R}}^{n}}}{\|{\overset{\sim}{\phi}{(u,t,x)}}\|}}$. ∎ The following lemma provide bounds for all supremum norms involves in our proofs.

### Lemma 7.14 (Bound all $\kappa$s)

Recall that, for any set $\mathcal{X}$, any Hilbert space $\mathcal{H}$, and any map $f:{\mathcal{X}\rightarrow\mathcal{Y}}$, we note The following list of constants $\kappa$s can be bounded by a constant that does not depend on $K$.

### Proof

Let us start with Same inequality holds for ${\hat{\phi}}_{k}$ but with ${\hat{p}}_{k}$ instead of $p$.

We conclude by noticing that the following kappas are bounded in our assumptions (independently of $k$): $\kappa_{\phi},\kappa_{\phi_{i}},\kappa_{\phi_{ij}},\kappa_{p},\kappa_{\frac{\partial p}{\partial x_{j}}},\kappa_{\frac{\partial^{2}p}{\partial{x_{i}{\partial x_{j}}}}},\kappa_{\frac{\partial p}{\partial t}},\kappa_{{\hat{p}}_{k}},\kappa_{\frac{\partial{\hat{p}}_{k}}{\partial x_{j}}},\kappa_{\frac{\partial^{2}{\hat{p}}_{k}}{\partial{x_{i}{\partial x_{j}}}}},\kappa_{\frac{\partial{\hat{p}}_{k}}{\partial t}}$. ∎

### Concentration inequalities

In this section, we provide the concentration inequalities used in the lemmas' proofs.

The following inequality is essentally a restatement of Proposition 2 of Rudi and Rosasco.

### Proposition 7.15 (Bernstein's inequality for sum of random vectors)

Let $\mathcal{Z}$ be a Polish space, $M:{\mathcal{Z}\rightarrow\mathcal{H}}$ be bounded maps with values in a separable Hilbert space $\mathcal{H}$, such that $\kappa_{M} \triangleq {\sup_{z \in \mathcal{Z}}{\|{M{(z)}}\|}_{\mathcal{H}}}$. Let $z_{1},\ldots,z_{N}$ be a sequence of independent and identically distributed random vectors. Then, for any $\delta \in {(0,1\rbrack}$, with probability at least $1 - \delta$, with $\sigma^{2} = {{\mathbb{E}}{\lbrack{\|{M{(z)}}\|}_{HS}^{2}\rbrack}}$.

### Proof

For $p \in {\mathbb{N}}^{\ast}$, we have One can conclude that, for $p \geq 2$, with $\sigma^{2} = {{\mathbb{E}}{\lbrack{\|{{{\psi{(z)}} \otimes \phi}{(z)}}\|}_{HS}^{2}\rbrack}}$, and $M = {8\kappa_{M}}$.

Then, application of Proposition 2 of Rudi and Rosasco gives us with probability at least $1 - \delta$. ∎ From Proposition 7.15. ‣ 7.11 Concentration inequalities ‣ 7 Proofs ‣ Learning Controlled Stochastic Differential Equations"), we deduce the following inequality.

### Proposition 7.16 (Covariance estimation, $\parallel. \parallel_{HS}$)

Let $\mathcal{Z}$ be a Polish space, ${\psi,\phi}:{\mathcal{Z}\rightarrow\mathcal{H}}$ be bounded maps with values in a separable Hilbert space $\mathcal{H}$, such that ${\kappa_{\psi} \triangleq {\sup_{z \in \mathcal{Z}}{\|{\psi{(z)}}\|}}},{\kappa_{\phi} \triangleq {\sup_{z \in \mathcal{Z}}{\|{\phi{(z)}}\|}}}$. Let $z_{1},\ldots,z_{N}$ be a sequence of independent and identically distributed random vectors. Then, for any $\delta \in {(0,1\rbrack}$, with probability at least $1 - \delta$, with $\sigma^{2} = {{\mathbb{E}}{\lbrack{\|{{{\psi{(z)}} \otimes \phi}{(z)}}\|}_{HS}^{2}\rbrack}}$, and $M = {8\kappa_{\psi}\kappa_{\phi}}$.

### Proof

For $i \in {⟦1,N⟧}$, we consider the random Hilbert-Schmidt operators and such that Then, application of Proposition 7.15. ‣ 7.11 Concentration inequalities ‣ 7 Proofs ‣ Learning Controlled Stochastic Differential Equations") gives us the desired bound. ∎ The following proposition adapts Proposition 7.16. ‣ 7.11 Concentration inequalities ‣ 7 Proofs ‣ Learning Controlled Stochastic Differential Equations") for our purposes.

### Proposition 7.17 (Mixed covariance estimation, $\parallel. \parallel_{HS}$)

Let $\mathcal{X},\mathcal{Y}$ be Polish spaces, ${\psi,\phi}:{{\mathcal{X} \times \mathcal{Y}}\rightarrow\mathcal{H}}$ be bounded maps with values in a separable Hilbert space $\mathcal{H}$, such that ${\kappa_{\psi} \triangleq {\sup_{{(x,y)} \in {\mathcal{X} \times \mathcal{Y}}}{\|{\psi{(x,y)}}\|}}},{\kappa_{\phi} \triangleq {\sup_{{(x,y)} \in {\mathcal{X} \times \mathcal{Y}}}{\|{\phi{(x,y)}}\|}}}$. Let $x_{1},\ldots,y_{N}$ be a sequence of independent and identically distributed random vectors. Then, for any $\delta \in {(0,1\rbrack}$, with probability at least $1 - \delta$, with $\sigma^{2} = {{\mathbb{E}}_{x,y}{\lbrack{\|{{{\psi{(x,y)}} \otimes \phi}{(x,y)}}\|}_{HS}^{2}\rbrack}}$, and $M = {8\kappa_{\psi}\kappa_{\phi}}$.

### Proof

Same proof as Proposition 7.16. ‣ 7.11 Concentration inequalities ‣ 7 Proofs ‣ Learning Controlled Stochastic Differential Equations") but defining $M_{i} = {{\mathbb{E}}_{y}{\lbrack{{{\psi{(x,y)}} \otimes \phi}{(x,y)}}\rbrack}}$ instead of $M_{i} = {{{\psi{(x)}} \otimes \phi}{(x)}}$. ∎ The following proposition adapts Lemma 3.6 in Rudi et al. to handle "mixed" covariance estimation.

### Proposition 7.18 (Mixed covariance estimation, $\parallel. \parallel_{\infty}$)

Let $\mathcal{X},\mathcal{Y}$ be Polish spaces, $\phi:{{\mathcal{X} \times \mathcal{Y}}\rightarrow\mathcal{H}}$ a bounded maps with values in a separable Hilbert space $\mathcal{H}$ such that $\kappa_{\phi} \triangleq {\sup_{{(x,y)} \in {\mathcal{X} \times \mathcal{Y}}}{\|{\phi{(x,y)}}\|}}$. Let $x_{1},\ldots,x_{N}$ be a sequence of independent and identically distributed random vectors. Let Then, for any $\delta \in {(0,1\rbrack}$, with probability at least $1 - \delta$, with $\beta = {\log\frac{4{({{\| C\|}_{\infty} + \lambda})}{{Tr}{(C)}}}{\delta\lambda{\| C\|}_{\infty}}}$.

In particular, if $\lambda \geq {\frac{18\kappa_{\phi}^{2}}{N}{\log\frac{N}{\delta}}}$,

### Proof

Same proof than Lemma 3.6 of Rudi et al., but defining instead of $Z_{i} \triangleq {{{C_{\lambda}^{- {1/2}}\phi{(x_{i})}} \otimes C_{\lambda}^{- {1/2}}}\phi{(x_{i})}}$.

More precisely, defining $U_{i} \triangleq {C_{\lambda}^{- {1/2}}\phi{(x_{i},y)}}$, we have $Z_{i} = {{\mathbb{E}}_{y|x_{i}}{\lbrack{U_{i} \otimes U_{i}}\rbrack}}$ instead of $Z_{i} = {U_{i} \otimes U_{i}}$.

Moreover, notice that using the inequality ${{\mathbb{E}}{(M)}^{2}} \preceq {{\mathbb{E}}{(M^{2})}}$ for are a random variable $M$ with values in the space of bounded self-adjoint operators.

### Proof of Theorem 4.2. ‣ Kernel-model for ∂𝑝/∂𝑡 induced from (𝑏,𝜎²). ‣ 4.2 Refined 𝐿² learning rates ‣ 4 Learning guarantees ‣ Learning Controlled Stochastic Differential Equations")

The following theorem establishes refined learning rates for the proposed estimator, showing that for regular problems, the rates of FP matching can improve at arbitrarily fast polynomial rates. However, this gain is constrained by the accuracy of the ${\hat{p}}_{k}$. In particular, the error remains greater than the $L^{2}$ error of any ${\hat{p}}_{k}$.

### Theorem 7.19 (Refined $L^{2}$ learning rates)

Under the assumptions of Theorem 4.1. ‣ 4.1 𝐿² learning rates ‣ 4 Learning guarantees ‣ Learning Controlled Stochastic Differential Equations"), Assumption (A5) (Regularity of ∂𝑝/∂𝑡). ‣ Kernel-model for ∂𝑝/∂𝑡 induced from (𝑏,𝜎²). ‣ 4.2 Refined 𝐿² learning rates ‣ 4 Learning guarantees ‣ Learning Controlled Stochastic Differential Equations"), and Assumption (A6) (Regularity of the features). ‣ Kernel-model for ∂𝑝/∂𝑡 induced from (𝑏,𝜎²). ‣ 4.2 Refined 𝐿² learning rates ‣ 4 Learning guarantees ‣ Learning Controlled Stochastic Differential Equations"), then there exist constants ${c_{1},c_{2}} > 0$ that do not depend on $N,K,\delta$, such that for any $\delta \in {(0,1\rbrack}$, defining $\varepsilon_{\infty} \triangleq {\sup_{k \in {⟦1,K⟧}}{L^{\infty}{({\hat{p}}_{k},{p{(u_{k})}})}}}$ where $L^{\infty}$ is a squared Sobolev norm defined as taking $\lambda = {c_{2}\left({\left({\frac{18c}{N}{\log^{2}\frac{N}{\delta}}} \right)^{\frac{1}{1 - r}} + \left({\frac{18c}{K}{\log^{2}\frac{K}{\delta}}} \right)^{\frac{1}{1 - s}}} \right)}$, if then with probability $1 - \delta$,

### Proof

The definitions of Section 7.4 allow for the following decomposition Using Lemma7.6, refined Lemmas 7.21. ‣ 7.13 Proof of refined lemmas ‣ 7 Proofs ‣ Learning Controlled Stochastic Differential Equations"), 7.22. ‣ 7.13 Proof of refined lemmas ‣ 7 Proofs ‣ Learning Controlled Stochastic Differential Equations"), and 7.23. ‣ 7.13 Proof of refined lemmas ‣ 7 Proofs ‣ Learning Controlled Stochastic Differential Equations"), and Lemma 7.14. ‣ Conclusion. ‣ 7.10 Auxiliary lemmas ‣ 7 Proofs ‣ Learning Controlled Stochastic Differential Equations"), we determine that for any $\delta \in {(0,1\rbrack}$, if $\lambda \geq {c_{2}{\log\frac{2}{\delta}}{({{N^{- 1}\varepsilon_{\infty}} + \varepsilon})}}$, $\lambda^{1 - r} \geq {\frac{18c}{N}{\log\frac{N}{\delta}}}$, and $\lambda^{1 - s} \geq {\frac{18c}{K}{\log\frac{K}{\delta}}}$, with probability $1 - \delta$, where constants ${c_{1},c_{2}} > 0$ are independent of $N$, $K$, and $\delta$. Therefore, setting $\lambda = {\left({\frac{18c}{N}{\log^{2}\frac{N}{\delta}}} \right)^{\frac{1}{1 - r}} + \left({\frac{18c}{K}{\log^{2}\frac{K}{\delta}}} \right)^{\frac{1}{1 - s}}}$, we find up to overloading $c_{1} > 0$. Assuming ${\varepsilon + {N^{- 1}\varepsilon_{\infty}}} \leq \lambda^{1 + {\alpha/2}}$, the condition $\lambda \geq {c_{2}{\log\frac{2}{\delta}}{({{N^{- 1}\varepsilon_{\infty}} + \varepsilon})}}$ holds true up to multiplying $\lambda$ by a constant, and overloading the constants $c_{1}$.

Moreover, notice that defining $\gamma = {r \land s}$, we have $\frac{\alpha + r}{1 - s} \geq \frac{\alpha + \gamma}{1 - \gamma}$, $\frac{\alpha + s}{1 - r} \geq \frac{\alpha + \gamma}{1 - r}$, $\frac{\alpha + 1}{1 - r} \geq \frac{\alpha + 1}{1 - \gamma}$, and $\frac{\alpha + 1}{1 - s} \geq \frac{\alpha + 1}{1 - \gamma}$.

Then, defining $P = {K \land N}$, we have Finally, Lemma 3.2. ‣ 3.1 Fokker-Planck matching inequality ‣ 3 Proposed method ‣ Learning Controlled Stochastic Differential Equations") allows to conclude the proof. ∎

### Proof of refined lemmas

In this section, we present refined versions of the lemmas previously utilized to establish the non-refined $L^{2}$ learning rate. To maintain clarity in our presentation, we do not restate the assumptions for each lemma if they are unchanged from their original, non-refined versions. The main ingredient for these proofs involves utilizing Assumption (A5) (Regularity of ∂𝑝/∂𝑡). ‣ Kernel-model for ∂𝑝/∂𝑡 induced from (𝑏,𝜎²). ‣ 4.2 Refined 𝐿² learning rates ‣ 4 Learning guarantees ‣ Learning Controlled Stochastic Differential Equations") and Assumption (A6) (Regularity of the features). ‣ Kernel-model for ∂𝑝/∂𝑡 induced from (𝑏,𝜎²). ‣ 4.2 Refined 𝐿² learning rates ‣ 4 Learning guarantees ‣ Learning Controlled Stochastic Differential Equations"), and performing derivations such as: to establish refined dependencies in $\lambda$. Furthermore, to avoid redundancy and streamline the presentation, we directly state the results without detailing the proofs when possible, focusing on clarifying the refinements made from their non-refined counterparts.

### Proposition 7.20 (Refined Lemma 7.18. ‣ 7.11 Concentration inequalities ‣ 7 Proofs ‣ Learning Controlled Stochastic Differential Equations"))

Assume that there exist constants $r \geq 0$ and $c > 0$ such that Then, for any $\delta \in {(0,1\rbrack}$, with probability at least $1 - \delta$: where $\beta = {\log\frac{4{({{\| C\|}_{\infty} + \lambda})}{{Tr}{(C)}}}{\delta\lambda{\| C\|}_{\infty}}}$.

In particular, if $\lambda \geq \left( {\frac{18c}{N}{\log\frac{N}{\delta}}} \right)^{\frac{1}{1 - r}}$,

### Proof

### Lemma 7.21 (Refined Lemma 7.7⁢𝐶^{1/2}‖_𝒢_𝑛). ‣ 7.7 Proof of Lemma 7.7 ‣ 7 Proofs ‣ Learning Controlled Stochastic Differential Equations"))

There exist constants ${c_{1},c_{2}} > 0$ that do not depend on $N,K,\delta$, such that, for any $\delta \in {(0,1\rbrack}$, with probability at least $1 - \delta$ provided that $\lambda \geq {c_{2}{\log\frac{2}{\delta}}{({{N^{- 1}\varepsilon_{\infty}} + \varepsilon})}}$, $\lambda \geq {\frac{18c}{N}{\log\frac{N}{\delta}}}$ and $\lambda \geq {\frac{18c}{K}{\log\frac{K}{\delta}}}$.

### Lemma 7.22 (Refined Lemma 7.8⁢𝐶^{1/2}‖_𝒢_𝑛). ‣ 7.8 Proof of Lemma 7.8 ‣ 7 Proofs ‣ Learning Controlled Stochastic Differential Equations"))

There exist a constant $c > 0$ that does not depend on $N,K,\delta$, such that, for any $\delta \in {(0,1\rbrack}$, with probability at least $1 - \delta$ provided that $\lambda^{1 - r} \geq {\frac{18c}{N}{\log\frac{N}{\delta}}}$ and $\lambda^{1 - s} \geq {\frac{18c}{K}{\log\frac{K}{\delta}}}$.

### Lemma 7.23 (Refined Lemma 7.9⁢𝐶^{1/2}‖_𝒢_𝑛). ‣ 7.9 Proof of Lemma 7.9 ‣ 7 Proofs ‣ Learning Controlled Stochastic Differential Equations"))

There exist a constant $c > 0$ that does not depend on $K,\delta$, such that, for any $\delta \in {(0,1\rbrack}$, with probability at least $1 - \delta$ if $\lambda^{1 - s} \geq {\frac{18c}{K}{\log\frac{K}{\delta}}}$.

### Lemma 7.24 (Refined Lemma 7.11. ‣ 7.10 Auxiliary lemmas ‣ 7 Proofs ‣ Learning Controlled Stochastic Differential Equations"))

For any $\delta \in {(0,1\rbrack}$, with probability at least $1 - \delta$ where $c > 0$ is a constant that does not depend on $N,K,\delta$.

### Lemma 7.25 (Refined Lemma 7.12. ‣ Conclusion. ‣ 7.10 Auxiliary lemmas ‣ 7 Proofs ‣ Learning Controlled Stochastic Differential Equations"))

For any $\delta \in {(0,1\rbrack}$, with probability at least $1 - \delta$, Moreover, if $\lambda \geq {2c{\log\frac{2}{\delta}}{({{\varepsilon_{\infty}N^{- 1}} + {\varepsilon N^{- {1/2}}} + \varepsilon})}}$, where $c > 0$ is a constant that does not depend on $N,K,\delta$.

### Lemma 7.26 (Refined Lemma 7.13. ‣ Conclusion. ‣ 7.10 Auxiliary lemmas ‣ 7 Proofs ‣ Learning Controlled Stochastic Differential Equations"))

For any $\delta \in {(0,1\rbrack}$, if $\lambda^{1 - r} \geq {\frac{18c}{N}{\log\frac{N}{\delta}}}$ and $\lambda^{1 - s} \geq {\frac{18c}{K}{\log\frac{K}{\delta}}}$, with probability at least $1 - \delta$,

### Proof of $L^{\infty}$ learning rates

### Lemma 7.27

Let $\gamma \triangleq {r \land s}$. Under the same assumptions as Theorem 4.2. ‣ Kernel-model for ∂𝑝/∂𝑡 induced from (𝑏,𝜎²). ‣ 4.2 Refined 𝐿² learning rates ‣ 4 Learning guarantees ‣ Learning Controlled Stochastic Differential Equations"), for any $\alpha \in {\lbrack 0,1\rbrack}$, with probability at least $1 - \delta$, we have where $c > 0$ is independent of $N,K,\delta$.

### Proof

Theorem 4.2. ‣ Kernel-model for ∂𝑝/∂𝑡 induced from (𝑏,𝜎²). ‣ 4.2 Refined 𝐿² learning rates ‣ 4 Learning guarantees ‣ Learning Controlled Stochastic Differential Equations") provides the bound taking $\lambda = {c_{2}\left({\left({\frac{18c}{N}{\log^{2}\frac{N}{\delta}}} \right)^{\frac{1}{1 - r}} + \left({\frac{18c}{K}{\log^{2}\frac{K}{\delta}}} \right)^{\frac{1}{1 - s}}} \right)}$, where constants ${c_{1},c_{2}} > 0$ are independent of $N$, $K$, and $\delta$.

The same proof as Theorem 4.2. ‣ Kernel-model for ∂𝑝/∂𝑡 induced from (𝑏,𝜎²). ‣ 4.2 Refined 𝐿² learning rates ‣ 4 Learning guarantees ‣ Learning Controlled Stochastic Differential Equations") leads, under the exact same assumptions, to the bound

### Corollary 7.1 ($L^{\infty}$ learning rates)

Under identical conditions to those in Theorem 4.2. ‣ Kernel-model for ∂𝑝/∂𝑡 induced from (𝑏,𝜎²). ‣ 4.2 Refined 𝐿² learning rates ‣ 4 Learning guarantees ‣ Learning Controlled Stochastic Differential Equations"), then for any $\delta \in {(0,1\rbrack}$, with probability at least $1 - \delta$ where $c > 0$ is a constant independent of $N$, $K$, or $\delta$.

### Proof

We have, defining $\gamma = {r \land s}$, almost everywhere, Therefore, there exists $c > 0$, such that Then, applying Lemma 7.27 allows to conclude the proof. ∎

### Proof of CVaR learning rates

### Value at Risk (VaR)

For any $\alpha \in {\lbrack 0,1\rbrack}$, the value at risk $VaR_{\alpha}{(X)}$ of a random variable $X:{\Omega\rightarrow{\mathbb{R}}}$ is defined as the smallest of the $\alpha \times 100$% worst (greatest) values of the distribution of $X$, namely

### Conditional Value at Risk (CVaR)

For any $\alpha \in {\lbrack 0,1\rbrack}$, the conditional value at risk of a variable $X:{\Omega\rightarrow{\mathbb{R}}}$ is defined as When the cumulative distribution function of $X$ is continuous at $VaR_{\alpha}{(X)}$, it holds that allowing to interpretate CVaR as the expected value conditional upon being within some percentage of the worst-case loss scenarios.

### Lemma 7.28

For any $f \in {L^{\infty}{({\mathbb{R}}^{n})}}$, $\alpha \in {\lbrack 0,1\rbrack}$, and two random variables ${X_{1},X_{2}}:{\Omega\rightarrow{\mathbb{R}}^{n}}$ with probability density functions $p_{1},p_{2}$, the following bound holds

### Proof

Let $f:{{\mathbb{R}}^{n}\rightarrow{\mathbb{R}}}$ and $\alpha \in {\lbrack 0,1\rbrack}$, we note ${{C_{1},C_{2}} = {CVaR_{\alpha}{({f{(X_{1})}})}}},{CVaR_{\alpha}{({f{(X_{2})}})}}$, ${{V_{1},V_{2}} = {VaR_{\alpha}{({f{(X_{1})}})}}},{VaR_{\alpha}{({f{(X_{1})}})}}$.

If ${\max{(V_{1},V_{2})}} = V_{2}$, for any $f:{{\mathbb{R}}^{n}\rightarrow{\mathbb{R}}}$, we have as ${\int\limits_{{f{(x)}} \leq V_{1}}{p_{1}{(x)}{dx}}} = {{\mathbb{P}}{({{f{(X_{1})}} \leq V_{1}})}} = {1 - \alpha}$ by definition of $V_{1}$, and similarly ${\int\limits_{{f{(x)}} \leq V_{2}}{p_{2}{(x)}{dx}}} = {1 - \alpha}$.

Finally, we obtain ${|{C_{1} - C_{2}}|} \leq {\alpha^{- 1}{\| f\|}_{\infty}{\|{p_{1} - p_{2}}\|}_{L^{1}}}$. If ${\max{(V_{1},V_{2})}} = V_{1}$, by symmetry, the same bound holds.

### Lemma 7.29

For any $f \in {L^{2}{({\mathbb{R}}^{n})}}$, if there exists $\beta > 1$ such that ${\|{fx^{\beta}}\|}_{L^{1}{({\mathbb{R}}^{n})}} < {+ \infty}$, then we have

### Proof

For $f \in {L^{2}{({\mathbb{R}}^{n})}}$, and $R > 0$, denoting $\mathcal{B} = {B_{R}^{{\mathbb{R}}^{n}}{}}$, we have Furthermore, similar proof than for the standard Markov's inequality gives Now, taking $R = {\| f\|}_{L^{2}{({\mathbb{R}}^{n})}}^{- \frac{n/2}{\beta + {n/2}}}$, gives

### Lemma 7.30 (Bounded moments of SDE solutions)

Denote $X_{\hat{b},\hat{\sigma}}{(u)}$ the solution to the SDE driven by ${(\hat{b},\sigma^{2})} \in \mathcal{F}$ under control $u \in {W^{4 + {\lfloor\frac{n}{2}\rfloor}}{({\lbrack 0,T\rbrack},{\mathbb{R}}^{d})}}$. Under Assumption (A1) (Smooth SDE). ‣ 3.1 Fokker-Planck matching inequality ‣ 3 Proposed method ‣ Learning Controlled Stochastic Differential Equations") and (A3) (Calibrated sampling). ‣ 3.1 Fokker-Planck matching inequality ‣ 3 Proposed method ‣ Learning Controlled Stochastic Differential Equations"), if ${{\mathbb{E}}{\lbrack{\| X_{0}\|}^{\beta}\rbrack}} < \infty$ for some $\beta > 2$, then there exists a constant $C > 0$ such that, for all $t \in {\lbrack 0,T\rbrack}$,

### Proof

Applying Hölder's and Burkholder-Davis-Gundy inequalities, we can find a constant $C > 0$ such that, for all $t \in {\lbrack 0,T\rbrack}$, Using classical embedding results (see, for instance, Theorem 2.1 in Bonalli and Rudi), results on composition for Sobolev spaces (see Theorem 9.1 in Bourdaud), along with Assumptions (A1) (Smooth SDE). ‣ 3.1 Fokker-Planck matching inequality ‣ 3 Proposed method ‣ Learning Controlled Stochastic Differential Equations") and (A3) (Calibrated sampling). ‣ 3.1 Fokker-Planck matching inequality ‣ 3 Proposed method ‣ Learning Controlled Stochastic Differential Equations"), and the condition $u \in {W^{4 + {\lfloor\frac{n}{2}\rfloor}}{({\lbrack 0,T\rbrack},{\mathbb{R}}^{d})}}$, we conclude that the drift $b{(\cdot, \cdot,{u{(\cdot)}})}$ and diffusion $\sigma{(\cdot, \cdot,{u{(\cdot)}})}$ are uniformly bounded. It follows that there exists a constant $C > 0$ such that

### Proof of Lemma 4.7

We recall the following result.

### Sobolev Spaces and regularity assumptions

Consider a least-squares regression problem where $f^{\ast}$ is $s$-times differentiable, and there exist constants ${c_{1},c_{2}} > 0$ such that ${c_{1}d\nu} \leq {d\rho_{z}} \leq {c_{2}d\nu}$ holds $\rho_{z}$-almost surely, with $\nu$ being the Lebesgue measure. Let $q > \frac{m}{2}$, and let $\mathcal{Z} \subset {\mathbb{R}}^{m}$ be a bounded subset of ${\mathbb{R}}^{m}$ with Lipschitz boundary. The Matérn kernel where $\mathcal{K}_{\frac{m}{2} - q}$ is the modified Bessel function of the second kind, induces the RKHS $\mathcal{F} = {W^{q}{(\mathcal{Z})}}$, where $W^{q}{(\mathcal{Z})}$ denotes the Sobolev space of smoothness $q$. The source condition is verified for $\alpha = {\frac{s}{q} - 1}$, and the embedding property is verified for any parameter $r > {1 - \frac{m}{2q}}$. For more details, we refer the reader to Example 2 in Pillaud-Vivien et al., Section 4 in Fischer and Steinwart, and Wendland, Steinwart et al..

### Regularity of Fokker-Planck matching

The previous result on Sobolev RKHS is not directly applicable to our setting. The chosen hypothesis spaces $\mathcal{F}$ for the coefficients and $\mathcal{H}$ for the controls induce the hypothesis space $\mathcal{M}$ for the Fokker-Planck matching. More precisely, Nevertheless, the following lemma establishes the embedding property for Fokker-Planck matching when the coefficients belong to a Sobolev space, and the control spaces is smoothly parametrized.

### Lemma 7.31

Let $q > {\frac{1 + n + m}{2} + 4}$, and $\mathcal{H} = \left. \{ u_{\theta} \middle| {\theta \in {\mathbb{R}}^{m}}\} \right.$ with ${\theta,t}\mapsto{u_{\theta}{(t)}} \in {W^{q}{({{\mathbb{R}}^{m} \times {\lbrack 0,T\rbrack}})}}$. Assume $\sigma^{2}$ is uniformly elliptic, with ${\forall{(t,x)}} \in {{{\lbrack 0,T\rbrack} \times {\mathbb{R}}^{n}}\sigma^{2}{(t,x)}} \geq {\kappa I_{{\mathbb{R}}^{n \times n}}}$ with $\kappa > 0$, and ${(b,{\sigma^{2} - {\kappa I_{{\mathbb{R}}^{n \times n}}}})} \in {W^{q}{({{\lbrack 0,T\rbrack} \times {\mathbb{R}}^{n} \times {\mathbb{R}}^{d}},{\mathbb{R}}^{n + n^{2}})}}$. Assume further that ${\theta,t,x}\mapsto{p{(u_{\theta},t,x)}} \in {W^{q - 2}{({{\mathbb{R}}^{m} \times {\lbrack 0,T\rbrack} \times {\mathbb{R}}^{n}},{\mathbb{R}})}}$. Additionally, let $p_{s},p_{c}$ be such that there exist constants ${c_{1},c_{2},c_{3},c_{4}} > 0$ ensuring $c_{1} \leq {p_{s}{(t,x)}} \leq c_{2}$ holds $p_{s}$-almost surely and $c_{3} \leq {p_{c}{(u)}} \leq c_{4}$ holds $p_{c}$-almost surely, and assume that the partial derivatives of $(b,{\sigma^{2} - {\kappa I_{{\mathbb{R}}^{n \times n}}}})$ are supported within the bounded set $D \triangleq {\text{supp}{(p_{s})}}$. Then, using a kernel that induces the Sobolev RKHS $W^{q}{({D \times {\mathbb{R}}^{d}},{\mathbb{R}}^{n + n^{2}})}$, the Assumptions (A1) (Smooth SDE). ‣ 3.1 Fokker-Planck matching inequality ‣ 3 Proposed method ‣ Learning Controlled Stochastic Differential Equations"), (A2) (Uniform ellipticity). ‣ 3.1 Fokker-Planck matching inequality ‣ 3 Proposed method ‣ Learning Controlled Stochastic Differential Equations"), (A3) (Calibrated sampling). ‣ 3.1 Fokker-Planck matching inequality ‣ 3 Proposed method ‣ Learning Controlled Stochastic Differential Equations"), (A4) (Attainability assumption). ‣ 4.1 𝐿² learning rates ‣ 4 Learning guarantees ‣ Learning Controlled Stochastic Differential Equations") are met, Assumption (A5) (Regularity of ∂𝑝/∂𝑡). ‣ Kernel-model for ∂𝑝/∂𝑡 induced from (𝑏,𝜎²). ‣ 4.2 Refined 𝐿² learning rates ‣ 4 Learning guarantees ‣ Learning Controlled Stochastic Differential Equations") is satisfied with $\alpha = 0$, Assumptions (A6) (Regularity of the features). ‣ Kernel-model for ∂𝑝/∂𝑡 induced from (𝑏,𝜎²). ‣ 4.2 Refined 𝐿² learning rates ‣ 4 Learning guarantees ‣ Learning Controlled Stochastic Differential Equations") are satisfied with $r = {1 - \frac{m}{2{({q - 2})}}}$ and $s = {1 - \frac{n + 1}{2{({q - 2})}}}$.

### Proof

The induced space for Fokker-Planck matching is a subset of the RKHS with kernel where $\overset{\sim}{\phi}:{{\mathcal{H} \times {\lbrack 0,T\rbrack} \times {\mathbb{R}}^{n}}\rightarrow\mathcal{F}}$ is the feature map previously defined.

Define the bounded set $D_{c} = {{supp}{(p_{c})}} \subset {\mathbb{R}}^{m}$. We have ${\theta,t,x}\mapsto{{(\hat{b},{\hat{\sigma}}^{2})}{(t,x,u_{\theta})}} \in {W^{q}{({D_{c} \times D},{\mathbb{R}}^{n + n^{2}})}}$ for any ${(\hat{b},{\hat{\sigma}}^{2})} \in \mathcal{F}$. This holds because ${\theta,t}\mapsto{u_{\theta}{(t)}} \in {W^{q}{({D_{c} \times {\lbrack 0,T\rbrack}})}}$ and $\mathcal{F} \subset \left. \{{(\hat{b},{{\hat{\sigma}}^{2} + {\kappa I_{{\mathbb{R}}^{n \times n}}}})} \middle| {{(\hat{b},\hat{\sigma})} \in {W_{2}^{q}{({D \times {\mathbb{R}}^{d}},{\mathbb{R}}^{n + n^{2}})}}}\} \right.$, and using results on composition for Sobolev spaces (see Theorem 9.1 in Bourdaud ). Therefore, we have $\mathcal{M} \subset {W_{2}^{q - 2}{({{\mathbb{R}}^{m} \times {\lbrack 0,T\rbrack} \times {\mathbb{R}}^{n}},{\mathbb{R}})}}$ since $p \in {W_{2}^{q - 2}{({{\mathbb{R}}^{m} \times {\lbrack 0,T\rbrack} \times {\mathbb{R}}^{n}},{\mathbb{R}})}}$ (see Theorem 6.1 in Behzadan and Holst ).

Moreover, defining the bounded linear operator for any $v \in \mathcal{F}$ and ${\theta,t,x} \in {{\mathbb{R}}^{m} \times {\lbrack 0,T\rbrack} \times {\mathbb{R}}^{n}}$, we have where ${\phi_{{q - 2},{n + 1}}{(\theta,t,x)}} \triangleq {k_{{q - 2},{n + 1}}{({(\theta,t,x)}, \cdot)}}$. Hence, for any ${\theta,t,x} \in {{\mathbb{R}}^{m} \times {\lbrack 0,T\rbrack} \times {\mathbb{R}}^{n}}$, Therefore, from the embedding property of Sobolev RKHSs, we have This concludes the proof for obtaining Assumption (A6.1). Similar proof gives Assumption (A6.2). ∎

## Implementation details of uncontrolled SDE estimation

This section details the implementation of the uncontrolled SDE estimation method proposed in Bonalli and Rudi, available on GitHub (lmotte/sde-learn) as an open-source Python library. We provide details on the computations involved, including vectorized versions for efficient computation with Python libraries such as NumPy, as well as the computational complexity of each step. In Section 8.1, we detail probability density estimation. In Section 8.2, Fokker-Planck matching is presented.

### Notations

We use the following notations. and similar notations for the partial derivatives of $\hat{g}$ and $\rho$.

### Step 1: probability density estimation

### Estimator closed-form

From Bonalli and Rudi, we have with ${k_{t}{(t)}} = {({k_{t}{(t,t_{l})}})}_{l} \in {\mathbb{R}}^{M}$, ${\hat{g}{(x)}} = {N^{- 1}\mathbf{1}^{T}{({\rho{(x,X_{kl})}})}_{k}}$, and ${\rho{(x,y)}} = {\mu^{n}{({2\pi})}^{- {n/2}}{\exp\left({- {\frac{\mu^{2}}{2}{\|{x - y}\|}^{2}}} \right)}}$. We consider $k_{t}$ defined as the Gaussian kernel with parameter $\nu$: ${k_{t}{(t,t')}} \triangleq {\exp{({- {\nu{({t - t'})}^{2}}})}}$.

### Algorithm

### Inputs

We are provided with a dataset of $Q$ sample paths ${({X^{tr}{(w_{i},t_{l})}})}_{{i \in {⟦1,Q⟧}},{l \in {⟦1,M⟧}}}$ sampled from an unknown SDE, along with the hyper-parameters ${\nu,\mu} > 0$.

### Step 1.1 ($\hat{p}$ fitting)

We compute and store $K_{t}^{- 1} = {({k_{t}{(t_{k},t_{l})}})}_{k,l}^{- 1} \in {\mathbb{R}}^{M \times M}$, ${(T_{l}^{tr})}_{l} \triangleq {(t_{l})}_{l} \in {\mathbb{R}}^{M}$, and ${(X_{kl})}_{kl} \triangleq {({X^{tr}{(w_{k},t_{l})}})}_{kl} \in {\mathbb{R}}^{Q \times M \times n}$.

The time and space complexities of this step are $\mathcal{O}{(M^{3})}$ and $\mathcal{O}{({M^{2} + {QMn}})}$, respectively.

### Step 1.2 ($\hat{p}$ prediction)

For any $T^{te} \in {\lbrack 0,T\rbrack}^{M_{te}}$ and $X^{te} \in {({\mathbb{R}}^{n})}^{N_{te}}$, the evaluations for each ${(t,x)} \in {T^{te} \times X^{te}}$ can be computed as and similar formulas hold for ${\hat{p}}_{i}$ (or ${\hat{p}}_{ij}$) by replacing $\rho$ with $\rho_{i}$ (or $\rho_{ij}$).

In particular, the fitting phase of step 2 requires the computation of the ${\hat{P}}_{ij}$ and $\hat{d}$. Using a dataset $Z^{fp} = {T^{fp} \times X^{fp}}$, with $T^{fp} \in {\mathbb{R}}^{M_{fp}}$ and $X^{fp} \in {\mathbb{R}}^{N}$, and denoting $D_{x} \triangleq {({X_{j}^{fp} - X_{il}})}_{ilj} \in {\mathbb{R}}^{N \times N \times M}$, the ${\hat{P}}_{ij}$ can be computed recursively as follows Moreover, denoting $D_{t} \triangleq {({T_{j}^{fp} - T_{l}})}_{lj} \in {\mathbb{R}}^{M_{fp} \times M}$, we have The time and space complexities are $\mathcal{O}{({QMN{\max{(M_{fp},M)}}})}$ and $\mathcal{O}{({QMN})}$, respectively.

### Outputs

We return $\hat{P},{({\hat{P}}_{i})}_{i = 1}^{n},{({\hat{P}}_{ij})}_{{i,j} = 1}^{n}$ and $\hat{d}$.

### Step 2: Fokker-Planck matching

### Estimator closed-form

### Optimization objective

We consider a uniform diffusion model where ${\sigma^{2}{(t,x)}} = {\sigma_{0}{(t,x)}^{2}I_{{\mathbb{R}}^{n}}}$, and we enforce the positivity of $\sigma^{2}$ over a subset of the training points ${(t_{i},x_{i})}_{i \in I} \subset {(t_{i},x_{i})}_{i = 1}^{N}$. Specifically, we solve the optimization problem:

### Solving the optimization problem

Given a p.d. kernel $k$ over ${\lbrack 0,T\rbrack} \times {\mathbb{R}}^{n}$, we consider the model where $\phi{(t,x)} \triangleq k{({(t,x)},{(.,.)})} \in \mathcal{G}$. Therefore, defining $w = {(\left. {(w_{b}^{i})}_{i = 1}^{n} \middle| w_{\sigma} \right.)} \in \mathcal{G}^{n + 1}$, Eq. is expressed as where $w = {(\left. w_{b} \middle| w_{\sigma} \right.)} \in \mathcal{G}^{n + 1}$, $\hat{C} = {N^{- 1}{\sum_{i = 1}^{N}{{({\overset{\sim}{\phi} \otimes \overset{\sim}{\phi}})}{(t_{i},x_{i})}}}}$, $v = {N^{- 1}{\sum_{i = 1}^{N}{{({\frac{\partial\hat{p}}{\partial t}\overset{\sim}{\phi}})}{(t_{i},x_{i})}}}}$, and Note the change of feature map $\overset{\sim}{\phi}$ compared to the non-uniform diffusion model where This can be equivalently expressed as where $\phi_{\gamma} = {\sum_{i \in I}{\gamma_{i}\phi{(t_{i},x_{i})}}}$, $U = {\sum_{i}{e_{i} \otimes {(\left. 0_{\mathcal{G}^{n}} \middle| e_{i} \right.)}_{i}}} \in {\mathcal{G} \otimes \mathcal{G}^{n + 1}}$, with ${(e_{i})}_{i}$ being an orthonormal basis of $\mathcal{G}$, ensuring $w^{\sigma} = {Uw}$.

Strong duality guarantees solvability for $w \in \mathcal{G}^{n + 1}$ via and the optimal $\gamma \in {\mathbb{R}}^{n}$ is obtained by solving the dual problem with ${QP{(\gamma)}} \triangleq {{- {\phi_{\gamma}^{\ast}UC_{\lambda}^{- 1}U^{\ast}\phi_{\gamma}}} - {2\phi_{\gamma}^{\ast}UC_{\lambda}^{- 1}v}}$.

### Closed-form formula for ${\hat{b}}_{pc},{\hat{\sigma}}_{pc}^{2}$ and $QP{(\gamma)}$

where ${\hat{w}}_{std} \triangleq {{({\hat{C} + {\lambda I}})}^{- 1}v}$ is the standard unconstrained ridge regression formula, and ${\hat{w}}_{+} \triangleq {{({\hat{C} + {\lambda I}})}^{- 1}U^{\ast}\phi_{\gamma}}$ is an adjustment stemming from the positivity constraint.

Additionally, by denoting $\overset{\sim}{K} = {{\sum_{i}{\overset{\sim}{K}}_{i}} + {\frac{1}{4}{\sum_{{i,j} = 1}^{n}{\overset{\sim}{K}}_{ii}^{jj}}}}$, we deduce using the Woodbury identity for any operators $A$ and $B$: ${({{AB} + {\lambda I}})}^{- 1} = {\lambda^{- 1}{({I - {A{({{BA} + {\lambda I}})}^{- 1}B}})}}$. Hence, setting $V_{i} = {\sum_{j}{e_{j} \otimes {(\left. e_{j} \middle| 0_{\mathcal{G}} \right.)}}}$, we derive Moreover, using ${UV_{i}^{\ast}} = 0$, we have where ${\hat{\sigma}}_{std}^{2}$ is the standard unconstrained ridge regression estimator, and using the following notations

### Gram matrices computations

The term ${(\mathcal{L}_{t}^{b,\sigma})}^{\ast}\hat{p}$ involves second derivatives of $\sigma \times \hat{p}$, leading to the feature maps ${\overset{\sim}{\phi}}_{ij}$, which are sums of four terms each. Consequently, the evaluation of the scalar product between two feature map values results in a sum of 16 terms.

### $\overset{\sim}{K}$ computation

Denoting $\odot$ as the Hadamard product, and ${{A \odot B}C} \triangleq {A \odot {({BC})}}$, we have

### Fast computation of the Gram matrices $K_{ij}^{kl}$ with Gaussian kernel

then, denoting $D_{z} \triangleq {({Z_{k} - Z_{l}})}_{{k,l} = 1}^{N}$, the $K_{pq}^{kl}$ can be computed recursively as follows. For ${i,j,k,l} \in {⟦1,n⟧}$,

### Algorithm

### Inputs

We are provided with a dataset ${(z_{l})}_{l = 1}^{N} = {({(x_{l},t_{l})})}_{l = 1}^{N}$ i.i.d. from $p_{s}$, along with a p.d. kernel $k$ over ${\lbrack 0,T\rbrack} \times {\mathbb{R}}^{n}$, and the hyper-parameter $\lambda > 0$.

### Step 2.1 ($(\hat{b},{\hat{\sigma}}^{2})$ fitting)

From Sections 8.2.1 and 8.2.2, at fitting time, one needs to compute and store The time and space complexities of this step are $\mathcal{O}{(N^{3})}$ and $\mathcal{O}{(N^{2})}$, respectively.

### Step 2.2 ($(\hat{b},{\hat{\sigma}}^{2})$ predictions)

Denoting $D_{z}^{te} = {({Z_{l} - Z_{l}^{te}})}_{k,l} \in {\mathbb{R}}^{N \times N_{te}}$, we have Then, predictions can be computed from the formulas provided in Section 7.3.

The time and space complexities of this step are $\mathcal{O}{({NN_{te}})}$ and $\mathcal{O}{({NN_{te}})}$, respectively.

### Outputs

We return the predicted SDE coefficients' values for the given test inputs.

### FP matching with Nyström approximation

Time and space complexities of Fokker-Planck matching can be reduced from $\mathcal{O}{(N^{3})}$ and $\mathcal{O}{(N^{2})}$ to $\mathcal{O}{({mN^{2}})}$ and $\mathcal{O}{({Nm})}$ by using Nyström approximation with $m$ anchors. More precisely, the Fokker-Planck matching objective with the Nyström approximation It can be solved with We deduce the following formula for ${\hat{b}}_{{ny},{pc}}$, ${\hat{\sigma}}_{{ny},{pc}}^{2}$. and the following formula for the dual problem

## Implementation details of controlled SDE estimation

This section details the implementation of the controlled SDE estimation method proposed in this work, available on GitHub (lmotte/controlled-sde-learn) as an open-source Python library. We update the formulas and computational complexity of each step provided in Section 8 for uncontrolled SDEs to adapt them for controlled SDEs.

### Step 1: probability density estimation

For controlled SDEs, the estimation of the probability density function involves repeating the algorithm from Step 1 of the uncontrolled case $K$ times. Each iteration corresponding to a specific control setting. At the end of this step, we have computed and stored and also the partial derivatives evaluations.

The time and space complexities of this step are $\mathcal{O}{({KM^{3}})}$ and $\mathcal{O}{({K{({M^{2} + {QMn}})}})}$ for fitting, and $\mathcal{O}{({KQMN{\max{(M_{fp},M)}}})}$ and $\mathcal{O}{({KQMN})}$ for predictions.

### Step 2: Fokker-Planck matching

Same algorithm but adding additional dimensions for the controls. More precisely, closed-form are updated with $z = {(t,x,v)} \in {{\lbrack 0,T\rbrack} \times {\mathbb{R}}^{n} \times {\mathbb{R}}^{d}}$ instead of $z = {(t,x)} \in {{\lbrack 0,T\rbrack} \times {\mathbb{R}}^{n}}$. We store and compute and store The time and space complexities of this step are $\mathcal{O}{({K^{3}N^{3}})}$ and $\mathcal{O}{({K^{2}N^{2}})}$ for fitting, and $\mathcal{O}{({KNN_{te}})}$ and $\mathcal{O}{({KNN_{te}})}$ for predictions.
