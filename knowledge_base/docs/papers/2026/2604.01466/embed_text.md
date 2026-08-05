<!-- arxiv-full-text:v1 {"arxiv_id": "2604.01466", "source": "arxiv-html"} -->

## Introduction

Understanding how traffic agents behave has many important applications in self-driving, from online motion forecasting for autonomy to offline traffic modeling for simulation. In these applications, a traffic scene typically consists of a set of geometric objects representing traffic agents, like vehicles and pedestrians, and contextual elements, like the map lane graph and traffic signals. Our goal is to learn an agent model that accurately predicts the actions of each agent in the scene from this context. This task has many symmetries, chief among which is equivariance to arbitrary 2D roto-translations of the scene; *i.e*., ${\text{SE}}$-equivariance. That is, if we apply a rigid transformation $\mathcal{T}\in{\text{SE}}$ to the input scene, the outputs of the model should also transform by that same rigid transformation, preserving their relative geometric relationships.

A natural question arises: how can we imbue our agent models with this equivariance? A common approach is to rely on data diversity. The hope is that with enough training examples, the model naturally learns a roughly equivariant function. While conceptually simple, this approach can be sample and compute inefficient and yet still struggle to generalize to new scenes as it is not truly equivariant. Alternatively, one can directly encode this property as an inductive bias into the model, designing the network architecture such that it is equivariant by construction. Approaches in this category typically explicitly model pairwise relationships between agents. For instance, one can transform the context around each agent into its own respective coordinate frame and process each agent's context independently or use pairwise relative positional encoding to process all agents simultaneously. Unfortunately, all of these approaches introduce an additional cost that scales quadratically with the number of agents, limiting its suitability to scale to ever larger scenes, models, datasets, *etc*.

In this paper, we propose DriveGATr, a novel architecture for modeling agents that achieves ${\text{SE}}$-equivariance without the computational cost of existing methods. Our approach builds on recent advances in geometric deep learning. In particular, we develop a novel extension of the Geometric Algebra Transformer (GATr) to ${\text{SE}}$-equivariance and new architectural primitives that improve its efficacy for agent modeling. First, we propose an efficient encoding of scene elements into the 2D projective geometric algebra ${\mathbb{R}^{*}_{2,0,1}}$, which allows for a native representation of 2D objects (*e.g*., points, lines) and operators (*e.g*., translations, rotations) as 8-dimensional multivectors. Next, we develop ${\text{SE}}$-equivariant neural network primitives, such as linear / bilinear layers, nonlinearities, normalization and scaled dot product attention. In addition, we design a new primitive to transform equivariant geometric representations into invariant features, since an agent's actions are ultimately invariant. These primitives form the basis of DriveGATr's transformer-based architecture.

Our approach has two key advantages. First, compared to non-equivariant models, DriveGATr is equipped with a geometric inductive bias that improves its expressivity, sample efficiency, and robustness to nuissance transformations. Second, unlike prior equivariant methods, DriveGATr achieves this without explicit pairwise relative positional encodings. Instead, it models geometric relationships between agents and scene elements using standard scaled dot product attention between multivectors, which have been heavily optimized. This gives us flexibility to improve the model's performance by growing each agent's context (*e.g*., to all agents or the entire lane graph) or scale to larger scenes, models, and datasets efficiently. Our experiments on the Waymo Open Motion Dataset confirm these attributes, showing that DriveGATr achieves comparable results to the state-of-the-art in traffic simulation while establishing a superior Pareto front in performance *vs*. computation cost compared to the baselines.

To summarize, we introduce DriveGATr, a tailoring of GATr to acheive efficient ${\text{SE}}$-equivariance with internal geometric algebra representations. We provide theoretical analysis showing it is provably equivariant by construction. We develop novel components targeted for agent modeling in self-driving, and empirically validate the effectiveness through extensive large scale experiments.

## Related work

### SE equivariance in traffic modeling

A natural symmetry in traffic modeling is equivariance to 2D roto-translations of the scene; *i.e*., SE equivariance. This symmetry gives rise to a powerful inductive bias for improving our traffic models' expressivity, efficiency, and generalization. Indeed, equivariant models tend to outperform their non-equivariant baselines at any compute or data budget. While the advantage of this inductive bias diminishes at scale, the scale required far exceeds that of any public self-driving datasets today, where equivariant models still top the leaderboards. Moreover, at a fixed compute budget, the optimal equivariant models are smaller, providing an additional inference time advantage.

To achieve SE equivariance, existing models explicitly compute relative poses between each pair of actors and map elements in the scene. In particular, state-of-the-art models like SMART use a transformer-based architecture that extends the attention dot product with Relative Positional Embeddings (RPE), where $\operatorname{RPE}(\text{pos}_{i\to j})$ featurizes the relative pose from $i$ to $j$. Explicitly computing pairwise RPEs scales quadratically with the number of scene elements, limiting the suitability of these models to scale to larger scenes, models, and datasets. Moreover, because they do not use standard scaled dot product attention, these models cannot use highly optimized attention kernels like FlashAttention.

To address this limitation, recent work have explored ways to avoid explicit RPEs. For example, DRoPE extends 1D rotary positional embeddings (RoPE) to 2D, modifying the attention dot product so that query and key embeddings are first transformed by blockwise rotation matrices $\mathbf{R}_{i}$ and $\mathbf{R}_{j}$ encoding poses of $i$ and $j$ While DRoPE bypasses the scalability issue, it lacks expressivity as it does not encode explicit geometric information about the scene elements. It is also translation-equivariant but not rotation-equivariant. Alternatively, VN-Transformer encodes poses as Vector-Neurons \[7-equivariant networks")\] and processes them with a transformer with SO equivariant layers. However, for numerical stability, VN-Transformer requires modifications that sacrifice true equivariance.

### Geometric Algebra Transformer

Recently, a novel method from geometric deep learning, called the Geometric Algebra Transformer (GATr), proposes an E-equivariant transformer-based architecture which represents geometric objects as elements of a projective geometric algebra. This projective geometric algebra provides a single, unified 16-dimensional algebraic structure to represent all types of geometric data, including points, lines, planes, rotations, and translations. GATr consists of E-equivariant network primitives, including equivariant attention, MLP, and normalization layers, which operate directly on these geometric algebra elements. Because it is built on the standard transformer framework, GATr is scalable, versatile, and efficient.

However, applying GATr directly to traffic agent modeling not only results in redundancy, but also inaccuracy. Notably, the original GATr architecture is $\text{E}$-equivariant, whereas a driving scene is only SE-equivariant due to gravity and right-hand traffic rules. In this work, we derive and implement efficient 2D geometric encodings and equivariant layers which operate on an algebraic structure using 8 dimensions instead of 16.

## DriveGATr

(a) Overview of the architecture.

(b) Multivector attention block.

(c) Equivariant MLP block.

Figure 1: The DriveGATr architecture. Figure 1(a) provides an overview. The poses and features of Nactor agents and Nmap nodes in each scene are encoded as multivectors in ℝ2, 0, 1* and scalars. These tensors are processed by N transformer blocks, each consisting of agent and map cross attention, temporal causal self-attention, equivariant MLPs and invariant adapters. Each of these modules contain skip connections, closely mimicking a standard transformer. Figure 1(b) describes the attention block. For all attention blocks, the query inputs are agent of interests. The key and value inputs are agents and map nodes for the cross attentions, attending across elements per-timestep. For self-attention, attention spans the temporal axis per-agent. Figure 1(c) describes the equivariant MLP block. Table 1 provides details on ℝ2, 0, 1* encodings. Section 3.4 provides details on each of the equivariant primitive layers. Section 3.5 describes the invariant adapter block.

This work is motivated by the goal of designing an efficient and expressive approach to equivariant traffic modelling. As we will see later, a key idea in our proposed method will be to extend the attention dot product with more invariant dot products. For example, if $h_{Q_{i}}$ and $h_{K_{j}}$ are 2D heading vectors, one could compute SE-invariant attention logits via so that query tokens attend more strongly to key tokens with similar heading. However, this naive example has several limitations: (i) $h_{Q_{i}}$ and $h_{K_{j}}$ are not learnable features, so this approach is not expressive; (ii) this only reasons about headings, and not positions; and (iii) in this example, the token features do not contain any explicit pose information. Using geometric algebra encodings will allow us to address all of these limitations.

The geometric algebra ${\mathbb{R}^{*}_{2,0,1}}$ gives us a unified and efficient way to represent 2D geometries, including points, lines, translations, and rotations. We will show how to encode 2D poses as elements of this algebra, called multivectors; in particular, the multivector representing the pose $(x,y,\theta)$ will have components corresponding to $x,y,\cos\theta$, and $\sin\theta$. To make our geometric features learnable, we will derive SE-equivariant layers $\mathcal{L}:{\mathbb{R}^{*}_{2,0,1}}\to{\mathbb{R}^{*}_{2,0,1}}$, including linear layers, normalization, and nonlinearities. The geometric algebra is also equipped with an invariant inner product $\langle\cdot,\cdot\rangle:{\mathbb{R}^{*}_{2,0,1}}^{2}\to\mathbb{R}$, which allows us to compute SE-invariant attention logits via where $Q^{MV}_{i}$ and $K^{MV}_{j}$ are multivector geometric features and $d^{MV}$ is the dimension of the invariant inner product. Notably, Equation 4 can be computed as standard dot-product attention via efficient kernels by concatenating $Q,K$ with (certain components of) $Q^{MV},K^{KV}$.

In the next sections, we first provide an overview of DriveGATr. We then provide a brief preliminary on generic geometric algebra and describe the details of DriveGATr, which is an efficient 2D extension of GATr with modifications for agent modeling. We refer the readers to the supplementary material for additional preliminaries.

### DriveGATr Architecture

Given a history of agent states $\mathcal{A}_{t}=\{a_{1}^{1:t},\dots,a_{N}^{1:t}\}$ and map nodes $\mathcal{M}=\{m_{1},\dots,m_{M}\}$, DriveGATr predicts an action for each agent: $\mu=\text{{\text{DriveGATr}}}(\mathcal{A},\mathcal{M})$ at the current timestep. A dynamics model $f$ advances the agent states: $a_{i}^{t+1}=f(a_{i}^{t},\mu_{i})$. We repeat this process to unroll the traffic scene in $T$ timesteps. By construction, the trajectories unrolled by the dynamics model are equivariant relative to the scene. Figure 1 provides an overview of the architecture.

For every token in $\mathcal{A}$ and $\mathcal{M}$, we encode its 2D global^11^1Theoretically, the choice of coordinate frame can be arbitrary due to SE equivariance, but for numerical stability we use the ego's initial pose. position $(x,y)$ with heading $\theta$ into a single multivector, using the bivector components to encode the point $(x,y)$, and the vector components to encode the line passing through $(x,y)$ with direction angle $\theta$.

We also encode invariant features in auxiliary scalars using a MLP. For agent states, we encode their speed and bounding box dimensions in the auxiliary scalars. For map segments, we encode their length, width, curvature, speed limit, and boundary types.

Our transformer consists of a sequence of factorized attention blocks, where each block consists of (i) multi-head cross attention between the agent states and map tokens, per timestep; (ii) multi-head self attention between the agent states, per timestep; (iii) multi-head causal self-attention between agent states, per agent; (iv) an equivariant MLP; and (v) an invariant adapter described in Section 3.5.

We use a final MLP on the auxiliary scalars to decode invariant action logits for each agent. We find it beneficial to attend agent states to the entire map in our cross-attention layer, rather than the nearest few map tokens.

### Geometric algebra

### Geometric product

The geometric product $xy$ of $x,y\in\mathbb{R}^{n}$ is a way of multiplying vectors together. The geometric product is defined to be bilinear and associative, and is characterized by the fundamental equation $v^{2}=\langle v,v\rangle$ where $\langle\cdot,\cdot\rangle$ is the standard inner product. This induces an algebra, called a Euclidean geometric algebra, whose elements are called multivectors. From the fundamental equation one can deduce that the geometric product is anticommutative on orthogonal basis vectors, i.e. $e_{i}e_{j}=-e_{j}e_{i}$ for $i\neq j$. Consequently, for $n=2$ the Euclidean geometric algebra consists of multivectors of the form $x=x^{\prime}+x_{1}e_{1}+x_{2}e_{2}+x_{12}e_{12}$, where $x^{\prime},x_{1},x_{2},x_{12}$ are real coefficients and $e_{12}:=e_{1}e_{2}$.

This structure is useful because it provides a unified framework for representing and manipulating geometric objects. For example, in 2D, we can rotate a vector $v=(x,y)$ by an angle $\theta$ using the geometric product: where we have used that $e_{1}^{2}=e_{2}^{2}=1$ and $e_{2}e_{1}=-e_{1}e_{2}$.

### Projective geometric algebra

Euclidean geometric algebra is only able to represent linear transformations. A translation is not a linear operation, but we can solve this by adding an extra, special dimension, similar to how homogeneous coordinates are used in computer graphics.

A projective geometric algebra is obtained by first adjoining an orthogonal basis vector $e_{0}$ to $\mathbb{R}^{n}$ with norm zero, that is, $e_{0}^{2}=0$. For $n=2$, the resulting algebra, denoted by ${\mathbb{R}^{*}_{2,0,1}}$, is 8-dimensional, spanned by the scalar 1, three vectors $e_{0},e_{1},e_{2}$, three bivectors $e_{01},e_{20},e_{12}$, and one pseudoscalar $e_{012}$.

### Geometric algebra primitives

We define additional geometric algebra primitives that will be useful later.

The *wedge product* is another way of multiplying vectors together, defined by $x\wedge y=(xy-yx)/2$. It is bilinear and associative, and has the property that $v\wedge v=0$ for any vector $v$. Also, for distinct basis vectors $e_{i},e_{j}$, from $e_{j}e_{i}=-e_{i}e_{j}$ one can derive that $e_{i}\wedge e_{j}=e_{i}e_{j}$ concides with the geometric product. The wedge product also extends to general multivectors.

The *multivector dual* $x\mapsto x^{*}$ is a linear operator, defined for a basis multivector $x$ as the multivector such that $x\wedge x^{*}$ equals the pseudoscalar.

The *join* operator of two multivectors is defined as $\textrm{Join}(x,y)=(x^{*}\wedge y^{*})^{*}$.

The $k$-*blade projection* $\langle x\rangle_{k}$ is defined to select specific components of a multivector $x\in{\mathbb{R}^{*}_{2,0,1}}$ We define the *invariant inner product* $\langle\cdot,\cdot\rangle$ between two multivectors in ${\mathbb{R}^{*}_{2,0,1}}$ as which ignores components containing $e_{0}$.

### Encodings

Counterclockwise rotation of angle θ $\cos\frac{\theta}{2}-\sin\frac{\theta}{2}e_{12}$ $\cos\frac{\theta}{2}+\sin\frac{\theta}{2}e_{12}$ Table 1: 2D encodings of geometries and transforms.

We encode 2D objects and transformations into ${\mathbb{R}^{*}_{2,0,1}}$ using Table 1 so that geometric features can be computed using the operations defined above. Following Brehmer et al., we encode 2D geometries and transforms such that the result of applying a transform to a geometry is given by a sandwich product. For example, if $t$ is a multivector representing a translation by $(a,b)$ and $p$ is a multivector representing the point $(x,y)$, then $tpt^{-1}$ is a multivector representing the point $(x+a,y+b)$. Given this property, we can state that a mapping $\mathcal{L}:{\mathbb{R}^{*}_{2,0,1}}\to{\mathbb{R}^{*}_{2,0,1}}$ is SE equivariant if for any roto-translation $u\in{\mathbb{R}^{*}_{2,0,1}}$ and input $x\in{\mathbb{R}^{*}_{2,0,1}}$, we have The encodings in Table 1 additionally satisfy the properties that (i) the intersection point of two lines $\ell_{1},\ell_{2}\in{\mathbb{R}^{*}_{2,0,1}}$ is given by their wedge product $p:=\ell_{1}\wedge\ell_{2}$; and (ii) the line joining two points $p_{1},p_{2}\in{\mathbb{R}^{*}_{2,0,1}}$ is given by a join operator $\ell:=\textrm{Join}(p_{1},p_{2})$. For a complete proof of the properties discussed above, please refer to the supplemental material.

### Equivariant layers

In this section we define the primitive equivariant layers of our model. For the full proofs that each of our layers satisfy Equation 12, please refer to the supplemental material.\Linear layers. We define $SE$-equivariant linear maps $\phi:{\mathbb{R}^{*}_{2,0,1}}\to{\mathbb{R}^{*}_{2,0,1}}$ by the form where $w_{k},v_{k},u_{k}$ are parameters and $\langle\cdot\rangle_{k}$ denotes blade projection. Since $\phi$ is linear and the map $x\mapsto uxu^{-1}$ is linear for any fixed operator $u$, to show that $\phi$ is equivariant it suffices to verify that $\phi(uxu^{-1})=u\phi(x)u^{-1}$ for any basis multivector $x$ and rotation or translation $u$; please refer to the supplement for details.

We then define affine layers between multivector arrays $\Phi:{\mathbb{R}^{*}_{2,0,1}}^{c}\to{\mathbb{R}^{*}_{2,0,1}}^{c^{\prime}}$ via where $\phi^{(i,j)}$ are equivariant linear layers and $b_{i}$ are learnable scalar bias terms.\Geometric bilinears. To increase expressivity, we include the geometric product which is equivariant as $(uxu^{-1})(uyu^{-1})=u(xy)u^{-1}$ for any $x,y$ and operator $u$, and we include the join operator which is also equivariant Brehmer et al.. These are combined to form the equivariant geometric layer $\textrm{Geometric}(w,x,y,z)=\textrm{Concatenate}(wx,\textrm{Join}(y,z))$.\Nonlinearities and normalization. We define the equivariant scalar-gated activation $\textrm{GatedRELU}(x)=\textrm{RELU}(\langle x\rangle_{0})x$. We define equivariant normalization over channels by $\textrm{LayerNorm}(x)=x/\sqrt{\mathbb{E}\langle x,x\rangle+\varepsilon}$ where $\langle\cdot,\cdot\rangle$ is the invariant inner product.\Scaled dot-product attention. For multivector query and key tokens $q,k\in{\mathbb{R}^{*}_{2,0,1}}^{C}$, the corresponding invariant attention logit may be computed as where $\langle\cdot,\cdot\rangle$ is the invariant inner product. We find it crucial to follow Brehmer et al. and extend the query and key multivectors with "distance awareness" features which have the property that $\phi(q)\cdot\psi(k)$ is invariant, and moreover if the bivector components of $q$ and $k$ represent points with $q_{12}=k_{12}=1$ then $\phi(q)\cdot\psi(k)=-\frac{1}{(1+\varepsilon)^{2}}[(k_{01}-q_{01})^{2}+(k_{20}-q_{20})^{2}]$ which is proportional to the negative squared distance between the two points.

Combining the multivector features, extended features, and auxiliary scalar features $q^{s},k^{s}\in\mathbb{R}^{C^{\prime}}$, the invariant attention logits are computed as As in a standard transformer, the attention logits are softmaxed and used to take a linear combination of the value tokens. Notably, Equation 18 can be computed as one dot-product by concatenating the three terms for both query and key, allowing drop-in usage of efficient attention kernels.

### Invariant adapter

The output of our model is an invariant action which can be decoded from the auxiliary scalar features. However, the multivector features contain important geometric information that should be used as well. To this end, we introduce a novel transform which converts each agent's equivariant geometric features into invariant features by transforming the multivectors into a local coordinate frame.

Specifically, given equivariant multivector features $v\in{\mathbb{R}^{*}_{2,0,1}}^{N\times d}$ and auxiliary scalar features $s\in\mathbb{R}^{N\times d^{\prime}}$, for each agent $n=1,\ldots,N$ we compute where $u_{n}\in{\mathbb{R}^{*}_{2,0,1}}$ is the roto-translation transforming global poses into the coordinate frame of agent $n$. Similar to all other layers, Equation 19 is batched across scenes and agent.

For each $n$, $u_{n}v_{n}u_{n}^{-1}$ is invariant because it converts global equivariant features $v_{n}$ into agent-centric features. Therefore, this transform preserves the invariance of the auxiliary scalars.

## Params

Table 2: Results on WOSAC 2024 validation set. RMM is the Realism Meta Metric used for ranking. DriveGATr achieves the best RMM among its baselines. Compared to publicly available state-of-the-art methods, DriveGATr achieves comparable realism without top-k sampling and closed-loop fine-tuning.

## Experiments

We evaluate DriveGATr in traffic simulation --- a representative task for modeling traffic agents. Our experiments demonstrate two key properties: comparable performance to the state-of-the-art; and a superior Pareto front in performance *vs*. computational costs compared to prior work.

### Comparison to state-of-the-art

In traffic simulation, equivariant models top the leaderboard but sacrifice computational efficiency due to their explicit relative positional encodings. We propose DriveGATr as an alternative that achieves SE-equivariance without the high computational costs of existing methods. Our first experiment seeks to answer the question: Does DriveGATr match the state-of-the-art?

### Dataset & metrics

We evaluate our method on the Waymo Open Motion Dataset (WOMD) using the protocol proposed by the Waymo Open Sim Agents Challenge (WOSAC). Given 1s of context in a traffic scenario, the task is to generate 32 rollouts of 8s closed-loop simulations at 10 Hz, each containing the trajectories of every agent in the scenario. The rollouts are evaluated using distribution matching metrics along three dimensions--- kinematic, interactive, and map-based metrics---which are then summarized into a single Realism Meta-Metric (RMM) score. We also report the lowest displacement error, averaged over time, across rollouts (minADE).

### Baselines

We compare against the state-of-the-art on WOSAC: BehaviorGPT, SMART, and CAT-K. BehaviorGPT and SMART use explicit relative positional encodings (RPEs). CAT-K further trains SMART with closed-loop fine-tuning.

We also compare against four baselines representative of how state-of-the-art methods achieve SE-equivariance. These baselines share the same base architecture and learning algorithm as DriveGATr, differing only in how they introduce equivariance. Transformer is a scene-centric model that uses roto-translation data augmentation to approximate equivariance and is based on Trajeglish. Transformer + DRoPE uses rotary positional encodings (RoPE) to achieve translation (but not rotation) equivariance. We faithfully reproduce DRoPE using publicly available information. Transformer + RPE uses explicit RPEs to achieve equivariance. Like other methods that use RPEs, we limit each agent's context to a neighbourhood (eight agents and four map tokens) so that it fits in GPU memory during training.

### Implementation details

We use a clustered discretized action space. Starting with a large number of state-to-state transitions, we use a k-disk procedure to select a vocabulary of 2048 actions for each agent class (vehicle, cyclist, pedestrian). We then use this vocabulary to discretize the trajectories in our training dataset, and use a cross entropy loss to train our model to predict the next action for each agent. We use 16 multivector channels, and six factorized attention blocks. Our 3M variant uses auxilliary dimension 128 for a total of 2.7 million parameters, and our 30M variant uses auxilliary dimension 512 for 29.4 million parameters. Similar to prior methods, we embed each query token with its prediction at the last timestep as well as its actor class. For all models and baselines, we train for 250,000 steps with learning rate $10^{-3}$ and cosine annealing. We conduct analysis on the 3M variant, except for the comparison in Table 2, for efficiency purposes.

### Results

Table 2 reports results on the WOSAC 2024 validation set. DriveGATr achieves comparable realism scores to the state-of-the-art despite its relatively small model size. In fact, DriveGATr achieves a 2% improvement in RMM over BehaviorGPT---a state-of-the-art model of similar size. The 30M variant of DriveGATr achieves comparable RMM with SMART, the top method on the WOSAC leaderboard. For simplicity, we did not explore closed-loop fine-tuning, top-$k$ sampling, and nucleus sampling in our experiments, but we expect that these techniques will improve performance if tuned properly.

DriveGATr marks a significant improvement over our baselines, despite sharing largely the same base architecture. From a modeling perspective, DriveGATr has two important advantages over the baselines: in contrast to Transformer and Transformer + DRoPE, DriveGATr is SE-equivariant by construction; and in contrast to Transformer + RPE, DriveGATr can grow each agent's context to encompass all agents and map tokens in the scene whereas the baseline is limited to a small neighbourhood due to the memory footprint of its explicit RPEs.

Figure 2: Training curves. We compare the envelope of minimal training loss per FLOP (left), compute efficiency as the number of agents scale (middle), and sample efficiency as the training dataset grows (right). Compared to the baselines, DriveGATr establishes a superior Pareto front in performance and computation cost thanks to its compute and sample efficiency.

### Scaling analysis

Our next set of experiments evaluate DriveGATr's scalability with respect to training compute and data.

### Experiment setup

For each of our baselines, we train two models with varying training FLOP profiles on the full WOMD training dataset. In our experiments, we vary batch size since we found that varying model size, learning rates, *etc*. was inconsequential. Then, for each training run, we smooth its training loss curve with Gaussian smoothing. Finally, from these training loss curves, we extract the envelope of minimal training loss per FLOP. This training loss envelope gives us an estimate of how each baseline's performance improves as we scale the available training compute.

### Results

Figure 2 (left) shows that DriveGATr's training loss envelope is significantly lower than those of the baselines. For any number of training FLOPs, DriveGATr achieves the lowest training loss, demonstrating its superior scalability with training compute. This comes down to DriveGATr's two key advantages: higher sample efficiency due to SE-equivariance; and higher compute efficiency due to how it achieves SE-equivariance.

To demonstrate DriveGATr's compute efficiency, we analyze how each model's number of FLOPs scale with number of agents during inference. From Figure 2 (middle), we see that DriveGATr has significantly lower computational overhead than Transformer + RPE. The latter requires computing explicit RPE, which introduces an additional overhead that is quadratic in the number of agents. DriveGATr avoids this overhead by modeling geometric relationships using standard attention between multivectors.

To demonstrate DriveGATr's sample efficiency, for each model family, we train on a range of dataset sizes: 1%, 10%, 50%, and 100%. Next, we plot each model's RMM on the validation split against the number of scenarios seen during training. Following Zhang et al., we evaluate on 2% of the validation set due to the high cost of evaluation. In Figure 2 (right), we see an intuitive ordering---models with more inductive bias built in tend to have higher sample efficiency.

### Additional analysis

Figure 3: Robustness to roto-translations. We compare Transformer (left), Transformer + DRoPE (middle), and DriveGATr (right)’s robustness to roto-translations. In each figure, we overlay rollouts from the original coordinate frame vs one rotated by 90°and translated by 100m forward. Blue trajectories visualize model predictions in the original input, and red visualize predictions in the transformed scene. DriveGATr produces consistent trajectories despite closed-loop execution, demonstrating its robustness to roto-translations.

### Robustness to roto-translations

SE-equivariance not only improves sample efficiency but also robustness to nuissance transformations. In Figure 4, we compare DriveGATr's robustness to roto-translations against Transformer and Transformer + DRoPE. In each figure, we overlay rollouts from when the model is given inputs in its original coordinate frame *vs*. one rotated by 90°and translated by 100m forward. Note that for each rollout, instead of sampling, the model at each timestep executes its highest scored action. As expected, Transformer is not robust to roto-translations---its rollouts change significantly when given the same inputs from different coordinate frames. Likewise, Transformer + DRoPE is not robust because it is not rotation equivariant. In contrast, DriveGATr is robust because it has a mathematical guarantee for SE-equivariance.

Table 3: Ablation studies on the WOSAC 2% validation split. On the top, we ablate the importance of the invariant adapter (IA) and distance-awareness (DA). On the bottom, we ablate the number of map tokens each agent attends to in agent-to-map attention.

### Ablation studies

In Table 3, we ablate two of DriveGATr's key architectural choices on the 2% validation set, namely (i) whether we use the invariant adapter after each factorized attention block (including the last one) and (ii) whether we use distance-awareness in DriveGATr's attention layers. From the left side of Table 3, we observe that both architectural choices improve DriveGATr's realism. For the invariant adapter, we see improvements in minADE only whereas for distance-awareness, we see improvements across both metrics. This matches our intuitions that there is important geometric information in the multivector features that should be mixed into the auxiliary scalars, and that agents should attend to nearby agents and map tokens.

### Latency

We provide memory footprint and latency comparisons in the supplementary material. We note that DriveGATr is faster and more memory efficient than the fully invariant baseline Transformer + RPE.

## Conclusion

SE equivariance is an inherent symmetry in agents modeling problems. It is a ubiqutous inductive bias in state-of-the-art agent traffic simulation models, improving their expressivity, sample efficiency, and robustness to nuissance transformations. However, existing approaches achieve this with high computational costs. We propose DriveGATr, a novel architecture for modeling traffic agents that guarantees SE equivariance yet avoids the high computational costs of existing approaches. By leveraging efficient 2D geometric algebra encodings and the equivariant layer primitives, DriveGATr is expressive, efficient and provably equivariant.

### Limitations and broader impact

Although ${\text{SE}}$ is a useful equivariance property for agent modeling, self-driving is ultimately a 3D problem. DriveGATr models equivariance in 2D but, like prior work, it can be easily extended to 2.5D by adding the height dimension to the auxiliary scalar features. Another possibility is combining our method of acheiving ${\text{SE}}$ equivariance in the $xy$-plane, with translational invariance in the $z$-axis. While we only evaluate DriveGATr in traffic simulation, we believe it is extensible to similar tasks like motion forecasting and ML-based planning. We also highlight that DriveGATr is capable of making not just invariant but equivariant predictions in the global coordinate frame, making it a suitable architectural choice for more challenging problems such as traffic scenario generation. We leave this direction for future work.
