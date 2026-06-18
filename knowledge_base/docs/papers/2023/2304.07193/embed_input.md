DINOv2: Learning Robust Visual Features without Supervision

Topics include Robustness, Foundation models, Computer vision, Self-supervised learning, Datasets, Benchmarks, Learning, DINOv2.

The recent breakthroughs in natural language processing for model pretraining on large quantities of data have opened the way for similar foundation models in computer vision. These models could greatly simplify the use of images in any system by producing all-purpose visual features, i.e., features that work across image distributions and tasks without finetuning. This work shows that existing pretraining methods, especially self-supervised methods, can produce such features if trained on enough curated data from diverse sources. We revisit existing approaches and combine different techniques to scale our pretraining in terms of data and model size. Most of the technical contributions aim at accelerating and stabilizing the training at scale. In terms of data, we propose an automatic pipeline to build a dedicated, diverse, and curated image dataset instead of uncurated data, as typically done in the self-supervised literature. In terms of models, we train a ViT model with 1B parameters and distill it into a series of smaller models that surpass the best available all-purpose features, OpenCLIP on most of the benchmarks at image and pixel levels.

## Introduction

Learning task-agnostic pretrained representations have become the standard in Natural Language Processing (NLP) (Radford et al. Raffel et al. Chowdhery et al. Hoffmann et al. Touvron et al., ). One can use these features "as they are", i.e., without fine-tuning, and achieve performances on downstream tasks that are significantly better than those produced by task-specific models. This success has been fueled by pretraining on large quantities of raw text using pretext objectives, such as language modeling or word vectors, that require no supervision.

Following this paradigm shift in NLP, we expect similar "foundation" models to appear in computer vision. These models should generate visual features that work out of the box on any task, both at the image level, e.g., image classification, and pixel level, e.g., segmentation. Most promising efforts towards these foundation models focus on text-guided pretraining, i.e., using a form of textual supervision to guide the training of the features (Joulin et al. Mahajan et al. Radford et al., )....

## Future work and Discussion

In this work, we present DINOv2, a new series of image encoders pretrained on large curated data with no supervision. This is the first SSL work on image data that leads to visual features that close the performance gap with (weakly) supervised alternatives across a wide range of benchmarks and without the need for finetuning....

We measure the impact of changing the resolution during the pretraining on the performance of image and patch-level features. We consider models trained from scratch using a fixed resolution of either $224 \times 224$ or $416 \times 416$, and a model trained from scratch at $224 \times 224$, then resumed for 10k more iterations at $416 \times 416$. High-resolution training is compute-intensive, so we conduct this ablation on a small setup: a ViT-L/16 trained on ImageNet1k. In Fig., we report the performance of a linear probe on ImageNet-1k and ADE-20k, evaluated at various resolutions....

Minimizing our objective with the AdamW optimizer requires 4 model replicas in float32 precision -- student, teacher, optimizer first moments, optimizer second moments. This sums to $16{GB}$ of memory for a billion-parameter model such as our ViT-g....
