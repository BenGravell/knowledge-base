<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Learning Controlled Stochastic Differential Equations

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Identification of nonlinear dynamical systems is crucial across various fields, facilitating tasks such as control, prediction, optimization, and fault detection. Many applications require methods capable of handling complex systems while providing strong learning guarantees for safe and reliable performance. However, existing approaches often focus on simplified scenarios, such as deterministic models, known diffusion, discrete systems, one-dimensional dynamics, or systems constrained by strong structural assumptions such as linearity. This work proposes a novel method for estimating both drift and diffusion coefficients of continuous, multidimensional, nonlinear controlled stochastic differential equations with non-uniform diffusion. We assume regularity of the coefficients within a Sobolev space, allowing for broad applicability to various dynamical systems in robotics, finance, climate modeling, and biology. Leveraging the Fokker-Planck equation, we split the estimation into two tasks: (a) estimating system dynamics for a finite set of controls, and (b) estimating coefficients that govern those dynamics.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

We provide strong theoretical guarantees, including finite-sample bounds for \(L^2\), \(L^\infty\), and risk metrics, with learning rates adaptive to coefficients' regularity, similar to those in nonparametric least-squares regression literature. The practical effectiveness of our approach is demonstrated through extensive numerical experiments. Our method is available as an open-source Python library.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

Models of dynamical systems describe how the state of a system evolves over time. They are central in engineering, robotics, physics, biology, and economics, where they support analysis, prediction, simulation, control, optimization, and fault detection. In some settings, these models can be derived from physical, mechanical, electrical, chemical, biological, or economic principles. In many others, first-principles equations are unavailable or incomplete. This motivates data-driven system identification: learning dynamical models from observations.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

We focus on continuous-time systems subject to both random fluctuations and control inputs. Specifically, we consider controlled stochastic differential equations of the form | | $\displaystyle dX(t)$ | $\displaystyle=b(t,X(t),u(t))\,dt+\sigma(t,X(t),u(t))\,dW(t),$ | | \(1\) | | | $\displaystyle X$ | $\displaystyle\sim p_{0},\qquad u\in\mathcal{H},$ | | | where $X(t)$ is an $n$-dimensional stochastic process, $W(t)$ is a standard Brownian motion, and $p_{0}$ is a probability density on $\mathbb{R}^{n}$. The set $\mathcal{H}\subset\mathcal{F}([0,T],\mathbb{R}^{d})$ denotes a class of deterministic open-loop controls, and denote the drift and diffusion coefficients.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

We study a passive learning setting for estimating $b$ and $a=\sigma\sigma^{\top}$. The learner observes trajectories generated under $K$ controls $u_{1},\ldots,u_{K}$, but does not choose these controls as part of the estimation procedure. Instead, the controls are modeled as independent draws from a fixed, possibly unknown, distribution on $\mathcal{H}$. This setting arises naturally when inputs come from logged operation, experimental protocols, environmental forcing, or other data-collection processes in which active probing is costly, unsafe, or unavailable. For each control $u_{k}$, we observe $Q$ independent trajectories of the SDE driven by $u_{k}$, observed only at times $t_{1},\ldots,t_{M}$. Thus the data consist of repeated trajectory observations under finitely many controls. The formal sampling model is stated in Section 2.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

Our goal is to learn controlled stochastic dynamics from these passive observations while quantifying generalization across controls. The data are collected under finitely many controls $u_{1},\ldots,u_{K}$, whereas the learned model is intended to reproduce the system's density flow under new controls from the same family. We study how the learning error depends on the number of sampled controls, the state dimension, the dimension and smoothness of the control parametrization, and whether performance is measured on average or uniformly across controls.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Contributions", "weight": 1.0} -->

We propose a kernel-based estimator for multidimensional controlled SDEs whose drift and diffusion may depend nonlinearly on time, state, and control. The method extends the uncontrolled estimator of Bonalli and Rudi: it first estimates the density flows associated with the sampled controls, and then learns drift and diffusion coefficients by matching these flows through the Fokker--Planck equation.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Contributions", "weight": 1.0} -->

We prove finite-sample bounds for the density flows induced by the learned coefficients. Our main results give $L^{2}$ learning rates for the densities of the true and estimated SDEs, averaged over controls, times, and states. The bounds quantify how the error decreases with the number $K$ of sampled controls, and how the rates depend on the state dimension, the dimension of the control parametrization, and the Sobolev regularity assumptions.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Contributions", "weight": 1.0} -->

We also establish $L^{\infty}$ learning rates, uniform over the control space, together with CVaR bounds for quantities evaluated under the learned SDE. These stronger guarantees are motivated by downstream applications where uniform or tail-sensitive reliability may be needed, including prediction, simulation, and model-based control. Finally, we provide numerical experiments and open-source Python implementations for both uncontrolled and controlled SDEs, available at [lmotte/sde-learn](2411.01982v2/lmotte/sde-learn) and [lmotte/controlled-sde-learn](2411.01982v2/lmotte/controlled-sde-learn).

<!-- chunk {"id": "body-0011", "role": "body", "section": "System identification", "weight": 1.0} -->

System identification has a long history, with foundations going back to the 1960s and mature treatments developed in the following decades. A wide variety of methods for identifying dynamical systems exists. We refer to Isermann and Münchhof; Nelles for comprehensive treatments.

<!-- chunk {"id": "body-0012", "role": "body", "section": "System identification", "weight": 1.0} -->

A system identification method is usually specified by a model class, an estimation criterion, and a data-collection protocol. Common model classes include state-space models, ARX and ARMAX models, linear and polynomial models, lookup tables, fuzzy models, neural networks, and Koopman-based representations. Estimation criteria include least squares, maximum likelihood, and Bayesian methods. The choice of inputs is also central. Classical experiment design uses conditions such as persistence of excitation or criteria based on Fisher information. More recent approaches use active learning or reinforcement learning to choose informative inputs during data collection. Online and adaptive identification methods update the model while the system operates, so that the data distribution can depend on previous model estimates and control actions.

<!-- chunk {"id": "body-0013", "role": "body", "section": "System identification", "weight": 1.0} -->

In this paper, the controls are observed inputs sampled from a fixed distribution. They are not chosen adaptively, and there is no feedback from the estimator to the data-collection process. We study how the learned controlled dynamics generalize from the finitely many controls observed in the dataset to new controls drawn from the same distribution.

<!-- chunk {"id": "body-0014", "role": "body", "section": "System identification", "weight": 1.0} -->

Finite-sample guarantees are well developed for linear dynamical systems. Existing nonlinear guarantees often rely on structured model classes for the dynamics. For example, several works study systems of the form $x_{t+1}=\phi(Ax_{t}+Bu_{t})$, where the nonlinearity $\phi$ is known and fixed. Mania et al. consider models of the form $x_{t+1}=A\phi(x_{t},u_{t})+w_{t}$, under assumptions including warm starts, computational oracles, and controllability. These settings differ from ours, where the drift and diffusion of a continuous-time stochastic system are nonparametric functions of time, state, and control.

<!-- chunk {"id": "body-0015", "role": "body", "section": "Uncontrolled SDE estimation", "weight": 1.0} -->

Most statistical work on SDE coefficient estimation considers autonomous systems without control inputs. Classical results often use one long trajectory and obtain asymptotic guarantees under ergodicity assumptions. This observation model differs from ours because there are no controls, and because the information comes from long-time observation of one process rather than repeated short-horizon trajectories under several inputs.

<!-- chunk {"id": "body-0016", "role": "body", "section": "Uncontrolled SDE estimation", "weight": 1.0} -->

A more recent line of work studies SDEs from independent sample paths observed over a fixed horizon. In particular, Bonalli and Rudi estimate multidimensional SDEs by first estimating the density flow and then fitting coefficients through the Fokker--Planck equation. We use the same density-flow and Fokker--Planck matching principle, but with coefficients that also depend on a control variable.

<!-- chunk {"id": "body-0017", "role": "body", "section": "Controlled SDE estimation", "weight": 1.0} -->

For controlled SDEs, the closest finite-sample analysis we are aware of is Nüske et al.. They consider nonlinear control-affine dynamics with drift of the form $b(t,x,u_{\theta}(t))=b_{0}(x)+B_{1}(x)\theta$, where the control is parametrized by $\theta\in\mathbb{R}^{m}$. In their setting, the diffusion coefficient does not depend on time or control. The model therefore excludes drift terms with general nonlinear dependence on $t$, $x$, and $u$, and excludes diffusion coefficients $a(t,x,u)$ depending on the control. Their method also does not aim at returning explicit estimates for a general drift-diffusion pair $b(t,x,u)$, $a(t,x,u)$. The present paper studies a complementary setting, in which both $b(t,x,u)$ and $a(t,x,u)$ may depend on time, state, and control, under regularity, ellipticity, and localization assumptions.

<!-- chunk {"id": "body-0018", "role": "body", "section": "Controlled SDE estimation", "weight": 1.0} -->

The guarantees are also stated at the density-flow level, rather than in a coefficient norm.

<!-- chunk {"id": "body-0019", "role": "body", "section": "Paper Organization", "weight": 1.0} -->

The paper is organized as follows. Section 2 states the learning problem. Section 3 presents the estimation method. Section 4 gives finite-sample error bounds. Section 5 reports the numerical experiments.

<!-- chunk {"id": "body-0020", "role": "body", "section": "Problem Setting", "weight": 1.0} -->

We now introduce the learning problem.

<!-- chunk {"id": "body-0021", "role": "body", "section": "Parametrized controls", "weight": 1.0} -->

We consider deterministic open-loop controls $u:[0,T]\to\mathbb{R}^{d}$ with a finite-dimensional parametrization: where $\Theta$ is a bounded Lipschitz domain.

<!-- chunk {"id": "body-0022", "role": "body", "section": "Controlled stochastic dynamics", "weight": 1.0} -->

We consider an $n$-dimensional controlled stochastic differential equation on a fixed time horizon $T>0$. Here $W$ is a standard Brownian motion, $p_{0}$ is a probability density on $\mathbb{R}^{n}$, and are the drift and diffusion coefficients. For $\theta\in\Theta$, we write $X^{\theta}$ for the solution of driven by $u_{\theta}$, whenever a unique strong solution exists.

<!-- chunk {"id": "body-0023", "role": "body", "section": "Density flows", "weight": 1.0} -->

Let $a=\sigma\sigma^{\top}$ be the diffusion matrix. Since the law of the SDE depends on $\sigma$ only through $a$, we index density flows by $(b,a)$, not by a particular square root $\sigma$. When with coefficients $(b,a)$ admits densities, we denote the associated density flow by Thus, for each $\theta\in\Theta$ and $t\in[0,T]$, $p_{b,a}(\theta,t,\cdot)$ is the density of $X^{\theta}(t)$ with respect to Lebesgue measure on $\mathbb{R}^{n}$.

<!-- chunk {"id": "body-0024", "role": "body", "section": "Dataset", "weight": 1.0} -->

We work in an offline episodic setting. Control parameters $(\theta_{k})_{k=1}^{K}$ are sampled independently from a fixed probability distribution $\mathbb{P}_{c}$ on $\Theta$. For each $\theta_{k}$, we observe $Q$ independent trajectories of driven by $u_{\theta_{k}}$, initialized from $p_{0}$, and sampled at times $(t_{\ell})_{\ell=1}^{M}\subset[0,T]$. The dataset is A formal probabilistic construction is given in Appendix A.1.

<!-- chunk {"id": "body-0025", "role": "body", "section": "Learning problem", "weight": 1.0} -->

Our goal is to estimate, from the dataset above, coefficients $(b,a)$ whose induced density flow reproduces that of the true controlled SDE. Given a hypothesis space $\mathcal{F}$ of coefficient functions from $[0,T]\times\mathbb{R}^{n}\times\mathbb{R}^{d}$ to $\mathbb{R}^{n+n^{2}}$, we formulate the estimation problem as where $p\triangleq p_{b,a}$ is the density flow of the true controlled SDE.

<!-- chunk {"id": "body-0026", "role": "body", "section": "Remark 1 (Learning at the level of density flows)", "weight": 1.0} -->

The objective in evaluates candidate coefficients through the density flows they induce. Thus, the target is not pointwise recovery of $(b,a)$ in a coefficient norm, but reproduction of the controlled dynamics at the distributional level. As a consequence, two coefficient pairs that induce the same density flow are indistinguishable for this criterion. Example 1 ‣ Learning problem. ‣ 2 Problem Setting ‣ Learning Controlled Stochastic Differential Equations") gives a simple case where distinct SDE coefficients induce the same density flow; see also Qiu et al.; Browning et al.; Miao et al.; Wang et al. for discussions.

<!-- chunk {"id": "body-0027", "role": "body", "section": "Example 1 (Distinct SDE coefficients inducing the same density)", "weight": 1.0} -->

Different SDE coefficients may induce the same probability density. Consider the uncontrolled Ornstein--Uhlenbeck process with $\theta>0$, $\mu\in\mathbb{R}$, and $\sigma>0$. For all $t\geq 0$, $X(t)$ is Gaussian, with mean $\mu+(m-\mu)e^{-\theta t}$ and variance $\frac{\sigma^{2}}{2\theta}(1-e^{-2\theta t})+s^{2}e^{-2\theta t}$. If $m=\mu$ and $s^{2}=\sigma^{2}/(2\theta)$, the process is stationary and has density $\mathcal{N}(m,s^{2})$ at all times.

<!-- chunk {"id": "body-0028", "role": "body", "section": "Example 1 (Distinct SDE coefficients inducing the same density)", "weight": 1.0} -->

Hence different pairs $(\tilde{\theta},\tilde{\sigma})$ satisfying $\tilde{\sigma}^{2}/(2\tilde{\theta})=\sigma^{2}/(2\theta)$ define different SDEs with the same density flow.

<!-- chunk {"id": "body-0029", "role": "body", "section": "Remark 2 (Parametrized controls)", "weight": 1.0} -->

Controls are parametrized as $\mathcal{H}=\{u_{\theta}:\theta\in\Theta\}$, and the sampling distribution $\mathbb{P}_{c}$ is defined on $\Theta$. Thus, sampling $\theta\sim\mathbb{P}_{c}$ induces a random control $u_{\theta}\in\mathcal{H}$. This avoids placing probability measures directly on the infinite-dimensional function space $\mathcal{H}$. Extending the analysis to such measures, for instance Gaussian measures on separable Hilbert spaces of controls, is left for future work.

<!-- chunk {"id": "body-0030", "role": "body", "section": "Proposed Method", "weight": 1.0} -->

We now present the estimator. It has two steps: first estimate the density flows associated with the sampled controls, then estimate the coefficients by Fokker--Planck matching. Section 3.1 gives the well-posedness assumptions and the matching inequality. Section 3.2 defines the estimator.

<!-- chunk {"id": "body-0031", "role": "body", "section": "Well-Posedness and Fokker--Planck Matching Inequality", "weight": 1.0} -->

We first state the assumptions used to ensure well-posedness of the controlled SDEs and to derive the Fokker--Planck matching inequality. Here and below, $H^{s}$ denotes the Sobolev space $W^{s,2}$.

<!-- chunk {"id": "body-0032", "role": "body", "section": "Assumption A1 (Uniform ellipticity)", "weight": 1.0} -->

A coefficient pair $(b,a)$ is uniformly elliptic if there exists $\kappa>0$ such that for all $(t,x,v)\in[0,T]\times\mathbb{R}^{n}\times\mathbb{R}^{d}$.

<!-- chunk {"id": "body-0033", "role": "body", "section": "Assumption A2 (Control regularity)", "weight": 1.0} -->

Let $s_{0}\triangleq 5+n+\left\lceil\frac{d+1}{2}\right\rceil$. There exists a bounded Lipschitz domain $V\subset\mathbb{R}^{d}$ such that, for every $\theta\in\Theta$, $u_{\theta}([0,T])\subset V$ and

<!-- chunk {"id": "body-0034", "role": "body", "section": "Assumption A4 (Coefficient localization)", "weight": 1.0} -->

There exist a bounded Lipschitz domain $D\subset\mathbb{R}^{n}$, a cutoff $\xi\in C_{c}^{\infty}(\mathbb{R}^{n})$, with $0\leq\xi\leq 1$ and $\operatorname{supp}(\xi)\subset D$, and functions $b_{0},a_{0}$ such that Assumption A4 ‣ 3.1 Well-Posedness and Fokker–Planck Matching Inequality ‣ 3 Proposed Method ‣ Learning Controlled Stochastic Differential Equations") means that the drift and the localized part of the diffusion vanish outside $[0,T]\times D$, with $\xi b_{0}$ and $\xi a_{0}$ understood to be extended by zero outside $D$. There, the dynamics reduce to Brownian motion with diffusion matrix $\kappa I_{n}$. This restricts the target class.

<!-- chunk {"id": "body-0035", "role": "body", "section": "Assumption A4 (Coefficient localization)", "weight": 1.0} -->

It can also be viewed as a smooth localization of a larger non-localized model; in that case, our results apply to the localized model and do not quantify the localization bias.

<!-- chunk {"id": "body-0036", "role": "body", "section": "Assumption A5 (Coefficient regularity)", "weight": 1.0} -->

The functions $b_{0}$ and $a_{0}$ from Assumption A4 ‣ 3.1 Well-Posedness and Fokker–Planck Matching Inequality ‣ 3 Proposed Method ‣ Learning Controlled Stochastic Differential Equations") satisfy

<!-- chunk {"id": "body-0037", "role": "body", "section": "Fokker--Planck operator", "weight": 1.0} -->

For $\theta\in\Theta$, the coefficients $(b,a)$ and the control $u_{\theta}$ define a Fokker--Planck operator acting on sufficiently smooth functions $q:[0,T]\times\mathbb{R}^{n}\to\mathbb{R}$ by The objective in depends on $(\hat{b},\hat{a})$ through the density flow $p_{\hat{b},\hat{a}}$, which is defined implicitly by the SDE. The next lemma replaces this implicit quantity by an explicit residual involving the true density flow $p$ and the candidate coefficients $(\hat{b},\hat{a})$. We call this residual the Fokker--Planck matching objective.

<!-- chunk {"id": "body-0038", "role": "body", "section": "Proposed Estimator", "weight": 1.0} -->

We now define the estimator, combining density estimation with Fokker--Planck matching.

<!-- chunk {"id": "body-0039", "role": "body", "section": "Controlled SDE estimator", "weight": 1.0} -->

For each sampled parameter $\theta_{k}$, let $\hat{p}_{k}$ be the density-flow estimator of Bonalli and Rudi trained on Let $z_{i}=(s_{i},y_{i})$, $i=1,\ldots,N$, be sampled uniformly from $[0,T]\times D$. Given $(\hat{p}_{k})_{k=1}^{K}$, we define

<!-- chunk {"id": "body-0040", "role": "body", "section": "Hypothesis space", "weight": 1.0} -->

It remains to specify the hypothesis space $\mathcal{F}$ and the regularization norm. We build $\mathcal{F}$ so that its elements satisfy the structural assumptions of Lemma 3 ‣ Fokker–Planck operator. ‣ 3.1 Well-Posedness and Fokker–Planck Matching Inequality ‣ 3 Proposed Method ‣ Learning Controlled Stochastic Differential Equations"): smoothness, uniform ellipticity, and localization. Let $k$ be a continuous positive definite kernel on $[0,T]\times D\times V$, with scalar RKHS $\mathcal{H}_{k}$ continuously embedded into $H^{s_{0}}([0,T]\times D\times V)$. Typical choices include Matérn kernels of sufficiently high order. We model the drift in the vector-valued RKHS $\mathbb{R}^{n}\otimes\mathcal{H}_{k}$. For the diffusion, write $a=\kappa I_{n}+a_{0}$.

<!-- chunk {"id": "body-0041", "role": "body", "section": "Hypothesis space", "weight": 1.0} -->

We enforce $a_{0}\succeq 0$ through a positive-semidefinite kernel parametrization. With $\phi(t,x,v)=k((t,x,v),\cdot)\in\mathcal{H}_{k}$, set where $w=(w_{ij})_{i,j=1}^{n}$ is self-adjoint and positive semidefinite. This guarantees $a(t,x,v)\succeq\kappa I_{n}$. The embedding of $\mathcal{H}_{k}$ into $H^{s_{0}}$, together with the algebra property of $H^{s_{0}}$, gives the required Sobolev regularity. Finally, we enforce localization with the cutoff $\xi$ from Assumption A4 ‣ 3.1 Well-Posedness and Fokker–Planck Matching Inequality ‣ 3 Proposed Method ‣ Learning Controlled Stochastic Differential Equations").

<!-- chunk {"id": "body-0042", "role": "body", "section": "Hypothesis space", "weight": 1.0} -->

The hypothesis space $\mathcal{F}$ is the set of all pairs $(b,a)$ of the form where $b_{0}\in\mathbb{R}^{n}\otimes\mathcal{H}_{k}$ and $a_{0}$ has the positive-semidefinite kernel parametrization above. See Appendix A.5 for the definition of $\|\cdot\|_{\mathcal{F}}$.

<!-- chunk {"id": "body-0043", "role": "body", "section": "Remark 4 (Alternative ellipticity constraints)", "weight": 1.0} -->

Uniform ellipticity can also be enforced by pointwise constraints at sampled locations. Given points $\zeta_{i}\in[0,T]\times D\times V$ and directions $r_{j}\in\mathbb{R}^{n}$, one may impose In the isotropic case $a=a_{0}I_{n}$, this reduces to $a_{0}(\zeta_{i})\geq\kappa$. The guarantees in this paper are proved for the hard positive-semidefinite parametrization above; the analysis of such pointwise constraints is left for future work.

<!-- chunk {"id": "body-0044", "role": "body", "section": "Learning Guarantees", "weight": 1.0} -->

We now state finite-sample guarantees for the estimator of Section 3. The error compares the density flows of the learned and true SDEs, and is measured with respect to the sampling distribution over controls. This quantifies generalization across the control family. We first give a baseline $L^{2}$ bound under attainability (Section 4.1), then refine it using source and embedding assumptions tailored to Fokker--Planck matching (Section 4.2). We next derive uniform-in-control bounds (Section 4.3) and CVaR-type guarantees (Section 4.4). Finally, we instantiate the assumptions and rates for Sobolev coefficients (Section 4.5).

<!-- chunk {"id": "body-0045", "role": "body", "section": "$L^{2}$ Learning Rates", "weight": 1.0} -->

We start with a baseline $L^{2}$ guarantee. It relies on the following well-specifiedness condition.

<!-- chunk {"id": "body-0046", "role": "body", "section": "Assumption A6 (Attainability)", "weight": 1.0} -->

The true coefficients belong to the hypothesis space: Assumption A6 ‣ 4.1 𝐿² Learning Rates ‣ 4 Learning Guarantees ‣ Learning Controlled Stochastic Differential Equations") expresses prior information on the target coefficients: the estimator searches over a class that contains the truth. This is the standard well-specified setting in regularized least-squares regression. Some restriction of this kind is unavoidable for uniform finite-sample guarantees, by no-free-lunch phenomena. Concrete examples are given in Section 4.5.

<!-- chunk {"id": "body-0047", "role": "body", "section": "Remark 6 (Dependence on $K$ and $N$)", "weight": 1.0} -->

Although the Fokker--Planck matching objective is evaluated on $KN$ pairs $(\theta_{k},z_{i})$, the rate in Theorem 5 ‣ 4.1 𝐿² Learning Rates ‣ 4 Learning Guarantees ‣ Learning Controlled Stochastic Differential Equations") is $K^{-1/2}+N^{-1/2}$, up to logarithmic factors, not $(KN)^{-1/2}$. This reflects the product structure of the empirical approximation: controls and state-time points approximate two different integrals. Increasing $N$ improves the approximation over $[0,T]\times D$, while increasing $K$ improves the approximation over the control distribution. Thus, for fixed $K$, the bound does not vanish as $N\to\infty$.

<!-- chunk {"id": "body-0048", "role": "body", "section": "Remark 7 (Role of $\\mathbb{P}_{c}$)", "weight": 1.0} -->

The bound in Theorem 5 ‣ 4.1 𝐿² Learning Rates ‣ 4 Learning Guarantees ‣ Learning Controlled Stochastic Differential Equations") is measured in $L^{2}(\mathbb{P}_{c})$ over control parameters, equivalently over controls through the pushforward of $\mathbb{P}_{c}$ by $\theta\mapsto u_{\theta}$. Its strength therefore depends on $\mathbb{P}_{c}$: errors on controls with small $\mathbb{P}_{c}$-mass have limited effect, while controls outside its support are not controlled. Thus, $(\Theta,\mathbb{P}_{c})$ should reflect the controls for which the learned dynamics will be used. Similarly, $p_{0}$ affects which regions of the state space are explored, and therefore the parts of the dynamics that can be accurately learned. We treat both choices as fixed and do not study experimental design.

<!-- chunk {"id": "body-0049", "role": "body", "section": "Remark 8 (Sampling over $[0,T]\\times D$)", "weight": 1.0} -->

In Theorem 5 ‣ 4.1 𝐿² Learning Rates ‣ 4 Learning Guarantees ‣ Learning Controlled Stochastic Differential Equations"), the Fokker--Planck residual is sampled on the same domain $[0,T]\times D$ for all controls. This follows Assumption A4 ‣ 3.1 Well-Posedness and Fokker–Planck Matching Inequality ‣ 3 Proposed Method ‣ Learning Controlled Stochastic Differential Equations"): the coefficients are localized on a fixed bounded state domain $D\subset\mathbb{R}^{n}$, independently of the control. One could instead allow a control-dependent domain $D(u)$, provided the localization and sampling assumptions are restated accordingly. We leave this extension to future work.

<!-- chunk {"id": "body-0050", "role": "body", "section": "Refined $L^{2}$ Learning Rates", "weight": 1.0} -->

Refined rates in kernel ridge regression usually follow from two quantities: the regularity of the regression target and the effective dimension of the feature distribution. We apply this principle to the kernel least-squares problem induced by Fokker--Planck matching.

<!-- chunk {"id": "body-0051", "role": "body", "section": "Fokker--Planck regression representation", "weight": 1.0} -->

Once the density $p$ is fixed, the RKHS coefficient model of Section 3 represents every candidate pair $(b,a)\in\mathcal{F}$ by a parameter $w_{b,a}\in\mathcal{G}_{n}$ such that for almost every $(\theta,t,x)\in\Theta\times[0,T]\times D$. Here $\mathcal{G}_{n}$ is the induced Hilbert space and $\tilde{\phi}:\Theta\times[0,T]\times D\to\mathcal{G}_{n}$ is the induced Fokker--Planck feature map; both are explicitly constructed in Appendix A.5. Thus, the regression input is $(\theta,t,x)$, the target is $\partial_{t}p(\theta,t,x)$, and the feature map is $\tilde{\phi}$.

<!-- chunk {"id": "body-0052", "role": "body", "section": "Fokker--Planck regression representation", "weight": 1.0} -->

Moreover, under Assumption A6 ‣ 4.1 𝐿² Learning Rates ‣ 4 Learning Guarantees ‣ Learning Controlled Stochastic Differential Equations"), let $w\in\mathcal{G}_{n}$ be the parameter associated with the true coefficients. Then, because $p$ solves the Fokker--Planck equation, $\partial_{t}p(\theta,t,x)=\langle w,\tilde{\phi}(\theta,t,x)\rangle_{\mathcal{G}_{n}}$ almost everywhere.

<!-- chunk {"id": "body-0053", "role": "body", "section": "Assumption A7 (Source condition)", "weight": 1.0} -->

There exists $\alpha\in$ such that Assumption A7 ‣ Fokker–Planck regression representation. ‣ 4.2 Refined 𝐿² Learning Rates ‣ 4 Learning Guarantees ‣ Learning Controlled Stochastic Differential Equations") is the standard kernel-ridge source condition, adapted to Fokker--Planck matching. The case $\alpha=0$ reduces to Assumption A6 ‣ 4.1 𝐿² Learning Rates ‣ 4 Learning Guarantees ‣ Learning Controlled Stochastic Differential Equations"). Concrete examples are discussed in Section 4.5.

<!-- chunk {"id": "body-0054", "role": "body", "section": "Assumption A8 (Embedding conditions)", "weight": 1.0} -->

For any $\theta\in\Theta$ and $(t,x)\in[0,T]\times D$, define (A8.1) There exist $r\in$ and $c>0$ such that (A8.2) There exist $s\in$ and $c>0$ such that Assumption A8 ‣ Fokker–Planck regression representation. ‣ 4.2 Refined 𝐿² Learning Rates ‣ 4 Learning Guarantees ‣ Learning Controlled Stochastic Differential Equations") adapts standard embedding conditions for kernel methods to our product-sampling structure. The conditions are imposed on the Fokker--Planck feature $\tilde{\phi}$, not on the original RKHS feature map. They are also separated: $C(\theta)$ averages over state-time points for a fixed control, while $C(t,x)$ averages over controls for a fixed state-time point. Thus $r$ and $s$ measure embedding strength in the state-time and control directions. The case $r=s=0$ holds whenever $\tilde{\phi}$ is bounded; larger values encode stronger regularity.

<!-- chunk {"id": "body-0055", "role": "body", "section": "Assumption A8 (Embedding conditions)", "weight": 1.0} -->

Concrete examples are given in Section 4.5.

<!-- chunk {"id": "body-0056", "role": "body", "section": "Remark 9 (Product-space embedding and capacity)", "weight": 1.0} -->

Assumption A8 ‣ Fokker–Planck regression representation. ‣ 4.2 Refined 𝐿² Learning Rates ‣ 4 Learning Guarantees ‣ Learning Controlled Stochastic Differential Equations") implies a corresponding product-space condition. By Jensen's operator inequality, $C(\theta)\preccurlyeq c\,\mathbb{E}_{t,x}[C(t,x)^{s}]\preccurlyeq c\,C^{s},\qquad\|C^{-rs/2}\tilde{\phi}(\theta,t,x)\|_{\mathcal{G}_{n}}\leq c.$ Consequently, Thus Assumption A8 ‣ Fokker–Planck regression representation. ‣ 4.2 Refined 𝐿² Learning Rates ‣ 4 Learning Guarantees ‣ Learning Controlled Stochastic Differential Equations") implies the usual capacity condition on the product space with exponent $rs$.

<!-- chunk {"id": "body-0057", "role": "body", "section": "Remark 9 (Product-space embedding and capacity)", "weight": 1.0} -->

The embedding condition is stronger than this trace condition: in noisy kernel ridge regression, capacity conditions improve rates from $N^{-1/4}$ to $N^{-1/2}$, while embedding conditions can yield arbitrarily fast polynomial rates in the noiseless setting.

<!-- chunk {"id": "body-0058", "role": "body", "section": "Remark 9 (Product-space embedding and capacity)", "weight": 1.0} -->

We now derive refined rates for the estimator. Throughout, for real numbers $x,y$, we write $x\wedge y\triangleq\min\{x,y\}$ and $x\vee y\triangleq\max\{x,y\}$.

<!-- chunk {"id": "body-0059", "role": "body", "section": "$L^{\\infty}$ Learning Rates", "weight": 1.0} -->

The previous bounds control the density-flow error on average over controls. This may be insufficient when the learned dynamics are later evaluated for a particular control. Below, we provide a uniform-in-control guarantee, while remaining $L^{2}$ in time and state.

<!-- chunk {"id": "body-0060", "role": "body", "section": "CVaR Learning Rates", "weight": 1.0} -->

The $L^{\infty}$-in-control guarantee controls the density-flow error under each admissible control. In safety-sensitive settings, one may also want to control tail-sensitive quantities of the learned dynamics. We show that, under a moment condition, the $L^{\infty}$ rates imply guarantees for Conditional Value at Risk.

<!-- chunk {"id": "body-0061", "role": "body", "section": "Conditional Value at Risk", "weight": 1.0} -->

For $\rho\in(0,1]$, the Conditional Value at Risk of a real-valued random variable $Y$ is When $Y$ is a loss, $\mathrm{CVaR}_{\rho}(Y)$ is the expected loss in the worst $\rho$-fraction of outcomes.

<!-- chunk {"id": "body-0062", "role": "body", "section": "Remark 12 (Risk-averse control)", "weight": 1.0} -->

A typical risk-averse control objective is where $f$ is a terminal loss, $D$ is a risk measure, and $\lambda>0$ balances average performance and risk sensitivity. Compared with the risk-neutral case $\lambda=0$, the second term penalizes risk. Choosing $D$ as CVaR emphasizes adverse tail events and is widely used in risk management and stochastic control.

<!-- chunk {"id": "body-0063", "role": "body", "section": "Application to Sobolev Spaces", "weight": 1.0} -->

We now give a Sobolev setting in which the abstract assumptions of the previous sections can be checked explicitly. Sobolev regularity has already been used above to state the well-posedness and Fokker--Planck stability assumptions. Here the point is different: we use Sobolev spaces to verify the source and embedding assumptions of Section 4.2, and therefore to obtain rates with explicit dependence on the dimensions $m$ and $n$ and on the smoothness parameter $\nu$.

<!-- chunk {"id": "body-0064", "role": "body", "section": "Remark 18 (Regularity of the density flow)", "weight": 1.0} -->

Lemma 17 ‣ 4.5 Application to Sobolev Spaces ‣ 4 Learning Guarantees ‣ Learning Controlled Stochastic Differential Equations") assumes Sobolev regularity of the density flow with respect to the control parameter: This is a regularity assumption on the dependence of the Fokker--Planck solution on the parametrized control. It is natural when the composed coefficients $(t,x,\theta)\mapsto(b,a)(t,x,u_{\theta}(t))$ are sufficiently smooth in $(t,x,\theta)$. A full proof of this parameter-regularity property is beyond the scope of this paper; related parabolic regularity results can be found in Lunardi and Friedman.

<!-- chunk {"id": "body-0065", "role": "body", "section": "Remark 18 (Regularity of the density flow)", "weight": 1.0} -->

We obtain the following Sobolev-specialized rate.

<!-- chunk {"id": "body-0066", "role": "body", "section": "Remark 20 (Statistical optimality)", "weight": 1.0} -->

When $N$ is large, Corollary 19 ‣ 4.5 Application to Sobolev Spaces ‣ 4 Learning Guarantees ‣ Learning Controlled Stochastic Differential Equations") gives, up to logarithmic factors, the control-sampling rate Here $\nu$ is the Sobolev regularity of the induced Fokker--Planck regression problem. Obtaining this effective regularity requires stronger upstream smoothness: regularity $2\nu+2$ for the controls and density flow, and Sobolev order $\tau>2\nu+2+(n+d+1)/2$ for the coefficient hypothesis space. These requirements reflect the composition with the parametrized controls and the spatial derivatives in the Fokker--Planck operator.

<!-- chunk {"id": "body-0067", "role": "body", "section": "Remark 20 (Statistical optimality)", "weight": 1.0} -->

For comparison, minimax $L^{\infty}$ rates for noiseless regression of $\nu$-smooth functions on $d$-dimensional compact domains are of order. Thus, with $d=m\vee(n+1)$, our rate has the same dimension--regularity scaling but loses one power in the exponent of $\log K/\sqrt{K}$. The Sobolev specialization is only one way to instantiate the abstract source and embedding assumptions with explicit exponents. Studying other RKHS choices for the coefficients, such as Gaussian kernels, and the rates they imply, is left for future work.

<!-- chunk {"id": "body-0068", "role": "body", "section": "Remark 20 (Statistical optimality)", "weight": 1.0} -->

We also obtain the following sample-complexity consequence.

<!-- chunk {"id": "body-0069", "role": "body", "section": "Remark 22 (Computational scaling)", "weight": 1.0} -->

The Fokker--Planck matching step uses $KN$ regression points: $K$ sampled controls and $N$ state-time collocation points. The resulting kernel system costs $O((KN)^{3})$ time and $O((KN)^{2})$ memory. Taking $N=K$ and using $K=O(\eta^{-2})$ from Corollary 21 ‣ 4.5 Application to Sobolev Spaces ‣ 4 Learning Guarantees ‣ Learning Controlled Stochastic Differential Equations") gives cost $O(\eta^{-12})$, up to logarithmic factors. Kernel approximations, such as Nyström methods and random features, can substantially reduce this cost while preserving statistical rates under suitable regularity assumptions, and have scaled kernel methods to datasets with billions of samples. Extending the present analysis to such approximations is left for future work.

<!-- chunk {"id": "body-0070", "role": "body", "section": "Remark 23 (Dependence on $M$ and $Q$)", "weight": 1.0} -->

The results above focus on the number $K$ of sampled controls and on the Fokker--Planck matching step. They assume that the first-stage density estimators $\hat{p}_{k}$ are sufficiently accurate, and therefore do not give a full statistical or computational analysis in terms of the number $Q$ of trajectories per control and the number $M$ of observation times. Finite-sample guarantees for density estimation are studied in Bonalli and Rudi for the error measure $\varepsilon$. Extending these bounds to the stronger uniform error $\varepsilon_{\infty}$ required by the $L^{\infty}$-in-control results would require additional uniform-in-time and uniform-in-space control, for instance through Sobolev embedding arguments. Here we focus on control sampling and Fokker--Planck matching, the main new elements of the controlled setting and, in our experiments, the main computational cost; see Section 5.

<!-- chunk {"id": "body-0071", "role": "body", "section": "Remark 24 (State-dependent controls)", "weight": 1.0} -->

For clarity, we focus on deterministic open-loop controls $u_{\theta}(t)$. An important extension is to allow state-dependent controls $u_{\theta}(t,x)$, as in feedback or closed-loop settings. Then the Fokker--Planck operator is evaluated along $u_{\theta}(t,x)$, and the induced feature map contains additional chain-rule terms involving spatial derivatives of the control. Establishing the corresponding guarantees would require additional control regularity assumptions and careful tracking of constants. We leave this extension to future work.

<!-- chunk {"id": "body-0072", "role": "body", "section": "Numerical Experiments", "weight": 1.0} -->

We present numerical experiments for uncontrolled SDE estimation (Section 5.1) and controlled SDE estimation (Section 5.2). The goal is to illustrate the main behavior of the proposed method.

<!-- chunk {"id": "body-0073", "role": "body", "section": "Purpose of uncontrolled SDE experiments", "weight": 1.0} -->

We begin our numerical study by implementing and evaluating the method proposed in Bonalli and Rudi for uncontrolled SDE estimation. The method of Bonalli and Rudi corresponds to our approach in the limiting case where the control space is reduced to a singleton $\mathcal{H}=\{u\}$. This study therefore provides useful insight before moving to the controlled SDE setting of Section 5.2.

<!-- chunk {"id": "body-0074", "role": "body", "section": "Python open-source library", "weight": 1.0} -->

Our implementation is available as an open-source Python library at [lmotte/sde-learn](2411.01982v2/lmotte/sde-learn). The library includes documentation and example scripts with light computational demands. In particular, it supports the Nyström approximation, which helps reduce the computational cost of Fokker--Planck matching. Further details, including derivations of the formulas used to implement the estimator and the computational complexity of each step, are given in Appendix B.

<!-- chunk {"id": "body-0075", "role": "body", "section": "Experimental setup", "weight": 1.0} -->

We consider an isotropic diffusion and use the pointwise positivity constraint described in Section 3 for the diffusion coefficient. All kernels are Gaussian kernels $k(x,y)=\exp(-\gamma\|x-y\|^{2})$ with different parameters $\gamma>0$. We select all hyperparameters by grid search on validation sets.

<!-- chunk {"id": "body-0076", "role": "body", "section": "Computational considerations", "weight": 1.0} -->

While the computational complexity of each step is given in Appendix B, we also report observed execution times to give a practical sense of scale. These experiments were run on a machine equipped with an Apple M3 Pro processor and 18 GB of RAM. For the 1D case, the probability density estimation step takes 0.015 seconds for training with 1000 sample paths and 100 time steps, and 0.11 seconds for prediction over a Fokker--Planck training set of size 2500. The Fokker--Planck matching step takes 6.0 seconds for training with 2500 data points and 3.7 seconds to generate 100 sample paths with 100 time steps. For the two 2D problems, probability density estimation training takes around 0.012 seconds for 3000 sample paths and 100 time steps, with prediction taking approximately 60 seconds over a Fokker--Planck training set of size 3000. The Fokker--Planck matching step takes about 10 seconds for training and 6 seconds to generate 100 sample paths with 100 time steps. These timings suggest that the method is computationally feasible for the moderate-size uncontrolled problems considered here.

<!-- chunk {"id": "body-0077", "role": "body", "section": "Ornstein--Uhlenbeck process", "weight": 1.0} -->

The Ornstein--Uhlenbeck (OU) process is a simple mean-reverting stochastic process. It is useful, for example, for modeling phenomena such as price volatility. It is defined by the SDE where $\mu$ is the mean to which the process reverts, $\theta$ is the mean-reversion coefficient, and $\sigma$ is the noise amplitude. The probability density of the OU process can be obtained explicitly from the Fokker--Planck equation. In particular, if $X$ is Gaussian with mean $\mu_{0}\in\mathbb{R}$ and covariance $\sigma_{0}^{2}>0$, then $X(t)$ remains Gaussian, with mean and covariance

<!-- chunk {"id": "body-0078", "role": "body", "section": "Datasets", "weight": 1.0} -->

We consider an Ornstein--Uhlenbeck process with constant variance and mean increasing from $0.5$ toward $2.5$ over $t\in$. Specifically, we set $\mu=2.5,\theta=0.5,\sigma^{2}=\theta/4,\mu_{0}=0.5,\sigma_{0}^{2}=\sigma^{2}/(2\theta)$, and $T=10$. In Figure 3, we plot 100 sample paths generated from this OU process. For the probability density estimation steps, we draw training and validation sets with $Q/Q_{val}=1000/100$ sample paths and $M/M_{val}=100/100$ time steps, respectively.

<!-- chunk {"id": "body-0079", "role": "body", "section": "Datasets", "weight": 1.0} -->

For the Fokker--Planck matching step, we draw a training set $(t_{i},x_{i})_{i=1}^{N}=\{t_{i}\}_{i=1}^{50}\times\{x_{i}\}_{i=1}^{50}$ by drawing times and positions uniformly within well-chosen intervals, and we draw a validation set with the same size and distribution.

<!-- chunk {"id": "body-0080", "role": "body", "section": "Step 1 (probability density estimation)", "weight": 1.0} -->

In Figure 1. ‣ 5.1.1 Linear Scalar SDE ‣ 5.1 Uncontrolled SDE Estimation ‣ 5 Numerical Experiments ‣ Learning Controlled Stochastic Differential Equations"), we plot the true and estimated probability densities, $p(t,x)$ and $\hat{p}(t,x)$, respectively. These densities are plotted on a uniformly spaced temporal grid, offset by $1/2$ unit from the training time discretization, and on a spatial grid with positions drawn uniformly within an interval. The estimated density gives a good visual approximation of the true dynamics.

<!-- chunk {"id": "body-0081", "role": "body", "section": "Step 2 (coefficient estimation via FP matching)", "weight": 1.0} -->

In Figure 2. ‣ 5.1.1 Linear Scalar SDE ‣ 5.1 Uncontrolled SDE Estimation ‣ 5 Numerical Experiments ‣ Learning Controlled Stochastic Differential Equations"), we plot the estimated coefficients obtained by FP matching. These coefficients differ significantly from the true coefficients. As discussed in Remark 1 ‣ Learning problem. ‣ 2 Problem Setting ‣ Learning Controlled Stochastic Differential Equations"), measuring accuracy through the $L^{2}$ distance to the true coefficients is not appropriate because the coefficients are not identifiable from densities alone. Our guarantees do not ensure recovery of the true coefficients; they ensure that the estimated coefficients reproduce the true dynamics at the distributional level. Specifically, they aim for the induced distribution $p_{\hat{b},\hat{a}}$ to be close to the true distribution $p_{b,a}$ in $L^{2}$.

<!-- chunk {"id": "body-0082", "role": "body", "section": "Recovering the true dynamics", "weight": 1.0} -->

We draw and plot 100 sample paths from the true and estimated coefficients in Figure 3 to assess recovery of the true dynamics. The estimated coefficients lead to visually comparable probability distributions, with close means and variances over time. Interestingly, while the distributions are similar, individual paths can look quite different.

<!-- chunk {"id": "body-0083", "role": "body", "section": "Nonlinear Multivariate SDE", "weight": 1.0} -->

For nonlinear multivariate SDE experiments, we consider two examples: a Dubins process and a finite exponential sum process.

<!-- chunk {"id": "body-0084", "role": "body", "section": "Dubins process", "weight": 1.0} -->

The Dubins process is defined by the SDE with $u(t)=\theta\sin(\frac{\pi t}{10})$, $v,\theta\in\mathbb{R}$, and $\sigma>0$.

<!-- chunk {"id": "body-0085", "role": "body", "section": "Finite exponential sum (FES) process", "weight": 1.0} -->

True SDE samples. Estimated SDE samples. Figure 5: FES process. 100 sample paths from the true and estimated SDEs.

<!-- chunk {"id": "body-0086", "role": "body", "section": "Datasets", "weight": 1.0} -->

For the Dubins process, we set $T=10$, $n=2$, $M=100$, $Q=3000$, $v=2$, $\theta=3$, and $\sigma=0.3$. For the probability density estimation steps, the training and validation sets consist of $Q/Q_{val}=3000/100$ sample paths and $M/M_{val}=100/10$ time steps, respectively. For the Fokker--Planck matching step, training and validation sets are drawn by sampling time-position pairs from the training sample paths, with sizes $N=3000$ and $N_{val}=1000$.

<!-- chunk {"id": "body-0087", "role": "body", "section": "Datasets", "weight": 1.0} -->

For the finite exponential sum process, the parameters are $T=3$, $n=2$, $M=100$, $Q=3000$, $n_{b}=n_{\sigma}=3$, $\gamma=1$, and $(t_{1},x_{1})=(0,)$, $(t_{2},x_{2})=(1,)$, and $(t_{3},x_{3})=(3,)$. For the probability density estimation steps, the training and validation sets consist of $Q/Q_{val}=3000/100$ sample paths and $M/M_{val}=100/100$ time steps, respectively. For the Fokker--Planck matching step, we use a training set $\{t_{i}\}_{i=1}^{30}\times\{x_{i}\}_{i=1}^{100}$, where the sets of times and positions are drawn uniformly in a well-chosen interval and two-dimensional box, respectively.

<!-- chunk {"id": "body-0088", "role": "body", "section": "Datasets", "weight": 1.0} -->

We use a validation set $\{t_{i}\}_{i=1}^{10}\times\{x_{i}\}_{i=1}^{100}$, where times and positions form uniform grids in a well-chosen interval and two-dimensional box. For both processes, the initial condition is $X\sim\mathcal{N}(0,1/4I_{\mathbb{R}^{2}})$.

<!-- chunk {"id": "body-0089", "role": "body", "section": "Recovering the true dynamics", "weight": 1.0} -->

We perform density estimation and Fokker--Planck (FP) matching for both processes, selecting hyperparameters on the validation sets as above. We draw and plot 100 sample paths from both the true and estimated coefficients in Figure 4 and Figure 5 process. ‣ 5.1.2 Nonlinear Multivariate SDE ‣ 5.1 Uncontrolled SDE Estimation ‣ 5 Numerical Experiments ‣ Learning Controlled Stochastic Differential Equations"). The estimated coefficients lead to probability distributions that are visually close to those of the true dynamics, with closely matching means and variances over time.

<!-- chunk {"id": "body-0090", "role": "body", "section": "Observations", "weight": 1.0} -->

Our experiments highlight two difficulties in estimating SDEs.

<!-- chunk {"id": "body-0091", "role": "body", "section": "Observations", "weight": 1.0} -->

Cumulative error. After the coefficients are estimated, the learned SDE is simulated by free rollout, without teacher forcing, i.e., without being reset or corrected using samples from the true process at intermediate times. Therefore, local errors in the estimated coefficients can accumulate over time. Even if the coefficients are accurate near a given time $t_{0}$, earlier errors on $0\leq t<t_{0}$ may already have changed the distribution of the learned process at time $t_{0}$.

<!-- chunk {"id": "body-0092", "role": "body", "section": "Observations", "weight": 1.0} -->

Error amplification. The learned process may enter regions of the time--state space where the training density is low and the coefficients are weakly constrained by data. In such regions, coefficient errors can be amplified, sometimes leading to path divergence or numerical termination. Increasing the variance of $X$ can improve coverage of the state space and reduce this instability.

<!-- chunk {"id": "body-0093", "role": "body", "section": "Python open-source library", "weight": 1.0} -->

Our implementation is available as an open-source Python library at [lmotte/controlled-sde-learn](2411.01982v2/lmotte/controlled-sde-learn). The library includes documentation and example scripts with light computational demands. More details are given in Appendix C, including derivations of the formulas used to implement the estimator.

<!-- chunk {"id": "body-0094", "role": "body", "section": "Experimental setup", "weight": 1.0} -->

We consider an isotropic diffusion and use the pointwise positivity constraint described in Remark 4 ‣ Hypothesis space. ‣ 3.2 Proposed Estimator ‣ 3 Proposed Method ‣ Learning Controlled Stochastic Differential Equations"). All kernels are Gaussian kernels $k(x,y)=\exp(-\gamma\|x-y\|^{2})$ with different parameters $\gamma>0$. For the 1D SDE, we select all hyperparameters by grid search on validation sets.

<!-- chunk {"id": "body-0095", "role": "body", "section": "Experimental setup", "weight": 1.0} -->

For the 2D SDE, to avoid excessive computation, we fix the hyperparameters for both probability density estimation and Fokker--Planck matching using those previously selected for the uncontrolled Dubins process in Section 5.1.2. Further details can be found in the code repository.

<!-- chunk {"id": "body-0096", "role": "body", "section": "Computational considerations", "weight": 1.0} -->

While the computational complexity of each step is given in Appendix C, we also report observed execution times to give a practical sense of scale. The experiments were run on a machine equipped with an Apple M3 Pro processor and 18 GB of RAM. For the 1D case, the probability density estimation step takes 5.6 seconds for training with 1000 sample paths, 100 time steps, and 10 training controls, and 1.0 seconds for prediction over a Fokker--Planck training set of size 10000. The Fokker--Planck matching step takes 190 seconds for training with 10000 data points and 150 seconds to generate 100 sample paths with 100 time steps for 10 different controls. For the 2D problem, probability density estimation training takes around 0.032 seconds for 3000 sample paths, 100 time steps, and 20 training controls, with prediction taking approximately 160 seconds over a Fokker--Planck training set of size 10000. The Fokker--Planck matching step takes about 490 seconds for training and 140 seconds to generate 100 sample paths with 100 time steps for 5 different controls. These timings show that controlled SDE estimation is substantially more demanding than the uncontrolled case, but remains feasible at the moderate scales considered here.

<!-- chunk {"id": "body-0097", "role": "body", "section": "Computational considerations", "weight": 1.0} -->

As expected, the cost increases with the number of training controls.

<!-- chunk {"id": "body-0098", "role": "body", "section": "Linear Scalar SDE", "weight": 1.0} -->

We first consider controlled Ornstein--Uhlenbeck processes.

<!-- chunk {"id": "body-0099", "role": "body", "section": "Controlled Ornstein--Uhlenbeck process", "weight": 1.0} -->

Let $X(t)$ be an Ornstein--Uhlenbeck process with controlled mean, defined by the SDE where $\theta\in\mathbb{R}$, $\sigma\in\mathbb{R}_{+}$, and $u\in\mathcal{H},u:[0,T]\to\mathbb{R}$. For simplicity, we take $\mathcal{H}$ to be the class of two-step control functions from $[0,T]$ to $\mathbb{R}$, namely In the experiments, the control parameter belongs to with parameter $(u_{0},u_{1},t_{1})$, and the three components are sampled independently and uniformly over their respective intervals. These controls fall outside Assumption A2 ‣ 3.1 Well-Posedness and Fokker–Planck Matching Inequality ‣ 3 Proposed Method ‣ Learning Controlled Stochastic Differential Equations"), but they provide a simple numerical illustration.

<!-- chunk {"id": "body-0100", "role": "body", "section": "Datasets", "weight": 1.0} -->

We consider a controlled OU process and set $\theta=0.5,\sigma^{2}=\theta/4,\mu_{0}=0.5,\sigma_{0}^{2}=\sigma^{2}/(2\theta)$, $T=10$, and $X\sim\mathcal{N}(\mu_{0},\sigma_{0}^{2})$. In Figure 7, we plot 100 sample paths generated from this OU process for three different controls. We draw a dataset of $K=10$ controls, shown in Figure 6, by sampling $(u_{0},u_{1},t_{1})$ independently according to the distribution defined above. For the probability density estimation steps, we draw training and validation sets with $Q/Q_{val}=1000/100$ sample paths and $M/M_{val}=100/100$ time steps, respectively.

<!-- chunk {"id": "body-0101", "role": "body", "section": "Datasets", "weight": 1.0} -->

For the Fokker--Planck matching step, we draw a training set $(t_{i},x_{i})_{i=1}^{N}=\{t_{i}\}_{i=1}^{20}\times\{x_{i}\}_{i=1}^{50}$ by drawing times and positions uniformly within well-chosen intervals, and we draw a validation set with the same size and distribution.

<!-- chunk {"id": "body-0102", "role": "body", "section": "Recovering the true controlled dynamics", "weight": 1.0} -->

For $K_{te}=3$ randomly drawn controls, we generate and plot 100 sample paths using both the true and estimated coefficients; see Figure 7. The estimated coefficients produce probability distributions that are visually close to the true ones, with matching means and variances over time. The three controls used for evaluation are not part of the training data.

<!-- chunk {"id": "body-0103", "role": "body", "section": "Nonlinear Multivariate SDE", "weight": 1.0} -->

We next consider controlled Dubins processes.

<!-- chunk {"id": "body-0104", "role": "body", "section": "Controlled Dubins process", "weight": 1.0} -->

Let $X(t)$ be a Dubins process with controlled angle, defined by the SDE where $v\in\mathbb{R}$, $\sigma>0$, and $u\in\mathcal{H}$, where $u:[0,T]\to\mathbb{R}$. We consider the parametrized control family Figure 8: Training set of 20 i.i.d. controls.

<!-- chunk {"id": "body-0105", "role": "body", "section": "Datasets", "weight": 1.0} -->

We consider a controlled Dubins process and set $v=2$, $\sigma=0.3$, $\mu_{0}=0$, $\sigma_{0}=0.5$, $T=10$, and $X\sim\mathcal{N}(\mu_{0},\sigma_{0}^{2}I_{\mathbb{R}^{2}})$. In Figure 9, we plot 100 sample paths generated from this process for five different controls. We build a dataset of $K=20$ controls, shown in Figure 8 (with amplitudes scaled by a factor of $10$), by drawing the amplitudes independently according to $\theta_{k}\sim\operatorname{Unif}(\Theta)$. For the probability density estimation steps, we generate a training set with $Q=3000$ sample paths and $M=100$ time steps.

<!-- chunk {"id": "body-0106", "role": "body", "section": "Datasets", "weight": 1.0} -->

For the Fokker--Planck matching step, we draw a training set $(\theta_{k},t_{i},x_{i})_{k\in\llbracket 1,20\rrbracket,i\in\llbracket 1,500\rrbracket}$ of size $10^{4}$. To avoid sampling regions where $p(\theta_{k},t,x)$ is negligible, for each $\theta_{k}$, we draw 500 pairs $(t_{i},x_{i})_{i=1}^{500}$ from 5 sample paths with 100 time steps, generated with the same parameters as the controlled Dubins process but with initial variance $\sigma_{0}=2.5$.

<!-- chunk {"id": "body-0107", "role": "body", "section": "Recovering the true controlled dynamics", "weight": 1.0} -->

For evaluation, we consider $K_{\mathrm{te}}=5$ held-out controls with amplitudes $\theta=-1,-1/2,0,1/2,1$. These amplitudes lie in the interior of the training range $[-1.2,1.2]$. We generate and plot 100 sample paths using both the true and estimated coefficients; see Figure 9. The estimated coefficients yield probability distributions that are visually close to the true ones, with similar means and variances over time.

<!-- chunk {"id": "body-0108", "role": "body", "section": "Conclusion", "weight": 1.5} -->

We studied the problem of learning multidimensional controlled SDEs whose drift and diffusion may depend nonlinearly on time, state, and control, from trajectory data collected under several controls. The proposed method follows a two-step strategy: it first estimates the state-density evolution associated with each observed control, and then learns drift and diffusion coefficients by least-squares Fokker--Planck matching.

<!-- chunk {"id": "body-0109", "role": "body", "section": "Conclusion", "weight": 1.5} -->

The main contribution is a finite-sample analysis of the density flows induced by the learned coefficients. The resulting bounds show how the error decreases with the number of sampled controls, and how this rate depends on the dimension and regularity of the control parametrization. Beyond average-case accuracy, we also obtain guarantees that hold uniformly over controls, together with CVaR-type bounds for tail-sensitive quantities under the learned dynamics.

<!-- chunk {"id": "body-0110", "role": "body", "section": "Conclusion", "weight": 1.5} -->

Several limitations should be kept in mind. The results are stated at the level of density-flow reconstruction, which is the natural object controlled by the Fokker--Planck equation, but does not in general imply identification of a unique drift--diffusion pair: distinct coefficients may induce the same laws. The setting is also passive and open-loop: the controls are observed inputs sampled from a fixed finite-dimensional family, rather than actions chosen adaptively by the learner. Finally, the analysis relies on smoothness, ellipticity, localization, and first-stage density-estimation assumptions, which make the finite-sample guarantees explicit but also delimit the regime covered by the theory.

<!-- chunk {"id": "body-0111", "role": "body", "section": "Conclusion", "weight": 1.5} -->

These limitations point to several directions for future work. A complete end-to-end analysis should track the density-estimation step more explicitly, including the number of trajectories per control and the time discretization. Beyond the Sobolev instantiation considered here, it would be interesting to verify the general source and embedding conditions for other kernels and structural assumptions, such as finite-dimensional, sparse, or low-rank representations, which may yield different dimension dependence and improved statistical guarantees. For larger problems, the kernel least-squares structure of the Fokker--Planck matching step makes Nyström methods, random features, sketching, stochastic optimization, and iterative solvers natural scaling tools. Further extensions include feedback controls, adaptive or safe exploration of the control space, weaker localization assumptions, and tests on real-world systems such as autonomous driving or space rendezvous.

<!-- chunk {"id": "body-0112", "role": "body", "section": "Conclusion", "weight": 1.5} -->

Acknowledgments and Disclosure of Funding This work was carried out while L.B.M. was a postdoctoral researcher at Laboratoire des Signaux et Systèmes, Université Paris-Saclay, CentraleSupélec. The Agence Nationale de la Recherche (grant ANR-22--0006, PI: R.B.) provided funds to support this research. A.R. acknowledges support from the European Research Council (grant REAL 947908).
