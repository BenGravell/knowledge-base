<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

EDGS: Eliminating Densification for Efficient Convergence of 3DGS

Topics include 3D Gaussian splatting, Scene reconstruction, Dense initialization, Densification, Computer vision, Neural rendering.

<!-- chunk {"id": "summary-0002", "role": "summary", "section": "Summary", "weight": 2.0} -->

Replaces iterative Gaussian-splat densification with a dense one-step initialization derived from image correspondences. The paper targets the slow convergence and high-frequency artifacts of standard 3DGS training by starting optimization from a more complete geometric scaffold.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

3D Gaussian Splatting reconstructs scenes by starting from a sparse Structure-from-Motion initialization and refining under-reconstructed regions. This process is slow, as it requires multiple densification steps where Gaussians are repeatedly split and adjusted, following a lengthy optimization path. Moreover, this incremental approach often yields suboptimal renderings in high-frequency regions. We propose a fundamentally different approach: eliminate densification with a one-step approximation of scene geometry using triangulated pixels from dense image correspondences. This dense initialization allows us to estimate the rough geometry of the scene while preserving rich details from input RGB images, providing each Gaussian with well-informed color, scale, and position. As a result, we dramatically shorten the optimization path and remove the need for densification. Unlike methods that rely on sparse keypoints, our dense initialization ensures uniform detail across the scene, even in high-frequency regions where other methods struggle. Moreover, since all splats are initialized in parallel at the start of optimization, we remove the need to wait for densification to adjust new Gaussians.

<!-- chunk {"id": "abstract-0004", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

EDGS reaches LPIPS and SSIM performance of standard 3DGS significantly faster than existing efficiency-focused approaches. When trained further, it exceeds the reconstruction quality of state-of-the-art models aimed at maximizing fidelity. Our method is fully compatible with other acceleration techniques, making it a versatile and efficient solution that can be integrated with existing approaches.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

Reconstructing 3D scenes from collections of 2D images is a fundamental challenge in computer vision, with applications in virtual and augmented reality, robotics, and content creation. The goal is to obtain high-quality 3D representations efficiently, enabling real-time rendering while maintaining reconstruction fidelity. However, achieving balance between efficiency, speed, and quality requires a representation that is both expressive and computationally efficient. NeRF-based models control the trade-off between quality, computational cost, and representation capacity by designing network architectures and increasing the number of parameters. In contrast, point-based graphics represent surfaces using discrete primitives, such as meshes or point clouds, offering more direct control over complexity but often struggling with quality and scalability.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

Recently, 3D Gaussian Splatting (3DGS) has emerged as a powerful and efficient alternative for representing 3D scenes. It models scenes as a set of optimized 3D Gaussians, mathematical primitives defined by their position, color, and spread. The method begins with sparse initialization, typically derived from Structure-from-Motion (SfM), and progressively refines scene by adding splats to under-reconstructed regions. Through this densification process, 3DGS reaches high rendering quality while efficiently allocating computational resources.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

However, this process is suboptimal. The original 3DGS detects under-reconstructed regions using the gradient norm of the photometric loss. But this metric often fails in high-frequency regions and does not align well with human perception. A separate branch of papers has proposed pixel-error-driven formulations, gradient calculation improvements, and even treating 3DGS as Markov Chain Monte Carlo samples. Despite these efforts, accurately capturing fine details, particularly in high-frequency regions, remains a challenge, as illustrated in Fig. 1. Furthermore, while each densification step is computationally efficient, the overall process is slow. It requires many update steps, as Gaussians must iteratively adjust their parameters before the model determines that additional splats are necessary. This results in a long optimization path, where individual Gaussians undergo multiple refinements before reaching their final states (see Sec. 4.5, Fig. 2 and Fig. 4). Densification delays convergence, as it takes many iterations for the model to identify areas requiring higher reconstruction fidelity. These challenges raise an important question: can we bypass densification entirely?

<!-- chunk {"id": "body-0008", "role": "body", "section": "Introduction", "weight": 1.5} -->

In this paper, we propose a direct initialization strategy that eliminates the need for incremental densification used in the original 3DGS method. Rather than waiting for the model to gradually fill in missing details, we precompute a dense set of 3D Gaussians by triangulating dense 2D correspondences across multiple input views. Knowing the viewing rays for each correspondence pixel and the camera poses, we recover 3D positions of Gaussians by triangulating matched pixels between image pairs. This allows us to assign each Gaussian well-informed initial parameters, such as position, color, and scale, from the start. To summarize, we replace the slow iterative densification process of the scene with a dense initialization. As a result, each Gaussian is immediately supervised by rich per-pixel photometric signal, allowing for efficient optimization of the entire scene.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Introduction", "weight": 1.5} -->

Although this initialization is noisy (see Fig. 1), we show that it remains robust and leads to faster convergence. Our experiments, quantitatively and qualitatively, confirm that EDGS yields higher reconstruction quality, shorter training time, fewer Gaussians, and eliminates the need for densification. Our contributions can be summarized as follows: We introduce a novel dense initialization for 3D Gaussian Splatting, based on the sampling distribution of triangulated multi-view correspondences, which effectively replaces the traditional incremental refinement process.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Introduction", "weight": 1.5} -->

EDGS achieves faster convergence and higher reconstruction quality than prior 3DGS methods. We further analyze how the proposed initialization affects the optimization trajectories of individual Gaussians.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Introduction", "weight": 1.5} -->

Our initialization improves reconstruction without modifying the optimization algorithm, making it compatible with other 3DGS methods. This makes it a complementary component that can be seamlessly integrated with adaptive densification strategies to further enhance performance.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Densification", "weight": 1.0} -->

Several studies suggest that using an effective strategy for splat densification can significantly enhance performance. RevDev introduced a per-pixel error function as a criterion for densification. AbsGS addressed the issue of gradient collision during the detection of under-reconstructed regions. MiniSplatting proposed a densification approach that incorporates both screen-space and world-space information. ScaffoldGS introduced anchor points and a growth algorithm to optimize Gaussians distribution. Meanwhile, 3DGS-MCMC reformulated densification as a Markov Chain Monte Carlo sampling process, enabling an efficient Gaussian distribution across scene. In contrast, we propose an improved initialization method that avoids densification altogether, eliminating the need to detect under-reconstructed regions.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Efficiency", "weight": 1.0} -->

A number of recent works aim to enhance the efficiency of 3DGS. One approach leverages pre-trained neural networks as priors to guide reconstruction. This data-driven strategy enables rapid reconstruction with high quality, particularly in sparse-view scenarios. We focus on dense-view reconstruction. Another area of research targets the optimization of 3DGS by refining the differentiable rasterizer or improving the framework itself. Separately, 3DGS-LM proposes a Levenberg-Marquardt optimizer that integrates with the 3DGS rasterizer and can be adapted to other rasterization methods. Our approach instead focuses on improving the initialization process, which is compatible with these optimizations.

<!-- chunk {"id": "body-0014", "role": "body", "section": "Initialization", "weight": 1.0} -->

Recent works, such as RAIN-GS and 3DGS-MCMC, shows that random initialization can match the performance of 3DGS. In contrast, RadSplat initializes from points extracted using pretrained NeRFs to improve quality, though it requires 9 hours of training. EDGS departs from both approaches by emphasizing efficiency while outperforming quality-focused methods.

<!-- chunk {"id": "body-0015", "role": "body", "section": "Method", "weight": 1.0} -->

Our goal is to initialize a dense set of Gaussian splats (Sec. 3.1). Instead of incrementally adding information via photometric loss, we leverage all available 2D image information from the start (Sec. 3.2). We first triangulate dense pixel correspondences into 3D space (Sec. 3.3). Then, we aggregate semantic confidence and geometric consistency across neighboring views to build a sampling distribution $\mathbf{p}^{i}$ for each reference image (Sec. 3.4), from which splats are sampled. Finally, we initialize spherical harmonics for the sampled splats (Sec. 3.5).

<!-- chunk {"id": "body-0016", "role": "body", "section": "Extract information from 2D prior", "weight": 1.0} -->

We begin by selecting a reference image $I^{i}$ from the training set. For each $I^{i}$, we identify neighboring images $\mathbb{I}_{i}=\{I^{1},\dots,I^{j}|j\in[0,J]\}$ that have maximal overlap with $I^{i}$, based on camera parameters and spatial proximity. We measure proximity between camera matrices using the Frobenius norm.

<!-- chunk {"id": "body-0017", "role": "body", "section": "Sampling distribution", "weight": 1.0} -->

Given triangulated correspondences between a reference view $I^{i}$ and a neighboring view $I^{j}$, directly using all matches for multi-view reconstruction is computationally infeasible. We therefore define a sampling distribution $\mathbf{p}^{i}$ to select geometrically consistent and semantically reliable correspondences. For each triangulated 3D point $\bm{g}^{x}_{k}$, we compute its reprojection error in the reference image $I^{i}$: where $\pi(\bm{P},\cdot)$ denotes projection with camera matrix $\bm{P}$; $\varepsilon_{k}^{j}$ is defined analogously. Points with high reprojection $\varepsilon_{k}^{ij}:=\text{max}(\varepsilon_{k}^{i},\varepsilon_{k}^{j})$ error are likely inconsistent across views and should be avoided.

<!-- chunk {"id": "body-0018", "role": "body", "section": "Sampling distribution", "weight": 1.0} -->

We convert reprojection errors and correspondence confidences $\mathbf{c}^{ij}(u^{i}_{k},v^{i}_{k})$ over some threshold $\tau_{\text{corr}}$ into uniform sampling distributions: Finally, we combine the geometry-based and confidence-based probabilities via element-wise multiplication for all nearest neighbors $\mathbb{I}_{i}$: which prioritizes points with the strongest geometric and correspondence consistency across neighbors.

<!-- chunk {"id": "body-0019", "role": "body", "section": "Sampling distribution", "weight": 1.0} -->

We then form the global sampling distribution by aggregating the per-reference $I^{i}$ probabilities $\mathbf{p}(k)\propto\bigcup_{i}\mathbf{p}^{i}_{k}$, effectively selecting correspondences that remain consistent across multiple reference views.

<!-- chunk {"id": "body-0020", "role": "body", "section": "Spherical harmonics", "weight": 1.0} -->

After sampling Gaussians from $\mathbf{p}^{i}$, we assign each splat an initial color from the reference image $I^{i}$ at pixel coordinates $(u_{k}^{i},v_{k}^{i})$. For each splat, we collect $n$ RGB observations $\mathbf{O}_{k}\in\mathbb{R}^{n\times 3}$ from view directions $\mathbf{v}_{1},\dots,\mathbf{v}_{n}\in\mathbb{R}^{3}$ and estimate the rest of its spherical harmonics (SH) coefficients. We build a matrix $\mathbf{Y}_{k}\in\mathbb{R}^{n\times 16}$, where each row contains the 16 real SH basis functions (up to degree $l=3$) evaluated at direction $\mathbf{v}_{i}$.

<!-- chunk {"id": "body-0021", "role": "body", "section": "Spherical harmonics", "weight": 1.0} -->

The SH coefficients $\hat{\mathbf{H}}_{k}\in\mathbb{R}^{16\times 3}$ are obtained by solving the system of linear equations: When $n<16$, we use the Moore--Penrose pseudoinverse, ensuring stable estimation under limited observations.

<!-- chunk {"id": "body-0022", "role": "body", "section": "Spherical harmonics", "weight": 1.0} -->

Finally, these initialized Gaussians undergo standard photometric loss optimization to refine their parameters and achieve precise 3D reconstructions.

<!-- chunk {"id": "body-0023", "role": "body", "section": "Experiments", "weight": 1.0} -->

Mip-NeRF 360 Densif. free SSIM ↑ PSNR ↑ LPIPS ↓ Train time #G gsplat ✗ 0.818 27.51 0.215 18 m 3.1 3DGS+3DGS-LM † ✗ 0.813 27.39 0.221 16 m 2.8⋆ EAGLES ✗ 0.809 27.20 0.232 16 m 1.3 Taming 3DGS ✗ 0.820 27.71 0.207 14 m 3.2 MiniSplatting ✗ 0.820 27.25 0.217 12 m 0.5 EDGS + 3DGS 10K ✓ 0.834 27.54 0.154 12 m 2.1 EDGS + 3DGS 5K ✓ 0.825 26.88 0.166 8 m 2.6 † From original paper. ⋆ Assumed same as 3DGS due to identical densification. Table 2: Quantitative evaluation under early-stopping settings on Mip-NeRF 360. When trained for a comparable duration (EDGS 10K), our method outperforms other efficient approaches.

<!-- chunk {"id": "body-0024", "role": "body", "section": "Experiments", "weight": 1.0} -->

Even with reduced training time (EDGS 5K), it outperforms all competing methods on two of the three standard metrics.

<!-- chunk {"id": "body-0025", "role": "body", "section": "Datasets and Metrics", "weight": 1.0} -->

We evaluate on Mip-NeRF360, Tanks&Temples, and Deep Blending datasets. Following standard protocol, we use 9, 2, and 2 scenes, respectively. Evaluation metrics include PSNR, SSIM, and LPIPS, along with training time and final Gaussians count. All experiments were run on NVIDIA A100 GPUs, with competing methods re-evaluated on the same hardware for fairness. Runtimes for EDGS include initialization (see Appendix A for time break-down).

<!-- chunk {"id": "body-0026", "role": "body", "section": "Baselines", "weight": 1.0} -->

For ray‑based methods, we include Plenoxels, Mip‑NeRF360, and Instant‑NGP. As our method is based on 3DGS, we also compare with the original 3DGS. We retrain it (denoted as 3DGS\*), as this resulted in better performance than the originally reported scores. We also include high-quality baselines AbsGS, Mip-Splatting, 3DGS-MCMC and Scaffold-GS. Since our method emphasizes the initialization stage, we include RAIN-GS. Notably, the mean values for Scaffold-GS and 3DGS-MCMC changed significantly, as they originally reported results for only 7 of the 9 Mip-NeRF360 scenes. Additionally, we report results for Scaffold-GS trained with the same resolution settings as 3DGS, which were not included in the original paper. We compare these models against our model with full $30000$-step convergence, pruning enabled, densification disabled denoted as EDGS + 3DGS in Tab. 1.

<!-- chunk {"id": "body-0027", "role": "body", "section": "Baselines", "weight": 1.0} -->

To evaluate speed and efficiency, we compare our model without densification, stopped at $5000$ and $10000$ steps (EDGS + 3DGS 5K and 10K) in Tab. 2) against the fastest competitive methods: EAGLES, 3DGS-LM, Taming 3DGS, gsplat, and MiniSplatting.

<!-- chunk {"id": "body-0028", "role": "body", "section": "Quantitative Evaluations", "weight": 1.0} -->

We evaluate EDGS across three aspects: reconstruction quality, training efficiency, and compatibility with existing methods. As shown in Tab. 1, our model achieves the best or second-best results across all three metrics, while maintaining comparable training time and Gaussian count, all without any densification. When trained for only 5K steps, EDGS matches the performance of efficiency-focused methods while converging faster (Tab. 2). Moreover, EDGS can be seamlessly integrated with existing Adaptive Density Control (ADC) methods by using it as an initialization. As shown in Tab. 3, this integration consistently improves reconstruction quality across all evaluated ADC variants on the Mip-NeRF360 dataset. Since EDGS itself does not perform densification, we intentionally initialize with fewer Gaussians in this experiment to allow ADC methods to further refine the scene. All ADC variants use identical initialization parameters for fairness. Despite the additional densification, total training time remains comparable or lower, as fewer Gaussians are introduced overall and less computation is spent on densification.

<!-- chunk {"id": "body-0029", "role": "body", "section": "Quantitative Evaluations", "weight": 1.0} -->

Finally, unlike prior 3DGS approaches that rely heavily on densification and degrade significantly without it, EDGS remains stable and achieves strong reconstruction quality even without it, see Tab. 4.

<!-- chunk {"id": "body-0030", "role": "body", "section": "Qualitative Evaluations", "weight": 1.0} -->

In Fig. 3, our approach shows clear improvements over other methods across all datasets. The examples show that EDGS excels not only in high-frequency regions, such as small stones near railroad tracks, grass, or concrete textures, but also in capturing fine details like flower stems (first row) and distant elements like roads (third row). Other models often fail to accurately reconstruct these details, either blurring them or introducing high-frequency artifacts. EDGS dense initialization ensures a Gaussian splat is placed at every meaningful location, enabling precise and detailed reconstruction. We also provide crops for our model, stopped at 3000 steps, showing that we achieve comparable perceptual quality much faster than other methods.

<!-- chunk {"id": "body-0031", "role": "body", "section": "Matching Algorithm Comparison", "weight": 1.0} -->

We evaluate image matching methods $\mathcal{M}$ for initializing splats. See Tab. 5 for a comparison on the Mip-NeRF360 dataset. Throughout this paper, we use RoMa as our matching algorithm, but we also experiment with LoFTR, DKM, and RAFT. All methods except RAFT achieve comparable performance; RAFT struggles due to its primary design for optical flow between consecutive video frames, where viewpoint differences are minimal.

<!-- chunk {"id": "body-0032", "role": "body", "section": "Gaussian Motion and Convergence", "weight": 1.0} -->

We study the parameters dynamics of each Gaussian during optimization. Fig. 4 presents the start-to-finish displacement and full motion trajectory length. Namely, we analyze how Gaussian coordinates and color parameters evolve during the optimization process by measuring two key distributions. Let $\bm{g}_{i}(t)$ denote the state of Gaussian $\bm{g}_{i}$ at optimization step $t$ for $i\in\{1,\dots,N\}$. The first distribution captures the displacement, defined as: and second measures the full trajectory length: where $T$ denotes the number of optimization steps. EDGS significantly reduces the final coordinate displacement, as Gaussians are initialized closer to surfaces, requiring fewer adjustments. Compared to 3DGS, our model reduces the coordinate displacement by 50 times and the coordinate trajectory length by 30 times. The color trajectory length also decreases, though less dramatically, by approximately a factor of two, as small oscillations remain along the trajectory. Visualizations of Gaussian motion are provided in Appendix D.

<!-- chunk {"id": "body-0033", "role": "body", "section": "Gaussian Motion and Convergence", "weight": 1.0} -->

Method pcorrij pprojij SH Init. PSNR↑ SSIM↑ LPIPS↓ EDGS (full) ✓ ✓ ✓ 28.02 0.839 0.141 w/o SH init. ✓ ✓ ✗ 27.80 0.840 0.175 w/o pprojij ✓ ✗ ✗ 27.72 0.830 0.179 w/o pcorrij ✗ ✓ ✗ 27.55 0.829 0.197 baseline ✗ ✗ ✗ 27.43 0.822 0.202 Table 6: Ablation study of EDGS components. Combining both sampling distributions with spherical harmonics initialization(SH Init) yields the best reconstruction quality.

<!-- chunk {"id": "body-0034", "role": "body", "section": "Sampling distribution", "weight": 1.0} -->

As defined in Eq. 11, the sampling distribution $\mathbf{p}^{i}$ combines two terms: the correspondence-based distribution $\mathbf{p}^{ij}{\text{corr}}$, which reflects matcher confidence, and the geometry-based distribution $\mathbf{p}^{ij}_{\text{proj}}$, which penalizes re-projection errors. These components complement each other: confidence alone captures semantic reliability but cannot enforce geometric consistency, whereas the re-projection term removes mismatched or unstable correspondences. To maintain spatial coverage, we perform uniform sampling over confidence-thresholded matches $\mathbf{c}^{ij}$, preventing bias toward high-confidence but spatially clustered regions. The combination of both terms yields a balanced, geometry-aware initialization that consistently outperforms using either component in isolation (Tab. 6).

<!-- chunk {"id": "body-0035", "role": "body", "section": "Sampling distribution", "weight": 1.0} -->

To assess the importance of the re-projection term, we replace the right-hand side of Eq. 11 with $\max_{j\in\mathbb{I}i}\mathbf{p}^{ij}_{\text{corr}}(k)$. Conversely, removing $\mathbf{p}^{ij}_{\text{corr}}$ entirely is infeasible as we still require match locations, but we can sample points proportionally to confidence by setting $\mathbf{p}^{ij}_{\text{corr}}\propto\mathbf{c}^{ij}$. As shown in Tab. 6, both modifications degrade performance, with the confidence-only variant having the strongest negative effect. This is expected: sampling in proportion to $\mathbf{c}^{ij}$ breaks uniform spatial coverage and concentrates splats around high-confidence edges or boundaries, leading to poorer initialization. Disabling both geometric and confidence cues further reduces accuracy and produces visibly more floaters.

<!-- chunk {"id": "body-0036", "role": "body", "section": "Sampling distribution", "weight": 1.0} -->

In Fig. 5, we visualize a set of keypoints extracted from a single pair of images. The results highlight that we need to sample keypoints from the image more uniformly, rather than focusing solely on keypoints with high confidence.

<!-- chunk {"id": "body-0037", "role": "body", "section": "Hyperparameter Sensitivity", "weight": 1.0} -->

We analyze how key hyperparameters, namely the number of reference views, the number of sampled correspondences per view, and the number of nearest neighbor views used for matching, affect reconstruction quality. As shown in Fig. 6, increasing any of these parameters improves results until a saturation point, after which gains become marginal. Following this behavior, we use up to $180$ reference views (limited by scene size), match each with $2$ nearest neighbors to obtain $\mathbf{p}^{i}$, from which we sample $20\text{k}$ correspondences. See Appendix C for details.

<!-- chunk {"id": "body-0038", "role": "body", "section": "Spherical harmonics", "weight": 1.0} -->

We further evaluate the effect of EDGS spherical harmonics initialization in Tab. 6. This initialization accelerates convergence for challenging Gaussians and improves the modeling of view-dependent effects, resulting in significantly lower LPIPS scores. We also observe that the benefits are more pronounced for indoor scenes, where complex lighting and reflections pose greater challenges, compared to outdoor environments.

<!-- chunk {"id": "body-0039", "role": "body", "section": "Robustness to noise", "weight": 1.0} -->

EDGS exhibits strong resilience to imperfections in the initial correspondences, which may arise from triangulation inaccuracies or suboptimal matches produced by $\mathcal{M}$. To quantitatively assess this robustness, we perturb the initialized Gaussian parameters with additive Gaussian noise $\epsilon\sim\mathcal{N}(0,\sigma)$ applied independently to either spatial coordinates or color values. We then evaluate reconstruction quality across varying noise levels $\sigma$. Formally, noise $\epsilon$ is injected into the color parameters $\bm{g}_{i}^{c}$ and coordinate parameters $\bm{g}_{i}^{x}$ of the initialized Gaussians. This design isolates the influence of each parameter type on convergence.

<!-- chunk {"id": "body-0040", "role": "body", "section": "Robustness to noise", "weight": 1.0} -->

As shown in Fig. 7, increasing coordinate or color noise leads to gradual degradation in PSNR and LPIPS. Remarkably, EDGS maintains substantially higher robustness to color perturbations than to spatial ones, supporting our claim that the method's primary advantage lies in reducing unnecessary Gaussian movement during optimization. Even under moderate coordinate noise, overall reconstruction quality remains stable, demonstrating the inherent regularization of our initialization. Notably, our method remains stable even with small amounts of added noise, likely because the initialization itself is already inherently noisy, as shown in Fig. A3. All experiments are conducted on the Mip-NeRF360 dataset. In Fig. A2, we visualized initialization for scene garden, which was noised with different scales for both coordinates (first row) and colors (second row).

<!-- chunk {"id": "body-0041", "role": "body", "section": "Different Initializations", "weight": 1.0} -->

Method Init Densif. PSNR↑ SSIM↑ LPIPS↓ type free 3DGS Random ✗ 22.19 0.704 0.313 COLMAP ✗ 27.49 0.816 0.215 Depth ✓ 26.99 0.810 0.202 Depth ✗ 27.18 0.819 0.197 VGGT-X VGGT ✗ 26.40 0.782 0.177 EDGS EDGS ✓ 28.02 0.839 0.141 Table 7: Qualitative comparison for different initialization strategies and densification. Checkmarks in the Densif. free column indicate models not using 3DGS densification. EDGS consistently achieves superior results across all metrics.

<!-- chunk {"id": "body-0042", "role": "body", "section": "Different Initializations", "weight": 1.0} -->

We study now different ways to initialize Gaussians for 3DGS. The first one is random noise, but this setup fails to achieve the performance of SFM-based initialization, further highlighting the critical role of proper initialization. Beyond matching-based initialization, we evaluate a depth-based strategy using DepthFM. For each reference view, we uniformly sample 20,000 pixels and backproject them to 3D using the predicted depth. However, monocular depth estimates often suffer from scale inconsistencies across views, leading to lower reconstruction quality. While DepthFM combined with densification outperforms the baseline 3DGS, it still falls short of our matching-based approach. We also compare with a neural initialization method that jointly estimates Gaussian positions and camera parameters; however, it does not reach the same reconstruction quality as EDGS. See Tab. 7 for quantitative comparison on the Mip-NeRF360. We additionally include, in Appendix E, further simpler initialization baselines.

<!-- chunk {"id": "body-0043", "role": "body", "section": "Extreme Viewpoint Rendering", "weight": 1.0} -->

EDGS effectively handles extreme viewpoint variations, outperforming the baseline when rendering from camera angles far outside the training set. As shown in Fig. 8, our dense initialization prevents the need for stretching small Gaussians to compensate for pixel loss at a distance, resulting in a more stable and accurate reconstruction. As visualized for garden scene from the Mip-NeRF360 dataset, our method avoids large Gaussians and exhibits less noise compared to the competing approach.

<!-- chunk {"id": "body-0044", "role": "body", "section": "Additional experiments and details", "weight": 1.0} -->

Implementation details are provided in Appendix A, with extra visualizations in Appendix F. For the table of notation see Appendix H. We also evaluate our method in a sparse view setting in Appendix B and show applicability of our approach to this setting as well.

<!-- chunk {"id": "body-0045", "role": "body", "section": "Conclusion", "weight": 1.5} -->

We introduce a new initialization strategy for 3D Gaussian Splatting that removes the need for iterative densification. The approach relies on carefully sampling 2D correspondences that are both geometrically consistent and provide uniform, dense coverage of the scene.

<!-- chunk {"id": "body-0046", "role": "body", "section": "Conclusion", "weight": 1.5} -->

Our method reaches state-of-the-art performance without any densification and matches efficiency-oriented methods with substantially fewer optimization steps. Moreover, EDGS functions as a plug-and-play initialization for adaptive density control techniques, improving reconstruction quality without increasing training time or Gaussian count, making it a practical and broadly applicable enhancement for 3D reconstruction pipelines.
