<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Is Your Conditional Diffusion Model Actually Denoising?

Topics include Diffusion models, Control, Sampling.

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

We study the inductive biases of diffusion models with a conditioning-variable, which have seen widespread application as both text-conditioned generative image models and observation-conditioned continuous control policies. We observe that when these models are queried conditionally, their generations consistently deviate from the idealized "denoising" process upon which diffusion models are formulated, inducing disagreement between popular sampling algorithms (e.g. DDPM, DDIM). We introduce Schedule Deviation, a rigorous measure which captures the rate of deviation from a standard denoising process, and provide a methodology to compute it. Crucially, we demonstrate that the deviation from an idealized denoising process occurs irrespective of the model capacity or amount of training data. We posit that this phenomenon occurs due to the difficulty of bridging distinct denoising flows across different parts of the conditioning space and show theoretically how such a phenomenon can arise through an inductive bias towards smoothness.

<!-- chunk {"id": "body-0003", "role": "body", "section": "Introduction", "weight": 1.5} -->

Diffusion models (DMs) have seen widespread adoption in domains as diverse as robotic control, molecule design, and image generation from text prompts. The diffusion formalism is popular both because it enables stable training of neural generative models, via the denoising training objective, and because it offers a broad menu of mathematical and algorithmic techniques for *inference*. For example, inference can be conducted via both Stochastic Differential Equation (SDE) and Ordinary Differential Equation (ODE) formalisms, the latter of which can be distilled further for accelerated sampling. The design of these inference strategies hinges on the following fact: for a given (forward) diffusion process, there are many distinct "reverse" stochastic processes, each of which can produce the same marginal distribution over generated samples. Hence, from a sampling perspective, the various stochastic processes are in effect equivalent.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

A trained diffusion model is only an imperfect neural approximation to the idealized reverse processes. Nevertheless, we might hope that this approximation is not too inaccurate. For example, even if a diffusion model does not perfectly capture the target training distribution, one might conjecture that the denoising training objective ensures that the model is at least consistent, in some appropriate sense, with the forward processes mapping its own generated samples to noise. At the very least, one would hope that as a diffusion model is trained on more data, or is conditioned on contexts that are well-represented in a training dataset, a learned diffusion model will converge towards its mathematical idealization.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Contributions", "weight": 1.0} -->

In this work, we initiate the study of the inductive biases of conditional diffusional models: diffusion models whose generations depend on some context $z$. For example, the context could represent text descriptions of an image, observational inputs to a robotic control policy, or molecular properties of a protein binding target. We investigate the extent to which the path probabilities, ($p_{s}$, Definition˜2.1. ‣ 2 Preliminaries ‣ Is Your Conditional Diffusion Model Actually Denoising?")) deviate from those of an idealized diffusion path ($p^{\textsc{imcf}}_{s}$, Definition˜2.4. ‣ Model-Consistent Diffusion Flows ‣ 2 Preliminaries ‣ Is Your Conditional Diffusion Model Actually Denoising?")) with the same initial and terminal distribution as our learned model (note: not necessarily the ground truth data distribution). To facility this study, we introduce a novel, rigorous metric, Schedule Deviation, that is designed to precisely measure the extent to which a flow field induces non-denoising behavior in intermediate marginal densities.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Contributions", "weight": 1.0} -->

> Conditional diffusion models routinely and consistently deviate from the idealized model-consistent diffusion probability path, $p^{\textsc{imcf}}$. This effect is a direct byproduct of the inductive bias of conditional diffusion, and is strongly correlated with the discrepancy between popular diffusion samplers which, mathematically, should be equivalent in the limit of small discretization error.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Contributions", "weight": 1.0} -->

In more detail, our contributions are as follows: We introduce Schedule Deviation (SD), our new metric which quantifies the extent to which a diffusion model (conditional or otherwise) deviates from the idealized diffusion probability path (Definition˜3.1. ‣ 3.1 Measuring Schedule Deviation ‣ 3 Conditional Diffusion is Not Denoising. ‣ Is Your Conditional Diffusion Model Actually Denoising?")). We show that (SD) is closely related to the average total variation distance between path measures (Theorem˜1), and that SD can be efficiently evaluated as a consequence of the transport equation (Proposition˜3.1). Moreover, unlike most prior metrics used to study non-denoising behavior, SD does not require access to the true score function or training data, and can be evaluated with access to only the (potentially conditional) flow-based model.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Contributions", "weight": 1.0} -->

Using Schedule Deviation, we show that the probability path of conditional diffusion models consistently and routinely deviates from the idealized path (Figure˜3, Figure˜4). Our findings are consistent across toy examples, conditional image generation, and trajectory planning. Furthermore, we show that SD is often predictive of the Earth Mover Distance (EMD) between the samples generated by popular inference algorithms.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Contributions", "weight": 1.0} -->

We demonstrate the Schedule Deviation cannot be significantly ameliorated by increased model capacity or training data, and even varies significantly between different classes which are equally represented in the training data (Figure˜5). Rather, we posit that SD in conditional settings arises as a natural inductive bias of conditional diffusion when interpolating between multimodal distributions.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Contributions", "weight": 1.0} -->

We provide a theoretical model (Section˜4, Theorem˜2. ‣ 4 Explaining Schedule Deviation via Smoothness and Self-Guidance ‣ Is Your Conditional Diffusion Model Actually Denoising?") and 3) of Schedule Deviation that shows the deviation can be attributed to an inductive bias of conditional diffusion involving *smoothing* with respect to the conditioning variable. We prove that, under appropriate conditions, conditional diffusion engages in "self-guidance," combining scores from nearby points in the training data set and demonstrate that this causes deviation from the idealized denoising process.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Model-Consistent Diffusion Flows", "weight": 1.0} -->

Under appropriate regularity conditions, all diffusion probability paths can be realized by an infinite family of conditional normalization flows ($v,p)$. We focus on one such path, the *model-consistent diffusion flow*, which corresponds to the solution of the DDPM objective. We use $\hat{v}$ and $\hat{p}$ throughout the rest of this paper to emphasize conditional normalizing flows which may be associated with a learned model, rather than the true data-generating distribution, i.e. where $\hat{p}_{0}\neq p^{\star}$.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Remark 2.1 (Ideal Model-Consistent Flow vs Ground Truth Flow)", "weight": 1.0} -->

We use $\hat{p}$ instead of $p$ in Definition˜2.4. ‣ Model-Consistent Diffusion Flows ‣ 2 Preliminaries ‣ Is Your Conditional Diffusion Model Actually Denoising?") from here on to emphasize that $\hat{p}_{0}\neq p^{\star}$, meaning that $v^{\textsc{imcf}}$ is the ideal flow associated with the distribution of *learned model* $\hat{v}$ under a given sampling algorithm; not necessarily the "true" flow $v^{\star}$. Hence, schedule deviation is potentially orthogonal as a metric to whether $p_{0}$ matches $p^{\star}$. However, we note that, by the construction of $v^{\textsc{imcf}}$, $\hat{p}_{0}=p^{\textsc{imcf}}_{0}$ and $\hat{p}_{1}=p^{\textsc{imcf}}_{1}$.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Conditional Diffusion is Not Denoising", "weight": 1.0} -->

This section introduces our first main finding: the probability paths in diffusion consistently deviate from the idealized model-consistent probability path $p^{\textsc{imcf}}$, often in regions with *high data density*, and in a manner that *does not abate with increased number of training examples.* Figure 3: For t-SNE-conditional MNIST generation, we evaluate the Schedule Deviation and empirical 1-Wassertstein Distance between DDPM/DDIM samples, ablated over the training dataset size N ∈ {10000, 30000, 60000}. We note strong structural similarity between the two metrics that appears related to the contours of the conditioning distribution and the conditional data distributions.

<!-- chunk {"id": "body-0014", "role": "body", "section": "Measuring Schedule Deviation", "weight": 1.0} -->

To quantify this effect, we start by introducing Schedule Deviation, a novel, natural metric which evaluates the extent to the flow field $v$ induces instantaneous deviations from the idealized probability path $p^{\textsc{imcf}}$ associated with $v^{\textsc{imcf}}=\textrm{IMCF}(\hat{p}_{0})$. Crucially, Schedule Deviation analyzes the behavior of the learned model $\hat{v}$ on $p^{\textsc{imcf}}$, that is, the forward process associated with the distribution $\hat{p}_{0}$ generated by the model and not the reverse process $\hat{p}_{t}$ itself (as in Daras et al. ).

<!-- chunk {"id": "body-0015", "role": "body", "section": "Remark 3.1 (Schedule Deviation v.s. Generation Fidelity)", "weight": 1.0} -->

Note that $p_{0}\neq p^{\star}$, so $v^{\textsc{imcf}}$ is the IMCF associated with the distribution of *learned model* under a given sampler; not necessarily the IMCF associated with the true data distribution $p^{\star}$. Hence, schedule deviation is potentially orthogonal as a metric to whether $p_{0}$ matches $p^{\star}$. Moreover, we note that $p_{0}=p^{\textsc{imcf}}_{0}$ and $p_{1}=p^{\textsc{imcf}}_{1}$, so that schedule deviation principally captures deviations from the reference process in the "middle\" of the denoising.

<!-- chunk {"id": "body-0016", "role": "body", "section": "Remark 3.2", "weight": 1.0} -->

It should be noted that Schedule Deviation is distinct from consistency distillation. Consistency distillation enforces a related condition: that a few-step model is consistent with the integrated flow map of the ODE induced by the flow-field $v$, whereas Schedule Deviation measures the deviation of the flow map from the denoising probability path.

<!-- chunk {"id": "body-0017", "role": "body", "section": "Schedule Deviation is Widely Prevalent", "weight": 1.0} -->

We evaluate the schedule deviation of trained neural networks in two distinct settings and 3 datasets, as described below. We use a U-Net architecture similar to Dhariwal and Nichol for all experiments. For full experiment details, see Appendix˜C.

<!-- chunk {"id": "body-0018", "role": "body", "section": "Schedule Deviation is Widely Prevalent", "weight": 1.0} -->

Setting 1 (Conditional Image Generation). We evaluate the schedule-deviation of conditional image diffusion models. For ease of visualization and in order to keep the associated dimensionality of $x$ low (as Definition˜3.1. ‣ 3.1 Measuring Schedule Deviation ‣ 3 Conditional Diffusion is Not Denoising. ‣ Is Your Conditional Diffusion Model Actually Denoising?") requires computing the divergence w.r.t. $x$), we consider the MNIST and Fashion-MNIST datasets, each conditioned on a 2-dimensional "latent\" obtained via a t-SNE embedding of the data. In Section˜C.1, we additionally consider a much larger model trained on the Celeb-A dataset, using a t-SNE of the discrete attribute space for the conditioning variable. We note that the Celeb-A experiments, which use a simplified Schedule Deviation without the divergence component, are much more noisy and less conclusive than the corresponding MNIST or Fashion-MNIST experiments.

<!-- chunk {"id": "body-0019", "role": "body", "section": "Schedule Deviation is Widely Prevalent", "weight": 1.0} -->

Setting 2 (Conditional Maze Paths). Second, we construct a simplified path-planning problem consisting of generating trajectories in a fixed maze. For a given randomly chosen starting point, we consider all paths $\{r_{i}\}_{i=0}^{K}$ to the center of the maze and sample a path $r_{i}$ with probability $p(r_{i})\propto e^{-(d(r_{i})-d(r^{\star}))}$, where $d(r_{i})$ is the length of the $i$th path and $d(r^{\star})$ is the length shortest path. This artificially introduces multimodality around points where multiple solutions are approximately equally optimal. For each sampled path, we use 64 points along smooth Bezier curve fit to the path such that $\mathcal{X}\subset\mathbb{R}^{64\times 2},\mathcal{Z}\subset\mathbb{R}^{2}$.

<!-- chunk {"id": "body-0020", "role": "body", "section": "Schedule Deviation is Widely Prevalent", "weight": 1.0} -->

Finding 1: Prevalence of Schedule Deviation. Our experiments broadly demonstrate that Schedule Deviation is prevalent across all datasets. We visualize the total Schedule Deviation over $z\in\mathcal{Z}$ in Figure˜3 and Figure˜4 for each of our datasets with varying subsets of the training data.

<!-- chunk {"id": "body-0021", "role": "body", "section": "Schedule Deviation is Widely Prevalent", "weight": 1.0} -->

Finding 2: Schedule Deviation Persists with Model Size and Data Amount. In Figure˜5, we explore the schedule deviation for the MNIST dataset in-depth for both model and data ablations. Interestingly, we find that while larger models tend to exhibit slightly lower Schedule Deviation----the improvements appear to diminish as the model size increases and more training data can potentially (and somewhat counter-intuitively) *increase* the Schedule Deviation. Furthermore Figure˜5 (right), shows that the Schedule deviation can vary dramatically between different classes, suggesting that the Schedule Deviation is both a function of the density and structure of underlying dataset.

<!-- chunk {"id": "body-0022", "role": "body", "section": "Schedule Deviation is Widely Prevalent", "weight": 1.0} -->

Key Takeaways: Our experiments indicate several key properties on the Schedule Deviation of conditional diffusion models: even high-capacity models can exhibit significant Schedule Deviation, Schedule Deviation appears to be intrinsically related to the underlying structure of the dataset, rather than the amount of data, and, perhaps most importantly, and as we will show in the following section, Schedule Deviation is strongly predictive of divergence between different samplers.

<!-- chunk {"id": "body-0023", "role": "body", "section": "Schedule Deviation Predicts Disagreement Between Samplers", "weight": 1.0} -->

Many popular sampling algorithms, such as DDPM and DDIM leverage an SDE formalism to sample from the target distribution $p^{\star}$ (see Appendix˜B for details). These sampling algorithms implicitly make use of the equivalence in Proposition˜2.1 between the learned flow $v$ and $\nabla\log p_{s}(x|z)$ to traverse the same denoising probability path with differing levels of noise in the reverse process. Thus, when $v=\textrm{IMCF}(p_{0})$, i.e. there is no schedule deviation, both are guaranteed to generate samples $X_{s}$ whose marginals coincide with the conditional flow in Definition˜2.1. ‣ 2 Preliminaries ‣ Is Your Conditional Diffusion Model Actually Denoising?") (provided the number of steps is sufficiently large that discretization error is negligible).

<!-- chunk {"id": "body-0024", "role": "body", "section": "Schedule Deviation Predicts Disagreement Between Samplers", "weight": 1.0} -->

Empirically, significant task-specific differences in performance between DDIM and DDPM have been observed Chi et al.; Song et al.; Karras et al.. In Figure˜2, we show that Schedule Deviation is strongly correlated with the difference between these samplers, as measured by the empirical 1-Wasserstein (i.e. Earth-Movers-Distance). The heatmaps Figure˜3, Figure˜4 further demonstrate the structural similarity of Schedule Deviation and DDPM/DDIM divergence across the conditioning space. Recall Theorem˜1, which confirms that SD is a proxy for the TV distance between the traversed path the ideal denoising path. Taken together with the strong correlation between SD and OT Distance (Figures˜4 and 3), we conclude > DDPM and DDIM deviate specifically for conditioning values where the trained diffusion model deviates from the idealization of denoising its generations.

<!-- chunk {"id": "body-0025", "role": "body", "section": "Schedule Deviation Predicts Disagreement Between Samplers", "weight": 1.0} -->

We believe that this finding both sheds light on the underlying cause for sampler divergence and demonstrates the utility of our proposed metric as an investigatory tool. In Appendix˜C, we show our metric is predictive for other sampling strategies, such as the Gradient-Estimation (GE) sampling algorithm.

<!-- chunk {"id": "body-0026", "role": "body", "section": "Explaining Schedule Deviation via Smoothness and Self-Guidance", "weight": 1.0} -->

Generalization in unconditional diffusion is broadly understood as a phenomena that arises from capacity-related underfitting of the empirical score function, thereby preventing memorization of the training data. Prior work in this area has examined the effect of an implicit bias towards *smoothness* and its relation to generalization. These works, however, do not fundamentally challenge the assumption that the learned flows denoise and instead show how "better\" denoisers arises by manifold learning or interpolation over convex hulls of the data. In fact, as we elucidate in Appendix˜B, the "natural\" nonparametric extension of the closed-form in constitutes an ideal flow. In this section, we provide intuition for how *non-denoising paths* can arise from smoothness with respect to the conditioning variable through a phenomena we term self-guidance.

<!-- chunk {"id": "body-0027", "role": "body", "section": "Explaining Schedule Deviation via Smoothness and Self-Guidance", "weight": 1.0} -->

Self-Guidance and Schedule Deviation under Discrete Support. We begin by considering the special case where the data generating distribution $p^{\star}(z)$ is supported by a discrete set $S_{z}$. We can observe in Figure˜6 that for the discrete conditioning distribution shown, the schedule deviation is almost uniformly $0$ for $z\in S_{z}$. Thus, we motivate the following assumptions: the model has sufficient capacity to exactly fit the training data everywhere where there is conditioning support, the model is second-order smooth with respect to $z$, and of all flows which fit on the support of the training data, the model generalizes via the "smoothest\" flow, as measured by $\|\nabla_{z}^{2}v_{s}(x,z)\|_{\mathcal{L}_{2}}$. Under these assumptions, we develop the following result for $\mathcal{Z}\subset\mathbb{R}$, (with proof in Section˜A.4.1 ‣ Appendix A Deferred Proofs ‣ Is Your Conditional Diffusion Model Actually Denoising?")):

<!-- chunk {"id": "body-0028", "role": "body", "section": "Remark 4.1", "weight": 1.0} -->

Because diffusion models exhibit both smoothness biases in both $x$ (e.g. Aithal et al. ) and $z$ (this work), the most comprehensive proxy would consider a smoothness penalty on the joint Hessian $\nabla_{x,z}^{2}v(x,z)$. This makes a closed form solution considerably more involved, and thus we focus solely on the $\nabla_{z}$ effect to isolate functional dependence on $z$.

<!-- chunk {"id": "body-0029", "role": "body", "section": "Remark 4.1", "weight": 1.0} -->

The optimal low-$z$-curvature flow characterized in Theorem˜2. ‣ 4 Explaining Schedule Deviation via Smoothness and Self-Guidance ‣ Is Your Conditional Diffusion Model Actually Denoising?") extrapolates to out-of-distribution variables $z$ to by linearly combining flows associated with in-distribution variables $z_{i}\in S_{z}$, with weights depending *only* on the conditioning variable $z$. We refer to the phenomenon of extrapolating via combinations of flows from other parts of the conditioning space as self-guidance, as these linear combinations of flows mirrors the practice of classifier free guidance, which composes conditional and unconditional flows $v(x|z),v(x)$ via a linear combination.

<!-- chunk {"id": "body-0030", "role": "body", "section": "Remark 4.1", "weight": 1.0} -->

Schedule Deviation Emerges from Smoothing. Linear combinations of flows in general cannot be written as denoising flows (e.g. in classifier guidance,). In particular, for unconditional diffusion probability paths $p_{s}(x|z=z^{(i)})$, linearly combining $v_{s}^{\star}(x,z^{(i)})=\gamma_{1}(s)\nabla\log p_{s}(x|z=z^{(i)})+\gamma_{2}(s)x$ (recall Proposition˜2.1) does not yield a diffusion probability path, i.e. for weights $c_{1},c_{2}$, where $[\tilde{p}]_{s}$ denotes the distribution of $X_{s}:=\alpha(s)X_{0}+\sigma(s)X_{1}$ in Definition˜2.3.

<!-- chunk {"id": "body-0031", "role": "body", "section": "Remark 4.1", "weight": 1.0} -->

‣ 2 Preliminaries ‣ Is Your Conditional Diffusion Model Actually Denoising?") under $\mathrm{Law}[X_{0}]=\tilde{p}$. Thus, Theorem˜2. ‣ 4 Explaining Schedule Deviation via Smoothness and Self-Guidance ‣ Is Your Conditional Diffusion Model Actually Denoising?") suggests that a simple inductive bias towards smoothness can naturally lead to schedule deviation in $v$ when the interpolated $v^{\textsc{imcf}}_{s}(x,z^{(i)})$. We show specifically how the schedule deviation arises for particular choices of diffusion probability paths, $p_{s}^{(i)}$, $p_{s}^{(j)}$ in Appendix˜B.

<!-- chunk {"id": "body-0032", "role": "body", "section": "Remark 4.1", "weight": 1.0} -->

Self-Guidance with Uniform Conditioning. We additionally show that self guidance can occur even in the presence of continuous densities, where the minimize $v^{\star}$ of Eq.˜2.2. ‣ Model-Consistent Diffusion Flows ‣ 2 Preliminaries ‣ Is Your Conditional Diffusion Model Actually Denoising?") is uniquely specified by considering a $\lambda$-weighted penalty term with respect to the Frobenius norm of the appropriate Hessian: where $L[v]$ is the original loss in Eq.˜2.2. ‣ Model-Consistent Diffusion Flows ‣ 2 Preliminaries ‣ Is Your Conditional Diffusion Model Actually Denoising?") above and the expectation $X_{s}\mid Z$ is taken with Definition˜2.3. ‣ 2 Preliminaries ‣ Is Your Conditional Diffusion Model Actually Denoising?"), whose density we recall is $p^{\textsc{imcf}}_{s}(x,z)$.

<!-- chunk {"id": "body-0033", "role": "body", "section": "Toy Datasets", "weight": 1.0} -->

Motivated by Theorem˜2. ‣ 4 Explaining Schedule Deviation via Smoothness and Self-Guidance ‣ Is Your Conditional Diffusion Model Actually Denoising?") and Theorem˜3, we consider two synthetic datasets with scalar $x\in\mathcal{X}\subset\mathbb{R}$ and condition $z\in\mathcal{Z}\subset$ consisting of mixtures with components centered at $\mu\in\{(0,-1) \}$. The first dataset (with "discrete support\") has Gaussian noise with scale $\sigma=0.1$ applied only to the $x$ component, while the second (with "continuous support\") has IID noise of magnitude $\sigma$ applied to both the $x,z$ components.

<!-- chunk {"id": "body-0034", "role": "body", "section": "Toy Datasets", "weight": 1.0} -->

We visualize these datasets and samples from a learned denoiser, as well as a closed-form interpolants, in Figure˜6. For the discrete-conditioning setting, our closed form interpolant considers a simple linear guidance-style interpolation of the flows at $z=0$ and $z=1$. In the continuous-conditioning setting, inspired by the Fourier-convolution weighting in Theorem˜3, we construct an interpolation with a nonlinear guidance function. See Appendix˜C for additional details. These experiments validate that self-guidance can be a fundamental primitive for extrapolation in conditional settings and predict the learned behavior of neural networks.

<!-- chunk {"id": "body-0035", "role": "body", "section": "Discussion", "weight": 1.5} -->

We introduce *Schedule Deviation*, a novel, principled metric for measuring divergence of diffusion models from their idealized denoising paths. This metric is strongly predictive of deviation between different samplers and is difficult to ameliorate via increased model capacity and data quantity. Taken together, our findings reveal that the central mathematical abstraction upon which equivalent inference algorithms are derived may not be representative of actual diffusion models trained in practice, and the breakdown thereof causes seemingly equivalent methods to differ. This finding has major implications for the development of future sampling and distillation methods, and serves as a broader word of caution for the use of mathematical principles, in isolation, as a sole basis for algorithm design. However, our study has a number of limitations (see Appendix˜D: in short, our metric requires computing the divergence of the flow over generated samples, an inherently expensive operation).
