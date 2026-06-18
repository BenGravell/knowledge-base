<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

A Stochastic Gradient Descent Approach to Design Policy Gradient Methods for LQR

Topics include Gradient descent, Stochastic gradients, Online algorithms, Policy gradients, Stochastic gradient descent, Gradient method.

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

In this work, we propose a stochastic gradient descent (SGD) framework to design data-driven policy gradient descent algorithms for the linear quadratic regulator problem. Two alternative schemes are considered to estimate the policy gradient from stochastic trajectory data: (i) an indirect online identification based approach, in which the system matrices are first estimated and subsequently used to construct the gradient, and (ii) a direct zeroth-order approach, which approximates the gradient using empirical cost evaluations. In both cases, the resulting gradient estimates are random due to stochasticity in the data, allowing us to use SGD theory to analyze the convergence of the associated policy gradient methods. A key technical step consists of modeling the gradient estimates as suitable stochastic gradient oracles, which, because of the way they are computed, are inherently based. We derive sufficient conditions under which SGD with a biased gradient oracle converges asymptotically to the optimal policy, and leverage these conditions to design the parameters of the gradient estimation schemes. Moreover, we compare the advantages and limitations of the two data-driven gradient estimators. Numerical experiments validate the effectiveness of the proposed methods.

<!-- chunk {"id": "body-0003", "role": "body", "section": "Introduction", "weight": 1.5} -->

Reinforcement learning (RL) has had a profound impact across a wide range of applications. A central component of RL is policy optimization, in which a parameterized policy is directly optimized with respect to a prescribed performance objective. Among various policy optimization framework, this work focuses on policy gradient (PG) methods. Understanding the behavior of PG methods, particularly their convergence to the optimal policy in the presence of uncertainty and stochastic disturbances, remains an active and important research direction, and is essential for their reliable deployment in real-world applications.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

The linear quadratic regulator (LQR) problem has emerged as a canonical benchmark for studying RL in continuous state and action spaces due to its analytical tractability and practical relevance. PG methods have attracted substantial interest in this setting. A seminal result in established global convergence of PG methods for deterministic LQR, which stimulated extensive follow-up works, such as. These studies typically assume exact knowledge of the system dynamics and access to exact gradients. To relax this assumption, more recent works such as analyze gradient-based methods under inexact gradients, providing valuable robustness insights. However, in these works, the gradient uncertainty is introduced through stylized perturbation models rather than arising naturally from data-driven estimation.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

To address gradient uncertainty arising from concrete estimation procedures rather than artificial perturbations, a prominent data-driven approach is the indirect method, which follows a two-step procedure: system dynamics are first estimated from data, and PG methods are then applied using the estimated model. Representative examples include, which combine least-squares identification with gradient-based updates under bounded noise assumptions. In contrast, direct data-driven methods bypass explicit model identification. One class of such methods estimates the quantities required for PG updates directly from data, with stochastic-setting examples given. Another line of work studies direct PG methods based on data-driven policy parameterizations, such as DeePC-based approaches, which typically operate under bounded-noise assumptions. While related, these direct data-driven approaches are not the primary focus of this work.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

Another class of methods, closely related to the present study, employs zeroth-order techniques in which gradients are approximated using noisy function evaluations. This line of research originates from in the deterministic LQR setting and has been extended to stochastic environments in and, which consider infinite- and finite-horizon problems, respectively. These approaches rely on ergodic data collection and exploit the inherent robustness of PG methods, namely, that sufficiently accurate gradient estimates ensure cost contraction at each iteration. However, existing analyses are often conservative in two key respects: they typically require a large number of samples per iteration to control gradient estimation error, leading to high sample complexity, and they rely on uniform concentration guarantees enforced via union bounds, resulting in confidence levels that deteriorate exponentially with the number of iterations.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

To reduce the conservativeness of prior analyses of zeroth-order methods, we propose here to incorporate stochastic gradient descent (SGD) into the analysis of PG methods. In SGD-based analyses, gradients are accessed through stochastic oracles, and convergence is characterized using tools from stochastic approximation. SGD has been shown to be effective in both convex and non-convex settings, including using zeroth-order optimization technique. While analyses assume unbiased gradient estimates, recent works extend the application of SGD theory with biased gradient oracles, providing a less restrictive modeling framework. For direct data-driven LQR, first adopted an SGD-style analysis under relatively strong assumptions on gradient estimation using zeroth-order methods. Subsequent works relaxed these assumptions by employing alternative gradient estimation schemes, leading to improved sample efficiency and robustness. In, only a single gradient estimation scheme (zeroth-order method) is considered, and the analysis provides convergence guarantees only to a suboptimal solution.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Introduction", "weight": 1.5} -->

In this work, we leverage the SGD framework to design data-driven policy gradient methods for solving the LQR problem in the presence of stochastic noise.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Introduction", "weight": 1.5} -->

Indirect method: Recursive least squares is used to estimate the system matrices, which are then used to compute a model-based gradient.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Introduction", "weight": 1.5} -->

Direct method: A zeroth-order approach is employed to estimate the gradient directly from empirical cost evaluations.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Introduction", "weight": 1.5} -->

For both methods, we formalize the gradient estimates computed using stochastic trajectory data as gradient oracles with analytical characterizations of their first and second moments.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Introduction", "weight": 1.5} -->

Due to the nonlinear structure of the gradient, these oracles are inherently biased. Leveraging the *gradient-dominated* and *quasi-smooth* properties of the LQR cost function, we derive conditions on the step size and bias under which an SGD algorithm equipped with a general biased gradient oracle converges asymptotically to the optimal policy. Unlike classical SGD analyses on gradient-dominated functions, which assume $L$-smoothness, our results extend these guarantees to quasi-smooth functions.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Introduction", "weight": 1.5} -->

Using the conditions derived above, we design the parameters of both the indirect and direct gradient estimation schemes so that the resulting gradient oracles satisfy the required bias conditions. This, in turn, ensures that the corresponding data-driven policy gradient descent algorithms converge asymptotically to the optimal policy. To the best of the authors' knowledge, this is the first work to demonstrate last iterate convergence to the optimal policy across *all data-driven policy gradient methods*, whereas previous results typically guarantee convergence only to suboptimal solutions. Using the derived conditions for convergence, we analyze and compare the advantages and limitations of the indirect and direct approaches.

<!-- chunk {"id": "body-0014", "role": "body", "section": "Introduction", "weight": 1.5} -->

The paper is organized as follows. Section 2 introduces the problem setting and the necessary preliminaries. Section 3 describes the indirect and direct data-driven policy gradient estimation frameworks and formalizes them as gradient oracles. Section 4 investigates the convergence of SGD with biased gradient oracles for gradient-dominated and quasi-smooth cost functions. Section 5 analyzes and compares the indirect and direct data-driven policy gradient methods based on the conditions derived in the previous section. Section 6 demonstrates the effectiveness of the proposed data-driven policy gradient methods and shows numerical simulations. Finally, Section 7 concludes the paper. Unless referenced otherwise, all the theoretical results are new. For readability, proofs can be found in the Appendix.

<!-- chunk {"id": "body-0015", "role": "body", "section": "Problem setting and Preliminaries", "weight": 1.0} -->

It is a well-known fact that the optimal $K^{\ast}$ minimizing $C$ satisfies

<!-- chunk {"id": "body-0016", "role": "body", "section": "Problem setting and Preliminaries", "weight": 1.0} -->

We recall the boundedness of $\parallel{{\nabla C}{(K)}}\parallel$ and $\parallel K\parallel$ and local Lipschitz continuity properties of $\Sigma_{K},C$ and $\nabla C$ over the level set, which are used in the subsequent analysis.

<!-- chunk {"id": "body-0017", "role": "body", "section": "Gradient Estimation and Gradient Oracles", "weight": 1.0} -->

In this section, we study two data-driven approaches for estimating the policy gradient when the system's model is unknown. The first is an indirect method that identifies the system matrices via recursive least squares, as described in Section 3.1. The second is a zeroth-order method that approximates the gradient directly by using empirical cost evaluations, discussed in Section 3.2. In both cases, the gradient estimates, denoted in the following as $\hat{\nabla}C{( \cdot )}$ are constructed from trajectory data generated by the stochastic system (1b), and thus inherit randomness from the data. Accordingly, these estimates can be viewed as stochastic gradients. Our objective is to study their properties and formalize them as gradient oracles, which are characterizations of the gradient estimates through their first and second moments.

<!-- chunk {"id": "body-0018", "role": "body", "section": "Gradient Estimation and Gradient Oracles", "weight": 1.0} -->

where $\Delta_{b}$ is the bias term introduced by the estimation schemes; $c$ is a uniform upper bound on the second moment of the gradient estimator. The existing literature typically assumes that ${\Delta_{b}{(K)}} = 0$, an assumption that cannot be satisfied when gradients are estimated from data.

<!-- chunk {"id": "body-0019", "role": "body", "section": "Indirect Gradient Oracle", "weight": 1.0} -->

In this subsection, we characterize the gradient oracle constructed from system matrix estimates obtained via the recursive least squares (RLS) algorithm. Let ${\hat{\theta}}_{j}:={\lbrack{{\hat{A}}_{j}{\hat{B}}_{j}}\rbrack}$ where ${\hat{A}}_{j}$ and ${\hat{B}}_{j}$ denote the RLS estimates at iteration $j$, and define the regressor data $d_{j}:={\lbrack x_{j}^{\top},u_{j}^{\top}\rbrack}^{\top}$ obtained from trajectory.

<!-- chunk {"id": "body-0020", "role": "body", "section": "Indirect Gradient Oracle", "weight": 1.0} -->

The selection of ${\hat{\theta}}_{0}$ and $H_{0}$ will be specified later. The gradient at iteration $j$ is computed using the online system estimates ${\hat{\theta}}_{j}$ (i.e. ${\hat{A}}_{j}$ and ${\hat{B}}_{j}$). Recall from Section 2 that for any $K \in \mathcal{S}$, the exact policy gradient is given. Accordingly, the gradient constructed from the estimated model is given by

<!-- chunk {"id": "body-0021", "role": "body", "section": "Indirect Gradient Oracle", "weight": 1.0} -->

It is crucial to quantify how the estimation errors propagate into the gradient computation. To this end, we consider generic estimates $\hat{A}$ and $\hat{B}$ (with a slight abuse of notation, suppressing the iteration index for clarity) and analyze the discrepancy between the true gradient and its estimated counterpart. We now introduce the following lemma to quantify the error in the estimated gradient induced by the model estimation error ${\Delta\theta}:={\lbrack{\hat{A} - A},{\hat{B} - B}\rbrack}$.

<!-- chunk {"id": "body-0022", "role": "body", "section": "Direct Gradient Oracle", "weight": 1.0} -->

In this subsection, we investigate the gradient oracle obtained from the direct method, which we refer to as the zeroth-order method (Z.O.M).

<!-- chunk {"id": "body-0023", "role": "body", "section": "Direct Gradient Oracle", "weight": 1.0} -->

where ${\mathbb{B}}_{v}$ denotes the uniform distribution over all matrices of size $n_{u} \times n_{x}$ with Frobenius norm less than the smoothing radius $v$.

<!-- chunk {"id": "body-0024", "role": "body", "section": "Direct Gradient Oracle", "weight": 1.0} -->

where ${\mathbb{S}}_{v}$ denotes the uniform distribution over the boundary of the Frobenius norm ball with radius $v$. The algorithm used to estimate the gradient is presented in Algorithm 2.

<!-- chunk {"id": "body-0025", "role": "body", "section": "Direct Gradient Oracle", "weight": 1.0} -->

We now characterize the gradient oracle associated.

<!-- chunk {"id": "body-0026", "role": "body", "section": "Convergence Analysis of SGD with Biased Gradient", "weight": 1.0} -->

In the previous section, we showed that the gradients generated by the two considered estimators can be modeled as gradient oracles. Inspection of their expressions reveals that the gradient estimators are biased. In this section, we analyze the convergence of stochastic gradient descent applied to *gradient-dominated* and *quasi-smooth* functions in the presence of biased gradient oracles.

<!-- chunk {"id": "body-0027", "role": "body", "section": "Convergence Analysis of SGD with Biased Gradient", "weight": 1.0} -->

where $\hat{\nabla}C{(K_{i})}$ is a stochastic gradient obtained from a suitable estimator, specifically one of the two concrete algorithms introduced in Section 3. From Lemmas 7 ‣ 3.1 Indirect Gradient Oracle ‣ 3 Gradient Estimation and Gradient Oracles ‣ A Stochastic Gradient Descent Approach to Design Policy Gradient Methods for LQR") and 8 ‣ 3.2 Direct Gradient Oracle ‣ 3 Gradient Estimation and Gradient Oracles ‣ A Stochastic Gradient Descent Approach to Design Policy Gradient Methods for LQR"), ${\forall i} \in {\mathbb{Z}}_{+}$, given an iterate $K_{i}$, both indirect and direct oracles satisfy the following properties almost surely (a.s.):

<!-- chunk {"id": "body-0028", "role": "body", "section": "Convergence Analysis of SGD with Biased Gradient", "weight": 1.0} -->

and the function $\overline{\Delta}{({C{(K)}})}$ decreases monotonically as the cost $C{(K)}$ decreases.

<!-- chunk {"id": "body-0029", "role": "body", "section": "Convergence Analysis of SGD with Biased Gradient", "weight": 1.0} -->

We provide the following explanations for the bias term as well as for the boundedness of the second moment.

<!-- chunk {"id": "body-0030", "role": "body", "section": "Convergence Analysis of SGD with Biased Gradient", "weight": 1.0} -->

the term $\Delta{(K_{i},i)}$ denotes the iteration-dependent bias introduced either by the model estimates ${\hat{A}}_{i},{\hat{B}}_{i}$ at $i$-th iteration (as discussed in Section 3.1) or by the exploration radius $v_{i}$, and the finite rollout length $\ell_{i}$ (as discussed in Section 3.2). This bias may vary across iterations. In the indirect setting, it evolves together with the model-learning process, whereas in the zeroth-order method it may arise from the iteration-varying choices of $v_{i}$ and $\ell_{i}$.

<!-- chunk {"id": "body-0031", "role": "body", "section": "Convergence Analysis of SGD with Biased Gradient", "weight": 1.0} -->

Because quantifying the bias term $\Delta{(K_{i},i)}$ is challenging, our analysis focuses on bounding its norm ${\parallel{\Delta{(K_{i},i)}}\parallel}_{F}$ (as in Lemma 7 ‣ 3.1 Indirect Gradient Oracle ‣ 3 Gradient Estimation and Gradient Oracles ‣ A Stochastic Gradient Descent Approach to Design Policy Gradient Methods for LQR") and Lemma 8 ‣ 3.2 Direct Gradient Oracle ‣ 3 Gradient Estimation and Gradient Oracles ‣ A Stochastic Gradient Descent Approach to Design Policy Gradient Methods for LQR")).

<!-- chunk {"id": "body-0032", "role": "body", "section": "Convergence Analysis of SGD with Biased Gradient", "weight": 1.0} -->

In the SGD literature, the second moment is often assumed to satisfy the following ABC condition: ${\mathbb{E}}\left\lbrack {\parallel\hat{\nabla}C{(K)}\parallel}_{F}^{2} \middle| K \leq a{(C{(K)} - C{(K^{\ast})})} + b{\parallel\nabla C{(K)}\parallel}^{2} + c \right.$. We assume a uniform second-moment bound, i.e., $a = b = 0$, instead of the more general ABC condition, because in the subsequent analysis, we show that such a bound can indeed be established for the proposed gradient estimators over a local level set.

<!-- chunk {"id": "body-0033", "role": "body", "section": "Convergence Analysis of SGD with Biased Gradient", "weight": 1.0} -->

The following assumption plays a crucial role for studying the convergence of to the optimal solution.

<!-- chunk {"id": "body-0034", "role": "body", "section": "Assumption 1", "weight": 1.0} -->

This assumption can be satisfied by appropriately choosing the parameters in the gradient estimation process for both methods. A detailed discussion is provided in Section 5. Before proceeding with the convergence analysis, we first introduce the following two lemmas.

<!-- chunk {"id": "body-0035", "role": "body", "section": "Closing the loop between SGD and gradient estimators", "weight": 1.0} -->

In the previous section, we analyzed the convergence of SGD applied to the LQR policy gradient problem with the generic gradient oracle. The analysis helped us identify sufficient conditions on stepsize choices and gradient accuracy under which SGD converges to the optimal cost. We now show how tuning parameters of the two gradient estimators presented in Section 3 can be chosen to satisfy these conditions. The block diagram corresponding to the two data-driven policy gradient algorithms is illustrated in Figure 1.

<!-- chunk {"id": "body-0036", "role": "body", "section": "Indirect Methods", "weight": 1.0} -->

The method is built upon Algorithm 1. At each iteration $i$, the system estimates ${\hat{\theta}}_{i}$, produced by Algorithm 1, are used to construct the gradient associated with the current policy $K_{i}$, followed by a policy gradient descent step. After applying the control input, new data are collected and subsequently leveraged to update the estimates of the system matrices ${\hat{\theta}}_{i + 1}$. We emphasize that, within the indirect framework, the excitation gain in does not need to be *on-policy*, as illustrated in Figure 1. In particular, the system can be operated using a fixed stabilizing gain $K$, corresponding to an *off-policy* setting. A detailed discussion on the distinction between off-policy and on-policy schemes is provided in Remark 1.

<!-- chunk {"id": "body-0037", "role": "body", "section": "Indirect Methods", "weight": 1.0} -->

The following theorem establishes convergence guarantees to the optimal solution using the indirect data-driven policy gradient algorithm based on Algorithm 1.

<!-- chunk {"id": "body-0038", "role": "body", "section": "Indirect Methods", "weight": 1.0} -->

Assume that the data sequence $\{ d_{i}\}$ is locally persistent with parameters $N_{0},M_{0},\alpha_{0}$.

<!-- chunk {"id": "body-0039", "role": "body", "section": "Indirect Methods", "weight": 1.0} -->

The proof combines the main results of Theorem 10 and Lemma 7 ‣ 3.1 Indirect Gradient Oracle ‣ 3 Gradient Estimation and Gradient Oracles ‣ A Stochastic Gradient Descent Approach to Design Policy Gradient Methods for LQR"). The key step is to verify that the bias term appearing in the gradient oracle decays at an appropriate rate. Under the local persistence assumption, the expected estimation error in the indirect method decreases at the rate $O{(i^{- {1/2}})}$, which matches the requirement for convergence of SGD with a biased gradient oracle. Moreover, a uniform upper bound on the second-moment term can always be established as $V_{I}{({b_{K}{(J_{0})}},{p{({b_{K}{(J_{0})}},{p_{\theta}^{\prime}{(J_{0})}})}})}$.

<!-- chunk {"id": "body-0040", "role": "body", "section": "Indirect Methods", "weight": 1.0} -->

Consequently, with a properly chosen step size, the indirect method converges asymptotically to the optimal policy without requiring any modification to the underlying indirect gradient estimation algorithm based on recursive least-squares.

<!-- chunk {"id": "body-0041", "role": "body", "section": "Remark 1", "weight": 1.0} -->

From Theorem 5.1, the parameter $c_{x}$ (defined in ), which depends on $\overline{x}$ introduced in (23 ‣ 3.1 Indirect Gradient Oracle ‣ 3 Gradient Estimation and Gradient Oracles ‣ A Stochastic Gradient Descent Approach to Design Policy Gradient Methods for LQR")), plays a critical role in the convergence analysis. In the *on-policy* setting, where the system is excited using the policies generated by the policy gradient updates, we can only guarantee the existence of such a bound. This is because, with high probability, each gain $\{ K_{i}\}$, $i \in {\mathbb{Z}}_{+}$, stabilizes the system and the sequence $\{ K_{i}\}$ converges asymptotically to $K^{\ast}$. However, the value of $c_{x}$ depends on the stochastic policy sequence $\{ K_{i}\}$, and a closed-form expression is generally unavailable.

<!-- chunk {"id": "body-0042", "role": "body", "section": "Remark 1", "weight": 1.0} -->

In contrast, in the *off-policy* setting, where the system is excited using a fixed stabilizing gain $K$ rather than the iterates $\{ K_{i}\}$ generated by the SGD algorithm, an explicit bound on $c_{x}$ can be computed directly. This enables a more precise characterization of $c_{x}$ and, in turn, leads to sharper bounds on the bias and convergence behavior under off-policy data collection.

<!-- chunk {"id": "body-0043", "role": "body", "section": "Direct Methods", "weight": 1.0} -->

The direct data-driven policy gradient method proceeds as follows. At each iteration, Algorithm 2 is used to estimate the gradient. We let the parameters $v_{i},\ell_{i}$, and $n_{i}$ in Algorithm 2 vary across the iterations to control the bias and variance. The estimated gradient is then applied in a policy gradient descent step. In the direct method, only an on-policy scheme can be employed.The following theorem establishes convergence guarantees to the optimal solution using the direct data-driven policy gradient Algorithm.

<!-- chunk {"id": "body-0044", "role": "body", "section": "Direct Methods", "weight": 1.0} -->

Then, the event $F$ occurs with probability at least $({1 - \delta})$.

<!-- chunk {"id": "body-0045", "role": "body", "section": "Direct Methods", "weight": 1.0} -->

The proof of Theorem 5.2 follows from Theorem 6 ‣ 3.1 Indirect Gradient Oracle ‣ 3 Gradient Estimation and Gradient Oracles ‣ A Stochastic Gradient Descent Approach to Design Policy Gradient Methods for LQR") and Lemma 8 ‣ 3.2 Direct Gradient Oracle ‣ 3 Gradient Estimation and Gradient Oracles ‣ A Stochastic Gradient Descent Approach to Design Policy Gradient Methods for LQR") by designing the parameters $r_{i},n_{i}$, and $\ell_{i}$ such that the resulting gradient oracle satisfies the required bias decay and bounded-variance conditions. To guarantee convergence to the optimal policy, the exploration radius $v_{i}$ must decrease and the rollout length $\ell_{i}$ must increase so that the bias term vanishes at the required rate. Nevertheless, a smaller $v_{i}$ leads to an inflation of the variance, which necessitates increasing the number of rollouts $n_{i}$ to maintain a bounded second moment.

<!-- chunk {"id": "body-0046", "role": "body", "section": "Comparison between the two gradient estimators", "weight": 1.0} -->

To guarantee convergence to the optimal policy, the indirect and direct policy gradient methods differ in the following aspects, as characterized in Theorems 5.1 and 5.2:

<!-- chunk {"id": "body-0047", "role": "body", "section": "Comparison between the two gradient estimators", "weight": 1.0} -->

*Sample Complexity:* the indirect and direct policy gradient methods impose fundamentally different sample requirements. The indirect method updates the system estimates using all previously collected data and requires only $O{}$ new samples per iteration to achieve the desired bias decay. In contrast, the direct method relies solely on empirical cost evaluations at the current iterate and cannot reuse past data, resulting in a per-iteration sample complexity of $O{(i^{2})}$. This disparity reflects the inherent bias and variance trade-off in zeroth-order gradient estimation, implying that direct methods require substantially more data than indirect methods to achieve convergence to the optimal policy.

<!-- chunk {"id": "body-0048", "role": "body", "section": "Comparison between the two gradient estimators", "weight": 1.0} -->

*Excitation Policy:* For the indirect method, convergence to the optimal policy requires the data sequence $\{ d_{i}\}$ to satisfy the local persistency condition defined in Definition 1 ‣ 3.1 Indirect Gradient Oracle ‣ 3 Gradient Estimation and Gradient Oracles ‣ A Stochastic Gradient Descent Approach to Design Policy Gradient Methods for LQR"). To this end, the dithering signal $\{ e_{i}\}$ is introduced. The excitation gain in the indirect framework may be either off-policy or on-policy, as discussed in Remark 1. In contrast, for the direct method, the gradient is approximated via the smoothing function, where a random perturbation matrix $U$ is introduced in the gain, leading to the control input format. In this case, only an on-policy implementation is possible.

<!-- chunk {"id": "body-0049", "role": "body", "section": "Comparison between the two gradient estimators", "weight": 1.0} -->

*Data Collection:* In the indirect method, online data are continuously used to update the system estimates, and the gradient is computed based on the updated estimates. For the direct method, data are collected via independent finite-horizon rollouts; that is, the state is re-initialized at $x_{0}^{(k)}$ for each trajectory, as specified in Algorithm 2.

<!-- chunk {"id": "body-0050", "role": "body", "section": "Comparison between the two gradient estimators", "weight": 1.0} -->

*Initial Data Collection Phase:* A limitation of the indirect method is that its convergence guarantees rely on an initial data collection phase to ensure that the system matrix estimates are sufficiently close to the true dynamics. In contrast, the direct method does not require such an initialization phase.

<!-- chunk {"id": "body-0051", "role": "body", "section": "Numerics", "weight": 1.0} -->

In this section, we present numerical simulation results^11^1The MATLAB codes used to generate these results are available at to illustrate and validate the theoretical findings developed in the previous sections.

<!-- chunk {"id": "body-0052", "role": "body", "section": "Gradient Oracle Analysis", "weight": 1.0} -->

In this subsection, we investigate how different factors affect the behavior of the gradient oracle, as discussed in Section 3. We consider the following benchmark linear system, which has been widely used in prior studies. The system dynamics are given by

<!-- chunk {"id": "body-0053", "role": "body", "section": "Gradient Oracle Analysis", "weight": 1.0} -->

The weight matrices $Q$ and $R$ are chosen as $0.001I_{3}$ and $I_{3}$. The initial covariance matrix $\Sigma_{0} = {10^{- 1}I_{3}}$. The gain $K$, for which we want to evaluate the gradient, is fixed at the optimal solution to $(A,B,{50Q},R)$. In this subsection, we plot the norm of bias (left $y$-axis) and variance (right $y$-axis) of the gradient estimates produced by Algorithms 1 and 2. All results are obtained from Monte Carlo simulations using $500$ independent data samples.

<!-- chunk {"id": "body-0054", "role": "body", "section": "Indirect Method (Algorithm 1)", "weight": 1.0} -->

We set $t_{0} = 50$ and $\Sigma_{\eta} = I_{3}$. Figure 2 ‣ 6.1 Gradient Oracle Analysis ‣ 6 Numerics ‣ A Stochastic Gradient Descent Approach to Design Policy Gradient Methods for LQR") shows the evolution of the estimation error and variance with respect to the iteration index, where increasing amounts of data lead to different gradient estimates at different iterations.

<!-- chunk {"id": "body-0055", "role": "body", "section": "Indirect Method (Algorithm 1)", "weight": 1.0} -->

We observe that both the estimation error (cyan solid line) and the variance (red dashed line) decrease as the number of samples increases. We also plot a reference line (black dashed line) given by ${{8.2 \times 10^{- 4}}i^{- {1/2}}} = {O{(i^{- {1/2}})}}$. The norm of the bias term closely follows this reference line and vanishes at the same rate, which is consistent with the behavior predicted by the gradient oracle in Lemma 7 ‣ 3.1 Indirect Gradient Oracle ‣ 3 Gradient Estimation and Gradient Oracles ‣ A Stochastic Gradient Descent Approach to Design Policy Gradient Methods for LQR"). Furthermore, a larger noise level, $\Sigma_{w} = 10^{- 3}$, results in both higher error and increased variance.

<!-- chunk {"id": "body-0056", "role": "body", "section": "Direct Method (Algorithm 2)", "weight": 1.0} -->

We illustrate separately the effects of the exploration radius $v$. In the following figure, the number of rollout is fixed to $n = 1$ and the length of rollout is fixed at $\ell = 800$. Figure 3 ‣ 6.1 Gradient Oracle Analysis ‣ 6 Numerics ‣ A Stochastic Gradient Descent Approach to Design Policy Gradient Methods for LQR") shows the bias and variance of the gradient estimates for different choices of $v$.

<!-- chunk {"id": "body-0057", "role": "body", "section": "Direct Method (Algorithm 2)", "weight": 1.0} -->

From the figure, we observe that, given a fixed rollout length and number of rollout, the estimation error (black solid line) and variance (red dashed line) are not monotonically increasing or decreasing with respect to $v$. When $v$ is either very small or very large, both the error and variance are relatively high. Focusing on the error, from (36a ‣ 3.2 Direct Gradient Oracle ‣ 3 Gradient Estimation and Gradient Oracles ‣ A Stochastic Gradient Descent Approach to Design Policy Gradient Methods for LQR")) we see that for small $v$, the term $\frac{1}{v}$ dominates the increase, whereas for large $v$ the term proportional to $v$ dominates. A similar phenomenon explains the behavior of the variance, as indicated by (36b ‣ 3.2 Direct Gradient Oracle ‣ 3 Gradient Estimation and Gradient Oracles ‣ A Stochastic Gradient Descent Approach to Design Policy Gradient Methods for LQR")). Additionally, a larger noise level increases both the error and variance, as can be seen when comparing the two groups of lines.

<!-- chunk {"id": "body-0058", "role": "body", "section": "Convergence Analysis of SGD Algorithm", "weight": 1.0} -->

In this subsection, we consider the control of the longitudinal dynamics of a Boeing 747 aircraft.

<!-- chunk {"id": "body-0059", "role": "body", "section": "Convergence Analysis of SGD Algorithm", "weight": 1.0} -->

The initial state and process noise are sampled as ${x_{0} \sim {\mathcal{N}{(0,{10^{- 6}I_{5}})}}},$ and $w_{t} \sim {\mathcal{N}{(0,{10^{- 3}I_{5}})}}$. The weight matrices $Q$ and $R$ are set to identity matrices. The initial control gain $K_{0}$ is chosen as the optimal solution to the LQR problem with cost matrices $(A,B,{40Q},R)$.

<!-- chunk {"id": "body-0060", "role": "body", "section": "Convergence Analysis of SGD with Biased Gradient", "weight": 1.0} -->

Here we illustrate the importance of a vanishing step size and a vanishing bias term using the system described above. The SGD algorithm is implemented according to, where the biased stochastic gradient is given by

<!-- chunk {"id": "body-0061", "role": "body", "section": "Convergence Analysis of SGD with Biased Gradient", "weight": 1.0} -->

with $\Delta_{i}$ being an artificial random matrix whose entries have variance $0.001$. The norm of its mean is bounded by either $0.05$ or $0.05i^{- {1/2}}$, as shown in the legend of Figure 4. This construction results in a biased stochastic gradient. The step size is chosen empirically in accordance with Theorem 6 ‣ 3.1 Indirect Gradient Oracle ‣ 3 Gradient Estimation and Gradient Oracles ‣ A Stochastic Gradient Descent Approach to Design Policy Gradient Methods for LQR"), using $0.05/{\lceil\frac{i^{51/100}}{100}\rceil}$, and is compared against a constant step size $0.05$. Figure 4 presents the evolution of the LQR cost under different combinations of step sizes and bias magnitudes. The results are obtained via a Monte Carlo simulation with $100$ independent runs. For each run, if the $K_{i}$ becomes destabilizing, all subsequent data from that run are discarded.

<!-- chunk {"id": "body-0062", "role": "body", "section": "Convergence Analysis of SGD with Biased Gradient", "weight": 1.0} -->

For the magenta dot-dashed curve, where both the step size and the bias term are fixed, the cost diverges. When the bias term does not vanish but the step size decreases, the cost still diverges. In contrast, when the bias term vanishes but the step size remains constant, the algorithm does not converge to the optimal solution: the cost decreases initially but eventually diverges. Only when both the bias term vanishes and the step size decreases do we observe convergence to the optimal cost. These observations are fully consistent with Theorem 6 ‣ 3.1 Indirect Gradient Oracle ‣ 3 Gradient Estimation and Gradient Oracles ‣ A Stochastic Gradient Descent Approach to Design Policy Gradient Methods for LQR") and highlight the critical interplay between the bias magnitude and the step size in ensuring convergence of SGD with biased gradient oracles.

<!-- chunk {"id": "body-0063", "role": "body", "section": "Indirect Method", "weight": 1.0} -->

The exploration noise is $e_{t} \sim {\mathcal{N}{(0,I_{5})}}$, and the initial data collection length is set to $t_{0} = 50$. Figure 5 illustrates the convergence behavior of the indirect data-driven policy gradient method under different step-size selections. The results are obtained from Monte Carlo simulations using $10$ independent data samples.

<!-- chunk {"id": "body-0064", "role": "body", "section": "Indirect Method", "weight": 1.0} -->

We consider two different step-size sequences. For the black solid line, the step size is chosen according to Theorem 5.1, with the denominator selected to ensure the step size vanishes sufficiently slowly; this sequence is not $\ell_{1}$- and but $\ell_{2}$-summable, as required in Theorem 5.1. Using this step size, the algorithm converges asymptotically to the optimal solution. In contrast, when the step size (red dashed line) is kept constant (without decreasing), the cost initially decreases, but eventually diverges due to the large step size. These results illustrate that a decreasing step-size schedule is critical for ensuring convergence to the optimal policy.

<!-- chunk {"id": "body-0065", "role": "body", "section": "Direct Method", "weight": 1.0} -->

In this subsection, we compare our results with the previous zeroth-order framework proposed, where constant algorithm parameters are used. Specifically, the parameters are configured as ${n = 300},{{\ell = 20},{{v = 0.01},{\eta = 0.002}}}$. In contrast, our method uses time-varying parameters defined as $n_{i} = {n{\lceil\frac{i}{40000}\rceil}}$, $\ell_{i} = {\ell{\lceil\frac{i}{40000}\rceil}}$, ${v_{i} = {v/{\lceil\frac{i^{1/2}}{250}\rceil}}},{\eta_{i} = {\eta/{\lceil\frac{i^{{1/2} + {1/100}}}{250}\rceil}}}$. Figure 6 illustrates the convergence behavior of the two direct data-driven policy gradient methods.

<!-- chunk {"id": "body-0066", "role": "body", "section": "Direct Method", "weight": 1.0} -->

The results are obtained from Monte Carlo simulations using $3$ independent data samples.

<!-- chunk {"id": "body-0067", "role": "body", "section": "Direct Method", "weight": 1.0} -->

We observe that when fixed algorithm parameters are used, the method converges only to a suboptimal solution, and the cost cannot decrease further beyond a certain threshold due to the persistent gradient estimation error. In contrast, our method improves performance by gradually decreasing the step size $\eta_{i}$ and the smoothing parameter $v_{i}$, while increasing the number of samples $n_{i}$ and rollout length $\ell_{i}$. This adaptive strategy reduces the gradient estimation error over time and leads to improved convergence behavior compared. However, we also note that for the direct method, reaching the true optimum is practically infeasible, since doing so would require an unbounded increase in the number of samples.

<!-- chunk {"id": "body-0068", "role": "body", "section": "Conclusion", "weight": 1.5} -->

In this work, we developed a stochastic gradient descent (SGD)--based framework for designing policy gradient algorithms for the Linear Quadratic Regulator (LQR) problem under stochastic disturbances. The gradients obtained from both indirect (identification-based) and direct (zeroth-order) data-driven methods were characterized as biased gradient oracles due to the nonlinear structure of the LQR cost. We established explicit conditions under which an SGD-type algorithm equipped with such biased gradient oracles converges to the optimal policy, under the gradient-dominance and quasi-smoothness properties of the LQR objective. Building on these results, we further analyzed how the indirect and direct data-driven methods satisfy the required oracle conditions, and accordingly designed the corresponding estimation schemes.

<!-- chunk {"id": "body-0069", "role": "body", "section": "Conclusion", "weight": 1.5} -->

Several directions for future research remain. One important extension is to analyze the interaction between the algorithmic dynamics and the closed-loop system dynamics, and to establish joint stability guarantees. Another promising direction is to investigate data-driven policy gradient methods for constrained LQR problems under stochastic dynamics. \\appendices
