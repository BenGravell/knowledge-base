<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Much Ado about Noising: Dispelling the Myths of Generative Robotic Control

Topics include Robotics, Diffusion models, Regression, Benchmarks, Control, Noising, Behavior cloning, Mixed-integer programming, Generative model.

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Generative models, like flows and diffusions, have recently emerged as popular and efficacious policy parameterizations in robotics. There has been much speculation as to the factors underlying their successes, ranging from capturing multi-modal action distribution to expressing more complex behaviors. In this work, we perform a comprehensive evaluation of popular generative control policies (GCPs) on common behavior cloning (BC) benchmarks. We find that GCPs do not owe their success to their ability to capture multi-modality or to express more complex observation-to-action mappings. Instead, we find that their advantage stems from iterative computation, as long as intermediate steps are supervised during training and this supervision is paired with a suitable level of stochasticity. As a validation of our findings, we show that a minimum iterative policy (MIP), a lightweight two-step regression-based policy, essentially matches the performance of flow GCPs, and often outperforms distilled shortcut models. Our results suggest that the distribution-fitting component of GCPs is less salient than commonly believed, and point toward new design spaces focusing solely on control performance.

<!-- chunk {"id": "body-0003", "role": "body", "section": "Introduction", "weight": 1.5} -->

Long-horizon, dexterous manipulation tasks such as furniture assembly, food preparation, and manufacturing have been a holy grail in robotics. Recent large robot action models (teamCarefulExaminationLarge2025; black2024pi_0; kim2024openvla) have made substantial breakthroughs towards these goals by imitating expert demonstrations of diverse qualities. We provide a more comprehensive review of related work in Section˜6, but highlight here a key trend: while supervised learning from demonstration, also known as *behavior cloning* (BC), has been applied across domains for decades (pomerleau1988alvinn), its recent success in robotic manipulation has coincided with the adoption of what we term generative control policies (GCPs): robotic control policies that use generative modeling architectures, such as diffusion models, flow models, and autoregressive transformers, as parameterizations of the mapping from observation to action. Given the seemingly transformative nature of GCPs for robot learning, there has been much speculation about the origin of their superior performance relative to policies trained with a regression loss, henceforth regression control policies (RCPs).

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

GCPs, by modeling conditional distributions over actions, are uniquely suited to the multi-task pretraining paradigm popular in today's large robotic models. However, a number of hypotheses regarding the superiority of GCPs pertain even in the *single task* setting (chi2023diffusion; reuss2023goal): Better performance on pixel-based control Capturing multi-modality in the training data Greater expressivity due to iterative computation of the observation-to-action mapping Representation learning due to stochastic data augmentation Improved training stability and scalability In this work, we systematically investigate these hypotheses to understand the mechanism by which GCPs have attained superior performance over RCPs. We aim to answer:\> Is there *really* a benefit to using GCPs for behavior cloning, or are their claimed successes... much ado about noising?

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

The gap between generative modeling and generative control. The objective for generative modeling in text and image domains is fundamentally different from the goal in a control task. In the former, one aims to generate high-quality and *diverse* samples from the original data distribution. In the latter, it suffices to select *any* action that leads to better downstream performance. Whereas much of the generative modeling literature has focused on the distribution of the *generated variable* (lee2023convergence), we aim to understand if it is necessary to reproduce the expert data distribution---for example by capturing any multi-modality---to attain strong control performance. If not, is most salient to capture about the *conditioning relationship* mapping $o\to a$?

<!-- chunk {"id": "body-0006", "role": "body", "section": "Contributions", "weight": 1.0} -->

This paper adopts careful experimental methodology to rigorously test the key design components (Section˜4: Isolating the Source of GCPs’ Success")) that contribute to the observed success of GCPs, and to account for the key mechanisms by which they contribute to improved performance in behavior cloning (Section˜5). We restrict our study to flow-based GCPs, given their popularity and adoption in industry (black2024pi_0; intelligence$p_05$VisionLanguageActionModel2025; nvidia2025gr00t).

<!-- chunk {"id": "body-0007", "role": "body", "section": "Contributions", "weight": 1.0} -->

We begin by first identifying which factors *do not* contribute to the advantage of GCPs over RCPs.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Contribution 1 (Neither multi-modality nor policy expressivity account for GCPs' success, Section˜3)", "weight": 1.0} -->

Through careful benchmarking, we show that RCPs with appropriate architectures are highly competitive on both state- and image-based (H1) robot learning benchmarks as well as vision-language-action (VLA) model finetuning (Section˜3.1). Performance gaps only arise on certain tasks requiring high precision. However, we show that neither multi-modality (H2, Section˜3.2) nor the ability to express more complex functions via multiple integration steps (H3, Section˜3.3) satisfactorily accounts for this phenomenon. In fact, GCPs do not even provide greater trajectory diversity compared to RCPs (Appendix˜G).

<!-- chunk {"id": "body-0009", "role": "body", "section": "Contribution 1 (Neither multi-modality nor policy expressivity account for GCPs' success, Section˜3)", "weight": 1.0} -->

Essential to this finding is controlling for architecture: to our knowledge, we are the first work to carefully benchmark expressive architectures popularized for Diffusion (chi2023diffusion; dasariIngredientsRoboticDiffusion2024) as regression policies. To determine what contributes to GCPs performance on these high-precision tasks (beyond architectural optimization), we parse the design space of generative control policies into three components, depicted in Figure˜1 (left).

<!-- chunk {"id": "body-0010", "role": "body", "section": "Contribution 2 (Exposing the design space of GCPs, Section˜4: Isolating the Source of GCPs’ Success\"))", "weight": 1.0} -->

- [C1: Isolating the Source of GCPs’ Success").]

<!-- chunk {"id": "body-0011", "role": "body", "section": "Contribution 2 (Exposing the design space of GCPs, Section˜4: Isolating the Source of GCPs’ Success\"))", "weight": 1.0} -->

*Distributional Learning*: matching a conditional distribution of actions given observations.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Contribution 2 (Exposing the design space of GCPs, Section˜4: Isolating the Source of GCPs’ Success\"))", "weight": 1.0} -->

- [C2: Isolating the Source of GCPs’ Success").]

<!-- chunk {"id": "body-0013", "role": "body", "section": "Contribution 2 (Exposing the design space of GCPs, Section˜4: Isolating the Source of GCPs’ Success\"))", "weight": 1.0} -->

*Stochasticity Injection*: injecting noise during training to improve the learning dynamics.

<!-- chunk {"id": "body-0014", "role": "body", "section": "Contribution 2 (Exposing the design space of GCPs, Section˜4: Isolating the Source of GCPs’ Success\"))", "weight": 1.0} -->

- [C3: Isolating the Source of GCPs’ Success").]

<!-- chunk {"id": "body-0015", "role": "body", "section": "Contribution 2 (Exposing the design space of GCPs, Section˜4: Isolating the Source of GCPs’ Success\"))", "weight": 1.0} -->

*Supervised Iterative Computation*: generating output with multiple steps, each of which receives supervision during training.

<!-- chunk {"id": "body-0016", "role": "body", "section": "Contribution 2 (Exposing the design space of GCPs, Section˜4: Isolating the Source of GCPs’ Success\"))", "weight": 1.0} -->

With this taxonomy in hand, Section˜4.1: Isolating the Source of GCPs’ Success") introduces a family of algorithms, each of which lies along a spectrum between GCPs and RCPs by exhibiting different combinations of the above components. While we find that neither C2: Isolating the Source of GCPs’ Success") nor C3: Isolating the Source of GCPs’ Success") in isolation improve over regression, we find their combination yields a policy whose performance is competitive with flow, leading to our next contribution.

<!-- chunk {"id": "body-0017", "role": "body", "section": "Contribution 3 (MIP: the power of C2: Isolating the Source of GCPs’ Success\")+C3: Isolating the Source of GCPs’ Success\"), Sections˜4.2: Isolating the Source of GCPs’ Success\") and 4.1: Isolating the Source of GCPs’ Success\"))", "weight": 1.0} -->

As an algorithmic ablation that only combines C2: Isolating the Source of GCPs’ Success")+C3: Isolating the Source of GCPs’ Success"), we devise a *minimal iterative policy* (MIP), which invokes only two iterations, one-step of stochasticity during training, and deterministic inference. Despite its simplicity, MIP essentially matches the performance of flow-based GCPs across state-, pixel- and 3D point-cloud-based BC tasks, exposing that the combination of C2: Isolating the Source of GCPs’ Success")+C3: Isolating the Source of GCPs’ Success") is responsible for the observed success of GCPs. In addition, we find that MIP often outperforms shortcut/few-step policies (Section˜4.3: Isolating the Source of GCPs’ Success")). This confirms our findings that distributional learning (which few-step policies, but not MIP, achieve) is not needed in robotic control.

<!-- chunk {"id": "body-0018", "role": "body", "section": "Contribution 3 (MIP: the power of C2: Isolating the Source of GCPs’ Success\")+C3: Isolating the Source of GCPs’ Success\"), Sections˜4.2: Isolating the Source of GCPs’ Success\") and 4.1: Isolating the Source of GCPs’ Success\"))", "weight": 1.0} -->

As described in Section˜4.3: Isolating the Source of GCPs’ Success"), MIP is substantively distinct from flow-map-based models (boffiFlowMapMatching2025; boffiHowBuildConsistency2025), including consistency models (songConsistencyModels2023; kim2023consistency) and their extensions (gengMeanFlowsOnestep2025; fransOneStepDiffusion2024), in that the latter do satisfy C1: Isolating the Source of GCPs’ Success"), and require training over a continuum of noise levels.

<!-- chunk {"id": "body-0019", "role": "body", "section": "Contribution 4 ( Attributing the benefits of C2: Isolating the Source of GCPs’ Success\")+C3: Isolating the Source of GCPs’ Success\"), Section˜5)", "weight": 1.0} -->

We identify that a property we term *manifold adherence* captures the inductive bias of GCPs and MIP relative to RCPs, even in the absence of lower validation loss. We explain how this property is a useful proxy for closed-loop performance in control tasks. Finally, we expose how C3: Isolating the Source of GCPs’ Success"), through iterative computation, encourages manifold adherence, but only if stochasticity during training (C2: Isolating the Source of GCPs’ Success")) is present to mitigate compounding errors across iteration steps (as described in Section˜5.2).

<!-- chunk {"id": "body-0020", "role": "body", "section": "Contribution 4 ( Attributing the benefits of C2: Isolating the Source of GCPs’ Success\")+C3: Isolating the Source of GCPs’ Success\"), Section˜5)", "weight": 1.0} -->

Manifold adherence in Section˜5.1 measures the generated action's plausibility given out of distribution observations, where only off-manifold component is evaluated rather than the distance to the neighbors (pari2021surprising). Note that manifold adherence reflects a favorable inductive bias during learning, rather than brute expressivity of more complex behavior (H3). Moreover, C2: Isolating the Source of GCPs’ Success") provides more of a supporting role to C3: Isolating the Source of GCPs’ Success"), rather than enhancing data-augmentation in its own right (H4). In addition, we find that C2: Isolating the Source of GCPs’ Success")+C3: Isolating the Source of GCPs’ Success") also enhance scaling behavior (H5), likely due to better model utilization through decoupling across iterations. Finally, we identify that the subtle interplay between architecture choice, policy parameterization and task can affect performance by an even greater magnitude than the choice of policy parametrization (Section˜5.3).

<!-- chunk {"id": "body-0021", "role": "body", "section": "Contribution 4 ( Attributing the benefits of C2: Isolating the Source of GCPs’ Success\")+C3: Isolating the Source of GCPs’ Success\"), Section˜5)", "weight": 1.0} -->

Takeaway. In robotic applications, our findings suggest that the distributional formulation of GCPs --- sampling from a *distribution* of actions given observations --- is the least important facet that contributes to their success. Rather, our work highlights that C2: Isolating the Source of GCPs’ Success")+C3: Isolating the Source of GCPs’ Success") offer an exciting and under-explored sandbox for future algorithm design in continuous control and beyond.

<!-- chunk {"id": "body-0022", "role": "body", "section": "Multi-modality and expressivity do not explain GCPs' performance", "weight": 1.0} -->

This section demonstrates that neither advantages on pixel-based control (H1), nor multi-modality (H2), nor improved expressivity (H3) fully account for the GCPs performance relative to RCPs. Instead, our analysis indicates that the advantage of GCPs is largely due to architectural innovations found in GCPs---specifically, the adoption of powerful models like Transformers and UNets, along with the use of action chunking techniques. Appendices˜F and G addresses other hypotheses, such as $k$-nearest neighbor approximation and the behavior diversity.

<!-- chunk {"id": "body-0023", "role": "body", "section": "When controlled for architecture, GCPs only outperform on few tasks", "weight": 1.0} -->

We first isolate the tasks in which GCPs exhibit stronger performance by comparing across 28 popular BC benchmarks including multi-task benchmarks like LIBERO (detailed in Section˜B.1), encompassing diverse data quality, modalities (state, point clouds, image and language), and domains (e.g., MetaWorld, Robomimic, Adroit, D4RL, Meta-World, LIBERO). Crucially, we implement RCPs using the exact same architectures as their corresponding flow models by simply setting the noise level and initial noise to zero: $z=0$, $t=0$, and study three widely-used architectures (Chi-Transformer, Sudeep-DiT, Chi-UNet as well as pre-trained VLA models like ~0~ (black2024pi_0); detailed in Section˜B.2). This architectural alignment enables RCPs to benefit from the sophisticated network designs typically reserved for GCPs, ensuring a fair comparison.

<!-- chunk {"id": "body-0024", "role": "body", "section": "When controlled for architecture, GCPs only outperform on few tasks", "weight": 1.0} -->

Under controlled comparison, we find GCPs and RCPs achieve parity across the vast majority of state-based, image-based, and VLA-based BC benchmarks. Performance gaps emerge only on a small subset of tasks requiring high precision (e.g. precise insertion tasks). We report best-case results in Fig.˜2 and comprehensive ablations (including worst-case architectures and loss variants) in Section˜B.4.

<!-- chunk {"id": "body-0025", "role": "body", "section": "When controlled for architecture, GCPs only outperform on few tasks", "weight": 1.0} -->

Our evaluation yields three key insights: Rare Benefit of GCPs: GCPs outperform RCPs by $>5\%$ on only a handful of tasks.

<!-- chunk {"id": "body-0026", "role": "body", "section": "When controlled for architecture, GCPs only outperform on few tasks", "weight": 1.0} -->

Modality Independence: Contrary to popular belief, observation modality does *not* correlate with GCP advantage.

<!-- chunk {"id": "body-0027", "role": "body", "section": "When controlled for architecture, GCPs only outperform on few tasks", "weight": 1.0} -->

Architectural Dominance: Architecture choice dictates performance far more than the generative vs. regression distinction.

<!-- chunk {"id": "body-0028", "role": "body", "section": "When controlled for architecture, GCPs only outperform on few tasks", "weight": 1.0} -->

We posit that the perceived superiority of GCPs in prior work was confounded by architectural asymmetry. To our knowledge, this is the first study to benchmark Sudeep-DiT, Chi-UNet, and ~0~ backbones as regression policies. In Section˜5.3, we demonstrate that when equipped with these modern backbones---or even tuned MLP baselines---RCPs are highly competitive. Furthermore, we find that hyperparameters such as action-chunking horizon (zhao2023learning; chi2023diffusion; zhang2025actionchunkingexploratorydata) exert a greater influence on success rate than the choice of objective function (Section˜F.1).\> Design decisions like architecture and action-chunking have a significant and consistent impact on control performance. In contrast, the choice between GCPs and RCPs is largely negligible outside of high-precision regimes.

<!-- chunk {"id": "body-0029", "role": "body", "section": "GCPs' performance does not arise from multi-modality", "weight": 1.0} -->

Earlier literature suggested that capturing multi-modality, as defined in Section˜2, was precisely the root of the observed performance benefits of GCPs (chi2023diffusion; reuss2023goal). However, examining Fig.˜2, we see that many tasks which have been understood to be multimodal (e.g., Push-T) do not show substantial performance gaps between RCPs and GCPs. On the other hand, RCPs and GCPs differ only on tasks that demand high precision (e.g. Tool-Hang, Transport). In this section, we provide additional evidence that multimodality is not the main factor responsible for witnessed performance advantages of GCPs.

<!-- chunk {"id": "body-0030", "role": "body", "section": "GCPs' performance does not arise from multi-modality", "weight": 1.0} -->

Evidence A: GCPs exhibit unstructured action distributions. For fixed observations, we draw multiple action samples by denoising from different initial latents and visualize the resulting action set with their Q values $Q(a,o)$. We deliberately choose *symmetry-critical* or *high-ambiguity* states to *maximize* potential multi-modality: (a) Push-T at the symmetry axis of the T-shape, where taking the left or right path is equivalent, (b) Kitchen from an initial state with multiple first-subtask choices, and (c) Tool-Hang at the insertion pre-contact pose where human demonstrators pause for varying durations. In (a-c) we observe *single* clusters rather than distinct modes (high-dimensional actions visualized with t-SNE); see Fig.˜3. Moreover, adherence to action cluster means do not correlate with performance: We color-code actions by Q-value, i.e. Monte-Carlo-estimated rewards-to-go (Section˜D.1). Highest returns are distributed evenly across samples.

<!-- chunk {"id": "body-0031", "role": "body", "section": "GCPs' performance does not arise from multi-modality", "weight": 1.0} -->

Evidence B: Taking mean actions does not meaningfully degrade GCPs' performance. We evaluate flow policy's performance with three sampling strategies: zero noise $a=\pi(z=0,o)$, stochastic sampling $a=\pi(z,o),z\sim\mathrm{N}(0,I)$, and *mean action* $a=\mdmathbb{E}_{z\sim\mathrm{N}(0,I)}[\pi(z,o)]$ (via Monte Carlo approximation). If the learned distribution were strongly multi-modal, or if their distributions lied on a manifold whose *curvature* was crucial to task success, the conditional mean would *collapse* modes and severely degrade performance. However, Table˜1 shows that replacing stochastic sampling with the mean action only slightly affects performance, indicating absence of distinct action modes.

<!-- chunk {"id": "body-0032", "role": "body", "section": "GCPs' performance does not arise from multi-modality", "weight": 1.0} -->

Evidence C: GCPs outperform RCPs on certain tasks even with deterministic experts. To fully remove any residual multi-modality, we recollect the dataset with trained flow policy evaluated in deterministic mode ($z=0$) detailed in Section˜D.2. The new dataset is fully deterministic because action labels are provided by a deterministic policy evaluated in a deterministic environment. While the gap in performance between GCPs and RCPs shrinks somewhat, we still find that GCPs still outperforms RCPs, as in Table˜2, suggesting that capturing some "hidden" stochasticity or multimodality in the data does not suffice to explain the gap between the two.\> Collectively, (A)--(C) indicate that the commonly cited explanation---"GCPs win because demonstrations are multi-modal"---does not hold for most studied behavior cloning benchmarks.

<!-- chunk {"id": "body-0033", "role": "body", "section": "GCPs' performance does not arise from multi-modality", "weight": 1.0} -->

Multi-modality and data coverage. The absence of observed multimodality is likely attributable to the large observation dimension of tasks relative to total number of demonstrations. That is, we rarely see two "conflicting" actions for nearby observation vectors (note: to grid a space of dimension $d$ requires $2^{d}$ points). Some degree of "hidden" multi-modality may still be present, as indicated by the slight narrowing of the performance gap in Table˜2. Still, our central claim is that multi-modality is not *sufficient* to explain the full difference in performance. Understanding to what extent multimodality appears in the multi-task setting is an exciting direction for future research.

<!-- chunk {"id": "body-0034", "role": "body", "section": "Limitations of the expressivity of GCPs in the absence of multimodality", "weight": 1.5} -->

An alternative to learning explicit multimodality is to represent rapid transition between actions as the observation changes. This is depicted in Figure˜4, where data that appears multi-modal can be fit with a policy that has a high Lipschitz constant, i.e. in which $\nabla_{o}\pi(a\mid o)$ is large. This reflects a broader principle in control that we need only capture the mapping from observation to a single effective action, rather than reproduce the distribution over all possible actions.

<!-- chunk {"id": "body-0035", "role": "body", "section": "Limitations of the expressivity of GCPs in the absence of multimodality", "weight": 1.5} -->

One may still conjecture that GCPs more easily higher-Lipschitz policies by leveraging iterative computation, as compared to RCPs. This is because deeper networks can express larger-Lipschitz functions more easily (telgarsky2016benefits), and many have equated the multi-step computation in flow-based generative models to depth (chen2018neural). Step-by-step generation is known to drastically increase expressivity in other domains as well, such as autoregressive language models (li2024chainthoughtempowerstransformers), However, flow-based generative models use their multi-step computation to express complex distributions over the *generated variable* (ho2020denoising; song2021denoising; zhang2022fast; nichol2021improved). It is less clear if the iteration computation assists with represent complex *observation-to-action* mappings.

<!-- chunk {"id": "body-0036", "role": "body", "section": "Limitations of the expressivity of GCPs in the absence of multimodality", "weight": 1.5} -->

Thus, we ask: > Does the iterative computation in GCPs aid in learning more complex observation-to-action mappings, even if the learned action distributions for a fixed observation are themselves are relatively simple (i.e. unimodal)?

<!-- chunk {"id": "body-0037", "role": "body", "section": "Limitations of the expressivity of GCPs in the absence of multimodality", "weight": 1.5} -->

We now provide evidence that suggests "no." We show that in the absence of multi-modality (as shown in Section˜3.2), GCPs cannot express more complex mappings from the conditioning variable $o$ to the generated variable $a$ than RCPs can. We begin by considering a ground-truth conditional flow field $b_{t}^{\star}(o\mid a)$. Let ${}^{\star}(z,o)$ represent the exactly integrated $b^{\star}$ from initial noise $z$ to $a$. Given the absence of multi-modality (Section˜3.2), we assume that the distribution of $a\mid o$ is -log-concave (Appendix˜H), satisfied by many classical unimodal distributions.

<!-- chunk {"id": "body-0038", "role": "body", "section": "GCPs and RCPs Exhibit Comparable Behavior Diversity", "weight": 1.0} -->

We conclude by rebutting a commonly believed hypothesis is that GCPs can express more diverse behaviors than RCPs by capturing the full distribution of expert actions (shafiullah2022behavior).^44^4Note that the expert might be stochastic but unimodal, so the findings in this section do not directly follow form those in Section 3.2. We evalute different variants of GCPs and RCPs on Franka-Kitchen, where the expert shows multiple task completion orders. As demonstrated in Fig.˜6, GCPs with both stochastic and deterministic sampling show similar task completion order diversity. Deterministic policies like regression and MIP (to be introduced in Section˜4: Isolating the Source of GCPs’ Success")) also demonstrate similar task completion order diversity. This indicates that, given sparse expert demonstrations, both GCPs and RCP learns high-Lipschitz policies to switch between different modes given different observations (corresponding to (b.2) case in Figure˜4).

<!-- chunk {"id": "body-0039", "role": "body", "section": "GCPs and RCPs Exhibit Comparable Behavior Diversity", "weight": 1.0} -->

RCPs and GCPs are equally good at learning such behaviors (Figure˜6), which explain why we see similar performance for both policy parametrizations, even on seemingly multi-modal tasks like Franka-Kitchen.

<!-- chunk {"id": "body-0040", "role": "body", "section": "Minimal Iterative Policy (MIP): Isolating the Source of GCPs' Success", "weight": 1.0} -->

In this section, we introduce a number of intermediates between RCPs and GCPs that isolate which design decisions contribute to the latter's superior performance. This leads to a Minimal Iterative Policy (MIP), which matches GCPs performance, thereby identifying the source of GCPs' success.

<!-- chunk {"id": "body-0041", "role": "body", "section": "Minimal Iterative Policy (MIP): Isolating the Source of GCPs' Success", "weight": 1.0} -->

We begin with a taxonomy of the three key algorithmic components (Figure˜7: Isolating the Source of GCPs’ Success")) present in GCPs.

<!-- chunk {"id": "body-0042", "role": "body", "section": "Component 1", "weight": 1.0} -->

Distributional learning denotes training a model to fit a conditional distribution $a\sim(o)$ of actions given observations, as opposed to deterministic predictions (i.e., $a=(o)$). ^55^5Note that Component˜1: Isolating the Source of GCPs’ Success") refers to *training* a model to fit a conditional distribution, not necessarily to the sampling. For example, training $b$ via flow model but conducting deterministic inference with ${}_{\theta,\mathrm{eul}}(z=0\mid o)$ is still considered distributional learning.

<!-- chunk {"id": "body-0043", "role": "body", "section": "Component 2", "weight": 1.0} -->

Stochasticity injection denotes the injection of additional stochastic inputs into the neural network during training time (e.g., the variable $z$ in Eq.˜2.2).

<!-- chunk {"id": "body-0044", "role": "body", "section": "Component 3", "weight": 1.0} -->

Supervised Iterative Computation (SIC) denotes the iterative refinement of predictions by feeding the previous outputs into the same network again during inference, and providing *supervision signals* at every step of the generation procedure at training time. For example, in flow GCPs, we integrate a supervised flow field $b_{t}(a_{t}\mid o)$ over time to get the final action $a$, and that $b_{t}$ receives an independent supervisory signal for each $t$ at training time (Eq.˜2.2).

<!-- chunk {"id": "body-0045", "role": "body", "section": "Component 3", "weight": 1.0} -->

From here, Section˜4.1: Isolating the Source of GCPs’ Success") proposes algorithmic variants which ablate these components: two novel variants we call minimal iterative policy (MIP, Components˜3: Isolating the Source of GCPs’ Success") and 2: Isolating the Source of GCPs’ Success")) and straight-flow (SF, Component˜2: Isolating the Source of GCPs’ Success") only), as well as a residual regression baseline (RR, Component˜3: Isolating the Source of GCPs’ Success") only). We evaluate the performance of different variants on challenging tasks in Section˜4.2: Isolating the Source of GCPs’ Success"), finding that MIP exhibits virtually the *same* performance as Flow across tasks, whereas SF matches the performance of Regression and RR exhibits even worse performance. This establishes that Components˜3: Isolating the Source of GCPs’ Success") and 2: Isolating the Source of GCPs’ Success"): SIC, when combined with stochasticity injection, drive performance.

<!-- chunk {"id": "body-0046", "role": "body", "section": "Component 3", "weight": 1.0} -->

Finally, we contrast MIP with other popular step policies ( Section˜4.3: Isolating the Source of GCPs’ Success")).

<!-- chunk {"id": "body-0047", "role": "body", "section": "MIP: a minimal intermediate between RCPs and GCPs", "weight": 1.0} -->

We introduce a range of policies which lie along the spectrum between RCP and flow-based GCPs via varying combinations of Components˜3: Isolating the Source of GCPs’ Success") and 2: Isolating the Source of GCPs’ Success"), culminating in the Minimal Iterative Policy (MIP). These policies do not satisfy Component˜1: Isolating the Source of GCPs’ Success"), because Sections˜3.2 and G suggests that this is not needed. In particular, we consider networks $(o,I_{t},t)$ that predict *actions*, not velocities, and given observations $o$, time indices $t$, and interpolants $I_{t}$ corresponding to noising actions. We state all networks below of $L_{2}$ minimization, but our findings remain consistent when minimizing $L_{1}$ error instead (Section˜F.2).

<!-- chunk {"id": "body-0048", "role": "body", "section": "MIP: a minimal intermediate between RCPs and GCPs", "weight": 1.0} -->

Regression as Single-Step Denoising. We begin by expression a regression policies (RCPs) as solving a single-step denoising problem, obtained by minimizing the $L_{2}$ prediction error of the action given observation and null action interpolant: where $(o,a)\sim p_{\mathrm{train}}$.In the limit of infinity data, RCPs predict the conditional mean of $a\mid o$ by mapping any noise $z$ to the same action $a$ given $o$.^66^6Note that in our comparisons between RCP and GCP (Section 3), we use the Eq. 4.1: Isolating the Source of GCPs’ Success") to implement RCPs on GCP architectures.

<!-- chunk {"id": "body-0049", "role": "body", "section": "MIP: a minimal intermediate between RCPs and GCPs", "weight": 1.0} -->

Straight Flow (SF, ours). Next we introduce Straightflow (SF), which adds only stochasticity injection Component˜2: Isolating the Source of GCPs’ Success") to RCPs. This is achieved by setting the interpolant $I_{0}$ to be Gaussian: where $(o,a)\sim p_{\mathrm{train}},z\sim\mathrm{N}(0,\mathbf{I})$. Inference is performed in a single step, by setting $a={}^{\textbf{{SF}}}(o,z,t=0)$. Equivalently, SF can be viewed as a flow model in which the flow field is constrained to be straight.

<!-- chunk {"id": "body-0050", "role": "body", "section": "MIP: a minimal intermediate between RCPs and GCPs", "weight": 1.0} -->

Like RCPs, the optimal SF policy is the conditional mean of $a\mid o$. The only difference between the two is injection of stochastic input $z$ during training. Our experiments with SF precisely isolate this effect---for example, determining if the additional stochasticity during training improves learning dynamics, or behaves like data augmentation. Like MIP below, we set $I_{0}=0$ at inference time, as stochasticity at inference time has little effect on policy performance.

<!-- chunk {"id": "body-0051", "role": "body", "section": "MIP: a minimal intermediate between RCPs and GCPs", "weight": 1.0} -->

Two-Step Denoising. As a next step towards GCPs, we now consider a two-step denoising (TSD) policy. As discussed in Section˜4.3: Isolating the Source of GCPs’ Success"), this parametrization is superficially similar to, but substantively different than, popular flow-map/consistency/shortcut models (boffiHowBuildConsistency2025). TSD performs two steps of denoising, one from zero, and a second from a fixed index $t_{\star}=.9$: where $(o,a)\sim p_{\mathrm{train}},z\sim\mathrm{N}(0,\mathbf{I})$, and $I_{t}=ta+(1-t)z$ is the same interpolant used in flow models, and where $t_{\star}=.9$ is fixed.

<!-- chunk {"id": "body-0052", "role": "body", "section": "MIP: a minimal intermediate between RCPs and GCPs", "weight": 1.0} -->

Minimal Iterative Policy. We find that ${}^{\textbf{{TSD}}}$ performs equivalently to a minimal policy which only adds training noise in the second step and has no stochasticity at inference time, which we call the minimal iterative policy.

<!-- chunk {"id": "body-0053", "role": "body", "section": "MIP: a minimal intermediate between RCPs and GCPs", "weight": 1.0} -->

Minimal iterative policy provides a *minimal* implementation that still exhibits competitive performance with flow. Starting, with TSD and replace $(t_{\star})^{-1}I_{t_{\star}}$ in the first term of the loss in Eq.˜4.3: Isolating the Source of GCPs’ Success") with its expectation $a=(t_{\star})^{-1}\mdmathbb{E}[I_{t_{\star}}]$. We set the initial noise $I_{0}=0$ to be zero, so that $z$ only contributes to the second training loss. Finally, we sample with $z=0$ to isolate the effect of adding stochasticity at training time, without stochasticity at inference time (as suggested by Table˜1).

<!-- chunk {"id": "body-0054", "role": "body", "section": "MIP: a minimal intermediate between RCPs and GCPs", "weight": 1.0} -->

Since we provide supervision for both first step ${}^{\textbf{{MIP}}}(o,I_{0}=0,t=0)$ and second step ${}^{\textbf{{MIP}}}(o,I_{0}=I_{t_{\star}},t=t_{\star})$ with ground truth action $a$, MIP also exemplifies SIC in its simplest form. We compare MIP to Shorctu Models in Section˜4.3: Isolating the Source of GCPs’ Success").

<!-- chunk {"id": "body-0055", "role": "body", "section": "MIP: a minimal intermediate between RCPs and GCPs", "weight": 1.0} -->

Finally, we study residual regression (RR), which replaces $I_{t_{\star}}$ in Eq.˜4.4: Isolating the Source of GCPs’ Success") with its expectation over $z$: $\mdmathbb{E}[I_{t_{\star}}]=t_{\star}a$. This preserves SIC (Component˜3: Isolating the Source of GCPs’ Success")) yet removes stochasticity injection. Full details are provided in Appendix˜A.

<!-- chunk {"id": "body-0056", "role": "body", "section": "MIP: a minimal intermediate between RCPs and GCPs", "weight": 1.0} -->

To summarize, minimal iterative policy (MIP), straight-flow (SF) and residual regression (RR) represent all combinations of Components˜3: Isolating the Source of GCPs’ Success") and 2: Isolating the Source of GCPs’ Success") without exhibiting Component˜1: Isolating the Source of GCPs’ Success").

<!-- chunk {"id": "body-0057", "role": "body", "section": "Components˜3: Isolating the Source of GCPs’ Success\") and 2: Isolating the Source of GCPs’ Success\") drive performance: MIP matches Flow", "weight": 1.0} -->

Based on the design space parsing in Section˜4: Isolating the Source of GCPs’ Success"), we are able to systematically ablate different design components' contribution to the final performance in Figs.˜8: Isolating the Source of GCPs’ Success") and 4: Isolating the Source of GCPs’ Success"). Our evaluation shows that either stochasticity injection (Component˜2: Isolating the Source of GCPs’ Success"), exhibit by SF) or supervised iterative computation (Component˜3: Isolating the Source of GCPs’ Success"), exhibited by RR) in isolation do not match the success of GCPs. MIP, being the only method which combines *supervised* iterative computation and stochasticity injection, achieves success on par with flow. Thus we conclude: the performance of GCPs comes from combining stochastic injection and iterative computation. Distributional training appears to be the least important factor.

<!-- chunk {"id": "body-0058", "role": "body", "section": "Remark 4.1", "weight": 1.0} -->

Section˜A.3 exhibits two further variants which preserve Components˜2: Isolating the Source of GCPs’ Success") and 3: Isolating the Source of GCPs’ Success"): one that does not supervise intermediate steps, and a second which does not condition a time step $t_{\star}$. The latter does not enable network to learn separate functions across time steps. Both perform even worse than regression, confirming the importance of supervision of intermediate steps and decoupling network behavior across time steps.

<!-- chunk {"id": "body-0059", "role": "body", "section": "MIP compares favorably to shortcut policies", "weight": 1.0} -->

MIP is superficially similar to Shortcut Models (boffiFlowMapMatching2025; boffiHowBuildConsistency2025; songConsistencyModels2023; gengMeanFlowsOnestep2025), as both perform inferences in few-steps. Shortcut models correctly learn target distributions (i.e. satisfy Component˜1: Isolating the Source of GCPs’ Success")) by integrating a flow field. On the other hand, MIP are trained to predict the conditional mean of the interpolant, which is not a valid objective for distribution fitting. The performance of MIP supports our overall theme that, in robotic control applications, faithfully capturing the full conditional distribution over actions is not needed for control performance.

<!-- chunk {"id": "body-0060", "role": "body", "section": "MIP compares favorably to shortcut policies", "weight": 1.0} -->

While being competitive with flow models performance-wise, MIP takes less integration steps (number of function evaluations (NFEs) = 2) compared to flow models (NFEs = 9). To further validate the computation efficiency of MIP, we compare it with consistency models which accelerate the sampling process of flow by distilling the learned flow into a shortcut model (songConsistencyModels2023; boffiFlowMapMatching2025; fransOneStepDiffusion2024; gengMeanFlowsOnestep2025). We benchmark MIP against consistency trajectory model (CTM) (kim2023consistency), where latter is trained in two-stage manner. Thus, CTM requires twice as many training time compared to MIP. As shown in Table˜5: Isolating the Source of GCPs’ Success"), MIP matches, and often outperforms CTM on most challenging tasks since CTM exhibits certain level of performance degradation compared to the teacher flow models. This again highlights that the fact that distributional learning is not necessary condition for GCPs performance and bypassing it offers computation efficiency at training and inference time.

<!-- chunk {"id": "body-0061", "role": "body", "section": "MIP compares favorably to shortcut policies", "weight": 1.0} -->

We further compare MIP with other few-step methods like Lagrangian map distillation (LMD) (boffiFlowMapMatching2025) and present full results in Section˜B.8.

<!-- chunk {"id": "body-0062", "role": "body", "section": "Manifold adherence, not reconstruction, drives performance", "weight": 1.0} -->

MIP, and the absence of multimodality, suggest a better ability to approximate the expert more accurately on training data. We test this by evaluating the $L_{2}$-error, i.e., reconstruction error, on validation set. Surprisingly, we find that MIP, Flow, and RCP exhibit the *same* validation loss; hence validation loss does predict their relative performance. Section˜E.1 reveals that validation loss doesn't correlate with performance across other axes of variation. Indeed, policy performance requires taking good actions on *o.o.d. states* under compounding error at deployment time (simchowitz2025pitfalls).

<!-- chunk {"id": "body-0063", "role": "body", "section": "Manifold adherence, not reconstruction, drives performance", "weight": 1.0} -->

Thus, we study a proxy which reflects performance in o.o.d. situations. We perturb expert trajectories in dataset as described in Section˜C.1, and evalute a novel metric that we call the *off-manifold norm*. Informally, this measures the projection error of a predicted action $a$ onto the space spanned by expert actions at neighboring states; see Section˜E.2 a for formal definition. Our metric assesses the quality of actions under simulated compounding error. Table˜6 reports both $L_{2}$ validation loss and off-manifold $L_{2}$ norm for different methods: while all methods achieve low validation loss, only MIP and Flow are able to achieve low off-manifold $L_{2}$ norm, indicating their better manifold adherence. As SF does not exhibit the same benefit, we conclude that supervised iterative computation facilitates projection onto the manifold of expert actions by refining the prediction across sequential steps. Figure˜9 provides additional illustraion of manifold hypothesis: with more iterations, flow model samples more plausible trajectories, which goes to the side of T-shape object rather than colliding right into it.

<!-- chunk {"id": "body-0064", "role": "body", "section": "Manifold adherence, not reconstruction, drives performance", "weight": 1.0} -->

Appendix˜J provides additional confirmation of this hypothesis on comprehensive toy experiments: GCPs are no better than RCP at fitting high frequency functions, but exhibit lower on-manifold error, suitably defined.

<!-- chunk {"id": "body-0065", "role": "body", "section": "Manifold adherence, not reconstruction, drives performance", "weight": 1.0} -->

Why manifold adherence matters for control. We conjecture that, for high-precision tasks, the sensitivity to errors is not homogeneous across error directions in action space. Our findings present preliminary evidence that some form an "on-manifold inductive bias" directly aligns with minimizing error along relevant directions, yet is permissive to error in directions of lesser consequence. We think that rigorously establishing this hypothesis is an exicting direction for future work.

<!-- chunk {"id": "body-0066", "role": "body", "section": "Manifold adherence, not reconstruction, drives performance", "weight": 1.0} -->

No known mechanism accounts for greater manifold adherence in GCPs vs. RCPs. There is a growing body of literature that shows that, if training data are supported on a given low dimensional manifold $\mathcal{M}$, then generative models learn to project onto $\mathcal{M}$ (boffi2024shallowdiffusionnetworksprovably; permenter2024interpretingimprovingdiffusionmodels). However, to our knowledge, there is no work that explains why this inductive bias would be *stronger* than what would be achieved with a well-trained regression model. Specifically, if $o\mid a$ lies in some (local) manifold, regression too should learn to project onto it.

<!-- chunk {"id": "body-0067", "role": "body", "section": "Manifold adherence, not reconstruction, drives performance", "weight": 1.0} -->

One might conjecture that the iterative computation provides many changes to predict an action that "stick" to the action manifold. However, such a mechanism would require that once an on-manifold action is predicted, subsequent predictions do not nudge the prediction off-manifold. In Appendix˜I, we show that simple arguments based on implicit regularization in linear models do not suffice to explain this hypothesis, at least for MIP. Much like the usefulness of manifold adherence for control described above, the mechanism behind manifold adherence remains a mystery for future study.

<!-- chunk {"id": "body-0068", "role": "body", "section": "Stochasticity stabilizes iterative computation", "weight": 1.0} -->

We recall from Figure˜8: Isolating the Source of GCPs’ Success") that SF matches regression, whilst RR under-performs regression. This suggests that sequential action generation is highly brittle in the absence of stochasticity (permenter2024interpretingimprovingdiffusionmodels). Our findings support the hypothesis that stochasticity injection serves to provide "coverage" of the generative process as illustrated in Figure˜10. Note that this is different from task MDP-level augmentation like image augmentation or exploratory data collection since the augmentation happens in iterative generative process. Specifically, we can think of learning to perform two-stage action generation as an "internal" behavior cloning problem (ren2024diffusion) under the dynamics induced by the generative process. Injecting stochasticity amounts to enhancing coverage of the action $\hat{a}_{0}$ in the first step of MIP, thus enable iterative improvement with more NFEs (Section˜B.7).

<!-- chunk {"id": "body-0069", "role": "body", "section": "Stochasticity stabilizes iterative computation", "weight": 1.0} -->

Its benefits are analogous to trajectory noising effective in other behavior cloning applications (laskey2017dart; block2023butterfly; block2024provable; simchowitz2025pitfalls; zhang2025actionchunkingexploratorydata). Similar benefits are found in the improved sensitivity analysis of diffusion relative to flows (albergo2024stochastic).

<!-- chunk {"id": "body-0070", "role": "body", "section": "Architecture remains essential for scaling", "weight": 1.0} -->

While all methods do scale, regression, enjoys stronger relative performance at the smallest model sizes but scales more poorly than flow and MIP with increased model capacity (Fig.˜11). We conjecture that supervised iterative computation can better utilize larger models, both by introducing more supervision steps at training, and by providing more parameters to represent different computations at successive generation steps. Nevertheless, *architecture design* plays an incredibly significant role. To showcase its importance, we ablate the performance of different method's average performance across both the 3 architectures above, and the more traditional MLP and RNN architectures, implemented with modern best practices including FiLM conditioning (perez2018film), and skip-connections (he2016deep)/LayerNorm (ba2016layer) where appropriate (details in Section˜B.2). As demonstrated in Fig.˜11, the combination of training method and architecture design has a strong yet somewhat erratic effect on both GCPs and RCP performance. In Tool-Hang, RCP achieves the best performance with an MLP architecture. In Transport, MLP with flow can even outperform more expressive architectures like Chi-Transformer.

<!-- chunk {"id": "body-0071", "role": "body", "section": "Architecture remains essential for scaling", "weight": 1.0} -->

The coupling between training and architecture choice highlights the importance of controlling architecture design when comparing across methods.

<!-- chunk {"id": "body-0072", "role": "body", "section": "Previous Works' Connection with GCP's Taxonomy", "weight": 1.0} -->

We classify GCPs into three components: distributional learning, stochasticity injection, and supervised iterative computation. Starting from regression, it has none of the three components. To model a more complex distribution, Gaussian Mixture Model (GMM) (zhuRobotLearningDemonstration2018) was used to parameterize the distribution, trained with cross entropy loss. To make the network be able to represent more complex distirbutions, prior to diffusion, non-parametric method like VAEs (zhaoLearningFineGrainedBimanual2023) was used to parameterize the distribution, trained with reconstruction loss. During the training, a latent variables is predicted to predict the style the motion by mapping it from a noise $z$. Another line of work try to improve the policy expressivity by introducing iterative compute, like implicit behavior cloning (florence2022implicit; dasariIngredientsRoboticDiffusion2024) and behavior transformer (shafiullah2022behavior). In IBC, the idea is to allow the network predict the energy function of the action rather the action itself.

<!-- chunk {"id": "body-0073", "role": "body", "section": "Previous Works' Connection with GCP's Taxonomy", "weight": 1.0} -->

Compared to diffusion, the major difference is that they do not explicitly injecting noise during training and no intermediate supervision is provided for the intermediate results. Similarly, in behavior transformer, a two step policy is introduced to first predict the policy class and then refine it with another network to achieve higher precision control. Lastly, flow-based GCPs (zhang2024flowpolicy; black2024pi_0; intelligence$p_05$VisionLanguageActionModel2025), which holds all the three components and demonstrate state-of-the-art performance on popular benchmarks. In this paper, we look into a new combination that haven't been explored before, which is the combination of stochasticity injection and supervised iterative computation.

<!-- chunk {"id": "body-0074", "role": "body", "section": "Discussion", "weight": 1.5} -->

Our comprehensive evaluation reveals a fundamental divergence between the objectives of generative modeling in vision or text and those in robotic control. We demonstrate that for control, fitting the exact data distribution (C1: Isolating the Source of GCPs’ Success")) is secondary; rather, the inductive bias of manifold adherence---facilitated by stochastic iterative computation (C2: Isolating the Source of GCPs’ Success")+C3: Isolating the Source of GCPs’ Success"))---is paramount. This insight not only demystifies the success of GCPs but also enables the design of streamlined architectures like MIP.

<!-- chunk {"id": "body-0075", "role": "body", "section": "Discussion", "weight": 1.5} -->

Theoretical Gaps. While we empirically identify manifold adherence as a proxy for closed-loop performance, a theoretical framework explaining why stochastic supervision with MSE loss induces this behavior remains elusive. Developing this theoretical grounding is a critical next step to replace exhaustive empirical benchmarking with principled policy design.

<!-- chunk {"id": "body-0076", "role": "body", "section": "Discussion", "weight": 1.5} -->

Broader Applications. Finally, our analysis focuses on behavior cloning. It remains an open question whether the benefits of the C2: Isolating the Source of GCPs’ Success")+C3: Isolating the Source of GCPs’ Success") paradigm persist in other settings, such as RL-finetuning, large-scale pretraining, or long-horizon planning. Future work should explore whether the \"myths\" of generative control hold true in these broader domains.
