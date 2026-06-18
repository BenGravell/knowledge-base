<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Fragility Analysis of Data-Driven Feedback Gains

Topics include Data-driven control, Feedback fragility, Robust control, Stabilization, Noisy data, Linear matrix inequalities, Semidefinite programming, Data informativity.

<!-- chunk {"id": "summary-0002", "role": "summary", "section": "Summary", "weight": 2.0} -->

Studies how stabilizing feedback gains designed from data react to perturbations in the gain itself. The paper extends direct data-driven stabilization from feasibility toward robustness diagnostics, fragility quantification, and least-fragile gain design.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

For linear time-invariant systems, input-state data collected during an open-loop experiment can remedy the lack of knowledge of system parameters. However, such data do not contain information about other system uncertainties such as feedback perturbations. In this paper, we study the effect of additive perturbations on control parameters in a data-based setting. To this end, we parameterize the set of quadratically stabilizing feedback gains obtained from noisy input-state data. We study the case where a stabilizing data-driven feedback gain is extremely sensitive to feedback perturbations, i.e., a small perturbation in the control parameters, no matter how small, could destabilize the unknown true system. We refer to this case as extreme fragility for which we provide a full characterization. We also present necessary and sufficient conditions for the case where the closed-loop system is completely immune to feedback perturbations. For the general case where the feedback gain is neither extremely fragile nor immune, we provide a measure by which one can quantize the control fragility directly based on the collected data. We also study the problem of designing the least fragile data-driven feedback gain.

<!-- chunk {"id": "abstract-0004", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

The results are presented either in closed-form, or in terms of linear matrix inequalities and semi-definite programs.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

Data-driven stabilization aims at designing a feedback law directly based on data collected from an *unknown system*, bypassing a system identification process (see \[4, Ch. 1.2\] for a historical background). Under suitable conditions on the data, such feedback laws can be obtained, and if implemented *exactly* as designed, they stabilize the unknown system. Nevertheless, data collected in an open-loop scenario do not contain information about perturbations arising from the feedback loop. As a result, a data-driven feedback that is unaware of such perturbations might be *fragile*. In this work, we study data-driven stabilization in the presence of perturbations on the controller parameters and the extent to which the stability of the unknown system is immune to such perturbations.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

From design to real-world implementation, a feedback gain might undergo various perturbations due to, e.g., truncation errors in the numerical computations, limited word-length implementation, conversions from analog to digital and vice versa, and instrumental precision. Some feedback perturbations caused, e.g., faults in the sensors and actuators, can also be modeled by perturbations on the feedback gain. In addition, it is appealing for a designed feedback to provide room for future adjustments caused by a change in the design objectives. Hence, it is important to design a feedback that is not extremely sensitive to variations in the control parameters, and to that end, it is useful to know the tolerance towards feedback perturbations.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

The problem of fragile controllers was raised in the paper by Keel and Bhattacharyya (see also and the references therein). They showed that a feedback gain obtained through $H_{\infty}$, $H_{2}$, $l_{1}$, or $\mu$ formulations can be fragile, which means that the stability of the closed-loop system is highly sensitive to variations in the control parameters. Since then, several design methods have been proposed to prevent fragile controllers, including the following works: Control fragility caused by fixed word-length implementations is studied, for which a loop-shaping method is introduced as a solution. Nonfragile controllers with linear-quadratic performance indices are studied, where it is observed that for some structured perturbations the problem can be tackled by convex optimization. The use of fixed-structure controllers to avoid fragility is considered. Nonfragile design through minimization of pole sensitivity is proposed in and the ellipsoidal sets of nonfragile feedback gains are studied.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Introduction", "weight": 1.5} -->

While most of the literature on nonfragile control is devoted to additive perturbations on the feedback gain, multiplicative perturbations are also studied, e.g,. Moreover, nonfragile filter design has also been a topic of research in the literature.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Introduction", "weight": 1.5} -->

For unknown linear time-invariant (LTI) systems, a stabilizing state-feedback gain can be directly obtained from a collection of noisy input-state data. Given that the noise belongs to a known deterministic model, the data give rise to the set of *data-consistent systems*, which includes all systems that could have generated the available data for some noise sequence agreeing with the noise model. In this setting, since any data-consistent system can potentially be the unknown true system, one may seek a feedback gain to stabilize all data-consistent systems. This problem has already been studied within the framework of *data informativity*, for which solutions are presented, e.g.,. To the authors' knowledge, however, the fragility issues of such data-driven feedback design methods have not been addressed in the literature.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Introduction", "weight": 1.5} -->

In this work, we answer the following question: *Given a state-feedback gain that stabilizes all data-consistent systems, to what extent such a guarantee is intact when the gain is perturbed?* We study the effect of additive perturbations on data-driven feedback gains. To that end, we parameterize all quadratically stabilizing feedback gains, for which we leverage the recently developed tools on quadratic matrix inequalities (QMIs). We call a data-driven feedback gain extremely fragile if a variation in the feedback gain, no matter how small in magnitude, destabilizes a subset of the data-consistent systems. Two extreme cases where the data-driven feedback gain is extremely fragile or is completely immune to perturbations are isolated by necessary and sufficient conditions. Next, we study the general case where the data-driven feedback is neither fragile nor immune, for which we characterize the set of perturbations that leave the stability guarantee intact. For this, we introduce a measure that quantifies the fragility of a feedback gain. We show that one can compute this measure and find the least fragile feedback gain by solving a semi-definite program (SDP).

<!-- chunk {"id": "body-0011", "role": "body", "section": "Introduction", "weight": 1.5} -->

For the sake of completeness and better understanding of the introduced concepts, we first study the underlying problems in the model-based setting, and then extend our study to the data-driven framework.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Introduction", "weight": 1.5} -->

This note is organized as follows: Section 2 provides a recap of the data-driven stabilization theory. In Section 3, we present a parametrization for the set of data-driven stabilizing feedback gains. In Section 4, we study the fragility of feedback gains within model-based and data-driven settings. Finally, Section 5 concludes the paper.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Recap of Data-driven Stabilization", "weight": 1.0} -->

In this section, we briefly review data-driven stabilization results within the *data informativity* framework based on the existing literature.

<!-- chunk {"id": "body-0014", "role": "body", "section": "Recap of Data-driven Stabilization", "weight": 1.0} -->

Consider an LTI system of the form

<!-- chunk {"id": "body-0015", "role": "body", "section": "Recap of Data-driven Stabilization", "weight": 1.0} -->

collected from system. These data are influenced by the unknown process noise

<!-- chunk {"id": "body-0016", "role": "body", "section": "Recap of Data-driven Stabilization", "weight": 1.0} -->

We assume that the noise signal satisfies an energy bound of the form

<!-- chunk {"id": "body-0017", "role": "body", "section": "Recap of Data-driven Stabilization", "weight": 1.0} -->

Several noise models can be captured by this energy bound (see \[18, p. 4\] for a detailed account), among which the noise-free case corresponds to $\Phi_{11} = 0$, $\Phi_{12} = \Phi_{21}^{\top} = 0$, and $\Phi_{22} = {- I}$.

<!-- chunk {"id": "body-0018", "role": "body", "section": "Recap of Data-driven Stabilization", "weight": 1.0} -->

A pair of real matrices $(A,B)$ is called a *data-consistent system* if it satisfies

<!-- chunk {"id": "body-0019", "role": "body", "section": "Recap of Data-driven Stabilization", "weight": 1.0} -->

for some $W_{-}$ satisfying. We define the set of all data-consistent systems as

<!-- chunk {"id": "body-0020", "role": "body", "section": "Parametrization of Data-driven Feedback Gains", "weight": 1.0} -->

In this section, we will parameterize the set of quadratically stabilizing feedback gains that can be obtained from the collected input-state data. To that end, suppose that $\begin{bmatrix}
\end{bmatrix}$ has full column rank. For $P > 0$ and $\alpha \geq 0$, we define

<!-- chunk {"id": "body-0021", "role": "body", "section": "Parametrization of Data-driven Feedback Gains", "weight": 1.0} -->

The set of all quadratically stabilizing feedback gains that can be obtained from data $\mathcal{D}$ is the union of the sets $\mathcal{K}{(P,\alpha)}$ over all $P > 0$ and $\alpha \geq 0$, which is denoted by

<!-- chunk {"id": "body-0022", "role": "body", "section": "Parametrization of Data-driven Feedback Gains", "weight": 1.0} -->

The following theorem provides a parameterization for such sets.

<!-- chunk {"id": "body-0023", "role": "body", "section": "Fragility Analysis", "weight": 1.0} -->

In this section, we study the effect of *additive* perturbations on the stabilizing feedback gains (see Fig. 1) within both model-based and data-driven settings.

<!-- chunk {"id": "body-0024", "role": "body", "section": "Model-based analysis", "weight": 1.0} -->

For a stabilizable $(A,B)$, let $K$ be such that

<!-- chunk {"id": "body-0025", "role": "body", "section": "Model-based analysis", "weight": 1.0} -->

is Schur. We define the radius of stabilizing gains centered around $K$ as

<!-- chunk {"id": "body-0026", "role": "body", "section": "Model-based analysis", "weight": 1.0} -->

The value of $\mu_{(A,B)}^{\text{a}}{(K)}$ gives the largest bound for an additive feedback perturbation so that the closed-loop system remains stable. The following theorem characterizes the case where $\mu_{(A,B)}^{\text{a}}{(K)}$ is finite.

<!-- chunk {"id": "body-0027", "role": "body", "section": "Remark 4.13", "weight": 1.0} -->

Suppose that $(A,B)$ is stabilizable and $B \neq 0$. Let $K$ be such that $A_{K}$ is Schur.

<!-- chunk {"id": "body-0028", "role": "body", "section": "Remark 4.13", "weight": 1.0} -->

The following example illustrates the results of Theorems 4.10 and Remark 4.13.

<!-- chunk {"id": "body-0029", "role": "body", "section": "Example 4.14", "weight": 1.0} -->

Consider $A = \begin{bmatrix}
\end{bmatrix}$ and $B = \begin{bmatrix}
\end{bmatrix}$. The set of all stabilizing feedback gains is shown by the triangle area in Fig. 2. In particular, for $K = {- \begin{bmatrix}
\end{bmatrix}}$ we have ${\mu_{(A,B)}^{\text{a}}{(K)}} = 0.447$, and Remark 4.13 yields ${\lambda_{(A,B)}^{\text{a}}{(K)}} = 0.333$. According to Theorem 4.10, we have $\lambda_{(A,B)}^{\text{a}} = 0.667$ that is attained by $K_{\ast} = {- \begin{bmatrix}
\end{bmatrix}}$.

<!-- chunk {"id": "body-0030", "role": "body", "section": "Example 4.14", "weight": 1.0} -->

Fig. 3 provides a contour plot illustrating the level sets of stabilizing feedback gains with constant $\lambda_{(A,B)}^{\text{a}}{(K)}$.

<!-- chunk {"id": "body-0031", "role": "body", "section": "Data-driven analysis", "weight": 1.0} -->

In this section, we turn our attention to the data-driven setting. Assume that the data $\mathcal{D}$ are informative for stabilization. Let $K$ be such that $A + {BK}$ is Schur for all ${(A,B)} \in \Sigma_{\mathcal{D}}$. Analogous to, we define

<!-- chunk {"id": "body-0032", "role": "body", "section": "Data-driven analysis", "weight": 1.0} -->

The value of $\mu_{\mathcal{D}}^{\text{a}}{(K)}$ gives the largest bound for an additive feedback perturbation so that the closed-loop remains stable for all systems within $\Sigma_{\mathcal{D}}$. The two extreme cases where $\mu_{\mathcal{D}}^{\text{a}}{(K)}$ is zero or not finite are fully characterized by the following theorem.

<!-- chunk {"id": "body-0033", "role": "body", "section": "Remark 4.17", "weight": 1.0} -->

In case ${\mu_{\mathcal{D}}^{\text{a}}{(K)}} = 0$, a small additive perturbation on the feedback gain, no matter how small, destabilizes a nonempty subset of $\Sigma_{\mathcal{D}}$. Therefore, a small additive perturbation may also destabilize the true system. We refer to this case as *extreme fragility*. Theorem 4.15 shows that if $\begin{bmatrix}
\end{bmatrix}$ does not have full column rank, then any data-driven stabilizing feedback gain is extremely fragile. This condition is equivalent to the case where the set of data-consistent systems is unbounded. Therefore, in the noise-free case, the data-driven feedback gain is extremely fragile *if and only if* the system cannot be uniquely identified, see \[1, Prop. 6\].

<!-- chunk {"id": "body-0034", "role": "body", "section": "Remark 4.17", "weight": 1.0} -->

Now, we aim at developing numerically tractable methods to approximate $\mu_{\mathcal{D}}^{\text{a}}{(K)}$. Suppose that the data $\mathcal{D}$ are informative for quadratic stabilization. Let $K$, $P > 0$, and $\alpha \geq 0$ be such that $K \in {\mathcal{K}{(P,\alpha)}}$. We define

<!-- chunk {"id": "body-0035", "role": "body", "section": "Remark 4.17", "weight": 1.0} -->

One can also define the largest value of $\kappa_{\mathcal{D}}^{\text{a}}{(P,\alpha,K)}$ over all $P > 0$ and $\alpha \geq 0$ as

<!-- chunk {"id": "body-0036", "role": "body", "section": "Remark 4.17", "weight": 1.0} -->

The value of $\lambda_{\mathcal{D}}^{\text{a}}$ can be obtained by solving an SDP as stated next.

<!-- chunk {"id": "body-0037", "role": "body", "section": "Remark 4.21", "weight": 1.0} -->

Suppose that ${{rank}\begin{bmatrix}
\end{bmatrix}} = {n + m}$, the data $\mathcal{D}$ are informative for quadratic stabilization, and (11 ‣ Proposition 1 ([19, Prop. 14]) ‣ 2 Recap of Data-driven Stabilization ‣ Fragility Analysis of Data-Driven Feedback Gains")) does not hold. Let $K \in {\mathcal{K}{(P,\alpha)}}$ for some $P > 0$ and $\alpha \geq 0$.

<!-- chunk {"id": "body-0038", "role": "body", "section": "Remark 4.21", "weight": 1.0} -->

The following example illustrates the results of Theorems 4.18 and Remark 4.21.

<!-- chunk {"id": "body-0039", "role": "body", "section": "Example 4.22", "weight": 1.0} -->

Consider the true system with

<!-- chunk {"id": "body-0040", "role": "body", "section": "Example 4.22", "weight": 1.0} -->

The LMIs in (16]) ‣ 2 Recap of Data-driven Stabilization ‣ Fragility Analysis of Data-Driven Feedback Gains")) are feasible^11^1For the numerical examples of this paper, the LMIs and SDPs are solved using the YALMIP toolbox of MATLAB with the MOSEK solver., hence, the data are informative for quadratic stabilization. The set $\mathcal{K}$ is shown in Fig. 4. In particular, for $K = {- \begin{bmatrix}
\end{bmatrix}}$, according to Remark 4.21 we have ${\lambda_{\mathcal{D}}^{\text{a}}{(K)}} = 0.055$. Theorem 4.18 yields $\lambda_{\mathcal{D}}^{\text{a}} = 0.087$, which is attained by $K_{\ast} = {- \begin{bmatrix}
\end{bmatrix}}$.

<!-- chunk {"id": "body-0041", "role": "body", "section": "Example 4.22", "weight": 1.0} -->

Fig. 5 provides a contour plot illustrating the level sets of stabilizing feedback gains with constant values of $\lambda_{\mathcal{D}}^{\text{a}}{(K)}$.

<!-- chunk {"id": "body-0042", "role": "body", "section": "Example 4.22", "weight": 1.0} -->

The following example discusses a more realistic case study compared to that of Example 4.22.

<!-- chunk {"id": "body-0043", "role": "body", "section": "Example 4.23", "weight": 1.0} -->

Consider the state-space model of a fighter aircraft \[25, Ex. 10.1.2\] as a benchmark example^22^2The Matlab files for this example, including the data set, are available at We discretize the continuous-time model with a sample time of $0.01$ to have

<!-- chunk {"id": "body-0044", "role": "body", "section": "Example 4.23", "weight": 1.0} -->

We collect $T = 500$ input and state data samples from this system. The data are generated starting from

<!-- chunk {"id": "body-0045", "role": "body", "section": "Example 4.23", "weight": 1.0} -->

with the input drawn at random from a zero-mean Gaussian distribution with unit variance. During this process, the entries of the noise samples are also drawn at random but from a uniform distribution between $- {0.005/6}$ and $0.005/6$. This noise model can be captured by with $\Phi_{11} = {0.005^{2}TI_{n}}$, $\Phi_{12} = \Phi_{21}^{\top} = 0$, and $\Phi_{22} = {- I_{T}}$.

<!-- chunk {"id": "body-0046", "role": "body", "section": "Example 4.23", "weight": 1.0} -->

We first design a feedback gain, $K_{o}$, using the method provided. This can be done using Proposition 4]) ‣ 2 Recap of Data-driven Stabilization ‣ Fragility Analysis of Data-Driven Feedback Gains"), which yields

<!-- chunk {"id": "body-0047", "role": "body", "section": "Example 4.23", "weight": 1.0} -->

For this feedback gain, using Remark 4.21 we have ${\lambda_{\mathcal{D}}^{\text{a}}{(K_{o})}} = 0.026$. Now, we use Theorem 4.18 to compute the least fragile feedback gain in the sense of measure as

<!-- chunk {"id": "body-0048", "role": "body", "section": "Conclusions", "weight": 1.0} -->

It has been shown that the fragility of a data-driven feedback gain can be quantified by means of a measure, and the least fragile data-driven feedback gain can be computed by solving a data-based SDP. In addition, it has been shown that extreme fragility and complete immunity of a data-driven feedback gain towards feedback perturbations can be fully characterized by conditions that only depend on input-state data and the noise model. In this work, we only focused on *additive* perturbation on the control parameters. Another type of feedback perturbation that is relevant in practical applications of data-driven controllers is the *multiplicative* one, which can capture the effect of various faults and failures. The study of this and other types of feedback perturbations is left as future work.
