Grounding DINO: Marrying DINO with Grounded Pre-Training for Open-Set Object Detection

Topics include Object detection, Open-set detection, Vision-language models, Grounded pretraining, DINO, Referring expression comprehension, Cross-modal fusion, Zero-shot transfer.

Combines the DINO detector with language-conditioned grounded pretraining to support open-set detection from category names or referring expressions. Its feature enhancer, language-guided query selection, and cross-modality decoder made Grounding DINO a widely used bridge between object detection and promptable vision-language grounding.

In this paper, we present an open-set object detector, called Grounding DINO, by marrying Transformer-based detector DINO with grounded pre-training, which can detect arbitrary objects with human inputs such as category names or referring expressions. The key solution of open-set object detection is introducing language to a closed-set detector for open-set concept generalization. To effectively fuse language and vision modalities, we conceptually divide a closed-set detector into three phases and propose a tight fusion solution, which includes a feature enhancer, a language-guided query selection, and a cross-modality decoder for cross-modality fusion. While previous works mainly evaluate open-set object detection on novel categories, we propose to also perform evaluations on referring expression comprehension for objects specified with attributes. Grounding DINO performs remarkably well on all three settings, including benchmarks on COCO, LVIS, ODinW, and RefCOCO/+/g. Grounding DINO achieves a 52.5 AP on the COCO detection zero-shot transfer benchmark, i.e., without any training data from COCO. It sets a new record on the ODinW zero-shot benchmark with a mean 26.1 AP....

## Introduction

A key indicator of an Artificial General Intelligence (AGI) system's capability is its proficiency in handling open-world scenarios. In this paper, we aim to develop a strong system to detect arbitrary objects specified by human language inputs, a task commonly referred to as open-set object detection^22^2We view the terms open-set object detection, open-world object detection, and open-vocabulary object detection the same task in this paper. To avoid confusion, we always use open-set object detection in our paper.. The task has wide applications for its great potential as a generic object detector....

In pursuit of this goal, we design the strong open-set object detector Grounding DINO by following the two principles: tight modality fusion based on DINO \[\] and large-scale grounded pre-train for concept generalization.

Limitations: Despite the great performance on open-set object detection settings, Grounding DINO cannot be used for segmentation tasks like GLIPv2. Our training data is less than the largest GLIP model, which may limit our final performance. Moreover, we find that our model will produce false positive results in some cases, which may need more techniques or data to reduce the hallucination.

Social Impacts: The use of deep learning models, such as this one, exposes them to vulnerabilities through adversarial attacks. Additionally, the accuracy and correctness of the model's outputs cannot be guaranteed. There is also the risk that the open-set detection capabilities of the model could be exploited for unlawful purposes.

### Implementation Details

Grounding DINO aims to detect objects from an image specified by an input text. To effectively leverage the input text to guide object detection, we design a language-guided query selection module to select features that are more relevant to the input text as decoder queries.

The other phenomenon is that Grounding DINO has larger gains with more data than GLIP. For example, Grounding DINO introduces $+ 1.8$ AP gains with the caption data Cap4M, whereas GLIP has only $+ 1.1$ AP. We believe that Grounding DINO has better scalability compared with GLIP. A larger-scale training will be left as our future work.

Tight modality fusion based on DINO. The key to open-set detection is introducing language for unseen object generalization....
