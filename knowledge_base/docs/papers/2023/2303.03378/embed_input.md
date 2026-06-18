PaLM-E: An Embodied Multimodal Language Model

Topics include Robotics, State estimation, Large language models, Planning, PaLM-E, Language models.

Large language models excel at a wide range of complex tasks. However, enabling general inference in the real world, e.g., for robotics problems, raises the challenge of grounding. We propose embodied language models to directly incorporate real-world continuous sensor modalities into language models and thereby establish the link between words and percepts. Input to our embodied language model are multi-modal sentences that interleave visual, continuous state estimation, and textual input encodings. We train these encodings end-to-end, in conjunction with a pre-trained large language model, for multiple embodied tasks including sequential robotic manipulation planning, visual question answering, and captioning. Our evaluations show that PaLM-E, a single large embodied multimodal model, can address a variety of embodied reasoning tasks, from a variety of observation modalities, on multiple embodiments, and further, exhibits positive transfer: the model benefits from diverse joint training across internet-scale language, vision, and visual-language domains....

## Introduction

Figure 2: PaLM-E-562B can do zero-shot multimodal chain-of-thought reasoning, can tell visually-conditioned jokes given an image, and demonstrates an array of robot-relevant multimodal-informed capabilities including perception, visually-grounded dialogue, and planning. PaLM-E also generalizes, zero-shot, to multi-image prompts despite only being trained on single-image prompts. PaLM-E can also perform math given an image with textually-interleaved handwritten numbers. In addition, the model can perform, zero-shot, question and answering on temporally-annotated egocentric vision, similar to what was shown in Zeng et al....

Large language models (LLMs) demonstrate strong reasoning capabilities across various domains, including dialogue Glaese et al.; Thoppilan et al., step-by-step reasoning Wei et al.; Kojima et al., math problem solving Lewkowycz et al.; Polu et al., and code writing Chen et al.. However, a limitation of such models for inference in the real world is the issue of grounding: while training LLMs on massive textual data may lead to representations that relate to our physical world, *connecting* those representations *to* real-world visual and physical sensor modalities is essential to solving a wider range of *grounded* real-world problems in...

## Conclusion

We proposed to build an embodied language model by injecting multi-modal information such as images into the embedding space of a pre-trained LLM. Experiments showed that off-the-shelf state-of-the-art vision-language models trained on general VQA and captioning tasks are not sufficient for embodied reasoning tasks, as well as limitations of a recent proposal for grounding language models through affordances....

### Robot Environments / Tasks

Vision Transformer (ViT). ViT ${\overset{\sim}{\phi}}_{\text{ViT}}$ Dosovitskiy et al. is a transformer architecture mapping an image $I$ into a number of token embeddings ${\overset{\sim}{x}}_{1:m} = {{\overset{\sim}{\phi}}_{\text{ViT}}{(I)}} \in {\mathbb{R}}^{m \times \overset{\sim}{k}}$. We consider several variants, including the 4 billion parameter model from Chen et al., which we refer to as ViT-4B, and a similar 22 billion parameter model, ViT-22B Dehghani et al., both of which have been pre-trained on image classification. We further investigate the ViT token learner architecture (ViT + TL) Ryoo et al....
