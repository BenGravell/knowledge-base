ReasonFlux: Hierarchical LLM Reasoning via Scaling Thought Templates

We present that hierarchical LLM reasoning via scaling thought templates can effectively optimize the reasoning search space and outperform the mathematical reasoning capabilities of powerful LLMs like OpenAI o1-preview and DeepSeek V3. We train our ReasonFlux-32B model with only 8 GPUs and introduces three innovations: (i) a structured and generic thought template library, containing around 500 high-level thought templates capable of generalizing to similar or relevant reasoning problems; (ii) performing hierarchical reinforcement learning on a sequence of thought templates instead of long CoTs, optimizing a base LLM to plan out an optimal template trajectory for gradually handling complex problems; (iii) a brand new inference scaling system that enables hierarchical LLM reasoning by adaptively scaling thought templates at inference time. With a template trajectory containing more explainable reasoning structures than DeepSeek-R1 and o3-mini, our ReasonFlux-32B significantly advances math reasoning capabilities to state-of-the-art levels. Notably, on the MATH benchmark, it achieves an accuracy of 91.2% and surpasses o1-preview by 6.7%....

## Introduction

Large Language Models (LLMs) have recently achieved remarkable progress, demonstrating exceptional capabilities in tackling complex reasoning tasks and even surpassing human experts in specific domains. For example, models such as OpenAI's O1, Google's Gemini-2.0, DeepSeek-V3, and Qwen-QwQ are at the forefront of this progress, characterized by their ability to emulate human reasoning through a slower, more deliberate thought process. These models leverage increased inference time to enhance reasoning accuracy....

Figure 1: Training framework for our ReasonFlux. We train with hierarchical reinforcement learning to enable the model to plan out an optimal and generalizable thought template trajectory for an input problem. Our new inference-scaling framework is in Figure 2.

## Conclusion

In this work, we present ReasonFlux, a new hierarchical LLM reasoning framework that adaptively scales fundamental and essential thought templates for simplifying the search space of complex reasoning, and outperforming the mathematical reasoning capabilities of powerful LLMs like OpenAI o1-preview and DeepSeek V3. We introduces a structured and compact thought template library, hierarchical reinforcement learning on thought template trajectory and a brand new inference scaling system. Extensive experiments across different challenging math benchmarks demonstrate the superiority of ReasonFlux....

where $T_{\text{rag}} = {\{ T_{1},T_{2},\ldots,T_{n}\}}$ is the set of $n$ retrieved templates that equals to the number of steps in the configured trajectory, and each is a structured template.

### Hierarchical Reinforcement Learning on Thought Template Trajectory

### Baselines

Subsequent research has focused on enhancing LLMs' reasoning capabilities on complex problems through inference-time strategies. These strategies can be divided into two categories: deliberate search and reward-model-guided methods. Deliberate search methods, like Tree of Thoughts (ToT) and Graph of Thoughts (GoT), allow LLMs to explore multiple reasoning paths and self-evaluate choices to find the optimal trajectory. Reward-model-guided methods leverage reward models to assess reasoning step quality....

To achieve more efficient and precise search of reasoning paths, a feasible approach is to utilize Retrieval-Augmented Generation (RAG)....
