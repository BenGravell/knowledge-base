<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

LeJEPA: Provable and Scalable Self-Supervised Learning without the Heuristics

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Learning manipulable representations of the world and its dynamics is central to AI. Joint-Embedding Predictive Architectures (JEPAs) offer a promising blueprint, but lack of practical guidance and theory has led to ad-hoc R&D. We present a comprehensive theory of JEPAs and instantiate it in {\bf LeJEPA}, a lean, scalable, and theoretically grounded training objective. First, we identify the isotropic Gaussian as the optimal distribution that JEPAs' embeddings should follow to minimize downstream prediction risk. Second, we introduce a novel objective - {\bf Sketched Isotropic Gaussian Regularization} (SIGReg) - to constrain embeddings to reach that ideal distribution.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Combining the JEPA predictive loss with SIGReg yields LeJEPA with numerous theoretical and practical benefits: (i) single trade-off hyperparameter, (ii) linear time and memory complexity, (iii) stability across hyper-parameters, architectures (ResNets, ViTs, ConvNets) and domains, (iv) heuristics-free, e.g., no stop-gradient, no teacher-student, no hyper-parameter schedulers, and (v) distributed training-friendly implementation requiring only approx50 lines of code. Our empirical validation covers 10+ datasets, 60+ architectures, all with varying scales and domains. As an example, using imagenet-1k for pretraining and linear evaluation with frozen backbone, LeJEPA reaches 79\% with a ViT-H/14. We hope that the simplicity and theory-friendly ecosystem offered by LeJEPA will reestablish self-supervised pre-training as a core pillar of AI research.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

Learning manipulable representations of the world and its dynamics is a long‑standing question in AI, with roots dating back centuries ago (von1867handbuch; tolman1948cognitive; gregory1980perceptions; sutton1991dyna; friston2010free). Across domains, e.g., image recognition, robotics, physics, space exploration, the unifying question is how to learn an organized and actionable high‑dimensional embedding space from observations? Using Deep Networks--parameterized nonlinear operators $f_{\mathbf{θ}}$--to map observations to embeddings is a standard first piece of that puzzle (lecun2015deep; goodfellow2016deep). The second, less standardized, piece of that puzzle is how to train $f_{\mathbf{θ}}$.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

Joint-Embedding Predictive Architectures (JEPAs) suggest training $f_{\mathbf{θ}}$ by maximizing predictive agreement between the embeddings of semantically related views (bromley1993signature; lecun2022path; balestriero2023cookbook). Views can come in two forms: transformations or corruptions. They can involve masking, cropping, blurring, temporal or spatial translations, geometric or photometric transformations, viewpoint changes, views from different sensor modalities, etc. The supervised forms involve human-produced components such as image-caption pairs, text-code pairs, etc (tian2020makes). In any case, views are expected to share some degree of semantic relationship to allow the prediction task to align $f_{\mathbf{θ}}$'s embeddings towards the underlying knowledge present in the data.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

Alas, JEPA's prediction task admits failure modes, such as representation collapse, where $f_{\mathbf{θ}}$ maps all inputs to nearly identical embeddings (complete collapse) or to a low-dimensional subspace (dimensional collapse) (jing2021understanding)(jing2021understanding; cosentino2022toward; balestriero2022contrastive). To mitigate such shortcut solutions, state‑of‑the‑art recipes rely on heuristics--stop‑gradient (chen2020simple), asymmetric view generation (wang2022importance), teacher--student networks with carefully tuned EMA schedules (caron2021emerging; tian2021understanding), explicit normalization and whitening layers (ermolov2021whitening; chen2021empirical)--and a delicate balance of hyperparameters.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

As a result, today's JEPA training is brittle and most research has shifted toward scaling data (vo2024automatic), models (fan2025scaling) and even post-training rodas2025diet while leaving the theoretical foundations of JEPAs largely unexplored.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Introduction", "weight": 1.5} -->

Our study proposes to break that cycle by questioning some of the fundamental design principles underpinning JEPAs. That introspection will start by asking what are the necessary conditions that JEPAs should abide by? Those minimal conditions will then act as axioms for us to design a novel and lean JEPA. We identify two axioms: (i) solving the prediction task while (ii) enforcing an isotropic Gaussian distribution of the embeddings (Section˜3). While (i) follows standard practice (balestriero2022contrastive), we introduce in Section˜4 a novel distribution matching objective--Sketched Isotropic Gaussian Regularization (SIGReg)--to enforce (ii). The use of SIGReg not only removes the need for the numerous heuristics previously employed to prevent representation collapse, but SIGReg also exhibits favorable scaling properties as its memory and computational complexity is linear in dimension and sample size. Crucially, SIGReg's isotropic Gaussian enforcement solves the collapsed shortcut solution and provably minimizes the model's expected risk over the space of downstream tasks to be encountered post-training.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Introduction", "weight": 1.5} -->

The resulting JEPA solution--coined Latent-Euclidean JEPA (LeJEPA)--is introduced in Section˜5. Beyond theoretical optimality, LeJEPA offers numerous benefits such as (i) provable statistical guarantees, (ii) removal of heuristics such as teacher-student networks, (iii) linear memory and computational complexity, and most importantly (iv) a unified design with a single trade-off parameter that works out of the box across datasets, architectures and scales (see Section˜6). We summarize our contributions below.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Introduction", "weight": 1.5} -->

Contribution 1: We prove the optimal embedding distribution for foundation models. We establish that the isotropic Gaussian uniquely minimizes downstream prediction risk across broad task families. In Section˜3, we derive this result rigorously for both linear (Section˜3.1) and nonlinear probes (Section˜3.2), providing the first principled answer to what distribution $f_{\mathbf{θ}}$'s embeddings should follow. This theoretical result transforms JEPA design from heuristic exploration to targeted optimization. Contribution 2: We introduce SIGReg, a distribution matching objective that uniquely combines provable correctness with computational efficiency at scale. We present Sketched Isotropic Gaussian Regularization (SIGReg), a novel objective that enforces distributional alignment via random projections and characteristic-function matching (Sections˜4 and 2). SIGReg provides statistical guarantees (Sections˜4.1 and 4.2) while achieving linear complexity and bounded gradients---a combination that existing distribution matching methods do not offer. Critically, its projection-based construction defeats the curse of dimensionality (Section˜4.3), making it both theoretically sound and practically efficient for high-dimensional embeddings.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Introduction", "weight": 1.5} -->

Contribution 3: We design LeJEPA, a statistically optimal JEPA that eliminates collapse by construction. By combining JEPA's predictive objective with SIGReg targeting the isotropic Gaussian, we introduce LeJEPA---Latent-Euclidean JEPA (Section˜5). LeJEPA requires only a single hyperparameter, eliminates representational collapse without stop-gradients or teacher-student architectures, and transfers across architectures and datasets without hyperparameter tuning. This demonstrates that principled theory directly yields practical simplicity.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Introduction", "weight": 1.5} -->

Contribution 4: We validate LeJEPA at scale across diverse architectures and establish in-domain pretraining as viable. Our experiments (Section˜6) span ViTs, ConvNeXts, ResNets, MaxViTs, and Swin Transformers at scales approaching 1 billion parameters, where LeJEPA matches or exceeds state-of-the-art methods while maintaining training simplicity and robustness. Critically, on domain-specific datasets (, Food101), LeJEPA outperforms DINOv2-based transfer learning when pretrained directly on target data. This challenges the transfer learning paradigm and demonstrates that principled SSL can unlock effective in-domain pretraining---previously considered impractical for small datasets.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Notations and Definitions", "weight": 1.0} -->

Data. We are in possession of a dataset of shape ${(N,V,D)} \in {}_{}^{}$ where $N$ is the number of samples, $V$ is the number of views, and $D$ is the dimension. One entry of this dataset is accessed via ${\mathbf{x}}_{n,v,d}$. Those dimensions are often interpreted as follows: (N) is the number of independent samples, e.g., different images or different videos, (V) is the number of views, e.g., data-augmentations for images, frames for videos, and (D) is the dimension of each ${\mathbf{x}}_{n,v}$, e.g., number of RGB pixels for images. In many cases the ordering over $V$ is given by time--but in some cases, e.g., data-augmentation of an image, ordering becomes irrelevant.

<!-- chunk {"id": "body-0014", "role": "body", "section": "Notations and Definitions", "weight": 1.0} -->

Our study does not require any particular choice to organize one's dataset into a $(N,V,D)$ tensor--and none of our theory and implementation assumes a particular design decision for that tensor. However, we will rely on the following two properties, (independence) the samples ${\mathbf{x}}_{n},{\mathbf{x}}_{n^{\prime}}$ have been obtained independently from each other $nn^{\prime}$, and (identically distributed) the sampling process was identical among ${\mathbf{x}}_{n},n$.

<!-- chunk {"id": "body-0015", "role": "body", "section": "Notations and Definitions", "weight": 1.0} -->

Deep Networks. Today's AI solutions rely on Deep (Neural) Networks (DNs), which are compositions of a large number of parameterized linear and nonlinear operators. We denote the DN's mapping as $f_{\mathbf{θ}}:{R^{D}\rightarrow R^{K}}$ with $K$ the dimension of the embedding space. The internals of $f_{\mathbf{θ}}$ are designed by the researcher to incorporate as much prior knowledge about the data as possible. The details of $f_{\mathbf{θ}}$ are irrelevant to our study--as we will see the proposed LeJEPA works out-of-the-box on any $f_{\mathbf{θ}}$. In any case, all the learnable parameters are gathered in the vector ${\mathbf{θ}} \in R^{P}$, with $P$ counting the total number of parameters.

<!-- chunk {"id": "body-0016", "role": "body", "section": "Notations and Definitions", "weight": 1.0} -->

A central challenge in AI research is to design the right architecture and training objective so that $\mathbf{θ}$ can be learned from gradient descent to ultimately produce a useful system, or foundation model, $f_{\mathbf{θ}}$.

<!-- chunk {"id": "body-0017", "role": "body", "section": "Notations and Definitions", "weight": 1.0} -->

JEPAs. A foundation model is any system, e.g., a DN, able to solve numerous downstream tasks without requiring any change in its internal parameters $\mathbf{θ}$. This is in sharp contrast with a supervised model that only considers its training task. JEPAs have formally been introduced by lecun2022path as a vehicle to produce foundation models. The core building blocks of JEPAs rely on numerous well-established techniques such as siamese networks (bromley1993signature) and predictive coding (helmholtz1867handbook; bruner1949perception). While the exact blueprint of JEPAs varies greatly between use-cases, they all rely on two core principles: (i) being able to predict the embedding of a view ${\mathbf{x}}_{n,v}$ from the embedding of another view ${\mathbf{x}}_{n,v^{\prime}},{v^{\prime}v}$, all while (ii) ensuring that the embeddings do not become degenerate.

<!-- chunk {"id": "body-0018", "role": "body", "section": "Notations and Definitions", "weight": 1.0} -->

Concretely, once a JEPA is designed and trained, it should be able to solve numerous downstream tasks in zero or few shots. The JEPA objective function, along with some examples for $\mathbf{x}$, is provided in Equation˜1. The predictability criterion can be done by directly comparing the embeddings of the partial views $Enc{({\mathbf{x}}_{n,v,.})}$ and $Enc{({\mathbf{x}}_{n,v^{\prime},.})}$ with a metric, e.g., $\ell_{p}$.

<!-- chunk {"id": "body-0019", "role": "body", "section": "Notations and Definitions", "weight": 1.0} -->

In some cases, an additional DN coined Pred, is employed to compare $Pred{({Enc{({\mathbf{x}}_{n,v,.})}})}$ against $Enc{({\mathbf{x}}_{n,v^{\prime},.})}$--which is only justified when there exists an asymmetry between the information content of the different views, e.g., by conditioning the predictions on observed actions from robotics data (khazatsky2024droid).

<!-- chunk {"id": "body-0020", "role": "body", "section": "The Need for Reliable Pretraining", "weight": 1.0} -->

The JEPA's prediction task is designed based on a priori knowledge of the data. Its design is often quite natural since it is relatively intuitive to form $\mathbf{x}$ so that its views share the relevant information content one hope to capture. On the other hand, the design of the "anti-collapse" criterion is much closer to a game of Whac-A-Mole. Today's designs rely on many different under-specified safeguards which are carefully combined in the hope that degenerate shortcut solutions are avoided during training. Such mechanisms include (i) feature whitening (ermolov2021whitening; bardes2021vicreg), (ii) negative samples (chen2020simple; he2020momentum), and (iii) asymmetric views and teacher-student networks with stop-gradient (caron2021emerging; assran2023self).

<!-- chunk {"id": "body-0021", "role": "body", "section": "The Need for Reliable Pretraining", "weight": 1.0} -->

Those mechanisms all suffer from at least two of the following limitations: (i) under-specification, i.e., the criteria can be minimized while embeddings are in a degenerate configuration, (ii) quadratic time and memory complexity with mini-batch size and/or embedding dimension, (iii) sensitivity to data distribution, hyperparameters, architecture, and (iv) lack of theoretical understanding and guarantees.

<!-- chunk {"id": "body-0022", "role": "body", "section": "The Need for Actionable Theory", "weight": 1.0} -->

For decades, the two major solutions for AI were supervised learning (lecun2015deep) and learning by reconstruction (rumelhart1986learning)--sometimes combined together, e.g., for semi-supervised learning (kingma2014semi). In supervised learning, the labels both ensure that semantically similar samples are close to each other in embedding space while preventing complete representation collapse. In particular, it is possible to measure the amount of collapse in supervised learning as a function of the number of classes (papyan2020prevalence). The reconstruction objective is similarly well suited to prevent representation collapse as the original input must be recovered from the embeddings, i.e., the embeddings must be as informative about the input as possible--up to some optional denoising tasks that users can setup as part of the training (vincent2010stacked).

<!-- chunk {"id": "body-0023", "role": "body", "section": "The Need for Actionable Theory", "weight": 1.0} -->

Because supervised and reconstruction-based learning have been widely studied for decades, there exists a large body of work to explain and inform practical designs--as well as studying their limitations in producing foundation models (balestriero2024learning; van2025joint). This is not the case for the more recent JEPAs where empirical advances quickly outpace anyone hoping to delve into their inner workings. This dynamic led the community to focus on post-hoc theoretical justification of already found solutions (liu2021self; shwartz2024compress; shwartz2022we; zhang2023matrix). In most cases, those studies involve the Mutual Information (MI) (shannon1948mathematical; cover1999elements) whose different bounds recover established methods (gutmann2010noise; ma2018noise; oord2018representation; poole2019variational; hjelm2018learning; mcallester2020formal). Because existing studies focus on explaining and interpreting already developed JEPAs, too little principled guidance and innovation has been brought forward.

<!-- chunk {"id": "body-0024", "role": "body", "section": "The Need for Actionable Theory", "weight": 1.0} -->

Instead, most of the recent empirical advances take the form of collecting larger dataset, scaling up pre-existing training recipes (goyal2019scaling; chen2020big; oquab2023dinov2; fan2025scaling), and deriving novel data curation processes (vo2024automatic; kerdreux2025efficient).

<!-- chunk {"id": "body-0025", "role": "body", "section": "The Need for Actionable Theory", "weight": 1.0} -->

In contrast, our goal in the following Sections˜3, 4 and 5 will be to derive a novel JEPA solution from first principles, i.e., whose design relies on proved necessary conditions for optimality, and with a pretraining recipe that can finally reconcile exploratory research, scalability, and state-of-the-art performances.

<!-- chunk {"id": "body-0026", "role": "body", "section": "Latent Euclidean: Embeddings Should be Isotropic Gaussian", "weight": 1.0} -->

We address a fundamental question: which distribution should ${Enc}{(\mathbf{x})}$ follow to minimize empirical risk on any downstream task? We prove that the isotropic Gaussian is the unique optimal distribution for both linear (Section˜3.1) and nonlinear probing (Section˜3.2), with geometric intuition provided in Section˜3.3. This theoretical result establishes the necessary design principle for our JEPA; Section˜4 then provides the practical implementation to achieve it.

<!-- chunk {"id": "body-0027", "role": "body", "section": "Linear Probing", "weight": 1.0} -->

We begin by identifying the optimal distribution for $f_{\mathbf{θ}}$'s embeddings by analyzing linear probes--one of the most popular methods for frozen encoder evaluation. Specifically, we ask: *which distribution for $f_{\mathbf{θ}}{(\mathbf{x})}$ would be most favorable for solving arbitrary downstream tasks, i.e., for any realization of targets $\mathbf{y}$?*

<!-- chunk {"id": "body-0028", "role": "body", "section": "Linear Probing", "weight": 1.0} -->

Denote as ${\mathbf{Z}} \in R^{N \times K}$ the matrix of $N$ embeddings, each $K$-dimensional, from $f_{\mathbf{θ}}{({\mathbf{x}}_{n})}$. The unknown corresponding labels are denoted as ${\mathbf{y}} \in R^{N}$. Without loss of generality, we consider univariate targets; the following analysis extends to multivariate targets. The linear probe minimizes the following least square problem (bishop2006pattern)

<!-- chunk {"id": "body-0029", "role": "body", "section": "Linear Probing", "weight": 1.0} -->

where $\overset{hat}{\beta}$ is the optimal probe parameters, and $\lambda \geq 0$ is an hyperparameter controlling the Tikhonov regularizer strength (bishop1995training; golub1999tikhonov). Despite not knowing $\mathbf{y}$, it is possible to describe the bias and variance of the estimator $\overset{hat}{\beta}$ as a function of the distribution of $\mathbf{Z}$. Consider two embeddings with identical column spans ${\mathbf{Z}}_{aniso},{\mathbf{Z}}_{iso}$.

<!-- chunk {"id": "body-0030", "role": "body", "section": "Linear Probing", "weight": 1.0} -->

${\mathbf{Z}}_{aniso}$'s covariance matrix eigenvalues are given by ${\{\lambda_{k}\}}_{k = 1}^{K}$ with at least two distinct values, while ${\mathbf{Z}}_{iso}$'s covariance matrix eigenvalues are all equal to $\frac{1}{K}{}_{k = 1}^{K}\lambda_{k}$. Hence, the two candidate embeddings ${\mathbf{Z}}_{aniso},{\mathbf{Z}}_{iso}$ capture the same intrinsic features and have same energy, but different geometries.

<!-- chunk {"id": "body-0031", "role": "body", "section": "Linear Probing", "weight": 1.0} -->

From the above Sections˜3.1 and 3.1 we obtain that the distribution of features must be isotropic. We now move to nonlinear probing where the standard Gaussian will emerge as the unique optimum.

<!-- chunk {"id": "body-0032", "role": "body", "section": "Nonlinear Probing", "weight": 1.0} -->

To allow for more flexible evaluation of the pretrained encoder $f_{\mathbf{θ}}$, it has become increasingly common to work with a nonlinear probe. We analyze two widely-used nonlinear methods: radius-based k-NN (taunk2019brief; sun2010adaptive; zhang2017efficient; abu2019effects) for its simplicity and kernel methods (nadaraya1964estimating; watson1964smooth) for their theoretical tractability.

<!-- chunk {"id": "body-0033", "role": "body", "section": "Nonlinear Probing", "weight": 1.0} -->

As in Section˜3.1, we ask ourselves which distribution of embeddings would be preferable for a foundation model. We first define our prediction function. The training data consists of the $N$ embeddings along with their training labels ${\{{({\mathbf{z}}_{n},{\mathbf{y}}_{n})}\}}_{n = 1}^{N}$. The prediction, using radius-based k-NN for a query vector $\mathbf{q}$ is formed as

<!-- chunk {"id": "body-0034", "role": "body", "section": "Nonlinear Probing", "weight": 1.0} -->

We search over all distributions of Z subject to a fixed total variance constraint, e.g., ${{Tr}{({{Cov}{({\mathbf{Z}})}})}} = \kappa_{1}$ or ${{Cov}{({\mathbf{Z}})}{}_{F}} = \kappa_{2}$. The specific value of $\kappa$ does not affect the optimal distribution shape. Following the same type of derivations as done in the linear regime--with the exception of some additional regularity conditions--we are able to precisely identify the isotropic Gaussian as the unique optimum to minimize bias as formalized below.

<!-- chunk {"id": "body-0035", "role": "body", "section": "Nonlinear Probing", "weight": 1.0} -->

Numerous additional details and discussions on the regularity assumptions we employed are provided in Appendix˜A. Together, these results establish the isotropic Gaussian distribution as the optimal design to minimize the worst-case risk of a foundation model across downstream tasks.

<!-- chunk {"id": "body-0036", "role": "body", "section": "Geometric and Practical Insights", "weight": 1.0} -->

We now empirically validate that the isotropic Gaussian is optimal when no information about downstream tasks is available. We focus on linear probing (Section˜3.1), where all considered distributions have the same total variance.

<!-- chunk {"id": "body-0037", "role": "body", "section": "Geometric and Practical Insights", "weight": 1.0} -->

When employing a linear probe, an anisotropic distribution increases both bias (with Tikhonov regularization) and variance. Examining bias first (Section˜3.1), we present in Figure˜18 visualizations for both continuous regression and discrete classification tasks. We observe that the cosine similarity between estimated and ground-truth parameters equals 1 only for isotropic distributions, degrading for anisotropic cases regardless of sample size or regularization strength. Regarding variance (Section˜3.1), we show in Figure˜3 that learned parameters vary significantly more across training sets when the covariance is anisotropic (right) compared to isotropic (left)---even when using logistic regression instead of OLS. Figure˜17 further illustrates this effect, showing the distribution of learned $\beta$ parameters across different training samples for both cases. The anisotropic distribution clearly produces higher-variance estimators.

<!-- chunk {"id": "body-0038", "role": "body", "section": "Geometric and Practical Insights", "weight": 1.0} -->

These theoretical and empirical results establish our design principle for LeJEPA: *embeddings $f_{\mathbf{θ}}{(\mathbf{x})}$ should follow an isotropic Gaussian distribution to minimize worst-case risk across downstream tasks encountered post-training*. Section˜4 introduces a novel regularizer to achieve this distribution.

<!-- chunk {"id": "body-0039", "role": "body", "section": "SIGReg: Reliable Isotropic Gaussian Regularization in High-Dimension", "weight": 1.0} -->

Having established the isotropic Gaussian as the optimal embedding distribution (Section˜3), we now introduce Sketched Isotropic Gaussian Regularization (SIGReg)--a distribution matching objective that is simultaneously (i) differentiable, (ii) scalable, (iii) provable, and (iv) interpretable. SIGReg builds on three key innovations. First, we formulate distribution matching as a statistical test under the null hypothesis $P_{\mathbf{θ}} = Q$ (Section˜4.1). Second, we identify a test that guarantees bounded gradients and curvature while maintaining linear complexity and efficient multi-GPU scaling (Section˜4.2). Third, SIGReg bypasses the curse of dimensionality, eliminating collapsed shortcut solutions entirely (Section˜4.3).

<!-- chunk {"id": "body-0040", "role": "body", "section": "Hypothesis Testing as a Judge", "weight": 1.0} -->

Asking for $f_{\mathbf{θ}}{({\mathbf{x}})}$'s distribution $P_{\mathbf{θ}}$ to match a target distribution $Q$ is typically done by creating various measures of distance or divergence, and estimating them in high-dimension. We propose a different starting point grounded in statistics. Consider the hypothesis testing framework (fisher1928statistical; neyman1933ix) given by

<!-- chunk {"id": "body-0041", "role": "body", "section": "Hypothesis Testing as a Judge", "weight": 1.0} -->

with $H_{0}$ being referred to as the null hypothesis. That is, we are asking in Equation˜2 if there is enough empirical evidence to reject the null. To answer that question, one (i) employs a test-statistic, i.e., a single scalar value summarizing the evidence from the empirical samples, (ii) determines a critical value $\tau_{\alpha}$ for the test-statistic based on the probability $\alpha$ of Type I error, i.e., of mistakenly rejecting a true null hypothesis, (iii) compares the test-statistic to the critical value $\tau_{\alpha}$; if the test-statistic exceeds $\tau_{\alpha}$, reject the null hypothesis. If the null is not rejected, we can only claim that there is not sufficient empirical evidence against $P_{\mathbf{θ}} = Q$.

<!-- chunk {"id": "body-0042", "role": "body", "section": "Hypothesis Testing as a Judge", "weight": 1.0} -->

As it stands, Equation˜2 remains impractical in large dimension as existing tests have at least quadratic complexity with the number of samples considered (more details in Appendix˜F). We thus propose to derive a sketching strategy by decomposing Equation˜2 into simpler univariate tests. Denoting the push-forward distributions $P_{\mathbf{θ}}^{({\mathbf{a}})}{({\mathbf{a}}^{\top})}_{\#}P_{\mathbf{θ}}$ and $Q^{({\mathbf{a}})}{({\mathbf{a}}^{\top})}_{\#}Q$, we can define the following directional univariate test

<!-- chunk {"id": "body-0043", "role": "body", "section": "Hypothesis Testing as a Judge", "weight": 1.0} -->

for a given directional unit-norm vector ${\mathbf{a}} \in \mathcal{S}^{K - 1}$. The corresponding *directional test-statistic* of Equation˜3 is computed as $T{({\{{{\mathbf{a}}^{\top}f_{\mathbf{θ}}{({\mathbf{x}}_{n})}}\}}_{n = 1}^{N})}$. Examples of tests $T$ will be provided in the later Section˜4.2. Repeating that process over a set of $M$ directions $A{\{{\mathbf{a}}_{1},\ldots,{\mathbf{a}}_{M}\}}$ and aggregating the individual values lead to the following *global test-statistic*

<!-- chunk {"id": "body-0044", "role": "body", "section": "Hypothesis Testing as a Judge", "weight": 1.0} -->

We now provide a formal statement asserting the consistency of Equation˜4 to test the original multivariate null hypothesis from Equation˜2. Our result leverages the well-known union-intersection principle (roy1953heuristic), and a slightly modified Cramér-Wold theorem. We denote by $\overset{d}{=}$ equality in distribution.

<!-- chunk {"id": "body-0045", "role": "body", "section": "Hypothesis Testing as a Judge", "weight": 1.0} -->

The assumptions required in the proof of Section˜4.1 hold for classical consistent univariate tests $T$ such as the ones presented in the following Section˜4.2.

<!-- chunk {"id": "body-0046", "role": "body", "section": "SIGReg: Sketching the Epps-Pulley Test is Stable and Scalable", "weight": 1.0} -->

Our proposed regularizer--coined Sketched Isotropic Gaussian Regularization (SIGReg)--follows directly from Section˜4.1 using any statistical test $T$ targeted towards the isotropic Gaussian, illustrated in Figures˜2 and 5, and formalized below.

<!-- chunk {"id": "body-0047", "role": "body", "section": "SIGReg: Sketching the Epps-Pulley Test is Stable and Scalable", "weight": 1.0} -->

We replace the maximum over ${\mathbf{a}} \in A$ in Section˜4.1 by an average in to avoid sparse gradient over the directions in $A$. We now delve on the choice of $T$ for which we compare well-known candidate tests in the field of statistics that are categorized into (i) moment based (Section˜4.2.1), (ii) CDF based (Section˜4.2.2), and (iii) CF based (Section˜4.2.3) statistics--ultimately justifying our choice of the Epps-Pulley statistic.

<!-- chunk {"id": "body-0048", "role": "body", "section": "Moments are Unstable and Insufficient", "weight": 1.0} -->

The first family of statistics we consider are moment-based. Taking the standard Gaussian as an instanciation for the moments, we can define the Jarque-Bera (jarque1980efficient) test that compares the third and fourth moments, i.e., skewness and kurtosis, as

<!-- chunk {"id": "body-0049", "role": "body", "section": "Moments are Unstable and Insufficient", "weight": 1.0} -->

where $\hat{skew}$ is the skewness computed from the data as $\frac{\frac{1}{n}{}_{i = 1}^{n}\left( {x_{i} - \overset{hat}{\mu}} \right)^{3}}{{\overset{hat}{\sigma}}^{3}}$ and $\hat{kurt}$ is the kurtosis $\frac{\frac{1}{n}{}_{i = 1}^{n}\left( {x_{i} - \overset{hat}{\mu}} \right)^{4}}{{\overset{hat}{\sigma}}^{4}}$. Typically, the (Jarque-Bera) test is used to see if a density follows a Gaussian distribution of any mean and variance--hence it only looks at moments 3 and 4. In our case we aim for a standard Gaussian test and thus add the usual statistics on the first two moments, leading to the extended test

<!-- chunk {"id": "body-0050", "role": "body", "section": "Moments are Unstable and Insufficient", "weight": 1.0} -->

The (Extended Jarque-Bera) acts as a moment matching problem over the first four moments. Such moment matching methods have proven powerful not only for statistical tests but also as mean to learn parametric and nonparametric models of data.

<!-- chunk {"id": "body-0051", "role": "body", "section": "Moments are Unstable and Insufficient", "weight": 1.0} -->

The Stability and Identifiability Conundrum. We now explain why moment-based tests--albeit powerful--will not be suited for LeJEPA. The $k^{th}$ of a distribution $P$ is denoted as $m_{k}{(P)}$. The first observation is that well-behaved distributions abiding the Carleman's condition ${{}_{k = 1}^{\infty}m_{2k}{(Q)}^{- {1/{({2k})}}}} = \infty$ (carleman1926fonctions), such as the Gaussian, or for distributions with finite interval (hausdorff1923momentprobleme) are uniquely determined by their moments. However, using a finite number of moments creates the following non-identifiability issue which well-known in statistics and often used as a motivation to use all moments (lehmann2005testing).

<!-- chunk {"id": "body-0052", "role": "body", "section": "Moments are Unstable and Insufficient", "weight": 1.0} -->

Hence Section˜4.2.1 prescribes us with the guideline to employ as large $K$ as possible to remove collapsed shortcut solution by making sure our distribution matching is accurate.

<!-- chunk {"id": "body-0053", "role": "body", "section": "Moments are Unstable and Insufficient", "weight": 1.0} -->

${J_{f_{\mathbf{θ}}}{({\mathbf{x}})}} \in R^{K \times P}$ the Jacobian matrix--hereby creating an impractical situation where training stability and identifiability can not be achieved simultaneously.

<!-- chunk {"id": "body-0054", "role": "body", "section": "Cumulative Density Functions are Impractical", "weight": 1.0} -->

The second family of tests acts upon the CDF. Because those tests require sorting, let's denote the $k^{th}$ order-statistics of $N$ samples by $x_{k:N}$. Two highly standard tests are quadratic Empirical Density Function statistics with different weighting known as Cramér-von Mises (cramer1928composition; von1981probability) and Anderson Darling (anderson1952asymptotic), and given by

<!-- chunk {"id": "body-0055", "role": "body", "section": "Cumulative Density Functions are Impractical", "weight": 1.0} -->

where $w{(x)}$ is a weighting function. Adding the $U^{2}$ statistics on top of Equation˜Cramér-von Mises recovers the Watson test (watson1961goodness)

<!-- chunk {"id": "body-0056", "role": "body", "section": "Cumulative Density Functions are Impractical", "weight": 1.0} -->

We do not consider the Kolmogorov-Smirnov test (kolmogorov1933) as it employs the $\ell_{\infty}$-norm instead of the $\ell_{2}$-norm hereby producing sparse gradients. Another common test is the Shapiro-Wilk test (shapiro1965analysis) which we found to be unstable in practice--details are provided in Appendix˜E.

<!-- chunk {"id": "body-0057", "role": "body", "section": "Cumulative Density Functions are Impractical", "weight": 1.0} -->

Lack of Scalability and Differentiability. CDF-based tests require sorting that have been highly optimized, e.g., with the $\mathcal{O}{({N{\log{(N)}}})}$ Quicksort algorithm (quicksort) but that nonetheless breaks the embarrassingly parallel nature of SGD--especially on multi-GPU (tanasic2013comparison; maltenberger2022evaluating) due to synchronization requirements. Moreover, these tests involve non-differentiable operations (sorting and order statistics), making them unsuitable for gradient-based optimization without relaxations (cuturi2019differentiable; grover2019stochastic; petersen2022monotonic). While there exists intricate sketching solutions (dunning2019computing; masson2019ddsketch; dunning2021t), each of those solutions introduce numerous additional hyper-parameters--going against our first motivation for LeJEPA.

<!-- chunk {"id": "body-0058", "role": "body", "section": "Characteristic Functions are Stable, Scalable and Identifiable", "weight": 1.0} -->

The third family of tests is concerned with Empirical Characteristic Functions (ECF) which are the Fourier transform of the density function. The Epps--Pulley test (epps1983test) is one of the most popular test and simply compares in weighted $\ell_{2}$-norm the ECF of the data against a target CF

<!-- chunk {"id": "body-0059", "role": "body", "section": "Characteristic Functions are Stable, Scalable and Identifiable", "weight": 1.0} -->

The first crucial observation is that the ECF being defined as ${{\overset{hat}{\phi}}_{X}{(t)}} = {\frac{1}{n}{}_{j = 1}^{n}e^{itX_{j}}}$ is naturally differentiable and easily computed in distributed settings via efficient all_reduce operations, as the ECF is a simple average of complex exponentials. The weight function is typically Gaussian, such as ${w{(t)}} = e^{- {t^{2}/\sigma^{2}}}$ with $\sigma$ commonly set to $1$.

<!-- chunk {"id": "body-0060", "role": "body", "section": "Characteristic Functions are Stable, Scalable and Identifiable", "weight": 1.0} -->

Other tests, e.g., based on the Entropy (szekely2005new) are not considered here as they require numerous additional design choices for the univariate Entropy estimation (silverman2018density; beirlant1997nonparametric), e.g., using kernels (joe1989estimation), or M-estimators (miller2003new).

<!-- chunk {"id": "body-0061", "role": "body", "section": "Characteristic Functions are Stable, Scalable and Identifiable", "weight": 1.0} -->

Epps-Pulley has bounded loss, gradient and curvature. We now consider the remaining two families of tests: moment-based and CF-based. First, recall that moments are polynomial in the data and with extreme growth rate for higher moment--assuming they even exist. Even for well-behaved distributions, raising values to a power of $k$ can quickly lead to exploding gradients. This comes in sharp contrast with the ECF which is always bounded and with bounded gradients for any input distribution for the projected samples $z_{i} = {{\mathbf{a}}^{\top}f_{\theta}{({\mathbf{x}}_{n})}}$, $n = {1,\ldots,N}$.

<!-- chunk {"id": "body-0062", "role": "body", "section": "Characteristic Functions are Stable, Scalable and Identifiable", "weight": 1.0} -->

def SIGReg(x, global_step, num_slices=256):
## slice sampling – synced across devices –
dev = dict(device=x.device)
g = torch.Generator(**dev)
g.manual_seed(global_step)
proj_shape = (x.size, num_slices)
A = torch.randn(proj_shape, generator=g, **dev)
## – Epps-Pulley stat. see Sec. 4.3 for alt. –
## integration points
t = torch.linspace(-5, 5, 17, **dev)
## theoretical CF for N and Gauss.

<!-- chunk {"id": "body-0063", "role": "body", "section": "Characteristic Functions are Stable, Scalable and Identifiable", "weight": 1.0} -->

window
exp_f = torch.exp(-0.5 * t**2)
## empirical CF – gathered across devices –
ecf = (1j * x_t).exp.mean
ecf = all_reduce(ecf, op="AVG")
## weighted L2 distance
err = (ecf - exp_f).abs.square.mul(exp_f)
N = x.size * world_size
T = torch.trapz(err, t, dim=1) * N
Algorithm 1: SIGReg with Epps-Pulley statistic with DDP support and 𝒪 (N) time and memory complexity. x is a (N, K) tensor, num_slices is |A| in Section˜4.2, ‘global_step‘ is used for sync. sampling across GPUs and can be omited for single-GPU training. An optimized implementation with caching is also provided in our official codebase, computation times provided in Table˜6.

<!-- chunk {"id": "body-0064", "role": "body", "section": "Characteristic Functions are Stable, Scalable and Identifiable", "weight": 1.0} -->

By the chain rule, Section˜4.2.3 directly gives ${{\nabla_{\theta}{EP}}{(\mathbf{a})}} \leq {\frac{4\sigma^{2}}{N}{}_{i = 1}^{N}\mathbf{a}^{\top}{\nabla_{\theta}f_{\theta}}{(\mathbf{x}_{i})}}$, providing stable gradients. The limitations of moment-based and CDF-based tests coupled with Section˜4.2.3 justifies our choice of the (Epps--Pulley): (i) DDP-friendly and scalable, (ii) uniformly bounded gradients and curvature regardless of input distribution, and (iii) hyper-parameter free implementation. Lastly, we highlight that our implementation has a linear memory and computational complexity of $\mathcal{O}{(N)}$, with $N$ the minibatch size.

<!-- chunk {"id": "body-0065", "role": "body", "section": "Characteristic Functions are Stable, Scalable and Identifiable", "weight": 1.0} -->

The implementation of SIGReg using that statistical test is provided in LABEL:lst:epps-pulley-pytorch, along with computation times of the forward-backward pass in Table˜6.

<!-- chunk {"id": "body-0066", "role": "body", "section": "Characteristic Functions are Stable, Scalable and Identifiable", "weight": 1.0} -->

As a last step before introducing LeJEPA, we ought to study the requirements on the number of directions ($|A|$) for (4.2) to be effective in high-dimension.

<!-- chunk {"id": "body-0067", "role": "body", "section": "How SIGReg Beats the Curse of Dimensionality", "weight": 1.0} -->

This last section seeks to characterize how many slices in $A$ one must sample for to be an effective statistical test. That design is crucial if we hope for LeJEPA to successfully converge towards isotropic Gaussian embeddings.

<!-- chunk {"id": "body-0068", "role": "body", "section": "Smoothness Beats the Curse of Dimensionality", "weight": 1.0} -->

Our first argument arguing for a favorable scaling of $|A|$ with the embedding dimension $K$ relies on the smoothness of $P_{\mathbf{θ}}$ as measured by its Sobolev regularity $\alpha$ (adams2003sobolev). We formalize below a bound on the directional test from Equation˜3 over all possible directions $\mathbf{a}$ when the test statistic is minimized over ${|A|} = M$ directions. While we provide bounds on the expected discrepancy over random directions $\mathbf{a}$ when the EP test is satisfied (equals zero) on a finite set of directions, the provided proof includes the case of moment-based and CDF-based tests as well.

<!-- chunk {"id": "body-0069", "role": "body", "section": "Smoothness Beats the Curse of Dimensionality", "weight": 1.0} -->

As ${|A|}\rightarrow\infty$, the bound decays as ${|A|}^{- {{2\alpha}/{({K - 1})}}}$, showing that ${|A|} = {O{(K)}}$ directions suffice for $\epsilon$-approximation when $\alpha$ is large. Some examples of embedding densities with varying $\alpha$ are provided in Figure˜4. The following statement characterizes how the $M$ directions actually constrain the entire space as a function of $\alpha$.

<!-- chunk {"id": "body-0070", "role": "body", "section": "Smoothness Beats the Curse of Dimensionality", "weight": 1.0} -->

The constant ${C{(K,\alpha)}} = \frac{2^{2\alpha}\pi^{{({K - 1})}/2}\left( {\alpha + \frac{K - 1}{2}} \right)}{{({K - 1})}{(\alpha)}\left( \frac{K - 1}{2} \right)}$ is visualized in Figure˜15 (left) depicting how $\alpha$ and $|A|$ interact. In words, we obtain that thanks to the natural smoothness of DN--either stemming from the architecture or the implicit and explicit regularizers used during training--applying SIGReg on $|A|$ directions can be sufficient to tightly constrain the entire space. We note that considering the worst case over $\mathbf{a}$ or using low-discrepancy sequences for $\mathbf{a}$ does not impact the asymptotic bounds, details provided in Appendix˜D.

<!-- chunk {"id": "body-0071", "role": "body", "section": "SGD Beats the Curse of Dimensionality", "weight": 1.0} -->

Our second argument leverages the iterative nature of DN training. Although we may use only $|A|$ to be a few hundreds, the cumulative number of sampled directions grows linearly with training time. This resampling effect (illustrated in Figure˜7, bottom) enables rapid convergence. Even small $|A|$ achieves tight distributional matching compared to keeping the set $A$ fixed throughout minibatches (recall Section˜4.3). Our experiments show that even with $|A|$ as low as $16$ can easily outperform a fixed set with $|A|$ of order of thousands thanks to the compounding effect of resampling at each minibatch.

<!-- chunk {"id": "body-0072", "role": "body", "section": "Empirical Validation on Synthetic Data", "weight": 1.0} -->

We conclude this section with a controlled experiment applying with gradient-based training to produce isotropic embeddings. In this setup, we directly consider embeddings $\mathbf{Z}$ which we will differentiate and optimized to minimize. By directly optimizing the embeddings we are able to observe the impact of the loss without any possible constraint and regularization that would come from the architecture. We sample $N$ i.i.d. samples ${\mathbf{x}}_{n}$ in a $D$-dimensional space. This sampling is based on an isotropic Gaussian distribution--but the first two dimensions are again set to the adversarial "X" shape. That is, among the $D$ dimensions, only two must be transformed as all the other ones already obey the isotropic Gaussian target distribution. We then make the samples ${\mathbf{x}}_{n}$ differentiable and optimize then to minimize the value of the different statistical tests compute on $M$ random $M$ random directions.

<!-- chunk {"id": "body-0073", "role": "body", "section": "Empirical Validation on Synthetic Data", "weight": 1.0} -->

Those directions are resampled after each gradient step--which follows the procedure we will employ in LeJEPA. We present the results in Figure˜6 demonstrating that even in challenging case, i.e., $D = 512$ and $M = 16$, SIGReg is able to detect the two degenerate dimensions and unfold them back to how they should look like under the target distribution.

<!-- chunk {"id": "body-0074", "role": "body", "section": "LeJEPA: Stable and Scalable Implementation", "weight": 1.0} -->

Having established that isotropic Gaussians are the optimal embedding distribution for foundation models (Section˜3) and introduced SIGReg to achieve this distribution (Section˜4.2), we now present the complete LeJEPA framework. We first evaluate candidate statistical tests (Sections˜4.2.1 and 4.2.2) and identify characteristic function-based tests as optimal for gradient-based training (Section˜4.2.3). The full LeJEPA implementation follows in Section˜5.1.

<!-- chunk {"id": "body-0075", "role": "body", "section": "LeJEPA: SIGReg + Prediction Loss", "weight": 1.0} -->

def LeJEPA(global_views, all_views, lambd):
"""global_views and all_views are lists of tensors, lambd is a scalar"""
## embedding of global views
g_emb = forward(torch.cat(glob_views))
## embedding of local views
## if resnet: skip with a_emb=g_emb
a_emb = forward(torch.cat(all_views))
## LeJEPA loss
centers = g_emb.view(-1, bs, K).mean
a_emb = a_emb.view(-1, bs, K)
sim = (centers - a_emb).square.mean
sigreg = mean(SIGReg(emb, global_step) for emb in a_emb)
return (1-lambd)*sim + lambd*sigreg
Algorithm 2: LeJEPA implementation–works out-of-the-box on any dataset, with DDP, with any backbone, e.g., torchvision or timm.

<!-- chunk {"id": "body-0076", "role": "body", "section": "LeJEPA: SIGReg + Prediction Loss", "weight": 1.0} -->

For non-ViT architectures (e.g., ResNet), set global_views = all_views. We use bs for the minibatch size, SIGReg is from LABEL:lst:epps-pulley-pytorch.

<!-- chunk {"id": "body-0077", "role": "body", "section": "LeJEPA: SIGReg + Prediction Loss", "weight": 1.0} -->

We now discuss the implementation of LeJEPA starting with SIGReg and followed by the prediction and total losses.

<!-- chunk {"id": "body-0078", "role": "body", "section": "LeJEPA: SIGReg + Prediction Loss", "weight": 1.0} -->

The SIGReg Loss. We chose (Epps--Pulley) for its provable boundedness (Section˜4.2.3) and its scalability. Its implementation follows exactly the equation except for the integrate which is estimated using a quadrature approximation. We find that the simple trapezoidal quadrature rule is sufficient even with as few knots as $17$, as ablated in Figure˜20. In particular, we leverage the symmetry of the integrand to double the number of knots for free, see the official code. On the other hand, the use of minibatches introduces a bias vanishing at rate $\mathcal{O}{({1/N})}$, as formalized below.

<!-- chunk {"id": "body-0079", "role": "body", "section": "LeJEPA: SIGReg + Prediction Loss", "weight": 1.0} -->

Hence, the gradients we obtain from using (Epps--Pulley) are biased by an explicit $\mathcal{O}{({1/N})}$ term. We found this bias to be minimal and not a concern even for minibatches as small as 16. Unbiased alternatives include using U-statistic debiasing of ${|\phi_{\theta}|}^{2}$ or sample splitting, which we do not explore in this study. Our final implementation of the SIGReg term with Epps-Pulley statistic is provided in LABEL:lst:epps-pulley-pytorch.

<!-- chunk {"id": "body-0080", "role": "body", "section": "LeJEPA: SIGReg + Prediction Loss", "weight": 1.0} -->

The Prediction Loss. To standardize notations, we adopt the DINO (caron2021emerging) setup of generating $V_{g}$ global views and $V_{l}$ local views, leading to a total of $V = {V_{g} + V_{l}}$ views. We set the first $1,\ldots,V_{g}$ indices of each ${\mathbf{z}}_{n,v}$ as the global views. For the cases without local views, simply set $V_{l} = 0$. The prediction loss is then given by having all views predict the global views as

<!-- chunk {"id": "body-0081", "role": "body", "section": "LeJEPA: SIGReg + Prediction Loss", "weight": 1.0} -->

LeJEPA Loss. The final total loss simply combines the above prediction loss along with SIGReg on each views as per

<!-- chunk {"id": "body-0082", "role": "body", "section": "LeJEPA: SIGReg + Prediction Loss", "weight": 1.0} -->

We present 's implementation in LABEL:code:lejepa. Altogether, the entire implementation--besides the usual model definitions, optimizers, and data loaders--only takes a few dozens lines in PyTorch (LABEL:lst:epps-pulley-pytorch and LABEL:code:lejepa). The absence of prototypes, stop-gradients, and teacher-student networks makes appealing as it only contains one hyperparameter, $\lambda$, balancing the trade-off between the prediction and isotropic Gaussian terms.

<!-- chunk {"id": "body-0083", "role": "body", "section": "Relation to Prior Work", "weight": 1.0} -->

Prior to presenting our experiments (Section˜6), we conclude by discussing how our proposed LeJEPA and SIGReg objective relate to existing frameworks in the literature.

<!-- chunk {"id": "body-0084", "role": "body", "section": "Relation to Prior Work", "weight": 1.0} -->

While there is no existing solution employing such slicing and distribution matching for JEPAs, there exists similar pipelines for generative models and optimal transport. Notably, the Sliced Score Matching (song2020sliced) proposes to leverage univariate slicing of the space to ease the estimation of a density for generative models. In a similar vein, the sliced Wasserstein distance (bonneel2015sliced; nguyen2023energy) uses such strategy to speed up and improve optimal transport. Furthermore, when the integral of the (Epps--Pulley) test is computed exactly, as opposed to our quadrature, each slice loss value recovers the kernel MMD (sriperumbudur2010hilbert; gretton2012kernel; chwialkowski2016kernel) measuring the distance between two distributions--albeit with a quadratic complexity. Lastly, it is possible to recover some existing SSL frameworks in the limit by employing LeJEPA with a particular test--instead of the preferred (Epps--Pulley).

<!-- chunk {"id": "body-0085", "role": "body", "section": "Relation to Prior Work", "weight": 1.0} -->

And since our invariance term is simply the $\ell_{2}$ distance between the views' embeddings, LeJEPA recovers VICReg for this degenerate statistical test. Based on Section˜4.2.1, we however strongly advocate against such a setting as it would lead to shortcut solutions--a phenomenon already observed in VICReg.

<!-- chunk {"id": "body-0086", "role": "body", "section": "LeJEPA: Empirical Validation", "weight": 1.0} -->

We now use the LeJEPA implementation described in Section˜5.1 to demonstrate its effectiveness through comprehensive experiments. We show that LeJEPA: (i) trains reliably across diverse architectures and datasets (Section˜6.1), (ii) provides an informative training loss for model selection (Section˜6.2), (iii) outperforms frontier vision models on small-scale in-domain pretraining (Section˜6.3), (iv) scales successfully to nearly 1 billion parameters on ImageNet-1k (Section˜6.4), and (v) learns rich semantic segmentation features without explicit supervision.

<!-- chunk {"id": "body-0087", "role": "body", "section": "LeJEPA's Stability Across Hyper-Parameters and Architectures", "weight": 1.0} -->

We now demonstrate LeJEPA's stability across hyperparameters, architectures, and experimental setups. Additional cross-domain stability results are presented in Section˜6.3.

<!-- chunk {"id": "body-0088", "role": "body", "section": "views (V = Vg + Vl)", "weight": 1.0} -->

Stability across standard hyperparameters. We begin by evaluating LeJEPA on ImageNet-100 and ImageNet-1K. On ImageNet-100, we train a ResNet-50 and vary the number of views and the loss weighting $\lambda$ (Figure˜8). Performance remains stable across both dimensions, leading us to recommend $\lambda = 0.05$ as a robust default. On ImageNet-1K, we train a ViT-Large/14 and explore batch size, as well as the number of global ($V_{g}$) and local ($V_{l}$) views (Table˜1b). We find that the configuration commonly used in prior work (${V_{g} = 2},{V_{l} = 8}$) transfers well to LeJEPA. Notably, LeJEPA achieves competitive performance with batch sizes as small as 128 on ImageNet-1K (Table˜1c), suggesting reduced memory requirements compared to existing methods.

<!-- chunk {"id": "body-0089", "role": "body", "section": "views (V = Vg + Vl)", "weight": 1.0} -->

We thus recommend to use $\lambda = 0.05$, $V_{g} = 2$, $V_{l} = 8$, and batch size $\geq 128$ as starting points.

<!-- chunk {"id": "body-0090", "role": "body", "section": "views (V = Vg + Vl)", "weight": 1.0} -->

Stability across Epps-Pulley hyperparameters. We next examine hyperparameters specific to LeJEPA: the number of slices $|\mathcal{A}|$ in SIGReg, the integration domain for the Epps-Pulley test (Epps--Pulley), and the number of quadrature points for numerical integration. Table˜1a shows ablations on ImageNet-1K with ViT-Large/14. Both the integration domain and number of quadrature points have negligible impact on performance. This is expected: since the characteristic function is accurate at zero, the moments of the distribution are well-characterized even with a modest integration range. The number of slices $|\mathcal{A}|$ has a modest effect---while more slices slightly improve performance, even 512 slices yield competitive results. We thus recommend to use 17 integration points, an integration domain of $\lbrack{- 5},5\rbrack$, and 1024 slices as starting points.

<!-- chunk {"id": "body-0091", "role": "body", "section": "views (V = Vg + Vl)", "weight": 1.0} -->

Stability across architectures. A key advantage of LeJEPA over recent methods (e.g., IJEPA, DINOv2) is its architecture-agnostic design. While most modern self-supervised methods are tailored to Vision Transformers, LeJEPA works across diverse architecture families without modification. To validate this claim, we pretrain approximately 50 architectures from 8 different families on ImageNet-10, selecting all models in the timm library with fewer than 20M parameters. All models are able to learn high-quality representations reaching between 91.5% to 95% top 1 accuracy with frozen backbone linear probing. It seems that models performing well in supervised learning setups are also the ones to favor for LeJEPA, such as resnets and ViTs. We thus recommend to use standard architectures such as ResNets and ViTs over specialized models like EfficientNet as stating point.

<!-- chunk {"id": "body-0092", "role": "body", "section": "views (V = Vg + Vl)", "weight": 1.0} -->

Removal of popular heuristics. In addition to providing reliable performance across models and datasets, LeJEPA's provable construction enables us to remove many heuristics traditionally used to prevent collapse. First, prior work has shown both empirically and theoretically that predictors in image JEPA (without asymmetric information) and teacher-student architectures serve primarily to prevent collapse (grill2020bootstrap; jing2021understanding; tian2021understanding; caron2021emerging; chen2021empirical). Removing these components produces collapsed encoders, i.e., with performances at chance-level. Thanks to LeJEPA's SIGReg loss, we can remove both the predictor and teacher-student architecture without suffering from collapse, as shown in Table˜4. While a teacher-student configuration does provide a small performance boost for ViT models---consistent with observations in supervised learning via Stochastic Weight Averaging (izmailov2019averagingweightsleadswider)---it is not necessary to prevent collapse. In our setup, we apply SWA on the encoder producing $\mu$ in Equation˜7.

<!-- chunk {"id": "body-0093", "role": "body", "section": "views (V = Vg + Vl)", "weight": 1.0} -->

Second, recent work demonstrated that register tokens are needed to prevent training instabilities in vision models (oquab2023dinov2; simeoni2025dinov3; darcet2023vision). We show in Table˜1 that such instabilities likely stem from poorly conditioned training objectives. In contrast, LeJEPA does not require register tokens and achieves stable performance with or without them. We thus recommend training without a predictor or register tokens, and optionally applying SWA with ViTs for a possible performance gain.

<!-- chunk {"id": "body-0094", "role": "body", "section": "LeJEPA's Training Loss is Informative of Downstream Performance", "weight": 1.0} -->

A major challenge in SSL pretraining is the lack of reliable signals conveying the quality of the learned representation. As a result, it is common to monitor a supervised downstream task performance, sometimes supplemented with unsupervised embedding statistics (agrawal2022alpha; garrido2023rankme; thilak2023lidar). This process is highly limiting since it requires labeled data that is costly and overly specialized. This is further exacerbated in the latest JEPA models where training losses exhibit low correlation with downstream performance--and may not even decrease monotonically during training.

<!-- chunk {"id": "body-0095", "role": "body", "section": "LeJEPA's Training Loss is Informative of Downstream Performance", "weight": 1.0} -->

In contrast, we find that LeJEPA's training loss behaves much more favorably--providing us with a meaningful signal on model quality. First, we provide in Figure˜10, the 2D plane spanned by the SIGReg and prediction losses where a clear trend with downstream task accuracy can be observed. More strikingly, the combined training loss with mixing coefficient $\lambda$ exhibits very high Spearman correlation (spearman1961proof), denoted as $\rho_{s}$, of about $85\%$ with downstream accuracy--which is considered a strong signal. This strong relationship holds across datasets and architectures. As a result, a lower LeJEPA training loss reliably indicates a better downstream performance.

<!-- chunk {"id": "body-0096", "role": "body", "section": "LeJEPA's Training Loss is Informative of Downstream Performance", "weight": 1.0} -->

We can further improve this correlation through a simple scaling law based upon the trade-off weighting hyperparameter $\lambda$

<!-- chunk {"id": "body-0097", "role": "body", "section": "LeJEPA's Training Loss is Informative of Downstream Performance", "weight": 1.0} -->

By setting $\alpha \approx 0.4$, LeJEPA's training loss is able to achieve nearly 99% correlation with downstream performance across multiple datasets and models. We depict the changes in $C^{(\alpha)}$ as a function of $\alpha$ on multiple datasets and models in Figure˜11, as well as the training LeJEPA loss against downstream performance in Figure˜19. The strong alignment between LeJEPA's training loss and model quality enables label-free SSL model selection and cross-validation.

<!-- chunk {"id": "body-0098", "role": "body", "section": "In-Domain LeJEPA Outperforms Frontier Model Transfer Learning", "weight": 1.0} -->

A key promise of self-supervised learning is to learn universal representations that generalize across tasks and domains. However, current frontier foundation models (e.g., DINOv2/v3, IJEPA) are pretrained on natural images forcing practitioners in specialized domains to collect large amount of labels for supervised finetuning. In fact, most frontier models can not be trained directly on those domains as the number of samples may be small and searching again for the hyper-parameters would be cumbersome yet necessary (assran2022hidden).

<!-- chunk {"id": "body-0099", "role": "body", "section": "In-Domain LeJEPA Outperforms Frontier Model Transfer Learning", "weight": 1.0} -->

To demonstrate LeJEPA's versatility and ability to resolve that current pain-point, we propose to pretrain directly on a new domain without any change in the loss or the pretraining pipeline. We select the dataset, a galaxy morphology classification task that differs significantly from natural images in both visual structure and statistical properties (balestriero2025gaussian). The dataset contains 11,000 training samples across 10 galaxy types. For LeJEPA, we use the default hyper-parameters and pretrain for 400 epochs a variety of backbones. We compare against the latest DINOv2, DINOv3 and IJEPA. We report in Figure˜12 the top1 accuracy for linear probing both with frozen backbone and full-finetuning. We observe that in-domain pretraining with LeJEPA substantially outperforms state-of-the-art frontier models (DINOv2, DINOv3) on both linear probing and full finetuning. Additional datasets and backbones are provided in Table˜5 depicting LeJEPA's ability to train in-domain, even with a dataset with $1000$ samples (flowers102).

<!-- chunk {"id": "body-0100", "role": "body", "section": "In-Domain LeJEPA Outperforms Frontier Model Transfer Learning", "weight": 1.0} -->

Coupling this result with the stability of LeJEPA across architectures and hyper-parameters should offer a promising alternatives in domains not yet accounted for by the latest frontier models.

<!-- chunk {"id": "body-0101", "role": "body", "section": "LeJEPA Scales Across Data and Models", "weight": 1.0} -->

We now propose to apply LeJEPA over a larger pretraining dataset, i.e., Imagenet-1k, and over larger backbones such as ViT/Large (0.3B), ConvNextV2-Huge (0.6B). For those two models, we reach an online linear probe accuracy on inet1k of 77.1% and 78.5% respectively. Beyond in-distribution performances, we also explore transfer learning. For those experiments, our baselines are IJEPA with a ViT-Huge (0.6B) which is the closest to our setup, and we also include a recent improved version of IJEPA including additional stochastic prediction tasks (bar2023stochastic) that is coined IJEPA + STOP. For LeJEPA, we employ the same recipe as described in Section˜6.1 and report transfer learning performances with frozen backbone in Table˜2. We observe that we consistently outperform IJEPA while employed a smaller model and shorted training schedule. Beyond top1 accuracy, we also echo our findings from Section˜6.2 about LeJEPA's training loss quality.

<!-- chunk {"id": "body-0102", "role": "body", "section": "LeJEPA Scales Across Data and Models", "weight": 1.0} -->

In our setup, we observe a very stable and smooth training curve indicating a stable optimization landscape removing the need for careful hyperparameter selection (recall Section˜4.2.3). We provide an example on a ViT-gigantic (1.8B parameters) in Figure˜2.

<!-- chunk {"id": "body-0103", "role": "body", "section": "Emergent Semantic Structure in LeJEPA Representations", "weight": 1.0} -->

A hallmark of successful self-supervised learning is the emergence of semantically meaningful attention patterns without explicit supervision (caron2021emerging). To assess whether LeJEPA learns such structure, we visualize the attention maps of the learned representations. Following DINO (caron2021emerging), we apply PCA to the embeddings and visualize the first principal components, which reveal clear correspondence to object boundaries and salient regions (Figure˜14). Furthermore, we explore whether these attention patterns can enable unsupervised video segmentation---a challenging task requiring temporal consistency and object understanding. By thresholding the self-attention maps of the \[CLS\] token, we obtain binary masks that track objects across frames without any segmentation labels during training. As shown in Figure˜13, LeJEPA's attention naturally segments foreground objects from background with remarkable temporal coherence, suggesting that the learned representations capture both spatial semantics and temporal structure. This emergent capability demonstrates that LeJEPA's stability-focused objective does not sacrifice the semantic richness of learned features.

<!-- chunk {"id": "body-0104", "role": "body", "section": "Conclusion", "weight": 1.5} -->

We have established a principled theoretical framework for JEPA-based self-supervised learning that fundamentally resolves its core pathologies. Our contributions span theory and practice: we proved that isotropic Gaussian embeddings uniquely minimize worst-case downstream risk, introduced SIGReg as a tractable and provably correct method to enforce this distribution, and demonstrated that this approach eliminates representational collapse by design--and not through ad-hoc combinations of teacher-student networks, stop-gradients, or asymmetric architectures.

<!-- chunk {"id": "body-0105", "role": "body", "section": "Conclusion", "weight": 1.5} -->

We validate LeJEPA across domains and over $60$ architectures including gigantic versions with 1.8B parameters. In spite of its simplicify, LeJEPA matches state-of-the-art performance while requiring fewer than 50 lines of core implementation. Critically, our approach provides what SSL has long needed: a mathematically rigorous foundation that directly informs practical algorithm design.
