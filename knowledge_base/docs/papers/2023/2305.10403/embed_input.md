PaLM 2 Technical Report

Topics include Large language models, Foundation models, Language models, Model scaling, Code generation, Machine translation, Artificial intelligence.

Reports the design and evaluation of the PaLM 2 family of language models, emphasizing stronger multilingual, reasoning, and coding performance relative to earlier PaLM systems. The report is mainly a model card and benchmark record for a production-scale foundation model family.

We introduce PaLM 2, a new state-of-the-art language model that has better multilingual and reasoning capabilities and is more compute-efficient than its predecessor PaLM. PaLM 2 is a Transformer-based model trained using a mixture of objectives. Through extensive evaluations on English and multilingual language, and reasoning tasks, we demonstrate that PaLM 2 has significantly improved quality on downstream tasks across different model sizes, while simultaneously exhibiting faster and more efficient inference compared to PaLM. This improved efficiency enables broader deployment while also allowing the model to respond faster, for a more natural pace of interaction. PaLM 2 demonstrates robust reasoning capabilities exemplified by large improvements over PaLM on BIG-Bench and other reasoning tasks. PaLM 2 exhibits stable performance on a suite of responsible AI evaluations, and enables inference-time control over toxicity without additional overhead or impact on other capabilities. Overall, PaLM 2 achieves state-of-the-art performance across a diverse set of tasks and capabilities....

## Introduction

Language modeling has long been an important research area since Shannon estimated the information in language with next word prediction. Modeling began with $n$-gram based approaches but rapidly advanced with LSTMs. Later work showed that language modelling also led to language understanding. With increased scale and the Transformer architecture, large language models (LLMs) have shown strong performance in language understanding and generation capabilities over the last few years, leading to breakthrough performance in reasoning, math, science, and language tasks....

We introduce PaLM 2, the successor to PaLM, a language model unifying modeling advances, data improvements, and scaling insights. PaLM 2 incorporates the following diverse set of research advances:

We would like to thank our reviewers and colleagues for valuable inputs and discussion on the project -- Jeff Dean, Zoubin Ghahramani, Johan Schalkwyk, Carrie Grimes Bostock, Eli Collins, Claire Cui, Noah Constant, Pengcheng Yin, Bin Ni, Scott Huffman, Salem Haykal, Zhishuai Zhang, Mia Chen, Heather Yoon, Natacha Mainville, Yanqi Zhou and Seojin Bang. We thank Lora Aroyo, Aida Davani, Emily Denton, Ben Hutchinson, Bec Johnson, Shayne Longpre, Vinodkumar Prabhakaran, Rida Qadri, and Greg Yauney for discussion and experiments on related aspects of responsible AI.

Our work builds on top of the work of many, many teams at Google. We'd especially like to recognize the Pax team, the Pathways infrastructure team, the Sax team, AIDA team, the JAX team, the Flaxformer team, the XLA team, the Plaque team, the Borg team, and the Datacenter networking infrastructure team. We gratefully acknowledge the support from our colleagues in infrastructure optimizations and resource management, including James Groeneveld, Dragos Stefanescu, Donghyun Koo, Michael Vorburger, Ken Durden, Steven Chan, Denis Vnukov, Adekunle Bello, Bryan Chiang, Nejc Trdin, Masoud Moshref, Ginger Perng, Josh Newlan, John Schuett, Bekir...

BLEURT: We use BLEURT^1010^10We used BLEURT version 0p2p1 for our measurements. as a SOTA automatic metric instead of BLEU due to BLEU's poor correlation with human judgements of quality, especially for high-quality translations.

The ability of large models to reason, to combine multiple pieces of information, and to make logical inferences is one of their most important...
