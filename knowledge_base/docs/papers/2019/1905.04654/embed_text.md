## Introduction

In the logistic bandit an agent observes a binary reward after each action, with outcome probabilities governed by a logistic function: Each action $a$ and parameter vector $\theta$ is a vector within the $d$-dimensional unit ball. The agent initially knows the scale parameter $\beta$ but is uncertain about the coefficient vector $\theta$. The problem of learning to improve action selection over repeated interactions is sometimes referred to as the logistic bandit problem or online logistic regression.

The logistic bandit serves as a model for a wide range of applications. One example is the problem of personalized recommendation, in which a service provider successively recommends content, receiving only binary responses from users, indicating "like" or "dislike." A growing literature treats the design and analysis of action selection algorithms for the logistic bandit. Upper-confidence-bound (UCB) algorithms have been analyzed in \[Filippi et al.Filippi, Cappe, Garivier, and Szepesvári, Li et al.Li, Lu, and Zhou, Russo and Van Roy\], while Thompson sampling (\[Thompson\]) was treated in \[Russo and Van Roy\] and \[Abeille and Lazaric\]. Each of these algorithms has been shown to converge on the optimal action with time dependence $\overset{\sim}{O}{({1/\sqrt{T}})}$, where $\overset{\sim}{O}$ ignores poly-logarithmic factors. However, previous analyses leave open the possibility that the convergence time increases exponentially with the parameter $\beta$, which seems counterintuitive. In particular, as $\beta$ increases, distinctions between good and bad actions become more definitive, which should make them easier to learn.

To shed light on this issue, we build on an information-theoretic line of analysis, which was first proposed in \[Russo and Van Roy\] and further developed in \[Bubeck and Eldan\] and \[Dong and Van Roy\]. A critical device here is the information ratio, which quantifies the one-stage trade-off between exploration and exploitation. The information ratio has also motivated the design of efficient bandit algorithms, as in \[Russo and Van Roy\], \[Russo and Van Roy\] and \[Liu et al.Liu, Buccapatnam, and Shroff\]. While prior bounds on the information ratio pertain only to independent or linear bandits, in this work we develop a new technique for bounding the information ratio of a logistic bandit. This leads to a stronger regret bound and insight into the role of $\beta$.

Regret Upper Bound ([Filippi et al.Filippi, Cappe, Garivier, and Szepesvári]) ([Russo and Van Roy]) K is the number of actions.

([Russo and Van Roy]) ([Abeille and Lazaric]) λ and η are independent of β Table 1: Comparison of various results on logistic bandits. The upper bound in this work depends on β-independent parameters λ and η, defined in Assumption 1 and Definition 3.2, respectively. We use the notation a ∨ b = max {a, b}.

Our Contributions. Let $\mathcal{A}$ and $\Theta$ be the set of feasible actions and the support of $\theta$, respectively. Under an assumption that $\mathcal{A} = \Theta$, we establish a $\overset{\sim}{O}{({d\sqrt{T}})}$ bound on Bayesian regret. This bound scales with the dimension $d$, but notably exhibits no dependence on $\beta$ or the number of feasible actions. We then generalize this bound, relaxing the assumption that $\mathcal{A} = \Theta$ while introducing dependence on two statistics of the these sets: the worst-case optimal log-odds $\lambda = {\min_{\theta \in \Theta}{\max_{a \in \mathcal{A}}{\alpha^{\top}\theta}}}$ and the fragility dimension $\eta$, which is the number of possible models such that the optimal action for each yields success probability no greater than 50% for any other. Assuming $\lambda > 0$, we establish a $\overset{\sim}{O}{({\sqrt{d\etaT}/\lambda})}$ bound on Bayesian regret. We also demonstrate that the fragility dimension plays an essential role, as for any function $f$, polynomial $p$, and $\epsilon > 0$, any algorithm for the logistic bandit cannot achieve Bayesian regret uniformly bounded by $f{(\lambda)}p{(d)}T^{1 - \epsilon}$. We believe that, although $\eta$ can grow exponentially with $d$, in most relevant contexts $\eta$ should scale at most linearly with $d$.

The assumption that the worst-case optimal log-odds are positive may be restrictive. This is equivalent to assuming that the for each possible model, the optimal action yields more than 50% probability of success. However, this assumption is essential, since it ensures that the fragility dimension is well-defined. When the worst-case optimal log-odds are negative, the geometry of action and parameter sets plays a less significant role than parameter $\beta$, therefore we conjecture that the exponential dependence on $\beta$ is inevitable. This could be an interesting direction for future research.\Notations. Throughout this article, for integer $n$ we will use $\lbrack n\rbrack$ to denote the set $\{ 1,\ldots,n\}$. We will also use $\mathbf{B}_{d}$ and $\mathbf{S}_{d - 1}$ to denote the unit ball and the unit sphere in ${\mathbb{R}}^{d}$, respectively.

## Problem Settings

We consider Bayesian generalized linear bandits, defined as a tuple $\mathcal{L} = {(\mathcal{A},\Theta,R,\phi,\rho)}$, where $\mathcal{A}$ and $\Theta$ are the action and parameter set, respectively, $R$ is a stochastic process representing the reward of playing each action, $\phi$ is the link function, and $\rho$ is the prior distribution over $\Theta$, which represents our prior belief of the groundtruth parameter $\theta^{\ast}$. Throughout this article, to avoid measure-theoretic subtleties, we assume that both $\mathcal{A}$ and $\Theta$ are finite subsets of $\mathbf{B}_{d}$. For simplicity, we assume that there exists a one-to-one mapping^33^3Note that Thompson sampling does not consider actions that are not optimal for any parameter. If an action is optimal for multiple parameters, we can add identical copies of the action to the action set such that the mapping between each parameter and the corresponding optimal action is one-to-one. between each parameter and the corresponding optimal action. Specifically, let $\mathcal{A} = {\{ a^{1},\ldots,a^{N}\}}$ and $\Theta = {\{\theta^{1},\ldots,\theta^{N}\}}$, with To specify the one-to-one mapping, for each $\theta \in \Theta$ we define $\alpha{(\theta)}$ to be the unique action that maximizes ${\mathbb{E}}{\lbrack{\left. {R{(a)}} \middle| \theta^{\ast} \right. = \theta}\rbrack}$. Letting $A^{\ast}$ be the optimal action, which is a random variable under our Bayesian setting, naturally we have $A^{\ast} = {\alpha{(\theta^{\ast})}}$.

The reward $R$ is related to the inner product between the action and the parameter by the link function $\phi$, as Specifically, in logistic bandits, the reward $R$ is the binary process $R_{B}$ and the link function is given by where $\beta > 0$ is a parameter that characterizes the "separability" of the model. Equivalently, conditioned on $\theta^{\ast} = \theta$, $R_{B}{(a)}$ is a Bernoulli random variable with mean $\phi_{\beta}{({a^{\top}\theta})}$. In the following, we will use $\mathcal{L}_{\beta}$ to denote the logistic bandits problem instance with parameter $\beta$.

At stage $t$ the agent plays action $A_{t}$ and observes reward $R_{t} = {R{(A_{t})}}$. Let $\mathcal{H}_{t} = {\sigma{(A_{1},R_{1},\ldots,A_{t},R_{t})}}$ be the $\sigma$-algebra generated by the past actions and observations (rewards). A (randomized) policy $\pi = {(\pi_{1},\pi_{2},\ldots)}$ is a sequence of functions such that for each $t$, $\pi_{t}{(\mathcal{H}_{t - 1})}$ is a probability distribution on the action set. The performance of policy $\pi$ on problem instance $\mathcal{L} = {(\mathcal{A},\Theta,R,\phi,\rho)}$ is evaluated by the Bayesian regret, defined as where $R^{\ast}:={R{(\theta^{\ast})}}$, the subscripts $\pi,\rho$ denote that $A_{t}$ is drawn from $\pi_{t}{(\mathcal{H}_{t - 1})}$ for $t \geq 1$ and $A_{0}$ is drawn from the prior $\rho$. In this work, we are interested in the Thompson sampling policy $\pi^{TS}$, characterized as i.e. the action played in each stage is drawn from the posterior of the optimal action. Since there is a one-to-one mapping between each parameter and the corresponding optimal action, the Thompson sampling policy can be equivalently carried out by sampling from the posterior of the true parameter $\theta^{\ast}$ at each stage, and acting greedily with respect to the sampled parameter.

## Main Results

We start off the section with a regret bound that only depends on dimension $d$ and the number of time steps $T$, for the particular setting where the action set $\mathcal{A}$ is the same as the parameter set $\Theta$.

### Theorem 3.1

For any $\beta > 0$, if $\mathcal{L}_{\beta} = {(\mathcal{A},\Theta,R_{B},\phi_{\beta},\rho)}$ is such that ${\mathcal{A},\Theta} \subset \mathbf{S}_{d - 1}$ and $\mathcal{A} = \Theta$, then Despite nonlinearity of the link function, Theorem 3.1 matches the $\overset{\sim}{O}{({d\sqrt{T}})}$ bound for linear bandits. It is worth noting that the this bound has no dependence on $\beta$ or the number of arms, and also matches the $\Omega{({d\sqrt{T}})}$ minimax lower bound for linear bandits in \[Dani et al.Dani, Hayes, and Kakade\], ignoring a $\sqrt{\log T}$ factor. This result shows that if there exists an action that aligns perfectly with each potential parameter, the performance of Thompson sampling only depends on the problem dimension $d$, and the dependence is at most linear.

However, as our next result shows, if the parameters do not align perfectly with their corresponding optimal actions, we have to introduce the fragility dimension to characterize the difficulty of the problem.

For our general result, we assume that the following assumption holds.

### Assumption 1

There exists constant $\lambda \in {\lbrack 0,1\rbrack}$ such that for every $\theta \in \Theta$ there is ${\alpha{(\theta)}^{\top}\theta} \geq \lambda$.

For a given logistic bandit problem instance $\mathcal{L}_{\beta} = {(\mathcal{A},\Theta,R,\phi_{\beta},\rho)}$ that satisfies Assumption 1, we show that the Bayesian regret of Thompson sampling on $\mathcal{L}_{\beta}$ is closely related to its "fragility dimension," a notion that we introduce below.

### Definition 3.2

For any given pair of (possibly infinite) subsets $(\mathcal{X},\mathcal{Y})$ of $\mathbf{B}_{d}$, the fragility dimension, denoted by $\eta{(\mathcal{X},\mathcal{Y})}$, is defined as the largest integer $M$, such that there exists ${\{ y_{1},\ldots,y_{M}\}} \subseteq \mathcal{Y}$, with where ${f^{\ast}{(y)}}:={\operatorname{argmax}_{x \in \mathcal{X}}{x^{\top}y}}$. The fragility dimension of a problem instance $\mathcal{L}_{0} = {(\mathcal{A}_{0},\Theta_{0},R_{0},\phi_{0},\rho_{0})}$ is defined as the fragility dimension of $(\mathcal{A}_{0},\Theta_{0})$, and is denoted by $\eta{(\mathcal{L}_{0})}$.

### Example 3.3

If the action set and the parameter set of $\mathcal{L}$ are identical subsets of $\mathbf{S}_{d - 1}$, then for each $\theta \in \Theta$, there is ${\alpha{(\theta)}} = \theta$. We will show in Appendix D.1 that in $\mathbf{S}_{d - 1}$ there exists at most $d + 1$ vectors with pairwise negative inner products. Therefore, the fragility dimension is bounded by

### Remark 3.4

Obviously the fragility dimension cannot exceed the cardinality of the action (parameter) set. We will show in Appendix D that we can upper bound the worst-case fragility dimension by the dimensionality $d$ and the constant $\lambda$ in Assumption 1. Roughly speaking, If $\mathcal{L}$ is such that $\lambda = 1$, then ${\eta{(\mathcal{L})}} \leq {d + 1}$ (cf. Example 3.3); For any fixed $\lambda \in {}$, if we only consider problem instances such that Assumption 1 holds with constant $\lambda$, then the worst-case fragility dimension grows exponentially with $d$.

For any $d \geq 3$, we can find a problem instance $\mathcal{L}$ such that Assumption 1 holds with constant $\lambda = 0$, whose fragility dimension is arbitrarily large.

### Remark 3.5

For given finite action and parameter sets $\mathcal{A}$ and $\Theta$, we can think of each parameter as a vertex in a graph $\mathcal{G}$. Two vertices $i$ and $j$ of $\mathcal{G}$ are connected by an edge if and only if Thus determining the fragility dimension of $(\mathcal{A},\Theta)$ is equivalent to finding the maximum clique in $\mathcal{G}$. This is a widely studied NP-complete problem and there exists a number of efficient heuristics, see \[Tarjan and Trojanowski\], \[Tomita and Kameda\] and references therein.

The following general result for the performance of Thompson sampling gives a $\overset{\sim}{O}{({\sqrt{d\etaT}/\lambda})}$ regret bound.

### Theorem 3.6

For any $\beta > 0$, if $\mathcal{L}_{\beta}$ is such that Assumption 1 holds with $\lambda \in {(0,1\rbrack}$, then where ${a \vee b} = {\max{\{ a,b\}}}$. It is worth noting that the fragility dimension only depends on the action and parameter sets of the problem instance, hence the right-hand side of has no dependence on $\beta$.

### Remark 3.7

Considering Example 3.3, and noting that when $\mathcal{A} = \Theta$, Assumption 1 holds with $\lambda = 1$, we immediately arrive at Theorem 3.1.

### Remark 3.8

Interestingly, the fragility dimension is not monotonic with respect to the inclusion of sets, i.e. there exist sets $\mathcal{X}_{1},\mathcal{X}_{2},\mathcal{Y}$, such that $\mathcal{X}_{1} \subset \mathcal{X}_{2}$ but ${\eta{(\mathcal{X}_{1},\mathcal{Y})}} > {\eta{(\mathcal{X}_{2},\mathcal{Y})}}$. As we show in Appendix D.4, this fact means that by reducing the size of the action set, we could arrive at a more difficult problem. This is a somewhat surprising result that is worth noting.

We also show that the $\eta$ term in is critical, since for any fixed $\lambda < 1$, there cannot exist an $\eta$-independent upper bound that is polynomial in $d$ and sublinear in $T$.

### Theorem 3.9

For any fixed $\lambda \in {\lbrack 0,1)}$, let $f{(\cdot)}$ be any real function, $p{(\cdot)}$ be any polynomial and $\epsilon > 0$ be any constant. There exists a logistic bandit problem instance $\mathcal{L}_{\beta}$ and integer $T_{0}$ such that $\mathcal{L}_{\beta}$ satisfies Assumption 1 with constant $\lambda$ and for any policy $\pi$.

## Main Devices in the proof of Theorem 3.6

In this section we discuss the two main devices in the proof of Theorem 3.6. In Section 4.1, we introduce the notion of information ratio, and present the result that relates information ratio with Bayesian regret. In Section 4.2, we highlight the role of fragility dimension. The full proof of Theorem 3.6 is given in Appendix B.

### Information Ratio

To quantify the exploration-exploitation trade-off at stage $t$, for problem instance $\mathcal{L}$ and policy $\pi$ we define the random variable information ratio as the square of one-stage expected regret divided by the amount of information that the agent gains from playing an action and observing the reward, i.e. where the subscript $t - 1$ in the right-hand side denotes evaluation under base measure ${\mathbb{P}}{(\cdot |\mathcal{H}_{t - 1})}$. If the information ratio is small at stage $t$, the agent executing the policy $\pi$ will only incur a large regret if she is about to acquire a large amount of information towards the optimal action. Past results have shown that, as long as the information ratio of Thompson sampling can be uniformly bounded, we immediately obtain a bound on the Bayesian regret of Thompson sampling.

### Proposition 4.1

(Theorem 4, \[Dong and Van Roy\]) Let $\mathcal{L}_{\beta} = {(\mathcal{A},\Theta,R,\phi_{\beta},\rho)}$ be any logistic bandit problem instance with ${\inf_{\theta \in \Theta}{|{\alpha{(\theta)}^{\top}\theta}|}} = \delta > 0$. Further assume that there exists constant $\overline{\Gamma}$ such that

### Fragility Dimension

The one-stage expected regret can be written as It is worth noting that $A^{\ast} = {\alpha{(\theta^{\ast})}}$ and by the definition of Thompson sampling, $A^{\ast}$ and $A_{t}$ are independent and identically distributed. Let's first consider the simple case where $\beta = \infty$, which motivates our analysis. When $\beta = \infty$, we have that ${\phi_{\beta}{(x)}} = 1$ for all $x \geq 0$ and ${\phi_{\beta}{(x)}} = 0$ for all $x < 0$^44^4For the sake of simplicity, we will assume that ${\phi_{\infty}{}} = 1$, while in fact ${\lim_{\beta\rightarrow\infty}{\phi_{\beta}{}}} = {1/2}$. The value of $\phi_{\infty}{}$ does not play a role in our analysis.. By Assumption 1, we have Therefore, to upper bound the right-hand side of, we need to lower bound ${\mathbb{P}}_{t - 1}{({{A_{t}^{\top}\theta^{\ast}} \geq 0})}$. The proposition below shows that this term is connected critically with the fragility dimension of $(\mathcal{A},\Theta)$. The proof is given in Appendix A.

### Proposition 4.2

Let $\mathcal{U},\mathcal{V}$ be finite subsets of $\mathbf{B}_{d}$. Suppose that there exists bijection $f^{\ast}:{\mathcal{V}\mapsto\mathcal{U}}$ such that and ${f^{\ast}{(v)}^{\top}v} > 0$ for all $v \in \mathcal{V}$. Let $V$ be any random variable supported on $\mathcal{V}$, $U = {f^{\ast}{(V)}}$ and $\hat{U}$ be an iid copy of $U$. Then

## Proof Sketch of Theorem 3.9

Recall that we can obtain regret bounds for linear bandits that are dependent only on the dimensionality of the problem $d$ rather than the number of actions (such as the one in \[Russo and Van Roy\]). The reason behind such bounds is that when the link function $\phi$ is linear, the difference between the mean rewards of two actions that are close to each other is always small. However, in logistic bandit problems, when parameter $\beta$ is large, we could run into cases where two close actions yield diametrically different rewards, as is illustrated in Figure 1.

Figure 1: The difference between linear and logistic bandits. The actions a1 and a2 are “similar” to each other in that their embeddings in the Euclidean space are close. Under the linear link function ϕ1, the mean rewards of a1 and a2 are also similar. However, under the logistic link function ϕ2, the performances of the two actions are diametrical.

Specifically, suppose that our action and parameter sets are such that that is, ${\eta{(\mathcal{A},\Theta)}} = {|\mathcal{A}|} = {|\Theta|}$. Then, when $\beta$ is large, conditioned on each parameter being the true parameter, there is exactly one action with mean reward close to 1, while the mean rewards of all other actions are close to 0. The following proposition shows that in this problem the optimal action is inherently hard to learn, in the sense that the regret of any algorithm grows linearly in the first ${{|\mathcal{A}|}/2} - 1$ stages. The proof can be found in Appendix C.

### Proposition 5.1

Let $\mathcal{L} = {(\mathcal{A},\Theta,R,\phi,\rho)}$ be a generalized linear bandit problem such that ${|\mathcal{A}|} = N < \infty$, $R$ is binary and $\rho$ is the uniform distribution over $\mathcal{A}$. Suppose that for each $a \in \mathcal{A}$, Then for any policy $\pi$, We can also show that (as in Appendix D), for any fixed $\lambda \in {}$, there exists $\gamma > 1$, such that for any $d \geq 2$ we can find a pair of action and parameter sets $(\mathcal{A}_{d},\Theta_{d})$ with ${\mathcal{A}_{d},\Theta_{d}} \in {\mathbb{R}}^{d}$, ${|\mathcal{A}_{d}|} = {|\Theta_{d}|} \geq \gamma^{d}$ that satisfies, and Assumption 1 with constant $\lambda$. For any real function $f{(\cdot)}$, polynomial $p{(\cdot)}$ and constant $\epsilon \in {}$, choose $d$ large enough such that $\gamma^{\epsilond} > {16f{(\lambda)}p{(d)}}$ and $\beta_{d}$ large enough such that Consider the problem $\mathcal{L} = {(\mathcal{A}_{d},\Theta_{d},R_{B},\phi_{\beta_{d}},{{Unif}{(\mathcal{A})}})}$ at stage $T_{0} = {\gamma^{d}/4}$, from Proposition 5.1 we have for any policy $\pi$.

Toyota Research Institute (TRI) provided funds to assist the authors (Tengyu Ma) with their research but this article solely reflects the opinions and conclusions of its authors and not TRI or any other Toyota entity. Shi Dong is supported by the Herb and Jane Dwight Stanford Graduate Fellowship.
