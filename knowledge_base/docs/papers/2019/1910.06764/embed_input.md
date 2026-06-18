<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Stabilizing Transformers for Reinforcement Learning

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Owing to their ability to both effectively integrate information over long time horizons and scale to massive amounts of data, self-attention architectures have recently shown breakthrough success in natural language processing (NLP), achieving state-of-the-art results in domains such as language modeling and machine translation. Harnessing the transformer's ability to process long time horizons of information could provide a similar performance boost in partially observable reinforcement learning (RL) domains, but the large-scale transformers used in NLP have yet to be successfully applied to the RL setting. In this work we demonstrate that the standard transformer architecture is difficult to optimize, which was previously observed in the supervised learning setting but becomes especially pronounced with RL objectives. We propose architectural modifications that substantially improve the stability and learning speed of the original Transformer and XL variant. The proposed architecture, the Gated Transformer-XL (GTrXL), surpasses LSTMs on challenging memory environments and achieves state-of-the-art results on the multi-task DMLab-30 benchmark suite, exceeding the performance of an external memory architecture.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

We show that the GTrXL, trained using the same losses, has stability and performance that consistently matches or exceeds a competitive LSTM baseline, including on more reactive tasks where memory is less critical. GTrXL offers an easy-to-train, simple-to-implement but substantially more expressive architectural alternative to the standard multi-layer LSTM ubiquitously used for RL agents in partially observable environments.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

It has been argued that self-attention architectures deal better with longer temporal horizons than recurrent neural networks (RNNs): by construction, they avoid compressing the whole past into a fixed-size hidden state and they do not suffer from vanishing or exploding gradients in the same way as RNNs. Recent work has empirically validated these claims, demonstrating that self-attention architectures can provide significant gains in performance over the more traditional recurrent architectures such as the LSTM. In particular, the Transformer architecture has had breakthrough success in a wide variety of domains: language modeling, machine translation, summarization (Liu & Lapata, ), question answering, multi-task representation learning for NLP, and algorithmic tasks.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

The repeated success of the transformer architecture in domains where sequential information processing is critical to performance makes it an ideal candidate for partially observable RL problems, where episodes can extend to thousands of steps and the critical observations for any decision often span the entire episode. Yet, the RL literature is dominated by the use of LSTMs as the main mechanism for providing memory to the agent. Despite progress at designing more expressive memory architectures that perform better than LSTMs in memory-based tasks and partially-observable environments, they have not seen widespread adoption in RL agents perhaps due to their complex implementation, with the LSTM being seen as the go-to solution for environments where memory is required. In contrast to these other memory architectures, the transformer is well-tested in many challenging domains and has seen several open-source implementations in a variety of deep learning frameworks ^11^1e.g.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

Motivated by the transformer's superior performance over LSTMs and the widespread availability of implementations, in this work we investigate the transformer architecture in the RL setting. In particular, we find that the canonical transformer is significantly difficult to optimize, often resulting in performance comparable to a random policy. This difficulty in training transformers exists in the supervised case as well. Typically a complex learning rate schedule is required (e.g., linear warmup or cosine decay) in order to train, or specialized weight initialization schemes are used to improve performance. These measures do not seem to be sufficient for RL. In Mishra et al., for example, transformers could not solve even simple bandit tasks and tabular Markov Decision Processes (MDPs), leading the authors to hypothesize that the transformer architecture was not suitable for processing sequential information.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

However in this work we succeed in stabilizing training with a reordering of the layer normalization coupled with the addition of a new gating mechanism to key points in the submodules of the transformer. Our novel gated architecture, the Gated Transformer-XL (GTrXL) (shown in Figure 1, Right), is able to learn much faster and more reliably and exhibit significantly better final performance than the canonical transformer. We further demonstrate that the GTrXL achieves state-of-the-art results when compared to the external memory architecture MERLIN on the multitask DMLab-30 suite. Additionally, we surpass LSTMs significantly on memory-based DMLab-30 levels while matching performance on the reactive set, as well as significantly outperforming LSTMs on memory-based continuous control and navigation environments. We perform extensive ablations on the GTrXL in challenging environments with both continuous actions and high-dimensional observations, testing the final performance of the various components as well as the GTrXL's robustness to seed and hyperparameter sensitivity compared to LSTMs and the canonical transformer.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Introduction", "weight": 1.5} -->

We demonstrate a consistent superior performance while matching the stability of LSTMs, providing evidence that the GTrXL architecture can function as a drop-in replacement to the LSTM networks ubiquitously used in RL.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Transformer Architecture and Variants", "weight": 1.0} -->

The transformer network consists of several stacked blocks that repeatedly apply self-attention to the input sequence. The transformer layer block itself has remained relatively constant since its original introduction. Each layer consists of two submodules: an attention operation followed by a position-wise multi-layer network (see Figure 1 (left)). The input to the transformer block is an embedding from the previous layer $E^{({l - 1})} \in {\mathbb{R}}^{T \times D}$, where $T$ is the number of time steps, $D$ is the hidden dimension, and $l \in {\lbrack 0,L\rbrack}$ is the layer index with $L$ being the total number of layers. We assume $E^{}$ is an arbitrarily-obtained input embedding of dimension $\lbrack T,D\rbrack$, e.g. a word embedding in the case of language modeling or an embedding of the per-timestep observations in an RL environment.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Transformer Architecture and Variants", "weight": 1.0} -->

Multi-Head Attention: The Multi-Head Attention (MHA) submodule computes in parallel $H$ soft-attention operations for every time step.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Transformer Architecture and Variants", "weight": 1.0} -->

Multi-Layer Perceptron: The Multi-Layer Perceptron (MLP) submodule applies a $1 \times 1$ temporal convolutional network $f^{(l)}$ (i.e., kernel size 1, stride 1) over every step in the sequence, producing a new embedding tensor $E^{(l)} \in {\mathbb{R}}^{T \times D}$. As in Dai et al., the network output does not include an activation function.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Transformer Architecture and Variants", "weight": 1.0} -->

Relative Position Encodings: The basic MHA operation does not take sequence order into account explicitly because it is permutation invariant. Positional encodings are a widely used solution in domains like language where order is an important semantic cue, appearing in the original transformer architecture. To enable a much larger contextual horizon than would otherwise be possible, we use the relative position encodings and memory scheme used in Dai et al.. In this setting, there is an additional $\mathcal{T}$-step memory tensor $M^{(l)} \in {\mathbb{R}}^{\mathcal{T} \times D}$, which is treated as constant during weight updates.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Transformer Architecture and Variants", "weight": 1.0} -->

where StopGrad is a stop-gradient function that prevents gradients flowing backwards during backpropagation. We refer to Appendix C for a more detailed description.

<!-- chunk {"id": "body-0014", "role": "body", "section": "Gated Transformer Architectures", "weight": 1.0} -->

While the transformer architecture has achieved breakthrough results in modeling sequences for supervised learning tasks, a demonstration of the transformer as a useful RL memory has been notably absent. Previous work has highlighted training difficulties and poor performance. When transformers have not been used for temporal memory but instead as a mechanism for attention over the input space, they have had success---notably in the challenging multi-agent Starcraft 2 environment. Here, the transformer was applied solely across Starcraft units and not over time.

<!-- chunk {"id": "body-0015", "role": "body", "section": "Gated Transformer Architectures", "weight": 1.0} -->

Multiplicative interactions have been successful at stabilizing learning across a wide variety of architectures. Motivated by this, we propose the introduction of powerful gating mechanisms in place of the residual connections within the transformer block, coupled with changes to the order of layer normalization in the submodules. As will be empirically demonstrated, the "Identity Map Reordering" and gating mechanisms are critical for stabilizing learning and improving performance.

<!-- chunk {"id": "body-0016", "role": "body", "section": "Identity Map Reordering", "weight": 1.0} -->

Our first change is to place the layer normalization on only the input stream of the submodules, a modification described in several previous works. The model using this *Identity Map Reordering* is termed TrXL-I in the following, and is depicted visually in Figure 1 (center). A key benefit to this reordering is that it now enables an identity map from the input of the transformer at the first layer to the output of the transformer after the last layer. This is in contrast to the canonical transformer, where there are a series of layer normalization operations that non-linearly transform the state encoding. Because the layer norm reordering causes a path where two linear layers are applied in sequence, we apply a ReLU activation to each sub-module output before the residual connection (see Appendix C for equations).

<!-- chunk {"id": "body-0017", "role": "body", "section": "Identity Map Reordering", "weight": 1.0} -->

The TrXL-I already exhibits a large improvement in stability and performance over TrXL (see Section 4.3.1). One hypothesis as to why the Identity Map Reordering improves results is as follows: assuming that the submodules at initialization produce values that are in expectation near zero, the state encoding is passed un-transformed to the policy and value heads, enabling the agent to learn a Markovian policy at the start of training (i.e., the network is initialized such that $\pi{( \cdot |s_{t},\ldots,s_{1})} \approx \pi{( \cdot |s_{t})}$ and ${V^{\pi}{(\left. s_{t} \middle| {s_{t - 1},\ldots,s_{1}} \right.)}} \approx {V^{\pi}{(\left. s_{t} \middle| s_{t - 1} \right.)}}$).

<!-- chunk {"id": "body-0018", "role": "body", "section": "Identity Map Reordering", "weight": 1.0} -->

In many environments, reactive behaviours need to be learned before memory-based ones can be effectively utilized, i.e., an agent needs to learn how to walk before it can learn how to remember where it has walked.

<!-- chunk {"id": "body-0019", "role": "body", "section": "Gating Layers", "weight": 1.0} -->

We further improve performance and optimization stability by replacing the residual connections in Equations 4 and 2 with gating layers. We call the gated architecture with the identity map reordering the *Gated Transformer(-XL)* (GTrXL).

<!-- chunk {"id": "body-0020", "role": "body", "section": "Gating Layers", "weight": 1.0} -->

where $g$ is a gating layer function. A visualization of our final architecture is shown in Figure 1 (right), with the modifications from the canonical transformer highlighted in red.

<!-- chunk {"id": "body-0021", "role": "body", "section": "Gating Layers", "weight": 1.0} -->

Input: The gated input connection has a sigmoid modulation on the input stream, similar to the short-cut-only gating from He et al.:

<!-- chunk {"id": "body-0022", "role": "body", "section": "Gating Layers", "weight": 1.0} -->

Gated-Recurrent-Unit-type gating: The Gated Recurrent Unit (GRU) is a recurrent network that performs similarly to an LSTM but has fewer parameters.

<!-- chunk {"id": "body-0023", "role": "body", "section": "Gating Layers", "weight": 1.0} -->

Gated Identity Initialization: We have claimed that the Identity Map Reordering aids policy optimization because it initializes the agent close to a Markovian policy / value function. If this is indeed the cause of improved stability, we can explicitly initialize the various gating mechanisms to be close to the identity map. This is the purpose of the bias $b_{g}^{(l)}$ in the applicable gating layers. We later demonstrate in an ablation that initially setting $b_{g}^{(l)} > 0$ can greatly improve learning speed.

<!-- chunk {"id": "body-0024", "role": "body", "section": "Experiments", "weight": 1.0} -->

In this section, we provide experiments on a variety of challenging single and multi-task RL domains: DMLab-30, Numpad and Memory Maze (see Fig. 8). Crucially we demonstrate that the proposed Gated Transformer-XL (GTrXL) not only shows substantial improvements over LSTMs on memory-based environments, but suffers no degradation of performance on reactive environments. The GTrXL also exceeds MERLIN, an external memory architecture which used a Differentiable Neural Computer coupled with auxiliary losses, surpassing its performance on both memory and reactive tasks.

<!-- chunk {"id": "body-0025", "role": "body", "section": "Experiments", "weight": 1.0} -->

For all transformer architectures except when otherwise stated, we train relatively deep 12-layer networks with embedding size 256 and memory size 512. These networks are comparable to the state-of-the-art networks in use for small language modeling datasets (see enwik8 results in ). We chose to train deep networks in order to demonstrate that our results do not necessarily sacrifice complexity for stability, i.e. we are not making transformers stable for RL simply by making them shallow. Our networks have receptive fields that can potentially span any episode in the environments tested, with an upper bound on the receptive field of 6144 (${{12\text{layers}} \times 512}\text{~memory}$ ). Future work will look at scaling transformers in RL even further, e.g. towards the 52-layer network in Radford et al.. See App. B for experimental details.

<!-- chunk {"id": "body-0026", "role": "body", "section": "Experiments", "weight": 1.0} -->

For all experiments, we used V-MPO, an on-policy adaptation of Maximum a Posteriori Policy Optimization (MPO) that performs approximate policy iteration based on a learned state-value function $V{(s)}$ instead of the state-action value function used in MPO. Rather than directly updating the parameters in the direction of the policy gradient, V-MPO uses the estimated advantages to first construct a target distribution for the policy update subject to a sample-based KL constraint, then calculates the gradient that partially moves the parameters toward that target, again subject to a KL constraint. V-MPO was shown to achieve state-of-the-art results for LSTM-based agents on the multi-task DMLab-30 benchmark suite.

<!-- chunk {"id": "body-0027", "role": "body", "section": "Transformer as Effective RL Memory Architecture", "weight": 1.0} -->

We first present results of the best performing GTrXL variant, the GRU-type gating, against a competitive LSTM baseline, demonstrating a substantial improvement on the multi-task DMLab-30 domain. Figure 2 shows mean return over all levels as training progresses, where the return is human normalized as done in previous work (meaning a human has a per-level mean score of 100 and a random policy has a score of 0), while Table 1 has the final performance at 10 billion environment steps. The GTrXL has a significant gap over a 3-layer LSTM baseline trained using the same V-MPO algorithm. Furthermore, we included the final results of a previously-published external memory architecture, MERLIN. Because MERLIN was trained for 100 billion environment steps with a different algorithm, IMPALA, and also involved an auxiliary loss critical for the memory component to function, the learning curves are not directly comparable and we only report the final performance of the architecture as a dotted line. Despite the differences, our results demonstrate that the GTrXL can match the state-of-the-art on DMLab-30.

<!-- chunk {"id": "body-0028", "role": "body", "section": "Transformer as Effective RL Memory Architecture", "weight": 1.0} -->

An informative split between a set of memory-based levels and more reactive ones (listed in Appendix D) reveals that our model specifically has large improvements in environments where memory plays a critical role. Meanwhile, GTrXL also shows improvement over LSTMs on the set of reactive levels, as memory can still be effectively utilized in some of these levels.

<!-- chunk {"id": "body-0029", "role": "body", "section": "Scaling with Memory Horizon", "weight": 1.0} -->

We next demonstrate that the GTrXL scales better compared to an LSTM when an environment's temporal horizon is increased, using the "Numpad" continuous control task of Humplik et al. which allows an easy combinatorial increase in the temporal horizon. In Numpad, a robotic agent is situated on a platform resembling the 3x3 number pad of a telephone (generalizable to $N \times N$ pads). The agent can interact with the pads by colliding with them, causing them to be activated (visualized in the environment state as the number pad glowing). The goal of the agent is to activate a specific sequence of up to $N^{2}$ numbers, but without knowing this sequence a priori. The only feedback the agent gets is by activating numbers: if the pad is the next one in the sequence, the agent gains a reward of +1, otherwise all activated pads are cleared and the agent must restart the sequence. Each correct number in the sequence only provides reward once, i.e. each subsequent activation of that number will no longer provide rewards. Therefore the agent must explicitly develop a search strategy to determine the correct pad sequence.

<!-- chunk {"id": "body-0030", "role": "body", "section": "Scaling with Memory Horizon", "weight": 1.0} -->

Once the agent completes the full sequence, all pads are reset and the agent gets a chance to repeat the sequence again for more reward. This means higher reward directly translates into how well the pad sequence has been memorized. An image of the scenario is provided in Figure 3. There is the restriction that contiguous pads in the sequence must be contiguous in space, i.e. the next pad in the sequence can only be in the Moore neighborhood of the previous pad. Furthermore, no pad can be pressed twice in the sequence.

<!-- chunk {"id": "body-0031", "role": "body", "section": "Scaling with Memory Horizon", "weight": 1.0} -->

We present two results in this environment in Figure 3. The first measures the final performance of the trained models as a function of the pad size. We can see that LSTM performs badly on all 3 pad sizes, and performs worse as the pad size increases from 2 to 4. The GTrXL performs much better, and almost instantly solves the environment with its much more expressive memory. On the center and right images, we provide learning curves for the $2 \times 2$ and $4 \times 4$ Numpad environments, and show that even when the LSTM is trained twice as long it does not reach GTrXL's performance.

<!-- chunk {"id": "body-0032", "role": "body", "section": "Scaling with Memory Horizon", "weight": 1.0} -->

Mean Human Norm.
Mean Human Norm., 100-capped

<!-- chunk {"id": "body-0033", "role": "body", "section": "Gating Variants + Identity Map Reordering", "weight": 1.0} -->

We demonstrated that the GRU-type-gated GTrXL can achieve state-of-the-art results on DMLab-30, surpassing both a deep LSTM and an external memory architecture, and also that the GTrXL has a memory which scales better with the memory horizon of the environment. However, the question remains whether the expressive gating mechanisms of the GRU could be replaced by simpler alternatives. In this section, we perform extensive ablations on the gating variants described in Section 3.2, and show that the GTrXL (GRU) has improvements in learning speed, final performance and optimization stability over all other models, even when controlling for the number of parameters.

<!-- chunk {"id": "body-0034", "role": "body", "section": "Performance Ablation", "weight": 1.0} -->

We first report the performance of the gating variants in DMLab-30. Table 1 and Figure 4 show the final performance and training curves of the various gating types in both the memory / reactive split, respectively. The canonical TrXL completely fails to learn, while the TrXL-I improves over the LSTM. Of the gating varieties, the GTrXL (Output) can recover a large amount of the performance of the GTrXL (GRU), especially in the reactive set, but as shown in Sec. 4.3.2 is generally far less stable. The GTrXL (Input) performs worse than even the TrXL-I, reinforcing the identity map path hypothesis. Finally, the GTrXL (Highway) and GTrXL (SigTanh) are more sensitive to the hyperparameter settings compared to the alternatives, with some settings doing worse than TrXL-I.

<!-- chunk {"id": "body-0035", "role": "body", "section": "Hyperparameter and Seed Sensitivity", "weight": 1.0} -->

Mean Human Norm. Score
## Param

<!-- chunk {"id": "body-0036", "role": "body", "section": "Hyperparameter and Seed Sensitivity", "weight": 1.0} -->

Beyond improved performance, we next demonstrate a significant reduction in hyperparameter and seed sensitivity for the GTrXL (GRU) compared to baselines and other GTrXL variants. We use the "Memory Maze" environment, a memory-based navigation task in which the agent must discover the location of an apple randomly placed in a maze of blocks. The agent receives a positive reward for collecting the apple and is then teleported to a random location in the maze, with the apple's position held fixed. The agent can make use of landmarks situated around the room to return as quickly as possible to the apple for subsequent rewards. Therefore, an effective mapping of the environment results in more frequent returns to the apple and higher reward.

<!-- chunk {"id": "body-0037", "role": "body", "section": "Hyperparameter and Seed Sensitivity", "weight": 1.0} -->

We chose to perform the sensitivity ablation on Memory Maze because it requires the use of long-range memory to be effective and it includes both continuous and discrete action sets (details in Appendix A) which makes optimization more difficult. In Figure 5, we sample 25 independent V-MPO hyperparameter settings from a wide range of values and train the networks to 2 billion environment steps (see Appendix B). Then, at various points in training (0.5B, 1.0B and 2.0B), we rank all runs by their mean return and plot this ranking. Models with curves which are both higher and flatter are thus more robust to hyperparameters and random seeds. Our results demonstrate that the GTrXL (GRU) can learn this challenging memory environment in much fewer environment steps than LSTM, and that GTrXL (GRU) beats the other gating variants in stability by a large margin, thereby offering a substantial reduction in necessary hyperparameter tuning. The values in Table 3 list what percentage of the 25 runs per model had losses that diverged to infinity.

<!-- chunk {"id": "body-0038", "role": "body", "section": "Hyperparameter and Seed Sensitivity", "weight": 1.0} -->

We can see that the only model reaching human performance in 2 billion environment steps is the GTrXL (GRU), with 10 runs having a mean score 8 and above.

<!-- chunk {"id": "body-0039", "role": "body", "section": "Parameter Count-Controlled Comparisons", "weight": 1.0} -->

For the final gating ablation, we compare transformer variants while tracking their total parameter count to control for the increase in capacity caused by the introduction of additional parameters in the gating mechanisms. To demonstrate that the advantages of the GTrXL (GRU) are not due solely to an increase in parameter count, we halve the number of attention heads (which also effectively halves the embedding dimension due to the convention that the embedding size is the number of heads multiplied by the attention head dimension). The effect is a substantial reduction in parameter count, resulting in less parameters than even the canonical TrXL. Fig. 6 and Tab. 3 compare the different models to the "Thin" GTrXL (GRU), with Tab. 3 listing the parameter counts. The Thin GTrXL (GRU) matches every other model (within variance) except the GTrXL (GRU), even matching the next best-performing model, the GTrXL (Output), with over 10 million less parameters.

<!-- chunk {"id": "body-0040", "role": "body", "section": "Gated Identity Initialization Ablation", "weight": 1.0} -->

All applicable gating variants in the previous sections were trained with the gated identity initialization (initial experiments found values $b_{g}^{(l)} = 2$ for GRU-type gating and $b_{g}^{(l)} = 1$ for other gating types to work well). We observed in initial Memory Maze results that the gated identity initialization significantly improved optimization stability and learning speed. Figure 7 compares an otherwise identical 4-layer GTrXL (GRU) trained with ($b_{g}^{(l)} = 2$) and without ($b_{g}^{(l)} = 0$) the gated identity initialization, with 10 hyperparameter samples per initial bias setting. Similarly to the previous sensitivity plots, we plot the ranked mean return of all 10 runs at various times during training. As can be seen from Fig. 7, there is a significant gap caused by the bias initialization, suggesting that preconditioning the transformer to be close to Markovian results in large learning speed gains.

<!-- chunk {"id": "body-0041", "role": "body", "section": "Conclusion", "weight": 1.5} -->

In this paper we provided evidence that confirms previous observations in the literature that standard transformer models, despite the recent successes in supervised learning, are too unstable to train in the RL setting and often fail to learn completely. We presented a new architectural variant of the transformer model, the GTrXL, which has increased performance, more stable optimization, and greater robustness to initial seed and hyperparameters than the canonical architecture. The key contributions of the GTrXL are reordered layer normalization modules, enabling an initially Markov regime of training, and a gating layer instead of the standard residual connections. We performed extensive ablation experiments testing the robustness, ease of optimization and final performance of the gating layer variations, as well as the effect of the reordered layer normalization. These results empirically demonstrate that the GRU-type gating performs best across all metrics, exhibiting comparable robustness to hyperparameters and random seeds as an LSTM while still maintaining a performance improvement.

<!-- chunk {"id": "body-0042", "role": "body", "section": "Conclusion", "weight": 1.5} -->

Furthermore, the GTrXL (GRU) learns faster, more stably and achieves a higher final performance (even when controlled for parameters) than the other gating variants on the challenging multitask DMLab-30 benchmark suite.

<!-- chunk {"id": "body-0043", "role": "body", "section": "Conclusion", "weight": 1.5} -->

Having demonstrated substantial and consistent improvement in DMLab-30, Numpad and Memory Maze over the ubiquitous LSTM architectures currently in use, the GTrXL makes the case for wider adoption of transformers in RL. A core benefit of the transformer architecture is its ability to scale to very large and deep models, and to effectively utilize this additional capacity in larger datasets. In future work, we hope to test the limits of the GTrXL's ability to scale in the RL setting by providing it with a large and varied set of training environments.
