<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Universal Sequence Preconditioning

Topics include Regret bounds, Neural networks, Recurrent neural networks, Universal sequence preconditioning.

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

We study the problem of preconditioning in sequential prediction. From the theoretical lens of linear dynamical systems, we show that convolving the target sequence corresponds to applying a polynomial to the hidden transition matrix. Building on this insight, we propose a universal preconditioning method that convolves the target with coefficients from orthogonal polynomials such as Chebyshev or Legendre. We prove that this approach reduces regret for two distinct prediction algorithms and yields the first ever sublinear and hidden-dimension-independent regret bounds (up to logarithmic factors) that hold for systems with marginally table and asymmetric transition matrices. Finally, extensive synthetic and real-world experiments show that this simple preconditioning strategy improves the performance of a diverse range of algorithms, including recurrent neural networks, and generalizes to signals beyond linear dynamical systems.

<!-- chunk {"id": "body-0003", "role": "body", "section": "Introduction", "weight": 1.5} -->

In sequence prediction the goal of the learner is to predict the next token accurately according to a specified loss function, such as the mean square error or cross-entropy. This fundamental problem in machine learning has gained increased importance with the rise of large language models, which perform sequence prediction on tokens using cross entropy. The focus of this paper is preconditioning, i.e. modifying the target sequence to make it easier to learn. A classic example is differencing, introduced by Box and Jenkins in the 1970s Box and Jenkins, which transforms observations $\mathbf{y}_{1},\mathbf{y}_{2},\ldots$ into successive differences,

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

It is widely acknowledged that learning this sequence can be "easier\" than learning the original sequence for a large number of modalities. In this work we seek a more general framework for sequence preconditioning that captures the same intuition behind differencing and extends it to a broader class of transformations. The question we ask is

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

What is the general form of sequence preconditioning that enables provably accurate learning?

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

We address this question by introducing a preconditioning method which takes in $n$ fixed coefficients $c_{0},\ldots,c_{n}$ and converts the sequence of observations $\mathbf{y}_{1},\ldots,\mathbf{y}_{t},\ldots$ to the sequence of convolved observations^11^1This recovers differencing when $n = 2$, $c_{0} = 1$, and $c_{1} = {- 1}$.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

From an information-theoretic perspective, approaches of this kind seem futile---predicting $\mathbf{y}_{t}$ or $\sum_{i}{c_{i}\mathbf{y}_{t - i}}$ seems equally hard in an adversarial setting. Yet we show that when the data arises from a linear dynamical system (LDS), there exists a *universal* form of preconditioning that provably improves learnability, independent of the specific system. In the LDS setting, we show that preconditioning significantly strengthens existing prediction methods, leading to new regret bounds. Here, preconditioning has an elegant effect: the preconditioning filter forms coefficients of an $n$ degree polynomial, and the hidden system transition matrix is evaluated on this polynomial-- potentially shrinking the domain. In this setting, shrinking the learnable domain is akin to making the problem "easier to learn", a relationship that is formalized by Hazan and Singh. This allows us to prove the first dimension-independent sublinear regret bounds for asymmetric linear dynamical systems that are marginally stable.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Our results", "weight": 1.0} -->

Our main contribution is *Universal Sequence Preconditioning*, a novel method of sequence preconditioning which convolves the target sequence with the coefficients of the $n$-th monic Chebyshev polynomial. We give a more general form of preconditioning, allowing arbitrary user-specified coefficients, in Algorithm and an online version in Algorithm (Appendix C). We analyze the effect of Universal Sequence Preconditioning on two canonical sequence prediction algorithms in the online setting: convex regression and spectral filtering. In either case, the results are impressive-- yielding the first known sublinear regret bounds as compared to the optimal ground-truth predictor that are simultaneously applicable to marginally stable systems, independent of the hidden dimension (up to logarithmic factors), and applicable to systems whose transition matrix is asymmetric^22^2Our results only hold for asymmetric matrices whose eigenvalues have imaginary component bounded above by $O{({1/{\log{(T)}}})}$. This is somewhat tight, see Section B..

<!-- chunk {"id": "body-0009", "role": "body", "section": "Our results", "weight": 1.0} -->

2: Input: training data (u1: T1: N,y1: T1: N) where (uti,yti) is the t-th input/output pair in the i-th sequence; coefficients c0: n; prediction algorithm 𝒜. 5: y1: Tpreconditioned, i ← convolution (y1: Ti,c0: n) ⊲ $\mathbf{y}_{t}^{\text{preconditioned},i} = {\mathbf{y}_{t}^{i} + {\sum_{j = 1}^{n}{c_{j}\mathbf{y}_{t - j}^{i}}}}$
7: Train 𝒜 on preconditioned data (u1: T1: N,y1: Tpreconditioned, 1: N).

<!-- chunk {"id": "body-0010", "role": "body", "section": "Our results", "weight": 1.0} -->

First, applying USP to standard convex regression results in regret $\overset{\sim}{O}{(T^{- {2/13}})}$, which holds simultaneously across the three settings above and remains dimension-independent. For comparison, a naive analysis of regression yields a vacuous regret bound of $O{(T^{5/2})}$ on marginally stable systems. Second, combining USP with a variant of *spectral filtering* Hazan et al. that uses novel filters, the algorithm is able learn a broader class of linear dynamical systems-- in particular systems whose hidden transition matrix may be asymmetric. The enhanced method achieves regret $\overset{\sim}{O}{(T^{- {3/13}})}$, the best known rate under the joint conditions of - discussed above: marginal stability, dimension independence, and asymmetry. Both results require that the transition matrix eigenvalues have imaginary parts bounded by $O{({1/{\log T}})}$---a near-tight condition for achieving dimension-free regret. Further discussion on this appears in Appendix B.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Our results", "weight": 1.0} -->

Empirical results in Section demonstrate that USP consistently improves performance across diverse algorithms---including regression, spectral filtering, and neural networks---and across data types extending beyond linear dynamical systems.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Intuition for Universal Sequence Preconditioning", "weight": 1.0} -->

We now give some brief intuition for the result. Linear dynamical systems (LDS) are perhaps the most basic and well studied dynamical systems in engineering and control science. Given input vectors ${\mathbf{u}_{1},\ldots,\mathbf{u}_{T}} \in {\mathbb{C}}^{d_{\text{in}}}$, the system generates a sequence of output vectors ${\mathbf{y}_{1},{\ldots\mathbf{y}_{T}}} \in {\mathbb{C}}^{d_{\text{out}}}$ according to the law

<!-- chunk {"id": "body-0013", "role": "body", "section": "Intuition for Universal Sequence Preconditioning", "weight": 1.0} -->

where ${\mathbf{x}_{0},\ldots,\mathbf{x}_{T}} \in {\mathbb{C}}^{d_{\text{hidden}}}$ is a sequence of hidden states and $(\mathbf{A},\mathbf{B},\mathbf{C},\mathbf{D})$ are matrices which parameterize the LDS. We assume w.l.o.g. that $\mathbf{D} = 0$. We can factor out the hidden state $\mathbf{x}_{t}$ so that the observation at time $t$ is

<!-- chunk {"id": "body-0014", "role": "body", "section": "Intuition for Universal Sequence Preconditioning", "weight": 1.0} -->

Consider a "preconditioned" target at time $t$ to be a linear combination of $\mathbf{y}_{t:{t - n}}$ with coefficients $c_{0:n}$. A key insight is the following identity,

<!-- chunk {"id": "body-0015", "role": "body", "section": "Intuition for Universal Sequence Preconditioning", "weight": 1.0} -->

If we take $c_{0} = 1$ (i.e. a monic polynomial), we can re-write $\mathbf{y}_{t}$ as

<!-- chunk {"id": "body-0016", "role": "body", "section": "Intuition for Universal Sequence Preconditioning", "weight": 1.0} -->

The universal preconditioning term: it depends only on the coefficients $c_{0:n}$and not on any learning algorithm.

<!-- chunk {"id": "body-0017", "role": "body", "section": "Intuition for Universal Sequence Preconditioning", "weight": 1.0} -->

A term learnable via convex relaxation and regression, for example by denoting

<!-- chunk {"id": "body-0018", "role": "body", "section": "Intuition for Universal Sequence Preconditioning", "weight": 1.0} -->

The diameter of the coefficient $\mathbf{Q}_{s}$ depends on the magnitude of the coefficients $c_{0:n}$.

<!-- chunk {"id": "body-0019", "role": "body", "section": "Intuition for Universal Sequence Preconditioning", "weight": 1.0} -->

The residual term with polynomial $p_{n}^{c}{(\mathbf{A})}$. By a careful choice of coefficients $c_{0:n}$, we can force this term to be very small.

<!-- chunk {"id": "body-0020", "role": "body", "section": "Intuition for Universal Sequence Preconditioning", "weight": 1.0} -->

The main insight we derive from this expression is the inherent tension between two terms $\aleph_{1},\aleph_{2}$.

<!-- chunk {"id": "body-0021", "role": "body", "section": "Intuition for Universal Sequence Preconditioning", "weight": 1.0} -->

The preconditioning coefficients grow larger with the degree $n$ of the polynomial and the magnitude of the coefficients $c_{i}$. A higher degree polynomial and larger coefficients increase the diameter of the search space over the preconditioning coefficients, and therefore increase the regret bound stemming from the $\aleph_{1}$ component learning.

<!-- chunk {"id": "body-0022", "role": "body", "section": "Intuition for Universal Sequence Preconditioning", "weight": 1.0} -->

On the other hand, a larger search space can allow a broader class of polynomials $p_{n}{( \cdot )}$ which can better control of the magnitude of $p_{n}{(\mathbf{A})}$, and therefore reduce the search space of the $\aleph_{2}$ component.

<!-- chunk {"id": "body-0023", "role": "body", "section": "Intuition for Universal Sequence Preconditioning", "weight": 1.0} -->

What choice of polynomial is best? This work considers the Chebyshev polynomial.

<!-- chunk {"id": "body-0024", "role": "body", "section": "Intuition for Universal Sequence Preconditioning", "weight": 1.0} -->

As an example, consider any LDS whose hidden transition matrix $\mathbf{A}$ is diagonalizable and has eigenvalues in $\lbrack{- 1},1\rbrack$^33^3This work considers a broader class of hidden transition matrices.. By the above property, observe that ${\|{p_{n}{(\mathbf{A})}}\|}_{\infty} \leq {2 \cdot 2^{- n}}$, therefore shrinking the $\aleph_{2}$ term at a rate exponential with the number of preconditioning coefficients. We pause to remark on the *universality* of this choice of polynomial. Indeed, one could instead have chosen the preconditioning coefficients to depend on $\mathbf{A}$ so that $p_{n}^{\mathbf{c}}{( \cdot )}$ is the characteristic polynomial of $\mathbf{A}$.

<!-- chunk {"id": "body-0025", "role": "body", "section": "Intuition for Universal Sequence Preconditioning", "weight": 1.0} -->

By the Cayley-Hamilton theorem, ${p_{n}{(\mathbf{A})}} = 0$. This means that $\aleph_{2}$ term is canceled out completely. However this would have required knowledge of the spectrum of $\mathbf{A}$. The Chebyshev polynomial, on the other hand, is agnostic to the particular hidden transition matrix. Moreover, even if the spectrum of $\mathbf{A}$ were known, choosing the preconditioning coefficients to form the characteristic polynomial would result in an algorithm which must learn hidden dimension many parameters, which is prohibitive. Instead, the degree of the Chebyshev polynomial must only grow logarithmically with the hidden dimension.

<!-- chunk {"id": "body-0026", "role": "body", "section": "Main Results", "weight": 1.0} -->

In this section we formally state our main algorithms and theorems. We show that the Universal Sequence Preconditioning method provides significantly improved regret bounds for learning linear dynamical systems than previously known when used in conjunction with two distinct methods. The first method is simple convex regression, and the second is spectral filtering. Both algorithms allow for learning in the case of marginally stable linear dynamical systems and allow for certain asymmetric transition matrices of arbitrary high hidden dimension. The regret bounds are free of the hidden dimension (up to logarithmic factors) -- which significantly extends the state of the art.

<!-- chunk {"id": "body-0027", "role": "body", "section": "Universal Sequence Preconditioning Applied to Regression", "weight": 1.0} -->

Algorithm is an instantiation of Algorithm for the method of convex regression. We set the preconditioning coefficients to be the coefficients of the $n$-th degree (monic) Chebyshev polynomial.

<!-- chunk {"id": "body-0028", "role": "body", "section": "Universal Sequence Preconditioning Applied to Regression", "weight": 1.0} -->

Algorithm 2 Universal Sequence Preconditioning for Regression

<!-- chunk {"id": "body-0029", "role": "body", "section": "Universal Sequence Preconditioning Applied to Regression", "weight": 1.0} -->

Theorem 2.1 shows that vanishing loss compared to the optimal ground-truth predictor, at a rate that is independent of the hidden dimension of the system.

<!-- chunk {"id": "body-0030", "role": "body", "section": "Universal Sequence Preconditioning Applied to Spectral Filtering", "weight": 1.0} -->

Our second main result is the application of Universal Sequence Preconditioning to the spectral filtering algorithm Hazan et al.. Our results are more general and apply to any choice of polynomial, not just Chebyshev. In addition to applying USP to spectral filtering, we also propose a novel spectral filtering basis. Both changes to the vanilla spectral filtering algorithm are necessary to extend its sublinear regret bounds to the case of underlying systems with asymmetric hidden transition matrices. First we define the spectral domain

<!-- chunk {"id": "body-0031", "role": "body", "section": "Universal Sequence Preconditioning Applied to Spectral Filtering", "weight": 1.0} -->

where $\overline{\alpha} \in {\mathbb{C}}$ denotes the complex conjugate. The novel spectral filters are the eigenvectors of $\mathbf{Z}_{T - n - 1}$, which we denote as $\phi_{1},\ldots,\phi_{T - n - 1}$. Note that in the standard spectral filtering literature, the spectral filtering matrix is an integral over the real line and does not involve the complex conjugate. Our new matrix has an entirely different structure and although it looks quite similar, it surprisingly upends the proof techniques to ensure exponential spectral decay, a critical property for the method. Future work examines this matrix more thoroughly, but in this paper we simply provide a standard bound on its eigenvalues.

<!-- chunk {"id": "body-0032", "role": "body", "section": "Universal Sequence Preconditioning Applied to Spectral Filtering", "weight": 1.0} -->

1: Input: initial Q1: n1, M1: k1, horizon T, convex constraints

<!-- chunk {"id": "body-0033", "role": "body", "section": "Regression: Proof of Theorem 2.1", "weight": 1.0} -->

In the case of regression, the domain is chosen so that $\aleph_{2}$ may be learned and the proof proceeds by bounding the diameter of such a domain and its corresponding maximum gradient norm to get regret $Cn^{2}\sqrt{d_{\text{out}}}{\| c\|}_{1}\sqrt{T}$ for a universal constant $C > 0$ which depends on the norms of matrices $\mathbf{B}$ and $\mathbf{C}$ from the underlying system. Then $\aleph_{3}$ is treated as an un-learnable error term. Let $\lambda{(\mathbf{A})}$ denote the set of eigenvalues of $\mathbf{A}$. By the simple magnitude bound of

<!-- chunk {"id": "body-0034", "role": "body", "section": "Regression: Proof of Theorem 2.1", "weight": 1.0} -->

the error of ignoring this term can be very small if $\max_{\lambda{(\mathbf{A})}}{|{p_{n}{({\lambda{(\mathbf{A})}})}}|}$ is small. In the proof of Theorem 2.1 in Appendix D we show that the regret for a generic polynomial $p_{n}^{c}$ defined by coefficients $c_{0:n}$ is

<!-- chunk {"id": "body-0035", "role": "body", "section": "Regression: Proof of Theorem 2.1", "weight": 1.0} -->

where $\mathcal{D}$ is the region where $\mathbf{A}$ is allowed to have eigenvalues (see Theorem D.1. ‣ Appendix D Proof of Convolutional Preconditioned Regression Performance Theorem 2.1 ‣ Universal Sequence Preconditioning")). Therefore, to get sublinear regret, we must choose a polynomial which has bounded $\ell_{1}$ norm of its coefficients, while also exhibits very small infinity norm on the domain of $\mathbf{A}$'s eigenvalues.

<!-- chunk {"id": "body-0036", "role": "body", "section": "Spectral Filtering: Proof of Theorem 2.2", "weight": 1.0} -->

In the case of spectral filtering, the domain is chosen so that both $\aleph_{2}$ and $\aleph_{3}$ may be learned. Because spectral filtering learns $\aleph_{3}$, it is able to accumulate less error and hence achieves a better regret bound of $O{(T^{- {3/13}})}$ as compared to regression's $O{(T^{- {2/13}})}$. At a high level, the proof proceeds by exploiting the fact that $p_{n}{(\mathbf{A})}$ shrinks the size of the learnable domain. However this is not enough, in order to extend the result to systems where $\mathbf{A}$ may have complex eigenvalues, the spectral filters must be eigenvalues of a new matrix, defined in Eq., whose domain of integration includes the possibly complex eigenvalues of $\mathbf{A}$.

<!-- chunk {"id": "body-0037", "role": "body", "section": "Spectral Filtering: Proof of Theorem 2.2", "weight": 1.0} -->

To get the dimension-independent regret bounds enjoyed by spectral filtering in this new setting where complex eigenvalues may occur, the exponential decay of $\mathbf{Z}_{T}$ from Eq. must be established. This is nontrivial and requires several novel techniques inspired by Beckermann and Townsend. The details are in Appendix E.3.1. Theorem 2.2 gives the main guarantee for the spectral filtering algorithm, which states that Algorithm instantiated with some choice of polynomial $p_{n}^{c}{( \cdot )}$ achieves regret

<!-- chunk {"id": "body-0038", "role": "body", "section": "Spectral Filtering: Proof of Theorem 2.2", "weight": 1.0} -->

Both this theorem, as well as our new guarantee for convex regression, leads us to the following question: Is there a universal choice of polynomial $p_{n}{(x)}$, where $n$ is independent of hidden dimension, which guarantees sublinear regret?\

<!-- chunk {"id": "body-0039", "role": "body", "section": "Using the Chebyshev Polynomial over the Complex Plane", "weight": 1.0} -->

For the real line, the answer to this question is known to be positive using the Chebyshev polynomials of the first kind. In general, the $n^{\text{th}}$ (monic) Chebyshev polynomial $M_{n}{(x)}$ satisfies ${\max_{x \in {\lbrack{- 1},1\rbrack}}{|{M_{n}{(x)}}|}} \leq 2^{- {({n - 1})}}$. However, we are interested in a more general question over the complex plane. Since we care about linear dynamical systems that evolve according to a general asymetric matrix, we need to extending our analysis to ${\mathbb{C}}_{\beta}$. This is a nontrivial extension since, in general, functions that are bounded on the real line can grow exponentially on the complex plane.

<!-- chunk {"id": "body-0040", "role": "body", "section": "Using the Chebyshev Polynomial over the Complex Plane", "weight": 1.0} -->

Indeed, ${2^{n - 1}M_{n}{(x)}} = {\cos{({n{\arccos{(x)}}})}}$ and while $\cos{(x)}$ is bounded within $\lbrack{- 1},1\rbrack$ for any $x \in \mathcal{R}$, over the complex numbers we have ${{\cos{(z)}} = {\frac{1}{2}{({e^{iz} + e^{- {iz}}})}}},$ which is unbounded. Thus, we analyze the Chebyshev polynomial on the complex plane and provide the following bound.

<!-- chunk {"id": "body-0041", "role": "body", "section": "Experimental Evaluation", "weight": 1.0} -->

We empirically validate that convolutional preconditioning with Chebyshev or Legendre coefficients yields significant online regret improvements across various learning algorithms and data types. Below we summarize our data generation, algorithm variants, hyperparameter tuning, and evaluation metrics.

<!-- chunk {"id": "body-0042", "role": "body", "section": "Synthetic Data Generation", "weight": 1.0} -->

We generate $N = 200$ sequences of length $T = 2000$ via three mechanisms: (i) a noisy linear dynamical system, (ii) a noisy nonlinear dynamical system, and (iii) a noisy deep RNN. Inputs $\mathbf{u}_{1:T} \sim {\mathcal{N}{(0,I)}}$.

<!-- chunk {"id": "body-0043", "role": "body", "section": "Deep RNN", "weight": 1.0} -->

We randomly initialize a sparse 10-layer stack of LSTMs with hidden dimension $100$ and ReLU nonlinear activations. Given $\mathbf{u}_{1:T}$ we use this network to generate $\mathbf{y}_{1:T}$.

<!-- chunk {"id": "body-0044", "role": "body", "section": "Algorithms and Preconditioning Variants", "weight": 1.0} -->

We evaluate the following methods: Regression, Spectral Filtering, DNN Predictor: $n$-layer LSTM with dims $\lbrack d_{1},\ldots,d_{n}\rbrack$, ReLU.

<!-- chunk {"id": "body-0045", "role": "body", "section": "Algorithms and Preconditioning Variants", "weight": 1.0} -->

*Chebyshev:* $\mathbf{c}_{0:n}$ are the coefficients for the $n$th-Chebyshev polynomial. Note that when $n = 2$ we have $\mathbf{c}_{0} = 1$ and $\mathbf{c}_{1} = {- 1}$ and therefore this is the method of *differencing* discussed in the introduction.

<!-- chunk {"id": "body-0046", "role": "body", "section": "Algorithms and Preconditioning Variants", "weight": 1.0} -->

*Legendre:* $\mathbf{c}_{0:n}$ are the coefficients for the $n$th-Legendre polynomial

<!-- chunk {"id": "body-0047", "role": "body", "section": "Algorithms and Preconditioning Variants", "weight": 1.0} -->

*Learned:* $\mathbf{c}_{0:n}$ is a parameter learned jointly with the model parameters

<!-- chunk {"id": "body-0048", "role": "body", "section": "Algorithms and Preconditioning Variants", "weight": 1.0} -->

We test polynomial degrees $n \in {\{ 2,5,10,20\}}$. This choice of degrees shows a rough picture of the impact of $n$.

<!-- chunk {"id": "body-0049", "role": "body", "section": "Hyperparameter Tuning", "weight": 1.0} -->

To ensure fair comparison, for each algorithm and conditioning $\mathbf{c}$ variant we perform a grid search over learning rates $\eta \in {\{ 10^{- 3},10^{- 2},10^{- 1}\}}$, selecting the one minimizing average regret across the $N$ sequences. In the case of the learned coefficients, we sweep over the 9 pairs of learning rates ${(\eta_{\text{model}},\eta_{\text{coefficients}})} \in {{\{ 10^{- 3},10^{- 2},10^{- 1}\}} \times {\{ 10^{- 3},10^{- 2},10^{- 1}\}}}$.

<!-- chunk {"id": "body-0050", "role": "body", "section": "Results", "weight": 1.0} -->

Tables -- report the mean $\pm$ std of the absolute error over the final 200 predictions, averaged across 200 runs. In the linear and nonlinear cases we train a 2-layer DNN (dims $$); for RNN-generated data we match the 10-layer (100-dim) generator.

<!-- chunk {"id": "body-0051", "role": "body", "section": "Results", "weight": 1.0} -->

Preconditioning drastically reduces baseline errors for all algorithms and data types.

<!-- chunk {"id": "body-0052", "role": "body", "section": "Results", "weight": 1.0} -->

Chebyshev and Legendre yield nearly identical gains.

<!-- chunk {"id": "body-0053", "role": "body", "section": "Results", "weight": 1.0} -->

For Chebyshev and Legendre, once the degree is higher than $5 - 10$ the performance degrades since ${\|\mathbf{c}\|}_{1}$ gets very large (see our Lemma 3.2 which shows that these coefficients grow exponentially fast).

<!-- chunk {"id": "body-0054", "role": "body", "section": "Results", "weight": 1.0} -->

Improvements decay as the complex threshold $\tau_{thresh}$ increases, consistent with our theoretical results which must bound ${Im}{(z_{j})}$.

<!-- chunk {"id": "body-0055", "role": "body", "section": "Results", "weight": 1.0} -->

Learned coefficients excel with regression and spectral filtering but destabilize the DNN on nonlinear and RNN‐generated data.

<!-- chunk {"id": "body-0056", "role": "body", "section": "ETTh1 Dataset", "weight": 1.0} -->

To evaluate whether our proposed preconditioning approach generalizes to real-world time series, we conduct experiments on the well-established ETTh1 dataset from the Electricity Transformer Temperature (ETT) benchmark Zhou et al.. The ETTh1 dataset consists of continuous hourly measurements of load and oil temperature collected from electricity transformers and has been used in several recent works Zhou et al.; Wu et al.; Nie et al.; Gu et al.; Gupta and et al.; Zeng et al.; Nguyen et al.. We study the effect of preconditioning on a $10$-layer LSTM with hidden dimension $100$ per layer using the Adam optimizer. We set the horizon to be $T = 5000$ and we sweep over a broader range of learning rates $\eta \in {\{ 10^{- j}\}}_{j = {0,1,2,3,4,5}}$. As before we consider (i) no preconditioning (baseline), (ii) fixed Chebyshev coefficients, (iii) fixed Legendre coefficients, and (iv) coefficients learned jointly with model parameters.

<!-- chunk {"id": "body-0057", "role": "body", "section": "ETTh1 Dataset", "weight": 1.0} -->

As seen in Figure, preconditioning with Chebyshev and Legendre for degree $5$ the best performance after only the first $1000$ iterations, while the performance of jointly learning the coefficients is worse at this stage. The performance of all three preconditioning methods are roughly on par with each other by $2500$ iterations and by the full horizon $T = 5000$, jointly learning the coefficients results in the best average prediction error.

<!-- chunk {"id": "body-0058", "role": "body", "section": "Discussion", "weight": 1.5} -->

There are many settings in machine learning where universal, rather than learned, rules have proven very efficient. For example, physical laws of motion can be learned directly from observation data. However, Newton's laws of motion succinctly crystallize very general phenomenon, and have proven very useful for large scale physics simulation engines. Similarly, in the theory of mathematical optimization, adaptive gradient methods have revolutionized deep learning. Their derivation as a consequence of regularization in online regret minimization is particularly simple Duchi et al., and thousands of research papers have not dramatically improved the initial basic ideas. These optimizers are, at the very least, a great way to initialize learned optimizers Wichrowska et al..

<!-- chunk {"id": "body-0059", "role": "body", "section": "Discussion", "weight": 1.5} -->

By analogy, our thesis in this paper is that universal preconditioning based on the solid theory of dynamical systems can be applicable to many domains or, at the very least, an initialization for other learning methods.
