## Introduction

A recent body of research has capitalized on implicit, coordinate-based neural networks as the 3D representation to optimize 3D volumes from calibrated 2D image supervision. In particular, Neural Radiance Fields (NeRF) demonstrated photorealistic novel viewpoint rendering, capturing scene geometry as well as view-dependent effects. This impressive quality, however, requires extensive computation time for both training and rendering, with training lasting more than a day and rendering requiring 30 seconds per frame, on a single GPU. Multiple subsequent papers reduced this computational cost, particularly for rendering, but single GPU training still requires multiple hours, a bottleneck that limits the practical application of photorealistic volumetric reconstruction.

Figure 1: Plenoxel: Plenoptic Volume Elements for fast optimization of radiance fields. We show that direct optimization of a fully explicit 3D model can match the rendering quality of modern neural based approaches such as NeRF while optimizing over two orders of magnitude faster.

In this paper, we show that we can train a radiance field from scratch, without neural networks, while maintaining NeRF quality and reducing optimization time by two orders of magnitude. We provide a custom CUDA implementation that capitalizes on the model simplicity to achieve substantial speedups. Our typical optimization time on a single Titan RTX GPU is 11 minutes on bounded scenes (compared to roughly 1 day for NeRF, more than a $100 \times$ speedup) and 27 minutes on unbounded scenes (compared to roughly 4 days for NeRF++, again more than a $100 \times$ speedup). Although our implementation is not optimized for fast rendering, we can render novel viewpoints at interactive rates $15$ fps. If faster rendering is desired, our optimized Plenoxel model can be converted into a PlenOctree.

Specifically, we propose an explicit volumetric representation, based on a view-dependent sparse voxel grid without any neural networks. Our model can render photorealistic novel viewpoints and be optimized end-to-end from calibrated 2D photographs, using the differentiable rendering loss on training views as well as a total variation regularizer. We call our model Plenoxel for plenoptic volume elements, as it consists of a sparse voxel grid in which each voxel stores opacity and spherical harmonic coefficients. These coefficients are interpolated to model the full plenoptic function continuously in space. To achieve high resolution on a single GPU, we prune empty voxels and follow a coarse to fine optimization strategy. Although our core model is a bounded voxel grid, we can model unbounded scenes by using normalized device coordinates (for forward-facing scenes) or by surrounding our grid with multisphere images to encode the background (for $360^{\circ}$ scenes).

Our method reveals that photorealistic volumetric reconstruction can be approached using standard tools from inverse problems: a data representation, a forward model, a regularization function, and an optimizer. Our method shows that each of these components can be simple and state of the art results can still be achieved. Our experiments suggest the key element of Neural Radiance Fields is not the neural network but the differentiable volumetric renderer.

## Related Work

### Classical Volume Reconstruction

We begin with a brief overview of classical methods for volume reconstruction, focusing on those which find application in our work. In particular, the most common classical methods for volume rendering are voxel grids and multi-plane images (MPIs). Voxel grids are capable of representing arbitrary topologies but can be memory limited at high resolution. One approach for reducing the memory requirement for voxel grids is to encode hierarchical structure, for instance using octrees (see for a survey); we use an even simpler sparse array structure. Using these grid-based representations combined with some form of interpolation produces a continuous representation that can be arbitrarily resized using standard signal processing methods (see for reference). This combination of sparsity and interpolation enables even a simple grid-based model to represent 3D scenes at high resolution without prohibitive memory requirements. We combine this classical sampling and interpolation paradigm with the forward volume rendering formula introduced by Max (based on work from Kajiya and Von Herzen and used in NeRF) to directly optimize a 3D model from indirect 2D observations. We further extend these classical approaches by modeling view dependence, which we accomplish by optimizing spherical harmonic coefficients for each color channel at each voxel. Spherical harmonics are a standard basis for functions over the sphere, and have been used previously to represent view dependence.

### Neural Volume Reconstruction

Recently, dramatic improvements in neural volume reconstruction have renewed interest in this direction. Neural implicit representations were first used to model occupancy and signed distance to an object's surface, and perform novel view synthesis from 3D point clouds. Several papers extended this idea of neural implicit 3D modeling to model a scene using only calibrated 2D image supervision via a differentiable volume rendering formulation.

NeRF in particular uses a differentiable volume rendering formula to train a coordinate-based multilayer perceptron (MLP) to directly predict color and opacity from 3D position and 2D viewing direction. NeRF produces impressive results but requires several days for full training, and about half an minute to render a full image, because every rendered pixel requires evaluating the coordinate-based MLP at hundreds of sample locations along the corresponding ray. Many papers have since extended the capabilities of NeRF, including modeling the background in $360^{\circ}$ views and incorporating anti-aliasing for multiscale rendering. We extend our Plenoxel method to unbounded $360^{\circ}$ scenes using a background model inspired by NeRF++.

Of these methods, Neural Volumes is the most similar to ours in that it uses a voxel grid with interpolation, but optimizes this grid through a convolutional neural network and applies a learned warping function to improve the effective resolution (of a $128^{3}$ grid). We show that the voxel grid can be optimized directly and high resolution can be achieved by pruning and coarse to fine optimization, without any neural networks or warping functions.

Figure 2: Overview of our sparse Plenoxel model. Given a set of images of an object or scene, we reconstruct a (a) sparse voxel (“Plenoxel”) grid with density and spherical harmonic coefficients at each voxel. To render a ray, we (b) compute the color and opacity of each sample point via trilinear interpolation of the neighboring voxel coefficients. We integrate the color and opacity of these samples using (c) differentiable volume rendering, following the recent success of NeRF. The voxel coefficients can then be (d) optimized using the standard MSE reconstruction loss relative to the training images, along with a total variation regularizer.

### Accelerating NeRF

In light of the substantial computational requirements of NeRF for both training and rendering, many recent papers have proposed methods to improve efficiency, particularly for rendering. Among these methods are many that achieve speedup by subdividing the 3D volume into regions that can be processed more efficiently. Other speedup approaches have focused on a range of computational and pre- or post-processing methods to remove bottlenecks in the original NeRF formulation. JAXNeRF, a JAX reimplementation of NeRF offers a speedup for both training and rendering via parallelization across many GPUs or TPUs. AutoInt restructures the coordinate-based MLP to compute ray integrals exactly, for more than $10 \times$ faster rendering with a small loss in quality. Learned Initializations employs meta-learning on many scenes to start from a better MLP initialization, for both $> 10 \times$ faster training and better priors when per-scene data is limited. Other methods achieve speedup by predicting a surface or sampling near the surface, reducing the number of samples necessary for rendering each ray.

Another approach is to pretrain a NeRF (or similar model) and then extract it into a different data structure that can support fast inference. In particular, PlenOctrees extracts a NeRF variant into a sparse voxel grid in which each voxel represents view-dependent color using spherical harmonic coefficients. Because the extracted PlenOctree can be further optimized, this method can speed up training by roughly $3 \times$, and because it uses an efficient GPU octree implementation without any MLP evaluations, it achieves $> 3000 \times$ rendering speedup. Our method extends PlenOctrees to perform end-to-end optimization of a sparse voxel representation with spherical harmonics, offering much faster training (two orders of magnitude speedup compared to NeRF). Our Plenoxel model is a generalization of PlenOctrees to support sparse plenoptic voxel grids of arbitrary resolution (not necessary powers of two) with the ability to perform trilinear interpolation, which is easier to implement with this sparse voxel structure.

## Method

Our model is a sparse voxel grid in which each occupied voxel corner stores a scalar opacity $\sigma$ and a vector of spherical harmonic (SH) coefficients for each color channel. From here on we refer to this representation as Plenoxel. The opacity and color at an arbitrary position and viewing direction are determined by trilinearly interpolating the values stored at the neighboring voxels and evaluating the spherical harmonics at the appropriate viewing direction. Given a set of calibrated images, we optimize our model directly using the rendering loss on training rays. Our model is illustrated in Fig. 2 and described in detail below.

### Volume Rendering

We use the same differentiable model for volume rendering as in NeRF, where the color of a ray is approximated by integrating over samples taken along the ray:

$T_{i}$ represents how much light is transmitted through ray r to sample $i$ (versus contributed by preceding samples), $\left( {1 - {\exp{({- {\sigma_{i}\delta_{i}}})}}} \right)$ denotes how much light is contributed by sample $i$, $\sigma_{i}$ denotes the opacity of sample $i$, and $\text{c}_{i}$ denotes the color of sample $i$, with distance $\delta_{i}$ to the next sample. Although this formula is not exact (it assumes single-scattering and constant values between samples ), it is differentiable and enables updating the 3D model based on the error of each training ray.

### Voxel Grid with Spherical Harmonics

Similar to PlenOctrees, we use a sparse voxel grid for our geometry model. However, for simplicity and ease of implementing trilinear interpolation, we do not use an octree for our data structure. Instead, we store a dense 3D index array with pointers into a separate data array containing values for occupied voxels only. Like PlenOctrees, each occupied voxel stores a scalar opacity $\sigma$ and a vector of spherical harmonic coefficients for each color channel. Spherical harmonics form an orthogonal basis for functions defined over the sphere, with low degree harmonics encoding smooth (more Lambertian) changes in color and higher degree harmonics encoding higher-frequency (more specular) effects. The color of a sample $\text{c}_{i}$ is simply the sum of these harmonic basis functions for each color channel, weighted by the corresponding optimized coefficients and evaluated at the appropriate viewing direction. We use spherical harmonics of degree 2, which requires 9 coefficients per color channel for a total of 27 harmonic coefficients per voxel. We use degree 2 harmonics because PlenOctrees found that higher order harmonics confer only minimal benefit.

Our Plenoxel grid uses trilinear interpolation to define a continuous plenoptic function throughout the volume. This is in contrast to PlenOctrees, which assumes that the opacity and spherical harmonic coefficients remain constant inside each voxel. This difference turns out to be an important factor in successfully optimizing the volume, as we discuss below. All coefficients (for opacity and spherical harmonics) are optimized directly, without any special initialization or pretraining with a neural network.

### Interpolation

The opacity and color at each sample point along each ray are computed by trilinear interpolation of opacity and harmonic coefficients stored at the nearest 8 voxels. We find that trilinear interpolation significantly outperforms a simpler nearest neighbor interpolation; an ablation is presented in Tab. 1. The benefits of interpolation are twofold: interpolation increases the effective resolution by representing sub-voxel variations in color and opacity, and interpolation produces a continuous function approximation that is critical for successful optimization. Both of these effects are evident in Tab. 1: doubling the resolution of a nearest-neighbor-interpolating Plenoxel closes much of the gap between nearest neighbor and trilinear interpolation at a fixed resolution, yet some gap remains due to the difficulty of optimizing a discontinuous model. Indeed, we find that trilinear interpolation is more stable with respect to variations in learning rate compared to nearest neighbor interpolation (we tuned the learning rates separately for each interpolation method in Tab. 1, to provide close to the best number possible for each setup).

Table 1: Ablation over interpolation method. Results are averaged over the 8 NeRF synthetic scenes. We find that trilinear interpolation provides dual benefits of improving effective resolution and improving optimization, such that trilinear interpolation at resolution 1283 outperforms nearest neighbor interpolation at 2563.

### Coarse to Fine

We achieve high resolution via a coarse-to-fine strategy that begins with a dense grid at lower resolution, optimizes, prunes unnecessary voxels, refines the remaining voxels by subdividing each in half in each dimension, and continues optimizing. For example, in the synthetic case, we begin with $256^{3}$ resolution and upsample to $512^{3}$. We use trilinear interpolation to initialize the grid values after each voxel subdivision step. In fact, we can resize between arbitrary resolutions using trilinear interpolation. Voxel pruning is performed using the method from PlenOctrees, which applies a threshold to the maximum weight $T_{i}{({1 - {\exp{({- {\sigma_{i}\delta_{i}}})}}})}$ of each voxel over all training rays (or, alternatively, to the density value in each voxel). Due to trilinear interpolation, naively pruning can adversely impact the the color and density near surfaces since values at these points interpolate with the voxels in the immediate exterior. To solve this issue, we perform a dilation operation so that a voxel is only pruned if both itself and its neighbors are deemed unoccupied.

### Optimization

We optimize voxel opacities and spherical harmonic coefficients with respect to the mean squared error (MSE) over rendered pixel colors, with total variation (TV) regularization. Specifically, our base loss function is:

Where the MSE reconstruction loss $\mathcal{L}_{recon}$ and the total variation regularizer $\mathcal{L}_{TV}$ are:

with $\Delta_{x}^{2}{(\mathbf{v},d)}$ shorthand for the squared difference between the $d$th value in voxel $\mathbf{v}:={(i,j,k)}$ and the $d$th value in voxel $({i + 1},j,k)$ normalized by the resolution, and analogously for $\Delta_{y}^{2}{(\mathbf{v},d)}$ and $\Delta_{z}^{2}{(\mathbf{v},d)}$. Note in practice we use different weights for SH coefficients and $\sigma$ values. These weights are fixed for each scene type (bounded, forward-facing, and $360^{\circ}$).

For faster iteration, we use a stochastic sample of the rays $\mathcal{R}$ to evaluate the MSE term and a stochastic sample of the voxels $\mathcal{V}$ to evaluate the TV term in each optimization step. We use the same learning rate schedule as JAXNeRF and Mip-NeRF, but tune the initial learning rate separately for opacity and harmonic coefficients. The learning rate is fixed for all scenes in all datasets in the main experiments.

Directly optimizing voxel coefficients is a challenging problem for several reasons: there are many values to optimize (the problem is high-dimensional), the optimization objective is nonconvex due to the rendering formula, and the objective is poorly conditioned. Poor conditioning is typically best resolved by using a second order optimization algorithm (*e.g*. as recommended in ), but this is practically challenging to implement for a high-dimensional optimization problem because the Hessian is too large to easily compute and invert in each step. Instead, we use RMSProp to ease the ill-conditioning problem without the full computational complexity of a second-order method.

### Unbounded Scenes

We show that Plenoxels can be optimized for a wide range of settings beyond the synthetic scenes from the original NeRF paper.

With minor modifications, Plenoxels extend to real, unbounded scenes, both forward-facing and $360^{\circ}$. For forward-facing scenes, we use the same sparse voxel grid structure with normalized device coordinates, as defined in the original NeRF paper.

### Background model

For $360^{\circ}$ scenes, we augment our sparse voxel grid foreground representation with a multi-sphere image (MSI) background model, which also uses learned voxel colors and opacities with trilinear interpolation within and between spheres. Note that this is effectively the same as our foreground model, except the voxels are warped into spheres using the simple equirectangular projection (voxels index over sphere angles $\theta$ and $\phi$). We place 64 spheres linearly in inverse radius from $1$ to $\infty$ (we pre-scale the inner scene to be approximately contained in the unit sphere). To conserve memory, we store only rgb channels for the colors (only zero-order SH) and store all layers sparsely by using opacity thresholding as in our main model. This is similar to the background model in NeRF++.

### Regularization

We illustrate the importance of TV regularization in Fig. 3. In addition to TV regularization, which encourages smoothness and is used on all scenes, for certain types of scenes we also use additional regularizers.

Figure 3: Ablation over TV regularization. Clear artifacts are visible in the forward-facing scenes without TV on both σ and SH coefficients, although PSNR does not always reflect this.

On the real, forward-facing and $360^{\circ}$ scenes, we use a sparsity prior based on a Cauchy loss following SNeRG:

where $\sigma{({\mathbf{r}_{i}{(t_{k})}})}$ denotes the opacity of sample $k$ along training ray $i$. In each minibatch of optimization on forward-facing scenes, we evaluate this loss term at each sample on each active ray. This is also similar to the sparsity loss used in PlenOctrees and encourages voxels to be empty, which helps to save memory and reduce quality loss when upsampling.

On the real, $360^{\circ}$ scenes, we also use a beta distribution regularizer on the accumulated foreground transmittance of each ray in each minibatch. This loss term, following Neural Volumes, promotes a clear foreground-background decomposition by encouraging the foreground to be either fully opaque or empty. This beta loss is:

where $\mathbf{r}$ are the training rays and $T_{FG}{(\mathbf{r})}$ is the accumulated foreground transmittance (between 0 and 1) of ray $\mathbf{r}$.

### Implementation

Since sparse voxel volume rendering is not well-supported in modern autodiff libraries, we created a custom PyTorch CUDA extension library to achieve fast differentiable volume rendering; we hope practitioners will find this implementation useful in their applications. We also provide a slower, higher-level JAX implementation. Both implementations will be released to the public.

The speed of our implementation is possible in large part because the gradient of our Plenoxel model becomes very sparse very quickly, as shown in Fig. 4. Within the first 1-2 minutes of optimization, fewer than 10% of the voxels have nonzero gradients.

Figure 4: Gradient sparsity. The gradient becomes very sparse spatially within the first 12800 batches (one epoch for the synthetic scenes), with as few as 1% of the voxels updating per batch in the synthetic case. This enables efficient training via sparse parameter updates. The solid lines show the mean and the shaded regions show the full range of values among all scenes of each type.

## Results

Figure 5: 1 minute, 20 seconds. Results on the synthetic scenes after 1 epoch of optimization, an average of 1 minute and 20 seconds.

We present results on synthetic, bounded scenes; real, unbounded, forward-facing scenes; and real, unbounded, $360^{\circ}$ scenes. We include time trial comparisons with prior work, showing dramatic speedup in training compared to all prior methods (alongside real-time rendering). Quantitative comparisons are presented in Tab. 2, and visual comparisons are shown in Fig. 6, Fig. 7, and Fig. 9. Our method achieves quality results after even the first epoch of optimization, less than 1.5 minutes, as shown in Fig. 5.

We also present the results from various ablation studies of our method. In the main text we present average results (PSNR, SSIM, and VGG LPIPS ) over all scenes of each type; full results on each scene individually are included in the supplement. We include full experimental details (hyperparameters, etc.) in the supplement.

### Synthetic Scenes

Our synthetic experiments use the 8 scenes from NeRF: chair, drums, ficus, hotdog, lego, materials, mic, and ship. Each scene includes 100 ground truth training views with 800 $\times$ 800 resolution, from known camera positions distributed randomly in the upper hemisphere facing the object, which is set against a plain white background. Each scene is evaluated on 200 test views, also with resolution 800 $\times$ 800 and known inward-facing camera positions in the upper hemisphere. We provide quantitative comparisons in Tab. 2 and visual comparisons in Fig. 6.

Table 2: Results. Top: average over the 8 synthetic scenes from NeRF; Middle: the 8 real, forward-facing scenes from NeRF; Bottom: the 4 real, 360∘ scenes from Tanks and Temples. 4 of the synthetic scenes train in under 10 minutes. *LLFF requires pretraining a network to predict MPIs for each view, and then can render novel scenes without further training; this pretraining is amortized across all scenes so we do not include it in the table.

Figure 6: Synthetic, bounded scenes. Example results on the lego and ship synthetic scenes from NeRF. Please see the supplementary material for more images.

We compare our method to Neural Volumes (NV) (as a prior method that predicts a grid for each scene, using a 3D convolutional network), and JAXNeRF. For Neural Volumes we use values reported in; for JAXNeRF we report results from our own rerunning, fixing the centered pixel bug. Our method achieves comparable quality compared to the best baseline, while training in an average of 11 minutes per scene on a single GPU and supporting interactive rendering.

### Real Forward-Facing Scenes

We extend our method to unbounded, forward-facing scenes by using normalized device coordinates (NDC), as derived in NeRF. Our method is otherwise identical to the version we use on bounded, synthetic scenes, except that we use TV regularization (with a stronger weight) throughout the optimization. This change is likely necessary because of the reduced number of training views for these scenes, as described in Sec. 4.4.

Our forward-facing experiments use the same 8 scenes as in NeRF, 5 of which are originally from LLFF. Each scene consists of 20 to 60 forward-facing images captured by a handheld cell phone with resolution 1008 $\times$ 756, with $\frac{7}{8}$ of the images used for training and the remaining $\frac{1}{8}$ of the images reserved as a test set.

We compare our method to Local Light Field Fusion (LLFF) (a prior method that uses a 3D convolutional network to predict a grid for each input view) and JAXNeRF. We provide quantitative comparisons in Tab. 2 and visual comparisons in Fig. 7.

Figure 7: Real, forward-facing scenes. Example results on the fern and orchid forward-facing scenes from NeRF.

### Real $360^{\circ}$ Scenes

We extend our method to real, unbounded, $360^{\circ}$ scenes by surrounding our sparse voxel grid with an multi-sphere image (MSI, based on multi-plane images introduced by ) background model, in which each background sphere is also a simple voxel grid with trilinear interpolation (both within each sphere and between adjacent background sphere layers).

Our $360^{\circ}$ experiments use 4 scenes from the Tanks and Temples dataset: M60, playground, train, and truck. For each scene, we use the same train/test split as.

We compare our method to NeRF++, which augments NeRF with a background model to represent unbounded scenes. We present quantitative comparisons in Tab. 2 and visual comparisons in Fig. 9.

Figure 9: Real, 360∘ scenes. Example results on the playground and truck 360∘ scenes from Tanks and Temples.

### Ablation Studies

In this section, we perform extensive ablation studies of our method to understand which features are core to its success, with such a simple model. In Tab. 1, we show that continuous (in our case, trilinear) interpolation is responsible for dramatic improvement in fidelity compared to nearest neighbor interpolation (*i.e*. constant within each voxel).

In Tab. 3, we consider how our method handles a dramatic reduction in training data, from 100 views to 25 views, on the 8 synthetic scenes. We compare our method to NeRF and find that, despite its lack of complex neural priors, by increasing TV regularization our method can outperform NeRF even in this limited data regime. This ablation also sheds light on why our model performs better with higher TV regularization on the real forward-facing scenes compared to the synthetic scenes: the real scenes have many fewer training images, and the stronger regularizer helps our optimization extend smoothly to sparsely-supervised regions.

We also ablate over the resolution of our Plenoxel grid in Tab. 4 and the rendering formula in Tab. 5. The rendering formula from Max yields a substantial improvement compared to that of Neural Volumes, perhaps because it is more physically accurate (as discussed further in the supplement). The supplement also includes ablations over the learning rate schedule and optimizer demonstrating Plenoxel optimization to be robust to these hyperparameters.

Ours: 100 images (low TV)

Ours: 25 images (low TV)

Ours: 25 images (high TV)

Table 3: Ablation over the number of views. By increasing our TV regularization, we exceed NeRF fidelity even when the number of training views is only a quarter of the full dataset. Results are averaged over the 8 synthetic scenes from NeRF.

Table 4: Ablation over the Plenoxel grid resolution. Results are averaged over the 8 synthetic scenes from NeRF.

Max, used in NeRF

Table 5: Comparison of different rendering formulas. We compare the rendering formula from Max (used in NeRF and our main method) to the one used in Neural Volumes, which uses absolute instead of relative transmittance. Results are averaged over the 8 synthetic scenes from NeRF.

## Discussion

We present a method for photorealistic scene modeling and novel viewpoint rendering that produces results with comparable fidelity to the state-of-the-art, while taking orders of magnitude less time to train. Our method is also strikingly straightforward, shedding light on the core elements that are necessary for solving 3D inverse problems: a differentiable forward model, a continuous representation (in our case, via trilinear interpolation), and appropriate regularization. We acknowledge that the ingredients for this method have been available for a long time, however nonlinear optimization with tens of millions of variables has only recently become accessible to the computer vision practitioner.

### Limitations and Future Work

As with any underdetermined inverse problem, our method is susceptible to artifacts. Our method exhibits different artifacts than neural methods, as shown in Fig. 10, but both methods achieve similar quality in terms of standard metrics (as presented in Sec. 4). Future work may be able to adjust or mitigate these remaining artifacts by studying different regularization priors and/or more physically accurate differentiable rendering functions.

Although we report all of our results for each dataset with a fixed set of hyperparameters, there is no optimal a priori setting of the TV weight $\lambda_{TV}$. In practice better results may be obtained by tuning this parameter on a scene-by-scene basis, which is possible due to our fast training time. This is expected because the scale, smoothness, and number of training views varies between scenes. We note that NeRF also has hyperparameters to be set such as the length of positional encoding, learning rate, and number of layers, and tuning these may also increase performance on a scene-by-scene basis.

Figure 10: Artifacts. JAXNeRF and Plenoxel models both exhibit artifacts, but the artifacts are different, as shown here in the specularities in the synthetic drums scene. Note that some artifacts are unavoidable for any underdetermined inverse problem, but the specific artifacts vary depending on the priors induced by the model and regularizer.

Our method should extend naturally to support multiscale rendering with proper anti-aliasing through voxel cone-tracing, similar to the modifications in Mip-NeRF. Another easy addition is tone-mapping to account for white balance and exposure changes, which we expect would help especially in the real $360^{\circ}$ scenes. A hierarchical data structure (such as an octree) may provide additional speedup compared to our sparse array implementation, provided that differentiable interpolation is preserved.

Since our method is two orders of magnitude faster than NeRF, we believe that it may enable downstream applications currently bottlenecked by the performance of NeRF--for example, multi-bounce lighting and 3D generative models across large databases of scenes. By combining our method with additional components such as camera optimization and large-scale voxel hashing, it may enable a practical pipeline for end-to-end photorealistic 3D reconstruction.
