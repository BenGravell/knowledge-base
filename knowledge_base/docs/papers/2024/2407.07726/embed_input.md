PaliGemma: A Versatile 3B VLM for Transfer

Topics include Language models, Vision-language models, Benchmarks, PaliGemma.

PaliGemma is an open Vision-Language Model (VLM) that is based on the SigLIP-So400m vision encoder and the Gemma-2B language model. It is trained to be a versatile and broadly knowledgeable base model that is effective to transfer. It achieves strong performance on a wide variety of open-world tasks. We evaluate PaliGemma on almost 40 diverse tasks including standard VLM benchmarks, but also more specialized tasks such as remote-sensing and segmentation.

## Introduction

Figure 1: PaliGemma’s architecture: a SigLIP image encoder feeds into a Gemma decoder LM.

PaliGemma is an open model, continuing the line of PaLI vision-language models in a combination with the Gemma family of language models.

## Conclusion

PaliGemma is a new, small, open base VLM that shines when transferred to a broad range of tasks. Our results show that VLMs on the "smaller" side can provide state-of-the-art performance across a wide variety of benchmarks. We also hope that providing the base model without instruction tuning serves as a useful starting point for further research in instruction tuning, specific applications, and encourages clearer separation of base models and fine-tunes in VLM research.

We conduct diverse ablations to gain deeper understanding of what matters for training and transferring VLMs. Unless noted otherwise, all ablations are run with the same setup as the main models, except for making the Stage1 pretraining 10x shorter (*i.e*. 100 M examples seen), and transfer results are reported on validation sets instead of withheld test-sets. For each experiment, we present only the salient result summary in the main text, but we provide a full per-task breakdown of results in the Appendix.

Just like for previous PaLI models, the pretraining (Stage1 and Stage2) is designed to result in a model that transfers well, not necessarily a model that is usable out of the box ("0 shot"). The intuition here is that we want a mix of tasks which force the model to acquire a broad range of "skills". We prefix each task with its unique prefix to avoid conflicting learning signals across skills \[\]. At transfer time (Stage3), the model then merely needs to recognize which skill is useful for the task, and rewire itself to use that while following the output syntax and vocabulary of the task....

Overall, we conclude that in our case, the linear connector seems preferable to the MLP connector.

PaLI is a series of state-of-the-art vision-language models, starting with the first PaLI \[\] showing promising scaling results up to 17 B, using classification pretrained ViT \[\] and mT5 \[\] language model. PaLI-X \[\] and PaLM-E \[\] then pushed this further, combining ViT-22 B \[\] and a 32 B UL2 \[\] language model or the 540 B PaLM \[\] language model, respectively, and getting further increased performance on vision-language...
