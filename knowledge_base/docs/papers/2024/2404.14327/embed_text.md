## Introduction

Learning-based planning has emerged as a potentially scalable approach for autonomous driving, attracting significant research interest. Imitation-based planning, in particular, has demonstrated noteworthy success in simulations and real-world applications. Yet, the efficacy of learning-based planning remains unsatisfactory. As indicated , conventional rule-based planning outperforms all learning-based alternatives, winning the 2023 nuPlan planning challenge. This paper delineates the principal challenges inherent in learning-based planning and presents our novel solutions, aimed at pushing the boundaries of what is achievable with learning-based planning.

The first challenge lies in acquiring multi-modal driving behaviors. It is observed that while learning-based planners are good at learning longitudinal tasks such as lane following, they struggle with lateral tasks, for instance, executing lane changes or navigating around obstacles, even when space permits. We attribute this deficiency to the absence of explicit lateral behavior modeling within the architectural design of the model. Our previous work attempted to address this issue by generating plans that are explicitly conditioned on nearby reference lines, though it was restricted to producing a maximum of three proposals and did not effectively integrate lateral and longitudinal behavior modeling. In the present study, we enhance this approach through the adoption of a query-based architecture capable of generating an extensive array of proposals by fusing longitudinal and lateral queries. The advanced model design enables our planner to demonstrate diverse and flexible driving behaviors, which we believe is a crucial step toward practical learning-based planning.

Beyond the model architecture, it is recognized that pure imitation learning encompasses inherent limitations, including the propensity for learning shortcuts, distribution shift, and causal confusion issues. This paper addresses these pervasive challenges across three dimensions: \(1\) Learning beyond pure imitation loss. We concur with previous studies that solely relying on imitation loss is insufficient for learning desired driving behaviors. It is imperative to impose explicit constraints during the training phase, particularly within the safety-critical realm of autonomous driving. A prevalent approach is to add auxiliary losses to penalize adverse behaviors, such as collisions and off-road driving, as previously demonstrated. However, their methods are either designed for heatmap-based output or need a differentiable rasterizer that renders each trajectory point into an image. As a result, the output resolution is restricted to reduce the computation burden. It remains unclear how to realize these losses efficiently for the more modern vector-based models. To bridge this gap, we introduce a novel auxiliary loss calculation methodology predicated on differentiable interpolation. This method not only spans a broad spectrum of auxiliary tasks but also facilitates batch-wise computation within modern deep-learning frameworks, thereby enhancing its applicability and efficiency.

\(2\) New data augmentations. Issues arise when the model undergoes open-loop training and closed-loop testing. For instance, the accumulation of errors over time may lead to input data deviating from the training distribution; the model may rely on unintended shortcuts rather than acquiring knowledge. Data augmentations have been extensively employed to alleviate these problems and have demonstrated effectiveness, *e.g*., perturbation-based augmentations teach the model to learn to recover from small deviations and dropout-based augmentations prevent learning shortcuts. In addition to these two augmentations, we introduce further augmentation techniques aimed at regulating driving behavior and enhancing interaction learning.

\(3\) Learning by constrast. Imitation learning-based models often struggle to recognize underlying causal relationships due to the absence of interactive feedback with the environment. This issue can significantly hinder performance; for instance, a planner may decelerate by mimicking the behavior of nearby agents rather than responding to a red light. Our goal is to address this issue without substantially complicating the training process, as would be the case with reinforcement learning or employing a data-driven simulator. Drawing inspiration from the effectiveness of contrastive learning, which enhances representation by differentiating between similar and dissimilar examples, we recognize an opportunity to infuse the model with causal understanding. This is achieved by enabling the model to differentiate between original and modified input data---for example, by excluding the leading vehicles from the autonomous vehicle's (AV's) perspective. Building on this approach and the two previously mentioned strategies, we introduce a novel unified framework termed Contrastive Imitation Learning (CIL).

In summary, this study introduces a comprehensive, data-driven planning framework named Pluto, designed to Push the Limit of imitation learning-based planning for aUTOnomous driving. Pluto incorporates innovative solutions in model architecture, data augmentation, and the learning framework. It has been evaluated using the large-scale real-world nuPlan dataset, where it has demonstrated superior closed-loop performance. Notably, Pluto surpasses the existing state-of-the-art rule-based planner PDM for the first time, marking a significant milestone in the field. Our main contributions are: We introduce a query-based model architecture that simultaneously addresses lateral and longitudinal planning maneuvers, enabling flexible and diverse driving behaviors.

We propose a novel method for calculating auxiliary loss based on differential interpolation. This method is applicable to a broad spectrum of auxiliary tasks and allows for efficient batch-wise computation in vector-based models.

We present the Contrastive Imitation Learning (CIL) framework, accompanied by a new set of data augmentations. The CIL framework is aimed at regulating driving behaviors and enhancing interaction learning, without significantly increasing the complexity of training.

Our evaluation on the large-scale nuPlan dataset demonstrates that Pluto achieves state-of-the-art performance in closed-loop planning. Our model and benchmark are publicly available.

## Related Work

### II-A Imitation-based Planning

Learning to drive by cloning the policies of experienced drivers is likely the most direct and scalable solution to autonomous driving, considering the abundance and affordability of data today. One of the popular methods is end-to-end (E2E) driving. This approach directly learns driving policies from raw sensor data and has made significant strides in a relatively short period. Initially, the focus was on convolutional neural network (CNN)-based models that mapped camera inputs to control policies. This evolved to incorporate more sophisticated methods that utilized multi-sensor fusion. More recently, developments spearheaded by entities such as LAV and UniAD have shifted towards a module-based E2E architecture. This approach integrates the processes of perception, prediction, and planning within a unified model. Despite their potential, most E2E strategies extensively depend on high-fidelity simulation environments like CARLA for both training and evaluation. Consequently, these methodologies are plagued by several issues, including a lack of realism and diversity in simulated agents, reliance on imperfect rule-based experts, and the imperative need to bridge the simulation-to-reality gap for applicability in real-world scenarios.

This paper focuses on another research direction, commonly referred to as the mid-to-mid approach, which employs post-perception results as input features. The primary advantage of this method is that the model can concentrate on learning to plan and be trained with real-world data, eliminating sim-to-real transfer concerns. Pioneering approaches such as ChauffeurNet, SafetyNet, and UrbanDriver have demonstrated the ability to operate autonomous vehicles in real-world environments, with subsequent works building upon these foundations. These approaches benefit significantly from advancements in the motion forecasting community, including the adoption of vector-based models that excel in prediction tasks, replacing early planning models based on rasterized bird's-eye-view images. However, many of these models overlook the inherent characteristics of planning tasks, such as the need for closed-loop testing and active decision-making capabilities. In contrast, our proposed framework is specifically designed for planning from the outset. Our network jointly models longitudinal and lateral driving behaviors through a query-based architecture, enabling a flexible and diverse driving style.

Prior studies have demonstrated the limitations of basic imitation learning and suggested methods for enhancement. In order to address compounding errors, an early solution can be traced back to DAgger, which interactively refines the trained model by incorporating additional expert demonstrations. Subsequently, ChauffeurNet introduced perturbation-based augmentation, enabling the model to recover from minor deviations and establishing a standard practice for later research. Adding auxiliary losses such as collision loss and off-road loss is another important aspect to improve the overall performance. However, their method is either designed for heatmap output or requires a differentiable rasterizer that converts the trajectory into a sequence of images with kernel functions. These approaches are not efficiently applicable to vector-based methods. Our research contributes to this field by introducing a novel technique that employs differentiable interpolation to bridge this gap.

### II-B Contrastive Learning

Contrastive learning is a framework that learns representation by comparing similar and dissimilar pairs, achieving significant success in computer vision and natural language processing. Within the context of autonomous driving, a few attempts have been made for motion prediction. Social NCE introduced a social contrastive loss to guide goal generation in pedestrian motion forecasting. Marah et al. utilized action-based contrastive learning loss to refine learned trajectory embeddings. FEND employed this approach to recognize long-tail trajectories. These studies underscore the potency of contrastive learning in incorporating domain-specific knowledge into models through the careful selection of positive and negative examples. In our research, we extend its application to the planning domain, aiming to improve driving behavior predictions and facilitate the understanding of implicit interactions among vehicles. As generating negative samples is crucial to contrastive methods, we also introduce a new set of data augmentation functions that defines the contrastive task.

## Methodology

Figure 1: The architectural overview of the Pluto model is presented in this section. The model initiates lateral queries Qlat using a polyline encoder based on adjacent reference lines. Simultaneously, longitudinal queries Qlon are established as learnable embeddings. These queries undergo a fusion process via factorized lateral-longitudinal self-attention layers. This integration serves as a basis for the subsequent decoding of trajectories and their associated scores.

### III-A Problem Formulation

In this study, we explore the task of autonomous driving within dynamic urban settings, considering the autonomous vehicle (AV), $N_{A}$ dynamic agents, $N_{S}$ static obstacles, a high-definition map $M$, and other traffic-related contexts $C$ such as traffic light status. We define the features of agents as $\mathcal{A} = A_{0:N_{A}}$, where $A_{0}$ represents the AV, and static obstacles are denoted by $\mathcal{O} = O_{1:N_{S}}$. Additionally, we denote the future state of agent $a$ at time $t$ as ${\mathbf{y}}_{a}^{t}$, with the historical and future horizons represented by $T_{H}$ and $T_{F}$, respectively. Our proposed system, Pluto, is designed to simultaneously generate $N_{T}$ multi-modal planning trajectories for the AV and a prediction for each dynamic agent. The selection of the final output trajectory, $\tau^{\ast}$, is executed by a scoring module, $\mathcal{S}$, which integrates learning-based outcomes with all scene contexts. Pluto is formulated as follows: | | | ${{{({\mathbf{T}}_{0},{\mathbf{π}}_{0})},{\mathbf{P}}_{1:N_{A}}} = {f{(\mathcal{A},\mathcal{O},M,\left. C \middle| \phi \right.)}}},$ | | \(1\) | | | | ${{(\tau^{\ast},\pi^{\ast})} = {\underset{{(\tau,\pi)}\in{({\mathbf{T}}_{0},{\mathbf{π}}_{0})}}{\text{arg max}}\mathcal{S}{(\tau,\pi,{\mathbf{P}}_{1:N_{A}},\mathcal{O},M,C)}}},$ | | | where $f$ denotes the neural network of Pluto, $\phi$ is the model parameters, ${({\mathbf{T}}_{0},{\mathbf{π}}_{0})} = \left. \{{({\mathbf{y}}_{0,i}^{1:T_{F}},\pi_{i})} \middle| {i = {1\ldots N_{T}}}\} \right.$ is AV's planning trajectories and corresponding confidence scores, ${\mathbf{P}}_{1:N_{A}} = \left. \{{\mathbf{y}}_{a}^{1:T_{F}} \middle| {a = {1\ldots N_{A}}}\} \right.$ are agents' predictions. The subsequent sections provide a detailed illustration of each component within the Pluto framework.

### III-B Input Representation and Scene Encoding

### Agent History Encoding

The observational state of each agent at any given time $t$ is denoted as ${\mathbf{s}}_{i}^{t} = \left( {\mathbf{p}}_{i}^{t},\theta_{i}^{t},{\mathbf{v}}_{i}^{t},{\mathbf{b}}_{i}^{t},{\mathbb{I}}_{i}^{t} \right)$, where $\mathbf{p}$ and $\theta$ represent the agent's position coordinates and heading angle, respectively; $\mathbf{v}$ refers to the velocity vector, $\mathbf{b}$ defines the dimensions (length and width) of the perception bounding box; and $\mathbb{I}$ is a binary indicator signifies the observation status of this frame. We convert the history sequence into vector form by calculating the difference between consecutive time steps: ${\hat{\mathbf{s}}}_{i}^{t} = \left( {{\mathbf{p}}_{i}^{t} - {\mathbf{p}}_{i}^{t - 1}},{\theta_{i}^{t} - \theta_{i}^{t - 1}},{{\mathbf{v}}_{i}^{t} - {\mathbf{v}}_{i}^{t - 1}},{\mathbf{b}}_{i}^{t},{\mathbb{I}}_{i}^{t} \right)$, resulting in agent's feature vector $F_{A} \in {\mathbb{R}}^{N_{A} \times {({T_{H} - 1})} \times 8}$. To extract and condense these historical features, we employ a neighbor attention-based Feature Pyramid Network (FPN), which produces an agent embedding $E_{A} \in {\mathbb{R}}^{N_{A} \times D}$, with $D$ representing the dimensionality of the hidden layers used consistently throughout this paper.

### Static Obstacles Encoding

In contrast to motion forecasting tasks where static obstacles are often overlooked, the presence of static obstacles is crucial for ensuring safe navigation. Static obstacles encompass any entities that an AV must not traverse, such as traffic cones or barriers. Each static obstacle within the drivable area is represented by ${\mathbf{o}}_{i} = \left( {\mathbf{p}}_{i},\theta_{i},{\mathbf{b}}_{i} \right)$. We use a two-layer multi-layer-perceptron (MLP) to encode static objects features ${\mathbf{F}}_{O} \in {\mathbb{R}}^{N_{S} \times 5}$, resulting in embedding ${\mathbf{E}}_{O} \in {\mathbb{R}}^{N_{S} \times D}$.

### AV's State Encoding

Drawing on insights from previous studies that imitation learning tends to adopt shortcuts from historical states, thereby detrimentally affecting performance, our approach only utilize the current state of AV as the input feature. This current state encompasses the AV's position, heading angle, velocity, acceleration, and steering angle. To encode the state feature while avoiding the generation of trajectories based on extrapolated kinematic states, we employ an attention-based state dropout encoder (SDE), as suggested . The encoded AV's embedding is ${\mathbf{E}}_{AV} \in {\mathbb{R}}^{1 \times D}$.

### Vectorized Map Encoding

The map consists of $N_{P}$ polylines. These polylines undergo an initial subsampling process to standardize the quantity of points, followed by the computation of a feature vector for each point. Specifically, for each polyline, the feature of the $i$-th point encompasses eight channels: $({{\mathbf{p}}_{i} - {\mathbf{p}}_{0}},{{\mathbf{p}}_{i} - {\mathbf{p}}_{i - 1}},{{\mathbf{p}}_{i} - {\mathbf{p}}_{i}^{\text{left}}},{{\mathbf{p}}_{i} - {\mathbf{p}}_{i}^{\text{right}}})$. Here, ${\mathbf{p}}_{0}$ denotes the initial point of the polyline, while ${\mathbf{p}}_{i}^{\text{left}}$ and ${\mathbf{p}}_{i}^{\text{right}}$ represent the left and right boundary points of the lane, respectively. Incorporating the boundary feature is crucial as it conveys information about the drivable area, essential for planning tasks. The features of the polylines are represented as $F_{P} \in {\mathbb{R}}^{N_{P} \times n_{p} \times 8}$, where $n_{p}$ denotes the number of points per polyline. To encode the map features, a PointNet-like polyline encoder is employed, resulting in an encoded feature space $E_{P} \in {\mathbb{R}}^{N_{P} \times D}$.

### Scene Encoding

To effectively capture the intricate interactions among various modal inputs, we concatenate different embeddings into a single tensor $E_{0} \in {\mathbb{R}}^{{({N_{A} + N_{S} + N_{P} + 1})} \times D}$. This tensor is subsequently integrated using a series of $L_{enc}$ Transformer encoders. Due to the vectorization process, the input features are stripped of their global positional information. To counteract this loss, a global positional embedding, denoted as $PE$, is introduced to each embedding. Following, $PE$ represents the Fourier embedding of the global position $({\mathbf{p}},\theta)$, utilizing the most recent positions of agents and static obstacles as well as the initial point of polylines. Additionally, to encapsulate inherent semantic attributes such as agent types, lane speed limits, and traffic light statuses, learnable embeddings $E_{attr}$ are incorporated alongside the input embeddings. $E_{0}$ is initialized as The $i$-th layer of the Transformer encoder is formulated as | | | ${{\hat{E}}_{i - 1} = {\text{LayerNorm}{(E_{i - 1})}}},$ | | \(3\) | | | | ${E_{i} = {E_{i} + {\text{FFN}\left({\text{LayerNorm}{(E_{i})}} \right)}}},$ | | | where $\text{MHA}{(q,k,v)}$ is the standard multi-head attention function, FFN is the feedforward network layer. We denote $E_{enc}$ as the output of the final layer of the enoder.

### III-C Multi-modal Planning Trajectory Decoding

The task of planning in autonomous driving is inherently multimodal, as there are often multiple valid behaviors that could be adopted in response to a given driving scenario. For instance, a vehicle might either continue to follow a slower vehicle ahead or opt to change lanes and overtake it. To address this complex issue, we utilize a query-based, DETR-like trajectory decoder. However, directly implementing the learned anchor-free queries has been found to result in mode collapse and training instability, as evidenced . Drawing inspiration from the observation that driving behaviors can be decomposed into combinations of lateral (*e.g*., lane changing) and longitudinal (*e.g*., braking and accelerating) actions, we introduce a semi-anchor-based decoding structure. An illustrative overview of our decoding pipeline is presented in Fig. 1, with subsequent paragraphs detailing the individual components.

### Reference Lines as Lateral Queries

Following the methodology outlined , this study employs reference lines as a high-level abstraction for lateral queries. Reference lines, typically derived from the autonomous vehicle's surrounding lanes on its route, serve as a critical component in conventional vehicle motion planning, guiding lateral driving behaviors. Initially, we identify lane segments within a radius of $R_{ref}$ from the AV's current position. Starting from each identified lane segment, a depth-first search is conducted to explore all potential topological connections, linking their respective lane centerlines. Subsequently, these connected centerlines are truncated to a uniform length and are resampled to maintain a consistent number of points. The approach for representing and encoding the features of reference lines mirrors that of vectorized map encoding, as outlined in Section III-B. Ultimately, the embedded reference lines are utilized as the lateral query $Q_{lat} \in {\mathbb{R}}^{N_{R} \times D}$, where $N_{R}$ represents the number of reference lines.

### Factorized Lateral-longitudinal Self-Attention

In addition to $Q_{lat}$, we employ $N_{L}$ anchor-free, learnable queries $Q_{lon} \in {\mathbb{R}}^{N_{L} \times D}$ to encapsulate the multi-modal nature of longitudinal behaviors. Following this, $Q_{lat}$ and $Q_{lon}$ are combined to create the initial set of lateral-longitudinal queries, denoted as $Q_{0} \in {\mathbb{R}}^{N_{R} \times N_{L} \times D}$: where Projection refers to either a simple linear layer or a multilayer perceptron. Since each query within $Q_{0}$ captures only the local region information pertaining to an individual reference line, we utilize self-attention mechanisms on $Q_{0}$ to integrate global lateral-longitudinal information across various reference lines. Nonetheless, applying self-attention directly to $Q_{0}$ results in computational complexity of $\mathcal{O}\left({N_{R}^{2}N_{L}^{2}} \right)$, which becomes prohibitively high as $N_{R}$ and $N_{L}$ increase. Drawing inspiration from similar approaches in the literature, we adopt a factorized attention strategy across each axis of $Q$, effectively reducing the computational complexity to $\mathcal{O}\left({{N_{R}^{2}N_{L}} + {N_{R}N_{L}^{2}}} \right)$.

### Trajectory Decoding

The trajectory decoder consists of a sequence of $L_{dec}$ decoding layers, each comprising three types of attention mechanisms: lateral self-attention, longitudinal self-attention, and query-to-scene cross-attention. These processes are mathematically represented as follows: | | | ${Q_{i} = {\text{CrossAttn}{({\hat{Q}}_{i - 1},E_{enc},E_{enc})}}}.$ | | | Here, $\text{SelfAttn}{({{X,\text{dim}} = i})}$ indicates the application of self-attention across the $i$-th dimension of $X$, and $\text{CrossAttn}{(Q,K,V)}$ incorporates layer normalization, multi-head attention, and a feed-forward network, analogous to the structure defined in Eq. 3. The decoder's final output, $Q_{dec}$, is then employed to determine the AV's future trajectory points and their respective scores using two MLPs: Each decoded trajectory point has six channels: $\lbrack p_{x},p_{y},{\cos\theta},{\sin\theta},v_{x},v_{y}\rbrack$. Furthermore, to accommodate scenarios lacking reference lines, an additional MLP head is introduced to directly decode a single trajectory from the encoded features of the AV:

### Imitation Loss

To avoid mode collapse, we employ the teacher-forcing technique during the training process. Firstly, the endpoint of the ground truth trajectory $\tau^{gt}$ is projected relative to reference lines, with the selection of the reference line closest in lateral distance serving as the target reference line. This target reference line is subsequently divided into $N_{L} - 1$ equal segments by distance. Each segment corresponds to the region managed by each longitudinal query, with the final query accounting for regions extending beyond the target reference line. The query encompassing the projected endpoint is designated as the target query. By integrating the target reference line with the target longitudinal query, we derive the target supervision trajectory, $\hat{\tau}$. For trajectory regression, we employ the smooth L1 loss, and for score classification, we utilize the cross-entropy loss, expressed as follows: | | $\mathcal{L}_{reg}$ | ${= {{\text{L1}_{smooth}{(\hat{\tau},\tau^{gt})}} + {\text{L1}_{smooth}{(\tau^{free},\tau^{gt})}}}},$ | | \(8\) | | | $\mathcal{L}_{cls}$ | ${= {\text{CrossEntropy}{({\mathbf{π}}_{0},{\mathbf{π}}_{0}^{\ast})}}},$ | | | where ${\mathbf{π}}_{0}^{\ast}$ signifies the one-hot distribution derived from the index of $\hat{\tau}$. The overall imitation loss is formulated as the sum of these two components, each weighted equally:

### Prediction Loss

A simple two-layer MLP is used to generate a single modal prediction for each dynamic agent from the encoded agents' embeddings: Firstly, this provides dense supervision which benefits the training. Secondly, the generated predictions play a crucial role in eliminating unsuitable planning proposals during the post-processing stage, as detailed in Section III-F. Denote agent's ground truth trajectory as ${\mathbf{P}}_{1:N_{A}}^{gt}$, the prediction loss is Figure 2: Illustration of the proposed auxiliary loss computation method. Initially, the trajectory produced by the neural network is mapped onto the image space associated with the cost map. Subsequently, the cost value is obtained via bilinear interpolation and employed in the formation of the loss function. Given the differentiable nature of all processes involved, it is feasible to incorporate auxiliary tasks directly into the framework, allowing for end-to-end training.

### III-D Efficient Differentiable Auxiliary Loss

As highlighted by earlier studies, pure imitation learning does not suffice to preclude undesired outcomes, such as collisions with stationary obstacles or deviations from the drivable path. Therefore, it is essential to incorporate these constraints as auxiliary losses in the model during its training phase. Nevertheless, the integration of these constraints in a manner that is differentiable and enables end-to-end training of the model presents a significant challenge. A frequently adopted method for this purpose is differentiable rasterization. For instance, Zhou et al. demonstrates a technique where each trajectory point is converted into rasterized images, using a differentiable kernel function, and subsequently calculates the loss using obstacle masks within the image space. This method, however, is limited by its computational and memory demands, which in turn limits the output resolution (*e.g*., it permits only large time intervals and short planning horizons). To mitigate these limitations, we propose a novel approach based on differentiable interpolation. This method facilitates the concurrent calculation of auxiliary loss for all trajectory points. We take the drivable area constraint an example to elucidate our proposed method.

### Cost Map Construction

The first step of our methodology involves transforming the constraint into a queryable cost-map representation. Specifically, for the drivable area constraint, we employ the widely recognized Euclidean Signed Distance Field (ESDF) for cost representation. This process encompasses mapping the non-drivable areas (*e.g*., off-road regions) onto an $H \times W$ rasterized binary mask, followed by executing distance transforms on this mask. A distinctive advantage of our approach over existing methods is its elimination of the need to render the trajectory into a series of images, thereby significantly reducing computational demands.

### Loss Calculation

In accordance with established methodologies in optimization-based vehicle motion planning, we model the vehicle's shape using $N_{c}$ covering circles. The trajectory point determines the centers of these circles, which can be derived in a differentiable manner. As illustrated in Fig. 2, for each covering circle $i$ associated with a trajectory point, we obtain its signed distance value $d_{i}$ through projection and bilinear interpolation. To ensure adherence to the drivable area constraint, we apply a penalty to the model when $d_{i}$ falls below the circle's radius $R_{c}$. The auxiliary loss is: where $\epsilon$ is a safety threshold. Eq. 12 is also applicable to punish collisions with a slight change to the cost map construction.

In practice, $d_{i}$ and $\mathcal{L}_{aux}$ can be differentiably and efficiently calculated batch-wise with the modern deep learning framework as shown in Algorithm 1. It is important to note that our approach is versatile and not confined to ESDF-based representations alone. Any cost representation that allows for continuous querying, such as potential fields, can be incorporated with an appropriately designed loss function.

## Pytorch style pseudo-code

## traj: Trajectory, [B, T, 4] (x, y, cos, sin)

## offset: constant offset of the centers

## sdf: Signed Distance Feild [B, H, W, 1]

## res: rasterization resolution of the SDF

## Rc: radius of the covering circle

## epsilon: safety threshold

def DriableAreaLoss(traj, sdf, offset, res, Rc, epsilon): centers = traj[..., None,:2] + offset * traj[..., None, 2:4]

## projection

centers_pixel = torch.stack([centers[..., 0] / resolution, -centers[..., 1] / resolution],dim=-1) grid = centers_pixel / torch.tensor([W//2, H//2])

## query distance in batch

distance = F.sample_grid (sdf.unsqueeze, grid, mode="bilinear").squeeze

## Hinge loss

cost = Rc + epsilon - distance loss_mask = cost > 0 cost.masked_fill_(∼loss_mask, 0) loss = F.l1_loss(cost, torch.zeros_like(cost), reduction="none").sum(-1) loss = loss.sum / (loss_mask.sum + 1e-6) Algorithm 1 Drivable Area Loss Pseudo-code

### III-E Contrastive Imitation Learning Framework

Figure 3: Illustration of the proposed contrastive imitation learning (CIL) framework. For any input data, we apply two data augmentation functions from different augmentation modules (t ∼ 𝒯+ and t′ ∼ 𝒯−) to obtain a positive sample and a negative sample. The projected latent embeddings z(⋅) are used to calculate the conservative loss which maximizes the agreement between z+ and z and minimizes the agreement of z− and z.

We introduce the Contrastive Imitation Learning (CIL) framework, designed to effectively address the challenges of distribution shift and causal confusion within a coherent and straightforward structure. Illustrated in Fig. 3, the CIL framework comprises four essential steps: Given a training scenario data sample, denoted as $\mathbf{x}$, we apply both a positive data augmentation module, $\mathcal{T}^{+}$, and a negative one, $\mathcal{T}^{-}$, to generate a positive sample ${\mathbf{x}}^{+}$ and a negative sample ${\mathbf{x}}^{-}$. Positive augmentations are those that preserve the validity of the original ground truth (*e.g*., see Fig. 4a), while negative augmentations alter the original causal structure, rendering the original ground truth inapplicable.

The Transformer encoder, as detailed in Sect. III-B, is utilized to derive the latent representations ${\mathbf{h}}^{( \cdot )}$ of both the original and augmented data samples. Subsequently, these representations are mapped to a new space, represented as ${\mathbf{z}},{\mathbf{z}}^{+},{\mathbf{z}}^{-}$, by a two-layer MLP projection head.

A triplet contrastive loss is calculated to enhance the agreement between $\mathbf{z}$ and ${\mathbf{z}}^{+}$ while decreasing the similarity between $\mathbf{z}$ and ${\mathbf{z}}^{-}$.

Finally, trajectories for the original and positively augmented data samples are decoded, and both the imitation loss and an auxiliary loss are computed.

In practice, we randomly sample a minibatch of $N_{bs}$ samples. Each sample undergoes positive and negative augmentation, executed by augmentors randomly chosen from the sets $\mathcal{T}^{+}$ and $\mathcal{T}^{-}$, respectively. This augmentation triples the total number of samples to $3N_{bs}$. All samples are processed by the same encoder and projection head. Let ${\text{sim}{({\mathbf{u}},{\mathbf{v}})}} = {{{{\mathbf{u}}^{T}{\mathbf{v}}}/\left. \parallel{\mathbf{u}}\parallel \right.}\left. \parallel{\mathbf{v}}\parallel \right.}$ denote the dot product between the $l2$ normalized $\mathbf{u}$ and $\mathbf{v}$, the softmax-based triple contrastive loss is defined as: where $\sigma$ denotes the temperature parameter. The contrastive loss is computed across all triplets in the mini-batch. Besides this, we provide supervision to both the original and positively augmented samples using the unmodified ground truth trajectory. Note that negatively augmented samples are only used to calculate the contrastive loss as their origin ground truth may be invalid after augmentation. The overall training loss comprises four components: imitation loss, prediction loss, auxiliary loss, and contrastive loss, represented as:

### Data augmentations

Figure 4: Exemplary scenarios of the proposed data augmentations. In each group, the figure on the left denotes the origin scenario and the right one shows the augmented scene. AV is marked in the orange, other vehicle agents are in blue, and dash-colored lines on the lanes denote the traffic light status. (a)-(b) belongs to the positive augmentations 𝒯+ and (c)-(f) are negative augmentations 𝒯−.

Data augmentation is the key for contrastive learning to work. While perturbation-based augmentations are prevalent, alternative augmentation strategies remain insufficiently explored. In this context, we present six carefully crafted augmentation functions that defines the contrastive task, with illustrative examples provided in Fig. 4.

State Perturbation $\in \mathcal{T}^{+}$ (Fig. 4a): introduces minor, randomly generated disturbances to the autonomous vehicle's current position, velocity, acceleration, and steering angle. This augmentation is intended to enable the model to learn recovery strategies for slight deviations from the training distribution. The CIL framework aims to maximize the similarity between the latent representations of original and augmented samples, thereby enhancing the model's resilience to error accumulation.

Non-interactive Agents Dropout $\in \mathcal{T}^{+}$ (Fig. 4b): omits agents from the input scenario that do not interact with the AV in the near future. Interactive agents are identified through the intersection of their future bounding boxes with the AV's trajectory. This augmentation prevents the model from learning behaviors by mimicking non-interactive agents, thereby encouraging the model to discern genuine causal relationships with interactive agents.

Leading Agents Dropout $\in \mathcal{T}^{-}$ (Fig. 4c): removes all agents located ahead of the AV. Special consideration is given to leading-following dynamics, a prevalent situation in real-world driving. This augmentation trains the model on leading-following behaviors to prevent rear-end collisions.

Leading Agent Insertions $\in \mathcal{T}^{-}$ (Fig. 4d): introduces a leading vehicle into the AV's original path, at a position where the AV's expected trajectory becomes invalid (*e.g*., would result in a collision). The inserted vehicle's trajectory data is sourced from a randomly selected agent in the current mini-batch to maintain data realism.

Interactive Agent Dropout $\in \mathcal{T}^{-}$ (Fig. 4e): excludes agents that have direct or indirect interactions with the AV. Identification of interactive agents follows the methodology outlined in Non-interactive Agents Dropout. This function aims to train the model on less intuitive interactions within complex scenarios, such as unprotected left turns and lane changes.

Traffic Light Inversion $\in \mathcal{T}^{-}$ (Fig. 4f): in scenarios where the AV approaches an intersection governed by traffic lights without a leading vehicle, the traffic light status is reversed (*e.g*., from red to green). This function teaches the model to adhere to basic traffic light rules.

These augmentation functions are designed with minimal inductive bias to ensure broad applicability. The contrastive learning task facilitates an implicit feedback mechanism, providing implicit reward signals. These signals reinforce adherence to fundamental driving principles.

### III-F Planning and Post-processing

Input: Init state y0, scenario feature x, constant K, α, NT procedure Trajectory Selection T0, π0, P1: NA = Pluto(x) ⊳ Run model inference T0 = TopK(T0, π0, K) ⊳ Select Top-K trajectories Initialize rollouts ${\overset{\sim}{T}}_{0} = {\lbrack{\mathbf{y}}_{0}\rbrack}$ for t in 1…NT do ⊳ Forward Simulation ${\overset{\sim}{\mathbf{T}}}_{0} = {\lbrack{\overset{\sim}{\mathbf{T}}}_{0},{\mathbf{y}}_{0}\rbrack}$ πrule = RuleBasedEvaluator(${\overset{\sim}{T}}_{0},{\mathbf{P}}_{1:N_{A}},{\mathbf{x}}$) Algorithm 2 Trajectory planning process of Pluto In the context of trajectory planning, our objective is to select a deterministic future trajectory from the diverse outcomes provided by the multi-modal outputs, as discussed in Section III-C. Rather than merely selecting the most likely trajectory, we integrate a post-processing module to serve as an additional safety verification mechanism, as illustrated in Algorithm 2.

Upon extracting the scenario's features, the model is executed to generate multi-modal planning trajectories ${\mathbf{T}}_{0} \in {\mathbb{R}}^{{N_{R}N_{L}} \times T_{F} \times 6}$, associated confidence scores ${\mathbf{π}}_{0} \in {\mathbb{R}}^{N_{R}N_{L}}$, and predictions for the agents' movements ${\mathbf{P}}_{1:N_{A}} \in {\mathbb{R}}^{N_{A} \times T_{F} \times 2}$. Given that the total trajectory count $N_{R}N_{L}$ for ${\mathbf{T}}_{0}$ can be extensive, an initial filtering step retains only the top $K$ trajectories, ranked by their confidence scores, to streamline subsequent computations.

Following, a closed-loop forward simulation is performed on ${\mathbf{T}}_{0}$ to obtain simulated rollouts ${\overset{\sim}{\mathbf{T}}}_{0}$, utilizing a linear quadratic regulator (LQR) for trajectory tracking and a kinematic bicycle model for state updates. It has been noted that trajectory-based imitation learning may not fully account for the dynamics of the underlying system, potentially leading to discrepancies between the model's planned trajectory and its actual execution. To mitigate this issue, our assessment relies on the simulated rollouts rather than the model's direct output, thus narrowing the gap.

Subsequently, a rule-based evaluator assigns scores ${\mathbf{π}}_{rule}$ to each simulated rollout based on criteria such as progress, driving comfort, and adherence to traffic regulations, in alignment with the framework established. This evaluation also incorporates predictions of agents' trajectories ${\mathbf{P}}_{1:N_{a}}$ to calculate the time-to-collision (TTC) metric, excluding rollouts that result in at-fault collisions. The ultimate score combines the initial learning-based confidence score ${\mathbf{π}}_{0}$ with the rule-based score ${\mathbf{π}}_{rule}$ via the equation: where $\alpha$ represents a fixed weighting factor. The selection of the final trajectory $\tau^{\ast}$ is based on maximizing $\mathbf{π}$. Unlike the post-processing step described, which typically utilizes an optimizer to refine the trajectory, our post-processing module acts solely as a trajectory selector, leaving the original planning trajectory unaltered. We regard the post-processing step as a proxy to inject human preference or control into the black-boxed neural network, acknowledging its current limitations, and providing a lower-bound safety assurance to mitigate the risk of catastrophic accidents.

## Experiments

### IV-A Experiment Setup

### nuPlan

Our model was trained and evaluated using the nuPlan dataset. This dataset comprises 1,300 hours of real-world driving data, encompassing up to 75 labeled scenario types. It introduces the first publicly accessible, large-scale planning benchmark for autonomous driving through its associated closed-loop simulation framework. Each simulation conducts a 15-second rollout at a frequency of 10 Hz, during which the autonomous vehicle is managed by a planner and tracker. Traffic agents within these simulations are controlled in two distinct manners: non-reactive, wherein agents' states are determined based on logged trajectories, and reactive, wherein agents are governed by an Intelligent Driver Model planner.

### Benchmark and Metrics

For all experiments, we use a standardized training split of 1M frames sampled from all scenario types. For evaluation, we use the benchmark, which contains up to 100 scenarios from the 14 scenario types specified in the nuPlan planning challenge, resulting in a total number of 1090 scenarios (we filter out a few scenarios that initialized as failed in the reactive simulations).

NuPlan employs three principal evaluation metrics: the open-loop score (OLS), the non-reactive closed-loop score (NR-score), and the reactive closed-loop score (R-score). Given that previous studies have demonstrated a minimal correlation between open-loop prediction performance and closed-loop planning effectiveness, we only focus on closed-loop performance in this paper. The closed-loop score is calculated as a weighted average of several key metrics: No ego at-fault collisions: A collision is identified when the autonomous vehicle's (AV) bounding box intersects with that of other agents or static obstacles. However, collisions initiated by other agents, such as rear-end collisions, are disregarded.

Time to collision (TTC) within bound: The TTC is defined as the time it would take for the AV and another entity to collide if they continue on their current trajectories and speeds. This metric mandates that the TTC exceeds a specified threshold.

Drivable area compliance: This criterion requires that the AV remains within the boundaries of the drivable roadway at all times, ensuring adherence to the designated driving area.

Comfortableness: The comfort of the AV is quantified by examining the minimum and maximum values of its longitudinal and lateral accelerations and jerks, as well as its yaw rate and acceleration. These parameters are assessed against established thresholds derived from empirical data.

Progress: Progress is evaluated by comparing the distance covered by the AV along its planned route to that achieved by an expert driver, expressed as a percentage.

Speed limit compliance: This metric checks whether the AV's speed falls within the legal limits prescribed for the roadway it is traversing.

Driving direction compliance: This measure penalizes deviations from the correct driving direction, particularly incidents where the AV is found traveling against the flow of traffic.

A more detailed description and calculation of the metrics can be found . We use the non-reactive closed-loop score (denoted as score if not specified) as our primary overall performance evaluation metric.

### Baselines

In this study, we conduct a comparative analysis between Pluto and both existing and state-of-the-art (SOTA) methodologies utilizing the nuPlan benchmark to demonstrate the efficacy of our proposed method. The baselines for comparison are categorized into three groups: rule-based, pure learning, and hybrid approaches. Rule-based methods rely on manually engineered rules without incorporating learning processes. In contrast, pure learning methods employ neural networks to directly generate the final planned trajectory, omitting any refinement or post-processing stages. Hybrid methods, however, include a post-processing module to refine or adjust outcomes derived from learning-based techniques. The benchmarked methods are outlined as follows: Intelligent Driver Model (IDM): This is a classic, time-continuous car-following model extensively utilized in traffic simulations. We employ the official implementation as referenced in the literature.

PDM-Closed: Identified as the winning entry in the 2023 nuPlan planning challenge, this method generates a series of proposals by integrating IDM policies with varying hyperparameters, subsequently selecting the optimal one through a rule-based scoring system. Despite its simplicity, it has proven effective in practice and currently holds the SOTA performance. Its open-source implementation is utilized in our study.

PDM-Open: This approach, centered around a predictive model that conditions on the centerline and utilizes MLPs, is implemented through an available open-source version.

GC-PGP: A predictive model that focuses on goal-conditioned lane graph traversals.

RasterModel: A CNN-based model that interprets the input scenario as a multi-channel image, as described in referenced literature.

UrbanDriver: A learning-based planner that leverages vectorized inputs through PointNet-based polyline encoders and Transformers. This model is assessed through its open-loop re-implementation, incorporating historical data perturbation during its training phase.

PlanTF: A strong pure imitation learning baseline that leverages a Transformer architecture to explore efficient design in imitation learning. Despite its simplicity, it stands as the current SOTA among pure learning models.

GameFormer: Modeled on DETR-like interactive planning and prediction based on level-k games, the output from this model serves as an initial estimate, which is further refined through a nonlinear optimizer. The official open-source code is used for implementation purposes.

PlanTF-H: This method enhances PlanTF by integrating a post-processing module as described in Sect. III-F, thereby converting it into a hybrid approach.

### IV-B Implementation Details

We present two variations Pluto^†^ and Pluto, differing only in that Pluto^†^ omits the post-processing step. Feature extraction focuses on map elements and agents within a 120-meter radius of the autonomous vehicle. We adhere to the nuPlan challenge by setting the planning and historical data horizons at 8 seconds and 2 seconds, respectively. The model incorporates auxiliary tasks designed to penalize off-road driving and collisions. Training was conducted using 4 RTX3090 GPUs, with a batch size of 128 over 25 epochs. We utilized the AdamW optimizer, applying a weight decay of $1e^{- 4}$. The learning rate is linearly increased to $1e^{- 3}$ over the first three epochs and then follows a cosine decay pattern throughout the remaining epochs. The loss weights $w_{1 - 4}$ are uniformly assigned a value of 1.0. The training finishes in 45 hours with CIL and 22 hours without it. Details on further parameter settings can be found in Table I.

Num. encoder layers Num. decoder layers Num. lon. queries Num. covering circles Cost map size Cost map resolution TABLE I: Parameters used in Pluto† and Pluto

## Results and Disscusion

TABLE II: Closed-loop planning results on the benchmark. All metrics are higher the better.

### V-A Comparison with State of the Art

The comparative analysis with other methods on the benchmark is detailed in Table II. Initially, our purely learning-oriented variant, Pluto^†^, surpasses all prior baselines dedicated to pure learning. Significantly, when compared to the leading model, PlanTF, Pluto^†^ demonstrates marked improvements across nearly all evaluated metrics, with particular enhancements observed in metrics pertinent to safety (*e.g*., Collisions improved from $94.13$ to $96.18$, TTC from $90.73$ to $93.28$, and Drivable from $96.79$ to $98.53$). These results highlight the constraints of models based solely on imitation and underscore the effectiveness of incorporating auxiliary loss and the design of the CIL framework.

Furthermore, our hybrid model, Pluto, attains the highest scores across all baselines, surpassing the current state-of-the-art rule-based model, PDM-Closed, for the first time. This achievement emphasizes the promise of learning-based approaches in planning. Remarkably, the performance of our methods closely aligns with that of the log-reply expert (scoring $93.68$ vs. $93.21$), indicating a significant stride towards expert-level planning.

In addition to quantitative outcomes, our method also presents an advantage in driving behavior over PDM-Closed. Given that PDM-Closed primarily focuses on speed planning, its capability in lateral maneuvers is somewhat restricted, limiting its ability to execute lane-change actions. In contrast, Pluto is designed to consider both longitudinal and lateral movements, thanks to the query-based architecture of our model. This capability will be further illustrated through case studies in the section on qualitative results.

Figure 5: Qualitative results of closed-loop planning for five representative scenarios from the test set. Each scenario (every row) lasts 15 seconds and we take 4 snapshots with a 5-second interval. Purple dash arrows denote the reference lines, the light blue lanes denote the global routing plan and other important legends are marked in Fig. a-1. It is recommended to refer to our project website for more vivid videos.

### V-B Qualitative Results

Fig. 5 presents selected scenarios from the nuPlan test set, showcasing the robust performance of our framework in complex, interactive urban driving situations through the exhibition of diverse, human-like behaviors. The scenarios are detailed as follows: The autonomous vehicle navigates to an adjacent empty lane to enhance efficiency and subsequently halts at a red light at the intersection. Observations from sequences a-2 and a-3 reveal that Pluto concurrently evaluates multiple potential plans for different behaviors (illustrated by gray candidate trajectories), enhancing the planning process's flexibility and resemblance to human driving.

In a scenario requiring the AV to maneuver around a roundabout, its path is narrowed by a parked vehicle. Our planning system adeptly navigates around this obstacle while yielding to an oncoming vehicle in a constrained space, exemplifying our method's competence in managing static obstacles and interacting with other vehicles.

Encountering a stationary vehicle within its lane, the AV executes a left lane change to bypass the obstacle, subsequently returning to its original lane to adhere to the intended route. This scenario underscores the planner's dynamic decision-making capabilities and its adeptness in route adherence and road topology comprehension.

During a left-turn maneuver in heavy traffic, the AV patiently waits for an opportune moment to execute the turn, illustrating our method's effectiveness in navigating intersections in high-density traffic conditions.

Upon following a slower vehicle, the AV opts to accelerate and overtake, showcasing a behavior that aligns closely with natural human driving and highlighting our proposed method's adaptability.

In summary, Pluto exhibits advanced and varied driving behaviors unattainable through simplistic speed-planning methods (*e.g*., PDM-Closed). Its ability to execute natural lane changes, navigate around obstacles, and dynamically modify decisions in interactive scenarios marks a significant advancement towards the realization of practical learning-based planning. For further insights, including videos, we direct interested readers to our project website.

### V-C Ablation Studies

For all ablation studies, we evaluate on a subset of nuPlan (non-overlapping with the benchmark), which contains 20 scenarios for each of the 14 scenarios types.

### Influence of Each Component

ℳ2 + Ref. free head TABLE III: Ablation study of the influence of each component Table II shows the trajectory from a base model to the top-performing learning-based planner. The initial model, denoted as $\mathcal{M}_{0}$, is constructed on the architecture depicted in Sect. III-B and III-C, employing solely imitation loss for training. $\mathcal{M}_{0}$ demonstrates performance on par with the previous SOTA pure learning-based method, PlanTF, an achievement we ascribe to the enhanced query-based architecture.

The introduction of the state dropout encoder (SDE) in $\mathcal{M}_{1}$, which randomly masks the autonomous vehicle's kinematic states during training to avert the generation of shortcut trajectories by state extrapolation, results in marked improvements over $\mathcal{M}_{0}$ across almost all metrics. $\mathcal{M}_{2}$ incorporates an auxiliary loss designed to penalize deviations from the drivable area and collisions. This modification leads to enhancements in both the Collision metric (from 97.37 to 97.98) and the Drivable metric (from 95.92 to 98.38). We would like to highlight that despite the seemingly minor difference in total scores between $\mathcal{M}_{2}$ and $\mathcal{M}_{1}$, the disparity in their actual performance is substantial. We direct interested readers to the project website for the model ablation results. The $\mathcal{M}_{3}$ model underscores the importance of integrating a reference line-free decoding head to effectively handle scenarios where reference lines are absent, such as in parking lots.

Further, $\mathcal{M}_{4}$ is trained using the proposed contrastive imitation learning framework, achieving a significant uplift in performance from 90.69 to 91.66. This improvement is noteworthy, particularly as it is already approaching the expert's performance.

Ultimately, $\mathcal{M}_{5}$ attains the best overall performance, though at a minor trade-off in the Comfort metric. This compromise stems from the increased incidence of emergency stops triggered by the safety checker, thereby enhancing safety-related metrics.

TABLE IV: Impact of different longitudinal queries NL (based on ℳ4)

### Number of Longitudinal Queries

. Table IV presents the outcomes associated with various quantities of longitudinal queries $N_{L}$ (utilizing model $\mathcal{M}_{4}$). The results indicate that a setting of $N_{L} = 12$ yields the most favorable performance among four tested variants. This suggests an appropriate number of queries is necessary to cover all the longitudinal behaviors for a planning horizon of 8s. An increase in $N_{L}$ beyond this point detracts from performance. This decline can likely be attributed to the sufficiency of $N_{L} = 12$ in capturing a diverse array of behaviors; additional queries become redundant, potentially increasing the training difficulty.

TABLE V: Impact of different K in post-processing (based on ℳ5)

### Top-K in Coarse Selection

. In the planning cycle, Pluto generates a total of $N_{R} \times N_{L}$ trajectories. Empirical evidence suggests that trajectories associated with low confidence scores often exhibit inferior quality. Consequently, employing a preliminary selection process based on confidence scores proves advantageous in eliminating such trajectories, thereby expediting subsequent post-processing. As illustrated in Table V, setting $K = 20$ turns out to be appropriate.

TABLE VI: Impact of α in trajectory selection (Based on ℳ5)

### Weight of the Learning-based Score

. As demonstrated in Equation 15, the final score is derived from the combined weighted contributions of the rule-based and the learning-based scores. This study examines the impact of the weight parameter $\alpha$, with the findings detailed in Table VI. Firstly, it is observed that incorporating the learning-based score significantly enhances performance compared to relying solely on the rule-based score (*i.e*., $\alpha = 0$). The limitation of the rule-based score lies in its hand-crafted nature, which may not accurately represent all possible scenarios, whereas the learning-based score offers greater generalizability by dynamically adapting to the input features. Furthermore, a combined approach proves superior to using a purely learning-based score ($\mathcal{M}_{4}$), indicating that the current model, while advanced, still benefits from the inclusion of a rule-based component as a form of safety assurance. Based on optimal performance, $\alpha = 0.3$ has been selected as the default setting.

TABLE VII: Constant velocity vs. learned prediction (Based on ℳ5)

### Prediction method

. In this study, we contrast the performance of our learned prediction model against the constant velocity prediction employed in PDM-Closed and presented in Table VII. It is evident that employing learned predictions for planning yields superior results compared to the simplistic constant velocity prediction, as it can more accurately discern the behaviors of the agents. Despite our prediction model producing only a singular modal trajectory for each agent, it works well in practice.

## Conclusion

In this study, we introduce Pluto, a pioneering data-driven planning framework that extends the capabilities of imitation learning within the autonomous driving domain. We propose innovative solutions concerning model architecture, data augmentation, and the learning framework, effectively addressing enduring challenges in imitation learning. The query-based model architecture furnishes the planner with the capacity for adaptable driving behaviors across both longitudinal and lateral dimensions. Our novel method for computing auxiliary loss, based on differentiable interpolation, offers a new approach for integrating constraints into the model. Additionally, the employment of a contrastive imitation learning framework, coupled with an advanced set of data augmentation techniques, enhances the acquisition of desired behaviors and comprehension of intrinsic interactions. Experimental evaluations utilizing real-world driving datasets demonstrate that our approach sets a new benchmark for closed-loop performance in the field. Notably, Pluto surpasses the previously best-performing rule-based planner, establishing a significant breakthrough in autonomous driving research.

### Limitations and Future Work

. In our approach, we predict a single trajectory for each dynamic agent. This methodology yields satisfactory outcomes in practical applications; nevertheless, the generation of meaningful joint multimodal predictions and their efficient incorporation into planning strategies represent significant areas for future research. The addition of a post-processing module has been demonstrated to improve overall performance effectively. However, it cannot handle scenarios where all generated trajectories are unusable. Transitioning the post-processing function to an intermediary role that directly influences trajectory generation could present a more advantageous strategy.
