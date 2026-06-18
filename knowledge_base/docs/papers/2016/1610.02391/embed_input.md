Grad-CAM: Visual Explanations from Deep Networks via Gradient-based Localization

Topics include Reinforcement learning, Robustness, Convolutional networks, Attention mechanisms, Classification, Datasets, Generalization, Learning, Grad-CAM, Visual question answering, Question answering.

We propose a technique for producing "visual explanations" for decisions from a large class of CNN-based models, making them more transparent. Our approach - Gradient-weighted Class Activation Mapping (Grad-CAM), uses the gradients of any target concept, flowing into the final convolutional layer to produce a coarse localization map highlighting important regions in the image for predicting the concept. Grad-CAM is applicable to a wide variety of CNN model-families: CNNs with fully-connected layers, CNNs used for structured outputs, CNNs used in tasks with multimodal inputs or reinforcement learning, without any architectural changes or re-training. We combine Grad-CAM with fine-grained visualizations to create a high-resolution class-discriminative visualization and apply it to off-the-shelf image classification, captioning, and visual question answering (VQA) models, including ResNet-based architectures.

## Introduction

Deep neural models based on Convolutional Neural Networks (CNNs) have enabled unprecedented breakthroughs in a variety of computer vision tasks, from image classification krizhevsky_nips12; he_cvpr15, object detection girshick2014rcnn, semantic segmentation long2015fcn to image captioning vinyals_cvpr15; chen2015microsoft; fang2015captions; johnson_cvpr16, visual question answering antol2015vqa; gao2015you; malinowski_iccv15; ren_nips15 and more recently, visual dialog visdial; guesswhat; visdial_rl and embodied question answering embodiedqa; gordon2017iqa.

In order to combine the best of both worlds, we show that it is possible to fuse existing pixel-space gradient visualizations with Grad-CAM to create Guided Grad-CAM visualizations that are both high-resolution and class-discriminative. As a result, important regions of the image which correspond to any decision of interest are visualized in high-resolution detail even if the image contains evidence for multiple possible concepts, as shown in Figures 1d and 1j.

\(1\) We introduce Grad-CAM, a class-discriminative localization technique that generates visual explanations for *any* CNN-based network without requiring architectural changes or re-training. We evaluate Grad-CAM for localization (Sec. 4.1), and faithfulness to model (Sec. 5.3), where it outperforms baselines.

\(3\) We show a proof-of-concept of how interpretable Grad-CAM visualizations help in diagnosing failure modes by uncovering biases in datasets. This is important not just for generalization, but also for fair and bias-free outcomes as more and more decisions are made by algorithms in society.

\(4\) We present Grad-CAM visualizations for ResNets he_cvpr15 applied to image classification and VQA (Sec. 8.2).

## Conclusion

In this work, we proposed a novel class-discriminative localization technique -- Gradient-weighted Class Activation Mapping (Grad-CAM) -- for making *any* CNN-based model more transparent by producing visual explanations. Further, we combined Grad-CAM localizations with existing high-resolution visualization techniques to obtain the best of both worlds -- high-resolution and class-discriminative Guided Grad-CAM visualizations. Our visualizations outperform existing approaches on both axes -- interpretability and faithfulness to original model.
