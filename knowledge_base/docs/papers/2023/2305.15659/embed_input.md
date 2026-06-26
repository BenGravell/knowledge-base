<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

How to Escape Sharp Minima with Random Perturbations

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Modern machine learning applications have witnessed the remarkable success of optimization algorithms that are designed to find flat minima. Motivated by this design choice, we undertake a formal study that (i) formulates the notion of flat minima, and (ii) studies the complexity of finding them. Specifically, we adopt the trace of the Hessian of the cost function as a measure of flatness, and use it to formally define the notion of approximate flat minima. Under this notion, we then analyze algorithms that find approximate flat minima efficiently. For general cost functions, we discuss a gradient-based algorithm that finds an approximate flat local minimum efficiently. The main component of the algorithm is to use gradients computed from randomly perturbed iterates to estimate a direction that leads to flatter minima. For the setting where the cost function is an empirical risk over training data, we present a faster algorithm that is inspired by a recently proposed practical algorithm called sharpness-aware minimization, supporting its success in practice.

<!-- chunk {"id": "body-0003", "role": "body", "section": "Introduction", "weight": 1.5} -->

In modern machine learning applications, the training loss function $f:{{\mathbb{R}}^{d}\rightarrow{\mathbb{R}}}$ to be optimized often has a continuum of local/global minima, and the central question is which minima lead to good prediction performance. Among many different properties for minima, "flatness" of minima has been a promising candidate extensively studied in the literature.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

Recently, there has been a resurgence of interest in flat minima due to various advances in both empirical and theoretical domains. Motivated by the extensive research on flat minima, this work undertakes a formal study that delineates a clear definition for flat minima, and studies the upper complexity bounds of finding them.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

We begin by emphasizing the significance of flat minima, based on recent advancements in the field.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Why Flat Minima?", "weight": 1.0} -->

Several recent optimization methods that are explicitly designed to find flat minima have achieved substantial empirical success. One notable example is sharpness-aware minimization (SAM), which has shown significant improvements in prediction performance of deep neural network models for image classification problems and language processing problems. Furthermore, research by Liu et al. indicates that for language model pretraining, the flatness of minima serves as a more reliable predictor of model efficacy than the pretraining loss itself, particularly when the loss approaches its minimum values.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Why Flat Minima?", "weight": 1.0} -->

Complementing the empirical evidence, recent theoretical research underscores the importance of flat minima as a desirable attribute for optimization. Key insights include: *Provable generalization of flat minima.* For overparameterized models, research by Ding et al. demonstrates that flat minima correspond to the true solutions in low-rank matrix recovery tasks, such as matrix/bilinear sensing, robust PCA, matrix completion, and regression with a single hidden layer neural network, leading to better generalization. This is further extended by Gatmiry et al. to deep linear networks learned from linear measurements. In other words, in a range of nonconvex problems with multiple minima, flat minima yield superior predictive performance.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Why Flat Minima?", "weight": 1.0} -->

*Benifits of flat minima in pretraining.* Along with the empirical validations, Liu et al. prove that in simplified masked language models, flat minima correlate with the most generalizable solutions.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Why Flat Minima?", "weight": 1.0} -->

*Inductive bias of algorithms towards flat minima.* It has been proved that various practical optimization algorithms inherently favor flat minima. This includes stochastic gradient descent (SGD), gradient descent (GD) with large learning rates, sharpness-aware minimization (SAM), and a communication-efficient variant of SGD. The practical success of these algorithms indicates that flatter minima might be linked to better generalization properties.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Why Flat Minima?", "weight": 1.0} -->

Motivated by such recent advances, the main goal of this work is to initiate a formal study of the behavior of algorithms for finding flat minima, especially an understanding of their upper complexity bounds.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Overview of Our Main Results", "weight": 1.0} -->

In this work, we formulate a particular notion of flatness for minima and design efficient algorithms for finding them. We adopt the trace of Hessian of the loss ${tr}{({{\nabla^{2}f}{({\mathbf{x}})}})}$ as a measure of "flatness," where lower values of the trace imply flatter regions within the loss landscape. The reasons governing this choice are many, especially its deep relevance across a rich variety of research, as summarized in Subsection 2.1. With this metric, we characterize a flat minimum as a local minimum where any local enhancement in flatness would result in an increased cost, effectively delineating regions where the model is both stable and efficient in terms of performance. More formally, we define the notion of $(\epsilon,\epsilon')$-flat minima in Definition 3-flat local minima). ‣ 2.2 Formal Definition of Flat Minima ‣ 2 Formulating Flat Minima ‣ How to Escape Sharp Minima with Random Perturbations"). See Section 2 for precise details.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Overview of Our Main Results", "weight": 1.0} -->

Given the notion of flat minima, the main goal of this work is to design algorithms that find an approximate flat minimum efficiently. At first glance, the goal of finding a flat minimum might seem computationally expensive because minimizing ${tr}{({\nabla^{2}f})}$ would require information about second or higher derivatives. Notably, this work demonstrates that one can reach a flat minimum using only first derivatives (gradients).

<!-- chunk {"id": "body-0013", "role": "body", "section": "Overview of Our Main Results", "weight": 1.0} -->

In Section 3, we present a gradient-based algorithm called the randomly smoothed perturbation algorithm (Algorithm 1) which finds a $(\epsilon,\sqrt{\epsilon})$-flat minimum within $\mathcal{O}\left( \epsilon^{- 3} \right)$ iterations for general costs without structure (Theorem 1). The main component of the algorithm is to use gradients computed from randomly perturbed iterates to estimate a direction that leads to flatter minima.

<!-- chunk {"id": "body-0014", "role": "body", "section": "Overview of Our Main Results", "weight": 1.0} -->

In Section 4, we consider the setting where $f$ is the training loss over a training data set and the initialization is near the set of global minima, motivated by overparametrized models in practice. In such a setting, we present another gradient-based algorithm called the sharpness-aware perturbation algorithm (Algorithm 2), inspired by sharpness-aware minimization (SAM). We show that this algorithm finds a $(\epsilon,\sqrt{\epsilon})$-flat minimum within $\mathcal{O}\left( {d^{- 1}\epsilon^{- 2}{({1 \vee \frac{1}{d^{3}\epsilon}})}} \right)$ iterations (Theorem 2) -- here $d$ denotes the dimension of the domain. This demonstrates that a practical algorithm like SAM can find flat minima much faster than the randomly smoothed perturabtion algorithm in high dimensional settings.

<!-- chunk {"id": "body-0015", "role": "body", "section": "Overview of Our Main Results", "weight": 1.0} -->

See Table 1 for a high level summary of our results.

<!-- chunk {"id": "body-0016", "role": "body", "section": "Overview of Our Main Results", "weight": 1.0} -->

Iterations for $(\epsilon,\sqrt{\epsilon})$-flat minima (Definition 3) 𝒪(ϵ−3) gradient queries (Theorem 1) Randomly Smoothed Perturbation (Algorithm 1) ${\mathcal{O}}\left({{\mathbf{d}}^{- \mathbf{1}}\mathbf{\epsilon}^{- \mathbf{2}}{({\mathbf{1} \vee \frac{\mathbf{1}}{{\mathbf{d}}^{\mathbf{3}}\mathbf{\epsilon}}})}} \right)$ gradient queries (Theorem 2) Sharpness-Aware Perturbation (Algorithm 2) Table 1: A high level summary of the main results with emphasis on the dependence on d and ϵ.

<!-- chunk {"id": "body-0017", "role": "body", "section": "Formulating Flat Minima", "weight": 1.0} -->

In this section, we formally define the notion of flat minima.

<!-- chunk {"id": "body-0018", "role": "body", "section": "Measure of Flatness", "weight": 1.0} -->

Within the literature reviewed in Subsection 1.1, a recurring metric for evaluating "flatness" in loss landscapes is the trace of the Hessian matrix of the loss function ${tr}{({{\nabla^{2}f}{({\mathbf{x}})}})}$. This metric intuitively reflects the curvature of the loss landscape around minima, where the Hessian matrix ${\nabla^{2}f}{({\mathbf{x}})}$ is expected to be positive semi-definite. Consequently, lower values of the trace indicate regions where the loss landscape is flatter. For simplicity, we will refer to this metric as *the trace of Hessian*. Key insights from recent research include: Figure 1: Figure from Liu et al.. They pretrain language models for probabilistic context-free grammar with different optimization methods, and compare their downstream accuracy. As shown in the plot, the trace of Hessian is a better indicator of the performance than the pretraining loss itself.

<!-- chunk {"id": "body-0019", "role": "body", "section": "Measure of Flatness", "weight": 1.0} -->

*Overparameterized low-rank matrix recovery.* In this domain, the trace of Hessian has been identified as the *correct notion of flatness*. Ding et al. show that the most desirable minima, which correspond to ground truth solutions, are those with the lowest trace of Hessian values. This principle is also applicable to the analysis of deep linear networks, as highlighted by Gatmiry et al., where the same measure plays a pivotal role.

<!-- chunk {"id": "body-0020", "role": "body", "section": "Measure of Flatness", "weight": 1.0} -->

*Language model pretraining.* The importance of the trace of Hessian extends to language model pretraining, as demonstrated by Liu et al.. More specifically, Liu et al. conduct an insightful experiment (see Figure 1) that demonstrates the effectiveness of the trace of Hessian as a good measure of model performance. This observation is backed by their theoretical results for simple language models.

<!-- chunk {"id": "body-0021", "role": "body", "section": "Measure of Flatness", "weight": 1.0} -->

*Model output stability.* Furthermore, the work links the trace of Hessian to the stability of model outputs in deep neural networks relative to input data variations. This relationship underscores the significance of the trace of Hessian in improving model generalization and enhancing adversarial robustness.

<!-- chunk {"id": "body-0022", "role": "body", "section": "Measure of Flatness", "weight": 1.0} -->

*Practical optimization algorithms.* Lastly, various practical optimization algorithms are shown to be inherently biased toward achieving lower values of the trace of Hessian. This includes SGD with label noise, as discussed in works by Blanc et al.; Damian et al.; Li et al., and without label noise for the language modeling pretraining. In particular, Damian et al. conduct an inspiring experiment showing a strong correlation between the trace of Hessian and the prediction performance of models (see Figure 2). Additionally, stochastic SAM is proven to prefer lower trace of Hessian values.

<!-- chunk {"id": "body-0023", "role": "body", "section": "Remark 1 (Other notions of flatness?)", "weight": 1.0} -->

Perhaps, another popular notion of flat minima in the literature is the maximum eigenvalue of Hessian $\lambda_{\max}{({{\nabla^{2}f}{(\mathbf{x})}})}$. However, recent empirical works have shown that the maximum eigenvalue of Hessian has limited correlation with the goodness of models (*e.g.*, generalization). On the other hand, as we detailed above, the trace of Hessian has been consistently brought up as a promising candidate, both theoretically and empirically. Hence, we adopt the trace of Hessian as the measure of flatness throughout.

<!-- chunk {"id": "body-0024", "role": "body", "section": "Formal Definition of Flat Minima", "weight": 1.0} -->

Motivated by the previous works discussed above, we adopt the trace of Hessian as the measure of flatness. Specifically, we consider the (normalized) trace of Hessian ${{{tr}{({{\nabla^{2}f}{({\mathbf{x}})}})}}/{{tr}{(I_{d})}}} = {{{tr}{({{\nabla^{2}f}{({\mathbf{x}})}})}}/d}$. Here we use the normalization to match the scale of flatness with the loss. For simplicity, we henceforth use the following notation: The reason we consider the normalized trace is to match its scale with that of loss $f{({\mathbf{x}})}$: the trace is in general the sum of $d$ second derivatives, so it's scale is $d$ times of that of $f{({\mathbf{x}})}$. Also, the normalization can be potentially beneficial in practice where models have different sizes.

<!-- chunk {"id": "body-0025", "role": "body", "section": "Formal Definition of Flat Minima", "weight": 1.0} -->

Larger models would typically have a higher trace of Hessian due to having more parameters, and the normalization could put them on the same scale.

<!-- chunk {"id": "body-0026", "role": "body", "section": "Formal Definition of Flat Minima", "weight": 1.0} -->

Given this choice, our notion of flat minima at a high level is *a local minimum (of $f$) for which one cannot locally decrease $\overline{\mathsf{t}\mathsf{r}}$ without increasing the cost $f$.* In particular, this concept becomes nontrivial when the set of local minima is connected (or locally forms a manifold), which is indeed the case for the over-parametrized neural networks, as shown empirically in and theoretically.

<!-- chunk {"id": "body-0027", "role": "body", "section": "Formal Definition of Flat Minima", "weight": 1.0} -->

One straightforward way to define a (locally) flat minimum is the following: a local minimum which is also a local minimum of $\overline{\mathsf{t}\mathsf{r}}$. However, this definition is not well-defined as the set of local minima of $f$ can be disjoint from that of $\overline{\mathsf{t}\mathsf{r}}$ as shown in the following example.

<!-- chunk {"id": "body-0028", "role": "body", "section": "Example 1", "weight": 1.0} -->

Hence, we consider the local optimality of $\overline{\mathsf{t}\mathsf{r}}$ restricted to the set of local minima $\mathcal{X}^{\star}$. In practice, finding local minima with respect to $\overline{\mathsf{t}\mathsf{r}}$ might be too stringent, so as an initial effort, we set our goal to find *a local minimum that is also a stationary point of $\overline{\mathsf{t}\mathsf{r}}$ restricted to the set of local minima*. To formalize this, we introduce the limit map under the gradient flow, following.

<!-- chunk {"id": "body-0029", "role": "body", "section": "Randomly Smoothed Perturbation Escapes Sharp Minima", "weight": 1.0} -->

In this section, we present a gradient-based algorithm for finding an approximate flat minimum. We first discuss the setting for our analysis.

<!-- chunk {"id": "body-0030", "role": "body", "section": "Randomly Smoothed Perturbation Escapes Sharp Minima", "weight": 1.0} -->

In order for our notion of flat minima (Definition 3-flat local minima). ‣ 2.2 Formal Definition of Flat Minima ‣ 2 Formulating Flat Minima ‣ How to Escape Sharp Minima with Random Perturbations")) to be well defined, we assume that the loss function is four times continuously differentiable near the local minima set $\mathcal{X}^{\star}$. More formally, we make the following assumption about the loss function.

<!-- chunk {"id": "body-0031", "role": "body", "section": "Assumption 1 (Loss near minima)", "weight": 1.0} -->

There exists $\zeta > 0$ such that within $\zeta$-neighborhood of the set of local minima $\mathcal{X}^{\star}$, the following properties hold: $f$ is four-times continuously differentiable.

<!-- chunk {"id": "body-0032", "role": "body", "section": "Assumption 1 (Loss near minima)", "weight": 1.0} -->

The limit map under gradient flow $\Phi$ (Definition 1. ‣ 2.2 Formal Definition of Flat Minima ‣ 2 Formulating Flat Minima ‣ How to Escape Sharp Minima with Random Perturbations")) is well-defined and is twice Lipschitz differentiable. Also, ${\Phi{({\mathbf{x}})}} \in \mathcal{X}^{\star}$ and the gradient flow starting at $\mathbf{x}$ is contained within the $\zeta$-neighborhood of $\mathcal{X}^{\star}$.

<!-- chunk {"id": "body-0033", "role": "body", "section": "Assumption 1 (Loss near minima)", "weight": 1.0} -->

It fact, the last two conditions (b), (c) are consequences of $f$ being four-times continuously differentiable. We include them for concreteness.

<!-- chunk {"id": "body-0034", "role": "body", "section": "Assumption 1 (Loss near minima)", "weight": 1.0} -->

We also discuss a preliminary step for our analysis. Since the question of finding candidates for approximate local minima (or second order stationary points) is well-studied, thanks to the vast literature on the topic over the last decade, we do not further explore it, but single out the question of seeking flatness by assuming that the initial iterate ${\mathbf{x}}_{0}$ is already close to the set of local minima $\mathcal{X}^{\star}$. For instance, assuming that the loss $f$ satisfies strict saddle properties, one can find a point ${\mathbf{x}}_{0}$ that satisfies $\left\| {{\nabla f}{({\mathbf{x}}_{0})}} \right\| \leq {\mathcal{O}(\epsilon)}$ within $\overset{\sim}{\mathcal{O}}{(\epsilon^{- 2})}$iterations. Now thanks to Assumption 1.

<!-- chunk {"id": "body-0035", "role": "body", "section": "Assumption 1 (Loss near minima)", "weight": 1.0} -->

‣ 3 Randomly Smoothed Perturbation Escapes Sharp Minima ‣ How to Escape Sharp Minima with Random Perturbations"), since we assume $f$ to be four-times continuously differentiable, it follows that $\left\| {{\mathbf{x}}_{0} - {\Phi{({\mathbf{x}}_{0})}}} \right\| \leq {\mathcal{O}\left( \left\| {{\nabla f}{({\mathbf{x}}_{0})}} \right\| \right)} \leq {\mathcal{O}(\epsilon)}$. Hence, we will often start our analysis with the initialization that is sufficiently close to the set of local minima $\mathcal{X}^{\star}$.

<!-- chunk {"id": "body-0036", "role": "body", "section": "Assumption 1 (Loss near minima)", "weight": 1.0} -->

We also define the following notation, which we will utilize throughout.

<!-- chunk {"id": "body-0037", "role": "body", "section": "Main Result", "weight": 1.0} -->

Under this setting, we present a gradient-based algorithm for finding approximate flat minima and its theoretical guarantees. Our proposed algorithm is called the randomly smoothed perturbation algorithm (Algorithm 1). The main component of the algorithm is the perturbed gradient step that is employed whenever the gradient norm is smaller than a tolerance $\epsilon_{0}$: Here ${\mathbf{g}}_{t} \sim {{Unif}{({\mathbb{S}}^{d - 1})}}$ is a random unit vector. At a high level, adds a perturbation direction ${\mathbf{v}}_{t}$ to the ordinary gradient step, where the perturbation direction ${\mathbf{v}}_{t}$ is computed using gradients at a randomly perturbed iterate ${\mathbf{x}}_{t} + {\rho{\mathbf{g}}_{t}}$ and then projecting out the gradient ${\nabla f}{({\mathbf{x}}_{t})}$.

<!-- chunk {"id": "body-0038", "role": "body", "section": "Main Result", "weight": 1.0} -->

The gradient of a randomly perturbed iterate ${\nabla f}{({{\mathbf{x}}_{t} + {\rho{\mathbf{g}}_{t}}})}$ can be also interpreted as the (stochastic) gradient of widely known *randomized smoothing* of $f$ (hence its name "randomly smoothed perturbation")---a widely known technique for nonsmooth optimization. In some sense, this work discovers a new property of randomized smoothing for nonconvex optimization: *randomized smoothing seeks flat minima!* We now present the theoretical guarantee of Algorithm 1.

<!-- chunk {"id": "body-0039", "role": "body", "section": "Main Result", "weight": 1.0} -->

0: x0, learning rates η, η′, perturbation radius ρ, tolerance ϵ0, the number of steps T. where vt ≔ Proj∇f(xt)⟂∇f(xt + ρgt) and gt ∼ Unif(𝕊d − 1) return $\hat{\mathbf{x}}$ uniformly at random111The uniformly chosen iterate is for the sake of analysis, and it’s a standard approach often used in convergence to stationary points analysis. See, e.g.,. from {x1, …, xT} Algorithm 1 Randomly Smoothed Perturbation

<!-- chunk {"id": "body-0040", "role": "body", "section": "Minimizing flatness only using gradients?", "weight": 1.0} -->

At first glance, finding a flat minimum seems computationally expensive since minimizing ${tr}{({\nabla^{2}f})}$ would require information about second or higher derivatives. Thus, Theorem 1 may sound quite surprising to some readers since Algorithm 1 only uses gradients which only pertains to information about first derivatives.

<!-- chunk {"id": "body-0041", "role": "body", "section": "Minimizing flatness only using gradients?", "weight": 1.0} -->

However, it turns out using the gradients from the perturbed iterates ${\mathbf{x}}_{t} + {\rho{\mathbf{g}}_{t}}$ lets us get access to specific third derivatives of $f$ in a parsimonious way. More precisely, as we shall see in our proof sketch, the crux of the perturbation step is that the gradients of $\overline{\mathsf{t}\mathsf{r}}$ can be estimated using gradients from perturbed iterates. In particular, we show that (see (16̄⁢(Φ⁢(𝒙_𝑡)) in expectation. ‣ 3.2 Proof Sketch of Theorem 1 ‣ 3 Randomly Smoothed Perturbation Escapes Sharp Minima ‣ How to Escape Sharp Minima with Random Perturbations"))) in expectation, it holds that Using this property, one can prove that each step of the perturbed gradient step decrease the trace of Hessian along the local minima set; see Lemma 2̄⁢(Φ⁢(𝒙_𝑡)) in expectation.

<!-- chunk {"id": "body-0042", "role": "body", "section": "Minimizing flatness only using gradients?", "weight": 1.0} -->

‣ 3.2 Proof Sketch of Theorem 1 ‣ 3 Randomly Smoothed Perturbation Escapes Sharp Minima ‣ How to Escape Sharp Minima with Random Perturbations"). We remark that this general principle of estimating higher order derivatives from gradients in a parsimonious way is inspired by recent works on understanding dynamics of sharpness-aware minimization and gradient descent at edge-of-stability.

<!-- chunk {"id": "body-0043", "role": "body", "section": "Perturbation does not increase the cost too much", "weight": 1.0} -->

First, since ${\mathbf{x}}_{0}$ is $\zeta$-close to $\mathcal{X}^{\star}$ where the loss function satisfies the Polyak--Łojasiewicz (PL) inequality, the standard linear convergence result of gradient descent guarantees that the iterate enters an $\mathcal{O}\left( \epsilon_{0} \right)$-neighborhood of $\mathcal{X}^{\star}$. We thus assume that ${\mathbf{x}}_{0}$ itself satisfies $\left\| {{\nabla f}{({\mathbf{x}}_{0})}} \right\| \leq \epsilon_{0}$ without loss of generality. We next show that the perturbation ${\mathbf{v}}_{t}$ we add at each step to the gradient only leads to a small increase in the cost. This claim follows from the following variant of well-known descent lemma.

<!-- chunk {"id": "body-0044", "role": "body", "section": "Perturbation step decreases $\\overline{\\mathsf{t}\\mathsf{r}}{({\\Phi{({\\mathbf{x}}_{t})}})}$ in expectation", "weight": 1.0} -->

Now the main part of the analysis is to show that the perturbation updates lead to decrease in the trace Hessian along $\mathcal{X}^{\star}$, i.e., decrease in $\overline{\mathsf{t}\mathsf{r}}{({\Phi{({\mathbf{x}}_{t})}})}$, as show in the following result.

<!-- chunk {"id": "body-0045", "role": "body", "section": "Putting things together", "weight": 1.0} -->

Using the results so far, we establish a high probability result by returning one of the iterates uniformly at random, following. For $t = {1,2,\ldots,T}$, and Let $P_{t}$ denote the probability of event $A_{t}$. Then, the probability of returning a $(\epsilon,\sqrt{\epsilon})$-flat minimum is simply equal to $\frac{1}{T}{\sum_{t = 1}^{T}{({1 - P_{t}})}}$. It turns out one can upper bound the sum of $P_{t}$'s using Lemma 2̄⁢(Φ⁢(𝒙_𝑡)) in expectation. ‣ 3.2 Proof Sketch of Theorem 1 ‣ 3 Randomly Smoothed Perturbation Escapes Sharp Minima ‣ How to Escape Sharp Minima with Random Perturbations"); see Appendix B for details. In particular, choosing $T = {\Omega\left({\epsilon^{- 3}\delta^{- 4}} \right)}$, we get This concludes the proof of Theorem 1.

<!-- chunk {"id": "body-0046", "role": "body", "section": "Faster Escape with Sharpness-Aware Perturbation", "weight": 1.0} -->

In this section, we present another gradient-based algorithm for finding an approximate flat minima for the case where the loss $f$ is a training loss over a training data set. More formally, we consider the following setting for training loss, following the one.

<!-- chunk {"id": "body-0047", "role": "body", "section": "Setting 1 (Training loss over data)", "weight": 1.0} -->

We note that the assumption that ${{\nabla p_{i}}{({\mathbf{x}})}} \neq \mathbf{0}$ for ${\mathbf{x}} \in \mathcal{X}^{\star}$ is without loss of generality. More precisely, by Sard's Theorem, $\mathcal{X}^{\star}$ defined above is just equal to the set of global minima, except for a measure-zero set of labels.

<!-- chunk {"id": "body-0048", "role": "body", "section": "Main Result", "weight": 1.0} -->

Under 1. ‣ 4 Faster Escape with Sharpness-Aware Perturbation ‣ How to Escape Sharp Minima with Random Perturbations"), we present another gradient-based algorithm for finding approximate flat minima (Algorithm 2). The main component of our proposed algorithm is the perturbed gradient step for random samples $i \sim {\lbrack n\rbrack}$ and $\sigma_{t} \sim {\{{\pm 1}\}}$.

<!-- chunk {"id": "body-0049", "role": "body", "section": "Remark 2", "weight": 1.0} -->

Here, note that the direction ${{\nabla f_{i}}\left( \mathbf{x}_{t} \right)}/\left\| {{\nabla f_{i}}\left( \mathbf{x}_{t} \right)} \right\|$ could be ill-defined when the stochastic gradient exactly vanishes at $\mathbf{x}_{t}$. In that case, one can use ${{\nabla f_{i}}\left( {\mathbf{x}_{t} + {\mathbf{ξ}}} \right)}/\left\| {{\nabla f_{i}}\left( {\mathbf{x}_{t} + {\mathbf{ξ}}} \right)} \right\|$ where $\mathbf{ξ}$ is a random vector with a small norm, say $\epsilon^{3}$. Hence, to avoid tedious technicality, we assume for the remaining of the paper that is well-defined at each step.

<!-- chunk {"id": "body-0050", "role": "body", "section": "Remark 2", "weight": 1.0} -->

Notice the distinction between and. In particular, for the randomly smoothed perturbation algorithm, ${\mathbf{v}}_{t}$ is computed using the gradient at a randomly perturbed iterate. On the other hand, in the update, ${\mathbf{v}}_{t}$ is computed using the *stochastic* gradient at an iterate perturbed along the *stochastic gradient direction*. The idea of computing the (stochastic) gradient at an iterate perturbed along the (stochastic) gradient direction is inspired by sharpenss-aware minimization (SAM) of Foret et al., a practical optimization algorithm showing substantial success in practice. Hence, we call our algorithm the *sharpness-aware perturbation* algorithm.

<!-- chunk {"id": "body-0051", "role": "body", "section": "Remark 2", "weight": 1.0} -->

As we shall see in detail in Theorem 2, the sharpness-aware perturbation step leads to an improved guarantee for finding a flat minimum. The key idea---as we detail in Subsection 4.2---is that this perturbation leads to faster decrease in $\overline{\mathsf{t}\mathsf{r}}$. In particular, Lemma 4̄⁢(Φ⁢(𝒙_𝑡)) faster.

<!-- chunk {"id": "body-0052", "role": "body", "section": "Remark 2", "weight": 1.0} -->

‣ 4.2 Proof Sketch of Theorem 2 ‣ 4 Faster Escape with Sharpness-Aware Perturbation ‣ How to Escape Sharp Minima with Random Perturbations") shows that each sharpness-aware perturbation decreases $\overline{\mathsf{t}\mathsf{r}}$ by $\Omega{({{{d{\min{\{ 1,{\epsilon d^{3}}\}}}} \cdot \delta^{3}}\epsilon^{2}})}$, which is $d\epsilon^{- 1}{\min{\{ 1,{\epsilon d^{3}}\}}}$ times larger than the decrease of $\Omega{({\delta^{3}\epsilon^{3}})}$ due to the randomly smoothed perturbation (shown in Lemma 2̄⁢(Φ⁢(𝒙_𝑡)) in expectation. ‣ 3.2 Proof Sketch of Theorem 1 ‣ 3 Randomly Smoothed Perturbation Escapes Sharp Minima ‣ How to Escape Sharp Minima with Random Perturbations")). We now present the theoretical guarantee of Algorithm 2.

<!-- chunk {"id": "body-0053", "role": "body", "section": "Curious role of stochastic gradients", "weight": 1.0} -->

Some readers might wonder the role of stochastic gradients in ---for instance, what happens if we replace them by *full-batch* gradients $\nabla f$? Empirically, it has been observed that for SAM's performance, it is important to use stochastic gradients over full-batch. Our analysis (see the proof sketch of Lemma 4̄⁢(Φ⁢(𝒙_𝑡)) faster. ‣ 4.2 Proof Sketch of Theorem 2 ‣ 4 Faster Escape with Sharpness-Aware Perturbation ‣ How to Escape Sharp Minima with Random Perturbations")) provides a partial explanation for the success of using stochastic gradients, from the perspective of finding flat minima. In particular, we show that stochastic gradients are important for faster decrease in the trace of the Hessian.

<!-- chunk {"id": "body-0054", "role": "body", "section": "Sharpness-aware perturbation decreases $\\overline{\\mathsf{t}\\mathsf{r}}{({\\Phi{({\\mathbf{x}}_{t})}})}$ faster", "weight": 1.0} -->

Similarly to Lemma 2̄⁢(Φ⁢(𝒙_𝑡)) in expectation. ‣ 3.2 Proof Sketch of Theorem 1 ‣ 3 Randomly Smoothed Perturbation Escapes Sharp Minima ‣ How to Escape Sharp Minima with Random Perturbations"), the main part is to show that the trace of Hessian decreases during each perturbed gradient step.

<!-- chunk {"id": "body-0055", "role": "body", "section": "Experiments", "weight": 1.0} -->

We run experiments based on training ResNet-18 on the dataset to test the ability of proposed algorithms to escape sharp global minima. Following, the algorithms are initialized at a point corresponding to a sharp global minimizer that achieve poor test accuracy. Crucially, we choose this setting because verify that test accuracy is inversely correlated with the trace of Hessian (see Figure 2). This bad global minimizer, due to, achieves $100\%$ training accuracy, but only $48\%$ test accuracy. We choose the constant learning rate of $\eta = 0.001$, which is small enough such that SGD baseline without any perturbation does not escape.

<!-- chunk {"id": "body-0056", "role": "body", "section": "Experiments", "weight": 1.0} -->

We discuss the results one by one. First of all, we highlight that the training accuracy stays at $100\%$ for all algorithms.

<!-- chunk {"id": "body-0057", "role": "body", "section": "Experiments", "weight": 1.0} -->

Comparison between two methods. In the left plot of Figure 3, we compare the performance of Randomly Smoothed Perturbation ("RS") and Sharpness-Aware Perturbation ("SA"). We choose the batch size of $128$ for both methods. Consistent with our theory, one can see that SA is more effective in escaping sharp minima even with a smaller perturbation radius $\rho$.

<!-- chunk {"id": "body-0058", "role": "body", "section": "Experiments", "weight": 1.0} -->

Different batch sizes. Our theory suggests that batch size $1$ should be effective in escaping sharp minima. We verify this in the right plot of Figure 3 by choosing the batch size to be $B = {1,64,128}$. We do see that the case of $B = 1$ is quite effective in escaping sharp minima.
