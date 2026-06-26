<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Matrix-free Second-order Optimization of Gaussian Splats with Residual Sampling

Topics include Computational complexity, Optimization, Learning, Sampling, LM, Conjugate gradient, CG, Line search.

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

3D Gaussian Splatting (3DGS) is widely used for novel view synthesis due to its high rendering quality and fast inference time. However, 3DGS predominantly relies on first-order optimizers such as Adam, which leads to long training times. To address this limitation, we propose a novel second-order optimization strategy based on Levenberg-Marquardt (LM) and Conjugate Gradient (CG), specifically tailored towards Gaussian Splatting. Our key insight is that the Jacobian in 3DGS exhibits significant sparsity since each Gaussian affects only a limited number of pixels. We exploit this sparsity by proposing a matrix-free and GPU-parallelized LM optimization. To further improve its efficiency, we propose sampling strategies for both camera views and loss function and, consequently, the normal equation, significantly reducing the computational complexity. In addition, we increase the convergence rate of the second-order approximation by introducing an effective heuristic to determine the learning rate that avoids the expensive computation cost of line search methods.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

As a result, our method achieves a 4x speedup over standard LM and outperforms Adam by ~5x when the Gaussian count is low while providing ~1.3x speed in moderate counts. In addition, our matrix-free implementation achieves 2x speedup over the concurrent second-order optimizer 3DGS-LM, while using 3.5x less memory.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

Photoreal novel view synthesis from multi-view images or video has attracted significant attention in recent years due to widely applicable downstream tasks in content creation, VR/XR, gaming, and the movie industry, to name a few. Here, Neural Radiance Fields (NeRF) and 3D Gaussian Splatting (3DGS) mark a major milestone, due to their unprecedented quality leading to follow ups beyond view synthesis like VR rendering, avatar creation, simultaneous localization and mapping (SLAM), and scene editing.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

However, NeRF-based models often require substantial training time, and researchers have developed various techniques to mitigate this problem. Some of them include neural hashing, employing explicit scene modeling, improved sampling strategies, and tensor factorization methods. 3DGS instead does not rely on coordinate-based representations, but leverages a set of 3D Gaussians, which can be effectively rendered into image space using tile-based rasterization. Nonetheless, optimizing the parameters of each Gaussian can still take hours. Previous work focused on finding better densification strategies, quantization and compression of Gaussians, and more efficient implementations for the backward pass, which led to substantially reduced training times. However, all of them mostly rely on a first-order optimization routine, i.e. gradient descent or Adam, and do not explore other (potentially second-order) alternatives.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

Second-order optimization is known for having better convergence guarantees compared to first-order methods. However, its adoption in 3DGS remains challenging due to the high memory and computational demands associated with storing and inverting large Jacobian matrices. Notably, the Jacobian size scales quadratically with both the number of Gaussians and image pixels. Unlike NeRFs, which rely on a dense neural network and a coordinate-based formulation, 3DGS benefits from inherently sparse Jacobians since each Gaussian influences only a small subset of pixels (residuals). Our *key idea* is to leverage this sparsity in order to make second-order optimization for Gaussian Splatting not only tractable, but also potentially more efficient than first-order baselines.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

To this end, we formulate fitting the Gaussian parameters to the multi-view images as a non-linear least squares optimization problem and leverage the Levenberg-Marquardt (LM) algorithm for solving it. Concurrent work 3DGS-LM also adopts the LM optimizer with Gaussian Splatting; however, it still suffers from the high storage and computation requirements of the Jacobian matrix. In addition, 3DGS-LM has to run the Adam optimizer first to provide fast convergence, since solving the numerical system arising from the normal equation is computationally expensive.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Introduction", "weight": 1.5} -->

To overcome these challenges, we propose a GPU-parallelized matrix-free conjugate gradient solver coupled with pixel sampling, which circumvents explicit storage of the Jacobian matrix and solves the matrix inverse iteratively. Firstly, we show that implementing a matrix-free solver naively does not result in a fast optimizer because of the high computational cost of Jacobian-vector products. Therefore, we propose to approximate the full normal equation by an effective view sampling strategy and by sampling individual pixels, which results in significantly faster convergence. These approximations make the Jacobian-vector products cheaper to begin with and obviate the need for the Adam optimizer. We also introduce a heuristic to automatically determine the learning rate, which eliminates the need for line search algorithms that are commonly used in conjunction with second-order optimizers.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Introduction", "weight": 1.5} -->

Overall, with these improvements, our proposed second-order optimizer is both memory and compute efficient compared to 3DGS-LM, suggesting that second-order optimization for 3DGS is a highly promising direction for further study. Our optimizer demonstrates improvements in settings with a low and moderate number of Gaussians over first-order optimizers as well. In summary, we propose a novel second-order optimizer for 3DGS with the following features: Formulating Gaussian Splatting as a non-linear least squares optimization problem that is solved using a memory and computationally efficient matrix-free Levenberg-Marquardt and conjugate gradient solver specifically tailored towards 3DGS.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Introduction", "weight": 1.5} -->

A view and importance sampling strategy over the pixels (residuals) to effectively approximate the loss, leading to a significant decrease in computational complexity.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Introduction", "weight": 1.5} -->

An effective heuristic to determine the learning rate, which eliminates the need for expensive line search methods while providing stable convergence for 3DGS optimization.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Method", "weight": 1.0} -->

We first introduce the LM optimizer in Sec. 4.1, which we adopt in this work. Then, we derive why a naive implementation is not feasible for Gaussian Splatting. To resolve this issue, in Sec. 4.2 Solver for 3DGS ‣ 4 Method ‣ Matrix-free Second-order Optimization of Gaussian Splats with Residual Sampling"), we discuss our matrix-free approach to adapt the LM optimizer. In detail, we propose a GPU-parallelized conjugate gradient solver for our second-order 3DGS optimizer, which circumvents explicit storage of the Jacobian matrix, and solves the matrix inverse iteratively. Next, in Sec. 4.3, we introduce a new view sampling strategy to effectively approximate the full normal equation, thereby providing reliable update step directions by integrating information from multiple views. In Sec. 4.4, we present our residual sampling, providing an approximate loss function, which results in significantly faster convergence.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Method", "weight": 1.0} -->

Lastly, in Sec. 4.5, we introduce a heuristic to automatically determine the learning rate, which eliminates the need for line search algorithms that are commonly used in conjunction with second-order optimizers. The overview of all the components is given in Fig. 2 ‣ Matrix-free Second-order Optimization of Gaussian Splats with Residual Sampling").

<!-- chunk {"id": "body-0014", "role": "body", "section": "Levenberg-Marquardt Optimizer for 3DGS", "weight": 1.0} -->

We use the LM optimizer with a fixed damping parameter to compute an update step by minimizing the loss over a mini-batch $B$, which includes images of the shape height $H$, width $W$, and channels $C$. The optimizable parameters for each Gaussian are opacity $o\in\mathbb{R}$, color $c\in\mathbb{R}^{3}$, mean value $\mathcal{X}\in\mathbb{R}^{3}$, scale $s\in\mathbb{R}^{3}$, and quaternion rotation $q\in\mathbb{R}^{4}$. We represent all Gaussian parameters with $\boldsymbol{\beta}\in\mathbb{R}^{P}$, where we denote the total number of optimizable parameters with $P$.

<!-- chunk {"id": "body-0015", "role": "body", "section": "Levenberg-Marquardt Optimizer for 3DGS", "weight": 1.0} -->

The rendering loss function in Eq. 5 ‣ Matrix-free Second-order Optimization of Gaussian Splats with Residual Sampling") can be rewritten as a nonlinear least squares objective: where $r$ is a residual and $M=BHWC$. The residuals are defined as pixel and structural similarity losses; however, to keep the derivation concise, we omit the structural similarity term: Then, the update vector $\Delta\boldsymbol{\beta}\in\mathbb{R}^{P}$ is retrieved by solving the following normal equation: where $\lambda$ is the fixed damping parameter, $\mathbf{r}\in\mathbb{R}^{M}$ is the vectorized form of the residuals $r_{i}$, and $\mathbf{J}\in\mathbb{R}^{M\times P}$ is the Jacobian of $\mathbf{r}$.

<!-- chunk {"id": "body-0016", "role": "body", "section": "Levenberg-Marquardt Optimizer for 3DGS", "weight": 1.0} -->

Input: Gaussians βk, cameras 𝒞 Output: Updated Gaussians βk + 1 1:ℐ, 𝒞B = getBatch(𝒞) ⊳ View Sampling, Sec. 4.3 2:$\hat{\mathcal{I}}=\text{splatting}({\boldsymbol{\beta}_{k}},\mathcal{C}_{B})$ 3:$\mathcal{\mathbf{r}}=\text{getResiduals}(\mathcal{I},\hat{\mathcal{I}})$ ⊳ Eq. 7 4: ⊳ Beginning of matrix-free PCG solver (Sec 4.2) 6:M−1 = 1/Diag(J⊤J + λI) ⊳ Estimated in Sec. 4.4

<!-- chunk {"id": "body-0017", "role": "body", "section": "Levenberg-Marquardt Optimizer for 3DGS", "weight": 1.0} -->

$\beta=\frac{\mathbf{r}_{i+1}^{T}\mathbf{z}_{i+1}}{\mathbf{r}_{i}^{T}\mathbf{z}_{i}}$ 19:βk + 1 = βk + η xi + 1 ⊳ Dynamic LR Sched., Sec. 4.5 Algorithm 1 One step of LM optimizer with matrix-free PCG solver.

<!-- chunk {"id": "body-0018", "role": "body", "section": "Levenberg-Marquardt Optimizer for 3DGS", "weight": 1.0} -->

One iteration of the LM optimizer is completed after we update all the Gaussian parameters $\boldsymbol{\beta}$ with the learning rate $\eta$: Note that in the original 3DGS, for each parameter group (opacity, color, mean, scale, and rotation), a different learning rate is used. On the other hand, we use a uniform learning rate across parameters because Gauss-Newton-type methods inherently incorporate parameter scaling through the Hessian approximation $\mathbf{J^{\top}J}$. In Sec. 4.5, we discuss a heuristic to determine the learning rate at every iteration.

<!-- chunk {"id": "body-0019", "role": "body", "section": "Levenberg-Marquardt Optimizer for 3DGS", "weight": 1.0} -->

In practice, naively solving the normal equation is not feasible, especially in large-scale numerical systems. First, the Jacobians scale quadratically with both the number of Gaussians and the number of pixels, and storing the Jacobians explicitly in memory quickly becomes infeasible. For example, using $100$ images at a resolution of $800\times 800$ pixels as training data, along with $10\,000$ Gaussians to model the 3D scene, would result in Jacobians exceeding $100$ TB in size. Even assuming a sparse storage format with a $99\%$ sparsity, the storage requirement would still exceed $1$ TB for a true LM optimizer. In addition, explicitly inverting the system matrix has O($P^{3}$) time complexity when implemented naively. Thus, computing the explicit inverse is often infeasible, and previous work has focused on solving the normal equation iteratively, but they still remain computationally expensive, as discussed in the next section.

<!-- chunk {"id": "body-0020", "role": "body", "section": "Matrix-free Preconditioned Conjugate Gradient (PCG) Solver for 3DGS", "weight": 1.0} -->

We first discuss our matrix-free PCG solver to adapt the LM optimizer. In this subsection, we present a GPU-parallelized conjugate gradient solver, which does not need to store the Jacobian matrix explicitly, avoiding the memory issues mentioned in Sec. 4.1. To achieve this, we solve Eq. 8 via the preconditioned conjugate gradient algorithm, which only needs results of Jacobian-vector products, and finds the solution $\Delta\boldsymbol{\beta}$ iteratively.

<!-- chunk {"id": "body-0021", "role": "body", "section": "Matrix-free Preconditioned Conjugate Gradient (PCG) Solver for 3DGS", "weight": 1.0} -->

To improve the condition number of the linear system in Eq. 8, we used the Jacobi preconditioner due to its simplicity and effectiveness. More specifically, we use $\frac{1}{\operatorname{diag}(\mathbf{J^{\top}J}+\lambda\mathbf{I})}\in\mathbb{R}^{P}$, as the precondition. We provide the implementation of the solver in CUDA, together with efficient Jacobian-vector product kernel, which is implemented with forward mode differentiation and dual numbers. See the supplementary material for details about the kernel design. The pseudocode of the optimizer is given in Alg. 1.

<!-- chunk {"id": "body-0022", "role": "body", "section": "Matrix-free Preconditioned Conjugate Gradient (PCG) Solver for 3DGS", "weight": 1.0} -->

Although this optimizer is able to converge to the final solution in a limited number of steps, it is $4\times$ slower than our final method, as shown in Tab. 3. The main reason for this is that the conjugate gradient algorithm needs to run several iterations, therefore, we need to repeatedly compute the $\mathbf{J}^{\top}\mathbf{J}\mathbf{p}$ product arising on line $10$ of Alg. 1. This kind of computational complexity commonly arises when a second-order optimizer is used in large-scale numerical systems, and usually, an approximation method is used for efficiency. The common approximation methods are diagonal and block-diagonal approximation of the Hessian or $\mathbf{J^{\top}J}$ matrix.

<!-- chunk {"id": "body-0023", "role": "body", "section": "Matrix-free Preconditioned Conjugate Gradient (PCG) Solver for 3DGS", "weight": 1.0} -->

We observe that the Hessian approximation $\mathbf{J^{\top}J}$ in 3DGS does not exhibit a dominant diagonal or block-diagonal structure, as illustrated in Fig. 3. This arises because each pixel is rendered through the interaction of multiple Gaussians, as described in Eq. 4 ‣ Matrix-free Second-order Optimization of Gaussian Splats with Residual Sampling"). In other words, no single Gaussian independently represents a surface; instead, it relies on the collective contribution of surrounding Gaussians to accurately capture the ground truth. This leads to many off-diagonal and off-block-diagonal entries in $\mathbf{J^{\top}J}$. Therefore, the common diagonal and block-diagonal approximations do not provide good approximations. To this end, we propose to estimate the loss function with our proposed view and residual sampling. The sampling techniques enable the matrix-free implementation as the cost of solving Eq. 8 is drastically reduced.

<!-- chunk {"id": "body-0024", "role": "body", "section": "View Sampling", "weight": 1.0} -->

Second-order methods like LM are typically used in deterministic settings where the full objective is evaluated at every iteration. If this is not the case, estimating local curvature can be problematic and become unreliable. This poses a challenge in the 3DGS setting, where the number of views can exceed hundreds, as incorporating all of them at the same time is infeasible. Yet, to compute meaningful gradients, we must find an effective way to approximate the full normal equation in Eq. 8.

<!-- chunk {"id": "body-0025", "role": "body", "section": "View Sampling", "weight": 1.0} -->

To this end, we introduce a camera sampling approach that allows us to get a diverse set of views in each batch. Let $\mathcal{C}=\{c_{1},c_{2},\dots,c_{N}\}$ be the set of all cameras. For each camera $c_{i}$, we form the feature vector: where $(x,y,z)$ is the cameras' normalized location and $({dx},{dy},{dz})$ is the viewing direction. We then run K-Means clustering on $\{f_{i}\}_{i=1}^{N}$ to partition the cameras into batch size number of clusters (e.g., 8 clusters created for a batch size of 8). A camera is then randomly selected from every cluster and collected in the set $\mathcal{C}_{B}$, which serves as training input. This approach ensures that each batch captures a more balanced and diverse set of views, resulting in a more accurate estimation of the curvature information. As evidenced by Tab.

<!-- chunk {"id": "body-0026", "role": "body", "section": "View Sampling", "weight": 1.0} -->

2, this method converges to higher scores compared to the random sampling of the cameras.

<!-- chunk {"id": "body-0027", "role": "body", "section": "Estimation of Loss Function with Residual Sampling", "weight": 1.0} -->

Additionally, to improve the efficiency and feasibility of our second-order optimizer for 3DGS, we further exploit the sparsity property within the 3DGS representation, which has been discussed in Sec. 4.2 Solver for 3DGS ‣ 4 Method ‣ Matrix-free Second-order Optimization of Gaussian Splats with Residual Sampling"). Yet, at the same time, as observed in Fig. 3, there does not exist a well-organized structure to the sparsity. Instead, in this paper, we propose to adopt a residual sampling approach.

<!-- chunk {"id": "body-0028", "role": "body", "section": "Estimation of Loss Function with Residual Sampling", "weight": 1.0} -->

We begin our derivation by rewriting our least squares loss function in Eq. 6 as an integral: Then, the loss function is given as: where the integral is defined over $\Omega$, the union of all image domains of all cameras, and calculated at the coordinates $\mathbf{p}\in\mathbb{R}^{2}$ of the image plane. To estimate the loss function $L$, we express it as an expectation with respect to an arbitrary probability distribution $q(\mathbf{p})$: This formulation allows us to interpret $q(\mathbf{p})$ as a sampling distribution over the domain $\Omega$. Consequently, we can approximate the expectation numerically using Monte Carlo estimation. In particular, by independently sampling $N$ pixels $\{\mathbf{p}_{i}\}_{i=1}^{N}$ from $q(\mathbf{p})$, the loss function can be approximated as: The estimated loss function allows us to derive the estimated versions of Jacobian-vector products arising in the PCG solver.

<!-- chunk {"id": "body-0029", "role": "body", "section": "Estimation of Loss Function with Residual Sampling", "weight": 1.0} -->

The derivative of the estimated loss function with respect to a parameter becomes: This gradient estimates the right-hand side of the normal equation given in Eq. 8 since $\frac{\partial r_{i}}{\partial\beta_{j}}=J_{ij}$.

<!-- chunk {"id": "body-0030", "role": "body", "section": "Estimation of Loss Function with Residual Sampling", "weight": 1.0} -->

Similarly, we can calculate the Hessian of the estimated loss function given in Eq. 13. To do so, we take the derivative of Eq. 14 with respect to parameter $\boldsymbol{\beta}_{k}$: When we apply the Gauss-Newton approximation to the Hessian matrix, the term with second derivative in Eq. 15 is ignored, and we are left with an estimation of $\mathbf{J^{\top}J}$.

<!-- chunk {"id": "body-0031", "role": "body", "section": "Estimation of Loss Function with Residual Sampling", "weight": 1.0} -->

Note that this approximation preserves the symmetry and positive semi-definiteness of $\mathbf{J^{\top}J}$, a property required for the convergence of the conjugate gradient algorithm.

<!-- chunk {"id": "body-0032", "role": "body", "section": "Estimation of Loss Function with Residual Sampling", "weight": 1.0} -->

In this work, we evaluated a range of candidate distributions $q$ and found that simple uniform distribution works well. For a comparison of alternative distributions and their respective results, please refer to the Supplementary.

<!-- chunk {"id": "body-0033", "role": "body", "section": "Estimation of Loss Function with Residual Sampling", "weight": 1.0} -->

In practice, sampling pixels over the image does not efficiently integrate with GPU programming and the backward pass of 3DGS. The reason is that an image is divided into $16\times 16$ tiles and when the pixels are selected randomly, some tiles get more samples than others, causing an unbalanced workload among thread blocks. Moreover, the random nature of the sampling does not allow fixed thread assignment per tile. Therefore, we use a stratified sampling strategy by distributing samples among tiles, and we perform sampling inside them. In other words, instead of sampling $N$ pixels from the entire image, we sample $N/\mathcal{T}$ pixels from each tile, where $\mathcal{T}$ is the total number of tiles in the image.

<!-- chunk {"id": "body-0034", "role": "body", "section": "Estimation of Loss Function with Residual Sampling", "weight": 1.0} -->

The sampling mechanism allows us to achieve $4\times$ speedup over the non-approximated LM optimizer, while maintaining similar performance, as shown in Tab. 3.

<!-- chunk {"id": "body-0035", "role": "body", "section": "Dynamic Learning Rate Scheduler", "weight": 1.0} -->

When second-order optimizers are applied to large-scale systems, numerical errors can occur, causing the solution vector $\Delta\boldsymbol{\beta}$ to overshoot the true loss landscape. To determine the optimal learning rate, line search algorithms or trust region methods are usually employed. However, these methods require additional forward or backward passes, increasing the computational overhead and slowing down the overall algorithm. Rather than relying on these methods, we estimate the learning rate by constraining the maximum update of color values. In 3DGS, the color parameters range between $\approx-1.77$ and $\approx 1.77$ due to the level $0$ spherical harmonic coefficient. This gives us a natural bound for the color parameters. We trust the update direction $\Delta\boldsymbol{\beta}$, as long as the resulting color change does not exceed 1. If the change surpasses this threshold, we scale $\Delta\boldsymbol{\beta}$ so that the maximum change remains 1. Notably, this scaling is applied uniformly across all parameters, regardless of their type (e.g., opacity, color, mean, scale, or rotation).

<!-- chunk {"id": "body-0036", "role": "body", "section": "Dynamic Learning Rate Scheduler", "weight": 1.0} -->

The effectiveness of this learning rate heuristic is demonstrated in Tab. 4, and examples of assigned learning rates are given in the Supplementary.

<!-- chunk {"id": "body-0037", "role": "body", "section": "Results", "weight": 1.0} -->

Datasets and Metrics. We conduct our main experiments on the synthetic NeRF and real-world Mip-NeRF360 indoor datasets. In the synthetic dataset, we position $10{,}000$ Gaussians at random locations with random colors inside of the cube encapsulating the object. In the real-world scenes, the Gaussians are initialized with structure-from-motion point clouds as in 3DGS. For all experiments, we use the default training and test splits. We report the test set performance based on structural similarity index (SSIM), learned perceptual image patch similarity score (LPIPS), and peak signal-to-noise ratio (PSNR).

<!-- chunk {"id": "body-0038", "role": "body", "section": "Results", "weight": 1.0} -->

Baselines. In the synthetic dataset, we compare our optimizer against Adam, RMSprop, and SGD with momentum, using their respective implementations in PyTorch. The gradients are computed using either the vanilla 3DGS or Taming 3DGS, which enhances the efficiency of the backward computation by storing the gradient state at every $32^{\text{nd}}$ splat.

<!-- chunk {"id": "body-0039", "role": "body", "section": "Results", "weight": 1.0} -->

In the real-world scenes, we compare against vanilla 3DGS and 3DGS-LM. For comparisons against 3DGS-LM, we contacted the authors^11^1At the time of our submission, the code for 3DGS-LM had not yet been released., who kindly provided PSNR scores, runtime, and average memory usage across several datasets. In addition, they provided results obtained without the Adam optimizer, which are denoted in the tables as 3DGS-LM (w/o Adam). First-order baselines are run for $10,000$ iterations, and we performed a hyperparameter search to find the best learning rates.

<!-- chunk {"id": "body-0040", "role": "body", "section": "Results", "weight": 1.0} -->

Implementation Details. We conducted synthetic dataset experiments on a NVIDIA Tesla A40 GPU and real-world experiments on a NVIDIA Tesla A100 GPU. Our method and the baselines optimize the mean squared error (MSE) loss. We set the sampled pixels per tile ($N$) to 32 in each experiment. We use a fixed damping parameter $\lambda$ of $0.1$ for the synthetic NeRF scenes and Mip-NeRF360 dataset. For the synthetic dataset, the batch size is fixed at $8$; for real-world datasets, it is initialized at $16$ and increased to $32$ after the 50th iteration. The maximum number of conjugate gradient iterations starts at $3$ for synthetic datasets and at $5$ for real-world datasets, rising to $8$ after the 50th iteration.

<!-- chunk {"id": "body-0041", "role": "body", "section": "Comparison", "weight": 1.0} -->

Next, we evaluate our method, named Levenberg-Marquardt with Residual Sampling (LM-RS), on synthetic NeRF scenes and present the results in Fig. 5. As shown, our second-order optimizer converges rapidly and achieves a substantial $\approx 5\times$ speedup over Adam. We observed that SGD with momentum consistently underperforms compared to other optimizers, despite our efforts at hyperparameter tuning. This highlights the importance of adaptive learning rates for optimizing 3DGS, a feature incorporated in all other evaluated optimizers. We also did not observe significant speed benefits from the optimizations of Taming 3DGS, which is likely due to a comparatively lower number of Gaussians in this setting that reduces the advantages of gradient caching.

<!-- chunk {"id": "body-0042", "role": "body", "section": "Comparison", "weight": 1.0} -->

In addition, we provide results in Mip-NeRF360 dataset in Tab. 1 and Fig. 4. Our method achieves $1.3\times$ speedup over Adam, $2\times$ over 3DGS-LM and $6\times$ speedup over 3DGS-LM (w/o Adam). Thanks to our matrix-free algorithm, we do not rely on the Adam optimizer at all, and our memory requirement is $3.5\times$ less than 3DGS-LM.

<!-- chunk {"id": "body-0043", "role": "body", "section": "Comparison", "weight": 1.0} -->

Please refer to the Supplementary for the results using SSIM loss, as well as quantitative results in Tanks & Temples and DeepBlending scenes.

<!-- chunk {"id": "body-0044", "role": "body", "section": "Ablation Studies", "weight": 1.0} -->

In this section, we ablate various design choices incorporated into our optimizer.

<!-- chunk {"id": "body-0045", "role": "body", "section": "Ablation Studies", "weight": 1.0} -->

View Sampling. We propose a view sampling approach in Sec. 4.3 to ensure that our optimizer can effectively estimate the local curvature of the loss landscape while still maintaining a relatively low batch size, through sampling of diverse views in a batch. In Tab. 2, we ablate our design choice, where we observe that our method shows improvements compared to random view sampling. We also report performance with reduced batch size, where we observe that the performance is significantly lower.

<!-- chunk {"id": "body-0046", "role": "body", "section": "Ablation Studies", "weight": 1.0} -->

Dynamic Learning Rate Scheduler. We compare our learning rate heuristic introduced in Sec. 4.5 against uniform learning rate, Armijo line search, and a grid search method in Tab. 4. The grid search method selects the learning rate at each iteration by identifying the value that results in the greatest reduction in the objective function. Although this method is stable, the learning rates obtained are too pessimistic, and it cannot reach the quality of our heuristic. Armijo line search improves the grid search method by picking the highest learning rate that results in sufficient reduction of the loss. While this approach has been successfully integrated as an improvement in deterministic second-order optimizers, our findings indicate that its effectiveness is limited in stochastic settings, such as ours, where optimization relies on multiple approximations. We also found that the uniform learning rate can diverge (LR=0.1) or behave suboptimally (LR=0.07) compared to our scheduler.

<!-- chunk {"id": "body-0047", "role": "body", "section": "Ablation Studies", "weight": 1.0} -->

Grid Line Search Armijo Line Search Our Scheduler (Sec. 4.5) Table 4: We show that our dynamic learning rate algorithm can converge faster, compared to uniform learning rate or search methods. The results are averaged across Mip-NeRF360 indoor scenes.

<!-- chunk {"id": "body-0048", "role": "body", "section": "Limitations", "weight": 1.5} -->

We use only a diagonally approximated SSIM loss for performance reasons, which may affect the convergence behavior. Future work could explore more efficient implementations enabling the use of full SSIM loss. In addition, our matrix-free implementation requires more intermediate vectors than Adam, leading $3\times$ higher memory usage.

<!-- chunk {"id": "body-0049", "role": "body", "section": "Conclusion", "weight": 1.5} -->

By leveraging the inherent sparsity of the Jacobian matrix and integrating a GPU-parallelized conjugate gradient solver, our method significantly reduces the computational overhead. Our novel view and pixel-wise sampling further enhance efficiency, enabling rapid convergence by decreasing the per-step overhead. Additionally, our dynamic learning rate scheduler eliminates the need for costly line search procedures, further accelerating training. Our approach achieves up to $5\times$ speedup over Adam, particularly excelling in scenarios with low number of Gaussians. Overall, our results highlight the potential of second-order methods in accelerating optimization for 3D Gaussian Splatting. We anticipate that future work will refine these techniques, particularly by incorporating additional loss terms without incurring runtime overhead, further advancing the efficiency and quality of Gaussian-based scene representations.
