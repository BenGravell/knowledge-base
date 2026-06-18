PaliGemma: A Versatile 3B VLM for Transfer

Topics include Language models, Vision-language models, Benchmarks, PaliGemma.

PaliGemma is an open Vision-Language Model (VLM) that is based on the SigLIP-So400m vision encoder and the Gemma-2B language model. It is trained to be a versatile and broadly knowledgeable base model that is effective to transfer. It achieves strong performance on a wide variety of open-world tasks. We evaluate PaliGemma on almost 40 diverse tasks including standard VLM benchmarks, but also more specialized tasks such as remote-sensing and segmentation.

## Introduction

PaliGemma is an open model, continuing the line of PaLI vision-language models in a combination with the Gemma family of language models.

PaLI is a series of state-of-the-art vision-language models, starting with the first PaLI showing promising scaling results up to 17 B, using classification pretrained ViT and mT5 language model. PaLI-X and PaLM-E then pushed this further, combining ViT-22 B and a 32 B UL2 language model or the 540 B PaLM language model, respectively, and getting further increased performance on vision-language tasks, albeit saturating performance on standard image classification and retrieval tasks. Finally, PaLI-3 demonstrates that through better pretraining with SigLIP and more careful multimodal data curation, a 2 B vision and 3 B language model (*i.e*.

PaliGemma continues this trend, combining the 400 M SigLIP and the 2 B Gemma models into a sub-3 B VLM that still maintains performance comparable to PaLI-X, PaLM-E, and PaLI-3.

Gemma is a family of auto-regressive decoder-only open large language models built from the same research and technology used to create the Gemini models. The models come in different sizes (2 B, 7 B), both pretrained and instruction fine-tuned. PaliGemma uses the 2 B pretrained version.

The main goal of our work is to provide a versatile base VLM. Hence, we show that it reaches state-of-the-art results not only on standard COCO captions, VQAv2, InfographicVQA and others, but also on more exotic Remote-Sensing VQA, TallyVQA, several video captioning and QA tasks, as well as referring expression *segmentation* (see full task list in Appendix B).

## Conclusion

PaliGemma is a new, small, open base VLM that shines when transferred to a broad range of tasks. Our results show that VLMs on the "smaller" side can provide state-of-the-art performance across a wide variety of benchmarks. We also hope that providing the base model without instruction tuning serves as a useful starting point for further research in instruction tuning, specific applications, and encourages clearer separation of base models and fine-tunes in VLM research.
