<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

No-Regret Algorithms for Unconstrained Online Convex Optimization

Topics include Online convex optimization, Unconstrained OCO, Regret bounds, Parameter-free learning, Reward doubling, Linear prediction.

<!-- chunk {"id": "summary-0002", "role": "summary", "section": "Summary", "weight": 2.0} -->

Develops unconstrained online convex optimization algorithms whose regret adapts to any comparator norm without needing the feasible-set radius in advance. The reward-doubling idea is important because it preserves near-optimal guarantees on unbounded domains, including constant regret to the zero comparator, and clarifies the lower-bound tradeoffs faced by parameter-free OCO.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Some of the most compelling applications of online convex optimization, including online prediction and classification, are unconstrained: the natural feasible set is R^n. Existing algorithms fail to achieve sub-linear regret in this setting unless constraints on the comparator point x^* are known in advance. We present algorithms that, without such prior knowledge, offer near-optimal regret bounds with respect to any choice of x^*. In particular, regret with respect to x^* = 0 is constant. We then prove lower bounds showing that our guarantees are near-optimal in this setting.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

Over the past several years, online convex optimization has emerged as a fundamental tool for solving problems in machine learning (see, e.g., for an introduction). The reduction from general online convex optimization to online linear optimization means that simple and efficient (in memory and time) algorithms can be used to tackle large-scale machine learning problems. The key theoretical techniques behind essentially all the algorithms in this field are the use of a fixed or increasing strongly convex regularizer (for gradient descent algorithms, this is equivalent to a fixed or decreasing learning rate sequence). In this paper, we show that a fundamentally different type of algorithm can offer significant advantages over these approaches. Our algorithms adjust their learning rates based not just on the number of rounds, but also based on the sum of gradients seen so far. This allows us to start with small learning rates, but effectively increase the learning rate if the problem instance warrants it.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

This approach produces regret bounds of the form $\mathcal{O}\left( {R\sqrt{T}{\log{({{({1 + R})}T})}}} \right)$, where $R = {\|\mathring{x}\|}_{2}$ is the $L_{2}$ norm of an arbitrary comparator. Critically, our algorithms provide this guarantee simultaneously for *all* $\mathring{x} \in {\mathbb{R}}^{n}$, without any need to know $R$ in advance. A consequence of this is that we can guarantee at most *constant* regret with respect to the origin, $\mathring{x} = 0$. This technique can be applied to any online convex optimization problem where a fixed feasible set is not an essential component of the problem.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Online Prediction", "weight": 1.0} -->

Perhaps the single most important application of online convex optimization is the following prediction setting: the world presents an attribute vector $a_{t} \in {\mathbb{R}}^{n}$; the prediction algorithm produces a prediction $\sigma{({a_{t} \cdot x_{t}})}$, where $x_{t} \in {\mathbb{R}}^{n}$ represents the model parameters, and $\sigma:{{\mathbb{R}}\rightarrow Y}$ maps the linear prediction into the appropriate label space. Then, the adversary reveals the label $y_{t} \in Y$, and the prediction is penalized according to a loss function $\ell:{{Y \times Y}\rightarrow{\mathbb{R}}}$.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Online Prediction", "weight": 1.0} -->

For appropriately chosen $\sigma$ and $\ell$, this becomes a problem of online convex optimization against functions ${f_{t}{(x)}} = {\ell{({\sigma{({a_{t} \cdot x})}},y_{t})}}$. In this formulation, there are no inherent restrictions on the model coefficients $x \in {\mathbb{R}}^{n}$. The practitioner may have prior knowledge that "small" model vectors are more likely than large ones, but this is rarely best encoded as a feasible set $\mathcal{F}$, which says: "all $x_{t} \in \mathcal{F}$ are equally likely, and all other $x_{t}$ are ruled out." A more general strategy is to introduce a fixed convex regularizer: $L_{1}$ and $L_{2}^{2}$ penalties are common, but domain-specific choices are also possible.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Online Prediction", "weight": 1.0} -->

While algorithms of this form have proved very effective at solving these problems, theoretical guarantees usually require fixing a feasible set of radius $R$, or at least an intelligent guess of the norm of an optimal comparator $\mathring{x}$.

<!-- chunk {"id": "body-0009", "role": "body", "section": "The Unconstrained Experts Problem and Portfolio Management", "weight": 1.0} -->

In the classic problem of predicting with expert advice (e.g., ), there are $n$ experts, and on each round $t$ the player selects an expert (say $i$), and obtains reward $g_{t,i}$ from a bounded interval (say $\lbrack{- 1},1\rbrack$). Typically, one uses an algorithm that proposes a probability distribution $p_{t}$ on experts, so the expected reward is $p_{t} \cdot g_{t}$.

<!-- chunk {"id": "body-0010", "role": "body", "section": "The Unconstrained Experts Problem and Portfolio Management", "weight": 1.0} -->

Our algorithms apply to an unconstrained version of this problem: there are still $n$ experts with payouts in $\lbrack{- 1},1\rbrack$, but rather than selecting an individual expert, the player can place a "bet" of $x_{t,i}$ on each expert $i$, and then receives reward ${\sum_{i}{x_{t,i}g_{t,i}}} = {x_{t} \cdot g_{t}}$. The bets are unconstrained (betting a negative value corresponds to betting against the expert). In this setting, a natural goal is the following: place bets so as to achieve as much reward as possible, subject to the constraint that total losses are bounded by a constant (which can be set equal to some starting budget which is to be invested). Our algorithms can satisfy constraints of this form because regret with respect to $\mathring{x} = 0$ (which equals total loss) is bounded by a constant.

<!-- chunk {"id": "body-0011", "role": "body", "section": "The Unconstrained Experts Problem and Portfolio Management", "weight": 1.0} -->

It is useful to contrast our results in this setting to previous applications of online convex optimization to portfolio management, for example and. By applying algorithms for exp-concave loss functions, they obtain log-wealth within $\mathcal{O}{({\log{(T)}})}$ of the best constant rebalanced portfolio. However, this approach requires a "no-junk-bond" assumption: on each round, for each investment, you always retain at least an $\alpha > 0$ fraction of your initial investment. While this may be realistic (though not guaranteed!) for blue-chip stocks, it certainly is not for bets on derivatives that can lose all their value unless a particular event occurs (e.g., a stock price crosses some threshold). Our model allows us to handle such investments: if we play $x_{i} > 0$, an outcome of $g_{i} = {- 1}$ corresponds exactly to losing 100% of that investment.

<!-- chunk {"id": "body-0012", "role": "body", "section": "The Unconstrained Experts Problem and Portfolio Management", "weight": 1.0} -->

Our results imply that if even one investment (out of exponentially many choices) has significant returns, we will increase our wealth exponentially.^††^Our bounds are not directly comparable to the bounds cited above: a $\mathcal{O}{({\log{(T)}})}$ regret bound on log-wealth implies wealth at least $\mathcal{O}\left( {\text{OPT}/T} \right)$, whereas we guarantee wealth like $\mathcal{O}\left( {\text{OPT’} - \sqrt{T}} \right)$. But more importantly, the comparison classes are different.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Comparison of Regret Bounds", "weight": 1.0} -->

The primary contribution of this paper is to establish matching upper and lower bounds for unconstrained online convex optimization problems, using algorithms that require no prior information about the comparator point $\mathring{x}$. Specifically, we present an algorithm that, for any $\mathring{x} \in {\mathbb{R}}^{n}$, guarantees ${{Regret}{(\mathring{x})}} \leq {\mathcal{O}\left( {{\|\mathring{x}\|}_{2}\sqrt{T}{\log{({{({1 + {\|\mathring{x}\|}_{2}})}\sqrt{T}})}}} \right)}$. To obtain this guarantee, we show that it is sufficient (and necessary) that reward is $\Omega{({\exp{({{|g_{1:T}|}/\sqrt{T}})}})}$ (see Theorem 1).

<!-- chunk {"id": "body-0014", "role": "body", "section": "Comparison of Regret Bounds", "weight": 1.0} -->

This shift of emphasis from regret-minimization to reward-maximization eliminates the quantification on $\mathring{x}$, and may be useful in other contexts.

<!-- chunk {"id": "body-0015", "role": "body", "section": "Comparison of Regret Bounds", "weight": 1.0} -->

Table 1 compares the bounds for Reward-Doubling (this paper) to those of two previous algorithms: online gradient descent and projected exponentiated gradient descent. For each algorithm, we consider a fixed choice of parameter settings and then look at how regret changes as we vary the comparator point $\mathring{x}$.

<!-- chunk {"id": "body-0016", "role": "body", "section": "Comparison of Regret Bounds", "weight": 1.0} -->

Gradient descent is minimax-optimal when the comparator point is contained in a hypershere whose radius is known in advance (${\|\mathring{x}\|}_{2} \leq R$) and gradients are sparse (${\| g_{t}\|}_{2} \leq 1$, top table). Exponentiated gradient descent excels when gradients are dense (${\| g_{t}\|}_{\infty} \leq 1$, bottom table) but the comparator point is sparse (${\|\mathring{x}\|}_{1} \leq R$ for $R$ known in advance). In both these cases, the bounds for Reward-Doubling match those of the previous algorithms up to logarithmic factors, even when they are tuned optimally with knowledge of $R$.

<!-- chunk {"id": "body-0017", "role": "body", "section": "Comparison of Regret Bounds", "weight": 1.0} -->

The advantage of Reward-Doubling shows up when the guess of $R$ used to tune the competing algorithms turns out to be wrong. When $\mathring{x} = 0$, Reward-Doubling offers constant regret compared to $\Omega{(\sqrt{T})}$ for the other algorithms. When $\mathring{x}$ can be arbitrary, only Reward-Doubling offers sub-linear regret (and in fact its regret bound is optimal, as shown in Theorem 8).

<!-- chunk {"id": "body-0018", "role": "body", "section": "Comparison of Regret Bounds", "weight": 1.0} -->

In order to guarantee constant origin-regret, Reward-Doubling frequently "jumps" back to playing the origin, which may be undesirable in some applications. In Section 4 we introduce Smooth-Reward-Doubling, which achieves similar guarantees without resetting to the origin.

<!-- chunk {"id": "body-0019", "role": "body", "section": "Comparison of Regret Bounds", "weight": 1.0} -->

${\|\mathring{x}\|}_{1}\sqrt{T}{\log\left(\frac{n{({1 + {\|\mathring{x}\|}_{1}})}\sqrt{T}}{\epsilon} \right)}$ Table 1: Worst-case regret bounds for various algorithms (up to constant factors). Exponentiated G.D. uses feasible set {x: ∥x∥1 ≤ R}, and Reward-Doubling uses $\epsilon_{i} = \frac{\epsilon}{n}$ in both cases.

<!-- chunk {"id": "body-0020", "role": "body", "section": "Reward and Regret", "weight": 1.0} -->

In this section we present a general result that converts lower bounds on reward into upper bounds on regret, for one-dimensional online linear optimization. In the unconstrained setting, this result will be sufficient to provide guarantees for general $n$-dimensional online convex optimization.

<!-- chunk {"id": "body-0021", "role": "body", "section": "Gradient Descent with Increasing Learning Rates", "weight": 1.0} -->

In this section we show that allowing the learning rate of gradient descent to sometimes increase leads to novel theoretical guarantees.

<!-- chunk {"id": "body-0022", "role": "body", "section": "Gradient Descent with Increasing Learning Rates", "weight": 1.0} -->

To build intuition, consider online linear optimization in one dimension, with gradients $g_{1},g_{2},\ldots,g_{T}$, all in $\lbrack{- 1},1\rbrack$.

<!-- chunk {"id": "body-0023", "role": "body", "section": "Analysis in One Dimension", "weight": 1.0} -->

In this section we analyze algorithm Reward-Doubling-1D (Algorithm 1), which consists of a series of epochs. We suppose for the moment that an upper bound $\overline{H}$ on $H = {\sum_{t = 1}^{T}g_{t}^{2}}$ is known in advance. In the first epoch, we run gradient descent with a small initial learning rate $\eta = \eta_{1}$. Whenever the total reward accumulated in the current epoch reaches $\eta\overline{H}$, we double $\eta$ and start a new epoch (returning to the origin and forgetting all previous gradients except the most recent one).

<!-- chunk {"id": "body-0024", "role": "body", "section": "Analysis in One Dimension", "weight": 1.0} -->

Parameters: initial learning rate η1, upper bound $\overline{H} \geq {\sum_{t = 1}^{T}g_{t}^{2}}$. Play xt, and receive reward xt gt. if $Q_{i} < {\eta_{i}\overline{H}}$ then Parameters: maximum origin-regret ϵi for 1 ≤ i ≤ n. Let Ai be a copy of algorithm Reward-Doubling-1D-Guess (see Theorem 4), with parameter ϵi. Play xt, with xt, i selected by Ai. Receive gradient vector gt = −▽ ft (xt).

<!-- chunk {"id": "body-0025", "role": "body", "section": "Extension to $n$ dimensions", "weight": 1.0} -->

To extend our results to general online convex optimization, it is sufficient to run a separate copy of Reward-Doubling-1D-Guess for each coordinate, as is done in Reward-Doubling (Algorithm 2). The key to the analysis of this algorithm is that overall regret is simply the sum of regret on $n$ one-dimensional subproblems which can be analyzed independently.

<!-- chunk {"id": "body-0026", "role": "body", "section": "An Epoch-Free Algorithm", "weight": 1.0} -->

In this section we analyze Smooth-Reward-Doubling, a simple algorithm that achieves bounds comparable to those of Theorem 4, without guessing-and-doubling. We consider only the 1-d problem, as the technique of Theorem 5 can be applied to extend to $n$ dimensions. Given a parameter $\eta > 0$, we achieve for all $T$ and $R$, which is better (by constant factors) than Theorem 4 when $g_{t} \in {\{{- 1},1\}}$ (which implies $T = H$). The bound can be worse on a problems where $H < T$.

<!-- chunk {"id": "body-0027", "role": "body", "section": "An Epoch-Free Algorithm", "weight": 1.0} -->

The idea of the algorithm is to maintain the invariant that our cumulative reward, as a function of $g_{1:t}$ and $t$, satisfies ${Reward} \geq {N{(g_{1:t},t)}}$, for some fixed function $N$. Because reward changes by $g_{t}x_{t}$ on round $t$, it suffices to guarantee that for any $g \in {\lbrack{- 1},1\rbrack}$, where $x_{t + 1}$ is the point the algorithm plays on round $t + 1$, and we assume ${N{}} = 0$.

<!-- chunk {"id": "body-0028", "role": "body", "section": "An Epoch-Free Algorithm", "weight": 1.0} -->

This inequality is approximately satisfied (for small $g$) if we choose This suggests that if we want to maintain reward at least ${N{(g_{1:t},t)}} = {\frac{1}{t}{({{\exp{({{|g_{1:t}|}/\sqrt{t}})}} - 1})}}$, we should set $x_{t + 1} \approx {{{sign}{(g_{1:t})}}t^{- {3/2}}{\exp\left(\frac{|g_{1:t}|}{\sqrt{t}} \right)}}$. The following theorem (proved in the appendix) provides an inductive analysis of an algorithm of this form.

<!-- chunk {"id": "body-0029", "role": "body", "section": "Lower Bounds", "weight": 1.0} -->

As with our previous results, it is sufficient to show a lower bound in one dimension, as it can then be replicated independently in each coordinate to obtain an $n$ dimensional bound. Note that our lower bound contains the factor $\log{({{|\mathring{x}|}\sqrt{T}})}$, which can be negative when $\mathring{x}$ is small relative to $T$, hence it is important to hold $\mathring{x}$ fixed and consider the behavior as $T\rightarrow\infty$. Here we give only a proof sketch; see Appendix A for the full proof.

<!-- chunk {"id": "body-0030", "role": "body", "section": "Future Work", "weight": 1.5} -->

This work leaves open many interesting questions. It should be possible to apply our techniques to problems that do have constrained feasible sets; for example, it is natural to consider the unconstrained experts problem on the positive orthant. While we believe this extension is straightforward, handling arbitrary non-axis-aligned constraints will be more difficult. Another possibility is to develop an algorithm with bounds in terms of $H$ rather than $T$ that doesn't use a guess and double approach.
