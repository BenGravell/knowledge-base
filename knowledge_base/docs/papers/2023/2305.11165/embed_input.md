<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

The Noise Level in Linear Regression with Dependent Data

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

We derive upper bounds for random design linear regression with dependent (beta-mixing) data absent any realizability assumptions. In contrast to the strictly realizable martingale noise regime, no sharp instance-optimal non-asymptotics are available in the literature. Up to constant factors, our analysis correctly recovers the variance term predicted by the Central Limit Theorem - the noise level of the problem - and thus exhibits graceful degradation as we introduce misspecification. Past a burn-, our result is sharp in the moderate deviations regime, and in particular does not inflate the leading order term by mixing time factors.

<!-- chunk {"id": "body-0003", "role": "body", "section": "Introduction", "weight": 1.5} -->

Ordinary least squares (OLS) regression from a finite sample is one of the most ubiquitous and widely used technique in machine learning. When faced with independent data, there are now sharp tools available to analyze its success optimally under relatively general assumptions. Indeed, a non-asymptotic theory matching the classical asymptotically optimal understanding from statistics has been developed over the last decade. However, once we relax the independence assumption and move toward data that exhibits correlations, the situation is much less well-understood---even for a problem as seemingly simple as linear regression. While sharp asymptotics are available through various limit theorems, there are no general results matching these in the finite sample regime.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

In this paper, we study the instance-specific performance of ordinary least squares in a setting with dependent data---and in contrast to much contemporary work on the theme---without imposing realizability.^11^1A distribution $\mathsf{P}_{X,Y}$ is (linearly) realizable if the regression function $x\mapsto{\mathbf{E}{\lbrack{{Y \mid X} = x}\rbrack}}$ is linear. If in addition to a realizability assumption the noise forms a martingale difference sequence, it is now well-known that martingale methods can be used to demonstrate that dependent linear regression is no harder than its independent counterpart. Furthermore, as long as one maintains such an assumption on the noise, a similar observation even holds true for generalized linear and bilinear models, and regression with square loss more generally.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

However, barring any such strong realizability assumption, martingale methods are no longer directly available, and neither are there any sharp non-asymptotics in the learning theory literature. Absent martingale techniques, a natural approach is to use the blocking technique to port concentration inequalities valid for independent data to the dependent setting. However, since blocking effectively reduces the sample size by a factor of the degree of dependence of the data, a judicious application is necessary in order to recover the correct noise level of the problem---the level predicted by the Central Limit Theorem (CLT).

<!-- chunk {"id": "body-0006", "role": "body", "section": "Contributions", "weight": 1.0} -->

This paper serves to explain how the combination of two simple yet powerful observations sidestep the aforementioned issues with blocking. To better appreciate these observations, we recall that the analysis of random design linear regression decomposes into: controlling the *lower tail* of the empirical covariance matrix; and controlling the interaction between the noise and the covariates.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Contributions", "weight": 1.0} -->

First, as noted by Mendelson, the dominant contribution to the error rate is due to the interaction of the noise with the covariates via the hypothesis class. In linear regression this interaction term takes the form of a random walk (see (2.6) and (2.8) below). While one must also analyze the lower tail of the empirical covariance matrix, its contribution to the final error tends to be lower order. This is exactly the point: the empirical covariance matrix tends to dominate its population counterpart under very mild assumptions. Hence deflating the sample size for this purpose by using dependency is of relatively minor consequence and only amounts to an additional burn-.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Contributions", "weight": 1.0} -->

Second, turning to the random walk---the noise-class interaction term---the above issue with blocking can be remedied if one restricts its use to control only the largest scale of deviation. This observation can be traced to the moderate deviations literature, but does not seem to have made its way into the learning theory literature.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Contributions", "weight": 1.0} -->

To explain this idea, let us recall Bernstein's inequality: for $b > 0$, $\delta \in {}$, and a sequence of $n \in {\mathbb{N}}$ iid mean zero $b$-bounded scalar random variables $V_{1:n}$, In the moderate deviations bandwidth ($\delta \gtrsim {\exp{({- {{n\mathbf{E}V_{1}^{2}}/b^{2}}})}}$), the leading term of (1.1) is exactly of the expected order, seen from a central limit heuristic: $\sqrt{\frac{\mathbf{E}V_{1}^{2}{\ln{({1/\delta})}}}{n}}$. Assume now for sake of argument that $k \in {\mathbb{N}}$ divides $n$ and set $m = {n/k}$.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Contributions", "weight": 1.0} -->

Applying (1.1) instead to the $bk$-bounded variables ${{\overline{V}}_{i:m},{\overline{V}}_{i}} \triangleq {\sum_{j = {{ik} - k - 1}}^{ik}V_{j}}$ we find instead: The (normalized) variance of iid random variables tensorizes nicely (${k^{- 1}\mathbf{E}{({\overline{V}}_{1})}^{2}} = {\mathbf{E}V_{1}^{2}}$), and so the only difference between (1.1) and (1.2) is that the large deviations term has been inflated by a factor $k$. More generally, however, (1.2) remains valid as long as every $k$ samples are blockwise independent. The leading term of (1.2) already captures the correct variance term in the blockwise independent, one-dimensional and bounded setting.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Contributions", "weight": 1.0} -->

The above two paragraphs illustrate the core of our argument: by combining the above two observations we can entirely relegate any dependence on mixing to additive burn-in factors. In the sequel, we produce a more general version of this argument. To allow for arbitrary dimensions and handle unbounded processes, we first replace Bernstein's inequality with a corollary to Talagrand's inequality due to Einmahl and Li. To allow for $\beta$-mixing processes, we replace the blockwise independence assumption with the blocking strategy of Yu. By combining with control of the lower tail, which as noted above holds under mild assumptions, this leads to our main result Theorem 3.1, captured informally below.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Informal version of Theorem 3.1", "weight": 1.0} -->

Past a mild burn-, polynomial in relevant problem quantities including the $\beta$-mixing coefficients of the data, and for a fixed failure probability $\delta \in {}$, OLS with one-dimensional targets and $d_{\mathsf{X}}$-dimensional covariates enjoys the following excess risk guarantee: Moreover, the term $\sigma^{2}$ in (1.3) accurately captures the noise level of the problem solely via the relevant second order statistics; it is not inflated by any mixing times.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Informal version of Theorem 3.1", "weight": 1.0} -->

The crux of this result is that past a burn-, the OLS excess risk does not directly depend on mixing times, but only on the relevant second order statistics. Put differently, the effect of slow mixing has been relegated to a small additive term with higher order dependence on $1/n$. This stands in stark contrast to the usual invocation of the blocking technique where the effect of mixing typically enters *multiplicatively*, thereby degrading the rate of convergence uniformly across all sample-sizes and past any burn-in times.

<!-- chunk {"id": "body-0014", "role": "body", "section": "Applicability", "weight": 1.0} -->

Before we proceed with the main development, we remark that the class of $\beta$-mixing is quite broad; a few examples where Theorem 3.1 can be instantiated are as follows: all $\phi$-mixing processes are $\beta$-mixing, stationary uniformly ergodic Markov chains are $\beta$-mixing, stationary Gaussian vector autoregressive moving average (ARMA) processes are $\beta$-mixing, many other sub-classes of GARCH models, often studied in the economics and finance literature, are $\beta$-mixing.

<!-- chunk {"id": "body-0015", "role": "body", "section": "Applicability", "weight": 1.0} -->

The list is far from exhaustive and further examples can for instance be found in Doukhan. The stationarity assumptions above can also typically be dropped. We also point out that it is precisely because we can handle misspecification that our result is of interest for many of these examples.

<!-- chunk {"id": "body-0016", "role": "body", "section": "Outline", "weight": 1.0} -->

The rest of this article is structured as follows. Section 2 fixes our notation and yields a more formal problem formulation. We provide our main result, Theorem 3.1, in Section 3. After stating our main theorem, we highlight its features and then proceed to compare it to related work in Section 3.1. We outline the proof of Theorem 3.1 and provide supporting results in Section 4, including separate analyses of the noise-interaction and the lower tail of the empirical covariance matrix. Section 5 concludes and technical details are relegated to Appendix A.

<!-- chunk {"id": "body-0017", "role": "body", "section": "Problem Formulation", "weight": 1.0} -->

We are given $n$ input-output tuples: $X_{1:n} \sim \mathsf{P}_{1:n}^{X}$ (taking values in ${\mathbb{R}}^{d_{\mathsf{X}}}$) and $Y_{1:n} \sim \mathsf{P}_{1:n}^{Y}$ (taking values in ${\mathbb{R}}^{d_{\mathsf{Y}}}$). Using these samples, the goal of the learner is to estimate the best linear hypothesis: where the distributions of $X$ and $Y$ in (2.1) are specified via: Note that (2.2) is equivalent to sampling from the uniform mixture over $(X_{1:n},Y_{1:n})$ with the index $i \in {\lbrack n\rbrack}$ sampled uniformly.

<!-- chunk {"id": "body-0018", "role": "body", "section": "Problem Formulation", "weight": 1.0} -->

The operator $\Sigma_{X} \triangleq {\mathbf{E}{\lbrack{XX^{\mathsf{T}}}\rbrack}}$ is the averaged covariance operator (with $X$ as in (2.2)). The excess risk of a linear hypothesis $M$ can then be written as: We now define the *noise variable* $W_{i} \triangleq {Y_{i} - {M_{\star}X_{i}}}$ but, as mentioned above, do not impose any (conditional) mean zero assumptions on the noise. To simplify the exposition, we will henceforth assume that $\Sigma_{X} \succ 0$, but our results easily extend to the case $\Sigma_{X} \succeq 0$ by restricting attention to the span of $\Sigma_{X}$.

<!-- chunk {"id": "body-0019", "role": "body", "section": "Problem Formulation", "weight": 1.0} -->

With these preliminaries in place, on the event that the design is nondegenerate, the OLS and its error equation can be specified as follows: Our task in the sequel is to establish that the choice $\hat{M}$ renders the excess risk (2.3) small.

<!-- chunk {"id": "body-0020", "role": "body", "section": "The Noise Term", "weight": 1.0} -->

Let us also define the following prefiltered noise-class interaction variables: The square of the following (weighted and possibly biased) random walk effectively characterizes the noise level in our problem: We remark that by construction ${\mathbf{E}S_{n}} = 0$ using the optimality of $M_{\star}$ in (2.1). To see this, simply invoke the optimality equation for $M_{\star}$ and note that ${\mathbb{R}}^{d_{\mathsf{X}} \times d_{\mathsf{Y}}}$ induces a convex class in the corresponding $L^{2}$-space over the mixtures (2.2). Note however that the increments of (2.6) are not necessarily mean zero unless $X_{1:n}$ and $Y_{1:n}$ are stationary.

<!-- chunk {"id": "body-0021", "role": "body", "section": "The Noise Term", "weight": 1.0} -->

However, since ${\mathbf{E}S_{n}} = 0$, we also have with $\overline{V_{i}} \triangleq {V_{i} - {\mathbf{E}V_{i}}}$: In light of (2.4) and (2.6), we have that the empirical excess risk depends on the norm of: Hence, we need to control the random walk in (2.7) and the lower tail of the prefiltered empirical covariance matrix. As mentioned previously, lower uniform laws for (2.9) are valid under mild assumptions, and blocking such results does not incur more than a worsening of the burn-. Hence, the noise level of the problem is very much dictated by the random walk (2.6).

<!-- chunk {"id": "body-0022", "role": "body", "section": "$\\beta$-mixing and the Blocking Technique", "weight": 1.0} -->

In the sequel we demonstrate that the standard blocking device combined with a (functional) version of Bernstein's inequality allows us to pass the distributional (or coarse) measure of dependency to a higher order additive term, yielding non-asymptotic rates consistent with the CLT as described in Section 1. We will also use blocking to derive our lower uniform law, controlling the lower tail of (2.9). To make these ideas rigorous we require the following standard measure of dependence (take $Z_{1:n} = {(X,Y)}_{1:n}$ below).

<!-- chunk {"id": "body-0023", "role": "body", "section": "Main Result", "weight": 1.0} -->

To give our main result for general target dimension we require one last preliminary notion. Given a $d$-dimensional square, symmetric positive semidefinite matrix $M \in {\mathbb{R}}^{d \times d}$, we say that its *effective* dimension is ${{\mathsf{e}\mathsf{d}\mathsf{i}\mathsf{m}}{(M)}} \triangleq {{tr}{M/{\| M\|}_{\mathsf{o}\mathsf{p}}}}$. Our main result is the following theorem.

<!-- chunk {"id": "body-0024", "role": "body", "section": "Comparison to Related Work", "weight": 1.0} -->

Having established our main result, Theorem 3.1, we now provide a more detailed comparison to the relevant literature. Most closely related to our results is Nagaraj et al., who study bounded linear regression models in which the data comes from an exponentially ergodic Markov chain. They find that strictly realizable linear regression is no harder than its iid counterpart in this setting, and show that a parallelized gradient algorithm achieves the optimal rate. More interestingly, in the absence of realizability, they also establish a lower bound demonstrating that the worst-case (global minimax) excess risk across all Markov chains with a given mixing time is deflated by said mixing time, thereby establishing a gap between realizable and non-realizable learning from dependent data.

<!-- chunk {"id": "body-0025", "role": "body", "section": "Comparison to Related Work", "weight": 1.0} -->

Of course, their lower bound is no longer valid if one drops the requirement that the predictor performs uniformly well across all distributions with a prescribed mixing time. It is exactly herein that our analyses differ. While Nagaraj et al. characterize the worst-case (or global) complexity of linear regression, we focus on the instance-specific (or local) complexity. In other words, they compete against the worst distribution at a given level of mixing, whereas we compete against a fixed distribution. To appreciate this distinction, let us momentarily assume that $d_{\mathsf{X}} = d_{\mathsf{Y}} = 1$. The noise term $\sigma^{2}$ in Theorem 3.1 can be upper-bounded as: by the Cauchy-Schwarz inequality. The right hand side of (3.8) is precisely inflated by the (maximal) block-length $\max_{i \in {\lbrack{2m}\rbrack}}{|a_{i}|}$.

<!-- chunk {"id": "body-0026", "role": "body", "section": "Comparison to Related Work", "weight": 1.0} -->

Seen in this light, our results being sharper in terms of the measure of dependency reduces to stating that our results are sharper by an application of the Cauchy-Schwarz Inequality. Moreover, the statement that the global complexity is worse than its iid counterpart by a factor of the mixing time amounts in our setting to stating that there exists a distribution achieving equality in (3.8). We remark that such a distribution is easily constructed by taking $X_{1:n}$ and $Y_{1:n}$ to be constant within each block and stationary across the blocks; this is precisely when the application of the Cauchy-Schwarz inequality in (3.8) turns to equality. To further appreciate the distinction between our results, note that our result measures dependence through correlation. By contrast, a result scaling with the mixing time measures dependence in a stronger variational sense. That is, the former measures dependence at the level of orthogonality of the random variables themselves, whereas the latter measures it at the level of orthogonality of all measurable functions of these random variables.

<!-- chunk {"id": "body-0027", "role": "body", "section": "Further Related Work", "weight": 1.0} -->

Another closely related line of work studies parameter identification in auto-regressive models. When the noise model is strictly realizable---the variables $W_{1:n}$ form a martingale difference sequence with respect to the filtration generated by $X_{1:n}$---identification is possible at the iid rate even in the absence of mixing. Naturally, our results do not cover the mixing-free regime as we consider: the agnostic setting in which self-normalized martingale arguments are not available; and excess risk bounds instead of parameter identification---it seems unlikely that (3.2) holds without some notion of stochastic stability due to the presence of $\Sigma_{X}$ on the left hand side.

<!-- chunk {"id": "body-0028", "role": "body", "section": "Further Related Work", "weight": 1.0} -->

More generally---moving beyond linear time-series models---several authors have considered learning under various weak dependency notions. Kuznetsov and Mohri give generalization bounds in a more general setting using the same blocking technique---due to Yu ---used here. Statements similar in spirit can also be found in e.g., Steinwart and Christmann, Duchi et al. and most recently Roy et al.. However, they all suffer the dependency deflation discussed above and in our introduction (Section 1). We also note that Ziemann and Tu obtain rates for strictly realizable square loss that---similar to ours here---relegate mixing times into additive burn-in factors. While they treat more general hypothesis classes, they do not go beyond strict realizability, and their analysis rests on the assumption that the noise interaction term is a martingale difference sequence.

<!-- chunk {"id": "body-0029", "role": "body", "section": "Blocking", "weight": 1.0} -->

Recall that we partition $\lbrack n\rbrack$ into $2m$ consecutive intervals, denoted $a_{j}$ for $j \in {\lbrack{2m}\rbrack}$, so that ${\sum_{j = 1}^{2m}{|a_{j}|}} = n$. Denote further by $O$ (resp. by $E$) the union of the oddly (resp. evenly) indexed subsets of $\lbrack n\rbrack$. We further abuse notation by writing ${\beta_{Z}{(a_{i})}} = {\beta_{Z}{({|a_{i}|})}}$ in the sequel.

<!-- chunk {"id": "body-0030", "role": "body", "section": "Dependent Random Walks", "weight": 1.0} -->

Once equipped with Corollary 4.1). ‣ 4.1 Blocking ‣ 4 Proof Overview ‣ The noise level in linear regression with dependent data"), we still require control of the independent blocks. The following Fuk-Nagaev inequality due to Einmahl and Li provides such control.

<!-- chunk {"id": "body-0031", "role": "body", "section": "The Lower Tail of the Empirical Covariance Matrix", "weight": 1.0} -->

We now proceed to analyze the lower tail of the empirical covariance matrix (2.9).

<!-- chunk {"id": "body-0032", "role": "body", "section": "Summary", "weight": 1.0} -->

The leading order term of our main result, Theorem 3.1, does not directly depend on any mixing-time type quantities. It mimics the asymptotic rate and scales solely in terms of the second order statistics of the process at hand. To arrive at this result, we rely on two facts: The lower tail of the empirical covariance matrix (2.9) is well-behaved under mild assumptions. In an excess risk bound, the contribution of the lower uniform law to the overall error is not of leading order. Hence, incurring a sample size deflation for this purpose is not critical.

<!-- chunk {"id": "body-0033", "role": "body", "section": "Summary", "weight": 1.0} -->

By combining blocking with a version of Bernstein's inequality, we are able to push the effect of blocking to only affect the large deviations regime. In the moderate and small deviations regimes, control of the leading order of the random walk in (2.7) is not directly impacted by slow mixing.
