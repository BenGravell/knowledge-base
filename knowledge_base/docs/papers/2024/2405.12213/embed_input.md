<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Octo: An Open-Source Generalist Robot Policy

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Large policies pretrained on diverse robot datasets have the potential to transform robotic learning: instead of training new policies from scratch, such generalist robot policies may be finetuned with only a little in-domain data, yet generalize broadly. However, to be widely applicable across a range of robotic learning scenarios, environments, and tasks, such policies need to handle diverse sensors and action spaces, accommodate a variety of commonly used robotic platforms, and finetune readily and efficiently to new domains. In this work, we aim to lay the groundwork for developing open-source, widely applicable, generalist policies for robotic manipulation. As a first step, we introduce Octo, a large transformer-based policy trained on 800k trajectories from the Open X-Embodiment dataset, the largest robot manipulation dataset to date. It can be instructed via language commands or goal images and can be effectively finetuned to robot setups with new sensory inputs and action spaces within a few hours on standard consumer GPUs. In experiments across 9 robotic platforms, we demonstrate that Octo serves as a versatile policy initialization that can be effectively finetuned to new observation and action spaces.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

We also perform detailed ablations of design decisions for the Octo model, from architecture to training data, to guide future research on building generalist robot models.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

^††^footnotetext: ^∗^Lead authors, ordered alphabetically, see Appendix A for list of contributions.\The common approach for robotic learning is to train policies on datasets collected for the specific robot and task at hand. Learning from scratch in this way requires significant data collection effort for each task, and the resulting policies usually exhibit only narrow generalization. In principle, collected experience from other robots and tasks offers a possible solution, exposing models to a diverse set of robotic control problems that may improve generalization and performance on downstream tasks. However, even as general-purpose models become ubiquitous in natural language) and computer vision, it has proven challenging to build the analogous "general-purpose robot model" that can control many robots for many tasks. Training a unified control policy in robotics presents unique challenges, requiring handling different robot embodiments, sensor setups, action spaces, task specifications, environments, and compute budgets.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

Towards this direction, several works have proposed robotic foundation models that directly map robot observations to actions and provide zero-shot or few-shot generalization to new domains and robots. We broadly refer to these models as "generalist robot policies" (GRPs), emphasizing their ability to perform low-level visuomotor control across tasks, environments, and robotic systems. For example, the GNM model generalizes across different robotic navigation scenarios, the RoboCat model handles different robot embodiments for goal-conditioned tasks, and the RT-X model performs language-conditioned manipulation across five robot embodiments. Although these models represent significant steps toward a true "general-purpose robot model," they have been limited in multiple important aspects: they typically constrain downstream users to a pre-defined and often restrictive set of input observations, e.g., a single camera stream; they lack support for effective finetuning to new domains; and importantly, the largest of these models are not available to the general public.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

We design a system for pretraining generalist robot policies more suitable for the diversity of interfaces in downstream robotic applications. The core of our model is a transformer architecture that maps arbitrary input tokens (created from observations and tasks) to output tokens (then decoded into actions), which can be trained on a diverse dataset of robots and tasks. With no additional training, this policy can accept different camera configurations (e.g., workspace or wrist cameras), can control different robots, and can be guided via either language commands or goal images --- all by simply changing which tokens are fed into the model. Most importantly, the model can be adapted to new robot setups with new sensory inputs, action spaces, or morphologies by adding appropriate adapters and finetuning with a small target domain dataset and an accessible compute budget.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

Our primary contribution is Octo, a transformer-based policy pretrained on the largest robot manipulation dataset to date: 800k robot demonstrations from the Open X-Embodiment dataset. Octo is the first GRP that can be effectively finetuned to new observations and action spaces and the first generalist robot manipulation policy that is fully open-source, including the training pipeline, model checkpoints, and data. Finally, while the individual components that comprise Octo --- a transformer backbone, support for both language and goal image specification, and a diffusion head to model expressive action distributions --- have been discussed in prior work, the particular combination of these components into a powerful generalist robot policy is unique and novel.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Introduction", "weight": 1.5} -->

We demonstrate through extensive experiments on 9 robots across 4 institutions that our combined system leads to state-of-the-art performance for out-of-the-box multi-robot control for single and dual-arm manipulation tasks and that Octo can be used as an effective initialization for finetuning to unseen setups with new observation and action spaces. In the process, we carefully study the effect of different design decisions when pretraining GRPs; we evaluate how the choice of data distribution, model architecture, and policy formulation affects the quality of the pretrained GRP. Our evaluation highlights the utility of scale and flexibility: our best models are those trained on the widest data mixtures, with the least restrictive inductive biases, and with policy objectives that can fit the diversity of behaviors in the pretraining data.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Introduction", "weight": 1.5} -->

Along with this paper, we release all resources required to train, use, reproduce, and finetune an Octo model. We provide pretrained Octo model checkpoints with 27M and 93M parameters that, out of the box, support multiple RGB camera inputs as well as both language and goal image task specification. We also provide scripts for finetuning these models on new domains, as well as our complete pretraining pipeline, including optimized data loaders, transformer implementations for multimodal inputs, and tools to monitor training progress.

<!-- chunk {"id": "body-0010", "role": "body", "section": "The Octo Model", "weight": 1.0} -->

In this section, we describe the Octo model, our open-source generalist robot policy that can be adapted to new robots and tasks --- including new sensory inputs and action spaces --- via finetuning. We discuss the key design decisions, training objectives, training dataset, and infrastructure. The design of the Octo model emphasizes flexibility and scale: it supports a variety of commonly used robots, sensor configurations, and actions while providing a generic and scalable recipe that can be trained on large amounts of data. It also supports natural language instructions, goal images, observation histories, and multi-modal, chunked action prediction via diffusion decoding. Furthermore, we designed Octo specifically to enable efficient finetuning to new robot setups, including robots with different action spaces and different combinations of cameras and proprioceptive information. This design was selected to make Octo a flexible and broadly applicable generalist robot policy that can be utilized for a variety of downstream robotics applications and research projects.

<!-- chunk {"id": "body-0011", "role": "body", "section": "III-A Architecture", "weight": 1.0} -->

At its core, Octo is a transformer-based policy $\pi$. It consists of three key parts: input tokenizers that transform language instructions $\ell$, goals $g$, and observation sequences $o_{1},\ldots,o_{H}$ into tokens $\left\lbrack \mathcal{T}_{l},\mathcal{T}_{g},\mathcal{T}_{o} \right\rbrack$ (Fig., left); a transformer backbone that processes the tokens and produces embeddings ${e_{l},e_{g},e_{o}} = {T{(\mathcal{T}_{l},\mathcal{T}_{g},\mathcal{T}_{o})}}$ (Fig., top); and readout heads $R{(e)}$ that produce the desired outputs, i.e., actions $a$.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Task and observation tokenizers", "weight": 1.0} -->

We convert task definitions (e.g., language instructions $\ell$ and goal images $g$) and observations $o$ (e.g., wrist and third-person camera streams) into a common "tokenized" format using modality-specific tokenizers (see Fig., left): Language inputs are tokenized, then passed through a pretrained transformer that produces a sequence of language embedding tokens. We use the t5-base (111M) model.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Task and observation tokenizers", "weight": 1.0} -->

Image observations and goals are passed through a shallow convolution stack, then split into a sequence of flattened patches.

<!-- chunk {"id": "body-0014", "role": "body", "section": "Task and observation tokenizers", "weight": 1.0} -->

We assemble the input sequence of the transformer by adding learnable position embeddings $p$ to task and observation tokens and then arranging them sequentially $\left\lbrack \mathcal{T}_{T},\mathcal{T}_{o,1},\mathcal{T}_{o,2},\ldots \right\rbrack$.

<!-- chunk {"id": "body-0015", "role": "body", "section": "Transformer backbone and readout heads", "weight": 1.0} -->

Once the inputs have been cast to a unified token sequence, they are processed by a transformer (see Fig., top). This is similar to prior works that train transformer-based policies on sequences of observations and actions. The attention pattern of the Octo transformer is block-wise masked: observation tokens can only attend causally to tokens from the same or earlier time steps $\mathcal{T}_{{o,0}:t}$ as well as task tokens $\mathcal{T}_{T}$ (green). Tokens corresponding to non-existing observations are fully masked out (e.g., a dataset without language instructions). This modular design enables us to add and remove observations or tasks during finetuning (see below). In addition to these input token blocks, we insert learned *readout tokens* $\mathcal{T}_{R,t}$ (purple).

<!-- chunk {"id": "body-0016", "role": "body", "section": "Transformer backbone and readout heads", "weight": 1.0} -->

A readout token at $\mathcal{T}_{R,t}$ attends to observation and task tokens before it in the sequence, but is not attended to by any observation or task token --- hence, they can only passively read and process internal embeddings without influencing them. Readout tokens act similarly to the \[CLS\] token in BERT, serving as a compact vector embedding of the observation sequence thus far. A lightweight "action head" that implements the diffusion process is applied to the embeddings for the readout tokens. This action head predicts a "chunk\" of several consecutive actions, similar to prior work.

<!-- chunk {"id": "body-0017", "role": "body", "section": "Transformer backbone and readout heads", "weight": 1.0} -->

Our design allows us to flexibly add new task and observation inputs or action output heads to the model during downstream finetuning. When adding new tasks, observations, or loss functions downstream, we can wholly retain the pretrained weights for the transformer, only adding new positional embeddings, a new lightweight encoder, or the parameters of the new head as necessitated by the change in specification (see Fig., bottom). This is in contrast to prior architectures, where adding or removing an image input or changing the task specification would require re-initializing or re-training large components of the pre-trained model.

<!-- chunk {"id": "body-0018", "role": "body", "section": "Transformer backbone and readout heads", "weight": 1.0} -->

This flexibility is crucial to make Octo a truly "generalist" model: since we cannot cover all possible robot sensor and action configurations during pretraining, being able to adapt Octo's inputs and outputs during finetuning makes it a versatile tool for the robotics community. Prior model designs that use standard transformer backbones or fuse visual encoders with MLP output heads lock in the type and order of inputs expected by the model. In contrast, switching the observation or task for Octo *does not* require re-initializing most of the model.

<!-- chunk {"id": "body-0019", "role": "body", "section": "III-B Training data", "weight": 1.0} -->

We train Octo on a mixture of 25 datasets from the Open X-Embodiment Dataset, a diverse collection of robot learning datasets. Our training mixture includes demonstration data of a variety of tasks from several robot embodiments and scenes. These datasets are heterogeneous not just in terms of the robot type, but also in the sensors (e.g., including or not including wrist cameras) and labels (e.g., including or not including language instructions). See Fig. 1 and Appendix C for the detailed mixture. To create our training mixture $D$, we curate the data by first removing all Open-X datasets that contain no image streams, as well as those that do not use delta end-effector control. We also remove datasets that are too repetitive, have a low image resolution, or consist of excessively niche tasks. For the remaining datasets, we roughly categorize them into "more diverse" and "less diverse" datasets based on the tasks and environments, and then double the weight of the more diverse datasets during training.

<!-- chunk {"id": "body-0020", "role": "body", "section": "III-B Training data", "weight": 1.0} -->

We also down-weight a few datasets with many repetitive episodes to avoid dominating the mixture. Finally, we zero-pad any missing camera channels and align the gripper action spaces between the datasets such that a gripper command of +1 means "the gripper is open" and 0 means "the gripper is closed." While we found the resulting training mixture to work well, future work should perform a more thorough analysis of data mixture quality for pretraining general robot policies.

<!-- chunk {"id": "body-0021", "role": "body", "section": "III-C Training objective", "weight": 1.0} -->

We use a conditional diffusion decoding head to predict continuous, multi-modal action distributions. Importantly, only one forward pass of the transformer backbone is performed per action prediction, after which the multi-step denoising process is carried out entirely within the small diffusion head. We found this policy parameterization to outperform policies trained with MSE action heads or discretized action distributions in both zero-shot and finetuning evaluations. To generate an action, we sample a Gaussian noise vector $x^{K} \sim {\mathcal{N}(0,I)}$ and apply $K$ steps of denoising with a learned denoising network $\epsilon_{\theta}{(x^{k},e,k)}$ that is conditioned on the output $x^{k}$ of the previous denoising step, the step index $k$, and the output embedding $e$ of the transformer action readout: The hyperparameters $\alpha$, $\gamma$, and $\sigma$ correspond to the noise schedule: we use the standard cosine schedule.

<!-- chunk {"id": "body-0022", "role": "body", "section": "III-C Training objective", "weight": 1.0} -->

We train the diffusion head using the standard DDPM objective first proposed, where we add Gaussian noise to the dataset actions and train the denoising network $\epsilon_{\theta}{(x^{k},e,k)}$ to reconstruct the original action. For a detailed explanation of diffusion policy training, see Chi et al.. We list all hyperparameters in Appendix D.

<!-- chunk {"id": "body-0023", "role": "body", "section": "III-C Training objective", "weight": 1.0} -->

We use the same diffusion training objective during finetuning and update the full model, a recipe which outperformed those that freeze subsets of the pretrained parameters. In all finetuning experiments, we employ the same recipe: given a small target domain dataset with around 100 trajectories, we finetune for 50k steps using a cosine decay learning rate decay with linear warmup.

<!-- chunk {"id": "body-0024", "role": "body", "section": "III-D Training Details", "weight": 1.0} -->

We trained two variants of our model: Octo-Small with a transformer backbone that mirrors the size of a ViT-S, and Octo-Base with a transformer backbone that mirrors the size of a ViT-B.

<!-- chunk {"id": "body-0025", "role": "body", "section": "III-D Training Details", "weight": 1.0} -->

We use the AdamW optimizer with an inverse square root decay learning rate schedule, with weight decay of 0.1 and gradient clipping of 1.0. The ViT-B was trained for 300k steps with a batch size of $2048$ using a TPU v4-128 pod, which took 14 hours. A finetuning run of the same model on a single NVIDIA A5000 GPU with 24GB of VRAM takes approximately 5 hours and can be sped up with multi-GPU training.

<!-- chunk {"id": "body-0026", "role": "body", "section": "III-D Training Details", "weight": 1.0} -->

We train using 2 frames of observation history; in our preliminary experiments, we found significantly diminishing gains beyond the first additional frame. We use hindsight goal relabeling, which selects a state uniformly from the future in the trajectory to assign as the goal image, similar to prior work. We apply common image data augmentations during training, and randomly zero out the language instruction or goal image per training example to enable Octo to be conditioned on *either* language instructions *or* goal images. For datasets without language annotations, we always use goal image conditioning. This enables our model to learn control mostly from self-supervised visual observations and reduces the burden on language annotation, similar to prior work on multi-context imitation learning. For more details on the choice of hyperparameters, see Appendix D.

<!-- chunk {"id": "body-0027", "role": "body", "section": "III-E Model Checkpoints & Code", "weight": 1.0} -->

We open-source all resources required to train, finetune and run our model: Pretrained Octo checkpoints for Octo-Small (27M params) and Octo-Base (93M params).

<!-- chunk {"id": "body-0028", "role": "body", "section": "III-E Model Checkpoints & Code", "weight": 1.0} -->

Finetuning scripts for Octo models, in JAX.

<!-- chunk {"id": "body-0029", "role": "body", "section": "III-E Model Checkpoints & Code", "weight": 1.0} -->

Model pretraining pipeline for Octo pretraining on the Open X-Embodiment dataset, in JAX.

<!-- chunk {"id": "body-0030", "role": "body", "section": "III-E Model Checkpoints & Code", "weight": 1.0} -->

Standalone data loaders for Open X-Embodiment data, compatible with JAX and PyTorch.

<!-- chunk {"id": "body-0031", "role": "body", "section": "III-E Model Checkpoints & Code", "weight": 1.0} -->

We provide a simple example for loading and running a pretrained Octo model in Appendix B.

<!-- chunk {"id": "body-0032", "role": "body", "section": "Experiments", "weight": 1.0} -->

Our experiments provide an empirical analysis of Octo, evaluating its ability to serve as a general robotic foundation model across several axes: Can Octo control multiple robot embodiments and solve language and goal tasks out of the box?

<!-- chunk {"id": "body-0033", "role": "body", "section": "Experiments", "weight": 1.0} -->

Do Octo weights serve as a good initialization for data-efficient finetuning to new tasks and robots, and does it improve over training from scratch and commonly used pretrained representations?

<!-- chunk {"id": "body-0034", "role": "body", "section": "Experiments", "weight": 1.0} -->

Which design decisions in Octo matter most for building generalist robot policies?

<!-- chunk {"id": "body-0035", "role": "body", "section": "Evaluation setups", "weight": 1.0} -->

We evaluate Octo's capabilities across a representative spectrum of 9 robot learning setups at 4 institutions (see Fig. 2). We test Octo's ability to control different robots out-of-the-box ("zero-shot") for language and goal image tasks using robot setups that match the pretraining data, where all robots are controlled with delta end-effector control actions and the observation spaces are RGB images. We also evaluate Octo for data-efficient finetuning to new environments and tasks, including with new observations (force-torque inputs in "Berkeley Insertion"), new action spaces (joint position control in "Berkeley Pick-Up") and new robot embodiments ("Berkeley Coke" and "Berkeley Bimanual"). Each of the finetuning setups uses $\sim 100$ in-domain demonstrations and finetunes in $< 5$ hours on a NVIDIA A5000 GPU, using the same hyperparameters across all setups (see Appendix D).

<!-- chunk {"id": "body-0036", "role": "body", "section": "Evaluation setups", "weight": 1.0} -->

Our evaluation tasks test Octo's ability to interact with diverse objects (e.g., "WidowX BridgeV2"), solve long-horizon tasks (e.g., "Stanford Coffee") and perform precise manipulation (e.g., "Berkeley Insertion"). For more details on each evaluation setup, see Appendix F.

<!-- chunk {"id": "body-0037", "role": "body", "section": "Comparisons", "weight": 1.0} -->

We compare Octo's ability to control multiple robots out-of-the-box to the best openly available generalist robot policy, RT-1-X, using the released checkpoint. Similar to Octo, RT-1-X is pretrained on the Open X-Embodiment robot dataset and aims to control multiple robots zero-shot, thus providing a natural point of comparison. We also compare the zero-shot capabilities of Octo to RT-2-X, a 55 billion parameter vision-language model finetuned on the Open X-Embodiment dataset to produce robot actions. The RT-1-X and RT-2-X models are trained on a more restricted subset of 350K episodes (compared to 800k episodes for Octo). We further compare Octo's performance as a policy initialization for data efficient finetuning to two common approaches: training on the target domain demonstrations *from scratch* and using pretrained visual representations. While a number of prior works have proposed other pretraining schemes for imitation finetuning, to our knowledge no prior method provides a pretrained *policy* that has been demonstrated to finetune successfully to *new* observation and action spaces.

<!-- chunk {"id": "body-0038", "role": "body", "section": "Comparisons", "weight": 1.0} -->

However, pretrained visual representations such as VC-1 have been used in this way, and therefore we use these methods as another point of comparison.

<!-- chunk {"id": "body-0039", "role": "body", "section": "Comparisons", "weight": 1.0} -->

For finetuning, we found that training our large transformer architecture from scratch overfit quickly on the small datasets. Instead, we obtained better from-scratch results using a canonical policy architecture employed by many prior works: a ResNet visual encoder with FiLM language conditioning, combined with a small transformer action decoder trained with a diffusion objective, similar to. Our instantiation of this architecture has 28M parameters (similar to RT-1 ). We adopt this as our from-scratch baseline ("ResNet+Transformer Scratch"). We also compare to a pretrained visual representation following the procedure of Majumdar et al.. A ViT-B visual encoder is initialized to the VC-1 weights, a state-of-the-art visual representation pretrained on 4,000 hours of ego-centric videos and ImageNet, and combined with an MLP action decoder. The full model is trained to predict expert actions using an MSE loss ("VC-1").

<!-- chunk {"id": "body-0040", "role": "body", "section": "IV-A Octo Controls Multiple Robots Out-of-the-Box", "weight": 1.0} -->

ResNet+Transformer Scratch TABLE I: Finetuning Evaluation. Octo enables data-efficient finetuning to new domains and out-performs training from scratch as well as state-of-the-art pretrained visual representations. Each domain uses ∼ 100 target demonstrations and the same finetuning hyperparameters. In each domain, success rates are averaged over 20 trials. *: New observation input (force-torque proprioception). †: New action space (joint position control).

<!-- chunk {"id": "body-0041", "role": "body", "section": "IV-A Octo Controls Multiple Robots Out-of-the-Box", "weight": 1.0} -->

We compare the zero-shot manipulation capabilities of Octo, RT-1-X, and RT-2-X in Fig. 3. We evaluated on several tasks selected from the pre-training dataset including picking and placing, wiping a table with a cloth, and opening and closing drawers. For each robot, we selected two language tasks from the corresponding OXE dataset and performed 10 trials per task with varying initial conditions (details in Appendix F). The chosen tasks are "in-distribution" from the pre-training data, but the evaluation requires methods to generalize to new object positions, lighting conditions, backgrounds, and distractor objects. While all methods acted reasonably across tasks in the pretraining environments, we found that on average Octo had a 29% higher success rate than RT-1-X (35M parameters). For the WidowX and RT-1 Robot evaluations, we also compared to RT-2-X (55 billion parameters) and found that Octo performed similarly.

<!-- chunk {"id": "body-0042", "role": "body", "section": "IV-A Octo Controls Multiple Robots Out-of-the-Box", "weight": 1.0} -->

Additionally, while RT-1-X and RT-2-X only support conditioning on language instructions, Octo also supports conditioning on goal images. We evaluated our model on the WidowX tasks using goal image conditioning and found that it achieved a 25% higher success rate than when evaluated with language conditioning. This is likely because goal images provide more information about how to achieve the task. In the BridgeV2 domain, we performed a fine-grained analysis of the zero-shot capabilities in Table VII; measuring performance on setups seen in the dataset, and for novel environments, scenes, and skills. While the Octo model achieves high success on novel objects, zero-shot performance slightly degrades in a new scene, and high degradation for novel behaviors like flipping or precise insertion.

<!-- chunk {"id": "body-0043", "role": "body", "section": "IV-B Octo Enables Data-Efficient Learning in New Domains", "weight": 1.0} -->

We report data-efficient finetuning results to new domains in Table I. We find that finetuning Octo leads to better policies than starting from scratch or with the pretrained VC-1 weights. On average across the six evaluation setups (detailed in Appendix F), Octo outperforms the next best baseline by 52%. Importantly, we use the same recipe and hyperparameters for fine-tuning Octo on all evaluation tasks (see Section III-C), making this a good default configuration.

<!-- chunk {"id": "body-0044", "role": "body", "section": "IV-B Octo Enables Data-Efficient Learning in New Domains", "weight": 1.0} -->

The results also underline Octo's ability to accommodate new observations (force-torque inputs for "Berkeley Insertion"), action spaces (joint position control for "Berkeley Pick-Up") and new robot embodiments ("Berkeley Coke" and "Berkeley Bimanual"). This makes Octo applicable to a wide range of single and dual arm robotic manipulation problems that go beyond a single camera input and end-effector position control.

<!-- chunk {"id": "body-0045", "role": "body", "section": "IV-C Design Decisions for Generalist Robot Policy Training", "weight": 1.0} -->

We have demonstrated the effectiveness of Octo as a zero-shot multi-robot controller and as an initialization for policy finetuning. We next analyze the effects of different design decisions on the performance of the Octo policy. Concretely, we focus on the following aspects: model architecture, training data, training objective, and model scale. Unless noted otherwise, we perform all ablations on the Octo-Small model due to our compute budget.

<!-- chunk {"id": "body-0046", "role": "body", "section": "IV-C Design Decisions for Generalist Robot Policy Training", "weight": 1.0} -->

RT-X dataset mix Single robot dataset (Bridge Data) Discretized Action Prediction Continuous Action Prediction (MSE) TABLE II: Model Ablations. We achieve best performance when using the ViT architecture, diffusion action head, and wide training data mixture. All evaluations are performed on the WidowX setup. Success rates are averaged over 40 trials across two language-conditioned tasks and two goal-conditioned tasks.

<!-- chunk {"id": "body-0047", "role": "body", "section": "Model architecture", "weight": 1.0} -->

Prior transformer-based policy designs typically encode input images with large ResNet-style encoders and fuse the resulting image features with a comparatively small transformer. Instead, we opt for a "transformer-first" architecture that uses very shallow CNN patch encoders and concentrates most of the parameters and FLOPS in the transformer backbone, similar to canonical vision transformer architectures. In Table II we show that this scalable architecture leads to substantially improved performance when training on the full Open X-Embodiment data mix. Importantly, we found ResNet-based architectures to perform better than ViTs when training on small datasets, e.g., in our "from scratch" comparisons, underlining that large transformer policies are uniquely suited for scalable training on diverse datasets.

<!-- chunk {"id": "body-0048", "role": "body", "section": "Training data", "weight": 1.0} -->

Octo is trained on the most diverse cross-embodied robot dataset to date, a mix of 25 datasets that we manually curated from the Open X-Embodiment dataset (see Section III-B). We ablate the impact of this training mix by comparing to Octo models trained on a smaller mix of 11 datasets used in training the RT-X models and a baseline trained only on data from the target robot domain. In Table II we show that the performance of Octo increases as we increase the number of training datasets. This suggests that expanding the data mix to even more datasets may further improve policy performance. We will leave this for future work, along with a more thorough investigation of best practices for data curation.

<!-- chunk {"id": "body-0049", "role": "body", "section": "Training objective", "weight": 1.0} -->

We compare Octo's diffusion decoding training objective (see Section III-C) to common alternatives from prior work: simple MSE loss and cross-entropy loss on discretized actions. In Table II we find that Octo's diffusion training objective leads to substantially improved performance. This improvement is likely because the diffusion head can model multi-modal action distributions (unlike the MSE head) while retaining the precision of continuous actions (unlike the discrete head). Qualitatively, the policy acts more decisively than MSE-trained policies, and more precisely than those trained with discretized actions.

<!-- chunk {"id": "body-0050", "role": "body", "section": "Model scale", "weight": 1.0} -->

We compare Octo models of three different sizes following the ladder of common vision transformer models: Octo-Tiny (10M), Octo-Small (27M), and Octo-Base (93M). In Figure 4 we show that the zero-shot performance of the policy scales with increasing model size. We find that the Base model is more robust to initial scene configuration than the Small model, and is less prone to early grasp attempts, indicating the larger model has better visual scene perception.

<!-- chunk {"id": "body-0051", "role": "body", "section": "Discussion and Future Work", "weight": 1.5} -->

We introduced Octo, a large transformer-based policy pretrained on the largest robot manipulation dataset to date, 800k robot trajectories. We demonstrated that Octo can solve a variety of tasks out-of-the-box and showed how Octo's compositional design enables finetuning to new inputs and action spaces, making Octo a versatile initialization for a wide range of robotic control problems. Apart from the model itself, we have released our full training and finetuning code, alongside tools that make it easier to train on large robot datasets.

<!-- chunk {"id": "body-0052", "role": "body", "section": "Discussion and Future Work", "weight": 1.5} -->

While Octo achieves strong performance in both zero-shot and finetuning evaluations, we find that the current model still has several short-comings, which we attribute in large parts to characteristics of the training data. First, we found that the current Octo model struggles with adequately processing wrist camera information. Often finetuning results were stronger when using only a third person camera instead of combining third person and wrist camera. Additionally, we notice a large difference between language-conditioned policy performance and goal-conditioned policy performance. In both cases, a lack of the respective modalities in the training data is the likely reason: only 27% of the data contains wrist camera information and only 56% of the pretraining data contains language annotations.

<!-- chunk {"id": "body-0053", "role": "body", "section": "Discussion and Future Work", "weight": 1.5} -->

Expanding the data used to train Octo is a natural avenue of improvement. Since the Open X-Embodiment dataset is comprised of optimal robot demonstrations, the current model trains via imitation; future work may consider learning from sub-optimal or online interaction data that require alternative objectives. Further, while we trained and evaluated Octo exclusively on single and dual-arm manipulators; expanding to a wider set of robots that perform navigation or mobile manipulation would be an direction of high opportunity.

<!-- chunk {"id": "body-0054", "role": "body", "section": "Discussion and Future Work", "weight": 1.5} -->

While Octo represents a step towards building generalist robot policies that work out-of-the-box on diverse robot setups, there remains work to improve the model, including better language conditioning, improved support for wrist cameras, and incorporating data beyond optimal demonstrations. We hope that Octo offers a simple launchpad for researchers and practitioners to access larger robotic datasets and leverage pretrained robotics models for efficient learning of new tasks and broad generalization.
