<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Making SGD Parameter-Free

Topics include Convex optimization, Regret bounds, Online algorithms, Optimization, SCO, Rate of convergence.

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

We develop an algorithm for parameter-free stochastic convex optimization (SCO) whose rate of convergence is only a double-logarithmic factor larger than the optimal rate for the corresponding known-parameter setting. In contrast, the best previously known rates for parameter-free SCO are based on online parameter-free regret bounds, which contain unavoidable excess logarithmic terms compared to their known-parameter counterparts. Our algorithm is conceptually simple, has high-probability guarantees, and is also partially adaptive to unknown gradient norms, smoothness, and strong convexity. At the heart of our results is a novel parameter-free certificate for SGD step size choice, and a time-uniform concentration result that assumes no a-priori bounds on SGD iterates.

<!-- chunk {"id": "body-0003", "role": "body", "section": "Introduction", "weight": 1.5} -->

Stochastic convex optimization (SCO) is a cornerstone of both the theory and practice of machine learning. Consequently, there is intense interest in developing SCO algorithms that require little to no prior knowledge of the problem parameters, and hence little to no tuning. In this work we consider the fundamental problem of non-smooth SCO (in a potentially unbounded domain) and seek methods that are adaptive to a key problem parameter: the initial distance to optimality.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

Current approaches for tackling this problem focus on the more general online learning problem of *parameter-free regret minimization*, where the goal is to to obtain regret guarantees that are valid for comparators with arbitrary norms. Research on parameter-free regret minimization has lead to practical algorithms for stochastic optimization, methods that are able to adapt to many problem parameters simultaneously and methods that can work with any norm. In the basic Euclidean setting with 1-Lipschitz losses where only the initial distance to optimality is unknown, there are essentially matching upper and lower bounds, showing that the best achievable parameter-free *average* regret scales as where $T$ is the number of steps, $\|\mathring{x}\|$ is the (Euclidean) comparator norm, and $\varepsilon > 0$ represents the (user-chosen) regret we will incur even if the comparator norm is zero. This is larger by a logarithmic factor than the optimal average-regret when the comparator norm is known in advance.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

Parameter-free regret bounds immediately translate into parameter-free SCO algorithms using online-to-batch conversion. The expected optimality gap bound of the resulting algorithm is identical to when we replace $\mathring{x}$ by $x_{\star} - x_{0}$, i.e., the difference between the optimum and the initial point. This bound is a logarithmic factor worse than what stochastic gradient descent (SGD) can achieve when we know the distance to optimality and use it to compute step sizes. While this logarithmic factor is unavoidable for regret minimization, it is unclear if it is necessary for SCO.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

In this paper we show it is possible to obtain stronger parameter-free rates for SCO by moving beyond the regret minimization abstraction. In particular, for any $\varepsilon > 0$ and $\delta \in {}$, we a obtain probability $1 - \delta$ optimality gap bounds of which is better than any bound achievable by online-to-batch conversion. While replacing the logarithmic factor by a double-logarithmic factor may appear a small improvement, we consider it important due to the fundamental nature of the problem as well as the theoretical separation it establishes between parameter-free SCO and OCO. Such separations are rare in the literature; we are only aware of one prior example.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

Our method also provides high probability guarantees on the suboptimality gap. This resolves an open problem in parameter-free optimization; see and \[29, §7\]. We are able to form high probability bounds because, unlike other parameter-free SCO algorithms, we prove a strong localization guarantee: our output $\overline{x}$ satisfies ${\|{\overline{x} - x_{\star}}\|} = {O{({\|{x_{0} - x_{\star}}\|})}}$, and key intermediate points satisfy a similar bound as well. We suspect that such localization is difficult to establish with online-to-batch conversion, since online parameter-free algorithms may need to let their iterates fluctuate wildly in order to handle difficult adversaries.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Introduction", "weight": 1.5} -->

In addition to independence of $\|{x_{0} - x_{\star}}\|$, our algorithm exhibits three additional forms of adaptivity. First, our algorithm has adaptivity to gradient norms on par with the best existing parameter-free result: the leading term of our bounds scales with a sum of squared observed gradient norms, and an a-priori gradient norm bound only affects low-order terms. Second, as a consequence, in the smooth and noiseless case our algorithm exhibits a $\frac{\log{\log T}}{T}$ rate of convergence. Finally, via a simple restart scheme we obtain the optimal rate for strongly-convex stochastic problems (up to double-logarithmic factors), without knowledge of the strong-convexity parameter.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Introduction", "weight": 1.5} -->

On a technical level, our development differs significantly from prior parameter-free optimization methods. While online methods rely on advanced tools such as coin betting, and online Newton steps, our approach is essentially a careful scheme for correctly setting the step size of SGD. Underlying our algorithm is a parameter-free certificate for SGD, which implies both localization and optimality gap bounds. The certificate takes the form of an implicit equation over the SGD step size, which we solve via bisection on the logarithm of the step size. To obtain high-probability bounds, we develop a time-uniform empirical-Berstein-type concentration bound independent of any a-priori assumptions on the iterate norms. Given the ubiquity of SGD in practice and in the classroom, our insights on how choose its step size may be of independent interest.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Paper organization", "weight": 1.0} -->

In the following subsections we review additional related work, as well as the problem setup and notation. Section 2 develops our parameter-free step size certificate. Section 3 presents our algorithm and its analysis in the noiseless regime. Section 4 lifts the analysis to the stochastic setting, proving our main result on parameter-free SCO. Finally, Section 5 shows how our method adapts to smoothness and (via restarts) to strong convexity.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Parameter-free methods from deterministic optimization", "weight": 1.0} -->

The literature on noiseless optimization also offers a rich variety of parameter-free algorithms. In the smooth setting, the Armijo rule is a standard technique for choosing step sizes for gradient descent. Using variants of this idea combined with acceleration, achieves essentially optimal and parameter-free rates of convergence. The Polyak step size rule simultaneously achieves optimal rates for smooth, non-smooth and strongly-convex optimization, but requires knowledge of the optimal function value. This requirement can be relaxed, making the Polyak method parameter-free, but at the cost of a multiplicative logarithmic factor to its bound. Consequently, non-smooth parameter-free deterministic optimization appears to be as hard as SCO. Multiple works generalize line-search and the Polyak method to the stochastic setting, but do not obtain parameter-free rates in the sense we consider here.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Limitations of online-to-batch conversion", "weight": 1.5} -->

To the best of our knowledge, the only previous example of an SCO rate that is provably unachievable by online to batch conversion of a (uniform) regret bound occurs for strongly-convex optimization. Specifically, any online strongly-convex optimization algorithm must have logarithmic regret (implying suboptimality ${({\log T})}/T$ via online to batch conversion), while Hazan and Kale and others have achieved the optimal $1/T$ rate for stochastic strongly-convex optimization. The variant of our algorithm in Section 5.2 is based on the Epoch-SGD algorithm of, and simultantiously breaks both regret minization barriers, achieving optimality gap ${({\log{\log T}})}/T$ for parameter-free strongly-convex stochastic optimization with high probability.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Grid search", "weight": 1.0} -->

In practice, the standard technique for selecting the step size of SGD (and hyperparameters more broadly) is grid search. This typically consists of testing all step sizes on a geometrically spaced grid and choosing the one with the best performance on a held out set. Compared to our method, such grid search is computationally wasteful, as it tests exponentially more steps sizes than we do. Moreover, in the context of parameter-free SCO, proving guarantees for grid search is surprisingly difficult, since it is unclear how to bound the objective value estimation error for points that may be arbitrarily far apart.

<!-- chunk {"id": "body-0014", "role": "body", "section": "Problem setup and notation", "weight": 1.0} -->

Let us briefly review the standard SCO setup, building up our notation along the way. Our goal is to minimize a convex objective function $f:{\mathcal{X}\rightarrow{\mathbb{R}}}$ defined on a closed an convex set $\mathcal{X} \subseteq {\mathbb{R}}^{d}$ (our results hold for $\mathcal{X} = {\mathbb{R}}^{d}$ as well). We let $x_{\star}$ denote a fixed minimizer of $f$, i.e., such that ${f{(x_{\star})}} \leq {f{(x)}}$ for all $x \in \mathcal{X}$, implicitly assuming such point exists (see Section D.1 for further discussion of this assumption).

<!-- chunk {"id": "body-0015", "role": "body", "section": "Problem setup and notation", "weight": 1.0} -->

We assume that our only access to $f$ is via a stochastic gradient oracle $\mathcal{O}$ that, upon receiving query point $x$, returns a vector ${\mathcal{O}{(x)}} \in {\mathbb{R}}^{d}$ that is a subgradient of $f$ in expectation, i.e., $\left. {\mathcal{O}{(x)}} \middle| x \right. \in {\partial{f{(x)}}}$. With slight abuse of notation, we write ${{\nabla f}{(x)}} ≔ \left. {\mathcal{O}{(x)}} \middle| x \right.$, corresponding to the gradient of $f$ when it is differentiable and a particular subgradient otherwise.

<!-- chunk {"id": "body-0016", "role": "body", "section": "Problem setup and notation", "weight": 1.0} -->

We interchangeably use *exact gradients*, *noiseless*, and *deterministic* to refer to the regime where ${\mathcal{O}{(x)}} = {{\nabla f}{(x)}}$ with probability 1.

<!-- chunk {"id": "body-0017", "role": "body", "section": "Problem setup and notation", "weight": 1.0} -->

Our development revolves around the classical fixed step size stochastic gradient descent (SGD) algorithm. Given step size $\eta$ and initialization $x_{0}$, SGD iterates and $\Pi_{\mathcal{X}}$ is the Euclidean projection onto $\mathcal{X}$; we intentionally feature the $\eta$ dependence of $x_{i}{(\eta)}$ and $g_{i}{(\eta)}$ prominently. We define the following quantities associated with the SGD iterates. First, we write the distance to $x_{\star}$ and its running maximum as Replacing $x_{\star}$ with $x_{0}$ in the above definitions, we write Finally, we denote the running sum of squared gradient norms and gradient oracle error by

<!-- chunk {"id": "body-0018", "role": "body", "section": "Additional notational conventions", "weight": 1.0} -->

Throughout, $\parallel \cdot \parallel$ denotes the Euclidean norm. We use $\log$ to denote the base 2 logarithm, and write ${\log_{+}{(x)}} ≔ {\max{\{ 2,{\log{(x)}}\}}}$ to simplify $O{( \cdot )}$ notation. For any particular value of $\eta$, the quantities $x_{i}{(\eta)}$, $g_{i}{(\eta)}$, etc. always refer to a *single* realization of the random process they represent.

<!-- chunk {"id": "body-0019", "role": "body", "section": "A parameter-free step-size selection criterion for SGD", "weight": 1.0} -->

In this section we present the key component of our development: a computable certificate for the efficiency of a candidate SGD step size. For ease of exposition, in this section we restrict some of our arguments to the exact gradient setting, but emphasize that they ultimately translate to high-probability bounds in the stochastic setting.

<!-- chunk {"id": "body-0020", "role": "body", "section": "A parameter-free step-size selection criterion for SGD", "weight": 1.0} -->

Our key proposal is to approximate the distance to the optimum $d_{0}$ with a computable proxy: the maximum distance traveled by the algorithm, ${{\overline{r}}_{T}{(\eta)}} ≔ {\max_{i \leq T}{\|{x_{0} - {x_{i}{(\eta)}}}\|}}$. We consider step sizes that (approximately) satisfy for nonnegative damping parameters $\alpha$ and $\beta$; in the exact gradient setting we can set $\alpha$ to any number $> 1$ and $\beta = 0$, while the stochastic setting requires scaling $\alpha$ and $\beta$ roughly as ${\mathsf{p}\mathsf{o}\mathsf{l}\mathsf{y}}{({\log{\log T}})}$.

<!-- chunk {"id": "body-0021", "role": "body", "section": "A parameter-free step-size selection criterion for SGD", "weight": 1.0} -->

Intuitively, ${\overline{r}}_{T}$ approximates $d_{0}$ since the SGD iterates should converge to $x_{\star}$ and therefore $\|{x_{0} - {x_{T}{(\eta)}}}\|$ should be similar to $\|{x_{0} - x_{\star}}\|$. However, in non-smooth optimization, convergence to $x_{\star}$ can be arbitrarily slow. We nevertheless prove that, when $\eta \leq {\phi{(\eta)}}$, we have ${{\overline{r}}_{T}{(\eta)}} = {O{(d_{0})}}$ (Lemma 2 below). With this result and a refined SGD error bound (Lemma 1 below), we show that (with exact gradients) any $\eta$ satisfying criterion recovers the optimal error bound.

<!-- chunk {"id": "body-0022", "role": "body", "section": "Propostion 1", "weight": 1.0} -->

In the noiseless setting, any step size $\eta > 0$ satisfying with $\alpha > 1$ and $\beta = 0$ produces $\overline{x} ≔ {\frac{1}{T}{\sum_{i < T}{x_{i}{(\eta)}}}}$ such that ${\|{x_{\star} - \overline{x}}\|} \leq {\frac{2\alpha}{\alpha - 1}{\|{x_{\star} - x_{0}}\|}}$ and Before proving Proposition 1, let us briefly discuss its algorithmic implications. Since the function $\phi{(\cdot)}$ is computable (at the cost of $T$ gradient queries) without a-priori assumptions on $d_{0}$, we have reduced parameter-free optimization to solving the one-dimensional implicit equation. However, the function $\phi$ might be discontinuous and an exact solution to the implicit equation might not even exist.

<!-- chunk {"id": "body-0023", "role": "body", "section": "Propostion 1", "weight": 1.0} -->

Nevertheless, in the next section we show that finding an interval $\lbrack\eta,{2\eta}\rbrack$ in which $h\mapsto{{\phi{(h)}} - h}$ changes sign, produces nearly the same error certificates at an interval edge. Since such interval is readily found via bisection, this forms the basis of a working parameter-free step size tuner. We leave the details to Section 3 and for the remainder of this section prove Proposition 1.

<!-- chunk {"id": "body-0024", "role": "body", "section": "Algorithm description, and analysis for exact gradients", "weight": 1.0} -->

In this section we turn the step-size selection criterion presented in the previous section into a complete algorithm (Algorithm 1)---valid for stochastic as well as exact gradients---and analyze it in the simpler setting of exact gradients, deferring the stochastic case to the following section. Our algorithm consists of a core log-scale bisection subroutine (RootFindingBisection) coupled with an outer loop that acts as an aggressive doubling scheme on the upper limit of the bisection. We describe and analyze the two components Sections 3.1 and 3.2, respectively. Then, in Section 3.3, we put these results together and obtain parameter-free rates in the exact gradient setting.

<!-- chunk {"id": "body-0025", "role": "body", "section": "Algorithm description, and analysis for exact gradients", "weight": 1.0} -->

Input: Initial step size ηε > 0, total gradient budget B ∈ ℕ, constants {α(k), β(k)} ⊳ In the deterministic case, α(k) = 3 (or any constant > 1) and β(k) = 0; in the stochastic case see eq.

<!-- chunk {"id": "body-0026", "role": "body", "section": "Algorithm description, and analysis for exact gradients", "weight": 1.0} -->

and) 5 if ηhi ≤ ϕ(ηhi) then return ∞ ⊳ ηhi is too low and should be increased if ηlo > ϕ(ηlo) then return ηlo ⊳ ηlo is sufficient (assuming it is very small) while ηhi > 2ηlo do ⊳ Invariant: ηlo < ηhi, ηlo ≤ ϕ(ηlo), ηhi > ϕ(ηhi) 6 $\eta_{mid}\leftarrow\sqrt{\eta_{lo}\eta_{hi}}$ if ηmid ≤ ϕ(ηmid) then ηlo ← ηmid else ηhi ← ηmid 7 if ${{\overline{r}}_{T}{(\eta_{hi})}} \leq {{\overline{r}}_{T}{(\eta_{lo})}\frac{\phi{(\eta_{hi})}}{\eta_{hi}}}$ then return ηhi else return ηlo Algorithm 1 Parameter-free SGD step size tuning

<!-- chunk {"id": "body-0027", "role": "body", "section": "Bisection subroutine", "weight": 1.0} -->

Let us describe the RootFindingBisection subroutine of Algorithm 1. Its input is an initial interval $\lbrack\eta_{lo},\eta_{hi}\rbrack$, SGD iteration number $T$ and damping parameters $(\alpha,\beta)$ for defining the bisection target ${\phi{(\eta)}} = {{{\overline{r}}_{T}{(\eta)}}/\sqrt{{\alpha G_{T}{(\eta)}} + \beta}}$.

<!-- chunk {"id": "body-0028", "role": "body", "section": "Bisection subroutine", "weight": 1.0} -->

{\frac{1}{2}{({\eta_{lo} + \eta_{hi}})}}$ would result in a logarithmic rather than double-logarithmic number of bisection steps.

<!-- chunk {"id": "body-0029", "role": "body", "section": "Bisection subroutine", "weight": 1.0} -->

The iterations stop when ${\eta_{hi}/\eta_{lo}} \leq 2$. Since each iteration halves $\log\frac{\eta_{hi}}{\eta_{lo}}$, the overall iteration number is double-logarithmic in the ratio of the input $\eta_{hi}$ and $\eta_{lo}$. Specifically, if the input interval satisfies ${\eta_{hi}/\eta_{lo}} = 2^{2^{k}}$ for $k \in {\mathbb{N}}$ (which it does in Algorithm 1), then RootFindingBisection performs exactly $k = {\log{\log\frac{\eta_{hi}}{\eta_{lo}}}}$ bisection steps. Consequently, the overall oracle complexity of the the subroutine is $O{({T{\log{\log_{+}\frac{\eta_{hi}}{\eta_{lo}}}}})}$.

<!-- chunk {"id": "body-0030", "role": "body", "section": "Bisection subroutine", "weight": 1.0} -->

We now focus on the end of the bisection procedure and explain the choice of output in algorithm 1. When the bisection loop is complete, we obtain a relatively narrow interval $\lbrack\eta_{lo}^{\star},\eta_{hi}^{\star}\rbrack$ in which ${\phi{(\eta)}} - \eta$ is guaranteed to change its sign. When $\phi$ is continuous, this implies that some $\eta \in {\lbrack\eta_{lo}^{\star},\eta_{hi}^{\star}\rbrack}$ solves $\eta = {\phi{(\eta)}}$ and therefore has a good error bound by Proposition 1. However, $\phi$ is not necessarily continuous.

<!-- chunk {"id": "body-0031", "role": "body", "section": "Bisection subroutine", "weight": 1.0} -->

To explain why the bisection still outputs a good value of $\eta$, first note that Proposition 1 continues to hold (with a slightly worse constant factor) even when $\eta$ only approximately solves $\eta = {\phi{(\eta)}}$, e.g., when The following lemma shows that the output of RootFindingBisection in fact satisfies a similar bound. See Appendix A.1 for the (easy) proof, and note the lemma also holds in the stochastic case.

<!-- chunk {"id": "body-0032", "role": "body", "section": "Doubling scheme for upper bisection limit", "weight": 1.0} -->

Algorithm 1 iteratively calls RootFindingBisection with upper bisection limits $\eta_{hi}$ of the form $2^{2^{k}}\eta_{\varepsilon}$ (for doubling values of $k$) until the bisection returns $\eta_{o} < \infty$, i.e., until $\eta_{hi} > {\phi{(\eta_{hi})}}$. To ensure the overall number of gradient queries never exceeds the budget $B$, for every $k$ the algorithm also adjusts the SGD complexity $T$. In the stochastic case, the parameters $\alpha$ and $\beta$ also increase with $k$ in order to enforce a union bound over an increasing number of SGD sample paths.

<!-- chunk {"id": "body-0033", "role": "body", "section": "Doubling scheme for upper bisection limit", "weight": 1.0} -->

Intuitively, the bisection should succeed once $\eta_{hi} > {d_{0}/{\| g_{0}\|}}$ since this is always an upper bound on the ideal step size $\phi_{ideal}$. Even though we do not know $d_{0}$ and therefore cannot set $\eta_{hi}$ a-priori,^33^3 If an upper bound $D \geq d_{0}$ is available (e.g., the domain diameter) then we may use it instead of a doubling scheme by directly fixing $k$ to be $\log{\log\frac{D}{\eta_{\varepsilon}{\| g_{0}\|}}}$. However, this can improve our error bounds by at most a constant factor. Algorithm 1 will reach such $\eta_{hi}$ when $k$ is roughly $\log{\log\frac{d_{0}}{\eta_{\varepsilon}{\| g_{0}\|}}}$.

<!-- chunk {"id": "body-0034", "role": "body", "section": "Doubling scheme for upper bisection limit", "weight": 1.0} -->

Lemma 4, whose proof appears in Appendix A.3, provides a rigorous version of our intuitive reasoning.

<!-- chunk {"id": "body-0035", "role": "body", "section": "Error guarantees for exact gradients", "weight": 1.0} -->

With Algorithm 1 explained and Proposition 1 and Lemma 4 in place, we are ready to state the parameter-free convergence guarantee in the exact gradient setting. For simplicity of exposition, we fix $\alpha = 3$ and $\beta = 0$, but note that any $\alpha > 1$ yields a similar guarantee.

<!-- chunk {"id": "body-0036", "role": "body", "section": "Analysis for stochastic gradients", "weight": 1.0} -->

In this section, we extend the analysis of Algorithm 1 to the stochastic setting, using the following simple strategy: we define a "good event" under which the noiseless analysis goes through essentially unchanged (Section 4.1), and show that this event occurs with high probability (Section 4.2), obtaining a stochastic, high-probability, analog of our exact gradient result (Section 4.3).

<!-- chunk {"id": "body-0037", "role": "body", "section": "Analysis in a \"good event\"", "weight": 1.0} -->

A careful inspection of our development thus far reveals that we only use the exact gradient assumption by substituting ${\sum_{i < T}\left\langle {\Delta_{i}{(\eta)}},{{x_{i}{(\eta)}} - x_{\star}} \right\rangle} \geq 0$ into Lemma 1. Therefore, we consider the event where this inequality is approximately true. In particular, for $T \in {\mathbb{N}}$, and ${\alpha,\beta,\eta} > 0$ define With this definition in hand, slightly modified versions of our key lemmas from the deterministic analysis (Lemma 2, Proposition 2, Lemma 4) continue to hold. See Sections B.1, B.2 and B.3 for proofs of these results, which follow very similarly to their exact-gradient counterparts.

<!-- chunk {"id": "body-0038", "role": "body", "section": "The good event is likely", "weight": 1.0} -->

We now arrive at the challenging part of the stochastic analysis: showing that the good event we defined occurs with high probability. For this, we require the following standard assumption.

<!-- chunk {"id": "body-0039", "role": "body", "section": "Assumption 1", "weight": 1.0} -->

The stochastic gradient oracle satisfies ${\|{\mathcal{O}{(\eta)}}\|} \leq L$ with probability 1.

<!-- chunk {"id": "body-0040", "role": "body", "section": "Assumption 1", "weight": 1.0} -->

In online parameter-free optimization such assumption is unavoidable if one seeks regret scaling linearly in the comparator norm. However, similarly to the best prior results, our bounds depend on $L$ only via a low-order term.

<!-- chunk {"id": "body-0041", "role": "body", "section": "Assumption 1", "weight": 1.0} -->

The following result shows that, for appropriate choices of $\alpha$ and $\beta$ and any fixed $\eta \geq 0$ the event ${\mathfrak{E}}_{T,\alpha,\beta}{(\eta)}$ has high probability.

<!-- chunk {"id": "body-0042", "role": "body", "section": "Propostion 4", "weight": 1.0} -->

Proposition 4 makes no a-priori assumption on the size of ${x_{i}{(\eta)}} - x_{\star}$, instead controlling it empirically via ${\overline{d}}_{t}{(\eta)}$; this is unusual in the literature and crucial for our purposes. Our proof (given in Section B.5) relies on a time-uniform empirical-Bernstein-type martingale concentration bound.

<!-- chunk {"id": "body-0043", "role": "body", "section": "Propostion 4", "weight": 1.0} -->

However, since this result requires martingale differences that are bounded with probability 1, we cannot apply it on $\left\langle {\Delta_{i}{(\eta)}},{{x_{i}{(\eta)}} - x_{\star}} \right\rangle$ (which is not bounded), nor can we apply it on ${\left\langle {\Delta_{i}{(\eta)}},{{x_{i}{(\eta)}} - x_{\star}} \right\rangle/{\overline{d}}_{t}}{(\eta)}$ (which is bounded but is not adapted to any filtration).

<!-- chunk {"id": "body-0044", "role": "body", "section": "Propostion 4", "weight": 1.0} -->

Instead, we consider processes of the form $\left\langle {\Delta_{i}{(\eta)}},{\Pi_{1}{({{\lbrack{{x_{i}{(\eta)}} - x_{\star}}\rbrack}/s})}} \right\rangle$, where $\Pi_{1}{( \cdot )}$ is the projection to the unit ball and $s$ is a fixed scalar. By carefully union bounding over a set of $O{({\log T})}$ values of $s$, we are able to control the probability of ${\mathfrak{E}}_{T,\alpha,\beta}{(\eta)}$.

<!-- chunk {"id": "body-0045", "role": "body", "section": "Propostion 4", "weight": 1.0} -->

Having shown that the good event occurs with high probably for any fixed $\eta$, our next step is to show that, for proper choices of $\alpha^{(k)}$ and $\beta^{(k)}$, good events hold with high probability for each and every single value of $\eta$ Algorithm 1 might try. Noting that, each value of $k$, Algorithm 1 only tests step size values of the form $2^{j}\eta_{\varepsilon}$ for $j \in {\{ 0,\ldots,2^{k}\}}$, the following lemma (which is a direct application of union bounds) provides the required guarantee; see proof in Section B.6.

<!-- chunk {"id": "body-0046", "role": "body", "section": "Parameter-free rates for stochastic convex optimization", "weight": 1.0} -->

We are ready to state our main result; see proof in Section B.7.

<!-- chunk {"id": "body-0047", "role": "body", "section": "Adaptivity to problem structure", "weight": 1.0} -->

In this section we showcase our algorithm's adaptivity by proving stronger rates of convergence under smoothness and strong-convexity assumptions, without introducing any new parameters.

<!-- chunk {"id": "body-0048", "role": "body", "section": "Adaptivity to smoothness with exact gradients", "weight": 1.0} -->

Let us assume that $f$ is $S$-smooth (i.e., has $S$-Lipschitz gradient), and consider for simplicity the exact gradient setting; we believe that similar results extend to the stochastic setting as well. Under these assumptions, we show that Algorithm 1, *without any changes*, achieves (up to double-logarithmic factors) the ${Sd_{0}^{2}}/T$ suboptimality bound of optimally-tuned GD, as long as $\eta_{\varepsilon} < \frac{1}{2S}$. See Section C.1 for proof.

<!-- chunk {"id": "body-0049", "role": "body", "section": "Adaptivity strong convexity using restarts", "weight": 1.0} -->

We now consider a standard strongly-convex stochastic setup \e.g., in which we assume $f$ to be $\mu$-strongly-convex in $\mathcal{X}$ and admit a stochastic gradient oracle bounded by $L$. (Note that this implies a bound of $L/\mu$ on the diameter of $\mathcal{X}$). Hazan and Kale propose to run SGD for epochs of doubling length and halving step sizes. For a total gradient budget of $B$, they obtain the optimal bound $O{({L^{2}/{({\mu B})}})}$ on the expected optimality gap. However, their scheme requires the initial step size to be proportional to $1/\mu$, and hence requires knowledge of $\mu$.

<!-- chunk {"id": "body-0050", "role": "body", "section": "Adaptivity strong convexity using restarts", "weight": 1.0} -->

We show that restarting Algorithm 1 with doubling gradient budgets (and no step size to tune) recovers (up to double-logarithmic factors) the optimal $1/B$ rate of convergence. To describe the procedure formally, let $\text{ParameterFreeTuner}{(x_{0},B,\delta,\eta_{\varepsilon})}$ denote the output of Algorithm 1 with initial point $x_{0}$, gradient budget $B$, failure probability $\delta$, minimal step size $\eta_{\varepsilon}$ and $\alpha^{(k)},\beta^{(k)}$ as in eq. 13. For user-specified $\varepsilon > 0$ and $\delta \in {}$ and $x^{} = x_{0}$, our doubling procedure is
