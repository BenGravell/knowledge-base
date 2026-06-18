## Introduction

Segment Anything Model (SAM) \[(https://arxiv.org/html/2411.11922v2#bib.bib26)\] has demonstrated impressive performance in segmentation tasks. Recently, SAM 2 \[(https://arxiv.org/html/2411.11922v2#bib.bib35)\] incorporates a streaming memory architecture, which enables it to process video frames sequentially while maintaining context over long sequences. While SAM 2 has shown remarkable capabilities in Video Object Segmentation (VOS \[(https://arxiv.org/html/2411.11922v2#bib.bib46)\]) tasks, generating precise pixel-level masks for objects throughout a video sequence, it still faces challenges in Visual Object Tracking (VOT \[(https://arxiv.org/html/2411.11922v2#bib.bib36)\]) scenarios.

The primary concern in VOT is maintaining consistent object identity and location despite occlusions, appearance changes, and the presence of similar objects. However, SAM 2 often neglects motion cues when predicting masks for subsequent frames, leading to inaccuracies in scenarios with rapid object movement or complex interactions. This limitation is particularly evident in crowded scenes, where SAM 2 tends to prioritize appearance similarity over spatial and temporal consistency, resulting in tracking errors. As illustrated in Figure (https://arxiv.org/html/2411.11922v2#S1.F1 "Figure 1 ‣ 1 Introduction ‣ SAMURAI: Adapting Segment Anything Model for Zero-Shot Visual Tracking with Motion-Aware Memory"), there are two common failure patterns: confusion in crowded scenes and ineffective memory utilization during occlusions.

To address these limitations, we propose incorporating motion information into SAM 2's prediction process. By leveraging the history of object trajectories, we can enhance the model's ability to differentiate between visually similar objects and maintain tracking accuracy in the presence of occlusions. Additionally, optimizing SAM 2's memory management is crucial. The current approach \[(https://arxiv.org/html/2411.11922v2#bib.bib35), (https://arxiv.org/html/2411.11922v2#bib.bib14)\] of indiscriminately storing recent frames in the memory bank introduces irrelevant features during occlusions, compromising tracking performance. Addressing these challenges is essential to adapt SAM 2's rich mask information for robust video object tracking.

To this end, we propose SAMURAI, a SAM-based Unified and Robust zero-shot visual tracker with motion-Aware Instance-level memory. Our proposed method incorporates two key advancements: a motion modeling system that refines the mask selection, enabling more accurate object position prediction in complex scenarios, and an optimized memory selection mechanism that leverages a hybrid scoring system, combining the original mask affinity, object, and motion scores to retain more relevant historical information, so as to enhance the model's overall tracking reliability.

Figure 1: Illustration of two common failure cases in visual object tracking using SAM 2: In a crowded scene with similar appearances between target and background objects, SAM 2 tends to ignore the motion cue and predict where the mask has the higher IoU score. The original memory bank simply chooses and stores the previous n frames into the memory bank, resulting in introducing some bad features during occlusion.

In conclusion, this paper makes the following contributions:

We enhance the visual tracking accuruacy of SAM 2 by incorporating motion information through motion modeling, to effectively handle the fast-moving and occluded objects.

We proposed a motion-aware memory selection mechanism that reduces error in crowded scenes in contrast to the original fixed-window memory by selectively storing relevant frames decided by a mixture of motion and affinity scores.

Our zero-shot SAMURAI achieves state-of-the-art performance on LaSOT, LaSOT$_{\text{ext}}$, GOT-10k, and other VOT benchmarks without additional training or fine-tuning, demonstrating strong generalization of our proposed modules across diverse datasets.

## Related Works

### Visual Object Tracking (VOT)

Visual Object Tracking (VOT) \[(https://arxiv.org/html/2411.11922v2#bib.bib36)\] aims to track objects in challenging video sequences that include variations in object scale, occlusions, and complex backgrounds so as to elevate the robustness and accuracy of tracking algorithms. Siamese-based \[(https://arxiv.org/html/2411.11922v2#bib.bib10), (https://arxiv.org/html/2411.11922v2#bib.bib52)\] and transformer-based \[(https://arxiv.org/html/2411.11922v2#bib.bib12), (https://arxiv.org/html/2411.11922v2#bib.bib47)\] trackers are common approaches by learning embedding similarity. However, due to lacking self-correction of these trackers in the single forward pass evaluation scheme, they can easily drift toward distractors. To this end, recent works \[(https://arxiv.org/html/2411.11922v2#bib.bib49), (https://arxiv.org/html/2411.11922v2#bib.bib18)\] further introduce memory bank and attention to find a better mapping between current frame and history information.

### Segment Anything Model (SAM)

The Segment Anything Model (SAM) \[(https://arxiv.org/html/2411.11922v2#bib.bib26)\] has sparked considerable follow-up research since its introduction. SAM introduces a prompt-based segmentation approach, where users could input points, bounding boxes, or text to guide the model in segmenting any object within an image. The use of SAM has wide-ranging applications like in video understanding \[(https://arxiv.org/html/2411.11922v2#bib.bib7), (https://arxiv.org/html/2411.11922v2#bib.bib38), (https://arxiv.org/html/2411.11922v2#bib.bib39)\] and editing \[(https://arxiv.org/html/2411.11922v2#bib.bib6)\]. Since then, various works have built upon SAM. For example, SAM 2 \[(https://arxiv.org/html/2411.11922v2#bib.bib35)\] expands the model's capabilities to video segmentation \[(https://arxiv.org/html/2411.11922v2#bib.bib11)\], incorporating memory mechanisms for tracking objects across multiple frames in dynamic video sequences. Additionally, efforts have been made to create more efficient variants of SAM for resource-constrained environments, aiming to reduce its computational demands \[(https://arxiv.org/html/2411.11922v2#bib.bib45), (https://arxiv.org/html/2411.11922v2#bib.bib54)\]. Research in medical imaging has also adopted SAM for specialized tasks \[(https://arxiv.org/html/2411.11922v2#bib.bib30)\]. Recently, SAM2Long \[(https://arxiv.org/html/2411.11922v2#bib.bib14)\] uses tree-based memory to enhance object segmentation for long video. However, their higher FPS video sequences and deeper memory tree architectures require exponentially more computing power and memory storage due to the overhead of storing exact paths and time-constrained memory paths. On the other hand, our proposed SAMURAI model, which is built upon SAM 2, has been trained on large-scale segmentation datasets to overcome these challenges and ensure good performance and generalization ability.

### Motion Modeling

Motion modeling is an important component in tracking tasks, which can be categorized into heuristic and learnable approaches. Heuristic methods, such as the widely-used Kalman Filter (KF) \[(https://arxiv.org/html/2411.11922v2#bib.bib24)\], rely on fixed motion priors and predefined hyper-parameters to predict object trajectories. While KF has proven effective in many tracking benchmarks, it often fails in scenarios with intense or abrupt motion. Other methods \[(https://arxiv.org/html/2411.11922v2#bib.bib1)\] attempt to counteract intense or abrupt object motion by compensating for camera movement before applying traditional KF-based prediction. However, both the standard and noise scale adaptive (NSA) Kalman Filters \[(https://arxiv.org/html/2411.11922v2#bib.bib15)\] come with a multitude of hyper-parameters, potentially restricting their effectiveness to specific types of motion scenarios. In contrast, learnable motion models have attracted increasing interest due to their data-driven nature. Tracktor \[(https://arxiv.org/html/2411.11922v2#bib.bib2)\] is the first to use trajectory boxes as Regions of Interest (RoI) in a Faster-RCNN to extract features and regress the object's position across frames. MotionTrack \[(https://arxiv.org/html/2411.11922v2#bib.bib43)\] enhances tracking by learning past trajectory representations to predict future movements. MambaTrack \[(https://arxiv.org/html/2411.11922v2#bib.bib22)\] further explores different learning-based motion models architecture like transformer \[(https://arxiv.org/html/2411.11922v2#bib.bib40)\] and state-space model (SSM) \[(https://arxiv.org/html/2411.11922v2#bib.bib21)\]. Our approach is also a learning-based motion modeling with an enhanced heuristic scheme.

Figure 2: The overview of our SAMURAI visual object tracker.

## Revisiting Segment Anything Model 2

Segment Anything Model 2 \[(https://arxiv.org/html/2411.11922v2#bib.bib34)\] contains an image encoder, a mask decoder with a prompt encoder, a memory attention layer, and a memory encoder. We will introduce some preliminaries of SAM 2 and specifically point out the part where SAMURAI is being added.

### Prompt Encoder

The prompt encoder design follows SAM \[(https://arxiv.org/html/2411.11922v2#bib.bib35)\], in which it takes two types of prompts, including sparse (e.g., points, bounding boxes) and dense (e.g., masks). The prompt tokens output by the prompt encoder can be represented as $x_{prompt} \in {N_{tokens} \times d}$. In the visual object tracking, where the ground-truth bounding box of the target object of the first frame $t_{0}$ is provided, SAM 2 takes the positional encoding for the top-left and bottom-right points as inputs while the rest of the sequence uses the predicted mask ${\overline{\mathcal{M}}}_{t - 1}$ from the previous frame as the input to the prompt encoder.

### Mask Decoder

The memory decoder is designed to take the memory-conditioned image embeddings produced by the memory attention layer along with the prompt tokens from the prompt encoder as its inputs. Its multi-head branches can then generate a set of predicted masks, along with the corresponding mask affinity score $s_{mask}$ (it is referred to as IoU score in \[(https://arxiv.org/html/2411.11922v2#bib.bib35), (https://arxiv.org/html/2411.11922v2#bib.bib34)\]), and one object score $s_{obj}$ for the frame as outputs.

The affinity mask score prediction of SAM 2 is supervised with MAE loss as it can represent the overall confidence of the mask, while the object prediction is supervised with cross-entropy loss to determine whether a mask should exist in the frame or not. In the original implementation, the final output mask, $\overline{\mathcal{M}} = \mathcal{M}_{i}$, is selected based on the highest affinity score among the $N_{mask}$ output masks.

However, the affinity score is not a very robust indicator in the case of visual tracking, especially in crowded scenarios where similar objects self-occlude with each other. We introduce an extra motion modeling to keep track of the motion of the target and provide an additional motion score to aid the selection of the prediction.

### Memory Attention Layer

The Memory attention block first performs self-attention with the frame embeddings and then performs cross-attention between the image embeddings and the contents of the memory bank. The unconditional image embeddings, therefore, get contextualized with the previous output masks, previous input prompts, and object pointers.

### Memory Encoder and Memory Bank

After the mask decoder generates output masks, the output mask is passed through a memory encoder to obtain a memory embedding. A new memory is created after each frame is processed. These memory embeddings are appended to a Memory Bank, which is a first-in-first-out (FIFO) queue of the latest memories generated during video decoding. At any given time $t$ in the sequence, we can form the memory bank $B_{t}$ as:

which takes the past $N_{mem}$ frames' output $m$ as the components of the memory bank.

This straightforward fixed-window memory implementation may suffer from encoding the incorrect or low-confidence object, which will cause the error to propagate considerably when in the context of a long sequence visual tracking task. Our proposed motion-aware memory selection will replace the original memory bank composition to ensure that better memory features can be kept and conditioned onto the image feature.

## Method

SAM 2 has demonstrated strong performance in basic Visual Object Tracking (VOT) and Video Object Segmentation (VOS) tasks. However, the original model can mistakenly encode incorrect or low-confidence objects, leading to substantial error propagation in long-sequence VOT.

To address the above issues, we propose a Kalman Filter (KF)-based motion modeling on top of the multi-masks selection (in [4.1](https://arxiv.org/html/2411.11922v2#S4.SS1 "4.1 Motion Modeling ‣ 4 Method ‣ SAMURAI: Adapting Segment Anything Model for Zero-Shot Visual Tracking with Motion-Aware Memory")) and an enhanced memory selection based on a hybrid scoring system that combines affinity and motion scores (in [4.2](https://arxiv.org/html/2411.11922v2#S4.SS2 "4.2 Motion-Aware Memory Selection ‣ 4 Method ‣ SAMURAI: Adapting Segment Anything Model for Zero-Shot Visual Tracking with Motion-Aware Memory")). These enhancements are designed to strengthen the model's ability to track objects accurately in complex video scenarios. Importantly, this approach does not require fine-tuning, nor does it require additional training, and it can be integrated directly into the existing SAM 2 model. By improving the selection of predicted masks without additional computational overhead, this method provides a reliable, real-time solution for online VOT.

### Motion Modeling

Motion modeling has long been an effective approach to Visual Object Tracking (VOT) and Multiple Object Tracking (MOT) \[(https://arxiv.org/html/2411.11922v2#bib.bib51), (https://arxiv.org/html/2411.11922v2#bib.bib5), (https://arxiv.org/html/2411.11922v2#bib.bib1)\] in resolving association ambiguities. We employ the linear-based Kalman filter \[(https://arxiv.org/html/2411.11922v2#bib.bib24)\] as our baseline to demonstrate the incorporation of motion modeling in improving tracking accuracy.

In our visual object tracking framework, we integrate the Kalman filter to enhance bounding box position and dimension predictions, which in turn helps select the most confident mask out of $N$ candidates from $\mathcal{M}$. We define the state vector $\mathbf{x}$ as:

where $x$, $y$ represents the center coordinate of the bounding box, $w$ and $h$ denote its width and height, respectively, and their corresponding velocities are represented by the dot notation. For each mask $\mathcal{M}_{i}$, the corresponding bounding box ${\mathbf{d}}_{i}$ is derived by computing the minimum and maximum $x$ and $y$ coordinates of the mask's non-zero pixels. The Kalman filter operates in a predict-correct cycle, where the state prediction ${\hat{\mathbf{x}}}_{t + {1|t}}$ is given by:

the KF-IoU score $s_{kf}$ is then computed by calculating the Intersection over Union (IoU) between the predicted masks $\mathcal{M}$ and the bounding box derived from the Kalman filter's predicted state. We then select the mask that maximizes a weighted sum of the KF-IoU score and the original affinity score:

Finally, the update is performed using:

where ${\mathbf{z}}_{t}$ is the measurement, the bounding box derived from the mask we selected, used to update. $\mathbf{F}$ is the linear state transition matrix, ${\mathbf{K}}_{n}$ is the Kalman gain, and $\mathbf{H}$ is the observation matrix. Furthermore, to ensure the robustness of the motion modeling after the targeted object reappears or the poor mask qualities for a certain period of time, we also maintain a stable motion state where we take consideration of the motion module if and only if the tracked object is being successfully update in the past $\tau_{kf}$ frames.

### Motion-Aware Memory Selection

Table 1: Visual object tracking results on LaSOT, LaSOText, and GOT-10k. † LaSOText are evaluated on trackers to be trained with LaSOT. ‡ GOT-10k protocol only allows trackers to be trained using its corresponding train split. The T, S, B, L represents the size of the ViT-based backbone while the subscript is the search region. Bold represents the best while underline represents the second.

The original SAM 2 prepares the conditioned visual feature of the current frame based on selecting $N_{mem}$ from the previous frames. In \[(https://arxiv.org/html/2411.11922v2#bib.bib34)\], the implementation simply selects the $N_{mem}$ most recent frames based on the qualities of the target. However, this approach has the weakness of not being able to handle longer occlusion or deformation, which is common in visual object tracking tasks.

To construct an effective memory bank of object cues considering motion, we employ a selective approach for choosing frames from previous time steps based on three scoring: the mask affinity score, object occurrence score, and motion score. We select the frame as an ideal candidate for memory if and only if all three scores meet their corresponding thresholds (e.g., $\tau_{mask}$, $\tau_{obj}$, $\tau_{kf}$). We iterate back in time from the current frame and repeat the verification. We select $N_{mem}$ memories based on the above scoring function and obtain a motion-aware memory bank $B_{t}$:

where $N_{max}$ is the maximum number of frames to look back. The motion-aware memory bank $B_{t}$ is subsequently passed through the memory attention layer and then directed to mask decoder $D_{mask}$ to perform mask decoding at current timestamp. Note that we follow the $N_{mem} = 7$ as the SAM 2 is trained under these specific memory bank settings.

The proposed motion modeling and memory selection module can significantly enhance visual object tracking without the need for retraining and does not add any computational overhead to the existing pipeline. It is also model-agnostic and potentially applicable to other tracking frameworks beyond SAM 2. By combining motion modeling with intelligent memory selection, we can enhance tracking performance in challenging real-world applications without sacrificing efficiency.

## Experiments

### Benchmarks

We evaluate the zero-shot performance of our SAMURAI on the following VOT benchmarks:

### LaSOT \[[16](https://arxiv.org/html/2411.11922v2#bib.bib16)\]

is a visual object tracking dataset comprising 1,400 videos across 70 diverse object categories with an average sequence length of 2,500 frames. It is divided into training and testing sets, consisting of 1,120 and 280 sequences, respectively, with 16 training and 4 testing sequences for each category.

### LaSOT$_{\text{ext}}$ \[[17](https://arxiv.org/html/2411.11922v2#bib.bib17)\]

is an extension to the original LaSOT dataset, introducing an additional 150 video sequences across 15 new object categories. These new sequences are specifically designed to focus on occlusions and variations in small objects, which is more challenging, and the standard protocol is to evaluate the models trained on LaSOT directly on the LaSOT$_{\text{ext}}$.

### GOT-10k \[[23](https://arxiv.org/html/2411.11922v2#bib.bib23)\]

comprises over 10,000 video segments of real-world moving objects, spanning more than 560 object classes and 80+ motion patterns. A key aspect of GOT-10k is its one-shot evaluation protocol, which requires trackers to be trained exclusively on the designated training split, with 170 videos reserved for testing.

### TrackingNet \[[33](https://arxiv.org/html/2411.11922v2#bib.bib33)\]

is a large-scale tracking dataset that covers a wide selection of object classes in broad and diverse contexts in the wild. It has a total of 30,643 videos split into 30,132 training videos and 511 testing videos.

### NFS \[[25](https://arxiv.org/html/2411.11922v2#bib.bib25)\]

consists of 100 videos with a total of 380k frames captured with higher frame rate (240 FPS) cameras from real-world scenarios. We use the 30 FPS version of the data with artificial motion blur following other VOT works.

### OTB100 \[[42](https://arxiv.org/html/2411.11922v2#bib.bib42)\]

is one of the earliest visual tracking benchmarks that annotated sequences with attribute tags. It contains 100 sequences with an average length of 590 frames.

Figure 3: SUC and Pnorm plots of LaSOT and LaSOText.

### Quantitative Results

### Results on LaSOT and LaSOT$_{\text{ext}}$

Table (https://arxiv.org/html/2411.11922v2#S4.T1 "Table 1 ‣ 4.2 Motion-Aware Memory Selection ‣ 4 Method ‣ SAMURAI: Adapting Segment Anything Model for Zero-Shot Visual Tracking with Motion-Aware Memory") presents the visual object tracking results on the LaSOT and LaSOT$_{\text{ext}}$ datasets. Our method, SAMURAI, demonstrates significant improvements over both the zero-shot and supervised methods on all three metrics (shown in Figure (https://arxiv.org/html/2411.11922v2#S5.F3 "Figure 3 ‣ OTB100 ‣ 5.1 Benchmarks ‣ 5 Experiments ‣ SAMURAI: Adapting Segment Anything Model for Zero-Shot Visual Tracking with Motion-Aware Memory")). Although the supervised VOT method such as \[(https://arxiv.org/html/2411.11922v2#bib.bib55), (https://arxiv.org/html/2411.11922v2#bib.bib29)\] show quite impressive results, the zero-shot SAMURAI in contrast show its great generalization ability with comparalbe zero-shot performance. Furthermore, all SAMURAI models surpass the state-of-the-art on all metrics on LaSOT$_{\text{ext}}$.

Table 2: Visual object tracking results on AUC (%) of our proposed method with state-of-the-art methods on TrackingNet, NFS, and OTB100 datasets. Bold represents the best while underline represents the second.

Table 3: Ablation on the effectiveness of the proposed modules.

Table 4: Ablation on the sensitivity of the motion weight αkf.

Table 5: Visual object tracking results of the proposed SAMURAI compare to the baseline SAM-based tracking method.

Table 6: Attribute-wise AUC(%) Results for LaSOT and LaSOText.

### Results on GOT-10k

Table (https://arxiv.org/html/2411.11922v2#S4.T1 "Table 1 ‣ 4.2 Motion-Aware Memory Selection ‣ 4 Method ‣ SAMURAI: Adapting Segment Anything Model for Zero-Shot Visual Tracking with Motion-Aware Memory") also presents the visual object tracking results on the GOT-10k dataset. Note that the GOT-10k protocol only allows trackers to be trained using its corresponding train split, as some papers may refer to them as a one-shot method. SAMURAI-B shows a 2.1% improvement on AO and 2.9% on OP~0.5~ over SAM2.1-B while SAMURAI-L shows a 0.6% improvement on AO and 0.7% on OP~0.5~. All SAMURAI models surpass the state-of-the-art on all metrics on GOT-10k.

### Results on TrackingNet, NFS, and OTB100

Table (https://arxiv.org/html/2411.11922v2#S5.T2 "Table 2 ‣ Results on LaSOT and LaSOT_"ext". ‣ 5.2 Quantitative Results ‣ 5 Experiments ‣ SAMURAI: Adapting Segment Anything Model for Zero-Shot Visual Tracking with Motion-Aware Memory") presents the visual object tracking results on four widely compared benchmarks. Our zero-shot SAMURAI-L model is comparable to or can surpass the state-of-the-art supervised method on AUC, showcasing the capability of our model on various datasets and generalization ability.

### Ablation Studies

### Effect of the Individual Modules

We demonstrate the effect of the with or without memory selection on various settings in Table (https://arxiv.org/html/2411.11922v2#S5.T3 "Table 3 ‣ Results on LaSOT and LaSOT_"ext". ‣ 5.2 Quantitative Results ‣ 5 Experiments ‣ SAMURAI: Adapting Segment Anything Model for Zero-Shot Visual Tracking with Motion-Aware Memory"). Both of the proposed modules had a positive impact on the SAM 2 model, while combining both can achieve the best AUC on the LaSOT dataset with an AUC of 74.23% and P$_{\text{norm}}$ of 82.60%.

### Effect of the Motion Weights

We showcase the effect of the weighting of the score of deciding which mask to trust in Table (https://arxiv.org/html/2411.11922v2#S5.T4 "Table 4 ‣ Results on LaSOT and LaSOT_"ext". ‣ 5.2 Quantitative Results ‣ 5 Experiments ‣ SAMURAI: Adapting Segment Anything Model for Zero-Shot Visual Tracking with Motion-Aware Memory"). The trade-off between motion score and mask affinity score demonstrates a significant impact on tracking performance. Our experiments reveal that setting the motion weight $\alpha_{motion} = 0.2$ yields the best AUC and P$_{\text{norm}}$ score on the LaSOT dataset, indicating an optimal balance enhances both accuracy and robustness in mask selection.

HIPTrack LoRAT SAMURAI (Ours) GT

SAM2.1 (Baseline) SAMURAI (Ours) GT

Figure 4: Visualization of tracking results comparing SAMURAIwith existing methods. (Top) Conventional VOT methods often struggle in crowded scenarios where the target object is surrounded by objects with similar appearances. (Bottom) The baseline SAM-based method suffers from fixed-window memory composition, leading to error propagation and reduced overall tracking accuracy due to ID switches.

### Baseline Comparison

To demonstrate the effectiveness of the proposed motion modeling and motion-aware memory selection mechanism in SAMURAI, we conduct a detailed apple-to-apple comparison of the SAM 2 \[(https://arxiv.org/html/2411.11922v2#bib.bib34)\] at all of the backbone variations on LaSOT and LaSOT$_{\text{ext}}$. The baseline SAM 2 employs the original memory selection and directly predicts the mask with the highest IoU score. Table (https://arxiv.org/html/2411.11922v2#S5.T5 "Table 5 ‣ Results on LaSOT and LaSOT_"ext". ‣ 5.2 Quantitative Results ‣ 5 Experiments ‣ SAMURAI: Adapting Segment Anything Model for Zero-Shot Visual Tracking with Motion-Aware Memory") shows that the proposed method consistently improves upon the baseline with a significant margin on all three metrics, which underscores the robustness and generalization of our approach across different model configurations.

### Attribute-Wise Performance Analysis

We analysis the LaSOT and LaSOT$_{\text{ext}}$ based on the 14 attributes defined in \[(https://arxiv.org/html/2411.11922v2#bib.bib16), (https://arxiv.org/html/2411.11922v2#bib.bib17)\]. In Table (https://arxiv.org/html/2411.11922v2#S5.T6 "Table 6 ‣ Results on LaSOT and LaSOT_"ext". ‣ 5.2 Quantitative Results ‣ 5 Experiments ‣ SAMURAI: Adapting Segment Anything Model for Zero-Shot Visual Tracking with Motion-Aware Memory"), SAMURAI shows consistent success in improving upon the original baseline across all attributes in both datasets but the label IV (Illumination Variation) label on LaSOT$_{\text{ext}}$. By considering motion scoring, the performance gains on attributes like CM (Camera Motion) and FM (Fast Motion) are the largest among the rest, the SAMURAI has a $16.5\%$ and $9.9\%$ gain on CM and FM respectively from LaSOT$_{\text{ext}}$ dataset which is considered one of the most challenging datasets in VOT. Furthermore, the occlusion-related attributes like FOC (Full Occlusion) and POC (Partial Occlusion) also greatly benefited from the proposed motion-aware instance-level memory selection, which showed steady improvement across all model variants and datasets. These findings suggest that the SAMURAI incorporates simple motion estimation to better account for global camera or rapid object movements for better tracking.

### Runtime Analysis

The incorporation of the motion modeling and an enhanced memory selection method into our tracking framework introduces minimal computational overhead, and the runtime measurements conducted on one NVIDIA RTX 4090 GPU remain consistent with the baseline model.

### Qualitative Results

Qualitative comparison between SAMURAI and other methods \[(https://arxiv.org/html/2411.11922v2#bib.bib34), (https://arxiv.org/html/2411.11922v2#bib.bib3), (https://arxiv.org/html/2411.11922v2#bib.bib29)\] are shown in Figure (https://arxiv.org/html/2411.11922v2#S5.F4 "Figure 4 ‣ Effect of the Motion Weights. ‣ 5.3 Ablation Studies ‣ 5 Experiments ‣ SAMURAI: Adapting Segment Anything Model for Zero-Shot Visual Tracking with Motion-Aware Memory"). SAMURAI demonstrates superior visual object tracking results in scenes where multiple objects with similar appearances are present in the video. The short-term occlusions in these examples make it challenging for existing VOT methods to predict or localize the same object consistently over time. Furthermore, the comparison between SAMURAI and the original baseline with visualized masks showcases the improvement gained by adding the motion modeling and memory selection modules, the predicted masks are not always a reliable source to serve as memory therefore having a systematic way of deciding which to trust is valuable. These enhancements benefit the existing framework by providing better guidance for visual tracking without the need to retrain the model or fine-tune it.

## Conclusion

We present SAMURAI, a visual object tracking framework built on top of the segment-anything model by introducing the motion-based score for better mask prediction and memory selection to deal with self-occlusion and abrupt motion in crowded scenes. The proposed modules show consistent improvement on all variations of the SAM models across multiple VOT benchmarks on all metrics. This method does not require re-training nor fine-tuning while demonstrating robust performance on multiple VOT benchmarks with the capability of real-time online inferences.
