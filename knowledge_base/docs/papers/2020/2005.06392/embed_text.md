## Introduction

The *policy gradient* is one of the most foundational concepts in Reinforcement Learning (RL), lying at the core of policy-search and actor-critic methods. This paper is concerned with the analysis of the convergence rate of *policy gradient methods*. As an approach to RL, the appeal of policy gradient methods is that they are conceptually straightforward and under some regularity conditions they guarantee monotonic improvement of the value. A secondary appeal is that policy gradient methods were shown to achieve effective empirical performance.

Despite the prevalence and importance of policy optimization in RL, the theoretical understanding of policy gradient method has, until recently, been severely limited. A key barrier to understanding is the inherent non-convexity of the value landscape with respect to standard policy parametrizations. As a result, little has been known about the global convergence behavior of policy gradient method. Recently, important new progress in understanding the convergence behavior of policy gradient has been achieved. As in this paper we will restrict ourselves to the tabular setting, we analyze the part of the literature that also deals with this setting. While the tabular setting is clearly limiting, this is the setting where so far the cleanest results have been achieved and understanding this setting is a necessary first step towards the bigger problem of understanding RL algorithms. Returning to the discussion of recent work, Bhandari & Russo showed that, without parametrization, projected gradient ascent on the simplex does not suffer from spurious local optima. In concurrent work, Agarwal et al. showed that (i) without parametrization, projected gradient ascent converges at rate $O{({1/\sqrt{t}})}$ to a global optimum; and (ii) with softmax parametrization, policy gradient converges asymptotically. Agarwal et al. also analyze other variants of policy gradient, and show that policy gradient with relative entropy regularization converges at rate $O{({1/\sqrt{t}})}$, natural policy gradient (mirror descent) converges at rate $O{({1/t})}$, and given a "compatible" function approximation (thus, going beyond the tabular case) natural policy gradient converges at rate $O{({1/\sqrt{t}})}$. Shani et al. obtains the slower rate $O{({1/\sqrt{t}})}$ for mirror descent. They also proposed a variant that adds entropy regularization and prove a rate of $O{({1/t})}$ for this modified problem.

Despite these advances, many open questions remain in understanding the behavior of policy gradient methods, even in the tabular setting and even when the true gradient is available in the updates. In this paper, we provide answers to the following three questions left open by previous work in this area: (i) What is the convergence rate of policy gradient methods with softmax parametrization? The best previous result, due to Agarwal et al., established asymptotic convergence but gave no rates. (ii) What is the convergence rate of entropy regularized softmax policy gradient? Figuring out the answer to this question was explicitly stated as an open problem by Agarwal et al.. (iii) Empirical results suggest that entropy helps optimization. Can this empirical observation be turned into a rigorous theoretical result?^11^1While Shani et al. suggest that entropy regularization speeds up mirror descent to achieve the rate of $O{({1/t})}$, in light of the corresponding result of Agarwal et al. who established the same rate for the unregularized version of mirror descent, their conclusion needs further support (e.g., lower bounds).

First, we prove that with the true gradient, policy gradient methods with a softmax parametrization converge to the optimal policy at a $O{({1/t})}$ rate, with constants depending on the problem and initialization. This result significantly strengthens the recent asymptotic convergence results of Agarwal et al.. Our analysis relies on two novel findings: (i) that softmax policy gradient satisfies what we call a non-uniform Łojasiewicz-type inequality with the constant in the inequality depending on the optimal action probability under the current policy; (ii) the minimum probability of an optimal action during optimization can be bounded in terms of its initial value. Combining these two findings, with a few other properties we describe, it can be shown that softmax policy gradient method achieves a $O{({1/t})}$ convergence rate.

Second, we analyze entropy regularized policy gradient and show that it enjoys a linear convergence rate of $O{(e^{- t})}$ toward the softmax optimal policy, which is significantly faster than that of the unregularized version. This result resolves an open question in Agarwal et al., where the authors analyzed a more aggressive relative entropy regularization rather than the more common entropy regularization. A novel insight is that entropy regularized gradient updates behave similarly to the contraction operator in value learning, with a contraction factor that depends on the current policy.

Third, we provide a theoretical understanding of entropy regularization in policy gradient methods. (i) We prove a new lower bound of $\Omega{({1/t})}$ for softmax policy gradient, implying that the upper bound of $O{({1/t})}$ that we established, apart from constant factors, is unimprovable. This result also provides a theoretical explanation of the optimization advantage of entropy regularization: even with access to the true gradient, entropy helps policy gradient *converge faster than any achievable rate of softmax policy gradient method without regularization*. (ii) We study the concept of non-uniform Łojasiewicz degree and show that, without regularization, the Łojasiewicz degree of expected reward cannot be positive, which allows $O{({1/t})}$ rates to be established. We then show that with entropy regularization, the Łojasiewicz degree of maximum entropy reward becomes $1/2$, which is sufficient to obtain linear $O{(e^{- t})}$ rates. This change of the relationship between gradient norm and sub-optimality reveals a deeper reason for the improvement in convergence rates. The theoretical study we provide corroborates existing empirical studies on the impact of entropy in policy optimization.

The remainder of the paper is organized as follows. After introducing notation and defining the setting in Section 2, we present the three main contributions in Sections 3, 4 and 5 as aforementioned. Section 6 gives our conclusions.

## Notations and Settings

For a finite set $\mathcal{X}$, we use $\Delta{(\mathcal{X})}$ to denote the set of probability distributions over $\mathcal{X}$. A finite Markov decision process (MDP) $\mathcal{M} = {(\mathcal{S},\mathcal{A},\mathcal{P},r,\gamma)}$ is determined by a finite state space $\mathcal{S}$, a finite action space $\mathcal{A}$, transition function $\mathcal{P}:{{\mathcal{S} \times \mathcal{A}}\rightarrow{\Delta{(\mathcal{S})}}}$, reward function $r:{{\mathcal{S} \times \mathcal{A}}\rightarrow{\mathbb{R}}}$, and discount factor $\gamma \in {\lbrack 0,1)}$. Given a policy $\pi:{\mathcal{S}\rightarrow{\Delta{(\mathcal{A})}}}$, the value of state $s$ under $\pi$ is defined as

We also let ${V^{\pi}{(\rho)}} ≔ {\mathbb{E}_{s \sim \rho}\left\lbrack {V^{\pi}{(s)}} \right\rbrack}$, where $\rho \in {\Delta{(\mathcal{S})}}$ is an initial state distribution. The state-action value of $\pi$ at ${(s,a)} \in {\mathcal{S} \times \mathcal{A}}$ is defined as

We let ${A^{\pi}{(s,a)}} ≔ {{Q^{\pi}{(s,a)}} - {V^{\pi}{(s)}}}$ be the so-called advantage function of $\pi$. The (discounted) state distribution of $\pi$ is defined as

and we let ${d_{\rho}^{\pi}{(s)}} ≔ {\mathbb{E}_{s_{0} \sim \rho}\left\lbrack {d_{s_{0}}^{\pi}{(s)}} \right\rbrack}$. Given $\rho$, there exists an optimal policy $\pi^{\ast}$ such that

We denote ${V^{\ast}{(\rho)}} ≔ {V^{\pi^{\ast}}{(\rho)}}$ for conciseness. Since $\mathcal{S} \times \mathcal{A}$ is finite, for convenience, without loss of generality, we assume that the one step reward lies in the $\lbrack 0,1\rbrack$ interval:

### Assumption 1 (Bounded reward)

${r{(s,a)}} \in {\lbrack 0,1\rbrack}$, $\forall{(s,a)}$.

The softmax transform of a vector exponentiates the components of the vector and normalizes it so that the result lies in the simplex. This can be used to transform vectors assigned to state-action pairs into policies:

### Softmax transform

Given the function $\theta:{{\mathcal{S} \times \mathcal{A}}\rightarrow{\mathbb{R}}}$, the softmax transform of $\theta$ is defined as $\pi_{\theta}{( \cdot |s)} ≔ {softmax}{(\theta{(s, \cdot )})}$, where for all $a \in \mathcal{A}$,

Due to its origin in logistic regression, we call the values $\theta{(s,a)}$ the *logit* values and the function $\theta$ itself a logit function. We also extend this notation to the case when there are no states: For $\theta:{{\lbrack K\rbrack}\rightarrow{\mathbb{R}}}$, we define $\pi_{\theta} ≔ {{softmax}{(\theta)}}$ using ${\pi_{\theta}{(a)}} = {{\exp{\{{\theta{(a)}}\}}}/{\sum_{a^{\prime}}{\exp{\{{\theta{(a^{\prime})}}\}}}}}$ ($a \in {\lbrack K\rbrack}$).

### H matrix

Given any distribution $\pi$ over $\lbrack K\rbrack$, let ${H{(\pi)}} ≔ {{\text{diag}{(\pi)}} - {\pi\pi^{\top}}} \in {\mathbb{R}}^{K \times K}$, where ${\text{diag}{(x)}} \in {\mathbb{R}}^{K \times K}$ is the diagonal matrix that has $x \in {\mathbb{R}}^{K}$ at its diagonal. The $H$ matrix will play a central role in our analysis because $H{(\pi_{\theta})}$ is the Jacobian of the $\theta\mapsto\pi_{\theta}:={{softmax}{(\theta)}}$ map that maps ${\mathbb{R}}^{\lbrack K\rbrack}$ to the $({K - 1})$-simplex:

Here, we are using the standard convention that derivatives give row-vectors. Finally, we recall the definition of smoothness from convex analysis:

### Smoothness

A function $f:{\Theta\rightarrow{\mathbb{R}}}$ with $\Theta \subset {\mathbb{R}}^{d}$ is $\beta$-smooth (w.r.t. $\ell_{2}$ norm, $\beta > 0$) if for all $\theta$, $\theta^{\prime} \in \Theta$,

## Policy Gradient

Policy gradient is a special policy search method. In policy search, one considers a family of policies parametrized by finite-dimensional parameter vectors, reducing the search for a good policy to searching in the space of parameters. This search is usually accomplished by making incremental changes (additive updates) to the parameters. Representative policy-based RL methods include REINFORCE, natural policy gradient, deterministic policy gradient, and trust region policy optimization. In policy gradient methods, the parameters are updated by following the gradient of the map that maps policy parameters to values. Under mild conditions, the gradient can be reexpressed in a convenient form in terms of the policy's action-value function and the gradients of the policy parametrization:

### Theorem 1 (Policy gradient theorem (Sutton et al., 2000))

Fix a map $\theta\mapsto{\pi_{\theta}{(\left. a \middle| s \right.)}}$ that for any $(s,a)$ is differentiable and fix an initial distribution $\mu \in {\Delta{(\mathcal{S})}}$. Then,

### Vanilla Softmax Policy Gradient

We focus on the policy gradient method that uses the softmax parametrization. Since we consider the tabular case, the policy is then parametrized using the logit $\theta:{{\mathcal{S} \times \mathcal{A}}\rightarrow{\mathbb{R}}}$ function and $\pi_{\theta}{( \cdot |s)} = {softmax}{(\theta{(s, \cdot )})}$. The vanilla form of policy gradient for this case is shown in Algorithm 1.

Input: Learning rate η &gt; 0.
Initialize logit θ1 (s,a) for all (s,a).
$\theta_{t + 1}\leftarrow{\theta_{t} + {\eta \cdot \frac{\partial{V^{\pi_{\theta_{t}}}{(\mu)}}}{\partial\theta_{t}}}}$.
Algorithm 1 Policy Gradient Method

With some calculation, Theorem 1). ‣ 3 Policy Gradient ‣ On the Global Convergence Rates of Softmax Policy Gradient Methods") can be used to show that the gradient takes the following special form in this case:

### Lemma 1

Softmax policy gradient w.r.t. $\theta$ is

Due to space constraints, the proof of this, as well as of all the remaining results are given in the appendix. While this lemma was known, we included a proof for the sake of completeness.

Recently, Agarwal et al. showed that softmax policy gradient asymptotically converges to $\pi^{\ast}$, i.e., ${V^{\pi_{\theta_{t}}}{(\rho)}}\rightarrow{V^{\ast}{(\rho)}}$ as $t\rightarrow\infty$ provided that ${\mu{(s)}} > 0$ holds for all states $s \in \mathcal{S}$. We strengthen this result to show that the rate of convergence (in terms of value sub-optimality) is $O{({1/t})}$. The next section is devoted to this result. For better accessibility, we start with the result for the bandit case which presents an opportunity to explaining the main ideas underlying our result in a clean fashion.

### Convergence Rates

### The Instructive Case of Bandits

As promised, in this section we consider "bandit case": In particular, assume that the MDP has a single state and the discount factor $\gamma$ is zero: $\gamma = 0$. In this case, Eq. 1 reduces to maximizing the expected reward,

With $\pi_{\theta} = {{softmax}{(\theta)}}$, even in this simple setting, the objective is non-concave in $\theta$, as shown by a simple example:

### Proposition 1

On some problems, $\theta\mapsto{\mathbb{E}_{a \sim \pi_{\theta}}{\lbrack{r{(a)}}\rbrack}}$ is a non-concave function over ${\mathbb{R}}^{K}$.

As $\gamma = 0$ and there is a single state, Lemma 1 simplifies to

Putting things together, we see that in this case the update in Algorithm 1 takes the following form:

### Update 1 (Softmax policy gradient, expected reward)

${{\theta_{t + 1}{(a)}}\leftarrow{{\theta_{t}{(a)}} + {{{\eta \cdot \pi_{\theta_{t}}}{(a)}} \cdot {({{r{(a)}} - {\pi_{\theta_{t}}^{\top}r}})}}}},$ ${\forall a} \in {\lbrack K\rbrack}$.

As is well known, if a function is smooth, then a small gradient update will be guaranteed to improve the objective value. As it turns out, for the softmax parametrization, the expected reward objective is $\beta$-smooth with $\beta \leq {5/2}$:

### Lemma 2 (Smoothness)

${\forall r} \in \lbrack 0,1\rbrack^{K}$, $\theta\mapsto{\pi_{\theta}^{\top}r}$ is $5/2$-smooth.

Smoothness alone (as is also well known) is not sufficient to guarantee that gradient updates converge to a global optimum. For non-concave objectives, the next best thing to guarantee convergence to global maxima is to establish that the gradient of the objective at any parameter dominates the sub-optimality of the parameter. Inequalities of this form are known as a Łojasiewicz inequality. The reason gradient dominance helps is because it prevents the gradient vanishing before reaching a maximum. The objective function of our problem also satisfies such an inequality, although of a weaker, "non-uniform" form. For the following result, for simplicity, we assume that the optimal action is unique. This assumption can be lifted with a little extra work, which is discussed at the end of this section.

### Lemma 3 (Non-uniform Łojasiewicz)

Assume $r$ has one unique maximizing action $a^{\ast}$. Let $\pi^{\ast} = {{\arg\max}_{\pi \in \Delta}{\pi^{\top}r}}$. Then,

The weakness of this inequality is that the right-hand side scales with $\pi_{\theta}{(a^{\ast})}$ -- hence we call it non-uniform. As a result, Lemma 3. ‣ 3.2.1 The Instructive Case of Bandits ‣ 3.2 Convergence Rates ‣ 3 Policy Gradient ‣ On the Global Convergence Rates of Softmax Policy Gradient Methods") is not very useful if $\pi_{\theta_{t}}{(a^{\ast})}$, the optimal action's probability, becomes very small during the updates.

Nevertheless, the inequality still suffices to get an following intermediate result. The proof of this result combines smoothness and the Łojasiewicz inequality we derived.

### Lemma 4 (Pseudo-rate)

Let $c_{t} = {{\min_{1 \leq s \leq t}\pi_{\theta_{s}}}{(a^{\ast})}}$. Using Update 1. ‣ 3.2.1 The Instructive Case of Bandits ‣ 3.2 Convergence Rates ‣ 3 Policy Gradient ‣ On the Global Convergence Rates of Softmax Policy Gradient Methods") with $\eta = {2/5}$, for all $t \geq 1$,

In the remainder of this section we assume that $\eta = {2/5}$.

### Remark 1

The value of $\pi_{\theta_{t}}{(a^{\ast})}$, while it is nonzero (and so is $c_{t}$) can be small (e.g., because of the choice of $\theta_{1}$). Consequently, its minimum $c_{t}$ can be quite small and the upper bound in Lemma 4. ‣ 3.2.1 The Instructive Case of Bandits ‣ 3.2 Convergence Rates ‣ 3 Policy Gradient ‣ On the Global Convergence Rates of Softmax Policy Gradient Methods") can be large, or even vacuous. The dependence of the previous result on $\pi_{\theta_{t}}{(a^{\ast})}$ comes from Lemma 3. ‣ 3.2.1 The Instructive Case of Bandits ‣ 3.2 Convergence Rates ‣ 3 Policy Gradient ‣ On the Global Convergence Rates of Softmax Policy Gradient Methods"). As it turns out, it is not possible to eliminate or improve the dependence on $\pi_{\theta}{(a^{\ast})}$ in Lemma 3. ‣ 3.2.1 The Instructive Case of Bandits ‣ 3.2 Convergence Rates ‣ 3 Policy Gradient ‣ On the Global Convergence Rates of Softmax Policy Gradient Methods"). To see this consider $r = {}^{\top}$, $\pi_{\theta} = {({2\epsilon},{{1/2} - {2\epsilon}},{1/2})}$ where $\epsilon > 0$ is small number. By algebra, ${{({\pi^{\ast} - \pi_{\theta}})}^{\top}r} = {1 - {2\epsilon}} > {1/2}$, $\frac{d\pi_{\theta}^{\top}r}{d\theta} = {({{2\epsilon} - {4\epsilon^{2}}},{{- \epsilon} + {4\epsilon^{2}}},{- \epsilon})}^{\top}$, $\left\| \frac{d\pi_{\theta}^{\top}r}{d\theta} \right\|_{2} = {\epsilon \cdot \sqrt{{6 - {24\epsilon}} + {32\epsilon^{2}}}} \leq {3\epsilon}$. Hence, for any constant $C > 0$,

which means for any Łojasiewicz-type inequality, $C$ necessarily depends on $\epsilon$ and hence on ${\pi_{\theta}{(a^{\ast})}} = {2\epsilon}$.

The necessary dependence on $\pi_{\theta_{t}}{(a^{\ast})}$ makes it clear that Lemma 4. ‣ 3.2.1 The Instructive Case of Bandits ‣ 3.2 Convergence Rates ‣ 3 Policy Gradient ‣ On the Global Convergence Rates of Softmax Policy Gradient Methods") is insufficient to conclude a $O{({1/t})}$ rate. since $c_{t}$ may vanish faster than $O{({1/t})}$ as $t$ increases. Our next result eliminates this possibility. In particular, the result follows from the asymptotic convergence result of Agarwal et al. which states that ${\pi_{\theta_{t}}{(a^{\ast})}}\rightarrow 1$ as $t\rightarrow\infty$. From this and because ${\pi_{\theta}{(a)}} > 0$ for any $\theta \in {\mathbb{R}}^{K}$ and action $a$, we conclude that $\pi_{\theta_{t}}{(a^{\ast})}$ remains bounded away from zero during the course of the updates:

### Lemma 5

We have ${\inf_{t \geq 1}{\pi_{\theta_{t}}{(a^{\ast})}}} > 0$.

Figure 1: Visualization of proof idea for Lemma 5.

With some extra work, one can also show that eventually $\theta_{t}$ enters a region where $\pi_{\theta_{t}}{(a^{\ast})}$ can only increase:

### Proposition 2

For any initialization there exist $t_{0} \geq 1$ such that for any $t \geq t_{0}$, $t\mapsto{\pi_{\theta_{t}}{(a^{\ast})}}$ is increasing. In particular, when $\pi_{\theta_{1}}$ is the uniform distribution, $t_{0} = 1$.

With Lemmas 4. ‣ 3.2.1 The Instructive Case of Bandits ‣ 3.2 Convergence Rates ‣ 3 Policy Gradient ‣ On the Global Convergence Rates of Softmax Policy Gradient Methods") and 5, we can now obtain an $O{({1/t})}$ convergence rate for softmax policy gradient method^22^2For a continuous version of Update 1. ‣ 3.2.1 The Instructive Case of Bandits ‣ 3.2 Convergence Rates ‣ 3 Policy Gradient ‣ On the Global Convergence Rates of Softmax Policy Gradient Methods"), Walton proves a $O{({1/t})}$ rate, using a Lyapunov function argument.:

### Theorem 2 (Arbitrary initialization)

Using Update 1. ‣ 3.2.1 The Instructive Case of Bandits ‣ 3.2 Convergence Rates ‣ 3 Policy Gradient ‣ On the Global Convergence Rates of Softmax Policy Gradient Methods") with $\eta = {2/5}$, for all $t \geq 1$,

where $c = {\inf_{t \geq 1}{\pi_{\theta_{t}}{(a^{\ast})}}} > 0$ is a constant that depends on $r$ and $\theta_{1}$, but it does not depend on the time $t$.

Proposition 2 suggests that one should set $\theta_{1}$ so that $\pi_{\theta_{1}}$ is uniform. Using this initialization, we can show that ${\inf_{t \geq 1}{\pi_{\theta_{t}}{(a^{\ast})}}} \geq {1/K}$, strengthening Theorem 2. ‣ 3.2.1 The Instructive Case of Bandits ‣ 3.2 Convergence Rates ‣ 3 Policy Gradient ‣ On the Global Convergence Rates of Softmax Policy Gradient Methods"):

### Theorem 3 (Uniform initialization)

Using Update 1. ‣ 3.2.1 The Instructive Case of Bandits ‣ 3.2 Convergence Rates ‣ 3 Policy Gradient ‣ On the Global Convergence Rates of Softmax Policy Gradient Methods") with $\eta = {2/5}$ and $\theta_{1}$ such that ${\pi_{\theta_{1}}{(a)}} = {1/K}$, $\forall a$, for all $t \geq 1$,

### Remark 2

In Section 5, we prove a lower bound $\Omega{({1/t})}$ for the same update rule, showing that the upper bound $O{({1/t})}$ of Theorem 2. ‣ 3.2.1 The Instructive Case of Bandits ‣ 3.2 Convergence Rates ‣ 3 Policy Gradient ‣ On the Global Convergence Rates of Softmax Policy Gradient Methods"), apart from constant factors, is unimprovable.

In general it is difficult to characterize how the constant $C$ in Theorem 2. ‣ 3.2.1 The Instructive Case of Bandits ‣ 3.2 Convergence Rates ‣ 3 Policy Gradient ‣ On the Global Convergence Rates of Softmax Policy Gradient Methods") depends on the problem and initialization. For the simple $3$-armed case, this dependence is relatively clear:

### Lemma 6

Let ${r{}} > {r{}} > {r{}}$. Then, $a^{\ast} = 1$ and ${\inf_{t \geq 1}{\pi_{\theta_{t}}{(a^{\ast})}}} = {{\min_{1 \leq t \leq t_{0}}\pi_{\theta_{t}}}{}}$, where

Note that the smaller ${r{}} - {r{}}$ and $\pi_{\theta_{1}}{}$ are, the larger $t_{0}$ is, which potentially means $c$ in Theorem 2. ‣ 3.2.1 The Instructive Case of Bandits ‣ 3.2 Convergence Rates ‣ 3 Policy Gradient ‣ On the Global Convergence Rates of Softmax Policy Gradient Methods") can be smaller.

### Visualization

Let $r = {(1.0,0.9,0.1)}^{\top}$. In Fig. 1(a), the region below the red line corresponds to $\mathcal{R} = \left\{ \pi_{\theta}:{{{{\pi_{\theta}{}}/\pi_{\theta}}{}} \geq {{({{r{}} - {r{}}})}/{({2 \cdot {({{r{}} - {r{}}})}})}}} \right\}$. Any globally convergent iteration will enter $\mathcal{R}$ within finite time (the closure of $\mathcal{R}$ contains $\pi^{\ast}$) and never leaves $\mathcal{R}$ (this is the main idea in Lemma 5). Subfigure (b) shows the behavior of the gradient updates with "good" ($\pi_{\theta_{1}} = {(0.05,0.01,0.94)}^{\top}$) and "bad" ($\pi_{\theta_{1}} = {(0.01,0.05,0.94)}^{\top}$) initial policies. While these are close to each other, the iterates behave quite differently (in both cases $\eta = {2/5}$). From the good initialization, the iterates converge quickly: after $100$ iterations the distance to the optimal policy is already quite small. At the same time, starting from a "bad" initial value, the iterates are first attracted toward a sub-optimal action. It takes more than $7000$ iterations for the algorithm to escape this sub-optimal corner! In subfigure (c), we see that $\pi_{\theta_{t}}{(a^{\ast})}$ increases for the good initialization, while in subfigure (d), for the bad initialization, we see that it initially decreases. These experiments confirm that the dependence of the error bound in Theorem 2. ‣ 3.2.1 The Instructive Case of Bandits ‣ 3.2 Convergence Rates ‣ 3 Policy Gradient ‣ On the Global Convergence Rates of Softmax Policy Gradient Methods") on the initial values cannot be removed.

### Non-unique optimal actions

When the optimal action is non-unique, the arguments need to be slightly modified. Instead of using a single $\pi_{\theta}{(a^{\ast})}$, we need to consider $\sum_{a^{\ast} \in \mathcal{A}^{\ast}}{\pi_{\theta}{(a^{\ast})}}$, i.e., the sum of probabilities of all optimal actions. Details are given in the appendix.

### General MDPs

For general MDPs, the optimization problem takes the form

Here, as before, $\pi_{\theta}{( \cdot |s)} = {softmax}{(\theta{(s, \cdot )})}$, $s \in \mathcal{S}$. Following Agarwal et al., the values here are defined with respect to an initial state distribution $\rho$ which may not be the same as the initial state distribution $\mu$ used in the gradient updates (cf. Algorithm 1), allowing for greater flexibility in our analysis. While the initial state distributions do not play any role in the bandit case, here, in the multi-state case, they have a strong influence. In particular, for the rest of this section, we will assume that the initial state distribution $\mu$ used in the gradient updates is bounded away from zero:

### Assumption 2 (Sufficient exploration)

The initial state distribution satisfies ${{\min_{s}\mu}{(s)}} > 0$.

2. ‣ 3.2.2 General MDPs ‣ 3.2 Convergence Rates ‣ 3 Policy Gradient ‣ On the Global Convergence Rates of Softmax Policy Gradient Methods") was also adapted by Agarwal et al., which ensures "sufficient exploration" in the sense that the occupancy measure $d_{\mu}^{\pi}$ of any policy $\pi$ when started from $\mu$ will be guaranteed to be positive over the whole state space. Agarwal et al. asked whether this assumption is necessary for convergence to global optimality.

### Proposition 3

There exists an MDP and $\mu$ with ${{\min_{s}\mu}{(s)}} = 0$ such that there exists $\theta^{\ast}:{{\mathcal{S} \times \mathcal{A}}\rightarrow{\lbrack 0,\infty\rbrack}}$ such that $\theta^{\ast}$ is the stationary point of $\theta\mapsto{V^{\pi_{\theta}}{(\mu)}}$ while $\pi_{\theta^{\ast}}$ is not an optimal policy. Furthermore, this stationary point is an attractor, hence, starting gradient ascent in a small enough vicinity of $\theta^{\ast}$ will make it converge to $\theta^{\ast}$.

The MDP of this proposition is $S$ bandit problems: Each state $s \in \mathcal{S}$ under each action deterministically gives itself as the next state. The reward is selected so that in each $s$ there is a unique optimal action. If $\mu$ leaves out state $s$ (i.e., ${\mu{(s)}} = 0$), clearly, the gradient of $\theta\mapsto{V^{\pi_{\theta}}{(\mu)}}$ w.r.t. $\theta$ is zero regardless of the choice of $\theta$. Hence, any $\theta$ such that ${\theta{(s,a)}} = {+ \infty}$ for $a$ optimal in state $s$ with ${\mu{(s)}} > 0$ and $\theta{(s,a)}$ finite otherwise will satisfy the properties of the proposition. It remains open whether the sufficient exploration condition is necessary for unichain MDPs.

According to 1. ‣ 2 Notations and Settings ‣ On the Global Convergence Rates of Softmax Policy Gradient Methods"), ${r{(s,a)}} \in {\lbrack 0,1\rbrack}$, ${Q{(s,a)}} \in {\lbrack 0,{1/{({1 - \gamma})}}\rbrack}$, and hence the objective function is still smooth, as was also shown by Agarwal et al.:

### Lemma 7 (Smoothness)

$V^{\pi_{\theta}}{(\rho)}$ is $8/{({1 - \gamma})}^{3}$-smooth.

As mentioned in Section 3.2.1, smoothness and (uniform) Łojasiewicz inequality are sufficient to prove a convergence rate. As noted by Agarwal et al., the main difficulty is to establish a (uniform) Łojasiewicz inequality for softmax parametrization. As it turns out, the results from the bandit case carry over to multi-state MDPs.

For stating this and the remaining results, we fix a *deterministic* optimal policy $\pi^{\ast}$ and denote by $a^{\ast}{(s)}$ the action that $\pi^{\ast}$ selects in state $s$. With this, the promised result on the non-uniform Łojasiewicz inequality is as follows:

### Lemma 8 (Non-uniform Łojasiewicz)

By 2. ‣ 3.2.2 General MDPs ‣ 3.2 Convergence Rates ‣ 3 Policy Gradient ‣ On the Global Convergence Rates of Softmax Policy Gradient Methods"), $d_{\mu}^{\pi_{\theta}}$ is also bounded away from zero on the whole state space and thus the multiplier of the sub-optimality in the above inequality is positive.

Generalizing Lemma 5, we show that ${\min_{s}\pi_{\theta_{t}}}{(\left. {a^{\ast}{(s)}} \middle| s \right.)}$ is uniformly bounded away from zero:

### Lemma 9

Let 2. ‣ 3.2.2 General MDPs ‣ 3.2 Convergence Rates ‣ 3 Policy Gradient ‣ On the Global Convergence Rates of Softmax Policy Gradient Methods") hold. Using Algorithm 1, we have, $c:={\inf_{{s \in \mathcal{S}},{t \geq 1}}{\pi_{\theta_{t}}{(\left. {a^{\ast}{(s)}} \middle| s \right.)}}} > 0$.

Using Lemmas 7. ‣ 3.2.2 General MDPs ‣ 3.2 Convergence Rates ‣ 3 Policy Gradient ‣ On the Global Convergence Rates of Softmax Policy Gradient Methods"), 8. ‣ 3.2.2 General MDPs ‣ 3.2 Convergence Rates ‣ 3 Policy Gradient ‣ On the Global Convergence Rates of Softmax Policy Gradient Methods") and 9, we prove that softmax policy gradient converges to an optimal policy at a $O{({1/t})}$ rate in MDPs, just like what we have seen in the bandit case:

### Theorem 4

Let 2. ‣ 3.2.2 General MDPs ‣ 3.2 Convergence Rates ‣ 3 Policy Gradient ‣ On the Global Convergence Rates of Softmax Policy Gradient Methods") hold and let ${\{\theta_{t}\}}_{t \geq 1}$ be generated using Algorithm 1 with $\eta = {{({1 - \gamma})}^{3}/8}$, $c$ the positive constant from Lemma 9. Then, for all $t \geq 1$,

As far as we know, this is the first convergence-rate result for softmax policy gradient for MDPs.

### Remark 3

Theorem 4 implies that the iteration complexity of Algorithm 1 to achieve $O{(\epsilon)}$ sub-optimality is $O\left( {\frac{S}{c^{2}{({1 - \gamma})}^{6}\epsilon} \cdot \left\| \frac{d_{\mu}^{\pi^{\ast}}}{\mu} \right\|_{\infty}^{2} \cdot \left\| \frac{1}{\mu} \right\|_{\infty}} \right)$, which, as a function of $\epsilon$, is better than the results of Agarwal et al. for (i) projected gradient ascent on the simplex ($O\left( {\frac{SA}{{({1 - \gamma})}^{6}\epsilon^{2}} \cdot \left\| \frac{d_{\rho}^{\pi^{\ast}}}{\mu} \right\|_{\infty}^{2}} \right)$) or for (ii) softmax policy gradient with relative-entropy regularization ($O\left( {\frac{S^{2}A^{2}}{{({1 - \gamma})}^{6}\epsilon^{2}} \cdot \left\| \frac{d_{\rho}^{\pi^{\ast}}}{\mu} \right\|_{\infty}^{2}} \right)$). The improved dependence on $\epsilon$ (or $t$) in our result follows from Lemmas 8. ‣ 3.2.2 General MDPs ‣ 3.2 Convergence Rates ‣ 3 Policy Gradient ‣ On the Global Convergence Rates of Softmax Policy Gradient Methods") and 9 and a different proof technique utilized to prove Theorem 4, while we pay a price because our bound depends on $c$, which adds an extra dependence on the MDP as well as on the initialization of the algorithm.

## Entropy Regularized Policy Gradient

Agarwal et al. considered relative-entropy regularization in policy gradient to get an $O{({1/\sqrt{t}})}$ convergence rate. As they note, relative-entropy is more "agressive" in penalizing small probabilities than the more "common" entropy regularizer (cf. Remark 5.5 in their paper) and it remains unclear whether this latter regularizer leads to an algorithm with the same rate. In this section, we answer this positively and in fact prove a much better rate. In particular, we show that entropy regularized policy gradient with the softmax parametrization enjoys a linear rate of $O{(e^{- t})}$. In retrospect, perhaps this is unsurprising as entropy regularization bears a strong similarity to introducing a strongly convex regularizer in convex optimization, where this change is known to significantly improve the rate of convergence of first-order methods.

### Maximum Entropy RL

In entropy regularized RL, or sometimes called maximum entropy RL, near-deterministic policies are penalized, which is achieved by modifying the value of a policy $\pi$ to

where ${\mathbb{H}}{(\rho,\pi)}$ is the "discounted entropy", defined as

and $\tau \geq 0$, the "temperature", determines the strength of the penalty.^33^3 To better align with naming conventions in information-theory, discounted entropy should be rather called the discounted action-entropy rate as entropy itself in the literature on Markov chain information theory would normally refer to the entropy of the stationary distribution of the chain, while entropy rate refers to what is being used here. Clearly, the value of any policy can be obtained by adding an entropy penalty to the rewards (as proposed originally by Williams & Peng ). Hence, similarly to Lemma 1, one can obtain the following expression for the gradient of the entropy regularized objective under the softmax policy parametrization:

### Lemma 10

It holds that for all $(s,a)$,

where ${\overset{\sim}{A}}^{\pi_{\theta}}{(s,a)}$ is the "soft" advantage function defined as

### Convergence Rates

As in the non-regularized case, to gain insight, we first consider MDPs with a single state and $\gamma = 0$.

### Bandit Case

In the one-state case with $\gamma = 0$, Eq. 15 reduces to maximizing the entropy-regularized reward,

Again, Eq. 20 is a non-concave function of $\theta$. In this case, regularized policy gradient reduces to

where $H{(\pi_{\theta})}$ is the same as in Eq. 6. Using the above gradient in Algorithm 1 we have the following update rule:

### Update 2 (Softmax policy gradient, maximum entropy reward)

$\theta_{t + 1}\leftarrow{\theta_{t} + {{\eta \cdot H}{(\pi_{\theta_{t}})}{({r - {\tau{\log\pi_{\theta_{t}}}}})}}}$.

Due to the presence of regularization, the optimal solution will be biased with the bias disappearing as $\tau\rightarrow 0$:

### Softmax optimal policy

$\pi_{\tau}^{\ast} ≔ {{softmax}{({r/\tau})}}$ is the optimal solution of Eq. 20.

### Remark 4

At this stage, we could use arguments similar to those of Section 3 to show the $O{({1/t})}$ convergence of $\pi_{\theta_{t}}$ to $\pi_{\tau}^{\ast}$. However, we can use an alternative idea to show that entropy-regularized policy gradient converges significantly faster. The issue of bias will be discussed later.

Our alternative idea is to show that Update 2. ‣ 4.2.1 Bandit Case ‣ 4.2 Convergence Rates ‣ 4 Entropy Regularized Policy Gradient ‣ On the Global Convergence Rates of Softmax Policy Gradient Methods") defines a contraction but with a contraction coefficient that depends on the parameter that the update is applied to:

### Lemma 11 (Non-uniform contraction)

Using Update 2. ‣ 4.2.1 Bandit Case ‣ 4.2 Convergence Rates ‣ 4 Entropy Regularized Policy Gradient ‣ On the Global Convergence Rates of Softmax Policy Gradient Methods") with ${\tau\eta} \leq 1$, ${\forall t} > 0$,

where $\zeta_{t} ≔ {{\tau\theta_{t}} - r - {\frac{{({{\tau\theta_{t}} - r})}^{\top}\mathbf{1}}{K} \cdot \mathbf{1}}}$.

This lemma immediately implies the following bound:

### Lemma 12

Using Update 2. ‣ 4.2.1 Bandit Case ‣ 4.2 Convergence Rates ‣ 4 Entropy Regularized Policy Gradient ‣ On the Global Convergence Rates of Softmax Policy Gradient Methods") with ${\tau\eta} \leq 1$, ${\forall t} > 0$,

Similarly to Lemma 5, we can show that the minimum action probability can be lower bounded by its initial value.

### Lemma 13

There exists $c = {c{(\tau,K,{\|\theta_{1}\|}_{\infty})}} > 0$, such that for all $t \geq 1$, ${{\min_{a}\pi_{\theta_{t}}}{(a)}} \geq c$. Thus, ${\sum_{s = 1}^{t - 1}{{\min_{a}\pi_{\theta_{s}}}{(a)}}} \geq {c \cdot {({t - 1})}}$.

A closed-form expression for $c$ is given in the appendix. Note that when $\tau = 0$ (no regularization), the result would no longer hold true. The key here is that ${{\min_{a}\pi_{\theta_{t}}}{(a)}}\rightarrow{{\min_{a}\pi_{\tau}^{\ast}}{(a)}} > 0$ as $t\rightarrow\infty$ and the latter inequality holds thanks to $\tau > 0$. From Lemmas 12 and 13, it follows that entropy regularized softmax policy gradient enjoys a linear convergence rate:

### Theorem 5

Using Update 2. ‣ 4.2.1 Bandit Case ‣ 4.2 Convergence Rates ‣ 4 Entropy Regularized Policy Gradient ‣ On the Global Convergence Rates of Softmax Policy Gradient Methods") with $\eta \leq {1/\tau}$, for all $t \geq 1$,

where ${\overset{\sim}{\delta}}_{t} ≔ {{{}_{}^{}\left( {r - {\tau{\log\pi_{\tau}^{\ast}}}} \right)} - {\pi_{\theta_{t}}^{\top}\left( {r - {\tau{\log\pi_{\theta_{t}}}}} \right)}}$ and $c > 0$ is from Lemma 13.

### General MDPs

For general MDPs, the problem is to maximize ${\overset{\sim}{V}}^{\pi_{\theta}}{(\rho)}$ in Eq. 15. The softmax optimal policy $\pi_{\tau}^{\ast}$ is known to satisfy the following consistency conditions:

Using a somewhat lengthy calculation, we show that the discounted entropy in Eq. 16 is smooth:

### Lemma 14 (Smoothness)

${\mathbb{H}}{(\rho,\pi_{\theta})}$ is ${({4 + {8{\log A}}})}/{({1 - \gamma})}^{3}$-smooth, where $A ≔ {|\mathcal{A}|}$ is the total number of actions.

Our next key result shows that the augmented value function ${\overset{\sim}{V}}^{\pi_{\theta}}{(\rho)}$ satisfies a "better type" of Łojasiewicz inequality:

### Lemma 15 (Non-uniform Łojasiewicz)

Suppose ${\mu{(s)}} > 0$ for all state $s \in \mathcal{S}$. Then,

The main difference to the previous versions of the non-uniform Łojasiewicz inequality is that the sub-optimality gap appears under the square root. For small sub-optimality gaps this means that the gradient must be larger -- a stronger "signal". Next, we show that action probabilities are still uniformly bounded away from zero:

### Lemma 16

Using Algorithm 1 with the entropy regularized objective, we have $c:={\inf_{t \geq 1}{{\min_{s,a}\pi_{\theta_{t}}}{(\left. a \middle| s \right.)}}} > 0$.

With Lemmas 14. ‣ 4.2.2 General MDPs ‣ 4.2 Convergence Rates ‣ 4 Entropy Regularized Policy Gradient ‣ On the Global Convergence Rates of Softmax Policy Gradient Methods"), 15. ‣ 4.2.2 General MDPs ‣ 4.2 Convergence Rates ‣ 4 Entropy Regularized Policy Gradient ‣ On the Global Convergence Rates of Softmax Policy Gradient Methods") and 16, we show a $O{(e^{- t})}$ rate for entropy regularized policy gradient in general MDPs:

### Theorem 6

Suppose ${\mu{(s)}} > 0$ for all state $s$. Using Algorithm 1 with the entropy regularized objective and softmax parametrization and $\eta = {{({1 - \gamma})}^{3}/{({8 + {\tau{({4 + {8{\log A}}})}}})}}$, there exists a constant $C > 0$ such that for all $t \geq 1$,

The value of the constant $C$ in this theorem appears in the proof of the result in the appendix in a closed form.

### Controlling the Bias

As noted in Remark 4, $\pi_{\tau}^{\ast}$ is biased, i.e., $\pi_{\tau}^{\ast} \neq \pi^{\ast}$ for fixed $\tau > 0$. We discuss two possible approaches to deal with the bias, but much remains to be done to properly address the bias. For simplicity, we consider the bandit case.

### A two-stage approach

Note that for any fixed $\tau > 0$, ${\pi_{\tau}^{\ast}{(a^{\ast})}} \geq {\pi_{\tau}^{\ast}{(a)}}$ for all $a \neq a^{\ast}$. Therefore, using policy gradient with $\pi_{\theta_{1}} = \pi_{\tau}^{\ast}$, we have ${\pi_{\theta_{t}}{(a^{\ast})}} \geq c_{t} \geq {1/K}$. This suggests a two-stage method: first, to ensure ${\pi_{\theta_{t}}{(a^{\ast})}} \geq {{\max_{a}\pi_{\theta_{t}}}{(a)}}$, use entropy-regularized policy gradient some iterations and then turn off regularization.

### Theorem 7

Denote $\Delta = {{r{(a^{\ast})}} - {{\max_{a \neq a^{\ast}}r}{(a)}}} > 0$. Using Update 2. ‣ 4.2.1 Bandit Case ‣ 4.2 Convergence Rates ‣ 4 Entropy Regularized Policy Gradient ‣ On the Global Convergence Rates of Softmax Policy Gradient Methods") for $t_{1} \in {O{({e^{1/\tau} \cdot {\log{(\frac{\tau + 1}{\Delta})}}})}}$ iterations and then Update 1. ‣ 3.2.1 The Instructive Case of Bandits ‣ 3.2 Convergence Rates ‣ 3 Policy Gradient ‣ On the Global Convergence Rates of Softmax Policy Gradient Methods") for $t_{2} \geq 1$ iterations, we have,

where $t = {t_{1} + t_{2}}$, and $C \in {\lbrack{1/K},1)}$.

This approach removes the nasty dependence on the choice of the initial parameters. While this dependence is also removed if we initialize with the uniform policy, uniform initialization is insufficient if only noisy estimates of the gradients are available. However, we leave the study of this case for future work. An obvious problem with this approach is that $\Delta$ is unknown. This can be helped by exiting the first phase when we detect "convergence" e.g. by detecting that the relative change of the policy is small.

### Decreasing the penalty

Another simple idea is to decrease the strength of regularization, e.g., set $\tau_{t} \in {O{({1/{\log t}})}}$. Consider the following update, which is a slight variation of the previous one:

### Update 3

$\theta_{t + 1}\leftarrow{\frac{\tau_{t}}{\tau_{t + 1}} \cdot {({\theta_{t} + {{\eta_{t} \cdot H}{(\pi_{\theta_{t}})}{({r - {\tau_{t}{\log\pi_{\theta_{t}}}}})}}})}}$.

The rationale for the scaling factor is that it allows one to prove a variant of Lemma 11. ‣ Softmax optimal policy. ‣ 4.2.1 Bandit Case ‣ 4.2 Convergence Rates ‣ 4 Entropy Regularized Policy Gradient ‣ On the Global Convergence Rates of Softmax Policy Gradient Methods"). While this is promising, the proof cannot be finished as before. The difficulty is that $\pi_{\theta_{t}}\rightarrow\pi^{\ast}$ (which is what we want to achieve) implies that ${{\min_{a}\pi_{\theta_{t}}}{(a)}}\rightarrow 0$, which prevents the use of our previous proof technique. We show the following partial results.

### Theorem 8

Using Update 3 with $\tau_{t} = \frac{\alpha \cdot \Delta}{\log t}$ for $t \geq 2$, where $\alpha > 0$, and $\eta_{t} = {1/\tau_{t}}$, we have, for all $t \geq 1$,

where $C ≔ \frac{2{({{\tau_{1}{\|\theta_{1}\|}_{\infty}} + 1})}\sqrt{K}}{\alpha \cdot \Delta}$.

The final rates then depend on how fast ${\min_{a}\pi_{\theta_{t}}}{(a)}$ diminishes as function of $t$. We conjecture that the rate in some cases degenerates to $O{(\frac{\log t}{t^{1/\alpha}})}$, which is strictly faster than $O{({1/t})}$ in non-regularized case when $\alpha \in {}$ and is observed in simulations in the appendix. We leave it as an open problem to study decaying entropy in general MDPs.

## Does Entropy Regularization Really Help?

The previous section indicated that entropy regularization may speed up convergence. In addition, ample empirical evidence suggest that this may be the case. In this section, we aim to provide new insights into why entropy may help policy optimization, taking an optimization perspective.

We start by establishing a lower bound that shows that the $O{({1/t})}$ rate we established earlier for softmax policy gradient without entropy regularization cannot be improved. Next, we introduce the notion of Łojasiewicz degree, which we show to increase in the presence of entropy regularization. We then connect a higher degree to faster convergence rates. Note that our proposal to view entropy regularization as an optimization aid is somewhat conflicting with the more common explanation that entropy regularization helps by encouraging exploration. While it is definitely true that entropy regularization encourages exploration, the form of exploration it encourages is not sensitive to epistemic uncertainty and as such it fails to provide a satisfactory solution to the exploration problem.

### Lower Bounds

The purpose of this section is to establish that the $O{({1/t})}$ rates established earlier for unpenalized policy gradient is tight. To get lower bounds, we need to show that progress in every iteration cannot be too large. This holds when we can reverse the inequality in the Łojasiewicz inequality. To this regard, in bandit problems we have the following result:

### Lemma 17 (Reversed Łojasiewicz)

Take any $r \in {\lbrack 0,1\rbrack}^{K}$. Denote $\Delta = {{r{(a^{\ast})}} - {{\max_{a \neq a^{\ast}}r}{(a)}}} > 0$. Then,

Using this result gives the desired lower bound:

### Theorem 9 (Lower bound)

Take any $r \in {\lbrack 0,1\rbrack}^{K}$. For large enough $t \geq 1$, using Update 1. ‣ 3.2.1 The Instructive Case of Bandits ‣ 3.2 Convergence Rates ‣ 3 Policy Gradient ‣ On the Global Convergence Rates of Softmax Policy Gradient Methods") with learning rate $\eta_{t} \in {(0,1\rbrack}$,

Note that Theorem 9. ‣ 5.1 Lower Bounds ‣ 5 Does Entropy Regularization Really Help? ‣ On the Global Convergence Rates of Softmax Policy Gradient Methods") is a special case of general MDPs. Next, we strengthen this result and show that the $\Omega{({1/t})}$ lower bound also holds for *any* MDP:

### Theorem 10 (Lower bound)

Take any MDP. For large enough $t \geq 1$, using Algorithm 1 with $\eta_{t} \in {(0,1\rbrack}$,

where $\Delta^{\ast} ≔ {\min_{{s \in \mathcal{S}},{a \neq {a^{\ast}{(s)}}}}{\{{{Q^{\ast}{(s,{a^{\ast}{(s)}})}} - {Q^{\ast}{(s,a)}}}\}}} > 0$ is the optimal value gap of the MDP.

### Remark 5

Our convergence rates in Section 3 match the lower bounds up to constant. However, the constant gap is large, e.g., $K^{2}$ in Theorem 3. ‣ 3.2.1 The Instructive Case of Bandits ‣ 3.2 Convergence Rates ‣ 3 Policy Gradient ‣ On the Global Convergence Rates of Softmax Policy Gradient Methods"), and $\Delta^{2}$ in Theorem 9. ‣ 5.1 Lower Bounds ‣ 5 Does Entropy Regularization Really Help? ‣ On the Global Convergence Rates of Softmax Policy Gradient Methods"). The gap is because the reversed Łojasiewicz inequality of Lemma 17. ‣ 5.1 Lower Bounds ‣ 5 Does Entropy Regularization Really Help? ‣ On the Global Convergence Rates of Softmax Policy Gradient Methods") uses $\Delta$, which is unavoidable when $\pi_{\theta}$ is close to $\pi^{\ast}$. We leave it as an open problem to close this gap.

With the lower bounds established, we confirm that entropy regularization helps policy optimization by speeding up convergence, though the question remains as to the mechanism by which the improved convergence rate manifests itself.

### Non-uniform Łojasiewicz Degree

To gain further insight into how entropy regularization helps, we introduce the non-uniform Łojasiewicz degree:

### Definition 1 (Non-uniform Łojasiewicz degree)

A function $f:{\mathcal{X}\rightarrow{\mathbb{R}}}$ has Łojasiewicz degree $\xi \in {\lbrack 0,1\rbrack}$ if^44^4In literature, $C$ cannot depend on $x$. Based on the examples we have seen, we relax this requirement.

${\forall x} \in \mathcal{X}$, where ${C{(x)}} > 0$ holds for all $x \in \mathcal{X}$.

The uniform degree, where $C{(x)}$ is a positive constant, has previously been connected to convergence speed in the optimization literature. Bárta studied this effect for first-, while Nesterov & Polyak; Zhou et al. studied this for second-order methods. As noted beforehand, a larger degree (smaller exponent of the sub-optimality) is expected to improve the convergence speed of algorithms that rely on gradient information. Intuitively, we expect this to continue to hold for the non-uniform Łojasiewicz degree as well. With this, we now study what Łojasiewicz degrees can one obtain with and without entropy regularization.

Our first result shows that the Łojasiewicz degree of the expected reward objective (in bandits) cannot be positive:

### Proposition 4

Let $r \in {\lbrack 0,1\rbrack}^{K}$ be arbitrary and consider $\theta\mapsto{\mathbb{E}_{a \sim \pi_{\theta}}{\lbrack{r{(a)}}\rbrack}}$. The non-uniform Łojasiewicz degree of this map with constant ${C{(\theta)}} = {\pi_{\theta}{(a^{\ast})}}$ is zero.

Note that according to Remark 1, it is necessary that $C{(\theta)}$ depends on $\pi_{\theta}{(a^{\ast})}$. The difference between Proposition 4 and the reversed Łojasiewicz inequality of Lemma 17. ‣ 5.1 Lower Bounds ‣ 5 Does Entropy Regularization Really Help? ‣ On the Global Convergence Rates of Softmax Policy Gradient Methods") is subtle. Lemma 17. ‣ 5.1 Lower Bounds ‣ 5 Does Entropy Regularization Really Help? ‣ On the Global Convergence Rates of Softmax Policy Gradient Methods") is a condition that implies impossibility to get rates faster than $O{({1/t})}$, while Proposition 4 says it is not sufficient to get rates faster than $O{({1/t})}$ using the same technique as in Lemma 4. ‣ 3.2.1 The Instructive Case of Bandits ‣ 3.2 Convergence Rates ‣ 3 Policy Gradient ‣ On the Global Convergence Rates of Softmax Policy Gradient Methods"). However, this does not preclude that other techniques could give faster rates.

Next, we show that the Łojasiewicz degree of the entropy-regularized expected reward objective is at least $1/2$:

### Proposition 5

Fix $\tau > 0$. With ${C{(\theta)}} = {{\sqrt{2\tau} \cdot {\min_{a}\pi_{\theta}}}{(a)}}$, the Łojasiewicz degree of $\theta\mapsto{\mathbb{E}_{a \sim \pi_{\theta}}\left\lbrack {{r{(a)}} - {\tau{\log\pi_{\theta}}{(a)}}} \right\rbrack}$ is at least $1/2$.

## Conclusions and Future Work

We set out to study the convergence speed of softmax policy gradient methods with and without entropy regularization in the tabular setting. Here, the error is measured in terms of the sub-optimality of the policy obtained after some number of updates. Our main findings is that without entropy regularization, the rate is $\Theta{({1/t})}$, which is faster than rates previously obtained. Our analysis also uncovered an unpleasant dependence on the initial parameter values. With entropy regularization, the rate becomes linear, where now the constant in the exponent is influenced by the initial choice of parameters. Thus, our analysis shows that entropy regularization substantially changes the rate at which gradient methods converge. Our main technical innovation is the introduction of a non-uniform variant of the Łojasiewicz inequality. Our work leaves open a number of interesting questions: While we have some lower bounds, there remains some gaps to be filled between the lower and upper bounds. Other interesting directions are extending the results for alternative (e.g., restricted) policy parametrizations or studying policy gradient when the gradient must be estimated from data. One also expects that non-uniform Łojasiewicz inequalities and the Łojasiewicz degree could also be put to good use in other areas of non-convex optimization.
