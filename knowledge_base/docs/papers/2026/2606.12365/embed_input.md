<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Ambient Diffusion Policy: Imitation Learning from Suboptimal Data in Robotics

Topics include Imitation learning, Diffusion policy, Robotics, Suboptimal demonstrations, Co-training, Robot learning, Open X-embodiment, Data quality.

<!-- chunk {"id": "summary-0002", "role": "summary", "section": "Summary", "weight": 2.0} -->

Introduces Ambient Diffusion Policy, a way to use suboptimal robot demonstrations by restricting when they influence diffusion-policy training. The paper argues that robot action data has useful spectral structure, then exploits diffusion time to extract coarse and local features from imperfect data without letting harmful mid-scale details dominate the learned policy.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

We propose Ambient Diffusion Policy, a simple and principled method for imitation learning from suboptimal data in robotics. High-quality, task-specific robot data is expensive and time-consuming to collect, while suboptimal datasets with lower-quality or out-of-distribution demonstrations are abundant. Existing methods that co-train on both data sources in robotics often fail to separate the meaningful and the harmful features in the suboptimal samples. In contrast, our method extracts only the useful features by introducing a new axis to co-training in robotics: noise-dependent data usage. Ambient Diffusion Policy restricts the contribution of suboptimal data during training to only the high and low diffusion times. To rigorously justify our approach, we first observe that robot action data exhibits a spectral power law. This induces two important properties on the optimal Diffusion Policy that we exploit: a global-to-local hierarchy and locality. We theoretically formalize this discussion using a simplified model. Our experiments validate Ambient Diffusion Policy on four types of suboptimal action data (noisy trajectories, sim-to-real gap, task mismatch, and large-scale data mixtures) across six tasks.

<!-- chunk {"id": "abstract-0004", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

The results show that it effectively learns from arbitrary sources of suboptimal data. Notably, it outperforms existing co-training baselines by up to 33% when scaled to Open X-Embodiment - a large dataset with heterogeneous data quality and unstructured distribution shifts. Overall, Ambient Diffusion Policy increases the utility of suboptimal demonstrations and expands the set of usable data sources in robotics.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

The training corpus of nearly every large-scale robot policy spans different tasks, real and simulated environments, embodiments, and even modalities. One reason for this data heterogeneity is that high-quality, task-specific robot data is expensive and time-consuming to collect; it requires skilled teleoperators and well-tuned low-level controllers. In contrast, suboptimal data is abundant. Any real-world data collection effort naturally produces failures and trajectories of differing quality. Out-of-distribution (OOD) data sources are also plentiful and widely available. These include simulation, cross-embodied data, and ego-centric video. Practitioners often draw from data sources of varying quality to create massive pretraining sets, yet methods for learning from arbitrary suboptimal or shifted distributions are underexplored in robotics. We propose a simple and principled method for training robot policies that can leverage suboptimal and OOD datasets.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

The simplest way to handle heterogeneous datasets with mixed quality is to discard the lowest-quality samples, but this data filtering is wasteful: even suboptimal samples contain useful learning signal. The most common alternative in robotics is to "co-train" on everything while down-weighting suboptimal datasets. However, training a model to sample from a mixture with low-quality distributions fundamentally biases the policy. Finetuning is a complementary method, but can be insufficient alone (Section 7.5).

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

Our key intuition is that suboptimal and high-quality samples differ in some features, but align in others. For example, non-expert teleoperators may share the same high-level plan as experts, but exhibit less precise manipulation skills. Conversely, pick-and-place data may be useful for grasping primitives, but encode the wrong task.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Introduction", "weight": 1.5} -->

We turn this intuition into an algorithm by observing that robotic data exhibits a spectral power law. We show that this spectral structure induces a *global-to-local hierarchy* in action diffusion and a locality property in the optimal denoisers. Concretely, Diffusion Policy learns high-level planning at high noise and motion primitives at low noise. Thus, a policy can selectively learn useful features from suboptimal data by using it only at noise levels where it aligns with the target distribution. This unlocks a new design axis for co-training in robotics: *noise-dependent data usage*.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Introduction", "weight": 1.5} -->

To this end, we propose Ambient Diffusion Policy, a principled algorithm for training Diffusion Policies on suboptimal robot data. Each suboptimal sample can only contribute to training at the high or low diffusion times where it aligns with the target data. Our method extends the Ambient Diffusion Omni framework (or "Ambient" for short), which has been applied to computer vision and protein design.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Introduction", "weight": 1.5} -->

Properties of Robot Data. We empirically demonstrate that robot action data exhibits a spectral power law, which induces a global-to-local hierarchy and locality in action diffusion. These properties make Ambient Diffusion Omni well-suited for robotics (Section 4).

<!-- chunk {"id": "body-0011", "role": "body", "section": "Introduction", "weight": 1.5} -->

Ambient Diffusion Policy. We propose a simple and principled method for learning from suboptimal data that requires just a single change to Diffusion Policy's data sampler (Section 6).

<!-- chunk {"id": "body-0012", "role": "body", "section": "Introduction", "weight": 1.5} -->

Generality. Ambient outperforms baselines when training on three common types of action suboptimality: noisy demonstrations, sim-to-real gap, and task mismatch (Section 7).

<!-- chunk {"id": "body-0013", "role": "body", "section": "Introduction", "weight": 1.5} -->

Scale. When trained on Open X-Embodiment ---a large dataset with mixed data quality and unstructured distribution shifts---Ambient outperforms the co-training baseline by up to 33% on two real-world tasks. Additionally, Ambient continues to improve as we scale the amount of suboptimal data in the training mixture, whereas co-training plateaus (Section 8).

<!-- chunk {"id": "body-0014", "role": "body", "section": "Introduction", "weight": 1.5} -->

Theory. We prove that for a simple theoretical model, the spectral power law implies fast contraction through noise (Theorem 1. ‣ 5.1 Contraction Through Noise ‣ 5 Theoretical Foundations ‣ Ambient Diffusion Policy: Imitation Learning from Suboptimal Data in Robotics")) and locality (Theorem 2. ‣ 5.2 Spectral Power Law Implies Locality ‣ 5 Theoretical Foundations ‣ Ambient Diffusion Policy: Imitation Learning from Suboptimal Data in Robotics")) of the optimal policies. These contributions justify our algorithm and advance the theoretical foundations of the broader Ambient Diffusion framework (Section 5).

<!-- chunk {"id": "body-0015", "role": "body", "section": "Robot Imitation Learning and Diffusion Policy", "weight": 1.0} -->

Given a dataset $\mathcal{D}_{p} = {\{{(O^{(i)},A^{(i)})}\}}_{i = 1}^{n_{p}}$ of observation-action pairs, imitation learning aims to train a policy $\pi{({A \mid O})}$ that approximates the conditional distribution $p{({A \mid O})}$. Here, $A$ and $O$ represent chunks of future actions and recent observations. Diffusion Policy samples from $\pi{({A \mid O})}$ with a conditional denoising process over the action space. Concretely, it learns a family of denoisers ${\{{h_{\theta}{(A_{t},O,t)}}\}}_{t \in {\lbrack 0,T\rbrack}}$ that predict the clean action $A_{0}$ from a noisy version^11^1Diffusion Policy uses a variance-preserving implementation.

<!-- chunk {"id": "body-0016", "role": "body", "section": "Robot Imitation Learning and Diffusion Policy", "weight": 1.0} -->

We present it from the variance-exploding perspective to lighten notation. The two perspectives are equivalent up to a change of variables; see Appendix B.

<!-- chunk {"id": "body-0017", "role": "body", "section": "Robot Imitation Learning and Diffusion Policy", "weight": 1.0} -->

where $T$ is a sufficiently large constant, $\sigma{(t)}$ is a strictly increasing function known as the noise schedule, and ${\sigma{}} = 0$. For brevity, we write $\sigma_{t}:={\sigma{(t)}}$.

<!-- chunk {"id": "body-0018", "role": "body", "section": "Robot Imitation Learning and Diffusion Policy", "weight": 1.0} -->

where $t \sim {\mathcal{U}{\lbrack 0,T\rbrack}}$, ${(O,A_{0})} \sim \mathcal{D}_{p}$, and $A_{t}$ is sampled from Eq.. For a sufficiently expressive $h_{\theta}$, the minimizer of Eq. is the conditional expectation ${h_{\theta}^{\ast}{(A_{t},O,t)}} = {{\mathbb{E}}{\lbrack{A_{0} \mid {A_{t},O}}\rbrack}}$. Given access to the conditional expectations, one can sample from the target distribution $\pi{({A \mid O})}$ by running a reverse diffusion process. Appendix E.2 provides implementation details for Diffusion Policy.

<!-- chunk {"id": "body-0019", "role": "body", "section": "Problem Setting", "weight": 1.0} -->

Suppose we have access to a (small) dataset, $\mathcal{D}_{p} = {\{{(O^{(i)},A^{(i)})}\}}_{i = 1}^{n_{p}}$, from a target distribution, $p$, and a much larger dataset, $\mathcal{D}_{q} = {\{{(O^{(i)},A^{(i)})}\}}_{i = 1}^{n_{q}}$, from a shifted or suboptimal distribution, $q$. As discussed in the Introduction, this is a common problem setting in robotics.

<!-- chunk {"id": "body-0020", "role": "body", "section": "Problem Setting", "weight": 1.0} -->

The definitions of $p$ and $q$ can be arbitrary. In general, $\mathcal{D}_{p}$ is a dataset that a practitioner considers "high-quality" for a downstream application. In this paper, we define $\mathcal{D}_{p}$ as expert demonstrations on the target robot, environment, and task; however, our framework applies equally well to any other definition, including heuristic measures or human labels. In Section 7, we construct $\mathcal{D}_{q}$ to contain controlled distribution shifts. In Section 8, we scale $\mathcal{D}_{q}$ to Open X-Embodiment (OXE).

<!-- chunk {"id": "body-0021", "role": "body", "section": "Ambient Diffusion Omni", "weight": 1.0} -->

This Problem Statement is not unique to robotics. Ambient Diffusion Omni was proposed by Daras et al. to address a similar problem in the vision domain. Their key idea is to allow suboptimal samples from $q$ to be used only at certain diffusion times during training. The algorithm assigns two parameters to samples from $\mathcal{D}_{q}$, denoted $t_{\min}$ and $t_{\max}$. Samples from $\mathcal{D}_{q}$ can only contribute to the learning at diffusion times $t \in {{\lbrack 0,t_{\max})} \cup {(t_{\min},T\rbrack}}$.

<!-- chunk {"id": "body-0022", "role": "body", "section": "Ambient Diffusion Omni", "weight": 1.0} -->

The algorithm leverages noise as a contraction mechanism: for any distributions $p$ and $q$ supported on a subset of ${\mathbb{R}}^{d}$ with diameter $D$, the authors show that

<!-- chunk {"id": "body-0023", "role": "body", "section": "Ambient Diffusion Omni", "weight": 1.0} -->

Simply put, noise erases distribution differences, i.e. $p$ and $q$ contract towards one another. Hence, there exists a sufficiently high diffusion time, $t_{\min}$, for which noisy actions from both the high-quality and suboptimal distributions become effectively indistinguishable. Consequently, $\mathcal{D}_{q}$ can safely contribute to training at high noise when $t \in {(t_{\min},T\rbrack}$. The utility of $q$ is highest when $t_{\min}$ is small (i.e. when $p$ and $q$ contract quickly). We discuss sufficient conditions for fast contraction and justification for using $\mathcal{D}_{q}$ for $t \in {\lbrack 0,t_{\max})}$ in subsequent sections.

<!-- chunk {"id": "body-0024", "role": "body", "section": "Ambient Diffusion Omni", "weight": 1.0} -->

Section 4 examines structural properties of action data that make this method well-suited for robotics. Section 5 theoretically formalizes the discussion in both Section 4 and prior work. Section 6 outlines our algorithm. Despite the in-depth motivation, the resulting method is remarkably simple: it requires a single change to the Diffusion Policy data sampler. We conclude with experiments that demonstrate the generality and scalability of our method.

<!-- chunk {"id": "body-0025", "role": "body", "section": "Distributional Properties of Robot Data", "weight": 1.0} -->

We empirically show that robot data exhibits a spectral power law. This spectral structure is special for two reasons. First, it is not universal: it is absent in natural audio, stellar spectra, and Poisson point processes. Second, we show that it makes Ambient Diffusion effective: it implies a global-to-local hierarchy (Figure 2), fast contraction through noise (Theorem 1. ‣ 5.1 Contraction Through Noise ‣ 5 Theoretical Foundations ‣ Ambient Diffusion Policy: Imitation Learning from Suboptimal Data in Robotics")), and a locality property (Theorem 2. ‣ 5.2 Spectral Power Law Implies Locality ‣ 5 Theoretical Foundations ‣ Ambient Diffusion Policy: Imitation Learning from Suboptimal Data in Robotics")). Hence, Ambient Diffusion is well-suited for robotics.

<!-- chunk {"id": "body-0026", "role": "body", "section": "Spectral Power Law in Robotics", "weight": 1.0} -->

The power spectral density (PSD) of a signal measures its energy at each frequency component, $f$. The signal exhibits a spectral power law if its PSD decays approximately as ${|f|}^{- \alpha}$, where $\alpha > 0$. In other words, its energy is concentrated in low-frequency components. A formal definition extended to random vectors is presented in Definition 1. ‣ 5 Theoretical Foundations ‣ Ambient Diffusion Policy: Imitation Learning from Suboptimal Data in Robotics"). Figures 3(a) ‣ 4.1 Spectral Power Law in Robotics ‣ 4 Distributional Properties of Robot Data ‣ Ambient Diffusion Policy: Imitation Learning from Suboptimal Data in Robotics") and 11 show that robot action data exhibits a spectral power law.

<!-- chunk {"id": "body-0027", "role": "body", "section": "Spectral Power Law in Robotics", "weight": 1.0} -->

(a) Spectral power law in robot action data. The power spectral density for OXE, a collection of 2.4M robot episodes across 70+ datasets, follows a power law. Figure 11 shows that this spectral power law is a more general property of robot data.

<!-- chunk {"id": "body-0028", "role": "body", "section": "Spectral Power Law in Robotics", "weight": 1.0} -->

(b) Locality in robot action data. Visualizing the sensitivity of the 8th action estimate to its neighboring actions (Eq. ). At low noise, the 8th action estimate is most sensitive to its temporal neighbors.

<!-- chunk {"id": "body-0029", "role": "body", "section": "Spectral Power Law in Robotics", "weight": 1.0} -->

Implications for Diffusion Policy: When a spectral power law exists, Dieleman showed that denoisers generate low-frequency features at high noise, and high-frequency features at low noise. Figure 4 illustrates that in robotics, low frequencies encode global features (e.g. the high-level plan), while high frequencies encode local features (e.g. grasping primitives and smoothness). Thus, Diffusion Policies exhibit a global-to-local hierarchy: they learn global planning at high noise and local motion primitives at low noise. Appendix D provides further experimental evidence.

<!-- chunk {"id": "body-0030", "role": "body", "section": "Spectral Power Law in Robotics", "weight": 1.0} -->

This hierarchy unlocks a new design axis for co-training algorithms in robotics: noise-dependent data usage. Diffusion Policies learn different features of the actions at each noise level; thus, suboptimal samples should only contribute to training at noise levels where $p$ and $q$ align.

<!-- chunk {"id": "body-0031", "role": "body", "section": "Spectral Power Law in Robotics", "weight": 1.0} -->

Implications for Ambient Diffusion Policy: Due to the spectral power law, adding Gaussian noise to robot data acts as a high-frequency mask (Figure 4). Thus, if differences between $p$ and $q$ are concentrated in a high-frequency tail (i.e. low-level actions), then $t_{\min}$ will be small. We formalize this in Theorem 1. ‣ 5.1 Contraction Through Noise ‣ 5 Theoretical Foundations ‣ Ambient Diffusion Policy: Imitation Learning from Suboptimal Data in Robotics"). By only learning from suboptimal samples when $t > t_{\min}$, policies can learn the useful global features in $\mathcal{D}_{q}$ and ignore the local suboptimality (which is masked by noise).

<!-- chunk {"id": "body-0032", "role": "body", "section": "Spectral Power Law in Robotics", "weight": 1.0} -->

Fortunately, the suboptimality in many robot datasets is in the local actions. For instance, non-expert and expert demonstrations may aim to achieve the same goal, but differ in the quality of the low-level motions. Similarly, in sim-to-real co-training or cross-embodied data, the high-level plan may be shared while the precise contact dynamics or feasible motions may differ.

<!-- chunk {"id": "body-0033", "role": "body", "section": "Locality in Robotics", "weight": 1.0} -->

A denoiser exhibits "locality" if its output at each coordinate depends primarily on a small receptive field in the noisy input.^22^2As in Lukoianov et al., "locality" is a property of the data which is inherited by the optimal denoiser at low noise. We use the term "locality" loosely as both a property of the data and the resulting denoisers. In robotics, this means that each action output from the denoiser is most sensitive to its temporal neighbors in the noisy input. In Theorem 2. ‣ 5.2 Spectral Power Law Implies Locality ‣ 5 Theoretical Foundations ‣ Ambient Diffusion Policy: Imitation Learning from Suboptimal Data in Robotics"), we prove that the spectral power law can imply locality in the optimal denoisers. Indeed, Figure 3(b) ‣ 4.1 Spectral Power Law in Robotics ‣ 4 Distributional Properties of Robot Data ‣ Ambient Diffusion Policy: Imitation Learning from Suboptimal Data in Robotics") empirically identifies this phenomenon in robotics. Intuitively, this is because these denoisers focus on resolving local motion primitives, so they do not need to attend to distant actions in the input.

<!-- chunk {"id": "body-0034", "role": "body", "section": "Locality in Robotics", "weight": 1.0} -->

Now suppose that $p$ and $q$ share the same local motion primitives but differ globally. Due to locality, there exists a sufficiently small $t_{\max}$ such that for all $t < t_{\max}$, $p$ and $q$ agree within the receptive field of the optimal denoiser. Section 5 formalizes this statement. Section 7.4 leverages locality to learn local grasping primitives from data at low noise, even when its task-level structure is incorrect.

<!-- chunk {"id": "body-0035", "role": "body", "section": "Locality in Robotics", "weight": 1.0} -->

Remark: A spectral power law and locality exists in all the examined robot datasets (Table 4). This suggests that these are general properties of robot data. Section 6 provides methods for estimating $t_{\min}$ and $t_{\max}$ to leverage these properties in Ambient Diffusion Policy.

<!-- chunk {"id": "body-0036", "role": "body", "section": "Theoretical Foundations", "weight": 1.0} -->

We prove two theorems that extend the theoretical foundations of Ambient Diffusion and rigorously justify our method for robotics. Prior works empirically identify the spectral power law and locality as important properties. We prove that for a simplified model, the former implies both fast contraction through noise (Theorem 1. ‣ 5.1 Contraction Through Noise ‣ 5 Theoretical Foundations ‣ Ambient Diffusion Policy: Imitation Learning from Suboptimal Data in Robotics")) and locality of the optimal denoiser (Theorem 2. ‣ 5.2 Spectral Power Law Implies Locality ‣ 5 Theoretical Foundations ‣ Ambient Diffusion Policy: Imitation Learning from Suboptimal Data in Robotics")). This establishes the spectral power law as the single fundamental property underlying the framework.

<!-- chunk {"id": "body-0037", "role": "body", "section": "Theoretical Foundations", "weight": 1.0} -->

Both theorems are proved for zero-mean stationary Gaussians. We adopt this setting for two reasons: 1) it simplifies the bounds, and 2) it is a natural model for latent-space diffusion, which has been proposed in robotics, and is common in generative modeling more broadly. Extending the analysis to general distributions is left to future work. Proofs are presented in Appendix A.

<!-- chunk {"id": "body-0038", "role": "body", "section": "Theoretical Foundations", "weight": 1.0} -->

We begin by formally defining the spectral power law for general random vectors.

<!-- chunk {"id": "body-0039", "role": "body", "section": "Contraction Through Noise", "weight": 1.0} -->

Theorem 1. ‣ 5.1 Contraction Through Noise ‣ 5 Theoretical Foundations ‣ Ambient Diffusion Policy: Imitation Learning from Suboptimal Data in Robotics") states that a spectral power law and low-frequency alignment between $p$ and $q$ imply fast contraction through noise. Moreover, this contraction is independent of the original distance.

<!-- chunk {"id": "body-0040", "role": "body", "section": "Spectral Power Law Implies Locality", "weight": 1.0} -->

The next theorem shows that the spectral power law implies locality for the optimal denoiser at low noise levels.

<!-- chunk {"id": "body-0041", "role": "body", "section": "Ambient Diffusion Policy: Method", "weight": 1.0} -->

Since robot data exhibits a spectral power law, learning from suboptimal data in robotics with Ambient is empirically and theoretically justified. We now present our algorithm: Ambient Diffusion Policy. It has two phases: a) data annotation, and b) training.

<!-- chunk {"id": "body-0042", "role": "body", "section": "Phase 1: Dataset annotation", "weight": 1.0} -->

This phase annotates $t_{\max}$ and $t_{\min}$ for the suboptimal samples from $\mathcal{D}_{q}$. The simplest method is to perform a hyperparameter sweep. A more principled solution is to use a classification network. In particular, $\sigma_{t_{\min}}$ corresponds to the minimal amount of noise required to make the distributions $p_{t}$ and $q_{t}$ indistinguishable. Hence, one way to find this noise level is to train a classifier, $c_{\phi}{(A_{t},t)}$ that predicts the probability that the noisy action $A_{t}$ came from $p_{t}$ (as opposed to $q_{t}$).

<!-- chunk {"id": "body-0043", "role": "body", "section": "Phase 1: Dataset annotation", "weight": 1.0} -->

Then, $t_{\min}$ is the minimum noise level required to fool the classifier into classifying samples from $q_{t}$ as samples from $p_{t}$ (i.e. the classifier cannot reliably distinguish $p_{t}$ and $q_{t}$). Formally, for some small $\tau > 0$, we assign

<!-- chunk {"id": "body-0044", "role": "body", "section": "Phase 1: Dataset annotation", "weight": 1.0} -->

This classifier can also be used to annotate samples at different granularities (e.g. one $t_{\min}$ per dataset vs one $t_{\min}$ per sample); Appendix G.3 and Figure 1919(f) ‣ Fig. 19 ‣ G.3 Sim-and-Real Co-training: Planar Pushing ‣ Appendix G Controlled Experiments ‣ Ambient Diffusion Policy: Imitation Learning from Suboptimal Data in Robotics") provide additional details. A similar classifier-based approach can be used to annotate $t_{\max}$, although we do not use it in this paper.

<!-- chunk {"id": "body-0045", "role": "body", "section": "Phase 2: Training", "weight": 1.0} -->

The training loop for Ambient Diffusion Policy is the same as Diffusion Policy with one required change: a custom data sampler. The custom sampler first draws a batch of diffusion times $t^{(i)} \sim {\mathcal{U}{\lbrack 0,T\rbrack}}$. Afterward, it draws admissible samples from $\mathcal{D}_{p} \cup \mathcal{D}_{q}$. Samples from $\mathcal{D}_{p}$ are always admissible; suboptimal samples from $\mathcal{D}_{q}$ are admissible only if $t^{(i)} \in {{\lbrack 0,t_{\max})} \cup {(t_{\min},T\rbrack}}$. Figure 1 visualizes the intervals where each dataset can contribute to training. Inference is identical to Diffusion Policy. We defer the full training pseudocode to Appendix E.1 to prevent implementation details from obscuring the essence of the method.

<!-- chunk {"id": "body-0046", "role": "body", "section": "Phase 2: Training", "weight": 1.0} -->

Variants of Ambient Diffusion Policy. Ambient Diffusion Policy provides an (optional) alternative loss function, which is discussed in Appendix C. Additionally, there is a variation of the algorithm that uses the classifier from Phase 1 for rejection sampling at training-time. We provide pseudocode and theoretical justification in Appendix E.3 and leave experimental verification of this variant to future work.

<!-- chunk {"id": "body-0047", "role": "body", "section": "Controlled Experiments", "weight": 1.0} -->

We evaluate Ambient Diffusion Policy on three distribution shifts in robot action data to illustrate its generality: noisy trajectories, sim-to-real gap, and task mismatch. This section compares our method against data filtering, co-training, and finetuning. Appendix F provides experimental details.

<!-- chunk {"id": "body-0048", "role": "body", "section": "Noisy Trajectories", "weight": 1.0} -->

Consider a 2D point robot that must navigate between random start and goal positions in a maze environment (Figure 1a). A policy rollout is successful if it reaches an $\epsilon$-ball around the goal within a time limit without collision. We measure a policy's global understanding of the maze using success rate, and its local smoothness using average squared acceleration (Eq. ).

<!-- chunk {"id": "body-0049", "role": "body", "section": "Noisy Trajectories", "weight": 1.0} -->

$\mathcal{D}_{p}$ contains 50 smooth trajectories from GCS; $\mathcal{D}_{q}$ contains 5,000 cheaper but jittery trajectories from RRT. Figure 5 visualizes the datasets. This mimics real-world sources of suboptimality, such as teleoperation with low-quality hardware or noisy control stacks.

<!-- chunk {"id": "body-0050", "role": "body", "section": "Noisy Trajectories", "weight": 1.0} -->

The policy trained with data filtering is smooth, but performs poorly (Table 1(a) ‣ Table 1 ‣ 7.1 Noisy Trajectories ‣ 7 Controlled Experiments ‣ Ambient Diffusion Policy: Imitation Learning from Suboptimal Data in Robotics")). Co-training and Ambient both perform well (${99.0\%} +$ success), but the Ambient Diffusion Policy is 2$\times$ smoother. This is because RRT's jittery behavior is a local property; thus, excluding it from training at low diffusion times prevents the policy from learning its non-smooth behavior. Figure 14 (Appendix G.1) visualizes the rollouts. Lastly, training on $\mathcal{D}_{q}$ trades smoothness for better data coverage and success rates. Ambient's Pareto frontier for this trade-off strictly dominates the co-training baseline (Figure 6(a) ‣ Fig. 6 ‣ 7.1 Noisy Trajectories ‣ 7 Controlled Experiments ‣ Ambient Diffusion Policy: Imitation Learning from Suboptimal Data in Robotics")).

<!-- chunk {"id": "body-0051", "role": "body", "section": "Noisy Trajectories", "weight": 1.0} -->

Ablation: We claim that $p_{t} \approx q_{t}$ for $t > t_{\min}$. If this were true, then we should be able to train an effective policy without using $\mathcal{D}_{p}$ for $t > t_{\min}$. To test this, we train a policy that exclusively trains on $\mathcal{D}_{q}$ for $t \in {(t_{\min},T\rbrack}$ and $\mathcal{D}_{p}$ for $t \in {\lbrack 0,t_{\min}\rbrack}$. Remarkably, it matches the performance of the Ambient Diffusion Policy, with a success rate of $99.0\%$ and a squared acceleration of $29.9$.

<!-- chunk {"id": "body-0052", "role": "body", "section": "Neural Motion Planning", "weight": 1.0} -->

We extend the maze experiment to neural motion planning with a 7-DoF robot arm in a cluttered environment (Figure 1b). The setup and metrics are analogous to the 2D maze, except that start and goal configurations are sampled around objects and shelves, and the planner predicts the entire plan open-loop. Appendix Table 7 compares the two setups. The main results in Table 1(b) ‣ Table 1 ‣ 7.1 Noisy Trajectories ‣ 7 Controlled Experiments ‣ Ambient Diffusion Policy: Imitation Learning from Suboptimal Data in Robotics") and Figure 6(b) ‣ Fig. 6 ‣ 7.1 Noisy Trajectories ‣ 7 Controlled Experiments ‣ Ambient Diffusion Policy: Imitation Learning from Suboptimal Data in Robotics") mirror the 2D maze experiments: Ambient achieves the highest success rate while remaining substantially smoother than co-training. The full experimental details and ablations are in Appendix G.2.

<!-- chunk {"id": "body-0053", "role": "body", "section": "Neural Motion Planning", "weight": 1.0} -->

Implications for Neural Motion Planning (NMP). Most neural motion planners are trained on large datasets of sampling-based trajectories (akin to $\mathcal{D}_{q}$) since they are inexpensive to generate. Unfortunately, sampling-based trajectories are non-smooth; thus, these approaches choose to prioritize data scale over quality. Our results suggest that an NMP trained with Ambient can enjoy the best of both worlds: augmenting the existing sampling-based datasets with a small amount of high-quality data could yield planners that are both general and smooth.

<!-- chunk {"id": "body-0054", "role": "body", "section": "Sim-to-Real Distribution Shift", "weight": 1.0} -->

We evaluate Ambient Diffusion Policy on sim-and-real co-training using the planar pushing setup from (Figure 1c), a canonical task in robot imitation learning. Our experiments use the sim-and-target problem from Wei et al. as a controlled proxy for the sim-and-real problem.

<!-- chunk {"id": "body-0055", "role": "body", "section": "Sim-to-Real Distribution Shift", "weight": 1.0} -->

$\mathcal{D}_{p}$ consists of 50 teleoperated demonstrations in the target environment; $\mathcal{D}_{q}$ consists of 2000 trajectories generated by a motion planner in the simulated environment. We use the same datasets from Wei et al. to enable direct comparisons with their method. A policy rollout is successful if it pushes the T to the target pose within a time limit.

<!-- chunk {"id": "body-0056", "role": "body", "section": "Sim-to-Real Distribution Shift", "weight": 1.0} -->

Ambient (tmin per dataset)
Ambient (tmin per datapoint)
Ambient + Locality (σtmax = 0.025)

<!-- chunk {"id": "body-0057", "role": "body", "section": "Sim-to-Real Distribution Shift", "weight": 1.0} -->

Table 2 reports the success rate for three variations of Ambient Diffusion Policy that annotate $t_{\min}$ at two granularities: per dataset (with a parameter sweep) and per datapoint (with the classifier approach). We explore intermediate granularities, scaling laws, and more ablations in Appendix G.3. All Ambient variations outperform the best co-trained policy. Annotating $t_{\min}$ per datapoint performs the best because even within a single dataset, the utility of each datapoint can vary. As before, Ambient learns from suboptimal simulation data by leveraging the diffusion hierarchy. $\mathcal{D}_{p}$ and $\mathcal{D}_{q}$ share the same high-level strategy; thus, $\mathcal{D}_{q}$ is safe to use at high noise. Locality ($t_{\max} > 0$) does not help since $\mathcal{D}_{p}$ and $\mathcal{D}_{q}$ exhibit different low-level contact dynamics.

<!-- chunk {"id": "body-0058", "role": "body", "section": "Task Mismatch", "weight": 1.0} -->

Ambient can leverage "locality" to learn local action primitives (e.g., grasping) from data collected on a different task. Consider the block sorting task in Figure 1d. The robot must sort red and blue blocks into the left and right bins, respectively. This requires two distinct skills: motion (grasping and placing blocks) and logic (selecting the correct bin).

<!-- chunk {"id": "body-0059", "role": "body", "section": "Task Mismatch", "weight": 1.0} -->

Motion metric: $\frac{\text{\# blocks placed}}{\text{\# total blocks}}$. This metric is independent of logical reasoning because the numerator counts any placed block, regardless of logical correctness.

<!-- chunk {"id": "body-0060", "role": "body", "section": "Task Mismatch", "weight": 1.0} -->

Logic metric: $\frac{\text{\# blocks placed correctly}}{\text{\# blocks placed}}$. This metric is independent of pick-and-place ability because the denominator only counts successfully placed blocks.

<!-- chunk {"id": "body-0061", "role": "body", "section": "Task Mismatch", "weight": 1.0} -->

The overall success rate is $\frac{\text{\# blocks placed correctly}}{\text{\# total blocks}}$, the product of the two metrics. $\mathcal{D}_{p}$ contains 50 demonstrations with the correct sorting. $\mathcal{D}_{q}$ contains 200 demonstrations with the opposite sorting. To isolate the effect of locality, we set $t_{\min} = 0$ and sweep $t_{\max}$ for $\mathcal{D}_{q}$.

<!-- chunk {"id": "body-0062", "role": "body", "section": "Task Mismatch", "weight": 1.0} -->

Table 3 presents the results. Co-training performs poorly because training on $\mathcal{D}_{q}$ at all diffusion times teaches the policy both the useful motion primitives and the incorrect logic. Ambient Diffusion Policy solves this problem by restricting $\mathcal{D}_{q}$ to $t \in {\lbrack 0,t_{\max})}$. As illustrated in Figures 2 and 7, the policy learns motion primitives at low diffusion times without attending to the (incorrect) task-level structure of the demonstrations. This results in near-perfect scores on both metrics simultaneously.

<!-- chunk {"id": "body-0063", "role": "body", "section": "Task Mismatch", "weight": 1.0} -->

Ablations: We present two ablations in Appendix G.4. 1) we add a one-hot encoding indicating the sorting direction to the policies. Ambient still outperforms the co-training. 2) we train a policy that exclusively uses $\mathcal{D}_{q}$ for $t \in {\lbrack 0,t_{\max})}$ and $\mathcal{D}_{p}$ for $t \in {\lbrack t_{\max},T\rbrack}$. This is the locality-version of the ablation in the 2D maze experiment. The resulting policy achieves a logic and motion score of $97.9\%$ and $93.8\%$, reinforcing our claim that action diffusion is hierarchical.

<!-- chunk {"id": "body-0064", "role": "body", "section": "Finetuning Comparison", "weight": 1.0} -->

Finally, we compare against the finetuning baseline. For each experiment, we finetune the best co-trained policy and the best Ambient policy on $\mathcal{D}_{p}$; implementation details are in Appendix I.1.

<!-- chunk {"id": "body-0065", "role": "body", "section": "Scaling Experiments: Open X-Embodiment", "weight": 1.0} -->

Having shown the generality of Ambient Diffusion Policy, we now scale to Open X-Embodiment (OXE). OXE is a large collection of real-world data with heterogeneous quality and unstructured distribution shifts. Our goal is to extract useful learning signal from as much of this "suboptimal" data as possible. The experiments evaluate Ambient Diffusion Policy on two real-world tasks.

<!-- chunk {"id": "body-0066", "role": "body", "section": "Scaling Experiments: Open X-Embodiment", "weight": 1.0} -->

1\) Table Cleaning (Figure 1e): the robot must open the drawer, place objects inside, and close the drawer. The diversity of the test-time objects (unseen during training) makes this challenging. Performance is measured with the task completion rubric in Table 11.

<!-- chunk {"id": "body-0067", "role": "body", "section": "Scaling Experiments: Open X-Embodiment", "weight": 1.0} -->

2\) Tower Building (Figure 1f): the robot must stack blocks in alternating directions and colors as high as possible. This task requires precise manipulation since placement errors compound as the tower grows. Performance is measured by the number of blocks placed before toppling the tower.

<!-- chunk {"id": "body-0068", "role": "body", "section": "Scaling Experiments: Open X-Embodiment", "weight": 1.0} -->

The training procedure for both tasks is identical. $\mathcal{D}_{p}$ consists of a small number of demonstrations for each task. $\mathcal{D}_{q}$ is one of two subsets of the Open X-Embodiment (OXE) dataset: 1) Magic Soup++ (MS++), 27 datasets from OXE used by OpenVLA, or 2) Custom OXE (COXE), 48 datasets from OXE that contain MS++ as a subset. $t_{\min}$ and $t_{\max}$ are annotated according to Phase 1 of the method. We note that COXE was curated to be as inclusive as possible; details are in Appendix H.1.

<!-- chunk {"id": "body-0069", "role": "body", "section": "Scaling Experiments: Open X-Embodiment", "weight": 1.0} -->

Lastly, for both co-training and Ambient, we re-weight each dataset's sampling probability at every diffusion time. Let $w_{i}$ denote the weight for dataset $i$, and $S_{t}$ denote the indices of datasets that are permissible at diffusion time $t$. The sampling probability of dataset $i$ at diffusion time $t$ is

<!-- chunk {"id": "body-0070", "role": "body", "section": "Scaling Experiments: Open X-Embodiment", "weight": 1.0} -->

In co-training, $S_{t}$ contains all datasets for all $t \in {\lbrack 0,T\rbrack}$; in Ambient, $S_{t}$ depends on each dataset's $t_{\min}$ and $t_{\max}$ (see Figures 21 and 22). Re-weighting marginally improves the Ambient policies but is not required; in contrast, it is necessary for co-training (see Section 8.2).

<!-- chunk {"id": "body-0071", "role": "body", "section": "Main Results", "weight": 1.0} -->

Table Cleaning ($\mathcal{D}_{p}$ with 50 demos): Data filtering achieves $68.2\%$ task completion; co-training adds just 2-3% and plateaus when $\mathcal{D}_{q}$ scales from MS++ to COXE. On the other hand, the best Ambient Diffusion Policy outperforms co-training by $12\%$ and improves when $\mathcal{D}_{q}$ scales from MS++ to COXE. Adding locality ($t_{\max} > 0$) appears to provide further gains.

<!-- chunk {"id": "body-0072", "role": "body", "section": "Main Results", "weight": 1.0} -->

Table Cleaning ($\mathcal{D}_{p}$ with 150 demos): When $\mathcal{D}_{p}$ is large, data filtering improves to $80.1\%$, and training on suboptimal data provides less relative value. However, for many real-world tasks, collecting enough data in $\mathcal{D}_{p}$ could be prohibitively expensive. Nonetheless, Ambient continues to outperform co-training by up to $10\%$. Adding locality did not improve performance in this setting. We hypothesize that when $\mathcal{D}_{p}$ is large, the policy can learn the relevant motion primitives from $\mathcal{D}_{p}$, making data from $\mathcal{D}_{q}$ unnecessary or even harmful with the wrong choice of $t_{\max}$. This is consistent with the classifier annotation method, which would have assigned $t_{\max} = 0$ to nearly all datasets.

<!-- chunk {"id": "body-0073", "role": "body", "section": "Main Results", "weight": 1.0} -->

Tower Building ($\mathcal{D}_{p}$ with 35 demos): On average, the Ambient Diffusion Policies build up to $84\%$ and $33\%$ taller than the data filtering and co-training baselines, respectively (Figure 9). Including $\mathcal{D}_{q}$ at low diffusion times appears to improve performance.

<!-- chunk {"id": "body-0074", "role": "body", "section": "Ablations", "weight": 1.0} -->

Dataset Re-weighting: Figure 10 ablates the effect of re-weighting in Eq. on co-training and Ambient. Re-weighting improves policy performance on the table cleaning task by $3$--$9\%$. On the other hand, re-weighting is necessary for co-training: the unweighted co-trained policies were too unsafe to evaluate on hardware. This contrast highlights another practical advantage of Ambient: the training algorithm is inherently less sensitive to dataset weights because $\mathcal{D}_{q}$ is only used when $p_{t} \approx q_{t}$. Co-training uses $\mathcal{D}_{q}$ at all diffusion times, making the weights critical and fragile.

<!-- chunk {"id": "body-0075", "role": "body", "section": "Ablations", "weight": 1.0} -->

Additional Ablations: We present two further ablations in Appendix H.2. 1) Finetuning the OXE policies on $\mathcal{D}_{p}$ produced no statistically significant change in performance (Appendix I.2 ‣ Appendix I Finetuning ‣ Ambient Diffusion Policy: Imitation Learning from Suboptimal Data in Robotics")), consistent with the controlled experiments (Section 7.5). 2) On table cleaning, the Ambient Diffusion Policies require 25-40% fewer grasps and less time per object than their co-trained counterparts.

<!-- chunk {"id": "body-0076", "role": "body", "section": "Limitations and Future Work", "weight": 1.5} -->

Ambient Diffusion Policy does not yet handle distribution shifts in the observation space. We explore two initial attempts in Appendix J. The classifier-based annotation method for $t_{\min}$ and $t_{\max}$ is theoretically grounded, but does not always outperform a (costly) hyperparameter sweep. Better annotation methods could improve performance. In addition, the theory in Section 5 is limited to Gaussians; extending the results to a broader class of distributions could provide further insights. Lastly, our method is more computationally expensive than data filtering since it trains on more data, but in most cases, its benefits are worthwhile.

<!-- chunk {"id": "body-0077", "role": "body", "section": "Limitations and Future Work", "weight": 1.5} -->

Ambient Diffusion Policy requires the user to partition their data into $\mathcal{D}_{p}$ and $\mathcal{D}_{q}$. The algorithm itself poses no restrictions on this partitioning, but it is an important design decision for downstream performance. This paper defines $\mathcal{D}_{p}$ as data from the target task and environment, but the right choice depends on the goal. For task-specific training or finetuning, our definition is appropriate; for pretraining a generalist policy, prior work suggests that $\mathcal{D}_{p}$ should contain diverse and high-quality demonstrations. The former suggests that we could expand our finetuning dataset to include suboptimal data. The latter requires a more principled understanding of data quality in robotics. Both settings are exciting directions for future work.

<!-- chunk {"id": "body-0078", "role": "body", "section": "Conclusion", "weight": 1.5} -->

High-quality robot data is scarce, making it essential to learn from suboptimal data sources. But even as data collection scales, suboptimal data will continue to grow alongside high-quality data. Thus, the problem of learning from suboptimal data sources is not a temporary artifact of today's data scarcity, but rather a fundamental and persistent challenge in robot imitation learning. The dominant approach for addressing this problem is to filter the worst data and co-train on the rest via re-weighting; but filtering is wasteful, and co-training teaches a policy the meaningful and the harmful parts of suboptimal distributions. In this paper, we propose Ambient Diffusion Policy, a principled method for training on suboptimal demonstrations.

<!-- chunk {"id": "body-0079", "role": "body", "section": "Conclusion", "weight": 1.5} -->

Neighboring fields have recognized the power of noise-dependent data usage. Our key experimental and theoretical insight is that this training paradigm is also well-suited for robotics. Our method makes no assumptions about the nature of the action suboptimality, outperforms existing baselines, and greatly expands the set of useful data sources for robot imitation learning. With Ambient Diffusion Policy, the question shifts from which data sources should be used, to when each should be used in the diffusion process.
