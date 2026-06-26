<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Robust and Controllable Object-Centric Learning through Energy-based Models

Topics include Robustness, Neural networks, Transformers, Attention mechanisms, Representation learning, Probabilistic models, Accuracy, Generalization, Control, Learning, Machine learning.

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Humans are remarkably good at understanding and reasoning about complex visual scenes. The capability to decompose low-level observations into discrete objects allows us to build a grounded abstract representation and identify the compositional structure of the world. Accordingly, it is a crucial step for machine learning models to be capable of inferring objects and their properties from visual scenes without explicit supervision. However, existing works on object-centric representation learning either rely on tailor-made neural network modules or strong probabilistic assumptions in the underlying generative and inference processes. In this work, we present \ours, a conceptually simple and general approach to learning object-centric representations through an energy-based model. By forming a permutation-invariant energy function using vanilla attention blocks readily available in Transformers, we can infer object-centric latent variables via gradient-based MCMC methods where permutation equivariance is automatically guaranteed. We show that \ours can be easily integrated into existing architectures and can effectively extract high-quality object-centric representations, leading to better segmentation accuracy and competitive downstream task performance. Further, empirical evaluations show that \ours's learned representations are robust against distribution shift.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Finally, we demonstrate the effectiveness of \ours in systematic compositional generalization, by re-composing learned energy functions for novel scene generation and manipulation.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

The ability to recognize objects and infer their properties and relations in a scene is a fundamental capability of human cognition. The central question of how objects are discovered and represented in the brain has been a subject of intense research for decades, and has prompted the field of cognitive science to ask how we might develop intelligent machine agents to learn to represent objects in the same way humans do, without being explicitly taught what those objects are. Developing artificial agents capable of decomposing complex scenes into discrete objects can be a crucial step for many applications in robotics, vision, reasoning, and planning. Learning such object-centric representations can further help to identify the relational and compositional structure among objects and enables the agent to reason about a novel scene composed of new objects by leveraging knowledge from previously-learned representations of similar objects.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

In recent years, many works have been proposed to learn object-centric representations from visual scenes without human supervision. A variety of models, in the form of structured generative models or specifically designed neural network modules, have been proposed to tackle the problem of visual scene decomposition and generation. On the other hand, recent progress in large language models and visual-language models shows the huge potential of training expressive neural network models with minimal hand-designed inductive biases. In a similar spirit, we ask whether we can learn object-centric representations with minimal human assumptions and task-specific architectures.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Contributions", "weight": 1.0} -->

In this work, we introduce EGO (EnerGy-based Object-centric learning), a conceptually simple yet effective approach to learning object-centric representations without the need for specially-tailored neural network architectures or excessive generative modeling (typically parametric) assumptions. Based on the Energy-based Model (EBM) framework, we propose to learn an energy function that takes as input a visual scene and a set of object-centric latent variables and outputs a scalar value that measures the consistency between the observation and the latent representation (Section 2). We minimally assume permutation invariance among objects and embed this assumption into the energy function by leveraging the vanilla attention mechanisms from the Transformer architecture (Section 2.1). In essence, our method makes models act as segmentation annotators, aiming to iteratively improve their annotations by minimizing our energy function. We use gradient-based Markov chain Monte Carlo (MCMC) sampling to efficiently sample latent variables from the EBM distribution, which automatically yields a permutation-equivariant update rule for the latent variables (Section 2.2).

<!-- chunk {"id": "body-0007", "role": "body", "section": "Contributions", "weight": 1.0} -->

This stochastic inference procedure also addresses the inherent uncertainty in learning object-centric representations; models can learn to represent scenes containing multiple objects and potential occlusions in a probabilistic and multi-modal manner. We demonstrate the effectiveness of our approach on a variety of unsupervised object discovery tasks and show both qualitatively and qualitatively that our model can learn to decompose complex scenes into highly accurate and interpretable objects, outperforming state-of-the-art methods on segmentation performance (Section 4.1). We also show that we can reuse the learned energy functions for controllable scene generation and manipulation, which enables systematic compositional generalization to novel scenes (Section 4.2). Finally, we demonstrate the robustness of our model to various distribution shifts and hyperparameter settings (Section 4.3).

<!-- chunk {"id": "body-0008", "role": "body", "section": "Energy-based Object-Centric Representation Learning", "weight": 1.0} -->

The goal of object-centric representation learning is to learn a mapping from a visual observation $\mathbf{x} \in {\mathbb{R}}^{D_{\mathbf{x}}}$ to a set of vectors $\{\mathbf{z}_{k}\}$, where each vector $\mathbf{z}_{k} \in {\mathbb{R}}^{D_{\mathbf{z}}}$ describes an individual object (or background) in $\mathbf{x}$.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Energy-based Object-Centric Representation Learning", "weight": 1.0} -->

In this work, we make use of an EBM $E{(\mathbf{x},\mathbf{z};{\mathbf{θ}})}$, parameterized by $\mathbf{θ}$, to learn a joint energy function which assigns low energy to regions where the visual observation $\mathbf{x}$ and the latent object descriptors $\mathbf{z}$ are consistent, where $\mathbf{z} = {\{\mathbf{z}_{k}\}}_{k = 1}^{K}$ are a set of $K$ object-centric latent variables. To implement the mapping from a visual scene to its constituting objects, we can sample from the posterior distribution $\mathbf{z} \sim {p{(\left.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Energy-based Object-Centric Representation Learning", "weight": 1.0} -->

\mathbf{z} \middle| {\mathbf{x};{\mathbf{θ}}} \right.)}} \propto e^{- {E{(\mathbf{x},\mathbf{z};{\mathbf{θ}})}}}$ by using any efficient MCMC sampling algorithm, such as the stochastic gradient Langevin dynamics method and Hamiltonian Monte Carlo. Accordingly, the EBM $E$ can be used as a generic module for object-centric representation learning, offering great flexibility in which neural network architectures can be used and the functional form of the energy function.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Permutation Invariant Energy Function", "weight": 1.0} -->

One fundamental inductive bias in object-centric representation learning is encoding the permutation invariance of a set of objects into model learning. In this section, we introduce two formulations of the energy function $E{(\mathbf{x},\mathbf{z};{\mathbf{θ}})}$ that are permutation invariant with respect to the order of the object-centric latent variables $\{\mathbf{z}_{k}\}$.

<!-- chunk {"id": "body-0012", "role": "body", "section": "EGO by composing individual energy functions", "weight": 1.0} -->

The individual energy function ${E{(\mathbf{x},\mathbf{z}_{k};{\mathbf{θ}}_{k})}}:{{{\mathbb{R}}^{D_{\mathbf{x}}} \times {\mathbb{R}}^{D_{\mathbf{z}}}}\mapsto{\mathbb{R}}}$ can be any function that takes the observation $\mathbf{x}$ and a single latent variable $\mathbf{z}_{k}$ as input, and outputs a scalar energy value which quantifies the belief that an object with representation $\mathbf{z}_{k}$ is present in the visual scene $\mathbf{x}$. We share the parameters ${\mathbf{θ}}_{k}$ across all the individual energy functions $\theta_{k} = {\theta{\forall k}}$, such that it can generalize to an arbitrary number of objects without breaking symmetry.

<!-- chunk {"id": "body-0013", "role": "body", "section": "EGO by composing individual energy functions", "weight": 1.0} -->

The aggregation function $\phi$ is a permutation-invariant function with respect to the set $\{{E{(\mathbf{x},\mathbf{z}_{k})}}\}$. We can use any function $\phi$ that is invariant to the order of inputs, such as the sum, minimum, or parameterized transformations. Throughout this work, we use the sum as the aggregation function, which is effective in encouraging the model to learn to decompose the input into discrete objects and local variations, as explored. We call the resulting EBM formulation EGO-Sum, given by

<!-- chunk {"id": "body-0014", "role": "body", "section": "EGO from permutation equivariant/invariant transformations", "weight": 1.0} -->

We introduce another formulation of the energy function $E{(\mathbf{x},\mathbf{z};{\mathbf{θ}})}$ that composes multiple permutation equivariant/invariant transformations on top of the set $\{\mathbf{z}_{k}\}$ and $\mathbf{x}$. In particular, we use vanilla attention blocks, such as cross-attention and self-attention, to build up these differentiable mappings.

<!-- chunk {"id": "body-0015", "role": "body", "section": "EGO from permutation equivariant/invariant transformations", "weight": 1.0} -->

We then use a stack of $L$ standard transformer blocks with a cross-attention layer to fuse the information in $\mathbf{h}$ and the object-centric latent variables $\mathbf{z} = {\{\mathbf{z}_{k}\}}_{k = 1}^{K}$. Each block consists of a multi-head cross-attention layer, followed by a position-wise, fully connected feed-forward network. In each cross-attention layer, a linear transformation is applied to the image feature map $\mathbf{h}$ to produce queries over the set of latent variables. Cross-attention weights are then computed between the queries and linearly-projected keys and values from the set of latent variables $\{\mathbf{z}_{k}\}$. The stacked transformer blocks allow the model to sufficiently capture information from $\{\mathbf{z}_{k}\}$ by attending to the most relevant subset of latent variables at each image feature location, such that the model can learn to tell whether the set of latent variables fully explains each object.

<!-- chunk {"id": "body-0016", "role": "body", "section": "EGO from permutation equivariant/invariant transformations", "weight": 1.0} -->

We then use an average pooling layer to aggregate the final output of the transformer blocks $\mathbf{h}_{L} \in {\mathbb{R}}^{N_{\mathbf{h}} \times D_{\mathbf{h}}}$, into a single vector, which is then passed through a fully-connected layer to produce the scalar energy term.

<!-- chunk {"id": "body-0017", "role": "body", "section": "Learning and Inference", "weight": 1.0} -->

For tasks requiring a geometric understanding of a visual scene and reasoning over entities, our model can be used as a plug-and-play module to be integrated into existing architectures for encoding structured object-centric representations. Owing to the great flexibility of EGO's energy function and learning objective formulation, we can customize the model to adapt to a wide range of task contexts and learning desiderata.

<!-- chunk {"id": "body-0018", "role": "body", "section": "Learning and Inference", "weight": 1.0} -->

Among many possible training objective choices (e.g., maximum likelihood training with MCMC sampling or Contrastive Divergence ) to learn the model as a monolithic generative model, akin to the family of existing approaches for visual scene understanding and generation, we focus on investigating the potential of EGO as a generic standalone module for extracting object-centric representations, similar to. To this end, we adopt an encoder-decoder architecture, with our EGO module serving as the encoder to transform the unstructured observation into structured object representations, which are then decoded by a separate decoder into reconstructions or other task-specific predictions.

<!-- chunk {"id": "body-0019", "role": "body", "section": "Learning and Inference", "weight": 1.0} -->

Input: Image data x ∈ ℝDx, number of latent variables K, number of MCMC iterations T, step size ϵ Parameters: EGO E (x, z; θ), decoder Decoder(z; ϕ) Output: Training loss for unsupervised object discovery

<!-- chunk {"id": "body-0020", "role": "body", "section": "Encoding object-centric representations by MCMC sampling", "weight": 1.0} -->

To infer the set of object-centric latent variables $\mathbf{z}$ from the input $\mathbf{x}$, we use gradient-based MCMC sampling methods to sample from the posterior distribution $\mathbf{z} \sim {p{(\left. \mathbf{z} \middle| \mathbf{x} \right.)}} \propto e^{- {E{(\mathbf{x},\mathbf{z};{\mathbf{θ}})}}}$. Specifically, in this work we utilize the Langevin MCMC method. Starting from a random initialization $\mathbf{z}^{0}$ drawn from a simple prior distribution, we iteratively update the latent variables by simulating the Langevin diffusion process for $T$ steps, with step size $\epsilon$, as follows: where $\mathbf{z}^{t}$ denotes the latent variables at the $t$-th iteration.

<!-- chunk {"id": "body-0021", "role": "body", "section": "Encoding object-centric representations by MCMC sampling", "weight": 1.0} -->

When $\epsilon\rightarrow 0$ and $T\rightarrow\infty$, the sampling process converges to the true posterior distribution $p{(\left. \mathbf{z} \middle| \mathbf{x} \right.)}$ under some regularity conditions.

<!-- chunk {"id": "body-0022", "role": "body", "section": "Encoding object-centric representations by MCMC sampling", "weight": 1.0} -->

Though running MCMC sampling until convergence can be computationally expensive, we are simulating the Langevin dynamics in the latent space $\mathbf{z} \in {\mathbb{R}}^{K \times D_{\mathbf{z}}}$ rather than the high-dimensional pixel space, in contrast to previous works. We also only run Langevin dynamics for a relatively small number of iterations ($T < 10$) and find that it is sufficient to produce good latent variable samples $\mathbf{z}^{T}$ in our experiments. This allows us to make use of the gradient-based MCMC sampling in a much more efficient manner, even comparable to amortized inference methods.

<!-- chunk {"id": "body-0023", "role": "body", "section": "Training procedure", "weight": 1.0} -->

We outline the detailed training procedure in Algorithm 1, taking the unsupervised object discovery task as an example. Given the encoded structured representation $\mathbf{z}^{T} \sim {p{(\left. \mathbf{z} \middle| {\mathbf{x};{\mathbf{θ}}} \right.)}}$ from MCMC sampling, we use a decoder to map the set of latent variables to task-specific predictions.

<!-- chunk {"id": "body-0024", "role": "body", "section": "Training procedure", "weight": 1.0} -->

For unsupervised object discovery, we follow prior approaches and use a spatial broadcast decoder to decode each latent variable $\mathbf{z}_{k}$ separately into an alpha mask ${\mathbf{α}}_{k} \in {\lbrack 0,1\rbrack}^{D_{\mathbf{x}}}$ and input reconstruction ${\overset{\sim}{\mathbf{x}}}_{k}$, which are then combined to produce the final output $\overset{\sim}{\mathbf{x}} = \sum_{k = 1}^{K}{Softmax}{({\mathbf{α}})}_{k}{\overset{\sim}{\mathbf{x}}}_{k}$. The model can be trained end-to-end to minimize the reconstruction loss. For other tasks, we can use corresponding decoders to map latent variables to predictions and train the model end-to-end to minimize task-specific losses.

<!-- chunk {"id": "body-0025", "role": "body", "section": "Object-centric learning", "weight": 1.0} -->

Object-centric representation learning plays an important role in scene understanding, visual reasoning, and compositional generalization. Many research works like MONet, IODINE, GENESIS, and SPACE propose various probabilistic models to build a spatial mixture model of visual scenes and use variational inference to learn object-centric latent variables. Slot attention proposed a novel inverted attention mechanism to iteratively assign objects to slots, by introducing competition among slots via attention weight normalization. further applied the slot attention module to video data, and improved the approach by using fixed points as object representations, yielding better stability. Besides reconstruction-based object-centric learning, various works tackle the problem from the perspective of contrastive learning and self-supervised learning. Object-centric representations are also explored in other tasks such as visual question answering, visual reasoning, and neural scene rendering.

<!-- chunk {"id": "body-0026", "role": "body", "section": "Set generation", "weight": 1.0} -->

Set generation has received much attention in computer vision and natural language processing tasks in the past few years. explored using a cardinality-conditioned transformer for set prediction. The DETR model also adopted a transformer to predict a set of objects for the object detection task. The Deep Set Prediction Network (DSPN) proposed a set prediction approach by using a gradient optimization inner-loop with a permutation-invariant encoder to iteratively update the representation of the target set prediction by minimizing the distance between the input and output in a latent space induced by the encoder. Though the bi-level optimization framework is similar to ours, the DSPN model uses the deterministic gradient descent procedure to optimize a pre-defined loss function, while our formulation uses stochastic MCMC sampling to optimize a learned energy function. Our formulation brings more flexibility to the optimization process, and the introduced stochasticity also results in more robustness and diversity in both inference and generation (Section 4.3).

<!-- chunk {"id": "body-0027", "role": "body", "section": "Energy-based models", "weight": 1.0} -->

Energy-based models (EBMs) have been widely used in learning abstract concepts and controllable generation, due to the compositionality nature of the energy function. proposed an EBM-based framework for learning abstract concepts from observations, which enables compositional generalization by test-time optimization. explored the approach of using EBM to replace the hand-crafted permutation-invariance loss functions which aim to optimize the prediction output towards observable ground-truth data, it differs from our work in that we focus on learning the latent object-centric representations from the EBM for unsupervised object discovery and controllable scene manipulation. also proposed to use EBM to learn both local and global factors of variations from image data, where they proposed to train the model by a nested gradient descent optimization in the high-dimensional pixel space, which can be much more computationally expensive compared to our model which runs Langevin dynamics in the lower-dimensional latent space.

<!-- chunk {"id": "body-0028", "role": "body", "section": "Unsupervised Object Discovery", "weight": 1.0} -->

We quantitatively and qualitatively evaluate our proposed model on the task of unsupervised object discovery, with the goal of decomposing the visual scene into a set of objects without any human supervision. As we will show, our approach is able to consistently segment images into highly interpretable and meaningful object masks.

<!-- chunk {"id": "body-0029", "role": "body", "section": "Datasets", "weight": 1.0} -->

In line with previous state-of-the-art works on object discovery, we use the following three multi-object datasets: CLEVR, Multi-dSprites, and Tetrominoes. We also use a variant of the CLEVR dataset which filters out scenes with more than $6$ objects, referred to as CLEVR-$6$. Same as IODINE and Slot-Attention, the first $70$K samples from the CLEVR-$6$ dataset and the first $60$K samples from the Multi-dSprites and Tetrominoes datasets are used for training. Evaluation is performed on $320$ test data examples.

<!-- chunk {"id": "body-0030", "role": "body", "section": "Implementation", "weight": 1.0} -->

For the EGO model, we first encode the image input $\mathbf{x}$ using a CNN backbone. We use the same CNN architecture from Slot-Attention, which is augmented with positional embeddings for all results in this section. To condition our EGO-Sum model $E{(\mathbf{x},\mathbf{z};{\mathbf{θ}})}$ on the latent variables, we use an MLP to project $\mathbf{z}$ to a vector, replicating it to match the spatial dimension of the image features and concatenating it along the channel dimension. We process the joint features through a set of self-attention layers, followed by a global average pooling layer and a fully-connected layer to produce the final energy value. For the EGO-Attention model, we obtain the energy value from Equation 5 in Section. 2.1. We do not use dropout in our self-attention and cross-attention layers. To decode the inferred latent variables into reconstructions, we apply spatial broadcast decoding and use the same architecture from IODINE.

<!-- chunk {"id": "body-0031", "role": "body", "section": "Implementation", "weight": 1.0} -->

We use $D_{\mathbf{z}} = 64$ for the latent variable dimension, as in baseline methods. We use $K = 7$ latent variables for CLEVR-$6$, $K = 6$ for Multi-dSprites, and $K = 4$ for Tetrominoes, which is one more than the maximum number of objects in the corresponding datasets. In Langevin MCMC sampling, we set the step size $\epsilon = 0.1$ and the number of Langevin steps $T = 5$. We train the model using the Adam optimizer with a learning rate of $0.0002$ for $500$K iterations, with a batch size of $128$. Additional implementation details and results can be found in the Appendix.

<!-- chunk {"id": "body-0032", "role": "body", "section": "Segmentation accuracy", "weight": 1.0} -->

Following the evaluation protocol in existing literature, we use the Adjusted Rand Index (ARI) metric, which measures how accurately the model can decompose the scene into discrete objects. We compare our model against a variety of baseline methods, including Slot Attention, IODINE, and MONet. Similar to IODINE and Slot-Attention, we take the alpha masks generated by the spatial broadcast decoder for each latent variable, compute the clustering similarity with the ground truth masks using the ARI metric, and exclude the background in the evaluation. We report the ARI scores across different datasets in Table LABEL:tab:ari_object_discovery. As can be seen, EGO consistently outperforms the baselines, achieving near-perfect segmentation accuracy on CLEVR-$6$ and Tetrominoes, and substantially better results on Multi-dSprites compared to the existing state-of-the-art. Notably, there are more occlusions among objects presented in Multi-dSprites, which makes the task more challenging and demonstrates the effectiveness of our model in handling more complex scenes.

<!-- chunk {"id": "body-0033", "role": "body", "section": "Downstream prediction", "weight": 1.0} -->

To investigate the usefulness and quality of the learned representations, We evaluate our learned object-centric model on downstream object property prediction tasks. Similar to IODINE, we probe pre-trained models' learned representations by training a linear model on top of the latent variables to predict associated object properties, such as color, shape, size, and position. Thanks to the object-centric nature of baseline methods and our model, where object representations share a common format, we can train a single probing model to independently extract properties from each object-centric latent variable. We train the probing model by using the Hungarian algorithm to match the latent variables to the ground-truth objects. Following the same training and evaluation procedure described, we compare our pre-trained EGO-Attention model against baseline approaches across different datasets in Figure 2. We see that the learned representations from our model are highly informative for predicting object properties and are comparable to or outperform the competitive baseline methods on all datasets.

<!-- chunk {"id": "body-0034", "role": "body", "section": "Scene Decomposition and Manipulation", "weight": 1.0} -->

We next qualitatively study the learned object-centric representations by inspecting scene decompositions and visualizing the inference procedure. We also demonstrate the ability of our model to manipulate the scene by recomposing learned energy functions to dynamically manipulate scenes.

<!-- chunk {"id": "body-0035", "role": "body", "section": "Scene decomposition", "weight": 1.0} -->

We visualize per-latent variable reconstruction results from the trained EGO-Attention model across different datasets in Figure 3(a). The examples show that our model is able to decompose the scene into highly-interpretable segmentations, which align well with the ground-truth objects. Extra latent variables are assigned to the background when there are more latent variables than the number of objects in the scene. Our model learns to spread objects across latent variables without explicit supervision, and object properties are also well-preserved in the inferred representations. Meanwhile, when multiple objects occlude each other, the model is able to infer the correct parts of objects by leveraging other clues such as shape and color. We further visualize scene reconstructions at each MCMC sampling step in Figure 3(c), showing that the inferred scenes are iteratively refined within a few steps. We also plot the energy function values evaluated at each Langevin dynamics iteration from a trained model with $T = 10$ steps on the Tetrominoes dataset in Figure 3(b).

<!-- chunk {"id": "body-0036", "role": "body", "section": "Scene decomposition", "weight": 1.0} -->

As can be seen, both energy values are monotonically decreasing, indicating that the model can infer the latent variables by optimizing the energy function efficiently and stably.

<!-- chunk {"id": "body-0037", "role": "body", "section": "Scene manipulation", "weight": 1.0} -->

With trained EGO models, learned energy functions can be used to dynamically manipulate a scene's constituent objects. In Figure 4(a), we show that we can combine arbitrary objects from different visual observations ($\mathbf{x}_{1}$ and $\mathbf{x}_{2}$) together into a novel scene, by sampling the latent variables from the joint EBM ${E{(\mathbf{x},\mathbf{z};{\mathbf{θ}})}} = {{E{(\mathbf{x}_{1},\mathbf{z};{\mathbf{θ}})}} + {E{(\mathbf{x}_{2},\mathbf{z};{\mathbf{θ}})}}}$, known as product-of-experts, and reconstructing the scene from the inferred latent variables.

<!-- chunk {"id": "body-0038", "role": "body", "section": "Scene manipulation", "weight": 1.0} -->

A visualization of the scene reconstructions and predicted masks associated with each latent variable is also included in the figure, showing that, starting from the first few iterations, the model captures object components from both images and combines them across the latent variables to generate the complete scene. We additionally show another example in Figure 4(b), where we can remove any specific object from the scene by reusing learned energy functions. As described, we form a new energy function as ${E{(\mathbf{x},\mathbf{z};{\mathbf{θ}})}} = {{E{(\mathbf{x}_{1},\mathbf{z};{\mathbf{θ}})}} - {E{(\mathbf{x}_{2},\mathbf{z};{\mathbf{θ}})}}}$ to remove the objects shown in $\mathbf{x}_{2}$ from the scene $\mathbf{x}_{1}$.

<!-- chunk {"id": "body-0039", "role": "body", "section": "Scene manipulation", "weight": 1.0} -->

Similarly, we also illustrate the intermediate results at each sampling step, where we can see that in the first few steps of the sampling procedure, the model recovers the complete scene from $\mathbf{x}_{1}$, and then gradually removes the objects in $\mathbf{x}_{2}$ by optimizing the latent representations towards the region where $E{(\mathbf{x}_{2},\mathbf{z};{\mathbf{θ}})}$ is higher. These results clearly demonstrate that the EBM formulation of EGO allows us to control the scene composition combinatorically, leading to systematic generalization to unseen object combinations.

<!-- chunk {"id": "body-0040", "role": "body", "section": "Scene manipulation", "weight": 1.0} -->

(b) Energy evaluation during sampling. (c) Scene reconstructions at each step.

<!-- chunk {"id": "body-0041", "role": "body", "section": "Robustness and Generalization Evaluation", "weight": 1.0} -->

Finally, we evaluate the generalization capability of EGO to out-of-distribution (OOD) visual scenes and investigate its robustness with respect to model hyperparameters and component choices in an ablation study.

<!-- chunk {"id": "body-0042", "role": "body", "section": "Robustness and Generalization Evaluation", "weight": 1.0} -->

(a) ARI scores on test data with unseen object styles.

<!-- chunk {"id": "body-0043", "role": "body", "section": "Unseen object style", "weight": 1.0} -->

We first study the generalization capability of our learned object-centric representations to unseen object styles by altering the visual styles of objects presented in the test data distribution, including color, shape, and texture. Following, we apply a random color jitter transformation to the color of a random object in the scene in CLEVR and Tetrominoes. Unseen object textures are simulated by applying random neural style transfer to a random object in CLEVR and Multi-dSprites. We use the previously-trained model from the unsupervised object discovery task and evaluate it on these modified datasets to test whether the learned representations are able to generalize to unseen object styles. ARI scores of our model and other baseline methods are shown in Figure 5(a). Our model achieves strong generalization performance to unseen object colors, textures, and shapes on CLEVR and Multi-dSprites, consistently providing high-quality segmentation masks in the presence of OOD object styles. We provide more details about the datasets and evaluation in the appendix.

<!-- chunk {"id": "body-0044", "role": "body", "section": "Increasing the number of objects", "weight": 1.0} -->

To test how our model generalizes when more objects are present in the scene (compared to the training data), we increase the number of objects at test time. We construct a sequence of datasets by filtering CLEVR to only contain scenes with at most $\lbrack 7,8,9,10\rbrack$ objects, referred to as CLEVR-$\lbrack{7\text{-}10}\rbrack$ respectively. We use EGO-Attention trained on CLEVR-$6$ with $K = 7$ latent variables, and test it on the newly-constructed datasets by increasing the number of latent variables to one more than the maximum number of objects in the corresponding dataset. We compute the ARI scores for each dataset, and report the results in Figure 4(b). We use Slot-Attention with $3$ iterations (same as $T = 3$ in our model) as the baseline. As can be seen, the segmentation quality of our model remains robust to unseen numbers of objects in the test dataset, and suffers less from the increase in the number of objects than the baseline approach.

<!-- chunk {"id": "body-0045", "role": "body", "section": "Model ablation", "weight": 1.0} -->

We perform ablation studies to evaluate the robustness of our approach to different hyperparameters and study the effect of different components of our model, particularly the number of MCMC sampling steps $T$, the step size $\epsilon$, and the noise in Langevin dynamics. We first run grid search over the hyperparameters, including ${\epsilon \in {\{ 0.01,0.05,0.1\}}},{T \in {\{ 3,5,10\}}}$, number of attention blocks $\in {\{ 1,2,3\}}$, and dropout rate $\in {\{ 0.0,0.1\}}$, and report the ARI scores on the Multi-dSprites dataset in Figure 4(d). Our model is quite robust to a wide range of the values of both the step size and the number of sampling steps, and we obtain near-optimal segmentation performance with each combination of the hyperparameters.

<!-- chunk {"id": "body-0046", "role": "body", "section": "Model ablation", "weight": 1.0} -->

We then investigate the role of the noise used in the Langevin dynamics sampling by introducing a weight term to rescale the noise variable in Equation 6. We train EGO-Attention variants with different rescaling weights $\in {\{ 1.0,0.1,0.0\}}$ on the Multi-dSprites dataset and evaluate their ARI scores in both the original dataset and the modified OOD dataset with unseen object styles. The results in Figure 5(b) demonstrate that the stochasticity brought by the noise in Langevin dynamics gives our model more robustness and generalization to novel scene configurations.

<!-- chunk {"id": "body-0047", "role": "body", "section": "Conclusion", "weight": 1.5} -->

In this work we present EGO, a novel energy-based object-centric learning model. EGO successfully combines three essential ingredients of object-centric learning: (i) minimal assumptions on the generative process, (ii) minimal usage of potentially unexpressive specifically-designed neural modules, and (iii) explicitly modeling randomness to allow one-to-many mappings to reason about occluded or partially-observed objects. We empirically demonstrate that EGO can achieve state-of-the-art performance on various unsupervised object discovery tasks and excels at generalizing to OOD scenes. Meanwhile, controllable scene generation and manipulation are also feasible by reusing learned energy functions. These advantages make EGO a strong candidate for scaling unsupervised object-centric learning to real-world datasets, as a promising next step for future investigation.
