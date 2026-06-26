<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

High-Probability Guarantees for Random Zeroth-Order (Stochastic) Gradient Descent

Topics include Gradient descent, Stochastic gradients, Bandits, Optimization, Learning, Stochastic gradient descent.

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Zeroth-order optimization aims to minimize an objective function using only function evaluations, and is therefore fundamental in black-box optimization, hyperparameter tuning, bandit learning, and adversarial machine learning. While classical zeroth-order methods are well understood in expectation, much less is known about their high-probability behavior, especially for smooth and strongly convex objectives. In this paper, we establish high-probability convergence guarantees for random zeroth-order gradient descent in both deterministic and stochastic settings. For deterministic L-smooth and mu-strongly convex objectives of d-dimension, we show that the classical two-query random zeroth-order method finds an epsilon-suboptimal solution with probability at least 1-delta using \[ \mathcal{O}\left( \frac{dL}μ\log\frac{1}{\varepsilon} + \log\frac{1}δ \right) \] function queries. Thus, compared with the standard in-expectation complexity, only an additive logarithmic dependence on the confidence parameter is needed.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

For stochastic objectives, under a bounded-noise condition and without assuming uniformly bounded stochastic gradients, we prove that random zeroth-order stochastic gradient descent achieves an epsilon-suboptimal solution with probability at least 1-delta using \[ \mathcal{O}\left( \frac{ d\log(1/\varepsilon) \left(\log(1/\varepsilon)+\log(1/δ)\right) }{\varepsilon} \right) \] queries. Our results provide high-confidence counterparts to classical expectation-based zeroth-order convergence guarantees and clarify the additional cost required to obtain reliable performance guarantees.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

Zeroth-order (or derivative-free) optimization concerns the minimization of an objective function using only function evaluations, without access to explicit gradient information. Such methods are central in black-box optimization, hyperparameter tuning, bandit problems, and adversarial machine learning, where gradients are either unavailable or prohibitively expensive to compute.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

In this paper, we try to solve the problem of minimizing an $L$-smooth, and $\mu$-strongly convex deterministic function using only zeroth-order information. Standard approaches estimate the gradient through randomized directional sampling or finite differences, and then perform (stochastic) gradient-descent steps based on these estimates.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

Classical analyses of zeroth-order optimization typically provide convergence guarantees in expectation, bounding the average performance over algorithmic randomness or stochasticity in the objective. For example, existing results bound $\mathbb{E}[f(\bm{x}_{t})-f(\bm{x}^{*})]$ as a function of the number of queries with $\bm{x}^{*}$ being the optimal point. While useful, in-expectation guarantees do not provide explicit high-confidence assurances, which are critical in safety-sensitive or high-stakes applications. In contrast, high-probability guarantees provide stronger assurances about the algorithm's performance in practice.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

High-probability convergence analysis of zeroth-order algorithms is substantially more challenging than expectation-based analysis. Zeroth-order gradient estimators, constructed via random directional sampling or finite differences, are inherently noisy, with variance scaling roughly linearly with the dimension $d$. The estimates are sequentially dependent: each iterate $\bm{x}_{t}$ affects the next estimate, creating a martingale-like structure that complicates standard concentration analysis. Moreover, smoothing techniques introduce bias, resulting in a delicate bias--variance tradeoff across iterations. Achieving a global confidence level $1-\delta$ over $T$ steps further requires sophisticated time-uniform concentration inequalities, as naive union bounds would be excessively loose. These factors collectively make high-probability analysis technically intricate and require careful probabilistic reasoning.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Introduction", "weight": 1.5} -->

The challenge intensifies for stochastic objectives, as in Eq. (1.2), where each function evaluation adds randomness atop the estimator noise. Controlling both sources simultaneously demands balancing the estimator's smoothing bias against stochastic noise. The sequential dependence of iterates combined with stochastic function realizations produces a double-martingale structure, complicating concentration further. Ensuring a $1-\delta$ confidence level now often incurs extra logarithmic factors in query complexity and amplifies dimension-dependent variance. Consequently, establishing high-probability convergence for stochastic zeroth-order methods is far more complex than in the deterministic case, requiring advanced probabilistic tools and meticulous iteration-wise analysis.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Introduction", "weight": 1.5} -->

In this work, we address this gap by establishing high-probability convergence guarantees for zeroth-order gradient descent in both deterministic and stochastic settings. Our main contributions are as follows: Deterministic objectives: For an $L$-smooth and $\mu$-strongly convex function, zeroth-order gradient descent converges to the global optimum with probability at least $1-\delta$, using function queries. Compared with the query complexity holding in expectation, our result shows that random zeroth-order algorithms only require only $\mathcal{O}(\log\frac{1}{\delta})$ extra queries to achieve a $1-\delta$ probability solution.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Introduction", "weight": 1.5} -->

Stochastic objectives: For $f(\bm{x})=\mathbb{E}_{\xi}[f(\bm{x};\xi)]$, the random zeroth-order gradient descent converges to the global optimum with probability at least $1-\delta$, with query complexity Compared with the query complexity of zeroth-order stochastic gradient holding in expectation which is $\mathcal{O}\left(\frac{d}{\varepsilon}\right)$, our result shows that random zeroth-order stochastic gradient descent methods only take $\mathcal{O}\left(\log\frac{1}{\varepsilon}\left(\log\frac{1}{\varepsilon}+\log\frac{1}{\delta}\right)\right)$ times extra queries to find an $\varepsilon$-suboptimal solution with a probability at least $1-\delta$.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Related Works", "weight": 1.0} -->

Zeroth-order optimization has received significant attention due to its ability to handle optimization problems when gradient information is unavailable. In this section, we review related works in three main directions which closely related to our work: random zeroth-order gradient descent, online convex optimization (OCO) with bandit feedback, and (zeroth-order) stochastic gradient descent.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Random Zeroth-Order Gradient Descent", "weight": 1.0} -->

Random zeroth-order gradient descent method considers the minimization of a deterministic function when only function evaluations are available. A seminal contribution in this direction is by Nesterov & Spokoiny established convergence guarantees of random zeroth-order gradient descent with the Gaussian smoothing. Their method achieves convergence rates comparable to first-order methods up to a dimension-dependent factor and includes an accelerated variant for convex objectives.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Random Zeroth-Order Gradient Descent", "weight": 1.0} -->

Subsequent works have extended the analysis to various settings. For example, Ghadimi & Lan, studied deterministic and stochastic first- and zeroth-order methods for nonconvex optimization, highlighting the effectiveness of multi-point gradient approximations. Ye et al., 2025b proposed Hessian-aware zeroth-order optimization which exploits the second order information to achieve faster convergence rate. However, all these works focus on the convergence analysis holding in expectation.

<!-- chunk {"id": "body-0014", "role": "body", "section": "Random Zeroth-Order Gradient Descent", "weight": 1.0} -->

Recently, Ye et al., 2025a showed that the random zeroth-order optimization with proper search direction and multi-point feedbacks can converge in high probability. Their work relied a large batch of feedbacks to guarantee a decay holding with a high probability for each iteration. Thus, Ye et al., 2025a can only achieve a query complexity $\mathcal{O}\left(\frac{(d+\log(1/\delta))L}{\mu}\log\frac{1}{\varepsilon}\log\log\frac{1}{\varepsilon}\right)$. The detailed comparison is listed in Table 1.

<!-- chunk {"id": "body-0015", "role": "body", "section": "Random Zeroth-Order Gradient Descent", "weight": 1.0} -->

Queries per Iter $\mathcal{O}\Big(\frac{dL}{\mu}\log\frac{1}{\varepsilon}\Big)$ $\mathcal{O}(\log\frac{1}{\varepsilon\delta})$ $\mathcal{O}\left(\frac{(d+\log(1/\delta))L}{\mu}\log\frac{1}{\varepsilon}\log\log\frac{1}{\varepsilon}\right)$ $\mathcal{O}\Big(\frac{dL}{\mu}\log\frac{1}{\varepsilon}+\log\frac{1}{\delta}\Big)$ Table 1: Comparison of query complexities for zeroth-order gradient descent. The table juxtaposes the most related bounds with our high-probability guarantees.

<!-- chunk {"id": "body-0016", "role": "body", "section": "Online Convex Optimization (OCO) with Bandit Feedback", "weight": 1.0} -->

In the online setting, zeroth-order methods have been extensively applied to bandit convex optimization. Flaxman et al., introduced single-point gradient estimators, providing expected regret bounds for convex losses when only function evaluations are observed. Later works obtained sharper regret bounds for bandit convex optimization using two-point (multi-point) feedback. Recently, Yu et al., showed that OCO with two-point feedback can achieve the optimal regret holding in expectation, which is optimal in both the time zone and the dimension for the strongly convex function. Almost the same time, Ye, obtain the same result holding with a high probability. Through the online to batch conversion technique, the result of Ye, can directly derive that random zeroth-order stochastic gradient descent can achieve a $\mathcal{O}\left(d\log(1/\varepsilon)/\varepsilon\right)$ query complexity holding with high probability. However, in the OCO setting, a bounded stochastic gradient is necessary to achieve the optimal regret. In contrast, our analysis does *not* require the bounded stochastic gradient.

<!-- chunk {"id": "body-0017", "role": "body", "section": "(Zeroth-order) Stochastic Gradient Descent", "weight": 1.0} -->

Stochastic gradient descent (SGD) is another closely related line of work. The classical stochastic approximation framework dates back to Robbins & Monro who introduced an iterative method for solving stochastic root-finding problems. For strongly convex objectives with bounded stochastic gradient, SGD-type methods can achieve the optimal $O(1/T)$ convergence rate after $T$ stochastic gradient queries holding with high probability. When the function is additionally smooth and the noise has bounded variance, then SGD-type methods can achieve the optimal $O(1/T)$ rate holding in expectation. However, without a bounded-gradient assumption, it becomes substantially more challenging to achieve the optimal rate holding with high probability. More recently, Liu & Zhou, developed a general framework for high-probability convergence of stochastic gradient methods under subgaussian noise, achieving an $\mathcal{O}(\log T/T)$ convergence rate without the unbounded gradient assumption.

<!-- chunk {"id": "body-0018", "role": "body", "section": "(Zeroth-order) Stochastic Gradient Descent", "weight": 1.0} -->

Stochastic zeroth-order optimization can be viewed as a derivative-free counterpart of stochastic gradient methods. Modern stochastic zeroth-order methods typically use randomized finite-difference or smoothing-based gradient estimators. Duchi et al., analyzed one- and two-point zeroth-order schemes and showed that two function evaluations can lead to nearly optimal rates up to dimension-dependent factors. Shamir, gave a simple optimal algorithm for bandit and zeroth-order convex optimization with two-point feedback. Ghadimi & Lan, studied stochastic first- and zeroth-order methods for nonconvex stochastic programming and derived complexity bounds for finding approximate stationary points, together with improved large-deviation guarantees through post-optimization procedures. More recently, when the objective function is smooth and strongly convex, several works showed that stochastic zeroth-order methods can achieve an expected query complexity $\mathcal{O}\left(d/\varepsilon\right)$.

<!-- chunk {"id": "body-0019", "role": "body", "section": "(Zeroth-order) Stochastic Gradient Descent", "weight": 1.0} -->

We provide a detailed comparison of query complexities for zeroth-order SGD in Table 2 Stochastic Gradient Descent. ‣ 1.1 Related Works ‣ 1 Introduction ‣ High-Probability Guarantees for Random Zeroth-Order Gradient Descent").

<!-- chunk {"id": "body-0020", "role": "body", "section": "(Zeroth-order) Stochastic Gradient Descent", "weight": 1.0} -->

$\mathcal{O}\left(\frac{d\cdot\left(\log\frac{1}{\varepsilon}\right)\left(\log\frac{1}{\varepsilon}+\log\frac{1}{\delta}\right)}{\varepsilon}\right)$ Table 2: Comparison of query complexities for zeroth-order gradient descent.

<!-- chunk {"id": "body-0021", "role": "body", "section": "(Zeroth-order) Stochastic Gradient Descent", "weight": 1.0} -->

We assume that the function is smooth and strongly convex except that Rakhlin et al., don’t require function be smooth. The works of Bottou et al. Rakhlin et al. Liu & Zhou, focus on convergence rates of the first-order SGD. We time d to their iteration complexities to obtain the query complexities.

<!-- chunk {"id": "body-0022", "role": "body", "section": "Assumptions", "weight": 1.0} -->

First, we introduce the first assumption that is widely used in the convergence analysis.

<!-- chunk {"id": "body-0023", "role": "body", "section": "Assumption 1", "weight": 1.0} -->

The function $f(\bm{x})$ is $L$-smooth and $\mu$-strongly convex. That is, for any $\bm{x},\bm{y}\in\mathbb{R}^{d}$, it holds that When the function $f(\bm{x})$ can be represented as Eq. (1.2), we will introduce the following two extra assumptions.

<!-- chunk {"id": "body-0024", "role": "body", "section": "Assumption 2", "weight": 1.0} -->

We assume that the stochastic gradient $\nabla f(\bm{x};\;\xi)$ is an unbiased estimation of $\nabla f(\bm{x})$, that is, $\mathbb{E}_{\xi}[\nabla f(\bm{x};\;\xi)]=\nabla f(\bm{x})$.

<!-- chunk {"id": "body-0025", "role": "body", "section": "Assumption 3 (Bounded Noise Assumption)", "weight": 1.0} -->

We also assume that with a probability $1$, it holds that Assumption 2 is the standard assumption in the analysis of stochastic gradient descent. Assumption 3. ‣ 2.1 Assumptions ‣ 2 Assumptions and Preliminaries ‣ High-Probability Guarantees for Random Zeroth-Order Gradient Descent") is also widely used. A more popular assumption is the bounded variance assumption. However, based on this assumption, we can only achieve the optimal convergence rate holding in expectation. Furthermore, if the objective function $f(\bm{x})=\frac{1}{n}\sum_{i=1}^{n}f_{i}(\bm{x})$, the bounded variance assumption, that is, $\mathbb{E}_{i}\left[\left\|\nabla f(\bm{x})-\nabla f_{i}(\bm{x})\right\|^{2}\right]\leq\sigma_{1}^{2}$, will directly imply that Assumption 3.

<!-- chunk {"id": "body-0026", "role": "body", "section": "Assumption 3 (Bounded Noise Assumption)", "weight": 1.0} -->

‣ 2.1 Assumptions ‣ 2 Assumptions and Preliminaries ‣ High-Probability Guarantees for Random Zeroth-Order Gradient Descent") hold. This can be obtained as Furthermore, if the noise only satisfies the bounded variance, without the extra assumption of the bounded gradient, one can *not* achieve a high probability convergence analysis to my best knowledge. In this work, we do *not* require the bounded gradient assumption, thus, we need a more strict assumption on the noise.

<!-- chunk {"id": "body-0027", "role": "body", "section": "Assumption 3 (Bounded Noise Assumption)", "weight": 1.0} -->

Liu & Zhou, assume that the noise is subgaussian and achieve a convergence rate $\mathcal{O}\left(\log T/T\right)$ when the iteration number $T$ is unknown. In this paper, we also consider the case that $T$ is unknown. Our bounded noise assumption is a little more strict than the subgaussian assumption. In fact, our convergence analysis can be easily extend to the case of subgaussian noise. A direct extension can be achieved using the fact that the subgaussian noise will imply Assumption 3. ‣ 2.1 Assumptions ‣ 2 Assumptions and Preliminaries ‣ High-Probability Guarantees for Random Zeroth-Order Gradient Descent") holds with a high probability at least $1-\delta$. This will only introduce an extra $\log(T/\delta)$ times queries. However, our work mainly focuses on the high probability convergence of *zeroth-order* SGD. The bounded noise assumption will help us to develop techniques to achieve high probability convergence analysis of zeroth-order SGD.

<!-- chunk {"id": "body-0028", "role": "body", "section": "Assumption 3 (Bounded Noise Assumption)", "weight": 1.0} -->

1: Input: Initial vector x0, number of total iteration T, and step size ηt. 4: Access to the value of f(xt + αut) and f(xt − αut) and construct the approximate gradient $$\bm{g}(\bm{x}_{t})=\frac{f(\bm{x}_{t}+\alpha\bm{u}_{t})-f(\bm{x}_{t}-\alpha\bm{u}_{t})}{2\alpha}\bm{u}_{t}.$$ Algorithm 1 Zeroth-order Gradient Descent

<!-- chunk {"id": "body-0029", "role": "body", "section": "Main Results", "weight": 1.0} -->

In this section, we will provide the convergence rates of Algorithm 1 and Algorithm 2 holding with high probabilities. Accordingly, we will also give their responding queries complexities. First, we will give the results of Algorithm 1 in the following theorem.

<!-- chunk {"id": "body-0030", "role": "body", "section": "Remark 1", "weight": 1.0} -->

To find an $\varepsilon$-suboptimal point, Nesterov & Spokoiny, requires that Comparing $T_{1}$ in above equation with our iteration $T$ in Eq. (3.2), to find an $\varepsilon$-suboptimal solution with a high probability $1-\delta$, Algorithm 1 only requires $\log\frac{1}{\delta}$ extra queries.

<!-- chunk {"id": "body-0031", "role": "body", "section": "Remark 1", "weight": 1.0} -->

At the same time, comparing $\alpha_{1}$ in Eq (3.4) with $\alpha$ in Eq. (3.3), to find an $\varepsilon$-suboptimal solution with a high probability, the smooth parameter $\alpha$ of Algorithm 1 should be set almost the same to the case holding in expectation.

<!-- chunk {"id": "body-0032", "role": "body", "section": "Remark 1", "weight": 1.0} -->

Above comparison shows that to find an $\varepsilon$-suboptimal solution with a probability at least $1-\delta$, the extra price of Algorithm 1 is only taking $\mathcal{O}(\log\frac{1}{\delta})$ extra queries.

<!-- chunk {"id": "body-0033", "role": "body", "section": "Remark 1", "weight": 1.0} -->

Next, we will provide the convergence of zeroth-order stochastic gradient descent (Algorithm 2) in the following theorem.

<!-- chunk {"id": "body-0034", "role": "body", "section": "Remark 2", "weight": 1.0} -->

First, we compare our work with Liu & Zhou, which provides a high probability convergence analysis of stochastic gradient descent with the iteration number $T$ unknown. Liu & Zhou, achieve an iteration complexity Compared with our query complexity in Eq. (3.7), our complexity has an extra factor of $d$ which is natural for zeroth-order methods due to the fact that an exact gradient estimation can be achieved via $d$ times finite differences. The additional logarithmic term $\log(1/\varepsilon)$ stems from the requirement of event $\mathcal{E}_{\Delta_{K}}$ holding for each iteration.

<!-- chunk {"id": "body-0035", "role": "body", "section": "Remark 2", "weight": 1.0} -->

Wang et al., provide a query complexity $\mathcal{O}\left(\frac{d}{\varepsilon}\right)$ holding in expectation. Our complexity has extra $\log(1/\varepsilon)$ terms which come from the requirement of event $\mathcal{E}_{\Delta_{K}}$ holding for each iteration. The extra price for a high probability rate is very small which is up to $\log\frac{1}{\varepsilon}$ times.

<!-- chunk {"id": "body-0036", "role": "body", "section": "Convergence Analysis of Random Zeroth-Order Gradient Descent", "weight": 1.0} -->

In this section, we will focus on the detailed convergence analysis of random zero-order gradient descent (Algorithm 1).

<!-- chunk {"id": "body-0037", "role": "body", "section": "Remark 3", "weight": 1.0} -->

In Lemma 2, we assume that $\{\bm{x}_{t}\}$ generated by Algorithm 1 satisfies $\left\|\nabla f(\bm{x}_{t})\right\|\neq 0$. This is a reasonable assumption. When $f(\bm{x})$ is strongly convex, there is only one optimal point for $f(\bm{x})$. At the same time, $\left\|\nabla f(\bm{x}_{t})\right\|=0$ implies that $\bm{x}_{t}$ is the optimal point. For a random algorithm, the probability to find an optimal point of zero measurement is also zero.

<!-- chunk {"id": "body-0038", "role": "body", "section": "Remark 4", "weight": 1.0} -->

Lemma 2 is the key to our high-probability convergence of random zero-order gradient descent. Instead of analyzing how the function value will decay after one-step, we consider the function value decay after $T$-step updates. If we analyze the one-step update, with a proper step size, we can obtain that Furthermore, the value $(\bm{u}_{t}^{\top}\nabla f(\bm{x}_{t}))^{2}\sim\left\|\nabla f(\bm{x})\right\|^{2}\cdot\chi^{2}$ will dominate the convergence property. Unfortunately, for a one-step update, we can *not* lower bound the value of $(\bm{u}_{t}^{\top}\nabla f(\bm{x}_{t}))^{2}$ with a high probability since the lower bound of $\chi^{2}$ can not hold with a high probability.

<!-- chunk {"id": "body-0039", "role": "body", "section": "Remark 4", "weight": 1.0} -->

The common way to overcome this dilemma is taking expectation since $\mathbb{E}[\xi^{2}]=1$. This is the reason why the convergence analysis of random zeroth-order algorithms commonly holds in expectation. Instead, Lemma 2 analyze function value decay after $T$-step updates to overcome the problem that one can not lower bound $\chi^{2}$ with high probability.

<!-- chunk {"id": "body-0040", "role": "body", "section": "Remark 5", "weight": 1.0} -->

We take a step size $\eta_{t}=\Omega(\frac{1}{\left\|\bm{u}_{t}\right\|^{2}L})$ in Lemma 2 instead of $\Omega(\frac{1}{dL})$ in the popular convergence analysis of random zeroth-order gradient descent. This is also important in our convergence analysis. By this step size, we have $\left(\frac{\bm{u}_{t}^{\top}\nabla f(\bm{x}_{t})}{\left\|\bm{u}_{t}\right\|\cdot\left\|\nabla f(\bm{x}_{t})\right\|}\right)^{2}\sim\text{Beta}(\frac{1}{2},\;\frac{d-1}{2})$. By this nice property and well-known results of beta distribution, we can obtain our high probability convergence analysis.

<!-- chunk {"id": "body-0041", "role": "body", "section": "Convergence Analysis of Zeroth-Order Stochastic Gradient Descent", "weight": 1.0} -->

In this section, we will focus on the detailed convergence analysis of random zero-order stochastic gradient descent (Algorithm 2).

<!-- chunk {"id": "body-0042", "role": "body", "section": "Linear Martingale Bound", "weight": 1.0} -->

In this section, we will bound the second term of the right hand of Eq. (5.7).

<!-- chunk {"id": "body-0043", "role": "body", "section": "Quadratic Term Bound", "weight": 1.0} -->

In this section, we will bound the third term of the right hand of Eq. (5.7). Similar to upper bounding the second term, we will first provide an upper bound of $\sum_{k=0}^{K-1}\frac{\rho_{K,k}}{T_{k}^{2}}\cdot\left\|\bm{u}_{k}^{\top}\bm{e}_{k}\right\|^{2}$ holding with a high probability. Then, combining with Lemma 10, we obtain the final upper bound.

<!-- chunk {"id": "body-0044", "role": "body", "section": "Upper Bound Related to Parameter $\\alpha$", "weight": 1.0} -->

Now we will bound the forth term of the right hand of Eq. (5.7) which is related to the smooth parameter $\alpha$.

<!-- chunk {"id": "body-0045", "role": "body", "section": "Base case", "weight": 1.0} -->

When $K=0$, since $T_{0}$ is deterministic, by the value of $\mathcal{C}$ in Eq. (3.6), we can directly obtain that Induction Hypothesis. Fixing any $K\in\{1,\dots,T-1\}$, we assume that event $\mathcal{E}_{\Delta_{K}}$ holds with a probability at least $1-\delta_{K}^{(\Delta)}$. That is, for every $k=0,\dots,K-1$, it holds that Assuming events $\mathcal{E}_{\rho_{K}}$ and $\mathcal{E}{\rho_{K,k}}$ (defined in Eq. (5.3) and (5.4)) hold, then Eq. (5.7) in Lemma 8 holds. Next, combining with induction hypothesis, we will bound the four terms on the right-hand side of Eq. (5.7) separately.

<!-- chunk {"id": "body-0046", "role": "body", "section": "The Initial Term", "weight": 1.0} -->

By Eq. (5.16. ‣ 5.4 Induction Proof of Theorem 3 ‣ 5 Convergence Analysis of Zeroth-Order Stochastic Gradient Descent ‣ High-Probability Guarantees for Random Zeroth-Order Gradient Descent")), we have $\rho_{K}\Delta_{0}\leq c_{\rho}\frac{T_{0}}{T_{K}}\Delta_{0}$. Hence, by the fact that $\mathcal{C}\geq 8c_{\rho}T_{0}\Delta_{0}/(d\Lambda^{2})$ in Eq. (3.6), we can obtain that Furthermore, above equation only depends on the event $\mathcal{E}_{\rho_{K}}$ defined in Eq. (5.3). Thus, it holds that

<!-- chunk {"id": "body-0047", "role": "body", "section": "Linear Martingale Bound", "weight": 1.0} -->

We may apply Lemma 12 with the deterministic upper bounds $\bar{\Delta}_{k}=\mathcal{C}d\Lambda^{2}/T_{k}$. Combining with Eq. (5.16. ‣ 5.4 Induction Proof of Theorem 3 ‣ 5 Convergence Analysis of Zeroth-Order Stochastic Gradient Descent ‣ High-Probability Guarantees for Random Zeroth-Order Gradient Descent")) and Eq. (5.13), we obtain Thus, we can obtain that Combining with Eq. (5.14), we can obtain that Moreover, to achieve above, it requires the events $\mathcal{E}_{\rho_{K,k}}$ with $k=0,\dots,K-1$, the induction hypothesis $\mathcal{E}_{\Delta_{K}}$ and Lemma 12 hold simultaneously. That is, by the union bound, we have

<!-- chunk {"id": "body-0048", "role": "body", "section": "Upper Bound Related to Parameter $\\alpha$", "weight": 1.0} -->

Combining Lemma 15 and Lemma 31, we can obtain that where the last inequality is because of Furthermore, above equation holds only depending the event $\mathcal{E}_{\alpha_{K}}$, that is, Step 6: Conclusion of the induction step.

<!-- chunk {"id": "body-0049", "role": "body", "section": "Upper Bound Related to Parameter $\\alpha$", "weight": 1.0} -->

Combining Eq. (5.7), (5.21), (5.23), (5.25), and (5.27), we conclude that This proves the induction step.

<!-- chunk {"id": "body-0050", "role": "body", "section": "Upper Bound Related to Parameter $\\alpha$", "weight": 1.0} -->

By Eq. (5.22), (5.24), (5.26), and (5.28), we can obtain that where the last equality is because of $\delta_{K}^{(\Delta)}=K/T$ and we set

<!-- chunk {"id": "body-0051", "role": "body", "section": "Conclusion", "weight": 1.5} -->

In this paper, we studied high-probability convergence guarantees for zeroth-order gradient descent methods for smooth and strongly convex optimization. Unlike most classical analyses, which establish convergence only in expectation, our results provide explicit confidence guarantees for the performance of random zeroth-order algorithms.

<!-- chunk {"id": "body-0052", "role": "body", "section": "Conclusion", "weight": 1.5} -->

For deterministic objectives, we proved that random zeroth-order gradient descent achieves an $\varepsilon$-suboptimal solution with probability at least $1-\delta$ using function queries. This matches the classical expectation-based query complexity up to only an additive logarithmic dependence on the confidence parameter. In particular, the result shows that the standard two-query random zeroth-order method can provide strong high-probability guarantees without requiring large batches of function evaluations at each iteration.

<!-- chunk {"id": "body-0053", "role": "body", "section": "Conclusion", "weight": 1.5} -->

We further considered stochastic objectives, where both randomized directional sampling and stochastic function evaluations introduce additional uncertainty. Under a bounded-noise assumption, and without imposing a uniformly bounded stochastic-gradient condition, we established a high-probability query complexity of This result gives a high-confidence analogue of the standard expected convergence guarantees for stochastic zeroth-order methods, with only additional logarithmic factors in the accuracy and confidence parameters.

<!-- chunk {"id": "body-0054", "role": "body", "section": "Conclusion", "weight": 1.5} -->

Overall, our analysis demonstrates that random zeroth-order gradient descent can achieve reliable high-probability performance guarantees in both deterministic and stochastic smooth strongly convex optimization. These results narrow the gap between expectation-based and high-probability theory for zeroth-order methods, and suggest several directions for future work, including improving the logarithmic factors in the stochastic setting, extending the analysis to weaker noise assumptions, and developing high-probability guarantees for broader classes of nonconvex or nonsmooth zeroth-order problems.
