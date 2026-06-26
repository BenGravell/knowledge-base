<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

An Overview of Diffusion Models: Applications, Guided Generation, Statistical Rates and Optimization

Topics include Diffusion models, Generative artificial intelligence, Score-based generative modeling, Stochastic processes, Controlled generation, Conditional sampling, High-dimensional optimization, Machine learning theory, Survey.

<!-- chunk {"id": "summary-0002", "role": "summary", "section": "Summary", "weight": 2.0} -->

This review surveys diffusion models as generative samplers, guided generators, and tools for structured optimization, emphasizing statistical rates, sampling guarantees, and the transition from unconditional diffusion to conditional and controlled generation.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Diffusion models, a powerful and universal generative AI technology, have achieved tremendous success in computer vision, audio, reinforcement learning, and computational biology. In these applications, diffusion models provide flexible high-dimensional data modeling, and act as a sampler for generating new samples under active guidance towards task-desired properties. Despite the significant empirical success, theory of diffusion models is very limited, potentially slowing down principled methodological innovations for further harnessing and improving diffusion models. In this paper, we review emerging applications of diffusion models, understanding their sample generation under various controls. Next, we overview the existing theories of diffusion models, covering their statistical properties and sampling capabilities. We adopt a progressive routine, beginning with unconditional diffusion models and connecting to conditional counterparts. Further, we review a new avenue in high-dimensional structured optimization through conditional diffusion models, where searching for solutions is reformulated as a conditional sampling problem and solved by diffusion models. Lastly, we discuss future directions about diffusion models. The purpose of this paper is to provide a well-rounded theoretical exposure for stimulating forward-looking theories and methods of diffusion models.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

The field of artificial intelligence (AI) has been revolutionized by generative models, particularly large language models and diffusion models. Recognized as foundation models, they are trained on massive corpora of data and have opened up vibrant possibilities in machine learning research and applications. While large language models focus on generating coherent text based on context, diffusion models excel at modeling complex data distributions and generating diverse samples, both of which find widespread use across various domains.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

Diffusion models, inspired by thermodynamics modeling, have emerged in recent years with ground-breaking performance, surpassing the previous state-of-the-art, such as Generative Adversarial Networks (GANs) and Variational AutoEncoders (VAEs). Diffusion models are widely adopted in computer vision and audio generation tasks, and further utilized in text generation, sequential data modeling, reinforcement learning and control, as well as life-science. For a more comprehensive exposition of applications, we refer readers to survey papers.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

The celebrated performance of diffusion models is indispensable to numerous methodological innovations that significantly expand the scope and boost the functionality of diffusion models, enabling high-fidelity generation, efficient sampling, and flexible control of the sample generation. For example, extend diffusion models to discrete data generation, while the vanilla diffusion models target at continuous data. Meanwhile, there is an active line of research aiming to expedite the sample generation speed of diffusion models. Last but not the least, a recent surge of research focuses on fine-tuning diffusion models towards generating samples of desired properties, such as generating images with peculiar aesthetic qualities. These task-specific properties are often encoded as guidance to the diffusion model, consisting of conditioning and control signals to steer the sample generation. Notably, guidance allows for the creation of diverse and relevant content across a wide range of applications, which underscores the versatility and adaptability of diffusion models. We term diffusion models with guidance as conditional diffusion models.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

Despite the rapidly growing body of empirical advancements, theories of diffusion models fall far behind. Some recent theories view diffusion models as an unsupervised distribution learner and sampler, and thus establish their sampling convergence guarantees and statistical distribution learning guarantees. Such results offer invaluable theoretical insights into the efficiency and accuracy of diffusion models for modeling complex data, with a central focus on the unconditioned diffusion models in distribution estimation. This leaves a gap between theory and practice for conditional diffusion models. In specific, a theoretical foundation to support and motivate principled methodologies for guidance design and adapting diffusion models to task-specific needs is still lacking.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Introduction", "weight": 1.5} -->

This paper serves as a contemporary exposure to diffusion models for stimulating sophisticated and forward-looking study on them. We mainly focus on the following fundamental theoretical questions of diffusion models: Can diffusion models learn data distributions accurately and efficiently? If so, what is the sample complexity, especially for structured data?

<!-- chunk {"id": "body-0009", "role": "body", "section": "Introduction", "weight": 1.5} -->

Can conditional diffusion models generate distributions aligned to guidance? If so, how can we properly design the guidance and what is the sample complexity?

<!-- chunk {"id": "body-0010", "role": "body", "section": "Introduction", "weight": 1.5} -->

For a systematic study, we will first review how diffusion models work and their emerging applications. Then we provide an overview of the existing theoretical underpinnings pertinent to the questions above. Our ultimate goal is to demonstrate and harness the power of diffusion models, connecting to broad interdisciplinary areas of applied mathematics, statistics, computational biology, and operations research.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Paper Organization", "weight": 1.0} -->

The rest of the paper is organized as follows. In Section 2, we present a continuous-time description of diffusion models using stochastic differential equations. The advantage of the continuous-time point of view lies in the clean and systematic formulation, and the seamless application of discretization schemes to replicate practical implementations.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Paper Organization", "weight": 1.0} -->

In Section 3, we review emerging applications of diffusion models, especially in various controlled generation tasks, aiming to elucidate the conditional distributions that diffusion models attempt to capture. Then, in Section 3.4, we relate conditional generation to black-box optimization via gauging the quality of the generated samples under control by a reward function.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Paper Organization", "weight": 1.0} -->

In Section 4, we delve into theoretical preliminaries and review theories of diffusion models. Specifically, in Section 4.1, we discuss how to learn the score function. Section 4.2 provides approximation theories for understanding proper neural network architectures for learning the score and statistical sample complexities of estimating the score function. Section 4.3 then discusses statistical sample complexities of distribution estimation using diffusion models and sampling theories by viewing diffusion models as samplers.

<!-- chunk {"id": "body-0014", "role": "body", "section": "Paper Organization", "weight": 1.0} -->

In Section 5, we focus on conditional diffusion models, continuing a similar study in Section 4. We introduce learning methods of conditional score functions in Section 5.1, connecting them to unconditional score by a so-called "guidance" term. This also motivates fine-tuning methods for conditional diffusion models. Section 5.2 then summarizes unconditional score approximation, estimation, and distribution learning theories. Section 5.3 revisits the guidance in conditional score functions and establishes theoretical insights for the impact of guidance.

<!-- chunk {"id": "body-0015", "role": "body", "section": "Paper Organization", "weight": 1.0} -->

In Section 6, we review theories and methodologies of data-driven black-box optimization using conditional diffusion models. We highlight that diffusion models generate high-fidelity solutions to the optimization objective function, preserving data latent structures, and the quality of the solutions aligns with the optimal off-policy bandit. This opens up new possibilities for optimization in high-dimensional complex and structured spaces through diffusion models.

<!-- chunk {"id": "body-0016", "role": "body", "section": "Paper Organization", "weight": 1.0} -->

Lastly, in Section 7, we discuss future directions and connections of diffusion models to broad research areas.

<!-- chunk {"id": "body-0017", "role": "body", "section": "Diffusion Model Preliminaries", "weight": 1.0} -->

Roughly speaking, diffusion model consists of a forward process and a backward process. In the forward process, a clean sample from the data distribution is sequentially corrupted by Gaussian random noise, and in the infinite-time limit, the data distribution is transformed into pure noise. In the backward process, a denoising neural network is trained to sequentially remove the added noise distribution in data and restore new clean data distribution. The forward and backward processes are depicted in Figure 1.

<!-- chunk {"id": "body-0018", "role": "body", "section": "Diffusion Model Preliminaries", "weight": 1.0} -->

To fully decipher how diffusion models work, we describe the forward and backward processes in a continuous time limit and review how to implement the backward process. Next, we will introduce guidance to realize conditioning in controlled sample generation using conditional diffusion models.

<!-- chunk {"id": "body-0019", "role": "body", "section": "Forward and Backward Processes", "weight": 1.0} -->

The forward process in diffusion models progressively adds noise to the original data. Here we consider the Ornstein-Ulhenbeck process, which is described by the following Stochastic Differential Equation (SDE), where initial $X_{0} \sim P_{data}$ follows the data distribution, ${(W_{t})}_{t \geq 0}$ is a standard Wiener process, and $g{(t)}$ is a nondecreasing weighting function. We denote the marginal distribution of $X_{t}$ at time $t$ as $P_{t}$. After an infinitesimal time, the forward process shrinks the magnitude of data and corrupts data by Gaussian noise. More precisely, given $X_{0}$, the conditional distribution of $\left.

<!-- chunk {"id": "body-0020", "role": "body", "section": "Forward and Backward Processes", "weight": 1.0} -->

The value of $g{(t)}$ controls the noise corruption speed in the forward process. In real-world usage, various choices on $g{(t)}$ are implemented. One example is to choose $g{(t)}$ so that the variance of the Gaussian noise in the forward process increases linearly with respect to time. Later, several improvement techniques of $g{(t)}$ are proposed, such as a cosine-based variance schedule. To simplify our presentation, we take ${g{(t)}} = 1$ for all $t$ in the sequel.

<!-- chunk {"id": "body-0021", "role": "body", "section": "Forward and Backward Processes", "weight": 1.0} -->

The forward process will terminate at a sufficiently large time $T > 0$, where the corrupted marginal distribution $P_{T}$ is expected to be close to the standard Gaussian distribution. Then diffusion models generate fake data by reversing the time of, which leads to the following backward SDE, where ${{\nabla\log}p_{t}}{(\cdot)}$ is the so-called "score function", i.e., the gradient of the log probability density function of $P_{t}$, ${\overline{W}}_{t}$ is another Wiener process independent of $W_{t}$, and we use the superscript $\leftarrow$ for distinguishing with the forward process.

<!-- chunk {"id": "body-0022", "role": "body", "section": "Forward and Backward Processes", "weight": 1.0} -->

Under mild conditions, when initialized at $X_{0}^{\leftarrow} \sim P_{T}$, the backward process ${(X_{t}^{\leftarrow})}_{0 \leq t < T}$ has the same distribution as the forward process ${(X_{T - t})}_{0 \leq t < T}$.

<!-- chunk {"id": "body-0023", "role": "body", "section": "Forward and Backward Processes", "weight": 1.0} -->

Working, however, leads to difficulties, as both the score function ${\nabla\log}p_{t}$ and the distribution $P_{T}$ are unknown. Therefore, several surrogates are deployed in practice. Firstly, we replace the unknown distribution $P_{T}$ by the standard Gaussian distribution $\mathsf{N}{(0,I_{D})}$. Secondly, we denote $\hat{s}{(x,t)}$ as an estimator to the ground truth score function ${{\nabla\log}p_{t}}{(x)}$. The estimated score $\hat{s}$ is often parameterized by a deep neural network and takes data and time as inputs. Substituting $\hat{s}$ into the backward process, we obtain the following practical continuous-time backward SDE, Diffusion models then generate data by simulating a discretization of with a proper step size.

<!-- chunk {"id": "body-0024", "role": "body", "section": "Forward and Backward Processes", "weight": 1.0} -->

A common practice is to set the step size of order $\mathcal{O}{({1/1000})}$ so that the backward SDE is discretized to hundreds of steps.

<!-- chunk {"id": "body-0025", "role": "body", "section": "Forward and Backward Processes", "weight": 1.0} -->

It is worth mentioning that simulating the backward process for thousands of steps to generate a sample is time-consuming. Accelerating the sampling speed of diffusion models is an active research direction. Some notable methods include sampling with stride to reduce the backward steps, replacing the backward SDE with an ODE or DDIM (Denoising Diffusion Implicit Models), using a pre-trained VAE to extract low-dimensional data representations and then implementing diffusion processes -- known as latent diffusion, training distillation and consistency models, as well as rectified flows. These methods have found extensive adoption in highly fine-tuned diffusion models, such as Sora and Stable Diffusion.

<!-- chunk {"id": "body-0026", "role": "body", "section": "Conditional Diffusion Models", "weight": 1.0} -->

Conditional diffusion models generate samples analogous to the unconditioned one, while the major difference is the added conditional information. We denote the conditional information as $y$. Then the goal of conditional diffusion models is to generate samples from the conditional data distribution $P{(\cdot |y)}$. The conditional forward process is again an Ornstein-Ulhenbeck process: Note that the initial distribution is now a conditional distribution $P_{0}{(\cdot |y)}$, which is different from the unconditioned forward process. The noise corruption is only performed on $x$, while $y$ is kept fixed. We use the superscript $y$ to emphasize the dependence of the process on $y$. Similarly, for sample generation, the backward process reverses the time: Here ${{\nabla\log}p_{T - t}}{(\left. X_{t}^{y,\leftarrow} \middle| y \right.)}$ is the so-called "conditional score function", which replaces the score function.

<!-- chunk {"id": "body-0027", "role": "body", "section": "Conditional Diffusion Models", "weight": 1.0} -->

The initialization is identical to as $X_{0}^{y,\leftarrow} \sim {\mathsf{N}{(0,I_{D})}}$, independent of the guidance $y$. Despite the similarity in forward and backward processes, the major difference between conditional diffusion models and unconditioned ones lies in the estimation of the conditional score function $\nabla\log p_{t}{(\cdot |y)}$. In specific, the conditional score function can be related to the unconditioned one, which motivates a collection of practical learning and fine-tuning methods, e.g., classifier guidance and classifier-free guidance. We defer an in-depth discussion to Section 5.1.

<!-- chunk {"id": "body-0028", "role": "body", "section": "Conditional Diffusion Models", "weight": 1.0} -->

With an estimated conditional score function $\hat{s}{(x,y,t)}$ replacing the ground truth conditional score ${{\nabla\log}p_{t}}{(\left. x \middle| y \right.)}$, the conditional sample generation is to simulate the following backward process In practical implementations, a proper discretization scheme is applied.

<!-- chunk {"id": "body-0029", "role": "body", "section": "Emerging Applications of Diffusion Models", "weight": 1.0} -->

Through extensive developments, modern diffusion models have achieved a startling success and are implanted in various applications (see, for example, the survey ). We highlight vast applications of diffusion models in the following, with a particular emphasis on conditional diffusion models for controlled sample generation.

<!-- chunk {"id": "body-0030", "role": "body", "section": "Vision and Audio Generation", "weight": 1.0} -->

Diffusion models achieve state-of-the-art performance in image and audio generation tasks and are one of the fundamental building blocks of image and audio synthesis systems, such as DALL-E, stable diffusion, and Diffwave.

<!-- chunk {"id": "body-0031", "role": "body", "section": "Vision and Audio Generation", "weight": 1.0} -->

Diffusion models' performance is appraised of high-fidelity sample generation and allows versatile guidance to control the generation. The simplest example of generation under guidance is to generate images of certain categories, such as cats or dogs. Such categorical information is taken as a conditional signal and fed into conditional diffusion models. In more detail, we train conditional diffusion models using a labeled data set consisting of sample pairs $(x_{i},y_{i})$, where $y_{i}$ is the label of an image $x_{i}$. The training is to estimate a conditional score function using the data set, modeling the correspondence between $x$ and $y$. In this way, conditional diffusion models are learning the conditional distribution $P{({x = {\text{image}\left| y \right.} = \text{given~label}})}$ and allow sampling from the distribution.

<!-- chunk {"id": "body-0032", "role": "body", "section": "Vision and Audio Generation", "weight": 1.0} -->

In text-to-image synthesis systems, the conditional information is an input text prompt, which can be a sentence consisting of objects or more abstract requirements, e.g., aesthetic quality. To generate images aligned with prompts, conditional diffusion models are trained with a massive annotated data set encompassing image and text summary pairs denoted as $(x_{i},y_{i})$. The text $y_{i}$ will be transformed into a word embedding and taken as input to a conditional diffusion model. Similar to the generation of images in certain categories, conditional diffusion models for text-to-image synthesis learn the conditional distribution $P{({x = {\text{image}\left| y \right.} = \text{text~prompt}})}$ and allow sampling from it. In more sophisticated synthesis systems, some fine-tuning steps are implemented to further enable abstract prompt conditioning and improve the quality of generated images. For example, reformulates the discretized backward process as a finite-horizon Markov Decision Process (MDP).

<!-- chunk {"id": "body-0033", "role": "body", "section": "Vision and Audio Generation", "weight": 1.0} -->

The state space represents images, the conditional score function is viewed as a policy, and a reward function is defined to measure the alignment of an image to its desired text prompt. Therefore, to generate prompt-aligned images amounts to optimize reward via finding an optimal policy. proposes a policy gradient-based method for fine-tuning pre-trained diffusion models. In Figure 2, we demonstrate a progressive improvement from left to right of fine-tuning a conditional diffusion model using the method.

<!-- chunk {"id": "body-0034", "role": "body", "section": "Vision and Audio Generation", "weight": 1.0} -->

Conditional diffusion models are also a powerful tool in image editing and restoration, as well as audio enhancement; see also surveys and the references therein. To showcase the idea, we consider the image inpainting task as an example. The goal of inpainting is to predict missing pixels of an image. We denote the known region of an image as $y$ and the original full image as $x$. Then inpainting boils down to sampling $x$ from the conditional distribution $P{({x = {\text{full~image}\left| y \right.} = \text{known~region~of~the~image}})}$. In all these applications, conditional diffusion models are shown to be highly expressive and effective in modeling the conditional distributions.

<!-- chunk {"id": "body-0035", "role": "body", "section": "Control and Reinforcement Learning", "weight": 1.0} -->

Apart from primary computer vision and audio tasks, diffusion models are actively deployed in Reinforcement Learning (RL) and control problems with appealing performance. For example, utilize conditional diffusion models to parameterize control/RL policies in highly complicated tasks, e.g., robot control and human behavior imitation. An extended review of the connection between diffusion models and RL can be found. In RL/control problems, a policy is a conditional probabilistic distribution on the action space given the state of an underlying dynamical system. Accordingly, when using diffusion models to parameterize policies, the goal is to learn a distribution $P{({a = {\text{action}\left| y \right.} = \text{system~states}})}$. focus on the imitation learning scenario, where the goal is to mimic the behaviors of an expert. The data set contains expert demonstrations denoted by $(y_{i},a_{i})$ pairs. Here $y_{i}$ is the state of the system and $a_{i}$ is the expert's chosen action.

<!-- chunk {"id": "body-0036", "role": "body", "section": "Control and Reinforcement Learning", "weight": 1.0} -->

Analogous to text-to-image synthesis, we train a conditional score network using the data set to capture the dependency between states and actions. During inference, given a new system state, we use the learned conditional diffusion model to generate plausible actions. Diffusion-QL further adds regularization to the training of the conditional diffusion model and tries to learn optimal actions based on a pre-collected data set.

<!-- chunk {"id": "body-0037", "role": "body", "section": "Control and Reinforcement Learning", "weight": 1.0} -->

Diffusion models also embody a new realm for algorithm design in control and RL problems by viewing sequential decision making as generative sequence modeling. In a typical task of reward-maximization planning in RL, the goal is to find an optimal policy that achieves large accumulative rewards. Conventional methods rely on iteratively solving for the Bellman optimality to obtain a corresponding policy. Generative sequence modeling, however, directly produces state-action trajectories of large rewards, avoiding explicitly solving for Bellman optimality. In other words, generative sequence modeling directly samples from the conditional distribution $P{({\tau = {\text{state-action~trajectory}\left| {\tau\text{attains~large~rewar}} \right.}})}$. Early success was demonstrated with transformer generative models. Later, conditional diffusion models are deployed with state-of-the-art performance. Namely, Diffuser generates state-action trajectories conditioned on high reward as guidance via conditional diffusion models. Decision Diffuser presents conditional trajectory generation, taking reward, constraints, or skills as guidance and enhances Diffuser's performance.

<!-- chunk {"id": "body-0038", "role": "body", "section": "Control and Reinforcement Learning", "weight": 1.0} -->

For instance, given a pre-collected data set consisting of $(\tau_{i},y_{i})$, where $\tau_{i}$ is the state-action trajectory and $y_{i}$ is the accumulative reward of $\tau_{i}$. We use a conditional diffusion model to model the conditional distribution $P{(\left. \tau \middle| y \right.)}$, by estimating the conditional score function. After training, we specify a proper target reward value and deploy the conditional diffusion model to generate sample trajectories. A policy can then be extracted from the generated trajectories via an inverse dynamics model. See the working flow of the decision diffuser in Figure 3. AdaptDiffuser further introduces a discriminator for fine-tuning the conditional diffusion models, allowing self-evolution and adaptation to out-of-distribution tasks.

<!-- chunk {"id": "body-0039", "role": "body", "section": "Life-Science Applications", "weight": 1.0} -->

In life-science applications, conditional diffusion models are making ever profound impacts. See also a survey on applications of diffusion models in bioinformatics. These results cover diverse tasks including single-cell image analysis, protein design and generation, drug design, small molecule generation, etc. The performance surpasses many of their predecessors using autoregressive, VAE, or GAN-type deep generative models.

<!-- chunk {"id": "body-0040", "role": "body", "section": "Life-Science Applications", "weight": 1.0} -->

To demonstrate the use of conditional diffusion models, we take protein design as an example. Protein design can be posed as a problem of finding a sequence $w$ of certain length, where each coordinate of the sequence represents the structural information of the protein. A protein is only useful if it can be expressed in living cells. A widely adopted metric of usefulness is the likelihood of a protein sequence being a natural one. In addition, the binding affinity and aggregation tendency are also vital properties of the protein structure. Combined with the usefulness metric, all these properties can be summarized by a vector-valued function $f{(w)}$. In this sense, conditional diffusion models actually generate protein sequences $w$ following a conditional distribution $P{({\left. w \middle| {f{(w)}} \right. \in \mathcal{E}})}$, where $\mathcal{E}$ is a set describing plausible protein structures. The training of conditional diffusion models for protein generation is analogous to text-to-image diffusion models, based on a training data set containing diverse protein structures with measured properties.

<!-- chunk {"id": "body-0041", "role": "body", "section": "Life-Science Applications", "weight": 1.0} -->

In the inference stage, we can first sample one configuration from $\mathcal{E}$ and conditioned on the configuration, we generate new proteins.

<!-- chunk {"id": "body-0042", "role": "body", "section": "Black-Box Optimization", "weight": 1.0} -->

In control, RL, and life-science applications, various guidance may be summarized as an abstract reward function $V{( \cdot )}$. Then the goal is to generate new samples from a conditional distribution, aiming to optimize the reward. Consequently, conditional diffusion models act as an optimizer which generates optimal solutions.

<!-- chunk {"id": "body-0043", "role": "body", "section": "Black-Box Optimization", "weight": 1.0} -->

We revisit the example of offline reward-maximization planning in RL. Recall that our data set comprises state-action trajectories $\tau_{i}$ and the associated accumulative rewards $y_{i} = {{V{(\tau_{i})}} + \epsilon_{i}}$, where $\epsilon_{i}$ is an independent observation noise. Reward-maximization planning essentially seeks solutions to the black-box optimization problem $\operatorname{argmax}_{\tau}{V{(\tau)}}$. In this setting, we are prohibitive to interact with the target function $V$ beyond the given data set. Early existing works utilize GANs for optimal solution generation, yet suffer from training instability and mode collapse issues. Recently, empirically presents superior performance of generating high-quality solutions using conditional diffusion models. The idea is to transform the black-box optimization problem into a conditional sampling problem. In specific, given a proper target value $a$, conditional diffusion models generate solutions from the conditional distribution $P{({\left.

<!-- chunk {"id": "body-0044", "role": "body", "section": "Black-Box Optimization", "weight": 1.0} -->

\tau \middle| {V{(\tau)}} \right. = a})}$. The subtlety stems from how to properly choose the target value $a$ to ensure the high-quality of the generated solutions. Roughly speaking, we are luring to choose a large $a$ so that the generated solutions achieve large rewards. However, if we choose $a$ too large compared to the given data set, significant extrapolation is required to generate corresponding solutions, leading to potential quality degradation. Consequently, a proper choice on $a$ heavily depends on the coverage of the collected data set. provides theoretical guidelines on how to choose $a$ to ensure good generated solutions, which we will introduce in Section 6. Empirically, proposes several methods to encourage large-reward solutions during the training of the conditional diffusion model, such as sample reweighting --- assigning large weights to samples with large rewards.

<!-- chunk {"id": "body-0045", "role": "body", "section": "Theoretical Progress on Unconditional Diffusion Models", "weight": 1.0} -->

This section reviews recent progress in the theoretical understanding of diffusion models. We recall from Section 2 that the score function is the key to implementing a diffusion model. From a theoretical perspective, the performance of diffusion models is intimately tied to whether or not the score function can be learned accurately. For a systematic treatment, we first introduce methods for learning the score and then dive into their theoretical insights. Specifically, we discuss how to properly choose neural networks for learning the score function, based on the universal and adaptive approximation capability of neural networks. More importantly, we demonstrate structural properties in the score function induced by data distribution assumptions, e.g., low-dimensional support and graphical models. Then we provide statistical sample complexities for estimating the score using the chosen neural networks. We are particularly interested in understanding how score estimation circumvents the curse of dimensionality issues in high-dimensional settings. Lastly, we study statistical rates for estimating the data distribution.

<!-- chunk {"id": "body-0046", "role": "body", "section": "Learning Score Function", "weight": 1.0} -->

We consider the goal of learning the score function ${{\nabla\log}p_{t}}{(x_{t})}$ using neural networks. A naive objective function is the weighted quadratic loss: where $w{(t)}$ is a weighting function and $\mathcal{S}$ is a concept class (deep neural networks). However, such an objective function is not computable using samples, as the score function ${\nabla\log}p_{t}$ is unknown. As shown in the seminal works and, rather than minimizing the integral, we can minimize an equivalent objective function, Here, $\phi_{t}{(\left. x_{t} \middle| x_{0} \right.)}$ denotes the Gaussian transition kernel of the forward process, so that ${\nabla\log}\phi_{t}$ admits an analytical form By this analytical expression, we could approximate the objective using finite samples. Note that ${{\nabla_{x_{t}}\log}\phi_{t}}{(\left.

<!-- chunk {"id": "body-0047", "role": "body", "section": "Learning Score Function", "weight": 1.0} -->

x_{t} \middle| x_{0} \right.)}$ is the noise added to $x_{0}$ at time $t$. Therefore, is also known as the denoising score matching. As shown, denoising score matching can also be derived using a variational perspective, reproducing the evidence lower bound for regularized data negative likelihood minimization.

<!-- chunk {"id": "body-0048", "role": "body", "section": "Score Blowup and Early-Stopping", "weight": 1.0} -->

One challenge of optimizing is the score blowup issue. To demonstrate the phenomenon, we consider a data distribution which lies in a linear subspace, where $x = {Az}$ for a representation matrix $A \in {\mathbb{R}}^{D \times d}$ and a latent variable $z \in {\mathbb{R}}^{d}$. Here $D$ represents the ambient dimension of data and $d$ is the intrinsic dimension, which is often much smaller than $D$. As shown, the ground truth score ${{\nabla\log}p_{t}}{(x)}$ assumes the following orthogonal decomposition, where $p_{t}^{ld}$ is the marginal density function of applying the forward diffusion process on the latent variable $z$. As can be seen, the term $(\mathcal{T})$ is orthogonal to the subspace spanned by matrix $A$. More importantly, as $t$ approaches $0$, the magnitude of $(\mathcal{T})$ grows to infinity as long as $x \neq 0$.

<!-- chunk {"id": "body-0049", "role": "body", "section": "Score Blowup and Early-Stopping", "weight": 1.0} -->

The reason behind this is that $(\mathcal{T})$ enforces the orthogonal component to vanish so that the low-dimensional subspace structure is reproduced in generated samples. Such a blowup issue appears in all geometric data. As a consequence, an early stopping time $t_{0} > 0$ is introduced and the practical score estimation loss is written as For practical implementation, we approximate by its empirical version. Specifically, given $n$ i.i.d. data points $x_{i} \sim P_{data}$ for $i = {1,\ldots,n}$, we sample $x_{t}$ given $x_{0} = x_{i}$ from the Gaussian distribution $\mathsf{N}{({\alpha{(t)}x_{i}},{h{(t)}I_{D}})}$. We also sample time $t$ from the interval $\lbrack t_{0},T\rbrack$ to approximate the integration with respect to $t$.

<!-- chunk {"id": "body-0050", "role": "body", "section": "Remark 1 (Network class $\\mathcal{S}$)", "weight": 1.0} -->

A common choice of the network class $\mathcal{S}$ is the U-Net, as demonstrated in Figure 4. The network architecture utilizes convolution layers and shortcut connections. In the network, an input is first compressed into a low-dimensional representation and then gradually lifted back to the original dimension. This encoder-decoder type structure aims to extract intrinsic structures in data and leads to an efficient learning. More recently, using transformer-based score network has demonstrated outstanding performance, which excels in capturing spatial-temporal dependencies in data.

<!-- chunk {"id": "body-0051", "role": "body", "section": "Score Approximation and Estimation", "weight": 1.0} -->

The choice of concept class $\mathcal{S}$ is vital to the learning of the score function as. There are two requirements on $\mathcal{S}$: 1) Class $\mathcal{S}$ should be rich enough to well-approximate the ground truth score function, i.e., there exists a candidate in $\mathcal{S}$ close to ${\nabla\log}p_{t}$; 2) Class $\mathcal{S}$ should not be overly complicated to obscure the learning process with finite training samples. We present theoretical insights on both aspects, and address 1) from a function approximation perspective and 2) from a statistical learning perspective.

<!-- chunk {"id": "body-0052", "role": "body", "section": "Score Approximation Guarantees", "weight": 1.0} -->

The question underscores score approximation is what the size and the architecture of score networks to ensure the existence of an $\epsilon$-error approximation to the score function. Here $\epsilon > 0$ is the desired error level and often represents an $L^{2}$ distance measure. Such a question is reminiscent of the universal function approximation ability of neural networks. However, we highlight some fundamental differences between score approximation and conventional function approximation. Firstly, the score function is defined on all of the high-dimensional Euclidean space, due to the added Gaussian noise, while conventional neural network approximation theory focuses on compact domains. Secondly, the score function depends on an additional time dimension, which complicates its approximation.

<!-- chunk {"id": "body-0053", "role": "body", "section": "Score Approximation Guarantees", "weight": 1.0} -->

Concurrent works and tackle the challenges via very different approaches and develop score approximation theories for Euclidean data and low-dimensional linear subspace data. rewrites the score function as ${{\nabla\log}p_{t}} = \frac{\nabla p_{t}}{p_{t}}$ and uses neural networks to approximate $p_{t}$ and $\nabla p_{t}$ separately. To address the time dependency, proposes a series of "diffused basis functions". More formally, diffused basis functions are the convolutions of the Gaussian transition kernel in the forward process with time-independent polynomials, such as Taylor polynomials and B-splines. The idea behind the diffused basis functions can be understood as tracking the evolution of $p_{t}$ with respect to time $t$. Indeed, once we can approximate the density of the clean data distribution $P_{data}$ with time-independent polynomials, the corresponding diffused polynomials automatically approximate the density $p_{t}$ for all $t$.

<!-- chunk {"id": "body-0054", "role": "body", "section": "Score Approximation Guarantees", "weight": 1.0} -->

On the other hand, resorts to a local Taylor approximation of the score function using neural networks. In this case, the score function ${\nabla\log}p_{t}$ is viewed as a multi-dimensional input-output mapping of certain regularity. Built upon the existing universal approximation theories of neural networks, devises a score approximation result. More interestingly, considers low-dimensional linear subspace data and shows that the ground truth score ${\nabla\log}p_{t}$ decomposes into two terms as. In this regard, a simplified U-Net architecture (Figure 5) with linear encoder and decoder is constructed for efficient score approximation, indicating that the data subspace structures circumvent the dependence on data ambient dimension.

<!-- chunk {"id": "body-0055", "role": "body", "section": "Score Approximation Guarantees", "weight": 1.0} -->

In deriving the approximation guarantees, leverage sophisticated input truncation to deal with the unbounded domain. The approximation error is in turn measured in the $L^{2}$ norm sense, instead of commonly used $L^{\infty}$ norm. In order to achieve an $\epsilon$ approximation error, the network size scales in the order $\overset{\sim}{\mathcal{O}}{(\epsilon^{- \gamma})}$, where $\gamma$ is data dimension dependent. We emphasize that when there exists low-dimensional subspace structures in data, $\gamma$ only depends on the subspace dimension.

<!-- chunk {"id": "body-0056", "role": "body", "section": "Sample Complexity of Score Estimation", "weight": 1.0} -->

We shift to understand how many samples are needed to learn a score estimator by optimizing. The learned estimator should generalize in the sense that its deviation to the ground truth score is small. This requires more than a good score network class $\mathcal{S}$, but also the learnability within $\mathcal{S}$, which is characterized by some complexity measure of $\mathcal{S}$.

<!-- chunk {"id": "body-0057", "role": "body", "section": "Sample Complexity of Score Estimation", "weight": 1.0} -->

An early work provides a sample complexity bound for score estimation. Yet the bound depends on some unknown Rademacher complexity of the score network class. Built upon the score approximation theory, and establish score estimation theories from the nonparametric statistics point of view. assumes the clean data distribution is supported on a unit cube with a Besov continuous density. In order to obtain an $\epsilon$-accurate score estimator in the $L^{2}$ norm, the sample size grows in the order $\overset{\sim}{\mathcal{O}}{(\epsilon^{- \frac{D + {2\beta}}{\beta}})}$, where $D$ is the data dimension and $\beta$ is the smoothness index of the density. As can be seen, the sample complexity indicates the curse of dimensionality, and reduces the dependence on $D$ when data has a known linear subspace structure. In the independent study, focuses on linear subspace data without knowing the subspace in advance.

<!-- chunk {"id": "body-0058", "role": "body", "section": "Sample Complexity of Score Estimation", "weight": 1.0} -->

Under assumptions of data having Gaussian tail and the score being Lipschitz, establishes a $\overset{\sim}{\mathcal{O}}{(\epsilon^{- {({d + 5})}})}$ sample complexity, where $d$ is the subspace dimension. While free of the curse of dimensionality, also proves that the unknown subspace can be automatically estimated via score estimation. Turning towards a kernel-based approach, establish optimal statistical score estimation rates using a regularized Gaussian kernel density estimation method. The obtained sample complexity is $\overset{\sim}{\mathcal{O}}{(\epsilon^{- {({d + 4})}})}$ for Lipschitz continuous score functions.

<!-- chunk {"id": "body-0059", "role": "body", "section": "Optimization Guarantees on Score Estimation", "weight": 1.0} -->

On the algorithmic side, we are aware of studying score estimation in Gaussian mixture models. They provide convergence analysis of using gradient descent to minimize the score estimation loss. The algorithmic behavior can be characterized in two phases, where in the large-noise phase, i.e., time $t$ large, gradient descent is analogous to power iteration. In the the small-noise phase, i.e., $t$ small, gradient descent is akin to the EM algorithm. Besides, studies the optimization guarantee of using two-layer neural networks for score estimation.

<!-- chunk {"id": "body-0060", "role": "body", "section": "Score Estimation in Graphical Models", "weight": 1.0} -->

Besides considering data distributions in continuous spaces, such as Euclidean space and linear subspace, studies score approximation and estimation in graphical models. Graphical models such as Markov random fields and restricted Boltzmann machines have been widely used for modeling image distributions in the literature, yet they are fundamentally different from distributions on continuous variables. proposes a novel approach for controlling the sample complexity of score estimation in high dimensions. In particular, the authors view the neural networks in diffusion models as a denoising algorithm, enabling an efficient score approximation.

<!-- chunk {"id": "body-0061", "role": "body", "section": "Score Estimation in Graphical Models", "weight": 1.0} -->

Specifically, assumes the data distribution follows an Ising model ${P_{data}{(\sigma)}} \propto {\exp{\{{\langle\sigma,{A\sigma}\rangle}\}}}$ for $\sigma \in {\{{\pm 1}\}}^{D}$. Under certain high-temperature conditions of the matrix $A \in {\mathbb{R}}^{D \times D}$, the score function $s{(x_{t},t)}$ can be approximately computed by variational inference algorithms such as message passing. This is an iterative algorithm of the form $m^{\ell + 1} = {\tanh{({{{({A - K})}m^{\ell}} + {c_{t}x_{t}}})}}$ with $m^{0} = 0$ for certain matrix $K \in {\mathbb{R}}^{D \times D}$.

<!-- chunk {"id": "body-0062", "role": "body", "section": "Score Estimation in Graphical Models", "weight": 1.0} -->

Each step of the message-passing algorithm comprises simple operations, including matrix-vector multiplication and pointwise nonlinearity, which could be efficiently approximated by one block of the residual network $u^{\ell + 1} = {u^{\ell} + {W_{1}{ReLU}{({W_{2}u^{\ell}})}}}$. This renders an efficient approximation of Ising model score functions using a residual network with $\mathcal{O}{({D^{2}L})}$ parameters, where $L$ is the number of neural network layers, allowing a moderate dependence on the problem size. Incorporating standard Rademacher complexity generalization error bound, provides an estimation error bound without the exponential dependence on dimensionality.

<!-- chunk {"id": "body-0063", "role": "body", "section": "Sampling and Distribution Estimation", "weight": 1.0} -->

Our ultimate goal of diffusion models is to learn the data distribution and provide easy access to generating new samples. This section first reviews sampling theories of diffusion models via the backward process, with a basic assumption on the accuracy of the estimated score function $\hat{s}$. Next, we move to an end-to-end analysis of diffusion models, by presenting sample complexity bounds for learning distributions.

<!-- chunk {"id": "body-0064", "role": "body", "section": "Sampling Theory", "weight": 1.0} -->

Several recent sampling theories of diffusion models prove that the distribution generated by the backward process is close to the data distribution, as long as the score function is accurately estimated. The central contribution is a relationship between $\epsilon_{dis}$ and $\epsilon_{score}$, where $\epsilon_{dis}$ is a discrepency between the sampled data distribution and the ground truth distribution, and $\epsilon_{score}$ is the score estimation error. Specifically, establish upper bounds of $\epsilon_{dis}$ using $\epsilon_{score}$ for diffusion Schrödinger bridges. The error $\epsilon_{dis}$ is measured in the total variation distance and $\epsilon_{score}$ is measured in the $L^{\infty}$ norm. More concrete bounds of $\epsilon_{dis}$ are provided. These works specialize $\epsilon_{score}$ to be the $L^{2}$ error of the estimated score function, and $\epsilon_{dis}$ to be the total variation distance between the generated distribution and the data distribution.

<!-- chunk {"id": "body-0065", "role": "body", "section": "Sampling Theory", "weight": 1.0} -->

requires the data distribution satisfying a log-Sobolev inequality. Concurrent works and relax the log-Sobolev assumption on the data distribution to only having bounded moments. The upper bound in takes the form Here $T$ is the terminal time in the forward process. The discretization-error depends on the regularity of the data distribution and the step size in the discretized backward process. The forward-error quantifies the divergence between $P_{T}$ and $P_{\infty} = {\mathsf{N}{(0,I_{D})}}$, since the forward process is terminated as a finite time $T$. It is worth mentioning that allows $\epsilon_{score}$ to be time-dependent and improves the data dimension dependency. Recently, largely enrich the study of sampling theory using diffusion models. Specifically, novel analyses based on Taylor expansions of the discretized backward process or localization method are developed, which improve the upper bound on $\epsilon_{dis}$. Further, extends to DDIM sampling scheme and considers the probabilistic ODE backward sampling.

<!-- chunk {"id": "body-0066", "role": "body", "section": "Sampling Theory", "weight": 1.0} -->

Besides Euclidean data, makes the first attempt to analyze diffusion models for learning low-dimensional manifold data. Assuming $\epsilon_{score}$ is small under the $L^{\infty}$ norm (extension to the $L^{2}$ norm is also provided), bound $\epsilon_{dis}$ of diffusion models in terms of the Wasserstein distance. The obtained bound has an exponential dependence on the diameter of the data manifold. Moreover, considers using diffusion processes to sample from noisy observations of symmetric spiked models and studies polynomial-time algorithms for sampling from Gibbs distributions based on diffusion processes. The construction of diffusion processes in leverages the idea of stochastic localization.

<!-- chunk {"id": "body-0067", "role": "body", "section": "Computational efficiency of sampling through diffusion models", "weight": 1.0} -->

Sampling from certain high-dimensional distributions can be computationally challenging. For instance, demonstrates the hardness of sampling from the low-temperature Sherrington-Kirkpatrick model using any stable algorithms. An intriguing line of inquiry would be to understand the computational complexity of sampling through diffusion models and its connection to the complexity of sampling via the Langevin dynamics.

<!-- chunk {"id": "body-0068", "role": "body", "section": "Computational efficiency of sampling through diffusion models", "weight": 1.0} -->

Using heuristic physics methods, investigated the relationship between the computational complexity of sampling through the Langevin dynamics and diffusion models in high-dimensional distributions widely studied in the statistical physics of disordered systems. They utilized the hardness of computing the score function as a proxy for the hardness of sampling with diffusion models. They generated phase diagrams of the computational complexity of sampling from these high-dimensional models, and identified parameter regions where diffusion models are unable to sample efficiently, while the Langevin dynamics can; conversely, they also identified regions where the Langevin dynamics are inefficient, yet diffusion models perform well.

<!-- chunk {"id": "body-0069", "role": "body", "section": "Sample Complexity of Distribution Estimation", "weight": 1.0} -->

Distribution estimation theory of diffusion models is explored in and from an asymptotic statistics point of view. These results do not provide an explicit sample complexity bound. Given the aforementioned sampling theory and score estimation theory, we can develop an end-to-end analysis of diffusion models. The following theorem summarizes the existing sample complexity bounds of diffusion models in and.

<!-- chunk {"id": "body-0070", "role": "body", "section": "Alternative Formulation: Stochastic Localization", "weight": 1.0} -->

Stochastic localization is a measure-valued stochastic process employed to study isoperimetric inequalities. As a mathematical technique, stochastic localization has been successfully utilized in proving versions of the Kannan-Lovász-Simonovits (KLS) conjecture. The process was later generalized in as a sampling algorithm with provable sampling error bounds. The connections between stochastic localization and the DDPM (Denoising Diffusion Probabilistic Model) diffusion models are demonstrated.

<!-- chunk {"id": "body-0071", "role": "body", "section": "Alternative Formulation: Stochastic Localization", "weight": 1.0} -->

We introduce the simplest stochastic localization process, following the presentation. Given the measure $P_{data}$, the stochastic localization process is a stochastic differential equation defined as: where ${m_{t}{(y)}} = {{\mathbb{E}}_{{(x,g)} \sim {{P_{data} \otimes \mathsf{N}}{(0,I_{D})}}}{\lbrack{\left. x \middle| {{tx} + {\sqrt{t}g}} \right. = y}\rbrack}}$ is the posterior expectation of $Y_{t}$ upon observing $y = {{tx} + {\sqrt{t}g}}$.

<!-- chunk {"id": "body-0072", "role": "body", "section": "Alternative Formulation: Stochastic Localization", "weight": 1.0} -->

Standard theory implies that the marginal distribution of $Y_{t}$ satisfies $Y_{t}\overset{d}{=}{{tx} + {\sqrt{t}g}}$, where ${(x,g)} \sim {{P_{data} \otimes \mathsf{N}}{(0,I_{D})}}$. Consequently, $\lim_{t\rightarrow\infty}{Y_{t}/t}$ converges to a random variable following the distribution $P_{data}$. In generative modeling tasks, one could fit the posterior expectation $m_{t}{(y)}$ using neural networks and training samples, and discretize the SDE as in Eq., similar to DDPM diffusion models.

<!-- chunk {"id": "body-0073", "role": "body", "section": "Alternative Formulation: Stochastic Localization", "weight": 1.0} -->

In sampling tasks for the distribution $P_{data}$ being spin-glasses models and posterior of spiked matrix models, show that the posterior expectation $m_{t}$ can be approximately computed using variational inference algorithms in the high-temperature regime, enabling efficient sampling from these distributions.

<!-- chunk {"id": "body-0074", "role": "body", "section": "Alternative Formulation: Stochastic Localization", "weight": 1.0} -->

A firm connection between stochastic localization to DDPM diffusion models is shown: The stochastic localization process ${\{ Y_{t}\}}_{t \geq 0}$ as in Eq. is equivalent to the backward SDE of the diffusion model up to time and scale reparametrization. further generalizes the stochastic localization scheme to general stochastic processes.

<!-- chunk {"id": "body-0075", "role": "body", "section": "Theoretical Progress on Conditional Diffusion Models", "weight": 1.0} -->

Although conditional diffusion models share many characteristics with their unconditional counterpart, their unique reliance on guidance requires new understanding and insights. As a result, theoretical results on conditional diffusion models are highly limited. In this section, we mimic the study of unconditional diffusion models yet put an extra emphasis on distinct uses and methods of conditional diffusion models. We first introduce the training of conditional diffusion models, which is to estimate the conditional score function. Interestingly, the conditional score function can be related to the unconditional score function, motivating a fine-tuning perspective for training conditional diffusion models. Next, we present conditional score estimation and distribution estimation guarantees. The last section is devoted to theoretical insights on the influence of guidance in Gaussian mixture models, where we corroborate common observations and reveal curious new discoveries.

<!-- chunk {"id": "body-0076", "role": "body", "section": "Learning Conditional Score", "weight": 1.0} -->

For conditional sample generation via, the conditional score function ${{\nabla\log}p_{t}}{(\left. x \middle| y \right.)}$ needs to be estimated. We slightly abuse the notation to denote $s$ as a conditional score network and $\mathcal{S}$ as the corresponding network class. By introducing an early-stopping time $t_{0}$, a conceptual quadratic loss for conditional score estimation is defined as where $w{(t)}$ is a time dependent reweighting function. Inspired by and, \[176, Proposition 3.1\] asserts the equivalence of to the following implementable loss function, which shares the same spirit as.

<!-- chunk {"id": "body-0077", "role": "body", "section": "Classifier and Classifier-Free Guidance", "weight": 1.0} -->

Practical implementations of conditional score estimation, such as classifier and classifier-free guidance methods, build upon for reduced computational cost or better performance. We begin with the classifier guidance method, which is arguably the first method to allow conditional generation in diffusion models similar to GANs or flow models. Specifically, when conditional information $y$ is discrete, e.g., image categories, the conditional score ${{\nabla\log}p_{t}}{(\left. x_{t} \middle| y \right.)}$ is rewritten via Bayes' rule as where $c_{t}$ is the likelihood function of an external classifier. In other words, classifier guidance combines the unconditional score function with the gradient of an external classifier. The external classifier is trained using the diffused data points in the forward process. As a result, the performance of classifier guidance methods is sometimes limited, since it is difficult to train the external classifier with highly corrupted data.

<!-- chunk {"id": "body-0078", "role": "body", "section": "Classifier and Classifier-Free Guidance", "weight": 1.0} -->

Later, classifier-free guidance proposes to remove the external classifier, circumventing the limitation caused by classifier training. The idea of classifier-free guidance is to introduce a mask signal to randomly ignore $y$ and unifies the learning of conditional and unconditional scores. Specifically, let $\tau \in {\{\varnothing,{id}\}}$ be a mask signal, where $\varnothing$ means to ignore the conditional information $y$ and $id$ to keep $y$. Corresponding to the two circumstances, we have Note that coincides, and recall that $t_{0}$ is an early-stopping time. Combining the two cases, classifier-free guidance method minimizes the following loss function: Here $\tau$ is randomly chosen among $\varnothing$ and $id$ following distribution $P_{\tau}$. The simplistic choice on $P_{\tau}$ is a uniform distribution on $\{\varnothing,{id}\}$, while it is preferred to bias towards $\tau = {id}$ in some applications.

<!-- chunk {"id": "body-0079", "role": "body", "section": "Classifier and Classifier-Free Guidance", "weight": 1.0} -->

Once the estimator $\hat{s}$ is learned, we compute with some $\eta > 0$ for substitution into the backward process. From a theoretical point of view, choosing $\eta > 0$ is counter-intuitive, as the resulting $\overset{\sim}{s}$ does not correspond to the conditional score function ${{\nabla\log}p_{t}}{(\left. x \middle| y \right.)}$. However, a properly chosen $\eta$ leads to improved performance on benchmarks in practice. More interestingly, increasing $\eta$ reduces the diversity of the generated samples but promotes distinguishablity of them. The coefficient $\eta$ can also be chosen dependent on time $t$. Unfortunately, a principled guidance on how to choose $\eta$ is still missing, yet some theoretical insights on the impact of $\eta$ are developed; see also Section 5.3.

<!-- chunk {"id": "body-0080", "role": "body", "section": "Adapting Uncondtional Score via Guidance", "weight": 1.0} -->

In real use cases, the desired criteria or objectives of conditional sample generation may shift over time, which necessitates quick adaptation of conditional diffusion models. Although classifier-free guidance method has been adopted for training conditional diffusion models from scratch, it is not tailored for adapting or fine-tuning diffusion models owing to the computational overhead. Consequently, this opens up new possibilities of theories and methods for fine-tuning diffusion models without compromising the pre-training performance.

<!-- chunk {"id": "body-0081", "role": "body", "section": "Adapting Uncondtional Score via Guidance", "weight": 1.0} -->

Recently, propose efficient fine-tuning methods when the quality of generated samples is measured by a scalar-valued reward function. To guide a pre-trained model for generating high-reward samples, assumes the differentiability of the reward function and directly fine-tunes parameters in the diffusion model by back-propagation. formulate the sample generation process of diffusion models as a finite-horizon Markov decision process. The score function is equivalent to a policy and allows for fine-tuning using reinforcement learning techniques, such as policy gradient methods.

<!-- chunk {"id": "body-0082", "role": "body", "section": "Adapting Uncondtional Score via Guidance", "weight": 1.0} -->

A more interesting and principled fine-tuning method draws motivation from the classifier guidance. We revisit the Bayes' rule for conditional score function, where the classifier $c_{t}$ acts as guidance to adapting the pre-trained score. Despite classifier guidance requires a discrete label $y$ (yet can be multi-dimensional), the decomposition in the last display has a profound impact on guidance-based fine-tuning. Indeed, extend guidance to arbitrary conditioning by incorporating gradients of a proper scalar-valued function. For demonstration, defines the so-call "universal guidance" in the form of ${\nabla_{x_{t}}\ell}{(y,{f{({\hat{x}}_{0})}})}$, where $f$ is a function measuring the quality of samples, ${\hat{x}}_{0}$ is the anticipated generated sample of the pre-trained diffusion model given current point $x_{t}$ in the backward process, and $\ell$ is a loss function.

<!-- chunk {"id": "body-0083", "role": "body", "section": "Adapting Uncondtional Score via Guidance", "weight": 1.0} -->

Note that ${\hat{x}}_{0}$ correlates with $x_{t}$ and the gradient is nontrivial. As a special example, when $y$ is the discrete label, $f$ is the classification likelihood, and $\ell$ is the cross-entropy loss, universal guidance reproduces classifier guidance.

<!-- chunk {"id": "body-0084", "role": "body", "section": "Conditional Score and Distribution Estimation", "weight": 1.0} -->

Theory of conditional score estimation and conditional distribution estimation is very limited. To the best of our knowledge, provides an initial study of using for conditional score estimation and distribution estimation. A systematic analysis of classifier-free guidance method is presented, with results highlighted by approximation theories of conditional score functions and sample complexities of conditional score estimation and distribution learning. In addition, shows the utility of the developed statistical theory in elucidating the performance of conditional diffusion models for diverse applications, including model-based transition kernel estimation in reinforcement learning, solving inverse problems, and reward conditioned sample generation.

<!-- chunk {"id": "body-0085", "role": "body", "section": "Conditional Score and Distribution Estimation", "weight": 1.0} -->

The core contribution of is the conditional score approximation theory, which is motivated by the idea of diffused basis approximation. In more detail, substantially broadens the framework to unbounded data domains and conditional distributions. The authors rewrite the conditional score function as ${{{\nabla\log}p_{t}}{(\left. x \middle| y \right.)}} = \frac{{\nabla p_{t}}{(\left. x \middle| y \right.)}}{p_{t}{(\left. x \middle| y \right.)}}$ and approximate ${\nabla p_{t}}{(\left. x \middle| y \right.)}$ and $p_{t}{(\left. x \middle| y \right.)}$ separately. On a technical side, the unbounded data domain and the conditioning on $y$ lead to new challenges. More importantly, however, lifts the technical conditions on data distributions in and obtains optimal statistical rates with a mild bounded Hölder norm assumption.

<!-- chunk {"id": "body-0086", "role": "body", "section": "Conditional Score and Distribution Estimation", "weight": 1.0} -->

We remark that takes the condition $y$ as independent input variables, leaving an open direction to identify intrinsic smoothness with respect to $y$ in the conditional distribution so as to improve the dimension dependency.

<!-- chunk {"id": "body-0087", "role": "body", "section": "Theoretical Insights on Strength of Guidance", "weight": 1.0} -->

We conclude the discussion on conditional diffusion models by a recent work on the influence of the strength of guidance. We are referring back to and studying the influence of $\eta$ on the sample generation. The same strength parameter can be introduced into classifier guidance as Hence, we will not distinguish different guidance methods, and term $\eta$ as the strength of guidance.

<!-- chunk {"id": "body-0088", "role": "body", "section": "Theoretical Insights on Strength of Guidance", "weight": 1.0} -->

A common observation of the consequence yielded by $\eta$ is best illustrated in Figure 6 on a three-component Gaussian mixture model. Here label $y$ indicates the Gaussian components and $x$ is a two-dimensional variable. When generating new samples, we fix a choice on $y$ to obtain within component samples. We observe that with an increased guidance strength $\eta$, the generated conditional distribution shifts its probability mass farther away from other components, and most of the mass becomes concentrated in smaller regions.

<!-- chunk {"id": "body-0089", "role": "body", "section": "Theoretical Insights on Strength of Guidance", "weight": 1.0} -->

The results in theoretically characterize the influence of strength on diffusion models in the context of Gaussian mixture models. Under mild conditions, proves that incorporating strong guidance not only boosts classification confidence but also diminishes distribution diversity, leading to a reduction in the differential entropy of the generated conditional distribution. These theories align closely with empirical observations.

<!-- chunk {"id": "body-0090", "role": "body", "section": "Theoretical Insights on Strength of Guidance", "weight": 1.0} -->

On the other hand, identifies a possible negative impact of large $\eta$ under discretized backward sampling in Gaussian mixture models, as depicted in Figure 7. There exists a phase shift as strength $\eta$ increases. Under large $\eta$, the center component of the original Gaussian mixture model splits into two symmetric clusters, harming the modality of the original data. The emergence of this negative effect is tied to the locations of the components and the discretization step size in the backward sampling process. Until this point, we are not aware of principled methods for tuning the strength $\eta$ in different tasks, which might be encouraged by the obtained theoretical insights.

<!-- chunk {"id": "body-0091", "role": "body", "section": "Diffusion Model for Optimization", "weight": 1.0} -->

This section introduces a novel avenue for optimization in high-dimensional complex and structured spaces through diffusion models. We focus on data-driven black-box optimization, where the goal is to generate new solutions that optimize an unknown objective function. Black-box optimization, also known as model-based optimization in machine learning, encapsulates various application domains such as reinforcement learning, computational biology and business management.

<!-- chunk {"id": "body-0092", "role": "body", "section": "Diffusion Model for Optimization", "weight": 1.0} -->

Solving data-driven black-box optimization differentiates from conventional optimization, as interactions with the objective function beyond a pre-collected data set are prohibitive, diminishing the possibility of sequentially searching for optimal solutions. Instead, people aim to extract pertinent information from the pre-collected data set and directly recommend solutions. To complicate matters, the solution space is often high-dimensional with rich latent structures. For example, in drug discovery, molecule structures need to satisfy global and local regularity to be expressive in living bodies. This poses a critical requirement for solving data-driven black-box optimization: we need to capture data latent structures to avoid suggesting unrealistic solutions that deviate severely from the original data domain.

<!-- chunk {"id": "body-0093", "role": "body", "section": "Diffusion Model for Optimization", "weight": 1.0} -->

To address the challenges, formulates data-driven black-box optimization as sampling from a conditional distribution, as demonstrated in Figure 8. The objective function value is the conditioning in the conditional distribution, meanwhile the distribution implicitly captures data latent structures.

<!-- chunk {"id": "body-0094", "role": "body", "section": "Diffusion Model for Optimization", "weight": 1.0} -->

The pre-collected data set in consists of two parts: 1) a massive unlabeled part $\mathcal{D}_{unlabel}$ and 2) a smaller labeled part $\mathcal{D}_{label}$. By terming the objective function as a reward function, considers two types of label feedback in $\mathcal{D}_{label}$: (Real-valued reward) The data set $\mathcal{D}_{label}$ consists of data and reward pairs, where the reward is a real-valued noise-perturbed version of the underlying ground truth reward; (Human preference) The data set $\mathcal{D}_{label}$ consists of triples taking two comparable data points and a binary preference label. The preference label indicates that the corresponding data point is likely to have an edge in the underlying reward over the other one.

<!-- chunk {"id": "body-0095", "role": "body", "section": "Diffusion Model for Optimization", "weight": 1.0} -->

Moreover, the data point $x \in {\mathbb{R}}^{D}$ is assumed to concentrate on a linear subspace, i.e., $x = {Az}$ for some unknown matrix $A \in {\mathbb{R}}^{D \times d}$, with $z \in {\mathbb{R}}^{d}$ being the latent variable. Therefore, newly generated samples should be kept close to the subspace to maintain high fidelity.

<!-- chunk {"id": "body-0096", "role": "body", "section": "Diffusion Model for Optimization", "weight": 1.0} -->

A semi-supervised learning algorithm is proposed in Figure 9. There are two training procedures: one in the first step for estimating the reward function and the other one in the third step for training the conditional diffusion model. In the fourth step, the target reward is set at a scalar value $a$, so that the generated samples follow the conditional distribution ${\hat{P}}_{a} = \hat{P}{( \cdot |\hat{\text{reward}} = a)}$, where $\hat{P}$ and $\hat{\text{reward}}$ emphasize that the distribution and the reward are estimated, rather than the ground truth. One may be curious about the quality of the generated samples. In particular, these two properties of the generated samples are of particular interest: 1) the reward levels of new samples and 2) their level of fidelity -- how much do new samples deviate from the latent subspace.

<!-- chunk {"id": "body-0097", "role": "body", "section": "Diffusion Model for Optimization", "weight": 1.0} -->

The results in provide a positive statistical answer. For the reward levels of new samples, defines to measure the gap between the sample average reward and the target reward. In the language of bandit learning, SubOpt can be interpreted as a form of off-policy sub-optimality. The following theorem proves an upper bound on SubOpt.

<!-- chunk {"id": "body-0098", "role": "body", "section": "Future Directions", "weight": 1.0} -->

We discuss several future directions of diffusion models, exploring their connections to stochastic control and distributional robustness; we also introduce discrete diffusion models.

<!-- chunk {"id": "body-0099", "role": "body", "section": "Connection to Stochastic Control", "weight": 1.0} -->

In either unconditioned diffusion models or conditional diffusion models, generating samples using backward processes or can be viewed as a stochastic control problem. The goal of stochastic control is to design the evolution of the controlled variable, so that certain cost is minimized. In diffusion models, the score function constitutes the control and steers the quality of the generated samples. In the simplest form of unconditioned diffusion models, we define the cost to be the distribution divergence between the generated distribution and the data distribution, such as the total variation distance and the Wasserstein distance. Then the score estimation essentially amounts to finding the optimal control for minimizing such costs.

<!-- chunk {"id": "body-0100", "role": "body", "section": "Connection to Stochastic Control", "weight": 1.0} -->

When using conditional diffusion models for black-box optimization, the cost is the negative of a reward function and the conditional score function is the control. The theory in chooses a proper target reward to design the control for optimizing the cost. Leveraging this control perspective, a series of empirical results attempt to fine-tune diffusion models by designing the control based on various cost forms. For instance, consider differentiable real-valued reward, while focus on the cost being human preferences. In terms of methodology, uses the policy gradient method in reinforcement learning for fine-tuning the control (conditional score function). resorts to the classifier guidance formula by directly augmenting the unconditioned score function by gradients of the cost.

<!-- chunk {"id": "body-0101", "role": "body", "section": "Connection to Stochastic Control", "weight": 1.0} -->

In this regard, principled methodologies and accompanying theories can be motivated from the stochastic control perspective, improving and analyzing diffusion models under various task objectives.

<!-- chunk {"id": "body-0102", "role": "body", "section": "Adversarial Robustness and Distributionally Robust Optimization", "weight": 1.0} -->

Diffusion models exhibit the natural denoising property in the backward processes, which are leveraged for adversarial purification and promoting robustness. To illustrate, in robust classification, a two-step classification procedure is proposed: A trained conditional diffusion model is first deployed to generate new samples given the input adversarial examples for multiple times, hoping to purify the added noise in the input sample. Then the generated samples are fed into a trained classifier to produce a predicted label. Due to the randomness in the diffusion models, multiple transformed samples of the same input adversarial example can be obtained. Therefore, a majority vote among the predicted labels is assigned as the label of the adversarial example. This method is motivated by a justification on the promotion of robustness using diffusion models and empirically shown to be effective. Yet an end-to-end analysis is still missing.

<!-- chunk {"id": "body-0103", "role": "body", "section": "Adversarial Robustness and Distributionally Robust Optimization", "weight": 1.0} -->

We also expect a close connection between diffusion models to Distributionally Robust Optimization (DRO). As shown in Theorem 1. ‣ 4.3.2 Sample Complexity of Distribution Estimation ‣ 4.3 Sampling and Distribution Estimation ‣ 4 Theoretical Progress on Unconditional Diffusion Models ‣ An Overview of Diffusion Models: Applications, Guided Generation, Statistical Rates and OptimizationEmails: {minshuochen, jqfan, mengdiw}@princeton.edu, songmei@berkeley.edu"), diffusion models generate samples in the close vicinity of a target distribution, which can be viewed as providing a certain coverage of the distributional uncertainty set in DRO. In this sense, diffusion models can potentially simulate the worst-case scenario in the uncertainty set. We suspect the emergence of innovative methods and theories in the corresponding intersection area, where motivating attempts have been made.

<!-- chunk {"id": "body-0104", "role": "body", "section": "Discrete Diffusion Models", "weight": 1.0} -->

Discrete diffusion models, analogous to the previous continuous counterparts, are designed to keep the finite data support during the forward and backward processes. Instead of using continuous Gaussian noise to corrupt clean data, discrete diffusion resorts to continuous-time Markov processes for transforming clean data. The discrete nature has appealing alignment to real data characterized by a massive but finite support, e.g., natural language represented by word tokens and molecular structures. As reported, discrete diffusion achieves competitive or better performance in language tasks with comparable sized models. demonstrates the possibility of using discrete diffusion for solving combinatorial problems.

<!-- chunk {"id": "body-0105", "role": "body", "section": "Discrete Diffusion Models", "weight": 1.0} -->

We describe a discrete distribution by a probability vector $p_{data}$ belonging to the simplex. Analogous to Gaussian noise corruption for continuous diffusion, we utilize a continuous-time Markov process driven by a time-dependent transition matrix $Q_{t}$, i.e., The process above is known as the forward discrete diffusion process. Several design choices of $Q_{t}$ are summarized, including discretized Gaussian, uniform, and absorbing transitions.

<!-- chunk {"id": "body-0106", "role": "body", "section": "Discrete Diffusion Models", "weight": 1.0} -->

The discrete forward process also asserts a time reversal: Here ${\overline{Q}}_{t}$ is the backward transition matrix and ${\lbrack \cdot \rbrack}_{i}$ (or ${\lbrack \cdot \rbrack}_{ij}$) denotes the $i$-th (or $(i,j)$-th) entry. We observe from the backward process that to generate new samples, we only need to estimate the ratios $\frac{{\lbrack p_{t}\rbrack}_{i}}{{\lbrack p_{t}\rbrack}_{j}}$ for $t \in {\lbrack 0,T\rbrack}$. We can view this probability ratio as an analogy to the score function in the continuous distribution. Some caveats arise that estimating the ratios suffers from the massive support size of the data distribution and the magnitude of ratios can vary significantly. It is also likely that a large fraction of the ratios are zero or approximately zero, inducing sparse structures.

<!-- chunk {"id": "body-0107", "role": "body", "section": "Discrete Diffusion Models", "weight": 1.0} -->

There are different empirical methods for estimating the ratios, such as using a quadratic loss or an entropy loss.

<!-- chunk {"id": "body-0108", "role": "body", "section": "Discrete Diffusion Models", "weight": 1.0} -->

From a theoretical stand of point, discrete diffusion poses interesting open questions: How to efficiently estimate the ratios using finite samples, with potential sparse structures and ill-spread ranges of ratios. More importantly, how to smartly design principled transition kernels relevant to data distributions remains unclear. Nonetheless, assuming access to estimated ratios, proves the first sampling theory of discrete diffusion models.

<!-- chunk {"id": "body-0109", "role": "body", "section": "Conclusion", "weight": 1.5} -->

In this paper, we have surveyed how diffusion models generate samples, their wide applications, and existing theoretical underpinnings of them. We have adopted a continuous-time description of the forward and backward processes in diffusion models and discussed their training procedure, especially when there exists guidance to steer the sample generation. We have started with an exposure to theories of unconditional diffusion models, covering its score approximation, statistical estimation, and sampling theories. Built upon the insights from the unconditional diffusion models, we have then turned towards conditional diffusion models, with a focus on their unique design properties and theories. Next, we have made a connection between generative diffusion models to black-box optimization, paving a new avenue for high-dimensional optimization problems. Lastly, we have discussed several trending future directions.
