Gemma: Open Models Based on Gemini Research and Technology

Topics include Safety, Benchmarks, Gemma.

This work introduces Gemma, a family of lightweight, state-of-the art open models built from the research and technology used to create Gemini models. Gemma models demonstrate strong performance across academic benchmarks for language understanding, reasoning, and safety. We release two sizes of models (2 billion and 7 billion parameters), and provide both pretrained and fine-tuned checkpoints. Gemma outperforms similarly sized open models on 11 out of 18 text-based tasks, and we present comprehensive evaluations of safety and responsibility aspects of the models, alongside a detailed description of model development. We believe the responsible release of LLMs is critical for improving the safety of frontier models, and for enabling the next wave of LLM innovations.

## Introduction

We present Gemma, a family of open models based on Google's Gemini models.

We trained Gemma models on up to 6T tokens of text, using architectures, data, and training recipes inspired by the Gemini model family. Like Gemini, these models achieve strong generalist capabilities in text domains, alongside state-of-the-art understanding and reasoning skills at scale. With this work, we release both pre-trained and fine-tuned checkpoints, as well as an open-source codebase for inference and serving.

Mihir Sanjay Kale\
Pier Giuseppe Sessa

Alek Andreev$\dagger$\
Kathleen Kenealy$\dagger$ ^††^$\dagger$ equal contribution.

Table 6: Academic benchmark results, compared to similarly sized, openly-available models trained on general English text data. † Mistral reports 50.2 on a different split for MBPP and on their split our 7B model achieves 54.5. ∗ evaluations run by us. Note that due to restrictive licensing, we were unable to run evals on LLaMA-2; all values above were previously reported in Touvron et al..

### Filtering

Perhaps of higher importance is the possibility that personal data might be memorized. As part of making Gemma pre-trained models safe and reliable, we used automated techniques to filter out certain personal information and other sensitive data from training sets.

Gemma comes in two sizes: a 7 billion parameter model for efficient deployment and development on GPU and TPU, and a 2 billion parameter model for CPU and on-device applications. Each size is designed to address different computational constraints, applications, and developer requirements. At each scale, we release raw, pretrained checkpoints, as well as checkpoints fine-tuned for dialogue, instruction-following, helpfulness, and safety. We thoroughly evaluate the shortcomings of our models on a suite of quantitative and qualitative benchmarks....

Gemma advances state-of-the-art performance relative to comparable-scale (and some larger), open models across a wide range of domains including both automated benchmarks and human evaluation. Example domains include question answering (Clark et al. Kwiatkowski et al., ), commonsense reasoning (Sakaguchi et al. Suzgun et al., ), mathematics and science (Cobbe et al. Hendrycks et al., ), and coding (Austin et al. Chen et al., ). See complete details in the Evaluation section.
