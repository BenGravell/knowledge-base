<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Zeroth-Order Optimization at the Edge of Stability

Topics include Stability analysis, Neural networks, Deep learning, Optimization, Learning, Zeroth-order optimization, ZO, FO.

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Zeroth-order (ZO) methods are widely used when gradients are unavailable or prohibitively expensive, including black-box learning and memory-efficient fine-tuning of large models, yet their optimization dynamics in deep learning remain underexplored. In this work, we provide an explicit step size condition that exactly captures the (mean-square) linear stability of a family of ZO methods based on the standard two-point estimator. Our characterization reveals a sharp contrast with first-order (FO) methods: whereas FO stability is governed solely by the largest Hessian eigenvalue, mean-square stability of ZO methods depends on the entire Hessian spectrum. Since computing the full Hessian spectrum is infeasible in practical neural network training, we further derive tractable stability bounds that depend only on the largest eigenvalue and the Hessian trace. Empirically, we find that full-batch ZO methods operate at the edge of stability: ZO-GD, ZO-GDM, and ZO-Adam consistently stabilize near the predicted stability boundary across a range of deep learning training problems.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Our results highlight an implicit regularization effect specific to ZO methods, where large step sizes primarily regularize the Hessian trace, whereas in FO methods they regularize the top eigenvalue.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

Zeroth-order (ZO) optimization methods, which rely only on function evaluations, are widely used when gradients are unavailable, unreliable, or expensive to compute. Such a setting arises in black-box learning, derivative-free control, and increasingly in modern large-model pipelines, where memory and systems constraints can make backpropagation costly. Recent work shows that ZO methods based on two-point function evaluations can fine-tune large language models (LLMs) with competitive accuracy while substantially reducing memory usage and compute overhead. Despite their growing practical relevance, the training dynamics of ZO methods in deep learning remain far less understood than those of first-order (FO) optimizers.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

For FO optimization in deep learning, one prominent empirical phenomenon is the *edge of stability* (EoS). In full-batch gradient descent (GD) with step size $\eta$ on a quadratic objective $f_{\mathrm{quad}}({\bm{x}})=\tfrac{1}{2}{\bm{x}}^{\top}{\bm{H}}{\bm{x}}$, the iterates diverge when $\eta>2/\lambda_{\max}({\bm{H}})$. In neural network training, however, optimization often remains well-behaved even at step sizes beyond this local quadratic threshold. Along the training trajectory $\{{\bm{x}}_{t}\}$, the top eigenvalue of the Hessian $\lambda_{\max}({\bm{H}}_{t})$ increases early in training and then stabilizes near the threshold $2/\eta$ over long horizons.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

This phenomenon has motivated a growing line of work aimed at understanding its mechanism and its connections to stability, curvature, and implicit regularization in deep learning optimization dynamics.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

In this work, we ask whether a similar phenomenon arises in *zeroth-order* training. At first glance, this is far from obvious: ZO methods update parameters by drawing random search directions at every iteration, and their stability cannot be understood through the deterministic arguments typically used to explain FO dynamics and stability.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Introduction", "weight": 1.5} -->

As a preliminary experiment, Figure 1 compares full-batch (first-order) GD and zeroth-order gradient descent (ZO-GD) with varying step sizes $\eta$. For GD, the top Hessian eigenvalue $\lambda_{\max}({\bm{H}}_{t})$ stabilizes near $2/\eta$, consistent with the behavior predicted by standard EoS theory. For ZO-GD, however, $\lambda_{\max}({\bm{H}}_{t})$ does not exhibit the same trend; instead, perhaps surprisingly, the Hessian trace $\operatorname{Tr}({\bm{H}}_{t})$ stabilizes slightly below $2/\eta$. This suggests that ZO training may be governed by a different stability mechanism than FO training, and that ZO methods may exhibit their own EoS phenomenon in deep learning.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Introduction", "weight": 1.5} -->

These observations motivate the following fundamental questions: ($i$) *do ZO methods operate at the edge of stability in neural network training*, and ($ii$) if so, *which curvature-related quantity governs their stability*?

<!-- chunk {"id": "body-0010", "role": "body", "section": "Introduction", "weight": 1.5} -->

We introduce a mean-square linear stability theory for ZO methods to investigate these questions. In Section 4, we provide an exact step size characterization of mean-square linear stability under the linearized dynamics for a family of ZO optimizers, including ZO-GD and its momentum and preconditioned variants. Unlike FO methods, whose stability is governed solely by the largest Hessian eigenvalue, mean-square stability of ZO methods depends on the entire Hessian spectrum. Moreover, momentum affects stability in opposite ways: increasing $\beta$ enlarges the stable regime for GD with momentum (GDM), but shrinks it for ZO-GD with momentum (ZO-GDM). Since computing the full spectrum is typically infeasible, we also derive tractable bounds that depend only on the Hessian trace and the largest eigenvalue (summarized in Table 1).

<!-- chunk {"id": "body-0011", "role": "body", "section": "Introduction", "weight": 1.5} -->

Technically, our analysis introduces a cone-preserving linear covariance operator with a rank-one global coupling term to capture the dynamics of the ZO second-moment recursion. This reduction allows one to characterize its spectral radius using the Krein--Rutman Theorem and derive the explicit mean-square stability conditions.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Introduction", "weight": 1.5} -->

In Section 5, we empirically find that full-batch ZO methods operate at the *mean-square* edge of stability across architectures and tasks: ZO methods (ZO-GD, ZO-GDM, and ZO-Adam) consistently stabilize near the predicted mean-square stability boundary. Notably, this behavior is governed primarily by trace-based curvature quantities, providing new insight into how large step sizes implicitly bias ZO training toward solutions with small (preconditioned) Hessian trace.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Linear stability analysis", "weight": 1.0} -->

Directly analyzing the full dynamics of optimizers in deep learning is typically intractable. Instead, we adopt the standard dynamical systems approach of studying stability near a local minimizer via the *linearized dynamics*. Exponential stability of the linearized dynamics implies local stability of the corresponding nonlinear dynamics near the equilibrium, which justifies linear stability analysis as a principled tool.

<!-- chunk {"id": "body-0014", "role": "body", "section": "Linear stability of first-order methods", "weight": 1.0} -->

The first-order (FO) counterparts of the ZO optimizers in Section 3, namely GD, GDM, and Frozen Adam, are deterministic, so their mean and mean-square linear stability conditions coincide. A key takeaway is that FO linear stability is governed solely by the top eigenvalue of the (preconditioned) Hessian, as summarized below.

<!-- chunk {"id": "body-0015", "role": "body", "section": "Linear stability of zeroth-order methods", "weight": 1.0} -->

The inherent stochasticity in ZO updates fundamentally changes the linear stability as shown in Figure 1. However, the *mean* dynamics of a ZO method matches that of its FO counterpart, and $\eta^{\star}_{\mathrm{mean}}$ coincides with the FO critical step size presented in Section 4.1. This is due to the fact that under the quadratic model $f_{\mathrm{quad}}$ in Definition 1. ‣ 4 Linear stability analysis ‣ Zeroth-Order Optimization at the Edge of Stability"), the two-point estimator is *unbiased*: $\mathbb{E}\big[\widehat{\nabla}f_{\mathrm{quad}}({\bm{x}}_{t})\big]=\nabla f_{\mathrm{quad}}({\bm{x}}_{t})$. The intricacy of ZO linear stability is only captured by the *mean-square* stability.

<!-- chunk {"id": "body-0016", "role": "body", "section": "Linear stability of zeroth-order methods", "weight": 1.0} -->

In particular, we show that $\eta^{\star}_{\mathrm{ms}}$ for ZO-GD, ZO-GDM, and Frozen ZO-Adam, depends on the entire eigen spectrum of the (preconditioned) Hessian and is dominated by its trace value.

<!-- chunk {"id": "body-0017", "role": "body", "section": "Remark 1 (Computing $\\eta^{\\star}_{\\mathrm{ms}}$)", "weight": 1.0} -->

If the full spectrum $\{\lambda_{i}\}_{i=1}^{d}$ were available, $\eta^{\star}_{\mathrm{ms}}$ in Theorem 1. ‣ 4.2 Linear stability of zeroth-order methods ‣ 4 Linear stability analysis ‣ Zeroth-Order Optimization at the Edge of Stability") can be computed by solving $\sum_{i=1}^{d}({\eta\lambda_{i}}/{2(1-\eta\lambda_{i})})=1$ over $\eta\in(0,1/\lambda_{\max}({\bm{H}}))$. In practice, we instead track the bounds equation 17.

<!-- chunk {"id": "body-0018", "role": "body", "section": "Remark 1 (Computing $\\eta^{\\star}_{\\mathrm{ms}}$)", "weight": 1.0} -->

‣ 4.2 Linear stability of zeroth-order methods ‣ 4 Linear stability analysis ‣ Zeroth-Order Optimization at the Edge of Stability"), which depend only on $\operatorname{Tr}({\bm{H}})$ and $\lambda_{\max}({\bm{H}})$ and can be estimated efficiently during training, which is critical for large models.

<!-- chunk {"id": "body-0019", "role": "body", "section": "Remark 2 (Commutativity assumption)", "weight": 1.0} -->

The condition ${\bm{P}}{\bm{H}}={\bm{H}}{\bm{P}}$ ensures that ${\bm{P}}^{-1}{\bm{H}}$ is diagonalizable in the same eigenbasis as ${\bm{H}}$, which allows the mean-square dynamics to decouple across eigendirections and enables a tractable spectral analysis. Without commutativity, the second-moment recursion generally couples different eigenspaces, and obtaining an explicit stability characterization becomes substantially less tractable.

<!-- chunk {"id": "body-0020", "role": "body", "section": "Remark 2 (Commutativity assumption)", "weight": 1.0} -->

Taken together, Theorems 1. ‣ 4.2 Linear stability of zeroth-order methods ‣ 4 Linear stability analysis ‣ Zeroth-Order Optimization at the Edge of Stability"), 2. ‣ 4.2 Linear stability of zeroth-order methods ‣ 4 Linear stability analysis ‣ Zeroth-Order Optimization at the Edge of Stability") and 3. ‣ 4.2 Linear stability of zeroth-order methods ‣ 4 Linear stability analysis ‣ Zeroth-Order Optimization at the Edge of Stability") provide exact mean-square stability characterizations under the linearized dynamics. In the next section, we use the corresponding upper and lower bounds in equation 17. ‣ 4.2 Linear stability of zeroth-order methods ‣ 4 Linear stability analysis ‣ Zeroth-Order Optimization at the Edge of Stability"), equation 19. ‣ 4.2 Linear stability of zeroth-order methods ‣ 4 Linear stability analysis ‣ Zeroth-Order Optimization at the Edge of Stability"), and equation 21.

<!-- chunk {"id": "body-0021", "role": "body", "section": "Remark 2 (Commutativity assumption)", "weight": 1.0} -->

‣ 4.2 Linear stability of zeroth-order methods ‣ 4 Linear stability analysis ‣ Zeroth-Order Optimization at the Edge of Stability") to empirically test whether ZO methods operate near the mean-square edge of stability during neural network training.

<!-- chunk {"id": "body-0022", "role": "body", "section": "Remark 2 (Commutativity assumption)", "weight": 1.0} -->

Our main theory focuses on the Gaussian symmetric two-point estimator in equation 3, which is the standard estimator used in MeZO-style LLM fine-tuning. Appendix B shows that the same covariance-operator framework extends naturally to other estimator choices, including forward finite differences, non-Gaussian directions, and multi-query averages.

<!-- chunk {"id": "body-0023", "role": "body", "section": "Zeroth-order optimization operates at the mean-square edge of stability", "weight": 1.0} -->

Building on the mean-square linear stability theory in Section 4.2, we empirically show that full-batch ZO methods on neural networks operate at the *mean-square* edge of stability (EoS): the training dynamics stabilizes near the predicted mean-square linear stability boundary.

<!-- chunk {"id": "body-0024", "role": "body", "section": "Tracking mean-square stability during training", "weight": 1.0} -->

Let ${\bm{H}}_{t}:=\nabla^{2}f({\bm{x}}_{t})$ denote the loss Hessian along the training trajectory. For each ZO optimizer, Section 4.2 provides explicit mean-square stability conditions under the linearized dynamics, together with computable lower and upper bounds on the corresponding stability threshold that depend only on the trace and top eigenvalue of the relevant curvature matrix. In large-scale neural network training, however, evaluating the exact mean-square stability condition is typically infeasible, since it requires the full spectrum of the Hessian (or the preconditioned Hessian for Adam-style methods). We therefore estimate only the trace and top eigenvalue during training, and use them to form tractable lower and upper bounds.

<!-- chunk {"id": "body-0025", "role": "body", "section": "Tracking mean-square stability during training", "weight": 1.0} -->

Concretely, for the purpose of visualizing these dynamic conditions between ${\bm{H}}_{t}$ and the step size $\eta$, we present our results in the following format: where the stability threshold depends on the step size $\eta$ and does not change over iterations and the upper and lower terms depend on the spectrum of ${\bm{H}}_{t}$ (e.g., Figure 2). We say the training operates near the mean-square EoS when the stability threshold remains within, or very close to, this interval for a sustained portion of training.

<!-- chunk {"id": "body-0026", "role": "body", "section": "Tracking mean-square stability during training", "weight": 1.0} -->

ZO-GD. From equation 17. ‣ 4.2 Linear stability of zeroth-order methods ‣ 4 Linear stability analysis ‣ Zeroth-Order Optimization at the Edge of Stability"), we track mean-square stability via ZO-GDM. From equation 19. ‣ 4.2 Linear stability of zeroth-order methods ‣ 4 Linear stability analysis ‣ Zeroth-Order Optimization at the Edge of Stability"), we track mean-square stability via ZO-Adam. For ZO-Adam, the bounds depend on the preconditioner ${\bm{P}}_{t}$ at iteration $t$. From equation 21. ‣ 4.2 Linear stability of zeroth-order methods ‣ 4 Linear stability analysis ‣ Zeroth-Order Optimization at the Edge of Stability") in Theorem 3. ‣ 4.2 Linear stability of zeroth-order methods ‣ 4 Linear stability analysis ‣ Zeroth-Order Optimization at the Edge of Stability"), we track mean-square stability via

<!-- chunk {"id": "body-0027", "role": "body", "section": "Experimental setup", "weight": 1.0} -->

We consider an image classification task on a subset of CIFAR-10 and train ZO methods using the squared loss. We evaluate three representative vision architectures: a CNN, a ResNet, and a Vision Transformer (ViT). Unless stated otherwise, we use full-batch training and a constant step size to match the linearized stability theory in Section 4.

<!-- chunk {"id": "body-0028", "role": "body", "section": "Experimental setup", "weight": 1.0} -->

Optimizers and hyperparameters. We study ZO-GD, ZO-GDM, and ZO-Adam, all using the standard two-point estimator with default smoothing parameter $\mu=10^{-3}$. During training, we log curvature statistics every $1{,}000$ iterations by estimating the top Hessian eigenvalue using power iteration and the Hessian trace using Hutchinson's estimator. Additional experimental details are provided in Appendix C.

<!-- chunk {"id": "body-0029", "role": "body", "section": "Main experiments", "weight": 1.0} -->

In Figure 2, we train ZO methods on the CNN and track the stability intervals in equation 23, equation 24, and equation 25. Across all three optimizers, we observe a consistent mean-square EoS pattern: after an initial phase of progressive sharpening, the tracked curvature terms adjust and stabilize so that the stability threshold remains within, or very close to, the corresponding intervals. As shown in Figure 6 and Figure 7, we observe the same behavior when training a ResNet and a ViT.

<!-- chunk {"id": "body-0030", "role": "body", "section": "Main experiments", "weight": 1.0} -->

To test whether this behavior is specific to vision, we also train LSTM and Mamba sequence models on the synthetic sorting task described in Karpathy, following the experimental setup used by Cohen et al.. These experiments exhibit the same qualitative mean-square EoS behavior; full plots are provided in Appendix D.1.

<!-- chunk {"id": "body-0031", "role": "body", "section": "Main experiments", "weight": 1.0} -->

Specifically, ($i$) for ZO-GD, the threshold $2/\eta$ remains close to the interval $[\operatorname{Tr}({\bm{H}}_{t}),\,\operatorname{Tr}({\bm{H}}_{t})+2\lambda_{\max}({\bm{H}}_{t})]$ across step sizes; ($ii$) for ZO-GDM, the threshold $2(1-\beta)/\eta$ remains close to $[\operatorname{Tr}({\bm{H}}_{t}),\,\operatorname{Tr}({\bm{H}}_{t})+\frac{2}{1+\beta}\lambda_{\max}({\bm{H}}_{t})]$ across momentum values; and ($iii$) for ZO-Adam, the threshold $2/\eta$ remains close to the corresponding preconditioned interval in equation 25. In all cases, the

<!-- chunk {"id": "body-0032", "role": "body", "section": "Main experiments", "weight": 1.0} -->

*trace* of the (preconditioned) Hessian provides the dominant stability signal throughout training.

<!-- chunk {"id": "body-0033", "role": "body", "section": "Additional experiments", "weight": 1.0} -->

Catapult dynamics. In Figure 3, we train ZO-GD and increase the step size midway through training (from $\eta_{1}$ to $\eta_{2}$ and then to $\eta_{3}$). We observe a pronounced spike in the training loss after each increase, consistent with the *catapult* dynamics. Immediately after the step size increase, the new step size temporarily exceeds the mean-square stability critical step size at the current iterate, so the dynamics become locally unstable and the loss increases sharply. At the same time, the Hessian trace drops rapidly below the new threshold and then rises again, re-equilibrating near the new threshold.

<!-- chunk {"id": "body-0034", "role": "body", "section": "Additional experiments", "weight": 1.0} -->

Effect of the smoothing parameter $\mu$. In Figure 4, we train ZO-GD with fixed step size and vary the smoothing parameter $\mu$ in the two-point estimator. For moderate and small $\mu$, the tracked stability terms increase early in training and then stabilize near the threshold $2/\eta$, consistent with mean-square EoS behavior. For larger $\mu$, both $\operatorname{Tr}({\bm{H}}_{t})$ and $\operatorname{Tr}({\bm{H}}_{t})+2\lambda_{\max}({\bm{H}}_{t})$ saturate at substantially smaller values and remain far below $2/\eta$, indicating that training does not approach the predicted mean-square stability boundary. Overall, mean-square EoS persists across a broad range of practically relevant smoothing levels, while overly large smoothing suppresses curvature growth. We attribute this phenomenon to implicit bias in Section 6.

<!-- chunk {"id": "body-0035", "role": "body", "section": "Additional experiments", "weight": 1.0} -->

Beyond full-batch: mini-batch ZO-SGD. Although our main results focus on full-batch ZO methods, we include a preliminary mini-batch experiment in Figure 5. Compared to full-batch ZO-GD, mini-batch ZO-SGD converges to significantly flatter regimes.

<!-- chunk {"id": "body-0036", "role": "body", "section": "Discussion", "weight": 1.5} -->

In this section, we discuss implications of our mean-square stability theory and empirical mean-square EoS results, and highlight several directions for future work.

<!-- chunk {"id": "body-0037", "role": "body", "section": "Discussion", "weight": 1.5} -->

Why mean-square stability is the relevant notion for ZO dynamics. In ZO optimization, randomness persists even in full-batch training due to random perturbation directions. As a result, stability cannot be assessed solely through the mean trajectory; $\mathbb{E}[{\bm{x}}_{t}]$ may remain bounded even when fluctuations grow and dominate the behavior of the iterates. Mean-square stability captures this effect by directly controlling the second moment $\mathbb{E}\|{\bm{x}}_{t}-{\bm{x}}^{\star}\|^{2}$, while remaining analyzable under the linearized dynamics and yielding explicit step size conditions. Other notions of stability are also meaningful, such as stability of higher moments or tail-probability bounds. Nevertheless, our experiments suggest that the curvature quantities appearing in the mean-square stability conditions closely track the stability behavior observed during ZO neural network training.

<!-- chunk {"id": "body-0038", "role": "body", "section": "Discussion", "weight": 1.5} -->

Curvature quantities that govern ZO stability. For FO methods under the linearized dynamics, stability depends only on the largest eigenvalue of the (preconditioned) Hessian. In contrast, our results show that mean-square stability of ZO methods depends on the full Hessian spectrum. This dependence appears explicitly in the exact stability conditions, and it is reflected in the computable bounds through both trace and top-eigenvalue terms. A practically important regime is when $\operatorname{Tr}({\bm{H}})$ dominates $\lambda_{\max}({\bm{H}})$, in which case these bounds become tight and the trace term largely sets the stability scale. Empirically, this matches our empirical observations: the Hessian trace (or the preconditioned trace for ZO-Adam) closely tracks the relevant stability threshold throughout training, while $\lambda_{\max}({\bm{H}}_{t})$ can be less informative for ZO dynamics.

<!-- chunk {"id": "body-0039", "role": "body", "section": "Momentum reshapes ZO stability differently from FO stability", "weight": 1.0} -->

Momentum provides a concrete example showing that ZO stability is not a direct analogue of FO stability. For GD with momentum (GDM), the linearized stability threshold increases with $\beta$, corresponding to stable training at sharper curvature levels, with $\lambda_{\max}({\bm{H}}_{t})\approx 2(1+\beta)/\eta$ at the EoS. For ZO-GDM, our mean-square conditions imply the opposite dependence: increasing $\beta$ shrinks the stable regime and reduces the corresponding stability scale. Empirically, this is consistent with ZO-GDM operating in lower-curvature regimes as $\beta$ increases, with $\operatorname{Tr}({\bm{H}}_{t})\approx 2(1-\beta)/\eta$ at the mean-square EoS.

<!-- chunk {"id": "body-0040", "role": "body", "section": "Momentum reshapes ZO stability differently from FO stability", "weight": 1.0} -->

Intuitively, in FO-GDM, momentum damps deterministic oscillations along sharp directions, which enlarges the stable step-size region. In ZO-GDM, by contrast, momentum accumulates not only the gradient signal but also the random-direction estimator noise. Since ZO stability is governed by second moments, this extra accumulated noise makes the dynamics less stable and causes increasing $\beta$ to shrink the stable region.

<!-- chunk {"id": "body-0041", "role": "body", "section": "Momentum reshapes ZO stability differently from FO stability", "weight": 1.0} -->

A similar contrast appears for adaptive methods. For (frozen) Adam, increasing $\beta_{1}$ increases the stability threshold, with $\lambda_{\max}({\bm{P}}_{t}^{-1}{\bm{H}}_{t})\approx 2(1+\beta_{1})/((1-\beta_{1})\eta)$. For ZO-Adam, by comparison, our experiments suggest that $\operatorname{Tr}({\bm{P}}_{t}^{-1}{\bm{H}}_{t})\approx 2/\eta$ at the mean-square EoS, which is independent of $\beta_{1}$ (see Figure 10 and Appendix D.2). Understanding how these effects translate into practical benefits (or tradeoffs) of momentum in ZO training is an interesting open question.

<!-- chunk {"id": "body-0042", "role": "body", "section": "Effect of the smoothing parameter $\\mu$ and trace-related implicit bias", "weight": 1.0} -->

The two-point estimator introduces smoothing, controlled by $\mu$, that changes both the bias and the noise structure of the ZO update. Zhang et al. connect such ZO optimization to an implicit preference for small-trace regions, formalized as approximately minimizing up to higher-order terms. Under this perspective, $\mu$ directly modulates a curvature-dependent bias in the effective objective, and large $\mu$ can prevent the dynamics from approaching the mean-square stability threshold predicted by the unsmoothed linearized model. A systematic theory that jointly captures ($i$) the mean-square stability constraint and ($ii$) the effect of smoothing bias on the effective landscape is an interesting direction for future work.

<!-- chunk {"id": "body-0043", "role": "body", "section": "Beyond full-batch: mini-batch ZO methods", "weight": 1.0} -->

Our analysis focuses on full-batch ZO dynamics, where the only randomness comes from the estimator directions. In practical settings, mini-batching introduces an additional noise source through stochastic sampling of data points. A complete stability theory for mini-batch ZO training would need to incorporate both estimator noise and sampling noise, and quantify how these two sources interact in the second-moment recursion. Recent work gives sharp mean-square stability thresholds for mini-batch SGD. Deriving analogous results for mini-batch ZO methods would clarify whether mean-square EoS persists under data subsampling, and which curvature quantities control stability in that regime.

<!-- chunk {"id": "body-0044", "role": "body", "section": "Conclusion", "weight": 1.5} -->

We developed a mean-square linear stability theory for zeroth-order (ZO) optimization methods based on the standard two-point estimator, including ZO-GD, ZO-GDM, and Adam-style preconditioned variants. We derived exact step size characterizations for mean-square stability via linearization, showing that ZO stability depends on the full spectrum of the (preconditioned) Hessian and admits computable bounds in terms of the trace and top eigenvalue.

<!-- chunk {"id": "body-0045", "role": "body", "section": "Conclusion", "weight": 1.5} -->

Guided by these results, we empirically studied full-batch ZO training on standard neural network architectures (CNN, ResNet, and ViT) and found consistent evidence that ZO methods operate at the mean-square edge of stability: the curvature quantities governing the theoretical stability threshold adapt during training and stabilize near the predicted boundary. Across methods, the stability behavior is driven primarily by trace-based curvature terms, providing a concrete mechanism through which large step sizes implicitly regularize ZO training dynamics.

<!-- chunk {"id": "body-0046", "role": "body", "section": "Conclusion", "weight": 1.5} -->

Our results position mean-square stability as a principled framework for analyzing and predicting ZO optimization behavior in deep learning. A natural next step is to use this mean-square EoS perspective to extend the central-flow framework of Cohen et al. to zeroth-order methods, and to empirically verify whether the resulting flow description captures ZO training dynamics across architectures and tasks. It is also important to extend the theory to mini-batch ZO methods. Another important direction is to understand how stability constraints interact with optimization efficiency and generalization in practice.
