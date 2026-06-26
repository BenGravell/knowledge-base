<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Shape-Constrained Regression Using Sum of Squares Polynomials

Topics include Shape-constrained regression, Sum of squares, Semidefinite programming, Convex regression, Monotone regression, Polynomial regression, Statistical consistency, Optimal transport.

<!-- chunk {"id": "summary-0002", "role": "summary", "section": "Summary", "weight": 2.0} -->

Builds an SDP hierarchy for fitting multivariate polynomial regressors subject to shape constraints such as convexity and monotonicity on a box. Beyond the estimator, the paper proves SOS density results for convex and monotone polynomials and clarifies when polynomial shape-constrained regression becomes computationally hard.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

We present a hierarchy of semidefinite programs (SDPs) for the problem of fitting a shape-constrained (multivariate) polynomial to noisy evaluations of an unknown shape-constrained function. These shape constraints include convexity or monotonicity over a box. We show that polynomial functions that are optimal to any fixed level of our hierarchy form a consistent estimator of the underlying shape-constrained function. As a byproduct of the proof, we establish that sum-of-squares-convex polynomials are dense in the set of polynomials that are convex over an arbitrary box. A similar sum of squares type density result is established for monotone polynomials. In addition, we classify the complexity of convex and monotone polynomial regression as a function of the degree of the polynomial regressor. While our results show NP-hardness of these problems for degree three or larger, we can check numerically that our SDP-based regressors often achieve similar training error at low levels of the hierarchy.

<!-- chunk {"id": "abstract-0004", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Finally, on the computational side, we present an empirical comparison of our SDP-based convex regressors with the convex least squares estimator introduced in [Hildreth, 1954] and [Holloway, 1979] and show that our regressor is valuable in settings where the number of data points is large and the dimension is relatively small. We demonstrate the performance of our regressor for the problem of computing optimal transport maps in a color transfer task and that of estimating the optimal value function of a conic program. A real-time application of the latter problem to inventory management contract negotiation is presented.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

Shape-constrained regression is a fundamental problem in statistics and machine learning. It posits the existence of a shape-constrained function $f$ that maps *feature vectors* to *response variables*. Its goal is to obtain an *estimator* (or *regressor*) of this function, with the same shape constraints, from noisy feature vector-response variable pairings. The shape constraints we consider are of two types here: convexity constraints over a box and $K$-bounded-derivative constraints over a box, as defined in Section 2 ‣ Shape-Constrained Regression using Sum of Squares Polynomials"). Bounded-derivative constraints include as subcases both the case where the regressor is constrained to be monotone and the case where it is constrained to be Lipschitz-continuous with a fixed Lipschitz constant. Combined, these shape constraints cover the wide majority of shape constraints arising in applications. A short and non-exhaustive list of areas where regression with shape constraints such as these appear include economics, psychology, engineering, and medicine.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

In this paper, we study a set of shape-constrained (multivariate) polynomial regressors, the Sum of Squares Estimators (SOSEs), which are obtained via a semidefinite programming hierarchy. They are parametric in $d$, their degree, and $r$, the level of the hierarchy (see Section 2.1 ‣ Shape-Constrained Regression using Sum of Squares Polynomials")). While we are not the first paper to consider shape-constrained polynomials of this type, we are the first to propose a systematic analysis of estimators defined in this way, from a variety of angles. More specifically, our contributions are the following: We showcase a regime in which the SOSEs are competitive in terms of computation time. This corresponds to the setting where the number of data points is large, the dimension is relatively small, and predictions need to be made often and quickly.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

Within this regime, we provide experimental evidence that the SOSEs outperform, in terms of generalization error, two alternative shape-constrained regressors, the Convex Least-Squares Estimator or CLSE and the Maximum-Affine Estimator or MAE, which are among the most prevalent convex regressors; see Section 2 ‣ Shape-Constrained Regression using Sum of Squares Polynomials").

<!-- chunk {"id": "body-0008", "role": "body", "section": "Introduction", "weight": 1.5} -->

We show that, for fixed $r$, the SOSEs are consistent estimators of the underlying shape-constrained function. In doing so, we prove that sos-convex polynomials (see Section 3.1 for a definition) are dense in the set of polynomials convex over a box. We also show that a similar result holds for monotonicity. These results can be viewed as analogs of sum of squares density results for nonnegative polynomials in for convex and monotone polynomials, and may be of independent interest; see Section 3.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Introduction", "weight": 1.5} -->

We compare the SOSEs against their limits as $r\rightarrow\infty$: these limits correspond to the solutions to convex and $K$-bounded-derivative polynomial regression. We provide a complete characterization of the complexity of solving these problems as a function of the degree $d$ of the regressor. Our results show NP-hardness for degree three or larger. We also propose a convex optimization-based method for bounding the gap between the optimal value of shape-constrained polynomial regression problems and that of the SOSE training problem (for fixed $r$). Our numerical experiments show that the gap is very small already for small values of $r$; see Section 4.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Introduction", "weight": 1.5} -->

We propose three applications which correspond to settings where the SOSEs perform particularly well. The first application is well known and involves fitting a production function to data in economics. Our main contribution here is to show that we outperform the prevalent approach in economics, which uses Cobb-Douglas functions. The second application is to the problem of computing optimal transport maps, and more specifically the problem of color transfer. While using shape-constrained regression to compute optimal maps is not new, we are the first to tackle it using sum of squares-based methods. This is intriguing as the approach adopted, which relies on a variant of the CLSE, is not as well-suited to color transfer as the SOSEs are. Our third application is, to the best of our knowledge, an entirely novel use of shape-constrained regression. It involves estimating the optimal value function of a conic program. We present a real-time application of this problem to inventory management contract negotiation; see Section 5.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Introduction", "weight": 1.5} -->

The sum of squares techniques we present in this paper have the advantage, unlike other techniques, of being very modular: they can handle with ease a wide variety of shape constraints, including convexity, monotonicity, Lipschitz continuity, or any combinations of these, globally or over regions. They also produce explicit algebraic certificates enabling users to independently verify that the regressors obtained possess the shape constraints of interest. This can help with interpretability and enhance user trust. Through this paper, we hope to encourage a broader use of these techniques for shape-constrained regression, particularly in settings, such as color transfer, for which they are well-suited.

<!-- chunk {"id": "body-0012", "role": "body", "section": "The Sum of Squares Estimators (SOSEs)", "weight": 1.0} -->

We define the SOSEs in Section 2.1 ‣ Shape-Constrained Regression using Sum of Squares Polynomials"), investigate their computation time and performance in Section 2.2 ‣ Shape-Constrained Regression using Sum of Squares Polynomials"), and compare them against two other estimators in Section 2.3 ‣ Shape-Constrained Regression using Sum of Squares Polynomials").

<!-- chunk {"id": "body-0013", "role": "body", "section": "Computing the SOSEs and Dependence on Input Parameters", "weight": 1.0} -->

It is well known that testing membership to $\Sigma_{n,{2d}}$ can be reduced to a semidefinite program (SDP). Indeed, a polynomial $p{(x_{1},\ldots,x_{n})}$ of degree $2d$ is sos if and only if there exists a positive semidefinite matrix $Q$ (we write $Q \succeq 0$) of size ${\mathbb{R}}^{{(\binom{n + d}{d})} \times {(\binom{n + d}{d})}}$ such that ${p{(x)}} = {z{(x)}^{T}Qz{(x)}}$, where ${z{(x)}} = {(1,x_{1},\ldots,x_{n},\ldots,x_{n}^{d})}^{T}$ is the vector of all monomials of degree at most $d$.

<!-- chunk {"id": "body-0014", "role": "body", "section": "Computing the SOSEs and Dependence on Input Parameters", "weight": 1.0} -->

Thus, computing the SOSEs amounts to solving SDPs. Of interest to us is how the size of the SDPs scales with ${m,n,d},$ and $r$. For both (3 ‣ Shape-Constrained Regression using Sum of Squares Polynomials")) and (4 ‣ Shape-Constrained Regression using Sum of Squares Polynomials")), the data points only appear in the objective: thus, the size of the SDPs is independent of the number $m$ of data points. Their size does depend however on ${n,d},$ and $r$.

<!-- chunk {"id": "body-0015", "role": "body", "section": "Computing the SOSEs and Dependence on Input Parameters", "weight": 1.0} -->

For (3 ‣ Shape-Constrained Regression using Sum of Squares Polynomials")), the number of equality constraints is equal to $\binom{n + 2}{2} \cdot \binom{n + {\max{\{{2r},{d - 2}\}}}}{\max{\{{2r},{d - 2}\}}}$ and the size of the $n + 1$ semidefinite constraints is ${{n \cdot \binom{n + r}{r}} \times n} \cdot \binom{n + r}{r}$.

<!-- chunk {"id": "body-0016", "role": "body", "section": "Computing the SOSEs and Dependence on Input Parameters", "weight": 1.0} -->

For (4 ‣ Shape-Constrained Regression using Sum of Squares Polynomials")), the number of equality constraints is equal to ${2n} \cdot \binom{n + {\max{\{{d - 1},{2r}\}}}}{\max{\{{d - 1},{2r}\}}}$ and the size of the ${2n} + 2$ semidefinite constraints is $\binom{n + r}{r} \times \binom{n + r}{r}$.

<!-- chunk {"id": "body-0017", "role": "body", "section": "Computing the SOSEs and Dependence on Input Parameters", "weight": 1.0} -->

Bearing in mind that $\binom{n + k}{k} = \binom{n + k}{n}$ and that $\binom{n + k}{k} = {O{({({n + k})}^{k})}}$, we get that, for fixed $n$, the sizes of (3 ‣ Shape-Constrained Regression using Sum of Squares Polynomials")) and (4 ‣ Shape-Constrained Regression using Sum of Squares Polynomials")) grow polynomially in $d$ and $r$, and that for fixed $d$ and $r$, the sizes of (3 ‣ Shape-Constrained Regression using Sum of Squares Polynomials")) and (4 ‣ Shape-Constrained Regression using Sum of Squares Polynomials")) grow polynomially in $n$.

<!-- chunk {"id": "body-0018", "role": "body", "section": "Computing the SOSEs and Dependence on Input Parameters", "weight": 1.0} -->

Even though the size of the SDPs scales polynomially with the parameters of interest, in practice, SDPs can suffer from scalability issues. Thus, computing the SOSEs is generally faster when $n,d,r$ are small, though $m$ can be taken as large as needed, as the size of the SDPs is independent of $m$. In practice, $m$ and $n$ are fixed as artifacts of the application under consideration. The parameters $r$ and $d$ however are fixed by the user. They should be chosen using a statistical model validation technique, such as cross validation, to ensure that generalization error is low on the test data. As an example, we experimentally investigate the impact of the choice of $r$ and $d$ on the generalization error for estimating the function We plot the results in Figure 1 ‣ Shape-Constrained Regression using Sum of Squares Polynomials"). To obtain these plots, we use datasets generated as explained in Appendix A.1 with $m = {10,000}$.

<!-- chunk {"id": "body-0019", "role": "body", "section": "Computing the SOSEs and Dependence on Input Parameters", "weight": 1.0} -->

An analogous plot with a different function $f_{2}$ is given in Appendix A.2. We vary the values of $n,d,r$ as indicated in Figure 1 ‣ Shape-Constrained Regression using Sum of Squares Polynomials"). The train RMSE (resp. test RMSE) are concepts formally defined in Appendix A.1. Roughly speaking, the lower they are, the closer the values obtained by evaluating the SOSEs on the training (resp. testing) feature vectors are to the training (resp. testing) response variables. Figure 1 ‣ Shape-Constrained Regression using Sum of Squares Polynomials") indicates that low values of $d$ and $r$ often lead to better test RMSE (i.e., generalization error) than larger $d,r$. In fact, low $d$ and $r$ seem to have a regularization effect.

<!-- chunk {"id": "body-0020", "role": "body", "section": "Computing the SOSEs and Dependence on Input Parameters", "weight": 1.0} -->

As well as being fast to compute when $m$ is large and $n$ is small, evaluating the SOSEs on a new feature vector is also fast to do as it simply amounts to evaluating a polynomial at a point. Thus, the SOSEs should be favored in applications where $m$ is large, $n$ is small, and predictions need to be made often and quickly (see Section 5 for examples). In the next subsection, we give experimental evidence that the SOSEs tend to have low generalization error when compared to other prominent methods for convex regression. In the section that follows, we show favorable theoretical properties of the SOSEs, namely that they are consistent statistical estimators even when $r$ is fixed.

<!-- chunk {"id": "body-0021", "role": "body", "section": "Comparison of the SOSEs Against Other Estimators", "weight": 1.0} -->

Many methods exist for shape-constrained regression, in particular for convex regression (see, e.g., and the references within for a comprehensive literature review). We restrict ourselves to two here, the Convex Least Squares Estimator (CLSE) as, and the Max-Affine Estimator (MAE), as, e.g.,.

<!-- chunk {"id": "body-0022", "role": "body", "section": "Comparison of the SOSEs Against Other Estimators", "weight": 1.0} -->

{1,\ldots,m}}$ are not, and consequently, defining ${\hat{g}}_{m}$ via (6 ‣ Shape-Constrained Regression using Sum of Squares Polynomials")) is needed.) The MAE is a convex piecewise-affine estimator as well, but parametric with parameter the number of pieces, $k$.

<!-- chunk {"id": "body-0023", "role": "body", "section": "Comparison of the SOSEs Against Other Estimators", "weight": 1.0} -->

We restrict ourselves to the CLSE for three reasons. First, it is arguably the most prevalent shape-constrained regressor in the literature. Second, the computation time for many popular alternative regressors (e.g., based on isotonic regression, lattice methods, etc.) grows exponentially in the number $n$ of features and we wish to compare the SOSE against methods which, just like the SOSE with any fixed $d,r$, are polynomial in $n$. Finally, like the SOSE, the CLSE can be obtained by solving a convex program. We also consider the MAE, though it does not fit these criteria, as it can be viewed as a parametric version of the CLSE and the SOSE is also parametric. A downside in our opinion for both the CLSE and the MAE relates to the limited type of constraints that can be required. For example, as the CLSE and MAE are globally convex by definition, we cannot require that they be monotonous only, or convex only over a region, which some applications may call.

<!-- chunk {"id": "body-0024", "role": "body", "section": "Comparison of the SOSEs Against Other Estimators", "weight": 1.0} -->

As they are piecewise-affine, we cannot require either that they be strongly convex, as needed, e.g., in the optimal transport application of Section 5.3. Extensions to incorporate $\ell$-strong convexity do exist \[53, Theorems 3.8, 3.14\], but we would argue that they are not very straightforward to derive, contrarily to the SOSE where we would simply replace $H_{g}{(x)}$ in (3 ‣ Shape-Constrained Regression using Sum of Squares Polynomials")) by ${H_{g}{(x)}} - {\ellI}$, where $I$ is the $n \times n$ identity matrix.

<!-- chunk {"id": "body-0025", "role": "body", "section": "Comparison of the SOSEs Against Other Estimators", "weight": 1.0} -->

In terms of computation, the SOSE and the CLSE can be viewed as methods best-suited to complementary settings. While the SOSE is quicker to compute when $n$ is small and $m$ is large, the CLSE is quicker to compute when $n$ is large and $m$ is small. Indeed, the QP in (5 ‣ Shape-Constrained Regression using Sum of Squares Polynomials")) has a number of variables that scales linearly and a number of constraints that scales quadratically with the number $m$ of data points (unlike the SDP whose size does not scale with $m$). This can be expected as the CLSE is non-parametric, while the SOSEs are not. We illustrate the differences in solving time in Figure 2 ‣ Shape-Constrained Regression using Sum of Squares Polynomials") (implementation details can be found in Appendix A.1). The SOSE is much faster to compute in settings where the number of data points is moderate to large; see Figure 2 ‣ Shape-Constrained Regression using Sum of Squares Polynomials").

<!-- chunk {"id": "body-0026", "role": "body", "section": "Comparison of the SOSEs Against Other Estimators", "weight": 1.0} -->

In fact, for most of the QPs solved for these values of $m$, the 4-hour time-out that we put into place was reached. Evaluation of the CLSE, when it is defined as above, can also be quite slow, as it requires solving a linear program whose size scales with $m$ (see (6 ‣ Shape-Constrained Regression using Sum of Squares Polynomials")) and, e.g., ). When solving this linear program, one can encounter issues of infeasibility if the quadratic program is not solved to high accuracy. One can also encounter unboundedness issues if asked for a prediction on a point which does not belong to the convex hull of the training points. This is not the case for the SOSEs, though we point out that our statistical guarantees from Section 3 only apply to points in the convex hull of the training points. Typical heuristics for computing the MAE run much faster than the CLSE, as their solving time does not scale with $m$. They also are faster to compute than the SOSEs as they involve solving cheaper convex optimization problems.

<!-- chunk {"id": "body-0027", "role": "body", "section": "Comparison of the SOSEs Against Other Estimators", "weight": 1.0} -->

Similarly, evaluation of the MAE is very fast, as it only requires evaluating $k$ affine functions and taking the maximum of the $k$ evaluations, which is comparable to the SOSEs. However, as the MAE is a solution to a non-convex optimization problem, this opens the door to a series of complications which are not encountered with the SOSEs such as choosing an appropriate heuristic or initializing in an appropriate manner.

<!-- chunk {"id": "body-0028", "role": "body", "section": "Comparison of the SOSEs Against Other Estimators", "weight": 1.0} -->

In terms of quality of prediction, we compare the SOSEs against the MAE and the CLSE in the regime where we advocate for the SOSE, namely $m$ large and $n$ smaller. The train and test RMSEs are given in Table 1 ‣ Shape-Constrained Regression using Sum of Squares Polynomials"). They are obtained using a dataset generated as explained in Appendix A.1 with $f = f_{1}$, $r = 1$ for the SOSEs, and varying $m,n,d,k$. The differences between Spect Opt, Rand Opt, and Rand are also explained in Appendix A.1; at a high level, they correspond to different initialization techniques for the MAE. The best results in terms of test RMSE are indicated in bold: these are always obtained by the SOSE. This happens even when we select the best performing hyperparameters for the MAE. We provide a similar table with $f = f_{2}$ in Appendix A.2.

<!-- chunk {"id": "body-0029", "role": "body", "section": "Comparison of the SOSEs Against Other Estimators", "weight": 1.0} -->

(a) Solver time of for different n, d, r, using m = 10, 000 training samples. The dashed blue line corresponds to the solver time for the CLSE QP.

<!-- chunk {"id": "body-0030", "role": "body", "section": "Comparison of the SOSEs Against Other Estimators", "weight": 1.0} -->

(b) Solver time needed to compute the CLSE and the SOSE in with respect to n. For the SOSE, we take r = 2 and a range of degrees d. Lighter colors correspond to fewer training points. All run-times capped at 4 hours per setup.

<!-- chunk {"id": "body-0031", "role": "body", "section": "Sum of Squares Approximations and Consistency of the SOSEs", "weight": 1.0} -->

In Section 3.1, we present two key results of the paper. While they are used as stepping stones towards our consistency results (Section 3.3), they may be of independent interest to the polynomial or algebraic optimization community as analogs of results in for convex/monotone polynomials (Section 3.2).

<!-- chunk {"id": "body-0032", "role": "body", "section": "Two Algebraic Approximation Results", "weight": 1.0} -->

We refer to a polynomial $p$ whose Hessian $H_{p}$ is an sos matrix as *sos-convex* (see, e.g., ) to a polynomial $p$ whose partial derivatives satisfy $K_{i}^{+} - \frac{\partial p}{\partial x_{i}}$ is sos for $i \in I^{+}$ and $\frac{\partial p}{\partial x_{i}} - K_{i}^{-}$ is sos for $i \in I^{-}$ as having *sos-$K$-bounded derivatives.* In the remainder of the paper, we assume that ${I^{+} \cap I^{-}} = \varnothing$. We show that any polynomial that is convex (resp. that has $K$-bounded derivatives) over ${\lbrack{- 1},1\rbrack}^{n}$ can be closely approximated by an sos-convex polynomial (resp.

<!-- chunk {"id": "body-0033", "role": "body", "section": "Two Algebraic Approximation Results", "weight": 1.0} -->

sos-$K$-bounded derivative polynomial), obtained by slightly perturbing its higher order terms.

<!-- chunk {"id": "body-0034", "role": "body", "section": "Implications of the Approximation Results Beyond Shape-Constrained Regression", "weight": 1.0} -->

Theorems 3.1 and 3.2 may be of broader interest when reinterpreted as algebraic density results over the set of convex and monotone polynomials.

<!-- chunk {"id": "body-0035", "role": "body", "section": "Consistency of the SOSEs", "weight": 1.0} -->

In this section, we make three statistical assumptions on the way ${(X_{i},Y_{i})}_{i = {1,\ldots,m}}$ are generated, which are standard for consistency results.

<!-- chunk {"id": "body-0036", "role": "body", "section": "Assumption 2", "weight": 1.0} -->

The support of the random vectors $X_{1}$, $\ldots$, $X_{m}$ is a full-dimensional box $B \subseteq {\mathbb{R}}^{n}$ as in (1 ‣ Shape-Constrained Regression using Sum of Squares Polynomials")), i.e., ${P{({X_{i} \in B})}} = 1$. Furthermore, for any full-dimensional set $C \subseteq B$, ${P{({X_{i} \in C})}} > 0$.

<!-- chunk {"id": "body-0037", "role": "body", "section": "Assumption 3", "weight": 1.0} -->

There exists a continuous function $f:{B\rightarrow{\mathbb{R}}}$ such that $Y_{i} = {{f{(X_{i})}} + \nu_{i}}$ for all ${i = {1,\ldots,m}},$ where $\nu_{i}$ are random variables with support $\mathbb{R}$ and the following characteristics: Assumptions 1 and 3 imply that the sequence ${\{{(X_{i},Y_{i})}\}}_{i = {1,\ldots,m}}$ is iid, that ${E{\lbrack\nu_{1}\rbrack}} = 0$, and that ${E{\lbrack Y_{1}^{2}\rbrack}} < \infty$. Using these three assumptions, we show *consistency* of the SOSEs. This is a key property of estimators stating that, as the number of observations grows, we are able to recover $f$.

<!-- chunk {"id": "body-0038", "role": "body", "section": "Remark 3.1", "weight": 1.0} -->

Under our assumptions, $d$ and $m$ need to go to infinity for consistency to hold and it is quite clear that these assumptions cannot be dropped. (The same assumptions are needed to show consistency of, e.g., unconstrained polynomial regression.) If we allow $r\rightarrow\infty$, it is easier to show consistency, as we are then able to leverage certain Positivstellensätze. As $r$ is fixed in Theorems 3.9 and 3.10, we do not make use of such results here. Note that one can fix $r$ to any value, including $r = 0$, and still obtain consistency as long as ${m,d}\rightarrow\infty$. In practice, we choose $d$ and $r$ via cross-validation (see Section 2.2 ‣ Shape-Constrained Regression using Sum of Squares Polynomials")) as it is not clear that $r = 0$ is preferable to larger $r$ in terms of generalization error.

<!-- chunk {"id": "body-0039", "role": "body", "section": "Remark 3.2", "weight": 1.0} -->

One could extend these theorems to the box $B$ itself, provided that we make assumptions on the sampling of the pairs of points ${(X_{i},Y_{i})}_{i = {1,\ldots,m}}$ on the boundary of $B$.

<!-- chunk {"id": "body-0040", "role": "body", "section": "Remark 3.2", "weight": 1.0} -->

Theorems 3.9 and 3.10 rely on three propositions and require the introduction of two sets of polynomials $g_{d}$, $h_{d}$ and ${\overline{g}}_{m,d}$, ${\overline{h}}_{m,d}$. Let $C_{n,d}$ (resp. $K_{n,d}$) be the set of $n$-variate polynomials of degree $d$ that are convex (resp. have $K$-bounded derivatives) on $B$.

<!-- chunk {"id": "body-0041", "role": "body", "section": "Connection to Training-Optimal Shape-Constrained Polynomial Regressors", "weight": 1.0} -->

The first notable difference between the SOSEs and their limits relates to their computation. As seen in Section 2.2 ‣ Shape-Constrained Regression using Sum of Squares Polynomials"), ${\overset{\sim}{g}}_{m,d,r}$ and ${\overset{\sim}{h}}_{m,d,r}$ can be obtained for any fixed $r$ by solving an SDP. By contrast, ${\overline{g}}_{m,d}$ and ${\overline{h}}_{m,d}$, however, are NP-hard to compute in general, as we prove next. More specifically, we provide a complete classification of the complexity of computing ${\overline{g}}_{m,d}$ and ${\overline{h}}_{m,d}$ based on their degree $d$.

<!-- chunk {"id": "body-0042", "role": "body", "section": "Connection to Training-Optimal Shape-Constrained Polynomial Regressors", "weight": 1.0} -->

We work in the standard Turing model of computation (see, e.g., ), where the input to the problem $({{{\{ X_{i},Y_{i}\}}_{i = {1,\ldots,m}},B} \subset {\mathbb{R}}^{n}})$ is described by rational numbers.

<!-- chunk {"id": "body-0043", "role": "body", "section": "Applications of Shape-Constrained Regression to Economics, Real-Time Optimization, and Optimal Transport", "weight": 1.0} -->

In this section, we present three applications of the SOSEs. The first is fitting a production function to data (Section 5.1). It is a well-known application of shape-constrained regression in economics and we show that it outperforms the prevalent approach there. The second is predicting the optimal value of a conic program and is, to the best of our knowledge, novel (Section 5.2). The third is in optimal transport, more specifically color transfer (Section 5.3), and has not been tackled using sum of squares methodology previously, despite it being a very relevant setting for the SOSEs.

<!-- chunk {"id": "body-0044", "role": "body", "section": "Fitting a Production Function to Data", "weight": 1.0} -->

The goal of this application is to estimate the functional relationship between the yearly inputs of Capital ($K$), Labor ($L$), and Intermediate goods ($I$) to an industry, and the yearly gross-output production $Out$ of that industry. As $Out$ is assumed to be a decreasing function in ${K,L},$ and $I$, as well as concave in $K$, $L,$ and $I$ by virtue of diminishing returns, an estimator constrained to have this shape is desirable. Traditionally, in the economics literature, this is done by fitting a *Cobb-Douglas production function* to the data, i.e., finding $(a,b,c,d)$ such that the function ${Out} = {a \cdot K^{b} \cdot L^{c} \cdot I^{d}}$ is as close as possible to the observed data.

<!-- chunk {"id": "body-0045", "role": "body", "section": "Fitting a Production Function to Data", "weight": 1.0} -->

The advantage of such an approach is that it can be couched as a linear regression problem by working in log-space, with the shape constraints being imposed via the constraints ${b,c,d} \geq 0$, ${b + c + d} \leq 1$ and $a \geq 0$. We compare the SOSE to the Cobb-Douglas estimator. To fit the estimators, we consider the USA KLEMS data, which contains yearly gross-output production data $Out$ for 65 industries in the US, from 1947 to 2014 as well as yearly inputs of Capital $K$, Labor $L$, and Intermediate goods $I$, adjusted for inflation. Since the data is temporal, we perform a temporal split for our training-testing splits. We then fit the Cobb-Douglas estimator and the SOSE with degree $d = 4$ and $r = 2$ and the aforementioned shape constraints to the data. The results obtained are given in Figure 3. As can be seen, our method outperforms the traditional Cobb-Douglas technique on 50 out of the 65 industries, sometimes quite significantly.

<!-- chunk {"id": "body-0046", "role": "body", "section": "Shape-Constrained Optimal Transport Maps and Color Transfer", "weight": 1.0} -->

An *optimal transport map* is a function that maps one probability measure to another while incurring minimum cost. In many applications, it is of interest to determine an optimal transport map given two measures and a cost function. Interestingly, the problem of computing an optimal transport map can be related back to shape-constrained regression, as optimal transport maps are known to have specific shapes when the cost function under consideration or the measures they are defined over have certain properties. For example, if the cost function is the $l_{2}$-norm and one of the measures is continuous with respect to the Lebesgue measure, the Brenier theorem states that the optimal transport map is uniquely defined as the gradient of a convex function. Following, rather than observing these properties of the map a posteriori, we use these shape constraints as regularizers when computing the optimal transport maps. This gives rise to shape-constrained regression problems. To solve these, propose an approach that can be viewed as a CLSE-based approach. We propose to use instead the SOSE, which we show is particularly well-suited to this application.

<!-- chunk {"id": "body-0047", "role": "body", "section": "Shape-Constrained Optimal Transport Maps and Color Transfer", "weight": 1.0} -->

To better illustrate our method, we focus on the concrete application of *color transfer*, though our methodology is applicable more widely to, e.g., the other applications mentioned in and voice transfer. The color transfer problem is defined by two images, the *input image* and the *target image*. The goal is to transfer the colors of the target image to the input image, thereby creating a third image, the *output image*; see Figure 4. We now describe how the color transfer problem can be reformulated as a sequence of shape-constrained regression problems, following.

<!-- chunk {"id": "body-0048", "role": "body", "section": "Shape-Constrained Optimal Transport Maps and Color Transfer", "weight": 1.0} -->

${{y_{j} \in {\lbrack 0,1\rbrack}^{3}},{j = {1,\ldots,\overset{\sim}{M}}}},$) to be the distinct color triples in the input (resp. target) image, with $\overset{\sim}{N}$ (resp. $\overset{\sim}{M}$) being less than or equal to the number of pixels in the input (resp. target) image, and $a_{i}$ (resp. $b_{j}$) to be the ratio of number of pixels of color $x_{i}$ (resp. $y_{j}$) to the total number of pixels.

<!-- chunk {"id": "body-0049", "role": "body", "section": "Shape-Constrained Optimal Transport Maps and Color Transfer", "weight": 1.0} -->

The idea is then to search for a function $f^{\ast}:{{\lbrack 0,1\rbrack}^{3}\rightarrow{\mathbb{R}}}$ that minimizes the 2-Wasserstein distance between the push-forward of $\mu$ under $\nabla f^{\ast}$ and $\nu$, under certain shape constraints.

<!-- chunk {"id": "body-0050", "role": "body", "section": "Shape-Constrained Optimal Transport Maps and Color Transfer", "weight": 1.0} -->

Similarly, a function $f:{{\mathbb{R}}^{n}\mapsto{\mathbb{R}}}$ is $\ell$-strongly convex over $B$ if ${H_{f}{(x)}} \succeq {\ellI}$, for all $x \in B$.) We derive from the optimal solution $f^{\ast}$ to, the optimal transport map (or color transfer map) ${{\nabla f^{\ast}}:{{\lbrack 0,1\rbrack}^{3}\rightarrow{\lbrack 0,1\rbrack}^{3}}}.$ To obtain the output image, we simply apply $\nabla f^{\ast}$ to the RGB triple of each pixel in the input image to obtain a new RGB triple (i.e., the new color of the pixel) for that pixel. In this context, smaller $L$ gives rise to more uniform colors whereas larger $\ell$ increases the contrast; see Figure 7.

<!-- chunk {"id": "body-0051", "role": "body", "section": "Shape-Constrained Optimal Transport Maps and Color Transfer", "weight": 1.0} -->

In its current form however, problem is not quite a shape-constrained regression problem of the type (3 ‣ Shape-Constrained Regression using Sum of Squares Polynomials")) or (4 ‣ Shape-Constrained Regression using Sum of Squares Polynomials")). This is due to the matrix variable $P$ which makes the problem non-convex. To circumvent this issue, we use alternate minimization: we fix $f$ and solve for $P$ using, e.g., Sinkhorn's algorithm (see). We then fix $P$ and solve for $f$. If we parametrize $f$ as a polynomial (with $P$ fixed), we obtain a shape-constrained polynomial regression problem: | | | s.t.

<!-- chunk {"id": "body-0052", "role": "body", "section": "Shape-Constrained Optimal Transport Maps and Color Transfer", "weight": 1.0} -->

| | ${{{\ell \cdot I} \preceq {H_{f}{(x)}} \leq {L \cdot I}},{{\forall x} \in {\lbrack 0,1\rbrack}^{3}}},$ | | | which we solve using the sos techniques from Section 2 ‣ Shape-Constrained Regression using Sum of Squares Polynomials"). We iterate this process until convergence.

<!-- chunk {"id": "body-0053", "role": "body", "section": "Shape-Constrained Optimal Transport Maps and Color Transfer", "weight": 1.0} -->

An example of the output images obtained via this process is given in Figure 4. Additional illustrations can be found in Figure 7 for different values of $l$ and $L$ with $d = 4$ and $r = 3$. The color transfer application works particularly well for the SOSE as the number of features is small (equal to 3), the number of data points is very large, as it corresponds to the number of pixels in the images, and as a large number of new predictions need to be made (one per pixel of the input image). In contrast, the CLSE approach considered in requires the authors to segment the images via k-means clustering to limit computation time. Pre-processing of this type can lead to undesirable artifacts in the output image and grainy texture, which our method avoids.
