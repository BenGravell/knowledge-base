Mean Flows for One-step Generative Modeling

Topics include Neural networks, Diffusion models, Learning.

We propose a principled and effective framework for one-step generative modeling. We introduce the notion of average velocity to characterize flow fields, in contrast to instantaneous velocity modeled by Flow Matching methods. A well-defined identity between average and instantaneous velocities is derived and used to guide neural network training. Our method, termed the MeanFlow model, is self-contained and requires no pre-training, distillation, or curriculum learning. MeanFlow demonstrates strong empirical performance: it achieves an FID of 3.43 with a single function evaluation (1-NFE) on ImageNet 256x256 trained from scratch, significantly outperforming previous state-of-the-art one-step diffusion/flow models. Our study substantially narrows the gap between one-step diffusion/flow models and their multi-step predecessors, and we hope it will motivate future research to revisit the foundations of these powerful models.

## Introduction

The goal of generative modeling is to transform a prior distribution into the data distribution. Flow Matching provides an intuitive and conceptually simple framework for constructing flow paths that transport one distribution to another. Closely related to diffusion models, Flow Matching focuses on the velocity fields that guide model training. Since its introduction, Flow Matching has seen widespread adoption in modern generative modeling.

Both Flow Matching and diffusion models perform iterative sampling during generation. Recent research has paid significant attention to few-step---and in particular, one-step, feedforward---generative models. Pioneering this direction, Consistency Models introduce a consistency constraint to network outputs for inputs sampled along the same path. Despite encouraging results, the consistency constraint is imposed as a property of the network's behavior, while the properties of the underlying ground-truth field that should guide learning remain unknown....

## Conclusion

We have presented MeanFlow, a principled and effective framework for one-step generation. Broadly speaking, the scenario considered in this work is related to multi-scale simulation problems in physics that may involve a range of scales, lengths, and resolution, in space or time. Carrying out numerical simulation is inherently limited by the ability of computers to resolve the range of scales. Our formulation involves describing the underlying quantity at coarsened levels of granularity, a common theme that underlies many important applications in physics....

We construct a new ground-truth field $v^{\text{cfg}}$:

To compute the $\frac{d}{dt}u$ term in Eq. 6, note that $\frac{d}{dt}$ denotes a total derivative, which can be expanded in terms of partial derivatives:

We use positional embedding \[\] to encode the time variables, which are then combined and provided as the conditioning of the neural network. We note that although the field is parameterized by $u_{\theta}{(z_{t},r,t)}$, it is not necessary for the network to directly condition on $(r,t)$. For example, we can let the network directly condition on $(t,{\Delta t})$, with ${\Delta t} = {t - r}$. In this case, we have ${u_{\theta}{( \cdot,r,t)}} \triangleq {\text{net}{( \cdot,t,{t - r})}}$ where net is the network. The JVP computation is always w.r.t....
