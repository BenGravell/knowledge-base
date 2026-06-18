<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

SAMURAI: Adapting Segment Anything Model for Zero-Shot Visual Tracking with Motion-Aware Memory

Topics include Visual tracking, Video segmentation, Segment anything, Zero-shot tracking, Motion-aware memory, Object tracking, Real-time vision, Foundation models.

<!-- chunk {"id": "summary-0002", "role": "summary", "section": "Summary", "weight": 2.0} -->

Adapts SAM 2 for zero-shot visual object tracking by adding motion-aware memory selection that filters the memories used to condition future masks. This directly addresses error accumulation in crowded or fast-motion videos and demonstrates that promptable segmentation models can be made into competitive trackers without task-specific fine-tuning.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

The Segment Anything Model 2 (SAM 2) has demonstrated strong performance in object segmentation tasks but faces challenges in visual object tracking, particularly when managing crowded scenes with fast-moving or self-occluding objects. Furthermore, the fixed-window memory approach in the original model does not consider the quality of memories selected to condition the image features for the next frame, leading to error propagation in videos. This paper introduces SAMURAI, an enhanced adaptation of SAM 2 specifically designed for visual object tracking. By incorporating temporal motion cues with the proposed motion-aware memory selection mechanism, SAMURAI effectively predicts object motion and refines mask selection, achieving robust, accurate tracking without the need for retraining or fine-tuning. SAMURAI operates in real-time and demonstrates strong zero-shot performance across diverse benchmark datasets, showcasing its ability to generalize without fine-tuning. In evaluations, SAMURAI achieves significant improvements in success rate and precision over existing trackers, with a 7.1% AUC gain on LaSOT_ext and a 3.5% AO gain on GOT-10k.

<!-- chunk {"id": "abstract-0004", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Moreover, it achieves competitive results compared to fully supervised methods on LaSOT, underscoring its robustness in complex tracking scenarios and its potential for real-world applications in dynamic environments.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

Segment Anything Model (SAM) has demonstrated impressive performance in segmentation tasks. Recently, SAM 2 incorporates a streaming memory architecture, which enables it to process video frames sequentially while maintaining context over long sequences. While SAM 2 has shown remarkable capabilities in Video Object Segmentation tasks, generating precise pixel-level masks for objects throughout a video sequence, it still faces challenges in Visual Object Tracking scenarios.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

The primary concern in VOT is maintaining consistent object identity and location despite occlusions, appearance changes, and the presence of similar objects. However, SAM 2 often neglects motion cues when predicting masks for subsequent frames, leading to inaccuracies in scenarios with rapid object movement or complex interactions. This limitation is particularly evident in crowded scenes, where SAM 2 tends to prioritize appearance similarity over spatial and temporal consistency, resulting in tracking errors. As illustrated in Figure, there are two common failure patterns: confusion in crowded scenes and ineffective memory utilization during occlusions.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

To address these limitations, we propose incorporating motion information into SAM 2's prediction process. By leveraging the history of object trajectories, we can enhance the model's ability to differentiate between visually similar objects and maintain tracking accuracy in the presence of occlusions. Additionally, optimizing SAM 2's memory management is crucial. The current approach of indiscriminately storing recent frames in the memory bank introduces irrelevant features during occlusions, compromising tracking performance. Addressing these challenges is essential to adapt SAM 2's rich mask information for robust video object tracking.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Introduction", "weight": 1.5} -->

To this end, we propose SAMURAI, a SAM-based Unified and Robust zero-shot visual tracker with motion-Aware Instance-level memory. Our proposed method incorporates two key advancements: a motion modeling system that refines the mask selection, enabling more accurate object position prediction in complex scenarios, and an optimized memory selection mechanism that leverages a hybrid scoring system, combining the original mask affinity, object, and motion scores to retain more relevant historical information, so as to enhance the model's overall tracking reliability.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Introduction", "weight": 1.5} -->

We enhance the visual tracking accuruacy of SAM 2 by incorporating motion information through motion modeling, to effectively handle the fast-moving and occluded objects.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Introduction", "weight": 1.5} -->

We proposed a motion-aware memory selection mechanism that reduces error in crowded scenes in contrast to the original fixed-window memory by selectively storing relevant frames decided by a mixture of motion and affinity scores.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Introduction", "weight": 1.5} -->

Our zero-shot SAMURAI achieves state-of-the-art performance on LaSOT, LaSOT$_{\text{ext}}$, GOT-10k, and other VOT benchmarks without additional training or fine-tuning, demonstrating strong generalization of our proposed modules across diverse datasets.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Visual Object Tracking (VOT)", "weight": 1.0} -->

Visual Object Tracking (VOT) aims to track objects in challenging video sequences that include variations in object scale, occlusions, and complex backgrounds so as to elevate the robustness and accuracy of tracking algorithms. Siamese-based and transformer-based trackers are common approaches by learning embedding similarity. However, due to lacking self-correction of these trackers in the single forward pass evaluation scheme, they can easily drift toward distractors. To this end, recent works further introduce memory bank and attention to find a better mapping between current frame and history information.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Segment Anything Model (SAM)", "weight": 1.0} -->

The Segment Anything Model (SAM) has sparked considerable follow-up research since its introduction. SAM introduces a prompt-based segmentation approach, where users could input points, bounding boxes, or text to guide the model in segmenting any object within an image. The use of SAM has wide-ranging applications like in video understanding and editing. Since then, various works have built upon SAM. For example, SAM 2 expands the model's capabilities to video segmentation, incorporating memory mechanisms for tracking objects across multiple frames in dynamic video sequences. Additionally, efforts have been made to create more efficient variants of SAM for resource-constrained environments, aiming to reduce its computational demands. Research in medical imaging has also adopted SAM for specialized tasks. Recently, SAM2Long uses tree-based memory to enhance object segmentation for long video. However, their higher FPS video sequences and deeper memory tree architectures require exponentially more computing power and memory storage due to the overhead of storing exact paths and time-constrained memory paths. On the other hand, our proposed SAMURAI model, which is built upon SAM 2, has been trained on large-scale segmentation datasets to overcome these challenges and ensure good performance and generalization ability.

<!-- chunk {"id": "body-0014", "role": "body", "section": "Motion Modeling", "weight": 1.0} -->

Motion modeling is an important component in tracking tasks, which can be categorized into heuristic and learnable approaches. Heuristic methods, such as the widely-used Kalman Filter (KF), rely on fixed motion priors and predefined hyper-parameters to predict object trajectories. While KF has proven effective in many tracking benchmarks, it often fails in scenarios with intense or abrupt motion. Other methods attempt to counteract intense or abrupt object motion by compensating for camera movement before applying traditional KF-based prediction. However, both the standard and noise scale adaptive (NSA) Kalman Filters come with a multitude of hyper-parameters, potentially restricting their effectiveness to specific types of motion scenarios. In contrast, learnable motion models have attracted increasing interest due to their data-driven nature. Tracktor is the first to use trajectory boxes as Regions of Interest (RoI) in a Faster-RCNN to extract features and regress the object's position across frames. MotionTrack enhances tracking by learning past trajectory representations to predict future movements. MambaTrack further explores different learning-based motion models architecture like transformer and state-space model (SSM).

<!-- chunk {"id": "body-0015", "role": "body", "section": "Motion Modeling", "weight": 1.0} -->

Our approach is also a learning-based motion modeling with an enhanced heuristic scheme.

<!-- chunk {"id": "body-0016", "role": "body", "section": "Revisiting Segment Anything Model 2", "weight": 1.0} -->

Segment Anything Model 2 contains an image encoder, a mask decoder with a prompt encoder, a memory attention layer, and a memory encoder. We will introduce some preliminaries of SAM 2 and specifically point out the part where SAMURAI is being added.

<!-- chunk {"id": "body-0017", "role": "body", "section": "Prompt Encoder", "weight": 1.0} -->

The prompt encoder design follows SAM, in which it takes two types of prompts, including sparse (e.g., points, bounding boxes) and dense (e.g., masks). The prompt tokens output by the prompt encoder can be represented as $x_{prompt} \in {N_{tokens} \times d}$. In the visual object tracking, where the ground-truth bounding box of the target object of the first frame $t_{0}$ is provided, SAM 2 takes the positional encoding for the top-left and bottom-right points as inputs while the rest of the sequence uses the predicted mask ${\overline{\mathcal{M}}}_{t - 1}$ from the previous frame as the input to the prompt encoder.

<!-- chunk {"id": "body-0018", "role": "body", "section": "Mask Decoder", "weight": 1.0} -->

The memory decoder is designed to take the memory-conditioned image embeddings produced by the memory attention layer along with the prompt tokens from the prompt encoder as its inputs. Its multi-head branches can then generate a set of predicted masks, along with the corresponding mask affinity score $s_{mask}$ (it is referred to as IoU score in ), and one object score $s_{obj}$ for the frame as outputs.

<!-- chunk {"id": "body-0019", "role": "body", "section": "Mask Decoder", "weight": 1.0} -->

The affinity mask score prediction of SAM 2 is supervised with MAE loss as it can represent the overall confidence of the mask, while the object prediction is supervised with cross-entropy loss to determine whether a mask should exist in the frame or not. In the original implementation, the final output mask, $\overline{\mathcal{M}} = \mathcal{M}_{i}$, is selected based on the highest affinity score among the $N_{mask}$ output masks.

<!-- chunk {"id": "body-0020", "role": "body", "section": "Mask Decoder", "weight": 1.0} -->

However, the affinity score is not a very robust indicator in the case of visual tracking, especially in crowded scenarios where similar objects self-occlude with each other. We introduce an extra motion modeling to keep track of the motion of the target and provide an additional motion score to aid the selection of the prediction.

<!-- chunk {"id": "body-0021", "role": "body", "section": "Memory Attention Layer", "weight": 1.0} -->

The Memory attention block first performs self-attention with the frame embeddings and then performs cross-attention between the image embeddings and the contents of the memory bank. The unconditional image embeddings, therefore, get contextualized with the previous output masks, previous input prompts, and object pointers.

<!-- chunk {"id": "body-0022", "role": "body", "section": "Memory Encoder and Memory Bank", "weight": 1.0} -->

After the mask decoder generates output masks, the output mask is passed through a memory encoder to obtain a memory embedding. A new memory is created after each frame is processed. These memory embeddings are appended to a Memory Bank, which is a first-in-first-out (FIFO) queue of the latest memories generated during video decoding.

<!-- chunk {"id": "body-0023", "role": "body", "section": "Memory Encoder and Memory Bank", "weight": 1.0} -->

which takes the past $N_{mem}$ frames' output $m$ as the components of the memory bank.

<!-- chunk {"id": "body-0024", "role": "body", "section": "Memory Encoder and Memory Bank", "weight": 1.0} -->

This straightforward fixed-window memory implementation may suffer from encoding the incorrect or low-confidence object, which will cause the error to propagate considerably when in the context of a long sequence visual tracking task. Our proposed motion-aware memory selection will replace the original memory bank composition to ensure that better memory features can be kept and conditioned onto the image feature.

<!-- chunk {"id": "body-0025", "role": "body", "section": "Method", "weight": 1.0} -->

SAM 2 has demonstrated strong performance in basic Visual Object Tracking (VOT) and Video Object Segmentation (VOS) tasks. However, the original model can mistakenly encode incorrect or low-confidence objects, leading to substantial error propagation in long-sequence VOT.

<!-- chunk {"id": "body-0026", "role": "body", "section": "Method", "weight": 1.0} -->

To address the above issues, we propose a Kalman Filter (KF)-based motion modeling on top of the multi-masks selection (in 4.1) and an enhanced memory selection based on a hybrid scoring system that combines affinity and motion scores (in 4.2). These enhancements are designed to strengthen the model's ability to track objects accurately in complex video scenarios. Importantly, this approach does not require fine-tuning, nor does it require additional training, and it can be integrated directly into the existing SAM 2 model. By improving the selection of predicted masks without additional computational overhead, this method provides a reliable, real-time solution for online VOT.

<!-- chunk {"id": "body-0027", "role": "body", "section": "Motion Modeling", "weight": 1.0} -->

Motion modeling has long been an effective approach to Visual Object Tracking (VOT) and Multiple Object Tracking (MOT) in resolving association ambiguities. We employ the linear-based Kalman filter as our baseline to demonstrate the incorporation of motion modeling in improving tracking accuracy.

<!-- chunk {"id": "body-0028", "role": "body", "section": "Motion Modeling", "weight": 1.0} -->

In our visual object tracking framework, we integrate the Kalman filter to enhance bounding box position and dimension predictions, which in turn helps select the most confident mask out of $N$ candidates from $\mathcal{M}$.

<!-- chunk {"id": "body-0029", "role": "body", "section": "Motion Modeling", "weight": 1.0} -->

where $x$, $y$ represents the center coordinate of the bounding box, $w$ and $h$ denote its width and height, respectively, and their corresponding velocities are represented by the dot notation. For each mask $\mathcal{M}_{i}$, the corresponding bounding box ${\mathbf{d}}_{i}$ is derived by computing the minimum and maximum $x$ and $y$ coordinates of the mask's non-zero pixels.

<!-- chunk {"id": "body-0030", "role": "body", "section": "Motion Modeling", "weight": 1.0} -->

the KF-IoU score $s_{kf}$ is then computed by calculating the Intersection over Union (IoU) between the predicted masks $\mathcal{M}$ and the bounding box derived from the Kalman filter's predicted state.

<!-- chunk {"id": "body-0031", "role": "body", "section": "Motion Modeling", "weight": 1.0} -->

where ${\mathbf{z}}_{t}$ is the measurement, the bounding box derived from the mask we selected, used to update. $\mathbf{F}$ is the linear state transition matrix, ${\mathbf{K}}_{n}$ is the Kalman gain, and $\mathbf{H}$ is the observation matrix. Furthermore, to ensure the robustness of the motion modeling after the targeted object reappears or the poor mask qualities for a certain period of time, we also maintain a stable motion state where we take consideration of the motion module if and only if the tracked object is being successfully update in the past $\tau_{kf}$ frames.

<!-- chunk {"id": "body-0032", "role": "body", "section": "Motion-Aware Memory Selection", "weight": 1.0} -->

The original SAM 2 prepares the conditioned visual feature of the current frame based on selecting $N_{mem}$ from the previous frames. In, the implementation simply selects the $N_{mem}$ most recent frames based on the qualities of the target. However, this approach has the weakness of not being able to handle longer occlusion or deformation, which is common in visual object tracking tasks.

<!-- chunk {"id": "body-0033", "role": "body", "section": "Motion-Aware Memory Selection", "weight": 1.0} -->

To construct an effective memory bank of object cues considering motion, we employ a selective approach for choosing frames from previous time steps based on three scoring: the mask affinity score, object occurrence score, and motion score. We select the frame as an ideal candidate for memory if and only if all three scores meet their corresponding thresholds (e.g., $\tau_{mask}$, $\tau_{obj}$, $\tau_{kf}$). We iterate back in time from the current frame and repeat the verification.

<!-- chunk {"id": "body-0034", "role": "body", "section": "Motion-Aware Memory Selection", "weight": 1.0} -->

where $N_{max}$ is the maximum number of frames to look back. The motion-aware memory bank $B_{t}$ is subsequently passed through the memory attention layer and then directed to mask decoder $D_{mask}$ to perform mask decoding at current timestamp. Note that we follow the $N_{mem} = 7$ as the SAM 2 is trained under these specific memory bank settings.

<!-- chunk {"id": "body-0035", "role": "body", "section": "Motion-Aware Memory Selection", "weight": 1.0} -->

The proposed motion modeling and memory selection module can significantly enhance visual object tracking without the need for retraining and does not add any computational overhead to the existing pipeline. It is also model-agnostic and potentially applicable to other tracking frameworks beyond SAM 2. By combining motion modeling with intelligent memory selection, we can enhance tracking performance in challenging real-world applications without sacrificing efficiency.

<!-- chunk {"id": "body-0036", "role": "body", "section": "LaSOT", "weight": 1.0} -->

is a visual object tracking dataset comprising 1,400 videos across 70 diverse object categories with an average sequence length of 2,500 frames. It is divided into training and testing sets, consisting of 1,120 and 280 sequences, respectively, with 16 training and 4 testing sequences for each category.

<!-- chunk {"id": "body-0037", "role": "body", "section": "LaSOT$_{\\text{ext}}$", "weight": 1.0} -->

is an extension to the original LaSOT dataset, introducing an additional 150 video sequences across 15 new object categories. These new sequences are specifically designed to focus on occlusions and variations in small objects, which is more challenging, and the standard protocol is to evaluate the models trained on LaSOT directly on the LaSOT$_{\text{ext}}$.

<!-- chunk {"id": "body-0038", "role": "body", "section": "GOT-10k", "weight": 1.0} -->

comprises over 10,000 video segments of real-world moving objects, spanning more than 560 object classes and 80+ motion patterns. A key aspect of GOT-10k is its one-shot evaluation protocol, which requires trackers to be trained exclusively on the designated training split, with 170 videos reserved for testing.

<!-- chunk {"id": "body-0039", "role": "body", "section": "TrackingNet", "weight": 1.0} -->

is a large-scale tracking dataset that covers a wide selection of object classes in broad and diverse contexts in the wild. It has a total of 30,643 videos split into 30,132 training videos and 511 testing videos.

<!-- chunk {"id": "body-0040", "role": "body", "section": "NFS", "weight": 1.0} -->

consists of 100 videos with a total of 380k frames captured with higher frame rate (240 FPS) cameras from real-world scenarios. We use the 30 FPS version of the data with artificial motion blur following other VOT works.

<!-- chunk {"id": "body-0041", "role": "body", "section": "OTB100", "weight": 1.0} -->

is one of the earliest visual tracking benchmarks that annotated sequences with attribute tags. It contains 100 sequences with an average length of 590 frames.

<!-- chunk {"id": "body-0042", "role": "body", "section": "Results on LaSOT and LaSOT$_{\\text{ext}}$", "weight": 1.0} -->

Table presents the visual object tracking results on the LaSOT and LaSOT$_{\text{ext}}$ datasets. Our method, SAMURAI, demonstrates significant improvements over both the zero-shot and supervised methods on all three metrics. Although the supervised VOT method such as show quite impressive results, the zero-shot SAMURAI in contrast show its great generalization ability with comparalbe zero-shot performance. Furthermore, all SAMURAI models surpass the state-of-the-art on all metrics on LaSOT$_{\text{ext}}$.

<!-- chunk {"id": "body-0043", "role": "body", "section": "Results on GOT-10k", "weight": 1.0} -->

Table also presents the visual object tracking results on the GOT-10k dataset. Note that the GOT-10k protocol only allows trackers to be trained using its corresponding train split, as some papers may refer to them as a one-shot method. SAMURAI-B shows a 2.1% improvement on AO and 2.9% on OP~0.5~ over SAM2.1-B while SAMURAI-L shows a 0.6% improvement on AO and 0.7% on OP~0.5~. All SAMURAI models surpass the state-of-the-art on all metrics on GOT-10k.

<!-- chunk {"id": "body-0044", "role": "body", "section": "Results on TrackingNet, NFS, and OTB100", "weight": 1.0} -->

Table presents the visual object tracking results on four widely compared benchmarks. Our zero-shot SAMURAI-L model is comparable to or can surpass the state-of-the-art supervised method on AUC, showcasing the capability of our model on various datasets and generalization ability.

<!-- chunk {"id": "body-0045", "role": "body", "section": "Effect of the Individual Modules", "weight": 1.0} -->

We demonstrate the effect of the with or without memory selection on various settings in Table. Both of the proposed modules had a positive impact on the SAM 2 model, while combining both can achieve the best AUC on the LaSOT dataset with an AUC of 74.23% and P$_{\text{norm}}$ of 82.60%.

<!-- chunk {"id": "body-0046", "role": "body", "section": "Effect of the Motion Weights", "weight": 1.0} -->

We showcase the effect of the weighting of the score of deciding which mask to trust in Table. The trade-off between motion score and mask affinity score demonstrates a significant impact on tracking performance. Our experiments reveal that setting the motion weight $\alpha_{motion} = 0.2$ yields the best AUC and P$_{\text{norm}}$ score on the LaSOT dataset, indicating an optimal balance enhances both accuracy and robustness in mask selection.

<!-- chunk {"id": "body-0047", "role": "body", "section": "Baseline Comparison", "weight": 1.0} -->

To demonstrate the effectiveness of the proposed motion modeling and motion-aware memory selection mechanism in SAMURAI, we conduct a detailed apple-to-apple comparison of the SAM 2 at all of the backbone variations on LaSOT and LaSOT$_{\text{ext}}$. The baseline SAM 2 employs the original memory selection and directly predicts the mask with the highest IoU score. Table shows that the proposed method consistently improves upon the baseline with a significant margin on all three metrics, which underscores the robustness and generalization of our approach across different model configurations.

<!-- chunk {"id": "body-0048", "role": "body", "section": "Attribute-Wise Performance Analysis", "weight": 1.0} -->

We analysis the LaSOT and LaSOT$_{\text{ext}}$ based on the 14 attributes defined. In Table, SAMURAI shows consistent success in improving upon the original baseline across all attributes in both datasets but the label IV (Illumination Variation) label on LaSOT$_{\text{ext}}$. By considering motion scoring, the performance gains on attributes like CM (Camera Motion) and FM (Fast Motion) are the largest among the rest, the SAMURAI has a $16.5\%$ and $9.9\%$ gain on CM and FM respectively from LaSOT$_{\text{ext}}$ dataset which is considered one of the most challenging datasets in VOT. Furthermore, the occlusion-related attributes like FOC (Full Occlusion) and POC (Partial Occlusion) also greatly benefited from the proposed motion-aware instance-level memory selection, which showed steady improvement across all model variants and datasets. These findings suggest that the SAMURAI incorporates simple motion estimation to better account for global camera or rapid object movements for better tracking.

<!-- chunk {"id": "body-0049", "role": "body", "section": "Runtime Analysis", "weight": 1.0} -->

The incorporation of the motion modeling and an enhanced memory selection method into our tracking framework introduces minimal computational overhead, and the runtime measurements conducted on one NVIDIA RTX 4090 GPU remain consistent with the baseline model.

<!-- chunk {"id": "body-0050", "role": "body", "section": "Qualitative Results", "weight": 1.0} -->

Qualitative comparison between SAMURAI and other methods are shown in Figure. SAMURAI demonstrates superior visual object tracking results in scenes where multiple objects with similar appearances are present in the video. The short-term occlusions in these examples make it challenging for existing VOT methods to predict or localize the same object consistently over time. Furthermore, the comparison between SAMURAI and the original baseline with visualized masks showcases the improvement gained by adding the motion modeling and memory selection modules, the predicted masks are not always a reliable source to serve as memory therefore having a systematic way of deciding which to trust is valuable. These enhancements benefit the existing framework by providing better guidance for visual tracking without the need to retrain the model or fine-tune it.

<!-- chunk {"id": "body-0051", "role": "body", "section": "Conclusion", "weight": 1.5} -->

We present SAMURAI, a visual object tracking framework built on top of the segment-anything model by introducing the motion-based score for better mask prediction and memory selection to deal with self-occlusion and abrupt motion in crowded scenes. The proposed modules show consistent improvement on all variations of the SAM models across multiple VOT benchmarks on all metrics. This method does not require re-training nor fine-tuning while demonstrating robust performance on multiple VOT benchmarks with the capability of real-time online inferences.
