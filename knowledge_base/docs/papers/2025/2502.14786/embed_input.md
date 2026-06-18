SigLIP 2: Multilingual Vision-Language Encoders with Improved Semantic Understanding, Localization, and Dense Features

We introduce SigLIP 2, a family of new multilingual vision-language encoders that build on the success of the original SigLIP. In this second iteration, we extend the original image-text training objective with several prior, independently developed techniques into a unified recipe - this includes captioning-based pretraining, self-supervised losses (self-distillation, masked prediction) and online data curation. With these changes, SigLIP 2 models outperform their SigLIP counterparts at all model scales in core capabilities, including zero-shot classification, image-text retrieval, and transfer performance when extracting visual representations for Vision-Language Models (VLMs). Furthermore, the new training recipe leads to significant improvements on localization and dense prediction tasks. We also train variants which support multiple resolutions and preserve the input's native aspect ratio. Finally, we train on a more diverse data-mixture that includes de-biasing techniques, leading to much better multilingual understanding and improved fairness.

## Introduction

Contrastive image-text embedding models trained on billion-scale datasets, as pioneered by CLIP and ALIGN, have become the mainstream approach for high-level, semantic understanding of visual data. These models enable fine-grained, zero-shot classification rivaling the quality of supervised methods and enable efficient text-to-image and image-to-text retrieval. Furthermore, they lead to excellent vision-language understanding capabilities when combined with Large Language Models (LLMs) to build Vision-Language Models (VLMs).

Developing on the success of CLIP, several improvements have been proposed such as re-captioning images, adding image-only self-supervised losses, and training with a small decoder for auxiliary tasks such as captioning and localization. At the same time, several groups have released model checkpoints for the open-source community. However, these releases do not include the full breadth of latest improvements into a single model, as they all relatively closely follow CLIP's original approach.

In

Dense features: We incorporate self-supervised losses as well as a decoder-based loss, which result in better dense features (e.g. for segmentation and depth estimation) and improve localization tasks (such as referring expression comprehension).

Native aspect ratio and variable resolution: SigLIP 2 also includes a NaFlex variant, which supports multiple resolutions and preserves the native image aspect ratio. These models have the potential to improve aspect sensitive applications such as document understanding.

## Conclusion

In this work, we introduced SigLIP 2, a family of open-weight multilingual vision-language encoders that builds on the success of SigLIP. By incorporating a combination of techniques such as decoder-based pretraining, self-supervised losses, and active data curation, SigLIP 2 achieves significant improvements in zero-shot classification, transfer performance as a vision encoder in VLMs, and in localization and dense prediction tasks. Furthermore, thanks to training on multilingual data and applying de-biasing filters, SigLIP 2 attains more balanced quality across culturally diverse data.
