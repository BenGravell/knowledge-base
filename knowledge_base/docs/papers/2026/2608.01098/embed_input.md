<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Fundamental Limitations of Data-Driven Control: A Statistical Decision Perspective

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Substantial research efforts have been devoted to the design of data-driven controllers; however, comparatively less is known about their statistical performance and fundamental limitations. This contribution develops a statistical decision framework for data-driven control, in which a controller is evaluated by its risk, defined as the expected performance degradation relative to the oracle model-based controller, and by its average risk over the parameter space. Within this framework, we propose a collection of design principles for data-driven controllers. We further derive lower bounds on risks by combining the bias-variance decomposition with the Cramér-Rao inequality. In particular, the optimal bias that attains the lower bound for the average risk is determined by calculus of variations, thereby making the bias-variance tradeoff in data-driven control explicit. Moreover, the derived bound reveals a ``waterbed'' effect in data-driven control: any improvement in risk relative to the lower bound over one region of the parameter space must be compensated by deterioration elsewhere. We illustrate the proposed framework on two canonical data-driven control problems: optimal feedforward control and the linear quadratic regulator benchmark.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

By comparing several representative data-driven controllers with the derived lower bounds, we sharpen the statistical interpretation of existing methods and reveal quantitative limitations that no controller design can avoid.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

Data-driven control, the task of designing controllers directly from process data, arises in a wide range of disciplines and has been studied for more than half a century. Early research paradigms include Iterative Feedback Tuning, correlation-based approaches, and Virtual Reference Feedback Tuning; approaches that blend identification and control, such as dual control, and identification for control; and many others. We refer to the survey for an earlier overview of these developments. Recently, the area has witnessed a renewed surge of interest, driven by advances at the intersection of control, learning, optimization and related fields. Among recent developments, two canonical benchmark problems have attracted considerable attention: data-driven model predictive control (MPC) and linear quadratic regulator (LQR). In data-driven MPC, Willems' behavioral framework has been leveraged, where collected input-output trajectories are incorporated into the constraints together with regularization terms in the control objective. The subspace predictive control has been further developed. Recently, it has been shown that the behavioral and model-based approaches can be unified in a Bayesian framework.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

For data-driven LQR, representative contributions include reinforcement learning methods, robust design, certainty-equivalence (CE) method, data informativity, direct data-driven methods, and Bayesian method. We refer to the double special issues for many more contributions.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

Despite the broad and rapidly growing literature on data-driven control, most existing works focus on the design and analysis of particular controllers. Comparisons between different data-driven control methods often still lead to the answer "it depends", as noted; consequently, determining which method should be preferred remains a nontrivial question. In theoretical analyses and numerical case studies, the advantage of one method over another is often demonstrated by showing that its performance is closer to that of the optimal model-based controller. This motivates us to raise a more foundational question: is there a limit to how close any data-driven controller can get to this ideal performance benchmark? Answering this question is important, because such a limit points directly to the inescapable hardness of the problem, thereby clarifying what is achievable, and conversely what is not achievable, in data-driven control.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

This work addresses the above problem by formulating offline data-driven control as a statistical decision problem. A data-driven controller is viewed as a decision rule constructed from data, and its performance is assessed by a risk measure: the expected deterioration in performance relative to the oracle model-based controller. We further introduce the average risk, which aggregates this deterioration over the parameter space of interest. Within this framework, lower bounds on risks are derived. Since these bounds are independent of any particular design method, they serve as benchmarks for practical algorithms. Moreover, they reveal how the intrinsic difficulty of the problem is shaped by both the system under study and the information contained in data.

<!-- chunk {"id": "body-0008", "role": "body", "section": "I-A Related Work", "weight": 1.0} -->

Although fundamental limitations are well established in classical model-based control, the limits on data-driven control are less studied. Recent statistical analyses of data-driven control have studied stability and robustness guarantees, suboptimality bounds, and CE principle for data-driven MPC; suboptimality bounds, convergence, consistency, and sample complexity for data-driven LQR and LQG; relations between direct and indirect data-driven control methods, and what type of linear systems are hard to learn and control.

<!-- chunk {"id": "body-0009", "role": "body", "section": "I-A Related Work", "weight": 1.0} -->

From the perspective of statistical decision theory, data-driven control closely resembles classical point estimation: in both cases, one infers quantities of interest from data and then makes decisions based on that information. This analogy has already influenced several developments in data-driven control. For instance, motivated in part by advances in regularized parameter estimation, model kernels that account for the expected deterioration in control performance have been proposed; see also for a broader discussion of regularization in data-driven control. Another line of work addresses noisy data through an average-risk framework, leading to what may be termed Bayes control methods. Meanwhile, fundamental limitations of point estimation are well established. A standard approach is to combine the bias-variance decomposition with the Cramér-Rao lower bound (CRLB) on the variance, which leads to global Cramér--Rao bounds and related Bayesian bounds. These developments suggest that tools from statistical decision theory may provide a principled way to study not only the design of data-driven controllers, but also their fundamental limitations. A recent step in this direction was taken, which proposed a bias-variance perspective on data-driven control. There, the bias and variance terms quantify the increase in control cost due to systematic error and controller variability, respectively.

<!-- chunk {"id": "body-0010", "role": "body", "section": "I-A Related Work", "weight": 1.0} -->

Moreover, lower bounds on the regret of online LQR were derived, and local minimax lower bounds for offline LQR and LQG were given in and, respectively. Compared with these works, this paper studies global lower bounds for data-driven control in a more general statistical decision framework. Moreover, we characterize the optimal bias that attains the lower bound for the average risk, thereby making the bias-variance tradeoff in data-driven control explicit.

<!-- chunk {"id": "body-0011", "role": "body", "section": "I-B Contributions", "weight": 1.0} -->

The main contributions of this paper are four-fold: \(1\) We introduce a general analysis framework for data-driven control from the perspective of statistical decision theory, in which a collection of decision rules for data-driven control is developed.

<!-- chunk {"id": "body-0012", "role": "body", "section": "I-B Contributions", "weight": 1.0} -->

\(2\) By combining the bias-variance decomposition with the CRLB, we derive fundamental lower bounds for data-driven control in a dynamical system setting. In particular, we formulate the problem of lower bounding the average risk as a calculus of variations problem, which can be further cast as an ordinary differential equation (ODE) boundary value problem. The resulting solution yields a tight lower bound and characterizes the bias function when the bound is attained, thus making the bias-variance tradeoff in data-driven control explicit.

<!-- chunk {"id": "body-0013", "role": "body", "section": "I-B Contributions", "weight": 1.0} -->

\(3\) A ''waterbed'' effect: Our results suggest that, for a data-driven controller, any reduction in risk relative to the lower bound in one region of the parameter space must be compensated by increased risk elsewhere. We refer to this phenomenon as a ''waterbed'' effect^11^ 1 An analogous limitation is well known in control theory: Bode's sensitivity integral shows that reductions in sensitivity over certain frequency ranges must be compensated by increased sensitivity elsewhere..

<!-- chunk {"id": "body-0014", "role": "body", "section": "I-B Contributions", "weight": 1.0} -->

\(4\) We apply the proposed framework to derive lower bounds for two canonical data-driven control problems: optimal feedforward control and the benchmark LQR. These bounds reveal quantitative limitations that no controller design can avoid and serve as benchmark for interpreting existing methods. Comparisons with several representative controllers show, in particular, that Bayesian methods are especially effective in approaching the lower bound on the average risk, in line with recent work.

<!-- chunk {"id": "body-0015", "role": "body", "section": "I-C Structure", "weight": 1.0} -->

The remainder of this paper is structured as follows: Section II introduces a statistical decision framework, in which a collection of decision rules is presented. Section III describes a dynamical system setting for data-driven control. Section IV develops lower bounds for risks of data-driven control. In two parallel Sections V and VI, we apply the proposed framework to two data-driven control tasks: the optimal feedforward control problem and the LQR problem, respectively. Finally, this paper is concluded in Section VII.

<!-- chunk {"id": "body-0016", "role": "body", "section": "II-A Design Principles", "weight": 1.0} -->

In this subsection we outline some basic principles for constructing data-driven decision rules. We let $\mathcal{D}_{h}$ be the set of decision rules that we can choose. Central to all techniques is that they aim at making the risk small but that they handle the fact that $\theta$ is unknown in different ways.

<!-- chunk {"id": "body-0017", "role": "body", "section": "II-A1 Unbiased Decision Rules", "weight": 1.0} -->

An unbiased decision rule $\hat{h}_{\text{UB}}$ is defined by For certain families of distributions it is possible to derive an optimal unbiased decision rule, called the uniformly minimum risk unbiased decision rule, within this class.

<!-- chunk {"id": "body-0018", "role": "body", "section": "II-A2 Maximum Likelihood (ML) Decision Rules", "weight": 1.0} -->

The well-known ML estimate of $\theta$ is given by By defining a likelihood function for the optimal decision $h(\theta)$, one may generalize from the ML estimate to a decision rule. We follow the approach in for such a generalization, where a likelihood function for a given value $\eta\in\mathcal{D}_{h}$ of $h(\theta)$ is defined by We call $p_{\text{M}}$ the max-likelihood and define the maximum max-likelihood decision rule for $h(\theta)$ as Since $\hat{\theta}_{\text{ML}}(Z)$ is the ML estimator of $\theta$, for any $\eta\in\mathcal{D}_{h}$ we have $p_{\text{M}}(Z;\eta)\leq p(Z;\hat{\theta}_{\text{ML}}(Z))$.

<!-- chunk {"id": "body-0019", "role": "body", "section": "II-A3 Loss and Certainty-Equivalence (CE) Tuning", "weight": 1.0} -->

Another approach is to estimate the loss function $L_{\theta}$, which is unknown due to its dependency on $\theta$, and choose the parameter that minimizes the estimated loss. The most straightforward way to estimate the loss is to replace the unknown $\theta$ in the loss $L_{\theta}$ by an estimate $\hat{\theta}(Z)$ and then in the given family $\mathcal{D}_{h}$ of decisions pick When the decision rule $h(\hat{\theta}(Z))$ is included in $\mathcal{D}_{h}$, this will result in the decision This approach is commonly known as the CE principle since it uses the parameter estimate as if it is the true value in the optimal decision rule.

<!-- chunk {"id": "body-0020", "role": "body", "section": "II-A3 Loss and Certainty-Equivalence (CE) Tuning", "weight": 1.0} -->

Comparing (12 Tuning ‣ II-A Design Principles ‣ II Preliminaries on Statistical Decision Theory ‣ Fundamental Limitations of Data-Driven Control: A Statistical Decision Perspective")) with (10 Decision Rules ‣ II-A Design Principles ‣ II Preliminaries on Statistical Decision Theory ‣ Fundamental Limitations of Data-Driven Control: A Statistical Decision Perspective")) we see that using the ML estimate of $\theta$ results in the ML estimate of $h(\theta)$, i.e., $\hat{h}_{\text{CE}(\hat{\theta}_{\text{ML}})}(Z)=h(\hat{\theta}_{\text{ML}}(Z))$.

<!-- chunk {"id": "body-0021", "role": "body", "section": "II-A4 (Weighted) Average Risk Tuning", "weight": 1.0} -->

A way to bypass the problem that the loss and risk functions that we would like to minimize are functions of $\theta$ is to instead replace the loss by its average in the $\theta$-domain. This leads naturally to the average risk $r(\hat{h})$ defined. Interchanging the order of integration gives Hence, for each fixed observation $z$, we are led to minimize Let $\hat{h}_{A(P)}(z)$ denote the minimizer of $V_{z}(\hat{h})$, where the subscript $A$ stands for the average risk minimization and $P$ has the origin in the Pitman estimator. Since $\hat{h}_{A(P)}(z)$ minimizes the integrand pointwise in $z$, the resulting rule $\hat{h}_{A(P)}$ minimizes the average risk $r(\hat{h})$.

<!-- chunk {"id": "body-0022", "role": "body", "section": "II-A4 (Weighted) Average Risk Tuning", "weight": 1.0} -->

For the quadratic loss $L_{\theta}(\hat{h})$, the unconstrained minimizer takes the form It should be mentioned that to compute $\hat{h}_{A(P)}(z)$, the integrals $\overline{W}(z)$ and $\overline{H}(z)$ have to be computed, which in general is intractable and requires sampling methods.

<!-- chunk {"id": "body-0023", "role": "body", "section": "II-A4 (Weighted) Average Risk Tuning", "weight": 1.0} -->

By the same argument as the average risk $r(\hat{h})$ where $\pi\equiv 1$, the minimizer of the general $r_{\pi}(\hat{h})$, denoted by $\hat{h}_{A(\pi)}(z)$, can be derived in a similar form to (15 Average Risk Tuning ‣ II-A Design Principles ‣ II Preliminaries on Statistical Decision Theory ‣ Fundamental Limitations of Data-Driven Control: A Statistical Decision Perspective")).

<!-- chunk {"id": "body-0024", "role": "body", "section": "II-A5 Composite Methods", "weight": 1.0} -->

In statistical decision theory, additional design principles such as minimax and risk tuning methods may also be considered. Together with the four families of methods introduced above, these can be combined to form a broad class of composite methods. The basic idea is to use one method to construct an intermediate parameter estimate or decision rule, and then use this as input to another method. Altogether, this shows that the different method families are not isolated alternatives, but can be combined in many ways to construct decision rules.

<!-- chunk {"id": "body-0025", "role": "body", "section": "II-B An Illustrative Example: Point Estimation", "weight": 1.0} -->

The main objective of this work is to derive lower bounds on the pointwise risk $R_{\theta}(\hat{h})$ and the average risk $r(\hat{h})$ for data-driven control problems in a dynamical system setting. Before turning to this control problem, we first revisit related results in a classical point estimation problem. This simpler setting provides a useful preview of the results that will later arise, in an analogous form, in data-driven control.

<!-- chunk {"id": "body-0026", "role": "body", "section": "II-B An Illustrative Example: Point Estimation", "weight": 1.0} -->

The loss of an estimator $\hat{\theta}$ is taken as $L_{\theta}(\hat{\theta})=\big(\hat{\theta}-\theta\big)^{2}$. Then, the corresponding risk $R_{\theta}(\hat{h})$ and the average risk $r(\hat{h})$ can be defined as in and, respectively.

<!-- chunk {"id": "body-0027", "role": "body", "section": "II-B An Illustrative Example: Point Estimation", "weight": 1.0} -->

Using Theorems IV.1 and IV.2 in this work (to be presented later in Section IV), we obtain that for any estimator, the average risk $r(\hat{\theta})$ over the interval $\mathcal{D}_{\theta}=[-L,L]$ is lower bounded by where $b_{\theta}^{*}=-\sigma_{z}\frac{\sinh(\frac{\theta}{\sigma_{z}})}{\cosh(\frac{\theta}{\sigma_{z}})}$ is the optimal bias that attains the lower bound, and $(b_{\theta}^{*})^{\prime}$ is its derivative w.r.t. $\theta$. The point estimation bound appeared in and is recovered here as a special case of Theorems IV.1 and IV.2.

<!-- chunk {"id": "body-0028", "role": "body", "section": "II-B An Illustrative Example: Point Estimation", "weight": 1.0} -->

Fig. 1: Risks Rθ(θ̂) of the three estimators over the interval [−1, 1]: the average risks of θ̂ML, θ̂0, and θ̂Bayes are 1.0, 0.667, and 0.392, respectively. The lower bound, shown by the hatched red region, is 0.372. Moreover, the optimal squared bias and variance associated with f(θ, σz), the integrand, are given.

<!-- chunk {"id": "body-0029", "role": "body", "section": "Dynamical System Setting", "weight": 1.0} -->

We are now prepared to consider a dynamical system setting. We denote the input and output of a dynamical system by $u(t)$ and $y(t)$, respectively. The observed output/input signal sequence that is available for data-driven control will be denoted by $Z^{N}=\{y(t),u(t)\}_{t=1}^{N}$. In a general form, the data is assumed to be generated as where $g_{t}(\cdot)$ is a deterministic function, $\{e(t)\}_{t=1}^{N}$ is a sequence of independent random vectors with pdfs $p_{t}(e)$ and has a zero mean, and $Z^{t-1}$ represents all past output/input data up to the time $t-1$.

<!-- chunk {"id": "body-0030", "role": "body", "section": "Dynamical System Setting", "weight": 1.0} -->

Using the chain rule of probability, together with the independence of the innovations, we obtain where $\varepsilon_{t}(Z^{t};\theta):=y(t)-g_{t}(Z^{t-1};\theta)$ denotes the one-step prediction error induced by $\theta$. Using we can define the log-likelihood function and the score function, as with $\Psi_{t}(Z^{t-1};\theta):=\frac{\partial}{\partial\theta}\varepsilon_{t}(Z^{t};\theta)$.

<!-- chunk {"id": "body-0031", "role": "body", "section": "Dynamical System Setting", "weight": 1.0} -->

To specify the conditions on $\{g_{t}\}$ and $\{p_{t}\}$, we will use the exponential forgetting framework in Ljung's seminal work. We will follow the version in which employs more flexible conditions than those.

<!-- chunk {"id": "body-0032", "role": "body", "section": "Assumption III.1", "weight": 1.0} -->

The Fisher information matrix is well defined, i.e., $I_{F,N}(\theta)\succ 0$.

<!-- chunk {"id": "body-0033", "role": "body", "section": "Assumption III.1", "weight": 1.0} -->

This assumption is standard in the literature. In particular, it is satisfied when $\{y(t)\}_{t=1}^{\infty}$ in is EF of order $q\cdot\gamma$, with $q>1$ and $\gamma>2$, and the family $\{p_{t}(\cdot;\theta):\theta\in\mathcal{D}_{\theta},\,t\in T=\mathbb{N}_{N}\}$ satisfies some regularity conditions (see ).

<!-- chunk {"id": "body-0034", "role": "body", "section": "Assumption III.1", "weight": 1.0} -->

Having specified the dynamical system setting and the data-generating mechanism, we now are ready to study the performance limits of data-driven control.

<!-- chunk {"id": "body-0035", "role": "body", "section": "Risk Lower Bounds in Data-Driven Control", "weight": 1.0} -->

In the point estimation problem reviewed in Section II, the lower bound for the average risk $r(\hat{\theta})$ is established using the celebrated CRLB. In this section, we extend this idea to data-driven control, where the target is not the parameter $\theta$ itself, but a general function $h(\theta)$, representing the optimal model-based controller.

<!-- chunk {"id": "body-0036", "role": "body", "section": "IV-A Lower Bound for the Pointwise Risk", "weight": 1.0} -->

We have the following lower bound on the pointwise risk $R_{\theta}(\hat{h})$ for data-driven control.

<!-- chunk {"id": "body-0037", "role": "body", "section": "IV-B Optimal-Bias Lower Bound for the Average Risk", "weight": 1.0} -->

Based, a lower bound on the average risk $r(\hat{h})$ can be obtained by minimizing its right-hand side over all admissible bias functions. To this end, define the functional Then the corresponding functional minimization problem is The solution to provides a lower bound on the average risk $r(\hat{h})$ for any data-driven controller $\hat{h}$. Here, $F(b_{\theta})$ is the cost functional, and $f(\theta,b_{\theta},b_{\theta}^{\prime})$ is the Lagrangian, viewed as a function of three independent variables $\theta$, $b_{\theta}$, and $b_{\theta}^{\prime}$. The functional minimization problem in is precisely a calculus of variations problem, a framework that has long played a central role in both point estimation and optimal control. To the best of our knowledge, however, this is the first time such a tool has been used to derive fundamental limitations in data-driven control problems.

<!-- chunk {"id": "body-0038", "role": "body", "section": "IV-B Optimal-Bias Lower Bound for the Average Risk", "weight": 1.0} -->

Solving the variational problem yields a sharp CRLB-based lower bound on the average risk, and determines the optimal bias that attains this bound. As in point estimation, the optimal bias makes the bias-variance tradeoff in data-driven control transparent by showing how risk is balanced between the two terms.

<!-- chunk {"id": "body-0039", "role": "body", "section": "IV-B Optimal-Bias Lower Bound for the Average Risk", "weight": 1.0} -->

In order to characterize the solutions of this functional minimization problem through optimality conditions, we first introduce some necessary differentiability assumptions.

<!-- chunk {"id": "body-0040", "role": "body", "section": "Assumption IV.2", "weight": 1.0} -->

The bias $b_{\theta}$ is twice continuously differentiable.

<!-- chunk {"id": "body-0041", "role": "body", "section": "Remark 1", "weight": 1.0} -->

The above assumptions ensure that all derivatives appearing in the subsequent analysis are continuous. Although they can be further relaxed, to streamline the presentation we do not attempt to state the weakest possible regularity conditions. For related discussions, see.

<!-- chunk {"id": "body-0042", "role": "body", "section": "Remark 1", "weight": 1.0} -->

Since the Fisher information $I_{F,N}(\theta)$ and the weighting $W(\theta)$ are positive definite, the Lagrangian function $f(\theta,b_{\theta},b_{\theta}^{\prime})$ is strictly convex in $(b_{\theta},b_{\theta}^{\prime})$ for every $\theta\in\mathcal{D}_{\theta}$. Then, we have the following theorem regarding the minimizer of the variational problem.

<!-- chunk {"id": "body-0043", "role": "body", "section": "Case Study I: Optimal Feedforward Control", "weight": 1.0} -->

We begin with a simple feedforward control problem to illustrate the implications of our framework in a transparent setting. Although this example does not involve a dynamical system, it has bearings to state-of-the-art. In fact, the optimal feedforward control corresponds to one-step predictive control treated. Moreover, its simplicity allows the fundamental limitations to be seen more clearly, thereby providing useful intuition for dynamical systems considered later.

<!-- chunk {"id": "body-0044", "role": "body", "section": "V-A Problem Formulation", "weight": 1.0} -->

Consider a scalar model $y=\theta u+e$, where $e\sim\mathcal{N}$, and the domain of interest is given by $\mathcal{D}_{\theta}=[\theta_{\text{min}},\theta_{\text{max}}]$. Suppose that $r$ is the desired noise free output and that the objective is to design $u$ such that $y$ is close to $r$. However, we do not want to use a too large input $u$, we therefore use a quadratic cost to determine $u$, which is given by where the second term, which penalizes large inputs, can be tuned with the parameter $\lambda>0$. The optimal controller is given by $u=h(\theta)=\frac{\theta}{\lambda+\theta^{2}}r$. Now define a quadratic cost for the data-driven controller, which is where we choose the weighting $W(\theta)=\lambda+\theta^{2}$.

<!-- chunk {"id": "body-0045", "role": "body", "section": "V-A Problem Formulation", "weight": 1.0} -->

Based on the loss above, the corresponding risk $R_{\theta}(\hat{h})$ and the average risk $r(\hat{h})$ can be defined as in and, respectively.

<!-- chunk {"id": "body-0046", "role": "body", "section": "V-A Problem Formulation", "weight": 1.0} -->

Based on design principles introduced in Section II, we next develop several data-driven controllers for this problem, where data is given by the observation $z=y$, which is a realization of the random variable $Z\sim\mathcal{N}(\theta,1)$. Moreover, the Fisher information $I_{F}=1$.

<!-- chunk {"id": "body-0047", "role": "body", "section": "V-B Design of Data-Driven Feedforward Controllers", "weight": 1.0} -->

We consider four controllers for comparison.

<!-- chunk {"id": "body-0048", "role": "body", "section": "V-B Design of Data-Driven Feedforward Controllers", "weight": 1.0} -->

The first one is the CE controller $\hat{h}_{\text{CE}(\hat{\theta}_{\text{ML}})}$, obtained by replacing the true parameter $\theta$ in the optimal controller $h(\theta)$ with its ML estimator ${\hat{\theta}}_{\text{ML}}=z$, giving The second one is the average risk tuning controller ${\hat{h}}_{A(P)}(z)$ in (15 Average Risk Tuning ‣ II-A Design Principles ‣ II Preliminaries on Statistical Decision Theory ‣ Fundamental Limitations of Data-Driven Control: A Statistical Decision Perspective")), which is known to minimize the average risk $r(\hat{h})$.

<!-- chunk {"id": "body-0049", "role": "body", "section": "V-B Design of Data-Driven Feedforward Controllers", "weight": 1.0} -->

To be specific, ${\hat{h}}_{A(P)}(z)$ is given by The third one is the weighed average risk tuning controller ${\hat{h}}_{A(\pi)}(z)$, where the weighting $\pi(\theta)$ is the pdf of Gaussian distribution $\mathcal{N}(0,\tau^{-1})$, with $\tau>0$. Then, it is easy to show that the controller ${\hat{h}}_{A(\pi)}(z)$ takes the form which corresponds to $h(\hat{\theta}_{\text{ML}}(z))$ where the penalty $\lambda$ in has been replaced by $\lambda+\frac{1}{1+\tau}$. We can interpret this as adding an information-dependent penalty on the control input: the less information is available, the larger the additional penalty is, i.e., a less certain control is more cautious.

<!-- chunk {"id": "body-0050", "role": "body", "section": "V-B Design of Data-Driven Feedforward Controllers", "weight": 1.0} -->

Note that the controllers in and both take the form where $c\in\mathbb{R}$ is a hyperparameter to be tuned. A natural way to choose $c$ is to minimize the average risk of $\hat{h}_{c}(Z)$ over $D_{\theta}$ w.r.t. $c$, that is, This minimization is carried out numerically and the resulting controller is used as the fourth controller, denoted by $\hat{h}_{c}$.

<!-- chunk {"id": "body-0051", "role": "body", "section": "V-C Calculating the Lower Bound for Feedforward Control", "weight": 1.0} -->

We now derive the optimal-bias lower bound on the average risk $r(\hat{h})$. Using the CRLB in Theorem IV.1, we have that where $f\bigl(\theta,b_{\theta},b_{\theta}^{\prime}\bigr)=b_{\theta}^{2}W(\theta)+W(\theta)(b_{\theta}^{\prime}+\frac{\lambda-\theta^{2}}{(\lambda+\theta^{2})^{2}}r)^{2}$. For this scalar case, the Euler-Lagrange equation reduces to and the natural boundary condition reduces to respectively. By numerically solving the Euler-Lagrange equation subject to the boundary condition, we obtain both the lower bound for the average risk and the optimal bias that attains this bound. The results are shown in the sequel.

<!-- chunk {"id": "body-0052", "role": "body", "section": "V-D Simulation Results", "weight": 1.0} -->

We now evaluate the performance of data-driven controllers introduced above against the lower bound for the average risk. We fix $\lambda=5$, the reference $r=1$, and let $\theta$ vary over $\mathcal{D}_{\theta}=$. For the third controller $\hat{h}_{A(\pi)}(z)$, we take $\tau=1$ in the weighting $\pi(\theta)$. For the fourth controller $\hat{h}_{c}(z)$, using a numerical minimization procedure, we obtain the optimal value $c=7.31$. For each fixed $\bar{\theta}$ in $\mathcal{D}_{\theta}$, we perform 100 Monte Carlo simulations to approximate the pointwise risk $R_{\theta}(\hat{h})$ for each controller.

<!-- chunk {"id": "body-0053", "role": "body", "section": "V-D Simulation Results", "weight": 1.0} -->

Fig. 2: Risks of the four controllers. The average risks of ĥCE, ĥA(π), ĥc and ĥA(P) are 0.178, 0.173, 0.163, and 0.039 respectively. The lower bound (hatched red region) is 0.038.

<!-- chunk {"id": "body-0054", "role": "body", "section": "V-D Simulation Results", "weight": 1.0} -->

Fig. 3: Bias-variance tradeoff in feedforward control Figure 3 shows the bias component $(b_{\theta}^{*})^{2}W(\theta)$ and the surrogate variance component $W(\theta)\bigl((b_{\theta}^{*})^{\prime}+h^{\prime}(\theta)\bigr)^{2}I_{F}^{-1}$ appearing in $f(\theta,b_{\theta}^{*},(b_{\theta}^{*})^{\prime})$. These two components exhibit the same rise-fall behavior observed in the point estimation example (see Figure 1). In regions where the variance lower bound decreases, the squared bias term increases, and vice versa. This clearly shows that there is also a bias-variance tradeoff in data-driven control.

<!-- chunk {"id": "body-0055", "role": "body", "section": "V-D Simulation Results", "weight": 1.0} -->

Before leaving this section, let us remark that, even if extremely simplified, this case study illustrates a fundamental trade-off in data-driven control: any reduction in risk relative to the lower bound over one region of the parameter space must be accompanied by an increase in risk elsewhere, analogous to the "waterbed" effect we introduced for point estimation. They also highlight the importance of evaluating how controller performance varies across the parameter space. Comparisons with several representative controllers show that the average risk minimization method is especially effective in approaching the lower bound, in line with recent Bayesian methods.

<!-- chunk {"id": "body-0056", "role": "body", "section": "Case Study II: LQR", "weight": 1.0} -->

We now show how our framework can be applied in data-driven control of dynamical systems. In particular, we consider data-driven LQR, a benchmark problem that has received considerable attention in recent years.

<!-- chunk {"id": "body-0057", "role": "body", "section": "VI-A Problem Formulation", "weight": 1.0} -->

Given a discrete-time linear time-invariant (LTI) system where $x_{k}\in\mathbb{R}^{n_{x}}$, $u_{k}\in\mathbb{R}^{n_{u}}$, and $e_{k}\in\mathbb{R}^{n_{x}}$ are the system state, input and noise at time $k$, respectively. We assume that $(A,B)$ is stabilizable and $A$ is Schur stable.

<!-- chunk {"id": "body-0058", "role": "body", "section": "VI-A Problem Formulation", "weight": 1.0} -->

The standard LQR problem for the system is where the weighting matrices $Q\succ 0$, $R\succ 0$, and the expectation is over the randomness from the initial state $x_{0}$ and the noise $e_{k}$. When system matrices $A$ and $B$ are known, this LQR problem can be solved by finding the positive definite solution $P$ to the discrete-time algebraic Riccati equation Then, the solution of is $u_{k}=-Kx_{k}$ with the optimal state feedback gain given by Alternatively, following this optimal controller can be determined by solving the following program: which can be further cast into a convex SDP after a change of variables; see \[25, Section III-C\].

<!-- chunk {"id": "body-0059", "role": "body", "section": "VI-A Problem Formulation", "weight": 1.0} -->

The data-driven LQR problem considers the case that system matrices $A$ and $B$ are unknown, while a batch of data generated by the system is available. In this work, we assume that the data is generated as follows: $e_{k}\sim\mathcal{N}(0,\sigma_{e}^{2}I_{n_{x}})$ are independent and identically distributed (i.i.d.), $u_{k}\sim\mathcal{N}(0,\sigma_{u}^{2}I_{n_{u}})$ are i.i.d., and $x_{0}\sim\mathcal{N}(0,\sigma_{0}^{2}I_{n_{x}})$. In addition, $x_{0}$, $\{e_{k}\}$ and $\{u_{k}\}$ are mutually independent.

<!-- chunk {"id": "body-0060", "role": "body", "section": "VI-A Problem Formulation", "weight": 1.0} -->

Let us introduce the data matrices constructed from a trajectory collected over a horizon $N$: Before introducing the controller design, we formulate the data-driven LQR into the general framework in Section II. To this end, we first introduce the following lemma.

<!-- chunk {"id": "body-0061", "role": "body", "section": "VI-B Design of Data-Driven LQR", "weight": 1.0} -->

By the linear dynamics, system matrices can be expressed in a linear regression form where $Z^{N}=[(U_{0}^{N})^{\top}\ (X_{0}^{N})^{\top}]^{\top}$, and $E_{0}^{N}$ stacks the noise sequence, defined analogously to the data matrices. Throughout this section, we assume that the data matrix $Z^{N}$ is full row rank, which is a necessary condition for data-driven LQR.

<!-- chunk {"id": "body-0062", "role": "body", "section": "VI-B Design of Data-Driven LQR", "weight": 1.0} -->

We first consider the indirect CE controller. The usual ML estimator for system matrices is given by By replacing the unknown parameter $\theta$ in the Riccati equation with $\hat{\theta}_{\text{ML}}$, solving for the corresponding matrix $\hat{P}$, and then substituting $\hat{P}$ into, we obtain the CE controller $\hat{h}_{\text{CE}(\hat{\theta}_{\text{ML}})}=h(\hat{\theta}_{\text{ML}})$. According to, given that $\hat{\theta}_{\text{ML}}$ is consistent and asymptotically efficient, $h(\hat{\theta}_{\text{ML}})$ is also asymptotically efficient. Moreover, recent works have provided finite-sample analysis for $\hat{\theta}_{\text{ML}}$ and $h(\hat{\theta}_{\text{ML}})$.

<!-- chunk {"id": "body-0063", "role": "body", "section": "VI-B Design of Data-Driven LQR", "weight": 1.0} -->

The second family of controllers we introduce is the so called direct data-driven LQR methods, which use data to synthesize a controller without explicitly identifying system matrices. There are many variants of direct data-driven LQR in the recent literature; see, for example,. We here highlight several representative milestones for comparison.

<!-- chunk {"id": "body-0064", "role": "body", "section": "VI-B Design of Data-Driven LQR", "weight": 1.0} -->

One of the earliest methods in this line of work appears, which is able to recover the optimal gain $K$ exactly in the absence of noise. However, recent work \[35, Th. 2\] shows that the resulting controller is not a consistent estimator of $K$ under noisy data unless suitably regularized with a data-size dependent regularization coefficient. It was later shown in that the indirect and direct methods can be viewed within a unified framework, which leads to the following regularized formulation: where $\Pi=I_{N}-(Z^{N})^{\dagger}Z^{N}$. Let $Y_{R}$ be the optimal solution of. The resulting controller is then given by According to, the regularization term $\lambda_{1}\|\Pi Y\|$ reflects a least-squares data-fitting criterion. When $\lambda_{1}=0$, reduces to the method in \[22, Th.

<!-- chunk {"id": "body-0065", "role": "body", "section": "VI-B Design of Data-Driven LQR", "weight": 1.0} -->

4\]; when the regularization parameter $\lambda_{1}$ is sufficiently large, it coincides with $h(\hat{\theta}_{\text{ML}})$.

<!-- chunk {"id": "body-0066", "role": "body", "section": "VI-B Design of Data-Driven LQR", "weight": 1.0} -->

Recently, a covariance-parameterized LQR formulation was proposed, followed by a regularized variant, where the regularization term accounts for uncertainty in both the steady-state covariance and the LQR objective. Very recently, using the same covariance parameterization as, a direct Bayesian LQR method was proposed in following the procedure. In this approach, posterior uncertainty is propagated into the control design through a variance-based regularization term. Specifically, system matrices $B$ and $A$ are assigned a matrix-normal prior $\pi$ with mean $\bar{B}$ and $\bar{A}$ and covariance $\Omega^{-1}$. Given the data $Z^{N}$, the posterior distribution of $A$, $B$ and the closed-loop $A-B\hat{K}$ remains matrix normal \[28, Lemma 1\].

<!-- chunk {"id": "body-0067", "role": "body", "section": "VI-B Design of Data-Driven LQR", "weight": 1.0} -->

Let $S_{\pi}$ and $\Sigma_{\pi}$ denote the optimal solutions to. The resulting controller is then given by Compared, the formulation has decision variables whose dimensions are independent of the data length $N$, and therefore enjoys better computational scalability. Moreover, numerical simulations in indicate that the Bayesian direct LQR method achieves a lower median optimality gap and a higher closed-loop stability rate than existing approaches.

<!-- chunk {"id": "body-0068", "role": "body", "section": "VI-B Design of Data-Driven LQR", "weight": 1.0} -->

The third type of controllers we consider is the average risk tuning controller ${\hat{h}}_{A(P)}(Z^{N})$ in (15 Average Risk Tuning ‣ II-A Design Principles ‣ II Preliminaries on Statistical Decision Theory ‣ Fundamental Limitations of Data-Driven Control: A Statistical Decision Perspective")), which is given by The pdf $p(Z^{N};\theta)$ can be decomposed using the Markovian property where the conditional distribution of $x_{k+1}$ is In the implementation, the integrals $\overline{W}(Z^{N})$ and $\overline{H}(Z^{N})$ are approximated using grid-based integration over the feasible set $\mathcal{D}_{\theta}$. To be specific, a fixed grid of candidate models $(A_{i},B_{i})$ is constructed within $\mathcal{D}_{\theta}$.

<!-- chunk {"id": "body-0069", "role": "body", "section": "VI-B Design of Data-Driven LQR", "weight": 1.0} -->

For each valid grid point, we precompute the corresponding LQR gain $K_{i}$ and weighting term $W_{i}$. Given the observed data $Z^{N}$, the likelihood $p(Z^{N};\theta_{i})$ is evaluated for each candidate model $\theta_{i}=(A_{i},B_{i})$, and the average-risk controller is computed as the resulting likelihood-weighted average.

<!-- chunk {"id": "body-0070", "role": "body", "section": "VI-B Design of Data-Driven LQR", "weight": 1.0} -->

The controllers $\hat{h}_{A(\pi)}$ in and $\hat{h}_{A(P)}$ in can be compared within the average risk minimization (Bayes) framework introduced in Section II-A. This comparison is postponed to the end of this section, where simulation results are presented to visualize the effect of the prior choice.

<!-- chunk {"id": "body-0071", "role": "body", "section": "VI-C Calculating the Lower Bound for LQR", "weight": 1.0} -->

We now apply the methodology developed in Section IV to derive lower bounds for the risk $R_{\theta}(\hat{h})$ in and the average risk $r(\hat{h})$ in for data-driven LQR. For the pointwise risk $R_{\theta}(\hat{h})$, we have where $f(\theta,b_{\theta},b_{\theta}^{\prime})$ is defined. In particular, for unbiased controllers, the lower bound reduces to the UCRLB.

<!-- chunk {"id": "body-0072", "role": "body", "section": "VI-C Calculating the Lower Bound for LQR", "weight": 1.0} -->

For the average risk, we have The optimal-bias lower bound for $r(\hat{h})$ is thus obtained by solving the variational problem of minimizing $F(b_{\theta})$.

<!-- chunk {"id": "body-0073", "role": "body", "section": "VI-C Calculating the Lower Bound for LQR", "weight": 1.0} -->

To compute the lower bounds above, one needs the Fisher information matrix $I_{F,N}(\theta)$, the optimal controller $h(\theta)$, and its derivative $h^{\prime}(\theta)$. For the scalar case with open-loop data, detailed expressions of the relevant quantities are provided in Appendices C and D, respectively. Once these quantities are available, the optimal-bias lower bound for the average risk $r(\hat{h})$ can be computed numerically by solving the the Euler-Lagrange equation subject to the natural boundary conditions. The multivariable case can be numerically solved in a similar manner.

<!-- chunk {"id": "body-0074", "role": "body", "section": "VI-D Simulation Results", "weight": 1.0} -->

We now use scalar systems to illustrate the implications of the theory and to benchmark the performance of the controllers introduced above. Without loss of generality, we consider the domain of interest $\mathcal{D}_{\theta}=\left\{\theta:(A-A_{\circ})^{2}+(B-B_{\circ})^{2}\leq\rho_{\circ}^{2}\right\}$, where $A_{\circ}=B_{\circ}=0.5$ and $\rho_{\circ}=0.4$. The experimental setting is as follows: $Q=1$, $R=0.1$, sample size $N=20$, and $\sigma_{e}^{2}=\sigma_{0}^{2}=\sigma_{u}^{2}=1$.

<!-- chunk {"id": "body-0075", "role": "body", "section": "VI-D Simulation Results", "weight": 1.0} -->

For each grid point $\theta_{i}=(A_{i},B_{i})$ in $\mathcal{D}_{\theta}$, we perform 200 Monte Carlo trials and use their average to estimate the risk and suboptimality gap of each realized data-driven LQR controller. For the regularization parameters in $\hat{h}_{R}$ and $\hat{h}_{A(\pi)}$, we take $\lambda_{1}=1$ and $\lambda_{2}=0.05$.

<!-- chunk {"id": "body-0076", "role": "body", "section": "VI-D Simulation Results", "weight": 1.0} -->

The first is the UCRLB for the pointwise risk $R_{\theta}(\hat{h})$ of unbiased decision rules, and the second is the optimal-bias lower bound on the average risk $r_{\theta}(\hat{h})$ that applies to all controllers.

<!-- chunk {"id": "body-0077", "role": "body", "section": "VI-D Simulation Results", "weight": 1.0} -->

Fig. 4: Comparison of the two lower bounds.

<!-- chunk {"id": "body-0078", "role": "body", "section": "VI-D Simulation Results", "weight": 1.0} -->

The resulting two lower bounds over $\mathcal{D}_{\theta}$ are given in Figures 4. The red surface labeled $f(\theta,b_{\theta},b_{\theta}^{\prime})$ represents the value of the Lagrangian after substituting the optimal bias function $b_{\theta}^{*}$ and its derivative $(b_{\theta}^{*})^{\prime}$ into $f(\theta,b_{\theta},b_{\theta}^{\prime})$, and the blue surface labeled UCRLB represents the bound for the pointwise risk $R_{\theta}(\hat{h})$. The lower bounds become significantly larger when $B$ is small and $A$ is close to $1$, indicating a region in which good control performance from finite data is intrinsically hard. This is especially pronounced for the UCRLB, which rises sharply in that part of the parameter domain. To understand this behavior, we examine the Fisher information.

<!-- chunk {"id": "body-0079", "role": "body", "section": "VI-D Simulation Results", "weight": 1.0} -->

This expression shows that, as $B$ becomes smaller and $|A|$ becomes larger, the Fisher information $I_{F,N}(\theta)$ decreases, indicating that the system becomes increasingly difficult to identify. Since the lower bounds depend on the inverse of Fisher information matrix, they increase significantly in this regime. This leads to an important observation: systems that are difficult to identify are likewise difficult to control in a data-driven manner. An alternative interpretation is that when $B$ becomes smaller and $|A|$ becomes larger, the system loses stabilizability. Our observation therefore is consistent with the arguments in and: systems with poor stabilizability are intrinsically hard to learn to control.

<!-- chunk {"id": "body-0080", "role": "body", "section": "VI-D Simulation Results", "weight": 1.0} -->

Fig. 5: The bias-variance tradeoff in LQR, with a slice at B = 0.5 along the direction A ∈ [0.1, 0.9].

<!-- chunk {"id": "body-0081", "role": "body", "section": "VI-D Simulation Results", "weight": 1.0} -->

Fig. 6: Pointwise risks Rθ(ĥ) of different controllers over 𝒟θ. The two slices correspond to varying A ∈ [0.1, 0.9] with B = 0.5, and varying B ∈ [0.1, 0.9] with A = 0.5.

<!-- chunk {"id": "body-0082", "role": "body", "section": "VI-D Simulation Results", "weight": 1.0} -->

Fig. 7: Suboptimality gaps of different controllers over 𝒟θ. The two slices correspond to varying A ∈ [0.1, 0.9] with B = 0.5, and varying B ∈ [0.1, 0.9] with A = 0.5.

<!-- chunk {"id": "body-0083", "role": "body", "section": "VI-D Simulation Results", "weight": 1.0} -->

(a) Pointwise risk Rθ(ĥ) of the certainty equivalence controller ĥCE (b) Pointwise risk Rθ(ĥ) of the SDP-based direct method ĥR (c) Pointwise risk Rθ(ĥ) of the covariance-parameterized Bayesian method ĥA(π) (d) Pointwise risk Rθ(ĥ) of the average risk tuning controller ĥA(P) Fig. 8: Comparison of data-driven LQR controllers vs. the lower bounds over 𝒟θ, with slices at B = 0.5 along the direction A ∈ [0.1, 0.9].

<!-- chunk {"id": "body-0084", "role": "body", "section": "VI-D Simulation Results", "weight": 1.0} -->

The four subplots in Figure 8 compare the performance of four data-driven LQR controllers with the corresponding lower bounds. In Figure 8(a), the certainty equivalence controller $\hat{h}_{\text{CE}}$ follows a similar profile and remains relatively close to the UCRLB over much of the parameter domain. Since this controller is consistent, the UCRLB remains a meaningful pointwise lower bound for the risk of $\hat{h}_{\text{CE}}$ and serves as a useful benchmark. By contrast, the situation is different for $\hat{h}_{R}$, $\hat{h}_{A(\pi)}$ and $\hat{h}_{A(P)}$, shown in Figures 8(b), 8(c) and 8(d). Since these controllers are biased when the regularization parameters are finite, the UCRLB is no longer an informative benchmark. Instead, their performance should be compared with the lower bound $f(\theta,b,b^{\prime})$, which accounts for bias and therefore applies to the average risk.

<!-- chunk {"id": "body-0085", "role": "body", "section": "VI-D Simulation Results", "weight": 1.0} -->

Finally, these observations also illustrate the "waterbed" effect in data-driven LQR. In Figure 8(c), the substantial reduction of risk around $A=0.5$ is compensated by a pronounced increase in risk for values of $A$ farther away from $0.5$. In contrast, Figure 8(d) shows a more moderate risk reduction near the center, accompanied by a smaller increase elsewhere. Thus, these observations show that reducing the risk in one region of the parameter domain is accompanied by increased risk in other regions. The proposed lower bound makes this redistribution effect explicit and provides a quantitative way to assess how severe it is.

<!-- chunk {"id": "body-0086", "role": "body", "section": "Conclusions", "weight": 1.0} -->

Motivated by fundamental limits in point estimation, this work developed a statistical decision framework for data-driven control. By combining the bias-variance decomposition with the CRLB, we derived fundamental lower bounds on the performance for data-driven control problems under quadratic loss. These results revealed quantitative limitations that no data-driven controller design can circumvent and make the bias--variance tradeoff explicit. They also reveal a "waterbed" effect in data-driven control, analogous to the fundamental limitation of sensitivity shaping in classical control.

<!-- chunk {"id": "body-0087", "role": "body", "section": "Conclusions", "weight": 1.0} -->

The two case studies, namely the feedforward control problem and the benchmark LQR problem, illustrated several implications of the framework. First, because the derived lower bounds depend explicitly on the inverse of Fisher information matrix, they show that the statistical difficulty of data-driven control is fundamentally shaped by the underlying system itself and the information available in the data. Second, the results show that no controller can be uniformly best over the entire parameter domain. Accordingly, controller design should be guided by the region of the parameter space most relevant to the intended application.

<!-- chunk {"id": "body-0088", "role": "body", "section": "Conclusions", "weight": 1.0} -->

In future, we will extend the proposed framework to analyze the statistical limitations of data-driven MPC, reinforcement learning, and online control methods.
