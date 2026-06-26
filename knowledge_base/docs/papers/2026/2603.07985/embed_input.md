<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

On the Feasibility and Opportunity of Autoregressive 3D Object Detection

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

LiDAR-based 3D object detectors typically rely on proposal heads with hand-crafted components like anchor assignment and non-maximum suppression (NMS), complicating training and limiting extensibility. We present AutoReg3D, an autoregressive 3D detector that casts detection as sequence generation. Given point-cloud features, AutoReg3D emits objects in a range-causal (near-to-far) order and encodes each object as a short, discrete-token sequence consisting of its center, size, orientation, velocity, and class. This near-to-far ordering mirrors LiDAR geometry - near objects occlude far ones but not vice versa - enabling straightforward teacher forcing during training and autoregressive decoding at test time. AutoReg3D is compatible across diverse point-cloud or backbones and attains competitive nuScenes performance without anchors or NMS. Beyond parity, the sequential formulation unlocks language-model advances for 3D perception, including GRPO-style reinforcement learning for task-aligned objectives.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

These results position autoregressive decoding as a viable, flexible alternative for LiDAR-based detection and open a path to importing modern sequence-modeling tools into 3D perception.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

Object detection has long been one of the most influential tasks in computer vision, with applications spanning recognition, healthcare \[39, 51")\], and a wide range of analytics. In 3D perception---critical for scene understanding and downstream tasks such as autonomous driving and robotic systems---detectors typically follow a "propose-then-classify" paradigm. These systems first generate region proposals and then refine and classify them, a design directly inspired by 2D methods. Both two-stage variants and their single-stage counterparts rely on classification and regression objectives to produce the final bounding boxes, achieving strong performance and remaining the dominant approach.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

However, proposal-based detectors depend on a rigid stack of hand-crafted machinery: anchor assignment, proposal matching, geometric regression targets, confidence thresholds, and NMS. This stack exists because predictions are made independently across spatial locations, yielding multiple overlapping boxes that must be filtered and de-duplicated. Although effective for redundancy control, these components introduce extra complexity, complicate training, and often discard information during post-processing. They also hinder composability with downstream modules, *e.g*., large language models (LLMs), limiting the scalability and extensibility of 3D detection beyond the regimes for which these systems were designed.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

We propose to address these issues by reintroducing dependence among predictions. Inspired by the success of autoregressive (AR) sequence modeling in language and emerging vision-generation tasks, we explore an alternative formulation for 3D detection: *casting bounding-box prediction as autoregressive sequence generation*. Unlike proposal-based detectors, an autoregressive model emits one object at a time while conditioning on previously predicted objects. This dependency lets the detector remain aware of prior outputs, naturally suppressing overlaps and obviating NMS or proposal filtering. While related ideas have shown promise for 2D detection, a scalable and competitive autoregressive alternative for 3D point-cloud detection has remained elusive due to the higher dimensionality, the challenges of discretizing continuous geometry, and the sheer spatial scale of LiDAR scenes.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

We present AutoReg3D, the first autoregressive 3D point-cloud detector that achieves performance competitive with state-of-the-art proposal-based and query-based systems. Our key insight is that LiDAR naturally induces a near-to-far ordering: objects closer to the ego-vehicle are physically encountered---and thus observed---before those farther away. This ordering reflects the causal structure of occlusion in 3D and provides an intuitive *sequential dependence* along which objects can be generated autoregressively. In contrast to 2D images, where the decoding order is largely arbitrary, 3D range provides a principled sequence axis that aligns with autoregressive modeling.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Introduction", "weight": 1.5} -->

Concretely, given a point cloud encoded by any encoder (*e.g*.,voxel-based ), AutoReg3D autoregressively generates a sequence of discrete tokens, each representing a single object. Every object is encoded as a short token sequence for its class, location $(x,y,z)$, size $(l,w,h)$, velocity $(v_{x},v_{y})$, and orientation $\psi$. To discretize continuous geometry effectively while respecting the distinct ranges and semantics of each axis in 3D, we use ego-relative coordinates with parameter-specific vocabularies, expanded along each of the bound box semantic axis, *i.e*. directions, orientation, *etc*. Generation begins with a \[start\] token, proceeds from near to far, and terminates with a \[end\] token---producing a threshold-free set of boxes and eliminating confidence thresholds and NMS.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Introduction", "weight": 1.5} -->

Our formulation not only simplifies 3D detection but also unlocks new capabilities. Because inference is autoregressive, AutoReg3D can readily adopt techniques from sequence and language modeling, including reinforcement-learning-based fine-tuning and advanced decoding. These techniques offer straightforward, plug-in paths to further improve performance without redesigning the core model.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Introduction", "weight": 1.5} -->

The goal of this work is to show viability: autoregressive modeling for 3D point-cloud detection can *match mainstream accuracy* while opening a path to modern sequence-modeling advances in 3D. We acknowledge a practical bottleneck---sequential decoding latency---which applies broadly to AR applications, and for this work, we view speed as orthogonal to our core contribution. We expect improvements with advances in autoregressive decoding and hardware acceleration; because AutoReg3D uses the canonical AR toolkit, these gains should transfer with minimal integration cost. Altogether, our contributions are: We introduce AutoReg3D, the first autoregressive 3D object detector that directly generates object sequences from point clouds, achieving performance on par with leading proposal-based and query-based detectors.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Introduction", "weight": 1.5} -->

We present a detailed ablation study of design factors---including object-level tokenization, sequence ordering, and decoding methodologies---that are critical for effective autoregressive 3D detection.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Introduction", "weight": 1.5} -->

We demonstrate unique capabilities enabled by the autoregressive formulation, including the elimination of NMS, compatibility with reinforcement learning (RL) fine-tuning, and promptable decoding.

<!-- chunk {"id": "body-0013", "role": "body", "section": "3D Object Detection from Point Clouds", "weight": 1.0} -->

3D object detection has been a cornerstone objective in the self-driving field, where methods have been developed to perceive from camera inputs and 3D LiDAR point clouds. Of these, LiDAR based 3D object detectors have to contend with high number of sensor reading points, and many works have been dedicated to processing them into deep learning features regressing the bounding boxes. These have collected into three main paradigm, consisting of point-based methods, pillar-based methods, and voxel-based methods. Point-based backbones were developed to directly process point cloud data, but suffer from high input scalability and have slower inference times. In contrast, voxel and pillar-based backbones divide the space into a constant number of features, and trade off some accuracy resolution, but are often have faster inference speeds. More recently, enabled by improved hardware, there have been improved Transformer and Mamba point cloud backbones. These methods all leverage the propose-then-classify subtasks, inspired from the object detection task from the 2D counterparts. Analogous to the image-based object detectors, 3D object detector heads often employ a two-stage or one-stage detection head, to name a few.

<!-- chunk {"id": "body-0014", "role": "body", "section": "3D Object Detection from Point Clouds", "weight": 1.0} -->

These methods have been well refined, but due to the inherent independent nature of the propose-then-classify objective, suffer from multiple independent predictions per-location, and must be post-processed by threshold selection and suppression techniques. Most popular among them is NMS, but these methods all lead to information loss.

<!-- chunk {"id": "body-0015", "role": "body", "section": "Autoregressive Object Detection", "weight": 1.0} -->

Sequential generation originally was popularized within Natural Language Processing (NLP), where transformer-based autoregressive models demonstrate great success in diverse NLP applications, such as machine translation, question answering, and reasoning. Recently, there has been significant interest in extending this sequential modeling paradigm to the vision domain. One direction is developing large vision-language models (VLMs). These models perform sequential language generation conditioned on visual inputs, primarily addressing tasks like visual question answering and image captioning. For the object detection task, Pix2Seq pioneered in formulating 2D object detection as a sequence prediction problem. It represents the set of bounding boxes and class labels as a discrete sequence of tokens, which a decoder generates autoregressively conditioned on the input image. Subsequent works like Pix2Seq v2 and Rex-Omni further extend this paradigm to create unified models that can perform both object detection and a variety of other 2D vision tasks. For the 3D LiDAR point cloud modality, autoregressive approaches to object detection remain largely unexplored. One related work, Point2Seq, models detection as the sequential prediction of bounding box attributes.

<!-- chunk {"id": "body-0016", "role": "body", "section": "Autoregressive Object Detection", "weight": 1.0} -->

However, its autoregressive process only operates along the attribute dimension. Across boxes, all bird's-eye-view (BEV) cells predict for the same type of attribute in parallel. To the best of our knowledge, we are the first to investigate fully autoregressive detection for LiDAR point cloud data.

<!-- chunk {"id": "body-0017", "role": "body", "section": "Method", "weight": 1.0} -->

Existing regression-based 3D detectors rely heavily on hand-crafted components such as customized losses for each box attribute and anchor assignment strategies. Inspired by language modeling, we cast 3D object detection as a sequence generation task, demonstrating that such complexity can be largely avoided. Our framework adopts a unified cross-entropy loss across all tokenized box attributes, and removes the need for post-processing steps such as matching and NMS, thereby significantly simplifying the modeling pipeline. Despite its simplicity, AutoReg3D achieves performance on par with state-of-the-art regression-based 3D detectors. Moreover, AutoReg3D is compatible with existing 3D backbones, enabling straightforward integration with current architectures.

<!-- chunk {"id": "body-0018", "role": "body", "section": "Method", "weight": 1.0} -->

Beyond a simpler detection process, our formulation also presents unique opportunities in improving 3D detection performance. By modeling a conditional probability distribution rather than performing direct regression, we are able to unlock two key capabilities. First, we demonstrate that the model can be further improved through reinforcement learning. Additionally, we show that by providing hints at test time, our method can recover from failure cases that are challenging for conventional detectors.

<!-- chunk {"id": "body-0019", "role": "body", "section": "Method", "weight": 1.0} -->

In this section, we begin by introducing our formulation, architecture, training objective, and inference process in Section 3.1, and then detail the unique opportunities in Section 3.2.

<!-- chunk {"id": "body-0020", "role": "body", "section": "3D Object as Tokens", "weight": 1.0} -->

In LiDAR-based 3D object detection, objects are described by their class label and 3D bounding boxes parameterized by their center $(x,y,z)$, dimensions $(l,w,h)$, yaw angle $(\psi)$, and velocity $(v_{x},v_{y})$ in an ego-relative coordinate system. To represent bounding boxes using tokens, we are inspired by the quantization strategy of and quantize the bounding box values uniformly into an integer between $t_{k}\in[1,n_{k}]$, where $k\in\{x,y,z,l,w,h,\psi,v_{x},v_{y}\}$. Unlike, which uses a shared vocabulary for all box parameters, we adopt a separate vocabulary for each parameter type to better model their distinct range and semantic meaning.

<!-- chunk {"id": "body-0021", "role": "body", "section": "Sequence Ordering", "weight": 1.0} -->

We order the token sequences of individual objects into a single sequence to represent the entire scene. In 2D object detection, autoregressive methods order objects randomly, and enforcing spatial ordering does not benefit final detection performance. In contrast, objects are inherently ordered in 3D space. For instance, in ego-relative settings such as driving, nearby objects occlude those farther away. It is therefore natural to detect foreground objects first before reasoning about occluded ones. This intrinsic dependency in 3D object detection motivates the use of a deterministic ordering between objects in the scene. In particular, we arrange objects in near-to-far order according to their distance from the ego vehicle.

<!-- chunk {"id": "body-0022", "role": "body", "section": "Autoregressive Model", "weight": 1.0} -->

We model the joint probability distribution of all tokens in the scene given the point-cloud $\mathbf{X}$: where ${\bm{o}}$ denotes the sequence of object tokens. To model the conditional probability $p({\bm{o}}_{i}|{\bm{o}}_{1:i-1},\mathbf{X})$, we adopt an encoder-decoder architecture, the encoder extracts a global feature representation from the point cloud, while a Transformer decoder autoregressively predicts tokens one at a time. By conditioning each prediction on prior outputs, the model naturally captures dependencies among objects in the scene. Our approach is flexible, as it is compatible with any point cloud encoder that outputs hidden scene representations. We intentionally keep our architecture design minimal and modular, enabling integration with a wide range of existing 3D backbones.

<!-- chunk {"id": "body-0023", "role": "body", "section": "Training Objective", "weight": 1.0} -->

We train the model to maximize the likelihood of the ground-truth token sequence ${\bm{o}}$ given the input point cloud $\mathbf{X}$. The optimization objective can be written as follows: Unlike regression-based detectors that require multiple task-specific losses (e.g., for box center, size, orientation, and velocity), our approach uses a single unified cross-entropy loss across all token types. This formulation eliminates the need for hand-crafted losses and weighting, reinforcing the overall simplicity of our design. See Algorithm 1 for implementation of training loop in pseudocode.

<!-- chunk {"id": "body-0024", "role": "body", "section": "cross_entropy: unified CE loss over all tokens", "weight": 1.0} -->

for X, boxes in dataloader: # point cloud and GT boxes boxes = sort(boxes) # enforce ordering seq = tokenizer.encode(boxes) seq_tgt = seq logits = Dec(F, seq_in) loss = cross_entropy(logits, seq_tgt) Algorithm 1 Training (Teacher Forcing)

<!-- chunk {"id": "body-0025", "role": "body", "section": "Inference and Decoding", "weight": 1.0} -->

At inference time, object tokens are sampled sequentially according to the learned conditional distribution $p({\bm{o}}_{i}|{\bm{o}}_{1:i-1},\mathbf{X})$. Unlike regression-based detectors that directly output fixed numbers of bounding boxes with associated confidence scores, our model samples tokens from a learned distribution, reflecting the probabilistic nature of scene generation. This formulation allows the number of predicted objects to vary naturally and eliminates the need for anchors, confidence thresholds, or post-processing steps such as NMS. We explore several decoding strategies commonly used in autoregressive models, including nucleus sampling, and deterministic approaches such as beam search, and greedy decoding, where we simply choose the most probable token. In practice, we adopt greedy decoding for all experiments unless otherwise specified, as it is the simplest approach with minimal computational overhead and achieves performance comparable to more complex decoding methods. The pseudocode for inference procedure is shown in Algorithm 2.

<!-- chunk {"id": "body-0026", "role": "body", "section": "Dec: autoregressive Transformer decoder", "weight": 1.0} -->

logits = Dec(F, seq) t = argmax(logits) # greedy decoding if t == "<END>" or len(seq) > T_max: boxes = tokenizer.decode(seq) # tokens to 3D boxes Algorithm 2 Inference (Autoregressive Decoding)

<!-- chunk {"id": "body-0027", "role": "body", "section": "Modeling Details", "weight": 1.0} -->

We model our detector as an encoder-decoder architecture, where the autoregressive 3D object detector's decoder is a 6-layer Transformer decoder that cross-attends to the point-cloud features encoded by the backbone model. A schematic of the encoder-decoder model is in Figure 2. The cross-attention mechanism ensures that object generation remains conditioned on the input point-cloud features throughout the decoding process, following standard practice in encoder-decoder architectures. We use learnable positional embeddings for the relative point-cloud features in bird's-eye view. Specifically, we decompose the 2D position into separate embeddings for the relative indices along the $x$ and $y$ directions, then sum these two embeddings to obtain the final positional encoding for each feature. This approach provides spatial awareness by distinguishing between the two spatial dimensions while maintaining linear space complexity rather than quadratic. We further embed the position of the sequence generation with a learnable positional embedding, common in sequence modeling. We purposefully keep the architecture design simple, and due to computational limitations, leave scaling model size to future work.

<!-- chunk {"id": "body-0028", "role": "body", "section": "Reinforcement Learning Fine-tuning", "weight": 1.0} -->

While teacher-forcing maximizes token likelihood, it does not explicitly optimize the set-level detection objective. Our sequence prediction formulation enables RL fine-tuning of AutoReg3D with a sequence-level reward aligned with detection quality at inference time, thereby improving global consistency. Specifically, we adopt RL strategy based on GRPO. Given a scene point cloud $\mathbf{X}$, we sample a group of $G$ detection sequences $\{{\bm{o}}_{1},{\bm{o}}_{2},\dots,{\bm{o}}_{G}\}$ from the current detection policy $\pi_{\theta}$.

<!-- chunk {"id": "body-0029", "role": "body", "section": "Reinforcement Learning Fine-tuning", "weight": 1.0} -->

We define a task-aligned reward. Given a set of ground-truth boxes $B_{c}=\{b_{1},b_{2},\dots,b_{3}\}$ and a set predicted boxes $\hat{B}_{c}=\{\hat{b}_{1},\hat{b}_{2},\dots,\hat{b}_{3}\}$ that belong to class $c\in\mathcal{C}$, we calculate each ground-truth box's maximum IoU $r^{*}_{i}$ with the predicted boxes in the same class. We calculate the class-averaged reward $r$ inspired by F1: The GRPO objective is formulated as follows: Where $\hat{A}_{i,t}$ is the estimated advantage, $\rho_{i,t}$ is the importance sampling ratio, and $\pi_{\text{ref}}$ is the frozen detection policy after supervised training.

<!-- chunk {"id": "body-0030", "role": "body", "section": "Cascading Refinement", "weight": 1.0} -->

A notable advantage of our conditional autoregressive formulation is its ability to incorporate external inputs as hints during inference. Unlike regression-based detectors, which predict objects independently, our model can condition future predictions on user-provided or pre-existing information, such as bounding boxes or partial detections, as input tokens to guide subsequent predictions.

<!-- chunk {"id": "body-0031", "role": "body", "section": "Cascading Refinement", "weight": 1.0} -->

To illustrate this capability, we cascade the output of a prior model, which generates a strong initial prediction, into a completion model that refines it. We then aggregate the predictions using a simple clustering strategy, where overlapping boxes with IoU above a threshold are aggregated. This procedure yields consistent improvements over using either the prior model or the completion model alone.

<!-- chunk {"id": "body-0032", "role": "body", "section": "Cascading Refinement", "weight": 1.0} -->

Overall, this conditional reasoning capability highlights the potential of the sequence-based formulation beyond standard 3D detection, allowing the model to incorporate external priors or partial observations from other detectors, systems, or user inputs.

<!-- chunk {"id": "body-0033", "role": "body", "section": "Experiments", "weight": 1.0} -->

In this section, we compare AutoReg3D with state-of-the-art LiDAR-based 3D detectors on nuScenes, demonstrate unique capabilities enabled by autoregressive formulation (RL-based optimization and interactive correction), and present ablation studies analyzing key design choices.

<!-- chunk {"id": "body-0034", "role": "body", "section": "Experiment Setup", "weight": 1.0} -->

We first describe the experimental setup, including the dataset, evaluation metrics, and implementation details.

<!-- chunk {"id": "body-0035", "role": "body", "section": "Dataset", "weight": 1.0} -->

We conduct our experiments on the nuScenes dataset. nuScenes is a large-scale autonomous driving dataset that is widely used for 3D perception. It consists of $1{,}000$ driving scenes collected in Boston and Singapore, with $700$ scenes for training, $150$ for validation, and $150$ for testing. The dataset provides 3D annotations for $10$ object categories, recorded at $2\,\mathrm{Hz}$ and covering a LiDAR range of approximately $50\,\mathrm{m}$.

<!-- chunk {"id": "body-0036", "role": "body", "section": "Metrics for Detection", "weight": 1.0} -->

The standard nuScenes 3D detection benchmark reports mean Average Precision (mAP) and the nuScenes Detection Score (NDS). NDS is computed as a weighted combination of mAP and five true-positive error terms that measure translation, scale, orientation, velocity, and attribute accuracy. However, mAP requires detectors to output confidence scores, which is natural for traditional anchor-based 3D detectors. These scores originate from formulating detection as a classification problem, where each anchor predicts how likely it corresponds to an object versus background. In contrast, our method casts detection as a sequence generation problem and does not produce such objectness scores. As a result, the standard mAP and NDS metrics are not directly applicable. Similar to, we adopt Precision, Recall, and F1 score as our evaluation metrics, which are score-independent. Following nuScenes conventions, a prediction is considered correct if its center lies within a set of official distance thresholds from a ground-truth box. For each class and each distance threshold, we compute Precision, Recall, and F1, and report their average.

<!-- chunk {"id": "body-0037", "role": "body", "section": "Tokenization", "weight": 1.0} -->

To build our customized vocabulary, we uniformly quantize each continuous box parameter $x,y,z,l,w,h,\psi,v_{x},v_{y}$. Specifically, we determine bin count by balancing quantization error with vocab size, with bin widths $0.05\,\mathrm{m}$ for center/size; $0.05\,\mathrm{rad}$ for yaw; and $0.1\,\mathrm{m/s}$ for velocity. Together with class tokens and the special \[start\], \[end\], and \[pad\] tokens, this results in a vocabulary of $6{,}819$ tokens. More details and analysis of different tokenization strategies are provided in Sec.˜D.2 of the supplementary.

<!-- chunk {"id": "body-0038", "role": "body", "section": "Implementation Details", "weight": 1.0} -->

For supervised learning (*i.e*., teacher forcing), we adopt the AdamW optimizer with a learning rate of $1\times 10^{-3}$ and a cosine warm-up and decay schedule. We follow the standard data processing and augmentation pipeline commonly used in prior LiDAR-based 3D detectors. During autoregressive decoding, we restrict sampling to the subset of tokens valid for the current attribute type. For GRPO training, we use a group size of 8, omit the KL penalty by setting $\beta=0$, and train with a batch size of 64. Please refer to supplementary for more implementation details.

<!-- chunk {"id": "body-0039", "role": "body", "section": "Main Results", "weight": 1.0} -->

Method Encoder Det. Head Prec. Rec. F1 PointPillars Pillar Conv. Anchor-based 58.3 50.0 53.1 CenterPoint Center-based 67.9 53.3 59.5 Ours AR Transformer 69.6 52.4 59.2 SECOND Voxel Conv. Anchor-based 63.5 55.6 59.1 CenterPoint Center-based 72.8 60.3 65.8 Ours AR Transformer 74.9 59.4 65.8 DSVT Transformer Non-AR Transformer 79.1 66.3 71.6 Ours AR Transformer 77.0 64.1 69.5 LION Mamba Non-AR Transformer 78.6 68.3 72.5 Ours AR Transformer 77.5 65.2 70.4 Table 1: NuScenes Validation Detection Performance. We report precision, recall, and F1 results for AutoReg3D compared to baseline methods, grouped by encoder type. For methods that require thresholding, we select the threshold that yields the highest F1 score on the training set. Across all encoder types, AutoReg3D achieves competitive performance and surpasses proposal-then-classify detectors.

<!-- chunk {"id": "body-0040", "role": "body", "section": "Supervised Training Performance", "weight": 1.0} -->

We evaluate the feasibility and general adaptability of our autoregressive formulation by comparing our method against a diverse set of commonly adopted baseline methods spanning three representative point cloud encoder families: pillar-based, voxel-based, transformer-based, and Mamba-based architectures. For each encoder type, we initialize our model with the corresponding pre-trained backbone used from prior works. Specifically, we use the encoder weights from CenterPoint-Pillar for pillar-based models, CenterPoint-Voxel for voxel-based models, DSVT for transformer-based models, and LION for Mamba-based models.

<!-- chunk {"id": "body-0041", "role": "body", "section": "Supervised Training Performance", "weight": 1.0} -->

Across all encoder types, AutoReg3D achieves precision--recall near the precision--recall frontier of their respective baselines (Figure 3). For fair comparison, we select the confidence thresholds for all baseline detectors by choosing the value that maximizes F1 score on the training set. As shown in Table 1, our method achieves performance on par with existing regression-based detectors across all encoder types. Our voxel-based model matches the F1 score of CenterPoint at 65.8. Notably, for both pillar-based and voxel-based models, our method attains higher precision than their regression-based counterparts. We attribute this to the interdependent nature of our autoregressive generation process, where each box is conditioned on previously generated ones. This reduces false positives compared to regression-based methods that assume independence among objects. See Figure 4 (a) for qualitative examples.

<!-- chunk {"id": "body-0042", "role": "body", "section": "Reinforcement Learning Performance", "weight": 1.0} -->

Our autoregressive formulation also enables further performance gains through reinforcement learning. During RL fine-tuning, we freeze the encoder and optimize only the autoregressive detection head using GRPO. As shown in Table 2, this additional training stage improves the voxel-based model's F1 score from 65.8 to 66.7. The improvement is primarily driven by increased recall, reflecting the impact of our task-specific reward, which encourages the model to generate more complete prediction sequences and successfully detect objects that were previously missed.

<!-- chunk {"id": "body-0043", "role": "body", "section": "Reinforcement Learning Performance", "weight": 1.0} -->

Model Precision Recall F1 Teacher Forcing 74.9 59.4 65.8 + GRPO 74.5 60.9 66.7 Table 2: Performance with RL Fine-tuning. Observe that fine-tuning with GRPO directly on IoU further boosts performance.

<!-- chunk {"id": "body-0044", "role": "body", "section": "Method Analysis", "weight": 1.0} -->

We perform ablation on token ordering, decoding and inference method using our voxel-based autoregressive model.

<!-- chunk {"id": "body-0045", "role": "body", "section": "Effect of Object Ordering", "weight": 1.0} -->

We study how different object ordering strategies affect detection performance in our autoregressive framework. As shown in Table 3, we compare three orderings: random order, descending order by the number of LiDAR points within each ground-truth box, and a distance-based near-to-far ordering. We observe that the near-to-far ordering significantly outperforms both random and point number-based ordering. By predicting objects from near to far, the model effectively exploits the interdependent nature of the task, where close-by objects inform the prediction of farther objects. Ordering by point count performs better than random ordering, as it partially correlates with distance (closer objects often contain more points), but it remains an imperfect proxy because small yet close objects (e.g., pedestrians) may have fewer points. Random ordering performs the worst, as it fails to exploit any structural dependencies between objects.

<!-- chunk {"id": "body-0046", "role": "body", "section": "Effect of Object Ordering", "weight": 1.0} -->

Order Precision Recall F1 Random 68.9 49.9 56.3 Point Number 72.8 55.2 61.8 Near-to-far 74.9 59.4 65.8 Table 3: Ablation on Object Ordering.

<!-- chunk {"id": "body-0047", "role": "body", "section": "Effect of Object Ordering", "weight": 1.0} -->

Order Precision Recall F1 Cls. Last 74.4 58.1 64.9 Cls. Middle 74.8 58.4 65.2 Cls. First 74.9 59.4 65.8 Table 4: Ablation on Token Ordering.

<!-- chunk {"id": "body-0048", "role": "body", "section": "Effect of Object Ordering", "weight": 1.0} -->

Method Precision Recall F1 Nucleus 67.1 57.8 61.9 Greedy 74.9 59.4 65.8 Beam Search 75.0 59.9 66.1 Table 5: Ablation on Decoding Method.

<!-- chunk {"id": "body-0049", "role": "body", "section": "Effect of Token Ordering", "weight": 1.0} -->

We also ablate the ordering of tokens within each object sequence. As shown in Table 4, we compare three strategies: placing the class token at the beginning, in the middle (after box location), or at the end of the sequence. Both the class-first and class-middle orderings outperform the class-last variant, with class-first yielding the best results. This indicates that having the model determine the object class earlier in the sequence provides useful context for predicting the remaining attributes, thereby improving overall detection performance.

<!-- chunk {"id": "body-0050", "role": "body", "section": "Effect of Decoding Method", "weight": 1.0} -->

We evaluate how different decoding strategies influence detection performance, as shown in Table 5. Specifically, we compare nucleus sampling (top-$p$=0.95, top-$k$=50), greedy decoding, and beam search (4 beams). Beam search achieves the best performance by trading off inference time for accuracy, as it explores multiple candidate sequences and approximates a more globally optimal decoding trajectory, whereas greedy decoding selects only the most likely next token. Nucleus sampling performs the worst, as it favors diversity over accuracy, which is essential for precise object detection.

<!-- chunk {"id": "body-0051", "role": "body", "section": "Effect of Decoding Method", "weight": 1.0} -->

Model Precision Recall F1 Prior only 74.9 59.4 65.8 Completion only 68.9 49.9 56.3 Prior → Completion 74.7 60.2 66.2 Table 6: Cascading Refinement Performance. Refinement via prompting the generation of a random-order model (Completion) improves performance over the distance-ordering model (Prior).

<!-- chunk {"id": "body-0052", "role": "body", "section": "Results on Cascading Refinement", "weight": 1.0} -->

Our near-to-far model accurately detects initial objects but its distance-based ordering prevents recovery of missed boxes at arbitrary locations. The random-order model, while less accurate initially, can generate boxes anywhere in the scene. We combine their complementary strengths through conditional sampling: the near-to-far model generates initial predictions, then the random-order model produces additional detections conditioned on these results to fill gaps. As shown in Table 6, this cascading approach outperforms either model alone. Notably, given approximately correct context from the distance-based model, the random-order model significantly exceeds its standalone performance and improves the performance over the initial prior. A qualitative example is shown in Figure 4 (b).

<!-- chunk {"id": "body-0053", "role": "body", "section": "Performance with Occlusion", "weight": 1.0} -->

We study the performance of AutoReg3D under occlusion by evaluating objects across four different visibility levels. Table 7 shows that AutoReg3D improves over the baseline *in cases of high occlusion* (visibility $\leq$ 60%), with the largest improvement at the most occluded case (0--40% visible). This supports the intuition that autoregressive modeling leverages the natural inter-object dependencies of 3D scenes, improving detection on partially observed objects.

<!-- chunk {"id": "body-0054", "role": "body", "section": "Failure Mode Analysis", "weight": 1.0} -->

Similar to existing detectors, AutoReg3D's failure modes include missed detections, extra detections, and misclassifications, especially for distant or sparse objects. Interestingly, the extra boxes predicted by AutoReg3D generally respect the overall scene structure (Figure 4 (c)): they rarely overlap with existing predictions and tend to follow road geometry. In contrast to methods that model objects independently, the autoregressive formulation leverages object inter-relations by conditioning on previous predictions, allowing AutoReg3D to produce plausible "guesses" grounded in scene geometry.

<!-- chunk {"id": "body-0055", "role": "body", "section": "Future Directions", "weight": 1.0} -->

Our work focuses on demonstrating the viability of autoregressive 3D point-cloud detection. Further experiments should explore model scaling to larger datasets and architectures. Additionally, while we leverage a semantically expanded vocabulary, learned codebooks that are specific to object detection could improve token efficiency and representation flexibility. These directions were beyond our computational budget but represent natural extensions.

<!-- chunk {"id": "body-0056", "role": "body", "section": "Inference Speed and Applicability", "weight": 1.0} -->

A shared limitation of the autoregressive formulation is inference latency. Despite using bfloat-16 precision and KV-caching, our implementation achieves $\sim$`<!-- -->`{=html}5 Hz under batched inference, corresponding to 1--2 Hz for single-scene inference with voxel-based backbones. While optimization techniques from language modeling exist, their effectiveness for detection remains unexplored, particularly for the LiDAR domain.

<!-- chunk {"id": "body-0057", "role": "body", "section": "Opportunities Enabled by Autoregressive Detectors", "weight": 1.0} -->

By formulating object detection as autoregressive modeling, we connect 3D detection to broader sequence modeling advances. Test-time scaling techniques that trade inference compute for performance may apply to detection. Furthermore, autoregressive representations could facilitate integration with language and vision-language models. This alignment could enable spatial-linguistic reasoning and allow LLMs to leverage 3D spatial data in pretraining. However, achieving such cross-modal alignment requires addressing fundamental differences in data and task objectives not explored in this work. We view our contribution as establishing autoregressive detection viability as a foundation for these future research directions.

<!-- chunk {"id": "body-0058", "role": "body", "section": "Conclusion", "weight": 1.5} -->

This work provides the first viability study for autoregressive 3D object detectors, demonstrating that sequence modeling can achieve competitive performance with proposal-based and query-based methods on standard benchmarks. By leveraging the natural near-to-far ordering in LiDAR data and discretizing geometry with parameter-specific vocabularies, we show that the rigid detection pipeline---anchor assignment, NMS, confidence thresholds---can be replaced with a single autoregressive decoder. Our approach establishes that 3D detection can be formulated as sequence generation, connecting it to the broader ecosystem of autoregressive modeling advances. We hope this work encourages further exploration of sequence modeling for 3D perception tasks.
