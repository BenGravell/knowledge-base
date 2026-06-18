<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

On the Performance of Thompson Sampling on Logistic Bandits

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

We study the logistic bandit, in which rewards are binary with success probability exp(betaa^(top) theta) / (1 + exp(betaa^(top) theta)) and actions a and coefficients theta are within the d-dimensional unit ball. While prior regret bounds for algorithms that address the logistic bandit exhibit exponential dependence on the slope parameter beta, we establish a regret bound for Thompson sampling that is independent of beta. Specifically, we establish that, when the set of feasible actions is identical to the set of possible coefficient vectors, the Bayesian regret of Thompson sampling is tildeO(dsqrt(T)). We also establish a tildeO(sqrt(detaT)/lambda) bound that applies more broadly, where lambda is the worst-case optimal log-odds and eta is the "fragility dimension," a new statistic we define to capture the degree to which an optimal action for one model fails to satisfice for others. We demonstrate that the fragility dimension plays an essential role by showing that, for any epsilon > 0, no algorithm can achieve poly(d, 1/lambda)* T^-epsilon regret.

<!-- chunk {"id": "body-0003", "role": "body", "section": "Introduction", "weight": 1.5} -->

Each action $a$ and parameter vector $\theta$ is a vector within the $d$-dimensional unit ball. The agent initially knows the scale parameter $\beta$ but is uncertain about the coefficient vector $\theta$. The problem of learning to improve action selection over repeated interactions is sometimes referred to as the logistic bandit problem or online logistic regression.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

The logistic bandit serves as a model for a wide range of applications. One example is the problem of personalized recommendation, in which a service provider successively recommends content, receiving only binary responses from users, indicating "like" or "dislike." A growing literature treats the design and analysis of action selection algorithms for the logistic bandit. Upper-confidence-bound (UCB) algorithms have been analyzed in \[Filippi et al.Filippi, Cappe, Garivier, and Szepesvári, Li et al.Li, Lu, and Zhou, Russo and Van Roy\], while Thompson sampling (\[Thompson\]) was treated in \[Russo and Van Roy\] and \[Abeille and Lazaric\]. Each of these algorithms has been shown to converge on the optimal action with time dependence $\overset{\sim}{O}{({1/\sqrt{T}})}$, where $\overset{\sim}{O}$ ignores poly-logarithmic factors. However, previous analyses leave open the possibility that the convergence time increases exponentially with the parameter $\beta$, which seems counterintuitive.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

In particular, as $\beta$ increases, distinctions between good and bad actions become more definitive, which should make them easier to learn.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

To shed light on this issue, we build on an information-theoretic line of analysis, which was first proposed in \[Russo and Van Roy\] and further developed in \[Bubeck and Eldan\] and \[Dong and Van Roy\]. A critical device here is the information ratio, which quantifies the one-stage trade-off between exploration and exploitation. The information ratio has also motivated the design of efficient bandit algorithms, as in \[Russo and Van Roy\], \[Russo and Van Roy\] and \[Liu et al.Liu, Buccapatnam, and Shroff\]. While prior bounds on the information ratio pertain only to independent or linear bandits, in this work we develop a new technique for bounding the information ratio of a logistic bandit. This leads to a stronger regret bound and insight into the role of $\beta$.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

([Filippi et al.Filippi, Cappe, Garivier, and Szepesvári])

<!-- chunk {"id": "body-0008", "role": "body", "section": "Introduction", "weight": 1.5} -->

Our Contributions. Let $\mathcal{A}$ and $\Theta$ be the set of feasible actions and the support of $\theta$, respectively. Under an assumption that $\mathcal{A} = \Theta$, we establish a $\overset{\sim}{O}{({d\sqrt{T}})}$ bound on Bayesian regret. This bound scales with the dimension $d$, but notably exhibits no dependence on $\beta$ or the number of feasible actions. We then generalize this bound, relaxing the assumption that $\mathcal{A} = \Theta$ while introducing dependence on two statistics of the these sets: the worst-case optimal log-odds $\lambda = {\min_{\theta \in \Theta}{\max_{a \in \mathcal{A}}{\alpha^{\top}\theta}}}$ and the fragility dimension $\eta$, which is the number of possible models such that the optimal action for each yields success probability no greater than 50% for any other.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Introduction", "weight": 1.5} -->

Assuming $\lambda > 0$, we establish a $\overset{\sim}{O}{({\sqrt{d\etaT}/\lambda})}$ bound on Bayesian regret. We also demonstrate that the fragility dimension plays an essential role, as for any function $f$, polynomial $p$, and $\epsilon > 0$, any algorithm for the logistic bandit cannot achieve Bayesian regret uniformly bounded by $f{(\lambda)}p{(d)}T^{1 - \epsilon}$. We believe that, although $\eta$ can grow exponentially with $d$, in most relevant contexts $\eta$ should scale at most linearly with $d$.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Introduction", "weight": 1.5} -->

The assumption that the worst-case optimal log-odds are positive may be restrictive. This is equivalent to assuming that the for each possible model, the optimal action yields more than 50% probability of success. However, this assumption is essential, since it ensures that the fragility dimension is well-defined. When the worst-case optimal log-odds are negative, the geometry of action and parameter sets plays a less significant role than parameter $\beta$, therefore we conjecture that the exponential dependence on $\beta$ is inevitable. This could be an interesting direction for future research.\

<!-- chunk {"id": "body-0011", "role": "body", "section": "Introduction", "weight": 1.5} -->

Notations. Throughout this article, for integer $n$ we will use $\lbrack n\rbrack$ to denote the set $\{ 1,\ldots,n\}$. We will also use $\mathbf{B}_{d}$ and $\mathbf{S}_{d - 1}$ to denote the unit ball and the unit sphere in ${\mathbb{R}}^{d}$, respectively.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Problem Settings", "weight": 1.0} -->

We consider Bayesian generalized linear bandits, defined as a tuple $\mathcal{L} = {(\mathcal{A},\Theta,R,\phi,\rho)}$, where $\mathcal{A}$ and $\Theta$ are the action and parameter set, respectively, $R$ is a stochastic process representing the reward of playing each action, $\phi$ is the link function, and $\rho$ is the prior distribution over $\Theta$, which represents our prior belief of the groundtruth parameter $\theta^{\ast}$. Throughout this article, to avoid measure-theoretic subtleties, we assume that both $\mathcal{A}$ and $\Theta$ are finite subsets of $\mathbf{B}_{d}$. For simplicity, we assume that there exists a one-to-one mapping^33^3Note that Thompson sampling does not consider actions that are not optimal for any parameter.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Problem Settings", "weight": 1.0} -->

If an action is optimal for multiple parameters, we can add identical copies of the action to the action set such that the mapping between each parameter and the corresponding optimal action is one-to-one. between each parameter and the corresponding optimal action. Specifically, let $\mathcal{A} = {\{ a^{1},\ldots,a^{N}\}}$ and $\Theta = {\{\theta^{1},\ldots,\theta^{N}\}}$, with

<!-- chunk {"id": "body-0014", "role": "body", "section": "Problem Settings", "weight": 1.0} -->

To specify the one-to-one mapping, for each $\theta \in \Theta$ we define $\alpha{(\theta)}$ to be the unique action that maximizes ${\mathbb{E}}{\lbrack{\left. {R{(a)}} \middle| \theta^{\ast} \right. = \theta}\rbrack}$. Letting $A^{\ast}$ be the optimal action, which is a random variable under our Bayesian setting, naturally we have $A^{\ast} = {\alpha{(\theta^{\ast})}}$.

<!-- chunk {"id": "body-0015", "role": "body", "section": "Problem Settings", "weight": 1.0} -->

The reward $R$ is related to the inner product between the action and the parameter by the link function $\phi$, as

<!-- chunk {"id": "body-0016", "role": "body", "section": "Problem Settings", "weight": 1.0} -->

Specifically, in logistic bandits, the reward $R$ is the binary process $R_{B}$ and the link function is given by

<!-- chunk {"id": "body-0017", "role": "body", "section": "Problem Settings", "weight": 1.0} -->

where $\beta > 0$ is a parameter that characterizes the "separability" of the model. Equivalently, conditioned on $\theta^{\ast} = \theta$, $R_{B}{(a)}$ is a Bernoulli random variable with mean $\phi_{\beta}{({a^{\top}\theta})}$. In the following, we will use $\mathcal{L}_{\beta}$ to denote the logistic bandits problem instance with parameter $\beta$.

<!-- chunk {"id": "body-0018", "role": "body", "section": "Problem Settings", "weight": 1.0} -->

At stage $t$ the agent plays action $A_{t}$ and observes reward $R_{t} = {R{(A_{t})}}$. Let $\mathcal{H}_{t} = {\sigma{(A_{1},R_{1},\ldots,A_{t},R_{t})}}$ be the $\sigma$-algebra generated by the past actions and observations (rewards). A (randomized) policy $\pi = {(\pi_{1},\pi_{2},\ldots)}$ is a sequence of functions such that for each $t$, $\pi_{t}{(\mathcal{H}_{t - 1})}$ is a probability distribution on the action set. The performance of policy $\pi$ on problem instance $\mathcal{L} = {(\mathcal{A},\Theta,R,\phi,\rho)}$ is evaluated by the Bayesian regret, defined as

<!-- chunk {"id": "body-0019", "role": "body", "section": "Problem Settings", "weight": 1.0} -->

where $R^{\ast}:={R{(\theta^{\ast})}}$, the subscripts $\pi,\rho$ denote that $A_{t}$ is drawn from $\pi_{t}{(\mathcal{H}_{t - 1})}$ for $t \geq 1$ and $A_{0}$ is drawn from the prior $\rho$. In this work, we are interested in the Thompson sampling policy $\pi^{TS}$, characterized as

<!-- chunk {"id": "body-0020", "role": "body", "section": "Problem Settings", "weight": 1.0} -->

i.e. the action played in each stage is drawn from the posterior of the optimal action. Since there is a one-to-one mapping between each parameter and the corresponding optimal action, the Thompson sampling policy can be equivalently carried out by sampling from the posterior of the true parameter $\theta^{\ast}$ at each stage, and acting greedily with respect to the sampled parameter.

<!-- chunk {"id": "body-0021", "role": "body", "section": "Main Results", "weight": 1.0} -->

We start off the section with a regret bound that only depends on dimension $d$ and the number of time steps $T$, for the particular setting where the action set $\mathcal{A}$ is the same as the parameter set $\Theta$.

<!-- chunk {"id": "body-0022", "role": "body", "section": "Assumption 1", "weight": 1.0} -->

There exists constant $\lambda \in {\lbrack 0,1\rbrack}$ such that for every $\theta \in \Theta$ there is ${\alpha{(\theta)}^{\top}\theta} \geq \lambda$.

<!-- chunk {"id": "body-0023", "role": "body", "section": "Assumption 1", "weight": 1.0} -->

For a given logistic bandit problem instance $\mathcal{L}_{\beta} = {(\mathcal{A},\Theta,R,\phi_{\beta},\rho)}$ that satisfies Assumption 1, we show that the Bayesian regret of Thompson sampling on $\mathcal{L}_{\beta}$ is closely related to its "fragility dimension," a notion that we introduce below.

<!-- chunk {"id": "body-0024", "role": "body", "section": "Example 3.3", "weight": 1.0} -->

If the action set and the parameter set of $\mathcal{L}$ are identical subsets of $\mathbf{S}_{d - 1}$, then for each $\theta \in \Theta$, there is ${\alpha{(\theta)}} = \theta$. We will show in Appendix D.1 that in $\mathbf{S}_{d - 1}$ there exists at most $d + 1$ vectors with pairwise negative inner products. Therefore, the fragility dimension is bounded by

<!-- chunk {"id": "body-0025", "role": "body", "section": "Remark 3.4", "weight": 1.0} -->

Obviously the fragility dimension cannot exceed the cardinality of the action (parameter) set. We will show in Appendix D that we can upper bound the worst-case fragility dimension by the dimensionality $d$ and the constant $\lambda$ in Assumption 1. Roughly speaking,

<!-- chunk {"id": "body-0026", "role": "body", "section": "Remark 3.4", "weight": 1.0} -->

For any fixed $\lambda \in {}$, if we only consider problem instances such that Assumption 1 holds with constant $\lambda$, then the worst-case fragility dimension grows exponentially with $d$.

<!-- chunk {"id": "body-0027", "role": "body", "section": "Remark 3.4", "weight": 1.0} -->

For any $d \geq 3$, we can find a problem instance $\mathcal{L}$ such that Assumption 1 holds with constant $\lambda = 0$, whose fragility dimension is arbitrarily large.

<!-- chunk {"id": "body-0028", "role": "body", "section": "Remark 3.5", "weight": 1.0} -->

For given finite action and parameter sets $\mathcal{A}$ and $\Theta$, we can think of each parameter as a vertex in a graph $\mathcal{G}$. Two vertices $i$ and $j$ of $\mathcal{G}$ are connected by an edge if and only if

<!-- chunk {"id": "body-0029", "role": "body", "section": "Remark 3.5", "weight": 1.0} -->

Thus determining the fragility dimension of $(\mathcal{A},\Theta)$ is equivalent to finding the maximum clique in $\mathcal{G}$. This is a widely studied NP-complete problem and there exists a number of efficient heuristics, see \[Tarjan and Trojanowski\], \[Tomita and Kameda\] and references therein.

<!-- chunk {"id": "body-0030", "role": "body", "section": "Remark 3.5", "weight": 1.0} -->

The following general result for the performance of Thompson sampling gives a $\overset{\sim}{O}{({\sqrt{d\etaT}/\lambda})}$ regret bound.

<!-- chunk {"id": "body-0031", "role": "body", "section": "Remark 3.7", "weight": 1.0} -->

Considering Example 3.3, and noting that when $\mathcal{A} = \Theta$, Assumption 1 holds with $\lambda = 1$, we immediately arrive at Theorem 3.1.

<!-- chunk {"id": "body-0032", "role": "body", "section": "Remark 3.8", "weight": 1.0} -->

Interestingly, the fragility dimension is not monotonic with respect to the inclusion of sets, i.e. there exist sets $\mathcal{X}_{1},\mathcal{X}_{2},\mathcal{Y}$, such that $\mathcal{X}_{1} \subset \mathcal{X}_{2}$ but ${\eta{(\mathcal{X}_{1},\mathcal{Y})}} > {\eta{(\mathcal{X}_{2},\mathcal{Y})}}$. As we show in Appendix D.4, this fact means that by reducing the size of the action set, we could arrive at a more difficult problem. This is a somewhat surprising result that is worth noting.

<!-- chunk {"id": "body-0033", "role": "body", "section": "Remark 3.8", "weight": 1.0} -->

We also show that the $\eta$ term in is critical, since for any fixed $\lambda < 1$, there cannot exist an $\eta$-independent upper bound that is polynomial in $d$ and sublinear in $T$.

<!-- chunk {"id": "body-0034", "role": "body", "section": "Main Devices in the proof of Theorem 3.6", "weight": 1.0} -->

In this section we discuss the two main devices in the proof of Theorem 3.6. In Section 4.1, we introduce the notion of information ratio, and present the result that relates information ratio with Bayesian regret. In Section 4.2, we highlight the role of fragility dimension. The full proof of Theorem 3.6 is given in Appendix B.

<!-- chunk {"id": "body-0035", "role": "body", "section": "Information Ratio", "weight": 1.0} -->

To quantify the exploration-exploitation trade-off at stage $t$, for problem instance $\mathcal{L}$ and policy $\pi$ we define the random variable information ratio as the square of one-stage expected regret divided by the amount of information that the agent gains from playing an action and observing the reward, i.e.

<!-- chunk {"id": "body-0036", "role": "body", "section": "Information Ratio", "weight": 1.0} -->

where the subscript $t - 1$ in the right-hand side denotes evaluation under base measure ${\mathbb{P}}{( \cdot |\mathcal{H}_{t - 1})}$. If the information ratio is small at stage $t$, the agent executing the policy $\pi$ will only incur a large regret if she is about to acquire a large amount of information towards the optimal action. Past results have shown that, as long as the information ratio of Thompson sampling can be uniformly bounded, we immediately obtain a bound on the Bayesian regret of Thompson sampling.

<!-- chunk {"id": "body-0037", "role": "body", "section": "Fragility Dimension", "weight": 1.0} -->

The one-stage expected regret can be written as

<!-- chunk {"id": "body-0038", "role": "body", "section": "Fragility Dimension", "weight": 1.0} -->

It is worth noting that $A^{\ast} = {\alpha{(\theta^{\ast})}}$ and by the definition of Thompson sampling, $A^{\ast}$ and $A_{t}$ are independent and identically distributed. Let's first consider the simple case where $\beta = \infty$, which motivates our analysis. When $\beta = \infty$, we have that ${\phi_{\beta}{(x)}} = 1$ for all $x \geq 0$ and ${\phi_{\beta}{(x)}} = 0$ for all $x < 0$^44^4For the sake of simplicity, we will assume that ${\phi_{\infty}{}} = 1$, while in fact ${\lim_{\beta\rightarrow\infty}{\phi_{\beta}{}}} = {1/2}$. The value of $\phi_{\infty}{}$ does not play a role in our analysis..

<!-- chunk {"id": "body-0039", "role": "body", "section": "Fragility Dimension", "weight": 1.0} -->

Therefore, to upper bound the right-hand side of, we need to lower bound ${\mathbb{P}}_{t - 1}{({{A_{t}^{\top}\theta^{\ast}} \geq 0})}$. The proposition below shows that this term is connected critically with the fragility dimension of $(\mathcal{A},\Theta)$. The proof is given in Appendix A.
