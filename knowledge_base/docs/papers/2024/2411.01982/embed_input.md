<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Learning Controlled Stochastic Differential Equations

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Identification of nonlinear dynamical systems is crucial across various fields, facilitating tasks such as control, prediction, optimization, and fault detection. Many applications require methods capable of handling complex systems while providing strong learning guarantees for safe and reliable performance. However, existing approaches often focus on simplified scenarios, such as deterministic models, known diffusion, discrete systems, one-dimensional dynamics, or systems constrained by strong structural assumptions such as linearity. This work proposes a novel method for estimating both drift and diffusion coefficients of continuous, multidimensional, nonlinear controlled stochastic differential equations with non-uniform diffusion. We assume regularity of the coefficients within a Sobolev space, allowing for broad applicability to various dynamical systems in robotics, finance, climate modeling, and biology. Leveraging the Fokker-Planck equation, we split the estimation into two tasks: (a) estimating system dynamics for a finite set of controls, and (b) estimating coefficients that govern those dynamics.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

We provide strong theoretical guarantees, including finite-sample bounds for \(L^2\), \(L^\infty\), and risk metrics, with learning rates adaptive to coefficients' regularity, similar to those in nonparametric least-squares regression literature. The practical effectiveness of our approach is demonstrated through extensive numerical experiments. Our method is available as an open-source Python library.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

Modeling complex dynamical systems is pivotal across various fields, enabling tasks such as analysis, prediction, simulation, control, optimization, and fault detection. Deriving models from first principles---such as physical, electrical, mechanical, chemical, biological, or economic laws---requires extensive knowledge, which is often lacking in practice. In response, the literature has seen the emergence of data-driven modeling approaches since at least the 1970s, utilizing input-output data sets to identify the most suitable model within a hypothesis set of possible models.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

Stochastic differential equations (SDEs) are a general mathematical tool for modeling dynamical systems subject to random fluctuations. Let $X{(t)}$ be a controlled $n$-dimensional stochastic process whose dynamics are governed by the controlled SDE

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

We consider the problem of estimating a controlled SDE from a data set of sample paths generated under various controls from $\mathcal{H}$. Namely, our goal is to estimate $(b,\sigma^{2})$ from a data set

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

where $X_{u_{k}}$ denotes the solution of Eq. under the control $u_{k}:{{\lbrack 0,T\rbrack}\mapsto{\mathbb{R}}^{d}}$. By treating controls as inputs and sample paths as outputs, we frame system identification as a supervised learning problem.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Introduction", "weight": 1.5} -->

While controlled SDEs cover a wide range of scenarios, estimating them poses significant statistical and computational challenges. Consequently, the existing literature on dynamical systems (see Section 1.1) imposes various limitations to develop practical methods. These include deterministic assumptions (e.g., using ordinary differential equations, omitting diffusion), discrete assumptions (e.g., using difference equations), dimensional assumptions (e.g., one-dimensional systems), and structural assumptions on the coefficients (e.g., linearity or parametric models).

<!-- chunk {"id": "body-0009", "role": "body", "section": "Contributions", "weight": 1.0} -->

This paper introduces a novel method addressing the controlled SDE estimation problem in its most general setting while enjoying strong theoretical guarantees. Our approach builds on recent advances in SDE estimation and kernel representation. More precisely, we establish finite-sample learning bounds for our method, featuring statistical rates that are adaptive to standard regularity assumptions on the learning problem. Specifically, we prove $L^{2}$ learning rates between the probability density of the true SDE and that of the estimated coefficients, offering guarantees in expectation over controls, times, and positions. We then derive $L^{\infty}$ learning rates, ensuring accuracy almost surely over times and controls---particularly relevant for optimal control. From these $L^{\infty}$ rates, we establish CVaR learning rates, ensuring accuracy in tail estimation, crucial for risk-averse applications, such as risk-averse optimal control. For clarity of exposition, we focus on deterministic controls throughout the paper, with extensions to stochastic controls presented in a dedicated result.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Contributions", "weight": 1.0} -->

Furthermore, we provide implementations and experimental evaluations of the method proposed for estimating uncontrolled SDEs ---as an insightful limit case of our approach where the control space reduces to a singleton--- as well as of our method for controlled SDEs. Both implementations are available as open-source Python libraries on the GitHub repositories lmotte/sde-learn and lmotte/controlled-sde-learn. Experimental results underscore the statistical and computational performance of the methods.

<!-- chunk {"id": "body-0011", "role": "body", "section": "System identification", "weight": 1.0} -->

The foundation of system identification theory was established in the 1960s by and further strengthened in the 1990s by works such as. A wide variety of methods for identifying dynamical systems exists. These methods are generally categorized based on three key aspects: the model, the fitting method (which includes fitting criteria and optimization techniques), and---distinctly from standard supervised learning---the strategy for selecting inputs, referred to as experiment design. Given the extensive literature on system identification, we provide only a brief overview of the most prevalent methods in the field as they relate to our work and refer the reader to for detailed presentations of these methods.

<!-- chunk {"id": "body-0012", "role": "body", "section": "System identification", "weight": 1.0} -->

(Models). Dynamical systems modeling can be characterized by how states and controls interact over time (see, e.g., state-space, ARX, ARMAX models) and the form of these interactions. Common models include linear, polynomial, lookup tables, neural network (e.g., RNN, LSTM, CNN ), and fuzzy models. Nonlinear modeling, while more involved, addressess a broader spectrum of engineering challenges by enabling capturing more complex dynamics. More recently, models based on the Koopman operator have emerged.

<!-- chunk {"id": "body-0013", "role": "body", "section": "System identification", "weight": 1.0} -->

(Fitting methods). Models are typically fitted by optimizing a criterion that matches the outputs of the true and estimated systems across a selected set of inputs. Common methods include least-squares, Bayesian, and maximum likelihood estimations. For models that are linear in their parameters, optimization is often solved with closed-form solutions. For models that are nonlinear in their parameters, iterative optimization is commonly used.

<!-- chunk {"id": "body-0014", "role": "body", "section": "System identification", "weight": 1.0} -->

(Experiment design). Selecting inputs that generate the most informative data for accurate model estimation poses a significant challenge. Typically, this involves obtaining data sets that allow discrimination between any two functions within the hypothesis set. This leads for instance to concepts such as persistence of excitation, and maximization of Fisher information, as discussed in the literature. Besides traditional experiment design strategies, there is a growing interest in using reinforcement learning and active learning techniques to dynamically select inputs in ways that maximize information gain for model identification.

<!-- chunk {"id": "body-0015", "role": "body", "section": "System identification", "weight": 1.0} -->

Regarding learning guarantees, substantial research exists on the identification of linear dynamical systems. In contrast, the identification of nonlinear dynamical systems has received much less attention, and sample complexity in nonlinear system identification remains largely underexplored. Several studies, such as Oymak, Bahmani and Romberg, Foster et al., Sattar and Oymak, investigate generalized linear dynamical systems of the form $x_{t + 1} = {\phi{({{Ax_{t}} + {Bu_{t}}})}}$, where $\phi$ is a specified function. Mania et al. analyze a parametric model defined as $x_{t + 1} = {{A\phi{(x_{t},u_{t})}} + w_{t}}$. Their approach, however, is constrained by several assumptions, including a "warm start" (an informed initial model guess), the availability of a computational oracle bypassing trajectory planning intractability, and controllability (the ability to drive the system from any state to a target-aligned feature vector).

<!-- chunk {"id": "body-0016", "role": "body", "section": "System identification", "weight": 1.0} -->

While these results contribute valuable insights, they also highlight the necessity for a statistical theory designed specifically for nonparametric models, as developed in this work.

<!-- chunk {"id": "body-0017", "role": "body", "section": "Online learning in system identification", "weight": 1.0} -->

Online learning refers to methods in which models are incrementally updated as new data becomes available, rather than being trained once on a static dataset. There is a substantial literature on online learning methods for system identification. These methods primarily focus on refining pre-existing nominal models, typically learned offline, by leveraging data gathered during system operation. The goal is to improve control performance by addressing uncertainties and adapting to environmental changes, rather than learning the system dynamics entirely from scratch. This is particularly important in many practical systems where the dynamics are only partially known, with time-varying or uncertain parameters (e.g., payloads or environmental conditions), necessitating adaptive methods that can handle these evolving conditions. A key assumption in these approaches is that the nominal model provides a reasonable approximation of the true system, ensuring safe data collection and refinement. In contrast, this work focuses on offline data collection and learning the system's dynamics from the ground up.

<!-- chunk {"id": "body-0018", "role": "body", "section": "Uncontrolled SDE estimation", "weight": 1.0} -->

The literature on learning SDE coefficients primarily focuses on autonomous systems, which operate independently of any control inputs. There is a broad range of methods for learning SDE coefficients. In terms of learning guarantees, most literature has focused on deriving guarantees for coefficient estimation by observing a single process up to time $T$ at discrete intervals of size $\Delta$, and then studying convergence rates as $T\rightarrow{+ \infty}$ and $\Delta\rightarrow 0$ under ergodicity assumptions. Such settings do not align with our needs in the control setting, where short time horizons are critical. Specifically, we aim to obtain arbitrarily accurate coefficients within a fixed time horizon as the number of observations increases. More recent studies consider the i.i.d. setting, where data consists of i.i.d. sample paths with fixed horizons. Comte and Genon-Catalot considers continuous observation of a one-dimensional process and provides risk bounds that hold in expectation. Bonalli and Rudi, Nüske et al., Zhang and Zuazua addresses a more realistic setting involving $n$-dimensional processes and discrete sampling observations, providing finite-sample bounds.

<!-- chunk {"id": "body-0019", "role": "body", "section": "Controlled SDE estimation", "weight": 1.0} -->

Despite the extensive literature on system identification and SDE estimation, to our knowledge, the study by Nüske et al. stands as the sole finite-data error analysis in the controlled setting. Their method is tailored for nonlinear control-affine SDEs, particularly under the structural assumption ${b{(t,x,{u_{\theta}{(t)}})}} = {{b_{0}{(x)}} + {B_{1}{(x)}\theta}}$, where $b_{0}:{{\mathbb{R}}^{n}\rightarrow{\mathbb{R}}^{n}}$, $B_{1}:{{\mathbb{R}}^{n}\rightarrow{\mathbb{R}}^{n \times m}}$ and the control space is parametrized by $\theta \in {\mathbb{R}}^{m}$ for $m \in {\mathbb{N}}^{\ast}$.

<!-- chunk {"id": "body-0020", "role": "body", "section": "Controlled SDE estimation", "weight": 1.0} -->

Additionally, they assume that the diffusion $\sigma$ does not depend on $u$ and $t$. Importantly, their methodology does not provide explicit estimates of the drift and diffusion coefficients. In contrast, our approach provides explicit coefficient estimates, relying only on regularity assumptions and offering learning rates adaptive to coefficient regularity.

<!-- chunk {"id": "body-0021", "role": "body", "section": "Paper organisation", "weight": 1.0} -->

The paper is organized as follows. In Section, we formulate the learning problem addressed in this work. In Section, we introduce our controlled SDEs estimation method. In Section, we provide the learning guarantees for this method. In Section, we present numerical experiments.

<!-- chunk {"id": "body-0022", "role": "body", "section": "Paper notations", "weight": 1.0} -->

Let ${q,r,s,d,n} \in {\mathbb{N}}_{+}$. Let $\mathcal{F}{(A,B)}$ denote the set of all functions from the set $A$ to the set $B$. Let $\mathcal{M}{(A,B)}$ denote the set of all measurable functions from the measurable space $(A,\mathcal{A})$ to $(B,\mathcal{B})$, where $\mathcal{A}$ and $\mathcal{B}$ are the Borel $\sigma$-algebras on $A$ and $B$, respectively. Let $W^{q}{(A,B)}$ denote the Sobolev Hilbert space from $A$ to $B$ whose weak derivatives are defined up to order $q$.

<!-- chunk {"id": "body-0023", "role": "body", "section": "Paper notations", "weight": 1.0} -->

In this work, $A$ is either ${\mathbb{R}}^{r}$ or the cylindrical domain ${\lbrack 0,T\rbrack} \times {\mathbb{R}}^{r}$, and $B = {\mathbb{R}}^{s}$, ensuring well-definition. We denote the Loewner partial ordering by $\preceq$, such that for any two bounded linear operators $A$ and $B$, $A \preceq B$ if and only if $B - A$ is positive. For any vectors $u,v$, $u \otimes v$ denotes the tensor product.

<!-- chunk {"id": "body-0024", "role": "body", "section": "Paper notations", "weight": 1.0} -->

Let $\mathcal{H} \subset {\mathcal{F}{({\lbrack 0,T\rbrack},{\mathbb{R}}^{d})}}$ denotes the space of possible controls, then for any sets $A,C$, $u \in \mathcal{H}$, and $f:{{\mathcal{H} \times A}\rightarrow C}$, we denote $f{(u)} \triangleq f{(u{( \cdot )}, \cdot )})$. We denote ${a \land b} \triangleq {\min{(a,b)}}$, and ${a \vee b} \triangleq {\max{(a,b)}}$. Throughout this work, $p_{c}$ denotes a probability measure on the control space $\mathcal{H}$. The following mixed norms are used

<!-- chunk {"id": "body-0025", "role": "body", "section": "Paper notations", "weight": 1.0} -->

where ${{ess}\sup}_{u \sim p_{c}}$ denotes the essential supremum taken $p_{c}$-almost surely over $\mathcal{H}$, ignoring sets of $p_{c}$-measure zero.

<!-- chunk {"id": "body-0026", "role": "body", "section": "Problem setting", "weight": 1.0} -->

In this section, we introduce and discuss the learning problem addressed in this work.

<!-- chunk {"id": "body-0027", "role": "body", "section": "Controlled SDE identification", "weight": 1.0} -->

where $T > 0$ is a fixed time horizon, $W{(t)}$ is a standard Brownian motion, $p_{0}$ is a probability density over ${\mathbb{R}}^{n}$, $\mathcal{H} \subset {\mathcal{F}{({\lbrack 0,T\rbrack},{\mathbb{R}}^{d})}}$ is a set of possible controls, thanks to a data set of controlled sample paths

<!-- chunk {"id": "body-0028", "role": "body", "section": "Probability density associated with $(b,\\sigma^{2})$", "weight": 1.0} -->

such that $p_{b,\sigma}{(u,t,.)}$ represents the probability density of $X_{u}{(t)}$ governed by Eq..

<!-- chunk {"id": "body-0029", "role": "body", "section": "Learning problem", "weight": 1.0} -->

Given a hypothesis space $\mathcal{F} \subset {\mathcal{M}{({{\lbrack 0,T\rbrack} \times {\mathbb{R}}^{n} \times {\mathbb{R}}^{d}},{\mathbb{R}}^{n + n^{2}})}}$ for the SDE coefficients, the controlled SDE identification problem can be formulated as

<!-- chunk {"id": "body-0030", "role": "body", "section": "Learning problem", "weight": 1.0} -->

where $p \triangleq p_{b,\sigma}$ represents the probability density associated with the true controlled stochastic process.

<!-- chunk {"id": "body-0031", "role": "body", "section": "Learning problem", "weight": 1.0} -->

The learning problem defined by Eq. is both statistically and computationally challenging due to the complex mapping ${\hat{b},{\hat{\sigma}}^{2}}\mapsto p_{\hat{b},\hat{\sigma}}$. In Section, we overcome this challenge, following the approach of recent work by Bonalli and Rudi, by leveraging the Fokker-Planck equation to cast this non-convex learning objective into a convex least-squares objective. This transformation allows for efficient resolution, with strong learning guarantees, harnessing the well-established literature on least-squares.

<!-- chunk {"id": "body-0032", "role": "body", "section": "Experiment design", "weight": 1.0} -->

The choice of $(\mathcal{H},p_{c})$ will determine the controls over which the estimated SDE is accurate (see Theorem 4.1. ‣ 4.1 𝐿² learning rates ‣ 4 Learning guarantees ‣ Learning Controlled Stochastic Differential Equations")). Therefore, it should align with the intended usage of the estimated SDE, and depend on the specific application at hand. We leave this choice to users, based on their specific experimental context. Additionally, the choice of the initial distribution $p_{0}$ can also be considered part of the experiment design. Similar to the choice of $(\mathcal{H},p_{c})$, it will determine the initial positions over which the estimated controlled SDE is accurate (see Theorem 4.1. ‣ 4.1 𝐿² learning rates ‣ 4 Learning guarantees ‣ Learning Controlled Stochastic Differential Equations")). We refer the curious reader to the related work section for a brief review of existing experiment design methods.

<!-- chunk {"id": "body-0033", "role": "body", "section": "Remark 1 (Non-identifiability of SDE coefficients)", "weight": 1.0} -->

This stems from the fact that identifying the true coefficients $(b,\sigma^{2})$ solely from sample paths constitutes an ill-posed problem, as distinct SDE coefficients can result in identical probability distributions of the sample paths due to unexplored regions of ${\lbrack 0,T\rbrack} \times {\mathbb{R}}^{n}$. In contrast, recovering the probability density function ${t,x}\mapsto{p_{b,\sigma}{(t,x)}}$ from the sample paths is a well-posed problem. Then, from $p_{b,\sigma}$, one can identify coefficients $(\overset{\sim}{b},{\overset{\sim}{\sigma}}^{2})$ that, while potentially distinct from $(b,\sigma^{2})$, yield the same probability density, i.e., such that $p_{\overset{\sim}{b},\overset{\sim}{\sigma}} = p_{b,\sigma}$.

<!-- chunk {"id": "body-0034", "role": "body", "section": "Remark 1 (Non-identifiability of SDE coefficients)", "weight": 1.0} -->

See Example. ‣ Experiment design. ‣ 2 Problem setting ‣ Learning Controlled Stochastic Differential Equations") for a prototypical case where different SDE coefficients lead to the same probability density. Investigating the conditions under which the distribution $p_{b,\sigma}$ uniquely determines $(b,\sigma^{2})$ is an interesting and complex question, though it lies beyond the scope of this study. Finally, obtaining coefficients that accurately generate $p_{b,\sigma}$ is sufficient for many practical scenarios where the main goal is to accurately reproduce the true controlled dynamics. This justifies our learning problem proposed in Eq..

<!-- chunk {"id": "body-0035", "role": "body", "section": "Example 1 (Prototypical non-identifiable SDE coefficients)", "weight": 1.0} -->

We provide an example where different coefficients yield the same probability density. Here, a change in the diffusion coefficient is offset by a corresponding adjustment in the drift coefficient. Consider the (uncontrolled) Ornstein-Uhlenbeck process $X{(t)}$ governed by the SDE

<!-- chunk {"id": "body-0036", "role": "body", "section": "Example 1 (Prototypical non-identifiable SDE coefficients)", "weight": 1.0} -->

where $\theta > 0$, $\mu \in {\mathbb{R}}$, $\sigma > 0$, and $W{(t)}$ denotes standard Brownian motion. The process $X{(t)}$ follows a normal distribution, with its mean and variance evolving over time as

<!-- chunk {"id": "body-0037", "role": "body", "section": "Proposed method", "weight": 1.0} -->

In this section, we present our method for estimating controlled SDEs. We leverage the Fokker-Planck (FP) matching inequality to split the estimation into two more manageable problems: a) estimation of the dynamics for a finite set of controls, and b) estimation of coefficients that could govern these dynamics. Section 3.1 introduces the FP matching inequality, while Section 3.2 details the estimator leveraging the decomposition principle.

<!-- chunk {"id": "body-0038", "role": "body", "section": "Fokker-Planck matching inequality", "weight": 1.0} -->

We assume that the true SDE coefficients $(b,\sigma^{2})$, the initial probability density $p_{0}$, and the considered model $\mathcal{F}$ meet a minimal smoothness assumption, characterized by a sufficiently high order of Sobolev regularity, essential for the validity of both the Strong FP equation and the FP matching inequality.

<!-- chunk {"id": "body-0039", "role": "body", "section": "Assumption (A1) (Smooth SDE)", "weight": 1.0} -->

We assume a uniform ellipticity condition on $\sigma$, which is a standard requirement in SDE analysis to ensure that the diffusion coefficient $\sigma$ remains uniformly non-degenerate.

<!-- chunk {"id": "body-0040", "role": "body", "section": "Assumption (A2) (Uniform ellipticity)", "weight": 1.0} -->

Additionally, we assume the ability to sample from a probability density $p_{s}$ over ${\lbrack 0,T\rbrack} \times {\mathbb{R}}^{n}$ that covers the supports of the true coefficients and their derivatives.

<!-- chunk {"id": "body-0041", "role": "body", "section": "Assumption (A3) (Calibrated sampling)", "weight": 1.0} -->

There exists a probability density $p_{s}$ over ${\lbrack 0,T\rbrack} \times {\mathbb{R}}^{n}$, and $a > 0$, such that

<!-- chunk {"id": "body-0042", "role": "body", "section": "Assumption (A3) (Calibrated sampling)", "weight": 1.0} -->

Moreover, the bounded support of $p_{s}$ contains the support of $(b,\sigma^{2})$ and their derivatives. Namely,

<!-- chunk {"id": "body-0043", "role": "body", "section": "Assumption (A3) (Calibrated sampling)", "weight": 1.0} -->

with the same conditions applied to the derivatives of $(b,\sigma^{2})$.

<!-- chunk {"id": "body-0044", "role": "body", "section": "Assumption (A3) (Calibrated sampling)", "weight": 1.0} -->

Under these assumptions, we derive the two following key lemmas for our method.

<!-- chunk {"id": "body-0045", "role": "body", "section": "Controlled SDE estimator", "weight": 1.0} -->

Consider a data set of controlled sample paths

<!-- chunk {"id": "body-0046", "role": "body", "section": "Defining the hypothesis space $\\mathcal{F}$ for $(b,\\sigma^{2})$ with RKHSs", "weight": 1.0} -->

FP matching (Eq. )) constitutes a convex learning problem, specifically quadratic with respect to $(b,\sigma^{2})$. This stems from the linearity of the dual Kolmogorov generator with respect to $(b,\sigma^{2})$, which is a linear combination of the partial derivatives of $(b,\sigma^{2})$. Consequently, RKHSs are well-suited for solving FP matching. In particular, they meet the key properties of maintaining the convexity that facilitates empirical risk minimization (Eq. ) while being universal approximators, leading both to good computational and statistical performance. Their ability for closed-form differentiation also significantly facilitates the computation of the Kolmogorov generator.

<!-- chunk {"id": "body-0047", "role": "body", "section": "Uniformly elliptic diffusion $\\sigma^{2}$", "weight": 1.0} -->

Meaningful diffusion coefficient $\sigma^{2}$ should satisfy the uniform ellipticity condition of Assumption (A2) (Uniform ellipticity). ‣ 3.1 Fokker-Planck matching inequality ‣ 3 Proposed method ‣ Learning Controlled Stochastic Differential Equations"). This requirement can be efficiently addressed as follows.

<!-- chunk {"id": "body-0048", "role": "body", "section": "Uniformly elliptic diffusion $\\sigma^{2}$", "weight": 1.0} -->

For a detailed discussion on the advantages of various PSD models, refer to Marteau-Ferey et al., Muzellec et al..

<!-- chunk {"id": "body-0049", "role": "body", "section": "Learning guarantees", "weight": 1.0} -->

In Section 4.1, we provide $L^{2}$-in-time-control-and-position learning rates for the proposed method. In Section 4.2, we provide refined $L^{2}$ learning rates under refined regularity assumptions on the learning problem. In Section 4.3, we provide $L^{\infty}$-in-time-and-control, $L^{2}$-in-position learning rates. In Section 4.4, we provide CVaR learning rates. In Section 4.5, we illustrate our theoretical results by analyzing the special case of SDE coefficients in Sobolev spaces. In Section 4.6, we discuss the proposed method's adaptability to the regularity of the learning problem. Finally, in Section 4.7, we extend our approach to encompass a larger class of controls, expanding from deterministic to stochastic controls within closed-loop systems.

<!-- chunk {"id": "body-0050", "role": "body", "section": "$L^{2}$ learning rates", "weight": 1.0} -->

To establish finite-sample bounds for our estimator, it is necessary to impose regularity assumptions on the learning problem, as underpinned by the No-Free-Lunch Theorem.

<!-- chunk {"id": "body-0051", "role": "body", "section": "Assumption (A4) (Attainability assumption)", "weight": 1.0} -->

The true coefficients indeed belong to the chosen hypothesis space. Namely,

<!-- chunk {"id": "body-0052", "role": "body", "section": "Assumption (A4) (Attainability assumption)", "weight": 1.0} -->

This is a standard assumption in the literature of regularized least-squares regression. For concrete examples, refer to Section 4.5.

<!-- chunk {"id": "body-0053", "role": "body", "section": "Sketch of the proof", "weight": 1.0} -->

Error stemming from the finite sampling approximation of times $\lbrack 0,T\rbrack$ and positions ${\mathbb{R}}^{n}$,

<!-- chunk {"id": "body-0054", "role": "body", "section": "Sketch of the proof", "weight": 1.0} -->

Error stemming from the finite sampling approximation of the space of controls $\mathcal{H}$.

<!-- chunk {"id": "body-0055", "role": "body", "section": "Sketch of the proof", "weight": 1.0} -->

Each error component is then bounded by representing all quantities as norms of linear operators, followed by appropriate decomposition and the application of Bernstein inequalities for sums of operators. ∎

<!-- chunk {"id": "body-0056", "role": "body", "section": "Sketch of the proof", "weight": 1.0} -->

Theorem 4.1. ‣ 4.1 𝐿² learning rates ‣ 4 Learning guarantees ‣ Learning Controlled Stochastic Differential Equations") demonstrates that, with sufficiently accurate density estimation (small enough $\varepsilon$), the estimator for the coefficients of the controlled SDE achieves the standard learning rate of kernel ridge regression with respect to $K$ and $N$---without additional assumptions in the noiseless setting, where the output is unambiguous given the input.

<!-- chunk {"id": "body-0057", "role": "body", "section": "Remark 2 (Dependency in $K$ and $N$)", "weight": 1.0} -->

Note that despite utilizing $KN$ data points ${(u_{k},t_{i},x_{i})}_{{i \in {⟦1,N⟧}},{l \in {⟦1,K⟧}}}$ in $\mathcal{H} \times {\lbrack 0,T\rbrack} \times {\mathbb{R}}^{n}$, we do not achieve a convergence rate of ${({KN})}^{- {1/2}}$. Instead, the rate is $K^{- {1/2}} + N^{- {1/2}}$. This outcome is expected, as the points ${(u_{k},t_{i},x_{i})}_{i,k}$ are not sampled independently. In particular, for a given finite number of observed controls $K \in {\mathbb{N}}^{\ast}$, the bound does not approach zero as $N$ tends to infinity.

<!-- chunk {"id": "body-0058", "role": "body", "section": "Remark 3 (Dependency in the density estimation)", "weight": 1.0} -->

The proposed method employs the probability density estimation from Bonalli and Rudi. However, our Theorem 4.1. ‣ 4.1 𝐿² learning rates ‣ 4 Learning guarantees ‣ Learning Controlled Stochastic Differential Equations") remains valid regardless of the chosen density estimator. In particular, the learning accuracy of our method is independent of the specific choice of density estimator, given $\epsilon$.

<!-- chunk {"id": "body-0059", "role": "body", "section": "Remark 4 (Control-dependent sampling of ${\\lbrack 0,T\\rbrack} \\times {\\mathbb{R}}^{n}$)", "weight": 1.0} -->

For the sake of clarity, we present our method considering drawing the ${(t_{i},x_{i})}_{i = 1}^{N}$ independently from the control $u_{k}$. Nevertheless, for each $u_{k}$, it might be advantageous to draw distinct data sets ${(t_{k,i},x_{k,i})}_{i = 1}^{N}$ i.i.d. from $p_{s}{( \cdot |u_{k})}$, typically sampling with preference for the high-value regions of ${\hat{p}}_{k}$. In this case, our analysis and learning rates still apply, as we do not rely on this independence assumption in our proofs.

<!-- chunk {"id": "body-0060", "role": "body", "section": "Remark 5 (Soft shape Constraint)", "weight": 1.0} -->

When considering the soft shape constraint for the diffusion coefficient, the theoretical analysis involves examining kernel ridge regression under additional linear constraints, which is not expected to introduce significant difficulties. We anticipate that this approach could yield rates comparable to those obtained under hard shape constraints; nonetheless, rigorous investigation is necessary to confirm this. We leave this question for future investigation.

<!-- chunk {"id": "body-0061", "role": "body", "section": "Refined $L^{2}$ learning rates", "weight": 1.0} -->

Applying additional regularity conditions that finely measure the effective dimension of the learning problem generally enables the derivation of refined learning rates. In the context of kernel ridge regression, this is standardly achieved by measuring the regularity of the features and of the target, leading to learning rates that are adaptive to the strength of these regularities. This section focuses on such assumptions tailored to our specific least-squares problem: FP matching.

<!-- chunk {"id": "body-0062", "role": "body", "section": "Kernel-model for $\\frac{\\partial p}{\\partial t}$ induced from $(b,\\sigma^{2})$", "weight": 1.0} -->

Considering a RKHS modeling for the coefficients, as defined in Section, and based on Lemma 3.1. ‣ 3.1 Fokker-Planck matching inequality ‣ 3 Proposed method ‣ Learning Controlled Stochastic Differential Equations"), Lemma 3.2. ‣ 3.1 Fokker-Planck matching inequality ‣ 3 Proposed method ‣ Learning Controlled Stochastic Differential Equations"), and Assumption (A4) (Attainability assumption). ‣ 4.1 𝐿² learning rates ‣ 4 Learning guarantees ‣ Learning Controlled Stochastic Differential Equations"), then there exists $w \in \mathcal{G}_{n}$ such that

<!-- chunk {"id": "body-0063", "role": "body", "section": "Assumption (A5) (Regularity of $\\frac{\\partial p}{\\partial t}$)", "weight": 1.0} -->

This condition is referred to as the source condition. Notably, Assumption (A5) (Regularity of ∂𝑝/∂𝑡). ‣ Kernel-model for ∂𝑝/∂𝑡 induced from (𝑏,𝜎²). ‣ 4.2 Refined 𝐿² learning rates ‣ 4 Learning guarantees ‣ Learning Controlled Stochastic Differential Equations") with $\alpha = 0$ corresponds to Assumption (A4) (Attainability assumption). ‣ 4.1 𝐿² learning rates ‣ 4 Learning guarantees ‣ Learning Controlled Stochastic Differential Equations"). It pertains to the regularity of $\frac{\partial p}{\partial t}$. For concrete examples, refer to Section 4.5.

<!-- chunk {"id": "body-0064", "role": "body", "section": "Assumption (A6) (Regularity of the features)", "weight": 1.0} -->

(A6.1) There exists $r \in {\lbrack 0,1\rbrack}$ and $c > 0$ such that

<!-- chunk {"id": "body-0065", "role": "body", "section": "Assumption (A6) (Regularity of the features)", "weight": 1.0} -->

(A6.2) There exists $s \in {\lbrack 0,1\rbrack}$ and $c > 0$ such that

<!-- chunk {"id": "body-0066", "role": "body", "section": "Assumption (A6) (Regularity of the features)", "weight": 1.0} -->

Assumptions (A6) (Regularity of the features). ‣ Kernel-model for ∂𝑝/∂𝑡 induced from (𝑏,𝜎²). ‣ 4.2 Refined 𝐿² learning rates ‣ 4 Learning guarantees ‣ Learning Controlled Stochastic Differential Equations"), known as embedding properties, are always satisfied for $r = s = 0$ (as $\overset{\sim}{\phi}$ is bounded) and become stricter as ${r,s} \in {\lbrack 0,1\rbrack}$ increase. The embedding property relates to the effective dimension of the input distribution through the RKHS (see Remark. ‣ Kernel-model for ∂𝑝/∂𝑡 induced from (𝑏,𝜎²). ‣ 4.2 Refined 𝐿² learning rates ‣ 4 Learning guarantees ‣ Learning Controlled Stochastic Differential Equations") below). Furthermore, by quantifying the minimal alignment of the covariance with any features almost surely over the input space, it measures of how well almost all input points are represented within the least-squares objective, indicating typically the presence or absence of low-probability regions. For concrete examples, refer to Section 4.5.

<!-- chunk {"id": "body-0067", "role": "body", "section": "Remark 6 (Decomposition of the embedding property)", "weight": 1.0} -->

Assumptions (A6) (Regularity of the features). ‣ Kernel-model for ∂𝑝/∂𝑡 induced from (𝑏,𝜎²). ‣ 4.2 Refined 𝐿² learning rates ‣ 4 Learning guarantees ‣ Learning Controlled Stochastic Differential Equations") can be viewed as decomposing the embedding property on ${\lbrack 0,T\rbrack} \times {\mathbb{R}}^{n} \times \mathcal{H}$ into two embedding properties on ${\lbrack 0,T\rbrack} \times {\mathbb{R}}^{n}$ and $\mathcal{H}$. In particular, Assumptions (A6) (Regularity of the features). ‣ Kernel-model for ∂𝑝/∂𝑡 induced from (𝑏,𝜎²).

<!-- chunk {"id": "body-0068", "role": "body", "section": "Remark 7 (Embedding property and capacity condition)", "weight": 1.0} -->

The embedding property is a finer assumption compared to the standard capacity condition. In particular, Assumptions (A6) (Regularity of the features). ‣ Kernel-model for ∂𝑝/∂𝑡 induced from (𝑏,𝜎²). ‣ 4.2 Refined 𝐿² learning rates ‣ 4 Learning guarantees ‣ Learning Controlled Stochastic Differential Equations") imply the capacity condition ${{Tr}{(C^{1 - {rs}})}} = {{\mathbb{E}}{\lbrack{\|{C^{- {{rs}/2}}\overset{\sim}{\phi}}\|}_{\mathcal{G}_{n}}^{2}\rbrack}} \leq c$ for $c > 0$. While the capacity condition allows refining learning rates from $n^{- {1/4}}$ to $n^{- {1/2}}$ in the noisy least-squares setting, Assumptions (A6) (Regularity of the features). ‣ Kernel-model for ∂𝑝/∂𝑡 induced from (𝑏,𝜎²).

<!-- chunk {"id": "body-0069", "role": "body", "section": "Remark 7 (Embedding property and capacity condition)", "weight": 1.0} -->

‣ 4.2 Refined 𝐿² learning rates ‣ 4 Learning guarantees ‣ Learning Controlled Stochastic Differential Equations") allow refining learning rates from $n^{- {1/2}}$ to arbitrarily fast polynomial decay in the noiseless setting, as $r$ and $s$ transition from 0 to 1.

<!-- chunk {"id": "body-0070", "role": "body", "section": "Remark 7 (Embedding property and capacity condition)", "weight": 1.0} -->

We derive refined learning rates for the proposed estimator.

<!-- chunk {"id": "body-0071", "role": "body", "section": "$L^{\\infty}$ learning rates", "weight": 1.0} -->

From an optimal control perspective, it is relevant to establish learning guarantees almost surely over the control space rather than in expectation over the control space. $L^{2}$ rates can be casted into $L^{\infty}$ rates thanks to Assumption (A6) (Regularity of the features). ‣ Kernel-model for ∂𝑝/∂𝑡 induced from (𝑏,𝜎²). ‣ 4.2 Refined 𝐿² learning rates ‣ 4 Learning guarantees ‣ Learning Controlled Stochastic Differential Equations").

<!-- chunk {"id": "body-0072", "role": "body", "section": "Conditional Value at Risk (CVaR)", "weight": 1.0} -->

For any $\alpha \in {\lbrack 0,1\rbrack}$, the conditional value at risk of a random variable $X:{\Omega\rightarrow{\mathbb{R}}}$ is defined as

<!-- chunk {"id": "body-0073", "role": "body", "section": "Conditional Value at Risk (CVaR)", "weight": 1.0} -->

CVaR is a risk measure that can essentially be interpreted as the expected value conditional upon being within some percentage of the worst-case scenarios (i.e., high X).

<!-- chunk {"id": "body-0074", "role": "body", "section": "Remark 8 (Risk averse optimal control)", "weight": 1.0} -->

CVaR has applications in risk-averse optimal control, where methods typically involve solving

<!-- chunk {"id": "body-0075", "role": "body", "section": "Remark 8 (Risk averse optimal control)", "weight": 1.0} -->

where $D$ is a risk measure, $f$ the loss, and $\lambda > 0$ a trade-off parameter. Compared to the approach of choosing $\lambda = 0$, it allows minimizing the dispersion of the loss around its mean. Various risk can be defined depending on the application. Typically, one can defined the risk measure as the variance. However, if one does not want to treats the excess over the mean equally as the shortfall, one will prefer the VaR or CVaR over the variance. The latter, enjoying better mathematical properties than the former, has become a standard tool in the litterature for managing risk.

<!-- chunk {"id": "body-0076", "role": "body", "section": "Application to Sobolev spaces", "weight": 1.0} -->

In this section, we analyze the example of SDE coefficients in Sobolev spaces.

<!-- chunk {"id": "body-0077", "role": "body", "section": "Application to Sobolev spaces", "weight": 1.0} -->

In this lemma, we examine the extent to which all previously discussed assumptions are satisfied when considering $(b,\sigma^{2})$ within a Sobolev space.

<!-- chunk {"id": "body-0078", "role": "body", "section": "Remark 9 (Regularity of $p$)", "weight": 1.0} -->

In Lemma 4.7, we operate under the assumption that the probability density function ${u,t,x}\mapsto{p{(u,t,x)}}$ associated with the stochastic differential equation is regular, specifically that it belongs to a Sobolev space of order $q - 2$ with respect to the parameter $\theta$. This regularity assumption is typically valid when the coefficients ${t,x,\theta}\mapsto{{(b,\sigma^{2})}{(t,x,{u_{\theta}{(t)}})}}$ of the SDE are themselves sufficiently regular in $t,x,\theta$. Although a comprehensive proof of this regularity goes beyond the scope of this paper, the general validity of the assumption can be inferred from the regularity properties of the coefficients and controls. For further details on such regularity results, refer to the appropriate literature on stochastic calculus and Fokker-Planck equations (see, for example, Lunardi, specifically Section 8.3.1, and Friedman, Theorem 7).

<!-- chunk {"id": "body-0079", "role": "body", "section": "Remark 9 (Regularity of $p$)", "weight": 1.0} -->

From Lemma 4.7, we deduce learning rates for our controlled SDE coefficients estimation method in the case of coefficients in Sobolev spaces.

<!-- chunk {"id": "body-0080", "role": "body", "section": "Remark 10 (Optimal learning rates)", "weight": 1.0} -->

Most existing literature focuses on the noisy regression setting. Nevertheless, in the noiseless setting, minimax rate in $L^{\infty}$-norm of $\mathcal{O}{({({\log^{1/2}{K/\sqrt{K}}})}^{\frac{2{({q - 2})}}{m}})}$ has been proven by Bauer et al. when estimating $q - 2$-times continuously differentiable function on ${\lbrack 0,1\rbrack}^{m}$ with $K$ i.i.d. data points. In comparison, our rates are $\mathcal{O}{({({\log{K/\sqrt{K}}})}^{\frac{2{({q - 2})}}{m}{({1 - \frac{m}{2{({q - 2})}}})}})}$ slower than their rates, but they converge closely as $q$ increases.

<!-- chunk {"id": "body-0081", "role": "body", "section": "Remark 10 (Optimal learning rates)", "weight": 1.0} -->

We derive the following results as a consequence of Corollary 4.2. ‣ 4.5 Application to Sobolev spaces ‣ 4 Learning guarantees ‣ Learning Controlled Stochastic Differential Equations").

<!-- chunk {"id": "body-0082", "role": "body", "section": "Remark 11 (Complexity analysis in $M$ and $Q$)", "weight": 1.0} -->

In our analysis, we assume that density estimation ${\hat{p}}_{k}$ for each $p{(u_{k})}$ is sufficiently accurate, and therefore omits a detailed examination of the computational complexity in terms of parameters $M$ and $Q$. While Bonalli and Rudi address this complexity in the case of $\varepsilon$, an extension is required for $\varepsilon_{\infty}$. Here, we focus on the number of controls required to reach a desired accuracy $\eta > 0$, and the computational cost of the Fokker-Planck step, which dominates the computational cost in our numerical experiments of Section.

<!-- chunk {"id": "body-0083", "role": "body", "section": "Adaptive learning rates", "weight": 1.0} -->

In Section 4.5, we examined Sobolev coefficients. While analyzing stronger assumptions could potentially lead to faster learning rates, this is not the primary focus of our paper. For illustrative purposes, we provide two examples of stronger assumptions in Examples. ‣ 4.6 Adaptive learning rates ‣ 4 Learning guarantees ‣ Learning Controlled Stochastic Differential Equations") and. ‣ 4.6 Adaptive learning rates ‣ 4 Learning guarantees ‣ Learning Controlled Stochastic Differential Equations"). However, a detailed analysis of these assumptions is beyond the scope of our study. The key result of this paper is the adaptability of the proposed method: it automatically benefits from the most favorable regularity assumptions, whether they pertain to Sobolev regularity or other types. Specifically, our method achieves the best learning rates based on the most advantageous parameters $r$ and $s$ in Assumptions (A6) (Regularity of the features). ‣ Kernel-model for ∂𝑝/∂𝑡 induced from (𝑏,𝜎²). ‣ 4.2 Refined 𝐿² learning rates ‣ 4 Learning guarantees ‣ Learning Controlled Stochastic Differential Equations"), without requiring prior knowledge of these optimal parameters.

<!-- chunk {"id": "body-0084", "role": "body", "section": "Example 2 (Parametric probability density)", "weight": 1.0} -->

Consider the scenario where $p{(u,t, \cdot )}$ lies, for all ${t,u} \in {{\lbrack 0,T\rbrack} \times \mathcal{H}}$, within a parametric family of dimension $m$. In this case, Fokker-Planck matching formulates as a least-squares problem over a space of dimension $m + 1 + n + d$, independent of the dimension of the control space $\mathcal{H}$.

<!-- chunk {"id": "body-0085", "role": "body", "section": "Example 2 (Parametric probability density)", "weight": 1.0} -->

set containing all distributions over ${\mathbb{R}}^{n}$ reached given the control space and initial distribution. Specifically,

<!-- chunk {"id": "body-0086", "role": "body", "section": "Example 2 (Parametric probability density)", "weight": 1.0} -->

where the explicit solution can be derived by means of the variation of constants formula, resulting in ${X{(t)}} \sim {\mathcal{N}{({\mu{(t)}},{\Sigma{(t)}})}}$, with $\mu$ and $\Sigma$ governed by linear ODEs. For more details, refer to Chapter 6.3. In this setting, $p{(u,t, \cdot )}$ for any control $u \in \mathcal{H} \triangleq {L^{2}{({\lbrack 0,T\rbrack},{\mathbb{R}}^{n})}}$ belongs to a parametric family of dimension $m = {n + {{n{({n - 1})}}/2}}$. Consequently, it is straightforward to show that Assumptions (A6) (Regularity of the features). ‣ Kernel-model for ∂𝑝/∂𝑡 induced from (𝑏,𝜎²).

<!-- chunk {"id": "body-0087", "role": "body", "section": "Example 2 (Parametric probability density)", "weight": 1.0} -->

‣ 4.2 Refined 𝐿² learning rates ‣ 4 Learning guarantees ‣ Learning Controlled Stochastic Differential Equations") are satisfied with $r = {1 - \frac{d + m}{2{({q - 2})}}}$ and $s = {1 - \frac{n + 1}{2{({q - 2})}}}$.

<!-- chunk {"id": "body-0088", "role": "body", "section": "Example 3 (Identifiability)", "weight": 1.0} -->

Equations ) and ) ensure that Assumptions (A6) (Regularity of the features). ‣ Kernel-model for ∂𝑝/∂𝑡 induced from (𝑏,𝜎²).

<!-- chunk {"id": "body-0089", "role": "body", "section": "Example 3 (Identifiability)", "weight": 1.0} -->

This suggests that identifiability necessitates minimal mass conditions, such as avoiding regions of ${\lbrack 0,T\rbrack} \times {\mathbb{R}}^{n}$ that, while having non-zero Lebesgue measure, are explored with zero probability. However, note that deriving conditions to ensure identifiability is generally intricate.

<!-- chunk {"id": "body-0090", "role": "body", "section": "Extension to closed-loop control", "weight": 1.0} -->

For clarity in exposition, we considered position-independent (a.k.a. open-loop) controls in the previous sections. Nevertheless, our approach and results seamlessly extend to position-dependent controls $u{(t,x)}$, which is essential for control systems employing monitoring feedback. This extension involves updating the Fokker-Planck equation, specifically the Kolmogorov generator (or equivalently, $\overset{\sim}{\phi}$), to account for the dependencies on the system's state variables. From a practical standpoint, modifying $\hat{\phi}$ is straightforward, although it requires knowledge of the controls' partial derivatives. From a theoretical standpoint, the required modifications are limited to Lemma 7.10-ϕ̂_𝑘⁢(𝑡,𝑥)‖_𝒢_𝑛²]). ‣ 7.10 Auxiliary lemmas ‣ 7 Proofs ‣ Learning Controlled Stochastic Differential Equations") and are also straightforward. We expect the learning rates to remain the same, though the constants will be updated and will depend on the supremum bounds of the control's partial derivatives.

<!-- chunk {"id": "body-0091", "role": "body", "section": "Numerical experiments", "weight": 1.0} -->

In this section, we present numerical experiments on the problems of uncontrolled (Section 5.1) and controlled (Section 5.2) SDE estimation, illustrating the main behaviors of the evaluated methods.

<!-- chunk {"id": "body-0092", "role": "body", "section": "Purpose of uncontrolled SDE experiments", "weight": 1.0} -->

We initiate our numerical study by implementing and evaluating the method proposed in Bonalli and Rudi for uncontrolled SDE estimation. Note that the method proposed in Bonalli and Rudi corresponds to our approach in the limit case where the control space is reduced to a singleton $\mathcal{H} = {\{ u\}}$. Therefore, this study provides important insights for the more intricate scenario of controlled SDEs considered in Section 5.2.

<!-- chunk {"id": "body-0093", "role": "body", "section": "Python open-source library", "weight": 1.0} -->

Our implementation is available as an open-source Python library on the GitHub repository lmotte/sde-learn. The library includes comprehensive documentation and example scripts demonstrating various use cases with light computational demands. In particular, our implementation supports the Nyström approximation, which aids in reducing the computational complexity of Fokker-Planck matching. Further details, including thorough derivations of all necessary formulas for implementing the proposed estimator and the computational complexity of each step, are provided in Section.

<!-- chunk {"id": "body-0094", "role": "body", "section": "Experimental setup", "weight": 1.0} -->

We consider uniform diffusion and use the soft-shape constraint presented in Section for the diffusion coefficient. All kernels are Gaussian kernels ${k{(x,y)}} = {\exp{({- {\gamma{\|{x - y}\|}^{2}}})}}$ with different parameters $\gamma > 0$. We select all hyperparameters using grid search and validation sets.

<!-- chunk {"id": "body-0095", "role": "body", "section": "Computational considerations", "weight": 1.0} -->

While the computational complexity of each step is provided in Section, we offer here a practical idea of the computational requirements by reporting the observed execution times from our experiments on the considered problem and data sets. These experiments were performed on a machine equipped with an Apple M3 Pro processor and 18 GB of RAM. For the 1D case, the probability density estimation step takes 0.015 seconds for training with 1000 sample paths and 100 time steps, and 0.11 seconds for prediction over a Fokker-Planck training set of size 2500. The Fokker-Planck matching step requires 6.0 seconds for training with 2500 data points and 3.7 seconds to generate 100 sample paths with 100 time steps. For the two 2D problems, probability density estimation training takes around 0.012 seconds for 3000 sample paths and 100 time steps, with prediction taking approximately 60 seconds over a Fokker-Planck training set of size 3000. The Fokker-Planck matching step requires about 10 seconds for training and 6 seconds to generate 100 sample paths with 100 time steps.

<!-- chunk {"id": "body-0096", "role": "body", "section": "Computational considerations", "weight": 1.0} -->

These results indicate that, although the computational times are non-trivial, they remain manageable---ranging from a few seconds to just over a minute---demonstrating the practicality of the method for the problem sizes considered.

<!-- chunk {"id": "body-0097", "role": "body", "section": "Linear scalar SDE", "weight": 1.0} -->

To carry out our first experiments, we consider Ornstein--Uhlenbeck processes.

<!-- chunk {"id": "body-0098", "role": "body", "section": "Ornstein--Uhlenbeck process", "weight": 1.0} -->

The Ornstein-Uhlenbeck (OU) process is a simple example of stochastic process, which tends to revert to a mean over time under the influence of a mean-reverting term and a stochastic noise term. It is a useful tool, for example, for modeling phenomena such as price volatility. It is defined by the following SDE

<!-- chunk {"id": "body-0099", "role": "body", "section": "Ornstein--Uhlenbeck process", "weight": 1.0} -->

where $\mu$ is the mean to which the process reverts, $\theta$ is the mean-reverting coefficient giving the strength of revertion to $\mu$, and $\sigma$ is the amplitude of the stochastic noise. The probability density function of the OU process can be explicitly derived by solving the Fokker-Planck equation. Notably, if $X{}$ is initially Gaussian-distributed with mean $\mu_{0} \in {\mathbb{R}}$ and covariance $\sigma_{0}^{2} > 0$, then $X{(t)}$ will follow a Gaussian distribution with the mean and covariance given by

<!-- chunk {"id": "body-0100", "role": "body", "section": "Data sets", "weight": 1.0} -->

We consider an Ornstein-Uhlenbeck process with constant variance and a mean that increases from $0.5$ to $2.5$ from $t = 0$ to $t = 10$. Specifically, we set ${\mu = 2.5},{{\theta = 0.5},{{\sigma^{2} = {\theta/4}},{{\mu_{0} = 0.5},{\sigma_{0}^{2} = {\sigma^{2}/{({2\theta})}}}}}}$, and $T = 10$. In Figure, we plot 100 sample paths generated from this OU process. For the probability density estimation steps, we draw training and validation sets with ${Q/Q_{val}} = {1000/100}$ sample paths and ${M/M_{val}} = {100/100}$ time steps, respectively.

<!-- chunk {"id": "body-0101", "role": "body", "section": "Data sets", "weight": 1.0} -->

For the Fokker-Planck matching step, we draw a training set ${(t_{i},x_{i})}_{i = 1}^{N} = {{\{ t_{i}\}}_{i = 1}^{50} \times {\{ x_{i}\}}_{i = 1}^{50}}$ by drawing times and positions uniformly within well-chosen intervals, and we draw a validation set with same size and distribution.

<!-- chunk {"id": "body-0102", "role": "body", "section": "Step 1 (probability density estimation)", "weight": 1.0} -->

In Figure. ‣ 5.1.1 Linear scalar SDE ‣ 5.1 Uncontrolled SDE estimation ‣ 5 Numerical experiments ‣ Learning Controlled Stochastic Differential Equations"), we plot the true and estimated probability densities, $p{(t,x)}$ and $\hat{p}{(t,x)}$, respectively. These densities are plotted on a uniformly spaced temporal grid, offset by $1/2$ unit from the training time discretization, and a spatial grid with positions randomly drawn from a uniform distribution within an interval. The estimated density reasonably approximates the true dynamics, as visually evident.

<!-- chunk {"id": "body-0103", "role": "body", "section": "Step 2 (coefficients estimation via FP matching)", "weight": 1.0} -->

In Figure. ‣ 5.1.1 Linear scalar SDE ‣ 5.1 Uncontrolled SDE estimation ‣ 5 Numerical experiments ‣ Learning Controlled Stochastic Differential Equations"), we plot the estimated coefficients obtained via FP matching. Notice that these estimated coefficients differ significantly from the true coefficients. As discussed in Remark. ‣ Experiment design. ‣ 2 Problem setting ‣ Learning Controlled Stochastic Differential Equations"), measuring the accuracy of the estimated coefficients using the $L^{2}$ distance from the true coefficients is excluded due to the non-identifiability of the coefficients. Our learning guarantees do not ensure the recovery of the true coefficients but rather ensure that the estimated coefficients accurately replicate the true dynamics. Specifically, this involves obtaining an induced distribution $p_{\hat{b},\hat{\sigma}}$ that closely approximates the true distribution $p_{b,\sigma}$ in terms of $L^{2}$ distance.

<!-- chunk {"id": "body-0104", "role": "body", "section": "Recovering the true dynamic", "weight": 1.0} -->

We draw and plot 100 sample paths from the true and estimated coefficients in Figure to assess the recovery of the true dynamics. Notice that the estimated coefficients lead to visually comparable probability distributions, with close means and variances over time. Interestingly, while the distributions are similar, individual paths appear quite different.

<!-- chunk {"id": "body-0105", "role": "body", "section": "Nonlinear multivariate SDE", "weight": 1.0} -->

To carry out nonlinear multivariate SDE experiments, we consider two examples: Dubins process, and finite exponential sum process.

<!-- chunk {"id": "body-0106", "role": "body", "section": "Dubins process", "weight": 1.0} -->

The Dubins process is defined by the following SDE

<!-- chunk {"id": "body-0107", "role": "body", "section": "Finite exponential sum (FES) process", "weight": 1.0} -->

We introduce the process defined by the SDE associated with the following coefficients

<!-- chunk {"id": "body-0108", "role": "body", "section": "Data sets", "weight": 1.0} -->

For the Dubins process, we set the parameters as follows: $T = 10$, $n = 2$, $M = 100$, $Q = 3000$, $v = 2$, $\theta = 3$, and $\sigma = 0.3$. For the probability density estimation steps, the training and validation sets consist of ${Q/Q_{val}} = {3000/100}$ sample paths and ${M/M_{val}} = {100/10}$ time steps, respectively. For the Fokker-Planck matching step, training and a validation set are drawn by sampling the set of training sample paths' time-position pairs, with size $N = {3000/N_{val}} = 1000$.

<!-- chunk {"id": "body-0109", "role": "body", "section": "Data sets", "weight": 1.0} -->

For the Fokker-Planck matching step, we use a training set ${\{ t_{i}\}}_{i = 1}^{30} \times {\{ x_{i}\}}_{i = 1}^{100}$ where the sets of times and positions are drawn uniformly in well-chosen interval and two-dimensional box, respectively. We use a validation set ${\{ t_{i}\}}_{i = 1}^{10} \times {\{ x_{i}\}}_{i = 1}^{100}$ where times and positions are uniform grids in well-chosen interval and two-dimensional box. For both processes, the initial condition is ${X{}} \sim {\mathcal{N}{(0,{{1/4}I_{{\mathbb{R}}^{2}}})}}$.

<!-- chunk {"id": "body-0110", "role": "body", "section": "Recovering the true dynamic", "weight": 1.0} -->

We perform density estimation and Fokker-Planck (FP) matching for both processes, selecting the hyperparameters based on the validation sets as previously. We draw and plot 100 sample paths from both the true and estimated coefficients in Figure and in Figure process. ‣ 5.1.2 Nonlinear multivariate SDE ‣ 5.1 Uncontrolled SDE estimation ‣ 5 Numerical experiments ‣ Learning Controlled Stochastic Differential Equations"). Notably, the estimated coefficients lead to probability distributions that are visually comparable to those of the true dynamics, with closely matching means and variances over time.

<!-- chunk {"id": "body-0111", "role": "body", "section": "Observations", "weight": 1.0} -->

Our experiments highlight key behaviors in the estimation of uncontrolled SDEs. Specifically, we observe the following phenomena.

<!-- chunk {"id": "body-0112", "role": "body", "section": "Observations", "weight": 1.0} -->

Cumulative error. The accuracy of the density $p_{\hat{b},\hat{\sigma}}{(t,x)}$, associated with the estimated coefficients $(\hat{b},{\hat{\sigma}}^{2})$, decreases over time due to cumulative error. Even if the coefficients at a given time $t_{0}$ are accurate, earlier inaccuracies for $0 \leq t < t_{0}$ can lead to an inaccurate $p_{\hat{b},\hat{\sigma}}{(t_{0},x)}$.

<!-- chunk {"id": "body-0113", "role": "body", "section": "Observations", "weight": 1.0} -->

Error amplification. Paths that enter regions of low probability, whether in time or space, where the accuracy of the coefficients is poor, experience error amplification. This often results in path divergence or termination. Increasing the variance of $X{}$ can facilitate a broader exploration of times and positions, thereby reducing this instability.

<!-- chunk {"id": "body-0114", "role": "body", "section": "Observations", "weight": 1.0} -->

An illustrative analogy is a marble run: small deviations early on can lead to cumulative errors and amplified divergence, much like the behavior observed in the estimation of coefficients in SDEs.

<!-- chunk {"id": "body-0115", "role": "body", "section": "Python open-source library", "weight": 1.0} -->

Our implementation is available as an open-source Python library on the GitHub repository lmotte/controlled-sde-learn. The library includes comprehensive documentation and example scripts demonstrating various use cases with light computational demands. More details are provided in Section, including detailed derivations of all necessary formulas for implementing the proposed estimator.

<!-- chunk {"id": "body-0116", "role": "body", "section": "Experimental setup", "weight": 1.0} -->

We consider uniform diffusion and the soft-shape constraint presented in Section for the diffusion coefficient. All kernels are Gaussian kernels ${k{(x,y)}} = {\exp{({- {\gamma{\|{x - y}\|}^{2}}})}}$ with different parameters $\gamma > 0$. For the 1D SDE, we select all hyperparameters using grid search and validation sets.

<!-- chunk {"id": "body-0117", "role": "body", "section": "Experimental setup", "weight": 1.0} -->

For the 2D SDE, to avoid excessive computation, we fix the hyperparameters for both the probability density estimation and the Fokker-Planck matching using previously selected hyperparameters for the estimation of uncontrolled Dubins process in Section 5.1.2. Further details can be found in the code repository.

<!-- chunk {"id": "body-0118", "role": "body", "section": "Computational considerations", "weight": 1.0} -->

While the computational complexity of each step is provided in Section, we offer here a practical idea of the computational requirements based on the observed execution times from our experiments on the considered problem and data sets, using a machine equipped with an Apple M3 Pro processor and 18 GB of RAM. For the 1D case, the probability density estimation step takes 5.6 seconds for training with 1000 sample paths, 100 time steps, and 10 training controls, and 1.0 seconds for prediction over a Fokker-Planck training set of size 10000. The Fokker-Planck matching step requires 190 seconds for training with 10000 data points and 150 seconds to generate 100 sample paths with 100 time steps for 10 different controls. For the 2D problem, probability density estimation training takes around 0.032 seconds for 3000 sample paths, 100 time steps, and 20 training controls, with prediction taking approximately 160 seconds over a Fokker-Planck training set of size 10000. The Fokker-Planck matching step requires about 490 seconds for training and 140 seconds to generate 100 sample paths with 100 time steps for 5 different controls. These results show that, while the computational demands are higher for controlled SDEs, they remain manageable.

<!-- chunk {"id": "body-0119", "role": "body", "section": "Computational considerations", "weight": 1.0} -->

As expected, the computational requirements increase as the sizes of the data sets are multiplied by the number of training controls.

<!-- chunk {"id": "body-0120", "role": "body", "section": "Linear scalar SDE", "weight": 1.0} -->

To carry out our first experiments, we consider controlled Ornstein--Uhlenbeck processes.

<!-- chunk {"id": "body-0121", "role": "body", "section": "Controlled Ornstein--Uhlenbeck process", "weight": 1.0} -->

Let $X{(t)}$ be a Ornstein--Uhlenbeck process with controlled mean, defined by the SDE

<!-- chunk {"id": "body-0122", "role": "body", "section": "Data sets", "weight": 1.0} -->

We consider a controlled OU process, and set ${\theta = 0.5},{{\sigma^{2} = {\theta/4}},{{\mu_{0} = 0.5},{\sigma_{0}^{2} = {\sigma^{2}/{({2\theta})}}}}}$, $T = 10$, and ${X{}} \sim {\mathcal{N}{(\mu_{0},\sigma_{0}^{2})}}$. In Figure, we plot 100 sample paths generated from this OU process for three different controls. We draw a data set of $K = 10$ controls, as shown in Figure, by drawing $u_{0},u_{1},t_{1}$ independently and uniformly in $\lbrack{- 2},2\rbrack$, $\lbrack{- 2},2\rbrack$, and $\lbrack 3,7\rbrack$, respectively.

<!-- chunk {"id": "body-0123", "role": "body", "section": "Data sets", "weight": 1.0} -->

For the probability density estimation steps, we draw training and validation sets with ${Q/Q_{val}} = {1000/100}$ sample paths and ${M/M_{val}} = {100/100}$ time steps, respectively. For the Fokker-Planck matching step, we draw a training set ${(t_{i},x_{i})}_{i = 1}^{N} = {{\{ t_{i}\}}_{i = 1}^{20} \times {\{ x_{i}\}}_{i = 1}^{50}}$ by drawing times and positions uniformly within well-chosen intervals, and we draw a validation set with same size and distribution.

<!-- chunk {"id": "body-0124", "role": "body", "section": "Recovering the true controlled dynamics", "weight": 1.0} -->

For $K_{te} = 3$ randomly drawn controls, we generate and plot 100 sample paths using both the true and estimated coefficients, as shown in Figure, to assess the recovery of the true controlled dynamics. The estimated coefficients produce probability distributions that are visually comparable to the true ones, with closely matching means and variances over time. It is important to note that the three controls used for evaluation are not part of the training data.

<!-- chunk {"id": "body-0125", "role": "body", "section": "Nonlinear multivariate SDE", "weight": 1.0} -->

To conduct nonlinear multivariate SDE experiments, we consider controlled Dubins processes.

<!-- chunk {"id": "body-0126", "role": "body", "section": "Controlled Dubins process", "weight": 1.0} -->

Let $X{(t)}$ be a Dubins process with a controlled angle, defined by the SDE

<!-- chunk {"id": "body-0127", "role": "body", "section": "Data sets", "weight": 1.0} -->

We consider a controlled Dubins process and set $v = 2$, $\sigma = 0.3$, $\mu_{0} = 0$, $\sigma_{0} = 0.5$, $T = 10$, and ${X{}} \sim {\mathcal{N}{(\mu_{0},{\sigma_{0}^{2}I_{{\mathbb{R}}^{2}}})}}$. In Figure, we plot 100 sample paths generated from this process for five different controls. We build a data set of $K = 20$ controls, as shown in Figure, by drawing $a$ independently and uniformly from $\lbrack{- 1.2},1.2\rbrack$. For the probability density estimation steps, we generate a training set with $Q = 3000$ sample paths and $M = 100$ time steps.

<!-- chunk {"id": "body-0128", "role": "body", "section": "Data sets", "weight": 1.0} -->

For the Fokker-Planck matching step, we draw a training set ${(u_{k},t_{i},x_{i})}_{{k \in {⟦1,20⟧}},{i \in {⟦1,500⟧}}}$ of size $10^{4}$. To avoid sampling regions where $p{(u_{k},t,x)}$ is negligible, for each $u_{k}$, we draw a set of 500 pairs ${(t_{i},x_{i})}_{i = 1}^{500}$ from a set of 5 sample paths with 100 time steps, generated using the same parameters as the controlled Dubins process but with an initial variance of $\sigma_{0} = 2.5$.

<!-- chunk {"id": "body-0129", "role": "body", "section": "Recovering the true controlled dynamics", "weight": 1.0} -->

For $K_{te} = 5$ controls with $a = {{- 1},{- {1/2}},0,{1/2},1}$, spanning the set of possible controls $\mathcal{H}$ with $a \in {\lbrack{- 1},1\rbrack}$, we generate and plot 100 sample paths using both the true and estimated coefficients, as shown in Figure, to evaluate the recovery of the true controlled dynamics. The estimated coefficients yield probability distributions that are visually comparable to the true ones, with matching means and variances over time. Notably, the five controls used for evaluation are not included in the training data.

<!-- chunk {"id": "body-0130", "role": "body", "section": "Conclusion", "weight": 1.5} -->

In this work, we address the problem of estimating continuous, multidimensional nonlinear controlled SDEs with non-uniform diffusion---a previously unaddressed challenge. We demonstrate how dynamical system identification can be approached through (a) density estimation of the dynamics for a finite set of controls, followed by (b) least-squares regression to estimate governing coefficients, using the Fokker-Planck matching inequality. This formulation enables us to derive strong theoretical guarantees by leveraging the rich and well-established literature on nonparametric least-squares regression. We believe this work lays a promising foundation for future research by providing a robust mathematical framework for identifying complex controlled dynamical systems, supporting further exploration of challenges such as experiment design, including online and safe exploration of the control space with theoretical guarantees. Although we illustrate our findings with prototype identification tasks, future research will focus on real-world applications, such as autonomous driving and space rendezvous.

<!-- chunk {"id": "body-0131", "role": "body", "section": "Notations", "weight": 1.0} -->

For the sake of readability, we employ the following notations.

<!-- chunk {"id": "body-0132", "role": "body", "section": "Organization of the proofs", "weight": 1.0} -->

The proofs are organized as follows.

<!-- chunk {"id": "body-0133", "role": "body", "section": "Organization of the proofs", "weight": 1.0} -->

Proof of the Fokker-Planck matching inequality. The FP matching inequality is proven in Section 7.3.

<!-- chunk {"id": "body-0134", "role": "body", "section": "Organization of the proofs", "weight": 1.0} -->

Proof of $L^{2}$ learning rates. We present necessary preliminary results in Section 7.4. The $L^{2}$ learning rates are then established in Section 7.5, based on four main lemmas detailed in Sections 7.6, 7.7, 7.8, and 7.9, respectively. These main lemmas are proven thanks to auxiliary lemmas, which are proven in Section 7.10. The auxiliary lemmas rely on concentration inequalities adapted to our needs, stated in Section 7.11.

<!-- chunk {"id": "body-0135", "role": "body", "section": "Organization of the proofs", "weight": 1.0} -->

Proof of refined $L^{2}$ learning rates. Refined $L^{2}$ learning rates are derived in Section 7.12 using a similar approach to the unrefined $L^{2}$ rates, but employing refined lemmas, which are proven in Section 7.13.

<!-- chunk {"id": "body-0136", "role": "body", "section": "Organization of the proofs", "weight": 1.0} -->

Proof of $L^{\infty}$ learning rates. The proofs for the $L^{\infty}$ learning rates are provided in Section 7.14.

<!-- chunk {"id": "body-0137", "role": "body", "section": "Organization of the proofs", "weight": 1.0} -->

Proof of CVaR learning rates. The proofs for deriving CVaR learning rates are detailed in Section 7.15.

<!-- chunk {"id": "body-0138", "role": "body", "section": "Organization of the proofs", "weight": 1.0} -->

Proofs for Sobolev coefficients. The embedding property of Fokker-Planck matching, when the coefficients belong to a Sobolev space, is derived in Section 7.16.

<!-- chunk {"id": "body-0139", "role": "body", "section": "Useful preliminary results for proving FP matching learning rates", "weight": 1.0} -->

In this section, we state necessary results to prove FP matching learning rates for the estimator proposed in Section with hard shape-constrained PSD diffusion.

<!-- chunk {"id": "body-0140", "role": "body", "section": "FP matching as least-squares regression", "weight": 1.0} -->

The FP matching problem can be formulated as a least-squares regression problem, expressed as

<!-- chunk {"id": "body-0141", "role": "body", "section": "FP matching as least-squares regression", "weight": 1.0} -->

$\overset{\sim}{\phi}:{\mathcal{Z}\rightarrow\mathcal{F}}$ is well-defined from Lemma 4.34 in Steinwart and Christmann.

<!-- chunk {"id": "body-0142", "role": "body", "section": "Empirical FP matching as ridge regression", "weight": 1.0} -->

regularized empirical FP matching (Eq. ) can be formulated as a ridge regression, expressed as

<!-- chunk {"id": "body-0143", "role": "body", "section": "Useful ridge estimators for Theorem 4.1. ‣ 4.1 𝐿² learning rates ‣ 4 Learning guarantees ‣ Learning Controlled Stochastic Differential Equations\") proof's decompositions", "weight": 1.0} -->

We define the ridge estimator $\hat{w}$ obtained from Eq. but without the cone constraint. Namely,

<!-- chunk {"id": "body-0144", "role": "body", "section": "Useful ridge estimators for Theorem 4.1. ‣ 4.1 𝐿² learning rates ‣ 4 Learning guarantees ‣ Learning Controlled Stochastic Differential Equations\") proof's decompositions", "weight": 1.0} -->

Moreover, we define the ridge estimator $w_{K}$, whose discrepancy from the target $w$ arises from the finite sampling of $\mathcal{H}$. Formally,

<!-- chunk {"id": "body-0145", "role": "body", "section": "Useful ridge estimators for Theorem 4.1. ‣ 4.1 𝐿² learning rates ‣ 4 Learning guarantees ‣ Learning Controlled Stochastic Differential Equations\") proof's decompositions", "weight": 1.0} -->

This proposition characterizes the ridge estimators as products and inverses of covariance operators.

<!-- chunk {"id": "body-0146", "role": "body", "section": "Remark 12 (Alternative assumptions to Assumptions (A6) (Regularity of the features). ‣ Kernel-model for ∂𝑝/∂𝑡 induced from (𝑏,𝜎²). ‣ 4.2 Refined 𝐿² learning rates ‣ 4 Learning guarantees ‣ Learning Controlled Stochastic Differential Equations\"))", "weight": 1.0} -->

We denote $\overset{\sim}{\phi} \triangleq {\overset{\sim}{\phi}{(u,t,x)}}$. The three following assumptions can be found in the literature of least-squares regression as alternative conditions on the regularity of the feature space

<!-- chunk {"id": "body-0147", "role": "body", "section": "Remark 12 (Alternative assumptions to Assumptions (A6) (Regularity of the features). ‣ Kernel-model for ∂𝑝/∂𝑡 induced from (𝑏,𝜎²). ‣ 4.2 Refined 𝐿² learning rates ‣ 4 Learning guarantees ‣ Learning Controlled Stochastic Differential Equations\"))", "weight": 1.0} -->

Assumptions and are known as the capacity condition and embedding property, respectively. Assumptions and provide progressively finer conditions on the regularity of the features $\overset{\sim}{\phi}{(u,t,x)}$. Indeed, it is straightforward to show that Assumption implies Assumption with $r_{2} = r_{1}$, and Assumption implies Assumption with $r_{3} = r_{2}$. In the setting of noisy kernel ridge regression, Assumption allows to refine learning rates from $n^{- {1/4}}$ ($r_{1} = 0$) to $n^{- {1/2}}$ ($r_{1} = 1$).

<!-- chunk {"id": "body-0148", "role": "body", "section": "Remark 12 (Alternative assumptions to Assumptions (A6) (Regularity of the features). ‣ Kernel-model for ∂𝑝/∂𝑡 induced from (𝑏,𝜎²). ‣ 4.2 Refined 𝐿² learning rates ‣ 4 Learning guarantees ‣ Learning Controlled Stochastic Differential Equations\"))", "weight": 1.0} -->

In the setting of noiseless kernel ridge regression, Assumption allows to refine learning rates from $n^{- {1/2}}$ ($r_{2} = 0$) to $n^{- 1}$ ($r_{2} = 1$), while Assumption allows to refine them from $n^{- 1}$ ($r_{3} = 0$) to arbitrarily fast polynomial decay as $r_{3}\rightarrow{+ \infty}$. For completeness, we present these three assumptions here; however, for clarity, in this work, we base our proofs on the more stringent Assumption (instead of considering Assumptions and ).

<!-- chunk {"id": "body-0149", "role": "body", "section": "Sketch of the proof", "weight": 1.0} -->

Error due to the finite sampling approximation of times $\lbrack 0,T\rbrack$ and positions ${\mathbb{R}}^{n}$,

<!-- chunk {"id": "body-0150", "role": "body", "section": "Sketch of the proof", "weight": 1.0} -->

Error due to the finite sampling approximation of the space of controls $\mathcal{H}$,

<!-- chunk {"id": "body-0151", "role": "body", "section": "Sketch of the proof", "weight": 1.0} -->

and then bounding each error component.

<!-- chunk {"id": "body-0152", "role": "body", "section": "Sketch of the proof", "weight": 1.0} -->

Denoting $z = {(t,x)}$, $\overset{\sim}{\phi} = {\overset{\sim}{\phi}{(u,t,x)}}$, and $\hat{\mathbb{E}}{\lbrack \cdot \rbrack}$ as the empirical expectation over the training points, this corresponds to the following successive approximations.

<!-- chunk {"id": "body-0153", "role": "body", "section": "Bound ${\\|{\\hat{D} - \\overset{\\sim}{D}}\\|}_{\\mathcal{G}_{n}}$", "weight": 1.0} -->

From Lemma 7.11. ‣ 7.10 Auxiliary lemmas ‣ 7 Proofs ‣ Learning Controlled Stochastic Differential Equations"), for any $\delta \in {(0,1\rbrack}$, with probability at least $1 - \delta$

<!-- chunk {"id": "body-0154", "role": "body", "section": "Bound ${\\|{\\hat{D} - \\overset{\\sim}{D}}\\|}_{\\mathcal{G}_{n}}$", "weight": 1.0} -->

where $c > 0$ is a constant that does not depend on $N,K,\delta$.

<!-- chunk {"id": "body-0155", "role": "body", "section": "Bound ${\\|{{\\hat{C}}_{\\lambda}^{- 1}C^{1/2}}\\|}_{\\infty}$", "weight": 1.0} -->

By Lemmas 7.12. ‣ Conclusion. ‣ 7.10 Auxiliary lemmas ‣ 7 Proofs ‣ Learning Controlled Stochastic Differential Equations") and 7.13. ‣ Conclusion. ‣ 7.10 Auxiliary lemmas ‣ 7 Proofs ‣ Learning Controlled Stochastic Differential Equations"), for any $\delta \in {(0,1\rbrack}$, if $\lambda \geq {c{\log\frac{2}{\delta}}{({N^{- 1} + \varepsilon})}}$, $\lambda \geq {\frac{18c}{N}{\log\frac{N}{\delta}}}$ and $\lambda \geq {\frac{18c}{K}{\log\frac{K}{\delta}}}$, then with probability at least $1 - \delta$,

<!-- chunk {"id": "body-0156", "role": "body", "section": "Bound ${\\|{{\\hat{C}}_{\\lambda}^{- 1}C^{1/2}}\\|}_{\\infty}$", "weight": 1.0} -->

where $c > 0$ is a constant that does not depend on $N,K,\delta$.

<!-- chunk {"id": "body-0157", "role": "body", "section": "Bound ${\\|{\\overset{\\sim}{D}{\\overset{\\sim}{C}}_{\\lambda}^{- 1}{({\\overset{\\sim}{C} - \\hat{C}})}{\\hat{C}}_{\\lambda}^{- 1}C^{1/2}}\\|}_{\\mathcal{G}_{n}}$", "weight": 1.0} -->

From Assumption (A4) (Attainability assumption). ‣ 4.1 𝐿² learning rates ‣ 4 Learning guarantees ‣ Learning Controlled Stochastic Differential Equations"), we have

<!-- chunk {"id": "body-0158", "role": "body", "section": "Bound ${\\|{\\overset{\\sim}{D}{\\overset{\\sim}{C}}_{\\lambda}^{- 1}{({\\overset{\\sim}{C} - \\hat{C}})}{\\hat{C}}_{\\lambda}^{- 1}C^{1/2}}\\|}_{\\mathcal{G}_{n}}$", "weight": 1.0} -->

Then, as for bound 2., from Lemma 7.12. ‣ Conclusion. ‣ 7.10 Auxiliary lemmas ‣ 7 Proofs ‣ Learning Controlled Stochastic Differential Equations") and Lemma 7.13. ‣ Conclusion. ‣ 7.10 Auxiliary lemmas ‣ 7 Proofs ‣ Learning Controlled Stochastic Differential Equations"), we have

<!-- chunk {"id": "body-0159", "role": "body", "section": "Bound ${\\|{\\overset{\\sim}{D}{\\overset{\\sim}{C}}_{\\lambda}^{- 1}{({\\overset{\\sim}{C} - \\hat{C}})}{\\hat{C}}_{\\lambda}^{- 1}C^{1/2}}\\|}_{\\mathcal{G}_{n}}$", "weight": 1.0} -->

where $c > 0$ is a constant that does not depend on $N,K,\delta$.

<!-- chunk {"id": "body-0160", "role": "body", "section": "Conclusion", "weight": 1.5} -->

Combining all bounds, we conclude that there exist constants ${c_{1},c_{2}} > 0$ that do not depend on $N,K,\delta$, such that, for any $\delta \in {(0,1\rbrack}$, with probability at least $1 - \delta$

<!-- chunk {"id": "body-0161", "role": "body", "section": "Bound ${\\|{C_{K,\\lambda}^{- {1/2}}{({\\overset{\\sim}{C} - C_{K}})}C_{K,\\lambda}^{- {1/2}}}\\|}_{\\infty}$", "weight": 1.0} -->

From Proposition 7.17. ‣ 7.11 Concentration inequalities ‣ 7 Proofs ‣ Learning Controlled Stochastic Differential Equations"), for any $\delta \in {(0,1\rbrack}$, with probability at least $1 - \delta$,

<!-- chunk {"id": "body-0162", "role": "body", "section": "Bound ${\\|{C_{K,\\lambda}^{- {1/2}}{({\\overset{\\sim}{C} - C_{K}})}C_{K,\\lambda}^{- {1/2}}}\\|}_{\\infty}$", "weight": 1.0} -->

and same proof as Proposition 7.17. ‣ 7.11 Concentration inequalities ‣ 7 Proofs ‣ Learning Controlled Stochastic Differential Equations") gives ${\|{C_{K} - C}\|}_{\infty} \leq {cK^{- {1/2}}{\log{({K\delta^{- 1}})}}}$ for a constant $c > 0$ that does not depend on $K,\delta$, if $K^{- 1} \leq \lambda \leq {\| C\|}_{\infty}$, such that

<!-- chunk {"id": "body-0163", "role": "body", "section": "Conclusion", "weight": 1.5} -->

We conclude by combining all bounds that there exist a constant $c > 0$ that does not depend on $N,K,\delta$, such that, for any $\delta \in {(0,1\rbrack}$, with probability at least $1 - \delta$

<!-- chunk {"id": "body-0164", "role": "body", "section": "Bound ${\\|{{({w_{K} - w_{\\lambda}})}C^{1/2}}\\|}_{\\mathcal{G}_{n}}$", "weight": 1.0} -->

Employing the same reasoning as in Lemma 7.8⁢𝐶^{1/2}‖_𝒢_𝑛). ‣ 7.8 Proof of Lemma 7.8 ‣ 7 Proofs ‣ Learning Controlled Stochastic Differential Equations"), there exists a constant $c > 0$ that does not depend on $K,\delta$, such that, for any $\delta \in {(0,1\rbrack}$, with probability at least $1 - \delta$

<!-- chunk {"id": "body-0165", "role": "body", "section": "Bound ${\\|{{({w_{\\lambda} - w})}C^{1/2}}\\|}_{\\mathcal{G}_{n}}$", "weight": 1.0} -->

From Assumption (A4) (Attainability assumption). ‣ 4.1 𝐿² learning rates ‣ 4 Learning guarantees ‣ Learning Controlled Stochastic Differential Equations"), we have

<!-- chunk {"id": "body-0166", "role": "body", "section": "Conclusion", "weight": 1.5} -->

We conclude by combining all bounds, that there exist a constant $c > 0$ that does not depend on $K,\delta$, such that, for any $\delta \in {(0,1\rbrack}$, with probability at least $1 - \delta$

<!-- chunk {"id": "body-0167", "role": "body", "section": "Auxiliary lemmas", "weight": 1.0} -->

This section presents auxiliary lemmas used in the proofs of the main lemmas, along with their proofs.

<!-- chunk {"id": "body-0168", "role": "body", "section": "Bound ${\\|{{\\hat{E}}_{1} - E_{1}}\\|}_{\\mathcal{G}_{n}}$", "weight": 1.0} -->

To apply Proposition 7.17. ‣ 7.11 Concentration inequalities ‣ 7 Proofs ‣ Learning Controlled Stochastic Differential Equations"), we define

<!-- chunk {"id": "body-0169", "role": "body", "section": "Bound ${\\|{{\\hat{E}}_{1} - E_{1}}\\|}_{\\mathcal{G}_{n}}$", "weight": 1.0} -->

Then, denoting $\varepsilon \triangleq {\sup_{k}{L{({\hat{p}}_{k},{p{(u_{k})}})}}}$, from Proposition 7.17. ‣ 7.11 Concentration inequalities ‣ 7 Proofs ‣ Learning Controlled Stochastic Differential Equations"), we have, for any $\delta \in {(0,1\rbrack}$, with probability at least $1 - \delta$,

<!-- chunk {"id": "body-0170", "role": "body", "section": "Bound ${\\|{{\\hat{E}}_{2} - E_{2}}\\|}_{\\mathcal{G}_{n}}$", "weight": 1.0} -->

To apply Proposition 7.17. ‣ 7.11 Concentration inequalities ‣ 7 Proofs ‣ Learning Controlled Stochastic Differential Equations"), we define

<!-- chunk {"id": "body-0171", "role": "body", "section": "Bound ${\\|{{\\hat{E}}_{2} - E_{2}}\\|}_{\\mathcal{G}_{n}}$", "weight": 1.0} -->

and, from Lemma 7.10-ϕ̂_𝑘⁢(𝑡,𝑥)‖_𝒢_𝑛²]). ‣ 7.10 Auxiliary lemmas ‣ 7 Proofs ‣ Learning Controlled Stochastic Differential Equations"), we obtain

<!-- chunk {"id": "body-0172", "role": "body", "section": "Bound ${\\|{{\\hat{E}}_{2} - E_{2}}\\|}_{\\mathcal{G}_{n}}$", "weight": 1.0} -->

Then, from Proposition 7.17. ‣ 7.11 Concentration inequalities ‣ 7 Proofs ‣ Learning Controlled Stochastic Differential Equations"), we have, for any $\delta \in {(0,1\rbrack}$, with probability at least $1 - \delta$,

<!-- chunk {"id": "body-0173", "role": "body", "section": "Conclusion", "weight": 1.5} -->

We conclude by combining all bounds that there exists a constant $c > 0$ that does not depend on $N,K,\delta$, such that, for any $\delta \in {(0,1\rbrack}$, with probability at least $1 - \delta$

<!-- chunk {"id": "body-0174", "role": "body", "section": "Concentration inequalities", "weight": 1.0} -->

In this section, we provide the concentration inequalities used in the lemmas' proofs.

<!-- chunk {"id": "body-0175", "role": "body", "section": "Concentration inequalities", "weight": 1.0} -->

The following inequality is essentally a restatement of Proposition 2 of Rudi and Rosasco.

<!-- chunk {"id": "body-0176", "role": "body", "section": "Value at Risk (VaR)", "weight": 1.0} -->

For any $\alpha \in {\lbrack 0,1\rbrack}$, the value at risk $VaR_{\alpha}{(X)}$ of a random variable $X:{\Omega\rightarrow{\mathbb{R}}}$ is defined as the smallest of the $\alpha \times 100$% worst (greatest) values of the distribution of $X$, namely

<!-- chunk {"id": "body-0177", "role": "body", "section": "Conditional Value at Risk (CVaR)", "weight": 1.0} -->

For any $\alpha \in {\lbrack 0,1\rbrack}$, the conditional value at risk of a variable $X:{\Omega\rightarrow{\mathbb{R}}}$ is defined as

<!-- chunk {"id": "body-0178", "role": "body", "section": "Conditional Value at Risk (CVaR)", "weight": 1.0} -->

When the cumulative distribution function of $X$ is continuous at $VaR_{\alpha}{(X)}$, it holds that

<!-- chunk {"id": "body-0179", "role": "body", "section": "Conditional Value at Risk (CVaR)", "weight": 1.0} -->

allowing to interpretate CVaR as the expected value conditional upon being within some percentage of the worst-case loss scenarios.

<!-- chunk {"id": "body-0180", "role": "body", "section": "Sobolev Spaces and regularity assumptions", "weight": 1.0} -->

where $\mathcal{K}_{\frac{m}{2} - q}$ is the modified Bessel function of the second kind, induces the RKHS $\mathcal{F} = {W^{q}{(\mathcal{Z})}}$, where $W^{q}{(\mathcal{Z})}$ denotes the Sobolev space of smoothness $q$. The source condition is verified for $\alpha = {\frac{s}{q} - 1}$, and the embedding property is verified for any parameter $r > {1 - \frac{m}{2q}}$. For more details, we refer the reader to Example 2 in Pillaud-Vivien et al., Section 4 in Fischer and Steinwart, and Wendland, Steinwart et al..

<!-- chunk {"id": "body-0181", "role": "body", "section": "Regularity of Fokker-Planck matching", "weight": 1.0} -->

The previous result on Sobolev RKHS is not directly applicable to our setting. The chosen hypothesis spaces $\mathcal{F}$ for the coefficients and $\mathcal{H}$ for the controls induce the hypothesis space $\mathcal{M}$ for the Fokker-Planck matching. More precisely,

<!-- chunk {"id": "body-0182", "role": "body", "section": "Regularity of Fokker-Planck matching", "weight": 1.0} -->

Nevertheless, the following lemma establishes the embedding property for Fokker-Planck matching when the coefficients belong to a Sobolev space, and the control spaces is smoothly parametrized.

<!-- chunk {"id": "body-0183", "role": "body", "section": "Implementation details of uncontrolled SDE estimation", "weight": 1.0} -->

This section details the implementation of the uncontrolled SDE estimation method proposed in Bonalli and Rudi, available on GitHub (lmotte/sde-learn) as an open-source Python library. We provide details on the computations involved, including vectorized versions for efficient computation with Python libraries such as NumPy, as well as the computational complexity of each step. In Section 8.1, we detail probability density estimation. In Section 8.2, Fokker-Planck matching is presented.

<!-- chunk {"id": "body-0184", "role": "body", "section": "Notations", "weight": 1.0} -->

and similar notations for the partial derivatives of $\hat{g}$ and $\rho$.

<!-- chunk {"id": "body-0185", "role": "body", "section": "Estimator closed-form", "weight": 1.0} -->

From Bonalli and Rudi, we have

<!-- chunk {"id": "body-0186", "role": "body", "section": "Step 1.1 ($\\hat{p}$ fitting)", "weight": 1.0} -->

The time and space complexities of this step are $\mathcal{O}{(M^{3})}$ and $\mathcal{O}{({M^{2} + {QMn}})}$, respectively.

<!-- chunk {"id": "body-0187", "role": "body", "section": "Solving the optimization problem", "weight": 1.0} -->

Given a p.d. kernel $k$ over ${\lbrack 0,T\rbrack} \times {\mathbb{R}}^{n}$, we consider the model

<!-- chunk {"id": "body-0188", "role": "body", "section": "Solving the optimization problem", "weight": 1.0} -->

Note the change of feature map $\overset{\sim}{\phi}$ compared to the non-uniform diffusion model where

<!-- chunk {"id": "body-0189", "role": "body", "section": "Solving the optimization problem", "weight": 1.0} -->

Strong duality guarantees solvability for $w \in \mathcal{G}^{n + 1}$ via

<!-- chunk {"id": "body-0190", "role": "body", "section": "Solving the optimization problem", "weight": 1.0} -->

and the optimal $\gamma \in {\mathbb{R}}^{n}$ is obtained by solving the dual problem

<!-- chunk {"id": "body-0191", "role": "body", "section": "Closed-form formula for ${\\hat{b}}_{pc},{\\hat{\\sigma}}_{pc}^{2}$ and $QP{(\\gamma)}$", "weight": 1.0} -->

where ${\hat{\sigma}}_{std}^{2}$ is the standard unconstrained ridge regression estimator, and

<!-- chunk {"id": "body-0192", "role": "body", "section": "Gram matrices computations", "weight": 1.0} -->

The term ${(\mathcal{L}_{t}^{b,\sigma})}^{\ast}\hat{p}$ involves second derivatives of $\sigma \times \hat{p}$, leading to the feature maps ${\overset{\sim}{\phi}}_{ij}$, which are sums of four terms each. Consequently, the evaluation of the scalar product between two feature map values results in a sum of 16 terms.

<!-- chunk {"id": "body-0193", "role": "body", "section": "$\\overset{\\sim}{K}$ computation", "weight": 1.0} -->

Denoting $\odot$ as the Hadamard product, and ${{A \odot B}C} \triangleq {A \odot {({BC})}}$, we have

<!-- chunk {"id": "body-0194", "role": "body", "section": "Step 2.1 ($(\\hat{b},{\\hat{\\sigma}}^{2})$ fitting)", "weight": 1.0} -->

From Sections 8.2.1 and 8.2.2, at fitting time, one needs to compute and store

<!-- chunk {"id": "body-0195", "role": "body", "section": "Step 2.1 ($(\\hat{b},{\\hat{\\sigma}}^{2})$ fitting)", "weight": 1.0} -->

The time and space complexities of this step are $\mathcal{O}{(N^{3})}$ and $\mathcal{O}{(N^{2})}$, respectively.

<!-- chunk {"id": "body-0196", "role": "body", "section": "Step 2.2 ($(\\hat{b},{\\hat{\\sigma}}^{2})$ predictions)", "weight": 1.0} -->

Then, predictions can be computed from the formulas provided in Section 7.3.

<!-- chunk {"id": "body-0197", "role": "body", "section": "Step 2.2 ($(\\hat{b},{\\hat{\\sigma}}^{2})$ predictions)", "weight": 1.0} -->

The time and space complexities of this step are $\mathcal{O}{({NN_{te}})}$ and $\mathcal{O}{({NN_{te}})}$, respectively.

<!-- chunk {"id": "body-0198", "role": "body", "section": "Outputs", "weight": 1.0} -->

We return the predicted SDE coefficients' values for the given test inputs.

<!-- chunk {"id": "body-0199", "role": "body", "section": "FP matching with Nyström approximation", "weight": 1.0} -->

Time and space complexities of Fokker-Planck matching can be reduced from $\mathcal{O}{(N^{3})}$ and $\mathcal{O}{(N^{2})}$ to $\mathcal{O}{({mN^{2}})}$ and $\mathcal{O}{({Nm})}$ by using Nyström approximation with $m$ anchors. More precisely, the Fokker-Planck matching objective with the Nyström approximation

<!-- chunk {"id": "body-0200", "role": "body", "section": "FP matching with Nyström approximation", "weight": 1.0} -->

and the following formula for the dual problem

<!-- chunk {"id": "body-0201", "role": "body", "section": "Implementation details of controlled SDE estimation", "weight": 1.0} -->

This section details the implementation of the controlled SDE estimation method proposed in this work, available on GitHub (lmotte/controlled-sde-learn) as an open-source Python library. We update the formulas and computational complexity of each step provided in Section for uncontrolled SDEs to adapt them for controlled SDEs.

<!-- chunk {"id": "body-0202", "role": "body", "section": "Step 1: probability density estimation", "weight": 1.0} -->

For controlled SDEs, the estimation of the probability density function involves repeating the algorithm from Step 1 of the uncontrolled case $K$ times. Each iteration corresponding to a specific control setting. At the end of this step, we have computed and stored

<!-- chunk {"id": "body-0203", "role": "body", "section": "Step 1: probability density estimation", "weight": 1.0} -->

and also the partial derivatives evaluations.

<!-- chunk {"id": "body-0204", "role": "body", "section": "Step 2: Fokker-Planck matching", "weight": 1.0} -->

Same algorithm but adding additional dimensions for the controls. More precisely, closed-form are updated with $z = {(t,x,v)} \in {{\lbrack 0,T\rbrack} \times {\mathbb{R}}^{n} \times {\mathbb{R}}^{d}}$ instead of $z = {(t,x)} \in {{\lbrack 0,T\rbrack} \times {\mathbb{R}}^{n}}$. We store
