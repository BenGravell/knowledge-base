Gemma 2: Improving Open Language Models at a Practical Size

Topics include Transformers, Attention mechanisms, Language models, Gemma 2.

In this work, we introduce Gemma 2, a new addition to the Gemma family of lightweight, state-of-the-art open models, ranging in scale from 2 billion to 27 billion parameters. In this new version, we apply several known technical modifications to the Transformer architecture, such as interleaving local-global attentions and group-query attention. We also train the 2B and 9B models with knowledge distillation instead of next token prediction. The resulting models deliver the best performance for their size, and even offer competitive alternatives to models that are 2-3 times bigger. We release all our models to the community.

## Introduction

Large language models (LLMs) have demonstrated strong capabilities in language understanding, generation, and reasoning (Radford et al. Raffel et al. Brown et al., ). Scaling has been key to this recent progress, with many new capabilities only emerging at scale. The newest large models not only reach unprecedented performance on reasoning benchmarks, but they also demonstrate multimodal and multilingual capabilities and even the ability to use context lengths of over 1M tokens.

Small-scale models have also shown a rapid increase in performance, but these gains are largely derived from increasing the length of training (Touvron et al. Jiang et al. Gemma Team, ). This approach only scales logarithmically with dataset size, and the latest small models require up to 15T tokens to improve the state of the art by less than 1-2%.

## Contributions and Acknowledgments

Pier Giuseppe Sessa^∗^\
Contributors (alphabetical order)\
Dominika Rogozińska\
Hanna Klimczak-Plucińska\
Jin Peng Zhou\
Joost van Amersfoort\
Lars Lowe Sjoesund\
Livio Baldini Soares\
Reza Ardeshir Rokni\

### Post-training Evaluations

In this section, we focus on the main finding of this work, which is the impact of knowledge distillation on small language models.

### Impact assessment

Yet, these continued improvements provide evidence that small models are still under-trained. In this work, we explore alternatives to improve small model performance without solely increasing training length. One solution is to improve the quality of information received by the network at each training step by replacing the next token prediction task with a richer objective.

In particular, we focus our efforts on knowledge distillation, which replaces the one-hot vector seen at each token with the distribution of potential next tokens computed from a large model. This approach is often used to reduce the training time of smaller models by giving them richer gradients. In this work, we instead train for large quantities of tokens with distillation in order to simulate training beyond the number of available tokens....

We also leverage several known modifications of Transformers, namely the interleaving of global and local attention layers from Beltagy et al., and the Grouped-Query Attention (GQA) mechanism of Ainslie et al..
