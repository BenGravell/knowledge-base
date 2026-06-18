A Careful Examination of Large Behavior Models for Multitask Dexterous Manipulation

Topics include Imitation learning, Robotics, Robustness, Diffusion models, Foundation models, Control, Learning.

Robot manipulation has seen tremendous progress in recent years, with imitation learning policies enabling successful performance of dexterous and hard-to-model tasks. Concurrently, scaling data and model size has led to the development of capable language and vision foundation models, motivating large-scale efforts to create general-purpose robot foundation models. While these models have garnered significant enthusiasm and investment, meaningful evaluation of real-world performance remains a challenge, limiting both the pace of development and inhibiting a nuanced understanding of current capabilities. In this paper, we rigorously evaluate multitask robot manipulation policies, referred to as Large Behavior Models (LBMs), by extending the Diffusion Policy paradigm across a corpus of simulated and real-world robot data. We propose and validate an evaluation pipeline to rigorously analyze the capabilities of these models with statistical confidence. We compare against single-task baselines through blind, randomized trials in a controlled setting, using both simulation and real-world experiments.

## Introduction

Achieving flexible, generalist robots is a central ambition of robotics research. While modern robots are physically capable of performing a wide array of tasks in myriad settings, reliable autonomy has traditionally been limited to simple tasks or highly structured environments. Recently, visuomotor learning-based methods---trained to condition on robot sensor observations and produce low-level actions---have emerged as promising solutions to bridge this gap between hardware capabilities and autonomous performance.

Despite these strengths, single-task behavior-cloned policies remain brittle, exhibiting limited generalization to task variations or environments outside their training distributions. To overcome this brittleness, the field is increasingly adopting Large Behavior Models (LBMs) --visuomotor foundation models trained on large-scale multitask datasets containing action-level demonstrations. Inspired by the success of large-scale generalist models in Computer Vision and Natural Language Processing, these models seek to improve reliability through broad training data support and more robust learned visual and sensory representations.

Through

Given the same amount of task-specific data, finetuned specialists derived from pretrained LBMs outperform single-task models when aggregating over tasks.

## Discussion and Conclusion

Large Behavior Models move dexterous manipulation away from task-specific engineering and into a scalable and data-driven paradigm similar to recent progress in language and vision. To rigorously quantify the capabilities of current LBMs, we train a series of models on roughly 1,700 hours of heterogeneous demonstration data and analyze their performance on 1,800 blind A/B-style real-world rollouts and over 47,000 simulation rollouts.

We find that finetuning LBMs into task-specific specialists consistently outperforms from-scratch training with a given amount of finetuning data or allow achieving from-scratch-equivalent performance with 3-5x less data required. These differences are also amplified under deployment distribution shift---when test-time conditions differ from those encountered during training. This finding is critical because distribution shift is virtually inescapable in real-world use cases and is often omitted from empirical robotics work, masking important information about real-world utility.
