<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Risk-sensitive Safety Analysis Using Conditional Value-at-Risk

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

This paper develops a safety analysis method for stochastic systems that is sensitive to the possibility and severity of rare harmful outcomes. We define risk-sensitive safe sets as sub-level sets of the solution to a non-standard optimal control problem, where a random maximum cost is assessed via Conditional Value-at-Risk (CVaR). The objective function represents the maximum extent of constraint violation of the state trajectory, averaged over a given percentage of worst cases. This problem is well-motivated but difficult to solve tractably because the temporal decomposition for CVaR is history-dependent. Our primary theoretical contribution is to derive computationally tractable under-approximations to risk-sensitive safe sets. Our method provides a novel, theoretically guaranteed, parameter-dependent upper bound to the CVaR of a maximum cost without the need to augment the state space. For a fixed parameter value, the solution to only one Markov decision process problem is required to obtain the under-approximations for any family of risk-sensitivity levels. In addition, we propose a second definition for risk-sensitive safe sets and provide a tractable method for their estimation without using a parameter-dependent upper bound.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

The second definition is expressed in terms of a new coherent risk functional, which is inspired by CVaR. We demonstrate our primary theoretical contribution via numerical examples.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

Control-theoretic formal verification methods for dynamical systems typically fall in the robust domain or in the stochastic domain. Robust methods for formal verification assume that uncertain disturbances lack probabilistic descriptions, live in bounded sets, and exhibit adversarial behavior. These assumptions are appropriate if probabilistic information about disturbances is not available, and if the conservative policy or safety specification that results from a pessimistic world view is useful in practice. However, when one considers formal verification as a design tool for safety-critical systems in the digital world today, it is reasonable to assume that simulation tools or sensor data are available to estimate probabilistic descriptions for disturbances. Moreover, it is reasonable to consider the following world view: disturbances need not be adversarial, but rare harmful outcomes are still possible.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

Control-theoretic stochastic formal verification methods do assume that disturbances are probabilistic and can be non-adversarial or adversarial in nature. These methods compute the probability of safety or performance by using expected indicator cost functions. The expectation, however, is not designed to quantify the features in the tails of a distribution, and the probability of a harmful outcome need not indicate its severity. Thus, formal verification methods at the intersection of the robust and stochastic domains are emerging. A method for distributionally robust safety analysis has been proposed, and methods that use risk measures to assess harmful tail costs, e.g., and our prior work, have been introduced.^11^1A *risk measure* (risk functional) is a map from a set of random variables to the extended real line. Exponential utility, Value-at-Risk, CVaR, and Mean-Deviation are examples. The terms risk measure and risk functional are interchangeable.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

While the notion of risk-sensitive formal verification is recent, it is related to the notion of risk-sensitive Markov decision processes (MDPs), which dates back to the early 1970s. In 1972, Howard and Matheson studied risk-sensitive MDPs on finite state spaces, where the cost is evaluated in terms of exponential utility. This idea was transferred to linear control systems by Jacobson in 1973 and was further developed in later decades. For example, see the seminal works by Whittle and di Masi and Stettner. The exponential utility of a non-negative random cost $Y$ ${\mathcal{J}_{\theta}{(Y)}} ≔ {\frac{- 2}{\theta}{\log{({E{(e^{\frac{- \theta}{2}Y})}})}}}$ assesses the risk of $Y$ in terms of the moments of $Y$ and is parametrized by a non-zero scalar $\theta$.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

Under appropriate conditions, $\mathcal{J}_{\theta}{(Y)}$ tends to $E{(Y)}$ as $\theta\rightarrow 0$ and ${\mathcal{J}_{\theta}{(Y)}} \approx {{E{(Y)}} - {\frac{\theta}{4}\text{Variance}{(Y)}}}$ if $|\theta|$ is sufficiently small. The risk-averse setting corresponds to $\theta < 0$. However, if $\theta$ is too negative, the controller can suffer from a phenomenon called "neurotic breakdown" in the linear-quadratic-Gaussian setting.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Introduction", "weight": 1.5} -->

Hence, the notion of risk-sensitive MDPs has been generalized beyond exponential utility. Kreps used the expectation of a utility function as a risk-sensitive performance criterion for MDPs. Ruszczyński defined a risk-sensitive performance criterion for MDPs in terms of a composition of risk measures. State-space augmentation has been used to optimize the cumulative cost of a MDP, where the cost is assessed via CVaR or a certainty equivalent risk measure. The former problem is called a CVaR-MDP. Convex analytic methods have been used to solve MDPs with expected utility or CVaR criteria via state-space augmentation and infinite-dimensional linear programming. A temporal decomposition for CVaR has been used to propose a dynamic programming (DP) algorithm on an augmented state space to solve a CVaR-MDP problem approximately. Analysis at the intersection of mean field games, linear systems, and risk measures with connections to CVaR is provided.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Introduction", "weight": 1.5} -->

Ruszczyński's approach and MDPs that assess cumulative costs via expectation or exponential utility are *time-consistent* problems. That is, these problems satisfy Bellman's Principle of Optimality on the original state space.^22^2Different meanings for time consistency have been proposed, e.g., see. We refer to the meaning for time consistency. However, a CVaR-MDP is time-inconsistent. Several solution concepts for time-inconsistent problems have been proposed. For example, a game-theoretic solution concept is studied, which considers the problem as a game against one's future self. Another popular approach is to focus on *pre-commitment strategies* that cannot be revised at later stages. Optimal or nearly optimal pre-commitment strategies can be obtained using the structure of CVaR; see, for example. Although an optimal pre-commitment strategy is globally optimal only at the initial stage, maintaining suitable empirical performance at later stages is possible, particularly when the time horizon is not too long. In mean-CVaR asset allocation problems, optimal pre-commitment strategies are shown to be effective even with long time horizons.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Introduction", "weight": 1.5} -->

A line of research that falls between risk-sensitive MDPs and standard risk-neutral MDPs is risk-constrained MDPs. Here, the goal is to minimize an expected cumulative cost subject to a risk constraint that limits the extent of a cost. Refs., for example, express this constraint in terms of CVaR.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Introduction", "weight": 1.5} -->

The additional effort required to solve time-inconsistent problems, including CVaR-MDPs, may be justified for safety-critical applications. A strong theoretical basis for using CVaR to assess harmful tail costs has been in development since the early 2000s, e.g., see and the references therein. Informally, CVaR represents the expected cost in the $\alpha \cdot 100$% worst cases, where $\alpha \in {(0,1\rbrack}$ (Fig. 1). CVaR quantifies the more harmful tail of a distribution, and managing this tail is paramount in safety-critical applications.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Introduction", "weight": 1.5} -->

This paper proposes a method to assess how well a stochastic system can remain within a desired operating region with respect to a range of worst-case perspectives. We call this method *risk-sensitive safety analysis* (Fig. 2). Its foundation is a non-standard optimal control problem that evaluates a random maximum cost via CVaR. The objective function represents the maximum extent of constraint violation of the state trajectory, averaged over the $\alpha \cdot 100$% worst cases, where $\alpha \in {(0,1\rbrack}$ is a *risk-sensitivity level*. This problem is difficult to solve tractably because the temporal decomposition for CVaR is history-dependent. We define risk-sensitive safe sets as sub-level sets of the solution to this non-standard problem. These sets are powerful tools for safety analysis. Indeed, they assess system behavior on a spectrum of worst cases, while being sensitive to the possibility and severity of rare harmful outcomes.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Introduction", "weight": 1.5} -->

Our primary theoretical contribution is to derive computationally tractable under-approximations to risk-sensitive safe sets. We derive these under-approximations by proving the following: for any control policy and any initial state, the CVaR of a maximum cost is upper bounded by a scaled logarithm of an expected cumulative cost, where the stage cost has a specific analytical form. For this proof, we use various properties of CVaR and the log-sum-exponential approximation to the maximum. The latter approximation depends on a parameter, $\gamma \in {\mathbb{R}}$. For a fixed $\gamma$, the solution to one MDP problem is required to obtain the under-approximations for any family of risk-sensitivity levels. We provide practical insights on how to choose such a parameter in the experimental section.

<!-- chunk {"id": "body-0014", "role": "body", "section": "Introduction", "weight": 1.5} -->

Our method provides a novel, theoretically guaranteed upper bound to the CVaR of a *maximum* cost for the purpose of *safety analysis* without the need to augment the state space. (Augmenting the state space may be less tractable in some settings, e.g., when the range of the augmented state is large.) In contrast, existing methods aim to compute the CVaR of a cumulative cost via state-space augmentation. By taking different approaches to augment the state space, Refs. and minimize the CVaR of a cumulative cost, and Ref. minimizes the CVaR of a cumulative cost approximately. These related works are focused on controller synthesis but are not focused on safety analysis.

<!-- chunk {"id": "body-0015", "role": "body", "section": "Introduction", "weight": 1.5} -->

Our secondary theoretical contribution is to propose a second definition for risk-sensitive safe sets and provide a tractable method for their estimation without using a parameter-dependent upper bound. The second definition is expressed in terms of a new risk functional, which is inspired by CVaR and has certain desirable properties. In particular, we prove that this risk functional admits an upper bound that can be computed via DP (on the original state space and without an additional parameter that requires tuning). This result forges a new path to estimate risk-sensitive safety criteria with desirable computational attributes.

<!-- chunk {"id": "body-0016", "role": "body", "section": "Introduction", "weight": 1.5} -->

*Organization*. We present notation and background on CVaR in Sec. 2. Our primary and secondary theoretical contributions are provided in Sec. 3 and Sec. 4, respectively. We develop computational examples of a temperature system and a stormwater system to demonstrate our primary theoretical contribution in Sec. 5. Sec. 6 presents conclusions and directions for future work.

<!-- chunk {"id": "body-0017", "role": "body", "section": "CVaR-Based Risk-Sensitive Safety Analysis", "weight": 1.0} -->

We use the CVaR functional to pose a safety analysis problem. We consider a stochastic system evolving on a discrete, finite-time horizon and start with the standard set-up for this setting. Let $S$ and $A$ be Borel spaces, representing the set of states and the set of controls of the system, respectively. Define the sample space $\Omega ≔ {{({S \times A})}^{T} \times S}$, where $\omega ≔ {(x_{0},u_{0},\ldots,x_{T - 1},u_{T - 1},x_{T})} \in \Omega$ is a finite sequence of states and controls that may be realized on a time horizon of length $T + 1$ and $T \in {\mathbb{N}}$ is given. The random state $X_{t}:{\Omega\rightarrow S}$ and the random control $U_{t}:{\Omega\rightarrow A}$ are projections.

<!-- chunk {"id": "body-0018", "role": "body", "section": "CVaR-Based Risk-Sensitive Safety Analysis", "weight": 1.0} -->

That is, for any $\omega \in \Omega$ of the form above, define ${X_{t}{(\omega)}} ≔ x_{t}$ and ${U_{t}{(\omega)}} ≔ u_{t}$, where the coordinates of $\omega$ have casual dependencies, to be described. The initial state $X_{0}$ is fixed arbitrarily at $x \in S$. The system's evolution is affected by $W$-valued random disturbances $(D_{0},D_{1},\ldots,D_{T - 1})$ with a common distribution $P_{D}$, where $W$ is a Borel space. $D_{t}$ is independent of the states, controls, and $D_{s}$ for any $s \neq t$.

<!-- chunk {"id": "body-0019", "role": "body", "section": "CVaR-Based Risk-Sensitive Safety Analysis", "weight": 1.0} -->

where $f:{{S \times A \times W}\rightarrow S}$ is a Borel-measurable map that models the system dynamics. We use the typical class of random, history-dependent policies $\Pi$. Each $\pi \in \Pi$ takes the form $\pi = {(\pi_{0},\pi_{1},\ldots,\pi_{T - 1})}$, where each $\pi_{t}$ is a Borel-measurable stochastic kernel on $A$ given $H^{t} ≔ {{({S \times A})}^{t} \times S}$.

<!-- chunk {"id": "body-0020", "role": "body", "section": "CVaR-Based Risk-Sensitive Safety Analysis", "weight": 1.0} -->

The above set-up is standard in discrete-time stochastic control. One reason is that, given $x \in S$ and $\pi \in \Pi$, the set-up allows the construction of a unique probability measure $P_{x}^{\pi}$ that characterizes the system's evolution, provided that the system is initialized at $x$ and uses the policy $\pi$ (Ionescu-Tulcea Theorem). The measure $P_{x}^{\pi}$ permits the prediction of the system's performance over time under uncertainty. Random costs incurred by the system are defined on $(\Omega,{\mathcal{B}{(\Omega)}},P_{x}^{\pi})$, a probability space parametrized by $x$ and $\pi$. The notation $E_{x}^{\pi}{( \cdot )}$ is the expectation operator with respect to $P_{x}^{\pi}$.

<!-- chunk {"id": "body-0021", "role": "body", "section": "On Evaluating a Random Cost via CVaR", "weight": 1.0} -->

We use $(\Omega,{\mathcal{B}{(\Omega)}},P_{x}^{\pi})$ to define a random cost for the system and to evaluate this cost via CVaR. Suppose that there is a *constraint set* $K \in {\mathcal{B}{(S)}}$, where the state trajectory $(X_{0},X_{1},\ldots,X_{T})$ of the system should remain inside. It may be impossible for the system to remain inside $K$ always due to random disturbances in the environment. Let $g_{K}:{S\rightarrow{\mathbb{R}}}$ be a bounded Borel-measurable function that represents a notion of distance between a state realization and the boundary of $K$. Specifically, $g_{K}{(x_{t})}$ is the *extent of constraint violation* of $x_{t}$, a realization of the random state $X_{t}$.

<!-- chunk {"id": "body-0022", "role": "body", "section": "On Evaluating a Random Cost via CVaR", "weight": 1.0} -->

More specifically, if $x_{t}$ is outside of $K$ and far from the boundary of $K$, then $g_{K}{(x_{t})}$ has a large positive value. However, if $x_{t}$ is inside of $K$, then $g_{K}{(x_{t})}$ may be

<!-- chunk {"id": "body-0023", "role": "body", "section": "On Evaluating a Random Cost via CVaR", "weight": 1.0} -->

zero, if one does not favor certain trajectories inside of $K$, or

<!-- chunk {"id": "body-0024", "role": "body", "section": "On Evaluating a Random Cost via CVaR", "weight": 1.0} -->

a more negative value when $x_{t}$ is more deeply inside of $K$, if one favors trajectories that remain deeply inside of $K$.

<!-- chunk {"id": "body-0025", "role": "body", "section": "On Evaluating a Random Cost via CVaR", "weight": 1.0} -->

Using $g_{K}$, we define a random $\mathbb{R}$-valued cost that quantifies the *maximum extent of constraint violation of the state trajectory*: for any $\omega = {(x_{0},u_{0},\ldots,x_{T - 1},u_{T - 1},x_{T})} \in \Omega$,

<!-- chunk {"id": "body-0026", "role": "body", "section": "On Evaluating a Random Cost via CVaR", "weight": 1.0} -->

In other words, $G$ quantifies how well the random state trajectory satisfies the safety criterion to remain inside of $K$. Hence, $G$ quantifies the safety of the random state trajectory, which is defined with respect to the constraint set $K$ via the function $g_{K}$. A deterministic (and continuous-time) version of is used in Hamilton-Jacobi reachability analysis, a robust safety analysis method for (non-stochastic) uncertain systems, which has been established over the past 15 years; e.g., see, and the references therein. A standard choice for $g_{K}$ is a clipped signed distance function with respect to $K$ \[43, p. 8\].

<!-- chunk {"id": "body-0027", "role": "body", "section": "On Evaluating a Random Cost via CVaR", "weight": 1.0} -->

In our numerical example of a thermostatically controlled load, we use ${g_{K}{(x_{t})}} = {\max{({x_{t} - 21},{20 - x_{t}})}}$ to quantify how far a state realization $x_{t}$ can be inside or outside of $K = {\lbrack 20,21\rbrack}$ ^∘^C (Sec. 5.1).

<!-- chunk {"id": "body-0028", "role": "body", "section": "On Evaluating a Random Cost via CVaR", "weight": 1.0} -->

We use and to define risk-sensitive safe sets next.

<!-- chunk {"id": "body-0029", "role": "body", "section": "Under-Approximation Method", "weight": 1.0} -->

Risk-sensitive safe sets are well-motivated but difficult to compute due to the presence of the CVaR and the maximum. Before presenting our approach to estimate risk-sensitive safe sets, we describe related methods in further detail.

<!-- chunk {"id": "body-0030", "role": "body", "section": "Under-Approximation Method", "weight": 1.0} -->

Several methods in the literature apply state-space augmentation techniques to estimate the risk of a random cost incurred by a MDP.^55^5An approach that does not require state-space augmentation is to evaluate a cumulative cost via a composition of risk functionals. We take inspiration from this idea in Sec. 4. Bäuerle and Ott use dynamic programming (DP) to minimize the CVaR of a sum of stage costs by defining an augmented state space. The range of the second state is $\lbrack 0,{\text{ess}{\sup{\sum_{t = 0}^{T}C_{t}}}}\rbrack$, where $C_{t}$ is the stage cost at time $t$ \[16, Remark 5.1\]. This state-space augmentation approach has been extended to optimize certainty equivalent risk functionals for MDPs. A certainty equivalent approximates the sum of the expectation and a function of the variance under particular conditions, and more generally, characterizes risk aversion in terms of functions of moments.

<!-- chunk {"id": "body-0031", "role": "body", "section": "Under-Approximation Method", "weight": 1.0} -->

However, CVaR provides a quantitative characterization of risk aversion by penalizing a random cost in a given fraction of the worst cases.

<!-- chunk {"id": "body-0032", "role": "body", "section": "Under-Approximation Method", "weight": 1.0} -->

Chow et al. proposed a DP algorithm to minimize approximately the CVaR of a cumulative cost via state-space augmentation, where the additional state ranges from 0 to 1. This approach is expected to be more tractable than the approach; compare the ranges of the additional states. However, it is not known if the algorithm in provides an upper bound or a lower bound to the solution to a CVaR-MDP problem. The algorithm in is based on a CVaR Decomposition Theorem \[40, Thm. 6\] \[41, Thm. 21, Lemma 22\], which requires knowledge of the history of a stochastic process. How to remove the history dependence and apply the Decomposition Theorem to derive the algorithm in is still an open research question.

<!-- chunk {"id": "body-0033", "role": "body", "section": "Under-Approximation Method", "weight": 1.0} -->

The algorithms invented by aim to minimize the CVaR of a *cumulative* cost subject to the dynamics of a MDP. The algorithm proposed by aims to minimize the CVaR of a more general cost (not necessarily a sum) but is history-dependent, which limits its computational tractability. The proof of the DP algorithm in requires an exchange between an essential supremum and an expectation, whose validity in multi-stage settings for MDPs with Borel state and control spaces is not known.

<!-- chunk {"id": "body-0034", "role": "body", "section": "Under-Approximation Method", "weight": 1.0} -->

Here, we propose a method to provide tractable, theoretically guaranteed under-approximations to risk-sensitive safe sets, which we define via CVaR. We focus on CVaR due to its *quantitative characterization of risk aversion* and since we aim to assess the degree of safety of a control system in terms of rarer, higher-consequence outcomes. In contrast, a certainty equivalent assesses risk in terms of functions of variance and other moments. In particular, variance does not distinguish between rarer, higher-consequence outcomes in the upper tail and rarer, lower-consequence outcomes in the lower tail. Unlike the methods, our method does not use state-space augmentation because this technique typically reduces computational tractability. For this reason, we do not augment the state space with the running maximum over each time period $Z_{t} ≔ {{\max_{i = {0,1,\ldots,t}}g_{K}}{(X_{i})}}$. The range of $Z_{t}$ may be large since the bounds of $g_{K}$ may be large.

<!-- chunk {"id": "body-0035", "role": "body", "section": "Under-Approximation Method", "weight": 1.0} -->

Instead of using state-space augmentation to handle the CVaR and the maximum, we use a scaled expectation to upper bound the CVaR and a log-sum-exponential function to upper bound the maximum, $G ≔ {{\max_{t = {0,1,\ldots,T}}g_{K}}{(X_{t})}}$. Our first main result is below.

<!-- chunk {"id": "body-0036", "role": "body", "section": "Remark 3.11 (Assessment of Approximation Errors)", "weight": 1.0} -->

Three approximations are required for the proof above. First, we use a soft-maximum, under which we have

<!-- chunk {"id": "body-0037", "role": "body", "section": "Remark 3.11 (Assessment of Approximation Errors)", "weight": 1.0} -->

where $Y = {\sum_{t = 0}^{T}e^{\gammag_{K}{(X_{t})}}}$, and there are positive constants $\underset{¯}{b}$ and $\overline{b}$ (which depend on $T$, $\gamma$, and the bounds of $g_{K}$) such that $Y \in {\lbrack\underset{¯}{b},\overline{b}\rbrack}$ everywhere. The inequality (36. ‣ 3.3 Under-Approximation Method ‣ 3 CVaR-Based Risk-Sensitive Safety Analysis ‣ Risk-sensitive safety analysis using Conditional Value-at-Risk*")) implies an improved approximation with larger values of $\gamma$ or smaller values of $T$.

<!-- chunk {"id": "body-0038", "role": "body", "section": "Remark 3.11 (Assessment of Approximation Errors)", "weight": 1.0} -->

However, since it is not feasible to optimize $\frac{1}{\gamma}\text{CVaR}_{\alpha,x}^{\pi}{({\log{(Y)}})}$ directly, our next step is to leverage the CVaR-log inequality provided by Lemma 3.5. ‣ 3.3 Under-Approximation Method ‣ 3 CVaR-Based Risk-Sensitive Safety Analysis ‣ Risk-sensitive safety analysis using Conditional Value-at-Risk*"). The associated error is given by

<!-- chunk {"id": "body-0039", "role": "body", "section": "Remark 3.11 (Assessment of Approximation Errors)", "weight": 1.0} -->

Since the range of $Y$ is $\lbrack\underset{¯}{b},\overline{b}\rbrack$, it follows that $\eta_{\alpha,x}^{\pi,\gamma} \leq {\frac{1}{\gamma}{\log{({\overline{b}/\underset{¯}{b}})}}}$. Therefore, we anticipate a smaller error $\eta_{\alpha,x}^{\pi,\gamma}$ when $Y$ has a smaller range, which occurs when $T$ is smaller, for example.

<!-- chunk {"id": "body-0040", "role": "body", "section": "Remark 3.11 (Assessment of Approximation Errors)", "weight": 1.0} -->

The last approximation is ${\log{({\text{CVaR}_{\alpha,x}^{\pi}{(Y)}})}} \leq {\log\left( {\frac{1}{\alpha}E_{x}^{\pi}{(Y)}} \right)}$, which of course is poor as $\alpha\rightarrow 0$. However, for a fixed $\alpha \in {}$, we anticipate that this approximation performs well when $P_{x}^{\pi}$ has a fat (upper) tail, which we state formally in the following lemma.

<!-- chunk {"id": "body-0041", "role": "body", "section": "Remark 3.13 (Fat tail condition ≤log({1/𝛼}⁢𝐸⁢(𝑌))). ‣ 3.3 Under-Approximation Method ‣ 3 CVaR-Based Risk-Sensitive Safety Analysis ‣ Risk-sensitive safety analysis using Conditional Value-at-Risk*\")))", "weight": 1.0} -->

The second inequality in ≤log({1/𝛼}⁢𝐸⁢(𝑌))). ‣ 3.3 Under-Approximation Method ‣ 3 CVaR-Based Risk-Sensitive Safety Analysis ‣ Risk-sensitive safety analysis using Conditional Value-at-Risk*")) means that the cumulative VaR in the upper $\alpha$-fraction of the distribution of $Y$, $\int_{1 - \alpha}^{1}{\text{VaR}_{1 - p}{(Y)}{dp}}$, is at least $m$ times greater than the cumulative VaR in the lower $({1 - \alpha})$-fraction of the distribution of $Y$, $\int_{0}^{1 - \alpha}{\text{VaR}_{1 - p}{(Y)}{dp}}$. The maximum value of $m$ that satisfies ≤log({1/𝛼}⁢𝐸⁢(𝑌))).

<!-- chunk {"id": "body-0042", "role": "body", "section": "Remark 3.13 (Fat tail condition ≤log({1/𝛼}⁢𝐸⁢(𝑌))). ‣ 3.3 Under-Approximation Method ‣ 3 CVaR-Based Risk-Sensitive Safety Analysis ‣ Risk-sensitive safety analysis using Conditional Value-at-Risk*\")))", "weight": 1.0} -->

‣ 3.3 Under-Approximation Method ‣ 3 CVaR-Based Risk-Sensitive Safety Analysis ‣ Risk-sensitive safety analysis using Conditional Value-at-Risk*")) is $\hat{m} = \frac{\int_{1 - \alpha}^{1}{\text{VaR}_{1 - p}{(Y)}{dp}}}{\int_{0}^{1 - \alpha}{\text{VaR}_{1 - p}{(Y)}{dp}}}$, which gives a measure of tail "fatness." For example, if the distribution of $Y$ is a standard log-normal with parameters $\mu = 0$ and $\sigma = 1$, and if $\alpha = 0.05$, then numerical integration yields ${\hat{m} \approx \frac{0.42}{1.2} \approx 0.35}.$ If $\sigma$ is increased to 2 under the same conditions, then $\hat{m} \approx \frac{4.7}{2.7} \approx 1.7$.

<!-- chunk {"id": "body-0043", "role": "body", "section": "Remark 3.13 (Fat tail condition ≤log({1/𝛼}⁢𝐸⁢(𝑌))). ‣ 3.3 Under-Approximation Method ‣ 3 CVaR-Based Risk-Sensitive Safety Analysis ‣ Risk-sensitive safety analysis using Conditional Value-at-Risk*\")))", "weight": 1.0} -->

Next, we prove Lemma 3.12)≤log({1/𝛼}⁢𝐸⁢(𝑌))). ‣ 3.3 Under-Approximation Method ‣ 3 CVaR-Based Risk-Sensitive Safety Analysis ‣ Risk-sensitive safety analysis using Conditional Value-at-Risk*").\

<!-- chunk {"id": "body-0044", "role": "body", "section": "Toward a Parameter-Independent Safety Analysis Framework", "weight": 1.0} -->

Previously, we have defined risk-sensitive safe sets in terms of the CVaR of a maximum random cost. However, this risk-sensitive safety criterion is difficult to optimize exactly without using state-space augmentation, which motivated us to derive a parameter-dependent upper bound. One may wonder whether there is another coherent risk functional (ideally related to CVaR) that admits an upper bound, which can be computed via DP on the original state space without an additional parameter that requires tuning. The answer is indeed positive, as presented below.

<!-- chunk {"id": "body-0045", "role": "body", "section": "Remark 4.17 (Interpretation for $\\rho_{\\alpha,x}^{\\pi}$)", "weight": 1.0} -->

Although we do not yet have an exact interpretation for $\rho_{\alpha,x}^{\pi}$, we provide a preliminary interpretation here. The quantity $\rho_{\alpha,x}^{\pi}{(Y)}$ is a distributionally robust expectation of $Y$, such that an uncertainty $\xi_{t}$ perturbs the system's nominal transition law $Q$ at each time $t$. $\xi_{t}$ may depend on the current time, state, and control. Moreover, $\rho_{\alpha,x}^{\pi}{(Y)}$ strikes a balance between the expectation and CVaR, as formalized below.

<!-- chunk {"id": "body-0046", "role": "body", "section": "Assumption 2 (Continuity property of $Q$)", "weight": 1.0} -->

The transition kernel $Q$ is continuous in total variation; that is, if ${(x_{n},u_{n})}\rightarrow{(x,u)}$, then $|Q{( \cdot |x_{n},u_{n})} - Q{( \cdot |x,u)}|{(S)}\rightarrow 0$.

<!-- chunk {"id": "body-0047", "role": "body", "section": "Remark 4.21 (Example that satisfies Assumption 2 ‣ 4 Toward a Parameter-Independent Safety Analysis Framework ‣ Risk-sensitive safety analysis using Conditional Value-at-Risk*\"))", "weight": 1.0} -->

Suppose that $P_{D}$ has a continuous non-negative density and $f$ in has the form ${f{(x,u,d)}} = {{f_{1}{(x,u)}} + {{d \cdot f_{2}}{(x,u)}}}$, where $W = S$ is a vector space with field $\mathbb{R}$, $f_{1}:{{S \times A}\rightarrow S}$ and $f_{2}:{{S \times A}\rightarrow{\mathbb{R}}}$ are continuous, and $f_{2}$ is non-zero. Then, by Scheffé's Lemma, Assumption 2 ‣ 4 Toward a Parameter-Independent Safety Analysis Framework ‣ Risk-sensitive safety analysis using Conditional Value-at-Risk*") is satisfied. We note that continuity of $f$ is a typical condition in stochastic control, e.g., see \[15, p.

<!-- chunk {"id": "body-0048", "role": "body", "section": "Remark 4.21 (Example that satisfies Assumption 2 ‣ 4 Toward a Parameter-Independent Safety Analysis Framework ‣ Risk-sensitive safety analysis using Conditional Value-at-Risk*\"))", "weight": 1.0} -->

209\], and requiring additional structure on the dynamics to achieve tractable algorithms is standard. For example, under some assumptions the dynamics may be decomposed into overlapping systems, to obtain conservative under-approximations to reachable sets for continuous-time, non-stochastic systems. A mixed monotone structure has been assumed to approximate reachable sets for discrete-time non-stochastic systems, with applications to traffic safety. More broadly, additive continuous noise is a realistic assumption in many domains, e.g., additive Gaussian noise in information theory and control (classical references include ) and additive Brownian motion in continuous-time epidemiological modeling.

<!-- chunk {"id": "body-0049", "role": "body", "section": "Remark 4.21 (Example that satisfies Assumption 2 ‣ 4 Toward a Parameter-Independent Safety Analysis Framework ‣ Risk-sensitive safety analysis using Conditional Value-at-Risk*\"))", "weight": 1.0} -->

Boundedness and upper semi-continuity of $c_{t}$ for all $t$ ensures that $Y \in {L^{\infty}{(\Omega,{\mathcal{B}{(\Omega)}},P_{x}^{\pi})}}$ for any $x \in S$ and $\pi \in \Pi$. Also, boundedness of $c_{t}$ ensures that the iterates of a DP recursion are bounded, which we use to show that a supremum over $\mathcal{R}_{\alpha}{(x,u)}$ of the form $\phi{(x,u)} ≔ \sup_{\xi \in {\mathcal{R}_{\alpha}{(x,u)}}}\int_{S}J\xi dQ{( \cdot |x,u)}$ is attained (Lemma 6.23. ‣ Appendix ‣ Risk-sensitive safety analysis using Conditional Value-at-Risk*"), Appendix).

<!-- chunk {"id": "body-0050", "role": "body", "section": "Remark 4.21 (Example that satisfies Assumption 2 ‣ 4 Toward a Parameter-Independent Safety Analysis Framework ‣ Risk-sensitive safety analysis using Conditional Value-at-Risk*\"))", "weight": 1.0} -->

This attainment and Assumption 2 ‣ 4 Toward a Parameter-Independent Safety Analysis Framework ‣ Risk-sensitive safety analysis using Conditional Value-at-Risk*") together guarantee that the supremum is usc in $(x,u)$ (Lemma 6.27. ‣ Appendix ‣ Risk-sensitive safety analysis using Conditional Value-at-Risk*"), Appendix). The upper semi-continuity of the supremum permits the derivation of an upper bound for $\inf_{\pi \in \Pi}{\rho_{\alpha,x}^{\pi}{(Y)}}$ via DP.

<!-- chunk {"id": "body-0051", "role": "body", "section": "Numerical Examples", "weight": 1.0} -->

Here, we present examples of risk-sensitive safe sets and their under-approximations as in Definition 1 ‣ 3.2 Risk-Sensitive Safe Sets ‣ 3 CVaR-Based Risk-Sensitive Safety Analysis ‣ Risk-sensitive safety analysis using Conditional Value-at-Risk*") for a temperature system and a stormwater system.^77^7We used the Tufts Linux Research Cluster (Medford, MA) with MATLAB (The Mathworks, Inc.). Our code is available from For each example, we have chosen a value of $\gamma$ by exploring increasing integer values and then stopping the exploration when improvements in the estimates of $\mathcal{U}_{\alpha,\gamma}^{r}$ were no longer apparent.

<!-- chunk {"id": "body-0052", "role": "body", "section": "Temperature System", "weight": 1.0} -->

Consider a thermostatically controlled load evolving on a finite-time horizon $t = {0,1,\ldots,{T - 1}}$ via a deterministic Markov policy $\pi = {(\pi_{0},\pi_{1},\ldots,\pi_{T - 1})}$,

<!-- chunk {"id": "body-0053", "role": "body", "section": "Temperature System", "weight": 1.0} -->

This model is. $X_{t}$ is the $\mathbb{R}$-valued random temperature (${}_{}^{}{}$) of a thermal mass at time $t$. $\pi_{t}{(X_{t})}$ is the $\lbrack 0,1\rbrack$-valued control at time $t$. The amount of power supplied to the system decreases as the value of the control increases from 0 to 1. $(D_{0},D_{1},\ldots,D_{T - 1})$ is a $\mathbb{R}$-valued, iid stochastic process that arises due to environmental uncertainties. We consider three discrete distributions for the disturbance process, where each distribution has a distinct skew (left skew, no skew, or right skew). In each distribution, the minimum disturbance value is $- 0.5$ ${}_{}^{}{}$, and the maximum disturbance value is 0.5 ${}_{}^{}{}$.

<!-- chunk {"id": "body-0054", "role": "body", "section": "Temperature System", "weight": 1.0} -->

Table 1 provides the model parameters.

<!-- chunk {"id": "body-0055", "role": "body", "section": "Temperature System", "weight": 1.0} -->

range of energy transfer to/from thermal mass

<!-- chunk {"id": "body-0056", "role": "body", "section": "Temperature System", "weight": 1.0} -->

We have chosen ${g_{K}{(X_{t})}} = {\max{({X_{t} - 21},{20 - X_{t}})}}$ to quantify the extent of constraint violation of the state $X_{t}$ with respect to the constraint set $K = {\lbrack 20,21\rbrack}$ ${}_{}^{}{}$. $K$ is a temperature range, where the state trajectory should remain inside whenever possible. For different values of $\gamma$ (see next paragraph), we have implemented classical DP with linear interpolation to estimate

<!-- chunk {"id": "body-0057", "role": "body", "section": "Temperature System", "weight": 1.0} -->

and a deterministic Markov policy $\pi_{\gamma} \in \Pi$ such that ${J_{\gamma}^{\ast}{(x)}} = {J_{\gamma}{(x,\pi_{\gamma})}}$ for all $x \in S$. DP on continuous state and control spaces is implemented typically via discretization and interpolation. In particular, we have discretized the set of controls $A = {\lbrack 0,1\rbrack}$ and the set of states $S = {\lbrack 18,23\rbrack}$ ${}_{}^{}{}$ uniformly at a resolution of 0.1. To improve efficiency of DP, approximate DP methods are being developed, e.g., see, and the references therein. While these methods are exciting, we leave investigations of their applicability to risk-sensitive safety analysis for future work.

<!-- chunk {"id": "body-0058", "role": "body", "section": "Temperature System", "weight": 1.0} -->

We have used $\gamma \in \Gamma ≔ {\{ 3,4,\ldots,20\}}$ because for all $y \in S$ and $\gamma \in \Gamma$, the stage cost $e^{\gammag_{K}{(y)}}$ is at most $e^{20 \cdot 2}$, a large number that a personal computer can handle. We have considered risk-sensitivity levels from nearly risk-neutral ($\alpha = 0.99$) to more risk-averse ($\alpha$ near 0). Specifically, we have chosen $\alpha \in \Lambda ≔ {\{ 0.99,0.05,0.01,0.005,0.001\}}$. A typical risk-sensitivity level is $\alpha = 0.05$ or $\alpha = 0.01$, and we have considered smaller values of $\alpha$ as well.

<!-- chunk {"id": "body-0059", "role": "body", "section": "Temperature System", "weight": 1.0} -->

For $\gamma \in \Gamma$ and $\alpha \in \Lambda$, we have estimated $J_{\alpha,\gamma}^{\ast}$ by dividing our estimate of $J_{\gamma}^{\ast}$ by $\alpha$. Let $\hat{S}$ denote the state space grid. By using our estimate of $\pi_{\gamma}$, we have simulated 100,000 trajectories from each initial state $x \in \hat{S}$ to generate an empirical distribution of $G ≔ {{\max_{t = {0,1,\ldots,T}}g_{K}}{(X_{t})}}$. Then, for each $\alpha \in \Lambda$, we have used a consistent CVaR estimator \[37, p. 300\] to estimate $\text{CVaR}_{\alpha,x}^{\pi_{\gamma}}{(G)}$.

<!-- chunk {"id": "body-0060", "role": "body", "section": "Temperature System", "weight": 1.0} -->

Fig. 3 provides a visual summary of the inequality that we have proved in Theorem 3.2. ‣ 3.3

<!-- chunk {"id": "body-0061", "role": "body", "section": "Temperature System", "weight": 1.0} -->

Each plot in Fig. 3 shows estimates of the right-hand-side of on the vertical axis versus estimates of the left-hand-side of on the horizontal axis for the 5 values of $\alpha$ in $\Lambda$. In each plot, each solid colored line consists of 5 points, one for each $\alpha \in \Lambda$. Points associated with smaller values of $\alpha$ (more risk-averse) are positioned farther away from the origin. In each plot, there are three solid colored lines, one for each distribution of the disturbance process. In each plot, $\gamma \in \Gamma$ and an initial state $x \in \hat{S}$ are fixed. We have chosen initial states inside or on the boundary of the constraint set $K = {\lbrack 20,21\rbrack}$ ${}_{}^{}{}$. Fig. 3 is consistent with the inequality that we have proved in Theorem 3.2.

<!-- chunk {"id": "body-0062", "role": "body", "section": "Temperature System", "weight": 1.0} -->

‣ 3.3 Under-Approximation Method ‣ 3 CVaR-Based Risk-Sensitive Safety Analysis ‣ Risk-sensitive safety analysis using Conditional Value-at-Risk*") since the solid colored lines are located above the gray line of slope 1. Fig. 3 suggests that there is no unique value of $\gamma$ that provides the best approximation for all initial states $x$, risk-sensitivity levels $\alpha$, and disturbance distributions.

<!-- chunk {"id": "body-0063", "role": "body", "section": "Temperature System", "weight": 1.0} -->

However, by Theorem 3.9, we have flexibility in choosing the value of $\gamma$. In particular, we favor the quality of the approximations for small values of $\alpha$ due to our focus on safety and present sets using $\gamma = 14$ as an example of a value that reflects this preference (Fig. 4).^88^8Higher-quality approximations are those in which the estimates of the under-approximations are generally closer to the estimates of the risk-sensitive safe sets when considering all three disturbance distributions. We suggest an approach to quantify the quality of the approximations in Fig. 4. Fig. 4 provides estimates of the $(\alpha,r)$-risk-sensitive safe set for $\pi_{\gamma} \in \Pi$ (9 ‣ 3.2 Risk-Sensitive Safe Sets ‣ 3 CVaR-Based Risk-Sensitive Safety Analysis ‣ Risk-sensitive safety analysis using Conditional Value-at-Risk*"))

<!-- chunk {"id": "body-0064", "role": "body", "section": "Temperature System", "weight": 1.0} -->

and the $(\alpha,r,\gamma)$-under-approximation set (22. ‣ 3.3 Under-Approximation Method ‣ 3 CVaR-Based Risk-Sensitive Safety Analysis ‣ Risk-sensitive safety analysis using Conditional Value-at-Risk*"))

<!-- chunk {"id": "body-0065", "role": "body", "section": "Stormwater System", "weight": 1.0} -->

Model parameters are in Table 2. The constraint set $K = {{\lbrack 0,k_{1}\rbrack} \times {\lbrack 0,k_{2}\rbrack}}$ specifies the maximum water elevations that the tanks can hold without surcharge. The stage cost ${g_{K}{(x)}} = {\max{({x_{1} - k_{1}},{x_{2} - k_{2}},0)}}$ is the maximum surcharged water level when the system occupies the state $x \in {\mathbb{R}}_{+}^{2}$.

<!-- chunk {"id": "body-0066", "role": "body", "section": "Stormwater System", "weight": 1.0} -->

We have identified a discrete distribution for the disturbance process with the approximate statistics, mean (12.2 cfs), variance (9.9 cfs^2^), and skew (0.74), where cfs is cubic feet per second. In previous work, we obtained runoff samples by simulating a design storm in PCSWMM (Computational Hydraulics International), which extends the US Environmental Protection Agency's Stormwater Management Model. In this previous work, the empirical distribution had positive skew, and the mean was about 12.2 cfs, which are reflected in the current distribution (not shown in the interest of space).

<!-- chunk {"id": "body-0067", "role": "body", "section": "Stormwater System", "weight": 1.0} -->

In Fig. 5, we show estimates of risk-sensitive safe sets and their under-approximations using $\gamma = 22$ for 5 risk-sensitivity levels (see also Table 3). The shape of the contour of $\mathcal{S}_{\alpha}^{r,\pi_{\gamma}}$ indicates a critical trade-off between the maximum initial water elevations in the two tanks from which the system meets a desired degree of safety. The similarity in the shapes of $\mathcal{S}_{\alpha}^{r,\pi_{\gamma}}$ and $\mathcal{U}_{\alpha,\gamma}^{r}$ is notable, suggesting that $\mathcal{U}_{\alpha,\gamma}^{r}$ may be a useful tool for inferring these critical trade-offs in networked water systems.

<!-- chunk {"id": "body-0068", "role": "body", "section": "Stormwater System", "weight": 1.0} -->

invert elevation of pipe from base of tank 1

<!-- chunk {"id": "body-0069", "role": "body", "section": "Stormwater System", "weight": 1.0} -->

invert elevation of pipe from base of tank 2

<!-- chunk {"id": "body-0070", "role": "body", "section": "Stormwater System", "weight": 1.0} -->

elevation from base of tank 2 to orifice

<!-- chunk {"id": "body-0071", "role": "body", "section": "Stormwater System", "weight": 1.0} -->

ft = feet, s = seconds, min = minutes, h = hours.

<!-- chunk {"id": "body-0072", "role": "body", "section": "Concluding Remarks", "weight": 1.0} -->

This paper develops trajectory-wise safety specifications for control systems that quantify the severity of random harmful outcomes and thereby generalize classical stochastic safety analysis. Our primary contribution is to develop a tractable, interpretable safety analysis method with theoretical guarantees that assesses the upper tail of a cost distribution by using CVaR. It is notable that our method provides a parameter-dependent upper bound to the CVaR of a maximum cost without augmenting the state space. We have developed compelling numerical examples, which demonstrate the utility and tractability of our under-approximation approach. Moreover, we have proposed a risk-sensitive safe set definition in terms of a new coherent risk functional, inspired by CVaR, that admits a parameter-independent upper bound. We show that this upper bound can be computed via DP on the original state space by proving the regularity of a supremum over a function space for a class of transition kernels. Numerical investigations of leveraging our approximation to provide an efficient preliminary estimate to the exact CVaR is an exciting future direction. For instance, we have recently demonstrated the usefulness of efficient approximate "warm-start" computations to examine the effect of different design changes to stormwater infrastructure.

<!-- chunk {"id": "body-0073", "role": "body", "section": "Concluding Remarks", "weight": 1.0} -->

More broadly, combining techniques from approximate dynamic programming, stochastic rollout, and risk-sensitive safety analysis could lead to novel controller synthesis algorithms for higher-dimensional systems.

<!-- chunk {"id": "body-0074", "role": "body", "section": "Concluding Remarks", "weight": 1.0} -->

This table provides the percentages $\frac{\text{Number of states in estimate of~}\mathcal{U}_{\alpha,\gamma}^{r}}{\text{Number of states in estimate of~}\mathcal{S}_{\alpha}^{r,\pi_{\gamma}}} \cdot {100\%}$ for the sets in Fig. 5 (stormwater system, γ = 22).
