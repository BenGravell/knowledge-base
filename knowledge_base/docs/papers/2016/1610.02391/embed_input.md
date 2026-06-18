Grad-CAM: Visual Explanations from Deep Networks via Gradient-based Localization

Topics include Reinforcement learning, Robustness, Convolutional networks, Attention mechanisms, Classification, Datasets, Generalization, Learning, Grad-CAM, Visual question answering, Question answering.

We propose a technique for producing "visual explanations" for decisions from a large class of CNN-based models, making them more transparent. Our approach - Gradient-weighted Class Activation Mapping (Grad-CAM), uses the gradients of any target concept, flowing into the final convolutional layer to produce a coarse localization map highlighting important regions in the image for predicting the concept. Grad-CAM is applicable to a wide variety of CNN model-families: CNNs with fully-connected layers, CNNs used for structured outputs, CNNs used in tasks with multimodal inputs or reinforcement learning, without any architectural changes or re-training. We combine Grad-CAM with fine-grained visualizations to create a high-resolution class-discriminative visualization and apply it to off-the-shelf image classification, captioning, and visual question answering (VQA) models, including ResNet-based architectures....

## Introduction

Deep neural models based on Convolutional Neural Networks (CNNs) have enabled unprecedented breakthroughs in a variety of computer vision tasks, from image classification krizhevsky_nips12; he_cvpr15, object detection girshick2014rcnn, semantic segmentation long2015fcn to image captioning vinyals_cvpr15; chen2015microsoft; fang2015captions; johnson_cvpr16, visual question answering antol2015vqa; gao2015you; malinowski_iccv15; ren_nips15 and more recently, visual dialog visdial; guesswhat; visdial_rl and embodied question answering embodiedqa; gordon2017iqa....

*Interpretability matters.* In order to build trust in intelligent systems and move towards their meaningful integration into our everyday lives, it is clear that we must build 'transparent' models that have the ability to explain *why they predict what they predict*. Broadly speaking, this transparency and ability to explain is useful at three different stages of Artificial Intelligence (AI) evolution. First, when AI is significantly weaker than humans and not yet reliably deployable (*e.g*....

## Conclusion

In this work, we proposed a novel class-discriminative localization technique -- Gradient-weighted Class Activation Mapping (Grad-CAM) -- for making *any* CNN-based model more transparent by producing visual explanations. Further, we combined Grad-CAM localizations with existing high-resolution visualization techniques to obtain the best of both worlds -- high-resolution and class-discriminative Guided Grad-CAM visualizations. Our visualizations outperform existing approaches on both axes -- interpretability and faithfulness to original model....

### Weakly-supervised Segmentation

CAM computes the final scores by, {ceqn}

Faithfulness of a visualization to a model is its ability to accurately explain the function learned by the model. Naturally, there exists a trade-off between the interpretability and faithfulness of a visualization -- a more faithful visualization is typically less interpretable and vice versa. In fact, one could argue that a fully faithful explanation is the entire description of the model, which in the case of deep models is not interpretable/easy to visualize. We have verified in previous sections that our visualizations are reasonably interpretable. We now evaluate how faithful they are to the underlying model....
