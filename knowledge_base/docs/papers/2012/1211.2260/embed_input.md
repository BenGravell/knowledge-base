No-Regret Algorithms for Unconstrained Online Convex Optimization

Topics include Online convex optimization, Unconstrained OCO, Regret bounds, Parameter-free learning, Reward doubling, Linear prediction.

Develops unconstrained online convex optimization algorithms whose regret adapts to any comparator norm without needing the feasible-set radius in advance. The reward-doubling idea is important because it preserves near-optimal guarantees on unbounded domains, including constant regret to the zero comparator, and clarifies the lower-bound tradeoffs faced by parameter-free OCO.

Some of the most compelling applications of online convex optimization, including online prediction and classification, are unconstrained: the natural feasible set is R^n. Existing algorithms fail to achieve sub-linear regret in this setting unless constraints on the comparator point x^* are known in advance. We present algorithms that, without such prior knowledge, offer near-optimal regret bounds with respect to any choice of x^*. In particular, regret with respect to x^* = 0 is constant. We then prove lower bounds showing that our guarantees are near-optimal in this setting.

## Introduction

Over the past several years, online convex optimization has emerged as a fundamental tool for solving problems in machine learning (see, e.g., for an introduction). The reduction from general online convex optimization to online linear optimization means that simple and efficient (in memory and time) algorithms can be used to tackle large-scale machine learning problems. The key theoretical techniques behind essentially all the algorithms in this field are the use of a fixed or increasing strongly convex regularizer (for gradient descent algorithms, this is equivalent to a fixed or decreasing learning rate sequence)....

This approach produces regret bounds of the form $\mathcal{O}\left( {R\sqrt{T}{\log{({{({1 + R})}T})}}} \right)$, where $R = {\|\mathring{x}\|}_{2}$ is the $L_{2}$ norm of an arbitrary comparator. Critically, our algorithms provide this guarantee simultaneously for *all* $\mathring{x} \in {\mathbb{R}}^{n}$, without any need to know $R$ in advance. A consequence of this is that we can guarantee at most *constant* regret with respect to the origin, $\mathring{x} = 0$. This technique can be applied to any online convex optimization problem where a fixed feasible set is not an essential component of the problem....

## Future Work

This work leaves open many interesting questions. It should be possible to apply our techniques to problems that do have constrained feasible sets; for example, it is natural to consider the unconstrained experts problem on the positive orthant. While we believe this extension is straightforward, handling arbitrary non-axis-aligned constraints will be more difficult. Another possibility is to develop an algorithm with bounds in terms of $H$ rather than $T$ that doesn't use a guess and double approach.

We now show that $k \geq \frac{|g_{1:T}|}{\sqrt{3\overline{H}}}$. At the end of round $t_{i + 1} - 1$, we must have had $Q_{i} < {\eta_{i}\overline{H}}$ (otherwise epoch $i + 1$ would have begun earlier). Thus, again using Lemma 2,

We give a proof of this theorem in the appendix. The duality between reward and regret can also be seen as a consequence of the fact that $\exp{(x)}$ and ${y{\log y}} - y$ are convex conjugates. The $\gamma$ term typically contains a dependence on $T$ like $1/\sqrt{T}$....
