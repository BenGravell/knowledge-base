<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

On the Sample Complexity of the Linear Quadratic Regulator

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

This paper addresses the optimal control problem known as the Linear Quadratic Regulator in the case when the dynamics are unknown. We propose a multi-stage procedure, called Coarse-ID control, that estimates a model from a few experimental trials, estimates the error in that model with respect to the truth, and then designs a controller using both the model and uncertainty estimate. Our technique uses contemporary tools from random matrix theory to bound the error in the estimation procedure. We also employ a recently developed approach to control synthesis called System Level Synthesis that enables robust control design by solving a convex optimization problem. We provide end-to-end bounds on the relative error in control cost that are nearly optimal in the number of parameters and that highlight salient properties of the system to be controlled such as closed-loop sensitivity and optimal control magnitude. We show experimentally that the Coarse-ID approach enables efficient computation of a stabilizing controller in regimes where simple control schemes that do not take the model uncertainty into account fail to stabilize the true system.

<!-- chunk {"id": "body-0003", "role": "body", "section": "Introduction", "weight": 1.5} -->

Having surpassed human performance in video games and Go, there has been a renewed interest in applying machine learning techniques to planning and control. In particular, there has been a considerable amount of effort in developing new techniques for *continuous control* where an autonomous system interacts with a physical environment. A tremendous opportunity lies in deploying these data-driven systems in more demanding interactive tasks including self-driving vehicles, distributed sensor networks, and agile robotics. As the role of machine learning expands to more ambitious tasks, however, it is critical these new technologies be safe and reliable. Failure of such systems could have severe social and economic consequences including the potential loss of human life. How can we guarantee that our new data-driven automated systems are robust?

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

Unfortunately, there are no clean baselines delineating the possible control performance achievable given a fixed amount of data collected from a system. Such baselines would enable comparisons of different techniques and would allow engineers to trade off between data collection and action in scenarios with high uncertainty. Typically, a key difficulty in establishing baselines is in proving *lower bounds* that state the minimum amount of knowledge needed to achieve a particular performance, regardless of method. However, in the context of controls, even *upper bounds* describing the worst-case performance of competing methods are exceptionally rare. Without such estimates, we are left to compare algorithms on a case-by-case basis, and we may have trouble diagnosing whether poor performance is due to algorithm choice or some other error such as a software bug or a mechanical flaw.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

In this paper, we attempt to build a foundation for a theoretical understanding of how machine learning interfaces with control by analyzing one of the most well-studied problems in classical optimal control, the *Linear Quadratic Regulator* (LQR). Here we assume that the system to be controlled obeys *linear* dynamics, and we wish to minimize some *quadratic* function of the system state and control action. This problem has been studied for decades in control: it has a simple, closed form solution on the infinite time horizon and an efficient, dynamic programming solution on finite time horizons. When the dynamics are unknown, however, there are far fewer results about achievable performance.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

Our contribution is to analyze the LQR problem when the dynamics of the system are unknown, and we can measure the system's response to varied inputs. A naïve solution to this problem would be to collect some data of how the system behaves over time, fit a model to this data, and then solve the original LQR problem assuming this model is accurate. Unfortunately, while this procedure might perform well given sufficient data, it is difficult to determine how many experiments are necessary in practice. Furthermore, it is easy to construct examples where the procedure fails to find a stabilizing controller.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

As an alternative, we propose a method that couples our uncertainty in estimation with the control design.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Introduction", "weight": 1.5} -->

Use supervised learning to learn a coarse model of the dynamical system to be controlled. We refer to the system estimate as the *nominal system*.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Introduction", "weight": 1.5} -->

Using either prior knowledge or statistical tools like the bootstrap, build probabilistic guarantees about the distance between the nominal system and the true, unknown dynamics.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Introduction", "weight": 1.5} -->

Solve a robust optimization problem over controllers that optimizes performance of the nominal system while penalizing signals with respect to the estimated uncertainty, ensuring stable and robust execution.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Introduction", "weight": 1.5} -->

We will show that for a sufficient number of observations of the system, this approach is guaranteed to return a control policy with small relative cost. In particular, it guarantees asymptotic stability of the closed-loop system. In the case of LQR, step 1 of coarse-ID control simply requires solving a linear least squares problem, step 2 uses a finite sample theoretical guarantee or a standard bootstrap technique, and step 3 requires solving a small semidefinite program. Analyzing this approach, on the other hand, requires contemporary techniques in non-asymptotic statistics and a novel parameterization of control problems that renders nonconvex problems convex.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Introduction", "weight": 1.5} -->

We demonstrate the utility of our method on a simple simulation. In the presented example, we show that simply using the nominal system to design a control policy frequently results in unstable closed-loop behavior, even when there is an abundance of data from the true system. However, the Coarse-ID approach finds a stabilizing controller with few system observations.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Problem Statement and Our Contributions", "weight": 1.0} -->

The standard optimal control problem aims to find a control sequence that minimizes an expected cost. We assume a dynamical system with *state* $x_{t} \in {\mathbb{R}}^{n}$ can be acted on by a *control* $u_{t} \in {\mathbb{R}}^{p}$ and obeys the stochastic dynamics

<!-- chunk {"id": "body-0014", "role": "body", "section": "Problem Statement and Our Contributions", "weight": 1.0} -->

where $w_{t}$ is a random process with $w_{t}$ independent of $w_{t^{\prime}}$ for all $t \neq t^{\prime}$. Optimal control then seeks to minimize

<!-- chunk {"id": "body-0015", "role": "body", "section": "Problem Statement and Our Contributions", "weight": 1.0} -->

Here, $c_{t}$ denotes the state-control cost at every time step, and the input $u_{t}$ is allowed to depend on the current state $x_{t}$ and all previous states and actions. In this generality, problem (1.4) encapsulates many of the problems considered in the reinforcement learning literature.

<!-- chunk {"id": "body-0016", "role": "body", "section": "Problem Statement and Our Contributions", "weight": 1.0} -->

Here $Q$ (resp. $R$) is a $n \times n$ (resp. $p \times p$) positive definite matrix, $A$ and $B$ are called the *state transition matrices*, and $w_{t} \in {\mathbb{R}}^{n}$ is Gaussian noise with zero-mean and covariance $\Sigma_{w}$. Throughout, $M^{\ast}$ denotes the Hermitian transpose of the matrix $M$.

<!-- chunk {"id": "body-0017", "role": "body", "section": "Problem Statement and Our Contributions", "weight": 1.0} -->

In what follows, we will be concerned with the *infinite time horizon* variant of the LQR problem where we let the time horizon $T$ go to infinity and minimize the average cost. When the dynamics are known, this problem has a celebrated closed form solution based on the solution of matrix Riccati equations. Indeed, the optimal solution sets $u_{t} = {Kx_{t}}$ for a fixed $p \times n$ matrix $K$, and the corresponding optimal cost will serve as our gold-standard baseline to which we will compare the achieved cost of all algorithms.

<!-- chunk {"id": "body-0018", "role": "body", "section": "Problem Statement and Our Contributions", "weight": 1.0} -->

In the case when the state transition matrices are unknown, fewer results have been established about what cost is achievable. We will assume that we can conduct experiments of the following form: given some initial state $x_{0}$, we can evolve the dynamics for $T$ time steps using any control sequence $\{ u_{0},\ldots,u_{T - 1}\}$, measuring the resulting output $\{ x_{1},\ldots,x_{T}\}$. If we run $N$ such independent experiments, what infinite time horizon control cost is achievable using only the data collected? For simplicity of bookkeeping, in our analysis we further assume that we can prepare the system in initial state $x_{0} = 0$.

<!-- chunk {"id": "body-0019", "role": "body", "section": "Problem Statement and Our Contributions", "weight": 1.0} -->

In what follows we will examine the performance of the Coarse-ID control framework in this scenario. We will estimate the errors accrued by least squares estimates $(\hat{A},\hat{B})$ of the system dynamics. This estimation error is not easily handled by standard techniques because the design matrix is highly correlated with the model to be estimated. Regardless, for theoretical tractability, we can build a least squares estimate using only the final sample $(x_{T},x_{T - 1},u_{T - 1})$ of each of the $N$ experiments. Indeed, in Section 2 we prove the following

<!-- chunk {"id": "body-0020", "role": "body", "section": "Estimation of unknown dynamical systems", "weight": 1.0} -->

Estimation of unknown systems, especially linear dynamical systems, has a long history in the system identification subfield of control theory. While the text of Ljung covers the classical asymptotic results, our interest is primarily in nonasymptotic results. Early results on nonasymptotic rates for parameter identification featured conservative bounds which are exponential in the system degree and other relevant quantities. More recently, Bento et al. show that when the $A$ matrix is stable and induced by a sparse graph, then one can recover the support of $A$ from a single trajectory using $\ell_{1}$-penalized least squares. Furthermore, Hardt et al. provide the first polynomial time guarantee for identifying stable linear systems with outputs. Their guarantees, however, are in terms of predictive output performance of the model, and require an assumption on the true system that is more stringent than stability. It is not clear how their statistical risk guarantee can be used in a downstream robust synthesis procedure.

<!-- chunk {"id": "body-0021", "role": "body", "section": "Estimation of unknown dynamical systems", "weight": 1.0} -->

Next, we turn our attention to system identification of linear systems in the frequency domain. A comprehensive text on these methods (which differ from the aforementioned state-space methods) is the work by Chen and Gu. For stable systems, Helmicki et al. propose to identify a finite impulse response (FIR) approximation by directly estimating the first $r$ impulse response coefficients. This method is analyzed in a non-adversarial probabilistic setting, who prove that a polynomial number of samples are sufficient to recover a FIR filter which approximates the true system in both $\ell_{p}$-norm and $\mathcal{H}_{\infty}$-norm. However, transfer function methods do not easily allow for optimal control with state variables, since they only model the input/output behavior of the system.

<!-- chunk {"id": "body-0022", "role": "body", "section": "Estimation of unknown dynamical systems", "weight": 1.0} -->

In parallel to the system identification community, identification of auto-regressive time series models is a widely studied topic in the statistics literature (see e.g. Box et al. for the classical results). Goldenshluger and Zeevi show that the coefficients of a stationary autoregressive model can be estimated from a single trajectory of length polynomial in $1/{({1 - \rho})}$ via least squares, where $\rho$ denotes the stability radius of the process. They also prove that their rate is minimax optimal. More recently, several authors have studied generalization bounds for non i.i.d. data, extending the standard learning theory guarantees for independent data. At the crux of these arguments lie various mixing assumptions, which limits the analysis to only hold for stable dynamical systems. Results in this line of research suggest that systems with smaller mixing time (i.e. systems that are more stable) are easier to identify (i.e. take less samples). Our result in Proposition 1.1, however, suggests instead that identification benefits from more easily excitable systems.

<!-- chunk {"id": "body-0023", "role": "body", "section": "Estimation of unknown dynamical systems", "weight": 1.0} -->

While our analysis holds when we have access to full state observations, empirical testing suggests that Proposition 1.1 reflects reality more accurately than arguments based on mixing. In follow up work we have begun to reconcile this issue for stable linear systems.

<!-- chunk {"id": "body-0024", "role": "body", "section": "Robust controller design", "weight": 1.0} -->

For end-to-end guarantees, parameter estimation is only half the picture. Our procedure provides us with a family of system models described by a nominal estimate and a set of unknown but bounded model errors. It is therefore necessary to ensure that the computed controller has stability and performance guarantees for any such admissible realization. The problem of robustly stabilizing such a family of systems is one with a rich history in the controls community. When modelling errors to the nominal system are allowed to be arbitrary norm-bounded linear time-invariant (LTI) operators in feedback with the nominal plant, traditional small-gain theorems and robust synthesis techniques can be applied to exactly solve the problem. However, when the errors are known to have more structure there are more sophisticated techniques based on structured singular values and corresponding $\mu$-synthesis techniques or integral quadratic constraints (IQCs). While theoretically appealing and much less conservative than traditional small-gain approaches, the resulting synthesis methods are both computationally intractable (although effective heuristics do exist) and difficult to interpret analytically. In particular, we know of no results in the literature that bound the degradation in performance of controlling an uncertain system in terms of the size of the perturbations affecting it.

<!-- chunk {"id": "body-0025", "role": "body", "section": "Robust controller design", "weight": 1.0} -->

To circumvent this issue, we leverage a novel parameterization of robustly stabilizing controllers based on the SLS framework for controller synthesis. We describe this framework in more detail in Section 3. Originally developed to allow for scaling optimal and robust controller synthesis techniques to large-scale systems, the SLS framework can be viewed as a generalization of the celebrated Youla parameterization. We show that SLS allows us to account for model uncertainty in a transparent and analytically tractable way.

<!-- chunk {"id": "body-0026", "role": "body", "section": "PAC learning and reinforcement learning", "weight": 1.0} -->

Concerning end-to-end guarantees for LQR which couple estimation and control synthesis, our work is most comparable to that of Fiechter, who shows that the *discounted* LQR problem is PAC-learnable. Fietcher analyzes an identify-then-control scheme similar to the one we propose, but there are several key differences. First, our probabilistic bounds on identification are much sharper, by leveraging modern tools from high-dimensional statistics. Second, Fiechter implicitly assumes that the true closed-loop system with the estimated controller is not only stable but also contractive. While this very strong assumption is nearly impossible to verify in practice, contractive closed-loop assumptions are actually pervasive throughout the literature, as we describe below. To the best of our knowledge, our work is the first to properly lift this technical restriction. Third, and most importantly, Fietcher proposes to directly solve the discounted LQR problem with the identified model, and does not take into account any uncertainty in the controller synthesis step. This is problematic for two reasons.

<!-- chunk {"id": "body-0027", "role": "body", "section": "PAC learning and reinforcement learning", "weight": 1.0} -->

First, it is easy to construct an instance of a discounted LQR problem where the *optimal* solution does not stabilize the true system (see e.g. ). Therefore, even in the limit of infinite data, there is no guarantee that the closed-loop system will be stable. Second, even if the optimal solution does stabilize the underlying system, failing to take uncertainty into account can lead to situations where the synthesized controller does not. We will demonstrate this behavior in our experiments.

<!-- chunk {"id": "body-0028", "role": "body", "section": "PAC learning and reinforcement learning", "weight": 1.0} -->

We are also particularly interested in the LQR problem as a baseline for more complicated problems in reinforcement learning (RL). LQR should be a relatively easy problem in RL because on can learn the dynamics from anywhere in the state space, vastly simplifying the problem of exploration. Hence, it is important to establish how well a pure exploration followed by exploitation strategy can fare on this simple baseline.

<!-- chunk {"id": "body-0029", "role": "body", "section": "PAC learning and reinforcement learning", "weight": 1.0} -->

There are indeed some related efforts in RL and online learning. Abbasi-Yadkori and Szepesvari propose to use the optimism in the face of uncertainty (OFU) principle for the LQR problem, by maintaining confidence ellipsoids on the true parameter, and using the controller which, in feedback, minimizes the cost objective the most among all systems in the confidence ellipsoid. Ignoring the computational intractability of this approach, their analysis reveals an exponential dependence in the system order in their regret bound, and also makes the very strong assumption that the optimal closed-loop systems are contractive for every $A,B$ in the confidence ellipsoid. The regret bound is improved by Ibrahimi et al. to depend linearly on the state dimension under additional sparsity constraints on the dynamics.

<!-- chunk {"id": "body-0030", "role": "body", "section": "PAC learning and reinforcement learning", "weight": 1.0} -->

In response to the computational intractability of the OFU principle, researchers in RL and online learning have proposed the use of Thompson sampling for exploration. Abeille and Lazaric show that the regret of a Thompson sampling approach for LQR scales as $\overset{\sim}{\mathcal{O}}{(T^{2/3})}$ and improve the result to $\overset{\sim}{\mathcal{O}}{(\sqrt{T})}$, where $\overset{\sim}{\mathcal{O}}{( \cdot )}$ hides poly-logarithmic factors. However, their results are only valid for the scalar $n = d = 1$ setting. Ouyang et al. show that in a *Bayesian* setting, the expected regret can be bounded by $\overset{\sim}{\mathcal{O}}{(\sqrt{T})}$. While this matches the bound of, the Bayesian regret is with respect to a particular Gaussian prior distribution over the true model, which differs from the frequentist setting considered.

<!-- chunk {"id": "body-0031", "role": "body", "section": "PAC learning and reinforcement learning", "weight": 1.0} -->

Furthermore, these works also make the same restrictive assumption that the optimal closed-loop systems are uniformly contractive over some known set.

<!-- chunk {"id": "body-0032", "role": "body", "section": "PAC learning and reinforcement learning", "weight": 1.0} -->

Jiang et al. propose a general exploration algorithm for contextual decision processes (CDPs) and show that CDPs with low *Bellman rank* are PAC-learnable; in the LQR setting, they show the Bellman rank is bounded by $n^{2}$. While this result is appealing from an information-theoretic standpoint, the proposed algorithm is computationally intractable for continuous problems. Hazan et al. study the problem of prediction in a linear dynamical system via a novel spectral filtering algorithm. Their main result shows that one can compete in a regret setting in terms of prediction error. As mentioned previously, converting prediction error bounds into concrete bounds on sub-optimality of control performance is an open question. Fazel et al. show that randomized search algorithms similar to policy gradient can learn the optimal controller with a polynomial number of samples in the noiseless case; an explicit characterization of the dependence of the sample complexity on the parameters of the true system is not given.

<!-- chunk {"id": "body-0033", "role": "body", "section": "System Identification through Least-Squares", "weight": 1.0} -->

To estimate a coarse model of the unknown system dynamics, we turn to the simple and classical method of linear least squares. By running experiments in which the system starts at $x_{0} = 0$ and the dynamics evolve with a given input, we can record the resulting state observations. The set of inputs and outputs from each such experiment will be called a rollout. For system estimation, we excite the system with Gaussian noise for $N$ rollouts, each of length $T$. The resulting dataset is $\{{(x_{t}^{(\ell)},u_{t}^{(\ell)})}:{{1 \leq \ell \leq N},{0 \leq t \leq T}}\}$, where $t$ indexes the time in one rollout and $\ell$ indexes independent rollouts. Therefore, we can estimate the system dynamics by

<!-- chunk {"id": "body-0034", "role": "body", "section": "System Identification through Least-Squares", "weight": 1.0} -->

For the Coarse-ID control setting, a good estimate of error is just as important as the estimate of the dynamics. Statistical theory and tools allow us to quantify the error of the least squares estimator. First, we present a theoretical analysis of the error in a simplified setting. Then, we describe a computational bootstrap procedure for error estimation from data alone.

<!-- chunk {"id": "body-0035", "role": "body", "section": "Least Squares Estimation as a Random Matrix Problem", "weight": 1.0} -->

We begin by explicitly writing the form of the least squares estimator. First, fixing notation to simplify the presentation, let $\Theta:=\begin{bmatrix}
\end{bmatrix}^{\ast} \in {\mathbb{R}}^{{({n + p})} \times n}$ and let $z_{t}:=\begin{bmatrix}
\end{bmatrix} \in {\mathbb{R}}^{n + p}$. Then the system dynamics can be rewritten, for all $t \geq 0$,

<!-- chunk {"id": "body-0036", "role": "body", "section": "Least Squares Estimation as a Random Matrix Problem", "weight": 1.0} -->

Then in a single rollout, we will collect

<!-- chunk {"id": "body-0037", "role": "body", "section": "Least Squares Estimation as a Random Matrix Problem", "weight": 1.0} -->

The system dynamics give the identity $X = {{Z\Theta} + W}$. Resetting state of the system to $x_{0} = 0$ each time, we can perform $N$ rollouts and collect $N$ datasets like (2.2). Having the ability to reset the system to a state independent of past observations will be important for the analysis in the following section, and it is also practically important for potentially unstable systems. Denote the data for each rollout as $(X^{(\ell)},Z^{(\ell)},W^{(\ell)})$. With slight abuse of notation, let $X_{N}$ be composed of vertically stacked $X^{(\ell)}$, and similarly for $Z_{N}$ and $W_{N}$. Then we have

<!-- chunk {"id": "body-0038", "role": "body", "section": "Least Squares Estimation as a Random Matrix Problem", "weight": 1.0} -->

The full data least squares estimator for $\Theta$ is (assuming for now invertibility of $Z_{N}^{\ast}Z_{N}$),

<!-- chunk {"id": "body-0039", "role": "body", "section": "Least Squares Estimation as a Random Matrix Problem", "weight": 1.0} -->

Then the estimation error is given by

<!-- chunk {"id": "body-0040", "role": "body", "section": "Least Squares Estimation as a Random Matrix Problem", "weight": 1.0} -->

The magnitude of this error is the quantity of interest in determining confidence sets around estimates $(\hat{A},\hat{B})$. However, since $W_{N}$ and $Z_{N}$ are not independent, this estimator is difficult to analyze using standard methods. While this type of analysis is an open problem of interest, in this paper we turn instead to a simplified estimator.

<!-- chunk {"id": "body-0041", "role": "body", "section": "Theoretical Bounds on Least Squares Error", "weight": 1.0} -->

In this section, we work out the statistical rate for the least squares estimator which uses just the last sample of each trajectory $(x_{T}^{(\ell)},x_{T - 1}^{(\ell)},u_{T - 1}^{(\ell)})$. This estimation procedure is made precise in Algorithm 1. Our analysis ideas are analogous to those used to prove statistical rates for standard linear regression, and they leverage recent tools in nonasymptotic analysis of random matrices. The result is presented above in Proposition 1.1.

<!-- chunk {"id": "body-0042", "role": "body", "section": "Theoretical Bounds on Least Squares Error", "weight": 1.0} -->

In the context of Proposition 1.1, a single data point from each $T$-step rollout is used. We emphasize that this strategy results in independent data, which can be seen by defining the estimator matrix directly. The previous estimator (2.3) is amended as follows: the matrices defined in (2.2) instead include only the final timestep of each trial, $X_{N} = \begin{bmatrix}
\end{bmatrix}^{\ast}$, and similar modifications are made to $Z_{N}$ and $W_{N}$. The estimator (2.3) uses these modified matrices, which now contain independent rows. To see this, recall the definition of $G_{T}$ and $F_{T}$ from (1.8),

<!-- chunk {"id": "body-0043", "role": "body", "section": "Theoretical Bounds on Least Squares Error", "weight": 1.0} -->

We can unroll the system dynamics and see that

<!-- chunk {"id": "body-0044", "role": "body", "section": "Theoretical Bounds on Least Squares Error", "weight": 1.0} -->

Since ${F_{T}F_{T}^{\ast}} \succ 0$, as long as both $\sigma_{u},\sigma_{w}$ are positive, this is a non-degenerate distribution.

<!-- chunk {"id": "body-0045", "role": "body", "section": "Theoretical Bounds on Least Squares Error", "weight": 1.0} -->

Therefore, bounding the estimation error can be achieved via proving a result on the error in random design linear regression with vector valued observations. First, we present a lemma which bounds the spectral norm of the product of two independent Gaussian matrices.

<!-- chunk {"id": "body-0046", "role": "body", "section": "Estimating Model Uncertainty with the Bootstrap", "weight": 1.0} -->

In the previous sections we offered theoretical guarantees on the performance of the least squares estimation of $A$ and $B$ from independent samples. However, there are two important limitations to using such guarantees in practice to offer upper bounds on $\epsilon_{A} = {\parallel{A - \hat{A}}\parallel}_{2}$ and $\epsilon_{B} = {\parallel{B - \hat{B}}\parallel}_{2}$. First, using only one sample per system rollout is empirically less efficient than using all available data for estimation. Second, even optimal statistical analyses often do not recover constant factors that match practice. For purposes of robust control, it is important to obtain upper bounds on $\epsilon_{A}$ and $\epsilon_{B}$ that are not too conservative.

<!-- chunk {"id": "body-0047", "role": "body", "section": "Estimating Model Uncertainty with the Bootstrap", "weight": 1.0} -->

We propose a vanilla bootstrap method for estimating ${\hat{\epsilon}}_{A}$ and ${\hat{\epsilon}}_{B}$. Bootstrap methods have had a profound impact in both theoretical and applied statistics since their introduction. These methods are used to estimate statistical quantities (e.g. confidence intervals) by sampling synthetic data from an empirical distribution determined by the available data. For the problem at hand we propose the procedure described in Algorithm 2.^11^1We assume that $\sigma_{u}$ and $\sigma_{w}$ are known. Otherwise they can be estimated from data.

<!-- chunk {"id": "body-0048", "role": "body", "section": "Estimating Model Uncertainty with the Bootstrap", "weight": 1.0} -->

There are many known guarantees for the bootstrap, particularly for the parametric version we use. We do not discuss these results here; for more details see texts by Van Der Vaart and Wellner, Shao and Tu, and Hall. Instead, in Appendix F we show empirically the performance of the bootstrap for our estimation problem. For mission critical systems, where empirical validation is insufficient, the statistical error bounds presented in Section 2.2 give guarantees on the size of $\epsilon_{A}$, $\epsilon_{B}$. In general, data dependent error guarantees will be less conservative. In follow up work we offer guarantees similar to the ones presented in Section 2.2 for estimation of linear dynamics from dependent data.

<!-- chunk {"id": "body-0049", "role": "body", "section": "Robust Synthesis", "weight": 1.0} -->

With estimates of the system $(\hat{A},\hat{B})$ and operator norm error bounds $(\epsilon_{A},\epsilon_{B})$ in hand, we now turn to control design. In this section we introduce some useful tools from *System Level Synthesis* (SLS), a recently developed approach to control design that relies on a particular parameterization of signals in a control system. We review the main SLS framework, highlighting the key constructions that we will use to solve the robust LQR problem. As we show in this and the following section, using the SLS framework, as opposed to traditional techniques from robust control, allows us to (a) compute robust controllers using semidefinite programming, and (b) provide sub-optimality guarantees in terms of the size of the uncertainties on our system estimates.

<!-- chunk {"id": "body-0050", "role": "body", "section": "Useful Results from System Level Synthesis", "weight": 1.0} -->

The SLS framework focuses on the *system responses* of a closed-loop system. As a motivating example, consider linear dynamics under a fixed a static state-feedback control policy $K$, i.e., let $u_{k} = {Kx_{k}}$. Then, the closed loop map from the disturbance process $\{ w_{0},w_{1},\ldots\}$ to the state $x_{k}$ and control input $u_{k}$ at time $k$ is given by

<!-- chunk {"id": "body-0051", "role": "body", "section": "Useful Results from System Level Synthesis", "weight": 1.0} -->

where $\{{\Phi_{x}{(k)}},{\Phi_{u}{(k)}}\}$ are called the *closed-loop system response elements* induced by the static controller $K$.

<!-- chunk {"id": "body-0052", "role": "body", "section": "Useful Results from System Level Synthesis", "weight": 1.0} -->

Note that even when the control is a linear function of the state and its past history (i.e. a linear dynamic controller), the expression (3.2) is valid. Though we conventionally think of the control policy as a function mapping states to input, whenever such a mapping is linear, both the control input and the state can be written as linear functions of the disturbance signal $w_{t}$. With such an identification, the dynamics require that the $\{{\Phi_{x}{(k)}},{\Phi_{u}{(k)}}\}$ must obey the constraints

<!-- chunk {"id": "body-0053", "role": "body", "section": "Useful Results from System Level Synthesis", "weight": 1.0} -->

As we describe in more detail below in Theorem 3.1. ‣ 3.1 Useful Results from System Level Synthesis ‣ 3 Robust Synthesis ‣ On the Sample Complexity of the Linear Quadratic Regulator"), these constraints are in fact both necessary and sufficient. Working with closed-loop system responses allows us to cast optimal control problems as optimization problems over elements $\{{\Phi_{x}{(k)}},{\Phi_{u}{(k)}}\}$, constrained to satisfy the affine equations (3.3). Comparing equations (3.1) and (3.2), we see that the former is non-convex in the controller $K$, whereas the latter is affine in the elements $\{{\Phi_{x}{(k)}},{\Phi_{u}{(k)}}\}$.

<!-- chunk {"id": "body-0054", "role": "body", "section": "Useful Results from System Level Synthesis", "weight": 1.0} -->

As we work with infinite horizon problems, it is notationally more convenient to work with *transfer function* representations of the above objects, which can be obtained by taking a $z$-transform of their time-domain representations. The frequency domain variable $z$ can be informally thought of as the time-shift operator, i.e., ${z{\{ x_{k},x_{k + 1},\ldots\}}} = {\{ x_{k + 1},x_{k + 2},\ldots\}}$, allowing for a compact representation of LTI dynamics. We use boldface letters to denote such transfer functions signals in the frequency domain, e.g., ${\mathbf{\Phi}_{x}{(z)}} = {\sum_{k = 1}^{\infty}{\Phi_{x}{(k)}z^{- k}}}$. Then, the constraints (3.3) can be rewritten as

<!-- chunk {"id": "body-0055", "role": "body", "section": "Useful Results from System Level Synthesis", "weight": 1.0} -->

and the corresponding (not necessarily static) control law $\mathbf{u} = {\mathbf{K}\mathbf{x}}$ is given by $\mathbf{K} = {\mathbf{\Phi}_{u}\mathbf{\Phi}_{x}^{- 1}}$. The relevant frequency domain connections for LQR are illustrated in Appendix C.

<!-- chunk {"id": "body-0056", "role": "body", "section": "Useful Results from System Level Synthesis", "weight": 1.0} -->

We formalize our discussion by introducing notation that is common in the controls literature. For a thorough introduction to the functional analysis commonly used in control theory, see Chapters 2 and 3 of Zhou et al.. Let $\mathbb{T}$ (resp. $\mathbb{D}$) denote the unit circle (resp. open unit disk) in the complex plane. The restriction of the Hardy spaces $\mathcal{H}_{\infty}{({\mathbb{T}})}$ and $\mathcal{H}_{2}{({\mathbb{T}})}$ to matrix-valued real-rational functions that are analytic on the complement of $\mathbb{D}$ will be referred to as $\mathcal{R}\mathcal{H}_{\infty}$ and $\mathcal{R}\mathcal{H}_{2}$, respectively. In controls parlance, this corresponds to (discrete-time) stable matrix-valued transfer functions.

<!-- chunk {"id": "body-0057", "role": "body", "section": "Useful Results from System Level Synthesis", "weight": 1.0} -->

For these two function spaces, the $\mathcal{H}_{\infty}$ and $\mathcal{H}_{2}$ norms simplify to

<!-- chunk {"id": "body-0058", "role": "body", "section": "Useful Results from System Level Synthesis", "weight": 1.0} -->

The most important transfer function for the LQR problem is the map from the state sequence to the control actions: the control policy. Consider an arbitrary transfer function $\mathbf{K}$ denoting the map from state to control action, $\mathbf{u} = {\mathbf{K}\mathbf{x}}$. Then the closed-loop transfer matrices from the process noise $\mathbf{w}$ to the state $\mathbf{x}$ and control action $\mathbf{u}$ satisfy

<!-- chunk {"id": "body-0059", "role": "body", "section": "Useful Results from System Level Synthesis", "weight": 1.0} -->

We then have the following theorem parameterizing the set of stable closed-loop transfer matrices, as described in equation (3.5), that are achievable by a given stabilizing controller $\mathbf{K}$.

<!-- chunk {"id": "body-0060", "role": "body", "section": "Robust LQR Synthesis", "weight": 1.0} -->

We return to the problem setting where estimates $(\hat{A},\hat{B})$ of a true system $(A,B)$ satisfy

<!-- chunk {"id": "body-0061", "role": "body", "section": "Robust LQR Synthesis", "weight": 1.0} -->

where $\Delta_{A}:={\hat{A} - A}$ and $\Delta_{B}:={\hat{B} - B}$ and where we wish to minimize the LQR cost for the worst instantiation of the parametric uncertainty.

<!-- chunk {"id": "body-0062", "role": "body", "section": "Robust LQR Synthesis", "weight": 1.0} -->

Before proceeding, we must formulate the LQR problem in terms of the system responses $\{{\Phi_{x}{(k)}},{\Phi_{u}{(k)}}\}$. It follows from Theorem 3.1. ‣ 3.1 Useful Results from System Level Synthesis ‣ 3 Robust Synthesis ‣ On the Sample Complexity of the Linear Quadratic Regulator") and the standard equivalence between infinite horizon LQR and $\mathcal{H}_{2}$ optimal control that, for a disturbance process distributed as $w_{t}\overset{i.i.d.}{\sim}\mathcal{N}{(0,{\sigma_{w}^{2}I})}$, the standard LQR problem (1.7) can be equivalently written as

<!-- chunk {"id": "body-0063", "role": "body", "section": "Robust LQR Synthesis", "weight": 1.0} -->

We provide a full derivation of this equivalence in Appendix C. Going forward, we drop the $\sigma_{w}^{2}$ multiplier in the objective function as it affects neither the optimal controller nor the sub-optimality guarantees that we compute in Section 4.

<!-- chunk {"id": "body-0064", "role": "body", "section": "Robust LQR Synthesis", "weight": 1.0} -->

We begin with a simple sufficient condition under which any controller $\mathbf{K}$ that stabilizes $(\hat{A},\hat{B})$ also stabilizes the true system $(A,B)$. To state the lemma, we introduce one additional piece of notation. For a matrix $M$, we let $\Re_{M}$ denote the resolvent

<!-- chunk {"id": "body-0065", "role": "body", "section": "Robust LQR Synthesis", "weight": 1.0} -->

We now can state our robustness lemma.

<!-- chunk {"id": "body-0066", "role": "body", "section": "Sub-optimality Guarantees", "weight": 1.0} -->

We now return to analyzing the Coarse-ID control problem. We upper bound the performance of the controller synthesized using the optimization (3.18) in terms of the size of the perturbations $(\Delta_{A}$, $\Delta_{B})$ and a measure of complexity of the LQR problem defined by $A$, $B$, $Q$, and $R$. The following result is one of our main contributions.

<!-- chunk {"id": "body-0067", "role": "body", "section": "Computation", "weight": 1.0} -->

As posed, the main optimization problem (3.18) is a semi-infinite program, and we are not aware of a way to solve this problem efficiently. In this section we describe two alternative formulations that provide upper bounds to the optimal value and that can be solved in polynomial time.

<!-- chunk {"id": "body-0068", "role": "body", "section": "Finite impulse response approximation", "weight": 1.0} -->

An elementary approach to reducing the aforementioned semi-infinite program to a finite dimensional one is to only optimize over the first $L$ elements of the transfer functions $\mathbf{\Phi}_{x}$ and $\mathbf{\Phi}_{u}$, effectively taking a finite impulse response (FIR) approximation. Since these are both stable maps, we expect the effects of such an approximation to be negligible as long as the optimization horizon $L$ is chosen to be sufficiently large -- in what follows, we show that this is indeed the case.

<!-- chunk {"id": "body-0069", "role": "body", "section": "Finite impulse response approximation", "weight": 1.0} -->

By restricting our optimization to FIR approximations of $\mathbf{\Phi}_{x}$ and $\mathbf{\Phi}_{u}$, we can cast the $\mathcal{H}_{2}$ cost as a second order cone constraint. The only difficulty arises in posing the $\mathcal{H}_{\infty}$ constraint as a semidefinite program. Though there are several ways to cast $\mathcal{H}_{\infty}$ constraints as linear matrix inequalities, we use the formulation in Theorem 5.8 of Dumitrescu's text to take advantage of the FIR structure in our problem. We note that using Dumitrescu's formulation, the resulting problem is affine in $\alpha$ when $\gamma$ is fixed, and hence we can solve for the optimal value of $\alpha$. Then the resulting system response elements can be cast as a dynamic feedback controller using Theorem 2 of Anderson and Matni.

<!-- chunk {"id": "body-0070", "role": "body", "section": "Sub-optimality guarantees", "weight": 1.0} -->

In this subsection we show that optimizing over FIR approximations incurs only a small degradation in performance relative to the solution to the infinite-horizon problem. In particular, this degradation in performance decays exponentially in the FIR horizon $L$, where the rate of decay is specified by the decay rate of the spectral elements of the optimal closed loop system response $\Re_{A + {BK_{\star}}}$.

<!-- chunk {"id": "body-0071", "role": "body", "section": "Sub-optimality guarantees", "weight": 1.0} -->

Before proceeding, we introduce additional concepts and notation needed to formalize guarantees in the FIR setting. A linear-time-invariant transfer function is stable if and only if it is exponentially stable, i.e., $\mathbf{\Phi} = {\sum_{t = 0}^{\infty}{z^{- t}\Phi{(t)}}} \in {\mathcal{R}\mathcal{H}_{\infty}}$ if and only if there exists positive values $C$ and $\rho \in {\lbrack 0,1)}$ such that for every spectral element $\Phi{(t)}$, $t \geq 0$, it holds that

<!-- chunk {"id": "body-0072", "role": "body", "section": "Sub-optimality guarantees", "weight": 1.0} -->

We introduce a version of the optimization problem (3.13)

<!-- chunk {"id": "body-0073", "role": "body", "section": "Sub-optimality guarantees", "weight": 1.0} -->

The slack term $V$ accounts for the error introduced by truncating the infinite response transfer functions of problem (3.13). Intuitively, if the truncated tail is sufficiently small, then the effects of this approximation should be negligible on performance. The next result formalizes this intuition.

<!-- chunk {"id": "body-0074", "role": "body", "section": "Static controller and a common Lyapunov approximation", "weight": 1.0} -->

As we have reiterated above, when the dynamics are known, the optimal LQR control law takes the form $u_{t} = {Kx_{t}}$ for properly chosen static gain matrix $K$. We can reparameterize the optimization problem (3.18)

<!-- chunk {"id": "body-0075", "role": "body", "section": "Static controller and a common Lyapunov approximation", "weight": 1.0} -->

Under this reparameterization, the problem is no longer convex. Here we present a simple application of the *common Lyapunov relaxation* that allows us to find a controller $K$ using semidefinite programming.

<!-- chunk {"id": "body-0076", "role": "body", "section": "Static controller and a common Lyapunov approximation", "weight": 1.0} -->

With these identifications, (5.3) can be reformulated as

<!-- chunk {"id": "body-0077", "role": "body", "section": "Static controller and a common Lyapunov approximation", "weight": 1.0} -->

Using standard techniques from the robust control literature, we can upper bound this problem via the semidefinite program

<!-- chunk {"id": "body-0078", "role": "body", "section": "Static controller and a common Lyapunov approximation", "weight": 1.0} -->

Note that this optimization problem is affine in $\alpha$ when $\gamma$ is fixed. Hence, in practice we can find the optimal value of $\alpha$ as well. A static controller can then be extracted from this optimization problem by setting $K = {ZX^{- 1}}$. A full derivation of this relaxation can be found in Appendix E. Note that this compact SDP is simpler to solve than the truncated FIR approximation. As demonstrated experimentally in the following section, the cost of this simplification is that the common Lyapunov approach provides a controller with slightly higher LQR cost.

<!-- chunk {"id": "body-0079", "role": "body", "section": "Numerical Experiments", "weight": 1.0} -->

We illustrate our results on estimation, controller synthesis, and LQR performance with numerical experiments of the end-to-end Coarse-ID control scheme. The least squares estimation procedure (2.1) is carried out on a simulated system in Python, and the bootstrapped error estimates are computed in parallel using PyWren.

<!-- chunk {"id": "body-0080", "role": "body", "section": "Numerical Experiments", "weight": 1.0} -->

All of the synthesis and performance experiments are run in MATLAB. We make use of the YALMIP package for prototyping convex optimization and use the MOSEK solver under an academic license. In particular, when using the FIR approximatsion described in Section 5.1, we find it effective to make use of YALMIP's dualize function, which considerably reduces the computation time.

<!-- chunk {"id": "body-0081", "role": "body", "section": "Estimation of Example System", "weight": 1.0} -->

We focus experiments on a particular example system. Consider the LQR problem instance specified by

<!-- chunk {"id": "body-0082", "role": "body", "section": "Estimation of Example System", "weight": 1.0} -->

The dynamics correspond to a marginally unstable graph Laplacian system where adjacent nodes are weakly connected, each node receives direct input, and input size is penalized relatively more than state. Dynamics described by graph Laplacians arise naturally in consensus and distributed averaging problems. For this system, we perform the full data identification procedure in (2.1), using inputs with variance $\sigma_{u}^{2} = 1$ and noise with variance $\sigma_{w}^{2} = 1$. The errors are estimated via the bootstrap (Algorithm 2) using $M = {2,000}$ trials and confidence parameter $\delta = 0.05$.

<!-- chunk {"id": "body-0083", "role": "body", "section": "Estimation of Example System", "weight": 1.0} -->

The behavior of the least squares estimates and the bootstrap error estimates are illustrated in Figure 1. The rollout length is fixed to $T = 6$, and the number of rollouts used in the estimation is varied. As expected, increasing the number of rollouts corresponds to decreasing errors. For large enough $N$, the bootstrapped error estimates are of the same order of magnitude as the true errors. In Appendix G we show plots for the setting in which the number of rollouts is fixed to $N = 6$ while the rollout length is varied.

<!-- chunk {"id": "body-0084", "role": "body", "section": "Controller Synthesis on Estimated System", "weight": 1.0} -->

Using the estimates of the system in (6.1), we synthesize controllers using two robust control schemes: the convex problem in 5.2 with filters of length $L = 32$ and $V$ set to $0$, and the common Lyapunov (CL) relaxation of the static synthesis problem (5.3). Once the FIR responses ${\{{\Phi_{x}{(k)}}\}}_{k = 1}^{F}$ and ${\{{\Phi_{u}{(k)}}\}}_{k = 1}^{F}$ are found, we need a way to implement the system responses as a controller. We represent the dynamic controller $\mathbf{K} = {\mathbf{\Phi}_{u}\mathbf{\Phi}_{x}^{- 1}}$ by finding an equivalent state-space realization $(A_{K},B_{K},C_{K},D_{K})$ via Theorem 2 of.

<!-- chunk {"id": "body-0085", "role": "body", "section": "Controller Synthesis on Estimated System", "weight": 1.0} -->

In what follows, we compare the performance of these controllers with the nominal LQR controller (the solution to (1.7) with $\hat{A}$ and $\hat{B}$ as model parameters), and explore the trade-off between robustness, complexity, and performance.

<!-- chunk {"id": "body-0086", "role": "body", "section": "Controller Synthesis on Estimated System", "weight": 1.0} -->

The relative performance of the nominal controller is compared with robustly synthesized controllers in Figure 2. For both robust synthesis procedures, two controllers are compared: one using the true errors on $A$ and $B$, and the other using the bootstrap estimates of the errors. The robust static controller generated via the common Lyapunov approximation performs slightly worse than the more complex FIR controller, but it still achieves reasonable control performance. Moreover, the conservative bootstrap estimates also result in worse control performance, but the degradation of performance is again modest.

<!-- chunk {"id": "body-0087", "role": "body", "section": "Controller Synthesis on Estimated System", "weight": 1.0} -->

Furthermore, the experiments show that the nominal controller often outperforms the robust controllers *when it is stabilizing.* On the other hand, the nominal controller is not guaranteed to stabilize the true system, and as shown in Figure 2, it only does so in roughly 80 of the 100 instances after $N = 60$ rollouts. It is also important to note a distinction between stabilization for nominal and robust controllers. When the nominal controller is not stabilizing, there is no indication to the user (though sufficient conditions for stability can be checked using our result in Corollary 3.4 or structured singular value methods ). On the other hand, the robust synthesis procedure will return as infeasible, alerting the user by default that the uncertainties are too high. We observe similar results when we fix the number of trials but vary the rollout length. These figures are provided in Appendix G.

<!-- chunk {"id": "body-0088", "role": "body", "section": "Controller Synthesis on Estimated System", "weight": 1.0} -->

The SLS framework guarantees a stabilizing controller for the true system provided that the computational approximations are feasible for *any* value of $\gamma$ between 0 and 1, as long as the system errors $(\epsilon_{A},\epsilon_{B})$ are upper bounds on the true errors. Figure 4 displays the controller performance for robust synthesis when $\gamma$ is set to 0.999. Simply ensuring a stable model and neglecting to optimize the nominal cost yields controllers that perform nearly an order of magnitude better than those where we search for the optimal value of $\gamma$. This observation aligns with common practice in robust control: constraints ensuring stability are only active when the cost tries to drive the system up against a safety limit. We cannot provide end-to-end sample complexity guarantees for this method and leave such bounds as an enticing challenge for future work.

<!-- chunk {"id": "body-0089", "role": "body", "section": "Controller Synthesis on Estimated System", "weight": 1.0} -->

LQR Cost Suboptimality
Figure 4: The performance of controllers synthesized on the results of 100 identification experiments is plotted against the number of rollouts. The plot compares the median suboptimality of nominal controllers with fixed-γ robustly synthesized controllers (γ = 0.999).

<!-- chunk {"id": "body-0090", "role": "body", "section": "Conclusions and Future Work", "weight": 1.0} -->

Coarse-ID control provides a straightforward approach to merging nonasymptotic methods from system identification with contemporary Systems Level Synthesis approaches to robust control. Indeed, many of the principles of Coarse-ID control were well established in the 90s, but fusing together an end-to-end result required contemporary analysis of random matrices and a new perspective on controller synthesis. These results can be extended in a variety of directions, and we close this paper with a discussion of some of the short-comings of our approach and of several possible applications of the Coarse-ID framework to other control settings.

<!-- chunk {"id": "body-0091", "role": "body", "section": "Other performance metrics", "weight": 1.0} -->

Though we focused exclusively on LQR in this paper, we note that all of our results on robust synthesis and end-to-end performance analysis extend to other metrics popular in control. Indeed, *any* norm on the system responses $\{{\Phi_{x}{(k)}},{\Phi_{u}{(k)}}\}$ can be solved robustly using our approach; Lemma 3.4 holds for any norm. In turn, we can mimic the derivation in Section 3 to yield a constrained optimization problem with respect to the nominal dynamics and a norm on the uncertainty $\hat{\mathbf{\Delta}}$. This means that our suboptimality bound in Corollary 4.3 holds true when we replace $\mathcal{H}_{2}{({\mathbb{T}})}$ with $\mathcal{H}_{\infty}{({\mathbb{T}})}$. Furthermore, similar results can be derived for other norms, so long as care is placed on the associated submultiplicative properties of the norms in question.

<!-- chunk {"id": "body-0092", "role": "body", "section": "Other performance metrics", "weight": 1.0} -->

For example, in follow up work we analyze robustness under the $\mathcal{L}_{1}$ norm in the context of constraints on the states and control signals.

<!-- chunk {"id": "body-0093", "role": "body", "section": "Improving the end-to-end analysis", "weight": 1.0} -->

There are several places where our analysis could be substantially improved. The most obvious is that in our estimator for the state-transition matrices, our algorithm only uses the final time step of each rollout. This strategy is data inefficient, and empirically, accuracy only improves when including all of the data. Analyzing the full least squares estimator is non-trivial because the design matrix strongly depends on data to be estimated. This poses a challenging problem in random matrix theory that has applications in a variety of control and reinforcement learning settings. In follow up work we have begun to address this issue for stable linear systems.

<!-- chunk {"id": "body-0094", "role": "body", "section": "Improving the end-to-end analysis", "weight": 1.0} -->

In the context of SLS, we use a very coarse characterization of the plant uncertainty to bound the quantity in Lemma 3.4 and to yield a tractable optimization problem. Indeed, the only property we use about the error between our nominal system and the true system is that the maps

<!-- chunk {"id": "body-0095", "role": "body", "section": "Improving the end-to-end analysis", "weight": 1.0} -->

are contractions. Nowhere do we use the fact that these are linear operators, or even the fact that they are the same operator from time-step to time-step. Indeed, there are stronger bounds that could be engineered using the theory of Integral Quadratic Constraints that would take into account these additional properties. Such tighter bounds could yield considerably less conservative control schemes in both theory and practice.

<!-- chunk {"id": "body-0096", "role": "body", "section": "Improving the end-to-end analysis", "weight": 1.0} -->

Additionally, it would be of interest to understand the loss in performance incurred by the common Lyapunov relaxation we use in our experiments. Empirically, we see that the approximation leads to good performance, suggesting that it does not introduce much conservatism into the synthesis task. Further, our numerical experiments suggest that optimizing a nominal cost subject to robust stability constraints, as opposed to directly optimizing the SLS upper bound, leads to better empirical performance. Future work will seek to understand whether this is a phenomenological observation specific to the systems used in our experiments, or if there is a deeper principle at play that leads to tighter sub-optimality guarantees.

<!-- chunk {"id": "body-0097", "role": "body", "section": "Lower bounds", "weight": 1.0} -->

Finding lower bounds for control problems when the model is unknown is an open question. Even for LQR, it is not at all clear how well the system $(A,B)$ needs to be known in order to attain good control performance. While we produce reasonable worst-case upper bounds for this problem, we know of no lower bounds. Such bounds would offer a reasonable benchmark for how well one could ever expect to do with no priors on the linear system dynamics.

<!-- chunk {"id": "body-0098", "role": "body", "section": "Integrating Coarse-ID control in other control paradigms", "weight": 1.0} -->

The end-to-end Coarse-ID control framework should be applicable in a variety of settings. For example, in Model Predictive Control (MPC), controller synthesis problems are approximately solved on finite time horizons, one step is taken, and then this process is repeated. MPC is an effective solution which substitutes fast optimization solvers for clever, complex control design. We believe it will be straightforward to extend the Coarse-ID paradigm to MPC, using a similar perturbation argument as in Section 3. The main challenges in MPC lie in how to guarantee that safety constraints are maintained throughout execution without too much conservatism in control costs.

<!-- chunk {"id": "body-0099", "role": "body", "section": "Integrating Coarse-ID control in other control paradigms", "weight": 1.0} -->

Another interesting investigation lies in the area of adaptive control, where we could investigate how to incorporate new data into coarse models to further refine constraint sets and costs. Indeed, some work has already been done in this space. We propose to investigate how to operationalize and extend the notion of *optimistic exploration* proposed in the context of continuous control by Abbasi-Yadkori and Szepesvari. The idea behind optimistic improvement is to select the model that would give the best optimization cost if the current model was true. In this way, we fail fast, either receiving a good cost or learning quickly that our model is incorrect. It would be worth investigating whether the Coarse-ID framework can make it simple to update a least squares estimate for the system parameters and then provide an efficient mechanism for choosing the next optimistic control.

<!-- chunk {"id": "body-0100", "role": "body", "section": "Integrating Coarse-ID control in other control paradigms", "weight": 1.0} -->

Finally, Coarse-ID control could be relevant to nonlinear control applications. In nonlinear control, iterative LQR schemes are remarkably effective. Hence, it would be interesting to understand how parametric model errors can be estimated and mitigated in a control loop that employs iterative LQR or similar dynamic programming methods.

<!-- chunk {"id": "body-0101", "role": "body", "section": "Sample complexities of reinforcement learning for continuous control", "weight": 1.0} -->

Finally, we imagine that the analysis in this paper may be useful for understanding popular reinforcement learning algorithms that are also being tested for continuous control. Reinforcement learning directly attacks a control cost in question without resorting to any specific identification scheme. While this suffers from the drawback that generally speaking, no parameter convergence can be guaranteed, it is ideally suited to ignoring modes that do not affect control performance. For instance, it might not be important to get a good estimate of very stable modes or of lightly damped modes that do not substantially affect the performance.

<!-- chunk {"id": "body-0102", "role": "body", "section": "Sample complexities of reinforcement learning for continuous control", "weight": 1.0} -->

There are two parallel problems here. First, it would be of interest to determine system identification algorithms that are tuned to particular control tasks. In the Coarse-ID control approach, the estimation and control are completely decoupled. However, it may be beneficial to inform the identification algorithm about the desired cost, resulting in improved sample complexity.

<!-- chunk {"id": "body-0103", "role": "body", "section": "Sample complexities of reinforcement learning for continuous control", "weight": 1.0} -->

From a different perspective, Policy Gradient and Q-Learning methods applied to LQR could yield important insights about the pros and cons of such methods. There are classic papers on Q-Learning for LQR, but these use asymptotic analysis. Recently, the first such analysis for Policy Gradient has appeared, though the precise scaling with respect to system parameters is not yet understood. Providing clean nonasymptotic bounds here could help provide a rapprochement between machine learning and adaptive control, with optimization negotiating the truce.
