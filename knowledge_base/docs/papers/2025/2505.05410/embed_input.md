Reasoning Models Don't Always Say What They Think

Chain-of-thought (CoT) offers a potential boon for AI safety as it allows monitoring a model's CoT to try to understand its intentions and reasoning processes. However, the effectiveness of such monitoring hinges on CoTs faithfully representing models' actual reasoning processes. We evaluate CoT faithfulness of state-of-the-art reasoning models across 6 reasoning hints presented in the prompts and find: for most settings and models tested, CoTs reveal their usage of hints in at least 1% of examples where they use the hint, but the reveal rate is often below 20%, outcome-based reinforcement learning initially improves faithfulness but plateaus without saturating, and when reinforcement learning increases how frequently hints are used (reward hacking), the propensity to verbalize them does not increase, even without training against a CoT monitor. These results suggest that CoT monitoring is a promising way of noticing undesired behaviors during training and evaluations, but that it is not sufficient to rule them out.

## Introduction

Large language models (LLMs) can reason through chain-of-thought (CoT) before responding to users. Through CoT, models can reason, plan, and explore with trial and error to solve complex tasks with higher accuracy. This CoT ability has been further enhanced in the recent surge of reasoning models such as OpenAI o1/o3 (OpenAI et al. OpenAI, ), DeepSeek R1, Gemini Flash Thinking and Claude 3.7 Sonnet Extended Thinking. In addition to improving task capabilities, we may get AI safety benefits from CoT: we can monitor a model's CoT reasoning to try to understand the intentions and goals behind a response.

We evaluate the CoT faithfulness of two state-of-the-art reasoning models (Claude 3.7 Sonnet and DeepSeek R1)^22^2We don't study the o1 or o3 reasoning models in this paper because we don't have access to their CoT and thus can't evaluate their faithfulness. across 6 kinds of reasoning hints presented in the prompts (Turpin et al. Chua and Evans, ) (Section 3). Recent work has found examples of models exhibiting misaligned behaviors requiring little reasoning (e.g., alignment faking, sandbagging, and reward tampering ), so in this work we focus on reasoning that models can perform in a single forward pass.

Scaling up outcome-based RL does not steadily improve CoT faithfulness beyond a low plateau;

## Limitations of Our Settings

Our settings have some important differences with more realistic settings where CoT monitoring might be used. First, our settings are variations on the sort of multiple-choice questions frequently used in benchmarks and exams, which usually expect reasoning that is about the question: during training most exam questions are followed by an explanation that is purely about the content, and that does not mention potential circumstantial hints.

## Conclusion

We empirically study the CoT faithfulness of reasoning models and find that CoT monitoring is a promising approach to noticing unintended behaviors, but that it is not reliable enough to rule out unintended behaviors. Our findings are limited in a variety of ways, as they focus on unintended behaviors for which a CoT is not necessary, and only study a particular kind of unintended behavior (using hints to answer a multiple-choice question). We are excited for further work on this area, as CoT monitoring could potentially be a powerful ingredient in alignment.
