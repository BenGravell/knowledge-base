Octo: An Open-Source Generalist Robot Policy

Large policies pretrained on diverse robot datasets have the potential to transform robotic learning: instead of training new policies from scratch, such generalist robot policies may be finetuned with only a little in-domain data, yet generalize broadly. However, to be widely applicable across a range of robotic learning scenarios, environments, and tasks, such policies need to handle diverse sensors and action spaces, accommodate a variety of commonly used robotic platforms, and finetune readily and efficiently to new domains. In this work, we aim to lay the groundwork for developing open-source, widely applicable, generalist policies for robotic manipulation. As a first step, we introduce Octo, a large transformer-based policy trained on 800k trajectories from the Open X-Embodiment dataset, the largest robot manipulation dataset to date. It can be instructed via language commands or goal images and can be effectively finetuned to robot setups with new sensory inputs and action spaces within a few hours on standard consumer GPUs.

## Introduction

^††^footnotetext: ^∗^Lead authors, ordered alphabetically, see Appendix A for list of contributions.\
Correspondence to [{dibya.ghosh, homer_walke, pertsch, kvablack, oier.mees}@berkeley.edu](mailto:dibya.ghosh@berkeley.edu,homer_walke@berkeley.edu,pertsch@berkeley.edu,kvablack@berkeley.edu,oier.mees@eecs.berkeley.edu)

The common approach for robotic learning is to train policies on datasets collected for the specific robot and task at hand. Learning from scratch in this way requires significant data collection effort for each task, and the resulting policies usually exhibit only narrow generalization. In principle, collected experience from other robots and tasks offers a possible solution, exposing models to a diverse set of robotic control problems that may improve generalization and performance on downstream tasks.

We design a system for pretraining generalist robot policies more suitable for the diversity of interfaces in downstream robotic applications. The core of our model is a transformer architecture that maps arbitrary input tokens (created from observations and tasks) to output tokens (then decoded into actions), which can be trained on a diverse dataset of robots and tasks. With no additional training, this policy can accept different camera configurations (e.g., workspace or wrist cameras), can control different robots, and can be guided via either language commands or goal images --- all by simply changing which tokens are fed into the model.

## Discussion and Future Work

We introduced Octo, a large transformer-based policy pretrained on the largest robot manipulation dataset to date, 800k robot trajectories. We demonstrated that Octo can solve a variety of tasks out-of-the-box and showed how Octo's compositional design enables finetuning to new inputs and action spaces, making Octo a versatile initialization for a wide range of robotic control problems. Apart from the model itself, we have released our full training and finetuning code, alongside tools that make it easier to train on large robot datasets.
