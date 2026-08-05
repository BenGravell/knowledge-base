<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Gaussian Process Optimization in the Bandit Setting: No Regret and Experimental Design

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Many applications require optimizing an unknown, noisy function that is expensive to evaluate. We formalize this task as a multi-armed bandit problem, where the payoff function is either sampled from a Gaussian process (GP) or has low RKHS norm. We resolve the important open problem of deriving regret bounds for this setting, which imply novel convergence rates for GP optimization. We analyze GP-UCB, an intuitive upper-confidence based algorithm, and bound its cumulative regret in terms of maximal information gain, establishing a novel connection between GP optimization and experimental design. Moreover, by bounding the latter in terms of operator spectra, we obtain explicit sublinear regret bounds for many commonly used covariance functions. In some important cases, our bounds have surprisingly weak dependence on the dimensionality. In our experiments on real sensor data, GP-UCB compares favorably with other heuristical GP optimization approaches.

<!-- chunk {"id": "body-0003", "role": "body", "section": "Introduction", "weight": 1.5} -->

In most stochastic optimization settings, evaluating the unknown function is expensive, and sampling is to be minimized. Examples include choosing advertisements in sponsored search to maximize profit in a click-through model or learning optimal control strategies for robots. Predominant approaches to this problem include the multi-armed bandit paradigm, where the goal is to maximize cumulative reward by optimally balancing exploration and exploitation, and experimental design, where the function is to be explored globally with as few evaluations as possible, for example by maximizing information Andreas Krause California Institute of Technology krausea@caltech.edu Matthias Seeger Saarland University mseeger@mmci.uni-saarland.de gain. The challenge in both approaches is twofold: we have to estimate an unknown function f from noisy samples, and we must optimize our estimate over some high-dimensional input space. For the former, much progress has been made in machine learning through kernel methods and Gaussian process (GP) models, where smoothness assumptions about f are encoded through the choice of kernel in a flexible nonparametric fashion. Beyond Euclidean spaces, kernels can be defined on diverse domains such as spaces of graphs, sets, or lists.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

1 This is the longer version of our paper in ICML 2010; see Srinivas et al.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

We are concerned with GP optimization in the multiarmed bandit setting, where f is sampled from a GP distribution or has low 'complexity' measured in terms of its RKHS norm under some kernel. We provide the first sublinear regret bounds in this nonparametric setting, which imply convergence rates for GP optimization. In particular, we analyze the Gaussian Process Upper Confidence Bound ( GP-UCB ) algorithm, a simple and intuitive Bayesian method. While objectives are different in the multi-armed bandit and experimental design paradigm, our results draw a close technical connection between them: our regret bounds come in terms of an information gain quantity, measuring how fast f can be learned in an information theoretic sense. The submodularity of this function allows us to prove sharp regret bounds for particular covariance functions, which we demonstrate for commonly used Squared Exponential and Mat´ ern kernels.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

Related Work. Our work generalizes stochastic linear optimization in a bandit setting, where the unknown function comes from a finite-dimensional linear space. GPs are nonlinear random functions, which can be represented in an infinite-dimensional linear space. For the standard linear setting, Dani et al. provide a near-complete characterization, explicitly dependent on the dimensionality. In the GP setting, the challenge is to characterize complexity in a different manner, through properties of the kernel function. Our technical contributions are twofold: first, we show how to analyze the nonlinear setting by focusing on the concept of information gain, and second, we explicitly bound this information gain measure using the concept of submodularity and knowledge about kernel operator spectra.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

Kleinberg et al. provide regret bounds under weaker and less configurable assumptions, which however degrade rapidly with the dimensionality of the problem (Ω( T d +1 d +2 )). In practice, linearity w.r.t. a fixed basis is often too stringent an assumption, while Lipschitz-continuity can be too coarse-grained, leading to poor rate bounds. Adopting GP assumptions, we can model levels of smoothness in a fine-grained way. For example, our rates for the frequently used Squared Exponential kernel, enforcing a high degree of smoothness, have weak dependence on the dimensionality: O ( √ T (log T ) d +1 ) (see Fig. 1).

<!-- chunk {"id": "body-0008", "role": "body", "section": "Introduction", "weight": 1.5} -->

There is a large literature on GP (response surface) optimization. Several heuristics for trading off exploration and exploitation in GP optimization have been proposed and successfully applied in practice. Brochu et al. provide a comprehensive review of and motivation for Bayesian optimization using GPs. The Efficient Global Optimization (EGO) algorithm for optimizing expensive black-box functions is proposed by Jones et al. and extended to GPs by Huang et al.. Little is known about theoretical performance of GP optimization. While convergence of EGO is established by Vazquez & Bect, convergence rates have remained elusive. Gr¨ unew¨ alder et al. consider the pure exploration problem for GPs, where the goal is to find the optimal decision over T rounds, rather than maximize cumulative reward (with no exploration/exploitation dilemma). They provide sharp bounds for this exploration problem. Note that this methodology would not lead to bounds for minimizing the cumulative regret. Our cumulative regret bounds translate to the first performance guarantees (rates) for GP optimization.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Introduction", "weight": 1.5} -->

- We analyze GP-UCB, an intuitive algorithm for GP optimization, when the function is either sam- Figure 1. Our regret bounds (up to polylog factors) for linear, radial basis, and Mat´ ern kernels d is the dimension, T is the time horizon, and ν is a Mat´ ern parameter.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Introduction", "weight": 1.5} -->

| Kernel | Linear | RBF | Matérn | pled from a known GP, or has low RKHS norm.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Introduction", "weight": 1.5} -->

- We bound the cumulative regret for GP-UCB in terms of the information gain due to sampling, establishing a novel connection between experimental design and GP optimization. - By bounding the information gain for popular classes of kernels, we establish sublinear regret bounds for GP optimization for the first time. Our bounds depend on kernel choice and parameters in a fine-grained fashion. - We evaluate GP-UCB on sensor network data, demonstrating that it compares favorably to existing algorithms for GP optimization.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Problem Statement and Background", "weight": 1.0} -->

Consider the problem of sequentially optimizing an unknown reward function f: D → R: in each round t, we choose a point x t ∈ D and get to see the function value there, perturbed by noise: y t = f ( x t ) + ϵ t. Our goal is to maximize the sum of rewards ∑ T t =1 f ( x t ), thus to perform essentially as well as x ∗ = argmax x ∈ D f ( x ) (as rapidly as possible). For example, we might want to find locations of highest temperature in a building by sequentially activating sensors in a spatial network and regressing on their measurements. D consists of all sensor locations, f ( x ) is the temperature at x, and sensor accuracy is quantified by the noise variance. Each activation draws battery power, so we want to sample from as few sensors as possible.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Problem Statement and Background", "weight": 1.0} -->

Regret. A natural performance metric in this context is cumulative regret, the loss in reward due to not knowing f 's maximum points beforehand. Suppose the unknown function is f, its maximum point 1 x ∗ = argmax x ∈ D f ( x ). For our choice x t in round t, we incur instantaneous regret r t = f ( x ∗ ) -f ( x t ). The cumulative regret R T after T rounds is the sum of instantaneous regrets: R T = ∑ T t =1 r t. A desirable asymptotic property of an algorithm is to be no-regret: lim T →∞ R T /T = 0. Note that neither r t nor R T are ever revealed to the algorithm. Bounds on the average regret R T /T translate to convergence rates for GP optimization: the maximum max t ≤ T f ( x t ) in the first T rounds is no further from f ( x ∗ ) than the average.

<!-- chunk {"id": "body-0014", "role": "body", "section": "Problem Statement and Background", "weight": 1.0} -->

1 x ∗ need not be unique; only f ( x ∗ ) occurs in the regret.

<!-- chunk {"id": "body-0015", "role": "body", "section": "Gaussian Processes and RKHS's", "weight": 1.0} -->

Gaussian Processes. Some assumptions on f are required to guarantee no-regret. While rigid parametric assumptions such as linearity may not hold in practice, a certain degree of smoothness is often warranted. In our sensor network, temperature readings at closeby locations are highly correlated (see Figure 2(a)). We can enforce implicit properties like smoothness without relying on any parametric assumptions, modeling f as a sample from a Gaussian process (GP): a collection of dependent random variables, one for each x ∈ D, every finite subset of which is multivariate Gaussian distributed in an overall consistent way. A GP ( µ ( x ), k ( x, x ′ )) is specified by its mean function µ ( x ) = E [ f ( x )] and covariance (or kernel) function k ( x, x ′ ) = E [( f ( x ) -µ ( x ))( f ( x ′ ) -µ ( x ′ ))]. For GPs not conditioned on data, we assume 2 that µ ≡ 0. Moreover, we restrict k ( x, x ) ≤ 1, x ∈ D, i.e., we assume bounded variance.

<!-- chunk {"id": "body-0016", "role": "body", "section": "Gaussian Processes and RKHS's", "weight": 1.0} -->

By fixing the correlation behavior, the covariance function k encodes smoothness properties of sample functions f drawn from the GP. A range of commonly used kernel functions is given in Section 5.2.

<!-- chunk {"id": "body-0017", "role": "body", "section": "Gaussian Processes and RKHS's", "weight": 1.0} -->

In this work, GPs play multiple roles. First, some of our results hold when the unknown target function is a sample from a known GP distribution GP(0, k (x, x ′)). Second, the Bayesian algorithm we analyze generally uses GP(0, k (x, x ′)) as prior distribution over f. A major advantage of working with GPs is the existence of simple analytic formulae for mean and covariance of the posterior distribution, which allows easy implementation of algorithms. For a noisy sample y T = [y 1... y T] T at points A T = { x 1,..., x T }, y t = f (x t)+ ϵ t with ϵ t ∼ N (0, σ 2) i.i.d. Gaussian noise, the posterior over f is a GP distribution again, with mean µ T (x), covariance k T (x, x ′) and variance σ 2 T (x): where k T (x) = [k (x 1, x).

<!-- chunk {"id": "body-0018", "role": "body", "section": "Gaussian Processes and RKHS's", "weight": 1.0} -->

k (x T, x)] T and K T is the positive definite kernel matrix [k (x, x ′)] x, x ′ ∈ A T.

<!-- chunk {"id": "body-0019", "role": "body", "section": "Gaussian Processes and RKHS's", "weight": 1.0} -->

RKHS. Instead of the Bayes case, where f is sampled from a GP prior, we also consider the more agnostic case where f has low 'complexity' as measured under an RKHS norm (and distribution free assumptions on the noise process). The notion of reproducing kernel Hilbert spaces is intimately related to GPs and their covariance functions k ( x, x ′ ). The RKHS H k ( D ) is a complete subspace of L 2 ( D ) of nicely behaved functions, with an inner product 〈·, ·〉 k obeying the reproducing property: 〈 f, k ( x, · ) 〉 k = f ( x ) for all f ∈ H k ( D ). It is literally constructed by completing the set of mean functions µ T for all possible T, { x t }, and y T. The induced RKHS norm ‖ f ‖ k = √ 〈 f, f 〉 k measures smoothness of f w.r.t. k: in much the same way as k 1 would generate smoother samples than k 2 as GP covariance functions, ‖·‖ k 1 assigns larger penalties than ‖·‖ k 2.

<!-- chunk {"id": "body-0020", "role": "body", "section": "Gaussian Processes and RKHS's", "weight": 1.0} -->

〈·, ·〉 k can be extended to all of L 2 ( D ), in which case ‖ f ‖ k < ∞ iff f ∈ H k ( D ). For most kernels discussed in Section 5.2, members of H k ( D ) can uniformly approximate any continuous function on any compact subset of D.

<!-- chunk {"id": "body-0021", "role": "body", "section": "Information Gain & Experimental Design", "weight": 1.0} -->

One approach to maximizing f is to first choose points x t so as to estimate the function globally well, then play the maximum point of our estimate. How can we learn about f as rapidly as possible? This question comes down to Bayesian Experimental Design, where the informativeness of a set of sampling points A ⊂ D about f is measured by the information gain, which is the mutual information between f and observations y A = f A + ϵ A at these points: quantifying the reduction in uncertainty about f from revealing y A. Here, f A = [f (x)] x ∈ A and ε A ∼ N (0, σ 2 I). For a Gaussian, H(N (µ, Σ)) = 1 2 log | 2 πe Σ |, so that in our setting I(y A; f) = I(y A; f A) = 1 2 log | I + σ -2 K A |, where K A = [k (x, x ′)] x, x ′ ∈ A. While finding the information gain maximizer among A ⊂ D, | A | ≤ T is NP-hard, it can be approximated by an efficient greedy algorithm.

<!-- chunk {"id": "body-0022", "role": "body", "section": "Information Gain & Experimental Design", "weight": 1.0} -->

If F (A) = I(y A; f), this algorithm picks x t = argmax x ∈ D F (A t -1 ∪{ x }) in round t, which can be shown to be equivalent to where A t -1 = { x 1,..., x t -1 }. Importantly, this simple algorithm is guaranteed to find a near-optimal solution: for the set A T obtained after T rounds, we have that at least a constant fraction of the optimal information gain value. This is because F (A) satisfies a diminishing returns property called submodularity, and the greedy approximation guarantee holds for any submodular function.

<!-- chunk {"id": "body-0023", "role": "body", "section": "Information Gain & Experimental Design", "weight": 1.0} -->

While sequentially optimizing Eq. 4 is a provably good way to explore f globally, it is not well suited for func- tion optimization. For the latter, we only need to identify points x where f ( x ) is large, in order to concentrate sampling there as rapidly as possible, thus exploit our knowledge about maxima. In fact, the ED rule does not even depend on observations y t obtained along the way. Nevertheless, the maximum information gain after T rounds will play a prominent role in our regret bounds, forging an important connection between GP optimization and experimental design.

<!-- chunk {"id": "body-0024", "role": "body", "section": "GP-UCB Algorithm", "weight": 1.0} -->

For sequential optimization, the ED rule can be wasteful: it aims at decreasing uncertainty globally, not just where maxima might be. Another idea is to pick points as x t = argmax x ∈ D µ t -1 (x), maximizing the expected reward based on the posterior so far. However, this rule is too greedy too soon and tends to get stuck in shallow local optima. A combined strategy is to choose where β t are appropriate constants. This latter objective prefers both points x where f is uncertain (large σ t -1 (·)) and such where we expect to achieve high rewards (large µ t -1 (·)): it implicitly negotiates the exploration-exploitation tradeoff. A natural interpretation of this sampling rule is that it greedily selects points x such that f (x) should be a reasonable upper bound on f (x ∗), since the argument in is an upper quantile of the marginal posterior P (f (x) | y t -1). We call this choice the Gaussian process upper confidence bound rule (GP-UCB), where β t is specified depending on the context (see Section 4).

<!-- chunk {"id": "body-0025", "role": "body", "section": "GP-UCB Algorithm", "weight": 1.0} -->

Pseudocode for the GP-UCB algorithm is provided in Algorithm 1. Figure 2 illustrates two subsequent iterations, where GP-UCB both explores (Figure 2(b)) by sampling an input x with large σ 2 t -1 (x) and exploits (Figure 2(c)) by sampling x with large µ t -1 (x).

<!-- chunk {"id": "body-0026", "role": "body", "section": "GP-UCB Algorithm", "weight": 1.0} -->

The GP-UCB selection rule Eq. 6 is motivated by the UCB algorithm for the classical multi-armed bandit problem. Among competing criteria for GP optimization (see Section 1), a variant of the GP-UCB rule has been demonstrated to be effective for this application. To our knowledge, strong theoretical results of the kind provided for GP-UCB in this paper have not been given for any of these search heuristics. In Section 6, we show that in practice GP-UCB compares favorably with these alternatives.

<!-- chunk {"id": "body-0027", "role": "body", "section": "GP-UCB Algorithm", "weight": 1.0} -->

If D is infinite, finding x t in may be hard: the upper confidence index is multimodal in general. However, global search heuristics are very effective in practice. It is generally assumed Algorithm 1 The GP-UCB algorithm. Input: Input space D; GP Prior µ 0 = 0, σ 0, k for t = 1, 2,... do Choose x t = argmax x ∈ D µ t -1 ( x ) + √ β t σ t -1 ( x ) Sample y t = f ( x t ) + ϵ t Perform Bayesian update to obtain µ t and σ t end for that evaluating f is more costly than maximizing the UCB index.

<!-- chunk {"id": "body-0028", "role": "body", "section": "GP-UCB Algorithm", "weight": 1.0} -->

UCB algorithms (and GP optimization techniques in general) have been applied to a large number of problems in practice. Their performance is well characterized in both the finite arm setting and the linear optimization setting, but no convergence rates for GP optimization are known.

<!-- chunk {"id": "body-0029", "role": "body", "section": "Regret Bounds", "weight": 1.0} -->

We now establish cumulative regret bounds for GP optimization, treating a number of different settings: f ∼ GP(0, k ( x, x ′ )) for finite D, f ∼ GP(0, k ( x, x ′ )) for general compact D, and the agnostic case of arbitrary f with bounded RKHS norm.

<!-- chunk {"id": "body-0030", "role": "body", "section": "Regret Bounds", "weight": 1.0} -->

GP optimization generalizes stochastic linear optimization, where a function f from a finite-dimensional linear space is optimized over. For the linear case, Dani et al. provide regret bounds that explicitly depend on the dimensionality 3 d. GPs can be seen as random functions in some infinite-dimensional linear space, so their results do not apply in this case. This problem is circumvented in our regret bounds. The quantity governing them is the maximum information gain γ T after T rounds, defined as: where I(y A; f A) = I(y A; f) is defined.

<!-- chunk {"id": "body-0031", "role": "body", "section": "Regret Bounds", "weight": 1.0} -->

Recall that I(y A; f A) = 1 2 log | I + σ -2 K A |, where K A = [k (x, x ′)] x, x ′ ∈ A is the covariance matrix of f A = [f (x)] x ∈ A associated with the samples A. Our regret bounds are of the form O ∗ (√ Tβ T γ T), where β T is the confidence parameter in Algorithm 1, while the bounds of Dani et al. are of the form O ∗ (√ Tβ T d) (d the dimensionality of the linear function space). Here and below, the O ∗ notation is a variant of O, where log factors are suppressed. While our proofs - all provided in the Appendix - use techniques similar to those of Dani et al., we face a number of additional significant technical challenges. Besides avoiding the finite-dimensional analysis, we must handle confidence issues, which are more delicate for nonlinear random functions.

<!-- chunk {"id": "body-0032", "role": "body", "section": "Regret Bounds", "weight": 1.0} -->

3 In general, d is the dimensionality of the input space D, which in the finite-dimensional linear case coincides with the feature space.

<!-- chunk {"id": "body-0033", "role": "body", "section": "Regret Bounds", "weight": 1.0} -->

Importantly, note that the information gain is a problem dependent quantity - properties of both the kernel and the input space will determine the growth of regret. In Section 5, we provide general methods for bounding γ T, either by efficient auxiliary computations or by direct expressions for specific kernels of interest. Our results match known lower bounds (up to log factors) in both the K -armed bandit and the d -dimensional linear optimization case.

<!-- chunk {"id": "body-0034", "role": "body", "section": "Regret Bounds", "weight": 1.0} -->

Bounds for a GP Prior. For finite D, we obtain the following bound.

<!-- chunk {"id": "body-0035", "role": "body", "section": "Regret Bounds", "weight": 1.0} -->

Theorem 1 Let δ ∈ and β t = 2 log(| D | t 2 π 2 / 6 δ). Running GP-UCB with β t for a sample f of a GP with mean function zero and covariance function k (x, x ′), we obtain a regret bound of O ∗ (√ Tγ T log | D |) with high probability. Precisely, The proof methodology follows Dani et al. in that we relate the regret to the growth of the log volume of the confidence ellipsoid - a novelty in our proof is showing how this growth is characterized by the information gain.

<!-- chunk {"id": "body-0036", "role": "body", "section": "Regret Bounds", "weight": 1.0} -->

This theorem shows that, with high probability over samples from the GP, the cumulative regret is bounded in terms of the maximum information gain, forging a novel connection between GP optimization and experimental design. This link is of fundamental technical importance, allowing us to generalize Theorem 1 to infinite decision spaces. Moreover, the submodularity of I( y A; f A ) allows us to derive sharp a priori bounds, depending on choice and parameterization of k (see Section 5). In the following theorem, we generalize our result to any compact and convex D ⊂ R d under mild assumptions on the kernel function k.

<!-- chunk {"id": "body-0037", "role": "body", "section": "Regret Bounds", "weight": 1.0} -->

Theorem 2 Let D ⊂ [0, r] d be compact and convex, d ∈ N, r > 0. Suppose that the kernel k (x, x ′) satisfies the following high probability bound on the derivatives of GP sample paths f: for some constants a, b > 0, Pick δ ∈, and define Running the GP-UCB with β t for a sample f of a GP with mean function zero and covariance function k (x, x ′), we obtain a regret bound of O ∗ (√ dTγ T) with high probability. Precisely, with C 1 = 8 / log(1 + σ -2) we have The main challenge in our proof (provided in the Appendix) is to lift the regret bound in terms of the confidence ellipsoid to general D. The smoothness assumption on k (x, x ′) disqualifies GPs with highly erratic sample paths.

<!-- chunk {"id": "body-0038", "role": "body", "section": "Regret Bounds", "weight": 1.0} -->

It holds for stationary kernels k (x, x ′) = k (x -x ′) which are four times differentiable (Theorem 5 of Ghosal & Roy), such as the Squared Exponential and Mat´ ern kernels with ν > 2 (see Section 5.2), while it is violated for the OrnsteinUhlenbeck kernel (Mat´ ern with ν = 1 / 2; a stationary variant of the Wiener process). For the latter, sample paths f are nondifferentiable almost everywhere with probability one and come with independent increments. We conjecture that a result of the form of Theorem 2 does not hold in this case.

<!-- chunk {"id": "body-0039", "role": "body", "section": "Regret Bounds", "weight": 1.0} -->

Bounds for Arbitrary f in the RKHS. Thus far, we have assumed that the target function f is sampled from a GP prior and that the noise is N (0, σ 2 ) with known variance σ 2. We now analyze GP-UCB in an agnostic setting, where f is an arbitrary function from the RKHS corresponding to kernel k ( x, x ′ ). Moreover, we allow the noise variables ε t to be an arbitrary martingale difference sequence (meaning that E [ ε t | ε <t ] = 0 for all t ∈ N ), uniformly bounded by σ. Note that we still run the same GP-UCB algorithm, whose prior and noise model are misspecified in this case. Our following result shows that GP-UCB attains sublinear regret even in the agnostic setting.

<!-- chunk {"id": "body-0040", "role": "body", "section": "Regret Bounds", "weight": 1.0} -->

Theorem 3 Let δ ∈. Assume that the true underlying f lies in the RKHS H k (D) corresponding to the kernel k (x, x ′), and that the noise ε t has zero mean conditioned on the history and is bounded by σ almost surely. In particular, assume ‖ f ‖ 2 k ≤ B and let β t = 2 B +300 γ t log 3 (t/δ). Running GP-UCB with β t, prior GP (0, k (x, x ′)) and noise model N (0, σ 2), we obtain a regret bound of O ∗ (√ T (B √ γ T + γ T)) with high probability (over the noise). Precisely, Note that while our theorem implicitly assumes that GP-UCB has knowledge of an upper bound on ‖ f ‖ k, standard guess-and-doubling approaches suffice if no such bound is known a priori. Comparing Theorem 2 and Theorem 3, the latter holds uniformly over all functions f with ‖ f ‖ k < ∞, while the former is a probabilistic statement requiring knowledge of the GP that f is sampled.

<!-- chunk {"id": "body-0041", "role": "body", "section": "Regret Bounds", "weight": 1.0} -->

In contrast, if f ∼ GP(0, k (x, x ′)), then ‖ f ‖ k = ∞ almost surely: sample paths are rougher than RKHS functions. Neither Theorem 2 nor 3 encompasses the other.

<!-- chunk {"id": "body-0042", "role": "body", "section": "Bounding the Information Gain", "weight": 1.0} -->

Since the bounds developed in Section 4 depend on the information gain, the key remaining question is how to bound the quantity γ T for practical classes of kernels.

<!-- chunk {"id": "body-0043", "role": "body", "section": "Submodularity and Greedy Maximization", "weight": 1.0} -->

In order to bound γ T, we have to maximize the information gain F (A) = I(y A; f) over all subsets A ⊂ D of size T: a combinatorial problem in general. However, as noted in Section 2, F (A) is a submodular function, which implies the performance guarantee for maximizing F sequentially by the greedy ED rule. Dividing both sides of by 1 -1 /e, we can upper-bound γ T by (1 -1 /e) -1 I(y A T; f), where A T is constructed by the greedy procedure. Thus, somewhat counterintuitively, instead of using submodularity to prove that F (A T) is near-optimal, we use it in order to show that γ T is 'near-greedy'. As noted in Section 2, the ED rule does not depend on observations y t and can be run without evaluating f.

<!-- chunk {"id": "body-0044", "role": "body", "section": "Submodularity and Greedy Maximization", "weight": 1.0} -->

The importance of this greedy bound is twofold. First, it allows us to numerically compute highly problem-specific bounds on γ T, which can be plugged into our results in Section 4 to obtain high-probability bounds on R T. This being a laborious procedure, one would prefer a priori bounds for γ T in practice which are simple analytical expressions of T and parameters of k. In this section, we sketch a general procedure for obtaining such expressions, instantiating them for a number of commonly used covariance functions, once more relying crucially on the greedy ED rule upper bound. Suppose that D is finite for now, and let f = [f (x)] x ∈ D, K D = [k (x, x ′)] x, x ′ ∈ D. Sampling f at x t, we obtain y t ∼ N (v T t f, σ 2), where v t ∈ R | D | is the indicator vector associated with x t. We can upper-bound the greedy maximum once more, by relaxing this constraint to ‖ v t ‖ = 1 in round t of the sequential method.

<!-- chunk {"id": "body-0045", "role": "body", "section": "Submodularity and Greedy Maximization", "weight": 1.0} -->

For this relaxed greedy procedure, all v t are leading eigenvectors of K D, since successive covariance matrices of P (f | y t -1) share their eigenbasis with K D, while eigenvalues are damped according to how many times the corresponding eigenvector is selected. We can upper-bound the information gain by considering the worst-case allocation of T samples to the min { T, | D |} leading eigenvectors of K D: subject to ∑ t m t = T, and spec(K D) = { ˆ λ 1 ≥ ˆ λ 2 ≥... }. We can split the sum into two parts in order to obtain a bound to leading order. The following Theorem captures this intuition: Therefore, if for some T ∗ = o (T) the first T ∗ eigenvalues carry most of the total mass n T, the information gain will be small. The more rapidly the spectrum of K D decays, the slower the growth of γ T. Figure 3 illustrates this intuition.

<!-- chunk {"id": "body-0046", "role": "body", "section": "Bounds for Common Kernels", "weight": 1.0} -->

In this section we bound γ T for a range of commonly used covariance functions: finite dimensional linear, Squared Exponential and Mat´ ern kernels. Together with our results in Section 4, these imply sublinear regret bounds for GP-UCB in all cases.

<!-- chunk {"id": "body-0047", "role": "body", "section": "Bounds for Common Kernels", "weight": 1.0} -->

Finite dimensional linear kernels have the form k ( x, x ′ ) = x T x ′. GPs with this kernel correspond to random linear functions f ( x ) = w T x, w ∼ N ( 0, I ).

<!-- chunk {"id": "body-0048", "role": "body", "section": "Bounds for Common Kernels", "weight": 1.0} -->

The Squared Exponential kernel is k ( x, x ′ ) = exp( -(2 l 2 ) -1 ‖ x -x ′ ‖ 2 ), l a lengthscale parameter. Sample functions are differentiable to any order almost surely.

<!-- chunk {"id": "body-0049", "role": "body", "section": "Bounds for Common Kernels", "weight": 1.0} -->

The Mat´ ern kernel is given by k ( x, x ′ ) = (2 1 -ν / Γ( ν )) r ν B ν ( r ), r = ( √ 2 ν/l ) ‖ x -x ′ ‖, where ν controls the smoothness of sample paths (the smaller, the rougher) and B ν is a modified Bessel function. Note that as ν → ∞, appropriately rescaled Mat´ ern kernels converge to the Squared Exponential kernel.

<!-- chunk {"id": "body-0050", "role": "body", "section": "Bounds for Common Kernels", "weight": 1.0} -->

Theorem 5 Let D ⊂ R d be compact and convex, d ∈ N. Assume the kernel function satisfies k (x, x ′) ≤ 1. 1. Finite spectrum. For the d -dimensional Bayesian linear regression case: γ T = O (d log T). 2. Exponential spectral decay. For the Squared Exponential kernel: γ T = O ((log T) d +1). 3. Power law spectral decay. For Mat´ ern kernels with ν > 1: γ T = O (T d (d +1) / (2 ν + d (d +1)) (log T)).

<!-- chunk {"id": "body-0051", "role": "body", "section": "Bounds for Common Kernels", "weight": 1.0} -->

A proof of Theorem 5 is given in the Appendix we only sketch the idea here. γ T is bounded by Theorem 4 in terms the eigendecay of the kernel matrix K D. If D is infinite or very large, we can use the operator spectrum of k ( x, x ′ ), which likewise decays rapidly. For the kernels of interest here, asymptotic expressions for the operator eigenvalues are given in Seeger et al., who derived bounds on the information gain for fixed and random designs (in contrast to the worst-case information gain considered here, which is substantially more challenging to bound). The main challenge in the proof is to ensure the existence of discretizations D T ⊂ D, dense in the limit, for which tail sums B ( T ∗ ) /n T in Theorem 4 are close to corresponding operator spectra tail sums.

<!-- chunk {"id": "body-0052", "role": "body", "section": "Bounds for Common Kernels", "weight": 1.0} -->

Together with Theorems 2 and 3, this result guarantees sublinear regret of GP-UCB for any dimension (see Figure 1). For the Squared Exponential kernel, the dimension d appears as exponent of log T only, so that the regret grows at most as O ∗ ( √ T (log T ) d +1 2 ) - the high degree of smoothness of the sample paths effectively combats the curse of dimensionality.

<!-- chunk {"id": "body-0053", "role": "body", "section": "Experiments", "weight": 1.0} -->

We compare GP-UCB with heuristics such as the Expected Improvement (EI) and Most Probable Improvement (MPI), and with naive methods which choose points of maximum mean or variance only, both on synthetic and real sensor network data.

<!-- chunk {"id": "body-0054", "role": "body", "section": "Experiments", "weight": 1.0} -->

For synthetic data, we sample random functions from a squared exponential kernel with lengthscale parameter 0. 2. The sampling noise variance σ 2 was set to 0. 025 or 5% of the signal variance. Our decision set D = is uniformly discretized into 1000 points. We run each algorithm for T = 1000 iterations with δ = 0. 1, averaging over 30 trials (samples from the kernel). While the choice of β t as recommended by Theorem 1 leads to competitive performance of GP-UCB, we find (using cross-validation) that the algorithm is improved by scaling β t down by a factor 5. Note that we did not optimize constants in our regret bounds.

<!-- chunk {"id": "body-0055", "role": "body", "section": "Experiments", "weight": 1.0} -->

Next, we use temperature data collected from 46 sensors deployed at Intel Research Berkeley over 5 days at 1 minute intervals, pertaining to the example in Section 2. We take the first two-thirds of the data set to compute the empirical covariance of the sensor readings, and use it as the kernel matrix. The functions f for optimization consist of one set of observations from all the sensors taken from the remaining third of the data set, and the results (for T = 46, σ 2 = 0. 5 or 5% noise, δ = 0. 1) were averaged over 2000 possible choices of the objective function.

<!-- chunk {"id": "body-0056", "role": "body", "section": "Experiments", "weight": 1.0} -->

Lastly, we take data from traffic sensors deployed along the highway I-880 South in California. The goal was to find the point of minimum speed in order to identify the most congested portion of the highway; we used traffic speed data for all working days from 6 AM to 11 AM for one month, from 357 sensors. We again use the covariance matrix from two-thirds of the data set as kernel matrix, and test on the other third. The results (for T = 357, σ 2 = 4. 78 or 5% noise, δ = 0. 1) were averaged over 900 runs.

<!-- chunk {"id": "body-0057", "role": "body", "section": "Conclusions", "weight": 1.0} -->

We prove the first sublinear regret bounds for GP optimization with commonly used kernels (see Figure 1), both for f sampled from a known GP and f of low RKHS norm. We analyze GP-UCB, an intuitive, Bayesian upper confidence bound based sampling rule. Our regret bounds crucially depend on the information gain due to sampling, establishing a novel connection between bandit optimization and experimental design. We bound the information gain in terms of the kernel spectrum, providing a general methodology for obtaining regret bounds with kernels of interest. Our experiments on real sensor network data indicate that GPUCB performs at least on par with competing criteria for GP optimization, for which no regret bounds are known at present. Our results provide an interesting step towards understanding exploration-exploitation tradeoffs with complex utility functions.
