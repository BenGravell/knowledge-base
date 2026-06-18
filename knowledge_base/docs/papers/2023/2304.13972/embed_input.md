<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Convergence of Adam under Relaxed Assumptions

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

In this paper, we provide a rigorous proof of convergence of the Adaptive Moment Estimate (Adam) algorithm for a wide class of optimization objectives. Despite the popularity and efficiency of the Adam algorithm in training deep neural networks, its theoretical properties are not yet fully understood, and existing convergence proofs require unrealistically strong assumptions, such as globally bounded gradients, to show the convergence to stationary points. In this paper, we show that Adam provably converges to epsilon-stationary points with O(epsilon^(-4)) gradient complexity under far more realistic conditions. The key to our analysis is a new proof of boundedness of gradients along the optimization trajectory of Adam, under a generalized smoothness assumption according to which the local smoothness (i.e., Hessian norm when it exists) is bounded by a sub-quadratic function of the gradient norm. Moreover, we propose a variance-reduced version of Adam with an accelerated gradient complexity of O(epsilon^(-3)).

<!-- chunk {"id": "body-0003", "role": "body", "section": "Introduction", "weight": 1.5} -->

In this paper, we study the non-convex unconstrained stochastic optimization problem

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

The Adaptive Moment Estimation (Adam) algorithm has become one of the most popular optimizers for solving when $f$ is the loss for training deep neural networks. Owing to its efficiency and robustness to hyper-parameters, it is widely applied or even sometimes the default choice in many machine learning application domains such as natural language processing, generative adversarial networks, computer vision, and reinforcement learning. It is also well known that Adam significantly outperforms stochastic gradient descent (SGD) for certain models like transformer.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

Despite its success in practice, theoretical analyses of Adam are still limited. The original proof of convergence in was later shown by Reddi et al. to contain gaps. The authors in also showed that for a range of momentum parameters chosen *independently with the problem instance*, Adam does not necessarily converge even for convex objectives. However, in deep learning practice, the hyper-parameters are in fact *problem-dependent* as they are usually tuned after given the problem and weight initialization. Recently, there have been many works proving the convergence of Adam for non-convex functions with various assumptions and problem-dependent hyper-parameter choices. However, these results leave significant room for improvement. For example, prove the convergence to stationary points assuming the gradients are bounded by a constant, either explicitly or implicitly. On the other hand, consider weak assumptions, but their convergence results are still limited. See Section 2 for more detailed discussions of related works.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

To address the above-mentioned gap between theory and practice, we provide a new convergence analysis of Adam *without assuming bounded gradients*, or equivalently, Lipschitzness of the objective function. In addition, we also relax the standard global smoothness assumption, i.e., the Lipschitzness of the gradient function, as it is far from being satisfied in deep neural network training. Instead, we consider a more general, relaxed, and non-uniform smoothness condition according to which the local smoothness (i.e., Hessian norm when it exists) around $x$ is bounded by a sub-quadratic function of the gradient norm $\left\| {{\nabla f}{(x)}} \right\|$ (see Definition 3.2 and Assumption 2 for the details). This generalizes the $(L_{0},L_{1})$ smoothness condition proposed by based on language model experiments. Even though our assumptions are much weaker and more realistic, we can still obtain the same $\mathcal{O}{(\epsilon^{- 4})}$ gradient complexity for convergence to an $\epsilon$-stationary point.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

The key to our analysis is a new technique to obtain a high probability, constant upper bound on the gradients along the optimization trajectory of Adam, without assuming Lipschitzness of the objective function. In other words, it essentially turns the bounded gradient assumption into a result that can be directly proven. Bounded gradients imply bounded stepsize at each step, with which the analysis of Adam essentially reduces to the simpler analysis of AdaBound. Furthermore, once the gradient boundedness is achieved, the analysis under the generalized non-uniform smoothness assumption is not much harder than that under the standard smoothness condition. We will introduce the technique in more details in Section 5. We note that the idea of bounding gradient norm along the trajectory of the optimization algorithm can be use in other problems as well. For more details, we refer the reader to our concurrent work in which we present a set of new techiniques and methods for bounding gradient norm for other optimization algorithms under a generalized smoothness condition.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Introduction", "weight": 1.5} -->

Another contribution of this paper is to show that the gradient complexity of Adam can be further improved with variance reduction methods. To this end, we propose a variance-reduced version of Adam by modifying its momentum update rule, inspired by the idea of the STORM algorithm. Under additional generalized smoothness assumption of the component function $f{( \cdot,\xi)}$ for each $\xi$, we show that this provably accelerates the convergence with a gradient complexity of $\mathcal{O}{(\epsilon^{- 3})}$. This rate improves upon the existing result of where the authors obtain an asymptotic convergence of their approach to variance reduction for Adam in the non-convex setting, under the bounded gradient assumption.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Contributions", "weight": 1.0} -->

In light of the above background, we summarize our main contributions as follows.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Contributions", "weight": 1.0} -->

We develop a new analysis to show that Adam converges to stationary points under relaxed assumptions. In particular, we do not assume bounded gradients or Lipschitzness of the objective function. Furthermore, we also consider a generalized non-uniform smoothness condition where the local smoothness or Hessian norm is bounded by a *sub-quadratic* function of the gradient norm. Under these more realistic assumptions, we obtain a *dimension free* gradient complexity of $\mathcal{O}{(\epsilon^{- 4})}$ if the gradient noise is centered and bounded.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Contributions", "weight": 1.0} -->

We generalize our analysis to the setting where the gradient noise is centered and has sub-Gaussian norm, and show the convergence of Adam with a gradient complexity of $\mathcal{O}{({\epsilon^{- 4}{\log^{3.25}{({1/\epsilon})}}})}$.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Contributions", "weight": 1.0} -->

We propose a variance-reduced version of Adam (VRAdam) with provable convergence guarantees. In particular, we obtain the accelerated $\mathcal{O}{(\epsilon^{- 3})}$ gradient complexity.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Convergence of Adam", "weight": 1.0} -->

Adam was first proposed by Kingma and Ba with a theoretical convergence guarantee for convex functions. However, Reddi et al. found a gap in the proof of this convergence analysis, and also constructed counter-examples for a range of hyper-parameters on which Adam does not converge. That being said, the counter-examples depend on the hyper-parameters of Adam, i.e., they are constructed after picking the hyper-parameters. Therefore, it does not rule out the possibility of obtaining convergence guarantees for problem-dependent hyper-parameters, as also pointed out.

<!-- chunk {"id": "body-0014", "role": "body", "section": "Convergence of Adam", "weight": 1.0} -->

Many recent works have developed convergence analyses of Adam with various assumptions and hyper-parameter choices. Zhou et al. show Adam with certain hyper-parameters can work on the counter-examples of. De et al. prove convergence for general non-convex functions assuming gradients are bounded and the signs of stochastic gradients are the same along the trajectory. The analysis in also relies on the bounded gradient assumption. Guo et al. assume the adaptive stepsize is upper and lower bounded by two constants, which is not necessarily satisfied unless assuming bounded gradients or considering the AdaBound variant. consider very weak assumptions. However, they show either 1) "convergence" only to some neighborhood of stationary points with a constant radius, unless assuming the strong growth condition; or 2) convergence to stationary points but with a slower rate.

<!-- chunk {"id": "body-0015", "role": "body", "section": "Variants of Adam", "weight": 1.0} -->

After Reddi et al. pointed out the non-convergence issue with Adam, various variants of Adam that can be proved to converge were proposed. For example, AMSGrad and AdaFom modify the second order momentum so that it is non-decreasing. AdaBound explicitly imposes upper and lower bounds on the second order momentum so that the stepsize is also bounded. AdaShift uses a new estimate of the second order momentum to correct the bias. There are also some works that provide convergence guarantees of these variants. One closely related work to ours is, which considers a variance-reduced version of Adam by combining Adam and SVRG. However, they assume bounded gradients and can only get an asymptotic convergence in the non-convex setting.

<!-- chunk {"id": "body-0016", "role": "body", "section": "Generalized smoothness condition", "weight": 1.0} -->

Generalizing the standard smoothness condition in a variety of settings has been a focus of many recent papers. Recently, proposed a generalized smoothness condition called $(L_{0},L_{1})$ smoothness, which assumes the local smoothness or Hessian norm is bounded by an affine function of the gradient norm. The assumption was well-validated by extensive experiments conducted on language models. Various analyses of different algorithms under this condition were later developed. One recent closely-related work is which studies converges of Adam under the $(L_{0},L_{1})$ smoothness condition. However, their results are still limited, as we have mentioned above. In this paper, we consider an even more general smoothness condition where the local smoothness is bounded by a sub-quadratic function of the gradient norm, and prove the convergence of Adam under this condition. In our concurrent work, we further analyze various other algorithms in both convex and non-convex settings under similar generalized smoothness conditions following the same key idea of bounding gradients along the trajectory.

<!-- chunk {"id": "body-0017", "role": "body", "section": "Variance reduction methods", "weight": 1.0} -->

The technique of variance reduction was introduced to accelerate convex optimization in the finite-sum setting. Later, many works studied variance-reduced methods in the non-convex setting and obtained improved convergence rates for standard smooth functions. For example, SVRG and SCSG improve the $\mathcal{O}{(\epsilon^{- 4})}$ gradient complexity of stochastic gradient descent (SGD) to $\mathcal{O}{(\epsilon^{- {10/3}})}$. Many new variance reduction methods were later proposed to further improve the complexity to $\mathcal{O}{(\epsilon^{- 3})}$, which is optimal and matches the lower bound. Recently, obtained the $\mathcal{O}{(\epsilon^{- 3})}$ complexity for the more general $(L_{0},L_{1})$ smooth functions. Our variance-reduced Adam is motivated by the STORM algorithm proposed, where an additional term is added in the momentum update to correct the bias and reduce the variance.

<!-- chunk {"id": "body-0018", "role": "body", "section": "Description of the Adam algorithm", "weight": 1.0} -->

The formal definition of Adam proposed in is shown in Algorithm 1, where Lines 5--9 describe the update rule of iterates ${\{ x_{t}\}}_{1 \leq t \leq T}$. Lines 5--6 are the updates for the first and second order momentum, $m_{t}$ and $v_{t}$, respectively. In Lines 7--8, they are re-scaled to ${\hat{m}}_{t}$ and ${\hat{v}}_{t}$ in order to correct the initialization bias due to setting $m_{0} = v_{0} = 0$.

<!-- chunk {"id": "body-0019", "role": "body", "section": "Assumptions", "weight": 1.0} -->

In what follows below, we will state our main assumptions for analysis of Adam.

<!-- chunk {"id": "body-0020", "role": "body", "section": "Function class", "weight": 1.0} -->

We start with a standard assumption in optimization on the objective function $f$ whose domain lies in a Euclidean space with dimension $d$.

<!-- chunk {"id": "body-0021", "role": "body", "section": "Assumption 1", "weight": 1.0} -->

The objective function $f$ is *differentiable* and *closed* within its *open domain* ${\operatorname{dom}{(f)}} \subseteq {\mathbb{R}}^{d}$ and is bounded from below, i.e., $f^{\ast}:={\inf_{x}{f{(x)}}} > {- \infty}$.

<!-- chunk {"id": "body-0022", "role": "body", "section": "Remark 3.1", "weight": 1.0} -->

A function $f$ is said to be closed if its sub-level set $\{{x \in {\operatorname{dom}{(f)}}}\mid{{f{(x)}} \leq a}\}$ is closed for each $a \in {\mathbb{R}}$. In addition, a continuous function $f$ over an open domain is closed if and only $f{(x)}$ tends to infinity whenever $x$ approaches to the boundary of $\operatorname{dom}{(f)}$, which is an important condition to ensure the iterates of Adam with a small enough stepsize $\eta$ stay within the domain with high probability. Note that this condition is mild since any continuous function defined over the entire space ${\mathbb{R}}^{d}$ is closed.

<!-- chunk {"id": "body-0023", "role": "body", "section": "Remark 3.1", "weight": 1.0} -->

Besides Assumption 1, the only additional assumption we make regarding $f$ is that its local smoothness is bounded by a sub-quadratic function of the gradient norm. More formally, we consider the following $(\rho,L_{0},L_{\rho})$ smoothness condition with $0 \leq \rho < 2$.

<!-- chunk {"id": "body-0024", "role": "body", "section": "Remark 3.3", "weight": 1.0} -->

When $\rho = 1$, Definition 3.2 reduces to the $(L_{0},L_{1})$ smoothness condition. When $\rho = 0$ or $L_{\rho} = 0$, it reduces to the standard smoothness condition.

<!-- chunk {"id": "body-0025", "role": "body", "section": "Assumption 2", "weight": 1.0} -->

The standard smooth function class is very restrictive as it only contains functions that are upper and lower bounded by quadratic functions. The $(L_{0},L_{1})$ smooth function class is more general since it also contains, e.g., univariate polynomials and exponential functions. Assumption 2 is even more general and contains univariate rational functions, double exponential functions, etc. See Appendix B.1 smoothness ‣ Convergence of Adam Under Relaxed Assumptions") for the formal propositions and proofs. We also refer the reader to our concurrent work for more detailed discussions of examples of $(\rho,L_{0},L_{\rho})$ smooth functions for different $\rho$s.

<!-- chunk {"id": "body-0026", "role": "body", "section": "Assumption 2", "weight": 1.0} -->

It turns out that bounded Hessian norm at a point $x$ implies local Lipschitzness of the gradient in the neighborhood around $x$. In particular, we have the following lemma.

<!-- chunk {"id": "body-0027", "role": "body", "section": "Remark 3.5", "weight": 1.0} -->

Lemma 3.4 can be actually used as the definition of $(\rho,L_{0},L_{\rho})$ smooth functions in place of Assumption 2. Besides the local gradient Lipschitz condition, it also suggests that, as long as the update at each step is small enough, the iterates will not go outside of the domain.

<!-- chunk {"id": "body-0028", "role": "body", "section": "Remark 3.5", "weight": 1.0} -->

In this case, Lemma 3.4 states that $\left\| {x - y} \right\| \leq {1/{({3L_{1}})}}$ implies ${\left\| {{{\nabla f}{(y)}} - {{\nabla f}{(x)}}} \right\| \leq {2{({L_{0} + {L_{1}\left\| {{\nabla f}{(x)}} \right\|}})}\left\| {y - x} \right\|}}.$ Therefore, it reduces to the local gradient Lipschitz condition for $(L_{0},L_{1})$ smooth functions in up to numerical constant factors. For $\rho \neq 1$, the proof is more involved because Grönwall's inequality used in no longer applies. Therefore we defer the detailed proof of Lemma 3.4 to Appendix B.2 smoothness ‣ Convergence of Adam Under Relaxed Assumptions").

<!-- chunk {"id": "body-0029", "role": "body", "section": "Stochastic gradient", "weight": 1.0} -->

We consider one of the following two assumptions on the stochastic gradient ${\nabla f}{(x_{t},\xi_{t})}$ in our analysis of Adam.

<!-- chunk {"id": "body-0030", "role": "body", "section": "Assumption 3", "weight": 1.0} -->

The gradient noise is centered and almost surely bounded. In particular, for some $\sigma \geq 0$ and all $t \geq 1$,

<!-- chunk {"id": "body-0031", "role": "body", "section": "Assumption 4", "weight": 1.0} -->

The gradient noise is centered with sub-Gaussian norm. In particular, for some $R \geq 0$ and all $t \geq 1$,

<!-- chunk {"id": "body-0032", "role": "body", "section": "Assumption 4", "weight": 1.0} -->

Assumption 4 is strictly weaker than Assumption 3 since an almost surely bounded random variable clearly has sub-Gaussian norm, but it results in a slightly worse convergece rate up to poly-log factors (see Theorems 4.1 and 4.2). Both of them are stronger than the most standard bounded variance assumption ${{\mathbb{E}}{\lbrack\left\| {{{\nabla f}{(x_{t},\xi_{t})}} - {{\nabla f}{(x_{t})}}} \right\|^{2}\rbrack}} \leq \sigma^{2}$ for some $\sigma \geq 0$, although Assumption 3 is actually a common assumption in existing analyses under the $(L_{0},L_{1})$ smoothness condition (see e.g. ). The extension to the bounded variance assumption is challenging and a very interesting future work as it is also the assumption considered in the lower bound.

<!-- chunk {"id": "body-0033", "role": "body", "section": "Assumption 4", "weight": 1.0} -->

We suspect that such an extension would be straightforward if we consider a mini-batch version of Algorithm 1 with a batch size of $S = {\Omega{(\epsilon^{- 2})}}$, since this results in a very small variance of $\mathcal{O}{(\epsilon^{2})}$ and thus essentially reduces the analysis to the deterministic setting. However, for practical Adam with an $\mathcal{O}{}$ batch size, the extension is challenging and we leave it as a future work.

<!-- chunk {"id": "body-0034", "role": "body", "section": "Results", "weight": 1.0} -->

In the section, we provide our convergence results for Adam under Assumptions 1, 2, and 3 or 4. To keep the statements of the theorems concise, we first define several problem-dependent constants. First, we let $\Delta_{1}:={{f{(x_{1})}} - f^{\ast}} < \infty$ be the initial sub-optimality gap. Next, given a large enough constant $G > 0$, we define

<!-- chunk {"id": "body-0035", "role": "body", "section": "Results", "weight": 1.0} -->

where $L$ can be viewed as the effective smoothness constant along the trajectory if one can show $\left\| {{\nabla f}{(x_{t})}} \right\| \leq G$ and $\left\| {x_{t + 1} - x_{t}} \right\| \leq r$ at each step (see Section 5 for more detailed discussions). We will also use $c_{1},c_{2}$ to denote some small enough numerical constants and $C_{1},C_{2}$ to denote some large enough ones. The formal convergence results under Assumptions 1, 2, and 3 are presented in the following theorem, whose proof is deferred in Appendix C.

<!-- chunk {"id": "body-0036", "role": "body", "section": "Bounding the gradients along the optimization trajectory", "weight": 1.0} -->

We want to bound the gradients along the optimization trajectory mainly for two reasons. First, as discussed in Section 2, many existing analyses of Adam rely on the assumption of bounded gradients, because unbounded gradient norm leads to unbounded second order momentum ${\hat{v}}_{t}$ which implies very small stepsize, and slow convergence. On the other hand, once the gradients are bounded, it is straightforward to control ${\hat{v}}_{t}$ as well as the stepsize, and therefore the analysis essentially reduces to the easier one for AdaBound. Second, informally speaking^11^1The statement is informal because here we can only show bounded gradients and Hessians at the iterate points, which only implies local smoothness near the neighborhood of each iterate point (see Section 5.2). However, the standard smoothness condition is a stronger global condition which assumes bounded Hessian at every point within a convex set., under Assumption 2, bounded gradients also imply bounded Hessians, which essentially reduces the $(\rho,L_{0},L_{\rho})$ smoothness to the standard smoothness.

<!-- chunk {"id": "body-0037", "role": "body", "section": "Bounding the gradients along the optimization trajectory", "weight": 1.0} -->

See Section 5.2 for more formal discussions.

<!-- chunk {"id": "body-0038", "role": "body", "section": "Bounding the gradients along the optimization trajectory", "weight": 1.0} -->

In this paper, instead of imposing the strong assumption of globally bounded gradients, we develop a new analysis to show that with high probability, the gradients are always bounded along the trajectory of Adam until convergence. The essential idea can be informally illustrated by the following "circular\" reasoning that we will make precise later. On the one hand, if $\left\| {{\nabla f}{(x_{t})}} \right\| \leq G$ for every $t \geq 1$, it is not hard to show the gradient converges to zero based on our discussions above. On the other hand, we know that a converging sequence must be upper bounded. Therefore there exists some $G^{\prime}$ such that $\left\| {{\nabla f}{(x_{t})}} \right\| \leq G^{\prime}$ for every $t \geq 1$. In other words, the bounded gradient condition implies the convergence result and the convergence result also implies the boundedness condition, forming a circular argument.

<!-- chunk {"id": "body-0039", "role": "body", "section": "Bounding the gradients along the optimization trajectory", "weight": 1.0} -->

This circular argument is of course flawed. However, we can break the circularity of reasoning and rigorously prove both the bounded gradient condition and the convergence result using a contradiction argument. Before introducing the contradiction argument, we first need to provide the following useful lemma, which is the reverse direction of a generalized Polyak-Lojasiewicz (PL) inequality, whose proof is deferred in Appendix B.3 smoothness ‣ Convergence of Adam Under Relaxed Assumptions").

<!-- chunk {"id": "body-0040", "role": "body", "section": "Local smoothness", "weight": 1.0} -->

In Section 5.1, we informally mentioned that $(\rho,L_{0},L_{\rho})$ smoothness essentially reduces to the standard smoothness if the gradient is bounded. In this section, we will make the statement more precise. First, note that Lemma 3.4 implies the following useful corollary.

<!-- chunk {"id": "body-0041", "role": "body", "section": "Warm-up: analysis in the deterministic setting", "weight": 1.0} -->

In this section, we consider the simpler deterministic setting where the stochastic gradient ${\nabla f}{(x_{t},\xi_{t})}$ in Algorithm 1 or is replaced with the exact gradient ${\nabla f}{(x_{t})}$. As discussed in Section 5.1, the key in our contradiction argument is to obtain both upper and lower bounds on ${f{(x_{\tau})}} - f^{\ast}$. In the following derivations, we focus on illustrating the main idea of our analysis technique and ignore minor proof details. In addition, all of them are under Assumptions 1, 2, and 3.

<!-- chunk {"id": "body-0042", "role": "body", "section": "Warm-up: analysis in the deterministic setting", "weight": 1.0} -->

In order to obtain the upper bound, we need the following two lemmas. First, denoting $\epsilon_{t}:={{\hat{m}}_{t} - {{\nabla f}{(x_{t})}}}$, we can obtain the following informal descent lemma for deterministic Adam.

<!-- chunk {"id": "body-0043", "role": "body", "section": "Extension to the stochastic setting", "weight": 1.0} -->

In this part, we briefly introduce how to extend the analysis to the more challenging stochastic setting. It becomes harder to obtain an upper bound on ${f{(x_{\tau})}} - f^{\ast}$ because $\Phi_{t}$ is no longer non-increasing due to the existence of noise. In addition, $\tau$ defined in is now a random variable. Note that all the derivations, such as Lemmas 5.4. ‣ 5.3 Warm-up: analysis in the deterministic setting ‣ 5 Analysis ‣ Convergence of Adam Under Relaxed Assumptions") and 5.5. ‣ 5.3 Warm-up: analysis in the deterministic setting ‣ 5 Analysis ‣ Convergence of Adam Under Relaxed Assumptions"), are conditioned on the random event $t < \tau$. Therefore, one can not simply take a total expectation of them to show ${\mathbb{E}}{\lbrack\Phi_{t}\rbrack}$ is non-increasing.

<!-- chunk {"id": "body-0044", "role": "body", "section": "Extension to the stochastic setting", "weight": 1.0} -->

Fortunately, $\tau$ is in fact a stopping time with nice properties. If the noise is almost surely bounded as in Assumption 3, by a more careful analysis, we can obtain a high probability upper bound on ${f{(x_{\tau})}} - f^{\ast}$ using concentration inequalities. Then we can still obtain a contradiction and convergence under this high probability event. If the noise has sub-Gaussian norm as in Assumption 4, one can change the definition of $\tau$ to

<!-- chunk {"id": "body-0045", "role": "body", "section": "Extension to the stochastic setting", "weight": 1.0} -->

for appropriately chosen $F$ and $\sigma$. Then at least when $t < \tau$, the noise is bounded by $\sigma$. Hence we can get the same upper bound on ${f{(x_{\tau})}} - f^{\ast}$ as if Assumption 3 still holds. However, when $t \leq T$, the lower bound ${{f{(x_{\tau})}} - f^{\ast}} > F$ does not necessarily holds, which requires some more careful analyses. The details of the proofs are involved and we defer them in Appendix C.

<!-- chunk {"id": "body-0046", "role": "body", "section": "Variance-reduced Adam", "weight": 1.0} -->

In this section, we propose a variance-reduced version of Adam (VRAdam). This new algorithm is depicted in Algorithm 2. Its main difference from the original Adam is that in the momentum update rule (Line 6), an additional term of ${({1 - \beta})}\left( {{{\nabla f}{(x_{t},\xi_{t})}} - {{\nabla f}{(x_{t - 1},\xi_{t})}}} \right)$ is added, inspired by the STORM algorithm. This term corrects the bias of $m_{t}$ so that it is an unbiased estimate of ${\nabla f}{(x_{t})}$ in the sense of total expectation, i.e., ${{\mathbb{E}}{\lbrack m_{t}\rbrack}} = {{\nabla f}{(x_{t})}}$. We will also show that it reduces the variance and accelerates the convergence.

<!-- chunk {"id": "body-0047", "role": "body", "section": "Variance-reduced Adam", "weight": 1.0} -->

Aside from the adaptive stepsize, one major difference between Algorithm 2 and STORM is that our hyper-parameters $\eta$ and $\beta$ are fixed constants whereas theirs are decreasing as a function of $t$. Choosing constant hyper-parameters requires a more accurate estimate at the initialization. That is why we use a mega-batch $\mathcal{S}_{1}$ to evaluate the gradient at the initial point to initialize $m_{1}$ and $v_{1}$ (Lines 2--3). In practice, one can also do a full-batch gradient evaluation at initialization. Note that there is no initialization bias for the momentum, so we do not re-scale $m_{t}$ and only re-scale $v_{t}$. We also want to point out that although the initial mega-batch gradient evaluation makes the algorithm a bit harder to implement, constant hyper-parameters are usually easier to tune and more common in training deep neural networks. It should be not hard to extend our analysis to time-decreasing $\eta$ and $\beta$ and we leave it as an interesting future work.

<!-- chunk {"id": "body-0048", "role": "body", "section": "Variance-reduced Adam", "weight": 1.0} -->

In addition to Assumption 1, we need to impose the following assumptions which can be viewed as stronger versions of Assumptions 2 and 3, respectively.

<!-- chunk {"id": "body-0049", "role": "body", "section": "Assumption 5", "weight": 1.0} -->

The objective function $f$ and the component function $f{( \cdot,\xi)}$ for each fixed $\xi$ are $(\rho,L_{0},L_{\rho})$ smooth with $0 \leq \rho < 2$.

<!-- chunk {"id": "body-0050", "role": "body", "section": "Assumption 6", "weight": 1.0} -->

The random variables ${\{\xi_{t}\}}_{1 \leq t \leq T}$ are sampled i.i.d. from some distribution $\mathcal{P}$ such that for any $x \in {\operatorname{dom}{(f)}}$,

<!-- chunk {"id": "body-0051", "role": "body", "section": "Remark 6.1", "weight": 1.0} -->

Assumption 6 is stronger than Assumption 3. Assumption 3 applies only to the iterates generated by the algorithm, while Assumption 6 is a pointwise assumption over all $x \in {\operatorname{dom}{(f)}}$ and further assumes an i.i.d. nature of the random variables ${\{\xi_{t}\}}_{1 \leq t \leq T}$. Also note that, similar to Adam, it is straightforward to generalize the assumption to noise with sub-Gaussian norm as in Assumption 4.

<!-- chunk {"id": "body-0052", "role": "body", "section": "Analysis", "weight": 1.0} -->

In this part, we briefly discuss challenges in the analysis of VRAdam. The detailed analysis is deferred in Appendix D. Note that Corollary 5.2 requires bounded update $\left\| {x_{t + 1} - x_{t}} \right\| \leq r$ at each step. For Adam, it is easy to satisfy for a small enough $\eta$ according to Lemma 5.3. However, for VRAdam, obtaining a good enough almost sure bound on the update is challenging even though the gradient noise is bounded. To bypass this difficulty, we directly impose a bound on $\left\| {{{\nabla f}{(x_{t})}} - m_{t}} \right\|$ by changing the definition of the stopping time $\tau$, similar to how we deal with the sub-Gaussian noise condition for Adam. In particular, we define

<!-- chunk {"id": "body-0053", "role": "body", "section": "Analysis", "weight": 1.0} -->

Then by definition, both $\left\| {{\nabla f}{(x_{t})}} \right\|$ and $\left\| {{{\nabla f}{(x_{t})}} - m_{t}} \right\|$ are bounded by $G$ before time $\tau$, which directly implies bounded update $\left\| {x_{t + 1} - x_{t}} \right\|$. Of course, the new definition brings new challenges to lower bounding ${f{(x_{\tau})}} - f^{\ast}$, which requires more careful analyses specific to the VRAdam algorithm. Please see Appendix D for the details.

<!-- chunk {"id": "body-0054", "role": "body", "section": "Convergence guarantees for VRAdam", "weight": 1.0} -->

In the section, we provide our main results for convergence of VRAdam under Assumptions 1, 5, and 6. We consider the same definitions of problem-dependent constants $\Delta_{1},r,L$ as those in Section 4 to make the statements of theorems concise. Let $c$ be a small enough numerical constant and $C$ be a large enough numerical constant. The formal convergence result is shown in the following theorem.

<!-- chunk {"id": "body-0055", "role": "body", "section": "Conclusion and future works", "weight": 1.5} -->

In this paper, we proved the convergence of Adam and its variance-reduced version under less restrictive assumptions compared to those in the existing literature. We considered a generalized non-uniform smoothness condition, according to which the Hessian norm is bounded by a sub-quadratic function of the gradient norm almost everywhere. Instead of assuming the Lipschitzness of the objective function as in existing analyses of Adam, we use a new contradiction argument to prove that gradients are bounded by a constant along the optimization trajectory. There are several interesting future directions that one could pursue following this work.

<!-- chunk {"id": "body-0056", "role": "body", "section": "Relaxation of the bounded noise assumption", "weight": 1.0} -->

Our analysis relies on the assumption of bounded noise or noise with sub-Gaussian norm. However, the existing lower bounds in consider the weaker bounded variance assumption. Hence, it is not clear whether the $\mathcal{O}{(\epsilon^{- 4})}$ complexity we obtain for Adam is tight in this setting. It will be interesting to see whether one can relax the assumption to the bounded variance setting. One may gain some insights from recent papers such as that analyze AdaGrad under weak noise conditions. An alternative way to show the tightness of the $\mathcal{O}{(\epsilon^{- 4})}$ complexity is to prove a lower bound under the bounded noise assumption.

<!-- chunk {"id": "body-0057", "role": "body", "section": "Potential applications of our technique", "weight": 1.0} -->

Another interesting future direction is to see if the techniques developed in this work for bounding gradients (including those in the the concurrent work ) can be generalized to improve the convergence results for other optimization problems and algorithms. We believe it is possible so long as the function class is well behaved and the algorithm is efficient enough so that ${f{(x_{\tau})}} - f^{\ast}$ can be well bounded for some appropriately defined stopping time $\tau$.

<!-- chunk {"id": "body-0058", "role": "body", "section": "Understanding why Adam is better than SGD", "weight": 1.0} -->

We want to note that our results can not explain why Adam is better than SGD for training transformers, because shows that non-adaptive SGD converges with the same $\mathcal{O}{(\epsilon^{- 4})}$ gradient complexity under even weaker conditions. It would be interesting and impactful if one can find a reasonable setting (function class, gradient oracle, etc) under which Adam or other adaptive methods provably outperform SGD.
