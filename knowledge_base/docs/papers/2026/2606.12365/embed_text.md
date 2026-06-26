## Introduction

The training corpus of nearly every large-scale robot policy spans different tasks, real and simulated environments, embodiments, and even modalities. One reason for this data heterogeneity is that high-quality, task-specific robot data is expensive and time-consuming to collect; it requires skilled teleoperators and well-tuned low-level controllers. In contrast, suboptimal data is abundant. Any real-world data collection effort naturally produces failures and trajectories of differing quality. Out-of-distribution (OOD) data sources are also plentiful and widely available. These include simulation, cross-embodied data, and ego-centric video. Practitioners often draw from data sources of varying quality to create massive pretraining sets, yet methods for learning from arbitrary suboptimal or shifted distributions are underexplored in robotics. We propose a simple and principled method for training robot policies that can leverage suboptimal and OOD datasets.

The simplest way to handle heterogeneous datasets with mixed quality is to discard the lowest-quality samples, but this data filtering is wasteful: even suboptimal samples contain useful learning signal. The most common alternative in robotics is to "co-train" on everything while down-weighting suboptimal datasets. However, training a model to sample from a mixture with low-quality distributions fundamentally biases the policy. Finetuning is a complementary method, but can be insufficient alone (Section 7.5).

Our key intuition is that suboptimal and high-quality samples differ in some features, but align in others. For example, non-expert teleoperators may share the same high-level plan as experts, but exhibit less precise manipulation skills. Conversely, pick-and-place data may be useful for grasping primitives, but encode the wrong task.

We turn this intuition into an algorithm by observing that robotic data exhibits a spectral power law. We show that this spectral structure induces a *global-to-local hierarchy* in action diffusion and a locality property in the optimal denoisers. Concretely, Diffusion Policy learns high-level planning at high noise and motion primitives at low noise. Thus, a policy can selectively learn useful features from suboptimal data by using it only at noise levels where it aligns with the target distribution. This unlocks a new design axis for co-training in robotics: *noise-dependent data usage*.

To this end, we propose Ambient Diffusion Policy, a principled algorithm for training Diffusion Policies on suboptimal robot data. Each suboptimal sample can only contribute to training at the high or low diffusion times where it aligns with the target data. Our method extends the Ambient Diffusion Omni framework (or "Ambient" for short), which has been applied to computer vision and protein design. Our contributions are as follows: Properties of Robot Data. We empirically demonstrate that robot action data exhibits a spectral power law, which induces a global-to-local hierarchy and locality in action diffusion. These properties make Ambient Diffusion Omni well-suited for robotics (Section 4).

Ambient Diffusion Policy. We propose a simple and principled method for learning from suboptimal data that requires just a single change to Diffusion Policy's data sampler (Section 6).

Generality. Ambient outperforms baselines when training on three common types of action suboptimality: noisy demonstrations, sim-to-real gap, and task mismatch (Section 7).

Scale. When trained on Open X-Embodiment ---a large dataset with mixed data quality and unstructured distribution shifts---Ambient outperforms the co-training baseline by up to 33% on two real-world tasks. Additionally, Ambient continues to improve as we scale the amount of suboptimal data in the training mixture, whereas co-training plateaus (Section 8).

Theory. We prove that for a simple theoretical model, the spectral power law implies fast contraction through noise (Theorem 1. ‣ 5.1 Contraction Through Noise ‣ 5 Theoretical Foundations ‣ Ambient Diffusion Policy: Imitation Learning from Suboptimal Data in Robotics")) and locality (Theorem 2. ‣ 5.2 Spectral Power Law Implies Locality ‣ 5 Theoretical Foundations ‣ Ambient Diffusion Policy: Imitation Learning from Suboptimal Data in Robotics")) of the optimal policies. These contributions justify our algorithm and advance the theoretical foundations of the broader Ambient Diffusion framework (Section 5).

## Related Work

Dataset Re-weighting. The prevailing method for training on heterogeneous datasets in robotics is to re-weight each dataset's contribution to the loss. In our problem setting, this method would optimize the loss where $\mathcal{L}_{\mathcal{D}_{p}}$ and $\mathcal{L}_{\mathcal{D}_{q}}$ denote the loss on the target and suboptimal datasets, and $\alpha\in$ is the re-weighting parameter. In the remainder of the paper, we use "co-training" to refer to this standard approach. A core challenge is weight selection for each dataset. But even with the optimal weights, training a policy to sample from a mixture with suboptimal distributions biases the policy. Our method avoids this issue by only training on suboptimal samples in specific intervals of the diffusion process. Importantly, these intervals have precise interpretations and can be automatically annotated.

Data Filtering. A related method is data filtering, which rejects suboptimal samples entirely. Our experiments and prior work show that data filtering is wasteful. For example, Dexora improves policy performance by discarding 80% of its training demonstrations using a kinematic smoothness heuristic. Section 7.1 shows the opposite for Ambient Diffusion Policy: training on additional non-smooth demonstrations improves performance while retaining the policy's smoothness. Similarly, OpenVLA's Magic Soup++ mixture includes only 27 of the datasets in OXE; Section 8 shows that our method can still extract useful learning signal from the discarded datasets.

Learning from Suboptimal or OOD Data. Prior works studied learning from corrupted data; however, many require multiple training runs or rely on knowing the form of the corruption. The latter is unrealistic in robotics. For example, the sim-to-real gap has no closed-form description. Recent works in robotics have also begun exploring training methods for suboptimal data. $\pi_{0.7}$ labels data quality and LDA-1B relegates low-quality trajectories to an auxiliary dynamics objective. Other approaches learn invariant representations between the target and suboptimal data, but are challenging to scale. Tangkaratt et al. and Liu et al. propose methods for robust imitation learning; however, they focus on ignoring corrupted samples instead of learning from them. They also require over half the data to be high-quality. Concurrent work explored a similar idea to ours for hand-tracking data. In contrast, our method learns from arbitrary mixtures of suboptimal action data, scales to large real-world datasets, has theoretical grounding, and is simple to implement.

## Background

### Robot Imitation Learning and Diffusion Policy

Given a dataset $\mathcal{D}_{p}=\{(O^{(i)},A^{(i)})\}_{i=1}^{n_{p}}$ of observation-action pairs, imitation learning aims to train a policy $\pi(A\mid O)$ that approximates the conditional distribution $p(A\mid O)$. Here, $A$ and $O$ represent chunks of future actions and recent observations. Diffusion Policy samples from $\pi(A\mid O)$ with a conditional denoising process over the action space. Concretely, it learns a family of denoisers $\{h_{\theta}(A_{t},O,t)\}_{t\in[0,T]}$ that predict the clean action $A_{0}$ from a noisy version^11^1Diffusion Policy uses a variance-preserving implementation. We present it from the variance-exploding perspective to lighten notation. The two perspectives are equivalent up to a change of variables; see Appendix B. where $T$ is a sufficiently large constant, $\sigma(t)$ is a strictly increasing function known as the noise schedule, and $\sigma=0$. For brevity, we write $\sigma_{t}:=\sigma(t)$.

These denoisers are trained by minimizing the denoising loss (or a reparametrization of it, as in flow matching): where $t\sim\mathcal{U}[0,T]$, $(O,A_{0})\sim\mathcal{D}_{p}$, and $A_{t}$ is sampled from Eq.. For a sufficiently expressive $h_{\theta}$, the minimizer of Eq. is the conditional expectation $h_{\theta}^{*}(A_{t},O,t)=\mathbb{E}[A_{0}\mid A_{t},O]$. Given access to the conditional expectations, one can sample from the target distribution $\pi(A\mid O)$ by running a reverse diffusion process. Appendix E.2 provides implementation details for Diffusion Policy.

### Problem Setting

Suppose we have access to a (small) dataset, $\mathcal{D}_{p}=\{(O^{(i)},A^{(i)})\}_{i=1}^{n_{p}}$, from a target distribution, $p$, and a much larger dataset, $\mathcal{D}_{q}=\{(O^{(i)},A^{(i)})\}_{i=1}^{n_{q}}$, from a shifted or suboptimal distribution, $q$. As discussed in the Introduction, this is a common problem setting in robotics.

The definitions of $p$ and $q$ can be arbitrary. In general, $\mathcal{D}_{p}$ is a dataset that a practitioner considers "high-quality" for a downstream application. In this paper, we define $\mathcal{D}_{p}$ as expert demonstrations on the target robot, environment, and task; however, our framework applies equally well to any other definition, including heuristic measures or human labels. In Section 7, we construct $\mathcal{D}_{q}$ to contain controlled distribution shifts. In Section 8, we scale $\mathcal{D}_{q}$ to Open X-Embodiment (OXE).

### Ambient Diffusion Omni

This Problem Statement is not unique to robotics. Ambient Diffusion Omni was proposed by Daras et al. to address a similar problem in the vision domain. Their key idea is to allow suboptimal samples from $q$ to be used only at certain diffusion times during training. The algorithm assigns two parameters to samples from $\mathcal{D}_{q}$, denoted $t_{\min}$ and $t_{\max}$. Samples from $\mathcal{D}_{q}$ can only contribute to the learning at diffusion times $t\in[0,t_{\max})\cup(t_{\min},T]$.

The algorithm leverages noise as a contraction mechanism: for any distributions $p$ and $q$ supported on a subset of $\mathbb{R}^{d}$ with diameter $D$, the authors show that where $d_{\text{TV}}$ is the Total Variation distance, $p_{t}=p\circledast\mathcal{N}(0,\sigma_{t}I)$, and $q_{t}=q\circledast\mathcal{N}(0,\sigma_{t}I)$.

Simply put, noise erases distribution differences, i.e. $p$ and $q$ contract towards one another. Hence, there exists a sufficiently high diffusion time, $t_{\min}$, for which noisy actions from both the high-quality and suboptimal distributions become effectively indistinguishable. Consequently, $\mathcal{D}_{q}$ can safely contribute to training at high noise when $t\in(t_{\min},T]$. The utility of $q$ is highest when $t_{\min}$ is small (i.e. when $p$ and $q$ contract quickly). We discuss sufficient conditions for fast contraction and justification for using $\mathcal{D}_{q}$ for $t\in0,t_{\max})$ in subsequent sections.

Section [4 examines structural properties of action data that make this method well-suited for robotics. Section 5 theoretically formalizes the discussion in both Section 4 and prior work. Section 6 outlines our algorithm. Despite the in-depth motivation, the resulting method is remarkably simple: it requires a single change to the Diffusion Policy data sampler. We conclude with experiments that demonstrate the generality and scalability of our method.

## Distributional Properties of Robot Data

We empirically show that robot data exhibits a spectral power law. This spectral structure is special for two reasons. First, it is not universal: it is absent in natural audio, stellar spectra, and Poisson point processes. Second, we show that it makes Ambient Diffusion effective: it implies a global-to-local hierarchy (Figure 2), fast contraction through noise (Theorem 1. ‣ 5.1 Contraction Through Noise ‣ 5 Theoretical Foundations ‣ Ambient Diffusion Policy: Imitation Learning from Suboptimal Data in Robotics")), and a locality property (Theorem 2. ‣ 5.2 Spectral Power Law Implies Locality ‣ 5 Theoretical Foundations ‣ Ambient Diffusion Policy: Imitation Learning from Suboptimal Data in Robotics")). Hence, Ambient Diffusion is well-suited for robotics.

### Spectral Power Law in Robotics

Figure 2: The spectral power law induces a global-to-local hierarchy in action diffusion. This is analogous to the “coarse-to-fine” hierarchy in image diffusion. (a) t ≥ t2 (global planning): the policy commits to a high-level path through the maze. t < t2 (local refinement): it refines the plan to be collision-free at t1 and smooth at t0. (b) t3: the policy plans to move a block to the right bin. t2: it plans which block to grasp. t < t2: it refines the grasping motion.

The power spectral density (PSD) of a signal measures its energy at each frequency component, $f$. The signal exhibits a spectral power law if its PSD decays approximately as $|f|^{-\alpha}$, where $\alpha>0$. In other words, its energy is concentrated in low-frequency components. A formal definition extended to random vectors is presented in Definition 1. ‣ 5 Theoretical Foundations ‣ Ambient Diffusion Policy: Imitation Learning from Suboptimal Data in Robotics"). Figures 3(a) ‣ 4.1 Spectral Power Law in Robotics ‣ 4 Distributional Properties of Robot Data ‣ Ambient Diffusion Policy: Imitation Learning from Suboptimal Data in Robotics") and 11 show that robot action data exhibits a spectral power law.

(a) Spectral power law in robot action data. The power spectral density for OXE, a collection of 2.4M robot episodes across 70+ datasets, follows a power law. Figure 11 shows that this spectral power law is a more general property of robot data.

(b) Locality in robot action data. Visualizing the sensitivity of the 8th action estimate to its neighboring actions (Eq. ). At low noise, the 8th action estimate is most sensitive to its temporal neighbors.

Implications for Diffusion Policy: When a spectral power law exists, Dieleman showed that denoisers generate low-frequency features at high noise, and high-frequency features at low noise. Figure 4 illustrates that in robotics, low frequencies encode global features (e.g. the high-level plan), while high frequencies encode local features (e.g. grasping primitives and smoothness). Thus, Diffusion Policies exhibit a global-to-local hierarchy: they learn global planning at high noise and local motion primitives at low noise. Appendix D provides further experimental evidence.

Figure 4: The spectral power law makes Gaussian noise act as a high-frequency mask. (a) Noisy trajectory visualizations. (b) PSD analysis for the noisy trajectories in the x-dimension at each diffusion time: the gray regions indicate masked frequencies, which have low SNR. As t increases, adding Gaussian noise destroys the signal in the trajectory, starting from the local (high-frequency) features first. This effect is visible in both the noisy trajectories and the PSD plots.

This hierarchy unlocks a new design axis for co-training algorithms in robotics: noise-dependent data usage. Diffusion Policies learn different features of the actions at each noise level; thus, suboptimal samples should only contribute to training at noise levels where $p$ and $q$ align.

Implications for Ambient Diffusion Policy: Due to the spectral power law, adding Gaussian noise to robot data acts as a high-frequency mask (Figure 4). Thus, if differences between $p$ and $q$ are concentrated in a high-frequency tail (i.e. low-level actions), then $t_{\min}$ will be small. We formalize this in Theorem 1. ‣ 5.1 Contraction Through Noise ‣ 5 Theoretical Foundations ‣ Ambient Diffusion Policy: Imitation Learning from Suboptimal Data in Robotics"). By only learning from suboptimal samples when $t>t_{\min}$, policies can learn the useful global features in $\mathcal{D}_{q}$ and ignore the local suboptimality (which is masked by noise).

Fortunately, the suboptimality in many robot datasets is in the local actions. For instance, non-expert and expert demonstrations may aim to achieve the same goal, but differ in the quality of the low-level motions. Similarly, in sim-to-real co-training or cross-embodied data, the high-level plan may be shared while the precise contact dynamics or feasible motions may differ.

### Locality in Robotics

A denoiser exhibits "locality" if its output at each coordinate depends primarily on a small receptive field in the noisy input.^22^2As in Lukoianov et al., "locality" is a property of the data which is inherited by the optimal denoiser at low noise. We use the term "locality" loosely as both a property of the data and the resulting denoisers. In robotics, this means that each action output from the denoiser is most sensitive to its temporal neighbors in the noisy input. In Theorem 2. ‣ 5.2 Spectral Power Law Implies Locality ‣ 5 Theoretical Foundations ‣ Ambient Diffusion Policy: Imitation Learning from Suboptimal Data in Robotics"), we prove that the spectral power law can imply locality in the optimal denoisers. Indeed, Figure 3(b) ‣ 4.1 Spectral Power Law in Robotics ‣ 4 Distributional Properties of Robot Data ‣ Ambient Diffusion Policy: Imitation Learning from Suboptimal Data in Robotics") empirically identifies this phenomenon in robotics. Intuitively, this is because these denoisers focus on resolving local motion primitives, so they do not need to attend to distant actions in the input.

Now suppose that $p$ and $q$ share the same local motion primitives but differ globally. Due to locality, there exists a sufficiently small $t_{\max}$ such that for all $t<t_{\max}$, $p$ and $q$ agree within the receptive field of the optimal denoiser. Section 5 formalizes this statement. Section 7.4 leverages locality to learn local grasping primitives from data at low noise, even when its task-level structure is incorrect.

Remark: A spectral power law and locality exists in all the examined robot datasets (Table 4). This suggests that these are general properties of robot data. Section 6 provides methods for estimating $t_{\min}$ and $t_{\max}$ to leverage these properties in Ambient Diffusion Policy.

## Theoretical Foundations

We prove two theorems that extend the theoretical foundations of Ambient Diffusion and rigorously justify our method for robotics. Prior works empirically identify the spectral power law and locality as important properties. We prove that for a simplified model, the former implies both fast contraction through noise (Theorem 1. ‣ 5.1 Contraction Through Noise ‣ 5 Theoretical Foundations ‣ Ambient Diffusion Policy: Imitation Learning from Suboptimal Data in Robotics")) and locality of the optimal denoiser (Theorem 2. ‣ 5.2 Spectral Power Law Implies Locality ‣ 5 Theoretical Foundations ‣ Ambient Diffusion Policy: Imitation Learning from Suboptimal Data in Robotics")). This establishes the spectral power law as the single fundamental property underlying the framework.

Both theorems are proved for zero-mean stationary Gaussians. We adopt this setting for two reasons: 1) it simplifies the bounds, and 2) it is a natural model for latent-space diffusion, which has been proposed in robotics, and is common in generative modeling more broadly. Extending the analysis to general distributions is left to future work. Proofs are presented in Appendix A.

We begin by formally defining the spectral power law for general random vectors.

### Definition 1 (Spectral Power Law)

Let $X$ be a zero-mean, stationary random vector on $\mathbb{R}^{N}$, and let $S_{X}(f):=\mathbb{E}\big[|(\mathcal{F}X)(f)|^{2}\big]$ denote its power spectral density in the orthonormal Fourier basis. We say that the distribution of $X$ follows a spectral power law if there exist a constant $C>0$, a rolloff exponent $\alpha>1$, and a cutoff frequency $f_{0}\geq 1$ such that the high-frequency spectrum satisfies: The exact spectral behavior below the cutoff $f_{0}$ is permitted to be arbitrary but bounded.

### Contraction Through Noise

Theorem 1. ‣ 5.1 Contraction Through Noise ‣ 5 Theoretical Foundations ‣ Ambient Diffusion Policy: Imitation Learning from Suboptimal Data in Robotics") states that a spectral power law and low-frequency alignment between $p$ and $q$ imply fast contraction through noise. Moreover, this contraction is independent of the original distance.

### Theorem 1 (Spectral Power Law implies fast contraction through noise)

Let $p_{0}=\mathcal{N}(0,\Sigma_{p})$ and $q_{0}=\mathcal{N}(0,\Sigma_{q})$ be zero-mean stationary Gaussians on $\mathbb{R}^{N}$ with power spectra $S_{p},S_{q}$. Fix a cutoff frequency $f^{\star}\geq 1$, an exponent $\alpha>\tfrac{1}{2}$, and a constant $C>0$. Assume: (Low-frequency agreement.) $S_{p}(f)=S_{q}(f)$ for every $f\leq f^{\star}$.

(Power-law tail.) $\max(S_{p}(f),S_{q}(f))\leq Cf^{-\alpha}$ for every $f$ such that $f^{\star}<f\leq\lfloor N/2\rfloor$.

Let $p_{t}:=p_{0}*\mathcal{N}(0,\sigma_{t}^{2}I)$ and $q_{t}:=q_{0}*\mathcal{N}(0,\sigma_{t}^{2}I)$. If In contrast, Eq. depends on the original TV distance (which can be arbitrarily close to 1) and decays only as $1/\sigma$. For our simple theoretical model, the spectral power law enables fast contraction and, consequently, high utilization of the suboptimal data in Ambient Diffusion.

### Spectral Power Law Implies Locality

The next theorem shows that the spectral power law implies locality for the optimal denoiser at low noise levels.

### Theorem 2 (Spectral Power Law implies locality of the optimal denoiser)

Let $X_{0}\sim\mathcal{N}(0,\Sigma)$ be a zero-mean stationary Gaussian on $\mathbb{R}^{N}$ whose power spectrum $S(f)$ follows a spectral power law with constant $C>0$ and exponent $\alpha>1$. Let $X_{t}=X_{0}+\sigma_{t}Z$ be the variance-exploding noisy observation, and $h^{\star}_{t}(x):=\mathbb{E}[X_{0}\mid X_{t}=x]$ denote the MMSE optimal denoiser.

Let $M_{i}$ be a circulant mask that sets to zero all coordinates of the input $x$ at a circular distance strictly greater than $L$ from index $i$. Then, for any mask size $1\leq L\leq\lfloor N/2\rfloor$, the absolute error in the $i$-th coordinate between the full optimal denoiser and the masked denoiser is bounded: In short, at low noise levels the optimal denoiser is functionally myopic: it can reconstruct the signal by observing only a local spatial neighborhood, safely ignoring the global structure of the input. This is precisely the property that Ambient Diffusion Policy exploits to learn local action primitives from suboptimal data, even when its global structure is incorrect (Section 7.4).

## Ambient Diffusion Policy: Method

Since robot data exhibits a spectral power law, learning from suboptimal data in robotics with Ambient is empirically and theoretically justified. We now present our algorithm: Ambient Diffusion Policy. It has two phases: a) data annotation, and b) training.

### Phase 1: Dataset annotation

This phase annotates $t_{\max}$ and $t_{\min}$ for the suboptimal samples from $\mathcal{D}_{q}$. The simplest method is to perform a hyperparameter sweep. A more principled solution is to use a classification network. In particular, $\sigma_{t_{\min}}$ corresponds to the minimal amount of noise required to make the distributions $p_{t}$ and $q_{t}$ indistinguishable. Hence, one way to find this noise level is to train a classifier, $c_{\phi}(A_{t},t)$ that predicts the probability that the noisy action $A_{t}$ came from $p_{t}$ (as opposed to $q_{t}$). Then, $t_{\min}$ is the minimum noise level required to fool the classifier into classifying samples from $q_{t}$ as samples from $p_{t}$ (i.e. the classifier cannot reliably distinguish $p_{t}$ and $q_{t}$). Formally, for some small $\tau>0$, we assign Figure 13 visualizes this method for $\tau=0.05$; details are in the Appendix. If the classifier is well-trained, we show that this annotation method guarantees distributional closeness between $p_{t}$ and $q_{t}$ for $t>t_{\min}$ (Theorem 4. ‣ Classifier threshold implies distributional closeness. ‣ A.3 Theoretical Justification of the Classifier-Based Annotation ‣ Appendix A Ambient Diffusion: Theoretical Foundations ‣ Ambient Diffusion Policy: Imitation Learning from Suboptimal Data in Robotics")).

This classifier can also be used to annotate samples at different granularities (e.g. one $t_{\min}$ per dataset vs one $t_{\min}$ per sample); Appendix G.3 and Figure 1919(f) ‣ Fig. 19 ‣ G.3 Sim-and-Real Co-training: Planar Pushing ‣ Appendix G Controlled Experiments ‣ Ambient Diffusion Policy: Imitation Learning from Suboptimal Data in Robotics") provide additional details. A similar classifier-based approach can be used to annotate $t_{\max}$, although we do not use it in this paper.

### Phase 2: Training

The training loop for Ambient Diffusion Policy is the same as Diffusion Policy with one required change: a custom data sampler. The custom sampler first draws a batch of diffusion times $t^{(i)}\sim\mathcal{U}[0,T]$. Afterward, it draws admissible samples from $\mathcal{D}_{p}\cup\mathcal{D}_{q}$. Samples from $\mathcal{D}_{p}$ are always admissible; suboptimal samples from $\mathcal{D}_{q}$ are admissible only if $t^{(i)}\in[0,t_{\max})\cup(t_{\min},T]$. Figure 1 visualizes the intervals where each dataset can contribute to training. Inference is identical to Diffusion Policy. We defer the full training pseudocode to Appendix E.1 to prevent implementation details from obscuring the essence of the method.

Variants of Ambient Diffusion Policy. Ambient Diffusion Policy provides an (optional) alternative loss function, which is discussed in Appendix C. Additionally, there is a variation of the algorithm that uses the classifier from Phase 1 for rejection sampling at training-time. We provide pseudocode and theoretical justification in Appendix E.3 and leave experimental verification of this variant to future work.

## Controlled Experiments

We evaluate Ambient Diffusion Policy on three distribution shifts in robot action data to illustrate its generality: noisy trajectories, sim-to-real gap, and task mismatch. This section compares our method against data filtering, co-training, and finetuning. Appendix F provides experimental details.

### Noisy Trajectories

Figure 5: GCS (left) vs RRT (right) data. The high-quality GCS trajectories are smoother and shorter than their RRT counterparts.

Consider a 2D point robot that must navigate between random start and goal positions in a maze environment (Figure 1a). A policy rollout is successful if it reaches an $\epsilon$-ball around the goal within a time limit without collision. We measure a policy's global understanding of the maze using success rate, and its local smoothness using average squared acceleration (Eq.). $\mathcal{D}_{p}$ contains 50 smooth trajectories from GCS; $\mathcal{D}_{q}$ contains 5,000 cheaper but jittery trajectories from RRT. Figure 5 visualizes the datasets. This mimics real-world sources of suboptimality, such as teleoperation with low-quality hardware or noisy control stacks.

(b) 7-DoF neural motion planning.

Table 1: Maze and Neural Motion Planning results (1000 trials each). In both settings, Ambient Diffusion Policy achieves the highest success rate and is substantially smoother than co-training.

(b) 7-DoF neural motion planning.

Figure 6: The “smoothness vs success rate” Pareto frontier for Ambient (blue) dominates co-training (red) in both the (a) maze and (b) neural motion planning experiments. This trade-off is controlled by σtmin for Ambient and α for co-training.

The policy trained with data filtering is smooth, but performs poorly (Table 1(a) ‣ Table 1 ‣ 7.1 Noisy Trajectories ‣ 7 Controlled Experiments ‣ Ambient Diffusion Policy: Imitation Learning from Suboptimal Data in Robotics")). Co-training and Ambient both perform well ($99.0\%+$ success), but the Ambient Diffusion Policy is 2$\times$ smoother. This is because RRT's jittery behavior is a local property; thus, excluding it from training at low diffusion times prevents the policy from learning its non-smooth behavior. Figure 14 (Appendix G.1) visualizes the rollouts. Lastly, training on $\mathcal{D}_{q}$ trades smoothness for better data coverage and success rates. Ambient's Pareto frontier for this trade-off strictly dominates the co-training baseline (Figure 6(a) ‣ Fig. 6 ‣ 7.1 Noisy Trajectories ‣ 7 Controlled Experiments ‣ Ambient Diffusion Policy: Imitation Learning from Suboptimal Data in Robotics")).

Ablation: We claim that $p_{t}\approx q_{t}$ for $t>t_{\min}$. If this were true, then we should be able to train an effective policy without using $\mathcal{D}_{p}$ for $t>t_{\min}$. To test this, we train a policy that exclusively trains on $\mathcal{D}_{q}$ for $t\in(t_{\min},T]$ and $\mathcal{D}_{p}$ for $t\in[0,t_{\min}]$. Remarkably, it matches the performance of the Ambient Diffusion Policy, with a success rate of $99.0\%$ and a squared acceleration of $29.9$.

### Neural Motion Planning

We extend the maze experiment to neural motion planning with a 7-DoF robot arm in a cluttered environment (Figure 1b). The setup and metrics are analogous to the 2D maze, except that start and goal configurations are sampled around objects and shelves, and the planner predicts the entire plan open-loop. Appendix Table 7 compares the two setups. The main results in Table 1(b) ‣ Table 1 ‣ 7.1 Noisy Trajectories ‣ 7 Controlled Experiments ‣ Ambient Diffusion Policy: Imitation Learning from Suboptimal Data in Robotics") and Figure 6(b) ‣ Fig. 6 ‣ 7.1 Noisy Trajectories ‣ 7 Controlled Experiments ‣ Ambient Diffusion Policy: Imitation Learning from Suboptimal Data in Robotics") mirror the 2D maze experiments: Ambient achieves the highest success rate while remaining substantially smoother than co-training. The full experimental details and ablations are in Appendix G.2.

Implications for Neural Motion Planning (NMP). Most neural motion planners are trained on large datasets of sampling-based trajectories (akin to $\mathcal{D}_{q}$) since they are inexpensive to generate. Unfortunately, sampling-based trajectories are non-smooth; thus, these approaches choose to prioritize data scale over quality. Our results suggest that an NMP trained with Ambient can enjoy the best of both worlds: augmenting the existing sampling-based datasets with a small amount of high-quality data could yield planners that are both general and smooth.

### Sim-to-Real Distribution Shift

We evaluate Ambient Diffusion Policy on sim-and-real co-training using the planar pushing setup from (Figure 1c), a canonical task in robot imitation learning. Our experiments use the sim-and-target problem from Wei et al. as a controlled proxy for the sim-and-real problem. $\mathcal{D}_{p}$ consists of 50 teleoperated demonstrations in the target environment; $\mathcal{D}_{q}$ consists of 2000 trajectories generated by a motion planner in the simulated environment. We use the same datasets from Wei et al. to enable direct comparisons with their method. A policy rollout is successful if it pushes the T to the target pose within a time limit.

Ambient (tmin per dataset) Ambient (tmin per datapoint) Ambient + Locality (σtmax = 0.025) Table 2: Main planar pushing results (200 trials). All Ambient variations outperform co-training.

Table 2 reports the success rate for three variations of Ambient Diffusion Policy that annotate $t_{\min}$ at two granularities: per dataset (with a parameter sweep) and per datapoint (with the classifier approach). We explore intermediate granularities, scaling laws, and more ablations in Appendix G.3. All Ambient variations outperform the best co-trained policy. Annotating $t_{\min}$ per datapoint performs the best because even within a single dataset, the utility of each datapoint can vary. As before, Ambient learns from suboptimal simulation data by leveraging the diffusion hierarchy. $\mathcal{D}_{p}$ and $\mathcal{D}_{q}$ share the same high-level strategy; thus, $\mathcal{D}_{q}$ is safe to use at high noise. Locality ($t_{\max}>0$) does not help since $\mathcal{D}_{p}$ and $\mathcal{D}_{q}$ exhibit different low-level contact dynamics.

### Task Mismatch

Table 3: Main block sorting results (∼800 blocks). Only Ambient Diffusion Policy (Locality) performs well on all metrics.

Ambient can leverage "locality" to learn local action primitives (e.g., grasping) from data collected on a different task. Consider the block sorting task in Figure 1d. The robot must sort red and blue blocks into the left and right bins, respectively. This requires two distinct skills: motion (grasping and placing blocks) and logic (selecting the correct bin). We design a metric to evaluate each skill: Motion metric: $\frac{\text{\# blocks placed}}{\text{\# total blocks}}$. This metric is independent of logical reasoning because the numerator counts any placed block, regardless of logical correctness.

Logic metric: $\frac{\text{\# blocks placed correctly}}{\text{\# blocks placed}}$. This metric is independent of pick-and-place ability because the denominator only counts successfully placed blocks.

The overall success rate is $\frac{\text{\# blocks placed correctly}}{\text{\# total blocks}}$, the product of the two metrics. $\mathcal{D}_{p}$ contains 50 demonstrations with the correct sorting. $\mathcal{D}_{q}$ contains 200 demonstrations with the opposite sorting. To isolate the effect of locality, we set $t_{\min}=0$ and sweep $t_{\max}$ for $\mathcal{D}_{q}$.

Table 3 presents the results. Co-training performs poorly because training on $\mathcal{D}_{q}$ at all diffusion times teaches the policy both the useful motion primitives and the incorrect logic. Ambient Diffusion Policy solves this problem by restricting $\mathcal{D}_{q}$ to $t\in0,t_{\max})$. As illustrated in Figures [2 and 7, the policy learns motion primitives at low diffusion times without attending to the (incorrect) task-level structure of the demonstrations. This results in near-perfect scores on both metrics simultaneously.

Figure 7: Left: Performance metrics vs σtmax. The logic metric plateaus before σtmax* = 0.46 and deteriorates rapidly afterwards; the opposite is true for the motion metric. Thus, the policy learns local motion-level features for t ∈ [0, tmax*) and global logic-level features for t ∈ (tmax*, T]. Right: Unlike co-training, Ambient achieves a near-optimal trade-off between logic and motion metrics.

Ablations: We present two ablations in Appendix G.4. 1) we add a one-hot encoding indicating the sorting direction to the policies. Ambient still outperforms the co-training. 2) we train a policy that exclusively uses $\mathcal{D}_{q}$ for $t\in[0,t_{\max})$ and $\mathcal{D}_{p}$ for $t\in[t_{\max},T]$. This is the locality-version of the ablation in the 2D maze experiment. The resulting policy achieves a logic and motion score of $97.9\%$ and $93.8\%$, reinforcing our claim that action diffusion is hierarchical.

### Finetuning Comparison

Figure 8: Left: success rate of policies finetuned from different base policies. Right: smoothness of finetuned policies in the maze experiment. We compare smoothness instead of success rate since all policies achieved 99.0%+ success rate.

Finally, we compare against the finetuning baseline. For each experiment, we finetune the best co-trained policy and the best Ambient policy on $\mathcal{D}_{p}$; implementation details are in Appendix I.1.

Figure 8 suggests three findings. First, finetuning an Ambient base policy consistently outperforms finetuning a co-trained base policy. Second, the Ambient base policy can often outperform the finetuned co-trained policy. Third, finetuning an Ambient base policy does not always help. We hypothesize that the Ambient policies already ignore undesirable features in the suboptimal data.

## Scaling Experiments: Open X-Embodiment

Having shown the generality of Ambient Diffusion Policy, we now scale to Open X-Embodiment (OXE). OXE is a large collection of real-world data with heterogeneous quality and unstructured distribution shifts. Our goal is to extract useful learning signal from as much of this "suboptimal" data as possible. The experiments evaluate Ambient Diffusion Policy on two real-world tasks.

1\) Table Cleaning (Figure 1e): the robot must open the drawer, place objects inside, and close the drawer. The diversity of the test-time objects (unseen during training) makes this challenging. Performance is measured with the task completion rubric in Table 11.

2\) Tower Building (Figure 1f): the robot must stack blocks in alternating directions and colors as high as possible. This task requires precise manipulation since placement errors compound as the tower grows. Performance is measured by the number of blocks placed before toppling the tower.

The training procedure for both tasks is identical. $\mathcal{D}_{p}$ consists of a small number of demonstrations for each task. $\mathcal{D}_{q}$ is one of two subsets of the Open X-Embodiment (OXE) dataset: 1) Magic Soup++ (MS++), 27 datasets from OXE used by OpenVLA, or 2) Custom OXE (COXE), 48 datasets from OXE that contain MS++ as a subset. $t_{\min}$ and $t_{\max}$ are annotated according to Phase 1 of the method. We note that COXE was curated to be as inclusive as possible; details are in Appendix H.1.

Lastly, for both co-training and Ambient, we re-weight each dataset's sampling probability at every diffusion time. Let $w_{i}$ denote the weight for dataset $i$, and $S_{t}$ denote the indices of datasets that are permissible at diffusion time $t$. The sampling probability of dataset $i$ at diffusion time $t$ is In co-training, $S_{t}$ contains all datasets for all $t\in[0,T]$; in Ambient, $S_{t}$ depends on each dataset's $t_{\min}$ and $t_{\max}$ (see Figures 21 and 22). Re-weighting marginally improves the Ambient policies but is not required; in contrast, it is necessary for co-training (see Section 8.2).

### Main Results

Table Cleaning ($\mathcal{D}_{p}$ with 50 demos): Data filtering achieves $68.2\%$ task completion; co-training adds just 2-3% and plateaus when $\mathcal{D}_{q}$ scales from MS++ to COXE. On the other hand, the best Ambient Diffusion Policy outperforms co-training by $12\%$ and improves when $\mathcal{D}_{q}$ scales from MS++ to COXE. Adding locality ($t_{\max}>0$) appears to provide further gains.

Table Cleaning ($\mathcal{D}_{p}$ with 150 demos): When $\mathcal{D}_{p}$ is large, data filtering improves to $80.1\%$, and training on suboptimal data provides less relative value. However, for many real-world tasks, collecting enough data in $\mathcal{D}_{p}$ could be prohibitively expensive. Nonetheless, Ambient continues to outperform co-training by up to $10\%$. Adding locality did not improve performance in this setting. We hypothesize that when $\mathcal{D}_{p}$ is large, the policy can learn the relevant motion primitives from $\mathcal{D}_{p}$, making data from $\mathcal{D}_{q}$ unnecessary or even harmful with the wrong choice of $t_{\max}$. This is consistent with the classifier annotation method, which would have assigned $t_{\max}=0$ to nearly all datasets.

Tower Building ($\mathcal{D}_{p}$ with 35 demos): On average, the Ambient Diffusion Policies build up to $84\%$ and $33\%$ taller than the data filtering and co-training baselines, respectively (Figure 9). Including $\mathcal{D}_{q}$ at low diffusion times appears to improve performance.

Figure 9: When scaled to OXE, Ambient Diffusion Policy outperforms data filtering and co-training by up to 15% on table cleaning and 84% on tower building (20 trials per policy).

### Ablations

Figure 10: Ambient is significantly less sensitive to dataset re-weighting than co-training. The Ambient Diffusion Policy performed at most 9% worse without re-weighting. The co-trained policies were too dangerous to evaluate without re-weighting.

Dataset Re-weighting: Figure 10 ablates the effect of re-weighting in Eq. on co-training and Ambient. Re-weighting improves policy performance on the table cleaning task by $3$--$9\%$. On the other hand, re-weighting is necessary for co-training: the unweighted co-trained policies were too unsafe to evaluate on hardware. This contrast highlights another practical advantage of Ambient: the training algorithm is inherently less sensitive to dataset weights because $\mathcal{D}_{q}$ is only used when $p_{t}\approx q_{t}$. Co-training uses $\mathcal{D}_{q}$ at all diffusion times, making the weights critical and fragile.

Additional Ablations: We present two further ablations in Appendix H.2. 1) Finetuning the OXE policies on $\mathcal{D}_{p}$ produced no statistically significant change in performance (Appendix I.2 ‣ Appendix I Finetuning ‣ Ambient Diffusion Policy: Imitation Learning from Suboptimal Data in Robotics")), consistent with the controlled experiments (Section 7.5). 2) On table cleaning, the Ambient Diffusion Policies require 25-40% fewer grasps and less time per object than their co-trained counterparts.

## Limitations and Future Work

Ambient Diffusion Policy does not yet handle distribution shifts in the observation space. We explore two initial attempts in Appendix J. The classifier-based annotation method for $t_{\min}$ and $t_{\max}$ is theoretically grounded, but does not always outperform a (costly) hyperparameter sweep. Better annotation methods could improve performance. In addition, the theory in Section 5 is limited to Gaussians; extending the results to a broader class of distributions could provide further insights. Lastly, our method is more computationally expensive than data filtering since it trains on more data, but in most cases, its benefits are worthwhile.

Ambient Diffusion Policy requires the user to partition their data into $\mathcal{D}_{p}$ and $\mathcal{D}_{q}$. The algorithm itself poses no restrictions on this partitioning, but it is an important design decision for downstream performance. This paper defines $\mathcal{D}_{p}$ as data from the target task and environment, but the right choice depends on the goal. For task-specific training or finetuning, our definition is appropriate; for pretraining a generalist policy, prior work suggests that $\mathcal{D}_{p}$ should contain diverse and high-quality demonstrations. The former suggests that we could expand our finetuning dataset to include suboptimal data. The latter requires a more principled understanding of data quality in robotics. Both settings are exciting directions for future work.

## Conclusion

High-quality robot data is scarce, making it essential to learn from suboptimal data sources. But even as data collection scales, suboptimal data will continue to grow alongside high-quality data. Thus, the problem of learning from suboptimal data sources is not a temporary artifact of today's data scarcity, but rather a fundamental and persistent challenge in robot imitation learning. The dominant approach for addressing this problem is to filter the worst data and co-train on the rest via re-weighting; but filtering is wasteful, and co-training teaches a policy the meaningful and the harmful parts of suboptimal distributions. In this paper, we propose Ambient Diffusion Policy, a principled method for training on suboptimal demonstrations.

Neighboring fields have recognized the power of noise-dependent data usage. Our key experimental and theoretical insight is that this training paradigm is also well-suited for robotics. Our method makes no assumptions about the nature of the action suboptimality, outperforms existing baselines, and greatly expands the set of useful data sources for robot imitation learning. With Ambient Diffusion Policy, the question shifts from which data sources should be used, to when each should be used in the diffusion process.
