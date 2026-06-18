<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Spectral State Space Models

Topics include Robustness, Convolutional networks, Learning.

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

This paper studies sequence modeling for prediction tasks with long range dependencies. We propose a new formulation for state space models (SSMs) based on learning linear dynamical systems with the spectral filtering algorithm (Hazan et al. ). This gives rise to a novel sequence prediction architecture we call a spectral state space model. Spectral state space models have two primary advantages. First, they have provable robustness properties as their performance depends on neither the spectrum of the underlying dynamics nor the dimensionality of the problem. Second, these models are constructed with fixed convolutional filters that do not require learning while still outperforming SSMs in both theory and practice. The resulting models are evaluated on synthetic dynamical systems and long-range prediction tasks of various modalities. These evaluations support the theoretical benefits of spectral filtering for tasks requiring very long range memory.

<!-- chunk {"id": "body-0003", "role": "body", "section": "Introduction", "weight": 1.5} -->

Handling long-range dependencies efficiently remains a core problem in sequence prediction/modelling. Recurrent Neural Networks (RNN) \[, RHW^+^85, \] are a natural choice, but are notoriously hard to train; they often suffer from vanishing and exploding gradients and despite techniques to mitigate the issue \[, CVMG^+^14, \], they are also hard to scale given the inherently sequential nature of their computation.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

In recent years, transformer models \[VSP^+^17\] have become the staple of sequence modelling, achieving remarkable success across multiple domains \[BMR^+^20, DBK^+^20, JEP^+^21\]. Transformer models are naturally parallelizable and hence scale significantly better than RNNs. However, attention layers have memory/computation requirements that scale quadratically with context length. Many approximations have been proposed (see for a recent survey).

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

RNNs have seen a recent resurgence in the form of state space models (SSM) which have shown promise in modelling long sequences across varied modalities \[, DFS^+^22 OSG^+^23, PMN^+^23, \]. SSMs use linear dynamical systems (LDS) to model the sequence-to sequence transform by evolving the internal state of a dynamical system according to the dynamics equations

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

Here $x_{t} \in {\mathbb{R}}^{d}$ is the hidden state of the dynamical system, $u_{t}$ is the input to the system, and $y_{t}$ are observations. The matrices $A,B,C,D$ govern the evolution of the system and are called system matrices. Despite its simplicity, this linear model can capture a rich set of natural dynamical systems in engineering and the physical sciences due to the potentially large number of hidden dimensions. Linear dynamical systems are also attractive as a sequence model because their structure is amenable to both fast inference and fast training via parallel scans or convolutions. A rich literature stemming from control theory and recent machine learning interest has given rise to efficient techniques for system identification, filtering, and prediction for linear dynamical systems. For a survey of recent literature see. These techniques make SSMs attractive for sequence tasks which inherently depend on long contexts that scale poorly for transformers. Examples include large language models \[DFS^+^22\], modelling time series \[ZSP^+^23\], and audio generation.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

To understand the factors affecting the memory in an SSM or simply a linear dynamical system, we now proceed to delineate how past states and inputs affect the future.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Geometric decay in LDS", "weight": 1.0} -->

The linear equations governing the dynamics are recursive in nature, and imply that in a noiseless environment, the $t$'th output can be written as

<!-- chunk {"id": "body-0009", "role": "body", "section": "Geometric decay in LDS", "weight": 1.0} -->

The matrix $A$ is asymmetric in general, and can have complex eigenvalues. If the amplitude of these eigenvalues is $> 1$, then the output $y_{t}$ can grow without bounds. This is called an "explosive\" system. In a well-behaved system, the eigenvalues of $A$ have magnitude $< 1$. If the magnitudes are bounded away from $1$, say ${|{\lambda_{i}{(A)}}|} < {1 - \delta}$, for some $\delta > 0$ (referred to as spectral gap), then we can write

<!-- chunk {"id": "body-0010", "role": "body", "section": "Geometric decay in LDS", "weight": 1.0} -->

for $k = {O{({\frac{1}{\delta}{\log\frac{1}{\varepsilon}}})}}$. This mathematical fact implies that the effective memory of the system is on the order of $\frac{1}{\delta}$. In general, the parameter $\delta$ is unknown apriori and can get arbitrarily small as we approach systems with have long range dependencies leading to instability in training linear dynamical systems with a long context. This issue is specifically highlighted in the work of \[OSG^+^23\] who observe that on long range tasks learning an LDS directly does not succeed and requires interventions such as stable exponential parameterizations and specific normalization which have been repeatedly used either implicitly or explicitly in the SSM literature. Unfortunately these reparametrizations and normalizations come with no theoretical guarantees.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Geometric decay in LDS", "weight": 1.0} -->

In fact this limitation is generally known to be fundamental to the use of linear dynamical systems, and can only be circumvented via a significant increase in sample complexity \[GLS^+^20\] or via control over the input sequence \[SMT^+^18\].

<!-- chunk {"id": "body-0012", "role": "body", "section": "Spectral filtering for linear dynamical systems", "weight": 1.0} -->

A notable deviation from the standard theory of linear dynamical systems that allows efficient learning in the presence of arbitrarily long memory is the technique of spectral filtering. The idea is to project the sequence of inputs to a small subspace that is constructed using special structure of discrete LDS where successive powers of the system matrix appear in the impulse response function. The basic idea is to represent the output as

<!-- chunk {"id": "body-0013", "role": "body", "section": "Spectral filtering for linear dynamical systems", "weight": 1.0} -->

where $\phi_{j}$ are spectral filters which are sequence-length sized vectors that given the target sequence length can be computed offline, and $M_{j}$ are matrices parameterizing the model. These spectral-filters are the eigenvectors of the matrix constructed as the average of outer products of the discrete impulse-response functions, viz $Z = {\int_{0}^{1}{{\lbrack 1,\alpha,{\alpha^{2}\ldots}\rbrack}{\lbrack 1,\alpha,{\alpha^{2}\ldots}\rbrack}^{\top}{d\alpha}}}$. It is shown that this matrix is inherently low-dimensional and for all $\alpha \in {\lbrack 0,1\rbrack}$, vectors of the form $\lbrack 1,\alpha,{\alpha^{2}\ldots}\rbrack$ are well approximated by the top-eigenspace of Z. Figure depicts these filters.

<!-- chunk {"id": "body-0014", "role": "body", "section": "Spectral filtering for linear dynamical systems", "weight": 1.0} -->

For the details of how these filters are derived and their computation, see Section.

<!-- chunk {"id": "body-0015", "role": "body", "section": "Why is spectral filtering important?", "weight": 1.0} -->

The main advantage of spectral filtering is that for certain types of linear dynamical systems, in particular those with symmetric matrices $A$, the effective memory(measured by the number of filters) required to represent an observation at any point in the sequence in the spectral basis is independent of the spectral gap parameter $\delta$!. This guarantee indicates that if we featurize the input into the spectral basis, we can potentially design models that are capable of efficiently and stably representing systems with extremely long memory even with $\delta\rightarrow 0$. This striking fact motivates our derivation of the recurrent spectral architecture, and is the underlying justification for the performance and training stability gains we see in experiments.

<!-- chunk {"id": "body-0016", "role": "body", "section": "Our Contributions", "weight": 1.0} -->

We start by proposing state space models with learned components that apply spectral filtering for their featurization. We consider two types of spectral filters, which augment the original spectral filters proposed with negative eigenvalues in two different ways. Our main contribution is a neural architecture that is based on these spectral state space models. This neural architecture can be applied recursively in layers, resulting in an expressive architecture for modeling sequential data.

<!-- chunk {"id": "body-0017", "role": "body", "section": "Our Contributions", "weight": 1.0} -->

Finally we implement this neural architecture and apply it towards synthetically generated data as well as the Long Range Arena benchmark \[TDA^+^21\]. We demonstrate that spectral state space models can stably and more efficiently learn on sequence modelling tasks with long range dependencies without the need for exponential parameterizations, particular initializations and normalizations.

<!-- chunk {"id": "body-0018", "role": "body", "section": "Main Advantages of Spectral SSM", "weight": 1.0} -->

Previously proposed convolutional models for sequence modeling, surveyed in the related work section, learn the kernels from the data. The kernels used in Spectral SSM are theoretically-founded and fixed and thus parameter-free. In addition, our models are provably as expressive as an LDS. In particular, their expressiveness neither depends on the spectra gap nor on the dimension of the system, which are necessary in all other methods.

<!-- chunk {"id": "body-0019", "role": "body", "section": "State space models", "weight": 1.0} -->

SSMs for learning long range phenomenon have received much attention in the deep learning community in recent years starting with the works \[GDE^+^20\],\[GJG^+^21\] which propose and develop the HiPPO theory. develop the S4 parameterization to address the bottlenecks of training efficiency, performance and numberical stability. The S4 parameterization restricts the system matrices $A$ to be normal plus low-rank, allowing for stable diagonalization. The S4 model was further streamlined in later works, viz. using diagonal system matrices without a loss in performance and the S5 model which uses a MIMO diagonal system and associative scans for computational efficiency. \[OSG^+^23\] investigate whether simpler deep Linear Recurrent Units (LRU) can recover the performance of deep SSMs, and provide an affirmative answer under the crucial caveat that specific modifications on linear RNNs, namely the stable exponential parameterization, $\gamma$- normalization and ring initialization, are necessary to learn on certain challenging long-context modeling tasks. We discuss the details of this ablation in the appendix (Section A.1).

<!-- chunk {"id": "body-0020", "role": "body", "section": "Spectral filtering", "weight": 1.0} -->

The technique of spectral filtering was developed as a convex improper learning alternative to directly parameterizing an LDS (as in the case of SSMs) leading to an efficient, polynomial-time algorithm and near-optimal regret guarantees. Different from regression-based methods (eg. SSMs) that aim to identify the system dynamics, spectral filtering's guarantee does not depend on the stability of the underlying system, and is the first method to obtain condition number-free regret guarantees for the MIMO setting. Extension to asymmetric dynamical systems was further studied in \[HLS^+^18\].

<!-- chunk {"id": "body-0021", "role": "body", "section": "Convolutional Models for Sequence Modeling", "weight": 1.0} -->

Exploiting the connnection between LDS and convolutions, various convolutional models have been proposed for sequence modelling. \[FEN^+^23\] employ direct learning of convolutional kernels but find that they underperform SSMs, identifying non-smoothness of kernels to be the culprit and propose applying explicit smoothing and squashing operations. \[LCZ^+^22\] identifies two key characteristics of convolutions to be crucial for long range modelling, decay in filters and small number of parameters parameterizing the kernel. propose a multiresolution kernel structure inspired from the wavelet transform and multiresolution analysis.

<!-- chunk {"id": "body-0022", "role": "body", "section": "Convolutional Models for Sequence Modeling", "weight": 1.0} -->

All these methods parameterize the kernels with specific structures and/or add further regularizations to emulate the convolution kernels implied by SSMs. In contrast our proposed kernels are fixed and thereby parameter-free and the number of parameters scale in the number of kernels and not the size of the kernel. Furthermore our kernels are provably more expressive than linear dynamical systems capable of directly capturing and improving the performance of SSMs without the need for specific initializations. Naturally our kernels by default satisfy both the smoothness and the decay condition identified (and explicitly enforced) by \[LCZ^+^22\] and \[FEN^+^23\].

<!-- chunk {"id": "body-0023", "role": "body", "section": "Sequence prediction", "weight": 1.0} -->

We treat sequence prediction as a game between a predictor/learner and nature in which iteratively at every time $t \in {\lbrack L\rbrack}$, the learner is presented an input $u_{t} \in {\mathbb{R}}^{d_{in}}$. The learner $A$ then produces a candidate output ${\hat{y}}_{t} = {{\hat{y}}_{t}{(A)}}$, and nature reveals the $t^{th}$ element of a target sequence $y_{t} \in {\mathbb{R}}^{d_{out}}$. The learner then suffers an instantaneous loss of ${\|{y_{t} - {\hat{y}}_{t}}\|}^{2}$. The task of the learner is to minimize regret over a benchmark set of learning algorithms $\mathcal{A}$, defined as follows

<!-- chunk {"id": "body-0024", "role": "body", "section": "Linear Dynamical Systems (LDS)", "weight": 1.0} -->

An example benchmark set of methods is that of a linear dynamical system, which has four matrix parameters, ${A \in {\mathbb{R}}^{N \times N}},{{B \in {\mathbb{R}}^{N \times d_{in}}},{{C \in {\mathbb{R}}^{d_{out} \times N}},{D \in {\mathbb{R}}^{d_{out} \times d_{in}}}}}$. The system evolves and generates outputs according to the following equations

<!-- chunk {"id": "body-0025", "role": "body", "section": "Linear Dynamical Systems (LDS)", "weight": 1.0} -->

Thus, an example class of benchmark algorithms $\mathcal{A}$ are all predictors that generate ${\hat{y}}_{t}$ according to these rules, for a fixed set of matrices $A,B,C,D$.

<!-- chunk {"id": "body-0026", "role": "body", "section": "Spectral Filtering", "weight": 1.0} -->

Another important set of predictors is one which is inspired by spectral filtering. The spectral filtering theory builds an efficient representation for all vectors in the range of the function $\mu:{{\lbrack 0,1\rbrack}\rightarrow{\mathbb{R}}^{L}}$ defined as ${\mu{(\alpha)}} \triangleq {{({\alpha - 1})}{\lbrack 1,\alpha,{\alpha^{2}\ldots}\rbrack}}$. To build this representation, for any $L$ define the following Hankel matrix $Z \in {\mathbb{R}}^{L \times L}$ whose entries are given by

<!-- chunk {"id": "body-0027", "role": "body", "section": "Spectral Filtering", "weight": 1.0} -->

It is shown in the appendix (see Lemma C.1) that $Z = {\int_{0}^{1}{\mu{(\alpha)}\mu{(\alpha)}^{\top}{d\alpha}}}$. Thus it can be seen that $Z$ is a real PSD Hankel matrix. It is known (see Lemma C.4. ‣ Appendix C Proof of Theorem 3.1 ‣ Spectral State Space Models") in the appendix) that real PSD Hankel matrices have an exponentially decaying spectrum. As a result, the crux of the spectral filtering theory, lies in showing that for all $\alpha \in {\lbrack 0,1\rbrack}$ ^11^1in particular all $\alpha$ close to 1, representing marginally stable systems., the vector $\mu{(\alpha)}$ is approximately contained in the subspace spanned by the top eigenvectors of Z, making the subspace spanned by top-eigenvectors of Z a very efficient subspace to project the input into. This fact is formalized as Lemma C.3 in the appendix.

<!-- chunk {"id": "body-0028", "role": "body", "section": "Spectral Filtering", "weight": 1.0} -->

We now use this intuition to describe the Spectral Filtering algorithm.

<!-- chunk {"id": "body-0029", "role": "body", "section": "Spectral Filtering", "weight": 1.0} -->

Since Z is a real PSD matrix, it admits a real spectral decomposition, and the (non-negative) eigenvalues can be easily ordered naturally by their value. Let ${\{{({{\sigma_{j} \in {\mathbb{R}}},{\phi_{j} \in {\mathbb{R}}^{T}}})}\}}_{j = 1}^{L}$ be the eigenvalue-eigenvector pairs of $Z$ ordered to satisfy $\sigma_{1} \geq \sigma_{2} \geq \ldots \geq \sigma_{d}$. We consider a fixed number $K$ of the above eigenvectors. Algorithms in the spectral filtering class generate ${\hat{y}}_{t}$ as follows.

<!-- chunk {"id": "body-0030", "role": "body", "section": "Spectral Filtering", "weight": 1.0} -->

For each $k \in K$, we first featurize the input sequence by projecting the input sequence until time $t$ on $\phi_{k}$, leading to a sequence $U_{t,k} \in {\mathbb{R}}^{d_{in}}$ defined as

<!-- chunk {"id": "body-0031", "role": "body", "section": "Spectral Filtering", "weight": 1.0} -->

Note that given an input sequence $u_{1:L}$ for any $k$, the $d_{in} \times T$ matrix $U_{1:{L,k}}$ can be efficiently computed via convolutions along the time dimension $L$ in total time $O{({{d_{in} \cdot L}{\log{(L)}}})}$. The following theorem (proved ) establishes that the spectral filtering class of predictors approximately contains bounded linear dynamical systems with positive semi-definite $A$.

<!-- chunk {"id": "body-0032", "role": "body", "section": "Spectral Transform Unit (STU)", "weight": 1.0} -->

Note that for every $k$, the sequence of features $U_{1:{L,k}}$ can be computed efficiently via convolution. The output sequence $\{{y_{1}\cdots y_{L}}\}$ is then given by

<!-- chunk {"id": "body-0033", "role": "body", "section": "Spectral Transform Unit (STU)", "weight": 1.0} -->

The above output contains a small auto-regressive component that essentially allows for stable learning of the spectral component as the memory grows. The differences from the original spectral filtering class are the introduction of a negative part in the spectral component and the slight change in the auto-regressive component. Both of these changes are necessitated by the requirement to capture negative eigenvalues of $A$. Note that ) corresponds to the specification of the algorithm presented in \[HLS^+^18\], when the eigenvalues are known to be real numbers. For completeness and ease of discourse we prove the following representation theorem in the Appendix which shows that the above class approximately contains any marginally-stable LDS with symmetric $A$.^33^3We discovered some small but easily fixable errors in the original proof of which we have corrected in our proof

<!-- chunk {"id": "body-0034", "role": "body", "section": "Remark 3.2", "weight": 1.0} -->

Comparing Theorem 3.1 ‣ Spectral State Space Models") (our contribution) and Theorem 2.1 (Theorem 1 ), we note firstly that our theorem holds for symmetric matrices and not just PSD matrices. allude to a direct extension for the symmetric case which we believe is not fully correct. We use a similar idea to prove this theorem. Secondly a minor difference is that in the sequential prediction setting the prediction is auto-regressive, i.e. uses its own $y$ to make the future predictions.

<!-- chunk {"id": "body-0035", "role": "body", "section": "Remark 3.2", "weight": 1.0} -->

Due to space limitations, we discuss the runtime scaling of our method and compare it with different methods in the appendix (Section A).

<!-- chunk {"id": "body-0036", "role": "body", "section": "Experiment: Learning a marginally-stable LDS", "weight": 1.0} -->

We provide a simple synthetic evaluation of the stability and training efficiency afforded by the STU. We consider a low-dimensional linear system $A,B,C,D$ generated as follows. ${B \in {\mathbb{R}}^{4 \times 3}},{C \in {\mathbb{R}}^{3 \times 4}}$ are matrices with iid unit Gaussian entries. $D$ is a diagonal matrix with iid unit Gaussian entries and $A$ is a diagonal matrix with $A_{ii} \sim {0.9999 \ast Z}$ where $Z$ is a random sign. By design this is a system with a very high stability constant ($\sim 10^{4}$). As a training dataset we generated $\{{(u_{i},y_{i})}\}$ where $u_{i}$ is a random input sequence and $y_{i}$ is the output generated by applying the linear dynamical system on $u_{i}$. We perform mini-batch (batch size 1) training with the l2 loss.

<!-- chunk {"id": "body-0037", "role": "body", "section": "Experiment: Learning a marginally-stable LDS", "weight": 1.0} -->

As comparison we perform the same procedure with an LRU (Linear Recurrent Unit) layer as proposed by \[OSG^+^23\] which directly parameterizes the linear system. The results of the training loss as seen by the two systems are presented in Figure 3(a) ‣ Spectral State Space Models").

<!-- chunk {"id": "body-0038", "role": "body", "section": "Experiment: Learning a marginally-stable LDS", "weight": 1.0} -->

We use all the initialization/normalization techniques as recommended by \[OSG^+^23\] for LRU including the stable exponential parameterization, $\gamma$-normalization and ring-initialization. Indeed we find that all these tricks were necessary to learn this system at all. We provide more details about the ablations and other hyperparameter setups in the appendix. We observe that the STU is significantly more efficient at learning the LDS as opposed to the LRU. We further find that there is a wide range of LRs where the STU has a stable optimization trajectory and the loss decreases continuously highlighting the advantages of a convex parameterization. On the other hand, LRU is able to eventually learn the system at the right learning rates, it requires almost 8x the number of samples to get to a system with non-trivial accuracy. More details can be found in the appendix. Curiously we observe that for the LRU training plateaus completely for the first 50% of training highlighting the difficulty of optimization via a non-convex landscape.

<!-- chunk {"id": "body-0039", "role": "body", "section": "Experiment: Learning a marginally-stable LDS", "weight": 1.0} -->

The STU layer in the previous experiment employs $K = 25$. In Figure 3(b) ‣ Spectral State Space Models") we plot the performance of STU at various levels of $K$. As predicted by the theory we observe an exponential decay in the error as $K$ increases with the error effectively plateauing after $K \geq 15$.

<!-- chunk {"id": "body-0040", "role": "body", "section": "Stacked STU", "weight": 1.0} -->

(a) Schematic displaying a multi-layer STU model.

<!-- chunk {"id": "body-0041", "role": "body", "section": "Stacked STU", "weight": 1.0} -->

(b) Comparison of the basic stacked STU model against LRU ablations in [OSG+23]

<!-- chunk {"id": "body-0042", "role": "body", "section": "Stacked STU", "weight": 1.0} -->

To increase the representation capacity and to maintain the efficiency of prediction through linear dynamical systems, proposed models in the SSM literature take the form of stacking these sequence to sequence transforms into multiple layers. Non-linearities in the model can then be introduced by sandwiching them as layers lying in between these sequence to sequence transforms.

<!-- chunk {"id": "body-0043", "role": "body", "section": "Stacked STU", "weight": 1.0} -->

In this paper we closely follow the stacking approach followed by \[OSG^+^23\], replacing the LRU layers appropriately by STU layers. A schematic for the resultant multi-layer model is displayed in Figure 4(a). In a nutshell, the input sequence is first embedded via a time-invariant embedding function followed by multiple repetitions of alternating STU layers and non-linearities (in particular we use GLU). Finally the resulting output is time-pooled followed by a final readout layer according to the task at hand. This composite model can now be trained in a standard fashion via back-propagation and other commonly used deep-learning optimization techniques.

<!-- chunk {"id": "body-0044", "role": "body", "section": "Experiments on Long Range Arena \\[TDA^+^21\\]", "weight": 1.0} -->

We evaluate the stacked STU model on the Long Range Arena (LRA) benchmark \[TDA^+^21\]. This benchmark aims to assess the performance of sequence prediction models in long-context scenarios and consists of six tasks of various modalities, including text and images. The context length for the tasks ranges from 1K to 16K, and the tasks require capabilities such as hierarchical reasoning, matching and retrieval, and visual-spatial understanding. SSMs have shown significantly superior performance on most of the tasks compared to Transformer architectures. In particular for the hardest task in the suite, PathX (image classification with context length of 16K), no transformer model has been able to achieve accuracy beyond random guessing. We provide the evaluation of the stacked STU model on the two hardest tasks namely PathFinder and PathX in Table 4(b).

<!-- chunk {"id": "body-0045", "role": "body", "section": "Experiments on Long Range Arena \\[TDA^+^21\\]", "weight": 1.0} -->

We compare our performance against the ablation carried out by \[OSG^+^23\] who find that ring initialization, stable exponential parameterization and $\gamma$-normalization are all crucial towards learning these tasks. In particular as reported by \[OSG^+^23\] all three of the above interventions were necessary to learn on PathX to any non-trivial accuracy. This is a result of the much larger context length of 16K employed by the PathX task. On the other hand we find that the the stacked STU (with the STU component exactly as represented by )) is sufficient to learn on both these tasks to relatively high accuracies. Notably we do not require any other normalizations or initialization techniques We initialize all the parameters of the STU i.e. M matrices to 0. Details about our implementation as well as details about the experiments including hyperparameters can be found in the appendix (Section E. This result in particular confirms and highlights the theoretical stability afforded by the STU even under learning tasks involving large sequence lengths. In the appendix (Table we provide the performance evalaution of the stacked STU on all tasks of the LRA benchmark.

<!-- chunk {"id": "body-0046", "role": "body", "section": "Experiments on Long Range Arena \\[TDA^+^21\\]", "weight": 1.0} -->

In the next section we highlight a simple technique towards significantly improving the achieved accuracy for the stacked STU model.

<!-- chunk {"id": "body-0047", "role": "body", "section": "Hybrid Temporal and Spectral Units", "weight": 1.0} -->

A simple extension to the STU model (Equation )) is to parameterize the dependence of $y_{t}$ on $y_{t - 2}$ with a parameter $M_{y}$, leading to the following prediction model

<!-- chunk {"id": "body-0048", "role": "body", "section": "Hybrid Temporal and Spectral Units", "weight": 1.0} -->

Setting $M^{y} = I$ we recover the guarantees afforded by Theorem 3.1 ‣ Spectral State Space Models") and thus the above model is strictly more powerful. We find that the above change leads to significant improvements over the accuracy achieved by the simple STU model. We can further extend the auto-regression to depend on multiple previous $y$ as opposed to just $y_{t - 2}$. Indeed as the following theorem shows adding sufficiently long auto-regression is powerful enough to capture any LDS.

<!-- chunk {"id": "body-0049", "role": "body", "section": "Conclusion", "weight": 1.5} -->

Insprired by the success of SSMs, we present a new theoretically-founded deep neural network architecture, Spectral SSM, for sequence modelling based on the Spectral Filtering algorithm for learning Linear Dynamical Systems. The SSM performs a reparameterization of the LDS and is guaranteed to learn even marginally stable symmetric LDS stably and efficiently. We demonstrate the core advantages of the Spectal SSM, viz. robustness to long memory through experiments on a synthetic LDS and the Long Range Arena benchmark. We find that the Spectral SSM is able to learn even in the presence of large context lengths/memory without the need for designing specific initializations, discretizations or normalizations which were necessary for existing SSMs to learn in such settings. While spectral SSMs only model symmetric A, our presented set of experiments on the LRA benchmark suggest that the gap between symmetric and general A is potentially small in real world tasks. Indeed more recent SSM models like \[, DSF^+^24\] work with real diagonals (i.e. symmetric case) as they do not find evidence that adding complex eigenvalues help.

<!-- chunk {"id": "body-0050", "role": "body", "section": "Conclusion", "weight": 1.5} -->

Spectral filtering has been extended in certain settings to asymmetric A \[HLS^+^18\] and a similar extension to our proposal is straightforward but comes with efficiency losses and we leave it to future work.
