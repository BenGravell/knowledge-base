## Introduction

We focus on quantifying the difficulty of fixed-budget best-arm identification (BAI) problem in non-stationary linear bandits. The linear bandit framework generalizes the classical multi-armed bandit problem by associating each arm with a feature vector and modeling rewards as linear in an unknown parameter. Algorithms such as UCB and Thompson Sampling are known to perform optimally in the well-studied regret-minimization setting. However, in the best-arm identification setting, where exploration is more important than cumulative reward, these algorithms are suboptimal, thus requiring specialized attention. In the standard BAI setting, a stationary environment is assumed where the rewards of arms are sampled i.i.d. However, algorithms designed for these environments can completely fail as soon as this assumption is lifted, for example, in settings where the value of an arm can change at any time step. An interesting question is *exactly how the difficulty of this setting changes once this stationary assumption is lifted*.

In recent work, Xiong et al. partially answered this question by showing that when the arm set is restricted to the standard basis, the difficulty of non-stationary BAI scales proportionally with the dimension. While informative, this result is ultimately unsatisfying as it collapses the linear bandit model back into a multi-armed bandit. Basis arm sets erase correlations between arms, precisely the geometric structure that linear bandits are meant to exploit. With this in mind, we aim to uncover precisely which relationship between arms truly governs the difficulty of non-stationary BAI. Inspired by Soare et al., a natural conjecture is that the pairwise relationships between every arm should be considered when measuring difficulty. However, such a characterization implies that any arm set containing a basis is no easier than the basis itself, and thus no progress is made. To refine this view, we introduce adjacency, a geometric notion that captures which pairs of arms can compete for optimality. Accordingly, we find that the pairwise relationships between adjacent arms are necessary and sufficient to measure the difficulty of non-stationary BAI. Formally, by leveraging the adjacent structure of the arm set, we refine the previous notion of difficulty in non-stationary BAI by establishing a measure of complexity that adapts to the geometry of any arm set, which we term as arm-set-dependent.

### Our contributions

Adjacency and Non-Stationary BAI. The main novelty of our paper stems from our characterization of non-stationary BAI as a problem of differentiating only between adjacent arms, a notion we formalize in later sections. The intuition for this restriction stems from our central Lemma 1. ‣ 4.2 Adjacency and Non-Stationary BAI ‣ 4 BAI in Non-Stationary Linear Bandits ‣ On The Complexity of Best-Arm Identification in Non-Stationary Linear Bandits"), which implies that if an arm is better than its adjacent arms, then it is the optimal arm. Accordingly, we introduce a new arm-set-dependent complexity measure $H_{Adjacent}{(\mathcal{X})}$ and show it strictly refines the minimax-optimal complexity $H_{G}$.

Arm-set-dependent lower bound. We show in Theorem 1 that for fixed arm set $\mathcal{X}$, the error probability of any algorithm must be at least $\exp\left( {- {O\left( {{T/H_{Adjacent}}{(\mathcal{X})}} \right)}} \right)$. Our lower bound builds off of previous works concerning lower bounds in best-arm identification for the multi-armed bandit setting. However, these methods alone are not sufficient for the linear setting, which we address by characterizing the lower bound as an optimization problem in Lemma 3. ‣ First step. ‣ 5.1 Proof Sketch of Theorem 1 ‣ 5 Lower Bound of BAI in Non-Stationary Linear Bandits ‣ On The Complexity of Best-Arm Identification in Non-Stationary Linear Bandits"), and which we solve in Lemma 4 by exploiting the adjacent geometry of the arm set.

Matching upper bound. We introduce the Adjacent-optimal design, a specialization of the well-known $\mathcal{X}\mathcal{Y}$-optimal design, that instead reduces variance only between adjacent arms. Using the Adjacent-optimal design, we introduce the algorithm Adjacent-BAI. Utilizing Lemma 1. ‣ 4.2 Adjacency and Non-Stationary BAI ‣ 4 BAI in Non-Stationary Linear Bandits ‣ On The Complexity of Best-Arm Identification in Non-Stationary Linear Bandits"), we obtain Theorem 2. ‣ 6.2 Adjacent-Optimal Best-Arm Identification (Adjacent-BAI) ‣ 6 Matching Upper Bound ‣ On The Complexity of Best-Arm Identification in Non-Stationary Linear Bandits") showing that for fixed arm set $\mathcal{X}$, the error probability of Adjacent-BAI is at most $\exp\left( {- {\Omega\left( {{T/H_{Adjacent}}{(\mathcal{X})}} \right)}} \right)$, verifying the tightness of our lower bound, and establishing $H_{Adjacent}{(\mathcal{X})}$ as the arm-set-dependent complexity measure of this setting.

## Related Work

Best-arm identification (BAI) seeks to identify the optimal arm while ignoring cumulative reward or regret. Even-Dar et al. marked the first substantial result in this area and the problem is now studied under two canonical settings: (i) the *fixed-confidence* setting, where the learner attains a prescribed error probability target using as few pulls as possible, and (ii) the *fixed-budget* setting, where the learner minimizes the error probability under a prescribed sampling budget; the latter was introduced by Bubeck et al..

### Best-arm identification with fixed confidence

For multi-armed bandits, Even-Dar et al. established the first sample-complexity upper bound, with a nearly matching lower bound later given by Mannor and Tsitsiklis. These bounds were subsequently tightened by Karnin et al. and Kaufmann et al.. Notably, Kaufmann et al. derived a general information-theoretic lower bound that underpins many linear-bandit lower bounds. In linear bandits, Soare et al. proposed the seminal $\mathcal{X}\mathcal{Y}$-allocation strategy, which has been refined and generalized in follow-up work. Nearly matching lower bounds were also established by Fiez et al. and Jedra and Proutiere.

### Best-arm identification with fixed budget

For multi-armed bandits, Audibert and Bubeck provided nearly matching upper and lower bounds, with improvements due to Karnin et al. and Kaufmann et al.. In contrast, comparatively little is known for linear bandits in this setting. Among existing results, Katz-Samuels et al. ---via a Gaussian-width analysis---gave the only arm-set-dependent upper bound. Methods based on G-optimal design yield arm-set-*independent* guarantees, as does the Bayesian-style approach of Hoffman et al.; similarly, a method based on the $\mathcal{X}\mathcal{Y}$-design in Alieva et al. remains arm-set-independent. On the lower-bound side, Yang and Tan proved a minimax bound, but to date, there is no arm-set-dependent lower bound for stationary linear bandits in the fixed-budget setting.

### Best-arm identification in non-stationary environments

Compared with regret minimization, non-stationarity has received less attention in BAI. In the fixed-confidence regime, non-stationary multi-armed bandits under models different from ours were studied by Jamieson and Talwalkar and Li et al.. In the fixed-budget regime, Abbasi-Yadkori et al. analyzed multi-armed bandits from a best-of-both-worlds perspective and established matching upper and lower bounds in a non-stationary setting; Xiong et al. extended the upper bounds to linear bandits. However, Xiong et al. does not provide lower bounds, and its non-stationary guarantees are arm-set-independent. Our work adopts a non-stationary model similar to Abbasi-Yadkori et al. and Xiong et al. and, to the best of our knowledge, presents the first arm-set-dependent lower bound for the fixed-budget setting.

## Preliminaries

### Notation

For $n \in {\mathbb{N}}$, denote ${\lbrack n\rbrack} = {\{ 1,\ldots,n\}}$. For a vector $x \in {\mathbb{R}}^{d}$ and a positive semidefinite matrix $A \in {\mathbb{S}}_{+}^{d}$, denote ${\| x\|}_{A} = \sqrt{x^{\top}Ax}$ as the Mahalanobis norm. For finite set $\mathcal{X} \subset {\mathbb{R}}^{d}$, and distribution $\lambda \in \bigtriangleup_{\mathcal{X}}$ over $\mathcal{X}$, denote ${A{(\lambda)}} = {\sum_{x \in \mathcal{X}}{\lambda_{x}xx^{\top}}}$. For $n \in {\mathbb{N}}$, denote $\Pi{(n)}$ as the set of all permutations on $\lbrack n\rbrack$.

### Definition 1

Given a finite set $\mathcal{X} \subset {\mathbb{R}}^{d}$, let $\mathcal{P} = {{conv}{(\mathcal{X})}}$ be the convex hull of $\mathcal{X}$, which is a polytope. We say $x \in \mathcal{X}$ is an extreme point if there exists $w \in {\mathbb{R}}^{d}$ such that

Equivalently, the extreme points of $\mathcal{X}$ are the vertices of $\mathcal{P}$. Two distinct extreme points ${x,x^{\prime}} \in \mathcal{X}$ are adjacent if there exists $w \in {\mathbb{R}}^{d}$ such that

Equivalently, $x$ and $x^{\prime}$ are adjacent if the line segment connecting them is an edge of $\mathcal{P}$.

Let $\mathcal{V}_{\mathcal{X}}$ denote the set of extreme points of $\mathcal{X}$. We denote

as the set of all distinct extreme point pairs of $\mathcal{X}$. Further, we denote

as the set of all adjacent pairs of $\mathcal{X}$, and, for $x \in \mathcal{V}_{\mathcal{X}}$, we denote

as the set of all points adjacent to $x$. It follows from this notation that

We omit the $\mathcal{X}$ subscript when clear from context.

## BAI in Non-Stationary Linear Bandits

We adopt a standard model of non-stationary linear bandits with fixed horizon $T \in {\mathbb{N}}$. In particular, given a finite arm set $\mathcal{X} \subset {\mathbb{R}}^{d}$ with ${|\mathcal{X}|} = K$ and ${{span}{(\mathcal{X})}} = {\mathbb{R}}^{d}$, an adversary fixes the parameter sequence $\left\{ \theta_{t} \right\}_{t = 1}^{T}$, which remains unknown to the learner. Then, at each round $t = {1,\ldots,T}$, the learner selects arm $x_{t} \in \mathcal{X}$ and observes a reward $r_{t} = {{x_{t}^{\top}\theta_{t}} + \epsilon_{t}}$, where each $\epsilon_{t}$ is independent, zero-mean, and 1-sub-Gaussian noise. Together, the arm set $\mathcal{X}$, parameter sequence $\left\{ \theta_{t} \right\}_{t = 1}^{T}$, and distribution of $\left\{ \epsilon_{t} \right\}_{t = 1}^{T}$ form an instance. The learner's objective is to identify the hindsight best arm $x_{\ast} = {\operatorname{argmax}_{x \in \mathcal{X}}{x^{\top}{\overline{\theta}}_{T}}}$, where ${\overline{\theta}}_{T} = {\frac{1}{T}{\sum_{t = 1}^{T}\theta_{t}}}$, and for simplicity, we assume that this best arm is unique.

A central measure of difficulty in bandit problems is the reward gap between the first and second best arm. Here, we deviate slightly from the standard definition by defining this gap only in terms of extreme points $\mathcal{V}$. This restriction is natural since by definition, non-extreme point arms can never be the best arm, and thus do not affect problem difficulty. Formally, we define the min-gap $\Delta_{}$ as the following:

Finally, for event $\mathcal{E}$, we denote ${\mathbb{P}}_{{\{\theta_{t}\}}_{t = 1}^{T}}{(\mathcal{E})}$ as the probability of $\mathcal{E}$ under instance with parameter sequence $\left\{ \theta_{t} \right\}_{t = 1}^{T}$. Accordingly, we measure algorithmic performance by the error probability ${\mathbb{P}}_{{\{\theta_{t}\}}_{t = 1}^{T}}{({\hat{x} \neq x_{\ast}})}$, where $\hat{x}$ denotes the arm output by the learner. We omit the dependence on $\left\{ \theta_{t} \right\}_{t = 1}^{T}$ when clear from context.

### Minimax-Optimal Complexity in Non-Stationary BAI

In prior work in the non-stationary setting, Xiong et al. showed that uniform sampling from the well-known G-optimal design

leads to a minimax-optimal error probability of

The relationship between $H_{G}$ and the G-optimal design stems from the Kiefer--Wolfowitz Theorem, which states that

$H_{G}$ is minimax-optimal since if the arm set is restricted to the standard basis vectors, $H_{G}$ matches the optimal complexity for the multi-armed bandit setting of $H_{UNIF} = \frac{K}{\Delta_{}^{2}}$. However, this notion of complexity is overly pessimistic in the linear bandit setting as it ignores potential advantages arising from arm sets with more complex structure. In contrast, we refine this notion of complexity by establishing an arm-set-dependent complexity that adapts to the geometry of any given arm set.

### Adjacency and Non-Stationary BAI

The main results of our paper are motivated by the following central lemma.

### Lemma 1 (Adjacency Lemma)

Let $\mathcal{X} \subset {\mathbb{R}}^{d}$, and $\theta \in {\mathbb{R}}^{d}$. For any $x \in \mathcal{V}$, there exists $y \in \mathcal{X}$ such that ${{({y - x})}^{\top}\theta} > 0$ if and only if there exists $z \in \mathcal{I}^{x}$ such that ${{({z - x})}^{\top}\theta} > 0$.

The formal proof of Lemma 1. ‣ 4.2 Adjacency and Non-Stationary BAI ‣ 4 BAI in Non-Stationary Linear Bandits ‣ On The Complexity of Best-Arm Identification in Non-Stationary Linear Bandits") is given in Appendix B. The idea behind the proof is quite simple: it is well known that for a polytope $P$ and a vertex $x \in P$,

Thus, the quantity ${({y - x})}^{\top}\theta$ must be a conic (non-negative) combination of the points in the set $\left\{ {{({x^{\prime} - x})}^{\top}\theta}:{x^{\prime} \in \mathcal{I}^{x}} \right\}$. Lemma 1. ‣ 4.2 Adjacency and Non-Stationary BAI ‣ 4 BAI in Non-Stationary Linear Bandits ‣ On The Complexity of Best-Arm Identification in Non-Stationary Linear Bandits") follows immediately from this fact.

One implication of Lemma 1. ‣ 4.2 Adjacency and Non-Stationary BAI ‣ 4 BAI in Non-Stationary Linear Bandits ‣ On The Complexity of Best-Arm Identification in Non-Stationary Linear Bandits") is that the first and second best arms of any instance must be adjacent. When constructing hard instances for our lower bound in Section 5, the key strategy is to construct two instances that are hard to distinguish from each other but have different best arms. Specifically, we construct one instance with best arm $x$ and second best arm $x^{\prime}$, and another instance with best arm $x^{\prime}$ and second best arm $x$. Lemma 1. ‣ 4.2 Adjacency and Non-Stationary BAI ‣ 4 BAI in Non-Stationary Linear Bandits ‣ On The Complexity of Best-Arm Identification in Non-Stationary Linear Bandits") tells us that to be able to do this, $x$ and $x^{\prime}$ need to be adjacent. Another implication of Lemma 1. ‣ 4.2 Adjacency and Non-Stationary BAI ‣ 4 BAI in Non-Stationary Linear Bandits ‣ On The Complexity of Best-Arm Identification in Non-Stationary Linear Bandits") comes from its negation, that is, if an arm is better than all its adjacent arms, then it must be the optimal arm. This implies that when identifying the best arm, we need only accurate comparisons between adjacent arms, a detail we use to design our algorithm with matching upper bound in Section 6. The main takeaway is that the distinguishability between adjacent arms solely determines the difficulty of identification. Given this, we introduce the following complexity measure

By Eq., we observe that for any arm set $\mathcal{X}$

Importantly, the above inequality can be arbitrarily loose for dense arm sets, showing that $H_{Adjacent}$ strictly refines the minimax-optimal complexity of Xiong et al.. For example, let ${\mathcal{C}{(K)}} \subset {\mathbb{R}}^{2}$ represent the arm set consisting of $K$ uniformly spaced arms on the unit circle. It is not hard to see that

since as the circle becomes more crowded, the distances between adjacent arms shrink toward zero. In the following sections, we establish $H_{Adjacent}$ as the arm-set-dependent complexity of this setting through a matching error probability lower and upper bound of

## Lower Bound of BAI in Non-Stationary Linear Bandits

We present, to the best of our knowledge, the first arm-set-dependent lower bound for BAI in the non-stationary linear bandit setting.

### Theorem 1

Fix $\mathcal{X} \subset {\mathbb{R}}^{d}$ and $\Delta_{} > 0$. For any algorithm, there exist parameter sequences $\left\{ \theta_{t} \right\}_{t = 1}^{T}$ and $\left\{ \theta_{t}^{\prime} \right\}_{t = 1}^{T}$, both with min-gap at least $\Delta_{}$, such that

where $H_{Adjacent}\left( \mathcal{X},\Delta_{} \right)$ is given by Eq..

The proof is deferred to Appendix A, of which we include a sketch in the next subsection. In Section 6, we present an algorithm that achieves the lower bound in Theorem 1, verifying the tightness of our bound, and establishing $H_{Adjacent}$ as the arm-set-dependent complexity of this setting.

### Proof Sketch of Theorem 1

In this section, we give a proof sketch of Theorem 1. We first obtain Lemma 2, which characterizes the lower bound by the *KL divergence* between two non-stationary multi-armed bandit instances and is a generalization of the stationary lower bound proposed in Lemma 15 of Kaufmann et al.. Generalizing the notation from Kaufmann et al., the statement of Lemma 2 is as follows:

### Lemma 2

Let $\nu = \left\{ \nu_{t} \right\}_{t = 1}^{T}$ and $\nu^{\prime} = \left\{ \nu_{t}^{\prime} \right\}_{t = 1}^{T}$ be non-stationary bandit models with different best arms. Then

The proof of this lemma is deferred to Appendix A and very closely follows that of Lemma 15 in Kaufmann et al.. Applying Lemma 2 requires two instances with different best arms, which motivates the following definition.

### Definition 2

Given fixed arm set $\mathcal{X}$ and $\Delta_{} > 0$, two parameter sequences ${\{\theta_{t}\}}_{t = 1}^{T}$ and ${\{\theta_{t}^{\prime}\}}_{t = 1}^{T}$ are feasible if they have different best arms, and each has min-gap at least $\Delta_{}$.

We now proceed with the proof sketch of Theorem 1.

### First step

We use Lemma 2 to obtain Lemma 3. ‣ First step. ‣ 5.1 Proof Sketch of Theorem 1 ‣ 5 Lower Bound of BAI in Non-Stationary Linear Bandits ‣ On The Complexity of Best-Arm Identification in Non-Stationary Linear Bandits") which states the following.

### Lemma 3 (Optimization-based Lower Bound)

Fix $\mathcal{X} \subset {\mathbb{R}}^{d}$ and $\Delta_{} > 0$. For any algorithm, there exist parameter sequences $\left\{ \theta_{t} \right\}_{t = 1}^{T}$ and $\left\{ \theta_{t}^{\prime} \right\}_{t = 1}^{T}$, both with min-gap at least $\Delta_{}$, such that

To prove Lemma 3. ‣ First step. ‣ 5.1 Proof Sketch of Theorem 1 ‣ 5 Lower Bound of BAI in Non-Stationary Linear Bandits ‣ On The Complexity of Best-Arm Identification in Non-Stationary Linear Bandits"), the core idea behind our construction is to split the horizon into two distinct halves, similar to that of Abbasi-Yadkori et al.. Unlike their explicit construction, however, we characterize the hard instance through an optimization problem. At a high level, the first half allows us to minimize the KL divergence of the two instances, while the second half ensures feasibility. Concretely, first, we pick a candidate pair of distinct arms ${(x,x^{\prime})} \in \mathcal{Y}$ as potential best arms for the two instances. Then, we proceed to construct the parameter sequences ${\{\theta_{t}\}}_{t = 1}^{T}$ and ${\{\theta_{t}^{\prime}\}}_{t = 1}^{T}$. For $t \leq \frac{T}{2}$ we choose $\theta_{t} = 0$^11^1The choice of $\theta_{t} = 0$ is arbitrary, any fixed choice such that ${\theta_{t}^{\prime} - \theta_{t}} = v$ works. and $\theta_{t}^{\prime} = v$, for perturbation $v$ of our choice. Then for $t > \frac{T}{2}$ we set $\theta_{t} = \theta_{t}^{\prime} = \theta$ for some $\theta$ of our choice. Further, we use the noise distribution $\epsilon_{t} \sim {\mathcal{N}{}}$ for each $t$, resulting in a KL divergence between the reward distributions of arm $x$ at time step $t$ of

For such a construction, applying Lemma 2, we obtain the lower bound

An algorithm cannot depend on the future, so for any $t \leq {T/2}$ we have that

Define $\lambda \in \bigtriangleup_{\mathcal{X}}$ such that for each $x \in \mathcal{X}$

Then, with some algebra, we can show that

yielding the objective in $f\left( \mathcal{X},\Delta_{} \right)$. The choice of $\theta$ in the second half enforces feasibility with respect to $(x,x^{\prime})$, giving rise to the constraints of $f\left( \mathcal{X},\Delta_{} \right)$. Crucially, since $v$, $\theta$, and $(x,x^{\prime})$ are independent of ${\{\theta_{t}\}}_{t = 1}^{T/2}$, we may choose them freely without affecting $\lambda$. To obtain the hardest feasible instance, we minimize over arm pairs $(x,x^{\prime})$, perturbations $v$, and parameters $\theta$ to make the KL divergence as small as possible. Finally, maximizing over $\lambda$ ensures the lower bound holds for any algorithm, concluding the proof of Lemma 3. ‣ First step. ‣ 5.1 Proof Sketch of Theorem 1 ‣ 5 Lower Bound of BAI in Non-Stationary Linear Bandits ‣ On The Complexity of Best-Arm Identification in Non-Stationary Linear Bandits").

### Second step

We bound the previous optimization problem by solving the following relaxed version of the optimization problem introduced in Lemma 3. ‣ First step. ‣ 5.1 Proof Sketch of Theorem 1 ‣ 5 Lower Bound of BAI in Non-Stationary Linear Bandits ‣ On The Complexity of Best-Arm Identification in Non-Stationary Linear Bandits"):

This is a relaxation because $\hat{f}\left( \mathcal{X},\Delta_{} \right)$ minimizes only over adjacent pairs ${(x,x^{\prime})} \in \mathcal{I}$ rather than all extreme point pairs ${(x,x^{\prime})} \in \mathcal{Y}$. Since, $\mathcal{I} \subseteq \mathcal{Y}$, and hence ${\hat{f}\left( \mathcal{X},\Delta_{} \right)} \geq {f\left( \mathcal{X},\Delta_{} \right)}$, we can substitute $f$ by $\hat{f}$ in the bound corresponding to Lemma 3. ‣ First step. ‣ 5.1 Proof Sketch of Theorem 1 ‣ 5 Lower Bound of BAI in Non-Stationary Linear Bandits ‣ On The Complexity of Best-Arm Identification in Non-Stationary Linear Bandits"). Requiring $(x,x^{\prime})$ to be adjacent is crucial: it enables a closed-form solution of the inner $(\theta,v)$ problem, described by the following lemma.

### Lemma 4

Let $\mathcal{X} \subset {\mathbb{R}}^{d}$ and $\Delta_{} > 0$. Consider $\lambda \in \bigtriangleup_{\mathcal{X}}$ with $A{(\lambda)}$ full rank and ${(x,x^{\prime})} \in \mathcal{I}$. We have:

The ideas behind the proof of Lemma 4 are as follows. Denote ${p^{\ast}:=\frac{4\Delta_{}^{2}}{{\|{x - x^{\prime}}\|}_{A{(\lambda)}^{- 1}}^{2}}}.$ We first lower bound the optimization problem by $p^{\ast}$ with a simple Cauchy-Schwarz argument. Then, to upper bound the optimization problem by $p^{\ast}$, we use the key fact that for adjacent $(x,x^{\prime})$, by Eq., there exists some $w \in {\mathbb{R}}^{d}$ such that

Thus, there is some $\varepsilon > 0$ such that ${x^{\top}w} = {x^{\prime\top}w} \geq {{y^{\top}w} + \varepsilon}$ for all $y \in {\mathcal{V} \smallsetminus {\{ x,x^{\prime}\}}}$. We choose $v,u$ such that ${v^{\top}A{(\lambda)}^{- 1}v} = p^{\ast}$ and

Then we pick $\theta = {u + {\alphaw}}$, for some $\alpha$ to be chosen. Note that since ${x^{\top}w} = {x^{\prime\top}w}$, we have

regardless of the value of $\alpha$, so this constraint is always satisfied. For any $y \in {\mathcal{V} \smallsetminus {\{ x,x^{\prime}\}}}$ we have

Hence, we can increase $\alpha$ until all other constraints are satisfied, thus $(\theta,v)$ is feasible, concluding the proof of Lemma 4. Combining Lemmas 3. ‣ First step. ‣ 5.1 Proof Sketch of Theorem 1 ‣ 5 Lower Bound of BAI in Non-Stationary Linear Bandits ‣ On The Complexity of Best-Arm Identification in Non-Stationary Linear Bandits") and 4, we obtain Theorem 1.

## Matching Upper Bound

In this section, we first introduce the Adjacent-optimal design, which is a modified version of the well-known $\mathcal{X}\mathcal{Y}$-optimal design. Based on this new design, we then develop the algorithm Adjacent-BAI, and show that it achieves an error probability guarantee that matches the lower bound presented in Section 5, verifying the tightness of our lower bound, and establishing the arm-set-dependent complexity of this setting.

### The Adjacent-Optimal Design

A central quantity in BAI problems is the $\mathcal{X}\mathcal{Y}$-optimal design, which aims to uniformly minimize the variance of predictions in directions defined by the pairwise differences between all arms. Formally, the $\mathcal{X}\mathcal{Y}$-optimal design is defined as

The relevance of the $\mathcal{X}\mathcal{Y}$-optimal design stems from the ranking nature of BAI; identifying the best arm only requires accurate estimates of the relative ordering between arms. Motivated by Lemma 1. ‣ 4.2 Adjacency and Non-Stationary BAI ‣ 4 BAI in Non-Stationary Linear Bandits ‣ On The Complexity of Best-Arm Identification in Non-Stationary Linear Bandits"), we refine this idea by introducing the Adjacent-optimal design, which uniformly minimizes the variance over differences only between adjacent arms. Formally, it is defined as

Lemma 1. ‣ 4.2 Adjacency and Non-Stationary BAI ‣ 4 BAI in Non-Stationary Linear Bandits ‣ On The Complexity of Best-Arm Identification in Non-Stationary Linear Bandits") implies that if an arm is better than all its adjacent arms, then it must be the optimal arm. Thus, when identifying the best arm, only accurate comparisons between adjacent arms are needed. The Adjacent-optimal design embodies this principle: reducing the variance of estimation of the relative ordering between adjacent arms is sufficient for identifying the best arm. Focusing on fewer, more informative directions leads to stronger estimation, which we make use of in the algorithm presented in the next section.

### Adjacent-Optimal Best-Arm Identification (Adjacent-BAI)

We now present the algorithm Adjacent-BAI. In the first step, we compute the adjacent set $\mathcal{I}$, for which we provide a polynomial-time procedure in Appendix C. We then compute the Adjacent-optimal design $\lambda^{\ast}$; however, we do not proceed by sampling directly from it. In order to obtain an optimal error rate using random sampling we would require an estimator that (i) admits sub-Gaussian, variance-only error and (ii) does not require a prespecified confidence level^22^2This requirement is unnecessary in the fixed-confidence setting, hence the use of Catoni's estimator in Camilleri et al... According to Devroye et al., this is impossible without stronger distributional assumptions. Instead, we employ the classical rounding procedure of Pukelsheim to obtain a static allocation $\left\{ x_{t} \right\}_{t = 1}^{T}$ such that the empirical design matrix $\frac{1}{T}{\sum_{t = 1}^{T}{x_{t}x_{t}^{\top}}}$ approximates the optimal design matrix ${A{(\lambda^{\ast})}} = {\sum_{x \in \mathcal{X}}{\lambda_{x}^{\ast}xx^{\top}}}$. Specifically, the rounding procedure guarantees that if $T \geq d^{2}$,^33^3We note the existence of a rounding procedure requiring only $T \geq {\Omega{(d)}}$ at the cost of significantly looser constants. An insightful discussion on both rounding procedures is provided in Appendix B of Fiez et al.. the following holds:

Then, to ensure our estimator is unbiased, we inject the necessary randomness by playing the allocation in a uniformly random order. Finally, we compute the least-squares estimator ${\hat{\theta}}_{T}$ and output its corresponding best arm. The complete procedure is summarized in Algorithm 1 ‣ 6 Matching Upper Bound ‣ On The Complexity of Best-Arm Identification in Non-Stationary Linear Bandits").

1: Input: budget T ∈ ℕ; arm set 𝒳 ⊂ ℝd
2: Find ℐ, the adjacent pairs of 𝒳
5: Sample permutation π ∼ Unif (Π (T))
7: Play xπ (t) and receive reward rt
9: ${\hat{\theta}}_{T}\leftarrow{\left( {\sum_{t = 1}^{T}{x_{t}x_{t}^{\top}}} \right)^{- 1}{\sum_{t = 1}^{T}{x_{\pi{(t)}}r_{t}}}}$
Algorithm 1 Adjacent–BAI

We characterize the error probability of Algorithm 1 ‣ 6 Matching Upper Bound ‣ On The Complexity of Best-Arm Identification in Non-Stationary Linear Bandits") in the following theorem.

### Theorem 2 (Error probability of Adjacent-BAI)

Fix time horizon $T \geq d^{2}$. Consider arm set $\mathcal{X} \subset {\mathbb{R}}^{d}$, and arbitrary unknown parameter sequence $\left\{ \theta_{t} \right\}_{t = 1}^{T}$ with min-gap $\Delta_{} > 0$. Assume ${\max_{x \in \mathcal{X}}{\| x\|}_{2}} \leq 1$ and ${\max_{t \in {\lbrack T\rbrack}}{\|\theta_{t}\|}_{2}} \leq 1$. If we run Algorithm 1 ‣ 6 Matching Upper Bound ‣ On The Complexity of Best-Arm Identification in Non-Stationary Linear Bandits") in this setting and obtain $\hat{x}$, then it holds that

where $H_{Adjacent}\left( \mathcal{X},\Delta_{} \right)$ is given by Eq..

The proof of Theorem 2. ‣ 6.2 Adjacent-Optimal Best-Arm Identification (Adjacent-BAI) ‣ 6 Matching Upper Bound ‣ On The Complexity of Best-Arm Identification in Non-Stationary Linear Bandits") is deferred to Appendix B, of which we include a sketch in the next subsection. Notably, the upper bound matches the lower bound presented in Theorem 1 up to constants, verifying the tightness of our lower bound, and establishing $H_{Adjacent}$ as the arm-set-dependent complexity of this setting.

### Proof Sketch of Theorem 2. ‣ 6.2 Adjacent-Optimal Best-Arm Identification (Adjacent-BAI) ‣ 6 Matching Upper Bound ‣ On The Complexity of Best-Arm Identification in Non-Stationary Linear Bandits")

We outline a proof sketch of Theorem 2. ‣ 6.2 Adjacent-Optimal Best-Arm Identification (Adjacent-BAI) ‣ 6 Matching Upper Bound ‣ On The Complexity of Best-Arm Identification in Non-Stationary Linear Bandits").

### First step

The statistical analysis of Theorem 2. ‣ 6.2 Adjacent-Optimal Best-Arm Identification (Adjacent-BAI) ‣ 6 Matching Upper Bound ‣ On The Complexity of Best-Arm Identification in Non-Stationary Linear Bandits") relies primarily on the following lemma.

### Lemma 5 (Sub-Gaussian error of least-squares estimator)

Let ${\hat{\theta}}_{T}$ be the estimator computed in Step 9 of Algorithm 1 ‣ 6 Matching Upper Bound ‣ On The Complexity of Best-Arm Identification in Non-Stationary Linear Bandits"). For any $z \in {\mathbb{R}}^{d}$, we have that $z^{\top}{({{\hat{\theta}}_{T} - {\overline{\theta}}_{T}})}$ is $3 \cdot {\| z\|}_{{({\sum_{t = 1}^{T}{x_{t}x_{t}^{\top}}})}^{- 1}}$-sub-Gaussian.

To obtain Lemma 5. ‣ First step. ‣ 6.3 Proof Sketch of Theorem 2 ‣ 6 Matching Upper Bound ‣ On The Complexity of Best-Arm Identification in Non-Stationary Linear Bandits"), because the arm choices $x_{\pi{(t)}}$ are dependent, the analysis requires particular care. Denote $A:={\sum_{t = 1}^{T}{x_{t}x_{t}^{\top}}}$. We begin by expanding the quantity of interest:

where we note that $\pi^{- 1} \sim {{Unif}{({\Pi{(T)}})}}$. Since each $\epsilon_{\pi^{- 1}{(t)}}$ is conditionally independent and 1-sub-Gaussian given $\pi^{- 1}$, it is straightforward to show that $\eta$ is conditionally ${\| z\|}_{A^{- 1}}$-sub-Gaussian given $\pi^{- 1}$. Analyzing $S$ requires closer attention, since each $\theta_{\pi^{- 1}{(t)}}$ is dependent, so we proceed with a martingale analysis. We construct the Doob martingale of $S$, ${\{ Z_{t}\}}_{t = 0}^{T}$, with $Z_{t} = {{\mathbb{E}}{\lbrack{S \mid \mathcal{F}_{t}}\rbrack}}$, where $\mathcal{F}_{t} = {\sigma{({\pi^{- 1}{}},\ldots,{\pi^{- 1}{(t)}})}}$. The key observation is that, intuitively, each martingale difference $|{Z_{t} - Z_{t - 1}}|$ behaves roughly on the order of $\left| {z^{\top}A^{- 1}x_{t}x_{t}^{\top}\theta_{\pi^{- 1}{(t)}}} \right|$. Given this, an Azuma inequality-style argument shows that

we obtain that $S$ is $\sqrt{8}{\| z\|}_{A^{- 1}}$-sub-Gaussian, completing the proof of Lemma 5. ‣ First step. ‣ 6.3 Proof Sketch of Theorem 2 ‣ 6 Matching Upper Bound ‣ On The Complexity of Best-Arm Identification in Non-Stationary Linear Bandits").

### Second step

Finally, we combine Lemmas 1. ‣ 4.2 Adjacency and Non-Stationary BAI ‣ 4 BAI in Non-Stationary Linear Bandits ‣ On The Complexity of Best-Arm Identification in Non-Stationary Linear Bandits") and 5. ‣ First step. ‣ 6.3 Proof Sketch of Theorem 2 ‣ 6 Matching Upper Bound ‣ On The Complexity of Best-Arm Identification in Non-Stationary Linear Bandits") to obtain the final bound in Theorem 2. ‣ 6.2 Adjacent-Optimal Best-Arm Identification (Adjacent-BAI) ‣ 6 Matching Upper Bound ‣ On The Complexity of Best-Arm Identification in Non-Stationary Linear Bandits"). We aim to bound the error probability

However, critically, by Lemma 1. ‣ 4.2 Adjacency and Non-Stationary BAI ‣ 4 BAI in Non-Stationary Linear Bandits ‣ On The Complexity of Best-Arm Identification in Non-Stationary Linear Bandits"), we have

Applying the union bound, we have

Fix some $x \in \mathcal{I}^{x_{\ast}}$. Combining Lemma 5. ‣ First step. ‣ 6.3 Proof Sketch of Theorem 2 ‣ 6 Matching Upper Bound ‣ On The Complexity of Best-Arm Identification in Non-Stationary Linear Bandits") and Hoeffding's inequality we have

Using that ${(x,x_{\ast})} \in \mathcal{I}$, and incorporating the rounding error from Eq. (36 ‣ 6 Matching Upper Bound ‣ On The Complexity of Best-Arm Identification in Non-Stationary Linear Bandits")), we have

Observing that, by definition of $\lambda^{\ast}$

completes the proof of Theorem 2. ‣ 6.2 Adjacent-Optimal Best-Arm Identification (Adjacent-BAI) ‣ 6 Matching Upper Bound ‣ On The Complexity of Best-Arm Identification in Non-Stationary Linear Bandits").

## Future Work

The most promising future direction is investigating whether adjacency can be leveraged to establish a stronger notion of complexity for the stationary fixed-budget setting. In the stationary fixed-budget setting, currently, no lower bound exists outside of a pessimistic minimax-optimal lower bound derived from a multi-armed bandit reduction. However, in the stationary fixed-confidence setting, it is well-known that for arm set $\mathcal{X}$, and parameter vector $\theta$, the instance-optimal sample complexity is of order

Evaluating the above quantity, we obtain the following proposition:

### Proposition 1

Given finite set $\mathcal{X} \subset {\mathbb{R}}^{d}$ and $\theta \in {\mathbb{R}}^{d}$, we have

The proof is deferred to Appendix D, which consists of a combination of Eq. and Jensen's inequality. Proposition 1 shows that in the stationary fixed-confidence setting, the instance-optimal sample complexity is determined solely by the arms adjacent to $x_{\ast}$. This suggests that adjacency is fundamentally tied to the difficulty of BAI even in stationary settings. This observation, together with what we have shown in the non-stationary setting, hints towards the possibility of establishing a stronger arm-set-dependent complexity in the stationary fixed-budget setting by exploiting the adjacent geometry of the arm set.
