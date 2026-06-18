Adam-mini: Use Fewer Learning Rates to Gain More

Topics include Language models, Learning, Adam-mini.

We propose Adam-mini, an optimizer that achieves on par or better performance than AdamW with 50% less memory footprint. Adam-mini reduces memory by cutting down the learning rate resources in Adam (i.e., 1/sqrt(v)). By investigating the Hessian structure of neural nets, we find Adam's v might not function at its full potential as effectively as we expected. We find that >= 99.9% of these learning rates in v could be harmlessly removed if we carefully partition the parameters into blocks following our new principle on Hessian structure; assign a single but good learning rate to each parameter block. We then provide one simple way to find good learning rates and propose Adam-mini. Empirically, we verify that Adam-mini performs on par or better than AdamW on various language models sized from 39M to 13B for pre-training, supervised fine-tuning, and RLHF. The reduced memory footprint of Adam-mini also alleviates communication overheads among GPUs, thereby increasing throughput. For instance, Adam-mini achieves 49.6% higher throughput than AdamW when pre-training Llama 2-7B on 2x A800-80GB GPUs, which saves 33% wall-clock time for pre-training.

## Introduction

Adam has become the de-facto optimizer for training large language models (LLMs) (e.g., (Vaswani et al. Achiam et al. Touvron et al. Team et al., )). Despite its superior performance, Adam is expensive to use. Specifically, Adam requires the memory for its optimizer states: the first-order momentum $m$, and the second-order momentum $v$. These in total take at least $2 \times$ the memory of the model size ^22^2We restate the update rules of Adam and AdamW in Appendix E.1.. This memory consumption has become a major burden in LLM training....

It is intriguing to design effective optimizers that require less memory. First, it lowers the threshold of training LLMs and encourages participation from more diverse researchers, especially those with limited GPU resources. Second, it requires fewer GPUs to train a model with a desired size, leading to substantial savings in both cost and energy. Third, it can ease the burden of CPU offloading and model sharding, which in turn, can enhance the throughput and accelerate the training process.

## Concluding Remarks

We proposed Adam-mini, an optimizer that saves 50% memory of Adam. We remark that there is great room to improve the design of Adam-mini: currently Adam-mini uses a simple and cost-effective way to design a learning rate for each dense Hessian sub-block, but it might not be an optimal way. We leave the development of stronger designs as a future direction.

Principle 1: We should partition parameters into blocks, such that each parameter block is associated with the smallest dense sub-block in Hessian.

where $\tau \in {\lbrack 0,1\rbrack}$ is the "diagonal-over-off-diagonal ratio", and we use it to measure how dense $H_{b}$ is ($H_{b}$ is pure diagonal when $\tau = 1$). $r \geq 0$ measures the effectiveness of Adam's preconditioner $D_{\text{Adam}}$ when operating on the Hessian-block $H_{b}$ (the smaller the better). We investigate the change of $r$ when changing the structure of $H_{b}$, including changing $\tau$, dimension $d$, and also $\kappa{(H_{b})}$. We emphasize that for a fixed $d$ or $\kappa{(H_{b})}$, we change $\tau$ by only rotating the eigenvectors, but not changing the eigenvalues of $H_{b}$....

Why using $\text{mean}{(v)}$ as learning rates. Due to limited space, we move the discussions to Appendix C.
