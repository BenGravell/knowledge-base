Gemma 2: Improving Open Language Models at a Practical Size

Topics include Transformers, Attention mechanisms, Language models, Gemma 2.

In this work, we introduce Gemma 2, a new addition to the Gemma family of lightweight, state-of-the-art open models, ranging in scale from 2 billion to 27 billion parameters. In this new version, we apply several known technical modifications to the Transformer architecture, such as interleaving local-global attentions and group-query attention. We also train the 2B and 9B models with knowledge distillation instead of next token prediction. The resulting models deliver the best performance for their size, and even offer competitive alternatives to models that are 2-3 times bigger. We release all our models to the community.

## Introduction

Large language models (LLMs) have demonstrated strong capabilities in language understanding, generation, and reasoning (Radford et al. Raffel et al. Brown et al., ). Scaling has been key to this recent progress, with many new capabilities only emerging at scale. The newest large models not only reach unprecedented performance on reasoning benchmarks, but they also demonstrate multimodal and multilingual capabilities and even the ability to use context lengths of over 1M tokens.

Small-scale models have also shown a rapid increase in performance, but these gains are largely derived from increasing the length of training (Touvron et al. Jiang et al. Gemma Team, ). This approach only scales logarithmically with dataset size, and the latest small models require up to 15T tokens to improve the state of the art by less than 1-2%.

Yet, these continued improvements provide evidence that small models are still under-trained. In this work, we explore alternatives to improve small model performance without solely increasing training length. One solution is to improve the quality of information received by the network at each training step by replacing the next token prediction task with a richer objective.

In this technical report, we provide an overview of models, including the architecture, training, and pre- and post-training recipes for Gemma 2. We also provide detailed evaluations across a wide variety of quantitative and qualitative benchmarks, as well as both standard academic benchmarks and human-preference evaluations. Finally, we discuss our approach to safe and responsible deployment and outline the broader implications of Gemma 2, its limitations, and advantages.

## Discussion and Conclusion

In this work, we have presented Gemma 2, the newest additions to the Gemma family of open language models for text and code. We show that distillation is an effective method for training these models, and the benefits distillation confers over raw text training. Specifically, we show how training over output probabilities can produce superior results over purely next token prediction. We hope that releasing these models to the community will unlock access to capabilities previously only seen in large-scale LLMs and fuel future waves of research and development.
