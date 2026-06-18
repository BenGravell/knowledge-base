AnglE-optimized Text Embeddings

Topics include Large language models, Language models, Datasets, Optimization, STS, SOTA.

High-quality text embedding is pivotal in improving semantic textual similarity (STS) tasks, which are crucial components in Large Language Model (LLM) applications. However, a common challenge existing text embedding models face is the problem of vanishing gradients, primarily due to their reliance on the cosine function in the optimization objective, which has saturation zones. To address this issue, this paper proposes a novel angle-optimized text embedding model called AnglE. The core idea of AnglE is to introduce angle optimization in a complex space. This novel approach effectively mitigates the adverse effects of the saturation zone in the cosine function, which can impede gradient and hinder optimization processes. To set up a comprehensive STS evaluation, we experimented on existing short-text STS datasets and a newly collected long-text STS dataset from GitHub Issues. Furthermore, we examine domain-specific STS scenarios with limited labeled data and explore how AnglE works with LLM-annotated data. Extensive experiments were conducted on various tasks including short-text STS, long-text STS, and domain-specific STS tasks....

## Introduction

The development of text embeddings (Kiros et al. Hill et al. Conneau et al. Cer et al. Reimers & Gurevych Gao et al., ) is an essential research challenge in the NLP community. Text embeddings effectively feature key semantic and syntactic information in language, which broadly affects the performance of downstream tasks, such as text classification, sentiment analysis (Suresh & Ong Zhang et al., ), semantic matching (Grill et al. Lu et al., ), clustering (Reimers & Gurevych Xu et al., ), and question-answering (QA) system....

Figure 1: The saturation zones of the cosine function. The gradient at saturation zones is close to zero. During optimization, the gradient could be killed, making the network difficult to learn.

## Conclusion and Future Work

In this paper, we have presented a novel text embedding model called AnglE, which optimizes the angle difference in complex space to overcome the adverse impact of the saturation zone of the cosine function, thereby improving text embeddings. To comprehensively evaluate the STS tasks, we have introduced the GitHub Issues Similarity Dataset to evaluate model performance on the long-text STS task. Furthermore, we have proposed an LLM-supervised learning method to cope with the scarcity of domain-supervised data....

### Existing STS Benchmarks

where $\tau$ is a temperature hyperparameter, $\cos{( \cdot )}$ is the cosine similarity function, and $s{(u,v)}$ is the similarity between $u$ and $v$. By optimizing the $\mathcal{L}_{cos}$, we expect the cosine similarity of the high similarity pair to be greater than that of the low similarity pair.

We compare our proposed model with widely used baselines, encompassing both unsupervised and supervised models. The unsupervised models are average GloVe, BERT-flow, BERT-whitening, LLaMA2, and contrastive learning models including IS-BERT, CT-BERT, SimCSE, ConSERT, and DiffCSE. On the other hand, the chosen supervised models are InferSent, USE, SBERT, CoSENT, as well as supervised versions of SimCSE and ConSERT.

Recent studies have utilized pre-trained language models such as BERT and RoBERTa in combination with contrastive learning to enhance the quality of text embeddings. These approaches involve pulling semantically similar samples together and pushing apart those not....
