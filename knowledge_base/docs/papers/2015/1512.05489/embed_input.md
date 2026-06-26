<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Data-driven Inverse Optimization with Imperfect Information

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

In data-driven inverse optimization an observer aims to learn the preferences of an agent who solves a parametric optimization problem depending on an exogenous signal. Thus, the observer seeks the agent's objective function that best explains a historical sequence of signals and corresponding optimal actions. We focus here on situations where the observer has imperfect information, that is, where the agent's true objective function is not contained in the search space of candidate objectives, where the agent suffers from bounded rationality or implementation errors, or where the observed signal-response pairs are corrupted by measurement noise. We formalize this inverse optimization problem as a distributionally robust program minimizing the worst-case risk that the predicted decision (i.e., the decision implied by a particular candidate objective) differs from the agent's actual response to a random signal. We show that our framework offers rigorous out-of-sample guarantees for different loss functions used to measure prediction errors and that the emerging inverse optimization problems can be exactly reformulated as (or safely approximated by) tractable convex programs when a new suboptimality loss function is used.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

We show through extensive numerical tests that the proposed distributionally robust approach to inverse optimization attains often better out-of-sample performance than the state-of-the-art approaches.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

In inverse optimization an observer aims to learn the preferences of an agent who solves a parametric optimization problem depending on an exogenous signal. The observer knows the constraints imposed on the agent's actions but is unaware of her objective function. By monitoring a sequence of signals and corresponding actions, the observer seeks to identify an objective function that makes the observed actions optimal in the agent's optimization problem. This learning problem can be cast as an inverse optimization problem over candidate objective functions. The hope is that the solution of this inverse problem enables the observer to predict the agent's future actions in response to new signals.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

Inverse optimization has a wide spectrum of applications spanning several disciplines ranging from econometrics and operations research to engineering and biology. For example, a marketing executive aims to understand the purchasing behavior of consumers with unknown utility functions by monitoring sales figures, a transportation planner wishes to learn the route choice preferences of the passengers in a multimodal transport system by measuring traffic flows, or a healthcare manager seeks to design clinically acceptable treatments in view of historical treatment plans. It is even believed that the behavior of many biological systems is governed by a principle of optimality with respect to an unknown decision criterion, which can be inferred by tracking the system. Inverse optimization has also been applied in geoscience, portfolio selection, production planning, inventory management, network design and control and the analysis of electricity prices.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

The main thrust of the early literature on inverse optimization is to identify an objective function that explains a single observation. In the seminal paper the agent solves a static (non-parametric) linear program and reveals her optimal decision to the observer, who then identifies the objective function closest to a prescribed nominal objective, under which the observed decision is optimal. This model was later extended to conic programs, integer programs and linearly constrained separable convex programs. Another variant of this problem is considered, where the observer identifies an admissible objective function for which the optimal value of the agent's problem is closest to the observed optimal value corresponding to the unknown true objective.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

This paper focuses on data-driven inverse optimization problems where the agent solves a parametric optimization problem several times. Accordingly, the observer has access to a finite sequence of signals and corresponding optimal responses. Using this training data, the observer aims to infer an objective function that accurately predicts the agent's optimal responses to unseen future signals. As in classical regression, this learning task could be addressed by minimizing an empirical loss that penalizes the mismatch between the predicted and true optimal responses to a given signal. Data-driven inverse optimization problems of this type have only just started to attract attention, and to the best of our knowledge there are currently only three papers that study such problems. In the observer seeks an objective function under which all observed decisions solve the Karush-Kuhn-Tucker (KKT) optimality conditions of the agent's convex optimization problem. To this end, the observer minimizes some norm of the KKT residuals at all observations. A similar goal is pursued, where the optimality conditions are expressed via variational inequalities that can be reformulated as tractable conic constraints using ideas from robust optimization.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Introduction", "weight": 1.5} -->

This approach has the additional benefit that it extends to more general inverse equilibrium problems, which indicates that inverse optimization problems constitute special instances of mathematical programs with equilibrium constraints. A comprehensive survey of variational inequalities and mathematical programs with equilibrium constraints is provided. The third paper suggests to minimize the empirical average of the squared Euclidean distances between the predicted and true observed decisions, in which case the data-driven inverse optimization problem reduces to a bilevel program.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Introduction", "weight": 1.5} -->

In summary, all existing approaches to data-driven inverse optimization solve an empirical loss minimization problem over some search space of candidate objectives. Different approaches mainly differ with respect to the loss functions that capture the mismatch between predictions and observations. The KKT loss used in quantifies the extent to which the observed response to some signal violates the KKT conditions for a fixed candidate objective. Similarly, the first-order loss used in measures the extent to which an observed response violates the first-order optimality conditions. Moreover, the predictability loss used in captures the squared distance between an observed response and the response predicted by a given candidate objective.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Introduction", "weight": 1.5} -->

In this paper we introduce the new suboptimality loss, which quantifies the degree of suboptimality of an observed response under a given candidate objective. We highlight that the predictability and suboptimality losses both enjoy a direct physical meaning, while the KKT and first-order losses are not as easily interpretable.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Introduction", "weight": 1.5} -->

Computational experiments in and suggest that empirical loss minimization problems under perfect information are likely to correctly identify the agent's true objective function if there is sufficient training data and the search space of candidate objectives is not too large. In any realistic setting, however, the observer is confronted with imperfect information such as model uncertainty (the agent's true objective is not one of the candidate objectives), noisy measurements (the observed signals and responses are corrupted by measurement errors) or bounded rationality (the agent settles for suboptimal responses due to cognitive or computational limitations). Due to overfitting effects, imperfect information can severely impair the predictive power of a candidate objective obtained via empirical loss minimization. This is simply a manifestation of the notorious 'garbage in-garbage out' phenomenon. As imperfect information certainly reflects the norm rather than the exception in inverse optimization, we propose here a systematic approach to combat overfitting via distributionally robust optimization.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Introduction", "weight": 1.5} -->

Specifically, inspired by and, we use the Wasserstein distance to construct a ball in the space of all signal-response-distributions centered at the empirical distribution on the training samples, and we formulate a distributionally robust inverse optimization problem that minimizes the worst-case risk of loss for any combination of a risk measure with a loss function, where the worst case is taken over all distributions in the Wasserstein ball. If the radius of the Wasserstein ball is chosen judiciously, we can guarantee that it contains the unknown data-generating distribution with high confidence, which in turn allows us to derive rigorous out-of-sample guarantees for the risk of loss of unseen future observations. The proposed distributionally robust inverse optimization problem can naturally be interpreted as a regularization of the corresponding empirical loss minimization problem. While regularization is known to improve the out-of-sample performance of numerous estimators in statistics, it has not yet been investigated systematically in the context of data-driven inverse optimization.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Introduction", "weight": 1.5} -->

We highlight the following main contributions of this paper relative to the existing literature: We propose the suboptimality loss as an alternative to the KKT, first-order and predictability losses. The suboptimality loss admits a direct physical interpretation (like the predictability loss) and leads to convex empirical loss minimization problems (like the KKT and first-order losses) whenever the candidate objective functions admit a linear parameterization. In contrast, empirical predictability loss minimzation problems constitute NP-hard bilevel programs even for linear candidate objectives. We also propose the bounded rationality loss, which generalizes the suboptimality loss to situations where the agent is known to select $\delta$-suboptimal decision due to bounded rationality.

<!-- chunk {"id": "body-0014", "role": "body", "section": "Introduction", "weight": 1.5} -->

We leverage the data-driven distributionally robust optimization scheme with Wasserstein balls developed in to regularize empirical inverse optimization problems under imperfect information. As such, the proposed approach offers out-of-sample guarantees for any combination of risk measures and loss functions. In contrast, develops out-of-sample guarantees only for the value-at-risk of the first-order loss, while and discuss no (finite) out-of-sample guarantees at all.

<!-- chunk {"id": "body-0015", "role": "body", "section": "Introduction", "weight": 1.5} -->

We study the tractability properties of the distributionally robust inverse optimization problem that minimizes the conditional value-at-risk of the suboptimality loss. We prove that this problem is equivalent to a convex program when the search space consists of all linear functions. We also show that this problem admits a safe convex approximation when the search space consists of all convex quadratic functions or all conic combinations of finitely many convex basis functions.

<!-- chunk {"id": "body-0016", "role": "body", "section": "Introduction", "weight": 1.5} -->

We argue that the first-order and suboptimality losses can be used as tractable approximations for the intractable predictability loss, which has desirable statistical consistency properties and is the preferred loss function if the observer aims for prediction accuracy. We show that if the candidate objective functions are strongly convex, then the estimators obtained from minimizing the first-order and suboptimality losses admit out-of-sample predictability guarantees. Moreover, the predictability guarantee corresponding to the suboptimality loss is stronger than the one obtained from the first-order loss. Recall that the predictability loss itself cannot be minimized in polynomial time.

<!-- chunk {"id": "body-0017", "role": "body", "section": "Introduction", "weight": 1.5} -->

We show through extensive numerical tests that the proposed distributionally robust approach to inverse optimization attains often better (lower) out-of-sample suboptimality and predictability than the state-of-the art approaches in and. All of our experiments are reproducible, and the underlying source codes are available at The rest of the paper develops as follows. In Sections 2 and 3 we formalizes the inverse optimization problem under perfect and imperfect information, respectively. Section 4 then introduces the distributionally robust approach to inverse optimization, while Sections 5 and 6 derive tractable reformulations and safe approximations for distributionally robust inverse optimization problems over search spaces of linear and quadratic candidate objectives, respectively. Numerical results are reported in Section 7.

<!-- chunk {"id": "body-0018", "role": "body", "section": "Inverse Optimization under Perfect Information", "weight": 1.0} -->

Consider also an independent observer who monitors the signal $s \in {\mathbb{S}}$ as well as the agent's optimal response $x \in {{\mathbb{X}}^{\star}{(s)}}$. We assume that the observer is ignorant of the agent's preferences encoded by the objective function $F$. Thus, a priori, the observer cannot predict the agent's response $x$ to a particular signal $s$. Throughout the paper we assume that the observed signal-response pairs $\xi ≔ {(s,x)}$ are governed by some probability distribution $\mathbb{P}$ supported on $\Xi ≔ \left\{ {(s,x)}:{{s \in {\mathbb{S}}},{x \in {{\mathbb{X}}{(s)}}}} \right\}$, which can be viewed as the graph of the feasible set mapping $\mathbb{X}$.

<!-- chunk {"id": "body-0019", "role": "body", "section": "Inverse Optimization under Perfect Information", "weight": 1.0} -->

Note that the marginal distribution of $s$ under $\mathbb{P}$ captures the frequency of the exogenous signals, while the conditional distribution of $x$ given $s$ places all probability mass on the argmin set ${\mathbb{X}}^{\star}{(s)}$. Note that, unless ${\mathbb{X}}^{\star}{(s)}$ is a singleton, the exact conditional distribution of $x$ given $s$ depends on the specific optimization algorithm used by the agent.

<!-- chunk {"id": "body-0020", "role": "body", "section": "Inverse Optimization under Perfect Information", "weight": 1.0} -->

In the following we assume that the observer has access to $N$ independent samples ${\hat{\xi}}_{i} ≔ {({\hat{s}}_{i},{\hat{x}}_{i})}$ from $\mathbb{P}$, which can be used to learn the agent's objective function. As the space of all possible objective functions is vast, the observer seeks to approximate $F$ by some candidate objective function from within a parametric hypothesis space $\mathcal{F} = {\{ F_{\theta}:{\theta \in \Theta}\}}$, where $\Theta$ represents a finite-dimensional parameter set. Ideally, the observer would aim to identify the hypothesis $F_{\theta}$ closest to $F$, e.g., by solving the least squares problem where $\ell_{\theta}{({\hat{s}}_{i},{\hat{x}}_{i})}$ denotes the identifiability loss as per the following definition.

<!-- chunk {"id": "body-0021", "role": "body", "section": "Example 1 (Risk measures)", "weight": 1.0} -->

A popular risk measure that the observer could use to quantify the risk of a positive loss is the conditional value-at-risk ($CVaR$) at level $\alpha \in {(0,1\rbrack}$, which is defined as By definition, the loss function $\ell_{\theta}{(\xi)}$ is non-negative for all $\xi \in \Xi$ and $\theta \in \Theta$. The monotonicity and normalization of the risk measure $\rho$ thus imply that which in turn implies that the optimal value of problem is necessarily larger than or equal to zero.

<!-- chunk {"id": "body-0022", "role": "body", "section": "Example 1 (Risk measures)", "weight": 1.0} -->

Moreover, if the agent's true objective function is contained in $\mathcal{F}$, that is, if $F = F_{\theta^{\star}}$ for some $\theta^{\star} \in \Theta$, then the loss $\ell_{\theta^{\star}}{({\hat{\xi}}_{i})}$ vanishes for all $i$, indicating that the optimal value of is zero and that $\theta^{\star}$ is optimal. In this case, the optimal value of the in-sample risk minimization problem is known a priori, and the only informative output of any solution scheme is an optimizer, that is, a model $\theta' \in \Theta$ with zero in-sample risk. If the number of training samples is moderate, then there may be multiple optimal solutions, and $\theta'$ may differ from the agent's true model $\theta^{\star}$.

<!-- chunk {"id": "body-0023", "role": "body", "section": "Remark 2.6 (Choice of risk measures)", "weight": 1.0} -->

If $F = F_{\theta^{\star}}$ for $\theta^{\star} \in \Theta$, then the minimum of vanishes and is minimized by $\theta^{\star}$ irrespective of $\rho$. Thus, one might believe that the choice of the risk measure is immaterial for the inverse optimization problem. However, different risk measures may result in different solution sets. For example, if $\rho$ is the $CVaR$ at level $\alpha \in {(0,1\rbrack}$, then $\theta'$ is a minimizer of if and only if ${\ell_{\theta'}{({\hat{s}}_{i},{\hat{x}}_{i})}} = 0$ for all $i \leq N$.

<!-- chunk {"id": "body-0024", "role": "body", "section": "Remark 2.6 (Choice of risk measures)", "weight": 1.0} -->

In contrast, if $\rho$ is the $VaR$ at level $\alpha \in {\lbrack 0,1\rbrack}$, then $\theta'$ is a minimizer of if and only if ${\ell_{\theta'}{({\hat{s}}_{i},{\hat{x}}_{i})}} = 0$ for a portion of at least $1 - \alpha$ of all $N$ training samples. Thus, the use of $VaR$ may lead to an inflated solution set. Moreover, the choice of $\rho$ impacts the tractability of; see Sections 5 and 6.

<!-- chunk {"id": "body-0025", "role": "body", "section": "Inverse Optimization under Imperfect Information", "weight": 1.0} -->

The proposed framework for inverse optimization described in Section 2 is predicated on the assumption of perfect information. Specifically, it is assumed that the agent is able to determine and implement the best response $x$ to any given signal $s$ and that the observer can measure $s$ and $x$ precisely. Moreover, it is implicitly assumed that the family $\mathcal{F}$ of candidate objective functions contains the agent's true objective function $F$. In practice, however, the observer may be confronted with the following challenges: Model uncertainty: The hypothesis space $\mathcal{F}$ chosen by the observer may not be rich enough to contain the agent's true objective function $F$ or any strictly increasing transformation of $F$ that encodes the same preferences.

<!-- chunk {"id": "body-0026", "role": "body", "section": "Inverse Optimization under Imperfect Information", "weight": 1.0} -->

Measurement noise: The observed signal-response pairs may be corrupted by noise, which prevents the observer from measuring them exactly.

<!-- chunk {"id": "body-0027", "role": "body", "section": "Inverse Optimization under Imperfect Information", "weight": 1.0} -->

Bounded rationality: The agent may settle for a suboptimal decision $x$ due to cognitive or computational limitations. Even if the best response can be computed exactly, an exact implementation of the desired best response may not be possible due to implementation errors.

<!-- chunk {"id": "body-0028", "role": "body", "section": "Inverse Optimization under Imperfect Information", "weight": 1.0} -->

In the presence of model uncertainty, that is, if neither $F$ nor any strictly increasing transformation of $F$ is contained in the chosen hypothesis space $\mathcal{F}$, then there exists typically no $\theta \in \Theta$ such that the loss functions described in Section 2 vanish on all training samples. In this case a perfect recovery of the agent's preferences is fundamentally impossible, and the optimal value of the empirical risk minimization problem is positive. The best the observer can hope for is to learn the parametric hypothesis that most accurately (but imperfectly) captures the agent's true preferences.

<!-- chunk {"id": "body-0029", "role": "body", "section": "Inverse Optimization under Imperfect Information", "weight": 1.0} -->

We will henceforth assume that the noisy samples ${\hat{\xi}}_{i}$ are mutually independent and follow an in-sample distribution ${\mathbb{P}}_{in}$, while the corresponding unperturbed samples ${\hat{\xi}}_{i}$ are governed by an out-of-sample distribution ${\mathbb{P}}_{out}$. While the distribution ${\mathbb{P}}_{out}$ of the perfect samples is supported on $\Xi$ by construction, the in-sample distribution ${\mathbb{P}}_{in}$ of the noisy samples may or may not be supported on $\Xi$. If the noisy samples can materialize outside of $\Xi$, then we call the noise inconsistent. If all noisy samples are guaranteed to reside within $\Xi$, on the other hand, then we call the noise consistent.

<!-- chunk {"id": "body-0030", "role": "body", "section": "Inverse Optimization under Imperfect Information", "weight": 1.0} -->

Thus, in the presence of measurement noise, the observer faces the challenging task to learn ${\mathbb{P}}_{out}$ from samples of ${\mathbb{P}}_{in}$. Note that in the absence of noise we have ${\mathbb{P}}_{in} = {\mathbb{P}}_{out}$, which coincides with the distribution $\mathbb{P}$ introduced in Section 2.

<!-- chunk {"id": "body-0031", "role": "body", "section": "Inverse Optimization under Imperfect Information", "weight": 1.0} -->

Agents suffering from *bounded rationality* may not be able to solve to global optimality. Such agents may respond to a given signal $s$ with a $\delta$-suboptimal solution $x_{\delta}$, that is, a decision $x_{\delta} \in {{\mathbb{X}}{(s)}}$ with ${F{(s,x_{\delta})}} \leq {{{\min_{x \in {{\mathbb{X}}{(s)}}}F}{(s,x)}} + \delta}$. Here, the parameter $\delta \geq 0$ quantifies the agent's irrationality. Indeed, if $\delta > 0$, the agent accepts a cost increase of up to $\delta$ for the freedom of choosing a $\delta$-suboptimal decision, which may require fewer cognitive or computational resources than finding a global minimizer. Note that the observer may mistakenly perceive the effects of bounded rationality as (consistent) measurement noise or vice versa.

<!-- chunk {"id": "body-0032", "role": "body", "section": "Inverse Optimization under Imperfect Information", "weight": 1.0} -->

So one might argue that there is no need to distinguish between these two types of imperfect information. However, bounded rationality is fundamentally different from measurement noise if the observer knows that the imperfect measurements are caused by bounded rationality. If the imperfections originate from measurement noise, then the observer aims to filter out the noise in order to predict the agent's pure decisions. If the imperfections originate from bounded rationality, on the other hand, then the observer aims to predict the agent's $\delta$-suboptimal decisions and not the ideal global optimizers. In other words, the observer always aims to predict the agent's responses bar measurement noise, irrespective of whether these responses are rational or not. An observer who knows the agent's degree of irrationality $\delta$ may thus improve the predictive power of her learning model by replacing the suboptimality loss (4b. ‣ 2. Inverse Optimization under Perfect Information ‣ Data-driven Inverse Optimization with Imperfect Information")) with the bounded rationality loss.

<!-- chunk {"id": "body-0033", "role": "body", "section": "Distributionally Robust Inverse Optimization", "weight": 1.0} -->

By combining different loss functions with different risk measures, one may synthesize different empirical risk minimization problems of the form. By construction, any solution of has minimum in-sample risk. However, the in-sample risk merely captures historical performance and is therefore of little practical interest. Instead, the observer seeks models that display promising performance on unseen future data.

<!-- chunk {"id": "body-0034", "role": "body", "section": "Remark 4.5 (Out-of-sample guarantees in )", "weight": 1.0} -->

The out-of-sample guarantees provided in only apply to the $VaR$, and an extension to other risk measures is not envisaged. Specifically, \[11, Theorem 6\] provides an out-of-sample guarantee for the $VaR$ of the first-order loss, while \[11, Theorem 6\] offers an out-of-sample guarantee for the $VaR$ of the predictability loss. In contrast, the distributionally robust approach discussed here offers out-of-sample guarantees for any normalized, positive homogeneous and monotone risk measure including the $VaR$ or any coherent risk measure such as the $CVaR$ etc.

<!-- chunk {"id": "body-0035", "role": "body", "section": "Linear Hypotheses", "weight": 1.0} -->

On the one hand, the hypothesis space $\mathcal{F}$ should be rich enough to contain the agent's unknown true objective function $F$. On the other hand, $\mathcal{F}$ should be small enough to ensure tractability of the distributionally robust inverse optimization problem and to prevent degeneracy of its optimal solutions. A particular class $\mathcal{F}$ that strikes this delicate balance and proves useful in many applications is the family of linear objective functions ${F_{\theta}{(s,x)}} ≔ \left\langle \theta,x \right\rangle$. The corresponding search space $\Theta \subseteq {\mathbb{R}}^{n}$ may account for prior information on the agent's objective and should not contain $\theta = 0$, which corresponds to a trivial constant objective function that renders every response optimal. Examples of tractable search spaces are listed below.

<!-- chunk {"id": "body-0036", "role": "body", "section": "Example 2 (Tractable search spaces)", "weight": 1.0} -->

If there is no prior information on $F$, it is natural to set If $F$ is known to be non-decreasing in the agent's decisions, a natural choice is This search space has been used in and constitutes a single convex polytope.

<!-- chunk {"id": "body-0037", "role": "body", "section": "Example 2 (Tractable search spaces)", "weight": 1.0} -->

If $F$ is believed to reside in the vicinity of a nominal objective function $\left\langle \theta_{0},x \right\rangle$ as, then we may set where $\parallel \cdot \parallel$ denotes a generic norm, and $\Gamma$ reflects the degree of uncertainty about the nominal model $\theta_{0}$.

<!-- chunk {"id": "body-0038", "role": "body", "section": "Example 2 (Tractable search spaces)", "weight": 1.0} -->

When focusing on linear hypotheses, the suboptimality loss function (4b. ‣ 2. Inverse Optimization under Perfect Information ‣ Data-driven Inverse Optimization with Imperfect Information")) reduces to and thus equals the first-order loss (4c. ‣ 2. Inverse Optimization under Perfect Information ‣ Data-driven Inverse Optimization with Imperfect Information")), which is positive homogeneous and subadditive in $\theta$. The tractability results to be established below rely on the following assumption.

<!-- chunk {"id": "body-0039", "role": "body", "section": "Assumption 5.1 (Conic representable support)", "weight": 1.0} -->

The signal space $\mathbb{S}$ and the feasible set ${\mathbb{X}}{(s)}$ are conic representable, that is, where the relations '$\succeq_{\mathcal{C}}$' and '$\succeq_{\mathcal{K}}$' represent conic inequalities with respect to some proper convex cones $\mathcal{C}$ and $\mathcal{K}$ of appropriate dimensions, respectively. The set $\Xi$ of all possible signal-response pairs thus reduces to We also assume that the convex set $\Xi$ admits a Slater point.

<!-- chunk {"id": "body-0040", "role": "body", "section": "Assumption 5.1 (Conic representable support)", "weight": 1.0} -->

Under Assumption 5.1. ‣ 5. Linear Hypotheses ‣ Data-driven Inverse Optimization with Imperfect Information"), the suboptimality loss $\ell_{\theta}{(s,x)}$ is concave in $(s,x)$ for every fixed $\theta$, see, e.g., \[14, Section 3.2.5\]. We are now ready to state our first tractability result for the class of linear hypotheses.

<!-- chunk {"id": "body-0041", "role": "body", "section": "Quadratic Hypotheses", "weight": 1.0} -->

Optimization problems with quadratic objectives abound in control, statistics, finance and many other application domains. Algorithms for inverse optimization that can learn quadratic objective functions from signal-response pairs are therefore of great practical interest. This motivates us to consider the class $\mathcal{F}$ of quadratic hypotheses of the form ${F_{\theta}{(s,x)}} ≔ {\left\langle x,{Q_{xx}x} \right\rangle + \left\langle x,{Q_{xs}s} \right\rangle + \left\langle q,x \right\rangle}$, which are encoded by a parameter $\theta ≔ {(Q_{xx},Q_{xs},q)}$. The corresponding search space should account for prior information on the agent's objective and should exclude $\theta = 0$. Examples of tractable search spaces are listed below.

<!-- chunk {"id": "body-0042", "role": "body", "section": "Example 3 (Tractable search spaces)", "weight": 1.0} -->

If $F$ is only known to be strongly convex in $x$, it is natural to set If $F$ is only known to be bilinear in $s$ and $x$, it is natural to set where the normalization $Q_{xs} = {\mathbb{I}}$ can always be enforced by redefining $s$ if necessary.

<!-- chunk {"id": "body-0043", "role": "body", "section": "Example 3 (Tractable search spaces)", "weight": 1.0} -->

If $F$ is close to a nominal objective function $\left\langle x,{Q_{xx}^{0}x} \right\rangle + \left\langle x,{Q_{xs}^{0}s} \right\rangle + \left\langle q^{0},x \right\rangle$, then we may set where $\parallel \cdot \parallel$ denotes a generic norm, and $\Gamma$ captures the uncertainty of the nominal model $\theta_{0} = {(Q_{xx}^{0},Q_{xs}^{0},q^{0})}$.

<!-- chunk {"id": "body-0044", "role": "body", "section": "Example 3 (Tractable search spaces)", "weight": 1.0} -->

When focusing on quadratic candidate objective functions, the suboptimality loss (4b. ‣ 2. Inverse Optimization under Perfect Information ‣ Data-driven Inverse Optimization with Imperfect Information")) reduces to As in Section 5, we suppose that Assumption 5.1. ‣ 5. Linear Hypotheses ‣ Data-driven Inverse Optimization with Imperfect Information") holds. In this setting the agent's decision problem constitutes a conic program and is therefore tractable for common choices of the cones $\mathcal{C}$ and $\mathcal{K}$. In contrast, the inverse optimization problem is hard. In fact, it is already hard to evaluate the objective function of for a fixed $\theta$. As we work with quadratic objectives, throughout this section we use the $2$-norm on the signal-response space and the $2$-Wasserstein metric to measure distances of distributions.

<!-- chunk {"id": "body-0045", "role": "body", "section": "Numerical Experiments", "weight": 1.0} -->

We now compare the proposed distributionally robust approach to inverse optimization against the state-of-the-art techniques described in and. The first experiment aims to learn a linear hypothesis from imperfect training samples, where the imperfection is explained by measurement noise or the agent's bounded rationality. Similarly, the second experiment endeavors to learn a quadratic hypothesis from imperfect training samples, where the imperfection is explained by measurement noise or model uncertainty.

<!-- chunk {"id": "body-0046", "role": "body", "section": "Numerical Experiments", "weight": 1.0} -->

All experiments are run on an Intel XEON CPU with 3.40GHz clock speed and 16GB of RAM. All linear, quadratic and second-order cone programs are solved with CPLEX 12.6, and all semidefinite programs are solved with MOSEK 8. In order to ensure that our experiments are reproducible, we make the underlying source codes available at

<!-- chunk {"id": "body-0047", "role": "body", "section": "Learning a Linear Hypothesis", "weight": 1.0} -->

The goal of this experiment is to learn a linear hypothesis from imperfect training samples where the measured responses represent feasible perturbations of the true optimal responses. The perturbations can be explained by measurement noise or by the agent's bounded rationality. We argue that different causes of the perturbations necessitate different inverse optimization models.

<!-- chunk {"id": "body-0048", "role": "body", "section": "7.1.A. Consistent Noisy Measurements", "weight": 1.0} -->

We also assume that the agent's feasible set is given by ${{\mathbb{X}}{(s)}} = {\{{x \in {\mathbb{R}}^{n}}:{{{\| x\|}_{\infty} \leq 1},{{Ax} \geq s}}\}}$, where the constraint matrix $A$ is sampled uniformly from the hypercube ${\lbrack{- 1},1\rbrack}^{m \times n}$. This feasible set can be brought to the standard form of Assumption 5.1. ‣ 5. Linear Hypotheses ‣ Data-driven Inverse Optimization with Imperfect Information") by setting For a fixed signal $s$, we denote the optimal value of the agent's true decision problem by $z^{\star}{(s)}$.

<!-- chunk {"id": "body-0049", "role": "body", "section": "7.1.A. Consistent Noisy Measurements", "weight": 1.0} -->

Generation of training samples: A single signal is constructed as $s = {Av_{1}}$, where the auxiliary random variable $v_{1}$ follows independent uniform distribution on ${\lbrack{- 1},1\rbrack}^{n}$. Thus, if $a_{i}$, $i \leq m$, denote the rows of the constraint matrix $A$, then the support of $s$ can be expressed as ${\mathbb{S}} = {\{{s \in {\mathbb{R}}^{m}}:{{|s_{i}|} \leq {{\| a_{i}\|}_{1}{\forall i}} \leq m}\}}$. This support can be brought to the standard form of Assumption 5.1.

<!-- chunk {"id": "body-0050", "role": "body", "section": "7.1.A. Consistent Noisy Measurements", "weight": 1.0} -->

‣ 5. Linear Hypotheses ‣ Data-driven Inverse Optimization with Imperfect Information") by setting As $v_{1} \in {{\mathbb{X}}{(s)}}$ by construction, problem is feasible for every $s \in {\mathbb{S}}$. We assume that the agent's response to $s$ is noisy in the sense that it constitutes a random $\delta$-suboptimal solution to for $\delta = 1$. Specifically, we assume that $x$ is obtained as a solution of an auxiliary optimization problem which minimizes a linear cost over the set of all $\delta$-suboptimal solutions to. The gradient $\theta_{rand}$ of the cost is sampled uniformly from ${\lbrack{- 1},1\rbrack}^{n}$. By construction, we have $x \in {{\mathbb{X}}{(s)}}$, which implies that ${(s,x)} \in \Xi$. Thus, the measurement noise is consistent with the know support of the exact signal-response pairs.

<!-- chunk {"id": "body-0051", "role": "body", "section": "7.1.A. Consistent Noisy Measurements", "weight": 1.0} -->

The imperfect consistent training samples $({\hat{s}}_{i},{\hat{x}}_{i})$, $i \leq N$, are now generated independently using the above procedure.

<!-- chunk {"id": "body-0052", "role": "body", "section": "7.1.A. Consistent Noisy Measurements", "weight": 1.0} -->

Decision problem of the observer: The observer aims to identify a linear hypothesis ${F_{\theta}{(s,x)}} ≔ \left\langle \theta,x \right\rangle$, $\theta \in \Theta$, that best predicts the agent's responses to new signals, where the search space $\Theta$ is set to the $\infty$-norm ball around the nominal model $\theta_{0}$ described above. We assume that the observer minimizes the suboptimality loss (4b. ‣ 2. Inverse Optimization under Perfect Information ‣ Data-driven Inverse Optimization with Imperfect Information")) and uses the expected value to measure risk. Moreover, the observer solves the distributionally robust inverse optimization problem over a $1$-Wasserstein ball around the empirical distribution on the training samples, where the $\infty$-norm is used as the transportation cost on $\Xi$. Note that this problem can be reformulated as the tractable linear program (25. ‣ 5. Linear Hypotheses ‣ Data-driven Inverse Optimization with Imperfect Information")) by virtue of Theorem 5.2.

<!-- chunk {"id": "body-0053", "role": "body", "section": "7.1.A. Consistent Noisy Measurements", "weight": 1.0} -->

‣ 5. Linear Hypotheses ‣ Data-driven Inverse Optimization with Imperfect Information").

<!-- chunk {"id": "body-0054", "role": "body", "section": "7.1.A. Consistent Noisy Measurements", "weight": 1.0} -->

Out-of-sample risk: To assess the quality of an estimator ${\hat{\theta}}_{N}$ obtained from (25. ‣ 5. Linear Hypotheses ‣ Data-driven Inverse Optimization with Imperfect Information")), we evaluate its out-of-sample risk ${\mathbb{E}}^{{\mathbb{P}}_{out}}{(\ell_{{\hat{\theta}}_{N}})}$ both with respect to the predictability loss (4a. ‣ 2. Inverse Optimization under Perfect Information ‣ Data-driven Inverse Optimization with Imperfect Information")) and the suboptimality loss (4b. ‣ 2. Inverse Optimization under Perfect Information ‣ Data-driven Inverse Optimization with Imperfect Information")), where ${\mathbb{P}}_{out}$ represents the distribution of a single test sample $(s,x)$ independent of the training samples, and where $x$ is an exact (non-noisy) response to $s$.

<!-- chunk {"id": "body-0055", "role": "body", "section": "7.1.A. Consistent Noisy Measurements", "weight": 1.0} -->

In practice, the out-of-sample risk cannot be evaluated analytically but only numerically by using 1,000 independent test samples from ${\mathbb{P}}_{out}$. By relying on non-noisy test samples, we assess how well the estimator ${\hat{\theta}}_{N}$ can predict the agent's exact optimal responses.

<!-- chunk {"id": "body-0056", "role": "body", "section": "7.1.A. Consistent Noisy Measurements", "weight": 1.0} -->

(a) Impact of the Wasserstein radius on the suboptimality and predictibility risk (b) Suboptimality learning curve (c) Predictibility learning curve Figure 1. Out-of-sample suboptimality and predictability risks in the presence of imperfect consistent training samples and perfect test samples All numerical results are averaged across $100$ independent problems instances $\{\theta_{0},\theta^{\star},A\}$. The first experiment involves $m = 50$ signal variables, $n = 50$ decision variables and $N = 10$ training samples. Figure 1(a) shows how the out-of-sample risk of the optimal estimator ${\hat{\theta}}_{N}{(\varepsilon)}$ obtained from (25. ‣ 5. Linear Hypotheses ‣ Data-driven Inverse Optimization with Imperfect Information")) changes with the radius $\varepsilon$ of the underlying Wasserstein ball.

<!-- chunk {"id": "body-0057", "role": "body", "section": "7.1.A. Consistent Noisy Measurements", "weight": 1.0} -->

This experiment suggests that both the predictability and suboptimality risks can be significantly reduced by using a distributionally robust inverse optimization model with a judiciously calibrated ambiguity set. Unfortunately, Figure 1(a), from which the optimal Wasserstein radii could be read off easily, is not available in the training phase as its construction requires large amounts of test samples. Instead, the Wasserstein radii offering the lowest out-of-sample risk must also be estimated from the training data. To this end, we use the following $k$-fold cross validation algorithm: Partition ${\hat{\xi}}_{1},\ldots,{\hat{\xi}}_{N}$ into $k$ folds, and repeat the following procedure for each fold $i = {1,\ldots,k}$. Use the $i$-th fold as a validation dataset and merge the remaining $k - 1$ folds to a training dataset of size $N_{i}$. Using only the $i$-th training dataset, solve (25.

<!-- chunk {"id": "body-0058", "role": "body", "section": "7.1.A. Consistent Noisy Measurements", "weight": 1.0} -->

‣ 5. Linear Hypotheses ‣ Data-driven Inverse Optimization with Imperfect Information")) for a large but finite number of candidate radii $\varepsilon \in \mathcal{E}$ to obtain an estimator ${\hat{\theta}}_{N_{i}}{(\varepsilon)}$. Use the $i$-th validation dataset to estimate the out-of-sample risk of ${\hat{\theta}}_{N_{i}}{(\varepsilon)}$ for each $\varepsilon \in \mathcal{E}$. Set ${\hat{\varepsilon}}_{N}^{i}$ to any $\varepsilon \in \mathcal{E}$ that minimizes this quantity.

<!-- chunk {"id": "body-0059", "role": "body", "section": "7.1.A. Consistent Noisy Measurements", "weight": 1.0} -->

After all folds have been processed, set ${\hat{\varepsilon}}_{N}$ to the average of the ${\hat{\varepsilon}}_{N}^{i}$ for $i = {1,\ldots,k}$, and re-solve (25. ‣ 5. Linear Hypotheses ‣ Data-driven Inverse Optimization with Imperfect Information")) with $\varepsilon = {\hat{\varepsilon}}_{N}$ using all $N$ samples. Report the optimal solution ${\hat{\theta}}_{N}$ and the optimal value ${\hat{J}}_{N}$ of (25. ‣ 5. Linear Hypotheses ‣ Data-driven Inverse Optimization with Imperfect Information")) as the recommended estimator and its corresponding certificate, respectively.

<!-- chunk {"id": "body-0060", "role": "body", "section": "7.1.A. Consistent Noisy Measurements", "weight": 1.0} -->

For brevity, we henceforth refer to the above cross-validation scheme as the distributionally robust optimization (DRO) approach. In the following, we compare the resulting DRO estimator against two state-of-the-art estimators from the literature. The first estimator is obtained from the variational inequality (VI) approach proposed, which minimizes the first-order loss (4c. ‣ 2. Inverse Optimization under Perfect Information ‣ Data-driven Inverse Optimization with Imperfect Information")) averaged across all training samples.

<!-- chunk {"id": "body-0061", "role": "body", "section": "7.1.A. Consistent Noisy Measurements", "weight": 1.0} -->

By \[10, Theorem 3\], the resulting inverse optimization problem is equivalent to the tractable linear program Note that as all training samples are consistent, that is, ${({\hat{s}}_{i},{\hat{x}}_{i})} \in \Xi$ for $i = {1,\ldots,n}$, one can show that all residuals $r_{i}$ are automatically non-negative, and the above linear program can be viewed as a special instance of that minimizes the first-order loss, where the risk measure is set to the expected value and the Wasserstein radius is set to zero. If there were inconsistent training samples that fall outside of $\Xi$, on the other hand, the absolute values of the residuals would be needed to prevent unboundedness.

<!-- chunk {"id": "body-0062", "role": "body", "section": "7.1.A. Consistent Noisy Measurements", "weight": 1.0} -->

The second estimator is obtained from the bilevel programming (BP) approach proposed, which minimizes the predictability loss (4a. ‣ 2. Inverse Optimization under Perfect Information ‣ Data-driven Inverse Optimization with Imperfect Information")) averaged across all training samples. As shown in \[6, Section 2.2\], the resulting inverse optimization problem is equivalent to the optimistic bilevel program Note that this bilevel program can be viewed as a special instance of that minimizes the predictability loss, where the risk measure is set to the expected value and the Wasserstein radius is set to zero.

<!-- chunk {"id": "body-0063", "role": "body", "section": "7.1.A. Consistent Noisy Measurements", "weight": 1.0} -->

The above bilevel program can be reformulated as a mixed integer quadratic program by replacing the '$\arg\min$'-constraint with the Karush-Kuhn-Tucker optimality conditions of the agent's linear program. Indeed, note that the resulting complementary slackness conditions can be linearized by introducing binary variables that identify the binding constraints. However, this approach requires big-$M$ constants to bound the optimal dual variables. As valid big-$M$ constants are difficult to obtain in general and as overly conservative big-$M$ constants lead to numerical instability, we use here the YALMIP interface for bilevel programming, which calls a dedicated branch and bound algorithm that branches directly on the complementarity slackness conditions. Throughout our experiments we limit all branch and bound calculations to $2,000$ iterations.

<!-- chunk {"id": "body-0064", "role": "body", "section": "7.1.A. Consistent Noisy Measurements", "weight": 1.0} -->

Figures 1(b) and 1(c) visualize the suboptimality and predictability learning curves, respectively, which capture how the out-of-sample risk of the different estimators changes with the number of training samples. As optimistic bilevel programs are NP-hard even when all objective and constraint functions are linear, this experiment focuses on problem instances with $n = m = 10$. Even for these moderate problem dimensions, however, the inverse optimization problems associated with the BP approach fails to find a feasible solution for more than 10 training samples. In contrast, all other approaches lead to tractable linear programs. Figure 1(b) shows that the DRO approach dominates the VI and BP approaches uniformly across all samples sizes in terms of out-of-sample suboptimality risk. This is reassuring as the DRO approach actually minimizes suboptimality risk. However, Figure 1(c) suggests that the DRO approach wins even in terms of out-of-sample predictability risk. This is perhaps surprising because, unlike the BP approach, the DRO approach only minimizes an approximation of the predictability loss.

<!-- chunk {"id": "body-0065", "role": "body", "section": "7.1.A. Consistent Noisy Measurements", "weight": 1.0} -->

We conclude that injecting distributional robustness may be more beneficial for out-of-sample performance than using the correct loss function.

<!-- chunk {"id": "body-0066", "role": "body", "section": "7.1.A. Consistent Noisy Measurements", "weight": 1.0} -->

Tables 1 and 2 report the out-of-sample suboptimality and predictability risks, respectively, for the DRO and VI estimators based on $N = 10$ training samples and for different signal and response dimensions. The BP approach is excluded from this comparison due to its intractability. We observe that the DRO estimator always attains the lowest suboptimality risk and often the lowest predictability risk. Whenever the VI estimator wins, the predictability risks of the VI and DRO estimators are in fact almost identical.

<!-- chunk {"id": "body-0067", "role": "body", "section": "7.1.A. Consistent Noisy Measurements", "weight": 1.0} -->

Table 1. Out-of-sample suboptimality risk in the presence of noisy consistent measurements Table 2. Out-of-sample predictability risk in the presence of consistent noisy measurements (a) Impact of the Wasserstein radius on the suboptimality and predictibility risk (b) Suboptimality learning curve (c) Predictibility learning curve Figure 2. Out-of-sample suboptimality and predictability risks in the presence of imperfect consistent training and test samples

<!-- chunk {"id": "body-0068", "role": "body", "section": "7.1.A. Bounded Rationality", "weight": 1.0} -->

Consider the exact same setting as in Section 7.1.A but assume now that the agent suffers from bounded rationality. Specifically, assume that the agent selects random $\delta$-suboptimal decisions that are perfectly measured by the observer. This means that the training samples are generated as in Section 7.1.A, but the imperfection of the training responses is now explained by the agent's bounded rationality instead of the observer's noisy measurements. At this point one may wonder why a new interpretation of the imperfections should impact the observer's inverse optimization problem. In the following we will assume, however, that the observer is aware of the agent's bounded rationality, knows the value of $\delta$ and aims to predict the agent's actual suboptimal decisions. Therefore, the DRO approach to inverse optimization is subject to two changes: The observer minimizes the bounded rationality loss (10. ‣ 3. Inverse Optimization under Imperfect Information ‣ Data-driven Inverse Optimization with Imperfect Information")) instead of the suboptimality loss (4b. ‣ 2. Inverse Optimization under Perfect Information ‣ Data-driven Inverse Optimization with Imperfect Information")).

<!-- chunk {"id": "body-0069", "role": "body", "section": "7.1.A. Bounded Rationality", "weight": 1.0} -->

The test samples are generated in the same way as the training samples. Thus, the test responses no longer constitute perfect minimizers of but represent random $\delta$-suboptimal solutions.

<!-- chunk {"id": "body-0070", "role": "body", "section": "7.1.A. Bounded Rationality", "weight": 1.0} -->

Recall that the bounded rationality loss favors hypotheses that correctly predict $\delta$-suboptimal responses. We also highlight that the observer's inverse optimization problem with bounded rationality loss can be reformulated as a tractable linear program by virtue of Corollary 5.4. ‣ 5. Linear Hypotheses ‣ Data-driven Inverse Optimization with Imperfect Information"). Moreover, by using imperfect test samples, the out-of-sample risk is now measured under the distribution of an imperfect signal-response pair, which is the correct performance criterion given that the observer aims to predict imperfect responses.

<!-- chunk {"id": "body-0071", "role": "body", "section": "7.1.A. Bounded Rationality", "weight": 1.0} -->

In analogy to Section 7.1.A, the impact of the Wasserstein radius on the out-of-sample suboptimality and predictability risk is shown in Figure 2(a). The suboptimality and predictability learning curves of different estimators are visualized in Figures 2(b) and 2(c), respectively. Here, the DRO estimator is defined in terms of the bounded rationality loss, while the VI and BP estimators are computed as in Section 7.1.A and are thus not corrected for the agent's bounded rationality. The impact of the signal and response dimensions on the out-of-sample suboptimality and predictability risk are reported in Tables 3 and 4, respectively. Unless otherwise stated, all experiments are parameterized exactly as in Section 7.1.A. Here, the DRO estimator systematically attains the lowest suboptimality risk, while the VI estimator almost always wins in terms of predictability risk, even though only by a small margin.

<!-- chunk {"id": "body-0072", "role": "body", "section": "7.1.A. Bounded Rationality", "weight": 1.0} -->

Table 3. Out-of-sample suboptimality risk in the presence of bounded rationality Table 4. Out-of-sample predictability risk in the presence of bounded rationality

<!-- chunk {"id": "body-0073", "role": "body", "section": "Learning a Quadratic Hypothesis", "weight": 1.0} -->

A fundamental problem in marketing is to understand the purchasing decisions of consumers, which is an essential prerequisite for estimating demand functions. In this section we study the inverse optimization problem of a marketing manager (the observer) aiming to learn the quadratic utility function that best explains the purchasing decisions of a consumer (the agent). This problem setup is inspired.

<!-- chunk {"id": "body-0074", "role": "body", "section": "7.2.B. Consistent Noisy Measurements", "weight": 1.0} -->

Decision problem of the agent: Assume that there are $n$ products with prices $s \in {\mathbb{R}}_{+}^{n}$. The agent aims to select a basket of goods $x \in {\mathbb{R}}_{+}^{n}$ that minimizes the true objective function ${F{(s,x)}} = {\left\langle s,x \right\rangle - {U{(x)}}}$, where $\left\langle s,x \right\rangle$ represents the purchasing costs, while the concave quadratic function ${U{(x)}} ≔ {{- \left\langle x,{Q_{xx}^{\star}x} \right\rangle} - \left\langle q^{\star},x \right\rangle}$ captures the utility of consumption. The positive definite matrix $Q_{xx}^{\star}$ is constructed as follows.

<!-- chunk {"id": "body-0075", "role": "body", "section": "7.2.B. Consistent Noisy Measurements", "weight": 1.0} -->

Sample a square matrix $A$ uniformly form ${\lbrack{- 1},1\rbrack}^{n \times n}$, denote by $R$ the orthogonal matrix consisting of the orthonormal eigenvectors of ${({A + A^{\intercal}})}/2$ and set $Q_{xx}^{\star} ≔ {R^{\intercal}DR}$, where $D$ is a diagonal matrix whose main diagonal is sampled uniformly form ${\lbrack 0.2,1\rbrack}^{n}$. Moreover, the gradient $q^{\star}$ is sampled uniformly from ${\lbrack{- 2},0\rbrack}^{n}$. Finally, define the agent's feasible set as ${{\mathbb{X}}{(s)}} = {\lbrack 0,5\rbrack}^{n}$, which can be brought to the standard form of Assumption 5.1.

<!-- chunk {"id": "body-0076", "role": "body", "section": "7.2.B. Consistent Noisy Measurements", "weight": 1.0} -->

‣ 5. Linear Hypotheses ‣ Data-driven Inverse Optimization with Imperfect Information") by setting As usual, for a fixed signal $s$, we denote the optimal value of the agent's true decision problem by $z^{\star}{(s)}$.

<!-- chunk {"id": "body-0077", "role": "body", "section": "7.2.B. Consistent Noisy Measurements", "weight": 1.0} -->

Generation of training samples: Signals follow the uniform distribution on the support set ${\mathbb{S}} = {\lbrack 0,1\rbrack}^{n}$, which can be brought to the standard form of Assumption 5.1. ‣ 5. Linear Hypotheses ‣ Data-driven Inverse Optimization with Imperfect Information") by setting $C = {({\mathbb{I}},{- {\mathbb{I}}})}^{\intercal} \in {\mathbb{R}}^{{2n} \times n}$, $d = {(0,{- 1})}^{\intercal} \in {\mathbb{R}}^{2n}$ and $\mathcal{C} = {\mathbb{R}}_{+}^{2n}$. As in Section 7.1.A, we assume that the agent's response to $s$ is noisy and constitutes a random $\delta$-suboptimal solution to for $\delta = 0.2$.

<!-- chunk {"id": "body-0078", "role": "body", "section": "7.2.B. Consistent Noisy Measurements", "weight": 1.0} -->

Thus, $x$ is obtained as a solution of the auxiliary problem which minimizes a convex quadratic cost over the set of all $\delta$-suboptimal solutions to. Specifically, $Q_{rand}$ is a diagonal matrix whose main diagonal is sampled uniformly form ${\lbrack 0,1\rbrack}^{n}$. As ${(s,x)} \in \Xi$ by construction, the measurement noise is consistent with the know support of the exact signal-response pairs. The imperfect consistent training samples $({\hat{s}}_{i},{\hat{x}}_{i})$, $i \leq N$, are now generated independently using the above procedure.

<!-- chunk {"id": "body-0079", "role": "body", "section": "7.2.B. Consistent Noisy Measurements", "weight": 1.0} -->

Decision problem of the observer: The observer aims to identify the best quadratic hypothesis of the form ${F_{\theta}{(s,x)}} ≔ {\left\langle x,{Q_{xx}x} \right\rangle + \left\langle x,s \right\rangle + \left\langle q,x \right\rangle}$, where the parameter $\theta = {(Q_{xx},q)}$ ranges over the search space Note that no hypothesis $F_{\theta}{(s,x)}$, $\theta \in \Theta$, can vanish identically due to the term $\left\langle x,s \right\rangle$. Note also that the agent's true objective function corresponds to $\theta^{\star} = {(Q_{xx}^{\star},q^{\star})} \in \Theta$. We assume that the observer minimizes the suboptimality loss (4b.

<!-- chunk {"id": "body-0080", "role": "body", "section": "7.2.B. Consistent Noisy Measurements", "weight": 1.0} -->

‣ 2. Inverse Optimization under Perfect Information ‣ Data-driven Inverse Optimization with Imperfect Information")), uses the expected value to measure risk and solves the distributionally robust inverse optimization problem over a $2$-Wasserstein ball around the empirical distribution on the training samples, where the $2$-norm is used as the transportation cost on $\Xi$. By Theorem 6.3. ‣ 6. Quadratic Hypotheses ‣ Data-driven Inverse Optimization with Imperfect Information"), the emerging inverse optimization problem is conservatively approximated by the tractable semidefinite program (53. ‣ 6. Quadratic Hypotheses ‣ Data-driven Inverse Optimization with Imperfect Information")).

<!-- chunk {"id": "body-0081", "role": "body", "section": "7.2.B. Consistent Noisy Measurements", "weight": 1.0} -->

Out-of-sample risk: The quality of an estimator ${\hat{\theta}}_{N}$ obtained from (53. ‣ 6. Quadratic Hypotheses ‣ Data-driven Inverse Optimization with Imperfect Information")) is measured by its out-of-sample risk ${\mathbb{E}}^{{\mathbb{P}}_{out}}{(\ell_{{\hat{\theta}}_{N}})}$ both with respect to the predictability loss (4a. ‣ 2. Inverse Optimization under Perfect Information ‣ Data-driven Inverse Optimization with Imperfect Information")) and the suboptimality loss (4b. ‣ 2. Inverse Optimization under Perfect Information ‣ Data-driven Inverse Optimization with Imperfect Information")), where ${\mathbb{P}}_{out}$ represents the distribution of a single test sample $(s,x)$ independent of the training samples, and where $x$ is an exact (non-noisy) response to $s$.

<!-- chunk {"id": "body-0082", "role": "body", "section": "7.2.B. Consistent Noisy Measurements", "weight": 1.0} -->

More precisely, the out-of-sample risk is evaluated approximately using 1,000 independent test samples from ${\mathbb{P}}_{out}$.

<!-- chunk {"id": "body-0083", "role": "body", "section": "7.2.B. Consistent Noisy Measurements", "weight": 1.0} -->

All numerical results are averaged across $100$ independent problems instances $\{ Q_{xx}^{\star},q^{\star}\}$. Under the assumption that the signal and response dimensions are set to $n = 10$ and there are $N = 20$ training samples, Figure 3(a) shows how the out-of-sample risk of the optimal estimator ${\hat{\theta}}_{N}{(\varepsilon)}$ obtained from changes with the Wasserstein radius $\varepsilon$. As in Section 7.1.A, this experiment suggests that both the predictability and suboptimality risks can be reduced by using a distributionally robust inverse optimization model.

<!-- chunk {"id": "body-0084", "role": "body", "section": "7.2.B. Consistent Noisy Measurements", "weight": 1.0} -->

(a) Imperfect consistent training samples and perfect test samples (b) Imperfect inconsistent training samples and perfect test samples Figure 3. Impact of the Wasserstein radius on the out-of-sample suboptimality and predictability risk

<!-- chunk {"id": "body-0085", "role": "body", "section": "7.2.B. Inconsistent Noisy Measurements", "weight": 1.0} -->

Assume now that the agent's optimal solutions to are corrupted by additive measurement noise that follows a uniform distribution on ${\lbrack{- 0.1},0.1\rbrack}^{n}$. Otherwise, we consider the exact same experimental setup as in Section 7.2.B. Under this premise, it is likely that some training responses are infeasible, that is, ${\hat{x}}_{i} \notin {{\mathbb{X}}{({\hat{s}}_{i})}}$ and---a fortiori---${({\hat{s}}_{i},{\hat{x}}_{i})} \notin \Xi$ for some $i \leq N$. These problematic training samples are inconsistent with the known support of the perfect signal-response pairs, and the corresponding empirical distribution ${\hat{\mathbb{P}}}_{N}$ fails to be supported on $\Xi$.

<!-- chunk {"id": "body-0086", "role": "body", "section": "7.2.B. Inconsistent Noisy Measurements", "weight": 1.0} -->

Thus, for all sufficiently small values of $\varepsilon$ there exists no distribution $\mathbb{Q}$ on $\Xi$ with ${W_{2}\left( {\mathbb{Q}},{\hat{\mathbb{P}}}_{N} \right)} \leq \varepsilon$, implying that the Wasserstein ball ${\mathbb{B}}_{\varepsilon}^{2}{({\hat{\mathbb{P}}}_{N})}$ is empty, in which case the distributionally robust inverse optimization problem (53. ‣ 6. Quadratic Hypotheses ‣ Data-driven Inverse Optimization with Imperfect Information")) becomes meaningless. Figure 3(b) visualizes the out-of-sample suboptimality and predictability risk of the optimal estimator $\hat{\theta}{(\varepsilon)}$ as a function of $\varepsilon$.

<!-- chunk {"id": "body-0087", "role": "body", "section": "7.2.B. Inconsistent Noisy Measurements", "weight": 1.0} -->

Note that for any fixed $\varepsilon$ the figure reports the out-of-sample risk averaged only across those problem instances $\{ Q_{xx}^{\star},q^{\star}\}$ for which ${{\mathbb{B}}_{\varepsilon}^{2}{({\hat{\mathbb{P}}}_{N})}} \neq \varnothing$. Inspecting the results at the instance level, we observe that the out-of-sample risk is typically minimized by the smallest value of $\varepsilon \geq 0$ for which ${{\mathbb{B}}_{\varepsilon}^{2}{({\hat{\mathbb{P}}}_{N})}} \neq \varnothing$ (this is not evident from the aggregate results shown in Figure 3(b)). We conclude that a distributionally robust approach may be necessary for consistency.

<!-- chunk {"id": "body-0088", "role": "body", "section": "7.2.B. Model Uncertainty", "weight": 1.0} -->

Assume next that the agent's objective function is not contained in the set of hypotheses $F_{\theta}{(s,x)}$, $\theta \in \Theta$, but that the signals and the agent's responses are unaffected by noise. Specifically, in analogy to, we assume that the true utility function is given by ${U{(x)}} ≔ \left\langle 1,\sqrt{{Ax} - b} \right\rangle$, where $A$ is a diagonal matrix whose main diagonal is sampled uniformly from ${\lbrack 0.5,1\rbrack}^{n}$, while $b$ is sampled uniformly from ${\lbrack 0,0.25\rbrack}^{n}$. The square root is applied componentwise and evaluates to $- \infty$ for negative arguments.

<!-- chunk {"id": "body-0089", "role": "body", "section": "7.2.B. Model Uncertainty", "weight": 1.0} -->

Otherwise, we consider the exact same experimental setup as in Section 7.2.B. Figure 3(c) shows the out-of-sample suboptimality and predictability risk of the optimal estimator $\hat{\theta}{(\varepsilon)}$ as a function of $\varepsilon$, indicating that the best results are obtained for strictly positive Wasserstein radii, which enable the observer to combat over-fitting to the training samples.

<!-- chunk {"id": "body-0090", "role": "body", "section": "7.2.B. Comparison of Different Data-Driven Inverse Optimization Schemes", "weight": 1.0} -->

In practice, the Wasserstein radii offering the lowest out-of-sample risk must be estimated from the training samples only. To this end, the DRO approach calibrates $\varepsilon$ via $k$-fold cross validation as in Section 7.1. Another estimator is obtained by solving the empirical risk minimization (ERM) problem using the empirical mean and the suboptimality loss (4b. ‣ 2. Inverse Optimization under Perfect Information ‣ Data-driven Inverse Optimization with Imperfect Information")). This approach effectively mimics the DRO approach but sets $\varepsilon = 0$, which can be viewed as a trivial data-driven strategy to calibrate the Wasserstein radius.^44^4We did not consider the ERM approach in Section 5 because it coincides with the VI approach for linear hypotheses. The VI approach also disregards ambiguity and minimizes the empirical first-order loss by solving the semidefinite program see \[10, Theorem 3\].

<!-- chunk {"id": "body-0091", "role": "body", "section": "7.2.B. Comparison of Different Data-Driven Inverse Optimization Schemes", "weight": 1.0} -->

As in Section 7.1.A, the absolute values of the residuals $r_{i}$ in the objective can be dropped whenever the training samples are consistent with $\Xi$. We exclude the BP approach from this experiment because it leads to severely intractable mixed integer semidefinite programming problems.

<!-- chunk {"id": "body-0092", "role": "body", "section": "7.2.B. Comparison of Different Data-Driven Inverse Optimization Schemes", "weight": 1.0} -->

All three approaches described above search over the parametric space of quadratic hypotheses. If the observer suspects that the true utility function fails to be quadratic, however, she may prefer a non-parametric approach that models the gradient of the utility function as a vector field $f \in \mathcal{H}^{n}$, where $\mathcal{H}$ represents a reproducing kernel Hilbert space of real-valued functions on ${\mathbb{R}}_{+}^{n}$, which is induced by a symmetric and positive definite kernel function $k:{{{\mathbb{R}}_{+}^{n} \times {\mathbb{R}}_{+}^{n}}\rightarrow{\mathbb{R}}}$.

<!-- chunk {"id": "body-0093", "role": "body", "section": "7.2.B. Comparison of Different Data-Driven Inverse Optimization Schemes", "weight": 1.0} -->

As $\mathcal{H}^{n}$ is typically infinite-dimensional and contains multiple candidate gradients $f \in \mathcal{H}^{n}$ that explain the training data, it has been suggested in \[10, Section 5\] to minimize the Hilbert norm $\sum_{i = 1}^{n}{\| f_{i}\|}_{\mathcal{H}}^{2}$ of $f$ subject to the constraint that the residuals of the first-order optimality condition at the training samples satisfy ${\frac{1}{N}{\sum_{i = 1}^{N}{|r_{i}|}}} \leq \kappa$ for some prescribed threshold $\kappa \geq 0$. This amounts to finding the smoothest (with respect to the kernel function $k$) candidate gradient $f \in \mathcal{H}^{n}$ that explains the training data to within accuracy $\kappa$.

<!-- chunk {"id": "body-0094", "role": "body", "section": "7.2.B. Comparison of Different Data-Driven Inverse Optimization Schemes", "weight": 1.0} -->

By leveraging a generalized representer theorem, the resulting infinite-dimensional optimization problem can be reformulated as the tractable quadratic program In the inverse optimization context studied here, however, the above non-parametric VI approach suffers from two shortcomings that are not addressed.

<!-- chunk {"id": "body-0095", "role": "body", "section": "7.2.B. Comparison of Different Data-Driven Inverse Optimization Schemes", "weight": 1.0} -->

The inverse optimization problem (82f) aims to learn the gradient field $f$ of the unknown utility function $U$. As the Hessian matrix of $U$ must be symmetric, the gradient field $f$ must satisfy By Stokes' theorem, this condition is necessary and sufficient to ensure that the utility function $U$ can be reconstructed uniquely (modulo an additive constant) from $f$. Specifically, this condition guarantees that the utility function is defined unambiguously through the line integral ${U{(x)}} = {{U{}} + {\int_{C}\left\langle {f{(x')}},{dx'} \right\rangle}}$, where $C$ represents an arbitrary piecewise smooth curve in ${\mathbb{R}}_{+}^{n}$ connecting $0$ and $x$.

<!-- chunk {"id": "body-0096", "role": "body", "section": "7.2.B. Comparison of Different Data-Driven Inverse Optimization Schemes", "weight": 1.0} -->

While the inverse optimization problem (82f) represents a tractable quadratic program, the resulting gradient field $f$ may induce a non-concave utility function $U$, which means that the agent's objective function ${F{(s,x)}} = {\left\langle s,x \right\rangle - {U{(x)}}}$ may have multiple local minima. Thus, even though learning $f$ is easy, predicting the optimal response $x$ to a given signal $s$ may require the solution of a hard non-convex optimization problem, which may severely complicate extensive out-of-sample tests. Similarly, evaluating the suboptimality loss $F{(s,x)}$ at a fixed signal-response pair is intractable.

<!-- chunk {"id": "body-0097", "role": "body", "section": "7.2.B. Comparison of Different Data-Driven Inverse Optimization Schemes", "weight": 1.0} -->

Here we address the first challenge by using the polynomial kernel function ${k{(x,x')}} = {({{c\left\langle x,x' \right\rangle} + 1})}^{p}$, which allows us to include the missing symmetry conditions in (82f) by appending the linear equality constraints The second challenge does not have a simple remedy, and therefore we abandon the ideal goal to solve to global optimality. Instead, for any given signal $s$, we use the gradient field $f$ obtained from directly to find a local solution of via the classical subgradient descent algorithm \[16, Chapter 3\], where the step size is set to $10^{- 3}$ and an initial feasible solution is selected uniformly at random from ${\mathbb{X}}{(s)}$. Note that the focus on local minima in prediction is consistent with the use of the first-order loss (4c.

<!-- chunk {"id": "body-0098", "role": "body", "section": "7.2.B. Comparison of Different Data-Driven Inverse Optimization Schemes", "weight": 1.0} -->

‣ 2. Inverse Optimization under Perfect Information ‣ Data-driven Inverse Optimization with Imperfect Information")) in inverse optimization because the first-oder loss cannot distinguish local and global optima and thus fails to penalize training samples $({\hat{s}}_{i},{\hat{x}}_{i})$ where ${\hat{x}}_{i}$ is a locally optimal but globally suboptimal response to ${\hat{s}}_{i}$.

<!-- chunk {"id": "body-0099", "role": "body", "section": "7.2.B. Comparison of Different Data-Driven Inverse Optimization Schemes", "weight": 1.0} -->

In our experiments we determine the parameter $c$ of the polynomial kernel via 5-fold cross validation. Once the gradient field $f$ has been inferred, we construct the corresponding utility function by integrating $f$ along the straight line $C$ between 0 and $x$ with parameterization ${g{(t)}} = {tx}$ for $t \in {\lbrack 0,1\rbrack}$, that is, we set Table 5 reports the out-of-sample suboptimality and predictability risks, respectively, for the DRO, VI and ERM estimators. The non-parametric VI approach is exclusively used in the presence of model uncertainty, which is the only scenario in which it has a chance to outperform the more parsimonious parametric approaches. Our results show that the DRO estimator consistently attains the lowest suboptimality and predictability risk among all parametric approaches. We emphasize that the suboptimality and predicatability risk of the non-parametric VI approach are evaluated with respect to the local minimum identified by the subgradient descent algorithm and are therefore largely meaningless.

<!-- chunk {"id": "body-0100", "role": "body", "section": "7.2.B. Comparison of Different Data-Driven Inverse Optimization Schemes", "weight": 1.0} -->

In fact, we observed that the suboptimality risk becomes even negative for certain instances in which the global minimum of could not be found. This artefact explains the low suboptimality risk of the non-parametric VI approach with $p = 3$. Note also that for $p \geq 4$ the number of symmetry conditions (82g) explodes, and thus can no longer be solved. We also reconfirm our earlier observation that injecting robustness reduces out-of-sample risk.

<!-- chunk {"id": "body-0101", "role": "body", "section": "7.2.B. Comparison of Different Data-Driven Inverse Optimization Schemes", "weight": 1.0} -->

Table 5. Data-driven inverse optimization: Out-of-sample suboptimality and predictability risk of the VI, ERM and DRO approaches in different experimental settings This work was supported by the Swiss National Science Foundation grant BSCGI0_157733.
