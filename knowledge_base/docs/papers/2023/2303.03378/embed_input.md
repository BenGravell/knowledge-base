PaLM-E: An Embodied Multimodal Language Model

Topics include Robotics, State estimation, Large language models, Planning, PaLM-E, Language models.

Large language models excel at a wide range of complex tasks. However, enabling general inference in the real world, e.g., for robotics problems, raises the challenge of grounding. We propose embodied language models to directly incorporate real-world continuous sensor modalities into language models and thereby establish the link between words and percepts. Input to our embodied language model are multi-modal sentences that interleave visual, continuous state estimation, and textual input encodings. We train these encodings end-to-end, in conjunction with a pre-trained large language model, for multiple embodied tasks including sequential robotic manipulation planning, visual question answering, and captioning. Our evaluations show that PaLM-E, a single large embodied multimodal model, can address a variety of embodied reasoning tasks, from a variety of observation modalities, on multiple embodiments, and further, exhibits positive transfer: the model benefits from diverse joint training across internet-scale language, vision, and visual-language domains.

## Introduction

Large language models (LLMs) demonstrate strong reasoning capabilities across various domains, including dialogue Glaese et al.; Thoppilan et al., step-by-step reasoning Wei et al.; Kojima et al., math problem solving Lewkowycz et al.; Polu et al., and code writing Chen et al..

In this paper we propose embodied language models, which directly incorporate continuous inputs from sensor modalities of an embodied agent and thereby enable the language model *itself* to make more grounded inferences for sequential decision making in the real world. Inputs such as images and state estimates are embedded into the same latent embedding as language tokens and processed by the self-attention layers of a Transformer-based LLM in the same way as text. We start from a pre-trained LLM in which we inject the continuous inputs through an encoder.

To investigate the approach's breadth, we evaluate on three robotic manipulation domains (two of which are closed-loop in the real-world), standard visual-language tasks such as VQA and image captioning, as well as language tasks. Our results indicate that multi-task training improves performance compared to training models on individual tasks. We show that this *transfer* across tasks can lead to high data-efficiency for robotics tasks, e.g. significantly increasing learning success from handfuls of training examples, and even demonstrating one-shot or zero-shot generalization to novel combinations of objects or unseen objects.

## Conclusion

We proposed to build an embodied language model by injecting multi-modal information such as images into the embedding space of a pre-trained LLM. Experiments showed that off-the-shelf state-of-the-art vision-language models trained on general VQA and captioning tasks are not sufficient for embodied reasoning tasks, as well as limitations of a recent proposal for grounding language models through affordances. To overcome these limitations, we proposed PaLM-E, a single model that is able to control different robots in simulation and in the real world, while at the same time being quantitatively competent at general VQA and captioning tasks.
