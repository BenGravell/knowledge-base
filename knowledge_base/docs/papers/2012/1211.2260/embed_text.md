<!-- arxiv-full-text:v1 {"arxiv_id": "1211.2260", "source": "ar5iv"} -->

## Introduction

Over the past several years, online convex optimization has emerged as a fundamental tool for solving problems in machine learning (see, e.g., for an introduction). The reduction from general online convex optimization to online linear optimization means that simple and efficient (in memory and time) algorithms can be used to tackle large-scale machine learning problems. The key theoretical techniques behind essentially all the algorithms in this field are the use of a fixed or increasing strongly convex regularizer (for gradient descent algorithms, this is equivalent to a fixed or decreasing learning rate sequence). In this paper, we show that a fundamentally different type of algorithm can offer significant advantages over these approaches. Our algorithms adjust their learning rates based not just on the number of rounds, but also based on the sum of gradients seen so far. This allows us to start with small learning rates, but effectively increase the learning rate if the problem instance warrants it.

This approach produces regret bounds of the form $\mathcal{O}\left( {R\sqrt{T}{\log{({{({1 + R})}T})}}} \right)$, where $R = {\|\mathring{x}\|}_{2}$ is the $L_{2}$ norm of an arbitrary comparator. Critically, our algorithms provide this guarantee simultaneously for *all* $\mathring{x} \in {\mathbb{R}}^{n}$, without any need to know $R$ in advance. A consequence of this is that we can guarantee at most *constant* regret with respect to the origin, $\mathring{x} = 0$. This technique can be applied to any online convex optimization problem where a fixed feasible set is not an essential component of the problem. We discuss two applications of particular interest below:

### Online Prediction

Perhaps the single most important application of online convex optimization is the following prediction setting: the world presents an attribute vector $a_{t} \in {\mathbb{R}}^{n}$; the prediction algorithm produces a prediction $\sigma{({a_{t} \cdot x_{t}})}$, where $x_{t} \in {\mathbb{R}}^{n}$ represents the model parameters, and $\sigma:{{\mathbb{R}}\rightarrow Y}$ maps the linear prediction into the appropriate label space. Then, the adversary reveals the label $y_{t} \in Y$, and the prediction is penalized according to a loss function $\ell:{{Y \times Y}\rightarrow{\mathbb{R}}}$. For appropriately chosen $\sigma$ and $\ell$, this becomes a problem of online convex optimization against functions ${f_{t}{(x)}} = {\ell{({\sigma{({a_{t} \cdot x})}},y_{t})}}$. In this formulation, there are no inherent restrictions on the model coefficients $x \in {\mathbb{R}}^{n}$. The practitioner may have prior knowledge that "small" model vectors are more likely than large ones, but this is rarely best encoded as a feasible set $\mathcal{F}$, which says: "all $x_{t} \in \mathcal{F}$ are equally likely, and all other $x_{t}$ are ruled out." A more general strategy is to introduce a fixed convex regularizer: $L_{1}$ and $L_{2}^{2}$ penalties are common, but domain-specific choices are also possible. While algorithms of this form have proved very effective at solving these problems, theoretical guarantees usually require fixing a feasible set of radius $R$, or at least an intelligent guess of the norm of an optimal comparator $\mathring{x}$.

### The Unconstrained Experts Problem and Portfolio Management

In the classic problem of predicting with expert advice (e.g., ), there are $n$ experts, and on each round $t$ the player selects an expert (say $i$), and obtains reward $g_{t,i}$ from a bounded interval (say $\lbrack{- 1},1\rbrack$). Typically, one uses an algorithm that proposes a probability distribution $p_{t}$ on experts, so the expected reward is $p_{t} \cdot g_{t}$.

Our algorithms apply to an unconstrained version of this problem: there are still $n$ experts with payouts in $\lbrack{- 1},1\rbrack$, but rather than selecting an individual expert, the player can place a "bet" of $x_{t,i}$ on each expert $i$, and then receives reward ${\sum_{i}{x_{t,i}g_{t,i}}} = {x_{t} \cdot g_{t}}$. The bets are unconstrained (betting a negative value corresponds to betting against the expert). In this setting, a natural goal is the following: place bets so as to achieve as much reward as possible, subject to the constraint that total losses are bounded by a constant (which can be set equal to some starting budget which is to be invested). Our algorithms can satisfy constraints of this form because regret with respect to $\mathring{x} = 0$ (which equals total loss) is bounded by a constant.

It is useful to contrast our results in this setting to previous applications of online convex optimization to portfolio management, for example and. By applying algorithms for exp-concave loss functions, they obtain log-wealth within $\mathcal{O}{({\log{(T)}})}$ of the best constant rebalanced portfolio. However, this approach requires a "no-junk-bond" assumption: on each round, for each investment, you always retain at least an $\alpha > 0$ fraction of your initial investment. While this may be realistic (though not guaranteed!) for blue-chip stocks, it certainly is not for bets on derivatives that can lose all their value unless a particular event occurs (e.g., a stock price crosses some threshold). Our model allows us to handle such investments: if we play $x_{i} > 0$, an outcome of $g_{i} = {- 1}$ corresponds exactly to losing 100% of that investment. Our results imply that if even one investment (out of exponentially many choices) has significant returns, we will increase our wealth exponentially.^††^Our bounds are not directly comparable to the bounds cited above: a $\mathcal{O}{({\log{(T)}})}$ regret bound on log-wealth implies wealth at least $\mathcal{O}\left( {\text{OPT}/T} \right)$, whereas we guarantee wealth like $\mathcal{O}\left( {\text{OPT’} - \sqrt{T}} \right)$. But more importantly, the comparison classes are different.

### Notation and Problem Statement

For the algorithms considered in this paper, it will be more natural to consider reward-maximization rather than loss-minimization. Therefore, we consider online linear optimization where the goal is to maximize cumulative reward given adversarially selected linear reward functions ${f_{t}{(x)}} = {g_{t} \cdot x}$. On each round $t = {1\ldotsT}$, the algorithm selects a point $x_{t} \in {\mathbb{R}}^{n}$, receives reward ${f_{t}{(x_{t})}} = {g_{t} \cdot x_{t}}$, and observes $g_{t}$. For simplicity, we assume $g_{t,i} \in {\lbrack{- 1},1\rbrack}$, that is, ${\| g_{t}\|}_{\infty} \leq 1$. If the real problem is against convex loss functions $\ell_{t}{(x)}$, they can be converted to our framework by taking $g_{t} = {- {\bigtriangledown\ell_{t}{(x_{t})}}}$ (see pseudo-code for Reward-Doubling), using the standard reduction from online convex optimization to online linear optimization.

We use the compressed summation notation $g_{1:t} = {\sum_{s = 1}^{t}g_{s}}$ for both vectors and scalars. We study the reward of our algorithms, and their regret against a fixed comparator $\mathring{x}$:

### Comparison of Regret Bounds

The primary contribution of this paper is to establish matching upper and lower bounds for unconstrained online convex optimization problems, using algorithms that require no prior information about the comparator point $\mathring{x}$. Specifically, we present an algorithm that, for any $\mathring{x} \in {\mathbb{R}}^{n}$, guarantees ${{Regret}{(\mathring{x})}} \leq {\mathcal{O}\left( {{\|\mathring{x}\|}_{2}\sqrt{T}{\log{({{({1 + {\|\mathring{x}\|}_{2}})}\sqrt{T}})}}} \right)}$. To obtain this guarantee, we show that it is sufficient (and necessary) that reward is $\Omega{({\exp{({{|g_{1:T}|}/\sqrt{T}})}})}$ (see Theorem 1). This shift of emphasis from regret-minimization to reward-maximization eliminates the quantification on $\mathring{x}$, and may be useful in other contexts.

Table 1 compares the bounds for Reward-Doubling (this paper) to those of two previous algorithms: online gradient descent and projected exponentiated gradient descent. For each algorithm, we consider a fixed choice of parameter settings and then look at how regret changes as we vary the comparator point $\mathring{x}$.

Gradient descent is minimax-optimal when the comparator point is contained in a hypershere whose radius is known in advance (${\|\mathring{x}\|}_{2} \leq R$) and gradients are sparse (${\| g_{t}\|}_{2} \leq 1$, top table). Exponentiated gradient descent excels when gradients are dense (${\| g_{t}\|}_{\infty} \leq 1$, bottom table) but the comparator point is sparse (${\|\mathring{x}\|}_{1} \leq R$ for $R$ known in advance). In both these cases, the bounds for Reward-Doubling match those of the previous algorithms up to logarithmic factors, even when they are tuned optimally with knowledge of $R$.

The advantage of Reward-Doubling shows up when the guess of $R$ used to tune the competing algorithms turns out to be wrong. When $\mathring{x} = 0$, Reward-Doubling offers constant regret compared to $\Omega{(\sqrt{T})}$ for the other algorithms. When $\mathring{x}$ can be arbitrary, only Reward-Doubling offers sub-linear regret (and in fact its regret bound is optimal, as shown in Theorem 8).

In order to guarantee constant origin-regret, Reward-Doubling frequently "jumps" back to playing the origin, which may be undesirable in some applications. In Section 4 we introduce Smooth-Reward-Doubling, which achieves similar guarantees without resetting to the origin. x̊ = 0 ∥x̊∥2 ≤ R Arbitrary x̊ Gradient Descent, $\eta = \frac{R}{\sqrt{T}}$ $R\sqrt{T}$ $R\sqrt{T}$ ∥x̊∥2 T Reward-Doubling ϵ $R\sqrt{T}{\log\left(\frac{n{({1 + R})}T}{\epsilon} \right)}$ ${\|\mathring{x}\|}_{2}\sqrt{T}{\log\left(\frac{n{({1 + {\|\mathring{x}\|}_{2}})}T}{\epsilon} \right)}$ x̊ = 0 ∥x̊∥1 ≤ R Arbitrary x̊ Exponentiated G.D. $R\sqrt{T{\log n}}$ $R\sqrt{T{\log n}}$ ∥x̊∥1 T Reward-Doubling ϵ $R\sqrt{T}{\log\left(\frac{n{({1 + R})}T}{\epsilon} \right)}$ ${\|\mathring{x}\|}_{1}\sqrt{T}{\log\left(\frac{n{({1 + {\|\mathring{x}\|}_{1}})}\sqrt{T}}{\epsilon} \right)}$ Table 1: Worst-case regret bounds for various algorithms (up to constant factors). Exponentiated G.D. uses feasible set {x: ∥x∥1 ≤ R}, and Reward-Doubling uses $\epsilon_{i} = \frac{\epsilon}{n}$ in both cases.

### Related Work

Our work is related, at least in spirit, to the use of a momentum term in stochastic gradient descent for back propagation in neural networks. These results are similar in motivation in that they effectively yield a larger learning rate when many recent gradients point in the same direction.

In Follow-The-Regularized-Leader terms, the exponentiated gradient descent algorithm with unnormalized weights of Kivinen and Warmuth plays ${x_{t + 1} = {{{\arg\min}_{x \in {\mathbb{R}}_{+}^{n}}{g_{1:t} \cdot x}} + {\frac{1}{\eta}{({{x{\log x}} - x})}}}},$ which has closed-form solution $x_{t + 1} = {\exp{({- {\etag_{1:t}}})}}$. Like our algorithm, this algorithm moves away from the origin exponentially fast, but unlike our algorithm it can incur arbitrarily large regret with respect to $\mathring{x} = 0$. Theorem 9 shows that no algorithm of this form can provide bounds like the ones proved in this paper.

Hazan and Kale give regret bounds in terms of the variance of the $g_{t}$. Letting $G = {|g_{1:t}|}$ and $H = {\sum_{t = 1}^{T}g_{t}^{2}}$, they prove regret bounds of the form $\mathcal{O}{(\sqrt{V})}$ where $V = {H - {G^{2}/T}}$. This result has some similarity to our work in that ${G/\sqrt{T}} = \sqrt{H - V}$, and so if we hold $H$ constant, then when $V$ is low, the critical ratio $G/\sqrt{T}$ that appears in our bounds is large. However, they consider the case of a known feasible set, and their algorithm (gradient descent with a constant learning rate) cannot obtain bounds of the form we prove.

## Reward and Regret

In this section we present a general result that converts lower bounds on reward into upper bounds on regret, for one-dimensional online linear optimization. In the unconstrained setting, this result will be sufficient to provide guarantees for general $n$-dimensional online convex optimization.

### Theorem 1

Consider an algorithm for one-dimensional online linear optimization that, when run on a sequence of gradients $g_{1},g_{2},\ldots,g_{T}$, with $g_{t} \in {\lbrack{- 1},1\rbrack}$ for all $t$, guarantees where ${\gamma,\kappa} > 0$ and $\epsilon \geq 0$ are constants. Then, against any comparator $\mathring{x} \in {\lbrack{- R},R\rbrack}$, we have letting ${0{\log 0}} = 0$ when $R = 0$. Further, any algorithm with the regret guarantee of Eq. must guarantee the reward of Eq..

We give a proof of this theorem in the appendix. The duality between reward and regret can also be seen as a consequence of the fact that $\exp{(x)}$ and ${y{\log y}} - y$ are convex conjugates. The $\gamma$ term typically contains a dependence on $T$ like $1/\sqrt{T}$. This bound holds for all $R$, and so for some small $R$ the $\log$ term becomes negative; however, for real algorithms the $\epsilon$ term will ensure the regret bound remains positive. The minus one can of course be dropped to simplify the bound further.

## Gradient Descent with Increasing Learning Rates

In this section we show that allowing the learning rate of gradient descent to sometimes increase leads to novel theoretical guarantees.

To build intuition, consider online linear optimization in one dimension, with gradients $g_{1},g_{2},\ldots,g_{T}$, all in $\lbrack{- 1},1\rbrack$. In this setting, the reward of unconstrained gradient descent has a simple closed form:

### Lemma 2

Consider unconstrained gradient descent in one dimension, with learning rate $\eta$. On round $t$, this algorithm plays the point $x_{t} = {\etag_{1:{t - 1}}}$. Letting $G = {|g_{1:t}|}$ and $H = {\sum_{t = 1}^{T}g_{t}^{2}}$, the cumulative reward of the algorithm is exactly We give a simple direct proof in Appendix A. Perhaps surprisingly, this result implies that the reward is totally independent of the order of the linear functions selected by the adversary. Examining the expression in Lemma 2, we see that the optimal choice of learning rate $\eta$ depends fundamentally on two quantities: the absolute value of the sum of gradients ($G$), and the sum of the squared gradients ($H$). If $G^{2} > H$, we would like to use as large a learning rate as possible in order to maximize reward. In contrast, if $G^{2} < H$, the algorithm will obtain negative reward, and the best it can do is to cut its losses by setting $\eta$ as small as possible.

One of the motivations for this work is the observation that the state-of-the-art online gradient descent algorithms adjust their learning rates based *only* on the observed value of $H$ (or its upper bound $T$); for example. We would like to increase reward by also accounting for $G$. But unlike $H$, which is monotonically increasing with time, $G$ can both increase and decrease. This makes simple guess-and-doubling tricks fail when applied to $G$, and necessitates a more careful approach.

### Analysis in One Dimension

In this section we analyze algorithm Reward-Doubling-1D (Algorithm 1), which consists of a series of epochs. We suppose for the moment that an upper bound $\overline{H}$ on $H = {\sum_{t = 1}^{T}g_{t}^{2}}$ is known in advance. In the first epoch, we run gradient descent with a small initial learning rate $\eta = \eta_{1}$. Whenever the total reward accumulated in the current epoch reaches $\eta\overline{H}$, we double $\eta$ and start a new epoch (returning to the origin and forgetting all previous gradients except the most recent one).

Parameters: initial learning rate η1, upper bound $\overline{H} \geq {\sum_{t = 1}^{T}g_{t}^{2}}$. Play xt, and receive reward xt gt. if $Q_{i} < {\eta_{i}\overline{H}}$ then Parameters: maximum origin-regret ϵi for 1 ≤ i ≤ n. Let Ai be a copy of algorithm Reward-Doubling-1D-Guess (see Theorem 4), with parameter ϵi. Play xt, with xt, i selected by Ai. Receive gradient vector gt = −▽ ft (xt).

### Lemma 3

Applied to a sequence of gradients $g_{1},g_{2},\ldots,g_{T}$, all in $\lbrack{- 1},1\rbrack$, where $H = {\sum_{t = 1}^{T}g_{t}^{2}} \leq \overline{H}$, Reward-Doubling-1D obtains reward satisfying for $a = {{\log{}}/\sqrt{3}}$.

### Proof

Suppose round $T$ occurs during the $k$'th epoch. Because epoch $i$ can only come to an end if $Q_{i} \geq {\eta_{i}\overline{H}}$, where $\eta_{i} = {2^{i - 1}\eta_{1}}$, we have We now lower bound $Q_{k}$. For $i = {1,\ldots,k}$ let $t_{i}$ denote the round on which $Q_{i}$ is initialized to 0, with $t_{1} \equiv 1$, and define $t_{k + 1} \equiv T$. By construction, $Q_{i}$ is the total reward of a gradient descent algorithm that is active on rounds $t_{i}$ through $t_{i + 1}$ inclusive, and that uses learning rate $\eta_{i}$ (note that on round $t_{i}$, this algorithm gets 0 reward and we initialize $Q_{i}$ to 0 on that round). Thus, by Lemma 2, we have that for any $i$, Applying this bound to epoch $k$, we have $Q_{k} \geq {- {\frac{1}{2}\eta_{k}\overline{H}}} = {- {2^{k - 2}\eta_{1}\overline{H}}}$. Substituting into gives We now show that $k \geq \frac{|g_{1:T}|}{\sqrt{3\overline{H}}}$. At the end of round $t_{i + 1} - 1$, we must have had $Q_{i} < {\eta_{i}\overline{H}}$ (otherwise epoch $i + 1$ would have begun earlier). Thus, again using Lemma 2, so ${|g_{t_{i}:{t_{i + 1} - 1}}|} \leq \sqrt{3\overline{H}}$. Thus, Rearranging gives $k \geq \frac{|g_{1:T}|}{\sqrt{3\overline{H}}}$, and combining with Eq. proves the lemma. ∎ We can now apply Theorem 1 to the reward (given by Eq.) of Reward-Doubling-1D to show for any $\mathring{x} \in {\lbrack{- R},R\rbrack}$, where $b = a^{- 1} = {\sqrt{3}/{\log{}}} < 2.5$. When the feasible set is also fixed in advance, online gradient descent with a fixed learning obtains a regret bound of $\mathcal{O}{({R\sqrt{T}})}$. Suppose we use the estimate $\overline{H} = T$. By choosing $\eta_{1} = \frac{1}{T}$, we guarantee constant regret against the origin, $\mathring{x} = 0$ (equivalently, constant total loss). Further, for *any* feasible set of radius $R$, we still have worst-case regret of at most $\mathcal{O}{({R\sqrt{T}{\log{({{({1 + R})}T})}}})}$, which is only modestly worse than that of gradient descent with the optimal $R$ known in advance.

The need for an upper bound $\overline{H}$ can be removed using a standard guess-and-doubling approach, at the cost of a constant factor increase in regret (see appendix for proof).

### Theorem 4

Consider algorithm Reward-Doubling-1D-Guess, which behaves as follows. On each era $i$, the algorithm runs Reward-Doubling-1D with an upper bound of ${\overline{H}}_{i} = 2^{i - 1}$, and initial learning rate $\eta_{1}^{i} = {\epsilon2^{- {2i}}}$. An era ends when ${\overline{H}}_{i}$ is no longer an upper bound on the sum of squared gradients seen during that era. Letting $c = \frac{\sqrt{2}}{\sqrt{2} - 1}$, this algorithm has regret at most

### Extension to $n$ dimensions

To extend our results to general online convex optimization, it is sufficient to run a separate copy of Reward-Doubling-1D-Guess for each coordinate, as is done in Reward-Doubling (Algorithm 2). The key to the analysis of this algorithm is that overall regret is simply the sum of regret on $n$ one-dimensional subproblems which can be analyzed independently.

### Theorem 5

Given a sequence of convex loss functions $f_{1},f_{2},\ldots,f_{T}$ from ${\mathbb{R}}^{n}$ to $\mathbb{R}$, Reward-Doubling with $\epsilon_{i} = \frac{\epsilon}{n}$ has regret bounded by

### Proof

Fix a comparator $\mathring{x}$. For any coordinate $i$, define Furthermore, ${Regret}_{i}$ is simply the regret of Reward-Doubling-1D-Guess on the gradient sequence $g_{1,i},g_{2,i},\ldots,g_{T,i}$. Applying the bound of Theorem 4 to each ${Regret}_{i}$ term completes the proof of the first inequality. For the second inequality, let $\overset{\rightarrow}{H}$ be a vector whose $i^{th}$ component is $\sqrt{H_{i} + 1}$, and let $\overset{\rightarrow}{x} \in {\mathbb{R}}^{n}$ where ${\overset{\rightarrow}{x}}_{i} = {|{\mathring{x}}_{i}|}$. Using the Cauchy-Schwarz inequality, we have This, together with the fact that ${\log{({{|{\mathring{x}}_{i}|}{({{2H_{i}} + 2})}^{5/2}})}} \leq {\log{({{\|\mathring{x}\|}_{2}^{2}{({{2H} + 2})}^{5/2}})}}$, suffices to prove second inequality. ∎ In some applications, $n$ is not known in advance. In this case, we can set $\epsilon_{i} = \frac{\epsilon}{i^{2}}$ for the $i$th coordinate we encounter, and get the same bound up to constant factors.

## An Epoch-Free Algorithm

In this section we analyze Smooth-Reward-Doubling, a simple algorithm that achieves bounds comparable to those of Theorem 4, without guessing-and-doubling. We consider only the 1-d problem, as the technique of Theorem 5 can be applied to extend to $n$ dimensions. Given a parameter $\eta > 0$, we achieve for all $T$ and $R$, which is better (by constant factors) than Theorem 4 when $g_{t} \in {\{{- 1},1\}}$ (which implies $T = H$). The bound can be worse on a problems where $H < T$.

The idea of the algorithm is to maintain the invariant that our cumulative reward, as a function of $g_{1:t}$ and $t$, satisfies ${Reward} \geq {N{(g_{1:t},t)}}$, for some fixed function $N$. Because reward changes by $g_{t}x_{t}$ on round $t$, it suffices to guarantee that for any $g \in {\lbrack{- 1},1\rbrack}$, where $x_{t + 1}$ is the point the algorithm plays on round $t + 1$, and we assume ${N{}} = 0$.

This inequality is approximately satisfied (for small $g$) if we choose This suggests that if we want to maintain reward at least ${N{(g_{1:t},t)}} = {\frac{1}{t}{({{\exp{({{|g_{1:t}|}/\sqrt{t}})}} - 1})}}$, we should set $x_{t + 1} \approx {{{sign}{(g_{1:t})}}t^{- {3/2}}{\exp\left(\frac{|g_{1:t}|}{\sqrt{t}} \right)}}$. The following theorem (proved in the appendix) provides an inductive analysis of an algorithm of this form.

### Theorem 6

Fix a sequence of reward functions ${f_{t}{(x)}} = {g_{t}x}$ with $g_{t} \in {\lbrack{- 1},1\rbrack}$, and let $G_{t} = {|g_{1:t}|}$. We consider Smooth-Reward-Doubling, which plays $0$ on round $1$ and whenever $G_{t} = 0$; otherwise, it plays with $\eta > 0$ a learning-rate parameter and Then, at the end of each round $t$, this algorithm has Two main technical challenges arise in the proof: first, we prove a result like Eq. for ${N{(g_{1:t},t)}} = {{({1/t})}{\exp\left({{|g_{1:t}|}/\sqrt{t}} \right)}}$. However, this Lemma only holds for $t \geq 6$ and when the sign of $g_{1:t}$ doesn't change. We account for this by showing that a small modification to $N$ (costing only a constant over all rounds) suffices.

By running this algorithm independently for each coordinate using an appropriate choice of $\eta$, one can obtain a guarantee similar to that of Theorem 5.

## Lower Bounds

As with our previous results, it is sufficient to show a lower bound in one dimension, as it can then be replicated independently in each coordinate to obtain an $n$ dimensional bound. Note that our lower bound contains the factor $\log{({{|\mathring{x}|}\sqrt{T}})}$, which can be negative when $\mathring{x}$ is small relative to $T$, hence it is important to hold $\mathring{x}$ fixed and consider the behavior as $T\rightarrow\infty$. Here we give only a proof sketch; see Appendix A for the full proof.

### Theorem 7

Consider the problem of unconstrained online linear optimization in one dimension, and an online algorithm that guarantees origin-regret at most $\epsilon$. Then, for any fixed comparator $\mathring{x}$, and any integer $T_{0}$, there exists a gradient sequence ${\{ g_{t}\}} \in {\lbrack{- 1},1\rbrack}^{T}$ of length $T \geq T_{0}$ for which the algorithm's regret satisfies

### Proof

(Sketch) Assume without loss of generality that $\mathring{x} > 0$. Let $Q$ be the algorithm's reward when each $g_{t}$ is drawn independently uniformly from $\{{- 1},1\}$. We have ${E{\lbrack Q\rbrack}} = 0$, and because the algorithm guarantees origin-regret at most $\epsilon$, we have $Q \geq {- \epsilon}$ with probability 1. Letting $G = g_{1:T}$, it follows that for any threshold $Z = {Z{(T)}}$, We choose ${Z{(T)}} = \sqrt{kT}$, where $k = \left\lfloor {{\log{(\frac{R\sqrt{T}}{\epsilon})}}/{\log{(p^{- 1})}}} \right\rfloor$. Here $R = {|\mathring{x}|}$ and $p > 0$ is a constant chosen using binomial distribution lower bounds so that ${\Pr{\lbrack{G \geq Z}\rbrack}} \geq p^{k}$. This implies This implies there exists a sequence with $G \geq Z$ and $Q < {R\sqrt{T}}$. On this sequence, regret is at least ${{G\mathring{x}} - Q} \geq {{R\sqrt{kT}} - {R\sqrt{T}}} = {\Omega{({R\sqrt{kT}})}}$. ∎

### Theorem 8

Consider the problem of unconstrained online linear optimization in ${\mathbb{R}}^{n}$, and consider an online algorithm that guarantees origin-regret at most $\epsilon$. For any radius $R$, and any $T_{0}$, there exists a gradient sequence gradient sequence ${\{ g_{t}\}} \in {({\lbrack{- 1},1\rbrack}^{n})}^{T}$ of length $T \geq T_{0}$, and a comparator $\mathring{x}$ with ${\|\mathring{x}\|}_{1} = R$, for which the algorithm's regret satisfies

### Proof

For each coordinate $i$, Theorem 7 implies that there exists a $T \geq T_{0}$ and a sequence of gradients $g_{t,i}$ such that (The proof of Theorem 7 makes it clear that we can use the same $T$ for all $i$.) Summing this inequality across all $n$ coordinates then gives the regret bound stated in the theorem. ∎ The following theorem presents a stronger negative result for Follow-the-Regularized-Leader algorithms with a fixed regularizer: for any such algorithm that guarantees origin-regret at most $\epsilon_{T}$ after $T$ rounds, worst-case regret with respect to any point outside $\lbrack{- \epsilon_{T}},\epsilon_{T}\rbrack$ grows linearly with $T$.

### Theorem 9

Consider a Follow-The-Regularized-Leader algorithm that sets where $\psi_{T}$ is a convex, non-negative function with ${\psi_{T}{}} = 0$. Let $\epsilon_{T}$ be the maximum origin-regret incurred by the algorithm on a sequence of $T$ gradients. Then, for any $\mathring{x}$ with ${|\mathring{x}|} > \epsilon_{T}$, there exists a sequence of $T$ gradients such that the algorithm's regret with respect to $\mathring{x}$ is at least $\frac{T - 1}{2}{({{|\mathring{x}|} - \epsilon_{T}})}$.

In fact, it is clear from the proof that the above result holds for any algorithm that selects $x_{t + 1}$ purely as a function of $g_{1:t}$ (in particular, with no dependence on $t$).

## Future Work

This work leaves open many interesting questions. It should be possible to apply our techniques to problems that do have constrained feasible sets; for example, it is natural to consider the unconstrained experts problem on the positive orthant. While we believe this extension is straightforward, handling arbitrary non-axis-aligned constraints will be more difficult. Another possibility is to develop an algorithm with bounds in terms of $H$ rather than $T$ that doesn't use a guess and double approach.
