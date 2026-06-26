<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Sharp Rates in Dependent Learning Theory: Avoiding Sample Size Deflation for the Square Loss

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

In this work, we study statistical learning with dependent (beta-mixing) data and square loss in a hypothesis class F subset L_Psi_p where Psi_p is the norm |f|_Psi_p defined as sup_m >= 1 m^(-1)/p |f|_L^(m) for some p in [2, infinity]. Our inquiry is motivated by the search for a sharp noise interaction term, or variance proxy, in learning with dependent data. Absent any realizability assumption, typical non-asymptotic results exhibit variance proxies that are deflated multiplicatively by the mixing time of the underlying covariates process. We show that whenever the topologies of L^ and Psi_p are comparable on our hypothesis class F - that is, F is a weakly sub-Gaussian class: |f|_Psi_p <~ |f|_L^^(eta) for some eta in (0, 1] - the empirical risk minimizer achieves a rate that only depends on the complexity of the class and second order statistics in its leading term.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Our result holds whether the problem is realizable or not and we refer to this as a near mixing-free rate, since direct dependence on mixing is relegated to an additive higher order term. We arrive at our result by combining the above notion of a weakly sub-Gaussian class with mixed tail generic chaining. This combination allows us to compute sharp, instance-optimal rates for a wide range of problems. Examples that satisfy our framework include sub-Gaussian linear regression, more general smoothly parameterized function classes, finite hypothesis classes, and bounded smoothness classes.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

While a significant portion the data used in modern learning algorithms exhibits temporal dependencies, we still lack a sharp theory of supervised learning from dependent data. Examples exhibiting such dependencies are far ranging and abundant, and include forecasting applications and data from controls/robotics systems. Over the last several decades, an order-wise rather sharp theory of learning with *independent* data has emerged. An entirely incomplete list of these advances includes the introduction of local Rademacher compleixities by Bartlett et al., sharp rates in misspecified linear regression by Hsu et al., and culminates in the learning without concentration framework by Mendelson, which enables an instance-optimal understanding of many standard learning problems through a *critical radius* that is sensitive to both the noise scale and the (local) geometry of the hypothesis class.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

In principle, one expects these results to be carried over to the dependent ($\beta$-mixing) setting through *blocking*.^11^1See Section D.1 for a description of this technique. At a high level, the blocking technique involves splitting the original data (of length $n \in {\mathbb{N}}$) into consecutive blocks, each of length $k \in {\mathbb{N}}$, with the length chosen such that the starting points of each block are approximately independent. Indeed, several prior works pursue this route. However, the drawback with this approach is that it typically deflates the original sample size by the block length factor $k$. If such a deflation were to appear in the final rate of convergence, this would clearly constitute worst-case behavior; it corresponds to every data point being revealed repeatedly, $k$ times and with perfect dependence, within a sequence of $n$ observations.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

In the context of the square loss function, the typical approach to sidestep this sample size deflation relies on the "noise" (residual term) forming a martingale difference sequence. This approach has been carried out for parametric inference in (generalized) linear dynamical systems by Simchowitz et al. and Kowshik et al. and also for more general hypothesis classes and supervised learning with square loss by Ziemann & Tu. For the square loss function the martingale approach requires that the problem is strongly realizable: the best predictor in the hypothesis class should coincide with the regression function (conditional expectation of targets given past inputs). Put differently, one requires that the hypothesis class is rich enough such that conditional expectation function (of the targets and given past inputs) can be realized by it.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

In this paper, we instead show how the blocking approach can be salvaged for a wide range of hypotheses classes and the square loss function. In contrast to the just-mentioned references, our analysis does not require a realizability assumption. Instead, we show how to extend the analysis of Ziemann et al. for linear regression to more general hypothesis classes. At a high level, this analysis involves combining the above-mentioned blocking technique with Bernstein's inequality. To motivate this approach, let us consider what happens in Bernstein's inequality when we are given $V_{1:n}$ $b$-bounded random variables that are $k$-wise independent, where $k$ divides $n$, and with identical marginals (for simplicity alone).^22^2We say that a sequence $Z_{1:n}$ is $k$-wise independent if each of the blocks $Z_{{{jk} + 1}:{{({j + 1})}k}}$ ($j = {0,1,\ldots,{{n/k} - 1}}$) are independent of each other.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Introduction", "weight": 1.5} -->

By applying Bernstein's inequality to the $bk$-bounded variables ${{\overline{V}}_{i:{n/k}},{\overline{V}}_{i}} \triangleq {\sum_{j = {{{ik} - k} + 1}}^{ik}V_{j}}$ we find that with probability at least $1 - \delta$: If the data instead were completely independent, then in the small and moderate deviations regime $\delta \gtrsim {\exp{({- {{{n\mathbf{E}V_{1}^{2}}/b^{2}}k}})}}$, (1.1) is just as sharp as directly applying Bernstein's inequality to the independent sum. In this regime for this problem, nothing is lost by blocking, even if the data happens to be iid and we use the blocked version of Bernstein's inequality.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Introduction", "weight": 1.5} -->

By contrast, if one were to carry out the same computation using Hoeffding's inequality (for bounded random variables) instead of Bernstein's, we would incur an irreducible factor $k$ in the leading term in all regimes---even if the dependent bound is instantiated for independent variables. This suggests that the variance interacts much more gracefully with blocking arguments than higher order moments.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Introduction", "weight": 1.5} -->

The difficulty in combining blocking with Bernstein's inequality lies in making Bernstein's inequality uniform across the correct portion of the hypothesis class $\mathcal{F}$. Namely, in statistical learning it typically does not suffice to control sums of a single sequence of random variables $V_{1:n}$ but rather we need to uniformly control sums of an indexed family $\{{V_{1:n}{(f)}}:{f \in \mathcal{F}}\}$. To obtain fast rates, this uniform control needs to combined with a localization argument, so that one does "pay" for hypotheses too far away from the ground truth but only those within a certain critical radius. Naïvely union-bounding (or chaining) over such a family unfortunately again reintroduces a sample-size deflation by the block-length factor $k$. This happens because the variance term in (1.1) starts to balance the boundedness term at the above-mentioned critical radius without further assumption.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Introduction", "weight": 1.5} -->

Ziemann et al. show how to overcome the issue of uniformity when $\mathcal{F}$ is a linear class via the Fuk-Nagaev inequality. Unfortunately, this inequality cannot be applied beyond the linear setting. Here, we introduce machinery based on a refinement of sub-Gaussian classes, and a refinement of Bernstein's inequality (due to Maurer & Pontil ), that we combine with mixed-tail generic chaining (as introduced by Dirksen ). Our approach allows us to overcome this issue with blocking and Bernstein's inequality for a surprisingly wide range of function classes, thereby relegating any dependence on mixing to additive higher order terms, instead of the typical multiplicative deflation term.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Contribution", "weight": 1.0} -->

Let us now make our contribution more precise. We are given stationary $\beta$-mixing data ${(X,Y)}_{1:n}$ where the $X_{i}$ (resp. $Y_{i}$) assume values in a subset of a normed space denoted $(\mathsf{X}, \parallel \cdot \parallel_{\mathsf{X}})$ (resp. a Hilbert space $(\mathsf{Y},{\langle \cdot, \cdot \rangle}, \parallel \cdot \parallel)$). We assume that ${(X,Y)}_{1:n}$ is stationary and denote for any $i \in {\lbrack n\rbrack}$ the joint distribution of $(X_{i},Y_{i})$ by $\mathsf{P}_{X,Y}$, and the corresponding marginals are denoted $\mathsf{P}_{X}$ and $\mathsf{P}_{Y}$.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Contribution", "weight": 1.0} -->

We study empirical risk minimization over a hypothesis class $\mathcal{F}$, containing functions $f:{\mathsf{X}\rightarrow\mathsf{Y}}$, and with the square loss function. In this scenario, we study the performance of the (any) empirical risk minimizer Our main contribution is to characterize the rate of convergence of (1.2) to the best possible predictor $f_{\star}$ in the class $\mathcal{F}$ defined as: Let us also denote by $\mathcal{F}_{\star}$ the star-hull of $\mathcal{F}$ around $f_{\star}$.

<!-- chunk {"id": "body-0014", "role": "body", "section": "Contribution", "weight": 1.0} -->

W_{i} \middle| X_{i} \right.\rbrack}} = 0$ for $i \in {\lbrack n\rbrack}$). Note that this restriction is due to a known shortcoming of ERM which holds even in iid settings, and can be removed by modifying the estimator itself; we will discuss this issue in more detail shortly.

<!-- chunk {"id": "body-0015", "role": "body", "section": "Contribution", "weight": 1.0} -->

As is typical in the learning theory literature, we characterize the rate of convergence of (1.2) through a fixed point, or critical radius. This critical radius takes the form as a solution to: where for ${r \in {\mathbb{R}}},{r > 0}$, $rS_{L^{2}}$ is the unit sphere of radius $r$ in $L^{2}$ (the space of square integrable functions, and with the corresponding unit ball denoted $rB_{L^{2}})$ and $\mathbf{V}{(\cdot)}$ denotes the variance operator.

<!-- chunk {"id": "body-0016", "role": "body", "section": "Contribution", "weight": 1.0} -->

This critical radius is akin to the one in Bartlett et al., but also resembles the noise interaction term of Mendelson in that our radius depends on the *weak variance*, $\sup_{g \in {\mathcal{F}_{\star} \cap {r_{\star}S_{L^{2}}}}}{\mathbf{V}\left({\frac{1}{\sqrt{n}}{\sum_{i = 1}^{n}\left\langle W_{i},\frac{g{(X_{i})}}{{\| g\|}_{L^{2}}} \right\rangle}} \right)}$.^33^3The terminology weak variance comes from the empirical processes literature in that the supremum in Definition 2.2. ‣ 2 Ψ_𝑝-Norms, Bernstein’s Inequality and Empirical Processes ‣ Sharp Rates in Dependent Learning Theory: Avoiding Sample Size Deflation for the Square Loss") is on the outside of the expectation.

<!-- chunk {"id": "body-0017", "role": "body", "section": "Contribution", "weight": 1.0} -->

To aid in the interpretation of $r_{\star}$, we will instantiate our main result, Theorem 3.1, for parametric classes and show that this radius exhibits the desired "dimension counting" scaled with noise-to-signal behavior, see Corollary 3.1. ‣ 3 The Main Result ‣ Sharp Rates in Dependent Learning Theory: Avoiding Sample Size Deflation for the Square Loss") and Corollary 3.2. ‣ 3 The Main Result ‣ Sharp Rates in Dependent Learning Theory: Avoiding Sample Size Deflation for the Square Loss"). Moreover, the weak variance term takes into account how targets $Y_{1:n}$ interact with the function class $\mathcal{F}$ through $W_{1:n}$, locally at radius $r_{\star}$ near the minimizer $f_{\star}$, via a second-order statistic. In particular, this variance term is always sharper than the corresponding iid variance term deflated by a factor of the mixing-time (or block-length).

<!-- chunk {"id": "body-0018", "role": "body", "section": "Contribution", "weight": 1.0} -->

With these preliminaries in place we are ready to state an informal version of our main result.

<!-- chunk {"id": "body-0019", "role": "body", "section": "Informal version of Theorem 3.1", "weight": 1.0} -->

*Given data that mixes sufficiently fast, for a wide range of convex or realizable hypothesis classes, any empirical risk minimizer $\hat{f}$ over such a class $\mathcal{F}$ converges at least as fast a rate characterized by the critical radius $r_{\star}$ given by the solution to (1.4) depending on the variance of the noise-class interaction and local scale of the class $\mathcal{F}$. That is with probability $1 - \delta$:* *Moreover, for $d$-dimensional parametric classes the leading term is ${} \times \frac{d + {\log{({1/\delta})}}}{n}$.* The crux of this result is that past a burn-, the ERM excess risk does not directly depend on mixing times, but only on the relevant second order statistics. Put differently, the effect of slow mixing has been relegated to a small additive term with higher order dependence on $1/n$.

<!-- chunk {"id": "body-0020", "role": "body", "section": "Informal version of Theorem 3.1", "weight": 1.0} -->

Indeed, both $r_{\star}$ and the variance term in (1.5) do not directly depend on slow mixing (i.e., are not deflated by the block-length $k$) but only on relevant second order statistics. Slow mixing only affects higher order additive terms that can be pushed into the burn-.

<!-- chunk {"id": "body-0021", "role": "body", "section": "Informal version of Theorem 3.1", "weight": 1.0} -->

The qualifier "wide range" above refers to the requirement that the class $\mathcal{F}$ satisfies a certain topological condition. Recall that for a random variable $Z$ the $\Psi_{p}$-norm is the norm ${\| Z\|}_{\Psi_{p}} = {\sup_{m \geq 1}{m^{- {1/p}}{\| Z\|}_{L^{m}}}}$. We will ask that for some $\eta \in {(0,1\rbrack}$ and $L > 0$, every $f \in \mathcal{F}_{\star}$ satisfies the inequality ${\| f\|}_{\Psi_{p}} \leq {L{\| f\|}_{L^{2}}^{\eta}}$. We will say that such classes are *weakly sub-Gaussian* and will verify that such an inequality indeed holds true for a range of examples in Section 4: bounded smoothness classes, see Proposition 4.1.

<!-- chunk {"id": "body-0022", "role": "body", "section": "Informal version of Theorem 3.1", "weight": 1.0} -->

‣ 4 Examples of Weakly sub-Gaussian Classes ‣ Sharp Rates in Dependent Learning Theory: Avoiding Sample Size Deflation for the Square Loss"); parametric classes that are Lipschitz in their parameterization, see Proposition 4.2; sub-Gaussian linear regression, see Proposition 4.3; finite hypothesis classes, see Proposition 4.4.

<!-- chunk {"id": "body-0023", "role": "body", "section": "Informal version of Theorem 3.1", "weight": 1.0} -->

Finally, the requirement that $\mathcal{F}$ be either convex or realizable can easily be removed with a few modifications if one replaces the empirical risk minimizer by the star estimator of Audibert. In this case (but with the $L^{2}$-error replaced with the no-longer directly comparable excess risk functional) the geometric inequality by Liang et al. takes a similar role to the basic inequality we use below. The necessity of imposing or is due to a known shortcoming of empirical risk minimization outside of convex (or realizable) classes, and not an issue directly related to dependent data.

<!-- chunk {"id": "body-0024", "role": "body", "section": "Talagrand's functionals", "weight": 1.0} -->

For $\alpha \in {(0,\infty)}$, the $\gamma_{\alpha}$-functional of $(\mathcal{H},d)$ is defined by where the infimum is taken over all admissible sequences (we write ${d{(h,H)}} = {\inf_{s \in H}{d{(h,s)}}}$ whenever $H$ is a set). For $\eta \in {}$, we slightly abuse notation and write $\gamma_{\alpha}{(\mathcal{H},d^{\eta})}$ for $d$ replaced with $d^{\eta}$ in (1.9) (while being mindful of that fact that $d^{\eta}$ is not a metric in general).

<!-- chunk {"id": "body-0025", "role": "body", "section": "Talagrand's functionals", "weight": 1.0} -->

Finally, since entropy integrals upper-bound $\gamma_{\alpha}$-functionals, it will also be useful to introduce the covering number $\mathcal{N}_{L^{2}}{(\mathcal{H},s)}$, which denotes the minimal number of $L^{2}$-balls of radius $s$ required to cover $\mathcal{H}$.

<!-- chunk {"id": "body-0026", "role": "body", "section": "$\\Psi_{p}$-Norms, Bernstein's Inequality and Empirical Processes", "weight": 1.0} -->

In this section we establish a few preliminary technical lemmas that will be useful for controlling the multiplier and quadratic processes ((1.8) and (1.6)). We begin with a version of Bernstein's inequality that controls the Laplace transform of $Z$ in terms of its $L^{2q}$-norm ($q \geq 1$) and some $\Psi_{p}$-norm. The lemma comes from Maurer & Pontil.

<!-- chunk {"id": "body-0027", "role": "body", "section": "The Multiplier Process", "weight": 1.0} -->

We will not directly control the multiplier process for $\beta$-mixing variables. Instead we first suppose that the model $\mathsf{P}_{{(X,Y)}_{1:n}}$ is $k$-wise independent (where $k$ divides $n$). We then port these results to the $\beta$-mixing setting by blocking (see Section D.1).

<!-- chunk {"id": "body-0028", "role": "body", "section": "The Multiplier Process", "weight": 1.0} -->

With these remarks in place, we now turn to establishing pointwise control of (1.8) using Lemma 2.1. ‣ 2 Ψ_𝑝-Norms, Bernstein’s Inequality and Empirical Processes ‣ Sharp Rates in Dependent Learning Theory: Avoiding Sample Size Deflation for the Square Loss").

<!-- chunk {"id": "body-0029", "role": "body", "section": "The Quadratic Process", "weight": 1.0} -->

A slight modification of the argument leading to Theorem 2.2. ‣ 2.2 The Quadratic Process ‣ 2 Ψ_𝑝-Norms, Bernstein’s Inequality and Empirical Processes ‣ Sharp Rates in Dependent Learning Theory: Avoiding Sample Size Deflation for the Square Loss") combined with a truncation argument detailed in Lemma C.1. ‣ Appendix C Controlling the Quadratic Process ‣ Sharp Rates in Dependent Learning Theory: Avoiding Sample Size Deflation for the Square Loss") also yields control of the quadratic process.

<!-- chunk {"id": "body-0030", "role": "body", "section": "$\\beta$-Mixing Processes", "weight": 1.0} -->

We extend the empirical process results of the preceding two sections to $\beta$-mixing processes in Section D.2. We do so by a simple blocking argument that we review in Section D.1, and for which we have already set the stage by establishing our results for $k$-wise independent processes. Here, we state the definition of dependence we rely on in the sequel.

<!-- chunk {"id": "body-0031", "role": "body", "section": "Further Comparison to Related Work", "weight": 1.0} -->

In terms of technical development, this work is most closely related to the work on iid learning in sub-Gaussian classes by Lecué & Mendelson and the result for misspecified (agnostic) dependent linear regression by Ziemann et al. ---which we generalize to more general function classes at the cost of more stringent moment assumptions. Returning to Lecué & Mendelson, and beside the fact that they work with independent data, the biggest difference is in how we deal with the multiplier process. We employ chaining with a mixed tail, instead of a single tail. On a practical level, the advantage of the mixed tail result is that it allows us to push the dependence, mixing, $L$ (the norm equivalence parameter in Theorem 3.1) and any higher order norms into the burn-. Crucially, we make the observation that chaining with a mixed tail allows us to work with weaker norm relations ($\eta < 1$ in Definition 2.1. ‣ 2 Ψ_𝑝-Norms, Bernstein’s Inequality and Empirical Processes ‣ Sharp Rates in Dependent Learning Theory: Avoiding Sample Size Deflation for the Square Loss")).

<!-- chunk {"id": "body-0032", "role": "body", "section": "Further Comparison to Related Work", "weight": 1.0} -->

We do not require equivalence of norms but rather a weaker notion of topological equivalence. Such equivalences hold in significantly wider generality than the sub-Gaussian class assumption as we show in Section 4 below. In particular we are able to handle smoothness classes in Proposition 4.1. ‣ 4 Examples of Weakly sub-Gaussian Classes ‣ Sharp Rates in Dependent Learning Theory: Avoiding Sample Size Deflation for the Square Loss"), which cannot be covered in the baseline sub-Gaussian class framework. Another advantage of this approach is that it allows to relegate the parameter $L$ to a higher order term, which appears multiplicatively instead of additively in the bound by Lecué & Mendelson. This is important in order to achieve the correct scaling with temporal dependency as there are typically no obvious bounds on this parameter other than in terms of the block-length $k$. Hence, if our dependence on $L$ were multiplicative instead of additive it would thereby re-introduce the sample-size deflation we sought to sidestep. Again, it is the invocation of the mixed-tail chaining result of Dirksen that allows for this.

<!-- chunk {"id": "body-0033", "role": "body", "section": "Further Comparison to Related Work", "weight": 1.0} -->

Another closely related line of work studies parameter identification in auto-regressive models. When the noise model is strictly realizable---the variables $W_{1:n}$ form a martingale difference sequence with respect to the filtration generated by $X_{1:n}$---parameter identification is possible at the iid rate even in the absence of mixing. Our results do not cover the mixing-free regime as we consider the agnostic setting in which self-normalized martingale arguments are not available. We consider providing a unified analysis of the martingale and mixing situations an interesting future direction.

<!-- chunk {"id": "body-0034", "role": "body", "section": "Further Comparison to Related Work", "weight": 1.0} -->

More generally, several authors have considered learning under various weak dependency notions. Kuznetsov & Mohri give generalization bounds in a more general setting using the same blocking technique---due to Yu ---used here. Statements similar in spirit can also be found in e.g., Steinwart & Christmann, Duchi et al. and most recently Roy et al.. However, they all suffer the dependency deflation discussed above and in our introduction (Section 1). We also note that Ziemann & Tu and Maurer obtain rates---similar to ours here---that relegate mixing times into additive burn-in factors. On the one hand, the work of Ziemann & Tu operates at a similar level of generality when it comes to hypothesis classes and also relies on the square loss function but requires a stringent realizability assumption to be applicable. Moreover, both our noise term and our complexity parameter are sharper than theirs. On the other hand, the work of Maurer operates at a higher level of generality than us, but does not seem to be able to reproduce sharp rates when specialized to our situation.

<!-- chunk {"id": "body-0035", "role": "body", "section": "Examples of Weakly sub-Gaussian Classes", "weight": 1.0} -->

We conclude by collecting a few examples of weakly sub-Gaussian classes (Definition 2.1. ‣ 2 Ψ_𝑝-Norms, Bernstein’s Inequality and Empirical Processes ‣ Sharp Rates in Dependent Learning Theory: Avoiding Sample Size Deflation for the Square Loss")). Arguably the most compelling example identified in the present manuscript are smoothness classes, which are not covered even in the iid setting by Lecué & Mendelson.

<!-- chunk {"id": "body-0036", "role": "body", "section": "Summary", "weight": 1.0} -->

In this work, we obtain instance-optimal convergence rates for learning with the square loss function and dependent data. We overcome the typical deflation, by the mixing time, of the sample size. The main technical step to arrive at this result is a refined analysis of the multiplier process (1.8) via mixed tail generic chaining that is suitable for dependent, $\beta$-mixing, random variables. Indeed, the leading order term of our main result, Theorem 3.1, does not directly depend on any mixing-time type quantities. It mimics the correct asymptotic rate and scales solely in terms of the statistics of order $2q$ of the process at hand (where typically $q = {1 + {o{}}}$). Finally, our result also allows us to evaluate said multiplier process for a wider range of hypothesis classes. Typically, sharp closed form expressions for this process are only available for linear functionals, covered in the iid setting by Lecué & Mendelson and Oliveira, and extended to the $\beta$-mixing setting by Ziemann et al..

<!-- chunk {"id": "body-0037", "role": "body", "section": "Summary", "weight": 1.0} -->

By contrast, since our result relies on a weaker notion of topological equivalence, it is applicable to more general classes, such as smoothness classes (Proposition 4.1. ‣ 4 Examples of Weakly sub-Gaussian Classes ‣ Sharp Rates in Dependent Learning Theory: Avoiding Sample Size Deflation for the Square Loss")) and parametric classes with sufficiently regular parameterization (Proposition 4.2).
