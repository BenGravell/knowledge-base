## Introduction

The goal of generative modeling is to transform a prior distribution into the data distribution. Flow Matching provides an intuitive and conceptually simple framework for constructing flow paths that transport one distribution to another. Closely related to diffusion models, Flow Matching focuses on the velocity fields that guide model training. Since its introduction, Flow Matching has seen widespread adoption in modern generative modeling.

Both Flow Matching and diffusion models perform iterative sampling during generation. Recent research has paid significant attention to few-step---and in particular, one-step, feedforward---generative models. Pioneering this direction, Consistency Models introduce a consistency constraint to network outputs for inputs sampled along the same path. Despite encouraging results, the consistency constraint is imposed as a property of the network's behavior, while the properties of the underlying ground-truth field that should guide learning remain unknown. Consequently, training can be unstable and requires a carefully designed "discretization curriculum" to progressively constrain the time domain.

In this work, we propose a principled and effective framework, termed MeanFlow, for one-step generation. The core idea is to introduce a new ground-truth field representing the average velocity, in contrast to the instantaneous velocity typically modeled in Flow Matching. Average velocity is defined as the ratio of displacement to a time interval, with displacement given by the time integral of the instantaneous velocity. Solely originated from this definition, we derive a well-defined, intrinsic relation between the average and instantaneous velocities, which naturally serves as a principled basis for guiding network training.

Building on this fundamental concept, we train a neural network to directly model the average velocity field. We introduce a loss function that encourages the network to satisfy the intrinsic relation between average and instantaneous velocities. No extra consistency heuristic is needed. The existence of the ground-truth target field ensures that the optimal solution is, in principle, independent of the specific network, which in practice can lead to more robust and stable training. We further show that our framework can naturally incorporate classifier-free guidance (CFG) into the target field, incurring no additional cost at sampling time when guidance is used.

Our MeanFlow Models demonstrate strong empirical performance in one-step generative modeling. On ImageNet 256$\times$`<!-- -->`{=html}256, our method achieves an FID of 3.43 using 1-NFE (Number of Function Evaluations) generation. This result significantly outperforms previous state-of-the-art methods in its class by a relative margin of 50% to 70% (Fig. 1). In addition, our method stands as a self-contained generative model: it is trained entirely from scratch, without any pre-training, distillation, or curriculum learning. Our study largely closes the gap between one-step diffusion/flow models and their multi-step predecessors, and we hope it will inspire future work to reconsider the foundations of these powerful models.

## Related Work

### Diffusion and Flow Matching

Over the past decade, diffusion models have been developed into a highly successful framework for generative modeling. These models progressively add noise to clean data and train a neural network to reverse this process. This procedure involves solving stochastic differential equations (SDE), which is then reformulated as probability flow ordinary differential equations (ODE). Flow Matching methods extend this framework by modeling the velocity fields that define flow paths between distributions. Flow Matching can also be viewed as a form of continuous-time Normalizing Flows.

### Few-step Diffusion/Flow Models

Reducing sampling steps has become an important consideration from both practical and theoretical perspectives. One approach is to distill a pre-trained many-step diffusion model into a few-step model, e.g., or score distillation. Early explorations into training few-step models are built upon the evolution of distillation-based methods. Meanwhile, Consistency Models are developed as a standalone generative model that does not require distillation. These models impose consistency constraints on network outputs at different time steps, encouraging them to produce the same endpoints along the trajectory. Various consistency models and training strategies have been investigated.

In recent work, several methods have focused on characterizing diffusion-/flow-based quantities with respect to two time-dependent variables. In, a Flow Map is defined as the integral of the flow between two time steps, with several forms of matching losses developed for learning. In comparison to the average velocity our method is based , the Flow Map corresponds to displacement. Shortcut Models introduce a self-consistency loss function in addition to Flow Matching, which captures relationships between the flows at different discrete time intervals. Inductive Moment Matching models the self-consistency of stochastic interpolants at different time steps.

## Background: Flow Matching

Figure 2: Velocity fields in Flow Matching. Left: conditional flows. A given zt can arise from different (x, ϵ) pairs, resulting in different conditional velocities vt. Right: marginal flows, obtained by marginalizing over all possible conditional velocities. The marginal velocity field serves as the underlying ground-truth field for network training. All velocities shown here are essentially instantaneous velocities. Illustration follows. (Gray dots: samples from prior; red dots: samples from data.)

Flow Matching is a family of generative models that learn to match the flows, represented by velocity fields, between two probabilistic distributions. Formally, given data $x \sim {p_{\text{data}}{(x)}}$ and prior $\epsilon \sim {p_{\text{prior}}{(\epsilon)}}$, a flow path can be constructed as $z_{t} = {{a_{t}x} + {b_{t}\epsilon}}$ with time $t$, where $a_{t}$ and $b_{t}$ are predefined schedules. The velocity $v_{t}$ is defined as $v_{t} = z_{t}' = {{a_{t}'x} + {b_{t}'\epsilon}}$, where ^′^ denotes the time derivative. This velocity is referred to as the conditional velocity , denoted by $v_{t} = {v_{t}{({z_{t} \mid x})}}$. See Fig. 2 left. A commonly used schedule is $a_{t} = {1 - t}$ and $b_{t} = t$, which leads to $v_{t} = {\epsilon - x}$.

Because a given $z_{t}$ and its $v_{t}$ can arise from different $x$ and $\epsilon$, Flow Matching essentially models the expectation over all possibilities, called the marginal velocity (Fig. 2 right): A neural network $v_{\theta}$ parameterized by $\theta$ is learned to fit the marginal velocity field: ${\mathcal{L}_{\text{FM}}{(\theta)}} = {{\mathbb{E}}_{t,{p_{t}{(z_{t})}}}{\|{{v_{\theta}{(z_{t},t)}} - {v{(z_{t},t)}}}\|}^{2}}$. Although computing this loss function is infeasible due to the marginalization in Eq. 1, it is proposed to instead evaluate the conditional Flow Matching loss: $\mathcal{L}_{\text{CFM}}{(\theta)} = {\mathbb{E}}_{t,x,\epsilon} \parallel v_{\theta}{(z_{t},t)} - v_{t}{(z_{t} \mid x)} \parallel^{2}$, where the target $v_{t}$ is the conditional velocity. Minimizing $\mathcal{L}_{\text{CFM}}$ is equivalent to minimizing $\mathcal{L}_{\text{FM}}$.

Given a marginal velocity field $v{(z_{t},t)}$, samples are generated by solving an ODE for $z_{t}$: starting from $z_{1} = \epsilon \sim p_{\text{prior}}$. The solution can be written as: $z_{r} = {z_{t} - {\int_{r}^{t}{v{(z_{\tau},\tau)}{d\tau}}}}$, where we use $r$ to denote another time step. In practice, this integral is approximated numerically over discrete time steps. For example, the Euler method, a first-order ODE solver, computes each step as: $z_{t_{i + 1}} = {z_{t_{i}} + {{({t_{i + 1} - t_{i}})}v{(z_{t_{i}},t_{i})}}}$. Higher-order solvers can also be applied.

It is worth noting that even when the conditional flows are designed to be straight ("rectified\"), the marginal velocity field (Eq. 1) typically induces a curved trajectory. See Fig. 2 for illustration. We also emphasize that this non-straightness is not only a result of neural network approximation, but rather arises from the underlying ground-truth marginal velocity field. When applying coarse discretizations over curved trajectories, numerical ODE solvers lead to inaccurate results.

## MeanFlow Models

### Mean Flows

The core idea of our approach is to introduce a new field representing average velocity, whereas the velocity modeled in Flow Matching represents the instantaneous velocity.

### Average Velocity

We define average velocity as the displacement between two time steps $t$ and $r$ (obtained by integration) divided by the time interval. Formally, the average velocity $u$ is: To emphasize the conceptual difference, throughout this paper, we use the notation $u$ to denote average velocity, and $v$ to denote instantaneous velocity. $u{(z_{t},r,t)}$ is a field that is jointly dependent on $(r,t)$. The field of $u$ is illustrated in Fig. 3. Note that in general, the average velocity $u$ is the result of a functional of the instantaneous velocity $v$: that is, $u = {\mathcal{F}{\lbrack v\rbrack}} \triangleq {\frac{1}{t - r}{\int_{r}^{t}{v{d\tau}}}}$. It is a field induced by $v$, not depending on any neural network. Conceptually, just as the instantaneous velocity $v$ serves as the ground-truth field in Flow Matching, the average velocity $u$ in our formulation provides an underlying ground-truth field for learning.

Figure 3: The field of average velocity u(z, r, t). Leftmost: While the instantaneous velocity v determines the tangent direction of the path, the average velocity u(z, r, t), defined in Eq. 3, is generally not aligned with v. The average velocity is aligned with the displacement, which is (t − r)u(z, r, t). Right three subplots: The field u(z, r, t) is conditioned on both r and t, and is shown here for t = 0.5, 0.7, and 1.0.

By definition, the field of $u$ satisfies certain boundary conditions and "consistency" constraints (generalizing the terminology of ). As $r\rightarrow t$, we have: ${\lim_{r\rightarrow t}u} = v$. Moreover, a form of "consistency\" is naturally satisfied: taking one larger step over $\lbrack r,t\rbrack$ is "consistent\" with taking two smaller consecutive steps over $\lbrack r,s\rbrack$ and $\lbrack s,t\rbrack$, for any intermediate time $s$. To see this, observe that ${{({t - r})}u{(z_{t},r,t)}} = {{{({s - r})}u{(z_{s},r,s)}} + {{({t - s})}u{(z_{t},s,t)}}}$, which follows directly from the additivity of the integral: ${\int_{r}^{t}{v{d\tau}}} = {{\int_{r}^{s}{v{d\tau}}} + {\int_{s}^{t}{v{d\tau}}}}$. Thus, a network that accurately approximates the true $u$ is expected to satisfy the consistency relation inherently, without the need for explicit constraints.

The ultimate aim of our MeanFlow model will be to approximate the average velocity using a neural network $u_{\theta}{(z_{t},r,t)}$. This has the notable advantage that, assuming we approximate this quantity accurately, we can approximate the entire flow path using a *single* evaluation of $u_{\theta}{(\epsilon,0,1)}$. In other words, and as we will also demonstrate empirically, the approach is much more amenable to single or few-step generation, as it does not need to explicitly approximate a time integral at inference time, which was required when modeling instantaneous velocity. However, directly using the average velocity defined by Eq. 3 as ground truth for training a network is intractable, as it requires evaluating an integral during training. Our key insight is that the definitional equation of average velocity can be manipulated to construct an optimization target that is ultimately amenable to training, even when only the *instantaneous* velocity is accessible.

### The MeanFlow Identity

To have a formulation amenable to training, we rewrite Eq. 3 as: Now we differentiate both sides with respect to $t$, treating $r$ as independent of $t$. This leads to: where the manipulation of the left hand side employs the product rule and the right hand side uses the fundamental theorem of calculus^11^1If $r$ depends on $t$, the Leibniz rule gives: ${\frac{d}{dt}{\int_{r}^{t}{v{(z_{\tau},\tau)}{d\tau}}}} = {{v{(z_{t},t)}} - {v{(z_{r},r)}\frac{dr}{dt}}}$.. Rearranging terms, we obtain the identity: We refer to this equation as the "MeanFlow Identity\", which describes the relation between $v$ and $u$. It is easy to show that Eq. 6 and Eq. 4 are equivalent (see Sec. B.3).

The right hand side of Eq. 6 provides a "target\" form for $u{(z_{t},r,t)}$, which we will leverage to construct a loss function to train a neural network. To serve as a suitable target, we must also further decompose the time derivative term, which we discuss next.

### Computing Time Derivative

To compute the $\frac{d}{dt}u$ term in Eq. 6, note that $\frac{d}{dt}$ denotes a total derivative, which can be expanded in terms of partial derivatives: With $\frac{dz_{t}}{dt} = {v{(z_{t},t)}}$ (see Eq. 2), $\frac{dr}{dt} = 0$, and $\frac{dt}{dt} = 1$, we have another relation between $u$ and $v$: This equation shows that the total derivative is given by the Jacobian-vector product (JVP) between $\lbrack{\partial_{z}u},{\partial_{r}u},{\partial_{t}u}\rbrack$ (the Jacobian matrix of the function $u$) and the tangent vector $\lbrack v,0,1\rbrack$. In modern libraries, this can be efficiently computed by the jvp interface, such as torch.func.jvp in PyTorch or jax.jvp in JAX, which we discuss later.

### Training with Average Velocity

Up to this point, the formulations are independent of any network parameterization. We now introduce a model to learn $u$. Formally, we parameterize a network $u_{\theta}$ and encourage it to satisfy the MeanFlow Identity (Eq. 6). Specifically, we minimize this objective: The term $u_{\text{tgt}}$ serves as the effective regression target, which is driven by Eq. 6. This target uses the instantaneous velocity $v$ as the only ground-truth signal; no integral computation is needed. While the target should involve derivatives of $u$ (that is, $\partial u$), they are replaced by their parameterized counterparts (that is, $\partial u_{\theta}$). In the loss function, a stop-gradient (sg) operation is applied on the target $u_{\text{tgt}}$, following common practice: in our case, it eliminates the need for "double backpropagation" through the Jacobian-vector product, thereby avoiding higher-order optimization. Despite these practices for optimizability, if $u_{\theta}$ were to achieve zero loss, it is easy to show that it would satisfy the MeanFlow Identity (Eq. 6), and thus satisfy the original definition (Eq. 3).

The velocity $v{(z_{t},t)}$ in Eq. 10 is the marginal velocity in Flow Matching (see Fig. 2 right). We follow to replace it with the conditional velocity (Fig. 2 left). With this, the target is: Recall that $v_{t} = {{a_{t}'x} + {b_{t}'\epsilon}}$ is the conditional velocity, and by default, $v_{t} = {\epsilon - x}$.

Pseudocode for minimizing the loss function Eq. 9 is presented in Alg. 1. Overall, our method is conceptually simple: it behaves similarly to Flow Matching, with the key difference that the matching target is modified by $- {{({t - r})}\left( {{v_{t}{\partial_{z}u_{\theta}}} + {\partial_{t}u_{\theta}}} \right)}$, arising from our consideration of the average velocity. In particular, note that if we were to restrict to the condition $t = r$, then the second term vanishes, and the method would exactly match standard Flow Matching.

## fn(z, r, t): function to predict u

## training batch

error = u - stopgrad(u_tgt) loss = metric(error) Algorithm 1 MeanFlow: Training. Note: in PyTorch and JAX, jvp returns the function output and JVP.

Algorithm 2 MeanFlow: 1-step Sampling In Alg. 1, the jvp operation is highly efficient. In essence, computing $\frac{d}{dt}u$ via jvp requires only a single backward pass, similar to standard backpropagation in neural networks. Because $\frac{d}{dt}u$ is part of the target $u_{\text{tgt}}$ and thus subject to stopgrad (w.r.t. $\theta$), the backpropagation for neural network optimization (w.r.t. $\theta$) treats $\frac{d}{dt}u$ as a constant, incurring no higher-order gradient computation. Consequently, jvp introduces only a single extra backward pass, and its cost is comparable to that of backpropagation. In our JAX implementation of Alg. 1, the overhead is less than 20% of the total training time (see appendix).

### Sampling

Sampling using a MeanFlow model is performed simply by replacing the time integral with the average velocity: In the case of 1-step sampling, we simply have $z_{0} = {z_{1} - {u{(z_{1},0,1)}}}$, where $z_{1} = \epsilon \sim {p_{\text{prior}}{(\epsilon)}}$. Alg. 2 provides the pseudocode. Although one-step sampling is the main focus on this work, we emphasize that few step sampling is also straightforward given this equation.

### Relation to Prior Work

While related to previous one-step generative models, our method provides a more principled framework. At the core of our method is the functional relationship between two underlying fields $v$ and $u$, which naturally leads to the MeanFlow Identity that $u$ must satisfy (Eq. 6). This identity does not depend on the introduction of neural networks. In contrast, prior works typically rely on extra consistency constraints, imposed on the behavior of the neural network. Consistency Models are focused on paths anchored at the data side: in our notations, this corresponds to fixing $r \equiv 0$ for any $t$. As a result, Consistency Models are conditioned on a single time variable, unlike ours. On the other hand, the Shortcut and IMM models are conditioned on two time variables: they introduce additional two-time self-consistency constraints. In contrast, our method is solely driven by the definition of average velocity, and the MeanFlow Identity (Eq. 6) used for training is naturally derived from this definition, with no extra assumption.

### Mean Flows with Guidance

Our method naturally supports classifier-free guidance (CFG). Rather than naïvely applying CFG at sampling time, which would double NFE, we treat CFG as a property of the underlying ground-truth fields. This formulation allows us to enjoy the benefits of CFG while maintaining the 1-NFE behavior during sampling.

### Ground-truth Fields

We construct a new ground-truth field $v^{\text{cfg}}$: which is a linear combination of a class-conditional and a class-unconditional field: where $v_{t}$ is the conditional velocity (more precisely, sample-conditional velocity in this context).

Following the spirit of MeanFlow, we introduce the average velocity $u^{\text{cfg}}$ corresponding to $v^{\text{cfg}}$. As per the MeanFlow Identity (Eq. 6), $u^{\text{cfg}}$ satisfies: Again, $v^{\text{cfg}}$ and $u^{\text{cfg}}$ are underlying ground-truth fields that do not depend on neural networks. Here, $v^{\text{cfg}}$, as defined in Eq. 13, can be rewritten as: where we leverage the relation^22^2Observe that: ${v^{\text{cfg}}{(z_{t},t)}} \triangleq {{\mathbb{E}}_{\mathbf{c}}{\lbrack{v^{\text{cfg}}{(z_{t},{t \mid \mathbf{c}})}}\rbrack}} = {{\omega{\mathbb{E}}_{\mathbf{c}}{\lbrack{v{(z_{t},{t \mid \mathbf{c}})}}\rbrack}} + {{({1 - \omega})}v{(z_{t},t)}}} = {v{(z_{t},t)}}$.: ${v{(z_{t},t)}} = {v^{\text{cfg}}{(z_{t},t)}}$, as well as ${v^{\text{cfg}}{(z_{t},t)}} = {u^{\text{cfg}}{(z_{t},t,t)}}$.

### Training with Guidance

With Eq. 15 and Eq. 16, we construct a network and its learning target. We directly parameterize $u^{\text{cfg}}$ by a function $u_{\theta}^{\text{cfg}}$. Based on Eq. 15, we obtain the objective: This formulation is similar to Eq. 9, with the only difference that it has a modified ${\overset{\sim}{v}}_{t}$: which is driven by Eq. 16: the term $v{(z_{t},{t \mid \mathbf{c}})}$ in Eq. 16, which is the marginal velocity, is replaced by the (sample-)conditional velocity $v_{t}$, following. If $\omega = 1$, this loss function degenerates to the no-CFG case in Eq. 9.

To expose the network $u_{\theta}^{\text{cfg}}$ in Eq. 17 to class-unconditional inputs, we drop the class condition with 10% probability, following. Driven by a similar motivation, we can also expose $u_{\theta}^{\text{cfg}}{(z_{t},t,t)}$ in Eq. 19 to both class-unconditional and class-conditional versions: the details are in Sec. B.1.

### Single-NFE Sampling with CFG

In our formulation, $u_{\theta}^{\text{cfg}}$ directly models $u^{\text{cfg}}$, which is the average velocity induced by the CFG velocity $v^{\text{cfg}}$ (Eq. 13). As a result, no linear combination is required during sampling: we directly use $u_{\theta}^{\text{cfg}}$ for one-step sampling (see Alg. 2), with only a single NFE. This formulation preserves the desirable single-NFE behavior.

### Design Decisions

### Loss Metrics

In Eq. 9, the metric considered is the squared L2 loss. Following, we investigate different loss metrics. In general, we consider the loss function in the form of $\mathcal{L} = {\|\Delta\|}_{2}^{2\gamma}$, where $\Delta$ denotes the regression error. It can be proven (see ) that minimizing ${\|\Delta\|}_{2}^{2\gamma}$ is equivalent to minimizing the squared L2 loss ${\|\Delta\|}_{2}^{2}$ with "adapted loss weights\". Details are in the appendix. In practice, we set the weight as $w = {1/{({{\|\Delta\|}_{2}^{2} + c})}^{p}}$, where $p = {1 - \gamma}$ and $c > 0$ (e.g., $10^{- 3}$). The adaptively weighted loss is ${\text{sg}{(w)}} \cdot \mathcal{L}$, with $\mathcal{L} = {\|\Delta\|}_{2}^{2}$. If $p = 0.5$, this is similar to the Pseudo-Huber loss . We compare different $p$ values in experiments.

### Sampling Time Steps $(r,t)$

We sample the two time steps $(r,t)$ from a predefined distribution. We investigate two types of distributions: (i) a uniform distribution, $\mathcal{U}{}$, and (ii) a logit-normal (lognorm) distribution, where a sample is first drawn from a normal distribution $\mathcal{N}{(\mu,\sigma)}$ and then mapped to $$ using the logistic function. Given a sampled pair, we assign the larger value to $t$ and the smaller to $r$. We set a certain portion of random samples with $r = t$.

### Conditioning on $(r,t)$

We use positional embedding to encode the time variables, which are then combined and provided as the conditioning of the neural network. We note that although the field is parameterized by $u_{\theta}{(z_{t},r,t)}$, it is not necessary for the network to directly condition on $(r,t)$. For example, we can let the network directly condition on $(t,{\Delta t})$, with ${\Delta t} = {t - r}$. In this case, we have ${u_{\theta}{( \cdot,r,t)}} \triangleq {\text{net}{( \cdot,t,{t - r})}}$ where net is the network. The JVP computation is always w.r.t. the function $u_{\theta}{( \cdot,r,t)}$. We compare different forms of conditioning in experiments.

## Experiments

### Experiment Setting

We conduct our major experiments on ImageNet generation at 256$\times$`<!-- -->`{=html}256 resolution. We evaluate Fréchet Inception Distance (FID) on 50K generated images. We examine the number of function evaluations (NFE) and study 1-NFE generation by default. Following, we implement our models on the latent space of a pre-trained VAE tokenizer. For 256$\times$`<!-- -->`{=html}256 images, the tokenizer produces a latent space of 32$\times$`<!-- -->`{=html}32$\times$`<!-- -->`{=html}4, which is the input to the model. Our models are all trained from scratch. Implementation details are in Appendix A.

In our ablation study, we use the ViT-B/4 architecture (namely, "Base\" size with a patch size of 4) as developed , trained for 80 epochs (400K iterations). As a reference, DiT-B/4 in has 68.4 FID, and SiT-B/4 (in our reproduction) has 58.9 FID, both using 250-NFE sampling.

### Ablation Study

We investigate the model properties in Tab. 1, analyzed next: Table 1: Ablation study on 1-NFE ImageNet 256×256 generation. FID-50K is evaluated. Default configurations are marked in gray: B/4 backbone, 80-epoch training from scratch.

### From Flow Matching to Mean Flows

Our method can be viewed as Flow Matching with a modified target (Alg. 1), and it reduces to standard Flow Matching when $r$ always equals $t$. Fig. 4(a) compares the ratio of randomly sampling $r \neq t$. A 0% ratio of $r \neq t$ (reducing to Flow Matching) fails to produce reasonable results for 1-NFE generation. A non-zero ratio of $r \neq t$ enables MeanFlow to take effect, yielding meaningful results under 1-NFE generation. We observe that the model balances between learning the instantaneous velocity ($r = t$) vs. propagating into $r \neq t$ via the modified target. Here, the optimal FID is achieved at a ratio of 25%, and a ratio of 100% also yields a valid result.

### JVP Computation

The JVP operation Eq. 8 serves as the core relation that connects all $(r,t)$ coordinates. In Fig. 4(b), we conduct a destructive comparison in which incorrect JVP computation is intentionally performed. It shows that meaningful results are achieved only when the JVP computation is correct. Notably, the JVP tangent along $\partial_{z}u$ is $d$-dimensional, where $d$ is the data dimension (here, 32$\times$`<!-- -->`{=html}32$\times$`<!-- -->`{=html}4), and the tangents along $\partial_{r}u$ and $\partial_{t}u$ are one-dimensional. Nevertheless, these two time variables determine the field $u$, and their roles are therefore critical even though they are only one-dimensional.

### Conditioning on $(r,t)$

As discussed in Sec. 4.3, we can represent $u_{\theta}{(z,r,t)}$ by various forms of explicit positional embedding, e.g., ${u_{\theta}{( \cdot,r,t)}} \triangleq {\text{net}{( \cdot,t,{t - r})}}$. Fig. 4(c) compares these variants. Fig. 4(c) shows that all variants of $(r,t)$ embeddings studied yield meaningful 1-NFE results, demonstrating the effectiveness of MeanFlow as a framework. Embedding $(t,{t - r})$, that is, time and interval, achieves the best result, while directly embedding $(r,t)$ performs almost as well. Notably, even embedding only the interval $t - r$ yields reasonable results.

### Time Samplers

Prior work has shown that the distribution used to sample $t$ influences the generation quality. We study the distribution used to sample $(r,t)$ in Fig. 4(d). Note that $(r,t)$ are first sampled independently, followed by a post-processing step that enforces $t > r$ by swapping and then caps the proportion of $r \neq t$ to a specified ratio. Fig. 4(d) reports that a logit-normal sampler performs the best, consistent with observations on Flow Matching.

### Loss Metrics

It has been reported that the choice of loss metrics strongly impacts the performance of few-/one-step generation. We study this aspect in Fig. 4(e). Our loss metric is implemented via adaptive loss weighting with power $p$ (Sec. 4.3). Fig. 4(e) shows that $p = 1$ achieves the best result, whereas $p = 0.5$ (similar to Pseudo-Huber loss ) also performs competitively. The standard squared L2 loss (here, $p = 0$) underperforms compared to other settings, but still produces meaningful results, consistent with observations .

### Guidance Scale

Fig. 4(f) reports the results with CFG. Consistent with observations in multi-step generation, CFG substantially improves generation quality in our 1-NFE setting too. We emphasize that our CFG formulation (Sec. 4.2) naturally support 1-NFE sampling.

### Scalability

Fig. 4 presents the 1-NFE FID results of MeanFlow across larger model sizes and different training durations. Consistent with the behavior of Transformer-based diffusion/flow models (DiT and SiT ), MeanFlow models exhibit promising scalability for 1-NFE generation.

### Comparisons with Prior Work

### ImageNet 256$\times$`<!-- -->`{=html}256 Comparisons

In Fig. 1 we compare with previous one-step diffusion/flow models, which are also summarized in Tab. 2 (left). Overall, MeanFlow largely outperforms previous methods in its class: it achieves 3.43 FID, which is an over 50% relative improvement vs. IMM's one-step result of 7.77; if we compare only 1-NFE (not just one-step) generation, MeanFlow has nearly 70% relative improvement vs. the previous state-of-the-art (10.60, Shortcut ). Our method largely closes the gap between one-step and many-step diffusion/flow models.

In 2-NFE generation, our method achieves an FID of 2.20 (Tab. 2, bottom left). This result is on par with the leading baselines of many-step diffusion/flow models, namely, DiT (FID 2.27) and SiT (FID 2.15), both having an NFE of 250$\times$`<!-- -->`{=html}2 (Tab. 2, right), under the same XL/2 backbone. Our results suggest that few-step diffusion/flow models can rival their many-step predecessors. Orthogonal improvements, such as REPA, are applicable, which are left for future work.

Notably, our method is self-contained and trained entirely from scratch. It achieves the strong results without using any pre-training, distillation, or the curriculum learning adopted .

Figure 4: Scalability of MeanFlow models on ImageNet 256×256. 1-NFE generation FID is reported. All models are trained from scratch. CFG is applied while maintaining the 1-NFE sampling behavior. Our method exhibits promising scalability with respect to model size.

1-NFE diffusion/flow from scratch 2-NFE diffusion/flow from scratch Table 2: Class-conditional generation on ImageNet-256×256. All entries are reported with CFG, when applicable. Left: 1-NFE and 2-NFE diffusion/flow models trained from scratch. Right: Other families of generative models as a reference. In both tables, “×2" indicates that CFG incurs an NFE of 2 per sampling step. Our MeanFlow models are all trained for 240 epochs, except that “MeanFlow-XL+” is trained for more epochs and with configurations selected for longer training, specified in appendix. †: iCT results are reported.

Table 3: Unconditional CIFAR-10.

### CIFAR-10 Comparisons

We report unconditional generation results on CIFAR-10 (32$\times$`<!-- -->`{=html}32) in Tab. 3. FID-50K is reported with 1-NFE sampling. All entries are with the same U-net developed from ($\sim$`<!-- -->`{=html}55M), applied directly on the pixel space. All other competitors are with the EDM-style pre-conditioner, and ours has no preconditioner. Implementation details are in the appendix. On this dataset, our method is competitive with prior approaches.

## Conclusion

We have presented MeanFlow, a principled and effective framework for one-step generation. Broadly speaking, the scenario considered in this work is related to multi-scale simulation problems in physics that may involve a range of scales, lengths, and resolution, in space or time. Carrying out numerical simulation is inherently limited by the ability of computers to resolve the range of scales. Our formulation involves describing the underlying quantity at coarsened levels of granularity, a common theme that underlies many important applications in physics. We hope that our work will bridge research in generative modeling, simulation, and dynamical systems in related fields.
