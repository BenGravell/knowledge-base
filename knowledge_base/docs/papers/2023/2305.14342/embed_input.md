Sophia: A Scalable Stochastic Second-order Optimizer for Language Model Pre-training

Given the massive cost of language model pre-training, a non-trivial improvement of the optimization algorithm would lead to a material reduction on the time and cost of training. Adam and its variants have been state-of-the-art for years, and more sophisticated second-order (Hessian-based) optimizers often incur too much per-step overhead. In this paper, we propose Sophia, Second-order Clipped Stochastic Optimization, a simple scalable second-order optimizer that uses a light-weight estimate of the diagonal Hessian as the pre-conditioner. The update is the moving average of the gradients divided by the moving average of the estimated Hessian, followed by element-wise clipping. The clipping controls the worst-case update size and tames the negative impact of non-convexity and rapid change of Hessian along the trajectory. Sophia only estimates the diagonal Hessian every handful of iterations, which has negligible average per-step time and memory overhead....

## Introduction

Language models (LLMs) have gained phenomenal capabilities as their scale grows. However, pre-training LLMs is incredibly time-consuming due to the massive datasets and model sizes---hundreds of thousands of updates to the model parameters are required. For example, PaLM was trained for two months on 6144 TPUs, which costed 10 million dollars.

Pre-training efficiency is thus a major bottleneck in scaling up LLMs. This work aims to improve pre-training efficiency with a faster optimizer, which either reduces the time and cost to achieve the same pre-training loss, or alternatively achieves better pre-training loss with the same budget.

## Conclusion

We introduced Sophia, a scalable second-order optimizer for language model pre-training. Sophia converges in fewer steps than first-order adaptive methods, while maintaining almost the same per-step cost. On language modeling with GPT models, Sophia achieves a 2x speed-up compared with AdamW in the number of steps, total compute, and wall-clock time.

We refer to Section B.1 for the details on hyperparameters and only discuss two key hyperparameters, $\gamma$ and the peak learning rate $\eta$ in the main text. Similar to the protocol of baselines, all other hyperparameters are tuned on a 30M model and remain fixed for all the model sizes. For the peak learning rate and $\gamma$, we found the following strategy general works well, and delivers almost the same performance as those found by grid search.

Option 2: Gauss-Newton-Bartlett (GNB) estimator. We leverage the structure of the loss to design a biased stochastic estimator for the diagonal Hessian, following Schraudolph; Martens; Wei et al.. Suppose $\ell{(\theta,{(x,y)})}$ is a loss function on an example $(x,y)$ of the form ${\ell{(\theta,{(x,y)})}} = {\ell_{\text{ce}}{({f{(\theta,x)}},y)}}$ where $\ell_{\text{ce}}$ is the cross-entropy loss and ${f{(\theta,x)}} \in {\mathbb{R}}^{V}$ is the logits, and $V$ is the number of items/classes in a multi-class classification problem (e.g., the vocabulary size in LLMs)....

Figure 6: Few-shot evaluation on SuperGLUE. With the same number of steps, models pre-trained with Sophia outperforms models pre-trained with AdamW and Lion on most tasks. Models pre-trained with Sophia for 200K steps have comparable performance as models pre-trained with AdamW for 400K steps.
