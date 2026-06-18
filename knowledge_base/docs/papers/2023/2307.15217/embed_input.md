Open Problems and Fundamental Limitations of Reinforcement Learning from Human Feedback

Reinforcement learning from human feedback (RLHF) is a technique for training AI systems to align with human goals. RLHF has emerged as the central method used to finetune state-of-the-art large language models (LLMs). Despite this popularity, there has been relatively little public work systematizing its flaws. In this paper, we survey open problems and fundamental limitations of RLHF and related methods; overview techniques to understand, improve, and complement RLHF in practice; and propose auditing and disclosure standards to improve societal oversight of RLHF systems. Our work emphasizes the limitations of RLHF and highlights the importance of a multi-faceted approach to the development of safer AI systems.

## Introduction

*Reinforcement learning from human feedback* (RLHF) has emerged as a prominent technique to adapt machine learning models to difficult-to-specify goals. In particular, RLHF is a key component of training state-of-the-art large language models (LLMs), such as OpenAI's GPT-4, Anthropic's Claude, Google's Bard, and Meta's Llama 2-Chat. RLHF and similar methods allow LLMs to go beyond modeling the distribution of their training data, and adapt the distribution of text so that model outputs are rated more highly by human evaluators.

We use RLHF to refer to methods that combine three interconnected processes: feedback collection, reward modeling, and policy optimization. Figure 1 (top) illustrates this setup. The feedback process elicits evaluations of model outputs from humans. The reward modeling process uses supervised learning to train a reward model that imitates these evaluations. The policy optimization process optimizes the AI system to produce outputs that recieve favorable evaluations from the reward model....

Claudia Shi, Thomas Krendl Gilbert, Jérémy Scheurer, Javier Rando, Rachel Freedman, Tomasz Korbak, David Lindner, Pedro Freire, Tony Wang, Samuel Marks, Charbel-Raphaël Segerie, Micah Carroll, Andi Peng, Phillip Christoffersen, Mehul Damani, Stewart Slocum, Usman Anwar, Anand Siththaranjan, Max Nadeau, Eric J. Michaud, Jacob Pfau, Xin Chen, Dmitrii Krasheninnikov, Lauro Langosco, and Peter Hase contributed to writing and planning the paper.

Erdem Bıyık, Anca Dragan, David Krueger, Dorsa Sadigh, and Dylan Hadfield-Menell served as advisors.

Fundamental: Policies can perform poorly in deployment even if rewards seen during training were perfectly correct. The deployment distribution can always differ from the training and evaluation distributions in real-world settings. Even with a correct reward signal, a policy can learn to competently pursue the wrong goal whenever the true goal is correlated with other events. Shah et al.; Di Langosco et al. and Hilton et al. study this type of failure in-depth. Shah et al. present an example scenario in which a systems trained with RLHF misgeneralizes to pursue the mechanism of reward administration itself instead of the intended goal.

Scalar feedback: Obtaining scalar feedback addresses some problems of comparison-based feedback -- it is significantly more expressive....
