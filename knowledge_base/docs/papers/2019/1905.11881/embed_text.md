<!-- arxiv-full-text:v1 {"arxiv_id": "1905.11881", "source": "ar5iv"} -->

## Introduction

We study optimization algorithms for neural network training and aim to resolve the mystery of why adaptive methods converge fast. Specifically, we study gradient-based methods for minimizing a differentiable nonconvex function $f:{{\mathbb{R}}^{d}\rightarrow{\mathbb{R}}}$, where $f{(x)}$ can potentially be stochastic, i.e., ${f{(x)}} = {{\mathbb{E}}_{\xi}{\lbrack{F{(x,\xi)}}\rbrack}}$. Such choices of $f$ cover a wide range of problems in machine learning, and their study motivates a vast body of current optimization literature.

A widely used (and canonical) approach for minimizing $f$ is the (stochastic) gradient descent (GD) algorithm. Despite its simple form, GD often achieves superior empirical performances and theoretical guarantees. However, in many tasks such as reinforcement learning and natural language processing (NLP), adaptive gradient methods (e.g., Adagrad, ADAM, and RMSProp ) outperform SGD. Despite their superior empirical performance, our understanding of the fast convergence of adaptive methods is limited. Previous analysis has shown that adaptive methods are more robust to variation in hyper-parameters and adapt to sparse gradients (a more detailed literature review is in Appendix A). However, in practice, the gradient updates are dense, and even after extensively tuning the SGD hyperparameters, it still converges much slower than adaptive methods in NLP tasks.

We analyze the convergence of clipped gradient descent and provide an explanation for its fast convergence. Even though gradient clipping is a standard practice in tasks such as language models, it lacks a firm theoretical grounding. Goodfellow et al.; Pascanu et al. discuss the gradient explosion problem in recurrent models and consider clipping as an intuitive work around. We formalize this intuition and prove that clipped GD can *converge arbitrarily faster than fixed-step gradient descent*. This result is shown to hold under a novel smoothness condition that is *strictly weaker* than the standard Lipschitz-gradient assumption pervasive in the literature. Hence our analysis captures many functions that are not globally Lipschitz smooth. Importantly, the proposed smoothness condition is derived on the basis of extensive NLP training experiments, which are precisely the same type of experiments for which adaptive gradient methods empirically perform superior to gradient methods.

By identifying a a new smoothness condition through experiments and then using it to analyze the convergence of adaptively-scaled methods, we reduce the following gap between theory and practice. On one hand, powerful techniques such as Nesterov's momentum and variance reduction theoretically accelerate convex and nonconvex optimization. But, at least for now, they seem to have limited applicability in deep learning. On the other hand, some widely used techniques (e.g., heavy-ball momentum, adaptivity) lack theoretical acceleration guarantees. We suspect that a major reason here is the misalignment of the theoretical assumptions with practice. Our work demonstrates that the concept of acceleration critically relies on the problem assumptions and that the standard global Lipschitz-gradient condition may not hold in the case of some applications and thus must be relaxed to admit a wider class of objective functions.

### Contributions

In light of the above background, the main contributions of this paper are the following: Inspired and supported by neural network training experiments, we introduce a new smoothness condition that allows the local smoothness constant to increase with the gradient norm. This condition is *strictly weaker* than the pervasive Lipschitz-gradient assumption.

We provide a convergence rate for clipped GD under our smoothness assumption (Theorem 3).

We prove an upper-bound (Theorem 6) and a lower-bound (Theorem 4) on the convergence rate of GD under our relaxed smoothness assumption. The lower-bound demonstrates that GD with fixed step size can be *arbitrarily slower* than clipped GD.

We provide upper bounds for stochastic clipped GD (Theorem 7) and SGD (Theorem 8). Again, stochastic clipped GD can be arbitrarily faster than SGD with a fixed step size.

We support our proposed theory with realistic neural network experiments. First, in the state of art LSTM language modeling (LM) setting, we observe the function smoothness has a strong correlation with gradient norm (see Figure 2). This aligns with the known fact that gradient clipping accelerates LM more effectively compared to computer vision (CV) tasks. Second, our experiments in CV and LM demonstrate that clipping accelerates training error convergence and allows the training trajectory to cross non-smooth regions of the loss landscape. Furthermore, gradient clipping can also achieve good generalization performance even in image classification (e.g., $95.2\%$ test accuracy in 200 epochs for on ). Please see Section 5 for more details.

## New Relaxed Smoothness Condition

In this section, we motivate and develop a relaxed smoothness condition that is weaker (and thus, more general) than the usual global Lipschitz smoothness assumption. We start with the traditional definition of smoothness.

### Function smoothness (Lipschitz gradients)

Recall that $f$ denotes the objective function that we want to minimize. We say that $f$ is $L$-smooth if For twice differentiable functions, condition (1 ‣ 2 A New Relaxed Smoothness Condition ‣ Why gradient clipping accelerates training: A theoretical justification for adaptivity")) is equivalent to ${{\|{{\nabla^{2}f}{(x)}}\|} \leq L},{{\forall x} \in {\mathbb{R}}^{d}}$. This smoothness condition enables many important theoretical results. For example, Carmon et al. show that GD with $h = {1/L}$ is up to a constant optimal for optimizing smooth nonconvex functions.

But the usual $L$-smoothness assumption (1 ‣ 2 A New Relaxed Smoothness Condition ‣ Why gradient clipping accelerates training: A theoretical justification for adaptivity")) also has its limitations. Assuming existence of a global constant $L$ that upper bounds the variation of the gradient is very restrictive. For example, simple polynomials such as ${f{(x)}} = x^{3}$ break the assumption. One workaround is to assume that $L$ exists in a compact region, and either prove that the iterates do not escape the region or run projection-based algorithms. However, such assumptions can make $L$ very large and slow down the theoretical convergence rate. In Section 4, we will show that a slow rate is unavoidable for gradient descent with fixed step size, whereas clipped gradient descent can greatly improve the dependency on $L$.

The above limitations force fixed-step gradient descent (which is tailored for Lipschitz smooth functions) to converge slowly in many tasks. In Figure 1 ‣ 2 A New Relaxed Smoothness Condition ‣ Why gradient clipping accelerates training: A theoretical justification for adaptivity"), we plot the estimated function smoothness at different iterations during training neural networks. We find that function smoothness varies greatly at different iterations. From Figure 1 ‣ 2 A New Relaxed Smoothness Condition ‣ Why gradient clipping accelerates training: A theoretical justification for adaptivity"), we further find that local smoothness positively correlates with the full gradient norm, especially in the language modeling experiment. A natural question is: > Can we find a fine-grained smoothness condition under which we can design theoretically and empirically fast algorithms at the same time?

To answer this question, we introduce the relaxed smoothness condition in the next section, which is developed on the basis of extensive experiments--- Figure 1 ‣ 2 A New Relaxed Smoothness Condition ‣ Why gradient clipping accelerates training: A theoretical justification for adaptivity") provides an illustrative example.

Figure 1: Gradient norm vs local gradient Lipschitz constant on a log-scale along the training trajectory for AWD-LSTM on PTB dataset. The colorbar indicates the number of iterations during training. More experiments can be found in Section 5. Experiment details are in Appendix H.

### A new relaxed smoothness condition

We observe strong positive correlation between function smoothness and gradient norm in language modeling experiments (Figure 1 ‣ 2 A New Relaxed Smoothness Condition ‣ Why gradient clipping accelerates training: A theoretical justification for adaptivity")(a)). This observation leads us to propose the following smoothness condition that allows local smoothness to grow with function gradients.

### Definition 1

A second order differentiable function $f$ is $(L_{0},L_{1})$-smooth if Definition 1 *strictly relaxes* the usual (and widely used) $L$-smoothness. There are two ways to interpret the relaxation: First, when we focus on a compact region, we can balance the constants $L_{0}$ and $L_{1}$ such that $L_{0} \ll L$ while $L_{1} \ll L$. Second, there exist functions that are $(L_{0},L_{1})$-smooth globally, but not $L$-smooth. Hence the constant $L$ for $L$-smoothness gets larger as the compact set increases but $L_{0}$ and $L_{1}$ stay fixed. An example is given in Lemma 2.

### Remark 1

It is worth noting that we do not need the Hessian operator norm and gradient norm to necessarily satisfy the linear relation. As long as these norms are positively correlated, gradient clipping can be shown to achieve faster rate than fixed step size gradient descent. We use the linear relationship for simplicity of exposition.

### Lemma 2

Let $f$ be the univariate polynomial ${f{(x)}} = {\sum_{i = 1}^{d}{a_{i}x^{i}}}$. When $d \geq 3$, then $f$ is $(L_{0},L_{1})$-smooth for some $L_{0}$ and $L_{1}$ but not $L$-smooth.

### Proof

The first claim follows from ${\lim_{x\rightarrow\infty}\left| \frac{f'{(x)}}{f^{\operatorname{\prime\prime}}{(x)}} \right|} = {\lim_{x\rightarrow{- \infty}}\left| \frac{f'{(x)}}{f^{\operatorname{\prime\prime}}{(x)}} \right|} = \infty$. The second claim follows by the unboundedness of $f^{\operatorname{\prime\prime}}{(x)}$. ∎

### Smoothness in neural networks

We saw that our smoothness condition relaxes the traditional smoothness assumption and is motivated empirically (Figure 1 ‣ 2 A New Relaxed Smoothness Condition ‣ Why gradient clipping accelerates training: A theoretical justification for adaptivity")). Below we develop some intuition for this phenomenon. We conjecture that the proposed positive correlation results from the common components in expressions of the gradient and the Hessian. We illustrate the reasoning behind this conjecture by considering an $\ell$-layer linear network with quadratic loss---a similar computation also holds for nonlinear networks.

The $L_{2}$ regression loss of a deep linear network is ${\mathcal{L}{(Y,{f{(X)}})}}:={\|{Y - {W_{\ell}\cdotsW_{1}X}}\|}^{2}$, where $Y$ denotes labels, $X$ denotes the input data matrix, and $W_{i}$ denotes the weights in the $i^{\text{th}}$ layer. By, we know that where ${vec}{(\cdot)}$ flattens a matrix in ${\mathbb{R}}^{m \times n}$ into a vector in ${\mathbb{R}}^{mn}$; $\otimes$ denotes the Kronecker product. For constants $i,j$ such that $\ell \geq j > i > 0$, the second order derivative When $j = i$, the second term equals $0$. Based on the above expressions, we notice that the gradient norm and Hessian norm may be positively correlated due to the following two observations. First, the gradient and the Hessian share many components such as the matrix product of weights across layers. Second, if one naively upper bounds the norm using Cauchy-Schwarz, then both upper-bounds would be monotonically increasing with respect to $\| W_{i}\|$ and ${\|{{f{(X)}} - Y}\|}.$

## Problems setup and algorithms

In this section, we state the optimization problems and introduce gradient based algorithms for them that work under the new smoothness condition. Convergence analysis follows in Section 4.

Recall that we wish to solve the nonconvex optimization problem ${\min_{x \in {\mathbb{R}}^{d}}f}{(x)}$. Since in general this problem is intractable, following common practice we also seek an $\epsilon$-stationary point, i.e., a point $x$ such that ${\|{{\nabla f}{(x)}}\|} \leq \epsilon$. Furthermore, we make the following assumptions to regularize the function class studied and subsequently provide nonasymptotic convergence rate analysis.

### Assumption 1

The function $f$ is lower bounded by $f^{\ast} > {- \infty}$.

### Assumption 2

The function $f$ is twice differentiable.

### Assumption 3 ($(L_{0},L_{1})$-smoothness)

The function $f$ is $(L_{0},L_{1})$-smooth, i.e., there exist positive constants $L_{0}$ and $L_{1}$ such that ${\|{{\nabla^{2}f}{(x)}}\|} \leq {L_{0} + {L_{1}{\|{{\nabla f}{(x)}}\|}}}$---see condition.

The first assumption is standard. Twice differentiability in Assumption 2 can relaxed to first-order differentiability by modifying the definition of $(L_{0},L_{1})$-smoothness as The above inequality implies ${\nabla f}{(x)}$ is locally Lipschitz, and hence almost everywhere differentiable. Therefore, all our results can go through by handling the integrations more carefully. But to avoid complications and simplify exposition, we assume that the function is twice differentiable.

To further relax the global assumptions, by showing that GD and clipped GD are monotonically decreasing in function value, we require the above assumptions to hold just in a neighborhood determined by the sublevel set $\mathcal{S}$^11^1The constant "$1$" in the expression is arbitrary and can be replaced by any fixed positive constant. for a given initialization $x_{0}$, where

### Gradient descent algorithms

In this section, we review a few well-known variants of gradient based algorithms that we analyze. We start with the ordinary *gradient descent* with a fixed step size $\eta$, This algorithm (pedantically, its stochastic version) is widely used in neural network training. Many modifications of it have been proposed to stabilize or accelerate training. One such technique of particular importance is *clipped gradient descent*, which performs the following updates: Another algorithm that is less common in practice but has attracted theoretical interest is *normalized gradient descent*. The updates for normalized GD method can be written as The stochastic version of the above algorithms replace the gradient with a stochastic estimator.

We note that Clipped GD and NGD are almost equivalent. Indeed, for any given $\eta_{n}$ and $\beta$, if we set ${\gamma\eta_{c}} = \eta_{n}$ and $\eta_{c} = {\eta_{n}/\beta}$, then we have Therefore, clipped GD is equivalent to NGD up to a constant factor in the step size choice. Consequently, the nonconvex convergence rates in Section 4 and Section 4.2 for clipped GD also apply to NGD. We omit repeating the theorem statements and the analysis for conciseness.

## Theoretical analysis

In this section, we analyze the oracle complexities of GD and clipped GD under our relaxed smoothness condition. All the proofs are in the appendix. We highlight the key theoretical challenges that needed to overcome in Appendix B (e.g., due to absence of Lipschitz-smoothness, already the first-step of analysis, the so-called "descent lemma" fails).

Since we are analyzing the global iteration complexity, let us recall the formal definition being used. We follow the notation from Carmon et al.. For a deterministic sequence ${\{ x_{k}\}}_{k \in {\mathbb{N}}}$, define the complexity of ${\{ x_{k}\}}_{k \in {\mathbb{N}}}$ for a function $f$ as For a random process ${\{ x_{k}\}}_{k \in {\mathbb{N}}}$, we define the complexity of ${\{ x_{k}\}}_{k \in {\mathbb{N}}}$ for function $f$ as In particular, if the condition is never satisfied, then the complexity is $\infty$. Given an algorithm $A_{\theta}$, where $\theta$ denotes hyperparameters such as step size and momentum coefficient, we denote $A_{\theta}{\lbrack f,x_{0}\rbrack}$ as the sequence of (potentially stochastic) iterates generated by $A$ when operating on $f$ with initialization $x_{0}$. Finally, we define the iteration complexity of an algorithm class parameterized by $p$ hyperparameters, $\mathcal{A} = {\{ A_{\theta}\}}_{\theta \in {\mathbb{R}}^{p}}$ on a function class $\mathcal{F}$ as The definition in the stochastic setting simply replaces the expression with the expression. In the rest of the paper, "iteration complexity" refers to the quantity defined above.

### Convergence in the deterministic setting

In this section, we present the convergence rates for GD and clipped GD under deterministic setting. We start by analyzing the clipped GD algorithm with update defined in equation.

### Theorem 3

Let $\mathcal{F}$ denote the class of functions that satisfy Assumptions 1, 2, and 3-smoothness). ‣ 3 Problems setup and algorithms ‣ Why gradient clipping accelerates training: A theoretical justification for adaptivity") in set $\mathcal{S}$ defined. Recall $f^{\ast}$ is a global lower bound for function value. With ${{\eta_{c} = \frac{1}{10L_{0}}},{\gamma = {\min{\{\frac{1}{\eta_{c}},\frac{1}{10L_{1}\eta_{c}}\}}}}},$ we can prove that the iteration complexity of clipped GD (Algorithm 5) is upper bounded by The proof of Theorem 3 is included in Appendix C.

Now, we discuss the convergence of vanilla GD. The standard GD is known to converge to first order $\epsilon$-stationary points in $\mathcal{O}{({{({L{({{f{(x_{0})}} - f^{\ast}})}})}\epsilon^{- 2}})}$ iterations for ${(L,0)} -$smooth nonconvex functions. By Theorem 1 of Carmon et al., this rate is up to a constant optimal.

However, we will show below that gradient descent is suboptimal under our relaxed $(L_{0},L_{1})$-smoothness condition. In particular, to prove the convergence rate for gradient descent with fixed step size, we need to permit it benefit from an additional assumption on gradient norms.

### Assumption 4

Given an initialization $x_{0}$, we assume that This assumption is in fact *necessary*, as our next theorem reveals.

### Theorem 4

Let $\mathcal{F}$ be the class of objectives satisfying Assumptions 1, 2, 3-smoothness). ‣ 3 Problems setup and algorithms ‣ Why gradient clipping accelerates training: A theoretical justification for adaptivity"), and 4 with fixed constants $L_{0} \geq 1$, $L_{1} \geq 1$, $M > 1$. The iteration complexity for the fixed-step gradient descent algorithms parameterized by step size $h$ is at least The proof can be found in Appendix D.

### Remark 5

Theorem 1 of Carmon et al. and Theorem 4 together show that gradient descent with a fixed step size cannot converge to an $\epsilon$-stationary point faster than $\Omega\left( {{({{{L_{1}M}/{\log{(M)}}} + L_{0}})}{({{f{(x_{0})}} - f^{\ast}})}\epsilon^{- 2}} \right)$. Recall that clipped GD algorithm converges as $\mathcal{O}\left( {{L_{0}{({{f{(x_{0})}} - f^{\ast}})}\epsilon^{- 2}} + {L_{1}^{2}{({{f{(x_{0})}} - f^{\ast}})}L_{0}^{- 1}}} \right)$. Therefore, clipped GD can be arbitrarily faster than GD when $L_{1}M$ is large, or in other words, when the problem has a *poor initialization*.

Below, we provide an iteration upper bound for the fixed-step gradient descent update.

### Theorem 6

Suppose assumptions 1, 2, 3-smoothness). ‣ 3 Problems setup and algorithms ‣ Why gradient clipping accelerates training: A theoretical justification for adaptivity") and 4 hold in set $\mathcal{S}$ defined. If we pick parameters such that $h = \frac{1}{({2{({{ML_{1}} + L_{0}})}})}$, then we can prove that the iteration complexity of GD with a fixed step size defined in Algorithm 4 is upper bounded by Please refer to Appendix E for the proof. Theorem 6 shows that gradient descent with a fixed step size converges in $\mathcal{O}{({{{({{ML_{1}} + L_{0}})}{({{f{(x_{0})}} - f^{\ast}})}}/\epsilon^{2}})}$ iterations. This suggests that the lower bound in Remark 5 is tight up to a log factor in $M$.

### Convergence in the stochastic setting

In the stochastic setting, we assume GD and clipped GD have access to an unbiased stochastic gradient ${\nabla\hat{f}}{(x)}$ instead of the exact gradient ${\nabla f}{(x)}$. For simplicity, we denote $g_{k} = {{\nabla\hat{f}}{(x_{k})}}$ below. To prove convergence, we need the following assumption.

### Assumption 5

There exists $\tau > 0$, such that ${\|{{{\nabla\hat{f}}{(x)}} - {{\nabla f}{(x)}}}\|} \leq \tau$ almost surely.

Bounded noise can be relaxed to sub-gaussian noise if the noise is symmetric. Furthermore, up to our knowledge, this is the first stochastic nonconvex analysis of adaptive methods that does not require the gradient norm $\parallel{{\nabla f}{(x)}}\parallel$ to be bounded globally.

The main result of this section is the following convergence guarantee for stochastic clipped GD (based on the stochastic version of the update ).

### Theorem 7

Let Assumptions 1--3-smoothness). ‣ 3 Problems setup and algorithms ‣ Why gradient clipping accelerates training: A theoretical justification for adaptivity") and 5 hold globally with $L_{1} > 0$. Let $h = {\min\left\{ \frac{1}{16\etaL_{1}{({{\| g_{k}\|} + \tau})}},\eta \right\}}$ where $\eta = {\min\left\{ \frac{1}{20L_{0}},\frac{1}{128L_{1}\tau},\frac{1}{\sqrt{T}} \right\}}$. Then we can show that iteration complexity for stochastic clipped GD after of update is upper bounded by In comparison, we have the following upper bound for ordinary SGD.

### Theorem 8

Let Assumptions 1--3-smoothness). ‣ 3 Problems setup and algorithms ‣ Why gradient clipping accelerates training: A theoretical justification for adaptivity"), and 5 hold globally with $L_{1} > 0$. Let $h = {\min\left\{ \frac{1}{\sqrt{T}},\frac{1}{L_{1}{({M + \tau})}} \right\}}$. Then the iteration complexity for the stochastic version of GD is upper bounded by We cannot provide a lower bound for this algorithm. In fact, lower bound is not known for SGD even in the global smoothness setting. However, the deterministic lower bound in Theorem 4 is still valid, though probably loose. Therefore, the convergence of SGD still requires additional assumption and can again be arbitrarily slower compared to clipped SGD when $M$ is large.

## Experiments

(a) Learning rate 30, with clipping.

(b) Learning rate 2, without clipping.

(c) Learning rate 2, with clipping.

Figure 2: Gradient norm vs smoothness on log scale for LM training. The dot color indicates the iteration number. Darker ones correspond to earlier iterations. Note that the spans of x and y axis are not fixed.

(a) SGD with momentum.

(b) Learning rate 1, without clipping.

(c) Learning rate 5, with clipping.

Figure 3: Gradient norm vs smoothness on log scale for training. The dot color indicates the iteration number.

(a) Training loss of LSTM with different optimization parameters.

(b) Validation loss of LSTM with different optimization parameters.

(c) Training loss of with different optimization parameters.

(d) Test accuracy of with different optimization parameters.

Figure 4: Training and validation loss obtained with different training methods for LSTM and ResNet training. The validation loss plots the cross entropy. The training loss additionally includes the weight regularization term. In the legend, ‘lr30clip0.25’ denotes that clipped SGD uses step size 30 and that the L2 norm of the stochastic gradient is clipped by 0.25. In ResNet training, we threshold the stochastic gradient norm at 0.25 when clipping is applied.

In this section, we summarize our empirical findings on the positive correlation between gradient norm and local smoothness. We then show that clipping accelerates convergence during neural network training. Our experiments are based on two tasks: language modeling and image classification. We run language modeling on the Penn Treebank (PTB) dataset with AWD-LSTM models ^22^2Part of the code is available at We train on the dataset. Details about the smoothness estimation and experimental setups are in Appendix H. An additional synthetic experiment is discussed in Appendix I.

First, our experiments test whether the local smoothness constant increases with the gradient norm, as suggested by the relaxed smoothness conditions defined in (Section 2). To do so, we evaluate both quantities at points generated by the optimization procedure. We then scatter the local smoothness constants against the gradient norms in Figure 2 and Figure 3. Note that the plots are on a log-scale. A linear scale plot is shown in Appendix Figure 5.

We notice that the correlation exists in the default training procedure for language modeling (see Figure 2(a)) but not in the default training for image classification (see Figure 3(a)). This difference aligns with the fact that gradient clipping is widely used in language modeling but is less popular in ResNet training, *offering empirical support to our theoretical findings*.

We further investigate the cause of correlation. The plots in Figures 2 and 3 show that correlation appears when the models are trained with clipped GD and large learning rates. We propose the following explanation. Clipping enables the training trajectory to stably traverse non-smooth regions. Hence, we can observe that gradient norms and smoothness are positively correlated in Figures 2(a) and 3(c). Without clipping, the optimizer has to adopt a small learning rate and stays in a region where local smoothness does not vary much, otherwise the sequence diverges, and a different learning rate is used. Therefore, in other plots of Figures 2 and 3, the correlation is much weaker.

As positive correlations are present in both language modeling and image classification experiments with large step sizes, our next set of experiments checks whether clipping helps accelerate convergence as predicted by our theory. From Figure 4, we find that clipping indeed accelerates convergence. Because gradient clipping is a standard practice in language modeling, the LSTM models trained with clipping achieve the best validation performance and the fastest training loss convergence as expected. For image classification, surprisingly, clipped GD also achieves the fastest convergence and matches the test performance of SGD+momentum. These plots show that clipping can accelerate convergence and achieve good test performance at the same time.

## Discussion

Much progress has been made to close the gap between upper and lower oracle complexities for first order smooth optimization. The works dedicated to this goal provide important insights and tools for us to understand the optimization procedures. However, there is another gap that separates theoretically *accelerated* algorithms from empirically fast algorithms.

Our work aims to close this gap. Specifically, we propose a relaxed smoothness assumption that is supported by empirical evidence. We analyze a simple but widely used optimization technique known as gradient clipping and provide theoretical guarantees that clipping can accelerate gradient descent. This phenomenon aligns remarkably well with empirical observations.

There is still much to be explored in this direction. First, though our smoothness condition relaxes the usual Lipschitz assumption, it is unclear if there is an even better condition that also matches the experimental observations while also enabling a clean theoretical analysis. Second, we only study convergence of clipped gradient descent. Studying the convergence properties of other techniques such as momentum, coordinate-wise learning rates (more generally, preconditioning), and variance reduction is also interesting. Finally, the most important question is: *"can we design fast algorithms based on relaxed conditions that achieve faster convergence in neural network training?"* Our experiments also have noteworthy implications. First, though advocating clipped gradient descent in ResNet training is not a main point of this work, it is interesting to note that gradient descent and clipped gradient descent with large step sizes can achieve a similar *test performance* as momentum-SGD. Second, we learned that the performance of the baseline algorithm can actually beat some recently proposed algorithms. Therefore, when we design or learn about new algorithms, we need to pay extra attention to check whether the baseline algorithms are properly tuned.
