<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Double Preconditioning (DoPr): Optimization for Test-Time Performance, Not Validation Loss

Topics include Optimization, Deep learning optimizers, Preconditioning, Test-time feedback, Autoregressive models, Robot policy learning, KFAC, Adam, Muon.

<!-- chunk {"id": "summary-0002", "role": "summary", "section": "Summary", "weight": 2.0} -->

Proposes Double Preconditioning, an optimizer design aimed at improving rolled-out test-time behavior rather than one-step validation loss. DoPr combines gradient-wise preconditioning with activation-wise preconditioning, arguing that optimization itself can mitigate error accumulation in autoregressive, flow-based, and robot-policy settings.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Many modern applications of deep learning involve training a neural network via a one-step prediction loss (e.g., L^ regression, cross-entropy), but deploy the network by rolling out along its own predictions. Key examples include autoregressive language modeling, flow-based generative modeling, and robot policy learning. It is well-documented that these settings induce a phenomenon we call test-time feedback (TTF): the mismatch between the training/validation loss and downstream metrics of interest, such as task success rate and generation quality, which grows with task length. While data curation, architecture, and objective design have been proposed to combat train-test shift in TTF settings, this paper proposes optimization as a new design axis to mitigate error accumulation. Specifically, we introduce a new optimization paradigm called double-preconditioning (DoPr) uniquely tailored to the challenges of TTF. DoPr combines gradient-wise preconditioning, as in Adam and Muon, with activation-wise preconditioning (AP), such as in KFAC. We show that the addition of AP yields a drop-in intervention for increasing downstream model performance across a range of TTF settings.

<!-- chunk {"id": "abstract-0004", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Interestingly, these gains in test-time performance do not consistently accompany improvements in validation loss, opening new questions about how to properly evaluate models trained with one-step supervised objectives.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

Recent years have seen a resurgence in the design of novel optimizers for deep learning, particularly via the use of "matrix-shaped" normalization or preconditioning. These optimizers adjust gradient updates by a "preconditioning" matrix to reweight the descent direction. The successes highlight improved *convergence time* on training or validation loss, such as Shampoo (gupta2018shampoo; anil2020scalable; shi2023distributed) winning the AlgoPerf optimizer competition (mlcommons2024algoperf) as measured by an overall "holdout error per unit compute" metric, and Muon (jordan2024muon) coming to prominence in greatly accelerating low "time to target validation loss" on NanoGPT pretraining and seeing adoption in training production-scale language models (team2025kimi).

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

These successes implicitly assume that low generalization error on the training objective implies good downstream performance, e.g. pass@$k$ in the context of language reasoning. However, it has been widely noted that validation loss may not track natural performance metrics. The two diverge under a regime we call test-time feedback (TTF), ubiquitous in contemporary deep learning, in which one *trains on per-step supervised objectives*, while deployment involves *rolling out multiple steps according to the model's own predictions*. Key examples include: robot policy learning where per-step (or per-chunk) imitation of expert actions along expert trajectories, and deployment involves rolling out using the learned policy's actions and autoregressive LLM training in which models are trained via next-token prediction, yet deployed via autoregressive sampling. In these settings, sequential deployment can cause the distribution of inputs (e.g., context tokens in language modeling) to diverge from that of the training distribution, leading to distribution shift driven solely by the model's own prediction errors.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

This "TTF shift" is widely attested in both robotics (ross2011reduction; simchowitz2025pitfalls) and in long-horizon language generation (e.g., (bengio2015scheduled; ranzato2015sequence; song2023consistency)).

<!-- chunk {"id": "body-0008", "role": "body", "section": "Introduction", "weight": 1.5} -->

> Is there a design space for lightweight, generally applicable interventions on deep learning optimizers that target improved downstream performance?

<!-- chunk {"id": "body-0009", "role": "body", "section": "Introduction", "weight": 1.5} -->

Contributions. First, we establish a rigorous connection between *distribution shift* induced by TTF and *imperfect feature learning* under today's popular optimizers that precondition updates solely using gradient statistics (e.g. kingma2014adam; kellerjordan/cifar10-airbench). Specifically, we observe that when activations/inputs at each layer are non-isotropic, feature learning suffers, which induces errors that can disproportionately drive distribution shift under TTF. Moreover, these *cannot* be remedied by updates at later layers (Proposition˜3.2. ‣ Understanding TTF from Feature Learning. ‣ 3.1 TTF Shift and Imperfect Feature Learning ‣ 3 Distribution Shift under Test-Time Feedback")).

<!-- chunk {"id": "body-0010", "role": "body", "section": "Introduction", "weight": 1.5} -->

Second, based on the above insights, we propose the Double Preconditioning (DoPr) framework, which couples an activation-based preconditioner (AP) using layer activations to compute a preconditioning matrix (e.g. martens2018kronecker) with more standard gradient-based preconditioners (GP), such as in Adam (kingma2014adam; loshchilov2017decoupled) or Muon (jordan2024muon). AP encourages more uniformly accurate feature learning, mitigating the TTF distribution shift described above, whilst benefiting from the training speed and stability afforded by GP.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Introduction", "weight": 1.5} -->

Whereas past variants of AP in the literature were introduced as standalone optimizers, DoPr shows how to incorporate AP as an *drop-in* modification to any GP optimizer, such as Adam and Muon, providing a stable training recipe and produces models with strong downstream performance. We develop an *invariance principle* under which DoPr updates can be systematically derived for any {architecture, GP } pairing, e.g., convolution and self-attention layers. Further, optimal hyperparameters can be reliably predicted by popular GP scaling heuristics (yang2023tensor).

<!-- chunk {"id": "body-0012", "role": "body", "section": "Introduction", "weight": 1.5} -->

Finally, we carefully evaluate the capabilities of DoPr across a range of continuous-control, robotics, and language generation tasks. We find that DoPr consistently improves downstream performance---measured via natural, task-specific metrics across numerous applications--- by intervening *purely on the optimizer*, without additional modifications to the data, training objective, or architecture.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Learning under Test-Time Feedback", "weight": 1.0} -->

We study the problem of learning under test-time feedback (TTF) --- where our goal is to learn a model that is deployed in feedback with its own generations (as in language modeling) or with the environment (as in robotics). We formalize TTF as a problem of behavior cloning (pomerleau1988alvinn) in a Markov Decision Process (MDP). Consider a finite-horizon MDP with states $\mathbf{s}_{t} \in S$, actions $\mathbf{a}_{t} \in A$, transitions $\mathbf{s}_{t + 1} \sim {P{(\mathbf{s}_{t},\mathbf{a}_{t})}}$, and total horizon $T$.

<!-- chunk {"id": "body-0014", "role": "body", "section": "Learning under Test-Time Feedback", "weight": 1.0} -->

Given a per-example training loss $L_{train}{(;\mathbf{s},\mathbf{a})}$ measuring the distance between $(\mathbf{s})$ and $\mathbf{a}$, and pairs of states and corresponding actions $(\mathbf{s},\mathbf{a})$ (blue denoting demonstrator/data distribution), we train a learned policy by minimizing

<!-- chunk {"id": "body-0015", "role": "body", "section": "Learning under Test-Time Feedback", "weight": 1.0} -->

In the infinite data regime, and assuming $(\mathbf{s}_{1},\mathbf{a}_{1},\ldots)$ are collected by a demonstrator ~demo~ deployed in the MDP, minimizing Eq.˜2.1 approximately minimizes *validation loss*

<!-- chunk {"id": "body-0016", "role": "body", "section": "Learning under Test-Time Feedback", "weight": 1.0} -->

When there is no risk of confusion, we will abbreviate $L_{train} = L$ and $\mathcal{L}_{val} = \mathcal{L}$.

<!-- chunk {"id": "body-0017", "role": "body", "section": "Language modeling", "weight": 1.0} -->

Language modeling with tokens $x_{t}$ can be cast as an instance of TTF (ouyang2022training; foster2024behavior), where the states $\mathbf{s}_{t} = x_{1:t}$ denote the current context, actions $\mathbf{a}_{t} = x_{t + 1}$ are the next token, and the dynamics are induced by concatenation: $\mathbf{s}_{t + 1} = x_{1:{t + 1}}$. The language model then produces tokens $x_{t + 1} \sim {{}_{}^{}{( \cdot \mid x_{1:t})}}$.

<!-- chunk {"id": "body-0018", "role": "body", "section": "Robotic behavior cloning", "weight": 1.0} -->

In robotics, $\mathbf{s}$ corresponds to the robot and environment state, and $\mathbf{a}$ to the robot actions. In practice, $\mathbf{s}$ is replaced by robot observations (e.g., pixels, tactile), and actions $\mathbf{a}$ may be short sequences or "action-chunks". Earlier works parameterize Gaussian policies ${{}_{}^{}{( \cdot \mid \mathbf{s})}} = N{({(\mathbf{s})},{}_{}^{})}$, motivating an $L_{2}$ training loss $L_{train}{({}_{}^{}\mathbf{s},\mathbf{a})} = \parallel {(\mathbf{s})} - \mathbf{a} \parallel^{2}$ whereas modern works use generative model parameterizations (e.g. flows or diffusion (chi2023diffusion; pan2025much)).

<!-- chunk {"id": "body-0019", "role": "body", "section": "Robotic behavior cloning", "weight": 1.0} -->

Typical rewards can include task success (e.g., an object was successfully moved to a desired location) or dense locomotive rewards (e.g., how far the robot has traversed).

<!-- chunk {"id": "body-0020", "role": "body", "section": "Optimizer Preconditioning for Minimizing $\\mathcal{L}_{train}$ in TTF", "weight": 1.0} -->

In our TTF formulation, $\mathcal{L}_{train}$ is a standard supervised-learning loss. We consider an optimization algorithm alg that produces iterates ${\{^{(k)}\}}_{k \geq 1}$ in order to minimize $\mathcal{L}_{train}$. Examples include mini-batch stochastic gradient descent (SGD), Adam (W), Shampoo (gupta2018shampoo; shi2023distributed), and the recently popularized Muon optimizer (jordan2024muon). Most popular deep learning optimizers can be viewed as *gradient-based preconditioners* (GP), where the update direction is shaped purely using gradient information.

<!-- chunk {"id": "body-0021", "role": "body", "section": "Optimizer Preconditioning for Minimizing $\\mathcal{L}_{train}$ in TTF", "weight": 1.0} -->

Many prominent members therein, such as Adam, Shampoo, Muon etc., are specifically structured approximations (e.g., diagonal, layer-wise) of the AdaGrad gradient-covariance $\sum_{k \geq 1}\nabla\mathcal{L}_{train}{(^{(k)})}\nabla\mathcal{L}_{train}{(^{(k)})}^{\top}$ (duchi2011adaptive), and admit specific interpretations as gradient *whiteners* or *normalizers*. We provide full discussion in Appendix˜A. Past work has extensively studied how the choice of optimization improves performance only on the *validation loss* $\mathcal{L}_{val}$, both in terms of final iterate $\lim_{k\rightarrow\infty}\mathcal{L}_{val}{(^{(k)})}$, or the convergence rate, i.e., how quickly $L_{val}{(^{(k)})}$ approaches its limit.

<!-- chunk {"id": "body-0022", "role": "body", "section": "Distribution Shift under Test-Time Feedback", "weight": 1.0} -->

Whereas the validation loss $\mathcal{L}_{val}$ evaluates training loss under the distribution of states induced by ~demo~, test-time reward $\mathcal{R}_{test}$ considers the distribution of states under. Due to sequential deployment in *feedback* with the MDP (e.g. through autoregressive generation in language modeling or with the environment in robotics), these two distributions do not agree (Figure˜2). We call their consequent difference test-time feedback (TTF) shift.

<!-- chunk {"id": "body-0023", "role": "body", "section": "Understanding TTF from Feature Learning", "weight": 1.0} -->

However, large subspace distance ${dist}{(\mathbf{G},\mathbf{G}_{\star})}$ means that there exist states $\mathbf{s}$ for which $\mathbf{G}_{\star}\mathbf{s}$ is non-zero, but $\mathbf{G}\mathbf{s}$ vanishes. Effectively, $\mathbf{G}$ "zeros out" certain directions of state-space, and therefore $\mathbf{F}\mathbf{G}$ will as well.

<!-- chunk {"id": "body-0024", "role": "body", "section": "Double Preconditioning (DoPr)", "weight": 1.0} -->

Toward addressing the pathologies of TTF, we propose the double preconditioning (DoPr) framework, which be summarized as applying layer-wise an *activation-covariance* preconditioner (AP) onto the gradient, then passing the AP-gradient into a *gradient preconditioner* (GP) of choice, such as in Adam or Muon.

<!-- chunk {"id": "body-0025", "role": "body", "section": "Double Preconditioning (DoPr)", "weight": 1.0} -->

where ${\hat{\nabla}}_{\mathbf{W}}$ is the minibatch gradient, and ${\hat{}}_{\mathbf{z}}$ the batch empirical uncentered covariance of $\mathbf{z}$. We display the core algorithm in Section˜4"), and discuss derivations for general architectures in Section˜4.2"). Full details and practical features are described in Appendix˜B.

<!-- chunk {"id": "body-0026", "role": "body", "section": "Double Preconditioning (DoPr)", "weight": 1.0} -->

Whereas much of the prior literature has focused on the role of *gradient* pre-conditioned optimization for stabilizing training and improving validation loss, we will show that DoPr's use of *activation* preconditioning mitigates TTF, and therefore improve downstream model performance independent of validation loss performance.

<!-- chunk {"id": "body-0027", "role": "body", "section": "Double Preconditioning (DoPr)", "weight": 1.0} -->

Algorithm 1 Double Preconditioning (Feedforward Layer, layer index ℓ suppressed)

<!-- chunk {"id": "body-0028", "role": "body", "section": "Gradient- v.s. Activation- preconditioning", "weight": 1.0} -->

We remark that activation preconditioning (AP) and many gradient preconditioners (GP's) are motivated as different approximations to different curvature preconditioners; see Appendix˜A for an extensive account. Prior work has modeled GP's (e.g., Adam, Muon) as performing (layer-wise) steepest descent with respect to a salient norm $\parallel \cdot \parallel$ (bernstein2024old; pethick2025lmo): $\mathbf{W}^{next} = {\mathbf{W} - {{\arg\max}_{{\parallel\mathbf{G}\parallel} \leq 1}\left\langle \mathbf{G},{\nabla_{\mathbf{W}}\mathcal{L}} \right\rangle}}$.^44^4Practical features like momentum and weight decay can be incorporated with slight modifications (pethick2025lmo).

<!-- chunk {"id": "body-0029", "role": "body", "section": "Gradient- v.s. Activation- preconditioning", "weight": 1.0} -->

Versions of AP have appeared in prior literature as a *standalone* optimizer (see e.g., amid2022locoprop; benzing2022gradient; zhang2023meta); we provide a full account in Appendix˜A. Rather than establishing the convergence/acceleratory properties of AP, we demonstrate how it is directly relevant to TTF. However, just as vanilla gradient descent can suffer from numerical instability in deep networks, the AP update requires stabilization to converge meaningfully on modern taskloads. This motivates the combination of AP with GP, yielding DoPr.

<!-- chunk {"id": "body-0030", "role": "body", "section": "Gradient- v.s. Activation- preconditioning", "weight": 1.0} -->

For example, setting ${\parallel \cdot \parallel} = {\parallel \cdot \parallel}_{\infty}$ as the entry-wise $\ell^{\infty}$-norm yields a Sign-Descent AP update ($\sim$Adam), and ${\parallel \cdot \parallel}_{{\mathsf{R}\mathsf{M}\mathsf{S}} - {\mathsf{R}\mathsf{M}\mathsf{S}}}$ recovers a Spectral-Descent AP update ($\sim$Muon).

<!-- chunk {"id": "body-0031", "role": "body", "section": "Theoretical Motivation: AP Mitigates TTF via Isotropic Feature Learning", "weight": 1.0} -->

Proposition˜3.2. ‣ Understanding TTF from Feature Learning. ‣ 3.1 TTF Shift and Imperfect Feature Learning ‣ 3 Distribution Shift under Test-Time Feedback") therefore reveals that non-uniform feature learning at a given layer (i.e., larger ${dist}{(\mathbf{G}_{1},\mathbf{G}_{\star})}$) can induce greater TTF shift and reduce downstream performance, regardless of what is learned at subsequent layers (the choice of $\mathbf{F}_{1}$). We now argue that AP optimizers exhibit more uniform feature learning by correcting a bias in GD that occurs when inputs are non-isotropic, i.e. $E^{_{demo}}{\lbrack{\mathbf{s}_{t}\mathbf{s}_{t}^{\top}}\rbrack}$ is ill conditioned (collins2021exploiting; zhang2023meta). Taken together, these findings imply that AP optimizers have the potential to mitigate TTF shift and its consequences.

<!-- chunk {"id": "body-0032", "role": "body", "section": "Lifting AP to General Architectures: An Invariance Principle", "weight": 1.0} -->

In Proposition˜4.1. ‣ 4.1 Theoretical Motivation: AP Mitigates TTF via Isotropic Feature Learning ‣ 4 Double Preconditioning (DoPr)"), we see that optimizers suffer from impaired feature learning, thus exacerbating TTF, when the covariances of layerwise activations are ill-conditioned, i.e. highly anisotropic, and observed that AP mitigates this by feature-learning *as if the covariances were isotropic*. Here, we leverage this observation to yield a general invariance principle, providing a reliable schematic for generalizing DoPr to general network layers, such as convolutions and self-attention.

<!-- chunk {"id": "body-0033", "role": "body", "section": "Remark 4.1 (Coordinate-dependent optimization paths)", "weight": 1.0} -->

In other words, two NNs of the same architecture initialized to have identical output, can take different optimization paths depending on the "coordinate system" of the internal activations, independently of the final output of the network. Consequently, the activation distributions propagated from the training distribution, e.g., ${}_{}^{}E^{_{demo}}{\lbrack\mathbf{s}_{t}\mathbf{s}_{t}^{\top}\rbrack}$ versus ${}_{\overline{}\mathbf{s}}^{}\mathbf{A}_{1}{{}_{}^{}{}_{}^{}}$, *impart a coordinate-dependent bias on the optimizer trajectory*, which Proposition˜3.1 and Proposition˜3.2. ‣ Understanding TTF from Feature Learning. ‣ 3.1 TTF Shift and Imperfect Feature Learning ‣ 3 Distribution Shift under Test-Time Feedback") demonstrate can exacerbate TTF.

<!-- chunk {"id": "body-0034", "role": "body", "section": "Remark 4.1 (Coordinate-dependent optimization paths)", "weight": 1.0} -->

Deriving AP for generic layer architectures boils down to the following principle: under an affine transformation on the input to the layer (and appropriate inverse transform to the applied weights) that preserve the layer output, what is the update rule that renders the layer outputs of the updated network invariant to the transform? In the feedforward case, this precisely yields the AP update as described in (DoPr).

<!-- chunk {"id": "body-0035", "role": "body", "section": "Remark 4.2", "weight": 1.0} -->

Isotropic activations have been understood to possess desirable properties for enabling feature learning, and thus are often (approximately) *enforced* by normalization layers such as BatchNorm (ioffe2015batch), LayerNorm (ba2016layer) etc. However, misplacement of normalization layers may have unintended consequences on the conditioning and expressivity of the network. The AP gradient provides a complementary approach: the effective model change under (AP) evolves *as if the activations were isotropic*, where $\nabla_{\mathbf{W}}\mathcal{L}{(f_{})}{}_{}^{- 1}\nabla_{\mathbf{W}}\mathcal{L}{(f_{})}$.

<!-- chunk {"id": "body-0036", "role": "body", "section": "Gradient-Preconditioning and Hyperparameter Scaling for DoPr", "weight": 1.0} -->

Determining favorable hyperparameters for large-scale training runs on a novel optimizer can prove challenging. This is a key motivation behind the "maximum-update parameterization" (P) (yang2022tensor; dey2025don), where the broad goal is to make hyperparameter choices invariant across network scales (e.g., width and depth); see Section˜C.4 for full discussion. Once made scale-invariant, hyperparameters can be tuned at small-scale and zero-shot transferred to the large-scale run. Recent work has demonstrated that in practice P is largely determined by coarse statistics such as the magnitude of the update direction (yang2023spectral; hong2025provable). Thus, in addition to the practical stabilizing and accelerating properties of GPs, a key benefit of using GPs in DoPr is as follows: whereas deriving scaling rules for a new optimizer can often be laborious, the *normalizing* property of GP trivializes this process for DoPr.

<!-- chunk {"id": "body-0037", "role": "body", "section": "Observation 4.3", "weight": 1.0} -->

Normalization by definition returns outputs of the same norm regardless of input. Thus, substituting the raw gradient with the AP gradient does not affect the magnitude of the update direction. Consequently, DoPr hyperparameter scaling rules can be ported directly from established rules based on the GP of choice, e.g. Adam, Muon, Shampoo etc. (everett2024scaling; qiu2025hyperparameter).

<!-- chunk {"id": "body-0038", "role": "body", "section": "Observation 4.3", "weight": 1.0} -->

We exhibit the immediate transfer of hyperparameter scaling rules in Figure˜6"), where we show learning rate and weight decay scaling transfer.

<!-- chunk {"id": "body-0039", "role": "body", "section": "Capabilities", "weight": 1.0} -->

In Section˜4"), we derive DoPr to address the poor feature learning of standard optimizers in TTF settings, with the promise of inducing better downstream behavior. To demonstrate this, we run experiments on diverse tasks and metrics across continuous control, robot policy learning, and LLM training. As noted in Section˜4.2"), DoPr need not improve the train/val loss convergence compared to the base GP, which we will revisit across our experiments. We also provide in Section˜C.1 general operating guidelines of our optimizer used in the ensuing experiments.

<!-- chunk {"id": "body-0040", "role": "body", "section": "Setting the Stage: Drop-in for Continuous Control", "weight": 1.0} -->

We first evaluate DoPr for imitation learning in Gymnasium (towers2025gymnasiumstandardinterfacereinforcement), which precisely aligns with our formalism of behavior cloning in MDPs. Here, we focus on the Humanoid-v5 task and refer to Section˜C.5 for full details and further experiments. We consider four GP primitives: Adam, Muon, Signum, and AdaMuon, that roughly cover instantaneous versus momentumized entrywise- and matrix-based normalization. We use a residual MLP architecture (he2015deepresiduallearningimage), and conduct a full sweep over the optimizer hyperparameters and report the results over independent evaluation trajectories and seeded training runs. We additionally use an EMA-ed copy of the policy parameters (block2024butterfly) for evaluation, which has been shown to be crucial for stabilizing BC policy performance in continuous control. We observe from Figure˜7 that: 1. different base GPs all have similar terminal rewards, 2. DoPr always improves terminal reward compared to the baseline counterparts, 3. the train/validation losses of DoPr variants are not uniformly better than the base GP.

<!-- chunk {"id": "body-0041", "role": "body", "section": "Image-Based Robot Policy Learning", "weight": 1.0} -->

We evaluate DoPr on pixel-based imitation learning with generative policies on Robomimic tasks. We focus on challenging tasks Tool-Hang Proficient-Human (PH) and Transport (PH), which are not solvable to $\sim {100\%}$ under modern BC recipes (pan2025much), and test complementary capabilities: dexterous precision in Tool-Hang and long-horizon coordination in Transport. Following pan2025much, we train a flow-based policy (lipman2023flow) with a U-Net backbone (chi2023diffusion). As in Section˜5.1, we apply model EMA to stabilize policy performance across all settings. Tuned hyperparameters are listed in Tables˜4 and 5, and full experiment details are in Section˜C.6. We report the best checkpoint success rate across training in Figure˜8. We observe that DoPr invariably improves the task success rate compared to the base GPs AdamW and Muon, while yielding worse or equal training loss---see Figure˜15. Notably, we see neither base GP is better than the other on both tasks simultaneously.

<!-- chunk {"id": "body-0042", "role": "body", "section": "Language Models", "weight": 1.0} -->

We finetune an LLM for mathematical reasoning, where training optimizes token likelihood but task performance depends on sequence accuracy. Section˜C.7 contains full experimental details.

<!-- chunk {"id": "body-0043", "role": "body", "section": "3B Supervised Fine-tuning", "weight": 1.0} -->

To characterize the behavior of DoPr, we first run a smaller-scale SFT experiment with the Llama-3.2-3B base model (llama3modelcard; grattafiori2024llama), using LoRA (hu2022lora) on a 100K-sample subset of OpenMathInstruct-2 (toshniwal2024openmathinstruct) for one epoch. This experiment probes learning-rate sensitivity, sample efficiency, and the relationship between downstream accuracy and token-level training loss. We report our results in Figure˜9. Across most learning rates, DoPr improves peak GSM8K performance. Notably, these improvements are *not explained by lower token-level training loss*: the final token-level training loss of DoPr is comparable to, or higher than, that of the base GP. We report similar trends for Muon (Figure˜16) in Section˜C.7.1.

<!-- chunk {"id": "body-0044", "role": "body", "section": "8B Supervised Fine-tuning: TTF at Larger Scale", "weight": 1.0} -->

Following the core SFT setup of OpenMathInstruct-2 (toshniwal2024openmathinstruct), we fine-tune Llama-3.1-8B (llama3modelcard; grattafiori2024llama) with LoRA (hu2022lora) on the OpenMathInstruct-2 train_1M split for two epochs. We sweep learning rates for AdamW and DoPr-AdamW, and evaluate the final checkpoints on GSM8K, GSM8K-CoT, and MATH-500, and estimate validation NLL on a 10K held-out subset of the SFT data. We examine in Figure˜10 how validation loss corresponds to downstream performance. For DoPr-AdamW, lower validation NLL generally corresponds to stronger downstream accuracy, especially on GSM8K-CoT and MATH-500. This is desirable, as holding data and architecture equal, one would expect a model with the best held-out NLL also has the best performance. However, this is not true for baseline AdamW.

<!-- chunk {"id": "body-0045", "role": "body", "section": "8B Supervised Fine-tuning: TTF at Larger Scale", "weight": 1.0} -->

For larger learning rates, AdamW-trained models predictably improve in-distribution validation loss but task performance (e.g., GSM8K) degrades. This illustrates our thesis that, without intervention, validation loss can be a poor proxy for full-sequence performance. Finally, DoPr-AdamW also reduces cross-task conflict: optimal learning rates on GSM8K-CoT are also (near-)optimal on MATH-500, whereas no AdamW checkpoints are simultaneously near-optimal for GSM8K and MATH-500 performance. This suggests that, as previewed in Section˜4.1"), DoPr encourages more robust feature learning. Additional results from the full sweep can be found in Section˜C.7.2.

<!-- chunk {"id": "body-0046", "role": "body", "section": "8B Supervised Fine-tuning: TTF at Larger Scale", "weight": 1.0} -->

We lastly remark additional experiments and discussion on flow-based generative modeling, another TTF setting, can be found in Section˜C.8.

<!-- chunk {"id": "body-0047", "role": "body", "section": "Discussion", "weight": 1.5} -->

Toward the ultimate goal of optimizing for downstream performance, we: 1. introduce Test-Time Feedback as a unified setting for many modern applications, 2. identify the mismatch between features that accelerate training convergence versus those sensitive under TTF, 3. prescribe Double Preconditioning (DoPr) that combines Activation Preconditioning (AP) to equalize feature learning and Gradient Preconditioning (GP) to stabilize training. We provide evidence for TTF and DoPr being useful abstractions via experiments across distinct TTF applications. Importantly, we find that improved downstream performance may not accompany improved train/validation loss, suggesting that there remains a viable design space for improving deep learning optimization that is orthogonal to accelerating loss convergence. Notably, our proposed recipe of combining activation- and gradient-preconditioning is just one candidate of double preconditioning; we posit that decoupling considerations for directionality (e.g., AP) and adaptivity (e.g., GP) may lead to fruitful optimizer design.
