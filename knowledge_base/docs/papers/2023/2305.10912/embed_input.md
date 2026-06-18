A Generalist Dynamics Model for Control

We investigate the use of transformer sequence models as dynamics models (TDMs) for control. We find that TDMs exhibit strong generalization capabilities to unseen environments, both in a few-shot setting, where a generalist TDM is fine-tuned with small amounts of data from the target environment, and in a zero-shot setting, where a generalist TDM is applied to an unseen environment without any further training. Here, we demonstrate that generalizing system dynamics can work much better than generalizing optimal behavior directly as a policy. Additional results show that TDMs also perform well in a single-environment learning setting when compared to a number of baseline models. These properties make TDMs a promising ingredient for a foundation model of control.

## Introduction

An important goal of robotics research is to create embodied agents that are able to achieve a wide range of flexibly defined goals in a wide range of complicated environments. During the last decade, advancements in artificial intelligence, specifically the renaissance of neural networks, have strongly influenced the field. Examples include deep visuomotor policies, dexterous manipulation or multi-agent soccer with humanoid robots. These works have in common that they demonstrate high-quality behavior for complicated tasks, but require large amounts of data, and result in specialist agents.

Recently, training large models on large amounts of data has enabled big leaps in generality in areas such as language modelling. This has inspired interest in using large models to improve generality of embodied agents as well; either by using language models for high-level decision making or by using the large model itself to output control instructions.

Concretely, we highlight two different aspects of TDMs in our experiments (see overview in Fig. 1): First, we demonstrate that TDMs generalize strongly across environments; specifically, we show that a generalist TDM can be used for few-shot or even zero-shot generalization to unseen environments. Second, we demonstrate that, compared to a number of baselines, TDMs make accurate predictions suitable for planning when learning from transition data of the target environment (specialist model learning).

## Discussion

Pixel observations: In this paper, we restrict our experiments to environments with state-based observations and did not consider pixel-based observations. Apart from reducing need for computational resources, this was done in order to isolate generalization effects due to a transfer of a basic understanding of physics from generalization effects due to a transfer of perceptual capabilities. That being said, pixel-based domains are an interesting and natural extension of our work for at least two reasons: First, pixel-based observations open up our approach to more data sources, especially for real-world environments.
