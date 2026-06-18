## Introduction

Figure 1: EoS behaviors of FO and ZO methods are captured by different spectral quantities of the Hessian. We train full-batch GD (left) and ZO-GD (right) with varying step sizes η on a CNN for CIFAR-10. For GD, the largest eigenvalue of the Hessian λmax (Ht) stabilizes near 2/η. For ZO-GD, the trace of the Hessian Tr(Ht) instead stabilizes slightly below 2/η.

Figure 2: Zeroth-order methods operate at the mean-square edge of stability. We train full-batch ZO methods on a CNN for CIFAR-10 and track the curvature terms defining the mean-square stability interval from Section 4.2. Across all panels, each color denotes one run; the solid curve is the lower-band term, the dash-dotted curve is the upper-band term, and the dashed line is the predicted stability threshold. Left (ZO-GD, varying η): lower Tr(Ht), upper Tr(Ht) + 2 λmax (Ht), threshold 2/η in Eq. equation 23. Middle (ZO-GDM, varying β with fixed η = 10−4): lower Tr(Ht), upper ${{Tr}{({\mathbf{H}}_{t})}} + {\frac{2}{1 + \beta}\lambda_{\max}{({\mathbf{H}}_{t})}}$, threshold 2 (1−β)/η in Eq. equation 24. Right (ZO-Adam, varying η with fixed (β1,β2) = (0.9,0.999)): lower Tr(Pt−1 Ht), upper ${{Tr}{({{\mathbf{P}}_{t}^{- 1}{\mathbf{H}}_{t}})}} + {\frac{2}{1 + \beta_{1}}\lambda_{\max}{({{\mathbf{P}}_{t}^{- 1}{\mathbf{H}}_{t}})}}$, threshold 2/η in Eq. equation 25. Across all methods, the threshold stays within (or very close to) the stability interval throughout training, indicating mean-square EoS behavior.

Zeroth-order (ZO) optimization methods, which rely only on function evaluations, are widely used when gradients are unavailable, unreliable, or expensive to compute. Such a setting arises in black-box learning, derivative-free control, and increasingly in modern large-model pipelines, where memory and systems constraints can make backpropagation costly. Recent work shows that ZO methods based on two-point function evaluations can fine-tune large language models (LLMs) with competitive accuracy while substantially reducing memory usage and compute overhead. Despite their growing practical relevance, the training dynamics of ZO methods in deep learning remain far less understood than those of first-order (FO) optimizers.

For FO optimization in deep learning, one prominent empirical phenomenon is the *edge of stability* (EoS). In full-batch gradient descent (GD) with step size $\eta$ on a quadratic objective ${f_{quad}{({\mathbf{x}})}} = {\frac{1}{2}{\mathbf{x}}^{\top}{\mathbf{H}}{\mathbf{x}}}$, the iterates diverge when $\eta > {{2/\lambda_{\max}}{({\mathbf{H}})}}$. In neural network training, however, optimization often remains well-behaved even at step sizes beyond this local quadratic threshold. Along the training trajectory $\{{\mathbf{x}}_{t}\}$, the top eigenvalue of the Hessian $\lambda_{\max}{({\mathbf{H}}_{t})}$ increases early in training and then stabilizes near the threshold $2/\eta$ over long horizons. This phenomenon has motivated a growing line of work aimed at understanding its mechanism and its connections to stability, curvature, and implicit regularization in deep learning optimization dynamics.

In this work, we ask whether a similar phenomenon arises in *zeroth-order* training. At first glance, this is far from obvious: ZO methods update parameters by drawing random search directions at every iteration, and their stability cannot be understood through the deterministic arguments typically used to explain FO dynamics and stability.

As a preliminary experiment, Figure 1 compares full-batch (first-order) GD and zeroth-order gradient descent (ZO-GD) with varying step sizes $\eta$. For GD, the top Hessian eigenvalue $\lambda_{\max}{({\mathbf{H}}_{t})}$ stabilizes near $2/\eta$, consistent with the behavior predicted by standard EoS theory. For ZO-GD, however, $\lambda_{\max}{({\mathbf{H}}_{t})}$ does not exhibit the same trend; instead, perhaps surprisingly, the Hessian trace ${Tr}{({\mathbf{H}}_{t})}$ stabilizes slightly below $2/\eta$. This suggests that ZO training may be governed by a different stability mechanism than FO training, and that ZO methods may exhibit their own EoS phenomenon in deep learning.

These observations motivate the following fundamental questions: ($i$) *do ZO methods operate at the edge of stability in neural network training*, and ($ii$) if so, *which curvature-related quantity governs their stability*?

We introduce a mean-square linear stability theory for ZO methods to investigate these questions. In Section 4, we provide an exact step size characterization of mean-square linear stability under the linearized dynamics for a family of ZO optimizers, including ZO-GD and its momentum and preconditioned variants. Unlike FO methods, whose stability is governed solely by the largest Hessian eigenvalue, mean-square stability of ZO methods depends on the entire Hessian spectrum. Moreover, momentum affects stability in opposite ways: increasing $\beta$ enlarges the stable regime for GD with momentum (GDM), but shrinks it for ZO-GD with momentum (ZO-GDM). Since computing the full spectrum is typically infeasible, we also derive tractable bounds that depend only on the Hessian trace and the largest eigenvalue (summarized in Table 1).

Technically, our analysis introduces a cone-preserving linear covariance operator with a rank-one global coupling term to capture the dynamics of the ZO second-moment recursion. This reduction allows one to characterize its spectral radius using the Krein--Rutman Theorem and derive the explicit mean-square stability conditions.

In Section 5, we empirically find that full-batch ZO methods operate at the *mean-square* edge of stability across architectures and tasks: ZO methods (ZO-GD, ZO-GDM, and ZO-Adam) consistently stabilize near the predicted mean-square stability boundary. Notably, this behavior is governed primarily by trace-based curvature quantities, providing new insight into how large step sizes implicitly bias ZO training toward solutions with small (preconditioned) Hessian trace.

Linear Stability Condition

$\eta_{mean}^{\star} = \eta_{ms}^{\star} = \frac{2}{\lambda_{\max}({\mathbf{H}})}$

$\eta_{mean}^{\star} = \eta_{ms}^{\star} = \frac{2\left( {1 + \beta} \right)}{\lambda_{\max}({\mathbf{H}})}$

$\eta_{mean}^{\star} = \eta_{ms}^{\star} = \frac{2\left( {1 + \beta_{1}} \right)}{\left( {1 - \beta_{1}} \right)\lambda_{\max}\left( {{\mathbf{P}}^{- 1}{\mathbf{H}}} \right)}$

$\eta_{ms}^{\star} \leq \frac{2}{{Tr}({\mathbf{H}})}$

$\eta_{ms}^{\star} \geq \frac{2}{{{Tr}({\mathbf{H}})} + {2\lambda_{\max}({\mathbf{H}})}}$

$\eta_{ms}^{\star} \leq \frac{2\left( {1 - \beta} \right)}{{Tr}({\mathbf{H}})}$

$\eta_{ms}^{\star} \geq \frac{2\left( {1 - \beta} \right)}{{{Tr}({\mathbf{H}})} + \frac{2\lambda_{\max}({\mathbf{H}})}{1 + \beta}}$

$\eta_{ms}^{\star} \leq \frac{2}{{Tr}\left( {{\mathbf{P}}^{- 1}{\mathbf{H}}} \right)}$

$\eta_{ms}^{\star} \geq \frac{2}{{{Tr}\left( {{\mathbf{P}}^{- 1}{\mathbf{H}}} \right)} + \frac{2\lambda_{\max}\left( {{\mathbf{P}}^{- 1}{\mathbf{H}}} \right)}{1 + \beta_{1}}}$

Table 1: Summary of linear stability conditions for FO and ZO methods under the linearized dynamics (Definition 1). For FO methods of GD, GDM, and Adam, we report the exact critical step size η⋆, and the mean and mean-square thresholds coincide. For ZO methods, we report lower and upper bounds on the mean-square critical step size ηms⋆; the critical step size in the mean, ηmean⋆, matches the corresponding FO threshold. For Adam and ZO-Adam, the reported conditions correspond to the frozen-preconditioner variants and are governed by the spectrum of the preconditioned Hessian P−1 H. See Section 4 for details.

## Related work

Zeroth-order optimization. ZO methods optimize objectives using only function evaluations, typically via the standard two-point estimator along a random direction. Empirically, Malladi et al. report that ZO methods can fine-tune LLMs with performance comparable to FO methods while achieving up to $12 \times$ memory and up to $2 \times$ GPU-hour reduction, highlighting ZO optimization as a promising approach for memory-efficient fine-tuning. ZO methods have also been applied to adversarial robustness, reinforcement learning, private fine-tuning and distributed learning, where gradients may be noisy, unavailable, or expensive to compute or communicate.

On the theory side, most prior work studies ZO methods through the lens of classical (non)convex optimization, emphasizing convergence under small step sizes and smoothness assumptions. Notably, Zhang et al. study the implicit bias of ZO-GD under smooth convex objectives and show that it favors solutions with small Hessian trace.

Edge of stability. Recent empirical work shows that FO methods often train near instability. In particular, Cohen et al. identify the edge of stability (EoS) in full-batch GD, where $\lambda_{\max}{({\mathbf{H}}_{t})}$ grows early in training and then equilibrates near $2/\eta$. This observation has motivated extensive follow-up work on the mechanisms and implications of EoS. EoS-type behavior has also been studied for momentum and adaptive optimizers, mini-batch stochastic gradient descent (SGD), and other families of FO optimizers, including sharpness-aware minimization and schedule-free methods.

Dynamical stability analysis of optimizers. A growing body of work studies optimization methods through the lens of dynamical stability. Recent work analyzes *linear stability* by examining the behavior of the linearized dynamics under a local quadratic approximation, extending beyond GD to momentum methods and stochastic optimization. For SGD, prior analyses have characterized linear stability condition in the mean-square sense, for higher moments, and in probability. Most closely related to our setting, Mulayoff & Michaeli derive the exact mean-square stability threshold of mini-batch SGD and show that it is monotonically non-decreasing in the batch size. Our work also studies mean-square linear stability, but for ZO methods, where stochasticity arises from the estimator directions even under full-batch training.

## Preliminaries

We consider the optimization problem

for a loss function $f:{{\mathbb{R}}^{d}\rightarrow{\mathbb{R}}}$ and a model parameter $\mathbf{x}$, and study the dynamics of zeroth-order (ZO) optimization methods. ZO methods iteratively update a sequence of iterates ${\{{\mathbf{x}}_{t}\}}_{t \geq 0}$ based solely on function evaluations without evaluating any gradients. We analyze the three most popular types of ZO methods: ZO-GD, ZO-GDM, and ZO-Adam.

ZO Gradient Descent (ZO-GD) replaces the gradient ${\nabla f}{({\mathbf{x}}_{t})}$ in the GD update with a gradient estimate $\hat{\nabla}f{({\mathbf{x}}_{t})}$:

for a step size $\eta > 0$. We consider the standard two-point estimator, defined as

where ${\mathbf{u}}_{t}\overset{i.i.d.}{\sim}\mathcal{N}{(\mathbf{0},{\mathbf{I}})}$ and $\mu > 0$ is a smoothing parameter. In general, $\hat{\nabla}f{({\mathbf{x}}_{t})}$ is a biased estimator of ${\nabla f}{({\mathbf{x}}_{t})}$, with bias that vanishes as $\mu\rightarrow 0$.

ZO Gradient Descent with Momentum (ZO-GDM) combines Polyak momentum terms with gradient estimates:

for a step size $\eta > 0$ and a momentum parameter $\beta \in {\lbrack 0,1)}$.

ZO-Adam combines adaptive moment estimation (Adam) with gradient estimates:

for step size $\eta > 0$, momentum parameters ${\beta_{1},\beta_{2}} \in {\lbrack 0,1)}$, and $\epsilon > 0$, where ${\mathbf{P}}_{t + 1}$ is a preconditioner defined using an exponential moving average (EMA) of squared (estimated) gradients:

and $\odot$ denotes element-wise multiplication. This form is equivalent to the standard bias-corrected Adam update, written as a preconditioned momentum step.

In practical neural network training, the short-term stability behavior of Adam is often well approximated by a *frozen-preconditioner* variant, in which the preconditioner is held fixed at its current value. Motivated by this, we also consider the corresponding ZO analogue.

Frozen ZO-Adam uses a fixed preconditioner ${\mathbf{P}} \succ 0$ with a step size $\eta > 0$:

and a momentum parameter $\beta_{1} \in {\lbrack 0,1)}$. This optimizer is introduced purely for theoretical analysis and serves as the ZO analogue of *Frozen Adam*, which was used to study the *adaptive edge of stability* of Adam.

## Linear stability analysis

Directly analyzing the full dynamics of optimizers in deep learning is typically intractable. Instead, we adopt the standard dynamical systems approach of studying stability near a local minimizer via the *linearized dynamics*. Exponential stability of the linearized dynamics implies local stability of the corresponding nonlinear dynamics near the equilibrium, which justifies linear stability analysis as a principled tool.

### Definition 1 (Linearized dynamics)

Let ${\mathbf{x}}^{\star}$ be a local minimizer of $f$, and assume that $f$ is twice differentiable in a neighborhood of ${\mathbf{x}}^{\star}$. Let ${\mathbf{H}}:={{\nabla^{2}f}{({\mathbf{x}}^{\star})}}$ be the Hessian at ${\mathbf{x}}^{\star}$. The *linearized dynamics* of an optimizer around ${\mathbf{x}}^{\star}$ are the dynamics obtained by applying the optimizer to the quadratic Taylor approximation of $f$ at ${\mathbf{x}}^{\star}$,

Throughout, we assume ${\mathbf{H}} \succeq 0$ and ${\mathbf{H}} \neq \mathbf{0}$. Let $\lambda_{1} \geq \cdots \geq \lambda_{d} \geq 0$ denote the eigenvalues of $\mathbf{H}$, and define ${\lambda_{\max}{({\mathbf{H}})}}:=\lambda_{1}$ and ${{Tr}{({\mathbf{H}})}}:={\sum_{i = 1}^{d}\lambda_{i}}$.

We next formalize the notion of linear stability for the resulting (possibly stochastic) optimizer dynamics.

### Definition 2 (Linear stability)

Let ${\mathbf{x}}^{\star}$ be as in Definition 1. ‣ 4 Linear stability analysis ‣ Zeroth-Order Optimization at the Edge of Stability"), and let ${\{{\mathbf{x}}_{t}\}}_{t \geq 0}$ denote the iterates generated by an optimizer applied to $f_{quad}$.

We say the optimizer is *linearly stable in the mean* if

We say the optimizer is *mean-square linearly stable* if

Mean-square linear stability implies linear stability in the mean by Jensen's inequality. For deterministic optimizers, the expectation is redundant, and the two notions coincide.

Our goal is to theoretically characterize the *critical step size* that guarantees linear stability of ZO methods and empirically connect it to the edge of stability phenomena.

### Definition 3 (Critical step size)

Consider an optimizer with step size $\eta > 0$ applied to $f_{quad}$, producing iterates ${\{{\mathbf{x}}_{t}\}}_{t \geq 0}$. The *critical step size in the mean* is defined as

and the *critical step size in the mean-square* is defined as

Next, we review known stability thresholds for FO methods (Section 4.1) and present our main results for ZO methods (Section 4.2). All proofs are deferred to Appendix A.

### Linear stability of first-order methods

The first-order (FO) counterparts of the ZO optimizers in Section 3, namely GD, GDM, and Frozen Adam, are deterministic, so their mean and mean-square linear stability conditions coincide. A key takeaway is that FO linear stability is governed solely by the top eigenvalue of the (preconditioned) Hessian, as summarized below.

### Proposition 1 (Stability of GD)

The critical step size of GD is $\eta_{mean}^{\star} = \eta_{ms}^{\star} = {{2/\lambda_{\max}}{(\mathbf{H})}}$.

The stability condition of GD with Momentum (GDM) was established in Theorem 2 of Cohen et al..

### Proposition 2 (Stability of GDM)

The critical step size of GDM is $\eta_{mean}^{\star} = \eta_{ms}^{\star} = {{{2{({1 + \beta})}}/\lambda_{\max}}{(\mathbf{H})}}$.

The stability condition of Frozen Adam was established in Lemma 2 and Proposition 1 of Cohen et al..

### Proposition 3 (Stability of Frozen Adam)

The critical step size of Frozen Adam is

### Linear stability of zeroth-order methods

The inherent stochasticity in ZO updates fundamentally changes the linear stability as shown in Figure 1. However, the *mean* dynamics of a ZO method matches that of its FO counterpart, and $\eta_{mean}^{\star}$ coincides with the FO critical step size presented in Section 4.1. This is due to the fact that under the quadratic model $f_{quad}$ in Definition 1. ‣ 4 Linear stability analysis ‣ Zeroth-Order Optimization at the Edge of Stability"), the two-point estimator is *unbiased*: ${{\mathbb{E}}\left\lbrack {\hat{\nabla}f_{quad}{({\mathbf{x}}_{t})}} \right\rbrack} = {{\nabla f_{quad}}{({\mathbf{x}}_{t})}}$. The intricacy of ZO linear stability is only captured by the *mean-square* stability. In particular, we show that $\eta_{ms}^{\star}$ for ZO-GD, ZO-GDM, and Frozen ZO-Adam, depends on the entire eigen spectrum of the (preconditioned) Hessian and is dominated by its trace value.

### Theorem 1 (Stability of ZO-GD)

For ZO-GD, $\eta_{mean}^{\star} = {{2/\lambda_{\max}}{(\mathbf{H})}}$, and the mean-square critical step size $\eta_{ms}^{\star}$ is the unique $\eta > 0$ satisfying

which admits the bounds

### Remark 1 (Computing $\eta_{ms}^{\star}$)

If the full spectrum ${\{\lambda_{i}\}}_{i = 1}^{d}$ were available, $\eta_{ms}^{\star}$ in Theorem 1. ‣ 4.2 Linear stability of zeroth-order methods ‣ 4 Linear stability analysis ‣ Zeroth-Order Optimization at the Edge of Stability") can be computed by solving ${\sum_{i = 1}^{d}{({{{\eta\lambda_{i}}/2}{({1 - {\eta\lambda_{i}}})}})}} = 1$ over $\eta \in {(0,{{1/\lambda_{\max}}{({\mathbf{H}})}})}$. In practice, we instead track the bounds equation 17. ‣ 4.2 Linear stability of zeroth-order methods ‣ 4 Linear stability analysis ‣ Zeroth-Order Optimization at the Edge of Stability"), which depend only on ${Tr}{({\mathbf{H}})}$ and $\lambda_{\max}{({\mathbf{H}})}$ and can be estimated efficiently during training, which is critical for large models.

### Theorem 2 (Stability of ZO-GDM)

For ZO-GDM, $\eta_{mean}^{\star} = {{{2{({1 + \beta})}}/\lambda_{\max}}{(\mathbf{H})}}$, and the mean-square critical step size $\eta_{ms}^{\star}$ is the unique $\eta > 0$ satisfying

which admits the bounds

### Proof sketch

We analyze the recursions of the second-moment matrices ${\mathbb{E}}{\lbrack{{\mathbf{x}}_{t}{\mathbf{x}}_{t}^{\top}}\rbrack}$, ${\mathbb{E}}{\lbrack{{\mathbf{x}}_{t}{\mathbf{m}}_{t}^{\top}}\rbrack}$, and ${\mathbb{E}}{\lbrack{{\mathbf{m}}_{t}{\mathbf{m}}_{t}^{\top}}\rbrack}$. Using the Isserlis' Theorem to evaluate Gaussian fourth moments, we obtain a linear recursion that can be expressed as a cone-preserving linear operator on a product cone. Mean-square stability is then equivalent to this operator having spectral radius smaller than one. We characterize this spectral radius using Theorem 4. ‣ A.2 Spectral analysis of the covariance operator ‣ Appendix A Proofs for the mean-square stability analysis of zeroth-order methods ‣ Zeroth-Order Optimization at the Edge of Stability") in Appendix A.2, which leverages the Krein--Rutman Theorem and leads to the explicit mean-square stability condition. ∎

### Theorem 3 (Stability of Frozen ZO-Adam)

Let ${\overset{\sim}{\lambda}}_{1} \geq {\overset{\sim}{\lambda}}_{2} \geq \cdots \geq {\overset{\sim}{\lambda}}_{d} \geq 0$ denote the eigenvalues of the preconditioned Hessian $\mathbf{P}^{- 1}\mathbf{H}$. For Frozen ZO-Adam, $\eta_{mean}^{\star} = {{2{({1 + \beta_{1}})}}/\left( {{({1 - \beta_{1}})}\lambda_{\max}{({\mathbf{P}^{- 1}\mathbf{H}})}} \right)}$. Assuming ${\mathbf{P}\mathbf{H}} = {\mathbf{H}\mathbf{P}}$, the mean-square critical step size $\eta_{ms}^{\star}$ is the unique $\eta > 0$ satisfying

and it admits the bounds

### Remark 2 (Commutativity assumption)

The condition ${{\mathbf{P}}{\mathbf{H}}} = {{\mathbf{H}}{\mathbf{P}}}$ ensures that ${\mathbf{P}}^{- 1}{\mathbf{H}}$ is diagonalizable in the same eigenbasis as $\mathbf{H}$, which allows the mean-square dynamics to decouple across eigendirections and enables a tractable spectral analysis. Without commutativity, the second-moment recursion generally couples different eigenspaces, and obtaining an explicit stability characterization becomes substantially less tractable. Empirically, in neural network training with ZO-Adam, we observe that ${\mathbf{P}}_{t}$ and ${\mathbf{H}}_{t}$ are nearly commuting: the relative commutator Frobenius norm ${\|{{{\mathbf{P}}_{t}{\mathbf{H}}_{t}} - {{\mathbf{H}}_{t}{\mathbf{P}}_{t}}}\|}_{F}/{\|{{\mathbf{P}}_{t}{\mathbf{H}}_{t}}\|}_{F}$ decreases from $0.8$--$0.9$ at initialization to below $0.05$ and remains below $0.05$ throughout training (see Appendix D.3).

Taken together, Theorems 1. ‣ 4.2 Linear stability of zeroth-order methods ‣ 4 Linear stability analysis ‣ Zeroth-Order Optimization at the Edge of Stability"), 2. ‣ 4.2 Linear stability of zeroth-order methods ‣ 4 Linear stability analysis ‣ Zeroth-Order Optimization at the Edge of Stability") and 3. ‣ 4.2 Linear stability of zeroth-order methods ‣ 4 Linear stability analysis ‣ Zeroth-Order Optimization at the Edge of Stability") provide exact mean-square stability characterizations under the linearized dynamics. In the next section, we use the corresponding upper and lower bounds in equation 17. ‣ 4.2 Linear stability of zeroth-order methods ‣ 4 Linear stability analysis ‣ Zeroth-Order Optimization at the Edge of Stability"), equation 19. ‣ 4.2 Linear stability of zeroth-order methods ‣ 4 Linear stability analysis ‣ Zeroth-Order Optimization at the Edge of Stability"), and equation 21. ‣ 4.2 Linear stability of zeroth-order methods ‣ 4 Linear stability analysis ‣ Zeroth-Order Optimization at the Edge of Stability") to empirically test whether ZO methods operate near the mean-square edge of stability during neural network training.

Our main theory focuses on the Gaussian symmetric two-point estimator in equation 3, which is the standard estimator used in MeZO-style LLM fine-tuning. Appendix B shows that the same covariance-operator framework extends naturally to other estimator choices, including forward finite differences, non-Gaussian directions, and multi-query averages.

## Zeroth-order optimization operates at the mean-square edge of stability

Building on the mean-square linear stability theory in Section 4.2, we empirically show that full-batch ZO methods on neural networks operate at the *mean-square* edge of stability (EoS): the training dynamics stabilizes near the predicted mean-square linear stability boundary.

### Tracking mean-square stability during training

Let ${\mathbf{H}}_{t}:={{\nabla^{2}f}{({\mathbf{x}}_{t})}}$ denote the loss Hessian along the training trajectory. For each ZO optimizer, Section 4.2 provides explicit mean-square stability conditions under the linearized dynamics, together with computable lower and upper bounds on the corresponding stability threshold that depend only on the trace and top eigenvalue of the relevant curvature matrix. In large-scale neural network training, however, evaluating the exact mean-square stability condition is typically infeasible, since it requires the full spectrum of the Hessian (or the preconditioned Hessian for Adam-style methods). We therefore estimate only the trace and top eigenvalue during training, and use them to form tractable lower and upper bounds. Concretely, for the purpose of visualizing these dynamic conditions between ${\mathbf{H}}_{t}$ and the step size $\eta$, we present our results in the following format:

where the stability threshold depends on the step size $\eta$ and does not change over iterations and the upper and lower terms depend on the spectrum of ${\mathbf{H}}_{t}$ (e.g., Figure 2). We say the training operates near the mean-square EoS when the stability threshold remains within, or very close to, this interval for a sustained portion of training.

ZO-GD. From equation 17. ‣ 4.2 Linear stability of zeroth-order methods ‣ 4 Linear stability analysis ‣ Zeroth-Order Optimization at the Edge of Stability"), we track mean-square stability via

ZO-GDM. From equation 19. ‣ 4.2 Linear stability of zeroth-order methods ‣ 4 Linear stability analysis ‣ Zeroth-Order Optimization at the Edge of Stability"), we track mean-square stability via

ZO-Adam. For ZO-Adam, the bounds depend on the preconditioner ${\mathbf{P}}_{t}$ at iteration $t$. From equation 21. ‣ 4.2 Linear stability of zeroth-order methods ‣ 4 Linear stability analysis ‣ Zeroth-Order Optimization at the Edge of Stability") in Theorem 3. ‣ 4.2 Linear stability of zeroth-order methods ‣ 4 Linear stability analysis ‣ Zeroth-Order Optimization at the Edge of Stability"), we track mean-square stability via

### Experimental setup

We consider an image classification task on a subset of CIFAR-10 and train ZO methods using the squared loss. We evaluate three representative vision architectures: a CNN, a ResNet, and a Vision Transformer (ViT). Unless stated otherwise, we use full-batch training and a constant step size to match the linearized stability theory in Section 4.

Optimizers and hyperparameters. We study ZO-GD, ZO-GDM, and ZO-Adam, all using the standard two-point estimator with default smoothing parameter $\mu = 10^{- 3}$. During training, we log curvature statistics every $1,000$ iterations by estimating the top Hessian eigenvalue using power iteration and the Hessian trace using Hutchinson's estimator. Additional experimental details are provided in Appendix C.

### Main experiments

In Figure 2, we train ZO methods on the CNN and track the stability intervals in equation 23, equation 24, and equation 25. Across all three optimizers, we observe a consistent mean-square EoS pattern: after an initial phase of progressive sharpening, the tracked curvature terms adjust and stabilize so that the stability threshold remains within, or very close to, the corresponding intervals. As shown in Figure 6 and Figure 7, we observe the same behavior when training a ResNet and a ViT.

To test whether this behavior is specific to vision, we also train LSTM and Mamba sequence models on the synthetic sorting task described in Karpathy, following the experimental setup used by Cohen et al.. These experiments exhibit the same qualitative mean-square EoS behavior; full plots are provided in Appendix D.1.

Specifically, ($i$) for ZO-GD, the threshold $2/\eta$ remains close to the interval $\lbrack{{Tr}{({\mathbf{H}}_{t})}},{{{Tr}{({\mathbf{H}}_{t})}} + {2\lambda_{\max}{({\mathbf{H}}_{t})}}}\rbrack$ across step sizes; ($ii$) for ZO-GDM, the threshold ${2{({1 - \beta})}}/\eta$ remains close to $\lbrack{{Tr}{({\mathbf{H}}_{t})}},{{{Tr}{({\mathbf{H}}_{t})}} + {\frac{2}{1 + \beta}\lambda_{\max}{({\mathbf{H}}_{t})}}}\rbrack$ across momentum values; and ($iii$) for ZO-Adam, the threshold $2/\eta$ remains close to the corresponding preconditioned interval in equation 25. In all cases, the *trace* of the (preconditioned) Hessian provides the dominant stability signal throughout training.

### Additional experiments

Figure 3: Catapult dynamics in ZO-GD. We train ZO-GD on CNN and increase the step size midway through training (from η1 to η2 and then to η3). Top: the training loss exhibits a pronounced spike after each step size increase, consistent with catapult dynamics. Bottom: the Hessian trace Tr(Ht) drops sharply during the catapult phase and then rises again, re-equilibrating near the new stability threshold 2/η.

Catapult dynamics. In Figure 3, we train ZO-GD and increase the step size midway through training (from $\eta_{1}$ to $\eta_{2}$ and then to $\eta_{3}$). We observe a pronounced spike in the training loss after each increase, consistent with the *catapult* dynamics. Immediately after the step size increase, the new step size temporarily exceeds the mean-square stability critical step size at the current iterate, so the dynamics become locally unstable and the loss increases sharply. At the same time, the Hessian trace drops rapidly below the new threshold and then rises again, re-equilibrating near the new threshold.

Effect of the smoothing parameter $\mu$. In Figure 4, we train ZO-GD with fixed step size and vary the smoothing parameter $\mu$ in the two-point estimator. For moderate and small $\mu$, the tracked stability terms increase early in training and then stabilize near the threshold $2/\eta$, consistent with mean-square EoS behavior. For larger $\mu$, both ${Tr}{({\mathbf{H}}_{t})}$ and ${{Tr}{({\mathbf{H}}_{t})}} + {2\lambda_{\max}{({\mathbf{H}}_{t})}}$ saturate at substantially smaller values and remain far below $2/\eta$, indicating that training does not approach the predicted mean-square stability boundary. Overall, mean-square EoS persists across a broad range of practically relevant smoothing levels, while overly large smoothing suppresses curvature growth. We attribute this phenomenon to implicit bias in Section 6.

Beyond full-batch: mini-batch ZO-SGD. Although our main results focus on full-batch ZO methods, we include a preliminary mini-batch experiment in Figure 5. Compared to full-batch ZO-GD, mini-batch ZO-SGD converges to significantly flatter regimes.

Figure 4: Effect of the smoothing parameter μ. We train ZO-GD on a CNN with a fixed step size and vary the smoothing parameter μ in the two-point estimator. For moderate and small smoothing (μ ≤ 10−3), ZO-GD operates at the mean-square EoS. For larger smoothing (μ ≥ 3 × 10−3), ZO-GD no longer reaches the EoS threshold and instead trains in a lower-curvature regime with a smaller Hessian trace.

Figure 5: Effect of batch size in mini-batch ZO-SGD. We train mini-batch ZO-SGD on a CNN with a fixed step size and vary the batch size. Compared to full-batch ZO-GD, mini-batch ZO-SGD trains in a lower-curvature regime with a smaller Hessian trace.

Figure 6: Mean-square EoS for full-batch ZO methods on ResNet. We train full-batch ZO-GD, ZO-GDM, and ZO-Adam on for CIFAR-10 and track the corresponding mean-square stability bounds and threshold in Section 5.1.

Figure 7: Mean-square EoS for full-batch ZO methods on Vision Transformer. We train full-batch ZO-GD, ZO-GDM, and ZO-Adam on a Vision Transformer for CIFAR-10 and track the corresponding mean-square stability bounds and threshold in Section 5.1.

## Discussion

In this section, we discuss implications of our mean-square stability theory and empirical mean-square EoS results, and highlight several directions for future work.

Why mean-square stability is the relevant notion for ZO dynamics. In ZO optimization, randomness persists even in full-batch training due to random perturbation directions. As a result, stability cannot be assessed solely through the mean trajectory; ${\mathbb{E}}{\lbrack{\mathbf{x}}_{t}\rbrack}$ may remain bounded even when fluctuations grow and dominate the behavior of the iterates. Mean-square stability captures this effect by directly controlling the second moment ${\mathbb{E}}{\|{{\mathbf{x}}_{t} - {\mathbf{x}}^{\star}}\|}^{2}$, while remaining analyzable under the linearized dynamics and yielding explicit step size conditions. Other notions of stability are also meaningful, such as stability of higher moments or tail-probability bounds. Nevertheless, our experiments suggest that the curvature quantities appearing in the mean-square stability conditions closely track the stability behavior observed during ZO neural network training.

Curvature quantities that govern ZO stability. For FO methods under the linearized dynamics, stability depends only on the largest eigenvalue of the (preconditioned) Hessian. In contrast, our results show that mean-square stability of ZO methods depends on the full Hessian spectrum. This dependence appears explicitly in the exact stability conditions, and it is reflected in the computable bounds through both trace and top-eigenvalue terms. A practically important regime is when ${Tr}{({\mathbf{H}})}$ dominates $\lambda_{\max}{({\mathbf{H}})}$, in which case these bounds become tight and the trace term largely sets the stability scale. Empirically, this matches our empirical observations: the Hessian trace (or the preconditioned trace for ZO-Adam) closely tracks the relevant stability threshold throughout training, while $\lambda_{\max}{({\mathbf{H}}_{t})}$ can be less informative for ZO dynamics.

### Momentum reshapes ZO stability differently from FO stability

Momentum provides a concrete example showing that ZO stability is not a direct analogue of FO stability. For GD with momentum (GDM), the linearized stability threshold increases with $\beta$, corresponding to stable training at sharper curvature levels, with ${\lambda_{\max}{({\mathbf{H}}_{t})}} \approx {{2{({1 + \beta})}}/\eta}$ at the EoS. For ZO-GDM, our mean-square conditions imply the opposite dependence: increasing $\beta$ shrinks the stable regime and reduces the corresponding stability scale. Empirically, this is consistent with ZO-GDM operating in lower-curvature regimes as $\beta$ increases, with ${{Tr}{({\mathbf{H}}_{t})}} \approx {{2{({1 - \beta})}}/\eta}$ at the mean-square EoS.

Intuitively, in FO-GDM, momentum damps deterministic oscillations along sharp directions, which enlarges the stable step-size region. In ZO-GDM, by contrast, momentum accumulates not only the gradient signal but also the random-direction estimator noise. Since ZO stability is governed by second moments, this extra accumulated noise makes the dynamics less stable and causes increasing $\beta$ to shrink the stable region.

A similar contrast appears for adaptive methods. For (frozen) Adam, increasing $\beta_{1}$ increases the stability threshold, with ${\lambda_{\max}{({{\mathbf{P}}_{t}^{- 1}{\mathbf{H}}_{t}})}} \approx {{2{({1 + \beta_{1}})}}/{({{({1 - \beta_{1}})}\eta})}}$. For ZO-Adam, by comparison, our experiments suggest that ${{Tr}{({{\mathbf{P}}_{t}^{- 1}{\mathbf{H}}_{t}})}} \approx {2/\eta}$ at the mean-square EoS, which is independent of $\beta_{1}$ (see Figure 10 and Appendix D.2). Understanding how these effects translate into practical benefits (or tradeoffs) of momentum in ZO training is an interesting open question.

### Effect of the smoothing parameter $\mu$ and trace-related implicit bias

The two-point estimator introduces smoothing, controlled by $\mu$, that changes both the bias and the noise structure of the ZO update. Zhang et al. connect such ZO optimization to an implicit preference for small-trace regions, formalized as approximately minimizing

up to higher-order terms. Under this perspective, $\mu$ directly modulates a curvature-dependent bias in the effective objective, and large $\mu$ can prevent the dynamics from approaching the mean-square stability threshold predicted by the unsmoothed linearized model. A systematic theory that jointly captures ($i$) the mean-square stability constraint and ($ii$) the effect of smoothing bias on the effective landscape is an interesting direction for future work.

### Beyond full-batch: mini-batch ZO methods

Our analysis focuses on full-batch ZO dynamics, where the only randomness comes from the estimator directions. In practical settings, mini-batching introduces an additional noise source through stochastic sampling of data points. A complete stability theory for mini-batch ZO training would need to incorporate both estimator noise and sampling noise, and quantify how these two sources interact in the second-moment recursion. Recent work gives sharp mean-square stability thresholds for mini-batch SGD. Deriving analogous results for mini-batch ZO methods would clarify whether mean-square EoS persists under data subsampling, and which curvature quantities control stability in that regime.

## Conclusion

We developed a mean-square linear stability theory for zeroth-order (ZO) optimization methods based on the standard two-point estimator, including ZO-GD, ZO-GDM, and Adam-style preconditioned variants. We derived exact step size characterizations for mean-square stability via linearization, showing that ZO stability depends on the full spectrum of the (preconditioned) Hessian and admits computable bounds in terms of the trace and top eigenvalue.

Guided by these results, we empirically studied full-batch ZO training on standard neural network architectures (CNN, ResNet, and ViT) and found consistent evidence that ZO methods operate at the mean-square edge of stability: the curvature quantities governing the theoretical stability threshold adapt during training and stabilize near the predicted boundary. Across methods, the stability behavior is driven primarily by trace-based curvature terms, providing a concrete mechanism through which large step sizes implicitly regularize ZO training dynamics.

Our results position mean-square stability as a principled framework for analyzing and predicting ZO optimization behavior in deep learning. A natural next step is to use this mean-square EoS perspective to extend the central-flow framework of Cohen et al. to zeroth-order methods, and to empirically verify whether the resulting flow description captures ZO training dynamics across architectures and tasks. It is also important to extend the theory to mini-batch ZO methods. Another important direction is to understand how stability constraints interact with optimization efficiency and generalization in practice.
