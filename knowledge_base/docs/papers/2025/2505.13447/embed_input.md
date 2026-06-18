<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Mean Flows for One-step Generative Modeling

Topics include Neural networks, Diffusion models, Learning.

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

We propose a principled and effective framework for one-step generative modeling. We introduce the notion of average velocity to characterize flow fields, in contrast to instantaneous velocity modeled by Flow Matching methods. A well-defined identity between average and instantaneous velocities is derived and used to guide neural network training. Our method, termed the MeanFlow model, is self-contained and requires no pre-training, distillation, or curriculum learning. MeanFlow demonstrates strong empirical performance: it achieves an FID of 3.43 with a single function evaluation (1-NFE) on ImageNet 256x256 trained from scratch, significantly outperforming previous state-of-the-art one-step diffusion/flow models. Our study substantially narrows the gap between one-step diffusion/flow models and their multi-step predecessors, and we hope it will motivate future research to revisit the foundations of these powerful models.

<!-- chunk {"id": "body-0003", "role": "body", "section": "Introduction", "weight": 1.5} -->

The goal of generative modeling is to transform a prior distribution into the data distribution. Flow Matching provides an intuitive and conceptually simple framework for constructing flow paths that transport one distribution to another. Closely related to diffusion models, Flow Matching focuses on the velocity fields that guide model training. Since its introduction, Flow Matching has seen widespread adoption in modern generative modeling.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

Both Flow Matching and diffusion models perform iterative sampling during generation. Recent research has paid significant attention to few-step---and in particular, one-step, feedforward---generative models. Pioneering this direction, Consistency Models introduce a consistency constraint to network outputs for inputs sampled along the same path. Despite encouraging results, the consistency constraint is imposed as a property of the network's behavior, while the properties of the underlying ground-truth field that should guide learning remain unknown. Consequently, training can be unstable and requires a carefully designed "discretization curriculum" to progressively constrain the time domain.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

In this work, we propose a principled and effective framework, termed MeanFlow, for one-step generation. The core idea is to introduce a new ground-truth field representing the average velocity, in contrast to the instantaneous velocity typically modeled in Flow Matching. Average velocity is defined as the ratio of displacement to a time interval, with displacement given by the time integral of the instantaneous velocity. Solely originated from this definition, we derive a well-defined, intrinsic relation between the average and instantaneous velocities, which naturally serves as a principled basis for guiding network training.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

Building on this fundamental concept, we train a neural network to directly model the average velocity field. We introduce a loss function that encourages the network to satisfy the intrinsic relation between average and instantaneous velocities. No extra consistency heuristic is needed. The existence of the ground-truth target field ensures that the optimal solution is, in principle, independent of the specific network, which in practice can lead to more robust and stable training. We further show that our framework can naturally incorporate classifier-free guidance (CFG) into the target field, incurring no additional cost at sampling time when guidance is used.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

Our MeanFlow Models demonstrate strong empirical performance in one-step generative modeling. On ImageNet 256$\times$`<!-- -->`{=html}256, our method achieves an FID of 3.43 using 1-NFE (Number of Function Evaluations) generation. This result significantly outperforms previous state-of-the-art methods in its class by a relative margin of 50% to 70% (Fig. 1). In addition, our method stands as a self-contained generative model: it is trained entirely from scratch, without any pre-training, distillation, or curriculum learning. Our study largely closes the gap between one-step diffusion/flow models and their multi-step predecessors, and we hope it will inspire future work to reconsider the foundations of these powerful models.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Diffusion and Flow Matching", "weight": 1.0} -->

Over the past decade, diffusion models have been developed into a highly successful framework for generative modeling. These models progressively add noise to clean data and train a neural network to reverse this process. This procedure involves solving stochastic differential equations (SDE), which is then reformulated as probability flow ordinary differential equations (ODE). Flow Matching methods extend this framework by modeling the velocity fields that define flow paths between distributions. Flow Matching can also be viewed as a form of continuous-time Normalizing Flows.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Few-step Diffusion/Flow Models", "weight": 1.0} -->

Reducing sampling steps has become an important consideration from both practical and theoretical perspectives. One approach is to distill a pre-trained many-step diffusion model into a few-step model, e.g., or score distillation. Early explorations into training few-step models are built upon the evolution of distillation-based methods. Meanwhile, Consistency Models are developed as a standalone generative model that does not require distillation. These models impose consistency constraints on network outputs at different time steps, encouraging them to produce the same endpoints along the trajectory. Various consistency models and training strategies have been investigated.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Few-step Diffusion/Flow Models", "weight": 1.0} -->

In recent work, several methods have focused on characterizing diffusion-/flow-based quantities with respect to two time-dependent variables. In, a Flow Map is defined as the integral of the flow between two time steps, with several forms of matching losses developed for learning. In comparison to the average velocity our method is based, the Flow Map corresponds to displacement. Shortcut Models introduce a self-consistency loss function in addition to Flow Matching, which captures relationships between the flows at different discrete time intervals. Inductive Moment Matching models the self-consistency of stochastic interpolants at different time steps.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Mean Flows", "weight": 1.0} -->

The core idea of our approach is to introduce a new field representing average velocity, whereas the velocity modeled in Flow Matching represents the instantaneous velocity.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Average Velocity", "weight": 1.0} -->

We define average velocity as the displacement between two time steps $t$ and $r$ (obtained by integration) divided by the time interval.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Average Velocity", "weight": 1.0} -->

To emphasize the conceptual difference, throughout this paper, we use the notation $u$ to denote average velocity, and $v$ to denote instantaneous velocity. $u{(z_{t},r,t)}$ is a field that is jointly dependent on $(r,t)$. The field of $u$ is illustrated in Fig. 3. Note that in general, the average velocity $u$ is the result of a functional of the instantaneous velocity $v$: that is, $u = {\mathcal{F}{\lbrack v\rbrack}} \triangleq {\frac{1}{t - r}{\int_{r}^{t}{v{d\tau}}}}$. It is a field induced by $v$, not depending on any neural network. Conceptually, just as the instantaneous velocity $v$ serves as the ground-truth field in Flow Matching, the average velocity $u$ in our formulation provides an underlying ground-truth field for learning.

<!-- chunk {"id": "body-0014", "role": "body", "section": "Average Velocity", "weight": 1.0} -->

By definition, the field of $u$ satisfies certain boundary conditions and "consistency" constraints. As $r\rightarrow t$, we have: ${\lim_{r\rightarrow t}u} = v$. Moreover, a form of "consistency\" is naturally satisfied: taking one larger step over $\lbrack r,t\rbrack$ is "consistent\" with taking two smaller consecutive steps over $\lbrack r,s\rbrack$ and $\lbrack s,t\rbrack$, for any intermediate time $s$.

<!-- chunk {"id": "body-0015", "role": "body", "section": "Average Velocity", "weight": 1.0} -->

The ultimate aim of our MeanFlow model will be to approximate the average velocity using a neural network $u_{\theta}{(z_{t},r,t)}$. This has the notable advantage that, assuming we approximate this quantity accurately, we can approximate the entire flow path using a *single* evaluation of $u_{\theta}{(\epsilon,0,1)}$. In other words, and as we will also demonstrate empirically, the approach is much more amenable to single or few-step generation, as it does not need to explicitly approximate a time integral at inference time, which was required when modeling instantaneous velocity. However, directly using the average velocity defined by Eq. 3 as ground truth for training a network is intractable, as it requires evaluating an integral during training. Our key insight is that the definitional equation of average velocity can be manipulated to construct an optimization target that is ultimately amenable to training, even when only the *instantaneous* velocity is accessible.

<!-- chunk {"id": "body-0016", "role": "body", "section": "The MeanFlow Identity", "weight": 1.0} -->

To have a formulation amenable to training, we rewrite Eq.

<!-- chunk {"id": "body-0017", "role": "body", "section": "The MeanFlow Identity", "weight": 1.0} -->

Now we differentiate both sides with respect to $t$, treating $r$ as independent of $t$.

<!-- chunk {"id": "body-0018", "role": "body", "section": "The MeanFlow Identity", "weight": 1.0} -->

where the manipulation of the left hand side employs the product rule and the right hand side uses the fundamental theorem of calculus^11^1If $r$ depends on $t$, the Leibniz rule gives: ${\frac{d}{dt}{\int_{r}^{t}{v{(z_{\tau},\tau)}{d\tau}}}} = {{v{(z_{t},t)}} - {v{(z_{r},r)}\frac{dr}{dt}}}$..

<!-- chunk {"id": "body-0019", "role": "body", "section": "The MeanFlow Identity", "weight": 1.0} -->

We refer to this equation as the "MeanFlow Identity\", which describes the relation between $v$ and $u$. It is easy to show that Eq. 6 and Eq. 4 are equivalent (see Sec. B.3).

<!-- chunk {"id": "body-0020", "role": "body", "section": "The MeanFlow Identity", "weight": 1.0} -->

The right hand side of Eq. 6 provides a "target\" form for $u{(z_{t},r,t)}$, which we will leverage to construct a loss function to train a neural network. To serve as a suitable target, we must also further decompose the time derivative term, which we discuss next.

<!-- chunk {"id": "body-0021", "role": "body", "section": "Computing Time Derivative", "weight": 1.0} -->

This equation shows that the total derivative is given by the Jacobian-vector product (JVP) between $\lbrack{\partial_{z}u},{\partial_{r}u},{\partial_{t}u}\rbrack$ (the Jacobian matrix of the function $u$) and the tangent vector $\lbrack v,0,1\rbrack$. In modern libraries, this can be efficiently computed by the jvp interface, such as torch.func.jvp in PyTorch or jax.jvp in JAX, which we discuss later.

<!-- chunk {"id": "body-0022", "role": "body", "section": "Training with Average Velocity", "weight": 1.0} -->

Up to this point, the formulations are independent of any network parameterization. We now introduce a model to learn $u$. Formally, we parameterize a network $u_{\theta}$ and encourage it to satisfy the MeanFlow Identity (Eq. 6).

<!-- chunk {"id": "body-0023", "role": "body", "section": "Training with Average Velocity", "weight": 1.0} -->

The term $u_{\text{tgt}}$ serves as the effective regression target, which is driven by Eq. 6. This target uses the instantaneous velocity $v$ as the only ground-truth signal; no integral computation is needed. While the target should involve derivatives of $u$ (that is, $\partial u$), they are replaced by their parameterized counterparts (that is, $\partial u_{\theta}$). In the loss function, a stop-gradient (sg) operation is applied on the target $u_{\text{tgt}}$, following common practice: in our case, it eliminates the need for "double backpropagation" through the Jacobian-vector product, thereby avoiding higher-order optimization. Despite these practices for optimizability, if $u_{\theta}$ were to achieve zero loss, it is easy to show that it would satisfy the MeanFlow Identity (Eq. 6), and thus satisfy the original definition (Eq. 3).

<!-- chunk {"id": "body-0024", "role": "body", "section": "Training with Average Velocity", "weight": 1.0} -->

The velocity $v{(z_{t},t)}$ in Eq. 10 is the marginal velocity in Flow Matching (see Fig. 2 right). We follow to replace it with the conditional velocity (Fig. 2 left).

<!-- chunk {"id": "body-0025", "role": "body", "section": "Training with Average Velocity", "weight": 1.0} -->

Pseudocode for minimizing the loss function Eq. 9 is presented in Alg. 1. Overall, our method is conceptually simple: it behaves similarly to Flow Matching, with the key difference that the matching target is modified by $- {{({t - r})}\left( {{v_{t}{\partial_{z}u_{\theta}}} + {\partial_{t}u_{\theta}}} \right)}$, arising from our consideration of the average velocity. In particular, note that if we were to restrict to the condition $t = r$, then the second term vanishes, and the method would exactly match standard Flow Matching.

<!-- chunk {"id": "body-0026", "role": "body", "section": "Training with Average Velocity", "weight": 1.0} -->

## fn(z, r, t): function to predict u
## training batch
error = u - stopgrad(u_tgt)
loss = metric(error)
Algorithm 1 MeanFlow: Training.
Note: in PyTorch and JAX, jvp returns the function output and JVP.

<!-- chunk {"id": "body-0027", "role": "body", "section": "Training with Average Velocity", "weight": 1.0} -->

In Alg. 1, the jvp operation is highly efficient. In essence, computing $\frac{d}{dt}u$ via jvp requires only a single backward pass, similar to standard backpropagation in neural networks. Because $\frac{d}{dt}u$ is part of the target $u_{\text{tgt}}$ and thus subject to stopgrad (w.r.t. $\theta$), the backpropagation for neural network optimization (w.r.t. $\theta$) treats $\frac{d}{dt}u$ as a constant, incurring no higher-order gradient computation. Consequently, jvp introduces only a single extra backward pass, and its cost is comparable to that of backpropagation. In our JAX implementation of Alg. 1, the overhead is less than 20% of the total training time (see appendix).

<!-- chunk {"id": "body-0028", "role": "body", "section": "Sampling", "weight": 1.0} -->

In the case of 1-step sampling, we simply have $z_{0} = {z_{1} - {u{(z_{1},0,1)}}}$, where $z_{1} = \epsilon \sim {p_{\text{prior}}{(\epsilon)}}$. Alg. 2 provides the pseudocode. Although one-step sampling is the main focus on this work, we emphasize that few step sampling is also straightforward given this equation.

<!-- chunk {"id": "body-0029", "role": "body", "section": "Relation to Prior Work", "weight": 1.0} -->

While related to previous one-step generative models, our method provides a more principled framework. At the core of our method is the functional relationship between two underlying fields $v$ and $u$, which naturally leads to the MeanFlow Identity that $u$ must satisfy (Eq. 6). This identity does not depend on the introduction of neural networks. In contrast, prior works typically rely on extra consistency constraints, imposed on the behavior of the neural network. Consistency Models are focused on paths anchored at the data side: in our notations, this corresponds to fixing $r \equiv 0$ for any $t$. As a result, Consistency Models are conditioned on a single time variable, unlike ours. On the other hand, the Shortcut and IMM models are conditioned on two time variables: they introduce additional two-time self-consistency constraints. In contrast, our method is solely driven by the definition of average velocity, and the MeanFlow Identity (Eq. 6) used for training is naturally derived from this definition, with no extra assumption.

<!-- chunk {"id": "body-0030", "role": "body", "section": "Mean Flows with Guidance", "weight": 1.0} -->

Our method naturally supports classifier-free guidance (CFG). Rather than naïvely applying CFG at sampling time, which would double NFE, we treat CFG as a property of the underlying ground-truth fields. This formulation allows us to enjoy the benefits of CFG while maintaining the 1-NFE behavior during sampling.

<!-- chunk {"id": "body-0031", "role": "body", "section": "Ground-truth Fields", "weight": 1.0} -->

where $v_{t}$ is the conditional velocity (more precisely, sample-conditional velocity in this context).

<!-- chunk {"id": "body-0032", "role": "body", "section": "Ground-truth Fields", "weight": 1.0} -->

Following the spirit of MeanFlow, we introduce the average velocity $u^{\text{cfg}}$ corresponding to $v^{\text{cfg}}$. As per the MeanFlow Identity (Eq.

<!-- chunk {"id": "body-0033", "role": "body", "section": "Ground-truth Fields", "weight": 1.0} -->

Again, $v^{\text{cfg}}$ and $u^{\text{cfg}}$ are underlying ground-truth fields that do not depend on neural networks. Here, $v^{\text{cfg}}$, as defined in Eq.

<!-- chunk {"id": "body-0034", "role": "body", "section": "Training with Guidance", "weight": 1.0} -->

With Eq. 15 and Eq. 16, we construct a network and its learning target. We directly parameterize $u^{\text{cfg}}$ by a function $u_{\theta}^{\text{cfg}}$. Based on Eq.

<!-- chunk {"id": "body-0035", "role": "body", "section": "Training with Guidance", "weight": 1.0} -->

which is driven by Eq. 16: the term $v{(z_{t},{t \mid \mathbf{c}})}$ in Eq. 16, which is the marginal velocity, is replaced by the (sample-)conditional velocity $v_{t}$, following. If $\omega = 1$, this loss function degenerates to the no-CFG case in Eq. 9.

<!-- chunk {"id": "body-0036", "role": "body", "section": "Training with Guidance", "weight": 1.0} -->

To expose the network $u_{\theta}^{\text{cfg}}$ in Eq. 17 to class-unconditional inputs, we drop the class condition with 10% probability, following. Driven by a similar motivation, we can also expose $u_{\theta}^{\text{cfg}}{(z_{t},t,t)}$ in Eq. 19 to both class-unconditional and class-conditional versions: the details are in Sec. B.1.

<!-- chunk {"id": "body-0037", "role": "body", "section": "Single-NFE Sampling with CFG", "weight": 1.0} -->

In our formulation, $u_{\theta}^{\text{cfg}}$ directly models $u^{\text{cfg}}$, which is the average velocity induced by the CFG velocity $v^{\text{cfg}}$ (Eq. 13). As a result, no linear combination is required during sampling: we directly use $u_{\theta}^{\text{cfg}}$ for one-step sampling (see Alg. 2), with only a single NFE. This formulation preserves the desirable single-NFE behavior.

<!-- chunk {"id": "body-0038", "role": "body", "section": "Loss Metrics", "weight": 1.0} -->

In Eq. 9, the metric considered is the squared L2 loss. Following, we investigate different loss metrics. In general, we consider the loss function in the form of $\mathcal{L} = {\|\Delta\|}_{2}^{2\gamma}$, where $\Delta$ denotes the regression error. It can be proven that minimizing ${\|\Delta\|}_{2}^{2\gamma}$ is equivalent to minimizing the squared L2 loss ${\|\Delta\|}_{2}^{2}$ with "adapted loss weights\". Details are in the appendix. In practice, we set the weight as $w = {1/{({{\|\Delta\|}_{2}^{2} + c})}^{p}}$, where $p = {1 - \gamma}$ and $c > 0$ (e.g., $10^{- 3}$).

<!-- chunk {"id": "body-0039", "role": "body", "section": "Loss Metrics", "weight": 1.0} -->

The adaptively weighted loss is ${\text{sg}{(w)}} \cdot \mathcal{L}$, with $\mathcal{L} = {\|\Delta\|}_{2}^{2}$. If $p = 0.5$, this is similar to the Pseudo-Huber loss. We compare different $p$ values in experiments.

<!-- chunk {"id": "body-0040", "role": "body", "section": "Sampling Time Steps $(r,t)$", "weight": 1.0} -->

We sample the two time steps $(r,t)$ from a predefined distribution. We investigate two types of distributions: (i) a uniform distribution, $\mathcal{U}{}$, and (ii) a logit-normal (lognorm) distribution, where a sample is first drawn from a normal distribution $\mathcal{N}{(\mu,\sigma)}$ and then mapped to $$ using the logistic function. Given a sampled pair, we assign the larger value to $t$ and the smaller to $r$. We set a certain portion of random samples with $r = t$.

<!-- chunk {"id": "body-0041", "role": "body", "section": "Conditioning on $(r,t)$", "weight": 1.0} -->

We use positional embedding to encode the time variables, which are then combined and provided as the conditioning of the neural network. We note that although the field is parameterized by $u_{\theta}{(z_{t},r,t)}$, it is not necessary for the network to directly condition on $(r,t)$. For example, we can let the network directly condition on $(t,{\Delta t})$, with ${\Delta t} = {t - r}$. In this case, we have ${u_{\theta}{( \cdot,r,t)}} \triangleq {\text{net}{( \cdot,t,{t - r})}}$ where net is the network. The JVP computation is always w.r.t. the function $u_{\theta}{( \cdot,r,t)}$. We compare different forms of conditioning in experiments.

<!-- chunk {"id": "body-0042", "role": "body", "section": "Experiment Setting", "weight": 1.0} -->

We conduct our major experiments on ImageNet generation at 256$\times$`<!-- -->`{=html}256 resolution. We evaluate Fréchet Inception Distance (FID) on 50K generated images. We examine the number of function evaluations (NFE) and study 1-NFE generation by default. Following, we implement our models on the latent space of a pre-trained VAE tokenizer. For 256$\times$`<!-- -->`{=html}256 images, the tokenizer produces a latent space of 32$\times$`<!-- -->`{=html}32$\times$`<!-- -->`{=html}4, which is the input to the model. Our models are all trained from scratch. Implementation details are in Appendix A.

<!-- chunk {"id": "body-0043", "role": "body", "section": "Experiment Setting", "weight": 1.0} -->

In our ablation study, we use the ViT-B/4 architecture (namely, "Base\" size with a patch size of 4) as developed, trained for 80 epochs (400K iterations). As a reference, DiT-B/4 has 68.4 FID, and SiT-B/4 (in our reproduction) has 58.9 FID, both using 250-NFE sampling.

<!-- chunk {"id": "body-0044", "role": "body", "section": "Ablation Study", "weight": 1.0} -->

We investigate the model properties in Tab.

<!-- chunk {"id": "body-0045", "role": "body", "section": "From Flow Matching to Mean Flows", "weight": 1.0} -->

Our method can be viewed as Flow Matching with a modified target (Alg. 1), and it reduces to standard Flow Matching when $r$ always equals $t$. Fig. 4(a) compares the ratio of randomly sampling $r \neq t$. A 0% ratio of $r \neq t$ (reducing to Flow Matching) fails to produce reasonable results for 1-NFE generation. A non-zero ratio of $r \neq t$ enables MeanFlow to take effect, yielding meaningful results under 1-NFE generation. We observe that the model balances between learning the instantaneous velocity ($r = t$) vs. propagating into $r \neq t$ via the modified target. Here, the optimal FID is achieved at a ratio of 25%, and a ratio of 100% also yields a valid result.

<!-- chunk {"id": "body-0046", "role": "body", "section": "JVP Computation", "weight": 1.0} -->

The JVP operation Eq. 8 serves as the core relation that connects all $(r,t)$ coordinates. In Fig. 4(b), we conduct a destructive comparison in which incorrect JVP computation is intentionally performed. It shows that meaningful results are achieved only when the JVP computation is correct. Notably, the JVP tangent along $\partial_{z}u$ is $d$-dimensional, where $d$ is the data dimension (here, 32$\times$`<!-- -->`{=html}32$\times$`<!-- -->`{=html}4), and the tangents along $\partial_{r}u$ and $\partial_{t}u$ are one-dimensional. Nevertheless, these two time variables determine the field $u$, and their roles are therefore critical even though they are only one-dimensional.

<!-- chunk {"id": "body-0047", "role": "body", "section": "Conditioning on $(r,t)$", "weight": 1.0} -->

As discussed in Sec. 4.3, we can represent $u_{\theta}{(z,r,t)}$ by various forms of explicit positional embedding, e.g., ${u_{\theta}{( \cdot,r,t)}} \triangleq {\text{net}{( \cdot,t,{t - r})}}$. Fig. 4(c) compares these variants. Fig. 4(c) shows that all variants of $(r,t)$ embeddings studied yield meaningful 1-NFE results, demonstrating the effectiveness of MeanFlow as a framework. Embedding $(t,{t - r})$, that is, time and interval, achieves the best result, while directly embedding $(r,t)$ performs almost as well. Notably, even embedding only the interval $t - r$ yields reasonable results.

<!-- chunk {"id": "body-0048", "role": "body", "section": "Time Samplers", "weight": 1.0} -->

Prior work has shown that the distribution used to sample $t$ influences the generation quality. We study the distribution used to sample $(r,t)$ in Fig. 4(d). Note that $(r,t)$ are first sampled independently, followed by a post-processing step that enforces $t > r$ by swapping and then caps the proportion of $r \neq t$ to a specified ratio. Fig. 4(d) reports that a logit-normal sampler performs the best, consistent with observations on Flow Matching.

<!-- chunk {"id": "body-0049", "role": "body", "section": "Loss Metrics", "weight": 1.0} -->

It has been reported that the choice of loss metrics strongly impacts the performance of few-/one-step generation. We study this aspect in Fig. 4(e). Our loss metric is implemented via adaptive loss weighting with power $p$ (Sec. 4.3). Fig. 4(e) shows that $p = 1$ achieves the best result, whereas $p = 0.5$ also performs competitively. The standard squared L2 loss (here, $p = 0$) underperforms compared to other settings, but still produces meaningful results, consistent with observations.

<!-- chunk {"id": "body-0050", "role": "body", "section": "Guidance Scale", "weight": 1.0} -->

Fig. 4(f) reports the results with CFG. Consistent with observations in multi-step generation, CFG substantially improves generation quality in our 1-NFE setting too. We emphasize that our CFG formulation (Sec. 4.2) naturally support 1-NFE sampling.

<!-- chunk {"id": "body-0051", "role": "body", "section": "Scalability", "weight": 1.0} -->

Fig. 4 presents the 1-NFE FID results of MeanFlow across larger model sizes and different training durations. Consistent with the behavior of Transformer-based diffusion/flow models (DiT and SiT ), MeanFlow models exhibit promising scalability for 1-NFE generation.

<!-- chunk {"id": "body-0052", "role": "body", "section": "ImageNet 256$\\times$`<!-- -->`{=html}256 Comparisons", "weight": 1.0} -->

In Fig. 1 we compare with previous one-step diffusion/flow models, which are also summarized in Tab. 2 (left). Overall, MeanFlow largely outperforms previous methods in its class: it achieves 3.43 FID, which is an over 50% relative improvement vs. IMM's one-step result of 7.77; if we compare only 1-NFE (not just one-step) generation, MeanFlow has nearly 70% relative improvement vs. the previous state-of-the-art. Our method largely closes the gap between one-step and many-step diffusion/flow models.

<!-- chunk {"id": "body-0053", "role": "body", "section": "ImageNet 256$\\times$`<!-- -->`{=html}256 Comparisons", "weight": 1.0} -->

In 2-NFE generation, our method achieves an FID of 2.20 (Tab. 2, bottom left). This result is on par with the leading baselines of many-step diffusion/flow models, namely, DiT (FID 2.27) and SiT (FID 2.15), both having an NFE of 250$\times$`<!-- -->`{=html}2 (Tab. 2, right), under the same XL/2 backbone. Our results suggest that few-step diffusion/flow models can rival their many-step predecessors. Orthogonal improvements, such as REPA, are applicable, which are left for future work.

<!-- chunk {"id": "body-0054", "role": "body", "section": "ImageNet 256$\\times$`<!-- -->`{=html}256 Comparisons", "weight": 1.0} -->

Notably, our method is self-contained and trained entirely from scratch. It achieves the strong results without using any pre-training, distillation, or the curriculum learning adopted.

<!-- chunk {"id": "body-0055", "role": "body", "section": "ImageNet 256$\\times$`<!-- -->`{=html}256 Comparisons", "weight": 1.0} -->

1-NFE diffusion/flow from scratch

<!-- chunk {"id": "body-0056", "role": "body", "section": "ImageNet 256$\\times$`<!-- -->`{=html}256 Comparisons", "weight": 1.0} -->

2-NFE diffusion/flow from scratch

<!-- chunk {"id": "body-0057", "role": "body", "section": "CIFAR-10 Comparisons", "weight": 1.0} -->

We report unconditional generation results on CIFAR-10 (32$\times$`<!-- -->`{=html}32) in Tab. 3. FID-50K is reported with 1-NFE sampling. All entries are with the same U-net developed ($\sim$`<!-- -->`{=html}55M), applied directly on the pixel space. All other competitors are with the EDM-style pre-conditioner, and ours has no preconditioner. Implementation details are in the appendix. On this dataset, our method is competitive with prior approaches.

<!-- chunk {"id": "body-0058", "role": "body", "section": "Conclusion", "weight": 1.5} -->

We have presented MeanFlow, a principled and effective framework for one-step generation. Broadly speaking, the scenario considered in this work is related to multi-scale simulation problems in physics that may involve a range of scales, lengths, and resolution, in space or time. Carrying out numerical simulation is inherently limited by the ability of computers to resolve the range of scales. Our formulation involves describing the underlying quantity at coarsened levels of granularity, a common theme that underlies many important applications in physics. We hope that our work will bridge research in generative modeling, simulation, and dynamical systems in related fields.
