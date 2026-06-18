Sophia: A Scalable Stochastic Second-order Optimizer for Language Model Pre-training

Given the massive cost of language model pre-training, a non-trivial improvement of the optimization algorithm would lead to a material reduction on the time and cost of training. Adam and its variants have been state-of-the-art for years, and more sophisticated second-order (Hessian-based) optimizers often incur too much per-step overhead. In this paper, we propose Sophia, Second-order Clipped Stochastic Optimization, a simple scalable second-order optimizer that uses a light-weight estimate of the diagonal Hessian as the pre-conditioner. The update is the moving average of the gradients divided by the moving average of the estimated Hessian, followed by element-wise clipping. The clipping controls the worst-case update size and tames the negative impact of non-convexity and rapid change of Hessian along the trajectory. Sophia only estimates the diagonal Hessian every handful of iterations, which has negligible average per-step time and memory overhead.

## Introduction

Language models (LLMs) have gained phenomenal capabilities as their scale grows. However, pre-training LLMs is incredibly time-consuming due to the massive datasets and model sizes---hundreds of thousands of updates to the model parameters are required. For example, PaLM was trained for two months on 6144 TPUs, which costed 10 million dollars.

Pre-training efficiency is thus a major bottleneck in scaling up LLMs. This work aims to improve pre-training efficiency with a faster optimizer, which either reduces the time and cost to achieve the same pre-training loss, or alternatively achieves better pre-training loss with the same budget.

Adam (or its variants (Loshchilov & Hutter Shazeer & Stern You et al., )) is the dominantly used optimizer for training LLMs, such as GPT (Radford et al. Brown et al., ), OPT, Gopher and LLAMA. Designing faster optimizers for LLMs is challenging. First, the benefit of the first-order (gradient-based) pre-conditioner in Adam is not yet well understood (Liu et al. Zhang et al. Kunstner et al., ). Second, the choice of pre-conditioners is constrained because we can only afford light-weight options whose overhead can be offset by the speed-up in the number of iterations.

This paper introduces Sophia, Second-order Clipped Stochastic Optimization, a light-weight second-order optimizer that uses an inexpensive stochastic estimate of the diagonal of the Hessian as a pre-conditioner and a clipping mechanism to control the worst-case update size. On pre-training language models such as GPT-2, Sophia achieves the same validation pre-training loss with 50$\%$ fewer number of steps than Adam. Because Sophia maintains almost the memory and average time per step, the speedup also translates to 50$\%$ less total compute and 50$\%$ less wall-clock time (See Figure (a)&(b)).

## Conclusion

We introduced Sophia, a scalable second-order optimizer for language model pre-training. Sophia converges in fewer steps than first-order adaptive methods, while maintaining almost the same per-step cost. On language modeling with GPT models, Sophia achieves a 2x speed-up compared with AdamW in the number of steps, total compute, and wall-clock time.
