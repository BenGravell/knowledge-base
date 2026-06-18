Open Problems and Fundamental Limitations of Reinforcement Learning from Human Feedback

Reinforcement learning from human feedback (RLHF) is a technique for training AI systems to align with human goals. RLHF has emerged as the central method used to finetune state-of-the-art large language models (LLMs). Despite this popularity, there has been relatively little public work systematizing its flaws. In this paper, we survey open problems and fundamental limitations of RLHF and related methods; overview techniques to understand, improve, and complement RLHF in practice; and propose auditing and disclosure standards to improve societal oversight of RLHF systems. Our work emphasizes the limitations of RLHF and highlights the importance of a multi-faceted approach to the development of safer AI systems.

## Introduction

*Reinforcement learning from human feedback* (RLHF) has emerged as a prominent technique to adapt machine learning models to difficult-to-specify goals. In particular, RLHF is a key component of training state-of-the-art large language models (LLMs), such as OpenAI's GPT-4, Anthropic's Claude, Google's Bard, and Meta's Llama 2-Chat. RLHF and similar methods allow LLMs to go beyond modeling the distribution of their training data, and adapt the distribution of text so that model outputs are rated more highly by human evaluators.

Many of these shortcomings are known to research and product teams, but there has been little public work to formally systematize problems with RLHF. In this paper, we survey challenges with RLHF to facilitate common knowledge for industry practitioners and identify open questions for further research. We focus primarily on applications to LLMs.

Concrete challenges with RLHF: In Section 3, we taxonomize and survey problems associated with RLHF. We divide them into three primary categories: challenges with the human feedback, challenges with the reward model, and challenges with the policy. We also distinguish between challenges with RLHF that are more tractable and could be addressed within the RLHF framework using improved methodology versus fundamental limitations of RLHF, which require alternative approaches.^11^1We use color only to highlight topics. This paper can be viewed in grayscale.

## Limitations of Feedback Types

Fundamental: RLHF suffers from a tradeoff between the richness and efficiency of feedback types. Below, we discuss challenges with the most prominent forms of feedback used in practice.

Comparison-based feedback: The most common type of feedback used with RLHF is binary preferences between pairs of examples though $k$-wise rankings or best-of-$k$ queries can be used as well. However, these methods do not offer precise information on the intensity of preferences. A learned preference ordering can fail to converge to the true one when the desirability of examples depends on noise or unmodeled, contextual details not contained in the observations (e.g., randomness in a human's feedback or differences between evaluators ).
