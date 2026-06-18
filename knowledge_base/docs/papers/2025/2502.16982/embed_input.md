Muon Is Scalable for LLM Training

Recently, the Muon optimizer based on matrix orthogonalization has demonstrated strong results in training small-scale language models, but the scalability to larger models has not been proven. We identify two crucial techniques for scaling up Muon: adding weight decay and carefully adjusting the per-parameter update scale. These techniques allow Muon to work out-of-the-box on large-scale training without the need of hyper-parameter tuning. Scaling law experiments indicate that Muon achieves ~ 2x computational efficiency compared to AdamW with compute optimal training. Based on these improvements, we introduce Moonlight, a 3B/16B-parameter Mixture-of-Expert (MoE) model trained with 5.7T tokens using Muon. Our model improves the current Pareto frontier, achieving better performance with much fewer training FLOPs compared to prior models. We open-source our distributed Muon implementation that is memory optimal and communication efficient. We also release the pretrained, instruction-tuned, and intermediate checkpoints to support future research.

## Introduction

The rapid advancement of large language models (LLMs) \[undefab, undefh, undefj, undefaj\] has significantly pushed forward the progress in artificial general intelligence. However, training capable LLMs remains a computationally intensive and resource-demanding process due to scaling laws \[undefq, undefm\]. Optimizers play a crucial role in efficiently and effectively training of LLMs, with Adam \[undefr\] and its variant AdamW \[undefz\] being the standard choice for most large-scale training.

Recent developments in optimization algorithms have shown potential to improve training efficiency beyond AdamW \[undefy, undefo, undefar, undefam, undefu, undefv, undefad, undefx, undefw, undefac\]. Among these, \[undefo\] proposed Muon, which updates matrix parameters with orthogonalized gradient momentum using Newton-Schulz iteration. Initial experiments with Muon have demonstrated promising results in small-scale language model training....

## Conclusions

In this technical report, we presented a comprehensive study on the scalability of Muon in LLM training. Through systematic analysis and improvements, we successfully applied Muon to a 3B/16B-parameter MoE model trained on 5.7 trillion tokens. Our results demonstrate that Muon can effectively replace AdamW as the standard optimizer for large-scale LLM training, offering significant advantages in both training efficiency and model performance....

For the MLP weight matrix of shape $\lbrack H,{4H}\rbrack$, both Update Norm and Adjusted LR obtain a weight RMS that is roughly doubled comparing to Baseline. This is reasonable as ${\sqrt{\text{max}{(H,{4H})}}/\sqrt{H}} = 2$, so the update RMS of Update Norm and Adjusted LR is roughly two times of Baseline;

DP Gather. For a local DP partitioned master weight (${1/D}P$ the size of the model weight), this operation is to gather the corresponding partitioned gradients into a full gradient matrix.

Our evaluation encompasses four primary categories of benchmarks, each designed to assess distinct capabilities of the model:

In this technical report, we present a comprehensive study addressing these challenges. Our work builds upon Muon while systematically identifying and resolving its limitations in large-scale training scenarios. Our technical contributions include:
