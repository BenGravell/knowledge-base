<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Flow Gym: A Framework for the Development, Benchmarking, Training, and Deployment of Flow-field Quantification Methods

Topics include Benchmarks, Real-time systems, Offline algorithms, Learning, Flow Gym, Particle image velocimetry, PIV.

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Particle image velocimetry (PIV) and related optical-flow methods are widely used to quantify fluid motion, but their development and evaluation are often hindered by fragmented software, inconsistent interfaces, and limited reproducibility. To address these challenges, we present Flow Gym, a framework for developing, benchmarking, training, and deploying flow-field quantification methods, with a primary focus on PIV. Its core contribution is a standardized interface that allows classical and learning-based algorithms to be integrated, compared, and deployed within a common pipeline. The framework includes JAX implementations and wrappers for existing methods, modular pre-processing and post-processing components, and utilities for training and benchmarking. By leveraging JAX, Flow Gym supports hardware-accelerated execution while remaining interoperable with external implementations from libraries such as OpenCV and PyTorch. It can operate on both synthetic and experimental data and supports the same workflow for offline benchmarking and real-time deployment. Flow Gym is designed to improve reproducibility, reduce barriers to method development, and facilitate the translation of flow-field quantification algorithms from research to experimental settings.

<!-- chunk {"id": "body-0003", "role": "body", "section": "Abstract", "weight": 1.5} -->

Particle image velocimetry (PIV) and related optical-flow methods are widely used to quantify fluid motion, but their development and evaluation are often hindered by fragmented software, inconsistent interfaces, and limited reproducibility. To address these challenges, we present Flow Gym, a framework for developing, benchmarking, training, and deploying flow-field quantification methods, with a primary focus on PIV. Its core contribution is a standardized interface that allows classical and learning-based algorithms to be integrated, compared, and deployed within a common pipeline. The framework includes JAX implementations and wrappers for existing methods, modular pre-processing and post-processing components, and utilities for training and benchmarking. By leveraging JAX, Flow Gym supports hardware-accelerated execution while remaining interoperable with external implementations from libraries such as OpenCV and PyTorch. It can operate on both synthetic and experimental data and supports the same workflow for offline benchmarking and real-time deployment. Flow Gym is designed to improve reproducibility, reduce barriers to method development, and facilitate the translation of flow-field quantification algorithms from research to experimental settings.

<!-- chunk {"id": "body-0004", "role": "body", "section": "keywords", "weight": 1.0} -->

Particle Image Velocimetry, Fluid Estimation, Deep Learning, Reinforcement Learning, GPU acceleration, JAX

<!-- chunk {"id": "body-0005", "role": "body", "section": "Code metadata", "weight": 1.0} -->

Permanent link to code/repository used for this code version

<!-- chunk {"id": "body-0006", "role": "body", "section": "Code metadata", "weight": 1.0} -->

Software code languages, tools, and services used

<!-- chunk {"id": "body-0007", "role": "body", "section": "Code metadata", "weight": 1.0} -->

Compilation requirements, operating environments &amp; dependencies
Python 3.10+, JAX 0.6.2+, tqdm 4.67.1, h5py 3.13.0+, ruamel.yaml 0.18.10+, robo-goggles 0.1.7+

<!-- chunk {"id": "body-0008", "role": "body", "section": "Code metadata", "weight": 1.0} -->

If available Link to developer documentation/manual

<!-- chunk {"id": "body-0009", "role": "body", "section": "Motivation and significance", "weight": 1.0} -->

Flow-field quantification from images of tracer particles is a central task in experimental fluid mechanics, with Particle Image Velocimetry (PIV) and optical flow among the most widely used techniques. Over the years, a broad range of methods has been developed for this purpose, including both classical approaches and learning-based methods. In recent years, advances in computer vision and deep learning have significantly influenced the design of new flow-field quantification methods.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Motivation and significance", "weight": 1.0} -->

However, despite the growing methodological diversity, software support for developing, comparing, and deploying such methods remains fragmented. Implementations are often distributed across different libraries and programming frameworks, rely on incompatible interfaces, and differ in pre-processing, post-processing, and evaluation protocols. As a result, fair comparison, reproducible benchmarking, and practical deployment remain unnecessarily difficult. By contrast, progress in neighboring fields has been accelerated by shared software abstractions, standardized reference implementations, and efficient execution on modern hardware. In computer vision and reinforcement learning, common interfaces and benchmark-oriented software ecosystems have played a central role in improving reproducibility and enabling systematic comparison. This is particularly important in settings where performance is sensitive to implementation details and experimental choices. Flow-field quantification pipelines exhibit a similar sensitivity, which makes standardized and reusable software infrastructure especially valuable.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Motivation and significance", "weight": 1.0} -->

With the software package presented in this paper, we aim to bring to flow-field quantification the same emphasis on reproducibility, comparability, and practical usability that has become standard in adjacent computational fields in the past decade.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Contributions", "weight": 1.0} -->

We present Flow Gym, a unified framework for developing, training, benchmarking, and deploying flow-field quantification methods; see Figure 1. Our main contributions are: • a standardized Estimator interface for classical and learning-based flow-field quantification methods; • shared training and evaluation workflows that support repeatable benchmarking and facilitate deployment on real experimental setups; • JAX-native implementations and interoperable wrappers for representative methods, providing accelerator-friendly execution together with compatibility with external libraries such as OpenCV, PyTorch, and OpenPIV. Flow Gym supports both consecutive (or recurrent) and independent estimation workflows for flow-field quantification. The same interface can also be used for related estimators beyond PIV, such as tracer-particle density estimation.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Software description and illustrative examples", "weight": 1.0} -->

Flow Gym is organized as a unified software framework for developing, benchmarking, training, and deploying flow-field quantification methods. The framework is centered around the Estimator interface, which provides a common foundation for standardized baselines and for integrating new methods within the same workflow. The same interface can also be extended to related quantification tasks, such as tracer-particle density estimation^33^3In this paper, for the sake of clarity, we focus on the flow-field quantification instance of the software package because it is the most widely studied in the literature..

<!-- chunk {"id": "body-0014", "role": "body", "section": "Estimator", "weight": 1.0} -->

The Estimator module defines a unified interface for algorithms that map observations (e.g., the PIV image pairs) to quantities of interest. To align with JAX's programming model, the Estimator interface is stateless and functional.

<!-- chunk {"id": "body-0015", "role": "body", "section": "Estimator", "weight": 1.0} -->

[⬇](data:text/plain;base64,bmV3X3N0YXRlLCBtZXRyaWNzID0gZXN0aW1hdG9yKGltYWdlLCBzdGF0ZSwgdHJhaW5hYmxlX3N0YXRlKQ==){download=""}

<!-- chunk {"id": "body-0016", "role": "body", "section": "Estimator", "weight": 1.0} -->

new_state, metrics = estimator(image, state, trainable_state)

<!-- chunk {"id": "body-0017", "role": "body", "section": "Estimator", "weight": 1.0} -->

In particular, new_state includes the rolled history and the updated PRNG key that is carried to the next iteration to ensure random draws in subsequent calls, and metrics provides task-specific logging information. The state of the Estimator captures the run-time context propagated across successive calls. For simple algorithms, this context may be limited only to the current image pair. This is the case, for example, for WIDIM-based algorithms and optical flow algorithms. More advanced flow-field quantification methods may also retain a short-term history, such as previous image pairs, previous estimates, or recurrent internal variables. As a result, the same interface supports "one-shot" estimators as well as "recurrent" estimators that exploit the temporal correlation across estimates. In the current implementation, the state also comprises a batch of PRNG keys for controlled randomness. When image pairs are processed independently (e.g., during benchmarking on a shuffled dataset), the state can simply be re-initialized before each estimation. The trainable state captures the long-term parameters of the estimator.

<!-- chunk {"id": "body-0018", "role": "body", "section": "Estimator", "weight": 1.0} -->

For learning-based estimators, this typically includes the model weights, optimizer state, and optimizer transformation. Classical estimators such as cross-correlation algorithms do not have trainable parameters; in those cases, Flow Gym simply propagates an empty trainable-state container through the same interface so that classical and learning-based methods can be compared and deployed within a common pipeline. Following JAX's functional programming style, the Estimator call is side-effect free: neither the trainable_state nor the input observation is mutated in place. An explanation of how to add a learning component to an Estimator instance is provided in "Training an estimator."

<!-- chunk {"id": "body-0019", "role": "body", "section": "Estimator", "weight": 1.0} -->

In addition to the core call, the class also provides standardized hooks for image processing. On the input side, Estimator supports a configurable sequence of *pre-processing* steps, explained in detail in Section 2.2.1. Each step is applied sequentially before estimation, ensuring consistent data pre-processing across algorithms. For flow-field quantification algorithms, the FlowFieldEstimator subclass additionally provides a standardized *post-processing* stage; see Section 2.2.3. This layered design allows pre-processing, estimation, and post-processing to be specified independently.

<!-- chunk {"id": "body-0020", "role": "body", "section": "Deployment of an estimator", "weight": 1.0} -->

Estimators can be instantiated directly from configuration files. Importantly, deployment is agnostic to the provenance of the input data: once instantiated, the same estimator can be applied to synthetic image pairs, recorded experimental datasets, or live acquisitions from a real setup. The deployment pipeline in LABEL:lst:example-make has already been adopted in several projects, including real-time fluid control.

<!-- chunk {"id": "body-0021", "role": "body", "section": "Deployment of an estimator", "weight": 1.0} -->

## Define the config (or load from YAML)
"estimator": "dis_jax",
"estimate_type": "flow",
"config": {"jit": True,..., },
## Create the estimator and associated functions
estimator_config, image_shape
## Choose an image pair of interest (synthetic or experimental)
image_0, image_1 = input_images
## Compute an estimate for an image pair
est_state_0 = create_state_fn(image_0, key0)
est_state_1, metrics = compute_estimate_fn(
image_1, est_state, trainable_state
## If this is a stream of images, rather than an image pair,
## one can use the estimator recurrently given a new image, image_2
est_state_2, metrics = compute_estimate_fn(
image_2, est_state_1, trainable_state
Listing 1: Example usage of make_estimator for deployment.

<!-- chunk {"id": "body-0022", "role": "body", "section": "Implementing a custom estimator", "weight": 1.0} -->

Within this interface, implementing a new estimator reduces to defining a single method: \_estimate. This method specifies how a pre-processed observation, together with the current estimator state and trainable state, is mapped to a new state and a set of metrics. The base Estimator class automatically handles auxiliary tasks such as pre-processing, PRNG-key management, and state-history updates. This allows developers to focus on the algorithm-specific logic of their estimator.

<!-- chunk {"id": "body-0023", "role": "body", "section": "Implementing a custom estimator", "weight": 1.0} -->

*Implement the algorithm natively in JAX.* This consists in writing the algorithm logic directly in \_estimate using JAX, thereby maximizing performance and integration, for example through compatibility with jit and vmap. For instance, we implemented DIS and -PIV natively in JAX.

<!-- chunk {"id": "body-0024", "role": "body", "section": "Implementing a custom estimator", "weight": 1.0} -->

*Wrap an existing external implementation.* This consists in using \_estimate as a wrapper around an external library (e.g., OpenCV or OpenPIV) or around a model implemented in another framework (e.g., PyTorch). Examples include the OpenCV-based DeepFlow estimator, included through the OpenCV API, and -PIV, whose PyTorch code was ported while providing appropriate attribution and respecting the upstream license. This approach enables benchmarking and deployment in Flow Gym even when the original method is not implemented natively in JAX.

<!-- chunk {"id": "body-0025", "role": "body", "section": "Training an estimator", "weight": 1.0} -->

When an estimator contains trainable weights or tunable parameters, Flow Gym provides a common training interface built on top of the Estimator abstraction.

<!-- chunk {"id": "body-0026", "role": "body", "section": "Training an estimator", "weight": 1.0} -->

create_trainable_state, which initializes the trainable_state object; by default, this is an empty pytree. This method is called automatically within make_estimator.

<!-- chunk {"id": "body-0027", "role": "body", "section": "Training an estimator", "weight": 1.0} -->

create_train_step, which returns a function specifying one optimization step. For example, for a neural-network-based estimator, this typically corresponds to one stochastic-gradient-descent step.

<!-- chunk {"id": "body-0028", "role": "body", "section": "Training an estimator", "weight": 1.0} -->

LABEL:lst:example-train shows a simplified supervised training loop based on the functional interface of Estimator together with a standard data loader. LABEL:lst:example-train-consecutive shows a simplified sequential training loop for a learnable estimator that exploits the history of observations across multiple steps. For this purpose, Flow Gym provides FluidEnv, a lightweight wrapper around SynthPix that exposes temporally consecutive observations through a minimal reset/step interface. Flow Gym also provides more structured versions of this boilerplate code in train.py and train_supervised.py.

<!-- chunk {"id": "body-0029", "role": "body", "section": "Training an estimator", "weight": 1.0} -->

Training is not restricted to synthetic data: the same interface can also be used with experimental image pairs, whether processed independently or as part of a temporal sequence; see also Section 2.3. In such cases, when ground-truth flow is unavailable, one can consider a different method as reference or an unsupervised loss defined directly from the images. For example, by warping one image with the estimated flow and measuring its consistency with the other. Sequential training relies on precomputed or externally generated time-resolved flows, which are often available from offline simulations and public datasets such as.

<!-- chunk {"id": "body-0030", "role": "body", "section": "Training an estimator", "weight": 1.0} -->

Not all estimators integrated in Flow Gym are trainable. Classical methods such as OpenPIV are included as standardized reference implementations for benchmarking and deployment under the same interface as learning-based methods, but are not trained with Flow Gym.

<!-- chunk {"id": "body-0031", "role": "body", "section": "Training an estimator", "weight": 1.0} -->

## Initialize trainable state and training step
train_step_fn = estimator.create_train_step
## Iterate through the dataloader
for imgs1, imgs2, ground_truth in data_loader:
## Create a new state for each batch
est_state = create_state_fn(imgs1, key)
## Functionally update the trainable state
est_state_new,
trainable_state_new,
trainable_state, est_state, imgs2, ground_truth
Listing 2: Example of training loop with Estimator and a data loader.

<!-- chunk {"id": "body-0032", "role": "body", "section": "Training an estimator", "weight": 1.0} -->

## Instantiate the environment
env = FluidEnv.make(env_config)
## Create the training step function
train_step_fn = estimator.create_train_step
## Iterate through the episodes
for episode in range(num_episodes):
## Reset the environment for every new episode
observations, env_state, done = env.reset(env_state)
est_state = create_state_fn(observations.images, key)
while not done.any:
## Estimator forward pass
est_state, metrics = compute_estimate_fn(
observations, est_state, trainable_state)
## Extract the action (the last estimate)
action = est_state["estimates"]
## Environment step
observations, env_state_new, reward, done = env.step(
## Optimization step
trainable_state_new,
est_state_new,
Listing 3: Example of training loop with FluidEnv and Estimator.

<!-- chunk {"id": "body-0033", "role": "body", "section": "Stable baselines", "weight": 1.0} -->

We organize the baseline implementations and comparisons into three categories: pre-processing, processing, and post-processing. Although not exhaustive, this collection covers several of the most commonly used components in the PIV image-analysis pipeline. By providing common implementations to build upon, Flow Gym facilitates the development, benchmarking, training, and deployment of new algorithms.

<!-- chunk {"id": "body-0034", "role": "body", "section": "Pre-processing", "weight": 1.0} -->

*Histogram equalization*. For every tile, the pixel intensities are adjusted to span the full range, so that low- and high-exposure regions are processed independently to maximize contrast.

<!-- chunk {"id": "body-0035", "role": "body", "section": "Pre-processing", "weight": 1.0} -->

*Intensity high-pass*. A high-pass filter removes low-frequency components associated with inhomogeneous lighting while preserving the high-frequency components associated with tracer particles.

<!-- chunk {"id": "body-0036", "role": "body", "section": "Pre-processing", "weight": 1.0} -->

*Intensity capping (clipping)*. Many PIV algorithms are affected by non-uniform particle brightness. To mitigate this effect, the maximum (and optionally minimum) intensity in an image can be clipped.

<!-- chunk {"id": "body-0037", "role": "body", "section": "Pre-processing", "weight": 1.0} -->

We also implement other standard operations, including Otsu thresholding, Gaussian blurring, and normalization. We illustrate in Figure 2 the effects of the different pre-processing techniques.

<!-- chunk {"id": "body-0038", "role": "body", "section": "Pre-processing configuration and customization", "weight": 1.0} -->

The pre-processing pipeline in Flow Gym is configured through a list of dictionaries, each specifying a pre-processing function and its parameters. To introduce a new pre-processing step, it suffices to define a function with signature

<!-- chunk {"id": "body-0039", "role": "body", "section": "Pre-processing configuration and customization", "weight": 1.0} -->

[⬇](data:text/plain;base64,aW1hZ2VzLCBzdGF0ZSwgdHJhaW5hYmxlX3N0YXRlID0gbXlfc3RlcCgKICAgIGltYWdlcywgc3RhdGUsIHRyYWluYWJsZV9zdGF0ZSwgcGFyYW0xLCAuLi4p){download=""}

<!-- chunk {"id": "body-0040", "role": "body", "section": "Pre-processing configuration and customization", "weight": 1.0} -->

images, state, trainable_state = my_step(

<!-- chunk {"id": "body-0041", "role": "body", "section": "Pre-processing configuration and customization", "weight": 1.0} -->

images, state, trainable_state, param1, \...)

<!-- chunk {"id": "body-0042", "role": "body", "section": "Pre-processing configuration and customization", "weight": 1.0} -->

The parameters "param1, \..." are automatically extracted from the configuration file when the pipeline is loaded. This modular design allows flexible composition of transformations such as normalization, filtering, or denoising. Each pre-processing step receives the input image and the estimator's state and trainable_state, which also makes it possible to implement dynamic or learning-based pre-processing. For example, one may include adaptive normalization or diffusion-based refinement.

<!-- chunk {"id": "body-0043", "role": "body", "section": "JAX implementations", "weight": 1.0} -->

We re-implement several optical flow and PIV methods in JAX, including DIS, OpenPIV, and -PIV. These implementations provide accelerator-friendly baselines under the same interface used throughout Flow Gym.

<!-- chunk {"id": "body-0044", "role": "body", "section": "Integration of existing implementations", "weight": 1.0} -->

Complementarily, Flow Gym provides wrappers around several existing implementations (e.g., OpenCV algorithms, OpenPIV, and PyTorch implementations ). This allows users to compare external implementations and JAX-native estimators under the same conditions, including methods that are not trained within Flow Gym and methods that do not support end-to-end JAX differentiation.

<!-- chunk {"id": "body-0045", "role": "body", "section": "Post-Processing", "weight": 1.0} -->

Following, we implement data validation, data interpolation, and data smoothing, introducing minor variations to these techniques. The parameters of the post-processing steps are specified analogously to the pre-processing steps, and we similarly allow the integration of (possibly learning-based) custom methods; see Section 2.2.1.

<!-- chunk {"id": "body-0046", "role": "body", "section": "Data validation", "weight": 1.0} -->

*Constant thresholding velocity filter*. All entries with a velocity magnitude outside a constant range $\lbrack u_{\min},u_{\max}\rbrack$ are marked as outliers.

<!-- chunk {"id": "body-0047", "role": "body", "section": "Data validation", "weight": 1.0} -->

*Adaptive thresholding velocity filter (local/global)*. The entries with a velocity magnitude outside $\lbrack{\overline{u} - {n\sigma_{u}}},{\overline{u} + {n\sigma_{u}}}\rbrack$ are marked as outliers, where $\overline{u}$ and $\sigma_{u}$ are computed either globally over the full field or locally within a square neighborhood of size $N \times N$ centered on each interrogation point. In the results of Figure 3, we use $N = 3$, corresponding to a $3 \times 3$ neighborhood.

<!-- chunk {"id": "body-0048", "role": "body", "section": "Data validation", "weight": 1.0} -->

*Universal outlier detection based on the median test*. We implement the algorithm presented. By making use of comparator networks we achieve sub-ms performance on megapixel images.

<!-- chunk {"id": "body-0049", "role": "body", "section": "Data validation", "weight": 1.0} -->

In Figure 3, we illustrate the effects of the different outlier detection schemes on an estimated flow from synthetic images.

<!-- chunk {"id": "body-0050", "role": "body", "section": "Data interpolation", "weight": 1.0} -->

*Tile-based averaging*, where each missing vector is replaced by the mean of its valid neighbors within a predefined stencil; this approach is computationally efficient and well suited for isolated outliers, but may oversmooth sharp gradients.

<!-- chunk {"id": "body-0051", "role": "body", "section": "Data interpolation", "weight": 1.0} -->

*Boundary-value solver*, where the inpainting problem is formulated as solving Laplace's equation with boundary conditions set by the valid neighboring vectors; this approach is computationally more expensive, but provides more globally consistent reconstructions.

<!-- chunk {"id": "body-0052", "role": "body", "section": "Data interpolation", "weight": 1.0} -->

Importantly, custom data-interpolation steps, possibly learning-based, such as diffusion-model-based data interpolation, can be easily integrated.

<!-- chunk {"id": "body-0053", "role": "body", "section": "Data smoothing", "weight": 1.0} -->

To attenuate residual noise and improve local consistency of the estimate, we provide efficient JAX implementations of several smoothing operators, including *average filtering*, *median filtering*, and *normalized least-squares smoothing*.

<!-- chunk {"id": "body-0054", "role": "body", "section": "Data sources", "weight": 1.0} -->

A key design choice in Flow Gym is that the Estimator interface is agnostic to the provenance of the input data. In particular, estimators and the shared training and benchmarking utilities operate on a standardized batch interface rather than assuming a specific flow solver, renderer, or acquisition pipeline. In the flow-field quantification setting considered in this paper, this interface consists of image pairs and, when available, the associated two-dimensional flow fields (or a two-dimensional slice of a three-dimensional field). In our current implementation, this standardized batch interface is provided by SynthPix, which can either (i) generate PIV image pairs from prescribed flow fields or (ii) load existing datasets; see. Consequently, the same estimator can be developed and benchmarked on synthetic data, offline simulation outputs, or recorded experimental datasets without changing its interface. Through a custom adapter, SynthPix can also be coupled to an external physics simulator that computes the flow online, enabling closed-loop setups such as active fluid control.

<!-- chunk {"id": "body-0055", "role": "body", "section": "Data sources", "weight": 1.0} -->

Importantly, deployment of an Estimator is decoupled from SynthPix: once instantiated, the same estimator can be applied directly to experimental image pairs acquired online, including live streams from real PIV setups such as water channels, and can therefore be used in real-time physical fluid-control loops. As a result, the same estimator interface can be used with a wide range of data sources, including (a) snapshots exported from physics-based solvers, (b) experimental PIV datasets with pre-recorded image pairs, (c) analytically specified vector fields, and (d) flows from other scientific domains or non-physical synthetic fields. This also makes it possible to interface Flow Gym with broader simulation collections such as *The Well* dataset and the *Johns Hopkins Turbulence Database*.

<!-- chunk {"id": "body-0056", "role": "body", "section": "Impact", "weight": 1.0} -->

Flow Gym has already been adopted as a shared software infrastructure across multiple research efforts in flow-field quantification and control. Since its initial development, it has enabled the rapid deployment and iteration of real-time flow-field quantification pipelines in experimental settings with hardware in the loop, as demonstrated. The framework also supported the development and evaluation of new estimation methodologies. For instance, Flow Gym was used to implement, test, and benchmark the consensus ADMM-based flow refinement approach introduced. In addition, Flow Gym was used to study learning-based estimators subject to hard constraints. The experimental validation of hard-constrained neural networks for flow estimation in relied on Flow Gym to evaluate constrained and unconstrained models within the same pipeline. Flow Gym currently supports ongoing research at ETH Zürich on adaptive PIV tuning and active fluid control.

<!-- chunk {"id": "body-0057", "role": "body", "section": "Conclusions", "weight": 1.0} -->

Flow Gym is a unified framework for developing, training, benchmarking, and deploying flow-field quantification methods, with a primary focus on PIV. Its core contribution is a standardized estimator interface that enables seamless integration, fair comparison, and practical deployment across both classical and learning-based methods. Implemented in JAX and interoperable with OpenCV and PyTorch, Flow Gym supports accelerator-friendly execution while remaining compatible with existing software stacks.

<!-- chunk {"id": "body-0058", "role": "body", "section": "Conclusions", "weight": 1.0} -->

*More algorithms.* The most important axis of improvement and future work is to increase the number of algorithms integrated into Flow Gym and their implementation in JAX.

<!-- chunk {"id": "body-0059", "role": "body", "section": "Conclusions", "weight": 1.0} -->

*Volumetric flow-field quantification.* Flow Gym currently targets only two-dimensional flow-field quantification, and extending it to volumetric setups is a key next step. Concretely, we plan to introduce an explicit configuration modality that selects the appropriate data interface and estimator pipeline and extend the data container from pairwise image batches (e.g., images1, images2) to *multi-camera grouped batches* for volumetric quantification, where each sample aggregates per-camera image pairs together with camera calibration and pose (intrinsics/extrinsics). Enabling this functionality requires extending the underlying synthetic generator (SynthPix ) to synthesize PIV images in a volumetric setting.

<!-- chunk {"id": "body-0060", "role": "body", "section": "Conclusions", "weight": 1.0} -->

*Real-world integration.* A promising direction is to connect Flow Gym directly to physical water channels---following efforts such as ---potentially via an Internet-accessible interface, enabling algorithms to be evaluated under real-world operating conditions.
