<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

LeJEPA: Provable and Scalable Self-Supervised Learning without the Heuristics

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Learning manipulable representations of the world and its dynamics is central to AI. Joint-Embedding Predictive Architectures (JEPAs) offer a promising blueprint, but lack of practical guidance and theory has led to ad-hoc R&D. We present a comprehensive theory of JEPAs and instantiate it in {\bf LeJEPA}, a lean, scalable, and theoretically grounded training objective. First, we identify the isotropic Gaussian as the optimal distribution that JEPAs' embeddings should follow to minimize downstream prediction risk. Second, we introduce a novel objective - {\bf Sketched Isotropic Gaussian Regularization} (SIGReg) - to constrain embeddings to reach that ideal distribution.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Combining the JEPA predictive loss with SIGReg yields LeJEPA with numerous theoretical and practical benefits: (i) single trade-off hyperparameter, (ii) linear time and memory complexity, (iii) stability across hyper-parameters, architectures (ResNets, ViTs, ConvNets) and domains, (iv) heuristics-free, e.g., no stop-gradient, no teacher-student, no hyper-parameter schedulers, and (v) distributed training-friendly implementation requiring only approx50 lines of code. Our empirical validation covers 10+ datasets, 60+ architectures, all with varying scales and domains. As an example, using imagenet-1k for pretraining and linear evaluation with frozen backbone, LeJEPA reaches 79\% with a ViT-H/14. We hope that the simplicity and theory-friendly ecosystem offered by LeJEPA will reestablish self-supervised pre-training as a core pillar of AI research.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

Learning manipulable representations of the world and its dynamics is a long-standing question in AI, with roots dating back centuries ago [Von Helmholtz, 1867, Tolman, 1948, Gregory, 1980, Sutton, 1991, Friston, 2010]. Across domains, e.g., image recognition, robotics, physics, space exploration, the unifying question is how to learn an organized and actionable high-dimensional embedding space from observations? Using Deep Networks-parameterized nonlinear operators 𝑓 𝜽 -to map observations to embeddings is a standard first piece of that puzzle [LeCun et al., 2015, Goodfellow et al., 2016]. The second, less standardized, piece of that puzzle is how to train 𝑓 𝜽. Joint-Embedding Predictive Architectures (JEPAs) suggest training 𝑓 𝜽 by maximizing predictive agreement between the embeddings of semantically related views [Bromley et al., 1993, LeCun, 2022, Balestriero et al., 2023]. Views can come in two forms: transformations or corruptions.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

They can involve masking, cropping, blurring, temporal or spatial translations, geometric or photometric transformations, viewpoint changes, views from different sensor modalities, etc. The supervised forms involve human-produced components such as image-caption pairs, text-code pairs, etc [Tian et al., 2020]. In any case, views are expected to share some degree of semantic relationship to allow the prediction task to align 𝑓 𝜽 's embeddings towards the underlying knowledge present in the data.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

Our study proposes to break that cycle by questioning some of the fundamental design principles underpinning JEPAs. That introspection will start by asking what are the necessary conditions that JEPAs should abide by? Those minimal conditions will then act as axioms for us to design a novel and lean JEPA. We identify two axioms: (i) solving the prediction task while (ii) enforcing an isotropic Gaussian distribution of the embeddings Alas, JEPA's prediction task admits failure modes, such as representation collapse, where 𝑓 𝜽 maps all inputs to nearly identical embeddings (complete collapse) or to a lowdimensional subspace (dimensional collapse) [Jing et al., 2021][Jing et al., 2021, Cosentino et al., 2022, Balestriero and LeCun, 2022].

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

To mitigate such shortcut solutions, state-of-the-art recipes rely on heuristics-stop-gradient [Chen et al., 2020a], asymmetric view generation [Wang et al., 2022], teacher-student networks with carefully tuned EMA schedules [Caron et al., 2021, Tian et al., 2021], explicit normalization and whitening layers [Ermolov et al., 2021, Chen et al., 2021]-and a delicate balance of hyperparameters. As a result, today's JEPA training is brittle and most research has shifted toward scaling data [Vo et al., 2024], models [Fan et al., 2025] and even post-training Rodas et al. while leaving the theoretical foundations of JEPAs largely unexplored.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Introduction", "weight": 1.5} -->

(Section 3). While (i) follows standard practice [Balestriero and LeCun, 2022], we introduce in Section 4 a novel distribution matching objective-Sketched Isotropic Gaussian Regularization (SIGReg)-to enforce (ii). The use of SIGReg not only removes the need for the numerous heuristics previously employed to prevent representation collapse, but SIGReg also exhibits favorable scaling properties as its memory and computational complexity is linear in dimension and sample size. Crucially, SIGReg's isotropic Gaussian enforcement solves the collapsed shortcut solution and provably minimizes the model's expected risk over the space of downstream tasks to be encountered post-training.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Introduction", "weight": 1.5} -->

The resulting JEPA solution-coined Latent-Euclidean JEPA (LeJEPA)-is introduced in Section 5. Beyond theoretical optimality, LeJEPA offers numerous benefits such as (i) provable statistical guarantees, (ii) removal of heuristics such as teacher-student networks, (iii) linear memory and computational complexity, and most importantly (iv) a unified design with a single trade-off parameter that works out of the box across datasets, architectures and scales (see Section 6). We summarize our contributions below.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Introduction", "weight": 1.5} -->

Contribution 3: We design LeJEPA, a statistically optimal JEPA that eliminates collapse by construction. By combining JEPA's predictive objective with SIGReg targeting the isotropic Gaussian, we introduce LeJEPA -LatentEuclidean JEPA (Section 5). LeJEPA requires only a single hyperparameter, eliminates representational collapse without stop-gradients or teacher-student architectures, and transfers across architectures and datasets without hyperparameter tuning. This demonstrates that principled Contribution 1: We prove the optimal embedding distribution for foundation models. We establish that the isotropic Gaussian uniquely minimizes downstream prediction risk across broad task families. In Section 3, we derive this result rigorously for both linear (Section 3.1) and nonlinear probes (Section 3.2), providing the first principled answer to what distribution 𝑓 𝜽 's embeddings should follow. This theoretical result transforms JEPA design from heuristic exploration to targeted optimization. Contribution 2: We introduce SIGReg, a distribution matching objective that uniquely combines provable correctness with computational efficiency at scale.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Introduction", "weight": 1.5} -->

We present Sketched Isotropic Gaussian Regularization (SIGReg), a novel objective that enforces distributional alignment via random projections and characteristic-function matching (Section 4 and Figure 2). SIGReg provides statistical guarantees (Sections 4.1 and 4.2) while achieving linear complexity and bounded gradients-a combination that existing distribution matching methods do not offer. Critically, its projection-based construction defeats the curse of dimensionality (Section 4.3), making it both theoretically sound and practically efficient for high-dimensional embeddings.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Introduction", "weight": 1.5} -->

Contribution 4: We validate LeJEPA at scale across diverse architectures and establish in-domain pretraining as viable. Our experiments (Section 6) span ViTs, ConvNeXts, ResNets, MaxViTs, and Swin Transformers at scales approaching 1 billion parameters, where LeJEPA matches or exceeds state-of-the-art methods while maintaining training simplicity and robustness. Critically, on domain-specific datasets (, Food101), LeJEPA outperforms DINOv2-based transfer learning when pretrained directly on target data. This challenges the transfer learning paradigm and demonstrates that principled SSL can unlock effective in-domain pretraining-previously considered impractical for small datasets.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Notations and Definitions", "weight": 1.0} -->

Data. Weareinpossessionofadatasetofshape ( 𝑁,𝑉, 𝐷 ) ∈ N ∗ 3 where 𝑁 is the number of samples, 𝑉 is the number of views, and 𝐷 is the dimension. One entry of this dataset is accessed via 𝒙 𝑛,𝑣,𝑑. Those dimensions are often interpreted as follows: ( N ) is the number of independent samples, e.g., different images or different videos, ( V ) is the number of views, e.g., data-augmentations for images, frames for videos, and ( D ) is the dimension of each 𝒙 𝑛,𝑣, e.g., number of RGB pixels for images. In many cases the ordering over 𝑉 is given by time -but in some cases, e.g., data-augmentation of an image, ordering becomes irrelevant. Our study does not require any particular choice to organize one's dataset into a ( 𝑁,𝑉, 𝐷 ) tensorand none of our theory and implementation assumes a particular design decision for that tensor.

<!-- chunk {"id": "body-0014", "role": "body", "section": "Notations and Definitions", "weight": 1.0} -->

However, we will rely on the following two properties, ( independence ) the samples 𝒙 𝑛, 𝒙 𝑛 ′ have been obtained independently from each other ∀ 𝑛 ≠ 𝑛 ′, and ( identically distributed ) the sampling process was identical among 𝒙 𝑛, ∀ 𝑛.

<!-- chunk {"id": "body-0015", "role": "body", "section": "Notations and Definitions", "weight": 1.0} -->

JEPAs. A foundation model is any system, e.g., a DN, able to solve numerous downstream tasks without requiring any change in its internal parameters 𝜽. This is in sharp contrast with a supervised model that only considers its training task. JEPAs have formally been introduced by LeCun as a vehicle to produce foundation models. The core building blocks of JEPAs rely on numerous wellestablished techniques such as siamese networks [Bromley et al., 1993] and predictive coding [Helmholtz et al., 1867, Bruner and Postman, 1949]. While the exact blueprint of Deep Networks. Today's AI solutions rely on Deep (Neural) Networks (DNs), which are compositions of a large number of parameterized linear and nonlinear operators. We denote the DN's mapping as 𝑓 𝜽: R 𝐷 → R 𝐾 with 𝐾 the dimension of the embedding space. The internals of 𝑓 𝜽 are designed by the researcher to incorporate as much prior knowledge about the data as possible. The details of 𝑓 𝜽 are irrelevant to our study-as we will see the proposed LeJEPA works out-of-the-box on any 𝑓 𝜽.

<!-- chunk {"id": "body-0016", "role": "body", "section": "Notations and Definitions", "weight": 1.0} -->

In any case, all the learnable parameters are gathered in the vector 𝜽 ∈ R 𝑃, with 𝑃 counting the total number of parameters. A central challenge in AI research is to design the right architecture and training objective so that 𝜽 can be learned from gradient descent to ultimately produce a useful system, or foundation model, 𝑓 𝜽.

<!-- chunk {"id": "body-0017", "role": "body", "section": "Notations and Definitions", "weight": 1.0} -->

Sec 1: Intro | Sec 2: Background | Sec 3: Why Gaussian? | Sec 4: SIGReg | Sec 5: LeJEPA | Sec 6: Experiments JEPAs varies greatly between use-cases, they all rely on two core principles: (i) being able to predict the embedding of a view 𝒙 𝑛,𝑣 from the embedding of another view 𝒙 𝑛,𝑣 ′, 𝑣 ′ ≠ 𝑣, all while (ii) ensuring that the embeddings do not become degenerate. Concretely, once a JEPA is designed and trained, it should be able to solve numerous downstream tasks in zero or few shots. The JEPA objective function, along with some examples for 𝒙, is provided in Equation. The predictability criterion can be done by directly comparing the embeddings of the partial views 𝐸𝑛𝑐 (𝒙 𝑛,𝑣,.) and 𝐸𝑛𝑐 (𝒙 𝑛,𝑣 ′,.) with a metric, e.g., ℓ 𝑝.

<!-- chunk {"id": "body-0018", "role": "body", "section": "Notations and Definitions", "weight": 1.0} -->

In some cases, an additional DN coined Pred, is employed to compare 𝑃𝑟𝑒𝑑 (𝐸𝑛𝑐 (𝒙 𝑛,𝑣,.)) against 𝐸𝑛𝑐 (𝒙 𝑛,𝑣 ′,.) -which is only justified when there exists an asymmetry between the information content of the different views, e.g., by conditioning the predictions on observed actions from robotics data [Khazatsky et al., 2024].

<!-- chunk {"id": "body-0019", "role": "body", "section": "The Need for Reliable Pretraining", "weight": 1.0} -->

The JEPA's prediction task is designed based on a priori knowledge of the data. Its design is often quite natural since it is relatively intuitive to form 𝒙 so that its views share the relevant information content one hope to capture. On the other hand, the design of the 'anti-collapse' criterion is much closer to a game of Whac-A-Mole. Today's designs rely on many different under-specified safeguards which are carefully combined in the hope that degenerate shortcut solutions are avoided during training. Such mechanisms include (i) feature whitening [Ermolov et al., 2021, Bardes et al., 2021], (ii) negative samples [Chen et al., 2020a, He et al., 2020], and (iii) asymmetric views and teacher-student networks with stop-gradient [Caron et al., 2021, Assran et al., 2023].

<!-- chunk {"id": "body-0020", "role": "body", "section": "The Need for Reliable Pretraining", "weight": 1.0} -->

Those mechanisms all suffer from at least two of the following limitations: (i) under-specification, i.e., the criteria can be minimized while embeddings are in a degenerate configuration, (ii) quadratic time and memory complexity with mini-batch size and/or embedding dimension, (iii) sensitivity to data distribution, hyperparameters, architecture, and (iv) lack of theoretical understanding and guarantees.

<!-- chunk {"id": "body-0021", "role": "body", "section": "The Need for Actionable Theory", "weight": 1.0} -->

For decades, the two major solutions for AI were supervised learning [LeCun et al., 2015] and learning by reconstruction [Rumelhart et al., 1986]-sometimes combined together, e.g., for semi-supervised learning [Kingma et al., 2014]. In supervised learning, the labels both ensure that semantically similar samples are close to each other in embedding space while preventing complete representation collapse. In particular, it is possible to measure the amount of collapse in supervised learning as a function of the number of classes [Papyan et al., 2020]. The reconstruction objective is similarly well suited to prevent representation collapse as the original input must be recovered from the embeddings, i.e., the embeddings must be as informative about the input as possible-up to some optional denoising tasks that users can setup as part of the training [Vincent et al., 2010].

<!-- chunk {"id": "body-0022", "role": "body", "section": "The Need for Actionable Theory", "weight": 1.0} -->

Because supervised and reconstruction-based learning have been widely studied for decades, there exists a large body of work to explain and inform practical designs-as well as studying their limitations in producing foundation models [Balestriero and LeCun, 2024, Van Assel et al., 2025]. This is not the case for the more recent JEPAs where empirical advances quickly outpace anyone hoping to delve into their inner workings. This dynamic led the community to focus on post-hoc theoretical justification of already found solutions [Liu et al., 2021, Shwartz Ziv and LeCun, 2024, Shwartz-Ziv et al., 2022, Zhang et al., 2023]. In most cases, those studies involve the Mutual Information (MI) [Shannon, 1948, Cover, 1999] whose different bounds recover established methods [Gutmann and Hyvärinen, 2010, Ma and Collins, 2018, Oord et al., 2018, Poole et al., 2019, Hjelm et al., 2018, McAllester and Stratos, 2020]. Because existing studies focus on explaining and interpreting already developed JEPAs, too little principled guidance and innovation has been brought forward.

<!-- chunk {"id": "body-0023", "role": "body", "section": "The Need for Actionable Theory", "weight": 1.0} -->

Instead, most of the recent empirical advances take the form of collecting larger dataset, scaling up pre-existing training recipes [Goyal et al., 2019, Chen et al., 2020b, Oquab et al., 2023, Fan et al., 2025], and deriving novel data curation processes [Vo et al., 2024, Kerdreux et al., 2025].

<!-- chunk {"id": "body-0024", "role": "body", "section": "The Need for Actionable Theory", "weight": 1.0} -->

In contrast, our goal in the following Sections 3 to 5 will be to derive a novel JEPA solution from first principles, i.e., whose design relies on proved necessary conditions for optimality, and with a pretraining recipe that can finally reconcile exploratory research, scalability, and state-of-theart performances.

<!-- chunk {"id": "body-0025", "role": "body", "section": "Latent Euclidean: Embeddings Should be Isotropic Gaussian", "weight": 1.0} -->

We address a fundamental question: which distribution should Enc ( 𝒙 ) follow to minimize empirical risk on any downstream task? We prove that the isotropic Gaussian is the unique optimal distribution for both linear (Section 3.1) and nonlinear probing (Section 3.2), with geometric intuition provided in Section 3.3. This theoretical result establishes the necessary design principle for our JEPA; Section 4 then provides the practical implementation to achieve it.

<!-- chunk {"id": "body-0026", "role": "body", "section": "Linear Probing", "weight": 1.0} -->

We begin by identifying the optimal distribution for 𝑓 𝜽 's embeddings by analyzing linear probes-one of the most popular methods for frozen encoder evaluation. Specifically, we ask: which distribution for 𝑓 𝜽 ( 𝒙 ) would be most favorable for solving arbitrary downstream tasks, i.e., for any realization of targets 𝒚 ?

<!-- chunk {"id": "body-0027", "role": "body", "section": "Linear Probing", "weight": 1.0} -->

Denote as 𝒁 ∈ R 𝑁 × 𝐾 the matrix of 𝑁 embeddings, each 𝐾 -dimensional, from 𝑓 𝜽 (𝒙 𝑛). The unknown corresponding labels are denoted as 𝒚 ∈ R 𝑁. Withoutlossofgenerality, we consider univariate targets; the following analysis extends to multivariate targets. The linear probe minimizes the following least square problem [Bishop and Nasrabadi, 2006] where ˆ 𝛽 is the optimal probe parameters, and 𝜆 ≥ 0 is an hyperparameter controlling the Tikhonov regularizer strength [Bishop, 1995, Golub et al., 1999]. Despite not knowing 𝒚, it is possible to describe the bias and variance of the estimator ˆ 𝛽 as a function of the distribution of 𝒁. Consider two embeddings with identical column spans 𝒁 aniso, 𝒁 iso. 𝒁 aniso 's covariance matrix eigenvalues are given by { 𝜆 𝑘 } 𝐾 𝑘 = 1 with at least two distinct values, while 𝒁 iso 's covariance matrix eigenvalues are all equal to 1 𝐾 ˝ 𝐾 𝑘 = 1 𝜆 𝑘.

<!-- chunk {"id": "body-0028", "role": "body", "section": "Linear Probing", "weight": 1.0} -->

Hence, the two candidate embeddings 𝒁 aniso, 𝒁 iso capture the same intrinsic features and have same energy, but different geometries.

<!-- chunk {"id": "body-0029", "role": "body", "section": "Nonlinear Probing", "weight": 1.0} -->

To allow for more flexible evaluation of the pretrained encoder 𝑓 𝜽, it has become increasingly common to work with a nonlinear probe. We analyze two widely-used nonlinear methods: radius-based k-NN [Taunk et al., 2019, Sun and Huang, 2010, Zhang et al., 2017, Abu Alfeilat et al., 2019] for its simplicity and kernel methods [Nadaraya, 1964, Watson, 1964] for their theoretical tractability.

<!-- chunk {"id": "body-0030", "role": "body", "section": "Nonlinear Probing", "weight": 1.0} -->

As in Section 3.1, we ask ourselves which distribution of embeddings would be preferable for a foundation model. We first define our prediction function. The training data consists of the 𝑁 embeddings along with their training labels {(𝒛 𝑛, 𝒚 𝑛)} 𝑁 𝑛 = 1. The prediction, using radius-based k-NN for a query vector 𝒒 is formed as where /u1D4A9 𝑟 0 (𝒒) = { 𝑛: ‖ 𝒛 𝑛 -𝒒 ‖ ≤ 𝑟 0 }. The specific choice of radius 𝑟 0 controls how many neighbors predictions are averaged to form the query's prediction. The kernel's prediction at a query 𝒒 ∈ R 𝐾 is given by Wesearch over all distributions of Z subject to a fixed total variance constraint, e.g., Tr (Cov (𝒁)) = 𝜅 1 or ‖ Cov (𝒁)‖ 𝐹 = 𝜅 2. The specific value of 𝜅 does not affect the optimal dis- tribution shape.

<!-- chunk {"id": "body-0031", "role": "body", "section": "Nonlinear Probing", "weight": 1.0} -->

Following the same type of derivations as done in the linear regime-with the exception of some additional regularity conditions-we are able to precisely identify the isotropic Gaussian as the unique optimum to minimize bias as formalized below.

<!-- chunk {"id": "body-0032", "role": "body", "section": "Geometric and Practical Insights", "weight": 1.0} -->

We now empirically validate that the isotropic Gaussian is optimal when no information about downstream tasks is available. We focus on linear probing (Section 3.1), where all considered distributions have the same total variance.

<!-- chunk {"id": "body-0033", "role": "body", "section": "Geometric and Practical Insights", "weight": 1.0} -->

When employing a linear probe, an anisotropic distribution increases both bias (with Tikhonov regularization) and variance. Examining bias first (lemma. 1), we present in Figure 18 visualizations for both continuous regression and discrete classification tasks. We observe that the cosine similarity between estimated and ground-truth parameters equals 1 only for isotropic distributions, degrading for anisotropic cases regardless of sample size or regularization strength. Regarding variance (lemma. 2), we show in Figure 3 that learned parameters vary significantly more across training sets when the covariance is anisotropic (right) compared to isotropic (left)-even when using logistic regression instead of OLS. Figure 17 further illustrates this effect, showing the distribution of learned 𝛽 parameters across different training samples for both cases. The anisotropic distribution clearly produces higher-variance estimators.

<!-- chunk {"id": "body-0034", "role": "body", "section": "Geometric and Practical Insights", "weight": 1.0} -->

These theoretical and empirical results establish our design principle for LeJEPA: embeddings 𝑓 𝜽 ( 𝒙 ) should follow an isotropic Gaussian distribution to minimize worst-case risk across downstream tasks encountered post-training. Section 4 introduces a novel regularizer to achieve this distribution.

<!-- chunk {"id": "body-0035", "role": "body", "section": "SIGReg: Reliable Isotropic Gaussian Regularization in High-Dimension", "weight": 1.0} -->

Having established the isotropic Gaussian as the optimal embedding distribution (Section 3), we now introduce Sketched Isotropic Gaussian Regularization (SIGReg)-a distribution matching objective that is simultaneously (i) differentiable, (ii) scalable, (iii) provable, and (iv) interpretable. SIGReg builds on three key innovations. First, we formulate distribution matching as a statistical test under the null hypothesis 𝑃 𝜽 = 𝑄 (Section 4.1). Second, we identify a test that guarantees bounded gradients and curvature while maintaining linear complexity and efficient multi-GPU scaling (Section 4.2). Third, SIGReg bypasses the curse of dimensionality, eliminating collapsed shortcut solutions entirely (Section 4.3).

<!-- chunk {"id": "body-0036", "role": "body", "section": "Hypothesis Testing as a Judge", "weight": 1.0} -->

Asking for 𝑓 𝜽 (𝒙) 's distribution 𝑃 𝜽 to match a target distribution 𝑄 is typically done by creating various measures of distance or divergence, and estimating them in highdimension. Weproposeadifferentstartingpointgrounded in statistics. Consider the hypothesis testing framework [Fisher, 1928, Neyman and Pearson, 1933] given by with 𝐻 0 being referred to as the null hypothesis. That is, we are asking in Equation if there is enough empirical evidence to reject the null. To answer that question, one (i) employs a test-statistic, i.e., a single scalar value summarizing the evidence from the empirical samples, (ii) determines a critical value 𝜏𝛼 for the test-statistic based on the probability 𝛼 of Type I error, i.e., of mistakenly rejecting a true null hypothesis, (iii) compares the test-statistic to the critical value 𝜏𝛼; if the test-statistic exceeds 𝜏𝛼, reject the null hypothesis. If the null is not rejected, we can only claim that there is not sufficient empirical evidence against 𝑃 𝜽 = 𝑄.

<!-- chunk {"id": "body-0037", "role": "body", "section": "Hypothesis Testing as a Judge", "weight": 1.0} -->

As it stands, Equation remains impractical in large dimension as existing tests have at least quadratic complexity with the number of samples considered (more details in Section F). We thus propose to derive a sketching strategy by decomposing Equation into simpler univariate tests. Denoting the push-forward distributions 𝑃 (𝒂) 𝜽 ≜ (𝒂 ⊤) # 𝑃 𝜽 and 𝑄 (𝒂) ≜ (𝒂 ⊤) # 𝑄, we can define the following directional univariate test for a given directional unit-norm vector 𝒂 ∈ /u1D4AE 𝐾 -1. The corresponding directional test-statistic of Equation is computed as 𝑇 ({ 𝒂 ⊤ 𝑓 𝜽 (𝒙 𝑛)} 𝑁 𝑛 = 1). Examples of tests 𝑇 will be provided in the later Section 4.2. Repeating that process over a set of 𝑀 directions A ≜ { 𝒂 1,..., 𝒂 𝑀 } and aggregating the individual values lead to the following global test-statistic We now provide a formal statement asserting the consistency of Equation to test the original multivariate null hypothesis from Equation. Our result leverages the well-known union-intersection principle [Roy, 1953], and a slightly modified Cramér-Wold theorem.

<!-- chunk {"id": "body-0038", "role": "body", "section": "SIGReg: Sketching the Epps-Pulley Test is Stable and Scalable", "weight": 1.0} -->

Our proposed regularizer-coined Sketched Isotropic Gaussian Regularization (SIGReg)-follows directly from thm. 2 using any statistical test 𝑇 targeted towards the isotropic Gaussian, illustrated in Figures 2 and 5, and formalized below.

<!-- chunk {"id": "body-0039", "role": "body", "section": "Moments are Unstable and Insufficient", "weight": 1.0} -->

The first family of statistics we consider are moment-based. Taking the standard Gaussian as an instanciation for the moments, we can define the Jarque-Bera [Jarque and Bera, 1980] test that compares the third and fourth moments, i.e., skewness and kurtosis, as Figure 5. Constructed data density with 'X' distribution whose marginals are standard Gaussian and whose covariance is identity (left densities). Applying 𝑀 = 10 projections on the half circle directions produces 10 univariate distributions that can be compared against a standard Gaussian (left) using any preferred statistic from Section 4.2. The appropriate direction is able to capture the degenerate distribution of the data hereby creating a spike in the statistic value.

<!-- chunk {"id": "body-0040", "role": "body", "section": "Moments are Unstable and Insufficient", "weight": 1.0} -->

where skew is the skewness computed from the data as 1 𝑛 ˝ 𝑛 𝑖 = 1 (𝑥𝑖 -ˆ 𝜇) 3 ˆ 𝜎 3 and d kurt is the kurtosis 1 𝑛 ˝ 𝑛 𝑖 = 1 (𝑥𝑖 -ˆ 𝜇) 4 ˆ 𝜎 4. Typically, the (Jarque-Bera) test is used to see if a density follows a Gaussian distribution of any mean and variance-hence it only looks at moments 3 and 4. In our case we aim for a standard Gaussian test and thus add the usual statistics on the first two moments, leading to the extended test The (Extended Jarque-Bera) acts as a moment matching problem over the first four moments. Such moment matching methods have proven powerful not only for statistical tests but also as mean to learn parametric and nonparametric models of data.

<!-- chunk {"id": "body-0041", "role": "body", "section": "Moments are Unstable and Insufficient", "weight": 1.0} -->

The Stability and Identifiability Conundrum. Wenow explain why moment-based tests-albeit powerful-will not be suited for LeJEPA. The 𝑘 𝑡ℎ of a distribution 𝑃 is denoted as 𝑚𝑘 ( 𝑃 ). The first observation is that wellbehaved distributions abiding the Carleman's condition ˝ ∞ 𝑘 = 1 𝑚 2 𝑘 ( 𝑄 ) -1 /( 2 𝑘 ) = ∞ [Carleman,1926], such as the Gaussian, or for distributions with finite interval [Hausdorff, 1923] are uniquely determined by their moments. However, using a finite number of moments creates the following non-identifiability issue which well-known in statistics and often used as a motivation to use all moments [Lehmann and Romano, 2005].

<!-- chunk {"id": "body-0042", "role": "body", "section": "Cumulative Density Functions are Impractical", "weight": 1.0} -->

Thesecondfamilyoftests acts upon the CDF. Because those tests require sorting, let's denote the 𝑘 th order-statistics of 𝑁 samples by 𝑥 𝑘: 𝑁. Twohighly standard tests are quadratic Empirical Density Function statistics with different weighting known as Cramér-von Mises [Cramér, 1928, Von Mises, 1981] and Anderson Darling [Anderson and Darling, 1952], and given by where 𝑤 (𝑥) is a weighting function. Adding the 𝑈 2 statistics on top of Equation (Cramér-von Mises) recovers the Watson test [Watson, 1961] Figure 6. 𝑁 = 100 samples are drawn from a 1024-dimensional standard Gaussian, and the first 2 coordinates are altered to produce the 'X' distribution from Figure 5 (left-most column). For each statistic (all other columns), we perform gradient descent on the samples to minimize their value, at each iteration step with sample 𝑀 = 10 random directions to evaluate SIGReg (recall def. 2).

<!-- chunk {"id": "body-0043", "role": "body", "section": "Cumulative Density Functions are Impractical", "weight": 1.0} -->

We obtain that albeit this is a high-dimensional distribution with limited number of samples, SIGReg is able to capture the degenerate subspace and adapt the data accordingly to match an isotropic Gaussian distribution. Additional figures with varying dimensions and number of 1d projections are provided in Figure 16.

<!-- chunk {"id": "body-0044", "role": "body", "section": "Cumulative Density Functions are Impractical", "weight": 1.0} -->

We do not consider the Kolmogorov-Smirnov test [Kolmogorov, 1933] as it employs the ℓ ∞ -norm instead of the ℓ 2-norm hereby producing sparse gradients. Another common test is the Shapiro-Wilk test [Shapiro and Wilk, 1965] which we found to be unstable in practice-details are provided in Section E.

<!-- chunk {"id": "body-0045", "role": "body", "section": "Cumulative Density Functions are Impractical", "weight": 1.0} -->

Lack of Scalability and Differentiability. CDF-based tests require sorting that have been highly optimized, e.g., with the /u1D4AA ( 𝑁 log ( 𝑁 )) Quicksort algorithm [Hoare, 1962] but that nonetheless breaks the embarrassingly parallel nature of SGD-especially on multi-GPU [Tanasic et al., 2013, Maltenberger et al., 2022] due to synchronization requirements. Moreover, these tests involve non-differentiable operations (sorting and order statistics), making them unsuitable for gradient-based optimization without relaxations [Cuturi et al., 2019, Grover et al., 2019, Petersen et al., 2022]. While there exists intricate sketching solutions [Dunning and Ertl, 2019, Masson et al., 2019, Dunning, 2021], each of those solutions introduce numerous additional hyper-parameters-going against our first motivation for LeJEPA.

<!-- chunk {"id": "body-0046", "role": "body", "section": "Characteristic Functions are Stable, Scalable and Identifiable", "weight": 1.0} -->

The third family of tests is concerned with Empirical Characteristic Functions (ECF) which are the Fourier transform of the density function. The Epps-Pulley test [Epps and Pulley, 1983] is one of the most popular test and simply compares in weighted ℓ 2 -norm the ECF of the data against a target CF The first crucial observation is that the ECF being defined as ˆ 𝜙 𝑋 (𝑡) = 1 𝑛 ˝ 𝑛 𝑗 = 1 𝑒 𝑖𝑡𝑋 𝑗 is naturally differentiable and easily computed in distributed settings via efficient all\_reduce operations, as the ECF is a simple average of complex exponentials. The weight function is typically Gaussian, such as 𝑤 (𝑡) = 𝑒 -𝑡 2 / 𝜎 2 with 𝜎 commonly set to 1.

<!-- chunk {"id": "body-0047", "role": "body", "section": "Characteristic Functions are Stable, Scalable and Identifiable", "weight": 1.0} -->

Epps-Pulley has bounded loss, gradient and curvature. We now consider the remaining two families of tests: moment-based and CF-based. First, recall that moments are polynomial in the data and with extreme growth rate Other tests, e.g., based on the Entropy [Székely and Rizzo, 2005] are not considered here as they require numerous additional design choices for the univariate Entropy estimation [Silverman, 2018, Beirlant et al., 1997], e.g., using kernels [Joe, 1989], or M-estimators [Miller, 2003].

<!-- chunk {"id": "body-0048", "role": "body", "section": "Characteristic Functions are Stable, Scalable and Identifiable", "weight": 1.0} -->

Algorithm 1. SIGReg with Epps-Pulley statistic with DDP support and /u1D4AA (𝑁) time and memory complexity. x is a (N, K) tensor, num\_slices is | A | in def. 2, 'global\_step' is used for sync. sampling across GPUs and can be omited for single-GPU training. An optimized implementation with caching is also provided in our official codebase, computation times provided in Table 6. def SIGReg(x, global_step, num_slices=256): # s l i c e sampling --synced across devices --dev = dict (device=x. device) g = t o r c h. Generator (∗∗ dev) g. manual_seed (global_step) proj_shape = (x. s i z e, num_slices) A = t o r c h. randn (proj_shape, generator=g, ∗∗dev) A / = A. norm(p=2, dim=0) # --Epps-Pulley st a t.

<!-- chunk {"id": "body-0049", "role": "body", "section": "Characteristic Functions are Stable, Scalable and Identifiable", "weight": 1.0} -->

see Sec. 4.3 f o r a l t. --# i n t e g r a t i o n points t = t o r c h. l i n s p a c e (-5, 5, 17, ∗∗dev) # t h e o r e t i c a l CF f o r N and Gauss. window exp_f = t o r c h. exp (-0.5 ∗ t ∗∗2) # empirical CF -gathered across devices --x_t = (x @ A). unsqueeze ∗ t # (N, M, T) ecf = (1 j ∗ x_t). exp. mean ecf = all_reduce (ecf, op="AVG") # weighted L2 distance err = (ecf -exp_f). abs. square. mul (exp_f) N = x. s i z e ∗ world_size T = t o r c h. t r a p z (e r r, t, dim=1) ∗ N return T for higher moment-assuming they even exist.

<!-- chunk {"id": "body-0050", "role": "body", "section": "Characteristic Functions are Stable, Scalable and Identifiable", "weight": 1.0} -->

Even for well-behaved distributions, raising values to a power of 𝑘 can quickly lead to exploding gradients. This comes in sharp contrast with the ECF which is always bounded and with bounded gradients for any input distribution for the projected samples 𝑧 𝑖 = 𝒂 ⊤ 𝑓 𝜃 (𝒙 𝑛), 𝑛 = 1,..., 𝑁.

<!-- chunk {"id": "body-0051", "role": "body", "section": "How SIGReg Beats the Curse of Dimensionality", "weight": 1.0} -->

This last section seeks to characterize how many slices in A one must sample for (SIGReg) to be an effective statistical test. That design is crucial if we hope for LeJEPA to successfully converge towards isotropic Gaussian embeddings.

<!-- chunk {"id": "body-0052", "role": "body", "section": "Smoothness Beats the Curse of Dimensionality", "weight": 1.0} -->

Our first argument arguing for a favorable scaling of | A | with the embedding dimension 𝐾 relies on the smoothness of 𝑃 𝜽 as measured by its Sobolev regularity 𝛼 [Adams and Fournier, 2003]. We formalize below a bound on the directional test from Equation over all possible directions 𝒂 when the test statistic is minimized over | A | = 𝑀 directions. While we provide bounds on the expected discrepancy over random directions 𝒂 when the EP test is satisfied (equals zero) on a finite set of directions, the provided proof includes the case of moment-based and CDF-based tests as well.

<!-- chunk {"id": "body-0053", "role": "body", "section": "Smoothness Beats the Curse of Dimensionality", "weight": 1.0} -->

As | A |→∞, the bound decays as | A | -2 𝛼 /( 𝐾 -1 ), showing that | A | = 𝑂 ( 𝐾 ) directions suffice for 𝜖 -approximation when 𝛼 is large. Some examples of embedding densities with varying 𝛼 are provided in Figure 4. The following statement characterizes how the 𝑀 directions actually constrain the entire space as a function of 𝛼. The constant 𝐶 ( 𝐾, 𝛼 ) = 2 2 𝛼 𝜋 ( 𝐾 -1 )/ 2 Γ ( 𝛼 + 𝐾 -1 2 ) ( 𝐾 -1 ) Γ ( 𝛼 ) Γ ( 𝐾 -1 2 ) is visualized in Figure 15 (left) depicting how 𝛼 and | A | interact. In words, we obtain that thanks to the natural smoothness of DN-either stemming from the architecture or the implicit and explicit regularizers used during training-applying SIGReg on | A | directions can be sufficient to tightly constrain the entire space. We note that considering the worst case over 𝒂 or using low-discrepancy sequences for 𝒂 does not impact the asymptotic bounds, details provided in Section D.

<!-- chunk {"id": "body-0054", "role": "body", "section": "SGD Beats the Curse of Dimensionality", "weight": 1.0} -->

Our second argument leverages the iterative nature of DN training. Although we may use only | A | to be a few hundreds, the cumulative number of sampled directions grows linearly with training time. This resampling effect (illustrated in Figure 7, bottom) enables rapid convergence. Even small | A | achieves tight distributional matching compared to keeping the set A fi xed throughout minibatches (recall thm. 5). Our experiments show that even with | A | as low as 16 can easily outperform a fixed set with | A | of order of thousands thanks to the compounding effect of resampling at each minibatch.

<!-- chunk {"id": "body-0055", "role": "body", "section": "Empirical Validation on Synthetic Data", "weight": 1.0} -->

We conclude this section with a controlled experiment applying (SIGReg) with gradient-based training to produce isotropic embeddings. In this setup, we directly consider embeddings 𝒁 which we will differentiate and optimized to minimize (SIGReg). By directly optimizing the embeddings we are able to observe the impact of the loss without any possible constraint and regularization that would come from the architecture. We sample 𝑁 i.i.d. samples 𝒙 𝑛 in a 𝐷 -dimensional space. This sampling is based on an isotropic Gaussian distribution-but the first Algorithm 2. LeJEPA implementation-works out-of-the-box on any dataset, with DDP, with any backbone, e.g., torchvision or timm. For non-ViT architectures (e.g., ResNet), set global\_views = all\_views. We use bs for the minibatch size, SIGReg is from algorithm 1.

<!-- chunk {"id": "body-0056", "role": "body", "section": "Empirical Validation on Synthetic Data", "weight": 1.0} -->

def LeJEPA(global_views, all_views, lambd): " " " g l o b a l _ v i e w s and all_views are l i s t s of t e nsors, lambd i s a scalar " " " # embedding of global views g_emb = f o r w a r d (t o r c h. c a t (glob_views)) # embedding of l o c a l views # i f r e s n e t: skip with a_emb=g_emb a_emb = f o r w a r d (t o r c h. c a t (a l l _ v i e w s)) # LeJEPA l o s s centers = g_emb. view(-1, bs, K). mean a_emb = a_emb. view(-1, bs, K) sim = (centers -a_emb).

<!-- chunk {"id": "body-0057", "role": "body", "section": "Empirical Validation on Synthetic Data", "weight": 1.0} -->

square.mean sigreg = mean(SIGReg(emb, global_step) f or emb i n a_emb) return (1-lambd)∗sim + lambd∗sigreg two dimensions are again set to the adversarial 'X' shape. That is, among the 𝐷 dimensions, only two must be transformed as all the other ones already obey the isotropic Gaussian target distribution. We then make the samples 𝒙 𝑛 differentiable and optimize then to minimize the value of the different statistical tests compute on 𝑀 random 𝑀 random directions. Those directions are resampled after each gradient step-which follows the procedure we will employ in LeJEPA. We present the results in Figure 6 demonstrating that even in challenging case, i.e., 𝐷 = 512 and 𝑀 = 16, SIGReg is able to detect the two degenerate dimensions and unfold them back to how they should look like under the target distribution.

<!-- chunk {"id": "body-0058", "role": "body", "section": "LeJEPA: Stable and Scalable Implementation", "weight": 1.0} -->

HavingestablishedthatisotropicGaussiansaretheoptimal embedding distribution for foundation models (Section 3) and introduced SIGReg to achieve this distribution (def. 2), we now present the complete LeJEPA framework. We first evaluate candidate statistical tests (Sections 4.2.1 and 4.2.2) and identify characteristic function-based tests as optimal for gradient-based training (Section 4.2.3). The full LeJEPA implementation follows in Section 5.1.

<!-- chunk {"id": "body-0059", "role": "body", "section": "LeJEPA: SIGReg + Prediction Loss", "weight": 1.0} -->

We now discuss the implementation of LeJEPA starting with SIGReg and followed by the prediction and total losses.

<!-- chunk {"id": "body-0060", "role": "body", "section": "LeJEPA: SIGReg + Prediction Loss", "weight": 1.0} -->

The SIGReg Loss. We chose (Epps-Pulley) for its provable boundedness (thm. 4) and its scalability. Its implementation follows exactly the equation except for the integrate which is estimated using a quadrature approximation. We find that the simple trapezoidal quadrature rule is sufficient even with as few knots as 17, as ablated in Figure 20. In particular, we leverage the symmetry of the integrand to double the number of knots for free, see the official code. On the other hand, the use of minibatches introduces a bias vanishing at rate /u1D4AA ( 1 / 𝑁 ), as formalized below.

<!-- chunk {"id": "body-0061", "role": "body", "section": "Relation to Prior Work", "weight": 1.0} -->

Prior to presenting our experiments (Section 6), we conclude by discussing how our proposed LeJEPA and SIGReg objective relate to existing frameworks in the literature.

<!-- chunk {"id": "body-0062", "role": "body", "section": "Relation to Prior Work", "weight": 1.0} -->

While there is no existing solution employing such slicing and distribution matching for JEPAs, there exists similar pipelines for generative models and optimal transport. Notably, the Sliced Score Matching [Song et al., 2020] proposes to leverage univariate slicing of the space to ease the estimation of a density for generative models. In a similar vein, the sliced Wasserstein distance [Bonneel et al., 2015, Nguyen and Ho, 2023] uses such strategy to speed up and improve optimal transport. Furthermore, when the integral of the (Epps-Pulley) test is computed exactly, as opposed to our quadrature, each slice loss value recovers the kernel MMD [Sriperumbudur et al., 2010, Gretton et al., 2012, Chwialkowski et al., 2016] measuring the distance between two distributions-albeit with a quadratic complexity. Lastly, it is possible to recover some existing SSL frameworks in the limit by employing LeJEPA with a particular test-instead of the preferred (Epps-Pulley).

<!-- chunk {"id": "body-0063", "role": "body", "section": "Relation to Prior Work", "weight": 1.0} -->

For example, Setting 𝑇 ({ 𝑥𝑛 } 𝐵 𝑛 = 1 ) = mean ({ 𝑥𝑛 } 𝐵 𝑛 = 1 ) 2 +( std ({ 𝑥𝑛 } 𝐵 𝑛 = 1 ) -1 ) 2 and using that 𝑇 with SIGReg in LeJEPA recovers the VICReg SSL method in the limit of large number of slices. In fact, SIGReg will enforce in expectation that E [ Z ] = 0 and Cov ( Z ) = I 𝑑, where I 𝑑 denotes the 𝑑 × 𝑑 identity matrix-derivations provided in Section B.14. And since our invariance term is simply the ℓ 2 distance between the views' embeddings, LeJEPA recovers VICReg for this degenerate statistical test. Based on thm. 3, we however strongly advocate against such a setting as it would lead to shortcut solutions-a phenomenon already observed in VICReg.

<!-- chunk {"id": "body-0064", "role": "body", "section": "LeJEPA: Empirical Validation", "weight": 1.0} -->

We now use the LeJEPA implementation described in Section 5.1 to demonstrate its effectiveness through comprehensive experiments. We show that LeJEPA: (i) trains reliably across diverse architectures and datasets (Section 6.1), (ii) provides an informative training loss for model selection (Section 6.2), (iii) outperforms frontier vision models on small-scale in-domain pretraining (Section 6.3), (iv) scales successfully to nearly 1 billion parameters on ImageNet-1k (Section 6.4), and (v) learns rich semantic segmentation features without explicit supervision.

<!-- chunk {"id": "body-0065", "role": "body", "section": "LeJEPA's Stability Across Hyper-Parameters and Architectures", "weight": 1.0} -->

WenowdemonstrateLeJEPA'sstability across hyperparameters, architectures, and experimental setups. Additional cross-domain stability results are presented in Section 6.3.

<!-- chunk {"id": "body-0066", "role": "body", "section": "LeJEPA's Stability Across Hyper-Parameters and Architectures", "weight": 1.0} -->

Stability across Epps-Pulley hyperparameters. Wenext examine hyperparameters specific to LeJEPA: the number of slices |/u1D49C| in SIGReg, the integration domain for the Epps-Pulley test (Epps-Pulley), and the number of quadrature points for numerical integration. Table 1a shows ablations on ImageNet-1K with ViT-Large/14. Both the integration domain and number of quadrature points have negligible impact on performance. This is expected: since the characteristic function is accurate at zero, the Stability across standard hyperparameters. We begin by evaluating LeJEPA on ImageNet-100 and ImageNet1K. On ImageNet-100, we train a ResNet-50 and vary the number of views and the loss weighting 𝜆 (Figure 8). Performance remains stable across both dimensions, leading us to recommend 𝜆 = 0. 05 as a robust default. On ImageNet-1K, we train a ViT-Large/14 and explore batch size, as well as the number of global (𝑉 g) and local (𝑉 l) views (Table 1b).

<!-- chunk {"id": "body-0067", "role": "body", "section": "LeJEPA's Stability Across Hyper-Parameters and Architectures", "weight": 1.0} -->

We find that the configuration commonly used in prior work (𝑉 g = 2, 𝑉 l = 8) transfers well to LeJEPA. Notably, LeJEPA achieves competitive performance with batch sizes as small as 128 on ImageNet-1K (Table 1c), suggesting reduced memory requirements compared to existing methods. We thus recommend to use 𝜆 = 0. 05, 𝑉 g = 2, 𝑉 l = 8, and batch size ≥ 128 as starting points.

<!-- chunk {"id": "body-0068", "role": "body", "section": "LeJEPA's Stability Across Hyper-Parameters and Architectures", "weight": 1.0} -->

Table 1. ViT/Large-14, on inet1k pretraining for 100 epochs and evaluated with frozen backbone linear probing (top1 accuracy, %). LeJEPA's performance is stable across all its hyperparameters and while some may slightly improve performance, e.g., the number of slices | A | and the projector sizes, none of the choices lead to a catastrophic collapse.

<!-- chunk {"id": "body-0069", "role": "body", "section": "(a) (Epps-Pulley) parameters", "weight": 1.0} -->

| integration | num_slices | config/bstat_n_points | config/bstat_n_points | config/bstat_n_points |

<!-- chunk {"id": "body-0070", "role": "body", "section": "(b) Number of local/global views", "weight": 1.0} -->

| # global_views (𝑉 g) # views (𝑉 = 𝑉 g + 𝑉 l) | 1 | 2 | 4 | | (c) Mini-batch size | (c) Mini-batch size | (c) Mini-batch size | (c) Mini-batch size | (c) Mini-batch size |

<!-- chunk {"id": "body-0071", "role": "body", "section": "(e) Register tokens", "weight": 1.0} -->

| reg_tokens num_slices | 0 | 1 | 2 | 4 | 8 | moments of the distribution are well-characterized even with a modest integration range. The number of slices |/u1D49C| has a modest effect-while more slices slightly improve performance, even 512 slices yield competitive results. We thus recommend to use 17 integration points, an integration domain of, and 1024 slices as starting points.

<!-- chunk {"id": "body-0072", "role": "body", "section": "(e) Register tokens", "weight": 1.0} -->

- LeJEPA pretrained, frozen backbone, linear eval 50 architectures ( <20 M params.)

<!-- chunk {"id": "body-0073", "role": "body", "section": "(e) Register tokens", "weight": 1.0} -->

Stability across architectures. A key advantage of LeJEPA over recent methods (e.g., IJEPA, DINOv2) is its architecture-agnostic design. While most modern selfsupervised methods are tailored to Vision Transformers, LeJEPA works across diverse architecture families without modification. To validate this claim, we pretrain approximately 50 architectures from 8 different families on ImageNet-10, selecting all models in the timm library with fewer than 20M parameters. All models are able to learn high-quality representations reaching between 91.5% to 95% top 1 accuracy with frozen backbone linear probing. It seems that models performing well in supervised learning setups are also the ones to favor for LeJEPA, such as resnets and ViTs. We thus recommend to use standard architectures such as ResNets and ViTs over specialized models like EfficientNet as stating point.

<!-- chunk {"id": "body-0074", "role": "body", "section": "(e) Register tokens", "weight": 1.0} -->

Weight Averaging [Izmailov et al., 2019]-it is not necessary to prevent collapse. In our setup, we apply SWA on the encoder producing 𝜇 in Equation. Second, recent work demonstrated that register tokens are needed to prevent training instabilities in vision models [Oquab et al., 2023, Siméoni et al., 2025, Darcet et al., 2023]. We show in Table 1 that such instabilities likely stem from poorly conditioned training objectives. In contrast, LeJEPA does not require register tokens and achieves stable performance with or without them. We thus recommend training without a predictor or register tokens, and optionally applying SWA with ViTs for a possible performance gain.

<!-- chunk {"id": "body-0075", "role": "body", "section": "Experiment Details 1", "weight": 1.0} -->

We strive for simplicity and thus adopt a unified pretraining pipeline. The following parameters apply to all experiments and figures unless stated otherwise in the corresponding caption and come from Section 6.1:

<!-- chunk {"id": "body-0076", "role": "body", "section": "Experiment Details 1", "weight": 1.0} -->

- All backbones are from timm and all optimizers/schedulers are from PyTorch without modifications - LeJEPA's implementation is given in algorithm 2 with hyperparameter 𝜆 - We employ eight views (𝑉 = 8) containing two global views (𝑉 g = 2) with resolution 224x224 and 96x96 for the local views - AdamW optimizer with lr ∈ { 5 𝑒 -3, 5 𝑒 -4 } and wd ∈ { 1 𝑒 -1, 1 𝑒 -2, 1 𝑒 -5 } -no scheduler on weight-decay, standard linear warm-up cosine-annealing for lr

<!-- chunk {"id": "body-0077", "role": "body", "section": "LeJEPA's Training Loss is Informative of Downstream Performance", "weight": 1.0} -->

Amajor challenge in SSL pretraining is the lack of reliable signals conveying the quality of the learned representation. As a result, it is common to monitor a supervised Removalofpopularheuristics. In addition to providing reliable performance across models and datasets, LeJEPA's provable construction enables us to remove many heuristics traditionally used to prevent collapse. First, prior work has shown both empirically and theoretically that predictors in image JEPA (without asymmetric information) and teacher-student architectures serve primarily to prevent collapse [Grill et al., 2020, Jing et al., 2021, Tian et al., 2021, Caron et al., 2021, Chen et al., 2021]. Removing these components produces collapsed encoders, i.e., with performances at chance-level.

<!-- chunk {"id": "body-0078", "role": "body", "section": "LeJEPA's Training Loss is Informative of Downstream Performance", "weight": 1.0} -->

Thanks to LeJEPA's SIGReg loss, we can remove both the predictor and teacher-student architecture without suffering from collapse, as shown in Table 4. While a teacher-student configuration does provide a small performance boost for ViT models-consistent with observations in supervised learning via Stochastic downstream task performance, sometimes supplemented with unsupervised embedding statistics [Agrawal et al., 2022, Garrido et al., 2023, Thilak et al., 2023]. This process is highly limiting since it requires labeled data that is costly and overly specialized. This is further exacerbated in the latest JEPA models where training losses exhibit low correlation with downstream performance-and may not even decrease monotonically during training.

<!-- chunk {"id": "body-0079", "role": "body", "section": "LeJEPA's Training Loss is Informative of Downstream Performance", "weight": 1.0} -->

In contrast, we find that LeJEPA's training loss behaves much more favorably-providing us with a meaningful signal on model quality. First, we provide in Figure 10, the 2D plane spanned by the SIGReg and prediction losses where a clear trend with downstream task accuracy can be observed. More strikingly, the combined training loss (LeJEPA) with mixing coefficient 𝜆 exhibits very high Spearman correlation [Spearman, 1961], denoted as 𝜌 𝑠, of about 85% with downstream accuracy-which is considered a strong signal. This strong relationship holds across datasets and architectures. As a result, a lower LeJEPA training loss reliably indicates a better downstream performance.

<!-- chunk {"id": "body-0080", "role": "body", "section": "LeJEPA's Training Loss is Informative of Downstream Performance", "weight": 1.0} -->

We can further improve this correlation through a simple scaling law based upon the trade-off weighting hyperparameter 𝜆 By setting 𝛼 ≈ 0. 4, LeJEPA's training loss is able to achieve nearly 99% correlation with downstream performance across multiple datasets and models. We depict the changes in 𝐶 (𝛼) as a function of 𝛼 on multiple datasets and models in Figure 11, as well as the training LeJEPA loss against downstream performance in Figure 19. The strong alignment between LeJEPA's training loss and model quality enables label-free SSL model selection and cross-validation.

<!-- chunk {"id": "body-0081", "role": "body", "section": "In-Domain LeJEPA Outperforms Frontier Model Transfer Learning", "weight": 1.0} -->

Akey promise of self-supervised learning is to learn universal representations that generalize across tasks and domains. However, current frontier foundation models (e.g., DINOv2/v3, IJEPA) are pretrained on natural images forcing practitioners in specialized domains to collect large amount of labels for supervised finetuning. In fact, most frontier models can not be trained directly on those domains as the number of samples may be small and searching again for the hyper-parameters would be cum- bersome yet necessary [Assran et al., 2022].

<!-- chunk {"id": "body-0082", "role": "body", "section": "In-Domain LeJEPA Outperforms Frontier Model Transfer Learning", "weight": 1.0} -->

Table 2. Few-shot classification accuracy (percentages) on 8 datasets spanning textures, objects, and fine-grained categories. Our LeJEPA achieves superior performance on fine-grained tasks (DTD, flowers102, food101) while requiring only 100 pretraining epochs compared to I-JEPA's 300 epochs-a 3× reduction in training time and computational resources without sacrificing downstream task performance. This efficiency gain is particularly valuable for practical applications where training budget is limited. Bold indicates best performance within the IN-1K comparison group, all numbers are percentages.

<!-- chunk {"id": "body-0083", "role": "body", "section": "In-Domain LeJEPA Outperforms Frontier Model Transfer Learning", "weight": 1.0} -->

| | | | | | Dataset | Dataset | Dataset | Dataset | Dataset | Dataset | Dataset | Dataset | Dataset | Figure 13. Emergent Object Segmentation via Last Layer Thresholding. LeJEPA naturally learns to segment and track salient objects (shown in attention maps on the right of each video) without explicit supervision. The results display impressive visual quality and strong temporal consistency across video frames (videos provided on our project page). This emergent capability demonstrates the rich semantic representations learned through our self-supervised approach.

<!-- chunk {"id": "body-0084", "role": "body", "section": "In-Domain LeJEPA Outperforms Frontier Model Transfer Learning", "weight": 1.0} -->

TodemonstrateLeJEPA'sversatility andability to resolve that current pain-point, we propose to pretrain directly on a new domain without any change in the loss or the pretraining pipeline. We select the dataset, a galaxy morphology classification task that differs significantly from natural images in both visual structure and statistical properties [Balestriero et al., 2025]. The dataset contains 11,000 training samples across 10 galaxy types. For LeJEPA, we use the default hyper-parameters and pretrain for 400 epochs a variety of backbones. We compare against the latest DINOv2, DINOv3 and IJEPA. We report in Figure 12 the top1 accuracy for linear probing both with frozen backbone and full-finetuning. We observe that in-domain pretraining with LeJEPA substantially outperforms state-of-the-art frontier models (DINOv2, DINOv3) on both linear probing and full finetuning. Additional datasets and backbones are provided in Table 5 depicting LeJEPA's ability to train in-domain, even with a dataset with 1000 samples (flowers102).

<!-- chunk {"id": "body-0085", "role": "body", "section": "In-Domain LeJEPA Outperforms Frontier Model Transfer Learning", "weight": 1.0} -->

Coupling this result with the stability of LeJEPA across architectures and hyper-parameters should offer a promising alternatives in domains not yet accounted for by the latest frontier models.

<!-- chunk {"id": "body-0086", "role": "body", "section": "LeJEPA Scales Across Data and Models", "weight": 1.0} -->

We now propose to apply LeJEPA over a larger pretraining dataset, i.e., Imagenet-1k, and over larger backbones such as ViT/Large (0.3B), ConvNextV2-Huge (0.6B). For those two models, we reach an online linear probe accuracy on inet1k of 77.1% and 78.5% respectively. Beyond in-distribution performances, we also explore transfer learning. For those experiments, our baselines are IJEPA with a ViT-Huge (0.6B) which is the closest to our setup, and we also include a recent improved version of IJEPA including additional stochastic prediction tasks [Bar et al., 2023] that is coined IJEPA + STOP. For LeJEPA, we employ the same recipe as described in Section 6.1 and report transfer learning performances with frozen backbone in Table 2. We observe that we consistently outperform IJEPA while employed a smaller model and shorted training schedule. Beyond top1 accuracy, we also echo our findings from Section 6.2 about LeJEPA's training loss quality.

<!-- chunk {"id": "body-0087", "role": "body", "section": "LeJEPA Scales Across Data and Models", "weight": 1.0} -->

In our setup, we observe a very stable and smooth training curve indicating a stable optimization landscape removing the need for careful hyperparameter selection (recall thm. 4). Weprovide an example on a ViT-gigantic (1.8B parameters) in Figure 1.

<!-- chunk {"id": "body-0088", "role": "body", "section": "Emergent Semantic Structure in LeJEPA Representations", "weight": 1.0} -->

A hallmark of successful self-supervised learning is the emergence of semantically meaningful attention patterns without explicit supervision [Caron et al., 2021]. To assess whether LeJEPA learns such structure, we visualize the attention maps of the learned representations. Following DINO [Caron et al., 2021], we apply PCA to the embeddings and visualize the first principal components, which reveal clear correspondence to object boundaries and salient regions (Figure 14). Furthermore, we explore whether these attention patterns can enable unsupervised video segmentation-a challenging task requiring temporal consistency and object understanding. By thresholding the self-attention maps of the [CLS] token, we obtain binary masks that track objects across frames without any segmentation labels during training. As shown in Figure 13, LeJEPA's attention naturally segments foreground objects from background with remarkable temporal coherence, suggesting that the learned representations capture both spatial semantics and temporal structure. This emergent capability demonstrates that LeJEPA's stabilityfocused objective does not sacrifice the semantic richness of learned features.

<!-- chunk {"id": "body-0089", "role": "body", "section": "Conclusion", "weight": 1.5} -->

We have established a principled theoretical framework for JEPA-based self-supervised learning that fundamentally resolves its core pathologies. Our contributions span theory and practice: we proved that isotropic Gaussian embeddings uniquely minimize worst-case downstream risk, introduced SIGReg as a tractable and provably correct method to enforce this distribution, and demonstrated that this approach eliminates representational collapse by design-and not through ad-hoc combinations of teacherstudent networks, stop-gradients, or asymmetric architectures.

<!-- chunk {"id": "body-0090", "role": "body", "section": "Conclusion", "weight": 1.5} -->

We validate LeJEPA across domains and over 60 architectures including gigantic versions with 1.8B parameters. In spite of its simplicify, LeJEPA matches state-of-the-art performance while requiring fewer than 50 lines of core implementation. Critically, our approach provides what SSL has long needed: a mathematically rigorous foundation that directly informs practical algorithm design.
