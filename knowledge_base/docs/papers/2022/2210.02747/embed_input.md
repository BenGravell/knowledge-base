<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Flow Matching for Generative Modeling

Topics include Robustness, Diffusion models, Generalization, Sampling, Normalizing flows, Optimal transport, FM, Flow matching, Generative model.

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

We introduce a new paradigm for generative modeling built on Continuous Normalizing Flows (CNFs), allowing us to train CNFs at unprecedented scale. Specifically, we present the notion of Flow Matching (FM), a simulation-free approach for training CNFs based on regressing vector fields of fixed conditional probability paths. Flow Matching is compatible with a general family of Gaussian probability paths for transforming between noise and data samples - which subsumes existing diffusion paths as specific instances. Interestingly, we find that employing FM with diffusion paths results in a more robust and stable alternative for training diffusion models. Furthermore, Flow Matching opens the door to training CNFs with other, non-diffusion probability paths. An instance of particular interest is using Optimal Transport (OT) displacement interpolation to define the conditional probability paths. These paths are more efficient than diffusion paths, provide faster training and sampling, and result in better generalization. Training CNFs using Flow Matching on ImageNet leads to consistently better performance than alternative diffusion-based methods in terms of both likelihood and sample quality, and allows fast and reliable sample generation using off-the-shelf numerical ODE solvers.

<!-- chunk {"id": "body-0003", "role": "body", "section": "Introduction", "weight": 1.5} -->

Deep generative models are a class of deep learning algorithms aimed at estimating and sampling from an unknown data distribution. The recent influx of amazing advances in generative modeling, e.g., for image generation Ramesh et al.; Rombach et al., is mostly facilitated by the scalable and relatively stable training of diffusion-based models Ho et al.; Song et al.. However, the restriction to simple diffusion processes leads to a rather confined space of sampling probability paths, resulting in very long training times and the need to adopt specialized methods (e.g., Song et al.; Zhang & Chen ) for efficient sampling.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

In this work we consider the general and deterministic framework of Continuous Normalizing Flows (CNFs; Chen et al.). CNFs are capable of modeling arbitrary probability path Figure 1: Unconditional ImageNet-128 samples of a CNF trained using Flow Matching with Optimal Transport probability paths. and are in particular known to encompass the probability paths modeled by diffusion processes. However, aside from diffusion that can be trained efficiently via, e.g., denoising score matching, no scalable CNF training algorithms are known. Indeed, maximum likelihood training (e.g., Grathwohl et al.) require expensive numerical ODE simulations, while existing simulation-free methods either involve intractable integrals or biased gradients.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

The goal of this work is to propose Flow Matching (FM), an efficient simulation-free approach to training CNF models, allowing the adoption of general probability paths to supervise CNF training. Importantly, FM breaks the barriers for scalable CNF training beyond diffusion, and sidesteps the need to reason about diffusion processes to directly work with probability paths.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

In particular, we propose the Flow Matching objective (Section 3), a simple and intuitive training objective to regress onto a target vector field that generates a desired probability path. We first show that we can construct such target vector fields through per-example (i.e., conditional) formulations. Then, inspired by denoising score matching, we show that a per-example training objective, termed Conditional Flow Matching (CFM), provides equivalent gradients and does not require explicit knowledge of the intractable target vector field. Furthermore, we discuss a general family of per-example probability paths (Section 4) that can be used for Flow Matching, which subsumes existing diffusion paths as special instances. Even on diffusion paths, we find that using FM provides more robust and stable training, and achieves superior performance compared to score matching. Furthermore, this family of probability paths also includes a particularly interesting case: the vector field that corresponds to an Optimal Transport (OT) displacement interpolant. We find that conditional OT paths are simpler than diffusion paths, forming straight line trajectories whereas diffusion paths result in curved paths. These properties seem to empirically translate to faster training, faster generation, and better performance.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

We empirically validate Flow Matching and the construction via Optimal Transport paths on ImageNet, a large and highly diverse image dataset. We find that we can easily train models to achieve favorable performance in both likelihood estimation and sample quality amongst competing diffusion-based methods. Furthermore, we find that our models produce better trade-offs between computational cost and sample quality compared to prior methods. Figure 1 depicts selected unconditional ImageNet 128$\times$`<!-- -->`{=html}128 samples from our model.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Flow Matching", "weight": 1.0} -->

Let $x_{1}$ denote a random variable distributed according to some unknown data distribution $q{(x_{1})}$. We assume we only have access to data samples from $q{(x_{1})}$ but have no access to the density function itself. Furthermore, we let $p_{t}$ be a probability path such that $p_{0} = p$ is a simple distribution, e.g., the standard normal distribution ${p{(x)}} = {\mathcal{N}{(\left. x \middle| {0,I} \right.)}}$, and let $p_{1}$ be approximately equal in distribution to $q$. We will later discuss how to construct such a path. The Flow Matching objective is then designed to match this target probability path, which will allow us to flow from $p_{0}$ to $p_{1}$.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Flow Matching", "weight": 1.0} -->

Given a target probability density path $p_{t}{(x)}$ and a corresponding vector field $u_{t}{(x)}$, which generates $p_{t}{(x)}$, we define the Flow Matching (FM) objective as where $\theta$ denotes the learnable parameters of the CNF vector field $v_{t}$ (as defined in Section 2), $t \sim {\mathcal{U}{\lbrack 0,1\rbrack}}$ (uniform distribution), and $x \sim {p_{t}{(x)}}$. Simply put, the FM loss regresses the vector field $u_{t}$ with a neural network $v_{t}$. Upon reaching zero loss, the learned CNF model will generate $p_{t}{(x)}$.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Flow Matching", "weight": 1.0} -->

Flow Matching is a simple and attractive objective, but naïvely on its own, it is intractable to use in practice since we have no prior knowledge for what an appropriate $p_{t}$ and $u_{t}$ are. There are many choices of probability paths that can satisfy ${p_{1}{(x)}} \approx {q{(x)}}$, and more importantly, we generally don't have access to a closed form $u_{t}$ that generates the desired $p_{t}$. In this section, we show that we can construct both $p_{t}$ and $u_{t}$ using probability paths and vector fields that are only defined *per sample*, and an appropriate method of aggregation provides the desired $p_{t}$ and $u_{t}$. Furthermore, this construction allows us to create a much more tractable objective for Flow Matching.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Constructing $p_{t},u_{t}$ from conditional probability paths and vector fields", "weight": 1.0} -->

A simple way to construct a target probability path is via a mixture of simpler probability paths: Given a particular data sample $x_{1}$ we denote by $p_{t}{(\left. x \middle| x_{1} \right.)}$ a *conditional probability path* such that it satisfies ${p_{0}{(\left. x \middle| x_{1} \right.)}} = {p{(x)}}$ at time $t = 0$, and we design $p_{1}{(\left. x \middle| x_{1} \right.)}$ at $t = 1$ to be a distribution concentrated around $x = x_{1}$, e.g., ${p_{1}{(\left. x \middle| x_{1} \right.)}} = {\mathcal{N}{(\left.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Constructing $p_{t},u_{t}$ from conditional probability paths and vector fields", "weight": 1.0} -->

x \middle| {x_{1},{\sigma^{2}I}} \right.)}}$, a normal distribution with $x_{1}$ mean and a sufficiently small standard deviation $\sigma > 0$. Marginalizing the conditional probability paths over $q{(x_{1})}$ give rise to *the marginal probability path* where in particular at time $t = 1$, the marginal probability $p_{1}$ is a mixture distribution that closely approximates the data distribution $q$, Interestingly, we can also define a *marginal vector field*, by "marginalizing" over the conditional vector fields in the following sense (we assume ${p_{t}{(x)}} > 0$ for all $t$ and $x$): where $u_{t}{(\cdot |x_{1})}:{\mathbb{R}}^{d}\rightarrow{\mathbb{R}}^{d}$ is a conditional vector field that generates $p_{t}{(\cdot |x_{1})}$.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Constructing $p_{t},u_{t}$ from conditional probability paths and vector fields", "weight": 1.0} -->

It may not seem apparent, but this way of aggregating the conditional vector fields actually results in the correct vector field for modeling the marginal probability path.

<!-- chunk {"id": "body-0014", "role": "body", "section": "Constructing $p_{t},u_{t}$ from conditional probability paths and vector fields", "weight": 1.0} -->

Our first key observation is this: *The marginal vector field (equation 8) generates the marginal probability path (equation 6).* This provides a surprising connection between the conditional VFs (those that generate conditional probability paths) and the marginal VF (those that generate the marginal probability path). This connection allows us to break down the unknown and intractable marginal VF into simpler conditional VFs, which are much simpler to define as these only depend on a single data sample. We formalize this in the following theorem.

<!-- chunk {"id": "body-0015", "role": "body", "section": "Conditional Flow Matching", "weight": 1.0} -->

Unfortunately, due to the intractable integrals in the definitions of the marginal probability path and VF (equations 6 and 8), it is still intractable to compute $u_{t}$, and consequently, intractable to naïvely compute an unbiased estimator of the original Flow Matching objective. Instead, we propose a simpler objective, which surprisingly will result in the same optima as the original objective. Specifically, we consider the *Conditional Flow Matching* (CFM) objective, where $t \sim {\mathcal{U}{\lbrack 0,1\rbrack}}$, $x_{1} \sim {q{(x_{1})}}$, and now $x \sim {p_{t}{(\left. x \middle| x_{1} \right.)}}$. Unlike the FM objective, the CFM objective allows us to easily sample unbiased estimates as long as we can efficiently sample from $p_{t}{(\left. x \middle| x_{1} \right.)}$ and compute $u_{t}{(\left.

<!-- chunk {"id": "body-0016", "role": "body", "section": "Conditional Flow Matching", "weight": 1.0} -->

x \middle| x_{1} \right.)}$, both of which can be easily done as they are defined on a per-sample basis.\Our second key observation is therefore: *The FM (equation 5) and CFM (equation 9) objectives have identical gradients w.r.t. $\theta$.* That is, optimizing the CFM objective is equivalent (in expectation) to optimizing the FM objective. Consequently, this allows us to train a CNF to generate the marginal probability path $p_{t}$---which in particular, approximates the unknown data distribution $q$ at $t$=$1$--- without ever needing access to either the marginal probability path or the marginal vector field. We simply need to design suitable *conditional* probability paths and vector fields. We formalize this property in the following theorem.

<!-- chunk {"id": "body-0017", "role": "body", "section": "Conditional Probability Paths and Vector Fields", "weight": 1.0} -->

The Conditional Flow Matching objective works with any choice of conditional probability path and conditional vector fields. In this section, we discuss the construction of $p_{t}{(\left. x \middle| x_{1} \right.)}$ and $u_{t}{(\left. x \middle| x_{1} \right.)}$ for a general family of Gaussian conditional probability paths. Namely, we consider conditional probability paths of the form where $\mu:{{{\lbrack 0,1\rbrack} \times {\mathbb{R}}^{d}}\rightarrow{\mathbb{R}}^{d}}$ is the time-dependent mean of the Gaussian distribution, while $\sigma:{{{\lbrack 0,1\rbrack} \times {\mathbb{R}}}\rightarrow{\mathbb{R}}_{> 0}}$ describes a time-dependent scalar standard deviation (std).

<!-- chunk {"id": "body-0018", "role": "body", "section": "Conditional Probability Paths and Vector Fields", "weight": 1.0} -->

There is an infinite number of vector fields that generate any particular probability path (e.g., by adding a divergence free component to the continuity equation, see equation 26), but the vast majority of these is due to the presence of components that leave the underlying distribution invariant---for instance, rotational components when the distribution is rotation-invariant---leading to unnecessary extra compute. We decide to use the simplest vector field corresponding to a canonical transformation for Gaussian distributions. Specifically, consider the flow (conditioned on $x_{1}$) When $x$ is distributed as a standard Gaussian, $\psi_{t}{(x)}$ is the affine transformation that maps to a normally-distributed random variable with mean $\mu_{t}{(x_{1})}$ and std $\sigma_{t}{(x_{1})}$. That is to say, according to equation 4, $\psi_{t}$ pushes the noise distribution ${p_{0}{(\left.

<!-- chunk {"id": "body-0019", "role": "body", "section": "Conditional Probability Paths and Vector Fields", "weight": 1.0} -->

x \middle| x_{1} \right.)}} = {p{(x)}}$ to $p_{t}{(\left. x \middle| x_{1} \right.)}$, i.e., This flow then provides a vector field that generates the conditional probability path: Reparameterizing $p_{t}{(\left. x \middle| x_{1} \right.)}$ in terms of just $x_{0}$ and plugging equation 13 in the CFM loss we get Since $\psi_{t}$ is a simple (invertible) affine map we can use equation 13 to solve for $u_{t}$ in a closed form. Let $f'$ denote the derivative with respect to time, i.e., $f' = {\frac{d}{dt}f}$, for a time-dependent function $f$.

<!-- chunk {"id": "body-0020", "role": "body", "section": "Special instances of Gaussian conditional probability paths", "weight": 1.0} -->

Our formulation is fully general for arbitrary functions $\mu_{t}{(x_{1})}$ and $\sigma_{t}{(x_{1})}$, and we can set them to any differentiable function satisfying the desired boundary conditions. We first discuss the special cases that recover probability paths corresponding to previously-used diffusion processes. Since we directly work with probability paths, we can simply depart from reasoning about diffusion processes altogether. Therefore, in the second example below, we directly formulate a probability path based on the Wasserstein-2 optimal transport solution as an interesting instance.

<!-- chunk {"id": "body-0021", "role": "body", "section": "Example I: Diffusion conditional VFs", "weight": 1.0} -->

Diffusion models start with data points and gradually add noise until it approximates pure noise. These can be formulated as stochastic processes, which have strict requirements in order to obtain closed form representation at arbitrary times $t$, resulting in Gaussian conditional probability paths $p_{t}{(\left. x \middle| x_{1} \right.)}$ with specific choices of mean $\mu_{t}{(x_{1})}$ and std $\sigma_{t}{(x_{1})}$. For example, the reversed (noise$\rightarrow$data) Variance Exploding (VE) path has the form where $\sigma_{t}$ is an increasing function, $\sigma_{0} = 0$, and $\sigma_{1} \gg 1$. Next, equation 16 provides the choices of ${\mu_{t}{(x_{1})}} = x_{1}$ and ${\sigma_{t}{(x_{1})}} = \sigma_{1 - t}$.

<!-- chunk {"id": "body-0022", "role": "body", "section": "Example I: Diffusion conditional VFs", "weight": 1.0} -->

Plugging these into equation 15 of Theorem 3 we get The reversed (noise$\rightarrow$data) Variance Preserving (VP) diffusion path has the form and $\beta$ is the noise scale function. Equation 18 provides the choices of ${\mu_{t}{(x_{1})}} = {\alpha_{1 - t}x_{1}}$ and ${\sigma_{t}{(x_{1})}} = \sqrt{1 - \alpha_{1 - t}^{2}}$. Plugging these into equation 15 of Theorem 3 we get Our construction of the conditional VF $u_{t}{(\left. x \middle| x_{1} \right.)}$ does in fact coincide with the vector field previously used in the deterministic probability flow (Song et al., equation 13) when restricted to these conditional diffusion processes; see details in Appendix D. Nevertheless, combining the diffusion conditional VF with the Flow Matching objective offers an attractive training alternative---which we find to be more stable and robust in our experiments---to existing score matching approaches.

<!-- chunk {"id": "body-0023", "role": "body", "section": "Example I: Diffusion conditional VFs", "weight": 1.0} -->

Another important observation is that, as these probability paths were previously derived as solutions of diffusion processes, they do not actually reach a true noise distribution in finite time. In practice, $p_{0}{(x)}$ is simply approximated by a suitable Gaussian distribution for sampling and likelihood evaluation. Instead, our construction provides full control over the probability path, and we can just directly set $\mu_{t}$ and $\sigma_{t}$, as we will do next.

<!-- chunk {"id": "body-0024", "role": "body", "section": "Example I: Diffusion conditional VFs", "weight": 1.0} -->

Diffusion path – conditional score function OT path – conditional vector field Figure 2: Compared to the diffusion path’s conditional score function, the OT path’s conditional vector field has constant direction in time and is arguably simpler to fit with a parametric model. Note the blue color denotes larger magnitude while red color denotes smaller magnitude.

<!-- chunk {"id": "body-0025", "role": "body", "section": "Example II: Optimal Transport conditional VFs", "weight": 1.0} -->

An arguably more natural choice for conditional probability paths is to define the mean and the std to simply change linearly in time, i.e., According to Theorem 3 this path is generated by the VF which, in contrast to the diffusion conditional VF (equation 19), is defined for all $t \in {\lbrack 0,1\rbrack}$. The conditional flow that corresponds to $u_{t}{(\left. x \middle| x_{1} \right.)}$ is and in this case, the CFM loss (see equations 9, 14) takes the form: Allowing the mean and std to change linearly not only leads to simple and intuitive paths, but it is actually also optimal in the following sense. The conditional flow $\psi_{t}{(x)}$ is in fact the Optimal Transport (OT) *displacement map* between the two Gaussians $p_{0}{(\left. x \middle| x_{1} \right.)}$ and $p_{1}{(\left. x \middle| x_{1} \right.)}$.

<!-- chunk {"id": "body-0026", "role": "body", "section": "Example II: Optimal Transport conditional VFs", "weight": 1.0} -->

The OT *interpolant*, which is a probability path, is defined to be (see Definition 1.1 in McCann): where $\psi:{{\mathbb{R}}^{d}\rightarrow{\mathbb{R}}^{d}}$ is the OT map pushing $p_{0}$ to $p_{1}$, $id$ denotes the identity map, i.e., ${{id}{(x)}} = x$, and ${{({1 - t})}{id}} + {t\psi}$ is called the OT displacement map. Example 1.7 in McCann shows, that in our case of two Gaussians where the first is a standard one, the OT displacement map takes the form of equation 22.

<!-- chunk {"id": "body-0027", "role": "body", "section": "Example II: Optimal Transport conditional VFs", "weight": 1.0} -->

Intuitively, particles under the OT displacement map always move in straight line trajectories and with constant speed. Figure 3 depicts sampling paths for the diffusion and OT conditional VFs. Interestingly, we find that sampling trajectory from diffusion paths can "overshoot" the final sample, resulting in unnecessary backtracking, whilst the OT paths are guaranteed to stay straight.

<!-- chunk {"id": "body-0028", "role": "body", "section": "Experiments", "weight": 1.0} -->

We explore the empirical benefits of using Flow Matching on the image datasets of CIFAR-10 and ImageNet at resolutions 32, 64, and 128. We also ablate the choice of diffusion path in Flow Matching, particularly between the standard variance preserving diffusion path and the optimal transport path. We discuss how sample generation is improved by directly parameterizing the generating vector field and using the Flow Matching objective. Lastly we show Flow Matching can also be used in the conditional generation setting. Unless otherwise specified, we evaluate likelihood and samples from the model using dopri5 at absolute and relative tolerances of 1e-5. Generated samples can be found in the Appendix, and all implementation details are in Appendix E.

<!-- chunk {"id": "body-0029", "role": "body", "section": "Density Modeling and Sample Quality on ImageNet", "weight": 1.0} -->

We start by comparing the same model architecture, i.e., the U-Net architecture from Dhariwal & Nichol with minimal changes, trained on CIFAR-10, and ImageNet 32/64 with different popular diffusion-based losses: DDPM, Score Matching (SM), and Score Flow (SF); see Appendix E.1 for exact details. Table 1 (left) summarizes our results alongside these baselines reporting negative log-likelihood (NLL) in units of bits per dimension (BPD), sample quality as measured by the Frechet Inception Distance (FID; Heusel et al. ), and averaged number of function evaluations (NFE) required for the adaptive solver to reach its a prespecified numerical tolerance, averaged over 50k samples. All models are trained using the same architecture, hyperparameter values and number of training iterations, where baselines are allowed more iterations for better convergence. Note that these are *unconditional* models. On both CIFAR-10 and ImageNet, FM-OT consistently obtains best results across all our quantitative measures compared to competing methods.

<!-- chunk {"id": "body-0030", "role": "body", "section": "Density Modeling and Sample Quality on ImageNet", "weight": 1.0} -->

We are noticing a higher that usual FID performance in CIFAR-10 compared to previous works that can possibly be explained by the fact that our used architecture was not optimized for CIFAR-10.

<!-- chunk {"id": "body-0031", "role": "body", "section": "Density Modeling and Sample Quality on ImageNet", "weight": 1.0} -->

Secondly, Table 1 (right) compares a model trained using Flow Matching with the OT path on ImageNet at resolution 128$\times$`<!-- -->`{=html}128. Our FID is state-of-the-art with the exception of IC-GAN which uses conditioning with a self-supervised model, and therefore is left out of this table. Figures 11, 12, 13 in the Appendix show non-curated samples from these models.

<!-- chunk {"id": "body-0032", "role": "body", "section": "Density Modeling and Sample Quality on ImageNet", "weight": 1.0} -->

Faster training. While existing works train diffusion models with a very high number of iterations (e.g., 1.3m and 10m iterations are reported by Score Flow and VDM, respectively), we find that Flow Matching generally converges much faster. Figure 5 shows FID curves during training of Flow Matching and all baselines for ImageNet 64$\times$`<!-- -->`{=html}64; FM-OT is able to lower the FID faster and to a greater extent than the alternatives. For ImageNet-128 Dhariwal & Nichol train for 4.36m iterations with batch size 256, while FM (with 25% larger model) used 500k iterations with batch size 1.5k, i.e., 33% less image throughput; see Table 3 for exact details. Furthermore, the cost of sampling from a model can drastically change during training for score matching, whereas the sampling cost stays constant when training with Flow Matching (Figure 10 in Appendix).

<!-- chunk {"id": "body-0033", "role": "body", "section": "Sampling Efficiency", "weight": 1.0} -->

Score Matching w/ Diffusion Flow Matching w/ Diffusion Figure 6: Sample paths from the same initial noise with models trained on ImageNet 64×64. The OT path reduces noise roughly linearly, while diffusion paths visibly remove noise only towards the end of the path. Note also the differences between the generated images.

<!-- chunk {"id": "body-0034", "role": "body", "section": "Sampling Efficiency", "weight": 1.0} -->

For sampling, we first draw a random noise sample $x_{0} \sim {\mathcal{N}{(0,I)}}$ then compute $\phi_{1}{(x_{0})}$ by solving equation 1 with the trained VF, $v_{t}$, on the interval $t \in {\lbrack 0,1\rbrack}$ using an ODE solver. While diffusion models can also be sampled through an SDE formulation, this can be highly inefficient and many methods that propose fast samplers (e.g., Song et al.; Zhang & Chen ) directly make use of the ODE perspective (see Appendix D). In part, this is due to ODE solvers being much more efficient---yielding lower error at similar computational costs ---and the multitude of available ODE solver schemes. When compared to our ablation models, we find that models trained using Flow Matching with the OT path always result in the most efficient sampler, regardless of ODE solver, as demonstrated next.

<!-- chunk {"id": "body-0035", "role": "body", "section": "Sampling Efficiency", "weight": 1.0} -->

Sample paths. We first qualitatively visualize the difference in sampling paths between diffusion and OT. Figure 6 shows samples from ImageNet-64 models using identical random seeds, where we find that the OT path model starts generating images sooner than the diffusion path models, where noise dominates the image until the very last time point. We additionally depict the probability density paths in 2D generation of a checkerboard pattern, Figure 4 (left), noticing a similar trend.

<!-- chunk {"id": "body-0036", "role": "body", "section": "Sampling Efficiency", "weight": 1.0} -->

Low-cost samples. We next switch to fixed-step solvers and compare low ($\leq$`<!-- -->`{=html}100) NFE samples computed with the ImageNet-32 models from Table 1. In Figure 7 (left), we compare the per-pixel MSE of low NFE solutions compared with 1000 NFE solutions (we use 256 random noise seeds), and notice that the FM with OT model produces the best numerical error, in terms of computational cost, requiring roughly only 60% of the NFEs to reach the same error threshold as diffusion models. Secondly, Figure 7 (right) shows how FID changes as a result of the computational cost, where we find FM with OT is able to achieve decent FID even at very low NFE values, producing better trade-off between sample quality and cost compared to ablated models. Figure 4 (right) shows low-cost sampling effects for the 2D checkerboard experiment.

<!-- chunk {"id": "body-0037", "role": "body", "section": "Sampling Efficiency", "weight": 1.0} -->

Error of ODE solution Flow matching w/ Diffusion Score matching w/ Diffusion Figure 7: Flow Matching, especially when using OT paths, allows us to use fewer evaluations for sampling while retaining similar numerical error (left) and sample quality (right). Results are shown for models trained on ImageNet 32×32, and numerical errors are for the midpoint scheme.

<!-- chunk {"id": "body-0038", "role": "body", "section": "Conditional sampling from low-resolution images", "weight": 1.0} -->

Lastly, we experimented with Flow Matching for conditional image generation. In particular, upsampling images from 64$\times$`<!-- -->`{=html}64 to 256$\times$`<!-- -->`{=html}256. We follow the evaluation procedure in and compute the FID of the upsampled validation images; baselines include reference (FID of original validation set), and regression. Results are in Table 2. Upsampled image samples are shown in Figures 14, 15 in the Appendix. FM-OT achieves similar PSNR and SSIM values to while considerably improving on FID and IS, which as argued by is a better indication of generation quality.

<!-- chunk {"id": "body-0039", "role": "body", "section": "Conclusion", "weight": 1.5} -->

We introduced Flow Matching, a new simulation-free framework for training Continuous Normalizing Flow models, relying on conditional constructions to effortlessly scale to very high dimensions. Furthermore, the FM framework provides an alternative view on diffusion models, and suggests forsaking the stochastic/diffusion construction in favor of more directly specifying the probability path, allowing us to, e.g., construct paths that allow faster sampling and/or improve generation. We experimentally showed the ease of training and sampling when using the Flow Matching framework, and in the future, we expect FM to open the door to allowing a multitude of probability paths (e.g., non-isotropic Gaussians or more general kernels altogether).

<!-- chunk {"id": "body-0040", "role": "body", "section": "Social responsibility", "weight": 1.0} -->

Along side its many positive applications, image generation can also be used for harmful proposes. Using content-controlled training sets and image validation/classification can help reduce these uses. Furthermore, the energy demand for training large deep learning models is increasing at a rapid pace, focusing on methods that are able to train using less gradient updates / image throughput can lead to significant time and energy savings.
