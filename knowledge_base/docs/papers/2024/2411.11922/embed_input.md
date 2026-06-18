SAMURAI: Adapting Segment Anything Model for Zero-Shot Visual Tracking with Motion-Aware Memory

Topics include Visual tracking, Video segmentation, Segment anything, Zero-shot tracking, Motion-aware memory, Object tracking, Real-time vision, Foundation models.

Adapts SAM 2 for zero-shot visual object tracking by adding motion-aware memory selection that filters the memories used to condition future masks. This directly addresses error accumulation in crowded or fast-motion videos and demonstrates that promptable segmentation models can be made into competitive trackers without task-specific fine-tuning.

The Segment Anything Model 2 (SAM 2) has demonstrated strong performance in object segmentation tasks but faces challenges in visual object tracking, particularly when managing crowded scenes with fast-moving or self-occluding objects. Furthermore, the fixed-window memory approach in the original model does not consider the quality of memories selected to condition the image features for the next frame, leading to error propagation in videos. This paper introduces SAMURAI, an enhanced adaptation of SAM 2 specifically designed for visual object tracking. By incorporating temporal motion cues with the proposed motion-aware memory selection mechanism, SAMURAI effectively predicts object motion and refines mask selection, achieving robust, accurate tracking without the need for retraining or fine-tuning. SAMURAI operates in real-time and demonstrates strong zero-shot performance across diverse benchmark datasets, showcasing its ability to generalize without fine-tuning. In evaluations, SAMURAI achieves significant improvements in success rate and precision over existing trackers, with a 7.1% AUC gain on LaSOT_ext and a 3.5% AO gain on GOT-10k....

## Introduction

Segment Anything Model (SAM) \[\] has demonstrated impressive performance in segmentation tasks. Recently, SAM 2 \[\] incorporates a streaming memory architecture, which enables it to process video frames sequentially while maintaining context over long sequences. While SAM 2 has shown remarkable capabilities in Video Object Segmentation tasks, generating precise pixel-level masks for objects throughout a video sequence, it still faces challenges in Visual Object Tracking scenarios.

The primary concern in VOT is maintaining consistent object identity and location despite occlusions, appearance changes, and the presence of similar objects. However, SAM 2 often neglects motion cues when predicting masks for subsequent frames, leading to inaccuracies in scenarios with rapid object movement or complex interactions. This limitation is particularly evident in crowded scenes, where SAM 2 tends to prioritize appearance similarity over spatial and temporal consistency, resulting in tracking errors....

## Conclusion

We present SAMURAI, a visual object tracking framework built on top of the segment-anything model by introducing the motion-based score for better mask prediction and memory selection to deal with self-occlusion and abrupt motion in crowded scenes. The proposed modules show consistent improvement on all variations of the SAM models across multiple VOT benchmarks on all metrics. This method does not require re-training nor fine-tuning while demonstrating robust performance on multiple VOT benchmarks with the capability of real-time online inferences.

where $N_{max}$ is the maximum number of frames to look back. The motion-aware memory bank $B_{t}$ is subsequently passed through the memory attention layer and then directed to mask decoder $D_{mask}$ to perform mask decoding at current timestamp. Note that we follow the $N_{mem} = 7$ as the SAM 2 is trained under these specific memory bank settings.

which takes the past $N_{mem}$ frames' output $m$ as the components of the memory bank.

### OTB100

To address these limitations, we propose incorporating motion information into SAM 2's prediction process. By leveraging the history of object trajectories, we can enhance the model's ability to differentiate between visually similar objects and maintain tracking accuracy in the presence of occlusions....
