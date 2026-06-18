DINO-WM: World Models on Pre-trained Visual Features Enable Zero-shot Planning

The ability to predict future outcomes given control actions is fundamental for physical reasoning. However, such predictive models, often called world models, remains challenging to learn and are typically developed for task-specific solutions with online policy learning. To unlock world models' true potential, we argue that they should 1) be trainable on offline, pre-collected trajectories, 2) support test-time behavior optimization, and 3) facilitate task-agnostic reasoning. To this end, we present DINO World Model (DINO-WM), a new method to model visual dynamics without reconstructing the visual world. DINO-WM leverages spatial patch features pre-trained with DINOv2, enabling it to learn from offline behavioral trajectories by predicting future patch features. This allows DINO-WM to achieve observational goals through action sequence optimization, facilitating task-agnostic planning by treating goal features as prediction targets....

## Introduction

Robotics and embodied AI have seen tremendous progress in recent years. Advances in imitation learning and reinforcement learning have enabled agents to learn complex behaviors across diverse tasks (Agarwal et al. Zhao et al. Lee et al. Ma et al. Hafner et al. Hansen et al. Haldar et al. Jia et al., ). Despite this progress, generalization remains a major challenge. Existing approaches predominantly rely on policies that, once trained, operate in a feed-forward manner during deployment---mapping observations to actions without any further optimization or reasoning....

Instead of learning the solutions to all possible tasks during training, an alternate is to fit a dynamics model on training data and optimize task-specific behavior at runtime. These dynamics models, also called world models, have a long history in robotics and control (Sutton Todorov & Li Williams et al., ). More recently, several works have shown that world models can be trained on raw sensory data (Hafner et al. Micheli et al. Robine et al. Hansen et al. Hafner et al., ). This enables flexible use of model-based optimization to obtain policies as it circumvents the need for explicit state-estimation....

## Impact Statement

This paper presents work whose goal is to facilitate the learning and applications of task-agnostic world models. There are many potential societal consequences of our work, none which we feel must be specifically highlighted here.

## Experiments

### Transition Model

### Optimizing Behaviors with DINO-WM

To understand the challenges in world modeling, let us consider the two broad paradigms in learning world models: online and offline. In the online setting, access to the environment is often required so data can be continuously collected to improve the world model, which in turn improves the policy and the subsequent data collection. However, the online world model is only accurate in the cover of the policy that was being optimized. Hence, while it can be used to train powerful task-specific policies, it requires retraining for every new task even in the same environment....

Figure 1: We present DINO-WM, a method for training visual models by using pretrained DINOv2 embeddings of image frames (a). Once trained, given a target observation oT, we can directly optimize agent behavior by planning through DINO-WM using model predictive control...
