## Introduction

Figure 1: We introduce the Segment Anything Model 2 (SAM 2), towards solving the promptable visual segmentation task (a) with our foundation model (b), trained on our large-scale SA-V dataset collected through our data engine (c). SAM 2 is capable of interactively segmenting regions through prompts (clicks, boxes, or masks) on one or multiple video frames by utilizing a streaming memory that stores previous prompts and predictions.

Segment Anything (SA) introduced a foundation model for promptable segmentation in images. However an image is only a static snapshot of the real world in which visual segments can exhibit complex motion, and with the rapid growth of multimedia content, a significant portion is now recorded with a temporal dimension, particularly in video data. Many important applications in AR/VR, robotics, autonomous vehicles, and video editing require temporal localization beyond image-level segmentation. We believe a universal visual segmentation system should be applicable to both images and videos.

Segmentation in video aims to determine the spatio-temporal extent of entities, which presents unique challenges beyond those in images. Entities can undergo significant changes in appearance due to motion, deformation, occlusion, lighting changes, and other factors. Videos often have lower quality than images due to camera motion, blur, and lower resolution. Further, efficient processing of a large number of frames is a key challenge. While SA successfully addresses segmentation in images, existing video segmentation models and datasets fall short in providing a comparable capability to "segment anything in videos".

We introduce the Segment Anything Model 2 (SAM 2), a unified model for video and image segmentation (we consider an image as a single-frame video). Our work includes a task, model, and dataset (see Fig. 1).

We focus on the Promptable Visual Segmentation (PVS) task that generalizes image segmentation to the video domain. The task takes as input points, boxes, or masks on any frame of the video to define a segment of interest for which the spatio-temporal mask (i.e., a 'masklet') is to be predicted. Once a masklet is predicted, it can be iteratively refined by providing prompts in additional frames.

Our model (§4) produces segmentation masks of the object of interest, in single images and across video frames. SAM 2 is equipped with a memory that stores information about the object and previous interactions, which allows it to generate masklet predictions throughout the video, and also effectively correct these based on the stored memory context of the object from previously observed frames. Our streaming architecture is a natural generalization of SAM to the video domain, processing video frames one at a time, equipped with a memory attention module to attend to the previous memories of the target object. When applied to images, the memory is empty and the model behaves like SAM.

We employ a data engine (§5) to generate training data by using our model in the loop with annotators to interactively annotate new and challenging data. Different from most existing video segmentation datasets, our data engine is not restricted to objects of specific categories, but instead targeted to provide training data for segmenting any object with a valid boundary, including parts and subparts. Compared to existing model-assisted approaches, our data engine with SAM 2 in the loop is 8.4$\times$ faster at comparable quality. Our final Segment Anything Video (SA-V) dataset (§5.2) consists of 35.5M masks across 50.9K videos, 53$\times$ more masks than any existing video segmentation dataset. SA-V is challenging with small objects and parts that get occluded and re-appear throughout the video. Our SA-V dataset is geographically diverse, and a fairness evaluation of SAM 2 indicates minimal performance discrepancy in video segmentation based on perceived gender, and little variance among the three perceived age groups we evaluated.

Our experiments (§6) show that SAM 2 delivers a step-change in the video segmentation experience. SAM 2 can produce better segmentation accuracy while using 3$\times$ fewer interactions than prior approaches. Further, SAM 2 outperforms prior work in established video object segmentation benchmarks, under multiple evaluation settings, and delivers better performance compared to SAM on image segmentation benchmarks, while being 6$\times$ faster. SAM 2 is shown to be effective across a variety of video and image distributions as observed through numerous zero-shot benchmarks including 17 for video segmentation and 37 for single-image segmentation.

We are releasing our work under permissive open licences, including the SA-V dataset (CC by 4.0), the SAM 2 model checkpoints^11^1All the results presented in this paper are based on a new version of SAM 2 (improved over our initial release; denoted as "SAM 2.1" in [https://github.com/facebookresearch/sam2](https://github.com/facebookresearch/sam2)), which we will refer to as SAM 2 throughout for brevity., training code (Apache 2.0), and code for our interactive online demo (Apache 2.0).

## Related work

### Image segmentation

Segment Anything introduces a promptable image segmentation task where the goal is to output a valid segmentation mask given an input prompt such as a bounding box or a point that refers to the object of interest. SAM trained on the SA-1B dataset allows for zero-shot segmentation which enabled its adoption to a wide range of applications. Recent work has extended SAM, e.g., by introducing a High-Quality output token to train on fine-grained masks, or improve SAM's efficiency. More broadly, SAM is used in a wide range of applications, including medical imaging, remote sensing, motion segmentation, and camouflaged object detection.

### Interactive Video Object Segmentation (iVOS)

Interactive video object segmentation has emerged as a crucial task to efficiently obtain object segmentations in videos (masklets) with user guidance, often in the form of scribbles, clicks, or bounding boxes. A few early approaches deploy graph-based optimization to guide the segmentation annotation process. More recent approaches often adopt a modular design, converting user inputs into a mask representation on a single frame and then propagating it to other frames.

Click-based input is easier to collect for interactive video segmentation. Recent works have used a combination of SAM on images with video trackers based on masks or points. However, these approaches have limitations: the tracker may not work for all objects, SAM may not perform well on video frames, and there is no mechanism to interactively refine a model's mistakes, other than re-annotating using SAM in each frame and restarting the tracking from there.

Our work shares a similar goal to these works to segment objects across videos interactively, and we build a strong unified model that directly takes prompts for interactive video segmentation, along with a large and diverse dataset in pursuit of solving this goal.

### Video Object Segmentation (VOS)

The VOS task begins with an object mask as input in the first frame, which must be accurately tracked throughout the video. The task is referred to as "semi-supervised VOS" since the input mask can be seen as supervision signal of the object which is available only in the first frame. This task has drawn significant attention due to its relevance in applications, including video editing or robotics.

Early deep learning based approaches have often used online fine-tuning on the first video frame or on all frames to adapt the model to the target object. Faster inference has been achieved with offline-trained models, conditioned either only on the first frame, or also integrating the previous frame. This multi-conditioning has been extended to all frames with RNNs and transformers.

Semi-supervised VOS can be seen as a special case of our Promptable Visual Segmentation (PVS) task, with only a mask prompt in the first video frame. Notably, annotating the required high-quality object mask in the first frame in VOS is practically challenging and time-consuming for inference.

### Video segmentation datasets

Many datasets have been proposed to support the VOS task. Early VOS datasets, such as DAVIS, include high-quality annotations but their size limits deep-learning based approaches. YouTube-VOS is the first large-scale dataset for VOS. As algorithms became better and benchmark performance started to saturate, researchers have looked at increasing the difficulty of the VOS task by specifically focusing on occlusions, long videos, extreme transformations, object diversity or scene diversity.

We find that current video segmentation datasets lack sufficient coverage to achieve the capability of "segmenting anything in videos". Their annotations typically cover entire objects (not parts) and datasets are often centered around specific object classes, such as people, vehicles, and animals. In comparison to these datasets, our released SA-V dataset not only focuses on whole objects but also extensively covers object parts and contains over an order of magnitude more masks.

## Task: promptable visual segmentation

Our PVS task allows providing prompts to the model on any frame of a video. Prompts can be positive/negative clicks, boxes, or masks, either to define an object to segment or to refine a model-predicted one. To provide an interactive experience, upon receiving a prompt on a specific frame, the model should immediately respond with a valid segmentation mask of the object on this frame. After receiving initial prompts (either on the same frame or different frames), the model should propagate these prompts to obtain the masklet of the object across the entire video, localizing the segmentation mask of the target on every video frame. Additional prompts can be provided to the model on any frame to refine the segment throughout the video (example in Fig. 2). For details on the task, see §B.

SAM 2 (§4) is applied as a data collection tool to the PVS task for building our SA-V dataset (§5). We evaluate the model (§6) by simulating interactive video segmentation scenarios across multiple frames, in the conventional semi-supervised VOS setting where annotations are limited to the first frame, and for image segmentation on the SA benchmarks.

Figure 2: Interactive segmentation with SAM 2. Step 1 (selection): we prompt SAM 2 in frame 1 to obtain the segment of the target object (the tongue). Green/red dots indicate positive/negative prompts respectively. SAM 2 automatically propagates the segment to the following frames (blue arrows) to form a masklet. If SAM 2 loses the object (after frame 2), we can correct the masklet by providing an additional prompt in a new frame (red arrow). Step 2 (refinement): a single click in frame 3 is sufficient to recover the object and propagate it to obtain the correct masklet. A decoupled SAM + video tracker approach would require several clicks in frame 3 (as in frame 1) to correctly re-annotate the object as the segmentation is restarted from scratch. With SAM 2’s memory, a single click can recover the tongue.

## Model

SAM 2 (Fig. 3) can be seen as a generalization of SAM to the video (and image) domain, taking point, box, and mask prompts on individual frames to define the spatial extent of the object to be segmented spatio-temporally. Spatially, the model behaves similarly to SAM. A promptable and light-weight mask decoder takes an image embedding and prompts (if any) and outputs a segmentation mask for the frame. Prompts can be iteratively added on a frame in order to refine the masks.

The frame embedding used by the SAM 2 decoder is not directly from an image encoder and is instead conditioned on memories of past predictions and prompted frames. It is possible for prompted frames to also come "from the future" relative to the current frame. Memories of frames are created by the memory encoder based on the current prediction and placed in a memory bank for use in subsequent frames. The memory attention operation takes the per-frame embedding from the image encoder and conditions it on the memory bank, before the mask decoder ingests it to form a prediction.

We describe individual components and training below and provide more details in Appendix D.

### Image encoder

For real-time processing of arbitrarily long videos, we take a streaming approach, consuming video frames as they become available. The image encoder is only run once for the entire interaction and its role is to provide unconditioned tokens (feature embeddings) representing each frame. We use an MAE pre-trained Hiera image encoder, which is hierarchical, allowing us to use multiscale features during decoding.

### Memory attention

The role of memory attention is to condition the current frame features on the past frames features and predictions as well as on any new prompts. We stack $L$ transformer blocks, the first one taking the image encoding from the current frame as input. Each block performs self-attention, followed by cross-attention to memories of (prompted/unprompted) frames and object pointers (see below), stored in a memory bank (see below), followed by an MLP. We use vanilla attention operations for self- and cross-attention, allowing us to benefit from recent developments in efficient attention kernels.

### Prompt encoder and mask decoder

Our prompt encoder is identical to SAM's and can be prompted by clicks (positive or negative), boxes, or masks to define the extent of the object in a given frame. Sparse prompts are represented by positional encodings summed with learned embeddings for each prompt type, while masks are embedded using convolutions and summed with the frame embedding.

Our decoder design largely follows SAM. We stack "two-way" transformer blocks that update prompt and frame embeddings. As in SAM, for ambiguous prompts (i.e., a single click) where there may be multiple compatible target masks, we predict multiple masks. This design is important to ensure that the model outputs valid masks. In video, where ambiguity can extend across video frames, the model predicts multiple masks on each frame. If no follow-up prompts resolve the ambiguity, the model only propagates the mask with the highest predicted IoU for the current frame.

Unlike SAM where there is always a valid object to segment given a positive prompt, in the PVS task it is possible for no valid object to exist on some frames (e.g. due to occlusion). To support this new output mode, we add an additional head that predicts whether the object of interest is present on the current frame. Another novelty are skip connections from our hierarchical image encoder (bypassing the memory attention) to incorporate high-resolution embeddings for mask decoding (see §D).

Figure 3: The SAM 2 architecture. For a given frame, the segmentation prediction is conditioned on the current prompt and/or on previously observed memories. Videos are processed in a streaming fashion with frames being consumed one at a time by the image encoder, and cross-attended to memories of the target object from previous frames. The mask decoder, which optionally also takes input prompts, predicts the segmentation mask for that frame. Finally, a memory encoder transforms the prediction and image encoder embeddings (not shown in the figure) for use in future frames.

### Memory encoder

The memory encoder generates a memory by downsampling the output mask using a convolutional module and summing it element-wise with the unconditioned frame embedding from the image-encoder (not shown in Fig. 3), followed by light-weight convolutional layers to fuse the information.

### Memory bank

The memory bank retains information about past predictions for the target object in the video by maintaining a FIFO queue of memories of up to $N$ recent frames and stores information from prompts in a FIFO queue of up to $M$ prompted frames. For instance, in the VOS task where the initial mask is the only prompt, the memory bank consistently retains the first frame's memory along with memories of up to $N$ recent (unprompted) frames. Both sets of memories are stored as spatial feature maps.

In addition to the spatial memory, we store a list of object pointers as lightweight vectors for high-level semantic information of the object to segment, based on mask decoder output tokens of each frame. Our memory attention cross-attends to both spatial memory features and these object pointers.

We embed temporal position information into the memories of $N$ recent frames, allowing the model to represent short-term object motion, but not into those of prompted frames, because the training signal from prompted frames is sparser and it is more difficult to generalize to the inference setting where prompted frames may come from a very different temporal range than seen during training.

### Training

The model is trained jointly on image and video data. Similar to previous work, we simulate interactive prompting of the model. We sample sequences of 8 frames and randomly select up to 2 frames to prompt and probabilistically receive corrective clicks which are sampled using the ground-truth masklet and model predictions during training. The training task is to sequentially (and "interactively") predict the ground-truth masklet. Initial prompts to the model can be the ground-truth mask with probability $0.5$, a positive click sampled from the ground-truth mask with probability $0.25$, or a bounding box input with probability $0.25$. See §D for more details.

## Data

To develop the capability to "segment anything" in video, we built a data engine to collect a large and diverse video segmentation dataset. We employ an interactive model in the loop setup with human annotators. Similar to Kirillov et al., we do not impose semantic constraints on the annotated masklets, and focus on both whole objects (e.g., a person) and parts (e.g., a person's hat). Our data engine went through three phases, each categorized based on the level of model assistance provided to annotators. Next, we describe each data engine phase and our SA-V dataset.

### Data engine

### Phase 1: SAM per frame

The initial phase used the image-based interactive SAM to assist human annotation. Annotators are tasked with annotating the mask of a target object in every frame of the video at 6 frames per second (FPS) using SAM, and pixel-precise manual editing tools such as a "brush" and "eraser". There is no tracking model involved to assist with the temporal propagation of masks to other frames. As this is a per-frame method, and all frames require mask annotation from scratch, the process is slow, with an average annotation time of 37.8 seconds per frame in our experiment. However, this yields high-quality spatial annotations per frame. In this phase, we collected 16K masklets across 1.4K videos. We further use this approach to annotate our SA-V val and test sets to mitigate potential biases of SAM 2 during evaluation.

### Phase 2: SAM + SAM 2 Mask

The second phase added SAM 2 into the loop, where SAM 2 only accepted *masks* as prompts. We refer to this version as SAM 2 Mask. Annotators used SAM and other tools as in Phase 1 to generate spatial masks in the first frame, and then use SAM 2 Mask to temporally propagate the annotated mask to other frames to get the full spatio-temporal masklets. At any subsequent video frame, annotators can spatially modify the predictions made by SAM 2 Mask by annotating a mask from scratch with SAM, a "brush" and/or "eraser", and re-propagate with SAM 2 Mask, repeating this process until the masklet is correct. SAM 2 Mask was initially trained on the Phase 1 data and publicly available datasets. During Phase 2, we re-trained and updated SAM 2 Mask in the annotation loop twice using the collected data. In Phase 2, we collected 63.5K masklets. The annotation time went down to 7.4 s/frame, a $\sim$`<!-- -->`{=html}5.1x speed up over Phase 1.

Despite an improvement in annotation time, this approach requires annotating masks in intermediate frames from scratch without previous memory. We then advanced to develop the fully-featured SAM 2, capable of both interactive segmentation and mask propagation in a unified model.

### Phase 3: SAM 2

In the final phase, we utilize the fully-featured SAM 2, which accepts various types of prompts, including points and masks. SAM 2 benefits from memories of objects across the temporal dimension to generate mask predictions. This means annotators only need to provide occasional refinement clicks to SAM 2 to edit the predicted masklets in intermediate frames, as opposed to annotating from scratch with a spatial SAM which has no such memory context. During Phase 3, we re-trained and updated SAM 2 using the collected annotations five times. With SAM 2 in the loop, the annotation time per frame went down to 4.5 seconds, a $\sim$`<!-- -->`{=html}8.4x speed up over Phase 1. In Phase 3, we collected 197.0K masklets.

### Quality verification

To uphold a high standard for annotation, we introduce a verification step. A separate set of annotators are tasked with verifying the quality of each annotated masklet as "satisfactory" (correctly and consistently tracking the target object across all frames) or "unsatisfactory" (target object is well defined with a clear boundary but the masklet is not correct or consistent). Unsatisfactory masklets were sent back to the annotation pipeline for refinement. Any masklets tracking not well defined objects were rejected entirely.

### Auto masklet generation

Ensuring diversity in annotation is important to enable the anything capability of our model. As human annotators might typically focus more on salient objects, we augment the annotations with automatically generated masklets (referred to as "Auto"). This serves a dual purpose of increasing the coverage of annotations and helping identify model failure cases. To generate auto masklets, we prompt SAM 2 with a regular grid of points in the first frame and generate candidate masklets. These are then sent to the masklet verification step for filtering. Automatic masklets tagged as "satisfactory" are added to the SA-V dataset. Masklets identified as "unsatisfactory" (i.e., model failure cases) are sampled and presented to annotators to refine with SAM 2 in the loop (Phase 3 of the data engine). These automatic masklets cover large salient central objects but also objects of varying sizes and positions in the background.

Model in the Loop
Time per Frame
Clicks per Clicked Frame
Phase 1 Mask Alignment Score (IoU&gt;0.75)

SAM + SAM 2 Mask

Table 1: Evolution of data engine phases showing the average annotation time per frame, the average percent of edited frames per masklet, the number of manual clicks per clicked frame, and Mask Alignment to Phase 1 by mask size.

### Analysis

Table 1 shows a comparison of the annotation protocol in each data engine phase through a controlled experiment (details in §E.2.2). We compare the average annotation time per frame, the average percentage of manually edited frames per masklet, and the average number of clicks per clicked frame. For quality evaluation, we define the *Phase 1 Mask Alignment Score* as the percentage of masks whose IoU compared to the corresponding masks in Phase 1 exceeds 0.75. Phase 1 data is chosen as a reference as it has per-frame high quality manual annotations. Phase 3 with SAM 2 in the loop leads to increased efficiency and comparable quality: it is 8.4$\times$ faster than Phase 1, has the lowest edited frame percentage and clicks per frame, and results in better alignment.

Table 2: Segmentation accuracy (𝒥&amp;ℱ metric) improvement from adding data from each data engine phase. “VOS” is a set of video object segmentation datasets. Details are in §F.

In Table 2, we show the performance comparison of SAM 2 trained on the available data at the end of each phase keeping the number of iterations fixed, therefore measuring solely the impact of the additional data. We evaluate on our own SA-V val set and also on 9 zero-shot benchmarks (see §F.1 for details) using the standard $\mathcal{J}\&\mathcal{F}$ accuracy metric (the higher the better) when prompting with 3-clicks on the first frame. We note a consistent improvement after iteratively including the data from each phase, not only on the in-domain SA-V val set, but also on the 9 zero-shot benchmarks.

### SA-V dataset

The SA-V dataset collected with our data engine comprises 50.9K videos with 642.6K masklets. In Table 3 we compare the SA-V composition to common VOS datasets across the number of videos, masklets, and masks. Notably, the number of annotated masks is 53$\times$ (15$\times$ without auto) larger than any existing VOS dataset, providing a substantial resource for future work. We are releasing SA-V under a permissive license.

### Videos

We collected a new set of 50.9K videos captured by crowdworkers. Videos comprise 54% indoor and 46% outdoor scenes with an average duration of 14 seconds. Videos feature "in-the-wild" diverse environments, and cover various everyday scenarios.

Figure 4: Example videos from the SA-V dataset with masklets overlaid (manual and automatic). Each masklet has a unique color, and each row represents frames from one video, with 1 second between them.

### Masklets

The annotations comprise 190.9K manual masklet annotations and 451.7K automatic masklets collected using our data engine. Example videos with masklets overlaid (manual and automatic) are shown in Fig. 4. SA-V has 53$\times$ (15$\times$ without auto annotations) more masks than the largest VOS dataset. The disappearance rate in SA-V Manual (the percentage of annotated masklets that disappear in at least one frame and then re-appear) is 42.5$\%$, competitive among existing datasets.

### SA-V training, validation and test splits

We split SA-V based on the video authors (and their geographic locations) to ensure minimal overlap of similar objects. To create SA-V val and SA-V test sets, we focus on challenging scenarios in selecting videos, and ask annotators to identify *challenging targets* that are fast-moving, have complex occlusions by other objects as well as disappearance/re-appearance patterns. These targets were annotated at 6 FPS using the data engine Phase 1 setup in §5.1. There are 293 masklets and 155 videos in the SA-V val split, and 278 masklets and 150 videos in the SA-V test split.

### Internal dataset

We also used internally available licensed video data to further augment our training set. Our internal dataset is comprised of 62.9K videos and 69.6K masklets annotated in Phase 2 and Phase 3 (see §5.1) for training, and 96 videos and 189 masklets annotated using Phase 1 for testing (Internal-test).

See Appendix E for more details on the data engine and SA-V dataset, including a fairness evaluation.

#Videos
#Masklets
#Masks
#Frames

SA-V Manual+Auto

Table 3: Comparison of our datasets with open source VOS datasets in terms of number of videos, duration, number of masklets, masks, frames, and disappearance rate. SA-V Manual contains only manually annotated labels. SA-V Manual+Auto combines manually annotated labels with automatically generated masklets.

## Zero-shot experiments

Here, we compare SAM 2 with previous work on zero-shot video and image tasks. We report the standard $\mathcal{J}\&\mathcal{F}$ metric for video and mIoU metric for image tasks. Unless otherwise mentioned, the results in this section follow our default setup using Hiera-B+ image encoder with a resolution of 1024 and trained on the full combination of datasets, i.e., SAM 2 (Hiera-B+) in Table 6 (see also §D.2 for details).

### Promptable video segmentation

(a) offline average 𝒥&amp;ℱ across datasets (3-click)
(b) online average 𝒥&amp;ℱ across datasets (3-click)

Figure 5: Zero-shot accuracy over 9 datasets in interactive offline and online evaluation settings.

We first evaluate promptable video segmentation, which involves simulating an interactive setting that resembles the user experience. We have two settings, offline evaluation, where multiple passes are made through a video to select frames to interact with based on the largest model error, and online evaluation, where the frames are annotated in a single forward pass through the video. These evaluations are conducted on 9 densely annotated zero-shot video datasets using $N_{click} = 3$ clicks per frame (see §F.1 for details).

We create two strong baselines, SAM+XMem++ and SAM+Cutie, based on two state-of-the-art models for video object segmentation, XMem++ and Cutie.

We use XMem++ to generate a video segmentation based on mask inputs on one or multiple frames. SAM is used to provide an initial mask or to refine an output (by feeding the current segmentation as a mask prompt to SAM). For the SAM+Cutie baseline, we modify Cutie to allow taking mask inputs on multiple frames.

In Fig. 5, we report the average $\mathcal{J}\&\mathcal{F}$ accuracy over $N_{frame} = {1,\ldots,8}$ interacted frames. SAM 2 outperforms SAM+XMem++ and SAM+Cutie for both offline and online evaluation settings. Across all 9 datasets (see per-dataset results in §F.1), SAM 2 dominates both methods, generating high-quality video segmentation from a few clicks while allowing continued refinement with prompts. Overall, SAM 2 can generate better segmentation accuracy, with $>$`<!-- -->`{=html}3$\times$ fewer interactions.

### Semi-supervised video object segmentation

Table 4: Zero-shot accuracy across 17 video datasets using different prompts. We report average accuracy for each type of prompt (1, 3 or 5 clicks, bounding boxes, or ground-truth masks) in the first video frame (‡: this case directly uses masks as inputs into XMem++ or Cutie without SAM).

We evaluate the semi-supervised video object segmentation (VOS) setting with click, box, or mask prompts only on the first frame of the video. When using click prompts, we interactively sample either 1, 3 or 5 clicks on the first video frame.

Similar to the interactive setting in §6.1, we compare to XMem++ and Cutie, using SAM for click and box prompts, and in their default setting when using mask prompts. We report the standard $\mathcal{J}\&\mathcal{F}$ accuracy, except for on VOST, where we report the $\mathcal{J}$ metric following its protocol. The results are in Table 4. SAM 2 outperforms both methods on the 17 datasets. The results underline that SAM 2 also excels at the conventional, non-interactive VOS task with mask input, for which these other works are specifically designed. Details are in §F.1.3.

### Image segmentation

We evaluate SAM 2 on the Segment Anything task across 37 zero-shot datasets, including 23 datasets previously used by SAM for evaluation. 1-click and 5-click mIoUs are reported in Table 5 and we show the average mIoU by dataset domain and model speed in frames per second (FPS) on a single A100 GPU.

The first column (SA-23 All) shows accuracy on the 23 datasets from SAM. SAM 2 achieves higher accuracy (58.9 mIoU with 1 click) than SAM (58.1 mIoU with 1 click), without using any extra data and while being 6$\times$ faster. This can be mainly attributed to the smaller but more effective Hiera image encoder in SAM 2.

The bottom row shows how training on our SA-1B and video data mix can further improve accuracy to 61.4% on average on the 23 datasets. We also see exceptional gains on the video benchmarks from SA-23 (video datasets are evaluated as images, identical to Kirillov et al. ), and the 14 new video datasets we added. More detailed results including a breakdown by dataset are in §F.3.

Table 5: Zero-shot accuracy on the Segment Anything (SA) task across 37 datasets. The table shows the average 1- and 5-click mIoU of SAM 2 compared to SAM by domains (image/video). We report the average metrics on the 23 datasets used by SAM (SA-23) and the average across 14 additional zero-shot video datasets (as detailed in §F.3).

## Comparison to state-of-the-art in semi-supervised VOS

Table 6: VOS comparison to prior work. SAM 2 performs well in accuracy (𝒥&amp;ℱ, 𝒢) for video segmentation based on first-frame ground-truth mask prompts. SAM 2 performs significantly better on SA-V val/test.

Our primary focus is on the general, interactive PVS task, but we also address the specific semi-supervised VOS setting (where the prompt is a ground-truth mask on the first frame), as it is a historically common protocol. We evaluate two versions of SAM 2 with varying image encoder sizes (Hiera-B+/-L) with different speed-vs-accuracy tradeoffs. We measure frames per second (FPS) on a single A100 GPU using a batch-size of one. SAM 2 based on Hiera-B+ and Hiera-L runs at real-time speeds of 43.8 and 30.2 FPS, respectively.

We present a comparison with existing state-of-the-art in Table 6, reporting accuracy using standard protocols. SAM 2 shows significant improvement over the best existing methods. We observe that using a larger image encoder brings significant accuracy gains across the board.

We also evaluate existing work on the SA-V val and test sets which measure performance for open-world segments of "any" object class. When comparing on this benchmark, we see that most previous methods peak at around the same accuracy. The best performance on SA-V val and SA-V test for prior work is significantly lower demonstrating the gap to a "segment anything in videos" capability. Finally, we see that SAM 2 also brings notable gains in long-term video object segmentation as observed in the LVOS benchmark result. For data and model ablations, see §A.

## Conclusion

We present a natural evolution of Segment Anything into the video domain, based on three key aspects: (i) extending the promptable segmentation task to video, (ii) equipping the SAM architecture to use memory when applied to video, and (iii) the diverse SA-V dataset for training and benchmarking video segmentation. We believe SAM 2 marks a significant advancement in visual perception, positioning our contributions as milestones that will propel further research and applications.
