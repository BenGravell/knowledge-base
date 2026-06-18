MMaDA: Multimodal Large Diffusion Language Models

We introduce MMaDA, a novel class of multimodal diffusion foundation models designed to achieve superior performance across diverse domains such as textual reasoning, multimodal understanding, and text-to-image generation. The approach is distinguished by three key innovations: (i) MMaDA adopts a unified diffusion architecture with a shared probabilistic formulation and a modality-agnostic design, eliminating the need for modality-specific components. This architecture ensures seamless integration and processing across different data types. (ii) We implement a mixed long chain-of-thought (CoT) fine-tuning strategy that curates a unified CoT format across modalities. By aligning reasoning processes between textual and visual domains, this strategy facilitates cold-start training for the final reinforcement learning (RL) stage, thereby enhancing the model's ability to handle complex tasks from the outset. (iii) We propose UniGRPO, a unified policy-gradient-based RL algorithm specifically tailored for diffusion foundation models.

## Introduction

Large language models (LLMs) have revolutionized natural language processing (NLP) by achieving state-of-the-art performance in diverse tasks, from text generation (e.g., ChatGPT ) to complex reasoning. Inspired by their success, the research community has extended LLMs to the multimodal domain, giving rise to multimodal large language models (MLLMs) or vision-language models (VLMs), such as GPT-4 and Gemini. These models aim to provide a unified framework for both understanding and generating across heterogeneous modalities---text, images, and beyond.

Although recent advancements have explored diffusion-based architectures for global context modeling and parallel generation, existing unified multimodal foundation models predominantly focus on model architecture design and pretraining strategies, leaving a critical gap in the exploration of post-training methodologies, particularly in non-autoregressive settings.

Unified Diffusion Foundation Architecture: We propose MMaDA, a class of diffusion-based models that extend traditional generators into generalist task solvers via a shared probabilistic formulation and modality-agnostic architecture. This design eliminates modality-specific components while maintaining strong performance across tasks.

Mixed Long-CoT Post-Training: We introduce mixed long chain-of-thought (CoT) finetuning to enable cold-start training. By curating a unified CoT format across tasks, we align reasoning processes between modalities (e.g., textual and visual), fostering cross-modal synergy and learning intermediate reasoning before final output generation.

## Conclusion

This work introduces a unified diffusion foundation model, namely MMaDA, that integrates textual reasoning, multimodal understanding, and generation within a single probabilistic framework. To the best of our knowledge, MMaDA is the first to systematically explore the design space of diffusion-based foundation models, proposing novel post-training strategies. Extensive experiments across diverse vision-language tasks demonstrate that MMaDA is comparable to or even better than specialized models, highlighting the potential of diffusion models as a next-generation foundation paradigm for multimodal intelligence.
