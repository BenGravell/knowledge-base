Octo: An Open-Source Generalist Robot Policy

Large policies pretrained on diverse robot datasets have the potential to transform robotic learning: instead of training new policies from scratch, such generalist robot policies may be finetuned with only a little in-domain data, yet generalize broadly. However, to be widely applicable across a range of robotic learning scenarios, environments, and tasks, such policies need to handle diverse sensors and action spaces, accommodate a variety of commonly used robotic platforms, and finetune readily and efficiently to new domains. In this work, we aim to lay the groundwork for developing open-source, widely applicable, generalist policies for robotic manipulation. As a first step, we introduce Octo, a large transformer-based policy trained on 800k trajectories from the Open X-Embodiment dataset, the largest robot manipulation dataset to date. It can be instructed via language commands or goal images and can be effectively finetuned to robot setups with new sensory inputs and action spaces within a few hours on standard consumer GPUs....

## Introduction

^††^footnotetext: ^∗^Lead authors, ordered alphabetically, see Appendix A for list of contributions.\
Correspondence to [{dibya.ghosh, homer_walke, pertsch, kvablack, oier.mees}@berkeley.edu](mailto:dibya.ghosh@berkeley.edu,homer_walke@berkeley.edu,pertsch@berkeley.edu,kvablack@berkeley.edu,oier.mees@eecs.berkeley.edu)

The common approach for robotic learning is to train policies on datasets collected for the specific robot and task at hand. Learning from scratch in this way requires significant data collection effort for each task, and the resulting policies usually exhibit only narrow generalization. In principle, collected experience from other robots and tasks offers a possible solution, exposing models to a diverse set of robotic control problems that may improve generalization and performance on downstream tasks....

Expanding the data used to train Octo is a natural avenue of improvement. Since the Open X-Embodiment dataset is comprised of optimal robot demonstrations, the current model trains via imitation; future work may consider learning from sub-optimal or online interaction data that require alternative objectives. Further, while we trained and evaluated Octo exclusively on single and dual-arm manipulators; expanding to a wider set of robots that perform navigation or mobile manipulation would be an direction of high opportunity.

While Octo represents a step towards building generalist robot policies that work out-of-the-box on diverse robot setups, there remains work to improve the model, including better language conditioning, improved support for wrist cameras, and incorporating data beyond optimal demonstrations. We hope that Octo offers a simple launchpad for researchers and practitioners to access larger robotic datasets and leverage pretrained robotics models for efficient learning of new tasks and broad generalization.

Pretrained Octo checkpoints for Octo-Small (27M params) and Octo-Base (93M params).

### III-B Training data

For finetuning, we found that training our large transformer architecture from scratch overfit quickly on the small datasets. Instead, we obtained better from-scratch results using a canonical policy architecture employed by many prior works: a ResNet visual encoder with FiLM \[\] language conditioning, combined with a small transformer action decoder trained with a diffusion objective,...
