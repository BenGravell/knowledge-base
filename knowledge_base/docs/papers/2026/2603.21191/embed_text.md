<!-- arxiv-full-text:v1 {"arxiv_id": "2603.21191", "source": "arxiv-html"} -->

## Introduction

Large-scale language model training is constrained by a token budget $T$ rather than by a fixed number of optimization steps. In this regime, we face a familiar batch size tradeoff: increasing the batch size $B$ improves hardware utilization, yet beyond a certain scale it can degrade optimization efficiency and hurt generalization.

A token budget-aware viewpoint makes this tradeoff explicit. With batch size $B$ and sequence length $S$, the number of parameter updates is $K\coloneqq\frac{T}{BS},$ and hence $(B,S)$ and the stepsize jointly determine how effectively the token budget is converted into optimization progress. This coupling raises a central question in model training: *how should $(B,S)$ and the stepsize be chosen, and adapted, to optimize performance under a fixed token budget $T$?* Recent empirical studies have further refined this picture. In particular, critical batch sizes -- the point at which scaling $B$ stops being beneficial -- appear to scale primarily with the effective data size and only weakly with model size under a fixed token budget. Additionally, the critical batch threshold is often stage-dependent, motivating warmup and stage-wise training schedules. Taken together, these findings suggest that the batch size should be treated as a dynamic optimization variable rather than a fixed hyperparameter. However, these insights remain largely empirical: they do not provide explicit optimization error laws as functions of $(B,S,T)$, nor do they characterize when increasing batch size becomes provably detrimental under a fixed token budget.

In parallel, hyperparameter transfer frameworks such as $\mu$P have shown that, with appropriate parameterization and initialization, gradient magnitudes can be kept $\Theta$ across model scales, enabling stable training without retuning learning rates. However, these results are inherently local: they ensure that individual updates neither explode nor vanish, but do not address how batch size, sequence length, and stepsize should scale *globally* with the token budget.

Our work bridges this gap by showing that hyperparameters that are locally optimal for a given $(B,S,T)$ can become provably suboptimal as the token budget increases, even under $\mu$P-style initialization. To obtain such global scaling laws, we derive an analysis for stochastic conditional gradient (SCG) methods, a projection-free framework that underlies several modern norm-constrained training algorithms. This class of algorithms is closely aligned with modern optimizers such as Muon.

Our analysis is carried out for stochastic optimization under smoothness (A1) in a general norm, norm equivalence (A2), and a $\mu$-Kurdyka--Łojasiewicz ($\mu$-KL) error bound (A3). The $\mu$-KL condition is particularly well matched to SCG geometry, as it relates first-order stationarity to suboptimality measured in the dual norm induced by the linear minimization oracle (LMO).

Specializing our convergence bounds to the fixed-token setting $T=KBS$ yields an explicit, non-monotone dependence of the achievable optimization error on the effective batch--sequence scale $BS$. Three regimes emerge: *(i)* a noise-dominated regime where increasing $BS$ improves performance, *(ii)* an intermediate regime where the best achievable error is essentially independent of $BS$, and *(iii)* a large-batch regime where performance deteriorates as $BS$ grows under a fixed token budget.

Balancing the dominant terms yields a *critical* effective batch--sequence--token (BST) scale rule $BS\asymp T^{2/3}$ up to problem-dependent factors that we derive in this work, revealing how curvature, noise, geometry, and error-bound strength shift the optimal operating point. Importantly, our analysis shows that large batch sizes do not inherently degrade performance: when batch size, sequence length, and learning rate are chosen according to our BST scaling rule, large-batch training remains effective and token-efficient. In contrast to $\mu$P, our perspective disentangles local stability, as controlled by parameterization and initialization, from global efficiency, as governed by token-budget--aware optimization.

Our contributions are as follows:\Convergence guarantees for momentum SCG under $\mu$-KL. We establish convergence guarantees for Algorithm˜1 under the $\mu$-KL condition (A3) in a general normed geometry, explicitly tracking the effects of momentum, smoothness, and stochastic gradient noise. Our bounds hold *in expectation* under bounded-variance and $L$-smoothness assumptions.

A token-budget view of batch, sequence length, and stepsize scaling. By translating iteration complexity into token complexity via $T=KBS$, we obtain explicit $(B,S,T)$-dependent error laws and identify the *critical* effective batch size $BS$ that separates beneficial from harmful scaling.\Actionable adaptive scheduling rules. We turn the theory into concrete recipes for choosing and *updating* $(\beta,B,S)$ during training under a fixed token budget, yielding the scaling relations -- and a two-stage (and more generally multi-stage) protocol validated empirically on NanoGPT (cf., Figure˜2).

Our results complement classical large-batch heuristics such as linear learning rate scaling with warmup and adaptive batch size schedules, while offering a *projection-free* viewpoint rooted in conditional gradient geometry. They are also consistent with empirical observations that there exists a largest useful batch size depending on training stage and problem statistics, and provide an explicit optimization-side mechanism for the "too-large batch hurts" regime under a fixed token budget.

## Related Works

### Assumptions in SCG methods: smoothness

Convergence analyses for stochastic conditional gradient (SCG) (aka Frank--Wolfe) methods and, more broadly, *LMO-based* methods, have been conducted under various assumptions. Most analyses, including our analysis, assume standard $L$-smoothness. However, recent works consider relaxed notions, such as $(L_{0},L_{1})$-smoothness and other extensions beyond global smoothness; Riabinin et al., 2025")). Extending our analysis to these generalized smoothness settings is an interesting direction for future work, but it lies beyond the scope of the present paper.

### Assumptions in SCG methods: structured nonconvexity

Most prior work considers either general nonconvex or (strongly) convex objectives, failing to capture practical learning rate and batch size scaling effects observed in large-scale training. This limitation motivates our study under structured nonconvexity.

Several recent works study structured nonconvexity for LMO-based or related methods. Yang et al. ) derives an analysis under a generalized Polyak--Łojasiewicz condition, which recovers our ˜3.3 as a special case. Their method, however, does not use momentum and assumes almost surely affine bounded noise, in contrast to the bounded variance setting considered here.

Kovalev studies stochastic conditional gradient methods under star-convexity, a condition closely related to the $\mu$-KL condition. However, our work empirically validates the $\mu$-KL condition in large-scale language models training and uses it to derive a principled BST scaling rule under a fixed token budget. Finally, Riabinin et al. ) study an LMO-based method with adaptive layer-wise learning rates under the classical Polyak-Łojasiewicz (PL) condition, restricted to the deterministic setting without momentum, limiting its applicability to the large-scale stochastic settings.

### Works on Hyperparameter Transfer

Transferring hyperparameters (HPs) tuned on small proxy models to large-scale training has become increasingly important as model sizes grow. This line of work was initiated by the $\mu$P framework, which enables zero-shot transfer of learning rates across model *width*, and was later extended to other aspects of the model architecture, such as depth.

Technically, $\mu$P-style analyses focus on parameterizations that ensure gradient magnitudes and parameter updates remain $\Theta$ around initialization. These analyses assume a fixed number of tokens processed per step and do not characterize optimization behavior when the number of optimization steps is significantly larger than the model width.

To reason about the latter regime, we analyze SCG methods under a $\mu$-KL condition and derive convergence guarantees that explicitly depend on the batch size $B$, sequence length $S$, and total token budget $T$. This trajectory-level analysis allows us to characterize how optimization error accumulates as a function of $(B,S,T)$ and to derive principled scaling rules for jointly adapting batch size, sequence length, and stepsize, in contrast to prior hyperparameter transfer works that focus on local, per-step stability governing early training behavior.

### Batch Size Scheduling

Adapting the batch size during training is a well-established and practical strategy, motivated by both computational efficiency and optimization dynamics. Increasing the batch size can serve as an alternative to learning rate decay, reduce the number of parameter updates, and improve parallel utilization. However, compared to small-batch training, large batches often lead to worse generalization performance and tend to converge to sharper minima.

A complementary empirical view suggests a *critical batch size* (CBS), beyond which increasing $B$ yields diminishing token efficiency; McCandlish et al. relate CBS to the gradient noise scale and argue that it evolves during training. In the LLM setting, scaling-law work ) primarily addresses how to allocate a fixed compute budget across model size and training tokens, rather than prescribing within-run batch size schedules. More recently, Bi et al. report empirical power-law relations between compute budget, batch size, and learning rate that perform well at scale.

Taken together, these works reinforce a central practical message: the best batch size is typically not a fixed constant, but depends on the training stage, optimization hyperparameters, and budget. Motivated by this, we seek *principled, token-budget--aware* rules that characterize how the optimal effective batch--sequence scale and stepsize should co-vary with $T$, and how $(B,S,\beta)$ should be adapted. compute $d_{k+1}={\rm arg}\min_{d\in\mathcal{X}}\langle m_{k+1},d\rangle$ s.t. ∥d∥ ≤ 1 Algorithm 1 Stochastic Conditional Gradient (SCG)

## Problem Formulation and Assumptions

We consider the following problem template: where the space $\mathcal{X}$ is equipped with a standard Euclidean norm $\|\cdot\|_{2}$ induced by the inner product $\langle\cdot,\cdot\rangle$, i.e., $\|x\|_{2}=\sqrt{\langle x,x\rangle}$, and another norm $\|\cdot\|$, which possibly does not coincide with the Euclidean one. For the norm $\|\cdot\|$, we define the associated dual norm $\|x\|_{*}\coloneqq\sup_{\|x^{\prime}\|\leq 1}\langle x,x^{\prime}\rangle$ for all $x\in\mathcal{X}$. We seek to solve using Algorithm˜1.

### Assumption 3.1

Let the gradient $\nabla f(\cdot)$ be Lipschitz continuous with respect to the norm $\|\cdot\|$: where $L>0$ is the gradient Lipschitz constant.

### Assumption 3.2

There exist a constant $\rho>0$ such that Note that such a constant always exists by norm equivalence, which always holds in finite-dimensional spaces $\mathcal{X}$.

### Assumption 3.3

The objective function $f(x)$ is $\mu$-KL for some $\mu>0$: where $f^{\star}=\min_{x\in\mathcal{X}}f(x)$.

Note that condition (A3) is closely related to the Polyak-Łojasiewicz (PL) condition $\|\nabla f(x)\|_{2}^{2}\geq\mu(f(x)-f^{\star})$ originally studied in Polyak; Łojasiewicz. Variants of the PL condition have been investigated for over-parameterized models. A key distinction between the $\mu$-PL and $\mu$-KL conditions lies in the exponent of the gradient norm, making the difference between them significant when the norm is small.

Figure 1: Empirical verification of the validity of ˜3.3 during the training of a 124M NanoGPT model. The points with a loss below 5 fit a linear function well, with a slope equal to μ.

Nevertheless, condition (A3) has been extensively used in the optimization literature to analyze gradient descent under the Euclidean norm. For problems with a bounded domain,the $\mu$-KL condition is closely related to $\zeta$-quasar convexity ($\zeta$-QC), which requires $\langle\nabla f(x),x-x^{\star}\rangle\geq\zeta(f(x)-f^{\star})$ for some $x^{\star}\in\mathcal{X}$ and all $x\in\mathcal{X}$. $\zeta$-QC naturally arises in the training of neural networks. When $\mathcal{X}$ is bounded with diameter $R$ with respect to the norm $\|\cdot\|$, $\zeta$-QC implies the $\mu$-KL condition with $\mu=\zeta/R$.

In this work, we extend the applicability of the standard $\mu$-KL assumption beyond the Euclidean norm. To demonstrate its validity in practice, we track the train loss and dual gradient norm during the training of a 124M NanoGPT model. In Figure˜1, we observe that the measurements fit a linear function well, especially when the loss is below 5 (cf., the description of the full setting in Section˜6.2) We make the assumption below for the gradient noise.

### Assumption 3.4

We have access to the unbiased estimator $g(\cdot;\xi)\colon\mathcal{X}\to\mathcal{X}$ of the gradient $\nabla f(\cdot)$, where $\xi\sim\mathcal{D}$ is a random variable sampled from a probability distribution $\mathcal{D}$. We assume that the stochastic gradient estimator $g(\cdot;\xi)$ is unbiased and has $\sigma$-bounded variance for some $\sigma\geq 0$: Additionally, let $\sigma^{2}=\frac{\sigma_{\star}^{2}}{BS}$, where $B$ and $S$ are batch size and sequence length respectively.

˜3.4 is a classical assumption for the in-expectation convergence analysis of stochastic methods. We verify the validity of ˜3.4 during the training in Figure˜2 (cf., the description of the full setting in Section˜6.1).

## Theoretical Analysis

This section establishes convergence guarantees for Algorithm˜1, guiding how to choose the batch size $B$, sequence length $S$, and stepsize $\beta$ under a fixed token budget $T$. The proof and the full statement of the following theorem are deferred to Appendix˜D.

### Theorem 4.1

Let Assumptions (A1), (A2), (A3), and (3.4) hold. Let $m_{0}=g(x_{0};\xi_{0})$. Let the parameters of Algorithm˜1 and initialization $x_{0}$ be chosen as follows where $\mathcal{O}$ hides all numerical constants and $\tilde{\mathcal{O}}$ hides all numerical and logarithmic factors. Then, the output of Algorithm˜1 after $K$ iterations satisfies $\mathbb{E}[f(x_{K})-f^{\star}]\leq\varepsilon$.

### Remark 4.1

Convergence bounds for SCG were derived in Pethick et al. for the Frank-Wolfe gap, then similar results to Theorem˜4.1 were given by Kovalev ^11^1Kovalev studies a stochastic first-order non-Euclidean trust-region method with momentum and weight decay, which is equivalent to Algorithm 1. under star-convexity, a special case of $\zeta$-quasar convexity with $\zeta=1$. In light of the relationship between the $\mu$-KL condition and $\zeta$-QC in Section 3, this similarity is expected.

Our work goes beyond this connection in two important ways. First, we provide empirical justification for the use of the $\mu$-KL condition in the analysis. Second, building on this framework, we derive new theory-guided scaling rules for both the learning rate and the batch size.

In practice, the number of iterations $K$ cannot be arbitrarily large. In fact, $K$ is trivially constrained by the available token budget $T$, the two being related by the simple identity $T=K\cdot B\cdot S$. Consequently, the requirement on $K$ in Theorem˜4.1^22^2We ignore the requirement $K=\widetilde{\mathcal{O}}$, as it is always satisfied in practice; see also Corollary D.1. ‣ Appendix D In-Expectation Convergence Proofs for SCG ‣ On the Role of Batch Size in Stochastic Conditional Gradient Methods") for the details. In the sequel, we omit numerical constants for clarity. can be equivalently expressed as a condition on $T$ by multiplying both sides by $BS$: Under a fixed token budget, the expression above indicates that we cannot achieve an arbitrary optimization error $\varepsilon$. Instead, Corollary˜4.1. ‣ 4 Theoretical Analysis ‣ On the Role of Batch Size in Stochastic Conditional Gradient Methods") lower bounds the achievable error.

### Corollary 4.1 (BST Scaling Rule)

Under the setup of Theorem˜4.1, running the algorithm with parameters from Theorem˜4.1 for $\frac{T}{BS}$ iterations, we achieve the optimization error where $\tilde{\mathcal{O}}$ hides numerical and logarithmic factors.

Figure 2: Empirical gradient variance and fitted power-law models as functions of batch size B with fixed sequence length S = 1024 (left) and sequence length S with fixed batch size B = 512 (right) when training a 124M NanoGPT model on the FineWeb dataset under a fixed token budget T = 2.7B. For the left plot, the estimated scaling exponent is λ ≈ 0.9 and $B_{\rm shift}\approx 90$, while for the right plot they are λ ≈ 1.1 and $S_{\rm shift}\approx 35$. The fitted models support the validity of ˜3.4.

Corollary˜4.1. ‣ 4 Theoretical Analysis ‣ On the Role of Batch Size in Stochastic Conditional Gradient Methods") provides key insights into how the error $\varepsilon$ typically varies as the product $BS$ changes: For small batch sizes, the third term in (3. ‣ 4 Theoretical Analysis ‣ On the Role of Batch Size in Stochastic Conditional Gradient Methods")) dominates, and $\varepsilon$ improves as $BS$ increases.\When the batch size exceeds $\left(\frac{\mu\rho\sigma_{\star}}{L}\right)^{2}$, the second term in (3. ‣ 4 Theoretical Analysis ‣ On the Role of Batch Size in Stochastic Conditional Gradient Methods")) becomes dominant. In this regime, the error is independent of the batch size and sequence length, and the error instead scales as $\sim T^{-1/3}$.\Further increasing the batch size moves the system into an iteration-starved regime where the first term dominates, causing the error to deteriorate linearly.

Corollary˜4.1. ‣ 4 Theoretical Analysis ‣ On the Role of Batch Size in Stochastic Conditional Gradient Methods") indicates that the optimal achievable performance lies in the second regime, where the optimization error $\varepsilon$ is independent of both the batch size and the sequence length. From a practical perspective, however, larger batch sizes are often preferred to improve GPU utilization.

This motivates us to select the batch size and sequence length at the crossover between the second and third regimes. Following this intuition, we choose $B$ and $S$ as balancing final performance and hardware efficiency. Next, the BST rule results in the Frank--Wolfe stepsize Notably, a Frank--Wolfe stepsize of this form is used in practice when employing decoupled weight decay to train LLMs near the Chinchilla-optimal token-per-parameter (TPP) regime, where the model depth scales proportionally with the token budget.

Using $\varepsilon=\left(\frac{L\rho^{2}\sigma_{\star}^{2}}{\mu^{4}T}\right)^{1/3}$, $BS=\left(\frac{T\mu\rho\sigma_{\star}}{L}\right)^{2/3}$, and ˜3.4 in Theorem˜4.1, we obtain that the momentum parameter $\alpha$ This suggests that if we find an optimal momentum parameter $\alpha$ for a small model, under the BST scaling rule, it transfers to the larger setting.

To summarize, the BST scaling rule suggests the following choice of parameters in Algorithm˜1: In Section˜5, we provide a more detailed explanation of the BST scaling rule for the parameter choice when training under a fixed TPP or increasing the token budget for the same model.

## Strategies for Hyperparameter Choice

### Training Setup

Training a model such that holds establishes working strategies on how to train a larger model of size $D_{\rm 1}$ efficiently, given that we have a tuned configuration (i.e., the tuned values of Frank--Wolfe stepsize $\beta_{\rm 0}$, momentum parameter $\alpha$, batch size $B_{\rm 0},$ and sequence length $S_{\rm 0}$) for a smaller model of size $D_{\rm 0}$. We consider the training under a fixed TPP, which implies that the available token budget increases proportionally to the model size, i.e., $\nicefrac{{T_{\rm 1}}}{{T_{\rm 0}}}=\nicefrac{{D_{\rm 1}}}{{D_{\rm 0}}}.$ Moreover, we assume that the problem constants $L=L(D),\mu=\mu(D),$ and $\rho=\rho(D)$ change with model size. We denote the constants with subscripts $1$ and $0$ for models of size $D_{\rm 1}$ and $D_{\rm 0}$, respectively.

### Remark 5.1

In this work, we assume that the variance constant $\sigma_{\star}^{2}$ in ˜3.4 does not depend on the model size, as estimating its scaling with model size is computationally infeasible. We acknowledge, however, that in practice $\sigma_{\star}^{2}$ may change as the model size grows.

### Increasing Batch Size

We assume that the optimal batch size $B_{0}^{\star}$, sequence length $S_{0}^{\star}$, and $\beta_{0}^{\star}$ are tuned for a small model^33^3Ideally, we want all hyperparameters of the optimizer and model to be tuned for a small model, including radii $\eta$ or the initialization. However, such a task is infeasible even for a small model. Therefore, we focus on the main hyperparameters that affect the final performance the most: batch size, sequence length, and Frank--Wolfe stepsize, while we set the rest according to default values obtained from prior work. of size $D_{\rm 0}$ and satisfy, namely We now determine $B_{1}$ and $S_{1}$ such that remains satisfied for a larger model. By simple manipulation, we have Note that the ratio $\nicefrac{{T_{1}}}{{T_{0}}}$ can be replaced by $\nicefrac{{D_{1}}}{{D_{0}}}$ under fixed TPP. Knowing how $L,\mu,\rho$ change with model size and batch size,^44^4In real-world applications, the change of constants with a model size might be ignored for simplicity, but later we provide estimates for them that we use in Section 6. we can adjust the batch size and sequence length for a larger model.

### Tuning the Frank--Wolfe Stepsize

From we know that the optimal Frank--Wolfe stepsize $\beta$ should scale as $\frac{1}{K}$; therefore, we have Since we increase batch size and sequence length according to, then the optimal Frank--Wolfe stepsize for a larger model is expected to be around

### Batch Size Scheduling

We now consider a training setting in which data arrives sequentially rather than being fully available upfront. In this setting, a model is first trained on an initial corpus and subsequently updated as additional data becomes available, causing the effective token budget to grow over time.

This departs from standard pretraining assumptions and raises a practical question: how should hyperparameters such as batch size and sequence length be adapted as the available token budget increases? Naïvely reusing batch and sequence settings tuned for early stages can lead to suboptimal token efficiency and slower convergence.

In the following, we propose a principled and practically implementable pipeline for selecting and adapting batch size and sequence length in the delayed-data regime.

### First stage (training with $T_{}=T_{0}$ tokens)

Assume that in the beginning, we only have a smaller token budget $T_{}=T_{0}$, which is sufficient to train a smaller model efficiently, but insufficient to do so for a larger model.

The remaining tokens $T_{}=T_{1}-T_{0}$ arrive at a later time. Based, when training the large model using $T_{}$ tokens,^55^5We should use $T_{}$ instead of $T_{1}$ in when TPP is not fixed. our theory suggests choosing the batch size $B_{1}$ and sequence length $S_{1}$ such that where [\\Hy@raisedlink](a. ‣ 5.3 Batch Size Scheduling ‣ 5 Strategies for Hyperparameter Choice ‣ On the Role of Batch Size in Stochastic Conditional Gradient Methods")) holds if problem constants do not change significantly, that is, the effective batch--sequence scale for the large model should closely match that of the small model when the problem-dependent constants do not vary substantially with the model size (see Section˜6.4).

From, the Frank--Wolfe stepsize should be chosen as where [\\Hy@raisedlink](a. ‣ 5.3 Batch Size Scheduling ‣ 5 Strategies for Hyperparameter Choice ‣ On the Role of Batch Size in Stochastic Conditional Gradient Methods")) holds since the first stage involves $T_{0}$ tokens to train a larger model; [\\Hy@raisedlink](b. ‣ 5.3 Batch Size Scheduling ‣ 5 Strategies for Hyperparameter Choice ‣ On the Role of Batch Size in Stochastic Conditional Gradient Methods")) holds when the problem constants do not change significantly. Such a choice of the Frank--Wolfe stepsize is also recommended by the $\mu$P literature, which advocates keeping the learning rate fixed when the token budget and batch configuration are unchanged.

### Second stage (training with the full budget $T_{}+T_{}$)

Next, we receive an additional $T_{}$ tokens. Eq. (3. ‣ 4 Theoretical Analysis ‣ On the Role of Batch Size in Stochastic Conditional Gradient Methods")) suggests that we should expect the optimization error to improve from order $T_{0}^{-1/3}$ at the end of the first stage to order $T_{1}^{-1/3}$ at the end of the second stage. To realize this improvement in practice, we switch to using and during the second stage, with the full token budget $T_{1}=T_{}+T_{}$.

Overall, this hyperparameter restart strategy for Scion suggests selecting the batch size, sequence length, and Frank--Wolfe stepsize based on the total number of tokens that will ultimately be available to the model. If additional tokens arrive at later times, the same procedure can be repeated: the batch size and sequence length are increased accordingly, and the Frank--Wolfe stepsize is adjusted based on the final token budget that the larger model will observe.

### Guidelines for Practitioners

We summarize all the details on how to adjust the optimizer's parameters under the BST scaling rule below to facilitate its implementation in practice.

### Hyperparameter Scaling: From Small to Large Models

In this scenario, the model size changes. Therefore, we need to account for a change of optimization problem constants, such as $L,\mu,\rho$. We summarize the resulting procedure below: Obtain optimal values of the batch size $B_{0}^{\star}$ and sequence length $S_{0}^{\star}$, Frank--Wolfe stepsize $\beta_{0}^{\star}$ by tuning a small model, while setting momentum parameter $\alpha$ and radii $\eta$ to default values.

Estimate the problem constants $L_{0},\mu_{0},\rho_{0}$ and $L_{1},\mu_{1},\rho_{1}$ for small and large models, respectively, based on the fitted power laws.

Choose batch size $B_{1}$, sequence length $S_{1}$, and Frank--Wolfe stepsize $\beta_{1}$ for larger model using and, namely while keeping radii $\eta$ and momentum $\alpha$ unchanged.

Use new parameters to train a larger model (either from the beginning or after processing the token budget used for tuning a smaller model).

### Hyperparameter Scaling: From Small to Large Token Budget

Now assume that the model size remains the same, but the token budget increases. Therefore, the constants $L$ and $\mu$ remain the same, while we need to account for a change of $\rho$ with batch size.

Obtain optimal values of the batch size $B_{0}$ and sequence length $S_{0}$, Frank--Wolfe stepsize $\beta_{0}$ by tuning a model for a smaller token budget, while setting momentum parameter $\alpha$ and radii $\eta$ to default values.

Estimate the problem constants $\rho_{0}$ and $\rho_{1}$ for small and large token budgets, respectively, based on the fitted power laws.

Choose batch size $B_{1}$, sequence length $S_{1}$, and Frank--Wolfe stepsize $\beta_{1}$ for a larger token budget $T_{1}$ using and, namely while keeping radii $\eta$ and momentum $\alpha$ unchanged.

Use new parameters to train a model for a longer horizon $T_{1}$ (either from the beginning or after processing the token budget used for a smaller model).

## Experiments

In this section, we empirically evaluate our theoretical results by training a modded NanoGPT model on the FineWeb dataset, following the experimental setup of Pethick et al. and based on the codebase of Jordan et al.. Details are given in Appendix˜A. For Scion, we adopt the recommended operator norms (Sign $\to$ Spectral $\to$ Sign): we choose the radius $\eta=3000$ for sign-updated layers and $\eta=50$ for matrix-type layers. Concretely, this corresponds to using the polar factor of the gradient for matrix-valued parameters and the elementwise sign of the gradient for all other parameter types (cf., ).

### Verification of Assumption 3.4

First, we empirically test the validity of ˜3.4 when training a 124M base model with Scion for a fixed number of iterations $K=5100$. To approximate the gradient variance as a function of the batch size $B$, we sample $m$ mini-batch gradients of size $B$ such that $mB=32768$, and compute the empirical variance across the sampled $m$ mini-batch gradients. We track the evolution of this empirical variance over training in Figure˜B.1 and observe that it stabilizes rapidly after a short initial transient phase. In Figure˜2, we report the final empirical variance values measured at the end of training. The fitted power-law relationships support $\sigma^{2}\sim\frac{1}{BS}$ as a reasonable working approximation in the regime $BS\ll T$.

### Verification of Assumption 3.3

Second, we conduct experiments to assess the validity of ˜3.3 in practice. We use the same experimental setup as in the previous section and track both the dual norm of mini-batch gradients and the corresponding mini-batch training loss throughout training. When using Scion, the primal and dual norms are defined as where $\|x_{\ell}\|_{\ell}$ and $\|x_{\ell}\|_{*,\ell}$ denote the primal and dual norms of the $\ell$-th layer of the network with $N$ layers, respectively. Their precise definitions are provided in Table 2 (second and third columns) of Pethick et al.. See also the recent work by Crawshaw et al..

We report the joint evolution of the dual gradient norm and the training loss over the course of training in Figure˜1. We observe that, once the training loss falls below approximately $5$, the data points closely follow a linear relationship, empirically supporting the use of ˜3.3 in this setting. To quantify this relationship, we estimate the slope using a robust linear regression model with Huber loss, which interpolates between least squares and absolute-error ($\ell_{1}$) regression and thereby reduces sensitivity to outliers.

Table 1: Final validation loss when training a 124M NanoGPT model varying the batch size while keeping the validation and train sequence lengths 1024 under the token budget 1.3B (TPP 10.8). We report the average across 5 runs along with a standard deviation. Bold numbers indicate the best performance in the column. The runs in red indicate the best configuration of batch size, sequence length, and Frank–Wolfe stepsize across all runs for a given token budget.

Table 2: Final validation loss when training a 124M NanoGPT model varying the train sequence length while keeping the batch size 256 under the token budget 1.3B. The validation sequence length is always 1024. We report the average across 5 runs along with a standard deviation. ∗ indicates that not all runs had a stable decrease in validation loss. Bold numbers indicate the best performance in the column. The runs in red indicate the best configuration of batch size, sequence length, and Frank–Wolfe stepsize across all runs for a given token budget.

### Ablations on Batch Size and Sequence Length

We conduct ablation studies by varying the batch size $B$ and sequence length $S$ to identify the optimal Frank--Wolfe stepsize $\beta$ for Scion when training a base 124M model with a fixed validation sequence length $1024$. We report results under a fixed token budget of $1.3$B in Tables 1 and 2. This corresponds to TPP ratio of $10.8$ (approximately $0.5\times$ the Chinchilla optimum).

We observe that once the batch size (or sequence length) is sufficiently large, the optimal Frank--Wolfe stepsize stabilizes at $3.6\cdot 10^{-4}$. Moreover, the results indicate that, for the base model, the optimal batch size and sequence length are approximately $256$ and $1024$, yielding the lowest validation loss. Additionally, for significantly short train sequence lengths of $256$, most runs were unstable and exhibited high standard deviations since the validation loss is $1024$. We also observe that the best performance between batch sizes $256$ and $512$ differs little, indicating that performance is almost batch-independent. This aligns with Corollary˜4.1. ‣ 4 Theoretical Analysis ‣ On the Role of Batch Size in Stochastic Conditional Gradient Methods"), which shows that there exists a batch-independent regime.

### Estimating Problem-Dependent Constants

In our next experiment, we estimate the problem-dependent constants $L$, $\mu$, and $\rho$ across different model configurations in order to track how these quantities change with model size. Specifically, we train models using a fixed Frank--Wolfe stepsize $\beta=3.6\cdot 10^{-4}$, batch size $B=512$, and sequence length $S=1024$ for $5100$ iterations, following the ablation study in Section˜6.3, while varying the number of layers n_layer and the embedding dimension n_embd. In this section, we ignore the change in the constants $L,\mu,\rho$ with the batch size, but later we account for this dependency in the hyperparameter transfer. The estimated values are reported in Appendix˜B. The estimation procedure is carried out as follows.

### Smoothness constant $L$

To estimate the smoothness constant, we measure the following ratio where $g(x_{k};\xi_{k})$ and $g(x_{k-1};\xi_{k-1})$ denote the mini-batch gradients at two consecutive iterations, and the norms are defined as in the previous section. This quantity has been used in prior work as a proxy for local curvature during training). As a final estimate of $L$, we average the measured ratio over the last $100$ iterations.

### KL condition constant $\mu$

The estimation of $\mu$ follows the same procedure as in Section˜6.2. In particular, we fit a robust linear regression model with Huber loss to the relationship between the dual gradient norm and the training loss, and use the resulting slope as an estimate of $\mu$.

### Norm-equivalence constant $\rho$

In the proof of Theorem˜4.1, we apply ˜3.2 to bound terms of the form To approximate the full gradient $\nabla f(x_{k})$, we follow the same procedure described in Section˜6.1. We track the ratio between the dual norm and the Euclidean norm throughout training, and report the average of this ratio over the last $100$ iterations as an estimate of $\rho$.

We conduct the estimation procedure for several model configurations and fit a shifted power law^66^6The choice of the fitting model is flexible, and alternative functional forms could also be considered. We leave the exploration of other functional dependencies to future work. for the problem constants $L,\mu,\rho$ of the form: $\searrow 0.5\times\penalty 10000\ {}^{(a)}$ $\searrow 0.54\times\penalty 10000\ {}^{(b)}$ $\nearrow 4\times\penalty 10000\ {}^{(a)}$ $\nearrow 4.37\times\penalty 10000\ {}^{(b)}$ (a) Taking into account the practical requirement that B and S should be powers of two. We increase the product BS rounding to the closest power of two. (b) Ignoring the practical requirement that B and S should be powers of two.

Table 3: Estimated problem-dependent constants, assuming that they change with the number of layers n_layer, embedding dimension n_embd, and batch size batch_size according to. The estimations of the change for β and BS are based on and.

Interestingly, the constant $\mu$ decreases with n_layer, while it remains unchanged with n_embd. In contrast, the constants $L$ and $\rho$ increase with both n_layer and n_emdb. Using the fitted power laws, we estimate the constants for $2$ model configurations used in the experiments of size 124M and 1B.

We observe that the problem-dependent constants vary slowly with model size and remain relatively stable across the model configurations we consider. Although we use these estimates in subsequent experiments, neglecting this variation does not significantly affect the resulting derivations. The impact of these changes becomes more pronounced only in regimes where $D_{1}\gg D_{0}$. Using estimated constants, we characterize how the Frank--Wolfe stepsize $\beta$ and the product $BS$ should be set for the 1B model, knowing the optimal configuration ($B=256,S=1024,\beta=3.6\cdot 10^{-4}$) for the 124M model in Table˜3 and using,. Note that we provide two configurations for the 1B model: whether the practical requirement that the batch size and sequence length be powers of $2$ should be taken into account.

### Increasing Batch Size and Sequence Length during Training

Next, we evaluate the proposed strategy from Section˜5.3. We use the 124M model as a base model, for which we previously identified batch size $B_{0}=256$, sequence length $S_{0}=1024$, and Frank--Wolfe stepsize $\beta_{0}=3.6\cdot 10^{-4}$ as providing the best performance under a token budget $T_{0}=1.3$B. We then consider training a larger 1B model under a total token budget of $T_{1}=10.8$B (the same TPP) using the following strategies: Restarted Scion. We follow the strategy described in Section˜5.3. During the first stage, corresponding to the initial $T_{0}$ tokens, we use batch size $B_{0}=256$ and sequence length $S_{0}=1024$ with stepsize $\beta_{0}=3.6\cdot 10^{-4}$. After processing $T_{0}$ tokens, we increase the product $BS$ four times and consider two restarted schemes: $B_{1}=512$ and sequence length $S_{1}=2048$ (in yellow) and $B_{2}=1024$ and sequence length $S_{2}=1024$ (in gray), both with stepsize $\beta_{1}=\beta_{0}/2=1.8\cdot 10^{-4}$ for the remaining token budget,^77^7The batch size, sequence length, and Frank--Wolfe stepsize used in the first and second training stages are determined using and and reported in Table 3. following the derivations in and, with estimates of the problem-dependent constants taken from Section˜6.4.

Fixed *tuned*-batch Scion. We train the 1B model using the *tuned* batch size $B_{0}=256$, which was obtained on a smaller 124M model. We set the sequence length $S_{0}=1024$ with Frank--Wolfe stepsize $\beta_{0}=3.6\cdot 10^{-4}$ over the entire horizon $T_{1}=10.8$B (in light blue). This configuration is motivated by hyperparameter transfer results under the $\mu$P framework, where the hyperparameters tuned for a smaller model are used when training a larger model.

Fixed *large*-batch Scion. We train the 1B model using a larger batch size--sequence-length product. In particular, we consider two settings. For $B_{1}=512,S_{1}=2048,$ we evaluate two baselines trained from the beginning over the full token budget $T_{1}=10.8$B: one with Frank--Wolfe stepsize $\beta_{0}$ (in orange), suggested by the $\mu$P framework, and one with stepsize $\beta_{1}$ (in pink), suggested . For $B_{2}=1024\quad\text{and}\quad S_{2}=1024,$ we again train from the beginning over the full token budget $T_{1}=10.8$B, and consider two baselines: one with stepsize $\beta_{0}$ (in blue), suggested by the $\mu$P framework, and one with stepsize $\beta_{1}$ (in green), suggested .

Figure 3: Comparison of batch size and sequence length scheduling strategies when training a 1B model. The restarting schemes (in yellow and gray) are compared against fixed schedules. The validation loss is evaluated with a smaller sequence length of 1024. The values of batch sizes B0, 1, 2, sequence lengths S0, 1, and Frank–Wolfe stepsizes β0, 1 are given in the legends. The notation (B0, 1, 2, S0, 1, 2, β0, 1) characterizes which batch size, sequence length, and Frank–Wolfe stepsize are used for the particular setup. The notation (B0, S0, β0) → (B1, 2, S1, 2, β1) characterizes how parameters of Scion change after restart (e.g., batch size increases from B0 to B1, 2), respectively. The notation μP or BST indicates the rule used to select B, S, and β.

### Remark 6.1

We note that the choice of batch size $B$ and sequence length $S$ in this set of experiments is partially guided by practical considerations, as these values are typically selected as powers of $2$. We follow this convention to evaluate the performance of the restarted and small- and large-batch baselines in a setting that more closely reflects real-world practice. However, in the later experiments aimed at demonstrating hyperparameter transfer, we select $B$ and $S$ strictly according to the BST scaling rule, ignoring the aforementioned practical constraints.

Based on the results in Figure˜3, we can make the following claims.

The $\mu$P framework, where all parameters of the algorithm, i.e., Frank--Wolfe stepsize, batch size, and sequence length remain unchanged, achieves the worst performance. This result demonstrates the limitation of the $\mu$P framework, which ignores changes of batch size and sequence length. Our BST scaling instead suggests increasing the product $BS$ that leads to enhanced performance.

Both restarting strategies for Scion demonstrate competitive performance compared to the other baselines. After the restart, both variants show accelerated improvement in training and validation loss relative to the baselines. Moreover, the training curves of the restarted Scion models remain consistently below those of the other methods from the restart point onward.

In addition, we observe that quadrupling the batch size while keeping the sequence length fixed performs slightly better than doubling both the batch size and the sequence length. In this setting, the former strategy achieves approximately a $0.01$ lower validation loss than the latter.

All large-batch baselines (with both values of Frank--Wolfe stepsize: $\beta_{0}$ suggested by $\mu$P and $\beta_{1}$ suggested by BST rule) achieve similar performance. The best performance is achieved when we double the batch size and the sequence length with Frank-Wolfe stepsize set according to. The other three baselines are slightly worse and achieve the validation loss $0.005-0.01$ higher.

### Increasing Batch Size Further Does Not Help

Next, we investigate whether increasing the product $BS$ by $8$ or $16$ times yields additional benefits when training a larger 1B model. All experiments are conducted with fixed training and validation sequence lengths of $1024$. We report results using both Frank--Wolfe stepsizes suggested by the $\mu$P framework and those determined by our BST scaling rule.

The results are shown in Figure˜4. We observe that Scion with a batch size of $1024$ outperforms the baselines with batch sizes $2048$ and $4096$. This finding suggests that our BST scaling rule, which prescribes how to scale the product $BS$, provides a reliable practical guideline. Increasing the product $BS$ beyond this recommendation does not yield further performance gains. In particular, the validation loss for Scion with batch size $2048$ worsens by approximately $0.005$-$0.01$, while for batch size $4096$ the degradation is more pronounced, around $0.03$-$0.04$.

Figure 4: Comparison of fixed large batch size strategies when training a 1B model. The validation loss is evaluated with a smaller sequence length 1024. Scion with a batch size of 1024 suggested by our BST scaling rule achieves the best performance compared to other baselines with batch sizes 2048 and 4096. The values of batch sizes B1, 2, 3, sequence lengths S, and Frank–Wolfe stepsizes β0, 1 are given in the legends. The notation (B1, 2, 3, S, β0, 1) characterizes which batch size, sequence length, and Frank–Wolfe stepsize are used for the particular setup, respectively. The notation BST indicates the rule used to select the B, S, and β.

Figure 5: The final performance of the 124M model when varying the Frank–Wolfe stepsize β under different token budgets (left: 2.7B, center: 5.3B, right: 8.0B). We average the train loss over 3 random seeds and report the moving average in the window of size 500. We observe that the BST scaling rule predicts a good estimate for the optimal β when increasing the token budget. Moreover, the difference in performance between BST and μP baselines grows with a token budget.

Figure 6: The final performance of the 124M model when varying the momentum α under different token budgets (left: 1.3B, center left: 2.7B, center right: 5.3B, right: 8.0B). We average the train loss over 3 random seeds and report the moving average in the window of size 500. We observe that rule momentum parameter α transfers under BST scaling.

Figure 7: The final performance of the 1B model when varying the Frank–Wolfe stepsize β (left) and momentum parameter (right) under different token budget 10.6 TPP. We report the final train loss, smoothed in the window of size 500. We observe that the BST scaling rule predicts a good estimate for both optimal α and β when transferring from a smaller 124M model to a larger 1B model.

### Hyperparameter Transfer

From Table˜1, we know that for a base 124M model, the optimal set of hyperparameters is $B=256,S=1024,\beta=3.6\cdot 10^{-4}$ under token budget $T=1.3$B (TPP 10.8). We want to use these parameters in BST rule to obtain them for a larger training horizon or model size. In this section, the reported train losses are averaged over 3 random seeds (only for 124M) and smoothed using running average in the window of size 500 (for both 124M and 1B models). We ignore the requirement for $B$ to be the powers of $2$ in these set of experiments.

### Increasing Token Budget for 124M Model

In this section, we report the pretraining results for 124M model under increased token budgets $(i)$ $T=2.7$B (TPP 21.6), $(ii)$ $T=5.3$B (TPP 43.1), and $(iii)$ $T=8.0$B (TPP 64.7). We set a batch size for longer horizons using: $B=416$ for $T=2.7$B, $B=672$ for $T=5.3$B, and $B=896$ for $T=8.0$B, using estimates of problem-dependent constants . Momentum and sequence length are set to $\alpha=0.1$ and $S=1024$, respectively.

To demonstrate the predictive power of the BST scaling rule in finding optimal Frank--Wolfe stepsize $\beta$ , we report the final train losses when varying $\beta$ under three token budgets. Momentum parameter is fixed to $\alpha=0.1$. We expect the optimal Frank--Wolfe stepsize to be around $(i)$ $\beta=3.0\cdot 10^{-4}$, $(ii)$ $\beta=2.4\cdot 10^{-4}$, and $(iii)$ $\beta=2.1\cdot 10^{-4}$. In Figure˜5, we observe that the BST scaling rule predicts Frank--Wolfe stepsize close to the optimal one in all the cases. Moreover, we observe that $\mu$P baseline $(B=256,S=1024,\beta=3.6\cdot 10^{-4})$ becomes more suboptimal when increasing the token budget, which demonstrates the limitations of the $\mu$P framework even further.

Next, we switch to testing the BST rule for predicting the optimal value of the momentum parameter $\alpha$. According to the BST rule, $\alpha$ should transfer. Empirical results in Figure˜6 support this claim. For all values of the token budget, the optimal $\alpha$ is close to $0.09$.

### Increasing Model Size

Now we want to train a 1B model with batch size $B=1120,S=1024$ under token budget $10.8$B (TPP 10.8). In this setup, we test the predictive power of the BST scaling rule when we change the model size. The value of the batch size is set according to, using estimates from Table˜3. We expect the optimal Frank--Wolfe stepsize to be close to $1.95\cdot 10^{-4}$, while the momentum parameter to be close to $0.09$. We report the results in Figure˜7. We observe that the BST rule provides a good estimation for both the optimal momentum $\alpha$ and Frank--Wolfe stepsize $\beta$, when increasing the model size.

## Conclusion

We developed a token-budget--aware theory for scaling batch size, sequence length, and Frank--Wolfe stepsize in SCG methods under a $\mu$-KL condition. Our analysis reveals a non-monotone dependence of optimization error on the effective batch--sequence scale and yields a principled BST-scaling rule that identifies when increasing batch size is beneficial and when it becomes suboptimal. In contrast to hyperparameter transfer approaches that ensure local stability at initialization, our results characterize long-horizon, trajectory-level behavior and explain how hyperparameters should adapt as the token budget grows. Empirically, we show that large batches are not inherently detrimental: when scaled according to our theory, jointly adapting $(B,S,\beta)$ improves both token efficiency and convergence in large-scale training.

## Limitations and Future Work

Note that in our experiments, the remaining hyperparameters, such as the radii $\eta$ and the variance initialization, were adopted directly from Pethick et al. without additional tuning. This configuration already yields strong empirical performance for Scion. However, for other model architectures, these hyperparameters may not be readily available. In such cases, we recommend selecting them based on prior literature or performing a small hyperparameter sweep. We expect their precise choice to be less critical for final performance than that of the batch size or the Frank--Wolfe stepsize.

More generally, substantially suboptimal choices of these hyperparameters may affect the predictive accuracy of our BST scaling rule. Determining the minimal set of hyperparameters that must be tuned on a small model to ensure that our theoretical predictions remain practically actionable remains an important open question, which we leave for future work.

Another important question that requires further investigation is the transfer of the momentum parameter. In our experiments, we observe that increasing the model size slightly shifts the range of near-optimal values of the momentum parameter $\alpha$ to lower values ($0.06$--$0.08$), compared to the range ($0.08$--$0.1$) for the base 124M model. This shift may be due to the power-law fits being based on an insufficient number of data points, suboptimal functional dependency, or because additional training parameters, such as the token budget, should be incorporated into the scaling analysis.
