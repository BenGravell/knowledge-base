<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Regret Analysis for Risk-aware Linear Quadratic Control

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

This paper investigates the regret associated with the Distributionally Robust Control (DRC) strategies used to address multistage optimization problems where the involved probability distributions are not known exactly, but rather are assumed to belong to specified ambiguity families. We quantify the price (distributional regret) that one ends up paying for not knowing the exact probability distribution of the stochastic system uncertainty while aiming to control it using the DRC strategies. The conservatism of the DRC strategies for being robust to worst-case uncertainty distribution in the considered ambiguity set comes at the price of lack of knowledge about the true distribution in the set. We use the worst case Conditional Value-at-Risk to define the distributional regret and the regret bound was found to be increasing with tighter risk level. The motive of this paper is to promote the design of new control algorithms aiming to minimize the distributional regret.

<!-- chunk {"id": "body-0003", "role": "body", "section": "Introduction", "weight": 1.5} -->

Stochastic optimization has been the backbone of success of several portfolio management systems in finance as they are equipped with necessary tools to handle risks of various kinds. Inspired by their application in finance, it is now being increasingly used in the control community as well. However, the success of stochastic optimization techniques depend on the knowledge of the true distribution of the random variable of interest as in \[Wozabal\]. For instance, it is a common practice in the well celebrated linear stochastic control approach to assume system uncertainties to be Gaussian as described in \[Aström, Athans and Falb\], just for the sake of simplicity and tractability. However, it is well known that system uncertainties in reality might be not known exactly and further they might be non-Gaussian. To address the shortcoming of not knowing the true distribution, the Distributionally Robust Optimization (DRO) approaches were developed in \[Wiesemann et al.Wiesemann, Kuhn, and Sim, Gao and Kleywegt\] to hedge against the worst case distributions of the uncertainties.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

In connection to the DRO approach, authors in \[Kishida and Cetinkaya\] proposed a risk aware linear quadratic control by hedging against the worst case distribution of the process disturbance using Conditional Value-at-Risk $({CVaR})$.\

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

In the process of being robust against any worst case arbitrary distribution in the assumed ambiguity set of distributions governing the random variable, all DRO techniques end up resulting in conservative decisions due to their pessimistic approach to the decision making problem. For instance, risk bounded motion planning for nonlinear robotic systems can be effectively performed as described in \[Renganathan et al.Renganathan, Safaoui, Kothari, Gravell, Shames, and Summers\] if we exactly know how much unnecessary conservatism is being exerted by DRO approach while deciding the control actions. On the contrary, if we analyze the same problem through the optimistic lens, it naturally leads us to investigate the price that one would pay for rather hedging against the worst case distribution instead of the true distribution of the system uncertainties (referred later as *distributional regret*). That is, we are interested in computing how much would any distributionally robust optimal control algorithm pay for not knowing the true distribution of the system uncertainty while trying to control the system by hedging against the worst case distribution of the system uncertainty.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

Out of several available DRO parameterizations, we address the regret with respect to moment based ambiguity set based problem formulation, especially with the first two moments as described in \[Delage and Ye, Jiang and Guan, Nie et al.Nie, Yang, Zhong, and Zhou, Zymler et al.Zymler, Kuhn, and Rustem\]. The regret associated with other DRO parameterizations are equally interesting and open as well and are currently being pursued in our ongoing future work.\

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

To compute the regret associated with the problem formulation with moment based ambiguity sets, it is natural to consider the DRO objective function formulated using the expectation or the worst case $CVaR$ as the risk functional as described in \[Rockafellar et al.Rockafellar, Uryasev, et al., Wang and Chapman\]. However, we show that expectation is not the right risk functional to be considered in our problem setting as it does not effectively capture the tail probabilities from different distributions in the considered ambiguity set. Analysing the regret for not knowing the exact distributions has been carried out in the field of auction based game theory in \[Guo et al.Guo, Jordan, and Vitercik\] where the authors used the learning approach to minimize the regret for not knowing the true distribution of items to buy. Our work is inspired by their motivation and we apply the same reasoning to the field of control theory for systems with stochastic uncertainties. Specifically, we study the regret incurred by the risk-aware linear quadratic control algorithm explained in \[Kishida and Cetinkaya\].

<!-- chunk {"id": "body-0008", "role": "body", "section": "Introduction", "weight": 1.5} -->

Similar analysis can be done in future for the risk-averse MPC described in \[Sopasakis et al.Sopasakis, Herceg, Bemporad, and Patrinos\].\

<!-- chunk {"id": "body-0009", "role": "body", "section": "Introduction", "weight": 1.5} -->

*Contributions:* To the best of our knowledge, this is one of the first articles in the literature to analyze the regret of a control policy that rather hedges against the worst case distributions of the stochastic system uncertainties and not knowing the exact true distribution of stochastic system uncertainties.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Introduction", "weight": 1.5} -->

We define the distributional regret for discrete time stochastic linear systems with system uncertainties namely the initial state $x_{0}$ and the disturbance $w_{k}$ modelled using moment based ambiguity sets containing distributions consistent with the set of finite first two moments.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Introduction", "weight": 1.5} -->

Our distributional regret definition proposes the use of distributionally robust risk functional namely the worst-case Conditional Value-at-Risk $({CVaR})$ to account for the price that a distributionally robust control algorithm would pay for not knowing the true distribution of the stochastic system uncertainties and purposefully hedging the worst case distribution instead.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Introduction", "weight": 1.5} -->

Our proposed regret analysis is simulated using numerical examples to demonstrate the growth of distributional regret over tighter risk level and time.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Introduction", "weight": 1.5} -->

Following a short summary of notations and preliminaries, the rest of the paper is organized as follows: We propose a regret definition for distributionally robust control with moment based ambiguity sets in §2. Subsequently, a regret analysis is performed in §3. The simulation results demonstrating our proposed approach is explained in §4. Finally, the paper is closed in §5 along with a summary and directions for future research.

<!-- chunk {"id": "body-0014", "role": "body", "section": "Control of Linear Systems with Unknown Distributions for System Uncertainties", "weight": 1.0} -->

Consider a linear, stochastic, discrete time-invariant system as follows

<!-- chunk {"id": "body-0015", "role": "body", "section": "Control of Linear Systems with Unknown Distributions for System Uncertainties", "weight": 1.0} -->

where $x_{k} \in {\mathbb{R}}^{n}$ and $u_{k} \in {\mathbb{R}}^{m}$ is the system state and input at time $k$, respectively and $T$ denotes the total time horizon. Further, $w_{k} \in {\mathbb{R}}^{r}$ denotes the stochastic process noise. Further, $A \in {\mathbb{R}}^{n \times n}$ is the dynamics matrix, $B \in {\mathbb{R}}^{n \times m}$ is the input matrix and $D \in {\mathbb{R}}^{n \times r}$ is the disturbance matrix and the pair $(A,B)$ is assumed to be stabilizable. We denote by $\mathbf{w}:={(w_{0},\ldots,w_{T - 1})}$.

<!-- chunk {"id": "body-0016", "role": "body", "section": "Problem Formulation Using Moment-based Ambiguity Set", "weight": 1.0} -->

Based on the assumption made on the knowledge of the distributions of the stochastic system uncertainties $x_{0}$ and $w$, we will define and analyse regret associated with it. There are several ambiguity set definitions for modeling the stochastic system uncertainties such as moment based, Wasserstein metric based, multimodality of the distribution and other parameterization. However, we limit our analysis to only moment-based ambiguity set. The analysis of regret for other parameterizations are left as an interesting direction of research for the future. The preliminaries of the details of the ambiguity sets used in this paper are given below.

<!-- chunk {"id": "body-0017", "role": "body", "section": "Assumption 1", "weight": 1.0} -->

The distribution of $w_{k}$, namely ${\mathbb{P}}_{w}$, is unknown but is believed to be belonging to a moment-based ambiguity set of distributions, $\mathcal{P}^{w}$ given by

<!-- chunk {"id": "body-0018", "role": "body", "section": "Assumption 1", "weight": 1.0} -->

Note that there are infinitely many distributions present in the considered set $\mathcal{P}^{w}$. For instance, both multivariate Gaussian and multivariate Laplacian distributions with zero mean and covariance $\Sigma_{w}$ belong to $\mathcal{P}^{w}$ with the latter having heavier tails than the former. We assume that the system is controllable under zero process noise meaning that given any ${x_{0},x_{f}} \in {\mathbb{R}}^{n}$, there exists a sequence of control input ${\{ u_{k}\}}_{k = 0}^{N - 1}$ that steers the system state from $x_{0}$ to $x_{f}$ for large $N \in {\mathbb{N}}$.

<!-- chunk {"id": "body-0019", "role": "body", "section": "Assumption 1", "weight": 1.0} -->

Since the considered system is stochastic, the initial condition $x_{0}$ is subject to a similar uncertainty model as the process noise, with the distribution belonging to a moment-based ambiguity set, $\mathcal{P}^{x_{0}}$ given by

<!-- chunk {"id": "body-0020", "role": "body", "section": "Assumption 1", "weight": 1.0} -->

If the control law $u_{k}$ is selected as an affine function of the state $x_{k}$ at any time $k$, similar moment-based ambiguity sets $\mathcal{P}^{x_{k}}$ can be written for ${{{\mathbb{P}}_{x_{k}},{\forall k}} \in 1},{\ldots,N}$ using the propagated mean and covariance at time $k$. Note that $\mathcal{P}^{x_{k}}$ would *not* be empty ${\forall k} \in {\lbrack 1,N\rbrack}$ as Gaussian distribution (due to its invariance under linear transformation) would be a guaranteed member in that set. Further, $x_{0}$ is assumed to independent of $w_{k},{\forall k}$. Here, we present the regret analysis for the control problem involving moment-based ambiguity set-based problem formulation.

<!-- chunk {"id": "body-0021", "role": "body", "section": "Assumption 1", "weight": 1.0} -->

Towards the regret definition, we require certain assumptions on the control policy to be used by the system considered.

<!-- chunk {"id": "body-0022", "role": "body", "section": "Assumption 2", "weight": 1.0} -->

We restrict the class of control policies to be causal and linear state feedback policies so that at each time instant $k$, the control input $u_{k} = {\pi_{k}{(x_{k},x_{k - 1},\ldots,x_{0})}}$, where the policy $\pi_{k} \in \Pi$ and $\Pi$ denotes the set of all linear state feedback policies.

<!-- chunk {"id": "body-0023", "role": "body", "section": "Minimax Problem with Moment-based Ambiguity Set", "weight": 1.0} -->

where $T \in {\mathbb{N}}$ is the finite time horizon, $Q \succeq 0$ and $R \succ 0$. That is, is the resulting cost when the state evolution of the system given by starting from $x_{0} \sim {\mathbb{P}}_{x_{0}} \in \mathcal{P}^{x_{0}}$ is governed by the policy $\pi \in \Pi$ under the disturbances ${{w_{k},{\forall k}} = 0},{\ldots,{T - 1}}$ coming from the distribution ${\mathbb{P}}_{w} \in \mathcal{P}^{w}$ and the resulting distribution of states being ${\mathbb{P}}_{\mathbf{x}}$. We define the risk functional $\rho$ operating on the random cost to be a map from the space of random variables to ${\mathbb{R}} \cup {\{\infty\}}$.

<!-- chunk {"id": "body-0024", "role": "body", "section": "Minimax Problem with Moment-based Ambiguity Set", "weight": 1.0} -->

There are several risk functionals available from the finance literature described in \[Rockafellar et al.Rockafellar, Uryasev, et al.\] such as the expectation, Value-at-Risk, Conditional Value-at-Risk, mean-variance etc. A good risk functional for a specific application should satisfy certain required axioms mentioned in \[Majumdar and Pavone\]. In this problem setting, risk functionals such as the expectation, Value-at-Risk, Conditional value-at-Risk can be used.

<!-- chunk {"id": "body-0025", "role": "body", "section": "Minimax Problem with Moment-based Ambiguity Set", "weight": 1.0} -->

Consider a random variable $Z \in {\mathbb{R}}$ with finite second order moments modeled using moment based ambiguity set $Z \sim {\mathbb{P}}_{Z} \in \mathcal{P}^{Z}:={\{{\mathbb{P}}_{Z}\mid{{{{\mathbb{E}}{\lbrack Z\rbrack}} = \mu_{Z}},{{{\mathbb{E}}{\lbrack{({Z - \mu_{Z}})}^{2}\rbrack}} = \Sigma_{Z}}}\}}$. Then, $VaR$ quantifies the threshold for a given tail probability corresponding to the distribution of the random variable and $CVaR$ quantifies the conditional expectation of losses exceeding the threshold defined using $VaR$. That is, for a given risk level $\alpha \in {}$, we define

<!-- chunk {"id": "body-0026", "role": "body", "section": "Minimax Problem with Moment-based Ambiguity Set", "weight": 1.0} -->

where is convex in $Z$ and ${\mathbb{F}}{(z)}$ denotes the cumulative distribution function of the random variable $Z$ and ${\mathbb{F}}{(z)}$ is both right-continuous and non-decreasing function. One can find the control policy that minimizes, if the distribution of the system uncertainties namely ${\mathbb{P}}_{\mathbf{x}},{\mathbb{P}}_{w}$ are known exactly as it would aide us in computing the risk functionals. However, in reality the distribution of the random variable is not known exactly or only partial information is known. Then in that case, we define the worst case ${CVaR}_{\alpha}{(Z)}$ of the random variable $Z$ as

<!-- chunk {"id": "body-0027", "role": "body", "section": "Minimax Problem with Moment-based Ambiguity Set", "weight": 1.0} -->

where we interchanged the $\inf$ and $\sup$ operation using the stochastic saddle point theorem in \[Shapiro and Kleywegt\]. Note that when $\alpha\rightarrow 1$, ${\overline{CVaR}}_{\alpha}{(Z)}$ reduces to ${\mathbb{E}}{\lbrack Z\rbrack}$. For instance, the classical stochastic linear quadratic regulator (LQR) problem setting assumes that the disturbances $w_{k} \sim {{\mathcal{N}{(0,\Sigma_{w})}},{\forall k}}$ with $\Sigma_{w} \in {\mathbb{S}}_{+}^{r}$ and the initial state $x_{0} \sim {\mathcal{N}{(\mu_{0},\Sigma_{0})}}$ with covariance $\Sigma_{0} \in {\mathbb{S}}_{+}^{n}$.

<!-- chunk {"id": "body-0028", "role": "body", "section": "Minimax Problem with Moment-based Ambiguity Set", "weight": 1.0} -->

Due to the linearity of the system dynamics, it is straightforward to see that ${{{\mathbb{P}}_{x_{k}},{\forall k}} = 0},{1,\ldots,T}$ will be Gaussian as well.

<!-- chunk {"id": "body-0029", "role": "body", "section": "Minimax Problem with Moment-based Ambiguity Set", "weight": 1.0} -->

where the risk functional $\rho$ is *not* the expectation operator. Let the optimal feedback control input at time $k$ be $u_{k}^{\star} = {\pi_{k}^{\star}{(x_{k}^{\star})}} = {K_{k}^{\star}x_{k}^{\star}}$, with $K_{k}^{\star} \in {\mathbb{R}}^{m \times n}$ given by the policy $\pi_{k}^{\star} \in \Pi$^11^1Note that we restrict ourselves to set of linear state feedback policies though potentially a nonlinear state feedback policy can do better that the linear counterparts..

<!-- chunk {"id": "body-0030", "role": "body", "section": "Regret of Distributionally Robust Control with Moment Based Ambiguity Sets", "weight": 1.0} -->

Regret for online controllers can be addressed using *policy regret* approach where the cost incurred by the online control policy operating without knowing the quantity of interest is compared against that of the optimal control policy available in hindsight that operates by knowing the quantity of interest. Since the distribution of the stochastic system uncertainties in stochastic LQR are exactly known, and moreover, it being the optimal linear state feedback solution, there is nothing that stochastic LQR can do to improve more as it has the entire knowledge about the stochastic system uncertainties. On the other hand, the case with the moment based ambiguity set is not straightforward and they demand a certain level of conservatism to be robust against any distribution in the respective ambiguity set. Hence, to investigate the conservatism of such control policies from an optimistic lens, we study their regret. Since, the policy $\pi_{k}^{\star} \in \Pi$ minimizes, it is important to mention in what sense it is optimal.

<!-- chunk {"id": "body-0031", "role": "body", "section": "Regret of Distributionally Robust Control with Moment Based Ambiguity Sets", "weight": 1.0} -->

Note that at any time $k = {0,\ldots,T}$, the true distribution of the state namely ${\breve{\mathbb{P}}}_{x_{k}} \in \mathcal{P}^{x_{k}}$ need not be equal to the worst case distribution of the state ${\mathbb{P}}_{x_{k}}^{\star} \in \mathcal{P}^{x_{k}}$. If $\pi^{\star} \in \Pi$ was designed to be robust against the worst case distributions of the states and the disturbance, then it will not fair well against the true distributions of the states and the disturbance, meaning that $\pi^{\star} \in \Pi$ will incur more cost for the system in face of the true distributions of the states and the disturbance which are not necessarily equal to the worst case distribution of the states and the disturbance.

<!-- chunk {"id": "body-0032", "role": "body", "section": "Numerical Results", "weight": 1.0} -->

and $D = I_{2}$. Assuming the system state distribution to be stationary in nature, the policy $\pi^{\star}$ was calculated using Theorem 4.2 of \[Kishida and Cetinkaya\] where the system was simulated with uncertainties stemming from *possibly* worst-case multivariate Gaussian in the first case and uncertainties stemming from the true distribution namely multivariate Laplacian (as it has heavier tails than the Gaussian counterpart) in the second case. The penalty matrices were assumed to be ${Q = {10I_{2}}},{R = 1}$. The risk level was chosen to be $\alpha = 0.20$. To compute the state error, each time the system was simulated for $T = 100$ time steps using the policy $\pi^{\star}$ from initial state sampled from multivariate Gaussian and multivariate Laplacian distributions respectively. The distributional regret bound corresponding to the term $G_{k}$ was computed using $N = 100$ samples of $e_{k}$.\

<!-- chunk {"id": "body-0033", "role": "body", "section": "Numerical Results", "weight": 1.0} -->

*Discussion of Results:* The simulation results are presented in Figures 2 and 2. To qualitatively study the bound on the distributional regret defined using Theorem 3.9, we simulated the system for different values of the risk level $\alpha \in {}$ by fixing the time $T$. It is clear from the results plotted in Figure 2 that the distributional regret bound increased with the time $T$ and with a tighter (or smaller) risk level $\alpha$. This means that when the true distribution has heavier tails than the worst-case distribution, the regret incurred will be higher when the risk level $\alpha$ is smaller as the worst-case ${CVaR}_{\alpha}{( \cdot )}$ will increase due to Lemma 3.6 and Lemma 3.8. The evolution of the mean of state error (almost zero for all time steps) and the percentiles are plotted in Figure 2 and this depicts that the system evolution with respect to uncertainties from true distribution and worst case distribution is different and the policy that is meant to work for the worst case uncertainty distributions need not work well for the uncertainties stemming from the true distributions governing the uncertainties.

<!-- chunk {"id": "body-0034", "role": "body", "section": "Conclusion", "weight": 1.5} -->

The regret incurred by distributionally robust optimal controller while controlling systems with stochastic uncertainties modelled using moment based ambiguity set was presented in this paper. The worst-case ${CVaR}_{\alpha}{( \cdot )}$ with risk level $\alpha \in {}$ was selected to hedge against the distributional uncertainty and using it the regret incurred by the controller for not hedging against the true distribution of system uncertainties was analysed. The distributional regret bound was found to be increasing with tighter (that is smaller) risk levels. Future research will address the distributional regret for risk-averse MPC problem and other DRO parameterizations such as the Wasserstein metric-based ambiguity sets.

<!-- chunk {"id": "body-0035", "role": "body", "section": "Conclusion", "weight": 1.5} -->

This project has received funding from the European Research Council (ERC) under the European Union's Horizon 2020 research and innovation program under grant agreement No 834142 (Scalable Control). The authors are with the ELLIIT Strategic Research Area at Lund University. The authors thank Bo Bernhardsson from the department of automatic control in Lund University for his insightful discussions and suggestions.
