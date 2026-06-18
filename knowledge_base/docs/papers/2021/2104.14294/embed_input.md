Emerging Properties in Self-Supervised Vision Transformers

Topics include Convolutional networks, Transformers, Semantic segmentation, Self-supervised learning, Supervised learning, Classifiers, Learning, DINO.

In this paper, we question if self-supervised learning provides new properties to Vision Transformer (ViT) that stand out compared to convolutional networks (convnets). Beyond the fact that adapting self-supervised methods to this architecture works particularly well, we make the following observations: first, self-supervised ViT features contain explicit information about the semantic segmentation of an image, which does not emerge as clearly with supervised ViTs, nor with convnets. Second, these features are also excellent k-NN classifiers, reaching 78.3% top-1 on ImageNet with a small ViT. Our study also underlines the importance of momentum encoder, multi-crop training, and the use of small patches with ViTs. We implement our findings into a simple self-supervised method, called DINO, which we interpret as a form of self-distillation with no labels. We show the synergy between DINO and ViTs by achieving 80.1% top-1 on ImageNet in linear evaluation with ViT-Base.

## Introduction

Transformers have recently emerged as an alternative to convolutional neural networks (convnets) for visual recognition. Their adoption has been coupled with a training strategy inspired by natural language processing (NLP), that is, pretraining on large quantities of data and finetuning on the target dataset. The resulting Vision Transformers (ViT) are competitive with convnets but, they have not yet delivered clear benefits over them: they are computationally more demanding, require more training data, and their features do not exhibit unique properties.

In this paper, we question whether the muted success of Transformers in vision can be explained by the use of supervision in their pretraining. Our motivation is that one of the main ingredients for the success of Transformers in NLP was the use of self-supervised pretraining, in the form of close procedure in BERT or language modeling in GPT. These self-supervised pretraining objectives use the words in a sentence to create pretext tasks that provide a richer learning signal than the supervised objective of predicting a single label per sentence.

While the self-supervised pretext tasks used in NLP are text specific, many existing self-supervised methods have shown their potential on images with convnets. They typically share a similar structure but with different components designed to avoid trivial solutions (collapse) or to improve performance. In this work, inspired from these methods, we study the impact of self-supervised pretraining on ViT features.

Self-supervised ViT features explicitly contain the scene layout and, in particular, object boundaries, as shown in Figure 1. This information is directly accessible in the self-attention modules of the last block.

## Conclusion

In this work, we have shown the potential of self-supervised pretraining a standard ViT model, achieving performance that are comparable with the best convnets specifically designed for this setting. We have also seen emerged two properties that can be leveraged in future applications: the quality of the features in $k$-NN classification has a potential for image retrieval where ViT are already showing promising results. The presence of information about the scene layout in the features can also benefit weakly supervised image segmentation.
