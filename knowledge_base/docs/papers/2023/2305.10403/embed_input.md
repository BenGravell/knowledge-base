PaLM 2 Technical Report

Topics include Large language models, Foundation models, Language models, Model scaling, Code generation, Machine translation, Artificial intelligence.

Reports the design and evaluation of the PaLM 2 family of language models, emphasizing stronger multilingual, reasoning, and coding performance relative to earlier PaLM systems. The report is mainly a model card and benchmark record for a production-scale foundation model family.

We introduce PaLM 2, a new state-of-the-art language model that has better multilingual and reasoning capabilities and is more compute-efficient than its predecessor PaLM. PaLM 2 is a Transformer-based model trained using a mixture of objectives. Through extensive evaluations on English and multilingual language, and reasoning tasks, we demonstrate that PaLM 2 has significantly improved quality on downstream tasks across different model sizes, while simultaneously exhibiting faster and more efficient inference compared to PaLM. This improved efficiency enables broader deployment while also allowing the model to respond faster, for a more natural pace of interaction. PaLM 2 demonstrates robust reasoning capabilities exemplified by large improvements over PaLM on BIG-Bench and other reasoning tasks. PaLM 2 exhibits stable performance on a suite of responsible AI evaluations, and enables inference-time control over toxicity without additional overhead or impact on other capabilities. Overall, PaLM 2 achieves state-of-the-art performance across a diverse set of tasks and capabilities.

## Introduction

Language modeling has long been an important research area since Shannon estimated the information in language with next word prediction. Modeling began with $n$-gram based approaches but rapidly advanced with LSTMs. Later work showed that language modelling also led to language understanding. With increased scale and the Transformer architecture, large language models (LLMs) have shown strong performance in language understanding and generation capabilities over the last few years, leading to breakthrough performance in reasoning, math, science, and language tasks.

We introduce PaLM 2, the successor to PaLM, a language model unifying modeling advances, data improvements, and scaling insights.

Improved dataset mixtures: Previous large pre-trained language models typically used a dataset dominated by English text (e.g., $\sim$`<!-- -->`{=html}78% of non-code in Chowdhery et al. ). We designed a more multilingual and diverse pre-training mixture, which extends across hundreds of languages and domains (e.g., programming languages, mathematics, and parallel multilingual documents). We show that larger models can handle more disparate non-English datasets without causing a drop in English language understanding performance, and apply deduplication to reduce memorization

## Discussion

Memorization analysis provides a systematic study which can inform the potential privacy risks in downstream uses. Importantly, we find significant reductions in verbatim memorization on average as compared to PaLM, and in particular for data repeated fewer than three times in the pre-training data. We note that these memorization rates are an estimate and do not provide a full characterization of what could be recovered by a successful adversary with access to PaLM 2.

## Conclusion

PaLM 2 is a new state-of-the-art model that significantly outperforms PaLM while using significantly less compute at inference time. PaLM 2 achieves gains on a wide range of different tasks, ranging from English and multilingual language understanding, to reasoning. With PaLM 2, we have independently verified the scaling laws from Hoffmann et al. at large scales; we have shown that training tokens should grow at roughly the same rate as the number of model parameters.
