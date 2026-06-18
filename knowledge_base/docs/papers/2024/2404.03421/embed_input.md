<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Gen3DSR: Generalizable 3D Scene Reconstruction via Divide and Conquer from a Single View

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Single-view 3D reconstruction is currently approached from two dominant perspectives: reconstruction of scenes with limited diversity using 3D data supervision or reconstruction of diverse singular objects using large image priors. However, real-world scenarios are far more complex and exceed the capabilities of these methods. We therefore propose a hybrid method following a divide-and-conquer strategy. We first process the scene holistically, extracting depth and semantic information, and then leverage an object-level method for the detailed reconstruction of individual components. By splitting the problem into simpler tasks, our system is able to generalize to various types of scenes without retraining or fine-tuning. We purposely design our pipeline to be highly modular with independent, self-contained modules, to avoid the need for end-to-end training of the whole system. This enables the pipeline to naturally improve as future methods can replace the individual modules. We demonstrate the reconstruction performance of our approach on both synthetic and real-world scenes, comparing favorable against prior works.

<!-- chunk {"id": "body-0003", "role": "body", "section": "Introduction", "weight": 1.5} -->

Single-view 3D scene reconstruction refers to the problem of understanding and explaining all the visible components that assembled together create a 3D scene which closely reproduces the original 2D observation. The computer vision and graphics communities have long been interested in automating this task, yet its complexity still leaves room for many improvements. Successful single-view applications have been developed for specific purposes such as face reconstruction and hair modeling. However, 3D understanding from a single image is far from solved in the case of larger scale problems such as indoor/outdoor scene reconstruction with multiple objects.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

In general, even reconstructing one 3D object from a single image is a severely ill-posed problem, *e.g*. it is impossible to tell precisely how the back side of an object looks like if the input image only observes the front. Nonetheless, if the distribution of objects that are naturally present in our day-to-day lives is known, one can plausibly predict the shape and appearance of a 3D object from very limited information. Accordingly, various priors have been used in the context of particular object classes (such as simple shapes, or human faces ). However, modeling entire scenes is a significantly more challenging problem.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

Given the complexity of real-world scenes, reversing the process of image capturing in an end-to-end fashion would require a huge amount of data covering the variability of realistic environments. Therefore, many works solve a simplified version of the task by focusing on single objects or indoor rooms with a limited number of object classes. Under these assumptions, most of the existent solutions rely on 3D scene geometry supervision from synthetic datasets. This class of methods usually struggles when applied to real-world images due to the domain gap and limited diversity in existing datasets. In contrast, we propose to tackle the single-view 3D scene reconstruction problem in a divide-and-conquer approach while building on the advances in related, simpler tasks. In Figure we show that, following this approach, our pipeline is able to reconstruct multi-object scenes with unprecedented quality.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

In the past few years, the field of computer vision has seen tremendous progress in solving particular tasks such as depth estimation and single-image 3D object reconstruction. It is the right time for these components to be assembled to solve the challenging task of full 3D scene reconstruction. We have identified the following sub-problems that together comprehensively explain a 3D scene and enable its reconstruction from a single input image: estimating the camera calibration, predicting the (metric) depth map, segmenting entities, detecting foreground instances, reconstructing the background, recovering the occluded parts of the individual objects (amodal completion), and reconstructing them. Our disentangled framework is open for incremental improvements and future enhanced modules can be easily plugged in to boost the reconstruction performance of the entire system.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

We design a compositional framework and the corresponding abstractions, enabling scene-level 3D reconstruction without end-to-end training.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Introduction", "weight": 1.5} -->

We build a model for amodal completion and show how it can be used towards achieving full scene reconstruction.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Introduction", "weight": 1.5} -->

We develop the connecting links for integrating individually reconstructed 3D objects into the scene layout by exploiting single-view depth estimation.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Introduction", "weight": 1.5} -->

We achieve an unmatched level of generalizability for real-world single-view 3D scene reconstruction, which we demonstrate through extensive evaluations.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Method", "weight": 1.0} -->

Our method, as illustrated in Figure, takes as input a single RGB image $I$ and predicts the full 3D scene reconstruction $R{(I)}$ represented as a collection of triangle meshes. The proposed solution does not require end-to-end training and instead relies on off-the-shelf models carefully integrated into a seamless framework. First, we parse the image of the scene by finding the composing entities, and estimating the depth and camera parameters. Then, we separate the identified entities in stuff (amorphus shapes) and things (characteristic shapes). To recover the full view of each object, we perform amodal completion on the masked crops of the instances. Each object is reconstructed individually in a normalized space and aligned to the view space using the scene layout guides from the depth map. Importantly, we address the differences in focal length, principal point, and camera-to-object distance between the two spaces through reprojection. Finally, we model the background as the surface that approximates the stuff entities collectively.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Scene analysis", "weight": 1.0} -->

Our framework decouples the object-agnostic from the object-specific processing, pursuing a balance between the representational power and the generalization capabilities of the integrated modules: That is, the perspective properties, semantic labels, and depth information are best retrieved by perceiving the scene as a whole

<!-- chunk {"id": "body-0013", "role": "body", "section": "Scene analysis", "weight": 1.0} -->

The geometry of a scene is characterized by its layout and the amodal shape of the contained objects. The layout of a scene refers to the surfaces that enclose the space (*e.g*., walls) and the 3D locations of the objects. To model the layout, we unproject a monocular depth estimation $D$, of the input image using predicted camera calibration parameters, $K_{img}$, as a point cloud in the 3D view space, $P^{view} \in {\mathbb{R}}^{3}$, and adopt it as our guide for positioning the scene components. A 2.5D representation is not sufficient to fully describe the layout of a scene as it only provides information for the visible parts. Still, it can be used to integrate individually reconstructed 3D objects into the scene (Section 3.2) and for background estimation (Section 3.3).

<!-- chunk {"id": "body-0014", "role": "body", "section": "Scene analysis", "weight": 1.0} -->

To parse the image, we opt for an entity segmentation approach in contrast to conventional 2D object detection, which enables us to segment all semantically-meaningful entities without being constrained to a predefined set of classes. This step partitions the image $I$ into instances $\{ M_{i}\}$ that can be individually reconstructed to compose the whole scene. Furthermore, we consider the natural separation of the instances in thing and stuff using a universal image segmentation model. This facilitates our method to tailor the reconstruction process for each group, leveraging their unique properties (objects vs background). In this stage, we also label the identified entities, which can provide more context for instance processing.

<!-- chunk {"id": "body-0015", "role": "body", "section": "Instance processing", "weight": 1.0} -->

Let an object $O_{i}$ be a well-defined shape categorised as thing, identified by its entity mask $M_{i}$, with corresponding RGB-D region $I_{i} = {I{\lbrack M_{i}\rbrack}}$, $D_{i} = {D{\lbrack M_{i}\rbrack}}$, and a label $L_{i}$. The processing steps are illustrated in Figure. We reconstruct each instance individually to fully benefit from a view-conditioned 2D diffusion model $\mathcal{Z}$, trained using multi-view images of mostly single objects from large scale collections. As the images used to train these models are rendered with a fixed predefined camera configuration $K_{crop}$, they generalize poorly to in-the-wild object crops. Therefore, we propose to address the domain-shift via reprojection of the object-associated pixels. To this end, we identify the virtual camera that together with the desired intrinsics $K_{crop}$ closely matches the observed image.

<!-- chunk {"id": "body-0016", "role": "body", "section": "Instance processing", "weight": 1.0} -->

Then, we use the transformation to project the unprojected pixels $P_{i}^{view}$ to a crop $C_{i}$ that resembles the training domain of $\mathcal{Z}$.

<!-- chunk {"id": "body-0017", "role": "body", "section": "Instance processing", "weight": 1.0} -->

For simple scenes in which there is no occlusion between instances, the crop $C_{i}$ represents the full view of the object $O_{i}$. However, this is not the case for most real-world scenes, and directly feeding $C_{i}$ to the object reconstruction method $\mathcal{R}$ would result in an incomplete object. Therefore, we propose to recover the missing parts of $C_{i}$ by leveraging the image prior embodied by pre-trained large-scale diffusion models like Stable Diffusion. We approach the task named amodal completion which deals with recovering the shape and appearance of partially visible instances as an image-to-image translation problem. Specifically, we train a model to predict the view ${\hat{C}}_{i}$ of the full object $O_{i}$ conditioned on the object parts depicted in $C_{i}$ and the label $L_{i}$. Given the difficulty of collecting well-segmented training images guaranteed to contain complete objects, we generate a synthetic dataset specifically for this task.

<!-- chunk {"id": "body-0018", "role": "body", "section": "Instance processing", "weight": 1.0} -->

We render synthetic objects from a large collection and then obtain the conditioning images by masking out parts of the object with a randomly overlaying silhouette of another object. For more details about the dataset generation and differences between amodal completion and inpainting please see the supplementary material. We use this dataset to fine-tune Stable Diffusion, following the methodology of InstructPix2Pix, and concatenate the encoded conditioning image to the noisy latent. The weights added to the base network are initialized with zero, while the rest are taken from the pre-trained model to benefit from the learned image prior.

<!-- chunk {"id": "body-0019", "role": "body", "section": "Instance processing", "weight": 1.0} -->

The complete crop ${\hat{C}}_{i}$ can now be used as input for the single-image 3D object reconstruction method $\mathcal{R}$. Using a view-conditioned diffusion prior enables the model to reconstruct a wide range of objects from a single view without the need for 3D training supervision. The object is reconstructed using a differentiable 3D representation (*e.g*., neural fields or 3D Gaussians ) that is either directly fitted to multi-view images generated by the diffusion prior, or by optimizing a Score Distillation Sampling-based loss against the diffusion prior. Then, a polygonal mesh $R_{i}^{obj}$ aligned with the input crop ${\hat{C}}_{i}$ is extracted from the 3D representation using Marching Cubes. The obtained mesh can optionally be further fine-tuned to refine the texture of the reconstructed object.

<!-- chunk {"id": "body-0020", "role": "body", "section": "Instance processing", "weight": 1.0} -->

We transform the reconstructed instance from the object space (DreamGaussian) $R_{i}^{obj}$ to the view space (our scene) with the inverse transformation determined by the virtual camera used for projection. The obtained mesh $R_{i}^{view}$ is aligned to the object points $P_{i}$ up to an unknown scale factor $s_{i}$; this is because $\mathcal{R}$ reconstructs objects at an arbitrary scale. We estimate $s_{i}$ as the scale factor that minimizes the distance between the visible points in $R_{i}^{view}$ and $P_{i}^{view}$.

<!-- chunk {"id": "body-0021", "role": "body", "section": "Implementation details", "weight": 1.0} -->

As the proposed framework is not constrained to specific modules, we leverage the significant progress made by the computer vision community in the recent years towards solving the different sub-tasks described above.

<!-- chunk {"id": "body-0022", "role": "body", "section": "Implementation details", "weight": 1.0} -->

In the scene analysis stage, we rely on CropFormer for entity segmentation, OneFormer to separate them in foreground instances and background entities, and Perspective Fields to estimate the camera calibration. We mainly use Marigold for depth estimation. However, the model predicts affine-invariant depth which differs by an unknown image-level offset and scale from the absolute physical units. During evaluations, we estimate these factors based on the ground truth depth available in the datasets to ensure that the reconstructions align with the target. For in-the-wild predictions, we empirically found that estimating the two unknowns of Marigold output based on a metric depth estimation, in our case, DepthAnything, achieves better results than using the latter by itself.

<!-- chunk {"id": "body-0023", "role": "body", "section": "Implementation details", "weight": 1.0} -->

In the instance processing stage, we perform amodal completion on the reprojected crops using our model obtained by fine-tuning Stable Diffusion v1.5. We also sample several points in the instance's mask and feed them to OVSAM together with the input image to obtain the text prompt for guiding the diffusion. The completed object is then reconstructed using DreamGaussian. We estimate the camera elevation required by DreamGaussian as. Then, we find the 3D points of the reconstruction that correspond to the unprojected instance points, which serve as our layout guide, and compute the scale which aligns them. Further specifications regarding the integrated models, possible alternatives for some of the processing stages and an analysis of the inference time of our method are provided in Section of the supplementary material.

<!-- chunk {"id": "body-0024", "role": "body", "section": "Results", "weight": 1.0} -->

We showcase the performance of our method using several datasets across diverse scenarios. For numerical evaluation we first consider 3D-FRONT, a synthetic dataset of indoor rooms with available ground truth geometry. Due to the large scale of the dataset, we manually sample 100 images from the test split of, avoiding the images with heavy scene occlusions (*e.g*., camera positioned behind a plant), intersecting objects, and scenes with very few objects. In addition, we use the 10 validation images of HOPE-Image dataset containing household objects captured under two scenarios. Though the dataset is intended for object pose evaluation, we find the ground-truth object alignment to match the input images well-enough for our purpose.

<!-- chunk {"id": "body-0025", "role": "body", "section": "Results", "weight": 1.0} -->

We report the quantitative results using the widely-employed metrics for 3D reconstruction: Chamfer Distance and F-Score. Both are computed between densely sampled sets of points from the reconstructed meshes and the ground truth respectively. As we focus the evaluation on whole scenes, the points are uniformly sampled from the entire geometry of a scene.

<!-- chunk {"id": "body-0026", "role": "body", "section": "Results", "weight": 1.0} -->

We compare our method against several solutions covering multiple approaches for 3D scene reconstruction. An overview of their capabilities is presented in Table. BUOL and Uni-3D are both feed-forward scene reconstruction methods that have been trained with 3D supervision on the 3D-FRONT dataset. While we evaluate the methods on the same dataset they were trained, we use a more realistic rendering, following. Even under this minor change, the methods' performance degrades significantly, as can be seen in Table and Figure, showing their lack of generalization.

<!-- chunk {"id": "body-0027", "role": "body", "section": "Results", "weight": 1.0} -->

InstPIFu and USL are both compositional approaches that rely on 2D and 3D object detectors for identifying the objects to be reconstructed and aligning them in the scene. However, InstPIFu requires direct 3D supervision and USL is trained end-to-end. This limits their application domain and generalizability. Furthermore, as seen in Tables and, our method is able to quantitatively match the performance of InstPIFu even when evaluated on the 3D-FRONT dataset (which InstPIFu used for training). The qualitative results in Figures and show that the method successfully reconstructs large furniture pieces and arranges them in a good layout; however, several objects such as plants and chandeliers are missing. The results of InstPIFu further degrade when evaluated out-of-distribution, as can be seen on real-world images in Figure. Since the implementation of USL is not publicly available, we only compare our visual results on the Hypersim dataset in Figure. USL also misses many objects, and the reconstructed components have a simplified geometry with no texture. In contrast, our results are more realistic and have higher visual quality.

<!-- chunk {"id": "body-0028", "role": "body", "section": "Results", "weight": 1.0} -->

Additionally, we compare our method with DreamGaussian by itself in a non-compositional approach. To apply the model, we treat all instances in a scene as a single object and reconstruct them together. As the model has seen several scenes composed of more than one object during its training, it performs reasonably under this setting. Given the different camera intrinsics in the evaluation, we also compare the results of applying the model on the images after using a reprojection similar to the one used in our pipeline. This further boosts its performance as measured in Table. Still, its results are worse compared to our compositional approach, which can be analyzed in the qualitative results in Figure and in the supplementary material.

<!-- chunk {"id": "body-0029", "role": "body", "section": "Results", "weight": 1.0} -->

Lastly, we evaluate in Figure the methods' performance on real-world data with diverse scenarios. The results show that the proposed solution reconstructs complex scenes well, while overcoming many limitations of prior works. We briefly address the reconstruction of outdoor scenes in the Section 7.4 of the supplementary material.

<!-- chunk {"id": "body-0030", "role": "body", "section": "Results", "weight": 1.0} -->

Ours (input view)
Ours (another view)

<!-- chunk {"id": "body-0031", "role": "body", "section": "Ablations", "weight": 1.0} -->

The two most important interfaces in combining the depth estimation and the single-view object reconstruction components are our reprojection and amodal completion. We present an ablation of these components in Table. Ablating the reprojection amounts to simply using image crops. This ignores projective geometry properties and leads to deformed reconstructions. Amodal completion is necessary to contend with the various occlusions that appear in the input view. This step boosts the performance on the 3D-FRONT dataset, but does not improve the numerical evaluation on HOPE-Image dataset, since most of the objects in the scenes are not occluded. More ablation results are included in the Section 7.3 of the supplementary material.

<!-- chunk {"id": "body-0032", "role": "body", "section": "Limitations", "weight": 1.5} -->

The proposed method has certain shortcomings and there is significant room for improvement, especially for in-the-wild predictions. By design, the failure cases of the individual modules (depth estimation, camera calibration, elevation estimation, etc.) become limitations of our framework. Since we do not train an end-to-end system, errors can propagate from one stage to the next. Therefore, the performance of the overall pipeline is limited by its weakest link.

<!-- chunk {"id": "body-0033", "role": "body", "section": "Limitations", "weight": 1.5} -->

We believe that most of the current limitations can be overcome by improving the implementation of some of the particular modules in our framework and by enhancing their interoperability: using estimated depth in 3D object reconstruction or global image context for amodal completion. We further discuss the method's limitations and provide concrete examples in the Section of the supplementary material.

<!-- chunk {"id": "body-0034", "role": "body", "section": "Conclusion", "weight": 1.5} -->

In this work, we introduce a modular framework for reconstructing complex 3D scenes from an image. We prioritize generalization by taking a divide-and-conquer approach rather than end-to-end. Our decomposing into multiple entities benefits from existing components, which effectively solve the established subtasks. We develop the necessary interfaces that enable the modules to function properly and finally yield a full 3D reconstruction. Our experiments decidedly show the advantage of the proposed method on various types of scenes. Considering the illustrated performance for diverse scenarios, we believe that our approach is a strong baseline and a stepping stone towards generalizable full 3D scene reconstruction from a single image.
