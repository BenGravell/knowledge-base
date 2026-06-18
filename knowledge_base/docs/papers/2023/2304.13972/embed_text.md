## Introduction

In this paper, we study the non-convex unconstrained stochastic optimization problem

The Adaptive Moment Estimation (Adam) algorithm has become one of the most popular optimizers for solving when $f$ is the loss for training deep neural networks. Owing to its efficiency and robustness to hyper-parameters, it is widely applied or even sometimes the default choice in many machine learning application domains such as natural language processing, generative adversarial networks, computer vision, and reinforcement learning. It is also well known that Adam significantly outperforms stochastic gradient descent (SGD) for certain models like transformer.

Despite its success in practice, theoretical analyses of Adam are still limited. The original proof of convergence in was later shown by Reddi et al. to contain gaps. The authors in also showed that for a range of momentum parameters chosen *independently with the problem instance*, Adam does not necessarily converge even for convex objectives. However, in deep learning practice, the hyper-parameters are in fact *problem-dependent* as they are usually tuned after given the problem and weight initialization. Recently, there have been many works proving the convergence of Adam for non-convex functions with various assumptions and problem-dependent hyper-parameter choices. However, these results leave significant room for improvement. For example, prove the convergence to stationary points assuming the gradients are bounded by a constant, either explicitly or implicitly. On the other hand, consider weak assumptions, but their convergence results are still limited. See Section 2 for more detailed discussions of related works.

To address the above-mentioned gap between theory and practice, we provide a new convergence analysis of Adam *without assuming bounded gradients*, or equivalently, Lipschitzness of the objective function. In addition, we also relax the standard global smoothness assumption, i.e., the Lipschitzness of the gradient function, as it is far from being satisfied in deep neural network training. Instead, we consider a more general, relaxed, and non-uniform smoothness condition according to which the local smoothness (i.e., Hessian norm when it exists) around $x$ is bounded by a sub-quadratic function of the gradient norm $\left\| {{\nabla f}{(x)}} \right\|$ (see Definition 3.2 and Assumption 2 for the details). This generalizes the $(L_{0},L_{1})$ smoothness condition proposed by based on language model experiments. Even though our assumptions are much weaker and more realistic, we can still obtain the same $\mathcal{O}{(\epsilon^{- 4})}$ gradient complexity for convergence to an $\epsilon$-stationary point.

The key to our analysis is a new technique to obtain a high probability, constant upper bound on the gradients along the optimization trajectory of Adam, without assuming Lipschitzness of the objective function. In other words, it essentially turns the bounded gradient assumption into a result that can be directly proven. Bounded gradients imply bounded stepsize at each step, with which the analysis of Adam essentially reduces to the simpler analysis of AdaBound. Furthermore, once the gradient boundedness is achieved, the analysis under the generalized non-uniform smoothness assumption is not much harder than that under the standard smoothness condition. We will introduce the technique in more details in Section 5. We note that the idea of bounding gradient norm along the trajectory of the optimization algorithm can be use in other problems as well. For more details, we refer the reader to our concurrent work in which we present a set of new techiniques and methods for bounding gradient norm for other optimization algorithms under a generalized smoothness condition.

Another contribution of this paper is to show that the gradient complexity of Adam can be further improved with variance reduction methods. To this end, we propose a variance-reduced version of Adam by modifying its momentum update rule, inspired by the idea of the STORM algorithm. Under additional generalized smoothness assumption of the component function $f{( \cdot,\xi)}$ for each $\xi$, we show that this provably accelerates the convergence with a gradient complexity of $\mathcal{O}{(\epsilon^{- 3})}$. This rate improves upon the existing result of where the authors obtain an asymptotic convergence of their approach to variance reduction for Adam in the non-convex setting, under the bounded gradient assumption.

### Contributions

In light of the above background, we summarize our main contributions as follows.

We develop a new analysis to show that Adam converges to stationary points under relaxed assumptions. In particular, we do not assume bounded gradients or Lipschitzness of the objective function. Furthermore, we also consider a generalized non-uniform smoothness condition where the local smoothness or Hessian norm is bounded by a *sub-quadratic* function of the gradient norm. Under these more realistic assumptions, we obtain a *dimension free* gradient complexity of $\mathcal{O}{(\epsilon^{- 4})}$ if the gradient noise is centered and bounded.

We generalize our analysis to the setting where the gradient noise is centered and has sub-Gaussian norm, and show the convergence of Adam with a gradient complexity of $\mathcal{O}{({\epsilon^{- 4}{\log^{3.25}{({1/\epsilon})}}})}$.

We propose a variance-reduced version of Adam (VRAdam) with provable convergence guarantees. In particular, we obtain the accelerated $\mathcal{O}{(\epsilon^{- 3})}$ gradient complexity.

## Related work

In this section, we discuss the relevant literature related to different aspects of our work.

### Convergence of Adam

Adam was first proposed by Kingma and Ba with a theoretical convergence guarantee for convex functions. However, Reddi et al. found a gap in the proof of this convergence analysis, and also constructed counter-examples for a range of hyper-parameters on which Adam does not converge. That being said, the counter-examples depend on the hyper-parameters of Adam, i.e., they are constructed after picking the hyper-parameters. Therefore, it does not rule out the possibility of obtaining convergence guarantees for problem-dependent hyper-parameters, as also pointed out by.

Many recent works have developed convergence analyses of Adam with various assumptions and hyper-parameter choices. Zhou et al. show Adam with certain hyper-parameters can work on the counter-examples of. De et al. prove convergence for general non-convex functions assuming gradients are bounded and the signs of stochastic gradients are the same along the trajectory. The analysis in also relies on the bounded gradient assumption. Guo et al. assume the adaptive stepsize is upper and lower bounded by two constants, which is not necessarily satisfied unless assuming bounded gradients or considering the AdaBound variant. consider very weak assumptions. However, they show either 1) "convergence" only to some neighborhood of stationary points with a constant radius, unless assuming the strong growth condition; or 2) convergence to stationary points but with a slower rate.

### Variants of Adam

After Reddi et al. pointed out the non-convergence issue with Adam, various variants of Adam that can be proved to converge were proposed. For example, AMSGrad and AdaFom modify the second order momentum so that it is non-decreasing. AdaBound explicitly imposes upper and lower bounds on the second order momentum so that the stepsize is also bounded. AdaShift uses a new estimate of the second order momentum to correct the bias. There are also some works that provide convergence guarantees of these variants. One closely related work to ours is, which considers a variance-reduced version of Adam by combining Adam and SVRG. However, they assume bounded gradients and can only get an asymptotic convergence in the non-convex setting.

### Generalized smoothness condition

Generalizing the standard smoothness condition in a variety of settings has been a focus of many recent papers. Recently, proposed a generalized smoothness condition called $(L_{0},L_{1})$ smoothness, which assumes the local smoothness or Hessian norm is bounded by an affine function of the gradient norm. The assumption was well-validated by extensive experiments conducted on language models. Various analyses of different algorithms under this condition were later developed. One recent closely-related work is which studies converges of Adam under the $(L_{0},L_{1})$ smoothness condition. However, their results are still limited, as we have mentioned above. In this paper, we consider an even more general smoothness condition where the local smoothness is bounded by a sub-quadratic function of the gradient norm, and prove the convergence of Adam under this condition. In our concurrent work, we further analyze various other algorithms in both convex and non-convex settings under similar generalized smoothness conditions following the same key idea of bounding gradients along the trajectory.

### Variance reduction methods

The technique of variance reduction was introduced to accelerate convex optimization in the finite-sum setting. Later, many works studied variance-reduced methods in the non-convex setting and obtained improved convergence rates for standard smooth functions. For example, SVRG and SCSG improve the $\mathcal{O}{(\epsilon^{- 4})}$ gradient complexity of stochastic gradient descent (SGD) to $\mathcal{O}{(\epsilon^{- {10/3}})}$. Many new variance reduction methods were later proposed to further improve the complexity to $\mathcal{O}{(\epsilon^{- 3})}$, which is optimal and matches the lower bound in. Recently, obtained the $\mathcal{O}{(\epsilon^{- 3})}$ complexity for the more general $(L_{0},L_{1})$ smooth functions. Our variance-reduced Adam is motivated by the STORM algorithm proposed by, where an additional term is added in the momentum update to correct the bias and reduce the variance.

## Preliminaries

Notation. Let $\left. \parallel \cdot \parallel \right.$ denote the Euclidean norm of a vector or spectral norm of a matrix. For any given vector $x$, we use ${(x)}_{i}$ to denote its $i$-th coordinate and $x^{2}$, $\sqrt{x}$, $|x|$ to denote its coordinate-wise square, square root, and absolute value respectively. For any two vectors $x$ and $y$, we use $x \odot y$ and $x/y$ to denote their coordinate-wise product and quotient respectively. We also write $x \preceq y$ or $x \succeq y$ to denote the coordinate-wise inequality between $x$ and $y$, which means ${(x)}_{i} \leq {(y)}_{i}$ or ${(x)}_{i} \geq {(y)}_{i}$ for each coordinate index $i$. For two symmetric real matrices $A$ and $B$, we say $A \preceq B$ or $A \succeq B$ if $B - A$ or $A - B$ is positive semi-definite (PSD). Given two real numbers ${a,b} \in {\mathbb{R}}$, we denote ${a \land b}:={\min{\{ a,b\}}}$ for simplicity. Finally, we use $\mathcal{O}{( \cdot )}$, $\Theta{( \cdot )}$, and $\Omega{( \cdot )}$ for the standard big-O, big-Theta, and big-Omega notation.

### Description of the Adam algorithm

2:Initialize m0 = v0 = 0 and x1 = xinit
4: Draw a new sample ξt and perform the following updates
7: ${\hat{m}}_{t} = \frac{m_{t}}{1 - {({1 - \beta})}^{t}}$
8: ${\hat{v}}_{t} = \frac{v_{t}}{1 - {({1 - \beta_{sq}})}^{t}}$
9: $x_{t + 1} = {x_{t} - {\frac{\eta}{\sqrt{{\hat{v}}_{t}} + \lambda} \odot {\hat{m}}_{t}}}$

The formal definition of Adam proposed in is shown in Algorithm 1, where Lines 5--9 describe the update rule of iterates ${\{ x_{t}\}}_{1 \leq t \leq T}$. Lines 5--6 are the updates for the first and second order momentum, $m_{t}$ and $v_{t}$, respectively. In Lines 7--8, they are re-scaled to ${\hat{m}}_{t}$ and ${\hat{v}}_{t}$ in order to correct the initialization bias due to setting $m_{0} = v_{0} = 0$. Then the iterate is updated by $x_{t + 1} = {x_{t} - {h_{t} \odot {\hat{m}}_{t}}}$ where $h_{t} = {\eta/{({\sqrt{{\hat{v}}_{t}} + \lambda})}}$ is the adaptive stepsize vector for some parameters $\eta$ and $\lambda$.

### Assumptions

In what follows below, we will state our main assumptions for analysis of Adam.

### Function class

We start with a standard assumption in optimization on the objective function $f$ whose domain lies in a Euclidean space with dimension $d$.

### Assumption 1

The objective function $f$ is *differentiable* and *closed* within its *open domain* ${\operatorname{dom}{(f)}} \subseteq {\mathbb{R}}^{d}$ and is bounded from below, i.e., $f^{\ast}:={\inf_{x}{f{(x)}}} > {- \infty}$.

### Remark 3.1

A function $f$ is said to be closed if its sub-level set $\{{x \in {\operatorname{dom}{(f)}}}\mid{{f{(x)}} \leq a}\}$ is closed for each $a \in {\mathbb{R}}$. In addition, a continuous function $f$ over an open domain is closed if and only $f{(x)}$ tends to infinity whenever $x$ approaches to the boundary of $\operatorname{dom}{(f)}$, which is an important condition to ensure the iterates of Adam with a small enough stepsize $\eta$ stay within the domain with high probability. Note that this condition is mild since any continuous function defined over the entire space ${\mathbb{R}}^{d}$ is closed.

Besides Assumption 1, the only additional assumption we make regarding $f$ is that its local smoothness is bounded by a sub-quadratic function of the gradient norm. More formally, we consider the following $(\rho,L_{0},L_{\rho})$ smoothness condition with $0 \leq \rho < 2$.

### Definition 3.2

A differentiable real-valued function $f$ is $(\rho,L_{0},L_{\rho})$ smooth for some constants ${\rho,L_{0},L_{\rho}} \geq 0$ if the following inequality holds *almost everywhere* in $\operatorname{dom}{(f)}$

### Remark 3.3

When $\rho = 1$, Definition 3.2 reduces to the $(L_{0},L_{1})$ smoothness condition in. When $\rho = 0$ or $L_{\rho} = 0$, it reduces to the standard smoothness condition.

### Assumption 2

The objective function $f$ is $(\rho,L_{0},L_{\rho})$ smooth with $0 \leq \rho < 2$.

The standard smooth function class is very restrictive as it only contains functions that are upper and lower bounded by quadratic functions. The $(L_{0},L_{1})$ smooth function class is more general since it also contains, e.g., univariate polynomials and exponential functions. Assumption 2 is even more general and contains univariate rational functions, double exponential functions, etc. See Appendix B.1 smoothness ‣ Convergence of Adam Under Relaxed Assumptions") for the formal propositions and proofs. We also refer the reader to our concurrent work for more detailed discussions of examples of $(\rho,L_{0},L_{\rho})$ smooth functions for different $\rho$s.

It turns out that bounded Hessian norm at a point $x$ implies local Lipschitzness of the gradient in the neighborhood around $x$. In particular, we have the following lemma.

### Lemma 3.4

Under Assumptions 1 and 2, for any $a > 0$ and two points ${x \in {\operatorname{dom}{(f)}}},{y \in {\mathbb{R}}^{d}}$ such that $\left\| {y - x} \right\| \leq \frac{a}{L_{0} + {L_{\rho}{({\left\| {{\nabla f}{(x)}} \right\| + a})}^{\rho}}}$, we have $y \in {\operatorname{dom}{(f)}}$ and

### Remark 3.5

Lemma 3.4 can be actually used as the definition of $(\rho,L_{0},L_{\rho})$ smooth functions in place of Assumption 2. Besides the local gradient Lipschitz condition, it also suggests that, as long as the update at each step is small enough, the iterates will not go outside of the domain.

For the special case of $\rho = 1$, choosing $a = {\max{\{\left\| {{\nabla f}{(x)}} \right\|,{L_{0}/L_{1}}\}}}$, one can verify that the required locality size in Lemma 3.4 satisfies $\frac{a}{L_{0} + {L_{1}{({\left\| {{\nabla f}{(x)}} \right\| + a})}}} \geq \frac{1}{3L_{1}}$. In this case, Lemma 3.4 states that $\left\| {x - y} \right\| \leq {1/{({3L_{1}})}}$ implies ${\left\| {{{\nabla f}{(y)}} - {{\nabla f}{(x)}}} \right\| \leq {2{({L_{0} + {L_{1}\left\| {{\nabla f}{(x)}} \right\|}})}\left\| {y - x} \right\|}}.$ Therefore, it reduces to the local gradient Lipschitz condition for $(L_{0},L_{1})$ smooth functions in up to numerical constant factors. For $\rho \neq 1$, the proof is more involved because Grönwall's inequality used in no longer applies. Therefore we defer the detailed proof of Lemma 3.4 to Appendix B.2 smoothness ‣ Convergence of Adam Under Relaxed Assumptions").

### Stochastic gradient

We consider one of the following two assumptions on the stochastic gradient ${\nabla f}{(x_{t},\xi_{t})}$ in our analysis of Adam.

### Assumption 3

The gradient noise is centered and almost surely bounded. In particular, for some $\sigma \geq 0$ and all $t \geq 1$,

where ${\mathbb{E}}_{t - 1}{\lbrack \cdot \rbrack}:={\mathbb{E}}{\lbrack \cdot |\xi_{1},\ldots,\xi_{t - 1}\rbrack}$ is the conditional expectation given $\xi_{1},\ldots,\xi_{t - 1}$.

### Assumption 4

The gradient noise is centered with sub-Gaussian norm. In particular, for some $R \geq 0$ and all $t \geq 1$,

where ${\mathbb{E}}_{t - 1}{\lbrack \cdot \rbrack}:={\mathbb{E}}{\lbrack \cdot |\xi_{1},\ldots,\xi_{t - 1}\rbrack}$ and ${\mathbb{P}}_{t - 1}{\lbrack \cdot \rbrack}:={\mathbb{P}}{\lbrack \cdot |\xi_{1},\ldots,\xi_{t - 1}\rbrack}$ are the conditional expectation and probability given $\xi_{1},\ldots,\xi_{t - 1}$.

Assumption 4 is strictly weaker than Assumption 3 since an almost surely bounded random variable clearly has sub-Gaussian norm, but it results in a slightly worse convergece rate up to poly-log factors (see Theorems 4.1 and 4.2). Both of them are stronger than the most standard bounded variance assumption ${{\mathbb{E}}{\lbrack\left\| {{{\nabla f}{(x_{t},\xi_{t})}} - {{\nabla f}{(x_{t})}}} \right\|^{2}\rbrack}} \leq \sigma^{2}$ for some $\sigma \geq 0$, although Assumption 3 is actually a common assumption in existing analyses under the $(L_{0},L_{1})$ smoothness condition (see e.g. ). The extension to the bounded variance assumption is challenging and a very interesting future work as it is also the assumption considered in the lower bound. We suspect that such an extension would be straightforward if we consider a mini-batch version of Algorithm 1 with a batch size of $S = {\Omega{(\epsilon^{- 2})}}$, since this results in a very small variance of $\mathcal{O}{(\epsilon^{2})}$ and thus essentially reduces the analysis to the deterministic setting. However, for practical Adam with an $\mathcal{O}{}$ batch size, the extension is challenging and we leave it as a future work.

## Results

In the section, we provide our convergence results for Adam under Assumptions 1, 2, and 3 or 4. To keep the statements of the theorems concise, we first define several problem-dependent constants. First, we let $\Delta_{1}:={{f{(x_{1})}} - f^{\ast}} < \infty$ be the initial sub-optimality gap. Next, given a large enough constant $G > 0$, we define

where $L$ can be viewed as the effective smoothness constant along the trajectory if one can show $\left\| {{\nabla f}{(x_{t})}} \right\| \leq G$ and $\left\| {x_{t + 1} - x_{t}} \right\| \leq r$ at each step (see Section 5 for more detailed discussions). We will also use $c_{1},c_{2}$ to denote some small enough numerical constants and $C_{1},C_{2}$ to denote some large enough ones. The formal convergence results under Assumptions 1, 2, and 3 are presented in the following theorem, whose proof is deferred in Appendix C.

### Theorem 4.1

Suppose Assumptions 1, 2, and 3 hold. Denote $\iota:={\log{({1/\delta})}}$ for any $0 < \delta < 1$. Let $G$ be a constant satisfying $G \geq {\max\left\{ {2\lambda},{2\sigma},\sqrt{C_{1}\Delta_{1}L_{0}},{({C_{1}\Delta_{1}L_{\rho}})}^{\frac{1}{2 - \rho}} \right\}}$. Choose

Let $T = {\max\left\{ \frac{1}{\beta^{2}},\frac{C_{2}\Delta_{1}G}{\eta\epsilon^{2}} \right\}}$. Then with probability at least $1 - \delta$, we have $\left\| {{\nabla f}{(x_{t})}} \right\| \leq G$ for every $1 \leq t \leq T$, and ${\frac{1}{T}{\sum_{t = 1}^{T}\left\| {{\nabla f}{(x_{t})}} \right\|^{2}}} \leq \epsilon^{2}$.

Note that $G$, the upper bound of gradients along the trajectory, is a constant that depends on $\lambda,\sigma,L_{0},L_{\rho}$, and the initial sub-optimality gap $\Delta_{1}$, but not on $\epsilon$. There is no requirement on the second order momentum parameter $\beta_{sq}$, although many existing works like need certain restrictions on it. We choose very small $\beta$ and $\eta$, both of which are $\mathcal{O}{(\epsilon^{2})}$. Therefore, from the choice of $T$, it is clear that we obtain a gradient complexity of $\mathcal{O}{(\epsilon^{- 4})}$, where we only consider the leading term. We are not clear whether the dependence on $\epsilon$ is optimal or not, as the $\Omega{(\epsilon^{- 4})}$ lower bound in assumes the weaker bounded variance assumption than our Assumpion 3. However, it matches the state-of-the-art complexity among existing analyses of Adam.

One limitation of the dependence of our complexity on $\lambda$ is $\mathcal{O}{(\lambda^{- 2})}$, which might be large since $\lambda$ is usually small in practice, e.g., the default choice is $\lambda = 10^{- 8}$ in the PyTorch implementation. There are some existing analyses on Adam whose rates do not depend explicitly on $\lambda$ or only depend on $\log{({1/\lambda})}$. However, all of them depend on $\operatorname{poly}{(d)}$, whereas our rate is dimension free. The dimension $d$ is also very large, especially when training transformers, for which Adam is widely used. We believe that independence on $d$ is better than that on $\lambda$, because $d$ is fixed given the architecture of the neural network but $\lambda$ is a hyper-parameter which we have the freedom to tune. In fact, based on our preliminary experimental results on CIFAR-10 shown in Figure 1, the performance of Adam is not very sensitive to the choice of $\lambda$. Although the default choice of $\lambda$ is $10^{- 8}$, increasing it up to $0.01$ only makes minor differences.

Figure 1: Test errors of different models trained on CIFAR-10 using the Adam optimizer with β = 0.9, βsq = 0.999, η = 0.001 and different λs. From left to right: (a) a shallow CNN with 6 layers; (b) ResNet-Small with 20 layers; and (c) ResNet110 with 110 layers.

As discussed in Section 3.2.2, we can generalize the bounded gradient noise condition in Assumption 3 to the weaker sub-Gaussian noise condition in Assumption 4. The following theorem formally shows the convergence result under Assumptions 1, 2, and 4, whose proof is deferred in Appendix C.6.

### Theorem 4.2

Suppose Assumptions 1, 2, and 4 hold. Denote $\iota:={\log{({2/\delta})}}$ and $\sigma:={R\sqrt{2{\log{({{4T}/\delta})}}}}$ for any $0 < \delta < 1$. Let $G$ be a constant satisfying $G \geq {\max\left\{ {2\lambda},{2\sigma},\sqrt{C_{1}\Delta_{1}L_{0}},{({C_{1}\Delta_{1}L_{\rho}})}^{\frac{1}{2 - \rho}} \right\}}$. Choose

Let $T = {\max\left\{ \frac{1}{\beta^{2}},\frac{C_{2}\Delta_{1}G}{\eta\epsilon^{2}} \right\}}$. Then with probability at least $1 - \delta$, we have $\left\| {{\nabla f}{(x_{t})}} \right\| \leq G$ for every $1 \leq t \leq T$, and ${\frac{1}{T}{\sum_{t = 1}^{T}\left\| {{\nabla f}{(x_{t})}} \right\|^{2}}} \leq \epsilon^{2}$.

Note that the main difference of Theorem 4.2 from Theorem 4.1 is that $\sigma$ is now $\mathcal{O}{(\sqrt{\log T})}$ instead of a constant. With some standard calculations, one can show that the gradient complexity in Theorem 4.2 is bounded by $\mathcal{O}{({\epsilon^{- 4}{\log^{p}{({1/\epsilon})}}})}$, where $p = {\max\left\{ 3,\frac{9 + {2\rho}}{4} \right\}} < 3.25$.

## Analysis

### Bounding the gradients along the optimization trajectory

We want to bound the gradients along the optimization trajectory mainly for two reasons. First, as discussed in Section 2, many existing analyses of Adam rely on the assumption of bounded gradients, because unbounded gradient norm leads to unbounded second order momentum ${\hat{v}}_{t}$ which implies very small stepsize, and slow convergence. On the other hand, once the gradients are bounded, it is straightforward to control ${\hat{v}}_{t}$ as well as the stepsize, and therefore the analysis essentially reduces to the easier one for AdaBound. Second, informally speaking^11^1The statement is informal because here we can only show bounded gradients and Hessians at the iterate points, which only implies local smoothness near the neighborhood of each iterate point (see Section 5.2). However, the standard smoothness condition is a stronger global condition which assumes bounded Hessian at every point within a convex set., under Assumption 2, bounded gradients also imply bounded Hessians, which essentially reduces the $(\rho,L_{0},L_{\rho})$ smoothness to the standard smoothness. See Section 5.2 for more formal discussions.

In this paper, instead of imposing the strong assumption of globally bounded gradients, we develop a new analysis to show that with high probability, the gradients are always bounded along the trajectory of Adam until convergence. The essential idea can be informally illustrated by the following "circular\" reasoning that we will make precise later. On the one hand, if $\left\| {{\nabla f}{(x_{t})}} \right\| \leq G$ for every $t \geq 1$, it is not hard to show the gradient converges to zero based on our discussions above. On the other hand, we know that a converging sequence must be upper bounded. Therefore there exists some $G^{\prime}$ such that $\left\| {{\nabla f}{(x_{t})}} \right\| \leq G^{\prime}$ for every $t \geq 1$. In other words, the bounded gradient condition implies the convergence result and the convergence result also implies the boundedness condition, forming a circular argument.

This circular argument is of course flawed. However, we can break the circularity of reasoning and rigorously prove both the bounded gradient condition and the convergence result using a contradiction argument. Before introducing the contradiction argument, we first need to provide the following useful lemma, which is the reverse direction of a generalized Polyak-Lojasiewicz (PL) inequality, whose proof is deferred in Appendix B.3 smoothness ‣ Convergence of Adam Under Relaxed Assumptions").

### Lemma 5.1

Under Assumptions 1 and 2, we have $\left\| {{\nabla f}{(x)}} \right\|^{2} \leq {3{({{3L_{0}} + {4L_{\rho}\left\| {{\nabla f}{(x)}} \right\|^{\rho}}})}{({{f{(x)}} - f^{\ast}})}}$.

Define the function ${\zeta{(u)}}:=\frac{u^{2}}{3{({{3L_{0}} + {4L_{\rho}u^{\rho}}})}}$ over $u \geq 0$. It is easy to verify that if $\rho < 2$, $\zeta$ is increasing and its range is $\lbrack 0,\infty)$. Therefore, $\zeta$ is invertible and $\zeta^{- 1}$ is also increasing. Then, for any constant $G > 0$, denoting $F = {\zeta{(G)}}$, Lemma 5.1 suggests that if ${{f{(x)}} - f^{\ast}} \leq F$, we have

In other words, if $\rho < 2$, the gradient is bounded within any sub-level set, even though the sub-level set could be unbounded. Then, let $\tau$ be the first time the sub-optimality gap is strictly greater than $F$, truncated at $T + 1$, or formally,

Then at least when $t < \tau$, we have ${{f{(x_{t})}} - f^{\ast}} \leq F$ and thus $\left\| {{\nabla f}{(x_{t})}} \right\| \leq G$. Based on our discussions above, it is not hard to analyze the updates before time $\tau$, and one can contruct some Lyapunov function to obtain an upper bound on ${f{(x_{\tau})}} - f^{\ast}$. On the other hand, if $\tau \leq T$, we immediately obtain a lower bound on $f{(x_{\tau})}$, that is ${{f{(x_{\tau})}} - f^{\ast}} > F$, by the definition of $\tau$ in. If the lower bound is greater than the upper bound, it leads to a contradiction, which shows $\tau = {T + 1}$, i.e., the sub-optimality gap and the gradient norm are always bounded by $F$ and $G$ respectively before the algorithm terminates. We will illustrate the technique in more details in the simple deterministic setting in Section 5.3, but first, in Section 5.2, we introduce several prerequisite lemmas on the $(\rho,L_{0},L_{\rho})$ smoothness.

### Local smoothness

In Section 5.1, we informally mentioned that $(\rho,L_{0},L_{\rho})$ smoothness essentially reduces to the standard smoothness if the gradient is bounded. In this section, we will make the statement more precise. First, note that Lemma 3.4 implies the following useful corollary.

### Corollary 5.2

Under Assumptions 1 and 2, for any $G > 0$ and two points ${x \in {\operatorname{dom}{(f)}}},{y \in {\mathbb{R}}^{d}}$ such that $\left\| {{\nabla f}{(x)}} \right\| \leq G$ and $\left\| {y - x} \right\| \leq r:={\min\left\{ \frac{1}{5L_{\rho}G^{\rho - 1}},\frac{1}{5{({L_{0}^{\rho - 1}L_{\rho}})}^{1/\rho}} \right\}}$, denoting $L:={{3L_{0}} + {4L_{\rho}G^{\rho}}}$, we have $y \in {\operatorname{dom}{(f)}}$ and

The proof of Corollary 5.2 is deferred in Appendix B.4 smoothness ‣ Convergence of Adam Under Relaxed Assumptions"). Although the inequalities in Corollary 5.2 look very similar to the standard global smoothness condition with constant $L$, it is still a local condition as it requires $\left\| {x - y} \right\| \leq r$. Fortunately, at least before $\tau$, such a requirement is easy to satisfy for small enough $\eta$, according to the following lemma whose proof is deferred in Appendix C.5.

### Lemma 5.3

Under Assumption 3, if $t < \tau$ and choosing $G \geq \sigma$, we have $\left\| {x_{t + 1} - x_{t}} \right\| \leq {\etaD}$ where $D:={{2G}/\lambda}$.

Then as long as $\eta \leq {r/D}$, we have $\left\| {x_{t + 1} - x_{t}} \right\| \leq r$ which satisfies the requirement in Corollary 5.2. Then we can apply the inequalities in it in the same way as the standard smoothness condition. In other words, most classical inequalities derived for standard smooth functions also apply to $(\rho,L_{0},L_{\rho})$ smooth functions.

### Warm-up: analysis in the deterministic setting

In this section, we consider the simpler deterministic setting where the stochastic gradient ${\nabla f}{(x_{t},\xi_{t})}$ in Algorithm 1 or is replaced with the exact gradient ${\nabla f}{(x_{t})}$. As discussed in Section 5.1, the key in our contradiction argument is to obtain both upper and lower bounds on ${f{(x_{\tau})}} - f^{\ast}$. In the following derivations, we focus on illustrating the main idea of our analysis technique and ignore minor proof details. In addition, all of them are under Assumptions 1, 2, and 3.

In order to obtain the upper bound, we need the following two lemmas. First, denoting $\epsilon_{t}:={{\hat{m}}_{t} - {{\nabla f}{(x_{t})}}}$, we can obtain the following informal descent lemma for deterministic Adam.

### Lemma 5.4 (Descent lemma, informal)

For any $t < \tau$, choosing $G \geq \lambda$ and a small enough $\eta$,

where "$\lessapprox$" omits less important terms.

### Proof Sketch of Lemma 5.4. ‣ 5.3 Warm-up: analysis in the deterministic setting ‣ 5 Analysis ‣ Convergence of Adam Under Relaxed Assumptions")

By the definition of $\tau$, for all $t < \tau$, we have ${{f{(x_{t})}} - f^{\ast}} \leq F$ which implies $\left\| {{\nabla f}{(x_{t})}} \right\| \leq G$. Then from the update rule in Proposition C.1 provided later in Appendix C, it is easy to verify ${\hat{v}}_{t} \preceq G^{2}$ since ${\hat{v}}_{t}$ is a convex combination of ${\{{({{\nabla f}{(x_{s})}})}^{2}\}}_{s \leq t}$. Let $h_{t}:={\eta/{({\sqrt{{\hat{v}}_{t}} + \lambda})}}$ be the stepsize vector and denote $H_{t}:={\text{diag}{(h_{t})}}$. We know

As discussed in Section 5.2, when $\eta$ is small enough, we can apply Corollary 5.2 to obtain

where in the first (approximate) inequality we ignore the second order term ${\frac{1}{2}L\left\| {x_{t + 1} - x_{t}} \right\|^{2}} \propto \eta^{2}$ in Corollary 5.2 for small enough $\eta$; the equality applies the update rule ${x_{t + 1} - x_{t}} = {- {H_{t}{\hat{m}}_{t}}} = {- {H_{t}{({{{\nabla f}{(x_{t})}} + \epsilon_{t}})}}}$; in the second inequality we use ${2a^{\top}Ab} \leq {\left\| a \right\|_{A}^{2} + \left\| b \right\|_{A}^{2}}$ for any PSD matrix $A$ and vectors $a$ and $b$; and the last inequality is due to. ∎

Compared with the standard descent lemma for gradient descent, there is an additional term of $\left\| \epsilon_{t} \right\|^{2}$ in Lemma 5.4. ‣ 5.3 Warm-up: analysis in the deterministic setting ‣ 5 Analysis ‣ Convergence of Adam Under Relaxed Assumptions"). In the next lemma, we bound this term recursively.

### Lemma 5.5 (Informal)

Choosing $\beta = {\Theta{({\etaG^{\rho + {1/2}}})}}$, if $t < \tau$, we have

### Proof Sketch of Lemma 5.5. ‣ 5.3 Warm-up: analysis in the deterministic setting ‣ 5 Analysis ‣ Convergence of Adam Under Relaxed Assumptions")

By the update rule in Proposition C.1, we have

For small enough $\eta$, we can apply Corollary 5.2 to get

where the second inequality is due to $L = {\mathcal{O}{(G^{\rho})}}$ and $\left\| {x_{t + 1} - x_{t}} \right\| = {\mathcal{O}{(\eta)}\left\| {\hat{m}}_{t} \right\|}$; and the last inequality uses ${\hat{m}}_{t} = {{{\nabla f}{(x_{t})}} + \epsilon_{t}}$ and Young's inequality $\left\| {a + b} \right\|^{2} \leq {{2\left\| a \right\|^{2}} + {2\left\| b \right\|^{2}}}$. Therefore,

where the first inequality uses and Young's inequality $\left\| {a + b} \right\|^{2} \leq {{{({1 + u})}\left\| a \right\|^{2}} + {{({1 + {1/u}})}\left\| b \right\|^{2}}}$ for any $u > 0$; the second inequality uses ${{({1 - \alpha_{t + 1}})}{({1 + {\alpha_{t + 1}/2}})}} \leq {1 - {\alpha_{t + 1}/2}}$ and; and in the last inequality we use $\beta \leq \alpha_{t + 1}$ and choose $\beta = {\Theta{({\etaG^{\rho + {1/2}}})}}$ which implies ${\mathcal{O}{({{\eta^{2}G^{2\rho}}/\alpha_{t + 1}})}} \leq \frac{\lambda\beta}{16G} \leq {\beta/4}$. ∎

Now we combine them to get the upper bound on ${f{(x_{\tau})}} - f^{\ast}$. Define the function $\Phi_{t}:={{{f{(x_{t})}} - f^{\ast}} + {\frac{2\eta}{\lambda\beta}\left\| \epsilon_{t} \right\|^{2}}}$. Note that for any $t < \tau$, (4. ‣ 5.3 Warm-up: analysis in the deterministic setting ‣ 5 Analysis ‣ Convergence of Adam Under Relaxed Assumptions"))$+ \frac{2\eta}{\lambda\beta} \times$(6. ‣ 5.3 Warm-up: analysis in the deterministic setting ‣ 5 Analysis ‣ Convergence of Adam Under Relaxed Assumptions")) gives

The above inequality shows $\Phi_{t}$ is non-increasing and thus a Lyapunov function. Therefore, we have

where in the last inequality we use $\Phi_{1} = {{f{(x_{1})}} - f^{\ast}} = \Delta_{1}$ since $\epsilon_{1} = {{\hat{m}}_{1} - {{\nabla f}{(x_{1})}}} = 0$ in the deterministic setting.

As discussed in Section 5.1, if $\tau \leq T$, we have $F < {{f{(x_{\tau})}} - f^{\ast}} \leq \Delta_{1}$. Note that we are able to choose a large enough constant $G$ so that $F = \frac{G^{2}}{3{({{3L_{0}} + {4L_{\rho}G^{\rho}}})}}$ is greater than $\Delta_{1}$, which leads to a contradiction and shows $\tau = {T + 1}$. Therefore, holds for all $1 \leq t \leq T$. Taking a summation over $1 \leq t \leq T$ and re-arranging terms, we get

if choosing $T \geq \frac{8G\Delta_{1}}{\eta\epsilon^{2}}$, i.e., it shows convergence with a gradient complexity of $\mathcal{O}{(\epsilon^{- 2})}$ since both $G$ and $\eta$ are constants independent of $\epsilon$ in the deterministic setting.

### Extension to the stochastic setting

In this part, we briefly introduce how to extend the analysis to the more challenging stochastic setting. It becomes harder to obtain an upper bound on ${f{(x_{\tau})}} - f^{\ast}$ because $\Phi_{t}$ is no longer non-increasing due to the existence of noise. In addition, $\tau$ defined in is now a random variable. Note that all the derivations, such as Lemmas 5.4. ‣ 5.3 Warm-up: analysis in the deterministic setting ‣ 5 Analysis ‣ Convergence of Adam Under Relaxed Assumptions") and 5.5. ‣ 5.3 Warm-up: analysis in the deterministic setting ‣ 5 Analysis ‣ Convergence of Adam Under Relaxed Assumptions"), are conditioned on the random event $t < \tau$. Therefore, one can not simply take a total expectation of them to show ${\mathbb{E}}{\lbrack\Phi_{t}\rbrack}$ is non-increasing.

Fortunately, $\tau$ is in fact a stopping time with nice properties. If the noise is almost surely bounded as in Assumption 3, by a more careful analysis, we can obtain a high probability upper bound on ${f{(x_{\tau})}} - f^{\ast}$ using concentration inequalities. Then we can still obtain a contradiction and convergence under this high probability event. If the noise has sub-Gaussian norm as in Assumption 4, one can change the definition of $\tau$ to

for appropriately chosen $F$ and $\sigma$. Then at least when $t < \tau$, the noise is bounded by $\sigma$. Hence we can get the same upper bound on ${f{(x_{\tau})}} - f^{\ast}$ as if Assumption 3 still holds. However, when $t \leq T$, the lower bound ${{f{(x_{\tau})}} - f^{\ast}} > F$ does not necessarily holds, which requires some more careful analyses. The details of the proofs are involved and we defer them in Appendix C.

## Variance-reduced Adam

In this section, we propose a variance-reduced version of Adam (VRAdam). This new algorithm is depicted in Algorithm 2. Its main difference from the original Adam is that in the momentum update rule (Line 6), an additional term of ${({1 - \beta})}\left( {{{\nabla f}{(x_{t},\xi_{t})}} - {{\nabla f}{(x_{t - 1},\xi_{t})}}} \right)$ is added, inspired by the STORM algorithm. This term corrects the bias of $m_{t}$ so that it is an unbiased estimate of ${\nabla f}{(x_{t})}$ in the sense of total expectation, i.e., ${{\mathbb{E}}{\lbrack m_{t}\rbrack}} = {{\nabla f}{(x_{t})}}$. We will also show that it reduces the variance and accelerates the convergence.

Aside from the adaptive stepsize, one major difference between Algorithm 2 and STORM is that our hyper-parameters $\eta$ and $\beta$ are fixed constants whereas theirs are decreasing as a function of $t$. Choosing constant hyper-parameters requires a more accurate estimate at the initialization. That is why we use a mega-batch $\mathcal{S}_{1}$ to evaluate the gradient at the initial point to initialize $m_{1}$ and $v_{1}$ (Lines 2--3). In practice, one can also do a full-batch gradient evaluation at initialization. Note that there is no initialization bias for the momentum, so we do not re-scale $m_{t}$ and only re-scale $v_{t}$. We also want to point out that although the initial mega-batch gradient evaluation makes the algorithm a bit harder to implement, constant hyper-parameters are usually easier to tune and more common in training deep neural networks. It should be not hard to extend our analysis to time-decreasing $\eta$ and $\beta$ and we leave it as an interesting future work.

2:Draw a batch of samples 𝒮1 with size S1 and use them to evaluate the gradient ∇f (xinit,𝒮1).
3:Initialize m1 = ∇f (xinit,𝒮1), v1 = βsq m12, and $x_{2} = {x_{\text{init}} - \frac{\etam_{1}}{\left| m_{1} \right| + \lambda}}$.
5: Draw a new sample ξt and perform the following updates:
8: ${\hat{v}}_{t} = \frac{v_{t}}{1 - {({1 - \beta_{sq}})}^{t}}$
9: $x_{t + 1} = {x_{t} - {\frac{\eta}{\sqrt{{\hat{v}}_{t}} + \lambda} \odot m_{t}}}$
Algorithm 2 Variance-Reduced Adam (VRAdam)

In addition to Assumption 1, we need to impose the following assumptions which can be viewed as stronger versions of Assumptions 2 and 3, respectively.

### Assumption 5

The objective function $f$ and the component function $f{( \cdot,\xi)}$ for each fixed $\xi$ are $(\rho,L_{0},L_{\rho})$ smooth with $0 \leq \rho < 2$.

### Assumption 6

The random variables ${\{\xi_{t}\}}_{1 \leq t \leq T}$ are sampled i.i.d. from some distribution $\mathcal{P}$ such that for any $x \in {\operatorname{dom}{(f)}}$,

### Remark 6.1

Assumption 6 is stronger than Assumption 3. Assumption 3 applies only to the iterates generated by the algorithm, while Assumption 6 is a pointwise assumption over all $x \in {\operatorname{dom}{(f)}}$ and further assumes an i.i.d. nature of the random variables ${\{\xi_{t}\}}_{1 \leq t \leq T}$. Also note that, similar to Adam, it is straightforward to generalize the assumption to noise with sub-Gaussian norm as in Assumption 4.

### Analysis

In this part, we briefly discuss challenges in the analysis of VRAdam. The detailed analysis is deferred in Appendix D. Note that Corollary 5.2 requires bounded update $\left\| {x_{t + 1} - x_{t}} \right\| \leq r$ at each step. For Adam, it is easy to satisfy for a small enough $\eta$ according to Lemma 5.3. However, for VRAdam, obtaining a good enough almost sure bound on the update is challenging even though the gradient noise is bounded. To bypass this difficulty, we directly impose a bound on $\left\| {{{\nabla f}{(x_{t})}} - m_{t}} \right\|$ by changing the definition of the stopping time $\tau$, similar to how we deal with the sub-Gaussian noise condition for Adam. In particular, we define

Then by definition, both $\left\| {{\nabla f}{(x_{t})}} \right\|$ and $\left\| {{{\nabla f}{(x_{t})}} - m_{t}} \right\|$ are bounded by $G$ before time $\tau$, which directly implies bounded update $\left\| {x_{t + 1} - x_{t}} \right\|$. Of course, the new definition brings new challenges to lower bounding ${f{(x_{\tau})}} - f^{\ast}$, which requires more careful analyses specific to the VRAdam algorithm. Please see Appendix D for the details.

### Convergence guarantees for VRAdam

In the section, we provide our main results for convergence of VRAdam under Assumptions 1, 5, and 6. We consider the same definitions of problem-dependent constants $\Delta_{1},r,L$ as those in Section 4 to make the statements of theorems concise. Let $c$ be a small enough numerical constant and $C$ be a large enough numerical constant. The formal convergence result is shown in the following theorem.

### Theorem 6.2

Suppose Assumptions 1, 5, and 6 hold. For any $0 < \delta < 1$, let $G > 0$ be a constant satisfying ${G \geq {\max\left\{ {2\lambda},{2\sigma},\sqrt{{C\Delta_{1}L_{0}}/\delta},{({{C\Delta_{1}L_{\rho}}/\delta})}^{\frac{1}{2 - \rho}} \right\}}}.$ Choose $0 \leq \beta_{sq} \leq 1$ and $\beta = {a^{2}\eta^{2}}$, where $a = {40L\sqrt{G}\lambda^{- {3/2}}}$. Choose

Then with probability at least $1 - \delta$, we have $\left\| {{\nabla f}{(x_{t})}} \right\| \leq G$ for every $1 \leq t \leq T$, and ${{\frac{1}{T}{\sum_{t = 1}^{T}\left\| {{\nabla f}{(x_{t})}} \right\|^{2}}} \leq \epsilon^{2}}.$

Note that the choice of $G$, the upper bound of gradients along the trajectory of VRAdam, is very similar to that in Theorem 4.1 for Adam. The only difference is that now it also depends on the failure probability $\delta$. Similar to Theorem 4.1, there is no requirement on $\beta_{sq}$ and we choose a very small $\beta = {\mathcal{O}{(\epsilon^{2})}}$. However, the variance reduction technique allows us to take a larger stepsize $\eta = {\mathcal{O}{(\epsilon)}}$ (compared with $\mathcal{O}{(\epsilon^{2})}$ for Adam) and obtain an accelerated gradient complexity of $\mathcal{O}{(\epsilon^{- 3})}$, where we only consider the leading term. We are not sure whether it is optimal as the $\Omega{(\epsilon^{- 3})}$ lower bound in assumes the weaker bounded variance condition. However, our result significantly improves upon, which considers a variance-reduced version of Adam by combining Adam and SVRG and only obtains asymptotic convergence in the non-convex setting. Similar to Adam, our gradient complexity for VRAdam is dimension free but its dependence on $\lambda$ is $\mathcal{O}{(\lambda^{- 2})}$. Another limitation is that, the dependence on the failure probability $\delta$ is polynomial, worse than the poly-log dependence in Theorem 4.1 for Adam.

## Conclusion and future works

In this paper, we proved the convergence of Adam and its variance-reduced version under less restrictive assumptions compared to those in the existing literature. We considered a generalized non-uniform smoothness condition, according to which the Hessian norm is bounded by a sub-quadratic function of the gradient norm almost everywhere. Instead of assuming the Lipschitzness of the objective function as in existing analyses of Adam, we use a new contradiction argument to prove that gradients are bounded by a constant along the optimization trajectory. There are several interesting future directions that one could pursue following this work.

### Relaxation of the bounded noise assumption

Our analysis relies on the assumption of bounded noise or noise with sub-Gaussian norm. However, the existing lower bounds in consider the weaker bounded variance assumption. Hence, it is not clear whether the $\mathcal{O}{(\epsilon^{- 4})}$ complexity we obtain for Adam is tight in this setting. It will be interesting to see whether one can relax the assumption to the bounded variance setting. One may gain some insights from recent papers such as that analyze AdaGrad under weak noise conditions. An alternative way to show the tightness of the $\mathcal{O}{(\epsilon^{- 4})}$ complexity is to prove a lower bound under the bounded noise assumption.

### Potential applications of our technique

Another interesting future direction is to see if the techniques developed in this work for bounding gradients (including those in the the concurrent work ) can be generalized to improve the convergence results for other optimization problems and algorithms. We believe it is possible so long as the function class is well behaved and the algorithm is efficient enough so that ${f{(x_{\tau})}} - f^{\ast}$ can be well bounded for some appropriately defined stopping time $\tau$.

### Understanding why Adam is better than SGD

We want to note that our results can not explain why Adam is better than SGD for training transformers, because shows that non-adaptive SGD converges with the same $\mathcal{O}{(\epsilon^{- 4})}$ gradient complexity under even weaker conditions. It would be interesting and impactful if one can find a reasonable setting (function class, gradient oracle, etc) under which Adam or other adaptive methods provably outperform SGD.
